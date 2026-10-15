#!/usr/bin/env python3
"""开源周刊确定性采集：七天 Trending 聚合、大牛新 Star 与历史报告回链。

用法：python3 src/scripts/collect_weekly_facts.py [YYYY-MM-DD] [--type ecosystem] [--out PATH]
日期为七天窗口终点（UTC），默认今天。只在 stdout 打印 facts JSON 路径。
缺少本周快照时返回空榜并记录警告，不使用过期数据。历史报告仅用于旧文重读。
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))


DATA = ROOT / "src" / "data"
TRENDING_SNAPSHOTS = DATA / "trending_snapshots.jsonl"
STARRED_JSON = DATA / "starred.json"
STARRED_SEED = DATA / "starred_seed.json"
REPORTS_JSON = DATA / "reports.json"
ENTITIES_YAML = DATA / "opensource-weekly" / "entities.yaml"
SCORING_YAML = DATA / "opensource-weekly" / "scoring.yaml"
DIGESTS_JSONL = DATA / "weekly_digests.jsonl"
CACHE_DIR = DATA / "opensource-weekly" / "cache"

WARNINGS: list[str] = []


def warn(msg: str) -> None:
    WARNINGS.append(msg)
    print(f"[collect_weekly_facts] warn: {msg}", file=sys.stderr)


def _load_json(path: Path, default):
    try:
        with path.open(encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        warn(f"缺失数据源 {path.relative_to(ROOT)}，降级为空")
        return default
    except (json.JSONDecodeError, OSError) as e:
        warn(f"读取 {path.relative_to(ROOT)} 失败: {e}")
        return default


def _load_yaml(path: Path, default):
    try:
        import yaml
        with path.open(encoding="utf-8") as f:
            return yaml.safe_load(f) or default
    except FileNotFoundError:
        warn(f"缺失配置 {path.relative_to(ROOT)}，用默认值")
        return default
    except Exception as e:  # noqa: BLE001  — 配置坏不致命
        warn(f"读取 {path.relative_to(ROOT)} 失败: {e}")
        return default


def norm_url(url: str) -> str:
    return (url or "").strip().rstrip("/").lower()


# ----------------------------------------------------------------- AI 相关性
def build_ai_matcher(entities: dict):
    h = (entities or {}).get("heuristics", {}) or {}
    keywords = [k.lower() for k in (h.get("keywords") or [])]
    owners = {o.lower() for o in (h.get("owners") or [])}
    ai_langs = set(h.get("languages") or [])

    def is_ai(name: str, description: str, language: str | None = None) -> bool:
        owner = (name or "").split("/")[0].strip().lower()
        if owner and owner in owners:
            return True
        text = f"{name} {description or ''}".lower()
        for kw in keywords:
            if kw and kw in text:
                return True
        return False

    return is_ai, ai_langs


# ----------------------------------------------------------------- 报告回链索引
def build_report_url_index() -> dict[str, str]:
    """reports.json originalUrl(归一) → slug。Python 版 data.ts:getAnalyzedUrlIndex。"""
    reports = _load_json(REPORTS_JSON, [])
    idx: dict[str, str] = {}
    for r in reports if isinstance(reports, list) else []:
        ou = r.get("originalUrl")
        slug = r.get("slug")
        if ou and slug:
            idx[norm_url(ou)] = slug
    return idx


# ----------------------------------------------------------------- 本周 Trending 聚合
from weekly_period import period


def load_rising_repos(date: str, idx: dict[str, str], is_ai) -> tuple[list[dict], dict]:
    """聚合最近七天 daily 榜；每仓库一条，以实际上榜天数和最佳排名排序。"""
    window = period(date)
    if not TRENDING_SNAPSHOTS.exists():
        warn("缺失 trending_snapshots.jsonl，rising_repos 为空")
        return [], {}
    current, previous = {}, {}
    previous_start = (datetime.strptime(window["since"], "%Y-%m-%d") - timedelta(days=6)).strftime("%Y-%m-%d")
    for line in TRENDING_SNAPSHOTS.read_text(encoding="utf-8").splitlines():
        try:
            r = json.loads(line)
        except json.JSONDecodeError:
            continue
        key = r.get("period_key", "")
        if r.get("period_type") != "daily" or not key:
            continue
        if not r.get("name") or not r.get("url"):
            continue
        url = norm_url(r["url"])
        rank = r.get("rank")
        if previous_start <= key <= window["since"]:
            if isinstance(rank, int):
                previous[url] = min(previous.get(url, rank), rank)
        elif window["window_start"] <= key <= date:
            entry = current.setdefault(url, {"record": r, "days": set(), "best_rank": None, "last_seen": key})
            entry["days"].add(key)
            if key >= entry["last_seen"]:
                entry.update(record=r, last_seen=key)
            if isinstance(rank, int):
                entry["best_rank"] = min(entry["best_rank"] or rank, rank)
    out = []
    for url, entry in current.items():
        r = entry["record"]
        rank = entry["best_rank"]
        prior = previous.get(url)
        out.append({
            **{k: r.get(k) for k in ("name", "url", "language", "description")},
            "stars": int(r.get("stars") or 0), "forks": int(r.get("forks") or 0),
            "rank": rank, "best_rank": rank,
            "rank_delta": prior - rank if prior is not None and rank is not None else None,
            "is_new": url not in previous,
            "trending_days": len(entry["days"]), "last_seen": entry["last_seen"],
            "ai": is_ai(r["name"], r.get("description"), r.get("language")),
            "report_slug": idx.get(url),
        })
    out.sort(key=lambda r: (-r["trending_days"], r["rank"] or 999, -r["stars"]))
    if not out:
        warn(f"{window['window_start']} 至 {date} 无 Trending 快照；不使用过期榜单冒充本周数据")
    return out, {"period_key": date, "total": len(out), "non_ai": sum(not r["ai"] for r in out)}


# ----------------------------------------------------------------- pro_stars（大牛新 star）
def load_new_pro_stars(since: str, date: str, idx: dict[str, str], is_ai) -> list[dict]:
    """读 starred.json（缺则 starred_seed.json），取 since < starredAt日期 <= date 的项，按 url 聚合。"""
    data = _load_json(STARRED_JSON, None)
    if not data:
        data = _load_json(STARRED_SEED, {"users": []})
    agg: dict[str, dict] = {}
    seen_pairs: set[tuple[str, str]] = set()
    for user in (data or {}).get("users", []):
        login = (user.get("login") or "").strip()
        uname = (user.get("name") or login).strip()
        for item in user.get("items", []):
            starred_at = (item.get("starredAt") or "").strip()
            if not starred_at or not (since < starred_at[:10] <= date):
                continue
            url = (item.get("url") or "").strip().rstrip("/")
            name = (item.get("name") or "").strip()
            if not url or "/" not in name:
                continue
            nu = norm_url(url)
            entry = agg.setdefault(nu, {
                "name": name,
                "url": url,
                "stars": 0,
                "star_users": 0,
                "starred_by": [],
                "latest_starred_at": starred_at,
                "description": item.get("description"),
                "report_slug": idx.get(nu),
                "ai": is_ai(name, item.get("description"), None),
            })
            entry["stars"] = max(entry["stars"], int(item.get("stars") or 0))
            entry["latest_starred_at"] = max(entry["latest_starred_at"], starred_at)
            if (login, nu) not in seen_pairs:
                seen_pairs.add((login, nu))
                entry["star_users"] += 1
                entry["starred_by"].append({"login": login, "name": uname})
    rows = list(agg.values())
    # 多人 star 优先；其次 star 数；其次最近
    rows.sort(key=lambda x: (x["star_users"], x["stars"], x["latest_starred_at"]), reverse=True)
    return rows


# ----------------------------------------------------------------- resurface（旧文重读）
def pick_resurface_reports(rising: list[dict], exclude_urls: set[str], is_ai, n: int = 4) -> list[dict]:
    """从已有报告里召回与本周 AI 主题相关、可重读的历史篇。

    优先级：AI 相关 > 语言命中本周 AI rising 主流语言 > star 高。
    用 is_ai(报告标题+摘要+owner) 过滤掉非 AI 报告（避免 public-apis 这类混进 开源周刊）。"""
    reports = _load_json(REPORTS_JSON, [])
    if not isinstance(reports, list):
        return []
    langs = [r.get("language") for r in rising if r.get("ai") and r.get("language")]
    top_langs = {l for l in langs}
    cand = []
    for r in reports:
        ou = norm_url(r.get("originalUrl") or "")
        if not ou or ou in exclude_urls:
            continue
        # 用 owner/repo + 标题 + 摘要 判 AI 相关
        owner_repo = ""
        if r.get("originalUrl"):
            parts = [p for p in (r["originalUrl"].split("github.com/")[-1]).split("/") if p]
            owner_repo = "/".join(parts[:2])
        ai_hit = is_ai(owner_repo, f"{r.get('title') or ''} {r.get('summary') or ''}", r.get("language"))
        lang_hit = (r.get("language") in top_langs) if top_langs else False
        cand.append((ai_hit, lang_hit, int(r.get("stars") or 0), r))
    # AI 相关优先 → 语言命中 → star
    cand = [c for c in cand if c[0]] or cand  # 有 AI 报告就只用 AI 的；否则退回全部
    cand.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True)
    out = []
    for _, _, _, r in cand[:n]:
        out.append({
            "slug": r.get("slug"),
            "title": r.get("title"),
            "summary": r.get("summary"),
            "language": r.get("language"),
            "stars": r.get("stars"),
            "originalUrl": r.get("originalUrl"),
        })
    return out


# ----------------------------------------------------------------- cache 提示
def load_cache_seen_keys(digest_type: str, date: str) -> list[str]:
    cache = _load_json(CACHE_DIR / f"{digest_type}.json", {"entries": []})
    cutoff = (datetime.strptime(date, "%Y-%m-%d") - timedelta(days=30)).strftime("%Y-%m-%d")
    return [e["key"] for e in cache.get("entries", [])
            if e.get("key") and cutoff <= e.get("date_seen", "") <= date]


# ----------------------------------------------------------------- 组装
def build_facts(date: str, digest_type: str) -> tuple[dict, dict]:
    entities = _load_yaml(ENTITIES_YAML, {})
    scoring = _load_yaml(SCORING_YAML, {})
    is_ai, _ai_langs = build_ai_matcher(entities)
    idx = build_report_url_index()
    window = period(date)
    since = window["since"]

    rising, rising_meta = load_rising_repos(date, idx, is_ai)
    pro_stars = load_new_pro_stars(since, date, idx, is_ai)
    heating = [r for r in rising if r["trending_days"] >= 2][:30]
    exclude = {norm_url(x["url"]) for x in rising} | {norm_url(x["url"]) for x in pro_stars}
    resurface = pick_resurface_reports(rising, exclude, is_ai)

    facts = {
        "schema_version": 2,
        **window,
        "type": digest_type,
        "date": date,
        "since": since,
        "after_date": since,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "config": {
            "concurrency_cap": int((scoring or {}).get("concurrency_cap", 10)),
            "min_non_seed_ratio": float((scoring or {}).get("min_non_seed_ratio", 0.2)),
        },
        "trending_period_key": rising_meta.get("period_key"),
        "stats": {
            "rising_total": rising_meta.get("total", 0),
            "rising_ai": sum(1 for x in rising if x["ai"]),
            "rising_non_ai": rising_meta.get("non_ai", 0),
            "pro_stars": len(pro_stars),
            "pro_stars_multi": sum(1 for x in pro_stars if x["star_users"] >= 2),
            "heating": len(heating),
            "resurface": len(resurface),
            "report_index": len(idx),
        },
        "rising_repos": rising,
        "pro_stars": pro_stars,
        "heating_up": heating,
        "resurface": resurface,
        "cache_seen_keys": load_cache_seen_keys(digest_type, date),
        "_warnings": WARNINGS,
    }
    return facts, idx


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        description="开源周刊确定性数据采集（开源信号层）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument("date", nargs="?", help="周刊日期 YYYY-MM-DD（缺省今天 UTC）")
    ap.add_argument("--type", choices=["ecosystem"], default="ecosystem")
    ap.add_argument("--out", type=Path, help="JSON 落地路径，缺省 tmp/weekly-facts-<type>-<date>.json")
    args = ap.parse_args(argv)

    date = args.date or datetime.now(timezone.utc).strftime("%Y-%m-%d")
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print(f"ERR: 非法日期 {date}（应为 YYYY-MM-DD）", file=sys.stderr)
        return 1

    facts, idx = build_facts(date, args.type)

    out_path = args.out or (ROOT / "tmp" / f"weekly-facts-{args.type}-{date}.json")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(facts, f, ensure_ascii=False, indent=2)

    # 报告回链全表单独落文件（供篇B 外部条目反查，不塞进主对话）
    idx_path = ROOT / "tmp" / f"weekly-report-index-{date}.json"
    with idx_path.open("w", encoding="utf-8") as f:
        json.dump(idx, f, ensure_ascii=False, indent=2)
    facts["report_url_index_path"] = str(idx_path.relative_to(ROOT))
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(facts, f, ensure_ascii=False, indent=2)

    st = facts["stats"]
    print(
        f"[collect_weekly_facts] type={args.type} date={date} since={facts['since']} | "
        f"rising {st['rising_ai']}/{st['rising_total']} AI | pro_stars {st['pro_stars']} "
        f"(多人 {st['pro_stars_multi']}) | heating {st['heating']} | resurface {st['resurface']} | "
        f"warnings {len(WARNINGS)}",
        file=sys.stderr,
    )
    print(out_path)  # stdout 只打印路径（同 collect_repo_facts.py）
    return 0


if __name__ == "__main__":
    sys.exit(main())
