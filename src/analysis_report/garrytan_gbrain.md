# GitHub 推荐：32K star 的 agent 记忆层：182 万行、98 条架构断言

> GitHub: https://github.com/garrytan/gbrain

## 一句话总结

GBrain 给已经在用的 AI agent 配一个「**文件即真相、可审计、可纠错**」的个人知识库（支持从 Obsidian / Notion 迁移笔记）——Canonical Markdown 存真相、**Postgres 只做派生索引**，混合搜索（关键词 + 向量 + RRF 融合）写入零 LLM 调用，**纠错与撤回是一等公民**。

## 值得关注的理由

1. **32K star 掩盖了 182 万行的工程密度**：2026-04-05 开仓，7 个月 14,033 次提交、100 个 Release、729 个 tag，最新版本 v0.60.644.0（一天甚至多版）。2026-10 单月 11,211 次 commit，占全生命周期 80%。作者是 YC 总裁兼 CEO，首发周末就拿 9.5K star——**热度有水分，但代码没有**。
2. **CI 不只是跑测试，而是跑 98 条架构断言**：分层边界、文件大小 ratchet、SQL 方言品牌、隐私读路径、secret 泄漏、孤儿模块……全部变成 `check:*` 脚本里独立的机器断言。这是本项目最独特、也最难被竞品抄走的工程实践。
3. **评测诚实度范式**：主动自曝基准泄漏（433/500 的判定数因答案 session id 对判定模型可见而失效，10 月 4 日用不透明 id 重跑），并把负面结果连同实验成本一起入库（摘要选择器 48/60 vs 全量 53/60，零改善 5 退步，成本 $8.01）。
4. **定位是「个人知识大脑」而非 agent 记忆基础设施**：Markdown 存在 Git 仓库里，diff / branch / audit / rebuild 全部成立，DB 只是可重建的派生索引；支持从 Obsidian / Notion / Logseq / Roam 迁移笔记。相邻赛道拥挤（Mem0 68K、Hindsight 60K），这条线上 gbrain 是唯一 30K 级选手。

## 项目展示

![GBrain 官网首页主视觉](https://gbrain.io/branding/cast/neo-quiet-hero-2baf1b726157ae8db55f3f8d590e4c9f.webp?vsn=d)
官网主站英雄图。产品定位是「给你已经在用的 agent 一个你自己拥有的记忆层」

![GBrain 的 Star 增长曲线](https://api.star-history.com/svg?repos=garrytan/gbrain&type=Date)
Star-History 曲线：首发周末约 9,500 star，此后逐月 +4.3K → +2.5K → +1.8K → +1.2K → +0.9K，衰减但未停（注：该服务 y 轴上限为 30K，曲线顶端已贴边）

![GBrain 的共享记忆概念插画](https://gbrain.io/branding/cast/neo-memory-robot-3727b5256eda75c81357ce67bfef2ec2.webp?vsn=d)
「共享记忆」概念可视化——团队场景下多人共用的私人大脑

![GBrain 的 Skill 卡片示例](https://gbrain.io/branding/cast/neo-skill-are-we-dying-0531a68813021630651c1fa82a0ca34c.webp?vsn=d)
Skill 卡片：75 个 skill 全部是 `SKILL.md` + frontmatter，作者称之为「Markdown is actually code」

![GBrain 字标](https://raw.githubusercontent.com/garrytan/gbrain/master/docs/images/brand/gbrain-wordmark.svg)
品牌字标。这个项目的价值载体是文字而非视觉——全仓库 markdown 里除字标外零图片引用

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/garrytan/gbrain |
| Star / Fork | 32,354 / 4,791（fork 率 14.8%，大量人是 clone 下来真改） |
| 代码行数 | 1,822,638（TypeScript 84.3%、JSON 13.8%、JavaScript 0.8%、Shell 0.6%）；注释 617,165 行，代码/注释比约 3:1 |
| 项目年龄 | 7.2 个月（2026-04-05 至今）；src/ 3,552 个 TS 文件约 80.1 万行，test/ 5,979 个 `*.test.ts` 约 108 万行（测试/源码 ≈ 1.3:1） |
| 开发阶段 | 密集开发（近 30 天 8,995 次 commit，近 90 天 13,149 次；2026-10 单月 11,211 次） |
| 贡献模式 | 独立开发（252 个名义作者身份中主作者占 58.2%，合并其多个 git 身份后实际约 85%，bus factor ≈ 1） |
| 热度定位 | 大众热门（名人光环驱动，首发即 9.5K；HN 讨论最高仅 23 分，无社区自组织热度） |
| 质量评级 | 代码[优秀] 文档[优秀] 测试[充分] |

## 作者视角：为什么存在这个项目

### 创始人/作者背景

**Garry Tan**，Y Combinator 总裁兼 CEO。GitHub 账号 2008 年注册（18.3 年老账号），15,942 粉丝，24 个公开仓库。个人博客 [blog.garrytan.com](https://blog.garrytan.com) 的内容是创业/管理/思维方法论，**没有任何 gbrain 相关的技术博客**——全部架构信息都写在仓库里。

工程能力的独立背书来自同一作者的 [`gstack`](https://github.com/garrytan/gstack)：141,012 star、20,804 fork、23 个 opinionated 工具。这说明 gbrain 的 32K 不是「名人光环独有的溢价」。

但身份上要清醒：**gbrain 是他个人的旗舰项目，不是公司项目**。README 第一人称「I built GBrain to run my own AI agents」，官网标注「Built by Garry Tan」。85% 的代码由一个人写，AI 辅助机器人（capy-ai[bot]）承担了一部分机械工作。

### 问题判断

**典型的 dogfooding 驱动的第一性需求**。项目的缘起写在 `docs/ethos/ORIGIN.md`：GBrain 源自 Garry Tan 的个人 agent 分支 OpenClaw，最初的「brain」只是一个扁平 markdown 目录，搜索靠 ripgrep，作者自嘲「Memory was vibes」。两个立刻暴露的问题：

1. **agent 在会话之间忘记东西**——周二的决定活不过周四；
2. **agent 不断重复劳动**——同一个公司的两条信号变成两个 people 页面，同一个人的三次会议变成三条互不相关的时间线，信噪比实时衰减。

**时机为什么是现在**，三个条件同时成熟：

- 2026 年的 agent 已经能连续跑几小时到几天，**「跨会话记忆」才第一次成为真需求**；
- Anthropic 意外把 Claude Code 源码发到 npm（2026-03-31，51.2 万行），作者读完确认了**「模型不是瓶颈，harness 才是」**这个框架（`docs/ethos/THIN_HARNESS_FAT_SKILLS.md` 原话：「the secret sauce isn't the model. It's the thing wrapping the model」）；
- Claude Code 的 20,000 行 CLAUDE.md 让模型注意力衰减，作者自己把它降到 200 行指针——**这就是 spring skill-loading 模式的直接动机**。

作者的观察是：**搜索给你页面，大脑给你答案**。README 用一个具体对照演示——普通工具返回 5 个需要你自己读的链接；GBrain 直接输出带引用的答案 + 三个待办项 + 一句 gap analysis（「brain 里关于 Alice 的信息已经 6 周没更新了，邮件和 Slack 它看不见」）。作者给这个 gap 起了个说法：**「the gap analysis is the part that changes how you use the brain」**。

### 解法哲学

`docs/ethos/THIN_HARNESS_FAT_SKILLS.md`（YC Spring 2026 演讲稿）定义了**五个定义**，实际上是整个项目的宪法：

| 定义 | 内容 | 代码里的体现 |
|---|---|---|
| **Skill File** | 「Markdown is actually code」——skill 是方法调用，参数由调用方给 | `skills/` 下 75 个 skill 目录全是 `SKILL.md` + frontmatter `triggers:` |
| **Harness** | 薄的：跑模型循环、读写文件、管上下文、管安全。反模式是「fat harness with thin skills」 | `src/core/skills/resolver/` 的 BM25F 索引 + `<relevant_skills>` 块（最多 5 条建议 / 400 token） |
| **Resolver** | 「Skills say HOW. Resolvers say WHAT to load WHEN」 | `skills/RESOLVER.md`（人类地图）+ `spring-index.ts`（机器索引）+ 确定性 BM25F 排序 |
| **Latent vs. Deterministic** | 「Latent space is where intelligence lives. Deterministic space is where trust lives」 | typed edge 抽取用规则而非 LLM；信任层用 SQL trigger 钳制 |
| **Diarization** | 「Read 50 documents, produce 1 page of judgment」——这是 LLM 必须做的，不能下放给 SQL/RAG | `gbrain think` 的 GATHER→SYNTHESIZE 流水线（`src/core/think/`，12 个模块） |

**明确不做的事**（都有代码级证据）：

- **不做浅色模式**：`DESIGN.md` —「Dark theme is the only theme. No light mode toggle planned — admin is an operator tool, not a marketing surface.」
- **不做图表库**：服务端纯函数 data→SVG，零新依赖
- **不做卡片框**：「Cards earn their existence」
- **不做模型侧记忆**：README 反复强调「Your harness subscription and any separately configured model API usage are different costs」
- **砍掉迭代型 self-optimization**：v0.60.569.0 正式废弃 SkillOpt 迭代循环——实验证明一次改写绑定约 1.8 倍成本，且每次保留的编辑都来自第一步

**价值观总结：简单 + 可拥有 > 功能完整**。作者宁可自己写一套调度器也不用现成框架，因为他要的是「像产品一样的手感」，不是「像基础设施一样的可组合性」。

### 战略意图

**核心产品（个人知识大脑）+ 薄基础设施（Postgres 兼容层）**，不是纯基础设施。三种部署拓扑可叠加，用 `GBRAIN_HOME` 统一解析：单 brain（本地 PGLite / Supabase）、跨机 thin client（agent 在本地、brain 在远端）、split-engine（多 Conductor worktree 不共享 code index）。

**商业化是 genuinely open，不是 open-core**：MIT 许可 + 自托管免费，核心能力（含多租户、RLS、审计）全在 MIT 里；付费的是托管运维（gbrain.io，Personal $49/月、Teams $199/月含 $100/月 AI credit、Enterprise 定制）。README 自己的原话是「MIT-licensed and free to self-host; gbrain.io is optional paid hosting」。

**真正的威胁不是竞品，而是自我蚕食**：同一作者的 `gstack` 已经有 14 万 star，如果它把记忆能力吸收进 Claude Code 工具链，gbrain 的独立价值会被压缩。这是无法用技术防御的风险。

## 核心价值提炼

### 创新之处

按新颖度 × 实用性排序：

1. **98 条架构断言组成的 CI（新颖度 5/5、实用性 5/5）** — CI 不只是跑测试，而是把分层边界、文件大小上限、SQL 方言品牌、隐私读路径、secret 泄漏、孤儿模块、生成产物新鲜度等全部变成 `check:*` 脚本里的独立断言。配合 `docs/architecture/KEY_FILES.md`（70 条子系统条目指向 `key-files/` 下 86 篇分册，脚本禁止「抬高上限」，只能拆分）。**这不是功能，是组织能力**，且随时间变宽——新人和新 agent 贡献时的准入质量由 CI 保证。
2. **Canonical Markdown 真相源 + 具名 DB-only 例外清单 + grep 门禁（4/5、5/5、5/5）** — `docs/architecture/system-of-record.md` 逐表列出哪些能重建、哪些不能；`scripts/check-system-of-record.sh` grep 封禁 7 个直接写派生表的调用，豁免必须在同一行写 `// gbrain-allow-direct-insert: <reason>`。关键诚实点：**作者明确承认「Markdown 导出 ≠ 完整备份」**，DB-only 的 withdrawal ledger / belief ledger / mutation journal 必须单独备份。
3. **纠错优先排序（4/5、5/5、4/5）** — 新事实带纠正线索 + 与旧事实共享 2 个匹配词 + 同 entity + 不降低信任 + 加数字或撤回 → 排到旧事实之前，旧事实标 `corrected_by`。「thanks for the correction, noted」不算纠正。实测 **27/27**（旧版 1/27），且零条旧结果丢失。
4. **披露制的行为变更通知（4/5、4/5、5/5）** — 「every change stays on, nothing waits for an answer, and delivery is never recorded as the user's consent」。身份 = notice-since × brain × channel × client；两个 marker 机制（本地 `wx` 独占创建 / HTTP bounded kv row），无迁移，fresh install 不打扰。
5. **确定性 typed edge 抽取 + 用户可扩展 schema pack（4/5、4/5、4/5）** — 三层管线（显式 grammar 语法 / NER + pack regex / 用户 pack 覆盖），**全部零 LLM 调用**。pack 正则走 `PageRegexBudget` + `runRegexBounded`（vm timeout + 长度上限 + star-height lint）。写入零成本零延迟，图谱免费生长。代价是召回率低于学习式抽取。
6. **单一 gateVoice() 门禁 + 小模型判官 + 手写兜底（4/5、4/5、5/5）** — 五个用户可见面共用一个函数，一个 Haiku 判官 + mode-specific rubric，最多 2 次重生成，回落到手写模板；**失败永不静默**。把「文案要像朋友不像评分系统」变成不可绕过的机器约束。
7. **行级租约 + fencing token 取代 advisory lock（4/5、4/5、4/5）** — `gbrain_cycle_locks` 表 + 每次获取铸新 `acquisition_token`，refresh/release 只按 `(id, holder_pid, acquisition_token)` 匹配。**为 PgBouncer 而生**（advisory lock 是 session-scoped，transaction pooling 会丢 session state）。配套 TLA+ 规约（`NoSpuriousLapse` 不变量）+ 变异测试 + 规约常量与代码常量的一致性测试。
8. **自曝基准缺陷 + 保留负面结果 + 记录实验成本（4/5、4/5、5/5）** — `docs/research/answer-evidence/` 15 篇一手论文逐条引用 + 支持跨度 + 哈希 + 跨模型评审；`docs/eval-bench.md` 明确写「Recorded experiments, **including negative results**」。**这是竞品对比里最难被复制的一项**——竞品的 LongMemEval 94.4% 全是厂商自报且语料不可比。
9. **故障注入式并发正确性证明（Crash Robot + 参考模型）（4/5、4/5、3/5）** — 生成 op 调度 → 真实 handler → 每步比对参考模型 → 注入崩溃 → 恢复 → 再比对；nightly 2,000 notes / 50ms RTT / 20 个种子化 kill，失败把种子和故障计划写进 step summary 可直接重放。
10. **服务端纯函数 data→SVG 渲染（3/5、4/5、5/5）** — 数值 `.toFixed()` 强制、字符串走 `escapeXml()` 全量转义、endpoint 由 `requireAdmin` 把关。零客户端图表库。

### 可复用的模式与技巧

1. **单函数门禁 + 模式化 rubric + 小模型判官 + 手写兜底** — 把一条产品哲学变成机器约束。适用：AI 产品文案、UX 规范、API 错误信息
2. **grep 门禁 + 行内豁免注释 + CI 集成** — 用最便宜的机制守住一条架构不变量。适用：分层架构、真相源约束、直接写禁令
3. **冻结上限的 ratchet（只降不升）** — `scripts/check-module-size.sh` 给每个巨型文件冻结行数上限，未列出的新文件硬上限 1500 行；规则还要求「上限 - 实测 > 50 行」也 FAIL，防止缩水后上限虚高。**唯一成长路径是 reviewer 可见的 TSV 编辑**。适用：任何长期演化的代码库
4. **AST 级 CI 断言** — `scripts/check-layering.ts` 用 TypeScript AST 解析 import 形式（含 type-only / dynamic import / require），三条不变量：`engine-sql/**` 不得 import 引擎 façade（防 ESM 循环）、`schema-migrations/**` 不得 import `migrate.ts`、`persistence/**` 不得 import `ai/gateway.ts`——**「the write commit path never calls a generative model」**
5. **生成产物 + freshness 检查 + `--check` 模式** — manifest / loaders / schema / llms.txt / error-codes 全部生成并守新鲜度
6. **TLA+ 规约 + 变异测试 + 常量一致性测试** — 把并发协议的形式化验证接进 CI。适用：分布式锁、租约、fencing、恢复协议
7. **具名例外清单（FS-canonical / derived / DB-only-by-design）** — 显式承认「哪些数据不可重建」
8. **降级而非丢弃的预算裁剪** — spring skill index 超预算时**先削最长行的 trigger，一次削一个，绝不丢 skill**，实在放不下就抛 `SkillIndexTooLarge` 并让调用方保持原文件不变。适用：任何有硬预算的上下文构建
9. **真相优先检索（纠错优先 + 生成页降权 + 显式 expired 状态 + 事实块前置）** — 让「当前真相」和「历史」在检索层就分开
10. **负面结果与实验成本一起入库** — 把失败的实验写进 `docs/eval-bench.md` 并附上花了多少钱
11. **拆分人格插件变体（plugin-variants/）** — 同一套 skill 按用户场景裁剪成多个可安装 persona（gbrain-coding / gbrain-daily）

### 关键设计决策

#### 1. Canonical Markdown + frontmatter 是真相源，DB 只是派生索引

- **问题**：一个「有状态的记忆系统」到底是**文件优先还是 DB 优先**？这决定了灾备、Git 协作、隐私边界、能否重建。
- **方案**：`docs/architecture/system-of-record.md` 定义三类——**FS-canonical**（Takes / Facts / Links / Timeline / Tags，markdown 里有 `<!--- gbrain:takes:begin -->` fence，DB 表是投影，各有 reconciler）、**Derived from FS but not user-authored**（`pages` / `content_chunks` / `page_versions`）、**DB-only by design**（`raw_data` / `oauth_*` / `access_tokens` / `withdrawal ledger` / `mutation journal + receipts + outbox` / `belief ledger`）。
- **Trade-off**：牺牲了「纯文件」叙事的优雅。收益是灾备变成一条无聊的短序列（验备份 → 擦派生表 → `gbrain reinit-pglite` → `gbrain sync` → `gbrain extract all`），多机同步就是 git，敏感页面可以 per-page gitignore。
- **可迁移性**：高。任何「AI 长期记忆 / 知识库 / 个人 wiki」项目都应该抄这一条。

#### 2. CLI 与 MCP 共用同一批 Operation 对象

- **问题**：agent 生态里 CLI 和 MCP 极易漂移——一边加了功能另一边没有。
- **方案**：`src/core/operations.ts` 拼装 194 个共享 `Operation` 对象（`src/core/ops/` 下 75 个文件）。`src/mcp/dispatch.ts` 顶部注释直接写着动机：*「Drift between transports caused PR #483's reversed-args + missing-context bugs; this module exists to prevent that recurring」*。更细一层：`scripts/build-operation-manifest.ts` 生成不含 handler 的 manifest（CLI dispatcher 和 MCP tools/list 都从它解析，**因此两者都不加载背后约 760 个模块的 handler 图**，直到真正调用某个 op），生成器还有一道硬断言：**「an operation must be exported by exactly one module under src/core」**。
- **Trade-off**：牺牲了 CLI 的自由（CLI 只能是 op 的薄壳），换来绝对对等。作者给了逃生口并在注释里写明原因（`forget` 是 CLI_ONLY 命令，放 cliHint 会被静默遮蔽）。
- **可迁移性**：高。任何需要多入口（HTTP / CLI / SDK / GUI）的项目都能用。

#### 3. 确定性 typed edge 抽取，零 LLM 调用

- **问题**：要回答「谁在 Acme 工作」就需要从自由文本抽 typed edge（`works_at` / `attended` / `invested_in` / `founded` / `advises`）。用 LLM 抽则**每次写入付费、有延迟、有不确定性**。
- **方案**：三层——**显式语法层**（`src/core/line-grammar.ts`，536 行纯函数，支持 `works_at [[companies/acme-example]] (since 2024)` 和 `@effective[start,end)` 内联有效期区间；守卫规则极细：category 只能一个 token、全大写 `[TODO]` 拒绝、代码块/blockquote/facts fence 内一律不读、**每个守卫只读一行**，所以一行的解析从不依赖邻居）；**NER + schema-pack 规则层**（`buildGazetteer` → `findMentionedEntities` → 取提及前后 80 字符 context window → 按 pack 声明的 `link_types[].inference.regex` 推断动词，「CEO of Acme」→ `works_at`）；**用户 pack 覆盖层**（pack 声明的动词优先于内置正则，「pack-driven verbs WIN over legacy inference because users opt into them deliberately」）。
- **Trade-off**：牺牲召回率（规则只认它认识的实体和措辞，别名需用户显式写）。收益是写入零成本零延迟、结果完全可复现。
- **效果数据**：BrainBench 上 relationship retrieval 把生产 R@5 从 **0.6626 提到 0.7241**（45/435 问变好，**0 问变差**）。作者明确标注 `graph-oracle-parse` 的 0.9791 是**上界，不是产品分**。

#### 4. 纠错与撤回是一等公民——从数据模型到排序到 CI 全链路

- **数据模型**：`src/core/trust/tier.ts` 定义 6 级信任（`user_confirmed > operator_curated > tool_observed > agent_written > unknown > external_untrusted`），**一套词汇、一个顺序、一套用户可见标签**（「confirmed by you」/「your notes」/「tool data」/「written by an agent」/「unverified origin」/「external, untrusted」）。等级用事务局部 setting（`gbrain.write_trust_tier`）传到 DB，由 BEFORE ROW trigger **只钳制不提升**。
- **读侧下限**：`oauth_clients.min_trust` / `access_tokens.min_trust` 是**每个连接**的读地板，只有可信本地 CLI 能写，MCP 和 admin HTTP 面都改不了。
- **forget 语义**：过期事实而**不删审计**，幂等；返回里区分「这次调用过期了」和「它本来就已经过期」。
- **生成页降权**：gbrain 自己生成的页面（`dream_generated: true`）在同 entity 竞争时**分数 × 0.5**——「a summary is not evidence」。但**记录纠正的生成页永不降权**。
- **信念账本**：`src/core/belief/`（22 文件），append-only 记录「这个脑曾经记录过什么」。`docs/designs/BELIEF_LEDGER.md` 花了整整一节论证**为什么行级捕获在这里必然失败**——facts 的 fence 投影是「过期并脱离」而非删除、改一句散文会重写 26 行而**零信念变化**、硬删除靠 FK cascade 无应用代码参与、低信任写不是被拒而是**被 contest**（新行照插、旧的留着、同时开一个 `trust_proposals`）。所以账本由**发布者本来就要算的 canonical diff** 喂。
- **Trade-off**：这是所有记忆系统里最贵的一条——信任分层要贯穿写入路径、读取路径、schema trigger、doctor check；信念账本是 DB-only 不可重建；纠错优先排序会牺牲一点召回（要 3/4 查询词命中）。收益是这是唯一能让 agent 长期持有事实而不被污染的机制。

#### 5. 搜索是「多臂 + RRF 融合 + 分数契约」的流水线

- **方案**：`src/core/search/` 117 个文件，核心流水线（`hybrid.ts` 注释）：`keyword + vector → RRF fusion → normalize → boost → cosine re-score → dedup`，`RRF score = Σ 1/(60 + rank_in_list)`，compiled truth boost 2.0x（只在 `detail='low'`），cosine re-score = `0.7*rrf + 0.3*cosine`。
- **两个精心细节**：`PRE_FUSION_POOL_FLOOR = 50`（「`limit*2` alone starves RRF fusion at small limits and turns offset pagination into a **cliff**」）；`COMPILED_TRUTH_BOOST` 只作用于 `detail='low'`（注释记了原 bug：曾写成 `detail !== 'high'`，把 `high` 当特例，而 RRF 在 100 深池子里的整个值域只有 1/60 → 1/160）。
- **分数契约**：`src/core/search/score-contract.ts` —— 排序分数不是裸相似度，是一个有文档、可被不同 arm 组合的契约。**每个开关都有测量数据**（如 query facts block：sealed held-out 200 题上 183 vs 151，加约 70 token）。
- **Trade-off**：多臂 + 融合 + rerank = 高延迟和复杂度。换来可解释的分数来源。

#### 6. 手写 SQL + 极克制的依赖（30 个 runtime）

- **问题**：为什么不用 ORM？为什么不用现成框架？
- **方案**：依赖表里**没有 ORM、没有前端框架、没有图表库、没有 LLM SDK 直调**（走 `ai` + provider SDK）——只有 `@electric-sql/pglite`、`pgvector`、`@modelcontextprotocol/sdk`、`zod`、`marked`、`express`、`chokidar`、`tree-sitter-wasms`、`@dqbd/tiktoken`、`@aws-sdk/client-s3` 等 30 个。SQL 手写并按存储域拆进 `src/core/engine-sql/`（每个域一份 SQL 实现 + 方言适配）。运行时用 **Bun 而非 Node**（`engines.bun >= 1.4.4`），`bun build --compile` 出单文件二进制。`vendor/postgres` 是自带 vendored 的 Postgres 驱动（`package.json` 的 `imports` 字段映射为 `#postgres`），`scripts/check-vendor-postgres.sh` 守这条。
- **Trade-off**：手写 SQL = 没有类型安全的查询构建器，迁移成本高；但换来**方言差异可控**。自 vendored Postgres = 背维护成本，换来无供应链风险。
- **可迁移性**：中。ORM-free 的决定高度绑定 Postgres 语义。

#### 7. 原子写入 = temp sibling + fsync + rename，且明说不解决 lost update

- **方案**：`src/core/atomic-write.ts` — 唯一 tmp sibling（`.<sha256(target)>.tmp.<uuid>`）→ 用目标原权限打开 → fchmod 过 umask → write → fsync → close →（可选）verify 回调读回磁盘字节校验 → rename 覆盖目标。POSIX 上 rename 原子，读者永不见撕裂文件。
- **细节**：`.sha256(target)` 前缀让「目标 basename 接近 NAME_MAX 时 stage 名仍合法」（#5861），且**两个并发写者永不撞 tmp 路径**。
- **诚实的地方**：「Note the rename does NOT prevent lost updates between two read-modify-write writers — callers that need that take the per-page lock」。先原子后加锁，分工明确。

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | GBrain | Mem0 | Hindsight | Zep + Graphiti | Letta |
|------|---------|------|-----------|--------|------|
| Star 数 | 32,354 | 68,736 | 60,200 | 5,001（+Graphiti 子仓约 30K） | 25,401 |
| 写入是否烧 LLM | **否**（typed edge 零 LLM） | 是（事实抽取） | **是**（每次 retain 一次调用） | 是 | 是 |
| 数据归属 | **Canonical Markdown，在 Git 里** | DB（provenance 最弱，蒸馏后出处丢失） | DB / 托管服务器 | 图数据库（需 Neo4j 栈） | agent 运行时内部 |
| 纠错与撤回 | **一等公民**：6 级信任 + per-token 读地板 + 纠错优先排序（27/27） | 无专门机制 | 有提案/反思机制 | **时序失效最强**（bi-temporal） | agent 自编辑记忆 |
| 多跳图遍历 / 时序推理 | **弱**（规则式广度优先） | 弱 | **强**（BEAM 10M 64.1% vs 次优 40.6%，SOTA） | **强** | 中 |
| 多租户就绪度 | **未完成面**（member 表 RLS 缺口 #8399 仍 open） | 中 | **强** | 强（企业导向） | 强 |
| 集成广度 | **弱**（Vectorize 给 2/5） | **最强**（3 行集成，框架无关） | 中 | 中 | 需自建运行时 |
| 评测透明度 | **最高**（公开 evals 仓库 + 自曝泄漏 + 保留负面结果） | 厂商自报 | 学术背书但由利益相关方复现 | 约 71.2% | 自报 |

### 差异化护城河

1. **System of Record 契约 + 98 条 CI 架构断言** — 这不是功能，是**组织能力**。竞品可以在几周内抄一个「记录 provenance」的字段，但抄不了「文件优先 + 具名例外清单 + grep 门禁 + 模块大小 ratchet + KEY_FILES 分层索引」这一整套。且**这层护城河随时间变宽**。
2. **评测诚实度** — `docs/research/answer-evidence/` + 负面结果库 + BrainBench 9 个套件（含 4 个 trust 套件 + poisoning + deletion）。竞品的 self-reported 数字全部厂商自报且语料不可比；gbrain 公开自己的失败（48/60、$8.01、433/500 的泄漏），这是**极难被追平的信任资产**。
3. **运维文化的整体水位** — 25 个 CI workflow、98 条断言、nightly-red issue 治理、CI 成本账本、TLA+ + 变异测试、Crash Robot + 参考模型。这是 14,033 次提交、7 个月、单人主导积累出来的。

### 竞争风险

1. **gstack 自我蚕食**（同作者，14 万 star）——最大威胁，且无法用技术防御。
2. **多租户是未完成面**：#8399（仍 open）同时挂着导出往返不对称、reader 权限放宽、写入门禁、**rule-id 冲突**、**member 表的 RLS 缺口**五个子问题；v0.60.463.0 才刚做过一次「RLS 全表回填」，**同一个洞 10 月补过一次，11 月在 member 表上还开着**。托管化一旦真跑起来，#6543 显示 read pool 2 小时 wedge 4 次、重启后 sync 写入悬挂、**且没有足够 telemetry 调试任何一个**——作者自己把「缺 telemetry」写进了 issue 标题。
3. **写权限收窄的自噬**（#5280）：`writer_coordinator_required` 是防「远程 agent 改写来源、抬高信任度」的正确防线，但收窄过头会让**维护写入者和 autopilot 自己的 extract 任务**被拒——即自愈能力失效。
4. **bus factor ≈ 1** + 不可持续的发版节奏：一天多个 patch、v0.60.644.0、14,033 次提交 / 7 个月。

### 生态定位

**「个人知识大脑」赛道唯一 30K 级选手**。相邻的「agent 记忆基础设施」赛道拥挤（Mem0 68K / Hindsight 60K / Graphiti 35K / Letta 25K），但那些是**基础设施**；gbrain 占的是**「一个人长期经营的私人大脑 + agent skill 协议」**这条正交航线。

它的护城河不是模型能力也不是检索算法（RAG 早已商品化），而是**「文件拥有 + 可审计 + 纠错一等公民 + 评测诚实」这四件事的组合**，加上一个已经把 CLI/MCP/插件/托管/评测全做齐的 7 个月单人高速迭代。

值得注意的定位细节：**gbrain 自己反向集成了 DeepWiki**（只读连接 DeepWiki 索引公开 GitHub 仓库）——项目本身就是 DeepWiki 的重度用户，所以 DeepWiki 收录得如此详尽并不意外。

## 套利机会分析

- **信息差**：star 层面**不存在低估**（首发即 9.5K，名人光环已被充分定价，HN 讨论最高仅 23 分说明不是社区自组织热度）。**被严重低估的是 star 数掩盖的工程密度**——20 篇架构文档、477 篇 docs、15 篇一手论文研究档案、98 条 CI 架构断言、108 万行测试。真正的读者收益在于「一个名人 CEO 用 7 个月砸 182 万行代码做出来的东西，架构决策全部写在仓库里且可验证」。
- **技术借鉴**：最有性价比的三件事，都是几十行到几百行的成本、收益立竿见影——① `gateVoice()` 门禁模式；② grep 门禁 + 行内豁免的架构不变量强制；③ 披露制的行为变更通知。其次是纠错优先排序、具名 DB-only 例外清单、冻结上限的 ratchet。
- **生态位**：填补了「个人知识库」和「agent 记忆基础设施」之间的空白——既有 Mem0 那类库的即插即用，又有 Zep 那类图的时序审计，还加了 git 作为审计层。
- **趋势判断**：符合三条趋势——agent 上下文管理从「塞更多工具」转向「thin harness + fat skills」；AI 产品从「黑盒记忆」转向「可审计可纠错记忆」；从「厂商自报 benchmark」转向「可复现可争议的评测」。**比竞品有后发优势**吗？部分有——竞品多是 Python 库起步，gbrain 直接选 TypeScript + Bun + Postgres 兼容层，一步到位跨 Claude Code / Codex / OpenClaw / Cursor 多个 harness。
- **反向机会（更值钱）**：这个项目 32K star、7 个月、每天发版，**几乎所有架构决策都还热着**。现在 fork 或借鉴正当其时，等它稳定下来再抄就晚了。

## 风险与不足

1. **bus factor ≈ 1 是最实质的风险**：作者 + bot 占约 85% 贡献。14,033 次提交 / 7 个月 / v0.60.644.0 的节奏不可持续，核心 85% 的代码由一个人写。
2. **多租户与可观测性欠债**：member 表 RLS 缺口仍 open；托管 Supabase 下 read pool wedge、sync 悬挂写入、telemetry 缺失三缺。**一个号称「自己掌控的记忆」的自托管产品，在出问题时反而缺少可观测性**，这是内在矛盾。
3. **能力短板：多跳图遍历与时序推理**。Hindsight 在 BEAM 上 64.1% vs 次优 40.6%，而 gbrain 根本没跑过 BEAM；确定性实体抽取只认规则认识的实体，别名需要用户显式声明。
4. **评测可比性有限**：自建 BrainBench 语料不同，数字不能与竞品直接对比；未在公共基准上跑过。
5. **冷启动是空白状态**：Vectorize 的评测明确警告——期待 set-and-forget 的用户会积累错误（事实会随着没有更新而失真）。
6. **集成广度不足**：一等公民集成只有 OpenClaw 和 Hermes，其他客户端要自己写 MCP。
7. **文档体量超出单人可持续范围**：CHANGELOG 5.1 MB / 1396 条版本条目，本身就是维护债（作者自己在 README 里也推荐读 `llms.txt` 而不是 CHANGELOG）。
8. **CI 成本明显偏高**：25 个 workflow、Ubicloud runner、330 分钟 timeout 的 nightly。对单人项目是真实的资源压力。

## 行动建议

- **如果你要用它**：
  - **选它**：你是重度 agent 用户（Claude Code / Codex / Cursor / OpenClaw），已经在维护 Markdown 知识库，**并且在意事实被污染**（合规、法务、个人健康档案这类「错了会出事的」场景）。它的 6 级信任分层 + 纠错优先 + 可审计写入在这个场景下几乎无替代。
  - **别选它**：你要的是「一个能用的记忆 API」→ 用 Mem0（3 行集成）；你要多跳推理 / 时序查询 / 多租户 → 用 Hindsight（BEAM SOTA）；你要 agent 自治长时间运行 → 用 Letta。
  - **起步提醒**：`gbrain init --pglite --no-embedding` 可以本地零配置试用（PGLite = WASM 版 Postgres 17），但**它是空白状态起步**，前几周会积累错误事实，要配合 `forget` 和人工校正。
  - **注意**：不要 `npm install -g gbrain`——README 明确警告那会装到无关的同名包，必须用 Bun。
- **如果你要学它**：**先读这 6 个文件**，覆盖 80% 的设计意图——
  1. `docs/ethos/THIN_HARNESS_FAT_SKILLS.md`（作者的宪法：五个定义）
  2. `docs/architecture/system-of-record.md`（真相源契约 + DB-only 例外清单）
  3. `docs/architecture/brains-and-sources.md`（三轴模型：brain=库 / source=库内仓库）
  4. `DESIGN.md`（产品哲学的可执行版本）
  5. `docs/research/answer-evidence/compendium.md`（作者怎么想「什么真正帮助 AI 用记忆」）
  6. `src/core/ops/contract.ts`（Operation 契约 + 统一错误信封）
  - **代码层面**重点看四个目录：`src/core/ops/`（契约）、`src/core/persistence/`（持久化）、`src/core/search/`（检索）、`src/core/trust/`（信任）。
  - **不要被代码量吓退也不要被 star 数误导**：182 万行里很大一部分是 generated（`operation-manifest.generated.ts` / `pglite-schema.generated.ts` 等）、schema migrations（v001…v292+，一文件一迁移）、以及 108 万行测试。
- **如果你要 fork 它**：改动前先跑一遍 `npm run check:*`——你会撞上 98 条架构断言。最值得做的三个方向：① **补上多租户**（member 表 RLS 是明确的已知缺口，#8399 里有完整的复现描述）；② **补可观测性**（托管场景的 telemetry 是作者自己承认的软肋）；③ **补 multi-hop 图遍历**（当前图是广度优先、毫秒级，缺深度推理）。

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | https://deepwiki.com/garrytan/gbrain （已收录，含 `src/core/operations.ts:124-156` 等源码行号引用） |
| Zread.ai | https://zread.ai/garrytan/gbrain （已收录） |
| 关联论文 | 无以 gbrain 为主体的 arXiv 论文。引用的是 [LongMemEval (ICLR 2025)](https://arxiv.org/abs/2410.10813)、Chain-of-Note (EMNLP 2024)、Sufficient Context (ICLR 2025)、ContextualJudgeBench (ACL 2025)、Lost in the Middle (TACL)、RECOMP (ICLR)、LongLLMLingua (ACL 2025) 等 15 篇，逐条审读记录在 `docs/research/answer-evidence/` |
| 在线 Demo | 无公开 playground。最接近：① gbrain.io 注册后托管试用（Personal $49/月）；② `gbrain init --pglite --no-embedding` 本地零配置试用 |
| 官方文档 | https://gbrain.io （GitHub 未配置 homepage，但 README 顶部直接引导过去）；另有 `llms.txt` / `llms-full.txt` 给 agent 用的文档地图 |
| 独立评测 | [Vectorize: GBrain Review](https://vectorize.io/articles/gbrain-review) ｜ [Vectorize: GBrain vs Hindsight](https://vectorize.io/articles/gbrain-vs-hindsight) （注意：Vectorize 是竞品 Hindsight 的作者方，有利益相关性，但 multi-hop 缺失、BEAM 未跑、评测不可比这三点可独立验证） |
