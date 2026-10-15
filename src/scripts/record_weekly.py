#!/usr/bin/env python3
"""Append 一条周刊记录到 src/data/weekly_digests.jsonl（镜像 record_publish.py）。

由 weekly-digest.yml 调用：每次 开源周刊产出后记录索引（站点读取 + 选 since 窗口 + 去重）。
本项目独立维护索引，按 ISO 周防重复。

示例：
    python3 src/scripts/record_weekly.py \\
        --type ecosystem --date 2026-06-07 --slug 2026-06-07 \\
        --title "开源周刊 | ..." --summary "..." \\
        --sections '{"rising":6,"pro_stars":4,"heating":3,"resurface":3}' \\
        --featured-urls "https://github.com/a/b,https://github.com/c/d" \\
        --ci-run-id "$GITHUB_RUN_ID"

jsonl 是 append-only；幂等键 = (type, ISO week)，重复调用跳过。
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from weekly_period import period

ROOT = Path(__file__).resolve().parents[2]
DIGESTS_JSONL = ROOT / "src" / "data" / "weekly_digests.jsonl"

VALID_TYPES = {"ecosystem"}


def _already_recorded(out: Path, digest_type: str, date: str) -> bool:
    """jsonl 里是否已有同 (type, ISO week) 记录（幂等）。"""
    if not out.exists():
        return False
    for line in out.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            continue
        try:
            if (rec.get("type") == digest_type and rec.get("date")
                    and period(rec["date"])["week"] == period(date)["week"]):
                return True
        except (ValueError, TypeError):
            continue
    return False


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--type", required=True, choices=sorted(VALID_TYPES))
    p.add_argument("--date", required=True, help="周刊日期 YYYY-MM-DD")
    p.add_argument("--slug", default="", help="周刊 slug（通常= date）")
    p.add_argument("--title", default="", help="周刊标题（进站点列表/公众号）")
    p.add_argument("--summary", default=None, help="一句话提要")
    p.add_argument("--sections", default=None, help="各板块计数 JSON，如 '{\"rising\":6}'")
    p.add_argument("--featured-urls", default=None, help="头条仓库/条目 URL，逗号分隔")
    p.add_argument("--ci-run-id", default=None, help="GitHub Actions runId")
    p.add_argument("--out", type=Path, default=DIGESTS_JSONL)
    p.add_argument("--check", action="store_true", help="只打印本周是否已有记录：true/false")
    args = p.parse_args(argv)

    try:
        datetime.strptime(args.date, "%Y-%m-%d")
    except ValueError:
        print(f"❌ 非法日期 {args.date}（应为 YYYY-MM-DD）", file=sys.stderr)
        return 1

    if args.check:
        print("true" if _already_recorded(args.out, args.type, args.date) else "false")
        return 0
    if not args.slug or not args.title:
        p.error("记录周刊需要 --slug 和 --title")

    if _already_recorded(args.out, args.type, args.date):
        print(f"⏭ 跳过：{args.type}/{args.date} 已有记录（幂等）")
        return 0

    sections = None
    if args.sections:
        try:
            sections = json.loads(args.sections)
        except json.JSONDecodeError:
            print(f"⚠ --sections 不是合法 JSON，置空：{args.sections}", file=sys.stderr)

    featured = [u.strip() for u in (args.featured_urls or "").split(",") if u.strip()]

    record = {
        **period(args.date),
        "cadence": "weekly",
        "recorded_at": datetime.now(timezone.utc).isoformat(),
        "type": args.type,
        "date": args.date,
        "slug": args.slug,
        "title": args.title,
        "summary": args.summary,
        "sections": sections,
        "featured_urls": featured,
        "ci_run_id": args.ci_run_id,
    }

    args.out.parent.mkdir(parents=True, exist_ok=True)
    if args.out.exists() and args.out.stat().st_size > 0:
        with args.out.open("rb") as f:
            f.seek(-1, 2)
            if f.read(1) != b"\n":
                with args.out.open("a", encoding="utf-8") as af:
                    af.write("\n")
    with args.out.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")

    print(f"✅ append → {args.out}: type={args.type} date={args.date} slug={args.slug}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
