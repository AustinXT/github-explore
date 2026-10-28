# GitHub推荐：JetBrains 的 agent IDE：把 104 份规范写成了源码

> GitHub: https://github.com/JetBrains/thinkrail

## 一句话总结

JetBrains 官方开源的 agentic IDE，把「规范」当成一等工程产物——104 份 `SPEC.md` 构成连通图谱，agent 通过工具读改它，每个并行 agent 住在独立的 git worktree 里，而宿主的铁律是「All of pi, nothing hidden」：绝不替引擎组装 prompt，绝不自己重算引擎的账。

## 值得关注的理由

- **规范即源码，不是文档即源码**：全仓改动最频繁的 Top 10 文件里有 **5 个是 `SPEC.md`**（合计 674 次修改），真正的代码热点只剩 4 个。更狠的是它有自研的 AST 级边界检查器——用 TypeScript compiler API 解析 import/export specifier，对照声明式允许边表判定违规，「模块纪律」不是口号而是 CI 门禁。
- **「不藏私」是一条被写成代码的承诺**：主流 agent IDE（Cursor / Claude Code）都在背后悄悄拼 prompt。ThinkRail 的原则是 `Expose, don't recompute`——成本、stats、模型可用性一律来自引擎的原始报告，宿主只允许「镜像 + parity 测试证明相等」，连错误上报都只带分类器，消息文本永不离开客户端。
- **一份罕见的「反向依赖账本」**：`pi-compatibility.md` 逐条记录宿主为弥补引擎缺失 API 而做的每处妥协，写明「什么条件下可以删掉这个适配」以及必须跑哪些测试。这把「依赖一个每日发破坏性 release 的上游」这件最危险的事，变成了可审计的工程资产。
- **对多 agent 并行的一个通用解**：worktree 隔离 + turn 级变更快照（用 scratch `GIT_INDEX_FILE` 拍 tree，不碰用户的 HEAD/index/reflog），让「这一轮 agent 到底改了什么」成为宿主可独立观测的事实，而不是 agent 的自述。

## 项目展示

![ThinkRail workbench：左侧工具栏 + 项目面板，中间的 pi 会话与工具步骤，右侧 diff，右上 Specs 树](https://raw.githubusercontent.com/jetbrains/thinkrail/main/.github/readme-assets/workbench-light.png)
*主工作台：左侧项目树、中间引擎会话与工具步骤、右侧 diff 审阅区，右上角是 Specs 图谱入口*

![从右侧 edge rail 打开的 Specs 工具，项目 spec 树 + 目标 spec 正文](https://raw.githubusercontent.com/jetbrains/thinkrail/main/.github/readme-assets/specs-light.png)
*Specs 面板：左侧 spec 树 + 右侧 spec 正文，规范是 agent 可导航的对象而非只读文档*

[官网 /vibecoding 页：可交互的 agent 会话演示 + 并行 worktree 示意图 + spec 校验输出](https://thinkrail.ai/vibecoding)
*在线 Demo：真实可交互的 agent 会话（可选模型、展示 agent 读 spec / 查路由 / 实现 endpoint / 跑测试 / 暂停提问的完整动作序列），另有 Parallel workspace map 与 `✓ Spec validation passed. Ready to spawn agent.` 的校验输出示例*

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/JetBrains/thinkrail |
| Star / Fork | 4,477 / 236 |
| Watcher / Open Issue / Open PR | 12 / 186 / 46 |
| 代码行数 | 315,832（语言：TypeScript 75.0%、TSX 19.0%、JSON 4.3%、CSS 1.3%） |
| 许可证 | Apache License 2.0 |
| 注释比 | 8.6%（代码:注释 = 11.6:1） |
| 运行时依赖 | **0**（16 个依赖全在 devDependencies，后端全靠 Bun 原生 API 自研） |
| 项目年龄 | 4.2 个月（2026-06-22 首次提交，2026-07-08 建库 → 2026-10-28 最新推送） |
| 总提交 / 贡献者 | 598 commits / 37 人（主作者 40.6%，前 5 人约 72%） |
| 开发阶段 | 密集开发（近 30 天 229 commits，近 90 天 454；10 月单月 213，为前四个月均值的 2 倍） |
| 开发模式 | 职业项目（周末占比 10.7%，深夜占比 14.0%） |
| 贡献模式 | JetBrains 内置团队主导 + 社区补丁（`jetbrains.com` 邮箱占约 31% 提交，`jetbrains-air[bot]` 自动提交） |
| 版本 | 125 个 tag / 100 个 Release，最新 `v0.3.0-nightly.8`，**尚无 1.0 正式版** |
| 热度定位 | 中等热度偏小众（3.7 个月 4,477 star，约 40 star/天） |
| 质量评级 | 代码 优秀（0 个 `: any`）/ 文档 优秀（104 份 SPEC.md + 42KB 架构文档）/ 测试 充分（642 个测试文件，测试/产品代码 ≈ 44%） |

## 作者视角：为什么存在这个项目

### 创始人/作者背景

OWNER 是组织账号 `JetBrains`（Netherlands，15.3 年老号，14,006 followers），README 顶部挂 incubator 徽章，官网 footer 署 InnovationHub——**这是 JetBrains 孵化器里的项目，不是产品线**。

真实开发者才是判断质量的关键：

- **`rsolmano`（Rinat S）**，提交邮箱 `rinat.suleimanov@jetbrains.com`，**JetBrains 正式员工**，仓库的第一个提交作者（`initial specs` / `idea folder` / `monorepo scaffold`），事实上的技术负责人。2024-08 才注册 GitHub，9 个公开仓库——典型的「工程师而非网红」。
- **`danyaberezun`（Daniil Berezun）**，537 次提交**居所有作者之首**，但用的是个人邮箱 `gmail.com`。2024 年才进入这个项目的贡献序列，是写代码的主力。
- `OLavrik`（Olga Lavrichenko）、`Julia.Shilova`、`Rustam Sadykov`、`Andrey Markin`、`Maciej Gorywoda`、`Iaroslav Postovalov` 等固定一批人。
- 外部贡献者里 `CommanderTvis` 质量最高——#428 的 WebSocket backpressure 根因分析就是他的，团队核心 Rinat S 直接回复「open a PR please」。

**这个团队的工程纪律有一个硬指标可以证明**：`AGENTS.md` 写明「Run `pi` in-process, never as a subprocess and never through a second agent runtime」。这句话不是文档装饰，它是 `packages/contracts` 里没有任何第二运行时依赖的原因。

### 问题判断

三个痛点写在 `goal-and-requirements.md` 的 Problem 段，每一条都很具体：

1. **并行 agent 在同一工作树里互相碰撞**——还撞用户自己的编辑；
2. **agent 的改动从 CLI 里很难审**——读 diff、对具体行评论、把反馈交回 agent；
3. **意图会蒸发**——聊天里做的决策随会话消失，下一次重新推导甚至自相矛盾。

**作者是怎么发现这个问题的？** 工程沉淀，不是学术延伸。Rinat S 写 0.2.0 的 blog 时说漏了嘴：「The agent finishes, says it's done, and I scroll the transcript trying to piece together what it actually changed. **That isn't a review. It's archaeology.**」——第一人称的自身痛点。

**为什么是现在，不是 2 年前？** pi 在 2026 年成了足够成熟的 harness（v1.4.0，daily breaking release），同时 JetBrains 有 IDE 背景却**没有**自己的 agent runtime——「做一个 pi 的 IDE 外壳」成了这个组织的天然位置。项目 2026-06-22 首提，4.2 个月 598 commits，到 10 月单月 213 次进入冲刺期。

### 解法哲学

**简单 vs 功能完整：选了「薄」。** 两条非目标被明确写进 `goal-and-requirements.md`（原文强调「Only these are excluded by decision」）：

1. **不做第二个 agent runtime**——禁掉 `claude-agent-sdk` 那一类东西，pi 独占 model registry / system prompt / skills / compaction / cost / session state；
2. **不做 ThinkRail 账号和登录 UI**——谁能访问 host 由网络决定（Tailscale ACL + 设备身份）。

**对比竞品，作者明确选择了不做什么：**

- 不用 tmux 做终端持久层（架构 Decision #12 给了 4 条拒绝理由：Windows 不可控的依赖、竞争的 tab 模型、env 传播断裂、poll 式捕获）；
- 不用 WebGL 终端渲染器（Decision #11：DOM 渲染器是触控支持的前提，WebGL 的 `dispose()` 会泄漏 WebGL2 context，对每 worktree 的终端 churn 是致命的）；
- 拒绝运行时动态加载扩展 bundle（React 单例 + 版本化 UI API + 安全故事先解决）；
- 拒绝「host 侧全局 platform adapter」这种预先抽象。

**性能 vs 易用性：选了「透明」。** 宁可让用户看到引擎的原始输出，也不做宿主侧的重算。

**开放 vs 封闭：开放但有护栏。** `pi-extensions/*` 打成 npm 包（`@thinkrail/pi-visualize`、`@thinkrail/pi-ask-user-question`），带 `provenance: true` 的 Trusted Publishing，且必须过「vanilla pi 兼容性门槛」——CI 里有一个专门的 job，在 **Node**（不是 Bun）下用 pi 自己的 loader 从 packed tarball 加载并真实执行工具。**「能脱离 IDE 用」是硬性发布条件。**

### 战略图景

**基础设施属性 > 核心产品属性**，但确实是 JetBrains 的核心战略动作，而且是**真开源（不是 open-core）**——Apache-2.0，runtime 依赖 0，无遥测强制，无付费墙。

商业化路径清晰，且它**故意不自己收钱**：`central-integration.md` 把 JetBrains AI 作为 provider 之一接入（走用户自己的 `central` CLI，走 AI 积分配额）；`apps/website` 是完整的公开站 + blog + `/vibecoding`，带 D1 存储做归因。

**姿态是「用 IDE 能力换取 agent 生态位」**：不收 token 费、不做账号体系，让 JetBrains AI 成为默认 provider 之一，同时把「JetBrains 出品」当作对 IDE 用户的信任背书。仓库挂在 incubator 下，说明它还在找形态。

**JetBrains 的 IDE 背景给了它三样别人没有的东西**：① 前端/渲染工程能力（`@pierre/diffs` + Monaco + Shiki + xterm.js + 12 种渲染器的资源渲染器矩阵，还有 `design-audit/` 按钮系统的 60 个样本矩阵 + 6 主题自动校验）；② spec-first 的工业纪律（IDE 厂商几十年的「活文档」文化被完整迁移到 agent 语境）；③ 国际化与可访问性的默认内建（UI 字符串全部走 `packages/locales/en.json` 的 key 目录，有 lint gate 拒绝硬编码 JSX 文本，用户往 `~/.thinkrail/locales/` 丢一个 `en.json` 就新增一种语言且存盘即生效）。

## 核心价值提炼

### 创新之处

**1. 「反向依赖账本」——把宿主对引擎的每一处妥协写成可审计的 removal gate（新颖度 5/5，实用性 5/5，可迁移性 5/5）**

`pi-compatibility.md` 不是「已知问题」列表，而是**能力账本**。每条适配写明：owner（哪个模块 spec 拥有它）、引擎的哪些私有事实让它必要（精确到 dist 文件和函数）、**removal gate**（什么条件下可以删）、以及必须跑哪些测试。里面写着：「A parity failure is evidence of drift, not permission to weaken the test」——parity 测试失败是漂移的证据，不是放松测试的许可。

典型条目：

- MCP 配置加载器是对引擎私有 `dist/core/mcp-servers.js` 的 port（因为引擎不导出 `loadMcpConfig`，且宿主提供的 `loadConfig` 会**整体替换**引擎的 loader），parity 测试把同一批 fixture 同时跑过引擎安装版的 loader 和宿主的实现；
- Anthropic SSE 分帧补丁（`patches/@earendil-works%2Fpi-ai@1.4.0.patch`）：不打补丁时，一个 CRLF 被网络分块切断的合法流和一个中途截断的流都会报不可重试的解析错误；补丁后前者成功、后者变成**可重试**的截断错误。每个版本升级都要跑 `anthropicStreamFraming.test.ts`，测试里的「defects the patch fixes」分组决定是删补丁还是移植补丁；
- `defaultModelPerProvider` 未导出，宿主镜像了一份并用 parity 测试钉住——上游一改，测试就红。

**适用场景**：任何「宿主依赖快速迭代的第三方引擎/SDK」的项目——嵌入 LLM SDK、编辑器内核、游戏引擎。

**2. 用 scratch `GIT_INDEX_FILE` 做无侵入 worktree 快照，实现 turn 级变更归因（4/5，5/5，4/5）**

`packages/server/src/git/snapshot.ts` 的 `snapshotWorktree`：把 index 复制到临时目录，`GIT_INDEX_FILE` 指向副本，`git add -A` + `git write-tree` 得到 tree oid，**用户的 HEAD、index、reflog 全不碰**。turn 开始拍一次、settle 时拍一次，两棵树的 diff 就是这一轮的真实变更。

这解决了 0.2.0「review the turn」的核心难题：靠 agent 自己的 tool call 统计不准——一条 shell 命令改的文件、格式化器、重命名都会漏。这个机制**能捕捉任何写入路径**，包括绕过宿主的 Bash 调用。

**3. spec 图谱作为 agent 可导航的对象（4/5，4/5，5/5）**

`packages/spec-graph/core/parse.ts` 定义 frontmatter 契约（`id`/`type`/`status`/`parent`/`depends-on`/`references`/`implements`/`covers`/`tags`），`graph.ts` 建双向邻接表并检测重复 id，`validate.ts` 检测悬空链接与 parent 环，工具面是 7 个 `spec_*`（`spec_grep`/`spec_get`/`spec_graph`/`spec_create`/`spec_update`/`spec_delete`/`spec_validate`）。

关键差异不是「有文档」，而是**图谱是可导航的对象而非散文**——文档里出现的 `[[architecture]]`、`[[module-pi-delegation]]` 是 id 引用，spec 之间用图连接，agent 可以读图、查环、加节点。而且 spec 是**手写的 source of truth，不是从代码反向生成的**。

**4. AST 级 monorepo 边界检查器（3/5，5/5，5/5）**

`scripts/check-module-boundaries.ts` 用 **TypeScript compiler API 解析 AST**（不是正则 grep），抽取每个源文件的 import/export specifier，对照声明式允许边表判定违规。它检查的不只是「A 能不能 import B」，还包括：manifest 里的 dependency 边、extension 的 web/server 两半交叉、extension-api 的 server 半泄漏进浏览器代码、浏览器安全源码里的引擎值导入（只允许 type-only）。错误信息精确到「creates forbidden apps/web -> packages/server edge」。

**5. 把「透明」做成可验证的不变量（4/5，4/5，4/5）**

成本、stats、session 状态、模型可用性一律来自引擎的报告，宿主不重算。代码里的体现是 `modelDefaults.ts` 镜像引擎未导出的 `defaultModelPerProvider` 并用 parity 测试钉住——**宿主的「自己算」被降级为「镜像 + 证明相等」**。同类还有 `subagentUsage.ts` 镜像引擎的 session-total loop，来对账崩溃的子会话。

**6. 可插拔的「能力协商」协议版本（3/5，4/5，4/5）**

不是「协议 v1/v2」，而是 40+ 个按能力递增的常量（`MCP_PROTOCOL_VERSION = 83`、`PROJECT_TRUST_PROTOCOL_VERSION = 81`、`TOOL_RESPONSE_PROTOCOL_VERSION = 93`……）。客户端从 `server.welcome` 里读版本号，就能精确知道 host 支持哪些能力，而不是做二元的老/新判断。

**7. tool-agnostic 的 human-in-the-loop「邮箱」（4/5，4/5，4/5）**

交互式工具契约按 `toolCallId` 键控，宿主从两处声明知道哪些工具在等：server 半的 `interactiveTools` 和 web 半的 `interactive: true`。**`contracts` / `agent` / `apps/web` 三层里从不出现任何具体工具名**——`ask_user_question` 只是这个契约的第一个客户端，不是特例。删掉某个扩展不需要动核心。

**8. 凭据掩码作为单一出口（3/5，5/5，5/5）**

`redactMcpText` 幂等、确定性，覆盖 URL userinfo、Bearer/Basic（任意大小写）、credential 命名的 `key=value`、已知 token 前缀（`gh[pousr]_`/`sk-`/`xox[abprs]-`/`glpat-`/`AKIA`）、32+ 位十六进制或 base64url 串。它套在**每一个引擎文本变成宿主 DTO 的位置**。

### 可复用的模式与技巧

| 模式 | 简述 | 适用场景 |
|------|------|---------|
| **能力账本 + removal gate** | 为每处对上游引擎的妥协写一条记录（owner / 依赖事实 / 删除条件 / 必须跑的测试），升级时逐条核对 | 依赖快速迭代的第三方引擎或 SDK |
| **scratch index 快照** | 用 `GIT_INDEX_FILE` 副本做无侵入快照，得到可审计的变更归因 | 需要对任意写入路径做行为审计的 agent 工具 |
| **hydrate-then-stream** | 客户端先读权威快照再订阅增量，永不假设自己「见过」事件 | 多端接入同一 agent 后端 |
| **AST 级依赖方向门禁** | 用 TS compiler API 判定模块间 import 是否合法 | 有强依赖方向的 TS monorepo |
| **精确 pin + 根 catalog 单点化** | 拒绝任何版本范围，让 lockfile 成为版本的唯一真相 | 上游每日发破坏性 release |
| **电平化流控** | 把边沿触发的 backpressure 改成「状态 + 定期 reconciler」 | 会话休眠/挂起的长连接终端 |
| **仅分类器的错误上报** | 只上报 type/code/自有 stack frame，消息永不离开客户端 | 有隐私承诺的客户端产品 |
| **spec 即源码** | 每个模块一份 SPEC.md，边界/契约变更必须同 commit 更新，**改动边界先改 spec** | 中大型 agent 协作项目 |
| **三 PR 交付律** | 扩展迁移拆成「新旧并存 → web 半 → server 半接线并删除旧包」，每个 PR 用户不可观察 | 已有用户的架构迁移 |
| **公开 post-mortem** | 在架构文档里直接写「Invariant 3 当前被违反，跟踪于 issue #287」并附事后分析 | 长生命周期项目 |

### 关键设计决策

**决策 1：worktree 隔离**
- 问题：并行 agent 互相碰撞 + agent 污染用户的主 checkout
- 方案：`packages/server/src/workspaces/workspaces.ts` 里 `git worktree add <path> -b <branch> --no-track <remoteBase ?? baseBranch>`，worktree 建在 `~/.thinkrail/worktrees/` 下（**不在项目里**，避免嵌套仓库干扰 git 语义）；`kind` 字段区分三种——「default」（项目目录本身，用户显式选择，永不自动进入）、「external」（用户已有的 worktree，就地挂载，ThinkRail 可以忘记但**永不修改**）、正常 worktree
- Trade-off：隔离是**路由，不是安全边界**——worktree 是同用户同凭据可达的兄弟路径。代价是每个 workspace 一份完整 checkout 的磁盘开销、跨 workspace 的语义冲突（两个各自合理的改动合并起来可能打架）、git 操作复杂度
- 可迁移性：**高**——这是任何「多 agent 并行」产品的通用解

**决策 2：thin host——宿主到底替引擎做了什么？答案是「几乎什么都不做，只做适配」**
- 问题：主流 IDE 的宿主会重算 cost、重算 stats、重组 prompt
- 方案：见上文创新点 1 的能力账本
- Trade-off：换来了「不与引擎竞争」和「引擎升级即收益」，代价是宿主背上了一批**跟随引擎版本走的不稳定适配**。这份账本就是为这种代价准备的证据链
- 可迁移性：**中**——模式可复制（能力账本 + removal gate），具体条目全是引擎特有的

**决策 3：turn 级变更快照**
- 问题：靠 agent 自述统计变更不准
- 方案：见上文创新点 2
- Trade-off：每次 turn 起止各一次全量 `git add` + `write-tree`，大树上有开销；换来的是变更归因不依赖 agent 的自述
- 可迁移性：**高**

**决策 4：barrel 作为唯一公开面 + AST 级检查**
- 问题：教科书式的 monorepo 边界纪律靠 code review 维持，会腐化
- 方案：`AGENTS.md` 规定「模块边界是分形的、每个子模块有 barrel 作为唯一公开面、兄弟模块只经 barrel 互相 import」，配合 `check-module-boundaries.ts` 与 `check:spec-surface`（把 spec 声明的公开面和实际 barrel 比对）双路把关
- Trade-off：自研静态分析工具需要维护，且比 ESLint 规则难懂；但能在 CI 里零成本执行，错误信息精确
- 可迁移性：**高**

**决策 5：信任边界——克隆的仓库能注入的东西必须逐条授权**
- 问题：陌生 git repo 可能带 `.pi/settings.json`、`.pi/extensions/`、`.pi/skills/`、committed skill alias、`.pi/mcp.json`，这些会直接影响 agent 行为
- 方案：两层。**per-project 信任**——仓库提供的 skill alias 和 `.pi/` 资源只在授予信任后加载（`projectTrust.ts` 的 `piResourceKinds` 枚举 7 类资源 + 祖先目录的 `.agents/skills`）。**MCP 逐条审批**——仓库定义的 MCP server 默认关闭，`fingerprintMcpEntry` 对定义文件里的原始条目做指纹，审批状态是 `approved`/`pending`/`changed`，**条目一变审批即失效**。授予状态存在 project record 上而不在 `.pi/mcp.json` 里，所以**仓库无法给自己预批准**
- Trade-off：首次使用每个 repo 都要过一次信任流程，摩擦明显；换来的是「clone 一个 repo 不会静默改变你的 agent 行为」
- 可迁移性：**高**

**决策 6：WebSocket 协议设计——为什么 `wsProtocol.ts` 是全仓耦合最高的文件**
- 问题：host 与 UI 是一对多、可重连、跨版本（UI 独立静态发布）的长连接
- 方案：三层结构——`WS_METHODS`（约 160 个请求方法常量）、`WS_CHANNELS`（26 个服务端推送频道）、`WsMethodMap`（每个方法的 params/result 类型映射）。`WsMethodName` 用 `SameUnion` 技巧保证 map 与 union 严格同步
- Trade-off：1135 行单一文件是全仓耦合最高的点，改任何方法都要碰它；换来的是客户端能精确知道哪些能力可用
- 可迁移性：**中**

**决策 7：终端 backpressure——从 issue #428 学到的教训**
- 问题：#428 报告 macOS 休眠后终端永久冻结。根因是**边沿触发**的流控：唯一解锁路径是 Bun 的 `drain` 事件，跨系统休眠丢失的 drain 永远不会重投，backpressure 闭锁永久卡死
- 方案：`packages/server/src/terminal/outputBatcher.ts` 把交付结果建模为三态 `delivered`/`backpressured`/`unavailable`（`terminalSend.ts` 把 Bun 的 `ws.send()` 返回值映射过来：>0 → delivered，-1 → backpressured，0 → unavailable）。修复方案是加一个 1 秒 reconciler 轮询 `getBufferedAmount() === 0` 来解锁——**把边沿触发改成电平触发**
- Trade-off：轮询有 1 秒延迟成本和一点常驻开销；换来的是不会永久卡死
- 可迁移性：**高**——「边沿触发流控 + 会话休眠」是所有长连接终端/流式 UI 的通用陷阱

**决策 8：依赖精确 pin + 根 catalog 单点化**
- 问题：pi 每天发破坏性 release，浮动版本范围是「活着的线」
- 方案：每个 manifest 的每个依赖都 pin **精确版本**（无 `^`/`~`/`>`/`.x`/`*`），跨切依赖在根 `workspaces.catalog` pin 一次并用 `catalog:` 引用。`scripts/check-catalog.ts`（pre-commit + CI）拒绝任何 range、任何 catalog 漂移、以及 react/react-dom 在 catalog 外解析。同时**规范里绝不重述版本号**——spec 写「验证了 dist 文件里的哪个函数、观察到什么规则，pi 升级时重新验证」，而不是「针对 v1.4.0 验证」
- Trade-off：每次引擎升级都要手工更新 catalog 并重跑全套 parity 测试，摩擦大；换来的是可复现构建
- 可迁移性：**高**

**决策 9：单引擎、无崩溃隔离——明确接受的取舍**
- 问题：pi 跑在宿主进程内，provider/agent 的致命故障会带走整个 host
- 方案：`AGENTS.md` 直说「Fatal provider/agent faults can take down the host; that lack of crash isolation is **accepted**」。对比 subprocess RPC 模式，换来的是零 IPC 开销、引擎状态的直接可读性
- Trade-off：一次 provider 崩溃 = 整个 IDE 掉线
- 可迁移性：**中**

**决策 10：扩展系统——server 半 / web 半分离 + 三 PR 交付律**
- 问题：要让 agent 自己造工具（README 的路线图），但运行时加载 bundle 有 React 单例、版本化 UI API、安全故事三个硬伤
- 方案：每个 extension 含引擎能力 + `./server` 半（宿主打包的 inline factory）+ `./web` 半（按 tool 名注册的渲染器），两半**永不互相 import，也不 import 宿主内部**——宿主拥有的状态只经显式 seam 到达 extension。交付律：每个 extension 以三个独立可交付 PR 到达（新包与旧包并存 → web 半迁移 → server 半接线并删除旧包），**每个 PR 都不改变任何用户可观察的行为**
- Trade-off：单个 extension 的上线成本 ×3；换来的是每个 PR 都可独立回滚
- 可迁移性：**高**

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | ThinkRail | Kiro（4,405★） | Orca（108,496★） | OpenSpec（73,225★） | oh-my-pi（36,903★） |
|------|-----------|----------------|-----------------|------------------|------------------|
| 形态 | 完整 IDE（Web/Desktop/CLI 三端） | 完整 IDE（云端会话） | 终端/多窗格编排台 | CLI 工具包 | pi 的 IDE 集成层 |
| Agent 引擎 | 单一（pi，进程内） | 闭源自研 | 任意（Claude Code 等） | 不限（提示词层） | pi |
| 隔离机制 | **git worktree 隔离** | 云端会话 | 无（终端格） | 无 | 无 |
| 规范形态 | **带 id/parent/depends-on 的连通图谱，agent 可读写** | IDE 内部流程 | 无 | 流程产物（人写） | 无 |
| 账号 / token | **无账号、无自有 token**，走用户本地凭据 | 闭源 credit 计费（~$19/月） | 无 | 无 | 无 |
| 宿主透明度 | **All of pi, nothing hidden**，不组装 prompt | 闭源不可见 | 部分 | 提示词层可见 | 部分 |
| 成熟度 | 0.3.0-nightly，**无 1.0**，无 winget/签名不全 | 商业化成熟 | 生态规模大 | 生态规模大 | 迭代快、社区驱动 |
| License | Apache-2.0（真开源） | 闭源 | 开源 | 开源 | 开源 |

### 差异化护城河

**技术 + 信任的组合，不是生态。**

- **技术护城河是「组织性」而非「生成性」的**——worktree 隔离、spec 图谱、hydrate-then-stream、turn 级变更归因、能力账本。这些都不难复制（好想法终究会扩散），但**复制需要同样的工程纪律**，而纪律需要时间。
- **信任护城河更硬**：JetBrains 品牌 + Apache-2.0 真开源 + runtime 依赖 0 + 「All of pi, nothing hidden」+ 无账号无 token + 错误只报分类器 + MCP 逐条审批。这是主流商业 agent IDE **结构性做不到**的——它们要收订阅、要托管凭据、要编排 prompt。对「我不想把代码交给某个 SaaS」的用户，这几乎是唯一的选项。
- **生态护城河最弱**：star 量级落后 Orca / OpenSpec / Spec Kit 一到两个数量级，npm 上只有两个 pi 包，两个 pi 扩展也是刚发布。生态位是「窄而深」。

### 竞争风险

1. **#907 LSP 缺失是最大的架构裂缝。** 用 Monaco 却不接语言服务器——没有跳转、补全、诊断。外部评论者的批评一针见血：「Users are left to manage things manually in pi's config files, **at which point the value of ThinkRail versus any other IDE comes into question**」。团队至今未回应。这条 issue 是 `enhancement` 且仍 open。
2. **单引擎单点。** pi 是外部项目，ThinkRail 为它背了 40+ 条适配——`pi-compatibility.md` 的整份账本就是这份风险的风险量化。引擎一次破坏性升级可能击穿多个 seam。
3. **无崩溃隔离的显式接受。** provider 一次崩溃带走整个 IDE。
4. **分发成熟度不足。** 无 winget（#477，社区自己建了非官方仓库）、macOS 未 notarize、Linux 未签名、125 tag / 100 release 却无 1.0。
5. **spec 与代码走同一套 CODEOWNERS，没有分开的审批门禁。** 外部评论已指出；`check:spec-surface` 只能比对导出面，无法验证叙述性断言。
6. **worktree 隔离不解决组合性冲突。** 两个各自合理的改动合并起来可能语义冲突——而模块级 `SPEC.md` 的不变量本可以充当缺失的裁判，但目前 spec 没有被强制作为合并仲裁。
7. **最危险的威胁来自上游而非竞品。** pi 生态自身在快速演进，`can1357/oh-my-pi` 已经做了「pi + IDE 集成」。如果 pi 官方或社区补上 IDE 层，ThinkRail 的存在理由会被直接削弱。

### 生态定位

**窄而深的细分市场。**「IDE + 持久化 spec 图谱 + git worktree 隔离 + 只跑一个引擎」这个四元组合目前**没有直接竞品**——oh-my-pi 有一半，Kiro 有一半，Orca 有工作区的一半。但它同时踩在两个红海（spec 工具、agent IDE）的交叉点上：**概念蓝海、流量红海**。

真实用户画像很清楚：**已经在用 pi 的人**。这是一个足够自洽的窄市场，不需要赢下整个 agent IDE 赛道。但这个市场到底有多大，仓库数据给不出答案——star 量级说明它还远未破圈。

**更广的生态价值在反向输出**：`@thinkrail/pi-visualize`、`@thinkrail/pi-ask-user-question`、`pi-spec-graph` 都是可以在 vanilla pi 里直接用的 npm 包。ThinkRail 把「pi 生态没有的东西」做成了开源补丁包，这比它自己的 IDE 本身更有扩散潜力。

## 套利机会分析

- **信息差**：**不构成 star 套利**。4,477 star 相对 315K 行代码 / 598 commits / 4 个月的比例已经偏高，是「热度已被充分定价」的典型 incubator 项目。真正的信息差在别处——**它的架构文档密度（42KB `architecture.md` + 104 份共 22,910 行的 `SPEC.md` + 一份反向依赖账本）相对 4,477 star 的比例，在 agentic IDE 里是断层式的**。同类项目（orca 108K star）根本没有这种文档资产。想学「怎么把架构纪律落成 CI 门禁」的人，比想用这个 IDE 的人多得多。
- **技术借鉴**：可直接搬走的有 6 件——① 能力账本 + removal gate（任何依赖快速迭代上游 SDK 的项目）；② scratch `GIT_INDEX_FILE` 快照（agent 行为审计）；③ AST 级 monorepo 边界门禁；④ 电平化 backpressure（长连接终端）；⑤ 精确 pin + 根 catalog + 检查器；⑥ 精确指纹的逐条审批（信任边界）。这 6 件都不依赖 JetBrains，也不依赖 pi。
- **生态位**：填补了「spec 工具」（OpenSpec / Spec Kit / GSD 全是提示词层）和「agent IDE」（Orca / Kiro / Cursor 全无持久化规范图谱）之间的空白。而且它把 spec 图谱本身作为可移植的 pi 包开源了出去——**在 pi 生态内部做基础设施，而不是跟 pi 生态抢位置**，这是最聪明的生态站位。
- **趋势判断**：符合两条明确趋势——「spec-driven development」已经有 GitHub 官方 topic（`spec-driven`、`spec-driven-coding`、`spec-driven-development`）和一批高星项目背书；「agent 多路并行」是所有 coding agent 的下一步。ThinkRail **有先发优势但没有体量优势**：概念领先一到两年，流量落后一到两个数量级。**它更像一个「方法论样板」而非「爆款产品」**——参考价值 >> 使用价值。
- **时间窗口提示**：README 明确下一步是「full extension support so ThinkRail can create the tools it needs based on how you actually work」。如果这条路线走通，「agent 自己造工具」会成为 agent IDE 的分水岭命题，而 ThinkRail 是目前唯一把这条路线写成文档的公开项目。

## 风险与不足

- **产品成熟度尚早**：31.5 万行代码、100 个 Release，却**没有一个 1.0 正式版**。语义化版本 + nightly 双通道意味着下游几乎无法写依赖约束。文档站还是「Coming soon」。
- **LSP 缺失是硬伤**：用 Monaco 却不接语言服务器，用户得手工在引擎配置文件里挂 LSP 扩展，而宿主 UI 还不认识自定义扩展、也不帮安装（#497）。这条 issue 至今 open、无官方回应。
- **崩溃隔离被显式放弃**：进程内跑引擎意味着 provider 致命故障会带走整个 IDE。这是性能换来的，但用户在生产环境会真切感受到。
- **Bun 单运行时锁定**：runtime 依赖 0 听起来是优点，实际上是把全部后端能力押注在 Bun 原生 API 上。`bun.lock` 被改了 100 次，依赖面频繁调整。迁移成本极高。
- **注释率 8.6%，阅读门槛被转移**：低注释率是有意的（`AGENTS.md`：「Comments are near-zero … rationale and narrative belong in the owning spec」），这在有 22,910 行 SPEC.md 的前提下成立，但**对外部读者意味着「读懂代码前必须先读 spec」**，抬高了贡献门槛。
- **没有 benchmark、没有使用数据**：两个独立外部评测都指出这一点，官方也未提供任何量化效果数据。这是一个**方法论驱动、尚未用数据证明效果**的产品。
- **规范自身的 drift 风险**：外部研究（arXiv 2026-10）直接挑战 spec-driven 的核心假设——「implementation-heavy specs decay」，因为 spec 通常在实现**之后**才与代码比对。ThinkRail 的 `check:spec-surface` 只比对导出面，管不了叙述性断言的漂移。**它既是这套方法论最有力的实践者，也是最有力的反例候选者。**
- **组合性冲突未解**：worktree 隔离解决的是「物理碰撞」，不是「语义碰撞」。两个各自合理的改动合并起来可能打架，而模块级 spec 的不变量本可以当裁判，但目前没有强制。
- **分发链短板**：macOS CLI 未 notarize、Linux 产物未签名、Windows 连 winget 包都没有。对一个 4,477 star 的 JetBrains 官方项目来说，这在工程成熟度叙事上是个刺眼的缺口。

## 行动建议

- **如果你要用它**：
  - **先确认你已经在用 pi**，且愿意接受「单一引擎 + 每 agent 一个 worktree」这两个硬约束——如果你的日常是 Claude Code / Cursor，ThinkRail 帮不了你。
  - **别当生产主力**，当「可审的探索环境」用：它的价值在 turn 级 diff 审阅和 spec 沉淀，不在吞吐。
  - **接受没有 LSP**——这是当前最大的体验缺口，团队至今未回应 issue #907。做纯文本/配置类工作无所谓，做大型 TS/Java 项目会很痛苦。
  - 建议从 [官网 /vibecoding 的可交互 Demo](https://thinkrail.ai/vibecoding) 起步，而不是 clone 源码。
  - 目标用户若是 Kiro 或 Spec Kit 的用户，**迁移成本不低**：Kiro 的用户要重新学引擎的心智模型，Spec Kit 的用户要重建 spec 习惯（且格式不兼容）。

- **如果你要学它**：**按这个顺序读，四个文件顶一万行代码**
  1. `goal-and-requirements.md`（9KB）——产品目标、6 条原则、**Non-goals 段**（作者明确不做什么，这是全仓库最有价值的一段）
  2. `architecture.md`（42KB）——23 条架构决策 + invariants，含每条决策的拒绝理由
  3. `pi-compatibility.md`——**反向依赖账本**，这是全网同类项目里几乎找不到的样本
  4. `AGENTS.md`——仓库级不变量，以及「模块边界先改 spec」的纪律
  - 然后直接看这四个实现：
    - `packages/server/src/git/snapshot.ts`（scratch index 快照，可审计归因）
    - `packages/server/src/terminal/outputBatcher.ts` + `packages/server/src/host/terminalSend.ts`（backpressure 三态模型）
    - `packages/spec-graph/core/parse.ts` + `graph.ts` + `validate.ts`（spec 图谱）
    - `scripts/check-module-boundaries.ts`（AST 级依赖门禁）
  - 再看 `packages/server/src/agent/projectTrust.ts` + `packages/server/src/agent/mcp/`（信任边界）和 `packages/server/src/agent/toolResponses.ts`（tool-agnostic 交互契约）。
  - **别先读 `apps/web`**——它占了 5,436 次目录修改但不是这套方法论的精华所在。

- **如果你要 fork 它**：**先评估你要不要换引擎**。fork 的最大成本不是那 31.5 万行代码，而是 `pi-compatibility.md` 里那 40+ 条适配——它们全部绑死在引擎的私有实现细节上。如果换引擎，这份账本要从零重写。**具体可改进的四个点**：
  1. **补 LSP**：#907 里外部贡献者已经指出了现实解法（`pi-lsp-extension`），这是当前回报最高的改动；
  2. **把 spec 审批与代码审批分开**：spec 与代码现在走同一套 CODEOWNERS，外部评论已指出这是缺口，加一道独立的 spec owner 门禁能显著降低 drift；
  3. **收敛版本策略**：nightly 通道（`v0.2.0` 单独烧了 34 个 nightly）让下游无法写依赖约束，加一条稳定的 `latest` 通道成本很低；
  4. **补分发**：winget + macOS notarize + Linux 签名，是把 4,477 star 转化成真实用户的最短路径。

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | 未收录（deepwiki.com/JetBrains/thinkrail 返回 429 / 安全检查，未能确认收录） |
| Zread.ai | 未收录（返回 403 / Cloudflare 挑战，无法验证） |
| 关联论文 | 无直接论文。倒有一篇 **arXiv 2026-10 的研究直接挑战 spec-driven 的核心假设**（implementation-heavy specs decay，spec 通常在实现之后才比对而产生 drift），值得对照阅读 |
| 在线 Demo | [thinkrail.ai/vibecoding](https://thinkrail.ai/vibecoding)（真实可交互的 agent 会话 + 并行 worktree 示意图 + spec 校验输出） |
| 自建知识入口 | **仓库本身就是它自己的 DeepWiki**——spec 图谱 + `architecture.md`（42KB）+ `goal-and-requirements.md` + `pi-compatibility.md` + `AGENTS.md` + `design-audit/` |
| 官方博客 | 5 篇（introducing → workspaces → SDD → pi philosophy → 0.2.0「review the turn」） |
