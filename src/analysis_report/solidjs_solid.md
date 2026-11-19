# GitHub推荐：Solid 2.0：删掉 7 个 API 才守住 7.6KB

> GitHub: https://github.com/solidjs/solid

## 一句话总结

React 早期核心成员 Ryan Carniato 做了八年的前端框架，用「编译期把 JSX 变成精确 DOM 操作 + 运行时一张细粒度响应式图」彻底绕开 Virtual DOM，2.0 版本把 Rust 编译器、异步内建进响应式图、以及「删掉 7 个核心 API」三件事一次性做完，并把 core 运行时体积用 CI 硬闸门锁死在 7.56 KB brotli。

## 值得关注的理由

1. **这是前端框架史上少见的「主动做减法」的大版本**。2.0 移除了 `createResource`、`batch`、`startTransition`、`on`、`createComputed`、`produce`、`createMutable` 七个核心 API，每个都有替代机制，且替代方案不是「换个名字」而是「换一个更小的机制接管」——这是对「API 表面在膨胀」这个行业通病的正面回答。
2. **体积守卫是全仓最值得抄的工程实践**。`scripts/size/` 用「brotli 定上限、minified 做判定、只降不升的棘轮、冻结地板需声明例外」四层机制，把「小」从口号变成了 CI 的 required status check，十年里靠它把核心地板从 7.1 KB 压回 7.56 KB 上限且禁止上调。
3. **它把「为什么我的组件重跑了」做成了结构化因果链**。`packages/signals/src/core/attribution.ts` 能在运行时输出 `[why-run] effect "docTitle" ran ← memo "userLabel" changed ← signal "notifications" write` 这样的归因链，并进一步按用户交互归因——这是所有隐式依赖系统（Svelte Runes / Vue / MobX / RxJS）都缺的一层。
4. **它是为 AI 编码代理写的前端框架**。仓库直接提供 `AGENTS.md`、765 行 `CHEATSHEET.md`、两个 agent skill 文件、`@solidjs/diagnostics` 结构化诊断包，CHEATSHEET 开头写着「Solid is not React, and 2.0 is not 1.x. Both priors are dominant bug sources here」——把「模型先验污染」当作一类真实 bug 来治，这在 2026 年是独有的做法。

## 项目展示

![SolidJS 2.0 Banner](https://assets.solidjs.com/banner?project=Library&type=core&version=2.0)
SolidJS 2.0 官方动态 banner（SVG，版本号随发布自动切换）

![Solid 2.0 – The Long Hold 发布公告封面](https://www.solidjs.com/img/blog/solid-2-0-the-long-hold/header.png)
2026-11-16 的 2.0 stable 发布公告头图，官方对「为什么现在做 2.0」的完整论证

![Async Solid – One Graph, Two Machines 封面](https://www.solidjs.com/img/blog/async-solid-one-graph-two-machines/header.png)
Async Solid 架构系列主文头图，对应 2.0 的核心叙事：同一张响应式图，客户端与服务端两台机器

![SolidJS Contributors](https://contrib.rocks/image?repo=solidjs/solid)
贡献者墙，268 位贡献者，其中第二名是 AI 编码代理 `claude`

> 官方发布公告全文：[Solid 2.0 – The Long Hold](https://www.solidjs.com/blog/solid-2-0-the-long-hold)

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/solidjs/solid |
| Star / Fork | 36,745 / 1,193（Watcher 212） |
| 许可证 | MIT |
| 代码行数 | 462,856（TypeScript 49.7%、TSX 23.4%、JavaScript 15.1%、**Rust 8.1%**） |
| 项目年龄 | 103 个月（2018-04-24 首次提交，至今未中断） |
| 开发阶段 | **密集开发**（近 90 天 1,728 个 commit，日均约 19 次） |
| 贡献模式 | 单人主导 + 社区协作（主作者占 87.1%，总贡献者 268 人） |
| 热度定位 | 大众热门（前端框架第一梯队，TIO 长期 Top 20） |
| 质量评级 | 代码 优秀 / 文档 优秀 / 测试 优秀 |
| 运行时依赖 | **0 个**（开发依赖 29 个） |
| 核心运行时体积 | **7.56 KB brotli**（CI 冻结地板，只许降不许升） |
| 当前版本 | `solid-js@2.0.3`（2.0 stable 发布于 2026-11-16，分析当天为第 3 天） |

## 作者视角：为什么存在这个项目

### 创始人/作者背景

Ryan Carniato（`ryansolid`）是 React 早期核心成员之一，参与过 React 早期开发与 Suspense 方向的技术讨论，2018 年 4 月离开后创立 Solid。他的主张非常直接：不要再用 Virtual DOM 做用户界面。

这个背景直接塑造了 Solid 的两个核心决策。第一，**Solid 是 React 早期「响应式优先」思路的极致化**——React 最终选择了 VDOM + 编译器 memoization（今天的 React Compiler），而 Solid 坚持在 2018 年就把答案定死：更新粒度应该是表达式级别的。第二，**Solid 学的是 React 的教训，不是 React 的代码**。React 早期最大的优势是「可组合性」——组件可以随便拼、随便换。Solid 2.0 的框架中立路线（TanStack Query / Router 作为一等公民、官方 SolidStart 退役为维护态）就是这条教训的直接产物：作者明确反对「一个大而全的 meta-framework 说了算」。

组织账号 SolidJS 于 2021 年才建立（项目先行、组织后置），本仓库在组织内活跃度排名第 1。商业化状态是 MIT + Open Collective 赞助（README 底部 16 个 sponsor），**没有 open-core 分层，没有付费层，是 genuinely open**。

### 问题判断

作者看到的问题不是「VDOM 太慢」，而是三个更根本的东西：

1. **更新粒度的浪费**。VDOM 要求每次状态变更重建一棵树再 diff，而实际受影响的往往只是几个表达式。Solid 的解法是让编译器在 build time 就知道每个表达式的依赖边界，把更新精确到 DOM 位置。
2. **异步是「平行世界」**。1.x 的 `createResource` 需要 `source()` / `mutate()` / `loading` / `error` 一整套专用 API，与 `createSignal` / `createMemo` 是两套心智。2.0 让任何计算都能返回 Promise 或 AsyncIterable，pending 状态成为图里的一个属性，`<Loading>` 成为 UI 边界——异步不再是平行 API，而是同一张图的推论。
3. **API 表面在膨胀**。`batch` / `on` / `createComputed` / `produce` / `createMutable` / `startTransition` 每个只解决一个小问题，用户却必须全部学会才能正确使用。

**为什么是现在**（这是最关键的一问）：2026 年是「全行业向 Signals 收敛」的时间点——Svelte 5 Runes（2024）、Vue 3.6 Vapor Mode、Angular 全面 Signals 化并弃用 zone.js、React Compiler 自动化 memoization。细粒度响应式正在从「差异化特性」变成「基线能力」。Solid 2.0 选择在这个窗口发布，说明作者判断：**一旦基线化完成，Solid 的差异化就会从「响应式模型」转移到「响应式模型的实现质量」**——所以 2.0 的重点不是「引入新特性」，而是把响应式内核、编译器、诊断、体积全部重做一遍。

另有两个时间点值得一提：2023-07 Chrome 团队发布《Chrome Supports Solid in Building a Performant Web》，项目进入大厂视野；2019 年的 issue #109（SSR Specification，45 条评论）社区就在追问「SSR 该怎么标准化」，答案直到 2.0 才给出——SSR 变成异步图的一种执行模式，能力下沉到 core，不再由 SolidStart 独占。Solid 花近 7 年把「渲染模式」从平行 API 收敛成同一张图的不同机器。

### 解法哲学

**「可组合优先于一致性」**——拒绝一个大而全的 meta-framework 说了算。2.0 把 SolidStart 退役为维护态，meta-framework 能力下沉到 core 与 Vite 插件的 `solid({ start: true })` 模式，TanStack Query / Router 成为一等公民。对追求一致性的用户是降级，对追求灵活性的用户是升级。

**「少即是多」——这是最硬的一条哲学，有完整证据链**：

| 移除的 API | 取代机制 | 证据位置 |
|---|---|---|
| `createResource` | async memo + `<Loading>` 边界 | `documentation/solid-2.0/05-async-data.md` |
| `batch` | 自动微任务批处理 + `flush()` | `packages/signals/src/core/scheduler.ts` |
| `startTransition` | 图管理 + `isPending()` / `latest()` | `05-async-data.md` |
| `on` | `createEffect(compute, apply)` 两阶段拆分 | `01-reactivity-batching-effects.md` |
| `createComputed` | split effect / function-form `createSignal` / `createMemo` | `02-signals-derived-ownership.md` |
| `produce` | draft-first setter（produce 成为默认行为） | `04-stores.md` |
| `createMutable` | `createStore` + draft setter | `MIGRATION.md:977` |

注意 `batch` 移除的语义变化：2.0 中 setter **不立即改变读取结果**，值在微任务 flush 后才可见。这是重大行为变更——把「同步批处理」换成「微任务批处理」，向 Vue / Svelte 靠拢，代价是破坏了 1.x 的同步读直觉。

**「Safe by construction rather than by exhaustion」**——不靠穷举状态机（VDOM 的 diff 规则），靠更小的图从结构上保证正确。这在代码里体现为：写错的地方在 dev 直接 throw（`REACTIVE_WRITE_IN_OWNED_SCOPE`、`ASYNC_STORE_SETTER`、`PENDING_ASYNC_UNTRACKED_READ`、`OPTIMISTIC_WRITE_BEFORE_LOAD` 等稳定诊断码），而不是「运行一下看看会不会坏」。

**明确不做什么**：不做 VDOM 与 diffing；不做「组件函数重跑」模型；不做 hooks 规则（组件就是普通函数）；不做「signals 解决一切」——`@solidjs/signals` 是独立可发布的包，React 应用可以用它管状态而不用 Solid 的渲染模型；2.0 **没有**第一方 RSC 实现，server components 仍是 RFC 状态。

### 战略图景

**定位是基础设施，不是应用框架**。SolidStart 从「一等 meta-framework」降级为「core 能力 + Vite 插件模式」，是刻意的去中心化——让 Solid 成为可被任意 meta-framework 消费的 reactive substrate。两个信号互相印证：`@solidjs/signals` 独立成包可脱离渲染层单独使用；框架中立化。

更大的规划是 **ReactiveScript / TSRX**——把响应式提升为一等语言。仓库里 `documentation/tsrx/` 有 specification snapshot，`packages/compiler/src/tsrx/` 有完整的 Rust 模块（`lower.rs` / `semantic.rs` / `tape.rs` / `style_projection.rs`）。编译器把 TSRX 作为 feature flag 实现，并刻意不跨边界共享 oxc 类型——`Cargo.toml` 里写明「it carries its own git-pinned oxc (0.140) which coexists with our crates.io oxc — no oxc types cross the boundary (the parse result is a revision-neutral FlatTape)」。这是极高质量的依赖边界设计。

## 核心价值提炼

### 创新之处

按「新颖度 × 实用性」排序：

1. **因果链归因引擎**（新颖度 5/5，实用性 4/5，可迁移性 5/5）
   `packages/signals/src/core/attribution.ts`（4,908 行）在每次值提交时给节点打上 `ChangeRecord`，计算重跑时找出「时间戳比上次运行新」的依赖作为原因，形成完整因果链，并按 `ChangeOrigin` 区分 6 种来源（`interaction` / `effect` / `action` / `async` / `navigation` / `external`）。架构上刻意与 core 解耦——core 只负责调用窄接口的 observe-tier hook，禁用成本是每个 hook 点一次 null check，生产构建完全折叠掉。

2. **双单位体积闸门 + 只降不升的棘轮 + 冻结地板**（新颖度 4/5，实用性 5/5，可迁移性 5/5）
   brotli 是真正发出去的单位但**不是输入的单调函数**——改几个 minified 字节，brotli 结果会跳 ±50–90 B。纯 brotli 闸门会因噪声挂 PR。解法是 **cap 用 brotli、判定用 minified**：每个 cap 记录「设 cap 时的 minified 大小」，余量按**记录值**算而非本 PR 的 base，这样两个连续 +15 B 的 PR 不能都过。棘轮让省下的体积自动拉低 cap 且只降不升；三个地板场景的 cap 被冻结，PR 只能降不能升，除非 body 里有 `Size-Exception:` 行。README 原话：「Ten weeks of individually justified 10–300 B bumps took the signals floor from 7.1 to 9.9 KB; the freeze makes the next one a decision, not a paragraph.」
   一个反直觉的决策：`scripts/size/` 目录**故意放在 pnpm workspace 之外**（自带 npm lockfile），理由写在 `size.yml` 注释里——「adding its tooling to the workspace graph re-keys pnpm peer instances (vitest, @codspeed/vitest-plugin), which relocates the benchmark harness and shows up as phantom CodSpeed regressions」。为了不让测量工具污染被测对象的依赖图，宁可维护两套 lockfile。

3. **世代戳 O(1) 边验证**（新颖度 4/5，实用性 5/5，可迁移性 4/5）
   `packages/signals/src/core/graph.ts` 的 `link()` 用 `Link._gen`（边创建时的订阅者世代号）把「这条边是否已在前缀内」的判定从 O(n) 扫描降为 O(1) 位比较，消除 alien-signals `isValidLink` 在「计算非连续重读早期依赖」场景下的 O(n²)。代码注释直接写明了来龙去脉。

4. **影子实现对拍**（新颖度 5/5，实用性 4/5，可迁移性 4/5）
   `packages/signals/src/core/seat.ts`（1,717 行，`__TEST__` only）是一份**独立重实现**「读应该看到哪个世界」的判定表，与真实实现的多个 decider 做 slot 级对拍（断言 slot 身份而非值相等）。用「两份独立实现对拍」代替「写更多断言」，在状态机密集的系统里是更高级的测试手段。

5. **统一的 world rank + posture 表**（新颖度 5/5，实用性 4/5，可迁移性 4/5）
   整个系统里，「一个读应该看到屏幕上的值 / 本次 flush 的暂存 / tick 的持有值 / 某个 lane 的值 / 抛 NotReady / 抛错」被抽象成一张可排序的层级表（world rank S < Fl < H + posture 优先级 F > A > V > L > D > U）。读只 RAIS，不 FALL。

6. **乐观更新的 lane / MVCC 覆盖语义**（新颖度 4/5，实用性 4/5，可迁移性 3/5）
   `lanes.ts` 头部注释定义得很清楚：「A lane is "a new base of a transition"」——乐观写不是「记下旧值失败时还原」，而是开一条新基线。配套的 `truth.ts` 提供 `covers`（覆盖语义）：guess 覆盖了某个 truth，truth 落地时 guess revert 到**它覆盖的那个 truth**，而不是回到旧值。authoritative reader（`until()`）**看不到**乐观覆盖。双槽存储 `_value` / `_pendingValue` 与信号节点的 committed/staged 模型完全同构。

7. **冷字段扩展 `_x` + presence bits**（新颖度 3/5，实用性 5/5，可迁移性 5/5）
   把「偶尔才用」的字段（`_inFlight` / `_error` / `_blocked` / `_pendingSources` / `_optimisticLane` 等）全挪到惰性分配的单例扩展对象 `_x`，核心对象字面量不得增长。`packages/signals/docs/NODE-SHAPE.md` §12 记录了实测：「computed literal 39 → 29 fields, signal 13 → 12; memo 553 B → 429 B (−22%), create 330 → 280 ns」。§11b 规定 presence bits 记录在恒存在的 `_config` 位掩码上，热路径只付一次 monomorphic masked read，规则原文是「a bit says 'consult _x', never the reverse」。代价是 +740 B 核心体积——对一个体积是最稀缺资源的项目，这是刻意选的方向。

8. **编译期条件谓词提升**（新颖度 3/5，实用性 5/5，可迁移性 4/5）
   看 `packages/compiler/__tests__/fixtures/dom/conditionalExpressions/output.js` 的实际输出：编译器把三元表达式的**判定部分**提升为独立 memo（`_c$ = _$memo(() => !!state.dynamic)`），分支体保持惰性。这是 alien-signals 风格 push-pull 图能在编译期被静态化的关键——编译器知道 `state.dynamic` 变了要重跑哪个分支，所以它把「判断」和「取值」分离。

9. **`action()` 用 generator 的 `yield` 作为事务安全挂起点**（新颖度 4/5，实用性 4/5，可迁移性 3/5）
   action 的每次调用开一个 transaction，`yield` 之前的写入被持有。关键约束是普通 `await` **不**安全——runtime 无法 hook async generator 内部的 await continuation，`await` 之后的代码在 transaction 之外跑。这被写进 RFC 并给出精确修复模式（先 `await` 拿类型化结果，再裸 `yield` 重新进入 transaction）。

10. **模块级可选钩子实现 tree-shaking**（新颖度 4/5，实用性 4/5，可迁移性 5/5）
    core 里的每个可选能力（lane、boundary、store、attribution、mark、verdict）都是一个模块级可空钩子，由对应模块在**求值时**安装。注释说清了为什么不用静态 import：「Optional-module hooks: module bindings, not `GlobalQueue` statics, so a bundle that never imports the installing module never assigns them — its minifier folds every guarded call site (and the branch behind it) away.」`scripts/size/` 里有专门的水合场景验证「不用 store 的 hydrate app 不携带 store 引擎」。

11. **Rust/Oxc 编译器 + wasm32-wasi 目标 + 双实现 parity**（新颖度 3/5，实用性 4/5，可迁移性 3/5）
    JSX 编译器从 Babel 插件重写为 Rust/Oxc（`packages/compiler/src/` 39,766 行，其中 Rust 代码 36,216 行），通过 napi-rs 暴露，同时提供 wasm32-wasip1 目标供浏览器内编译。`AGENTS.md` 明确要求 Babel 路径与 Rust 路径「their validators and codegen must stay in parity (shared test expectations)」。

12. **`<Loading on={...}>` 的依赖列表语义**（新颖度 4/5，实用性 4/5，可迁移性 4/5）
    `on` 属性的语义是「`id()` 读了什么」而不是「`id()` 的值是什么」。因为「只有通知才重要，值从不比较」，`on={(id(), 1)}` 在 `id` 变化时通知，`on={() => id()}` 永不通知（函数没人调用）。

### 可复用的模式与技巧

按可迁移性从高到低：

1. **双单位体积闸门 + 记录值余量 + 只降不升的棘轮 + 冻结地板**——适用场景：任何把体积当卖点的库（Preact、Ark UI、Zustand）。尤其值得借鉴的是「余量按记录值算而非按本 PR base 算」这一条，它是防跨 PR 蠕变的关键。
2. **影子实现对拍**——适用场景：状态机 / 调度器 / 协议实现。写第二份独立实现来验证第一份，比堆断言更省事也更强。
3. **世代戳边验证**——适用场景：增量式依赖图、构建器、增量编译。把「边是否已在前缀内」从 O(n) 扫描降为 O(1) 位比较。
4. **冷字段扩展 + presence bits**——适用场景：V8 上任何大量小对象系统（状态管理库、渲染引擎、GC 敏感的 SDK）。
5. **两阶段 effect（compute / apply 分离）**——适用场景：任何需要「副作用延迟到所有计算完成之后」的响应式系统。
6. **微任务批处理 + 显式 `flush()`**——适用场景：任何 reactive 系统都会面临「同步读 vs 自动批处理」的选择，Vue 3 和 Svelte 5 都选了微任务路线。
7. **MVCC 覆盖语义替代值回滚**——适用场景：任何有乐观 UI 的框架（React 19 的 `useOptimistic` 是简化版本）。
8. **统一分类权威**——`packages/compiler/src/shared/classify.rs` 明令「Nothing outside this module may re-derive dynamic classification」。适用场景：多后端编译器、多模式渲染器。
9. **降级阶梯**——编译器 / hyperscript (`@solidjs/h`) / tagged template (`@solidjs/html`) / 自定义 renderer 四条入口，同一语义不同性能档位。适用场景：需要覆盖从「极致性能」到「零构建」全谱系的框架。
10. **稳定诊断码 + 每码修复指南 + 结构化事件通道**——适用场景：任何要服务 AI agent 或建立错误知识库的框架。

### 关键设计决策

**决策 1：编译期把 JSX 变成精确 DOM 操作**
- 问题：VDOM 需要运行时重建一棵树再 diff
- 方案：编译器降级成直接 DOM 操作 + 精确响应式绑定；同 markup 的模板抽成模块级常量，运行时 `<template>` 克隆
- Trade-off：牺牲「写 JSX 就能用」的通用性——编译器必须能静态识别「什么是动态的」，因此有了 `isDynamic`（`classify.rs`）与 `/*@static*/` 标记等规则；同时丢失了「组件函数重跑」这一 React 直觉
- 可迁移性：高

**决策 2：侵入式链表 + 高度堆调度 + 世代戳边验证**
- 问题：issue #46「Duplicate edges in signal graph」——同一信号被多个计算读取时产生重复边，重复订阅、内存放大、无谓重算。这是细粒度依赖图的根本复杂度税
- 方案：依赖图用侵入式链表（`_deps` / `_subs` / `_nextDep` / `_prevSub`），脏节点用按高度索引的堆调度，边复用靠世代戳做 O(1) 判定
- Trade-off：换来 O(1) 边验证和无 GC 压力，代价是**图的手工内存管理极其复杂**——`trimStaleDeps` / `unlinkSubs` / `clearDeps` / `deferredReleases` / `dormantNodes` 一整套释放协议，注释里满是 issue 号。这也解释了 `seat.ts` 这个 1,717 行影子实现的存在
- 可迁移性：中（世代戳技巧可移植，完整释放协议高度项目特定）

**决策 3：微任务批处理 + `flush()`——把「同步读」变成显式动作**
- 问题：1.x 的 `batch()` 需要用户主动包裹，忘记包裹就产生中间态渲染
- 方案：`scheduler.ts` 的 `schedule()` 在非同步深度时 `queueMicrotask(flush)`；`flush()` 有精细边界——在 action 内调用 dev throw `[FLUSH_IN_ACTION]`，在 effect callback 内调用 dev warn `[FLUSH_IN_EFFECT_CALLBACK]`，drain 循环有 `1e5` 次迭代保护并在触发时报告「last staged node」
- Trade-off：破坏 1.x 的同步读直觉（`setCount(1); count()` 仍返回旧值），换来「永远不会有中间态」的强保证。对测试和命令式集成代码是真实痛点，所以保留 `flush()`
- 可迁移性：高

**决策 4：owned scope 内禁止写入——把一类 bug 变成编译期错误**
- 问题：这类写入是反馈循环的主要来源；因为追踪是隐式的，用户很难发现自己在组件体里意外读了一个 signal 从而被订阅
- 方案：在 effect compute / memo / 组件体里写 signal，dev 直接 throw。`untrack` **不能**绕过——「the check is on the owning scope, and `untrack` only stops dependency tracking」
- Trade-off：破坏性的，1.x 里合法的写法在 2.0 直接抛错；诊断码本身给出了反模式示范（RFC 里明确标注 `// ❌ BAD: using ownedWrite to suppress the write-under-scope error`），说明作者知道这会被滥用
- 可迁移性：高

**决策 5：编译器双实现（Rust + Babel）并行**
- 问题：Rust 编译器的速度是 2.0 的核心卖点（官方数据：1MB 模块 24,975ms → 70ms），但生态里 Babel 插件路径不能断
- 方案：`@solidjs/compiler`（Rust/napi-rs）与 `@solidjs/babel-plugin`（TS）双实现，`AGENTS.md` 要求两者 codegen 与 validator 保持 parity
- Trade-off：双实现的维护成本是必要代价——但这也让 `packages/compiler/src/shared/condition.rs` 里出现注释「Faithful port of the Babel plugin's `transformCondition`」这样的双向同步注释
- 可迁移性：中

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | Solid 2.0 | Svelte 5 | Vue 3.6 | Preact | React 19 + Compiler |
|------|-----------|---------|--------|--------|-------------------|
| Star 数 | 36,745 | 89,747 | 55,037（core） | 39,007 | 约 23 万+（社区口径） |
| npm 近 30 天下载 | 4,519 万 | 3,779 万 | 9,966 万 | 2.26 亿 | 10.16 亿 |
| 运行时体积 | **7.56 KB** brotli（CI 强制冻结地板） | 约 28 KB（外部数据） | 约 20+ KB（外部数据） | 3 KB（React 兼容层） | 约 45 KB（外部数据） |
| 更新粒度 | 编译期可证的表达式级 | 编译期 + Runes | VDOM → Vapor Mode 推进中 | VDOM（Signal 为附加层） | VDOM + 自动 memoization |
| 组件执行次数 | **一次** | 状态变化时重跑 | 组件级重渲染 | 重跑 | 重跑 |
| 异步模型 | **值级**（Promise 是图里一等值） | `{#await}` 块级 | Suspense 边界级 | 无对应物 | `use()` 边界级 |
| 体积守卫工程 | 双单位闸门 + 棘轮 + 冻结地板 | 有监控，无此组合 | 无 | 无 | 无 |

> 运行时体积除 Solid 的 7.56 KB 外，均为社区测量数据，未在本仓库内独立验证；Solid 的 7.56 KB 来自 `scripts/size/floor-caps.json`（eager entry chunk，core floor，brotli），可独立复核。

### 差异化护城河

1. **技术护城河（最强）**：编译期 JSX → 精确 DOM + 世代戳依赖图 + 微任务批处理 + MVCC 语义 lane，这套组合的复杂度本身就是壁垒——`packages/signals/src`（TypeScript，20,030 行代码）+ `packages/compiler/src`（Rust，36,216 行代码）**加起来比整个 Preact 还大**。竞品要达到同等语义，得重做同样的工程量。
2. **诊断 / 归因护城河（独特）**：稳定诊断码 + 因果归因链 + agent 可消费协议 + 修复 skill。竞品在「让 AI 写对代码」和「让人看懂为什么重跑」两个维度上都没走到这个深度。
3. **体积护城河（可持续）**：三套机制让「小」不会被时间侵蚀。这是最容易被抄袭、也最难被追赶的护城河——因为它是一套**流程**而不是一项技术。
4. **信任护城河（弱）**：Ryan 的个人信誉 + Chrome 团队的背书。但单人依赖既是护城河也是风险。

### 竞争风险

**最大的威胁不是任何单一竞品，而是「全行业向 Signals 收敛」**：React Compiler / Vue Vapor / Svelte 5 Runes / Angular Signals 四路并进，把细粒度响应式从差异化特性变成基线能力，Solid 的技术优势被摊平。Solid 2.0 在基线化完成前发布，正是对这个威胁的回应。

按威胁程度排序：
1. **全行业基线化**（结构性）——这是主因
2. **Vue Vapor Mode**——保留整个 Vue 生态（下载量 2.2 倍）却拿到 Solid 式性能模型，是对「性能强 + 生态薄」组合的精准打击
3. **React Compiler 抹平性能差距**——React 的性能问题从来不是 VDOM 本身，是 memoization 不够；自动化之后 Solid 剩下的优势只有体积和更新粒度的确定性
4. **单人依赖风险**——ryansolid 占 87.1% 提交。AI 编码代理已成规模贡献（第二名 `claude`，316 commits）是缓解也是新风险
5. **文档密度**——issue #167 有 116 条讨论，是全库最高热度 issue。这是**非技术**的最大短板，直接对应「理解成本」这一采用门槛

### 生态定位

**不是「React 的替代品」，而是「响应式基础设施」**。两个信号互相印证：`@solidjs/signals` 独立成包且可脱离 Solid 渲染层单独使用；框架中立化（TanStack Query / Router 一等公民，SolidStart 退役）。

生态现状：SolidStart（5,921 star）已退役为维护态，能力下沉到 core + Vite 插件；`solidjs/filesystem-routing` 仅 20 star（2.0 新拆出）；社区层 `solid-primitives`（1,577）与 `kobalte`（1,892，无障碍组件库）已跟进 2.0 stable。

**最适合**：高频交互 UI（数据看板、编辑器、实时协作、图表）——这些场景里「更新粒度」和「响应延迟」直接决定产品体验，也是 React 的 VDOM 模型最难优化的场景。
**最不适合**：需要庞大现成组件库（Ant Design / MUI 等 React 生态）、需要第一方 RSC、团队人才池只有 React。

## 套利机会分析

- **信息差**：Solid 2.0 stable 发布才 3 天，社区文章几乎全是发布通稿。**真正的信息差在三个地方**：① 体积守卫的三层机制（双单位闸门 + 棘轮 + 冻结地板）在中文圈几乎无人讨论；② 世代戳 O(1) 边验证与 `seat.ts` 影子实现对拍；③ lane / MVCC 覆盖语义与 `attribution.ts` 因果归因链。这三块对任何做响应式系统、状态管理库或构建器的人都有直接迁移价值。
- **技术借鉴**：最值得抄的三件事——体积双单位闸门（任何以体积为卖点的库）、两阶段 effect（compute/apply）、影子实现对拍（状态机密集系统的测试策略）。V8 hidden-class 工程（`NODE-SHAPE.md`）对做大量小对象的 JS 系统同样适用。
- **生态位**：Solid 正在把自己从「一个有竞争的框架」重新定位为「一个被任意框架消费的响应式内核」。`@solidjs/signals` 独立成包意味着——**React 应用可以用 Solid 的信号引擎管理状态，而不用 Solid 的渲染模型**。这是一个被低估的、跨框架的生态位。
- **趋势判断**：符合趋势且**有后发优势**。行业正在向细粒度响应式收敛，Solid 8 年前就选好了这条路，现在是把实现质量做到极致的时候。但要注意「价值窗口」：2.0 stable 刚发布，star 收割正处高峰，真正的生态沉淀期预计在 2027 年上半年。现在读源码正当时（架构细节最全、文档最密集），但**现在写「Solid 值得用」的推荐文章为时过早**。

## 风险与不足

1. **2.0 的破坏性断层被普遍低估**。`MIGRATION.md` 有 1,100 行移除与替换指南，7 个核心 API 移除之外还有至少 12 项其他移除，JSX 语义也变了（`classList` 移除、属性/布尔前缀移除、`on` / `capture` 移除、`<Suspense>` → `<Loading>`、`onMount` → `onSettled`、`<Index>` → `<For keyed={false}>`、store setter 转 draft-first）。Hello World bundle 从 4.7 KB 涨到 9.8 KB。对存量用户是实打实的破坏。
2. **最常见静默性能陷阱：props 解构冻结响应性**。React 里 `{count}` 解构 props 完全正常，Solid 里必须用 `splitProps` / `omit`。因为追踪是隐式的，解构掉一个 props 后它就永远不再更新——不报错、不警告（只有 dev 模式下的 `STRICT_READ_UNTRACKED` 提示），只是默默不更新。这是迁移期最贵的坑。
3. **微任务批处理改变了同步读语义**。`setCount(1); count()` 在 2.0 里仍返回旧值。命令式集成代码、测试断言、第三方库对接都需要重新思考时序。
4. **文档密度是公认短板**（issue #167，116 条讨论，全库最高热度）。尽管 2.0 有 12 篇冻结的 RFC + 765 行 CHEATSHEET + `packages/signals/docs/` 内部设计记录，总量已达 94,961 行 Markdown——但**「有文档」和「好上手」是两回事**。
5. **单人依赖严重**。ryansolid 占 87.1% 的提交（4,271 / 4,901）。2.0 期间的高强度协作（23 个 RC、14 周、971 个 PR、753 个 issue 关闭）说明流程化能力在改善，但 bus factor 风险未被解决。
6. **超大源文件影响可维护性**。`attribution.ts` 4,908 行 / 213 KB 是全仓最大源文件，同目录还有 `scheduler.ts`（1,884 行）、`seat.ts`（1,717 行）、`store/store.ts`（129 KB）。极密集且质量极高的注释降低了阅读门槛，但新贡献者的进入门槛依然很高。
7. **没有第一方 RSC**。server components 仍是 RFC 状态，`packages/signals/src/core/` 里只有 frames transport。这是「大幅削减客户端工作」诉求的硬伤。
8. **编译期 fixture 只存输出不存输入**。`packages/compiler/__tests__/fixtures/dom/*/output.js` 有输出却没输入源码，想理解某个 transform 的读者看不到原始 JSX。
9. **本文未独立验证的性能数字**。Solid 核心 runtime 7.6 KB gzip、React 约 45 KB、1000 行表格 22.7ms vs 25.6ms 等来自外部来源；本仓库内可独立复核的只有 `scripts/size/floor-caps.json` 的 7.56 KB brotli 一项。

## 行动建议

### 如果你要用它

**适合**：高频交互 UI（看板、编辑器、实时协作）、对 bundle 体积敏感的场景、愿意为性能付出学习曲率的团队、嵌入式或边缘运行时。

**不适合**：依赖大型成熟 React 组件库的项目、需要第一方 RSC 的团队、团队人才池只有 React 的组织——**最后这一条往往比性能更能决定成败**，因为「理解 Solid 需要多久」和「团队约定成本」是真实的组织成本。

**如果用，要做三件事**：
1. 迁移前先读 `packages/solid/skills/solid-2.0/SKILL.md`（primer，8 KB 以内）和 `CHEATSHEET.md`——官方自己说这是为了对抗模型先验污染，值得逐条过一遍
2. 把 `splitProps` / `omit` 写进团队 lint 规则，堵住 props 解构这个最贵的静默陷阱
3. 开启 `attribution` 归因引擎。它是排查「为什么重跑了」的唯一高效手段，而 2.0 里它已经是一等能力

**对比竞品的选型口径**：如果你的团队已经标准化了 Vue 或 React 且没有强性能诉求，迁移到 Solid 几乎不划算——Vue → Solid 是范式级重写；Preact → Solid 是零成本但性能上限更低；Solid → Preact 极低迁移成本。只有在「更新粒度直接决定产品体验」的场景下，Solid 的优势才值得付迁移成本。

### 如果你要学它

**必读，按优先级**：

| 顺序 | 文件 | 学什么 |
|---|---|---|
| 1 | `packages/signals/docs/NODE-SHAPE.md` | V8 hidden-class 工程：39 → 29 字段、presence bits、冷字段扩展 `_x` |
| 2 | `scripts/size/README.md` + `gate.mjs` + `ratchet.mjs` + `floor-caps.json` | 双单位体积闸门 + 棘轮 + 冻结地板，**最值得直接抄走** |
| 3 | `packages/signals/src/core/graph.ts` | 世代戳 O(1) 边验证 |
| 4 | `packages/signals/src/core/seat.ts` | 影子实现对拍——用两份独立实现互相验证 |
| 5 | `packages/signals/src/core/lanes.ts` + `truth.ts` | MVCC 覆盖语义在 UI 状态系统里的落地 |
| 6 | `packages/signals/src/core/scheduler.ts` | 微任务批处理 + `flush()` 的边界处理 |
| 7 | `packages/signals/src/core/attribution.ts`（先读头部 200 行） | 因果归因引擎的架构：与 core 解耦的 observe-tier hook |
| 8 | `packages/compiler/src/shared/condition.rs` + `classify.rs` | 编译期条件提升、单一分类权威 |
| 9 | `documentation/solid-2.0/01-reactivity-batching-effects.md` | 2.0 的响应式哲学原文 |
| 10 | `AGENTS.md` | 依赖分层与文档权威顺序（`RULES-FUNDAMENTALS` > `RULES-DERIVED` > `SCENARIOS`，未决分歧进 `OPEN-QUESTIONS`） |

**如果只读一篇**，读 `scripts/size/README.md`。它是全仓工程成熟度最高的部分，而且**与框架技术栈无关**，任何团队都能直接借鉴。

### 如果你要 fork 它

**值得改进的方向**：

1. **超大文件拆分**。`attribution.ts`（4,908 行）应当按「ChangeRecord 记录 / 归因查询 / 交互归因 / feedback 统计」拆开，配合现有的 `attribution.prod.ts` 做生产裁剪
2. **补齐第一方 RSC**。`documentation/server-components/` 仍是 RFC，而这是当前最大的功能缺口，也是与 React 生态正面对撞时最缺的弹药
3. **补编译期 fixture 的输入源码**。只存 `output.js` 让 fixture 无法自解释，回归定位成本高
4. **补 ESLint 规则**。目前只有 Prettier + clippy + 类型测试。「props 解构冻结响应性」这种错误完全可以由 lint 规则静态捕获——这是迁移期最高频的坑，而 lint 是最便宜的防线
5. **扩大编译器分类的自动化**。`classify.rs` 是单一权威，但规则演进靠人工；可以加基于 fixture 的分类一致性回归测试

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | [deepwiki.com/solidjs/solid](https://deepwiki.com/solidjs/solid)（已收录，含完整子页结构；直接抓取会返回 429 Vercel 安全检查，需经搜索引擎索引确认） |
| Zread.ai | [zread.ai/solidjs/solid](https://zread.ai/solidjs/solid)（HTTP 200，但索引内容以使用 Solid 的第三方项目为主，未见核心库的独立深度中文手册） |
| 关联论文 | [The Event Loop That Wasn't: What Happens to a Reactive System When You Remove JavaScript](https://dlnext.acm.org/doi/abs/10.1145/3840562.3844970)（ACM DL, VMIL '26, DOI 10.1145/3840562.3844970）— 把 Solid 响应式核心移植到 Rust，**不需要 executor / futures / threads**，正是 2.0 Rust 化的学术背书<br>[Signal-First Architectures: Rethinking Front-End Reactivity](https://arxiv.org/pdf/2506.13815)（arXiv:2506.13815）— 直接以 Solid 的 signal 模型为基础提出「Signal-First Architecture」 |
| 在线 Demo | [playground.solidjs.com](https://playground.solidjs.com)（浏览器内跑 Solid 编译器，支持 DOM / SSR / hydration / universal 四种渲染模式对比）<br>[codesandbox.io/examples/package/solid-js](https://codesandbox.io/examples/package/solid-js) |
| 官方文档 | [docs.solidjs.com](https://docs.solidjs.com)（含 `llms.txt` / `llms-full.txt`）<br>仓库内 `documentation/solid-2.0/`（12 篇 RFC，2.0.0 发布时冻结为设计记录）+ `MIGRATION.md`（1,100 行） |
| 官方博客 | [Solid 2.0 – The Long Hold](https://www.solidjs.com/blog/solid-2-0-the-long-hold)（stable 发布公告）<br>[Solid 2.0 RC: The Big Reveal](https://www.solidjs.com/blog/solid-2-0-rc-the-big-reveal)（Rust 编译器性能数据）<br>[Async Solid – One Graph, Two Machines](https://www.solidjs.com/blog/async-solid-one-graph-two-machines)（异步架构） |
| 外部深度分析 | [Facing the Future: SolidJS's Challenges and Opportunities](https://www.mtechresearch.tech/facing-the-future-solidjss-challenges-and-opportunities)（2026-01-09，指出缺少第一方 RSC、DevTools 可视化弱、治理池小） |
