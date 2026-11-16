# GitHub 推荐：12.5K star 的 AI 评审层：全仓第二热的文件是一份给 AI 看的规约

> GitHub: https://github.com/backnotprop/plannotator

## 一句话总结

Plannotator 给 11 个主流 AI 编程客户端装上一层统一的「人类评审面」——agent 提计划、出 diff 时本地浏览器自动弹出，人做行内批注和批准/驳回，结构化反馈直接回流成 agent 的下一轮输入，形成闭环而不是单向审阅记录。

## 值得关注的理由

1. **它填的不是「再造一个 agent」，而是「人和 agent 之间那层一直空着的东西」**。Claude Code、Codex、OpenCode 各自都有 plan 审批，但都是纯终端文本，没法行内批注、没法看 diff、每家语义还不一样。Plannotator 用一套界面、一个反馈格式，把 11 个异构宿主统一了——README 里那句「One installer covers almost every agent」就是它的全部定位。
2. **全仓第二热的文件不是代码，是 `AGENTS.md`**。它被改了 604 次，排在 `packages/inbox/inbox.css`（901 次）之后、所有实现文件之前，末尾一条是「commit / tag / release note 一律不带 AI 署名」。把「与 agent 协作的规则」当一等工程资产维护，这在开源项目里极其罕见。
3. **它把「开源版和商业版共用一套 UI」这个老大难，用 seam 模式结构化地解决了**。30+ 个模块级单例 + setter 做后端注入点，默认值必须复刻现状行为；ADR-005 甚至写下了「Singletons 在 SSR 下是错的，但这里就是我们会重新考虑的确切条件」——把决策的失效条件一起写下来，比写「这个决策是对的」有价值得多。

## 项目展示

![Plannotator banner](https://raw.githubusercontent.com/backnotprop/plannotator/main/.github/assets/banner.webp)
项目主视觉：本地优先的 AI 评审面

![Plannotator Inbox（桌面 + 手机双视图）](https://raw.githubusercontent.com/backnotprop/plannotator/main/.github/assets/inbox-light.webp)
2026 年 10 月起的主战场 Inbox——多个 agent 的会话聚合成一个收件箱

![Code review with file tree and side-by-side diff](https://raw.githubusercontent.com/backnotprop/plannotator/main/.github/assets/review.webp)
代码评审视图：文件树 + 左右分栏 diff + 行内标注

![Guided review chapter: overview + annotatable diff](https://raw.githubusercontent.com/backnotprop/plannotator/main/.github/assets/guided-review.webp)
Guided Review：agent 把 diff 按「核心 → 后果 → 胶水」分章，把注意力放在最该看的地方

![Annotate UI with inline annotations](https://raw.githubusercontent.com/backnotprop/plannotator/main/.github/assets/annotate.webp)
行内标注：选中文本直接打标，支持 HTML artifact 与运行中的页面

[Plannotator Inbox demo 影片](https://plannotator.ai/assets/inbox-film.mp4)

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/backnotprop/plannotator |
| Star / Fork | 12,505 / 1,225（fork 率 9.8%） |
| 许可证 | Apache-2.0 OR MIT |
| 代码行数 | 1,246,977（TypeScript 62.6% + TSX 29.3% + JSON 4.5%；注释率 18.3%，6,621 个文件） |
| 项目年龄 | 10.6 个月（首次提交 2025-12-27） |
| 开发阶段 | 密集开发（近 30 天 8,213 次提交，占全生命周期 83%） |
| 贡献模式 | 独立开发（作者一人占 96.9% 贡献，Bus factor = 1；203 个 commit 作者 / 30 位 API 贡献者） |
| 热度定位 | 大众热门（12.5K star，但直接竞品仅 1.3K——细分赛道里的领跑者） |
| 质量评级 | 代码[优秀] 文档[优秀] 测试[充分] CI[完善]；无 linter/formatter 配置，缺根级 CHANGELOG |

## 作者视角：为什么存在这个项目

### 创始人/作者背景

Michael Ramos（backnotprop），纽约，独立开发者，GitHub 账号 12.6 年，163 个公开仓库，1741 粉丝。bio 写着「day to day is complex critical systems, mostly involving AI」。

他的履历有个清晰的转向：早期在大规模政府机构的 K8s/GKE 上做 transformer 训练相关基础设施，做过 GPU 集群和 worktree 工具（worktree-aliases），近两年明显转向 AI agent 工具链——pstack、prompt-tower、rg_history，还参与过 eqtylab/agent-console 这类 agent 可视化项目。

这个背景直接塑形了 Plannotator 的设计口味：**在可控的进程边界内承认异质性**（Bun 跑不了 node-pty 就换 Node sidecar，而不是强行统一）、**把决策写下来**（ADR 体系）、**多写者下的序号单调与崩溃恢复**（Inbox 的 append-only 日志）。这不是一个「产品经理想了个点子」的项目，是一个系统工程师把自己的工程习惯整体搬过来的项目。

### 问题判断

作者看到的不是「agent 写得不好」，而是「**我和 agent 之间的带宽不够**」。每次 plan 评审都要在终端里滚动、复制粘贴行号、手写反馈——人类的注意力被终端这个纯文本介质卡住了。他把这当作**接口问题**而非**模型问题**来解。

时机为什么是现在？三条线在 2026 年中汇合：

1. **Claude Code 的 hook 机制成熟了**，`PermissionRequest` matcher 可以按 `ExitPlanMode` 精确拦截，「拦截 agent 生命周期中的特定事件」第一次变得可行；
2. **多 agent 并行成为常态**（Claude Code / Codex / OpenCode / Gemini / Copilot / Cursor……），单 agent 内部的评审流不再够用，需要一层 agent-agnostic 的中间层；
3. **agent 的产出从「代码」扩展到「计划、决策、原型」**。而计划比代码更需要人类判断——代码可以靠测试兜底，计划错了整个方向就废了。

作者的时间线本身就是方法的产物：2026-06 建 ADR-0001 记录架构决策，2026-07 转向产品化，2026-08 写下 ADR-007（可移植导出），2026-10 转向 Inbox。

### 解法哲学

四条不可动摇的铁律，写进 `AGENTS.md` 的 Hard rules 第一节：

1. **Never compromise UX.**「开源产品必须 work well and feel like magic，不是企业关键系统。不要为防御性理由加摩擦：不要额外的门禁、确认、owner-only 检查、警告或让产品更难用的设置。当一个安全想法会损害 UX 时，先问 owner。」——这条把「安全 vs 好用」的价值排序**明确反转**于常规企业工程直觉。
2. **Reuse, not copies.** 同一能力必须多 surface 共用一套组件与状态。ADR-006 直接写「Annotation parity is a hard constraint」。
3. **隔离风险边界。** 不在主进程里做危险的事，失败必须优雅降级。
4. **先写决策再写代码。** ADR → research SPIKE → implementation spec 三层文档体系，每个决策标注日期、状态和 Context-Decision-Consequences。

**明确不做什么，比做什么更能说明取舍**：

- **不做 SSR**。ADR-005 写明：模块级单例在 SSR 下是错的，但「Plannotator 和 Workspaces 都不做 SSR，**如果将来加 SSR 那就是引入 Provider 的触发条件**，在那之前不付这个复杂度」。写下 revisit condition 而非默认选 Provider，是罕见的克制。
- **不做「以前的 guides」列表**（ADR-007 D6：「一个 guide 一次，不是功能，只是别把输入扔掉」）。
- **不做自动上传分享链接**，直到加密 + 密文托管契约落地（ADR-007 D11 明确列为 out of scope）。
- **不重写 UI**。ADR-005 记录了一次真实失败：曾尝试 from-scratch 重实现 UI，**把应用搞坏并被回滚**；PR #957 期间分支被 rebase 了 4 次，fork 方案已经落后 4 个同步点。

### 战略意图

**位置**：核心产品是 Inbox——「the missing review layer between you and multi-agent work」。annotate / code review / guided review 是围绕它的多个入口。

**商业化分层非常清楚**：① 开源本地版（MIT OR Apache-2.0）；② `guides.show`（Cloudflare Worker + R2，托管可移植 guide 与加密分享链接）；③ `apps/relay`（Cloudflare Worker + Durable Object，手机端中继）；④ **Workspaces**（商业托管协作层，官网标「Workspaces soon」+ waitlist）。

**开源策略是 open-core，但核心 genuinely open**——`@plannotator/core`（browser-safe 零依赖）和 `@plannotator/ui` 都发布到 npm，商业 Workspaces 复用同一套 UI 自己接后端。反向的操作也有：`@plannotator/references` 是**从商业 Workspaces 仓库反向切出来的**，`PROVENANCE.md` 逐文件记录了来源路径、last-touched commit hash、删改内容、携带的测试用例。

商业层做的是**托管、多租户、身份、实时协同、存储**——这些恰好是 seam 抽象允许宿主替换的部分。这是一个设计得非常干净的 open-core 边界：商业版没有阉割任何开源功能，反而是把「商业代码与开源代码同源」的信任问题用 PROVENANCE 账本解决了。

## 核心价值提炼

### 创新之处

按新颖度 × 实用性排序：

1. **Seam 模式：模块级单例 + setter 的后端注入点**（新颖度 4/5，实用性 5/5，可迁移性 5/5）
   每个 UI↔后端接触点是一个可替换的模块级实现 + setter + reset，默认值**复刻 Plannotator 的字面行为**。`configurePlannotatorUI()` 是唯一前门，一次性注入。现已 ship 30+ 个 seam：storage / identity（含 `isEditable`）/ imageSrcResolver / uploadTransport / docPreviewFetcher / fileTreeBackend / aiTransport / skillCatalog / webmcp / mathRendererLoader / commentCard 等。配套 `*.seam.test.tsx` 证明「默认行为不变 + 宿主覆盖生效」。`@plannotator/shared` 用 one-line shim（`export * from '@plannotator/core/x'`）re-export，使得**约 99 个内部 import 点一行未改**——用的是 `git mv` 而非 copy。

2. **版本由内容决定的严格快照格式**（4/5，4/5，5/5）
   快照带 version N **当且仅当**它含有只有 vN 才有的字段——所以旧 reader（严格拒绝未知字段）永远不会被递给它读不懂的东西。当前已演进到 version 1-5，解析器 `strict()` 在每一层拒绝未知字段，每版都有 fixture + 兼容性测试。

3. **一个 renderer 两种宿主**（3/5，5/5，5/5）
   把整条 guide 渲染链（`GuideView → GuideSectionCard → GuideFileCard → GuideViewportManager → AllFilesCodeView`）搬进 `@plannotator/guide-viewer`，应用内和导出后引用同一份代码。作者的原话：「**No visual drift is structural, not a promise.**」

4. **HKDF 用途隔离的零知识 relay**（4/5，4/5，4/5）
   从配对 secret 用 HKDF-SHA256 + deviceId 盐派生 4 个**用途隔离**的 key：`key`（下行）、`upKey`（上行，「so the relay cannot reflect one direction's envelope into the other」）、`collapseKey`（push collapse id 的 HMAC，「一个 envelope key 不该干两件事」）、`relaySecret`（bearer，relay 只存它的 SHA-256）。Durable Object 里**永不存正文或密钥**。

5. **`serverSession` nonce 抗陈旧页**（4/5，4/5，5/5）
   每个 server 进程启动时发一个随机 nonce，页面加载时拿到 payload，每次决策 POST 时回传；不匹配就 409 `session_mismatch`，**在认领或结算任何东西之前**。解决「固定端口 / 随机端口复用时，旧标签页批准了另一份文档」。这件事很少有人做。

6. **撕裂行容忍的 append-only 记录日志 + seq 单调**（4/5，5/5，5/5）
   每行是记录的**完整快照**（不是增量 patch）；读时跳过解析不了的行；向撕裂的文件追加前先补一个换行，让碎片保持为独立的不可读行；删除时重写整个文件（temp → rename）并把最高 seq 记进 `seq.json`，让已经越过它的 agent 游标**永远看不到这个号被重发**。

7. **`lettersByCode` 快捷键的跨键盘布局回退**（4/5，3/5，4/5）
   字母绑定在输入字符超出 A-Z 时按物理键 `event.code` 匹配，让西里尔/希腊/希伯来布局下字母键仍可用；但标点、dead key、未识别键**永不回退**（避免误触发）。

8. **Worker pool 的「活探针 + 4 秒放弃」降级**（5/5，3/5，3/5）
   从 `file://` 打开的文档与 CDN 是不同 origin，浏览器对 blob worker 的支持各不相同且异步失败。作者用**每次页面加载的活探针**发现可用构造方式（Chrome 拒绝 `file://` 的 blob *module* worker 但接受 classic），pool 4 秒内起不来就丢弃并回退主线程渲染——「一个死掉的 pool 永远不能留下空 diff」。

9. **`@plannotator/references` 的反向开源提取与 PROVENANCE 记账**（4/5，3/5，4/5）
   从商业仓库切出读侧代码进开源仓库，逐文件记录来源路径、commit hash、删改内容、携带的测试。所有 `src` 文件保留两行 provenance 注释。

10. **测试即规约**（3/5，4/5，5/5）
    文档有 CI 门禁（`tests/agents-md-size.test.ts`：超预算 / 链接失效即失败）；测试哲学写进硬规则——「**A test must guard a behavior that can actually regress. Before writing one, name the failure it catches; if you can't, don't write it.**」，并明确禁止把散文文案快照化。

### 可复用的模式与技巧

1. **Seam 模式**（模块级单例 + setter + reset，默认值 = 现状行为）——适用场景：OSS 内核 + 商业宿主；多后端可插拔。**配套铁律**：未经人在浏览器确认 parity 前不删工作代码。
2. **版本由内容决定的严格格式**——适用场景：配置格式、导出物、跨版本协议；目标是「老 reader 永不见新字段」。
3. **一个 renderer 两种宿主**——适用场景：应用内视图 + 可分享静态物。
4. **三层守卫：Host allowlist → Origin 写守卫 → session nonce**——适用场景：本地 HTTP server 的浏览器暴露面。
5. **单写者 + append-only + 全量快照行 + 撕裂容忍 + seq 单调 + 删除 temp→rename**——适用场景：本地优先状态存储、agent 消息存储、需跨机器同步的本地状态。
6. **HKDF 用途隔离 + 上下行分离 key + fragment 传密钥 + 服务端只存密文**——适用场景：零知识托管、推送中继、分享链接。
7. **优雅降级三件套：能力探测 → 手动旁路 → 明确的能力表**——适用场景：N 个语义不一致的宿主集成；不追求统一拦截。
8. **Node sidecar 隔离运行时边界 + 父进程死亡管道 + 失败禁用面板**——适用场景：运行时能力缺失（PTY / 原生模块 / GPU）时的架构降级。
9. **快捷键注册表**（解析器 + 格式化器 + 分发器 + 校验器 + 平台覆盖 + 按物理键回退）——适用场景：多 surface 桌面/浏览器应用。
10. **三层文档体系 + 逐条可追溯的 verification matrix**——适用场景：单人主导但需要「可审计」的大型项目。
11. **「给 agent 读的规约文档」分层路由 + CI 门禁**——适用场景：AI 参与开发的高频迭代仓库。
12. **「先命名失败再写测试」+ 禁止散文快照 + agent 指令 clean room 评估**——适用场景：任何有大量 UI 文案的仓库。

### 关键设计决策

**决策 1：Seam 模式做后端注入**
- 问题：商业 Workspaces 需要 Plannotator 的文档 UI，但有自己的存储、身份、上传、实时通道。fork 会持续落后（PR #957 期间 rebase 4 次），from-scratch 重写**直接把应用搞坏并被回滚**。
- 方案：每个接触点是一个模块级变量 + setter + reset，默认值复刻现状行为；`configurePlannotatorUI({...})` 是唯一前门。
- Trade-off：牺牲了 **SSR 正确性**（模块级全局在多用户服务端渲染下会串号）。作者接受了这个代价，并**写下了明确的 revisit condition**：加 SSR 时引入 `<PlannotatorUIServices>` provider，`configurePlannotatorUI` 退化为兼容 shim。
- 可迁移性：**高**。这是「同一份 UI 服务多个宿主」的标准解。

**决策 2：可移植 Guide 格式 = 严格版本化 + 纯函数导出 + 内容寻址不可变**（ADR-007）
- 问题：早期分支 `guided-review-html-export`（从未合并）试图把整个 review app（17-18 MB）打进 HTML，或引用一个可变的 `v1/` viewer，且只能导出内存里的当前 guide。两个属性都与目标冲突。
- 方案：**D1** 导出物大小只跟 diff 走，不打包应用，对 diff 本身不设上限（「拒绝的是应用基线，不是大 diff」）；**D5** 版本由内容决定的严格自描述格式；**D2** 一个 renderer 两种宿主；**D6** 在 guide job 启动时捕获 diff（「guide 描述的是它生成时所针对的 diff」）；**D8** `/v1/` 下每个文件内容寻址、永不覆盖，HTML pin 住确切 viewer build（hash + `integrity`），高亮在 worker pool 里跑、4 秒起不来就回退主线程；**D9** 导出是纯函数 `(snapshot) → HTML`，三个调用方；**D11** 默认加密上传，密钥只在 URL fragment。
- Trade-off：放弃离线完全自包含（需要联网取 viewer），换来「单个几十 KB 的 HTML 就能永远打开且不会视觉漂移」。严格性意味着**格式演进必须显式声明版本**——这是有意的摩擦。
- 可迁移性：**高**。

**决策 3：双 runtime（Bun server / Pi Node server）**
- 问题：Claude Code 和 OpenCode 走 Bun server，Pi 扩展走独立的 Node.js server，API 表面相同但底层是 `Bun.serve` vs `node:http`。
- 方案：`AGENTS.md` 硬规则——「**两个 server runtime 一起改。** 一个 endpoint 改动要进两个实现；共享逻辑放 `packages/shared/`。」例外被显式枚举：Inbox server 和 Shapes server 是 **Bun-only**（Pi 只是客户端）。
- Trade-off：**每个框架 API 差异都要写两份**。Issue #528（`fetch(req) did not return a Response object`）正是这张账单。此外 `apps/pi-extension/vendor.sh` 还要把 shared/core **vendor 进** Pi 扩展（Pi 是第三方宿主，不能假定能装 workspace 依赖），又多一层同步负担。
- 可迁移性：**中**。模式通用，但代价真实，只在「必须支持非 Bun 宿主」时才值得。

**决策 4：Node sidecar 隔离 PTY（ADR-002）**
- 问题：WebTUI 的 node-pty 在 Bun 下能启动 PTY 但**传不出终端数据**，同一后端在 Node 下正常。
- 方案：Bun server 起一个 **lazy 的 Node sidecar** 跑 PTY WebSocket server，绑 loopback 随机内部端口、**不对浏览器暴露**；浏览器只看到与 annotate server **同源**的路径（避免 SSH / devcontainer 的端口转发摩擦）；Bun 父进程死亡时通过**父进程死亡管道**带走 sidecar。
- Trade-off：牺牲简洁，换来 ADR 原文那句：「The sidecar keeps the risky runtime boundary small and isolated to terminal transport.」
- 可迁移性：**高**。「运行时能力缺失时用 sidecar 隔离，且失败必须优雅降级」是完全通用的模式。

**决策 5：优雅降级旁路，而非强求统一拦截**
- 问题：11 个 agent harness 的 plan 生命周期语义完全不同（Claude 的 `ExitPlanMode`、Codex 的实验性 Stop hook、OpenCode 的 `exit_plan_mode`、DeepSeek 的同名钩子）。Issue #328（20 评论）和 #479（13 评论）暴露了「拦截计划」这个抽象在异质宿主上的脆弱性。
- 方案：hooks 支持的用 hooks，不支持的降级为 slash command；OpenCode 提供**手动 review 模式 + `/plannotator-last`**（评审最近一条 agent 消息）作为 eager `submit_plan` 的替代路径；每个 agent 的 skill 目录里放轻量 skill，且有 `plannotator-skill-reference.test.ts` 保证 skill 里的子命令列表与 `cli.ts` 的实际 CLI **不漂移**。
- Trade-off：牺牲「一个 hook 走天下」的简洁，得到「每个宿主都有可用的路径」。
- 可迁移性：**高**。

**决策 6：Inbox 单写者 + append-only JSONL + 撕裂行容忍**
- 问题：需要既能被 agent 通过 MCP 写、又能被人通过 UI 读、还要跨机器同步的本地存储。
- 方案：一个写者进程；每次变更追加一行完整快照；撕裂行容忍；删除重写整个 project 文件（temp → rename）并把最高 seq 记进 `seq.json`；`FLOORED` 集合记录老 Inbox 永不读的文件 kind（seq 仍计数，避免号复用）；跨机器通过 tailnet 的 door 互访，动作发给拥有该 thread 的机器。
- Trade-off：全量快照写放大，换来**崩溃安全的极简性**和「日志即真相」的可审计性。
- 可迁移性：**高**。

**决策 7：三层安全守卫**
- 问题：本地 server 绑 loopback，但 DNS rebinding、跨站 POST、陈旧标签页都可能造成误操作或数据串写。
- 方案：`request-host-guard.ts` 在 fetch 最前面跑（覆盖 HTML、API、WebSocket 升级），Host 不在允许列表 → 403；`request-origin-guard.ts` 紧随其后，任何写方法来自别的站 → 403 **在读取任何内容或启动任何进程之前**（放行清单：无 Origin 的非浏览器客户端、自己的页面、VS Code 面板的 cookie 代理、`PLANNOTATOR_ALLOWED_HOSTS` 点名的 Origin）；`server-session.ts` 用 nonce 抗陈旧页（body 里没有 `serverSession` 的旧客户端照旧接受）。
- Trade-off：每层都可能误伤合法客户端，所以每条都写明放行清单。
- 可迁移性：**高**。

**决策 8：Annotation parity 硬约束（ADR-006 第 5 条）**
- 问题：Guided Review 是第二个 diff 渲染 surface，很容易在这里复制一份渲染 + 标注逻辑，然后两边慢慢分叉。
- 方案：「Diff 内的标注用与普通 diff 视图完全相同的组件和状态——同一套 toolbar/popover/suggestion 机制，同一份 `CodeAnnotation` 列表，同一份 feedback 导出。在 guide 里做的标注与在 diff 视图做的无法区分，流进同一个 Send Feedback payload。**Reuse, not copies.**」
- Trade-off：抽象出可复用部分意味着要解耦 `useAnnotationToolbar` / `DiffViewer` 对 dock layout 的耦合——比复制更费力，但换来长期不漂移。
- 可迁移性：**高**。「parity 是硬约束」这个提法本身可以推广到任何「第二 surface」场景。

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | Plannotator | Crit | dachev/plan-review | Qodo / CodeHealth MCP | 各 agent 原生 plan 审批 |
|------|-----------|------|--------|--------|--------|
| 形态 | 本地浏览器评审面 + Inbox | 本地浏览器评审面（Go 单二进制） | CLI，无 UI | 商用 SaaS，PR 侧评审 | agent 内置终端流 |
| Star | 12,505 | 1,311 | 969 | 商用 | n/a |
| 覆盖 agent 数 | 11 个编程 agent + 4 个个人助理 | agent-agnostic 但生态窄（119 forks） | 单 CLI 路径 | n/a | 各家自己 |
| 反馈是否回流 agent | 是（结构化 + 行号锚点） | 部分（单向审阅面） | 是（但评审者是第二个模型） | 是 | 是（纯文本） |
| diff 可视化 | 有（章节化 + 行内标注） | 有（Story 模式需额外 LLM 调用） | 无 | 有 | 无 |
| 本地优先 | 是（`~/.plannotator`，127.0.0.1） | 是 | 是 | 否 | — |
| 二次开发成本 | 高（12 万行 monorepo、多 runtime） | 低（单二进制，下载即用） | 极低 | 中 | 零 |

### 差异化护城河

- **生态护城河（最强）**：11 个 agent 适配层 + 一份统一反馈格式 + `~/.plannotator` 跨 surface 共享的数据目录（浏览器评审与终端评审**累积**）。新 agent 接入成本高（每家 plan 生命周期语义不同），且每个接入都会带来新用户。
- **信任护城河（次强）**：local-first（数据全在本地）、零知识托管（relay / share 只存密文）、`@plannotator/core` 强制 browser-safe 零依赖、PROVENANCE 逐文件记账、反 AI 署名条款。对一个 12.5K star 的开源项目，「数据不出机器 + 商业代码反向开源 + 有 provenance 账本」是稀缺的信任组合。
- **技术护城河（相对弱）**：核心 diff 渲染依赖 `@pierre/diffs`（还打了 patch）；annotation 是成熟但非独有技术。真正的差异化更多来自**产品整合度与工程方法论纪律**，而非单点算法。

### 竞争风险

1. **最高风险：agent 原生流**。若 Claude Code / Codex 把章节化 diff 评审 + 结构化批注做进原生体验，Plannotator 在这两个宿主上的价值归零。作者的对冲是**把 Inbox 做成「多 agent 的统一面」而非「某 agent 的评审器」**——这在原生流收窄功能时依然成立，但也意味着必须持续追新 agent。
2. **次高风险：Crit 这类轻量竞品**。12 万行 monorepo vs Go 单二进制，在「我就想点开看看」的用户面前差距明显。Plannotator 的对策是功能纵深 + 生态广度，但这是「大而全」路线，代价是维护债。
3. **商业层风险**：Workspaces 尚未发布（waitlist）。seam 模式已经把商业版的核心价值（UI）开源了——这是有意为之（降低信任门槛），但也意味着如果 Workspaces 迟迟不出，OSS 用户会问「那我为什么要装这个」。
4. **作者单点风险**：96.9% 的贡献集中度，Bus factor = 1。作者 12.5 万行、9,857 次提交的代码风格和纪律是这个项目最不可替代的资产，也是最脆弱的一环。

### 生态定位

**AI agent 工具链中的「人类接口层」（Human Interface Layer）**——位于模型与 agent 之间、agent 与人之间。它不是模型、不是 agent、不是 IDE，而是**让人重新成为 agent 工作流中的决策者**的那一层。

它的参照系是 VCS 和 issue tracker（Git 让协作可审计、Linear 让工作可追踪），而不是另一个 agent 工具。终局形态是「**agent 的 Slack + GitHub 的 PR 视图**」的合体——而 GitHub 自己的 Copilot 评审正从另一侧逼近。

作者自己的布局也印证了这个定位：`plannotator` org 下 28 个仓库，包括 `effective-html`（4.2K star，HTML artifact skills）、`herdr-annotate`（765，Rust 终端版）、`plannotator-tui`（252，Rust 终端版）、`guides.show`（托管服务）——不是造一堆互相竞争的工具，而是沿着「人类接口层」这个位置向不同宿主和形态铺开。

## 套利机会分析

- **信息差**：**star 数层面的套利已经不存在**（12.5K star + 9.8% fork 率，已被充分发现，10 月起月增从 ~800 陡升到 ~2600）。但**方法论层面的信息差极大**——ADR-005 的 seam 四条铁律、ADR-007 的 D1/D5/D6/D8/D9、「先写决策再写代码」的三层文档体系、以及「给 agent 读的规约文档当一等工程资产」这一整套，几乎没有中文读者系统讨论过。这才是这个项目对读者最大的价值。
- **技术借鉴**：如果你在做 agent 工具或 IDE 插件，可以直接拿走三样东西——① **seam 模式**（含「默认值必须是现状行为」这条不变量和「用 git mv + one-line shim 让 99 个 import 点零改动」的具体手法）；② **多宿主集成的优雅降级三件套**（能力探测 → 手动旁路 → 明确能力表）；③ **本地 server 的三层守卫**（Host → Origin → session nonce，尤其最后那条抗陈旧页）。
- **生态位**：填补了「agent 产出需要人类判断，但人类只有终端文本可用」这个空白。这个位置目前只有 Plannotator 占住了，而且作者正在把它从「评审器」上移到「统一人类接口层」——后者比任何单一 agent 的评审器更难被替代。
- **趋势判断**：**符合趋势但同时背着趋势的债**。向上，agent 数量与并行度都在涨，「多 agent 统一人类入口」的需求是确定性的；向下，21 个适配层 + 双 runtime 的维护债是确定性的，且随着上游 harness 迭代加速（Issue #596：OpenCode Beta 一改就断）会越来越重。作者已经用「Inbox 上移」来回应，但这个回应本身又是一次大规模重构（10 月单月 2,595 次提交、11 月半月 5,912 次）。**这个项目正在被自己的成功压着走。**

## 风险与不足

1. **Bus factor = 1**。作者一人贡献 96.9%，且项目的工程质量高度依赖他的个人纪律与判断。ADR 体系、seam 模式、测试哲学这些都是「有人持续维护」才成立的东西，不是自动生效的机制。
2. **维护债的结构性问题**。17 个 agent 适配 app + Bun/Node 双 runtime，Issue #551（hook 可靠性，25 条讨论）、#328、#479、#528、#596 全部是这条链路的账单。上游每家 CLI 的每次 breaking change 都要跟一遍。
3. **「local-first」不是「零网络」**。独立评测指出：每个 app surface 都会向 GitHub 检查新版且**无法关闭**，不适合 air-gapped 环境；本地 git review 会用 `git ls-remote` 探 origin；URL 标注默认走第三方 Jina Reader，「Ask AI」把选定上下文送外部 AI provider 而非本地模型。这是营销话术与实际网络边界之间的落差。
4. **发版过于频繁**。10.6 个月 232 个 tag、100 个 release，近 30 天发布 43 个 release，最新三个版本跨度仅 3 天。版本号（0.28.x）已经失去语义信息量，外部用户无法判断自己是否落后。独立评测也建议「在非关键环境先试升级」。
5. **无 linter / formatter 配置**（唯一明显短板）。没有 ESLint / Biome / Prettier，质量约束改由 `tsc --noEmit`（跨 20+ 个 tsconfig 的巨型 typecheck）、CI 门禁脚本和测试文化承担。在一个 12 万行、单人主导的项目里，这个选择可以理解，但它意味着**风格一致性完全靠个人自觉**，且新人上手没有自动化护栏。
6. **缺根级 CHANGELOG**。改用 `docs/releases/` + GitHub Releases + tag 驱动的 release workflow 代替，但对只想知道「这个版本改了什么」的普通用户不够友好。
7. **百万行代码的构成存疑**。6,621 个文件里大量是「一文件一测试」的 TDD 产物，`packages/inbox` 单包 1,498 个文件、300+ 个 `inbox-*.ts`。功能纵深是真，但**模块边界是否清晰是明显的问号**——这也是本次分析中无法完全验证的一点。
8. **Workspaces 长期停留在 waitlist**。商业化叙事（团队协作、托管、多租户）目前全部未落地，「为什么要装这个」在 OSS 侧缺少一个强答案。

## 行动建议

- **如果你要用它**：
  - **选它**，当且仅当以下至少一条成立：① 你同时用两个以上 AI 编程客户端（Plannotator 的核心价值就是统一面，单 agent 场景原生流已经够用）；② 你的 plan 或 diff 复杂到值得逐行批注；③ 你需要把评审结果**回灌**给 agent 而不是自己读终端抄行号；④ 你在意数据不出机器。
  - **别选它**，当你：只有一个 agent 且用它自带的 plan 审批；工作流偏纯终端/远程无 GUI（浏览器面是硬伤）；或你只想要一个轻量评审工具——那 **Crit** 的 Go 单二进制对你更合适。
  - 部署前先看 `~/.plannotator` 的数据边界：本地 git review 会 `git ls-remote` 探 origin（可加 `--no-git-remote-check`），URL 标注默认走第三方 Jina Reader，「Ask AI」会送外部 provider——有合规要求的话先把这些关掉。
  - **升级节奏要保守**。43 个 release / 30 天的发版密度意味着每个版本都可能是 breaking，建议固定在某个 tag 上跑一段时间再跟。

- **如果你要学它**：
  - 优先读 `adr/decisions/005-publish-document-ui-as-packages-20260701.md` 和 `007-portable-guided-reviews-20260815.md`——两篇 ADR 里记着**被否决的方案**（fork 方案因 rebase 4 次被弃、from-scratch 重写 UI 把应用搞坏并回滚），这比看最终代码有用得多。
  - 然后读 `packages/core/guide-format.ts`（1190 行，严格版本化 + 纯函数导出的完整实现）和 `packages/ui` 里 `configurePlannotatorUI()` 的 seam 定义。
  - **`AGENTS.md` 只有 41 行，是一张地图**，真正的规约在 `docs/agent-guides/` 的 24 篇里。先读 `agents-md-size.test.ts`——它展示了「用 CI 门禁强制文档纪律」的具体做法。
  - 想学多宿主集成，看 `apps/hook/` 怎么把 ExitPlanMode / Stop hook / exit_plan_mode 抽象成统一接口，以及 `/plannotator-last` 这个优雅降级旁路怎么实现的。
  - 想学安全，看 `packages/server/` 里的 `request-host-guard.ts` → `request-origin-guard.ts` → `server-session.ts` 这三层递进。
  - **注意别被代码量吓退**：124 万行里注释率 18.3%、1669 个测试文件，真正值得读的是 `packages/core`、`packages/ui` 和 `adr/`。

- **如果你要 fork 它**：
  - 唯一明显可改进的方向是**发版节奏与版本号策略**——把 0.28.x 的连续补丁号改成有时间语义的版本（如日期版本），让用户能判断自己是否落后。
  - 补上 **linter / formatter 配置**（Biome 或 ESLint + Prettier），对一个 12 万行、准备接纳外部贡献者的项目，这是必需的护栏。
  - 可以考虑**把 `packages/inbox` 拆分**——300+ 个 `inbox-*.ts` 挤在一个包里，长期看会成为维护瓶颈。
  - 如果要做**严格本地模式**，加一个真正能关掉所有出网检查的 flag（评测明确指出当前无法关闭），这在企业内网场景是有区分度的功能。
  - 但请先读 `AGENTS.md` 的 Hard rules——**未经人在浏览器确认 parity 前不删工作代码**那条，以及「Never compromise UX」那条，会约束你的所有改动。

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | https://deepwiki.com/backnotprop/plannotator （未能确认收录——站点反爬返回 429，非「未收录」） |
| Zread.ai | https://zread.ai/backnotprop/plannotator （已收录） |
| 官方文档站 | https://docs.plannotator.ai/ （含 Learn 栏目 20+ 篇） |
| 关联论文 | 无（属工程/产品实践，无学术论文） |
| 在线 Demo | https://share.plannotator.ai ｜ https://plannotator.ai/inbox/ ｜ https://plannotator.ai/assets/inbox-film.mp4 |
| 作者博客 | https://backnotprop.com/blog/plannotator/ （2026-01-03，初版动机） |
| 兄弟仓库 | https://github.com/plannotator （28-repo org，含 effective-html / herdr-annotate / plannotator-tui） |
| 独立评测 | [tau-home 评测](https://tau-home.com/en/post/plannotator-local-review-workspace-ai-coding-agents) ｜ [hysenlabs 评测](https://hysenlabs.com/zh-cn/projects/backnotprop-plannotator) |
