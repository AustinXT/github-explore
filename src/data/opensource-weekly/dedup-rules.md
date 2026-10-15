# 去重规则

三层去重 + 跨「内部信号 ↔ 外部新闻」合并 + 30 天 cache 滚动。
L1 由 `src/scripts/dedup_weekly.py` 确定性完成；L2/L3 由主对话 LLM 完成。

## L1 — URL 精确去重（确定性，dedup_weekly.py）

URL 归一后比较（`dedup_weekly.normalize_url()`）：
- 统一 https、去 `utm_*`/`?ref=`/`#fragment`、去尾斜杠、域名小写。
- `github.com/{owner}/{repo}` → 取规范主键 `github.com/owner/repo`（剥 `/tree`、`/blob` 等子路径）。
- `arxiv.org/abs|pdf/{id}` → 归一为 `arxiv:{id}`（abs 与 pdf 视为同一条）。
- `huggingface.co/{org}/{model}` → 归一为 `hf:{org}/{model}`。

本周池内按归一 key 去重；并与 `cache/<type>.json`（近 30 天）比对，**已推送过的剔除**。

## L2 — 标题语义去重（LLM）

同一事件被多家转载、换标题搬运、翻译 → 按归一标题聚类，每组保留一条。

## L3 — 内容语义去重（LLM）

不同措辞描述同一发布（如 arxiv 原文 vs 媒体解读 vs 公众号翻译）→ 按摘要/要点语义合并。

## 跨「内部信号 ↔ 外部新闻」合并

若内部 trending/starred 的仓库与某条外部「发布/release」新闻指向同一仓库：
**合并为一条，以外部新闻为主体**，内部信号作为增强徽标挂上（如「本站 Trending #N / 被 M 位大牛 Star」），
不重复成两条。若外部无对应新闻，则内部信号单独成「开源信号」板块条目。

## 保留优先级（同组重复时留哪条）

1. 论文：arXiv/OpenReview 原文 > 二手解读。
2. 开源：GitHub 仓库 > 介绍博文。
3. 新闻：官方公告 > 媒体转载。
4. 同级时：评分高者 > 独立源多者 > `event_date` 早者。
5. 内部信号默认以「增强」挂靠，不单独成条（除非外部无对应新闻）。

## cache 规约（30 天滚动）

`src/data/opensource-weekly/cache/<type>.json`（git 跟踪 SoR，per-type 互不影响）：

```json
{ "meta": { "last_run": "2026-06-06", "window_days": 30 },
  "entries": [ { "key": "github.com/owner/repo", "canonical_url": "https://...",
                 "event_date": "2026-06-05", "date_seen": "2026-06-06" } ] }
```

- 运行开始：`dedup_weekly.py --prune` 剔除 `date_seen` 超 `window_days` 的条目。
- 报告定稿后：`dedup_weekly.py --commit <entries.json>` 把本周采纳条目追加进 cache，供下期去重。
