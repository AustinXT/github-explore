# Github 仓库探索技能

一个用于探索 GitHub 仓库的 Agent Skill，能够解读代码仓库的内容，分析出有价值的信息，并发布到微信公众号。

## 本地用法

```bash
# 分析单个仓库
/repo-miner https://github.com/owner/repo

# 批量并发分析
./batch_analyze.sh src/analysis_report/repos.md 1 0 8

# 发布报告到公众号草稿箱
/md2wechat src/analysis_report/{username}_{repo}.md
```

## 站点域名与 HTTPS

目标地址：<https://nightvoyager.top/github-explore/>，由 GitHub Pages 托管。
仓库为 `AustinXT/github-explore`，项目路径与仓库名一致；Actions 直接上传 `site/dist`。
站点导航、全文搜索、canonical、RSS、索引推送和公众号回链均使用新地址。

根域名 `nightvoyager.top` 配置在 `AustinXT/AustinXT.github.io` 的 Pages 设置中，
本项目继承该域名，项目的 Custom domain 留空。不要把路径 `/github-explore` 填进域名或 DNS。
在 DNS 中为 `@` 添加四条 A 记录：`185.199.108.153`、`185.199.109.153`、
`185.199.110.153`、`185.199.111.153`。DNS 校验通过、GitHub 签发证书后，
启用 Enforce HTTPS；保留 GitHub 域名所有权验证的 TXT 记录。

Actions Variables 如已设置 `SITE_URL` / `PUBLIC_BASE_PATH`，应分别更新为
`https://nightvoyager.top` / `/github-explore`；未设置时使用上述默认值。

## GitHub Actions 自动化（无人值守）

整套流水线 `.github/workflows/auto-analyze.yml`，三种触发方式：

| 方式 | 适用场景 |
|---|---|
| `schedule` cron | 每小时触发 + 自动节流：仅在「有够分的新选题且最近 24h 未达产量上限」时才出 1 篇，否则空转跳过（阈值 `MIN_SCORE`/`DAILY_CAP` 见 `select_next_repo.py`） |
| `workflow_dispatch` | Actions 页面手动触发，可选输入 `repo_url` / `skip_publish` / `force_backend` |
| `issue_comment` | 在仓库新建 issue 后评论 `/analyze <github-url>` 即可触发（仅授权用户） |

### 准备 Secrets

去仓库 Settings → Secrets and variables → Actions 添加：

| Secret | 必需 | 说明 |
|---|---|---|
| `MINIMAX_API_KEY` | 是 | [Minimax token plan](https://platform.minimaxi.com/docs/token-plan/claude-code) 申请，CI 里会被映射为 `ANTHROPIC_AUTH_TOKEN` |
| `WECHAT_APPID` | 是 | 微信公众号 AppID |
| `WECHAT_APPSECRET` | 是 | 微信公众号 AppSecret |
| `ANTHROPIC_API_KEY` | 否 | 仅应急降级用，正常运行不要配。配上后手动 dispatch 选 `force_backend=anthropic` 才生效 |

> 公众号后台「IP 白名单」必须清空或加 GitHub Actions 出口 IP；动态 IP 几乎只能选清空。

### 推理后端策略

默认只走 **Minimax 的 Anthropic 兼容端点**，模型固定为 **MiniMax-M3**，无 fallback：

```
claude -p "/repo-miner …" --dangerously-skip-permissions
   ANTHROPIC_BASE_URL   = https://api.minimaxi.com/anthropic   ← 国内版，写死在 run_skill.sh
   ANTHROPIC_AUTH_TOKEN = $MINIMAX_API_KEY                     ← Minimax 用 AUTH_TOKEN 而非 API_KEY
   ANTHROPIC_API_KEY    = (清空，避免冲突)
   ANTHROPIC_MODEL      = MiniMax-M3
```

Sonnet / Opus / Haiku 别名和小型快速模型也统一映射到 `MiniMax-M3`；运行日志会打印实际配置的模型名称。所有调用 `run_skill.sh` 的 Workflow 共用此设置。

同后端失败时自动重试 1 次（默认值，`--retries N` 可调）。**用国际版** `api.minimax.io/anthropic` 时把 `src/scripts/run_skill.sh` 顶部 `MINIMAX_ENDPOINT` 改掉，或临时设环境变量 `MINIMAX_BASE_URL_OVERRIDE`。

**应急降级**：万一 Minimax 在某个 skill 行为上不兼容（例如 subagent / tool use 协议），可手动 dispatch 时选 `force_backend=anthropic`，前提是先配了 `ANTHROPIC_API_KEY` secret。这只是「跑通」兜底，**不是常态用法**。

### 端到端流程

```
guard (鉴权 / 跳过非 /analyze 评论)
  ↓
analyze
  ├─ Checkout main
  ├─ setup_ci_env.sh  ── 装 gh/jq/tokei/claude-code，vendor skill → ~/.claude/skills/
  ├─ Decide target URL ── 优先 dispatch 输入 → issue 评论 → 自动选 (select_next_repo.py)
  ├─ run_skill.sh "/repo-miner $URL …"
  ├─ run_skill.sh "/md2wechat <report> 入草稿箱"
  ├─ 更新 src/publish.md，commit & push 回 main
  └─ 上传 tmp/logs 为 artifact（14 天）
```

### 验证清单

首次跑之前：

1. 把上面 5 个 secrets 都填好
2. Actions → Auto Analyze & Publish → Run workflow，**留空 repo_url** 让脚本自动选
3. 等 15-30 分钟
4. 检查：
   - `src/analysis_report/{owner}_{repo}.md` 是否生成（三阶段中间产物写在 `tmp/`，不入库）
   - 微信公众号后台「草稿箱」是否有新草稿（封面 + 标题 + 正文）
   - `src/data/publish_history.jsonl` 是否追加了一行
   - main 分支是否有 `feat(auto): 分析 ...` 的新 commit

### 同步 vendored skills

升级 `repo-miner` / `md2wechat` 后：

```bash
42plugin update opc/starlight/repo-miner
42plugin update zhiping/creator/md2wechat
cp -RL .claude/skills/repo-miner ci/skills/
cp -RL .claude/skills/md2wechat ci/skills/
git add ci/skills && git commit -m "chore: 同步 vendored skills"
```

## 目录速查

- `src/analysis_report/` — 最终分析报告（375+ 篇）
- `src/data/` — 站点元数据 + 各数据源 SoR（`publish_history.jsonl` 发布历史 / `starred_seed.json` 大牛 Star / `trending_snapshots.jsonl` Trending；`db.sqlite` 不入库，CI 重建）
- `src/trending_repo/` — `parse_trending.py`（生成 SoR）+ `all_repos_deduped.json`（去重汇总）
- `notes/` — 提示词模板 / 工单 / 待办（三阶段中间产物在 `tmp/`，不入库）
- `src/scripts/` — CI / 核心脚本（select_next_repo / run_skill / setup_ci_env 等）
- `scripts/` — 一次性辅助脚本（公众号同步、DB 查询、历史迁移）
- `ci/skills/` — vendored skill 文件，CI 启动时拷到 runner 的 `~/.claude/skills/`
- `.github/workflows/auto-analyze.yml` — 主自动化 workflow


## 开源周刊与 AI 周刊

开源周刊入口为 `/opensource-weekly [YYYY-MM-DD]`，站点栏目为 `/weekly`（兼容旧 `/daily` 链接及 RSS）。
每周五北京时间 06:00 自动生成，聚合截至前一日 UTC 的最近七天 Trending 与大牛 Star 动态，
按 ISO 周防重复；数据刷新仍每日进行。文章在 `src/weekly_report/`，
索引为 `src/data/weekly_digests.jsonl`，原日报保留原始标题及日期作为存档。
工作流 `.github/workflows/weekly-digest.yml` 沿用开源篇的公众号草稿发布设置，手动可选 `skip_publish`。

AI 周刊已独立迁移到 `~/proj.xt.com/ai-info`，在那里使用 `/ai-weekly [YYYY-MM-DD]`。
新项目有独立采集配置、七天窗口、去重索引和 Actions 流程，不依赖本仓库。

```sh
python3 src/scripts/collect_weekly_facts.py 2026-10-18 --type ecosystem
python3 -m unittest discover -s tests -p 'test_weekly.py'
```
