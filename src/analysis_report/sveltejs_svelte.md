# GitHub推荐：Svelte 89k star：十年两次推翻自己，把运行时请回来

> GitHub: https://github.com/sveltejs/svelte

## 一句话总结

Svelte 用一个编译器把声明式组件翻译成精准的 DOM 操作，十年里两次推翻自己的响应式架构——2019 年把组件级失效拆成 `$:` 静态分析，2024 年又从「编译期消灭运行时」退回到「编译期 + 运行时信号图」，并在 2025–2026 年把「一次更新」重写成可并发、可推测的 Batch 视图模型。

## 值得关注的理由

1. **它是「编译器消灭运行时」这条路线的活样本，也是一次公开的反悔**。Svelte 最早的立身之本是「Virtual DOM is pure overhead」，最硬的技术资产是 `dependencies.runtime = 0`（19 个依赖全是编译期依赖）。但 Svelte 5 的实现里，`internal/client/runtime.js` 有 1636 行、`reactivity/batch.js` 有 2004 行——一个 10 年前以「不送框架本身」为荣的项目，如今把运行时请了回来，而且用一份 `documentation/internals/decision-log.md` 逐条记录了这次反悔的理由、代价与被否掉的备选方案。**这份决策日志是全仓库最值钱、最可迁移的资产。**
2. **「Batch 视图模型」是本仓库最值得单独学的架构**。它把「一次更新」从「一次 flush」升级为「一个 batch」，多个 batch 可以同时在飞（因为有 pending 的异步工作），每个 batch 拥有一个自己的世界视图（overlay 值 + derived 缓存 + run 记录），彼此通过 merge / rebase 协调。配套的 `fork()` 把「推测性更新」做成一等公民，且 commit 时**刻意保留 fork 内分配的版本号**，使 fork 中已算出的 derived 结果在提交后依然有效。这是 React 19 `useOptimistic` 的完整形态。
3. **它同时是「怎么把架构承诺变成可执行断言」的范本**。零运行时依赖不是口号：`scripts/check-treeshakeability.js` 对 package.json 的每个 export 逐个 rollup 并断言 tree-shaking 后零残留；ESLint 自定义规则 `no_compiler_imports` 用源码文本扫描禁止运行时 import 编译器。**把架构边界写成 CI 断言，而不是靠 code review 自觉**，这条经验适用于任何声称「零依赖」的库。

## 项目展示

![Svelte - web development for the rest of us](https://raw.githubusercontent.com/sveltejs/svelte/main/assets/banner.png)

Svelte 官方 Banner。副标题「Web development for the rest of us」是创始人 Rich Harris 对整个项目的一句话定位。

![Svelte 官方暗色主题 banner](https://raw.githubusercontent.com/sveltejs/svelte/main/assets/banner_dark.png)

官方暗色主题变体（README 中通过 `<picture>` + `prefers-color-scheme` 自动切换）。

![Svelte 编译器工作原理动画插画](https://svelte.dev/_app/immutable/assets/svelte-machine-mobile.DtvNEgov.png)

官网首页的动画插画：一张「组件源码 → 编译器 → 精准 DOM 操作」的示意图，是理解 Svelte 核心命题最直观的一张图。

![Svelte Summit 社区合影](https://svelte.dev/_app/immutable/assets/summit.CCzKB27v.png)

Svelte Summit 社区活动实景。1,030 位历史贡献者、每年线下峰会，这是「志愿者驱动的开源旗舰」模式的社区侧写。

> [Svelte Origins 纪录片](https://www.offerzen.com/community/svelte-origins-documentary) — 官方首页挂出的十年回顾纪录片，适合作为「一个框架的十年」类内容的素材。

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/sveltejs/svelte（官网 https://svelte.dev） |
| Star / Fork | 89,780 / 6,222（Watcher 923；open issues 988、open PR 321） |
| 代码行数 | 200,405 行（tokei，不含空行/注释）。JavaScript 57.4%、JSON 16.6%、Svelte 16.3%、TypeScript 仅 6.6%（86 个文件）、CSS 0.9%。注释 34,162 行（占 17%） |
| 项目年龄 | 120.2 个月（组织创建 2016-11-20，首次提交 2016-11-15） |
| 开发阶段 | **密集开发**。近 365 天 771 次提交（≈2.1 次/天），近 90 天 173 次，近 30 天 43 次，最近一次提交就在 2026-11-19 |
| 贡献模式 | 开源组织主导 + 社区驱动。1,030 位历史贡献者，创始人 Rich Harris 独占约 30%–54%（取决于 git shortlog / API 贡献两种口径），核心 5–6 人按专长分工 |
| 热度定位 | 大众热门（Top-tier，低于 React 252k / Vue 212k），**版本驱动的周期性爆发**：2026 年 30 次上 GitHub Trending，4/7、6/29、7/3 三次登总榜第 1 |
| 质量评级 | 代码[优秀] 文档[优秀] 测试[充分] |

**关于版本号的一个坑**：仓库同时存在两条 tag 线——`v*` 前缀共 395 个，**冻结在 v3.59.2（2023-06-20）**；`svelte@*` 前缀共 641 个，从 `svelte@4.0.0-next.0` 起步，**当前版本是 `svelte@5.58.0`（2026-11-18）**，GitHub Release 也是 641 个。任何按 `v` 前缀排序取「最新版本」的脚本都会误报成 3.59.2——那只是一种已经停更三年的历史命名遗留。

**另一个值得注意的量化事实**：npm 周下载量 `svelte` 达 10,383,642（2026-11-12~18），已超过 star 数的 1.15 倍；`@sveltejs/kit` 5,523,695。**下载量超过 star 数，说明这是被真实生产依赖的库，而不是「收藏型」项目。**

## 作者视角：为什么存在这个项目

### 创始人/作者背景

**Rich Harris** 是英国前端工程师，但他的原始背景不是「前端框架」，而是**数据可视化 + 编译器**——他做过 Ractive（MVC 框架），做过 D3 衍生方向的可视化工作，写过 Observable 的可视化框架。Svelte 2016-11-20 成立（与首个 commit 同日），2018 年写下那篇定义性的《Virtual DOM is pure overhead》，2019 年「Svelte 3: Rethinking reactivity」，2023 年「Introducing runes」——官方自己的措辞是「Rethinking 'rethinking reactivity'」。

**这个背景在代码里留下了可验证的指纹**：`packages/svelte/src/compiler/phases/2-analyze/css/css-prune.js` 里的 `apply_selector()` 是一个**双向（FORWARD 找后代 / BACKWARD 找祖先）CSS 选择器匹配器**，支持 `:has` / `:is` / `:where` / 嵌套选择器 / `:global()`，还内嵌了 HTML 规范里 40 个「枚举值属性大小写不敏感」的白名单。这不是「写个正则删掉没用到的 CSS」，而是**实现了一个 CSS 引擎的匹配子集**——和可视化工具链里「哪些数据点被哪个选择器命中」是同一个问题。**作者从 A 领域带来的成熟解法，被原样移植进了 B 领域。**

核心团队按专长分工而非层级：**Conduitry**（编译与工具链）、**Tan Li Hau / T3RR**（Svelte 3/4 编译器与响应式）、**Simon H / dummdidumm**（SvelteKit 架构，现属 Vercel）、**Paolo Ricciuti**（现属 Mainmatter，主导 custom renderers 方向，2026-11-19 仍有 `docs: custom renderers (#19337)` 活跃提交）。Rich Harris 本人至今仍在写最底层的编译器 bug——2026-11-19 的 `fix: Writing through an object alias...` 属于编译器 alias 追踪这种只有原作者才会碰的深层问题。

### 问题判断

作者看到的不是「VDOM 太慢」，而是**「框架强制用户为不需要的抽象付费」**。这个判断的独特之处在于它同时是**技术判断**和**伦理判断**——一份外部深度分析把它进一步推演为：多 shipped 的字节对慢设备用户、弱网用户是转嫁的负担，在数十亿次页面加载下累积成能源消耗；因此「复杂度只需支付一次」，build step 是产品责任的一部分，而不只是附加工具。

**时机为什么是 2016 而非更晚**：Svelte 3（2019）赶上了三大框架集体把「编译期优化」当差异化叙事；Svelte 5（2024-10）赶上了 signals 在前端圈复兴（Preact Signals、Vue 的 `ref` 争议）——runes 本质上是「把 Solid.js 的信号图移植进编译器的产物格式」，但保留了编译期 CSS scoping 与模板静态化。**十年的时间点选择，恰好卡在两次行业共识转向的中间。**

### 解法哲学

1. **Unix 哲学式的极简**：package.json 的 exports 表是物证——除根入口外，每个都是**独立可单独引入的窄接口**：`./action` `./animate` `./attachments` `./compiler` `./easing` `./elements` `./events` `./legacy` `./motion` `./reactivity` `./reactivity/window` `./server` `./store` `./transition`（另有一组 `./internal/*` 内部逃生舱）。`svelte/reactivity` 里只有 `SvelteDate` / `SvelteSet` / `SvelteMap` / `SvelteURL` / `SvelteURLSearchParams` / `MediaQuery` / `createSubscriber` 七个公开导出，**没有一个是「框架」**。
2. **性能 vs 易用性的明确偏向：偏向性能，且用编译期换取**。`decision-log.md` 有一整节叫「Preserve common-case fast paths」，逐条记录了「早期实验在每次读取时记录版本、移除快速路径、给全局 run 包一层额外对象」各自带来多少开销，最终选择「版本在 run 结束时记录而非每次读取时记录」。**把实现优雅让位给热路径性能**，这是典型证据。
3. **零运行时依赖是硬约束，且被当作架构目标来守**：不是靠自觉，而是靠三道可执行守卫（见「关键设计决策」第 9 条）。
4. **明确不做什么**：custom renderer 组件直接列出不支持的能力——`bind:` on elements、transitions / animations、legacy `on:`、`{@html}`、`<svelte:head>` / `<svelte:window>` / `<svelte:document>` / `<svelte:body>`、`<svelte:options css="injected">`。**能力边界用编译期错误表达，而不是运行时静默降级。**
5. **官方引导而非强制**：SvelteKit 不预装 UI 库，CSS 框架与 TanStack Query 等交给社区。代价就是「内部 API 被生态当公共 API 用」的困境（见 #10359），但应对策略是维持产物格式兼容 + 逐库 drop-in 替代，而不是开放稳定内部 API。

### 战略图景

**核心编译器保持 MIT + 志愿者驱动 + 零商业包袱；商业化压力由应用层承接。** FUNDING.json 只有 ethereum drips（社区打赏），README 指向 Open Collective 众筹，且明确写明众筹款项仅用于「compensating expenses related to Svelte's development such as hosting costs」——**当前阶段不承诺用众筹养核心开发者的工资**。本仓库只含 `packages/svelte`（编译器 + runtime），SvelteKit 在独立仓库 `sveltejs/kit`（20,921 star）。Simon H 加入 Vercel、Paolo Ricciuti 属 Mainmatter 都是这个分工的自然结果。

**最大的战略赌注是 custom renderers**：如果成功，Svelte 从「一个前端框架」变成「一个 UI 编译器」——编译器前端（parse/analyze）服务任意后端，DOM 只是一个 renderer 实现。收益是**平台位**（目前无人占据：React Native 的 Fabric、Flutter 的 Impeller 都在自己的运行时里做，没做成可插拔的编译器后端）；成本是**必须把 DOM 从编译器架构里彻底剥离**。当前该特性仍在 `origin/svelte-custom-renderer` 分支上，编译器侧改了 39 个文件（+437/-76），文档自己标注「The API may change before the experimental flag is removed」。

## 核心价值提炼

### 创新之处

按新颖度 × 实用性排序：

1. **Batch 视图模型：并发更新各自拥有一个可见的世界**（新颖度 5/5 · 实用性 4/5 · 可迁移性 5/5）
   把「一次更新」建模为一个 Batch，Batch 拥有 overlay 的值（`batch_values`）、derived 缓存（`view_cache`）、run 记录（`records`）和被折叠的前序 batch（`folded`）。读路径在「赋值覆盖 → batch record → 全局 run → 现场重算」四级之间按视图语义挑选。多个 batch 可以并发在飞（因为 pending 异步），彼此通过 merge / rebase 协调。
   **适用场景**：任何需要「并发未完成更新、每个有自己的可见状态」的 UI 场景——乐观更新、路由预加载、并发请求竞态、协同编辑。React 19 的 `useOptimistic`、TanStack Query 的乐观更新都是它的退化形态。

2. **Fork：推测性更新 + 版本号保留的提交**（5/5 · 4/5 · 4/5）
   `fork(fn)` 提供隔离视图的推测执行；`commit()` 把 fork 的写入应用到真实世界，**且保留 fork 内部分配的版本号**——这是全仓库最精妙的一处实现智慧：如果版本号变了，所有在 fork 里算过的 derived 都会被判定过期并重算，fork 的价值当场归零。
   **适用场景**：路由预加载（预取 + 预渲染 + 提交）、表单乐观提交后与服务端对账、「先看看结果再决定要不要用」。

3. **可插拔渲染宿主（Custom Renderers）**（5/5 · 3/5（尚实验性）· 5/5）
   用统一的 Renderer 接口抽象「节点树 + 属性 + 事件」，编译器前端与 DOM 完全解耦；跨渲染器嵌套通过 guest.embed / host.host 双向协商协议解决，crossing 在 host 树里只留一个 host-owned 节点。**Svelte 是目前唯一把「多宿主渲染」做到编译器层的前端框架。**

4. **有序读依赖与通知边分离**（4/5 · 3/5 · 4/5）
   每个 reaction 同时持有 `deps`/`dv`（本次 run 按读取顺序的精确依赖与版本）和 `edges`（跨所有存活 run 的依赖超集，只用于通知）。late read（await 之后的读取）直接挂 edges 并立即建立通知关系；run 被替换时整体换掉 deps，通知图不受影响。**这是 fork / 多视图机制能成立的技术前提。**

5. **通过 `save()` 改写 await 以保留响应式上下文**（4/5 · 4/5 · 5/5）
   编译器把 `await a + b` 改写为 `(await $.save(a))() + b`。`save()` 在 await 前捕获 effect / reaction / component_context / batch 四个句柄，await 后恢复并返回续延函数；配套的 `unsave()` 保证「foreign microtask 永远不会跑在恢复的 reaction 上下文里」。这是异步与响应式正确性耦合这一经典难题的工程解。

6. **版本精确的新鲜度检查 + 「赋值覆盖的 derived」语义**（4/5 · 4/5 · 5/5）
   `is_dirty()` 区分三种状态：ASSIGNED（被赋值覆盖）用 `changed_since(deps, wv)` 判断「依赖是否在赋值之后被写过」；DIRTY 直接重算；MAYBE_DIRTY 逐个比较依赖版本（按读序短路）。同时 `rv`（read version）机制让「同一 run 内重复读同一 signal」与「上次读的依赖位置相同」都能走快路径而不分配新数组。

7. **编译器内的 CSS 选择器双向匹配器**（3/5 · 4/5 · 5/5）
   见「创始人背景」一节。**适用场景**：所有做组件级样式隔离的编译型框架（Vue SFC scoped、Marko、Astro），比运行时 CSS 匹配快一个数量级。

8. **`ExpressionMetadata` + `Memoizer`：把「表达式是否值得提取」建模为一等元数据**（3/5 · 5/5 · 5/5）
   analyze 阶段为每个表达式计算 `has_state / has_call / has_await / has_member_expression / has_assignment / dependencies / references / blockers`；transform 阶段的 `Memoizer` 据此把复杂表达式提取成 `$0/$1` 变量。**把「表达式是否响应式」当作类型系统式的一等元数据来传播**，而不是靠散落的布尔标志。

### 可复用的模式与技巧

1. **「精确版本比较」代替布尔 dirty 位** — 用「上次读到的依赖版本数组」与「当前视图下的依赖版本」逐项比较判断新鲜度。适用于任何带乐观更新、并发写入或多视图的响应式系统（Solid 的版本号是简化版，Preact Signals 的 epoch 是另一版）。
2. **「视图」作为第一等概念** — 把「当前可读到的值集合」抽象为 view，而非「全局状态 + 脏标记」。适用于缓存层（每请求一视图）、事务（每事务一视图）、协同编辑（每协作者一视图）。**Svelte 把这个概念从数据库/编译器领域搬进了 UI 运行时。**
3. **「记录（record）与全局状态分离」** — reaction 的全局 run 与 batch 内的 record 是两份数据，commit 时通过 `promote_record` 提升。适用于任何需要「回滚到上一状态」的缓存/计算系统。
4. **上下文捕获-恢复用于跨越 await** — 捕获 {effect, reaction, component_context, batch}，跨 await 恢复。数据库事务跨 await 保持上下文是同一模式。
5. **「把不应存在的状态显式拒绝」而非静默降级** — custom renderer 里 `bind:` / transitions / `{@html}` 直接编译期报错；错误信息内嵌 `https://svelte.dev/e/<code>` 文档链接。
6. **「先写决策日志，再写代码」** — `documentation/internals/decision-log.md` 逐条记录每个设计决策的**理由、被否掉的备选方案、代价**（例如：「Comparing values directly was considered, but would retain those values for the lifetime of a run and would need to preserve notification semantics for mutable values and stores」）。**适用于任何要在几年内持续演进且有大量贡献者的核心系统——这份文档本身就是 Svelte 最高价值的可迁移资产。**
7. **「已知缺陷文档 + 活跃回归样本」双轨** — `known-bugs-and-gaps.md` 明确区分「有 skipped 复现样本的已确认限制」与「需重新验证的旧报告」，每条附上对应的测试样本路径。比「拿 issue tracker 当文档」严谨得多。
8. **「守卫脚本 + lint 规则」把架构承诺变成断言** — 零运行时依赖、runtime 不引 compiler。适用于所有有架构边界约束的仓库。
9. **「读取顺序 + 版本数组」双缓冲依赖追踪** — `skipped_deps`（本次 run 与上次 run 的公共前缀，不重新分配）/ `new_deps`（新增部分），显著降低高频重算系统的 GC 压力。
10. **「组合式渲染器」与「宿主/客渲染器」握手协议** — guest 优先 `embed`，host 次选 `host`，都没有则报错。React Native 的 Fabric 是类似思路，但没做成编译器层可插拔。

### 关键设计决策

#### 1. 三层信号节点 + push-pull 混合的新鲜度检查

- **问题**：纯 push 会在无谓依赖上浪费重算；纯 pull 需要遍历全图找变化点。更棘手的是 runes 引入后，「哪些依赖变化了」不再是组件级问题，而是「在某个视图里，这个 derived 的这次 run 读到的版本是否还成立」。
- **方案**：每个 Value 带三个版本号——`wv`（write version，写入时的版本）、`rv`（read version，上次读取时的版本，用于同一 run 内去重）、`dv`（dependency versions，该 run 读到的每个依赖的版本数组）。写入时 push 标记失效（MAYBE_DIRTY），读取时 pull 校验依赖版本决定是否重算。
- **Trade-off**：每个节点多存 2 个数字 + 每个 run 多存一个版本数组；换来的是「派生值可以被赋值覆盖并在依赖变化时精确失效」——这是 Svelte 5.25 引入「derived 可写」后必需的能力，也是异步场景下正确性的基础。
- **可迁移性**：高。「按精确版本比较而非布尔 dirty 位」是任何带乐观更新/并发写入的响应式系统都该抄的。

#### 2. Batch：把「一次更新」从「一次 flush」升级为「一个可并发的视图」

- **问题**：Svelte 6 要支持的 async Svelte 里，最难的不是「await 能不能跑」，而是「await 期间的并发更新该看到什么」。React 的答案（Suspense + 丢弃整棵树重画）与 Solid 的答案（微任务级同步）都不够。
- **方案**：一次用户写入开启一个 batch；每个 batch 拥有一个「视图」——被 overlay 的值 + derived 缓存 + 本 batch 内产出的 run 记录。batch 之间可以 merge（折叠）、rebase（视图因他者提交而变化后重校验）。**「视图不是不可变快照」**——每次 batch 重新处理时重建视图，因此外部提交导致视图变化时只需 revalidate 局部失效。
- **Trade-off**：复杂度极高——`batch.js` 2004 行，决策日志用了整整一节讲「Separate committing writes from finishing all pending work」这类细节；文档明说实时世界「can be ahead of what is currently rendered」。**代价直接可见**：`known-bugs-and-gaps.md` 记录了两个「内容保留在屏幕外但已暂停」的活跃缺陷（async-if-branch-kept-offscreen-live / async-each-item-kept-offscreen-live，样本当前是 skipped）。
- **可迁移性**：高，但门槛也高。这是一个「乐观并发 UI」的通用架构——任何 UI 框架只要支持「并发多个未完成的更新，每个有自己的可见状态」，就需要这套东西。

#### 3. 编译期静态/动态切分 + expression memoization

- **问题**：模板里 `{a + b}` 这种表达式如果每次更新都重新 inline 展开会重复执行；含 await 的表达式如果 inline，编译器无法把它 hoist 成可复用的独立异步任务。
- **方案**：`ExpressionMetadata` 在 analyze 阶段标注每个表达式的元数据，`Memoizer` 据此决定是否提取为 `$0/$1` 变量（同步的变 `$.derived(() => expr)`，异步的变 `async_thunk(expr)`）。**注意用 `b.arrow` 而非 `b.thunk`**——注释说明原因：deferred async/template effect 必须读活的 binding 而非快照。静态元素判定 `is_static_element()`：无动态 fragment、无自定义元素、无事件属性、无不可静态设置的属性（value/checked/dir 等）→ 该元素完全进静态模板，运行时零成本。
- **Trade-off**：编译器复杂度与产物体积之间的取舍。Memoizer 让「哪些表达式该提取」成为可复用的小型策略对象，但也让 transform 阶段多了一层间接。
- **可迁移性**：高。这是「把运行时开销前移到编译期」的通用范式，Vue SFC、Marko、Astro 都有对应机制。

#### 4. CSS scoping：构建期剪枝 + hash 后缀，零运行时成本

- **问题**：传统 CSS scoping（Shadow DOM 或运行时插入 style + 属性选择器）要么需要 polyfill，要么有运行时成本，要么破坏全局样式。
- **方案**：编译期双向匹配选择器与模板元素，未被任何元素匹配的规则整条删除；命中的规则选择器加 hash class（`svelte-xxxx`，djb2 变体哈希），模板对应元素加同一 class。无法静态判定时用 `NODE_PROBABLY_EXISTS` 保守保留。
- **Trade-off**：选择器匹配不可能 100% 精确（动态 class、运行时注入的元素），静态剪枝可能误删「运行时才出现」的规则。但这是**纯收益型取舍**——省下的字节不占运行时。
- **可迁移性**：高。任何做组件级样式隔离的编译型框架都应实现这个。

#### 5. Async derived 的「首次值归属」协调

- **问题**：组件脚本里的 `await` 只会让脚本**继续一次**，而其后的反应式表达式可以在多个视图里更新。因此「第一个 await 出来的值」必须绑定到「继续这个脚本的那个 batch」——若让最先 resolve 的结果恢复脚本，会把不同 batch 的值混在一起。
- **方案**：`async_expression` 维护三个角色——`runner`（创建该表达式的 runner）、`resolver`（「谁提供第一个值」的 batch）、`waiting`（缓冲中的后续结果）。结果到达时若 resolver 已定且 merge_target 不同，则 push 进 waiting 等合并后再释放；第一个被接受的 batch 执行 `runner.switch(batch)`，让脚本在自己的视图里继续读值。
- **Trade-off**：复杂度集中在 `deriveds.js` 的 `async_expression`（约 180 行），需要 resolver / waiting / merge_target 三套状态协同。收益是「await 之后再读 state 依然是响应式的」。
- **可迁移性**：中高。「恢复上下文而非重新订阅」+「首次值归属」两个模式对任何想在 async 函数里保持响应式的框架都适用。

#### 6. 「零运行时依赖」的三重可执行守卫

- **问题**：运行时依赖 0 是 Svelte 最硬的技术资产，但极易在无意中破坏——一次随手的 import 就可能把 acorn 或 zimmerframe 拖进浏览器 bundle。
- **方案**：(a) package.json exports 精确到 15 个公开子路径，每个是窄接口（外加 `./internal/*` 一组内部逃生舱）；(b) `scripts/check-treeshakeability.js` 对每个 export 逐个 rollup，断言 tree-shaking 后零残留，构建脚本强制执行；(c) ESLint 自定义规则 `no_compiler_imports` 扫描 `packages/svelte/src/**`（compiler 除外）的源码文本，出现 `'../compiler/'` 或 `'#compiler'` 即报错——理由写在规则注释里：防止编译器被打进产物，以及防止 TypeScript 拾取到不该在浏览器存在的 ambient types。
- **Trade-off**：规则用字符串搜索而非 AST（注释承认理论上可能误报），但对性能与误报率而言是正确的取舍。
- **可迁移性**：高。用 lint 规则守住架构边界是零依赖库的通用做法（类比 Rust 的 no_std 检查、Go 的 import guard）。

#### 7. 代理化 `$state` 的「不可描述属性」防御

- **问题**：Proxy 的 invariant 要求——如果目标对象自身有不可配置、不可写、不可枚举的属性，代理必须如实报告该属性。Svelte 的代理把属性存在内部的 sources Map 里，目标对象的真实属性被隐藏了；一旦用户 defineProperty 一个 accessor 或 freeze 对象，就会破坏 Proxy invariant，产生难以追踪的 TypeError。
- **方案**：只接受「普通」描述符（必须有 value，configurable/enumerable/writable 都为 true），否则抛 `state_descriptors_fixed` 错误。同时 proxy 只对 plain object / plain array 生效（class 实例原样返回）。**「forkable 的要求直接写进了错误信息里」——代理没有把写落到 target 上，正是为了让 fork 能隔离状态。**
- **Trade-off**：用户不能用 getter/setter 做响应式对象成员；换来「state 可以被 fork」这一核心能力。
- **可迁移性**：中高。Proxy + 内部存储的「可 fork 状态」是稀缺能力，这个 invariant 冲突的分析方法可迁移到任何用 Proxy 做响应式的库。

#### 8. 依赖图的可断可连（CONNECTED 标志）

- **问题**：长期运行的 SPA 里，组件反复挂载/卸载会留下大量「无人依赖但仍持有依赖链」的 derived，形成内存泄漏。
- **方案**：derived 节点带 `CONNECTED` 标志。当没有任何 effect 依赖某个 derived 时它被从图中断开（可 GC 或稍后重连）；一旦有 effect 依赖则重新连上。断开状态下的 derived 保持「可疑」（MAYBE_DIRTY），以便重连时能正确判断是否需要重算。配合 `prune_edges` 修剪通知图中的无用连接。
- **Trade-off**：一个 bit 的状态管理成本，换来 derived 的可回收性。
- **可迁移性**：高。任何长生命周期的信号系统都需要「无订阅者的计算单元回收」策略。

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | Svelte | Solid.js | Qwik | React / Vue |
|------|---------|--------|--------|--------|
| 核心路线 | 编译期 + 运行时混合 | 纯运行时细粒度信号 | 可恢复性（无 hydration） | VDOM（React）/ 组件级依赖收集（Vue） |
| 运行时依赖 | **0** | 有（信号运行时） | 有（Qwik runtime） | 有 |
| 更新粒度 | 表达式级（derived / effect） | 表达式级 | 事件级按需唤醒 | 组件级（memo 可缓解） |
| 样式隔离 | **编译期剪枝，零运行时成本** | 无（完全外置给用户） | 无 | Shadow DOM / scoped 运行时 |
| 异步模型 | Batch 视图 + fork（实验性，最完整） | 微任务级同步 | QRL 懒加载 | Suspense / 顶层 await |
| 多宿主渲染 | **编译器层可插拔（实验分支）** | JSX 可渲染任意目标（但非编译器层） | 不支持 | React Native 有（运行时层） |
| Star | 89,780 | 36,781 | 22,078 | React 252,784 / Vue 212,515（vuejs/core 55,048） |
| 生态完整度 | 中（SvelteKit 强，企业 UI 套件弱） | 中低 | 低 | **压倒性领先** |

### 差异化护城河

1. **信任护城河（最强）**：10 年、11,489 次提交从未中断、MIT、零运行时依赖、依赖可执行守卫、decision-log 与 known-bugs 文档、3,146 个测试样本、CI 覆盖 5 个 OS × Node 矩阵。**一个 10 年没有断更、且把设计理由写进仓库的框架，在「关键路径基础设施」这个位置上具备极高可信度。**
2. **技术护城河（真实但正被侵蚀）**：编译期 + 运行时的混合优化——CSS 剪枝、静态元素提取、细粒度 signal DAG，这套组合目前只有 Svelte 同时具备。但护城河在变薄：Solid 证明了纯运行时信号模型也能很快，React Compiler 在把 React 推向同样方向。**Svelte 的独有区（编译期零成本样式隔离 + 模板静态化）比它的信号实现更难被复制。**
3. **生态护城河（最弱）**：SvelteKit 之外没有 Svelte 版的企业级 UI 套件，shadcn-svelte / Bits UI / Skeleton 等社区库活跃但体量远小于 MUI / Ant Design。**这是 Svelte 在企业市场的真正瓶颈——不是技术，是招聘和交接。**
4. **新护城河（在建设中）**：custom renderers 若成功，会把护城河从「Web 前端框架」扩展到「通用 UI 编译器」，这个位置目前无人占据。

### 竞争风险

1. **最大风险来自 React Compiler**：如果自动 memoization 成熟，React 的「运行时开销」这一唯一硬伤被抹平，Svelte 的性能叙事就失去说服力——而 Svelte 剩下能打的只有 DX 与生态。**有趣的是，React 团队自己在推进 React Compiler，方向上等于承认了 Svelte 的论点。**
2. **Solid 的纯度优势会侵蚀「高级用户」**：Svelte 5 的 batch / view / record / fork 四层概念叠加后，复杂度已经接近 Solid 的纯运行时复杂度，但收益不如 Solid 直接。如果「细粒度响应式」成为行业共识，Svelte 的编译器层会显得像包袱。
3. **Qwik 抢占 SSR 性能心智**：在「首屏指标就是一切」的场景，resumability 是结构性保证，而 Svelte 的「快」是实现优化的结果。
4. **内部风险**：`batch.js` 2004 行 + 两个活跃的 offscreen-paused 缺陷，说明 async / batch 系统的复杂度已接近团队当前掌控力的边界。**若 Svelte 6 转正 async 而这些缺陷未解，会是信任伤害。**

### 生态定位

**「编译期优化的专业前端框架 + 通用 UI 编译器的孵化场」**。它不打算赢下 React/Vue 的存量竞争（社区规模差距是数量级的），而是双轨作战：(a) 守住「愿意为极致 DX 与性能付溢价的小团队、独立开发者、内容站点、渐进增强 SSR 场景」；(b) 通过 custom renderers 把自己从「Web 框架」升维为「跨平台 UI 编译器」，在 React Native / Flutter / Electron 各自为政的空白地带开辟新战场。

**用户迁移成本速查**：React → Svelte **高**（hooks 依赖数组 vs 自动追踪是两种心智；JSX → 模板要重写；React 生态组件库大多无 Svelte 等价物——这正是 #10359 类兼容问题的根源）。Vue → Svelte **中**（模板几乎可逐行迁移，`ref`/`computed` ↔ `$state`/`$derived` 映射清晰，但 `watch` ↔ `$effect` 语义不完全等价，Pinia / VueUse 需重找替代）。Preact → Svelte **低**（团队心智不必变，但组件仍要重写）。

## 套利机会分析

- **信息差**：**几乎没有低关注度空间**——89,780 star 已是既定事实，「低星高质」的机会不存在。但存在**版本驱动的周期脉冲**：SvelteKit 3（2026-10-01 正式）+ `sv` CLI 1.0 同批发布、Svelte 6 移除 legacy API 与 `experimental.async` 转正、custom renderers 推进——**每一次换代都是一个内容窗口**，且 2026 年 30 次 Trending（3 次总榜第 1）、11-19 单日 +692 star 说明它仍在主动争夺注意力。真正的信息差在于：**大部分人只看到「Svelte 5 更快了」，看不到「Svelte 5 把编译期信条改成了运行时信条」这个范式反转**。
- **技术借鉴**：五项可直接迁移——① 「精确版本比较代替布尔 dirty 位」；② 「视图作为第一等概念」；③ 「记录与全局状态分离」；④ 「上下文捕获-恢复跨 await」；⑤ 「守卫脚本 + lint 规则把架构承诺变成断言」。另加一份通用方法论：**先写决策日志再写代码**。
- **生态位**：填补「Web UI 框架」与「通用 UI 编译器」之间的空白。custom renderers 落地后，终端 UI（Ink 风格）、原生移动（Lynx.js）、3D（Threlte）、PDF 生成都不必再各自造一套模板编译器。
- **趋势判断**：增长仍在（近 5 个月 +2.8%，日均 +15 star；周均 +310，某周 +1,021），且**后发优势明显**——它经历了 Vue 3 和 React 没经历过的「第二次范式转移」，并且公开记录了这次转移的代价。后发劣势则在生态与人才储备上是数量级的差距（React 252k vs Svelte 89.8k）。**Svelte 5 的经验对正在做类似迁移的框架（尤其 Vue 3 的 Vapor mode、React Compiler）有教科书价值。**

## 风险与不足

1. **生态兼容债未清偿**：#10359（**至今 OPEN**，82 条评论）——`svelte/internal` 被大量第三方库当公共 API 使用（issue 中点名 `@tanstack/svelte-table`、shadcn-svelte 的 cmdk-sv），内部 API 在 runes 重构后全部变更。维护者被迫逐个建档、判定「不可能全部兼容」并手写 drop-in 替代。**这是「编译器型框架的内部 API 一旦被生态当公共 API 用，架构重构就会被第三方绑架」的教科书案例**，也是 Svelte 5 迁移至今仍有阻力的直接原因。
2. **零 refactor 信号**：近 200 次提交中 fix 占 61.0%、feature 仅 7.0%、**refactor 恰为 0.0%**。对刚在 2024 年完成大重写的项目，连续零重构是异常的。合理解释是「重写已一次性做完、现在处于稳定化期」；**但如果持续零 refactor 而 issue 积压继续上升（988 open issues，平均关闭时长约 61 天），就需要重新评估架构健康度**。
3. **复杂度已经溢出**：`batch.js` 2004 行 + 两个活跃的 offscreen-paused 缺陷。Svelte 5 的 batch/view/record/fork 四层概念叠加后，「为什么我的 UI 没更新」的排查难度显著上升——**这正是纯运行时方案（Solid）相对 Svelte 的真实优势**。
4. **技术债的卫生问题**：仓库同时保留 `package-lock.json`（295 次修改）与 `pnpm-lock.yaml`（212 次修改），npm → pnpm 的迁移完成但旧 lock 未清理；新旧文档站双轨并存（`sites/svelte.dev` 1,369 + `documentation/content` 1,098 + `documentation/docs` 873 vs `site/content` 2,971 + `site/src` 1,014 + `site/static` 881）；编译器新旧架构并存（`src/compiler` 2,589 + `src/generators` 2,585 vs v3 遗留的 `src/compile` 1,184）。**核心开发焦点 100% 集中在框架本体，这些清理债始终没被排上日程。**
5. **API 债**：#3105「Change body class via `<svelte:body />`」——2017 年提出、**至今 OPEN**、82 条评论，一个极基础的需求开了近 9 年，至今无法用 runes 优雅表达。这是「Svelte 5 移除 legacy API 后、非组件级 DOM 操作表达能力不足」的活体样本，也侧面说明 Svelte 6 清理 legacy API 时会再撕开一批口子。
6. **商业化与治理**：核心编译器明确不承诺众筹养核心开发者工资，商业化压力全压在应用层（SvelteKit）。这在信任上是加分（MIT + 纯志愿者驱动），但在**核心维护者稳定性**上是长期风险。
7. **组织风险**：生态规模与人才池远小于 React/Vue，企业级选型时这是硬伤。外部深度分析给出的判断值得引用：**「Svelte 生态小是组织风险」**——大型企业理性上仍应选 React。

## 行动建议

- **如果你要用它**：追求最小 bundle、最小心智负担、且团队有能力接受「编译器心智」的中小团队 / 内容站点 / 工具类应用，选 Svelte。要企业级组件库、招聘池、供应商支持、跨端（React Native）——选 React。已经在用 Vue 且想要更小的运行时——Svelte 是合理替代，但 Pinia/VueUse 生态要重新找落点。**切勿在有大量 `svelte/internal` 依赖的存量项目上直接升 Svelte 5**，#10359 不是修完就能过的。
- **如果你要学它**（这是本仓库最大的价值）：
  - `documentation/internals/decision-log.md` — **先读这个**。每个设计决策的理由、被否掉的备选方案、代价，以及「历史包袱」记录。这是全仓库最值得逐字读的文件。
  - `documentation/internals/reactivity-overview.md` — 概念导览，建立心智模型的入口。
  - `documentation/internals/known-bugs-and-gaps.md` — 怎么给一个异步/并发系统写缺陷文档的范本。
  - `packages/svelte/src/internal/client/reactivity/batch.js`（2004 行）+ `runtime.js`（1636 行）— Batch 视图模型与版本精确新鲜度检查的实现。
  - `packages/svelte/src/compiler/phases/2-analyze/css/css-prune.js` — 双向 CSS 选择器匹配器。
  - `packages/svelte/src/compiler/phases/nodes.js` 的 `ExpressionMetadata` + `phases/3-transform/client/visitors/shared/utils.js` 的 `Memoizer` — 编译期表达式提升策略。
  - `packages/svelte/scripts/check-treeshakeability.js` + `eslint.config.js` 的 `no_compiler_imports` — 把架构约束写成断言。
- **如果你要 fork 它**：技术上没有好的理由 fork 编译器本身（MIT + 生态齐全）；**真正值得 fork 的是 `batch.js` 这套 Batch/View 模型本身**——把它抽成独立库，接进你自己的 UI 层（任何支持乐观更新 + 并发未完成请求的场景都能用）。另一个方向是 custom renderers：这是官方尚未合并的分支（`origin/svelte-custom-renderer`，编译器侧改了 39 个文件），抢先实现一个非 DOM 宿主（终端 / WebGL / PDF）是最有价值也最有风险的切口。

### 知识入口

| 资源 | 链接 |
|------|------|
| **内部架构文档**（最推荐） | `documentation/internals/` — `decision-log.md` / `reactivity-overview.md` / `known-bugs-and-gaps.md`（仓库内，226 行合计） |
| 官方文档 | https://svelte.dev ；面向 LLM 的纯文本入口 https://svelte.dev/docs/ai |
| 在线 Demo | https://svelte.dev/playground（官方 REPL，可分享） |
| DeepWiki | 未确认（https://deepwiki.com/sveltejs/svelte 返回 HTTP 429，无法判定收录状态） |
| Zread.ai | 未收录（https://zread.ai/sveltejs/svelte 返回 HTTP 403） |
| 关联论文 | 无 Svelte 自身的 arXiv 论文。最接近：[The State of Disappearing Frameworks in 2023](https://arxiv.org/abs/2309.4188)（把 Svelte 归入「消失的框架」一族）、[Signal-First Architectures: Rethinking Front-End Reactivity](https://arxiv.org/abs/2506.13815)（信号优先架构，Svelte 5 runes 的理论近亲）。**架构知识沉淀在官方 blog + `sveltejs/rfcs` 仓库，而非论文——这本身就是一个信号：它是工程驱动的项目，不是学术驱动的** |
| 官方博客 | https://svelte.dev/blog（Svelte 3 → 5 → 6 的完整架构演进史，可查） |
| RFC 流程 | https://github.com/sveltejs/rfcs |
