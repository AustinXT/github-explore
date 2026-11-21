# GitHub推荐：13.7K stars 的 AI SRE：OpenSRE 把 CI 红了变成一个待审 PR

> GitHub: https://github.com/tracer-cloud/opensre

## 一句话总结

OpenSRE 是一个自托管的 AI SRE CLI agent——它读失败的 CI run、用确定性规则而非 LLM 猜测区分「CI 坏了」和「代码坏了」、然后把修复推成一个待审的 PR（实际改代码由 Claude Code / Codex / Cursor 这类编码 agent 执行），而不是重跑一次掩盖症状。

## 值得关注的理由

1. **它做的是别人没做的那个垂直。** 2026 年的 AI SRE agent 赛道已经很挤：HolmesGPT、Aurora、K8sGPT、Keep、Robusta、商业侧的 incident.io AI / Datadog Bits AI 都能做「告警来了，帮我查为什么」。但它们全都在处理「代码已经在跑、然后坏了」的场景。OpenSRE 处理的是「代码还没跑起来」——CI 红了，读日志、定位、改代码、推 PR。这个缺口看起来只是场景平移，实际上证据源、动作集、交付物全都不同：前者产出诊断结论，后者产出一个可合并的 diff。修代码这一步它不自己实现，而是把 Claude Code / Codex / Cursor / Pi 当作可插拔后端调用——「手」角色被明确禁止 commit/push，分支与 PR 机制留在调用方手里。

2. **它把评测环境当成产品主线在建。** Issue #2074 的标题就是「Benchmark opensre+LLM vs LLM-alone」，89 条评论里维护者把 8 个社区 benchmark 资源映射进框架（CloudOpsBench 论文与 HF 数据集已集成，OpenSRE-bench leaderboard 提案被提升为第二适配器，RCAEval / OpenRCA 排队中），并自比 SWE-bench：「SWE-bench 展示了 agent 在真实任务+清晰反馈下进步最快。流水线故障比本地代码任务更慢、更噪、更难复现，所以我们用同样的标准要求自己。」这个赛道目前还没有第二个项目在做这件事。

3. **它自己就是自己的第一个用户。** git log 里有一条提交 `3345ad5b5` 的正文是 OpenSRE 修自己的 CI——修了 8 个可复现的失败，根因是 mock 流缺少 `finish_reason` 被 CI 锁定的 LiteLLM 1.109.1 拒绝，提交信息署名 `Co-authored-by: OpenSRE Agent <opensreagent@opensre.com>`。仓库里还带了一个可运行的合成故障床：`integrations/github/tools/ci_repair_demo/seed.py` 会程序化创建一个私有 repo，main 上 `calculator.py` 是 `return a + b`（通过），分支 `demo/failing-ci` 改成 `return a - b`（失败），配真实 GitHub Actions workflow，并用 AGENTS.md 把修复范围精确限定为「只改 calculator.py，不许改测试或 workflow」——所以修复是否成功是可判定的。

## 项目展示

![OpenSRE 官网首屏](https://opensre.com/images/home/opensre-hero.webp)
*官网首屏。定位是一句话：CI 告诉你坏了，但不告诉你为什么坏、怎么修。*

![How OpenSRE Works 六层管道架构图](https://opensre.com/images/home/how-it-works-opensre.svg)
*六层管道：失败接入 → 上下文装配 → 归因分类 → agent 循环调查 → 置信度门控 → 可交付修复报告。*

![CI 成本度量面板](https://opensre.com/images/home/ci-costing-fr-2.webp)
*竞品都不做的一张图：把「CI 可靠性」直接换算成钱——失败率、因不可靠 CI 浪费的开发者工时、main 分支保持红色的时长。*

![Who fixes the build 所有权框架](https://opensre.com/images/home/who-fixes-the-build.webp)
*官方最有意思的一张叙事图：应用团队、平台 DevOps、服务 owner 各负责哪类失败。*

![OpenSRE CLI 欢迎界面](https://raw.githubusercontent.com/tracer-cloud/opensre/main/docs/images/opensre-welcome.png)
*CLI 入口。交互式 REPL 要求已登录账号 + TTY，headless 场景走 `opensre ask "<question>"`。*

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/tracer-cloud/opensre |
| Star / Fork | 13,722 / 1,931（fork 率 14%，说明是真实下载试用而非纯收藏）|
| 许可证 | Apache-2.0 |
| 代码行数 | 522,581 行 Python（Python 98.2%），3,979 个文件 |
| 项目年龄 | 10.3 个月（2026-01-13 创建）|
| 开发阶段 | 密集开发（近 90 天 976 次提交，近 30 天 136 次，2026-11-21 当天仍有提交）|
| 贡献模式 | 社区驱动 + 商业团队主导（396 名贡献者，主作者占比仅 10.5%）|
| 热度定位 | 大众热门且仍处上升通道（2026-01 建仓不足 1 万 star，11-02 已 12,660，11-21 达 13,722）|
| 质量评级 | 代码**优秀** 文档**优秀** 测试**充分**（测试行数 ≈ 生产代码行数）|

## 作者视角：为什么存在这个项目

### 创始人/作者背景

背后是 **Tracer Cloud**——一家做 SRE 编排平台的商业公司，核心产品是把可观测性、基础设施、告警接进聊天里。OpenSRE 的 GitHub 简介是「the world's first open source AI SRE」，账号创建仅 1.8 年、8 个公开仓库，其中 opensre 是绝对主导（第二名 `tracer-client` 只有 18 star，投入权重差 760 倍）。

Top 贡献者 `davincios`（Vincent Hus）和 `YauhenBichel` 同时是公司员工和 issue 署名者。最能说明作者性格的一次披露是 Issue #344——创始人亲自开 issue 招募 maintainer，条件是「每周 dev call（周四 17:00 UK time）+ 评估委员会 2 票通过 + $300–500/月 symbolic sponsorship」，并在正文里把项目自述为「an open reinforcement learning environment for agentic infrastructure incident response」。注意用词：RL 环境，不是工具。

### 问题判断

作者的出发点是 dogfooding，而且是硬狗。三个关键洞察：

**第一，CI 失败有三种成因，而现有工具不区分。** 代码错、CI 基础设施错、所有权不明——不区分开就知道该找谁修。这条判断在代码里被做成了确定性算法：`integrations/github/tools/ci_analytics/metrics.py` 的 `classify_failures` 按 (workflow, head_repo, branch, PR) 分组、按完成时间排序，然后判定——同一个 commit 上失败后又在同一个 commit 上通过 = **RELIABILITY**（CI 造成的）；在新 commit 上才通过 = **SOURCE**（代码造成的）；一直没通过 = **UNRESOLVED**。这直接对应官网「谁该修这个 build」的所有权框架。

**第二，失败的归属不该由 LLM 猜。** 交给模型分类会不可复现、无法审计。所以作者用 git 历史语义做判定，延迟计算还要减去该 workflow 的正常时长（`normal_minutes`），避免把「正常跑 8 分钟」算成「浪费了 8 分钟」。这是全项目最值得抄的一段代码。

**第三，时机是 SWE-bench 范式的迁移。** README 明确写：「SWE-bench 展示了 agent 在真实任务+清晰反馈下进步最快。流水线故障比本地代码任务更慢、更噪、更难复现，所以我们用同样的标准要求自己。」技术前提是 Codex / Claude Code 这类编码 agent 在 2025–2026 成熟到足以承担「修 CI」这项工作。

### 解法哲学

设计哲学被压缩成一句话：**「Fix when sure. Ask when not.」**（有把握就修，没把握就问）。展开是四条：

- **修因而非重跑**（Fix the cause, not just the rerun）——与竞品最锋利的分界
- **证据链驱动**——结论必须挂证据，不允许猜；`core/state/turn_evidence.py` 保留结构化证据（用户消息、每批工具调用及其结果、最终回复）而不只是转录文本
- **局部可逆**——标识符 masking 后再出网、本地还原
- **人在环内**——推 PR 而非自动合并

更值得注意的是几条**被写进代码规约的**选择：

**「LLM 是唯一的工具选择器」。** `docs/interactive-shell-action-policy.md`（2026-06-18）完整记录了一次决策反转——原来有 regex / 关键词映射做意图路由，后来全部移除。原因是「启发式规则和 LLM 竞争，导致误分类，是优先级漂移的反复来源」。这条被提升到 AGENTS.md 的全仓库强制条款：**自然语言意图属于 action agent，没有 regex / keyword / fuzzy 路由或确定性旁路**。唯一的例外是用户逐字输入的 `/slash` 命令。这份文档本身就是一份极有价值的「反模式档案」——记录了作者踩过什么坑以及为什么掉头。

**「技能是自然语言，不是脚本」。** `core/agent_harness/prompts/skills/AGENTS.md` 写着：「一个需要超过几个 helper 的技能是在描述一个工具，不是技能」「没有决策留在脚本里」「把脚本串起来让工作流无需模型推理就跑完，那不是技能，那是戴着技能卡的工具」。判据是一句可操作的检验：「每个脚本能不能删掉而那一步仍能用一句话描述？」

**「人类的文件人类拥有」。** `SKILL.md` 和 `core/agent_harness/prompts/opensre_system_prompt.md` 是绝对禁改的——agent 只能提建议、引用当前文本和拟议文本，唯一例外是用户逐字给出「当前文本 → 替换文本」。这条很少见：大多数 agent 项目里，agent 的提示词是可以被自己的工具改写的。

**「拒绝自欺的确定性」。** AGENTS.md 写「永远不要用恒假条件开关或跳过测试来掩盖失败」。

### 战略意图

**开源自带的不是全部。** Apache-2.0 内核之外有闭源商业侧：OpenSRE Cloud 托管网关、`app.opensre.com` 账号体系（Clerk 认证）、Fargate 网关。开源版是引流漏斗——README 首屏引导 `opensre` 登录即激活托管模型，`core/llm/factory.py:resolve_llm_route()` 里有一条 `account_route is not None` 分支直接把路由强制到 OpenAI，即登录用户默认走托管模型。这是 open-core，不是 genuinely open。

**技能是热更新的 SaaS 层。** `infrastructure/skills_registry/` 实现了一套签名发布 / 拉取 / 回滚系统：ECDSA P-256 签名验证、公钥在 `config/constants/skills.py`、`opensre skills push` / `rollback`、每 5 分钟后台拉取、ETag/304 协商、版本门控（不改 `metadata.version` 就不发布）。**把「提示词工程」做成可版本化、可签名、可回滚的制品**——这在开源项目里极罕见。

**但主线有一个明确的战略摇摆。** CI/CD 修复是核心产品（README 首屏、CI 徽章、demo 菜单第一项），事故调查是遗留能力。`pyproject.toml` 的 description 至今仍写着「Open-source SRE agent for automated incident investigation and root cause analysis. Automatically analyzes alerts from Slack, Grafana, Datadog」，与 README 的「CI/CD reliability agent」分裂——外部评测者把这条列为主要批评之一，代码可证。

反过来，团队也主动砍掉过泛化野心。Issue #1506 提议做一个「监控本机上其他 AI agent 的 fleet dashboard」（把 Claude Code / Cursor / Aider / Codex CLI 当微服务，套 golden signals / SLO / 事故响应，支持 `/agents trace<pid>` tail stdout、`/agents kill <pid>`），最终标记 **not planned**。这说明当前优先级是 CI/CD 可靠性 + 评测环境，不是「agent 运维 agent」。

## 核心价值提炼

### 创新之处

**1. 技能即签名制品：自然语言工作流进入软件供应链**（新颖度 5/5 | 实用性 4/5 | 可迁移性 4/5）

技能卡被当作版本化制品管理：ECDSA P-256 签名、版本门控、原子发布、ETag 协商、后台拉取、一键回滚、**per-turn 快照绑定**（`SkillCatalogSnapshot` 构建一次后不再读文件，新 release 下一回合才生效，绝不 mid-turn 切换）、「release 整体接受或整体拒绝」。

版本号规则也踩过坑并写下来了：minor 是**计数器不是小数**（「2.9 → 2.10」而不是「2.10 = 2.1」）；MAJOR 只在破坏外部契约时动（改名、移除入口菜单问题、移除被持久化 schedule 依赖的步骤）。

适用场景：任何把提示词 / 工作流当作运行时可加载制品分发的系统。

**2. CI-caused vs code-caused 的纯确定性归因**（新颖度 4/5 | 实用性 5/5 | 可迁移性 5/5）

不用 LLM，用 git 历史语义判定责任方。配套的「谁该修这个 build」模型给出三类默认响应人（应用团队 / 平台 DevOps / 服务 owner），以及一句被反复引用的论断：**「30 秒内找不到 build owner，说明这是组织所有权问题而非 CI 工具问题」**。

适用场景：任何需要区分「环境问题 vs 代码问题」的自动化流水线。

**3. 共享回合内核 + 「默认值即 transport 路径」的防漂移设计**（新颖度 4/5 | 实用性 5/5 | 可迁移性 5/5）

`infrastructure/turn_host/turn_runner.py`（311 行）是交互式 REPL、Slack、Discord、Telegram、Buzz 五个入口跑 agent 回合的唯一实现。妙处在参数默认值：`console` / `confirm_fn` / `is_tty` 等全部默认成 transport 路径的值，因此「省略全部关键字 = transport 路径」在类型层面成立，两条入口不可能漂移。配套 `SessionAgentPool` 保证一个逻辑 session 一个 agent，`session_execution_lock` 是可重入租约。

适用场景：多通道 agent（CLI / REPL / Slack / Teams / Web）需要行为一致时。

**4. 可逆标识符 masking 的工程细节**（新颖度 3/5 | 实用性 5/5 | 可迁移性 5/5）

`infrastructure/safety/masking/` 三件套（policy / rules / detectors），占位符统一为 `<KIND_N>`，同一标识符在同一 session 内映射稳定。细节做得相当细：

- `_derive_counters` 先扫全表取每 kind 的**最大**索引再统一 +1——注释明确说「循环内 +1 会在乱序时多计」（`<NS_2>, <NS_0>` 会得到 4 而非 3）
- `unmask` 用单次左到右扫描 + `<[^<>]+>` 边界，因此 `<NAMESPACE_10>` 不会被 `<NAMESPACE_1>` 部分改写；**替换文本不二次扫描**
- `_canonical_label` 清洗用户自定义 label 里的括号和空格，维持「单层括号」不变量
- policy 每次运行重建，不做模块级单例，因此 env 改动下次生效

与 guardrail 的分工是清晰的二元设计：**guardrail 是单向硬阻断**（信用卡、API key → `[REDACTED]`，不可逆），**masking 是双向可逆**（基础设施标识符，在具体 call site 选择性 opt-in）。

**5. 观察指纹式停滞检测**（新颖度 4/5 | 实用性 5/5 | 可迁移性 5/5）

`core/agent/react_loop.py` 的 `_observation_fingerprint` 对 (工具名, public 输入, is_error 布尔, 成功结果内容) 做 sha256。**故意不哈希错误文本**——因为「provider 会给每次错误装饰新的 request id 或时间戳」，哈希错误内容就永远不重复，检测就失效了。另有独立计数器专治「工具发现反复找到相同能力」的空转。

触发上限时不硬停，而是给模型一个安全交接提示词：「基于已有工作和工具结果给出简明最终交接……**不要声称任务已完成**，不要请求或描述另一个工具调用。」

**6. AST 静态描述符索引 + 运行时插件注册双轨工具目录**（新颖度 4/5 | 实用性 4/5 | 可迁移性 4/5）

125 个集成目录、888 个 .py，全量 import 一次要 ~1.5 秒。`tools/registry_index.py` 用 **`ast` 模块**读工具元数据而不 import 执行器，按 surface 懒加载；运行时注册扩展点线程安全幂等；PyInstaller frozen build 把索引烘进 bundle。

**7. `defer_loading` + `tool_reference` 保住 prompt cache 前缀**（新颖度 4/5 | 实用性 4/5 | 可迁移性 3/5）

Anthropic 缓存的是 `tools → system → messages` 前缀，中途往 `tools` 里加一个工具，后面全部重新计价。`core/llm/transports/sdk/anthropic_deferred_tools.py` 用 `tool_reference` 让搜索揭示的工具延后加载，且在搜索前后 `tools` 读起来完全一致。4.5+ 模型才支持，400 报错自动降级为全量前置加载并永久停止 deferring。

### 可复用的模式与技巧

以下每一条都可以直接搬走：

| 模式 | 要点 | 适用场景 |
|------|------|---------|
| `.importlinter` 分层契约 + 显式豁免台账 | 5 条 contract 把架构边界变成 CI 强制的不变量，技术债边逐条列出并标注工单号 | 任何多包 Python 项目 |
| 默认参数即「最常用路径」的防漂移设计 | 两个入口共享实现，可选参数默认值 = 最常见调用形态 | 多入口库 / 多 transport agent |
| Port/Protocol 端口 + 组合根注册表 | 领域内核只认 Protocol，能力包各自注册，宿主在唯一位置 `CAPABILITY_REGISTRARS` 装配 | 插件化 agent / 依赖倒置框架 |
| 「技能=签名制品」供应链 | 签名 + 版本门控 + 原子发布 + ETag + 回滚 + per-turn 快照 | 运行时加载自然语言制品的系统 |
| 确定性归因替代 LLM 分类 | 用平台语义（git 历史、运行记录）而非模型判断判定责任方 | CI 修复 / 告警分级 / 故障归属 |
| 证据加权置信度 + 结构化 verdict | 加权平均出置信度标签（每项带 rationale），闭环判定用 JSON Schema enum 而非文本抓取 | 需要「够确定才动手」的 agent |
| 可逆 masking + 单向 guardrail 二元模型 | 硬阻断不可逆内容，可逆处理基础设施标识符 | 连外部模型的自托管 agent |
| 观察指纹停滞检测 | 对失败结果只哈希错误布尔值，以对抗 provider 的装饰性差异 | 任何工具循环 agent |
| 工具交换对为单位的上下文驱逐 | 成对驱逐避免孤儿 tool_use；用 provider 自报数修正字符估算但夹住修正系数在 [0.25, 1.5] | 长上下文工具 agent |
| AST 静态描述符索引 + 运行时插件注册 | 免 import 拿元数据，按 surface 懒加载 | 大量 vendor 集成的 CLI |
| 中间件式入站编排上移 | 「两个 transport 都要的 → 上移到 middleware 层」，用 independence contract 强制 | 多 chat 通道网关 |
| 类型化失败种类 + 双套文案 | 内部记全细节，外部只给「什么阻塞了 + 怎么修 + 下一步」 | 集成密集的工具型 agent |
| 合成故障床（作用域精确限定的 fixture） | 程序化创建带真实 CI workflow 的失败场景，限定可改文件使修复可判定 | agent 修 bug 的评测 |
| 「人类拥有文件」的机器可执行规约 | agent 只能提建议并引用当前+拟议文本，唯一例外是逐字 find-and-replace | AI 参与开发的仓库 |
| 能力探测（存在 ≠ 可用） | 探测工具是否真的能跑（`print(1+1)` 得 2 才算 Python 可用），而不是只查 PATH | agent 工具暴露前的预检 |
| 词表化命名规约 + 反模式清单 | 一词一义 + 模块命名模板 `{domain}_{role}.py` + 禁用包名前缀的类型命名 | 大型 Python 仓库的 onboarding |

### 关键设计决策

**决策 1：置信度不靠 LLM 自评，靠结构化 verdict + 客观证据**

- **问题**：「Fix when sure. Ask when not.」怎么落地？让模型说「我有 80% 把握」是最不可靠的做法。
- **方案**：分三层。闭环目标判定用 Pydantic `Literal["GOAL_REACHED","NOT_REACHED"]`（JSON Schema enum），失败返回 `None` 而不是猜；相关性置信度用加权证据——`core/domain/correlation/confidence.py` 的 `build_weighted_confidence` 对每个 `EvidenceContribution(source, score, weight, rationale)` 加权平均，阈值 0.75 / 0.4 分 high/medium/low，权重全部是确定性纯函数（时间窗 0.45、拓扑 0.30、周期性 0.10、特性/工作流 0.15，和为 1.0）；执行层面靠能力探测（只有真能用的工具才暴露）+ 四档自主度 `/auto off|low|med|high`。
- **Trade-off**：阈值是拍出来的经验值，没有公开评测支撑（正是 Issue #2074 暴露的问题）；换来**可审计、可解释**。
- **可迁移性**：**高**。

**决策 2：CI 归因用 git 历史判定，零 LLM**

- **问题**：「修因而非重跑」需要先分清是谁的错。
- **方案**：见上文创新点 2。
- **Trade-off**：只能分类「已修复的失败」，正在发生的失败只有 UNRESOLVED 一档。
- **可迁移性**：**高**。

**决策 3：多 LLM provider 用「统一路由决策 + 双传输层」归一**

- **问题**：Anthropic / OpenAI / Codex / Ollama / Gemini / OpenRouter / NVIDIA NIM / Bedrock / Azure OpenAI，加上 10 个 CLI 型 provider（claude-code / codex / cursor / copilot / gemini-cli / kimi / grok / opencode / pi / antigravity），每个的流式格式、工具调用格式、schema 方言都不同。
- **方案**：`core/llm/factory.py:resolve_llm_route()` 把 (settings, provider, cli_provider_registration, use_litellm) 解析成冻结的 `LLMRoute` dataclass，**所有角色（agent / reasoning / classification / toolcall）共用**——原文说这是为了「so an Azure/LiteLLM routing fix cannot drift between the tool-calling agent and the reasoning/classification/toolcall clients」。`LLMRole` 是「需要哪种能力」而非「用哪家」，加一个 provider 是表里加一行而不是改四个 dispatcher。传输层二选一（原生 SDK / LiteLLM）。schema 归一用结构化 Protocol 而非 import 具体类型，注释解释了原因：「把它放进 `core.llm` 会造成 `core.tool` 的包循环，而它什么也没买到：每个 provider client 最终都把参数放宽成 `list[Any]`」。
- **Trade-off**：抽象层吃掉了 provider 的独特能力（比如 Gemini 的 `thought_signature` 需要在 `raw_content` 里保留原始 dict）；换来**加 provider 成本 = 一行表**。
- **可迁移性**：**高**。

**决策 4：把「另一个编码 agent」当成可插拔后端，且拆成「脑」「手」两个正交角色**

- **问题**：要修代码就得有编码能力——要么自己实现，要么用现成的。
- **方案**：`integrations/coding_agent/` 有 `claude_code_backend` / `codex_backend` / `cursor_backend` / `pi_backend` / `native_backend`。每个跑同一个二进制的**「手」角色**（`-p` print mode + `--permission-mode acceptEdits` + 显式 tool allowlist `Bash,Edit,Write,Read,Glob,Grep`）；`integrations/llm_cli/` 里同一个二进制的**「脑」角色**（prompt in, text out）。安全设计很讲究：`build_guarded_task_prompt` 构造的提示词**禁止 commit/push**——「branch/commit/PR 机制留在调用方手里」；内置 agent 只在修复 checkout 里跑，带 `CI=true` 且**剥离 OpenSRE / provider 密钥**的环境。
- **Trade-off**：依赖外部 CLI 二进制的存在与登录状态；换来不重复实现编码能力，且能复用用户已有的 Claude Code / Codex 订阅（`CODING_AGENT=auto` 自动挑第一个就绪的）。
- **可迁移性**：**中高**。

**决策 5：上下文预算以「工具交换对」为单位驱逐，且用 provider 自报数自校准**

- **问题**：200k 窗口的工具调用循环，工具输出能把窗口吃光。
- **方案**：`core/context_budget.py`。驱逐以（assistant tool_use + 对应 tool_result）为单位，不是按单条消息——拆开会让 provider 拿到孤儿 tool_use 而报错。区分三类消息：`_opensre_seed`（钉住，永不驱逐）、`_opensre_duplicate_result`（重复结果，可先驱逐）、`_opensre_evicted`（已替换成驱逐桩，不再二次处理）。token 估算初始按字符算「故意偏高的 0.50 token/char」，每次调用后用 provider 自己报的数修正，但修正系数夹在 `[0.25, 1.5]`、ceiling 拉伸不超过 3.0 倍——注释写着「不要把请求裁到真实窗口的一半」。溢出重试时预算降到被拒请求估计值的 0.6 倍。
- **Trade-off**：字符估算不精确；换来溢出重试 + 渐进裁剪 + 不发孤儿块三件事同时成立。
- **可迁移性**：**高**。

**决策 6：`.importlinter` 把架构边界变成 CI 强制的不变量**

- **问题**：52 万行 Python、2446 个非测试文件、7 个平级包；「core 不 import surfaces」靠人自觉必然漂移。
- **方案**：五层栈——`surfaces/` + `gateway/`（宿主）→ `tools/` + `integrations/`（能力）→ `core/` + `infrastructure/`（运行时）→ `config/`（底座，只被读）。唯一的双向对是 `core ⟷ infrastructure`，原因是「分成两层反而禁止这条边，所以它们同层互为兄弟」。`.importlinter` 里 5 条 contract 覆盖全量跨包关系（含 `type = layers` / `forbidden` / `independence` 三种），并**显式列出 15 条「T-4 技术债」豁免边**——豁免是被追踪的，不是沉默的破例。`.github/ci/check_direct_imports.py` 补齐「直接边」这一层。
- **Trade-off**：豁免列表本身是负担（新增边要改配置才能过 CI）；换来**分层真的不会塌**——一次涉及 12 万行的目录重构没有引入循环依赖。
- **可迁移性**：**高**。

**决策 7：失败分类用「类型化失败种类 + 面向用户的下一步建议」**

- **问题**：集成失败时给用户吐栈回溯毫无帮助。
- **方案**：`integrations/github/tools/ci_analytics/failure.py` 定义 `GitHubFailureKind`（RATE_LIMITED / UNAUTHORIZED / NOT_FOUND / TLS_UNTRUSTED / UNREACHABLE / SERVER_ERROR / INVALID_RESPONSE），每种配一句**给模型看**的 `_NEXT_STEP`（「不要在额度恢复前重跑分析，告诉用户什么时候恢复并提出届时再跑」）。给用户的是另一条 `analysis_failure_line`——「一行说清什么阻塞了读取、怎么修，**绝不暴露异常细节**」。
- **设计原则**（AGENTS.md）：「在外部 HTTP/chat 响应边界脱敏，不在共享调用点脱敏。」
- **可迁移性**：**高**。

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | OpenSRE | HolmesGPT | Aurora | keep | 商业 AI SRE |
|------|---------|-----------|--------|------|-----------|
| Star | 13,722 | 3,949 | 未公开 | 12,543 | 不适用 |
| 主场景 | **CI 红了 → 修 → 推 PR** | 生产事故调查 | 调查 + 复盘 + 审批门控修复 PR | 告警中枢 / AIOps | 平台内自动分诊 |
| 交付物 | 可合并的 diff | 诊断结论 | 修复 PR | 告警工单 | 摘要 / 建议 |
| 准确率实测 | **无独立评测** | 31/38 | 34/38（自评） | — | 有生产数据 |
| 速度实测 | — | 中位 45s（最快） | 中位 154s | — | — |
| 自托管 + 自带模型 | ✅ | ✅ | ✅ | ✅ | ❌ 厂商锁定 |
| 账号门控 | ⚠️ 交互 REPL 强制登录 + TTY | ❌ | ❌ | ✅ 需注册 | ✅ |
| 评测环境 | ✅ **在做**（CloudOpsBench 已集成）| ❌ | ❌ | ❌ | ❌ |
| License | Apache-2.0 | Apache-2.0 | — | Apache-2.0 | 商业闭源 |

### 差异化护城河

**技术护城河（中等偏强，非独占）**：「CI 修复语义 + 确定性归因 + 评测环境」三件套。确定性归因不是谁都能快速抄——它需要吃透 GitHub Actions 的运行语义（`find_outages` 的注释就暴露了这一点：「GitHub 在最新 commit 有失败检查时把分支显示为红色，所以 outage 跟随 commit 而非 per-workflow 时间线：一个之后再也不运行的 workflow（路径过滤、改名、删除）不能在后续 commit 全绿后还让分支保持红色」）。评测环境是最有可能变成真正护城河的部分——SWE-bench 之所以有护城河，是因为它定义了一个可比的标准。

**工程护城河（强，但只对内）**：2446 个非测试 .py、13249 个测试、5 条 import 契约、CodeQL、per-PR p90 90s SLO、三阶段 CI、原子发布 + 签名技能。**这个工程质量在开源同类里罕见**——HolmesGPT 的规模小一个数量级。问题是它现在只保护自己，不构成对外部的壁垒。

**信任护城河（弱）**：自托管 + 数据主权是真实的差异化主张，但在「没有独立评测数据」的前提下说服力打折。

**生态护城河（弱）**：125 个集成目录是覆盖度优势，但外部评测明确指出「覆盖度不等于深度」；且 10 个月仍未形成稳固的外部 maintainer 层。

### 竞争风险

**最大风险是评测缺席。** HolmesGPT 和 Aurora 的实测数据都在对手手里，OpenSRE 一个都没有——外部对比评测（arvokas.io 收录 Aurora / HolmesGPT / K8sGPT / AURA / kagent / OpenSRE 六个 Apache-2.0 项目）**直接跳过了 OpenSRE**。这是唯一一个能单枪匹马改变竞争格局的缺口，而作者在 Issue #2074 里已经诚实记录了自己造 benchmark 比造 agent 更难：legacy adapter 把 AWS backend 挂在 `sources["aws"]` 而工具读 `sources["eks"]`，导致 State Snapshot 工具从未被调用、process metrics 全 0；旧 scorer 的 exact-match 太严，agent 正确诊断出 `incorrect_image_reference` 却得 0 分。**这两个 bug 本身就是「benchmark 比 agent 难造」的证据。**

**可复现性风险。** 安装器永远拉 `main` 最新构建，同一套安装命令在不同时间装出不同 agent；交互 REPL 强制要求「已登录账号 + TTY」，排除无人值守自动化和多数 CI 环境；Python API 无法从安装的二进制使用，必须 source checkout + 本地构建——「CLI 产品」与「可嵌入框架」两条线尚未收敛成一个干净的打包架构。任何严肃的第三方评测或企业落地都会先撞上这堵墙。

**自主度默认值的信任风险。** alpha 阶段 `/auto high` 是默认值（全部放行），且明确「intentionally no shell-command safety policy」。这对「数据主权」叙事是反讽——你控了数据，但没控 agent 动作。讽刺的是 Aurora 在审批门控上做得更好（`DEFAULT_AUTO_LEVEL = AutoLevel.HIGH` vs Aurora 内建审批门控）。唯一被无条件追问的工具是 `execute_python_code`（`ASK_AT_EVERY_AUTO_LEVEL_TOOL_NAMES`），理由是「生成的代码可能被不可信日志或告警内容操纵」。

**上游依赖风险。** `anthropic>=0.77.1`、`litellm>=1.106.2,<1.110.0`、`openai>=2.0.0` 全是大版本浮动，而 `defer_loading` 这类 beta 特性依赖 provider 版本——本仓库那条 `3345ad5b5` 提交就是 LiteLLM 1.109.1 拒绝了 mock stream 的 `finish_reason` 缺失，OpenSRE 修的是自己的 CI。

### 生态定位

**「AI SRE 的 SWE-bench」是唯一有想象力的定位**——不做更好的通用事故调查（打不过 HolmesGPT 的社区和实测），而是做**基础设施事故响应领域的标准评测基座**。如果 OpenSRE-bench 真的立起来，位置就从「另一个 agent」变成「这个领域的度量衡制定者」。

但目前是「基建先行、内容后补」：BenchmarkAdapter ABC 设计成 metric-agnostic，先把评测架子搭起来，再逐个把外部基准套进来。风险是架子搭好了没人往里灌数据。

## 套利机会分析

- **信息差**：不是「低 star 高质量」那类经典信息差——13.7k star 已经是充分发现的状态。**真正的信息差在评测环境这条副线**：社区关注度几乎全在 CLI 产品上，而 CloudOpsRE-bench / CloudOpsBench 适配 + 「AI SRE 的 SWE-bench」这条叙事还没被市场定价。想找「能抄的」人应该去看 `infrastructure/skills_registry/`（签名发布的自然语言制品）、`core/context_budget.py`（工具交换对驱逐）、`react_loop.py`（观察指纹停滞检测）——这三个是**任何工具型 agent 都能立刻搬走**的。
- **技术借鉴**：`ci_analytics/metrics.py` 的确定性归因、`importlinter` 分层契约 + 豁免台账、`docs/NAMING.md` 的词表化命名规约、`docs/interactive-shell-action-policy.md` 的决策反转记录——这四样今天就能用。`TurnRunner` 的「默认值即最常用路径」防漂移设计适合任何多入口 agent。
- **生态位**：填补了「SRE agent 只做诊断、不做修复」和「CI 修复工具没有评测」两个空白。有点讽刺的是，同赛道竞品（HolmesGPT / Aurora）反而有更硬的评测数据——OpenSRE 想做度量衡制定者，但自己还没被度量。
- **趋势判断**：仍在增长（11-02 到 11-21 涨了 1062 star），且发布节奏没减速（近 30 天 136 次提交、当天仍有提交）。后发优势有两条：一是编码 agent 成熟让它现在才做得成；二是 CI/CD 修复这个垂直没人认真做，有先占窗口。**但后发劣势同样明确**：所有实测数据都在竞品手里。

## 风险与不足

1. **产品面欠账**：README 说 CI/CD reliability，`pyproject.toml` 的 description 说 incident investigation from Slack/Grafana/Datadog——定位分裂，代码可证。
2. **评测缺席**：如上，唯一能单枪匹马改变格局的缺口。
3. **不可复现**：main channel 滚动二进制 + 强制账号 + TTY + Python API 必须 source checkout。
4. **自主度过高**：alpha 默认全放行、无 shell 安全策略。
5. **集成深度未知**：「60+ 集成」是覆盖度不是深度——建议接入前逐个跑 `opensre integrations verify`。
6. **维护层不稳**：13.7k star、10 个月，仍靠公司雇员轮值 + 现金悬赏招募 maintainer。
7. **缺 CHANGELOG 与 examples**：用 GitHub Releases 代替 CHANGELOG；无 `examples/` 目录（替代物是 `docs/` 下的 .mdx 指南 + `ci_repair_demo/` 这个可运行的合成故障 demo）。
8. **上游版本脆弱**：大版本浮动依赖 + provider beta 特性耦合。

## 行动建议

- **如果你要用它**：先跑 `opensre integrations verify` 逐个验证你要用的集成，别信「60+ 集成」的覆盖率数字。确认你有至少一个可用的 coding agent（Claude Code / Codex / Cursor / Pi 任一）——没有的话它修不了代码。**必须用 `opensre ask "<question>"` headless 模式而不是交互 REPL**，除非你的环境确实有 TTY。安全上，把 `/auto` 从默认的 `high` 降到 `med` 或 `low`，尤其在第一次跑的时候。把这个 alpha 当成「值得试用的原型」而不是「能进生产的工具」——作者自己都还没被独立 benchmark 跑过。
- **如果你要学它**：按这个顺序读，每个都是可独立迁移的：
  - `integrations/github/tools/ci_analytics/metrics.py` — 确定性归因（最值得抄）
  - `infrastructure/turn_host/turn_runner.py` — 唯一回合内核 + 防漂移默认值
  - `infrastructure/safety/masking/rules.py` — 可逆 masking 的边界处理
  - `core/agent/react_loop.py` — 观察指纹停滞检测
  - `core/context_budget.py` — 工具交换对驱逐 + token 估算校准
  - `core/agent_harness/prompts/skills/AGENTS.md` — 技能卡契约（信息密度极高）
  - `docs/interactive-shell-action-policy.md` — 决策反转记录（反模式档案）
  - `docs/NAMING.md` — 命名词表与反模式
  - `.importlinter` — 分层契约与 15 条技术债豁免
  - `integrations/github/tools/ci_repair_demo/seed.py` — 合成故障床
- **如果你要 fork 它**：先补上它最缺的两样——**一份可信的独立评测**（把 CloudOpsBench 适配器跑通、修掉 `sources["aws"]` vs `sources["eks"]` 那个 bug、放宽 scorer 的 exact-match），以及**一条收敛的定位**（把 `pyproject.toml` 的 description、README、仓库 topics 全部对齐到 CI/CD reliability，砍掉遗留的事故调查叙事）。这两件做完，fork 的价值会远高于直接贡献。另外把安装器改成固定版本（配 `uv.lock` 或 PyPI 发布），并给交互 REPL 提供无账号的本地路径——这是所有第三方评测的入场券。

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | 未收录（`https://deepwiki.com/tracer-cloud/opensre` 持续返回 429/无内容）|
| Zread.ai | 未收录（`https://zread.ai/tracer-cloud/opensre` 返回 HTTP 403）|
| 关联论文 | OpenSRE 本身无 arXiv 论文；方法论锚点为 [SWE-bench (arXiv:2310.06770)](https://arxiv.org/abs/2310.06770)，已集成 [CloudOpsBench (arXiv:2603.00468)](https://arxiv.org/abs/2603.00468) 及其 HF 数据集 `tracer-cloud/cloud-ops-bench-dataset`，参考 [OpenRCA (ICLR'25)](https://github.com/microsoft/OpenRCA) 与 RCAEval (FSE'26) |
| 在线 Demo | 无公开在线 Playground。可本地跑 `opensre setup --dev` 起本地 web app（http://localhost:3000），或跑合成故障 demo `integrations/github/tools/ci_repair_demo/` |
| 官网 | https://opensre.com |
| 关键 Issue | [#2074 Benchmark（CloudOpsBench）](https://github.com/Tracer-Cloud/opensre/issues/2074) · [#344 招募 maintainer](https://github.com/Tracer-Cloud/opensre/issues/344) · [#1506 本机 agent 监控（已砍）](https://github.com/Tracer-Cloud/opensre/issues/1506) |
