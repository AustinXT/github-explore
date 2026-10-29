# GitHub 推荐：2.5 个月 3285 星：OpenBot 把 Codex、Claude、Grok 收编成一支团队

> GitHub: https://github.com/nightly-labs/openbot

## 一句话总结

一个前 Solana DeFi CEO 做的 Electron 桌面工作台，把你**已经在付费订阅**的 Codex、Claude、Grok 等 13 个 CLI agent 收编成一支有角色、能互相委派、共享文件的「AI 团队」，全程 local-first；代价是它用的是 PolyForm 非商用协议（不是开源），而且 macOS 之外根本没有进程隔离。

## 值得关注的理由

1. **13 个 provider 靠一张「能力声明表」统一，核心代码零分支**。`packages/contracts/src/agent-providers.ts` 里每个 provider 一行，声明 13 项能力（`steer` 是 native 还是 deferred、支不支持并发、怎么隔离工作区、用量怎么上报、skill 目录在哪）。表格用 `as const satisfies Record<AgentProviderId, AgentProviderDescriptor>` 收口——**新增一个 provider 忘了填行，TypeScript 直接报 TS2741 并点名那个 id**，不用跑测试就能发现。渲染层在问 main 之前就知道该 provider 支不支持某个按钮。这是目前开源 agent 编排工具里最扎实的 provider 抽象层。

2. **把 SQLite 用成了一条可重放的事件账本**。`src/backend/database/database-core.ts` 的 `dispatch(commandId, events, project)` 在**单个 SQLite 事务**里完成「追加事件 → 执行读投影 → 写命令回执 → 提交」，回执让 `commandId` **幂等**；`src/backend/database/thread-replay.ts` 能从事件流按 sequence 重放，重建全部投影状态。投影是**同步**的（同一个事务内直接写 `projection_*` 表），不是异步追平。这不是「用了 SQLite」，是拿 SQLite 承载了一条有回执、可审计、可崩溃恢复的账本。

3. **29.5 commits/天、0.69 天一个版本、105 个 Release**。2.5 个月 2304 次提交，10 月单月 1306 次（比 8 月高 5.8 倍且仍在加速），版本号从 0.1.0 走到 0.53.2 只用了 76 天，平均每个 release 间隔不到一天。对比一下：普通活跃开源项目是 1–3 commits/天、1–4 周一个版本。

4. **一批可以直接抄走的工程纪律工具**。`scripts/debt-ratchet.ts` + `type-ratchet.ts` 用「per-file per-check 的 baseline，只允许降低不允许升高」把技术债变成 CI 可判定的单调递减量（实测 `src/` + `packages/` 非测试代码 `@ts-ignore` / `@ts-expect-error` = **0**，`any` = 34 处）；`changelog.d/` 增量 changelog 目录让两个 PR 永远不会改同一行 CHANGELOG；`scripts/verify-preload-bundle.ts` 验证的是**打出来的 preload bundle** 而不是源码。

5. **它敢把安全问题写在 README 顶部**。README 第 13–18 行直接写「Agents currently run with `danger-full-access` and `approvalPolicy: never`」，`SECURITY.md` 补一句「Full local access is an explicit current product decision, not a security boundary」。在 2026 年的 agent 工具里，这种诚实是稀缺的——而且它的隔离代码在 Linux/Windows 上是**拒绝启动进程**而不是静默降级。

## 项目展示

![共享频道中的多 agent 协作：Chief / Research / Builder / Launch 四个角色互派任务并共享文件产物](https://openbot.run/assets/a-channel-Cfnf--ZC.webp)
*这是这个项目最关键的一张图：不是「一个聊天框里多个模型」，而是有角色、有频道、有派工的团队。左侧 Chief 派活，Builder 产出的文件直接挂在频道里*

![Agent 线程内的任务看板：Workstream / Owner / Status 三列派工表 + 文件产物 + Shell 命令](https://openbot.run/assets/a-thread-C4YG4M8v.webp)
*「角色 → 任务 → 产物」的数据模型：每个任务有唯一 owner，产物和 Shell 执行记录都在同一视图里*

![Routines 定时调度与 run history（工作日 9:00 AM）](https://openbot.run/assets/a-routine-CV81WGxY.webp)
*Routines 是它区别于所有 CLI agent 的核心能力——agent 常驻、按表干活，而不是你坐在终端前一轮一轮喂*

![Provider / Model 选择器：ChatGPT(Codex CLI)、OpenAI、Gemini 等多 provider 入口](https://openbot.run/assets/pick-a-model-BWAQz_tq.webp)
*provider-neutral 抽象的视觉证据：换模型是下拉框里的一行，而不是重开一个工具*

![OpenBot 品牌卡 Meet OpenBot](https://openbot.run/openbot-social.png)
*官方品牌卡（1600×900）*

> 说明：README 里一张产品图都没有（只有 2 个 badge），上图全部来自官网 `openbot.run` 的 `apps/auth-api` 指南资源目录，链接均已实测可访问。

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/nightly-labs/openbot |
| Star / Fork / Watcher | 3,285 / 316 / 10 subscribers |
| Open Issue / Open PR | 265 / 47（已合并 PR 500+，37 位贡献者） |
| 代码行数 | 916,278 行（TypeScript 68.1%、TSX 24.0%、CSS 5.7%）；**扣除 i18n 翻译资源后 ≈ 75.7 万行真实业务代码** |
| 注释比 | 11.2%（代码：注释 = 8.9:1） |
| 文件 / 依赖 | 5,970 个文件 / 66 个运行时+开发依赖（runtime 40 + dev 26） |
| 许可证 | **PolyForm Noncommercial 1.0.0**（source-available，非 OSI 开源；≤0.1.11 曾为 Apache-2.0） |
| 项目年龄 | **2.5 个月**（2026-08-12 首次提交，2026-10-28 最后推送） |
| 总提交 / 贡献者 | 2,304 commits（**29.5/天**）/ 44 人（主作者 58.9%，含 `github-actions[bot]` 55 次） |
| 开发阶段 | 密集开发（近 30 天 1,450 commits，10 月单月 1,306 且仍在加速） |
| 开发模式 | 职业项目（周末占比 19.4%、深夜占比 8.5%） |
| 版本发布 | v0.53.2 / 122 tag / 105 Release，**平均 0.69 天一个版本** |
| 热度定位 | 中等热度 + 爆发上升通道（3 天从 1,279 → 3,285，日榜最高第 2） |
| 质量评级 | 代码[优秀] 文档[优秀] 测试[充分] |

**技术栈与形态**：Bun workspaces monorepo（7 个顶层工作区）+ Electron + SolidJS + Effect + SQLite（本地状态）/ Cloudflare Workers + D1 + R2（账号与元数据）/ WebRTC v3 + 自建 Signal 服务（远程接入）/ Expo React Native（移动端）/ Docker + seccomp + Nix flake（分发）。**桌面端、移动端、自托管服务端、Discord/Telegram/Slack bot、官网五端同仓**，这是它发布节奏能这么快的结构性原因——一次改动同时影响五个产品面。

## 作者视角：为什么存在这个项目

### 创始人/作者背景

`nightly-labs` 是个组织账号，法人主体是波兰有限责任公司 **Synthetify Labs sp. z o.o.**（署名在 `NOTICE`、`LICENSE` 和 Windows 发行签名里）。创始人 **Norbert Bodziony** 此前是 Solana 生态 DeFi 合成资产协议 **Synthetify** 的 CEO，2022 年做过加密钱包 **Nightly**——「Nightly Labs」这个名字是延续下来的。2026 年他带团队转入 AI agent 工具赛道。

**这个背景不是装饰**，它直接解释了项目的三条路线选择：

- **为什么是 local-first + 自托管**：钱包生意的本质是「用户资产与密钥必须在我能控制的设备上，多设备可达但不外包托管」。这条基因原封不动地迁移成了「编排状态、文件、浏览器数据都在你自己机器上，手机随时接入但不用把工作区交出去」。
- **为什么是 PolyForm 非商用 + CLA 收版权**：crypto 项目的 source-available 商业化是作者熟悉的打法。`AGENTS.md` 把「Keep PolyForm Noncommercial 1.0.0」列为不可谈判项，商业授权走 `licenses@openbot.run`。
- **为什么是「一个任务一个 owner + 显式委派」**：这是链上账本式的资源独占模型——一个任务一个 owner，转移用显式 handoff，冲突在状态机层被拒绝，而不是靠 prompt 里写「请不要同时做这件事」。

### 问题判断

作者看到的是一个**已经存在但被浪费的资产**：到 2026 年，ChatGPT/Codex、Claude Code、Grok、Cursor、Cline、Muse Code 的消费级订阅已经普及，但这些 CLI agent 各自跑在不同终端、互不通信、上下文随会话消失、退出即失忆。用户为一堆能力重复付费，却拿不到任何协作能力。

于是他的定位切口非常锋利：**provider 已经是商品，OpenBot 不训模型、不做模型路由网关，只做「agent 编排层 + 状态宿主」**。这是唯一能让「已付费的订阅」不被浪费的产品形态。

时机也踩得很准——2026 年正好是「CLI agent 能力成熟 + 商业订阅普及 + ACP（Agent Client Protocol）成为行业标准」三者的交点。`agent-providers.ts` 里 13 个 provider 的排列本身就是一条时间线：从 codex/claude/grok（自研协议适配）到 opencode/antigravity/cursor/cline（走 ACP），再到 pi/muse/inception/deepseek/openrouter（**共用同一个 `cliName: "Pi CLI"`**——不重新造 CLI，而是复用已有 CLI 的多 provider 支持，这个省力设计很典型）。

### 解法哲学

**① 核心封闭、外围开放。** 编排模型、数据库、IPC 契约严格内部化；对外只留 ACP 一个标准口子给任意第三方 agent，另有 MCP（agent 自带工具）、Skills、Plugins、Marketplace 四层扩展。

**② 功能完整，但用「能力声明」把复杂度外推给 provider。** 作者没有选择让每个 provider 走同一条代码路径，而是让每个 provider 明确声明自己会什么，编排层按声明调度。这是整个项目最核心的哲学——**复杂性不消灭，被表格化**。

**③ 易用性优先，但用「诚实降级」代替静默失败。** Linux/Windows 上 Workspace-only 隔离**直接不启动进程**，报错要求用户显式选 Full access，而不是降级成无约束执行还装作有隔离。

**④ 拒绝「假装安全」。** README 顶部 WARNING 明写 `danger-full-access` + `approvalPolicy: never`，`SECURITY.md` 写明「Full local access is an explicit current product decision, not a security boundary」。**这既是诚实的，也是自我限定的**：它把「这不是安全边界」写进合同，而不是留给用户去发现。

### 战略意图

这是一个**核心产品**，而且**明确有商业化意图**，走的是 open-core 而非 genuinely open：

- 代码在 GitHub 公开可读，但 LICENSE 是 PolyForm 非商用，**商业使用需单独授权**；CLA 要求所有外部贡献者把版权转让给 Synthetify Labs。
- 商业化路径清晰可见：`apps/auth-api` 跑在 Cloudflare Workers + D1 + R2，含 **Stripe**（`stripe:bootstrap` 脚本）、hosted servers 目录、hosted sites、billing、host key handover、cloud authorization、multi-tenant hosting；另有 macOS **Host Manager**（多租户 Mac mini 客户机）。
- 云侧只放**账号与元数据**。`AGENTS.md` 原话：「Cloudflare holds accounts, avatars, host configuration, memberships, invitations, and logical sessions; it does not hold chats, files, or commands.」**云是控制面，不是数据面**——这是刻意的信任边界设计，也是它能同时卖「本地优先」和「托管多租户」的原因。
- 平台层的野心在 Marketplace（`marketplace/plugin-catalog`、`production-catalog`）、Skills、Plugins、Team API v4+。

## 核心价值提炼

### 创新之处

1. **Provider 能力声明表 + 编译期全覆盖检查** — 新颖度 4/5 | 实用性 5/5 | 可迁移性 5/5
   `packages/contracts/src/agent-providers.ts`（708 行）用 `as const satisfies Record<AgentProviderId, AgentProviderDescriptor>` 定义 13 个 provider × 13 项能力。缺行 → TS2741 点名。新增 provider 的成本被压缩到「一行表 + 一个 driver」（`src/backend/provider-drivers.ts`）。**适用场景**：任何后端数量会持续增长、而前端需要按能力差异化渲染的系统。

2. **命令回执式幂等 dispatch（event log + projection + receipt 同事务）** — 新颖度 4/5 | 实用性 5/5 | 可迁移性 5/5
   `database-core.ts` 的 `dispatch<T>(commandId, events, project)` 在 `BEGIN IMMEDIATE` 事务内追加 `orchestration_events` → 执行投影 → 写 `orchestration_command_receipts`（含 `result_json`）→ `COMMIT`。重复 `commandId` 直接返回缓存结果。`thread-replay.ts` 的 `rebuildThreadProjection(threadId)` 从事件流重放重建 messages / turns / provider-session 链接 / summaries / attachments 投影。**适用场景**：需要崩溃恢复 + 幂等重试 + 可审计历史的本地状态存储。

3. **ACP Flavor Hook：「协议原生 + 观测到的 quirk」** — 新颖度 4/5 | 实用性 4/5 | 可迁移性 5/5
   `src/backend/acp-flavor.ts` 的 `AcpFlavor` 接口**全是可选 hook，缺省即协议原生行为**（`DEFAULT_ACP_FLAVOR = {}`，注释写明这就是 Grok 和 Cline 的行为）。已有 hook 如 `CURSOR_ACP_FLAVOR.noiseChunk` 精确匹配 Cursor 2026.10.22-27dcf5f 的一个 chunk，`sessionNotFound` 只在 `-32602` 且 `data.message` 匹配时才返回 true。注释要求「每个 hook 注明观察到的具体 agent 版本」。**核心代码零 provider 分支，quirk 全部可追溯。**

4. **构建产物级的 preload 验证** — 新颖度 4/5 | 实用性 4/5 | 可迁移性 4/5
   `scripts/verify-preload-bundle.ts`（8.8KB）在 `bun run build` **之后**把真正打出来的 preload bundle 放进 VM、配一个假 Electron，断言：只暴露 `openbot` 这一个 world；每个方法都被 `IPC_ENDPOINTS` 命名；每个方法发到正确 channel；request 必须 `invoke`、event 必须 `on`/`once`；bundle 不得加载 sandboxed preload 加载不了的模块、不得含 `import()`。**大部分同类项目只测源码不测产物。**

5. **多级任务所有权状态机（owner 与 assignment 分离）** — 新颖度 4/5 | 实用性 4/5 | 可迁移性 4/5
   `src/backend/channel-service.ts`（2811 行）里每个 `ChannelTask` 有 `ownerAgentId`，**一个 task 同时只有一个 owner**。转交（`reassign`）会替换 owner 记录，但**旧 owner 的 assignment 仍在跑**——代码注释说得很清楚：「the identity of the owner alone does not show that the task is free: the assignment of the previous owner does」。占用判定看 assignment，不看 owner 字段。

6. **能力字符串协商的协议版本系统** — 新颖度 3/5 | 实用性 4/5 | 可迁移性 4/5
   `packages/contracts/src/team-protocol/` 下有 v1..v8 共 8 个版本，每版四个文件（冻结的 wire / base / adapter / webrtc-adapter），外加约 130 个能力模块。兼容不靠「版本号 + if/else」，而是**协商出 capability 字符串集合**，host 只在协商到时才发新字段（如 `history-extent-v1` 才让 channel page 带 unloaded length）。**适用场景**：长生命周期客户端-服务端协议演进。

7. **流式 SHA-256 + 版本化 sidecar manifest** — 新颖度 3/5 | 实用性 4/5 | 可迁移性 5/5
   `src/backend/file-hash.ts` 的 `sha256File` 用 `createReadStream` + Effect 的 `acquireUseRelease` 流式哈希，**不整体读入内存**。`src/backend/attachment-files.ts` 为每次传输写 `.openbot-transfer.json`（`version: 2`——v1→v2 是因为字段从 `recipientBotIds` 改名成 `recipientAgentIds`，注释解释了为什么不能把两种形状塞进同一版本号），包含每个附件的 `sha256`/`size`/`mimeType`。注释明确写：**「Nothing in the app reads this sidecar back - it is written for the user and the model looking at the transfer directory」**——manifest 是写给人（和 agent）看的，让接收方能独立验证完整性。

8. **技术债棘轮（debt-ratchet / type-ratchet）** — 新颖度 3/5 | 实用性 5/5 | 可迁移性 5/5
   `scripts/debt-ratchet.ts` 提供通用规则，`scripts/type-ratchet.ts` 用它约束 TypeScript 选项。机制：baseline 文件 `tools/typescript/type-baseline.json` 记录**每个文件在每项检查下的当前计数**，实际计数超过 baseline 就失败；`--write` 只能**降低** baseline（「a higher count is a hand edit that a reviewer sees」）；某项检查清零后从 baseline 移除并把对应 TS 选项打开。**适用场景**：任何想清理 `any` / lint 债务但不想被一次大清理阻塞发布的团队。

9. **隐藏 Electron 窗口做构建期 WebGL 渲染** — 新颖度 4/5 | 实用性 3/5 | 可迁移性 3/5
   `apps/auth-api` 跑在 Cloudflare Workers，**没有 WebGL**，但文章配图要用 `@paper-design/shaders` 程序化生成。解法：`apps/auth-api/content-image-electron.mjs` 开一个**隐藏的 BrowserWindow**（`contextIsolation: true, nodeIntegration: false, sandbox: true, webgl: true`，且必须 `paintWhenInitiallyHidden: true` + `backgroundThrottling: false`，因为 shader 库靠 ResizeObserver 定 canvas 尺寸），在 `about:blank` 注入 bundle，每张图 `executeJavaScript("window.openBotContentImage.render(...)")` 返回 data URL。产物 commit 进 `content-art/`，`content-images.ts` 算 manifest key，**只有输入变了的图才重画**，没文章引用的图被删除——「The build fails until the folder matches the articles」。代价：需要一台有 GPU 的开发机，CI 跑不了这一段（注释明说「this runs on a developer's machine and not in CI」）。

10. **记忆审阅按单价而非按名字降级模型** — 新颖度 3/5 | 实用性 4/5 | 可迁移性 4/5
    v0.53.2 引入的 agent 长期记忆，触发条件是每 20 轮 / 静默 15 分钟 / 清空聊天 / 关闭 side thread。记忆上限从 64 提到 256 条，prompt 只注入必要记忆。`reviewModel()` 用 `inputPrice(provider, id)` 比较，**只有当 provider 默认模型单价确实更低时才降级**，价格未知就保持原模型。**适用场景**：后台辅助任务（摘要、记忆整理、分类）用便宜模型跑。

### 可复用的模式与技巧

1. **能力声明表 + `satisfies` 编译期全覆盖** — 多 provider / 多后端 / 多端适配层，新增项漏配时在编译期报错并点名。
2. **命令回执幂等 dispatch** — 本地状态存储需要崩溃恢复、幂等重试与审计时。
3. **协议原生 + quirk hook** — 接入一批「基本兼容但各有小毛病」的第三方实现（ACP、SSE 变体、私有 API）。
4. **构建产物级 bridge 验证** — Electron preload、sandbox bridge、序列化边界。
5. **能力字符串协商** — 长生命周期客户端-服务端协议演进与混合版本共存。
6. **流式哈希 + sidecar manifest** — agent 间文件传输与完整性自证。
7. **技术债棘轮（只降不升 baseline）** — 渐进式清理类型/lint 债务。
8. **`changelog.d/` 增量 changelog** — 高频发布 + 多 PR 并行的项目；每个 PR 写自己的一份，发布时汇总，**两个 PR 永远不改 CHANGELOG.md 的同一行**。
9. **lane 化 FIFO 队列** — `src/backend/agent/drain-scheduler.ts` 把一个 agent 的 own chat、channel task、messaging delivery 拆成独立 lane，每条 lane 内串行（「One queue that runs one turn at a time」）。
10. **乐观并发的摘要版本号** — 多个任务并发更新同一份压缩上下文时用版本号检测冲突。
11. **fail-closed 的平台能力降级** — 沙箱/隔离能力在部分平台缺失时，宁可功能不可用也不静默降级。

### 关键设计决策

**决策 1：用「能力矩阵」取代「provider 分支」**
- 问题：13 个 provider 各有协议、登录方式、steer 能力、并发能力、用量上报、skill 目录约定、隔离方式。若用 `switch (provider)`，分支会散落在 renderer、preload、backend 多处，漏一处就是静默 bug。
- 方案：13 项能力集中在一张 `as const satisfies` 收口的表里，新增 id 缺行 → TS2741 点名。
- Trade-off：牺牲了 provider 的**动态**可扩展性（新增 provider 必须改 contracts 包），换来「加一个 provider 只需两处改动」，且渲染层无需往返 main 就能决定 UI。
- 可迁移性：高。

**决策 2：`ForeignProviderId` —— 用品牌类型处理「新 host 对旧 client」**
- 问题：Team API v1-v8 并存，host 可能比 client 新，client 会见到不认识的 provider id。
- 方案：`declare const FOREIGN_PROVIDER: unique symbol; type ForeignProviderId = string & { readonly [FOREIGN_PROVIDER]: true }`。不认识的 id 仍可读、仍可路由，但 `isKnownAgentProvider()` 为 false，OpenBot 不会为它建账号或选模型。
- Trade-off：引入了必须处处小心的第三态（known / foreign / local-only），换来**旧 client 面对新 host 不崩**。
- 可迁移性：高。

**决策 3：IPC 契约手写而非 codegen，但验证做到构建产物层**
- 问题：renderer ↔ main 的 IPC 通道如果只是字符串约定，加一个 endpoint 要改三四处。
- 方案：`packages/contracts/src/ipc-endpoints.ts`（1915 行）是单一真相源，每个 endpoint 携带 wire channel、所属 group、kind（request/event）与载荷类型；类型是**幻影成员**（`readonly __request?: void`，只为类型检查存在，运行时仍是 `{ kind, channel }`）。**没有 codegen 是刻意的**——手写 TS 比 DSL+生成器更易 review，且 `satisfies` 的编译期保证更强。
- Trade-off：手工维护 1915 行契约 + 100 多行验证脚本，比 codegen 重；换来**没有生成器、没有 stale 生成产物、契约即文档**。
- 可迁移性：高（尤其「验证产物而非源码」这一层）。

**决策 4：ACP 接入 = 协议原生 + 每 agent quirk hook**
- 问题：ACP 是行业标准，但每个实现都有偏差（missing session 错误码不同、失败提示混进答案文本、后台任务让 `session/prompt` 长时间不返回、reasoning 插在答案 token 之间）。
- 方案：**进程与协议分离**——`acp-connection.ts`（219 行）只管子进程 + `ndJsonStream` + 退出诊断（含 Windows 进程树 `endProcessTree`），完全不碰 session；`acp-client.ts`（2846 行）管 session。quirk 全部推到 `AcpFlavor` hook。
- Trade-off：每个新 agent 可能要加一个 flavor 文件（当前 `acp-flavor.ts` / `-antigravity` / `-opencode` 三个）；换来**核心代码零分支、quirk 可追溯到具体版本**。
- 可迁移性：高。

**决策 5：Provider 一致性测试 —— 用假 agent 跑同一组用例**
- 方案：`scripts/provider-conformance-e2e.ts` 对每个说 ACP 的 driver 跑**同一组用例**（列模型、单轮、模型切换、取消、取消后再一轮、新进程 resume、missing session、必需的 sign-in），用 `scripts/provider-fakes/agents/conformance.ts` 假 agent 驱动，**跳过某个用例即失败**。
- Trade-off：只覆盖 ACP 系（codex/claude/pi/inception/deepseek/openrouter/muse 走别的协议，报告里明确列在 `notCovered`）；换来**协议一致性由测试保证而非人工回归**。
- 可迁移性：中高。

**决策 6：内嵌浏览器隔离 —— 独立 Electron session + 能力受限的 webPreferences**
- 方案：`src/backend/browser-host.ts` 的 `BROWSER_WEB_PREFERENCES`：`sandbox: true, contextIsolation: true, nodeIntegration: false, nodeIntegrationInSubFrames: false, nodeIntegrationInWorker: false, webviewTag: false, webSecurity: true, allowRunningInsecureContent: false`。每个 agent profile / tab 用**独立的 `session.fromPartition()`**（`persist:openbot-browser` 为共享，每个 profile 一个 `persist:<partition>`），cookie / storage / cache 物理隔离；私隐 session 用 `session.fromPartition("openbot-private-<uuid>", { cache: false })`。
- 关键：agent 的浏览器能力**通过 MCP 工具暴露**，而不是给页面注入任何特权；浏览器页在另一个 WebContentsView 里，拿不到 `window.openbot`，也读不到托管附件。凭据填充有防护：`PreparedBrowserSecret.agentScriptedOrigin` 标记「该 origin 上 agent 自己跑过脚本」，此时**只有用户能填，agent 不能**。
- Trade-off：每个 profile 一个 partition 占磁盘；换来**浏览器侧真实的 session 级隔离**。
- 可迁移性：中高。

**决策 7：进程隔离 —— macOS Seatbelt 沙箱，Linux/Windows fail closed**
- 方案：`src/backend/process-confinement.ts` 在 macOS 用 `/usr/bin/sandbox-exec` 加载**动态生成的 Seatbelt profile**（`seatbeltProfile(writable, protectedPaths, inProjects, contents, lockFolders)`），规则是「写入拒绝 → 允许 writable → 再次拒绝 protected」，**最后匹配的规则生效**。每个 provider 的 state path 单独建模（五个维度：writable / protected / protectedInProjects / writableContents / lockFolders）——比如 OpenCode 的 cache 目录要单独一份，因为里面有 npm 包和 language server。
- Linux/Windows **明确抛错**：`throw new ProcessConfinementUnavailableError(sourceText("error.agent.workspaceOnlyMacOnly"))`，文件顶部注释写明「on Linux and Windows the process does not start, and the user must choose Full access」。
- Trade-off：Windows/Linux 上 Workspace-only 模式不可用（功能缺失）；换来**绝不静默降级为无约束执行**。
- 可迁移性：中高（macOS 路线可直接抄）。

**决策 8：多 agent 频道 —— 单一 task owner + 显式委派 + lane 化队列**
- 方案：`channel-service.ts` 的 `ChannelTask` 单一 owner；委派用 `channel_assign` 工具建子任务形成依赖图，父任务等依赖完成；`drain-scheduler.ts` 的 lane 机制保证每个 agent 的每条 lane 内串行。
- 未完成时的诚实处理：owner 忙 / 用量超限 / owner 被隐藏 / owner 离开，任务进 `heldByLimit` 等状态等待，**不会**派给别的 agent。
- Trade-off：串行化牺牲吞吐；换来**责任归属清晰、无重复劳动**。
- 可迁移性：高。

**决策 9：上下文预算 —— 摘要链 + 0.8 阈值 + 乐观并发版本号**
- 方案：`src/backend/agent/context-compaction.ts` 在 0.8 阈值触发，`CONTEXT_COMPACTION_TIMEOUT_MS = 120_000`，启动后的 compaction 有 10 倍宽限期（#3466）。**compaction 本身是一个真实的 provider turn**，所以要用 `claimTurn` 吞掉属于它的 `turn/started`。预算按**外部 provider thread id** 而非 agent id 记账（一个 agent 的多个 thread 并行跑）。Codex 在 compaction turn 期间拒绝输入，所以有 `RefusalHold` 机制把被拒消息放回队列。频道摘要：`CONTEXT_CHARACTERS = 120_000`、`SUMMARY_CHARACTERS = 12_000`、`SUMMARY_TARGET_CHARACTERS = 8_000`。
- Trade-off：摘要必然有损；换来频道历史在有界 prompt 窗口内无限延伸。
- 可迁移性：高。

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | OpenBot | OpenClaw | Paperclip | Orca | CopilotKit/OpenBot | Vibe Kanban |
|------|----------|-----------|----------|------|------------------|--------------|
| Stars | 3,285 | 393,299 | 108,307 | 109,081 | 7,655 | 28,491 |
| 许可 | **PolyForm 非商用** | MIT | MIT | MIT | MIT | Apache-2.0 |
| 形态 | 桌面 app + 移动 + 自托管 | 终端 + IM 渠道 | 服务端（自建 Node+DB） | 桌面 + 移动 + 远程 | Docker + PostgreSQL | 看板 Web |
| 多 agent 角色/频道语义 | **完整**（角色、频道、委派、依赖图） | 弱（单人助理） | 中（org chart） | 中 | 中 | 弱（仅任务卡） |
| 跨 provider 会话连续 | **有**（provider-handoffs 带 32k 字符历史迁移） | 无 | 无 | 无 | 无 | 无 |
| 接入 provider 数 | **13**（含 ACP 标准口） | 少 | 少 | 少 | 中 | 中 |
| 部署门槛 | **下载即用，零部署** | 低 | 高（需自建服务端+DB） | 中 | 高（Docker+PG） | 低 |
| 治理/审计/权限 | **弱**（#1967 待补） | 弱 | 中 | 弱 | **强**（CEL 网关+审计+容器化） | 弱 |
| 进程隔离 | macOS Seatbelt；**Win/Linux 拒绝启动** | 未验证 | 未验证 | 未验证 | **per-bot 容器化** | 无 |

### 差异化护城河

1. **Provider 抽象的深度** —— 13 个 provider × 13 项能力声明 + ACP flavor hook + conformance e2e 一致性测试 + `provider-handoffs/` 的跨 provider 会话迁移。这是纯工程量堆出来的护城河，**竞品短期内抄不动**——尤其是 conformance e2e 那套「所有 ACP driver 跑同一组用例、跳过即失败」的机制。
2. **本地状态的完整性** —— 事件溯源 + 幂等回执 + 可重放投影，加上桌面 / web / 移动三端共享同一套 `packages/contracts` 契约。
3. **契约冻结纪律** —— 8 个 Team API 版本永久保留（`AGENTS.md`：「Released Team API adapters are permanent」），任何旧 client 都能连新 host；`agent-providers.ts` 里的注释把能力表类比为「released vocabulary，must never move」。

### 竞争风险

1. **治理/审计缺失是硬伤**。Issue [#1967](https://github.com/nightly-labs/openbot/issues/1967) 要求 per-user / per-bot 权限与 owner/admin/member 多角色，并且明确「权限必须在 host 侧强制执行，不只是 UI 隐藏」。**多租户 hosting 已经交付，权限模型还在排队**——这既是企业市场的准入证，也是 Team API 商业线的真正阻塞项。
2. **PolyForm 非商用是商业天花板**。同赛道竞品清一色 MIT / Apache-2.0（OpenClaw、Paperclip、Orca、Vibe Kanban），企业采购的法务门槛高一个量级。这既是护城河的一部分（source-available 保护），也是它最难跨过的坎。
3. **同名混淆**。`CopilotKit/OpenBot`（7.7K star）是实打实的品牌损耗，两个项目在做完全不同的事，却在 SEO 和心智上持续互相干扰。
4. **Windows/Linux 用户拿不到安全承诺**。`process-confinement.ts` 在非 macOS 上 fail-closed 是正确的工程选择，但产品后果是**Windows 用户（agent 工具的主力人群之一）只能选 Full access**。
5. **社区成熟度远低于产品成熟度**。90 万行代码、122 个 tag、105 个 Release 对应的外部贡献基本是 1–2 人贡献量级（`detasar` 19、`aniruddhaadak80` 17、`634634624` 14）。制度（CONTRIBUTING 11KB + CODE_OF_CONDUCT + CLA）搭好了，跑在社区规模前面。

### 生态定位

**local-first 的 agent 团队工作台 + 未来的托管平台**。它不与 OpenClaw 抢「IM 入口」，不与 Paperclip 抢「企业编排」，不与 Vibe Kanban 抢「任务看板」，而是占据「**桌面 + 自托管 + 多 provider**」这个象限，并用 ACP 作为向第三方 agent 开放的接口。Marketplace + Skills + Plugins + Host Manager 构成未来的平台层。

**唯一未被挤压的缝隙是 hosted server / Team API / 多租户托管这条商业化线**——而它正卡在 #1967 的权限模型缺口上：**商业化蓝海的入口，同时是当前最明确的产品待办**。

## 套利机会分析

- **信息差**：**star 溢价已经发生，不算被低估**。2.5 个月 3285 star、日均 +1300、Trending 三天涨 1995，是典型的一次性曝光曲线。但**开发密度远超 star 增速**——这不是「一夜爆红后无人维护」。真正的信息差在别处：PolyForm 非商用 + CLA 把大企业挡在门外，于是「同款能力、没有授权费的路径」成了缺口；而 #1967 一旦补上，这个缺口就同时变成产品优势和商业入口。
- **技术借鉴**：本报告里 11 个可复用模式中，**技术债棘轮、命令回执幂等 dispatch、能力声明表 + `satisfies`、构建产物级 bridge 验证、`changelog.d/` 增量 changelog** 这五个是「半小时内可以抄进自己项目」的级别，且都带具体文件路径。
- **生态位**：填补的是「**多 agent 协作的状态宿主**」这个空白——不是又一个 agent runtime（OpenCode / Crush / OpenHands），不是又一个 agent 编排框架（Paperclip / Orca），而是「谁在跑、跑在哪、上下文怎么留、文件怎么共享、provider 怎么换」这一层。
- **趋势判断**：**有后发优势**。OpenClaw 393K star、Paperclip 108K、Orca 109K 都比它早，但 OpenBot 在两个维度上是后来者才做对的：① 用 **ACP 行业标准**而不是自研协议接入第三方 agent；② 用 **capability 协商**而不是版本号 if/else 来做协议演进。这两点在 2026 年才成熟，它直接吃到了。
  - 反面：它也吃了后发者该吃的亏——**同名混淆**（CopilotKit/OpenBot 更早占了这个名字）、**Windows/Linux 隔离缺位**、**PolyForm 授权**让企业采用曲线比 MIT 对手长得多。

## 风险与不足

1. **不是开源软件**。PolyForm Noncommercial 1.0.0 不是 OSI 认证的自由软件，商业使用需单独授权，CLA 还会把外部贡献的版权集中到 Synthetify Labs 一家手里。**引用它的代码到商业闭源产品里会踩法律问题**，这是选型时最容易被 README 一句话掩盖的雷。
2. **默认安全姿态就是「完全放权」**。`danger-full-access` + `approvalPolicy: never` 是默认值，不是可选项。外部红队文章的判断在这一点上**成立**：prompt injection 直接等价于系统级命令执行；agent 间通信会放大单个被攻陷 agent 的影响半径。
3. **进程隔离只有 macOS 有**。Windows/Linux 上 Workspace-only 模式**拒绝启动**，用户只能选 Full access。（注：外部有文章称这是「静默降级为无约束执行」，**这个措辞不准确**——代码是 fail-closed 的显式拒绝，比静默降级更负责任，但产品后果仍然存在。）
4. **Computer Use 路线落后于社区**。`cua-driver` 纯像素方案每步要 1280x800+ 全分辨率截图（1,500–2,500 token/帧）+ 3–5 秒延迟，5 步任务烧 10,000–15,000 token。社区在 Issue #3782 里提议的 AT-SPI2 可访问性树 + CDP 四层语义架构（视觉降级为 fallback）明显更优，**官方 CHANGELOG 里的推进明显更保守**——社区已经跑在官方前面。
5. **频道摘要是当前最脆的一环**。读 `src/backend/channel-history.ts` 可以精确定位两个同源 bug：
   - **#1693**：摘要链把**上一轮摘要也作为输入**，所以每过一轮摘要就再长一点；一旦某轮超过 12k 且 shorten pass 也没压下来，直接 `channelHistoryInvalid` 失败，且 `summary` 变量**未被写回**（`saveSummary` 只在成功路径调用），`throughSequence` 保持不变。修法不是「缩预算重试」，而是改成**增量式摘要**或让 shorten pass 无条件先执行。
   - **#3761**：版本冲突时**整体丢弃**本次摘要结果（连 `throughSequence` 一起丢），下一轮从旧的 `throughSequence` 重新处理同一批消息 → 因为 `throughSequence` 没推进，输入集合不变，同样摘要任务反复失败，这就是「lead 久等」的机制。修法是版本冲突时**合并**而非丢弃。
   - 这不是架构限制，是**明确可落地的 bug**。
6. **并发能力声明是编译期常量**。`agent-providers.ts` 里 custom ACP 的 `concurrentTurns: false` 是硬编码常量（`as const satisfies`），不随运行时变化。但底层 session 模型（每 thread 一个 ACP `session/new`）本已支持并行——**并发是「provider 能力声明」层面的保守声明，不是架构限制**。修复路径不是改一个 boolean，而是让它变成可运行时声明（自定义 agent 注册时携带能力字段，来自 `src/main/custom-agent-store.ts`）。社区成员 botdoggy 已在自己 fork 实现并配了确定性 e2e，等 `approved` label 即可开 PR。
7. **i18n 是真正的维护放大器**。`packages/i18n` 8344 次改动、159,275 行、13 种语言、1,378 个文件——**每加一条 UI 文案要同步 13 个语言文件**。这个成本随语言数线性增长，会成为多语言扩张的硬天花板。
8. **协议演进包袱**。8 个 Team API 版本各 4 个文件 + 约 130 个能力模块，`knip.config.ts` 得专门为 `team-protocol/v*.ts` 关掉 unused-export 报告。**能力协商本身值得学，8 份手抄副本属于过度工程**。
9. **缺乏可验证的性能承诺**。README 里没有任何 benchmark（外部审计专门指出了这点）。内部虽有 `scripts/web-client-perf-e2e.ts` 和 `dev-automation/bench.ts`，但没有对用户公开的对比数据。`bun run dev:bench` 有 CPU/RAM 场景基准，但没进文档。
10. **没有正式版本稳定承诺**。0.53.x 的版本号意味着**契约尚未稳定**。对一个要被放进别人工作流、要托管别人文件的桌面应用来说，API 破坏性变更的频率是个实际风险。

## 行动建议

- **如果你要用它**：
  - **适合**：macOS 用户，已同时订阅多个 AI CLI（Codex / Claude / Grok / Cursor / Cline 任一），想让人 agent 真的组队干活、能自己排班（用 Routines）、需要内嵌浏览器和 Computer Use，且**你的代码和凭据不能交出去**。
  - **不适合**：企业生产环境（治理与审计缺位 + PolyForm 法务门槛）、Windows/Linux 用户（有强隔离需求时）、团队协作场景（#1967 未解决意味着**能上服务器 = 能看所有 bot**）、以及任何要把它的代码集成进商业闭源产品的团队（授权问题）。
  - **替代路线**：想走真 MIT 开源就选 OpenClaw / Orca / Paperclip；想要企业治理能力看 CopilotKit/OpenBot（注意同名）；只想在终端里跑多个 agent 选 Claude Squad。
  - **落地建议**：先只开**一个** provider 的 Full access 试跑，别一上来把所有 agent 和频道都配上；把 `~/OpenBot/Shared/Transfers` 里的 `.openbot-transfer.json` 纳入你的备份；不要在生产凭据的浏览器 profile 上开 Computer Use。

- **如果你要学它**（按价值密度排序）：
  - `packages/contracts/src/agent-providers.ts`（708 行）— 能力声明表 + `satisfies` 编译期全覆盖，**最值得抄**
  - `src/backend/database/database-core.ts` + `src/backend/database/thread-replay.ts` — 事件溯源 + 幂等回执 + 可重放投影，**本项目最值得抄的架构**
  - `scripts/debt-ratchet.ts` + `scripts/type-ratchet.ts` — 技术债棘轮，**最值得抄的小工具**（半小时能落地）
  - `src/backend/acp-flavor.ts` — 协议原生 + quirk hook 的适配层写法
  - `scripts/verify-preload-bundle.ts` — 验证构建产物而非源码的 bridge 测试思路
  - `src/backend/process-confinement.ts` — macOS Seatbelt profile 动态生成 + fail-closed 降级
  - `src/backend/browser-host.ts` — 多 Electron session 隔离 + 能力受限 webPreferences
  - `src/backend/channel-service.ts` — owner/assignment 分离的任务状态机
  - `src/backend/agent/drain-scheduler.ts` — lane 化 FIFO 队列
  - `docs/ARCHITECTURE.md` + `docs/architecture/`（13 篇专题）— 架构文档纪律的范例

- **如果你要 fork 它**：
  1. **补权限模型**（#1967）：在 host 侧强制 owner/admin/member + per-bot 授权，而不是 UI 隐藏——这是团队付费和合规的准入证，也是它相对 CopilotKit/OpenBot 唯一的短板。
  2. **修频道摘要的两个同源 bug**（#1693 / #3761）：摘要改增量式、版本冲突改合并而非丢弃。这是明确的 bug 而非架构限制。
  3. **把 `concurrentTurns` 改成运行时可声明**（#3763）：能力应来自自定义 agent 的注册记录（`src/main/custom-agent-store.ts`），而不是一张全局常量表。botdoggy 的 fork 实现路径是对的。
  4. **推进语义 Computer Use**（#3782）：AT-SPI2 可访问性树 + CDP，视觉降级为 fallback——省下的是 token 和延迟，不是画质。
  5. **补 Windows/Linux 隔离**：`process-confinement.ts` 的 fail-closed 是对的，但功能缺失就是产品缺失。Windows 上可以用 Job Object / AppContainer，Linux 上 bubblebang 其实能做但注释说它「无法拒绝尚不存在的新文件」——这个约束是可以绕过的（预创建目标文件、或用 mount namespace 做只读 bind mount）。
  6. **公开 benchmark**：把 `dev:bench` 的结果做成 README 里的对比表，这是外部审计反复提的要求。

### 知识入口

| 资源 | 链接 |
|------|------|
| 官方网站 | https://openbot.run/ |
| 官方文档 | https://openbot.run/docs |
| 长文介绍 | https://openbot.run/news/introducing-openbot |
| 架构文档（仓库内） | https://github.com/nightly-labs/openbot/blob/main/docs/ARCHITECTURE.md |
| 自托管部署 | https://github.com/nightly-labs/openbot/blob/main/docs/self-hosting.md |
| 多租户托管 | https://github.com/nightly-labs/openbot/blob/main/docs/multi-tenant-hosting.md |
| Provider 条款 | https://github.com/nightly-labs/openbot/blob/main/docs/provider-terms.md |
| DeepWiki | 未收录（探测被 Vercel Security Checkpoint 拦截，搜索索引无条目） |
| Zread.ai | 未收录（403 bot 拦截） |
| 关联论文 | 无（工程型产品项目，无学术定位） |
| 在线 Demo | 无独立 playground；官网首页有可交互脚本化 landing demo |
| 独立审计 | https://mrkeyoor.com/repos/nightly-labs-openbot |
| 安全红队分析 | https://explainx.ai/blog/nightly-labs-openbot-desktop-workspace-codex-claude-grok-agents-danger-full-access-polyform-noncommercial-2026 |
