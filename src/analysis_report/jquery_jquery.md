# GitHub推荐：6 万 star 的 jQuery：20 年老库如何用减法重写

> GitHub: https://github.com/jquery/jquery

## 一句话总结
一个服役 20 年、装在 62.9% 全球网站上的前端库，正在用「只删不加」的方式完成它的最后一次自我重写——删掉自研选择器引擎 Sizzle、砍掉 13 个已废弃 API、把 AMD 源码换成 ES Module，并正式把「维护存量代码」当成一门生意。

## 值得关注的理由

1. **一份罕见的「遗留库瘦身」工程案例**：jQuery 4.x 做的是减法，不是加法——移除 `isArray`/`parseJSON`/`trim`/`type`/`now`/`unique`/`nodeName`/`fx.interval`/`camelCase`/`cssProps`/`isFunction`/`isNumeric`/`isWindow` 等 13 个已废弃 API、删掉未文档化的原型方法 `push`/`sort`/`splice`、把自研选择器引擎换成原生 `querySelectorAll`。任何维护过长生命周期的系统的人，都能从这份「如何有尊严地砍掉自己」的工程里学到东西。
2. **技术护城河已近于零，但商业护城河极深**：W3Techs 数据显示 jQuery 在全网网站的使用率正从 72.1%（2025-11）跌到 62.9%（2026-11），同期 Bootstrap 从 19.4% 涨到 25.8%、Next.js 从 2.0% 翻倍到 4.0%——**旧世界的收缩速度，几乎等于新世界的扩张速度**。但 npm 上 jQuery 仍有 7,141 万次月下载，官方把旧版本商业支持外包给 HeroDevs 和 TuxCare。技术在被替代，维护被变现。
3. **「兼容层」模式依然没过时**：jQuery 从不嗅探 UA，只做运行时能力探测；探测结果用函数而非布尔（惰性 + 一次性成本）；浏览器行为不可靠时，构造离屏元素做真实布局测量来判定。这套三件套是本项目最值得迁移的资产。

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/jquery/jquery |
| Star / Fork | 60,022 / 20,709（Watcher 3,114） |
| 代码行数 | 52,875（JavaScript 75.0%, JSON 21.2%, HTML 2.8%）——tokei 口径，不含空行与注释；JSON 多为 package-lock 噪声，核心源码 `src/` 实为 138 文件 10,547 行 |
| 许可证 | MIT |
| 依赖数量 | **运行时 0 个**，开发依赖 33 个（package.json） |
| 项目年龄 | 248.2 个月（首次提交 2006-03-22「Inital Import.」，GitHub 仓库建于 2009-04-03） |
| 开发阶段 | 稳定维护（近 30 天 10 次 commit，近 365 天 81 次；2011-04 曾达月均 224 次的历史峰值） |
| 贡献模式 | 社区驱动但决策集中（358 位历史贡献者，John Resig 占 19.3%，核心 Top 4 约占 65%） |
| 热度定位 | 大众热门（存量型）——npm 月下载 7,141 万次，W3Techs 全网覆盖率 62.9%，但增量归零 |
| 质量评级 | 代码[优秀] 文档[优秀] 测试[充分] |

## 作者视角：为什么存在这个项目

### 创始人/作者背景
jQuery 挂在一个**组织账号**下（不是个人号），账号年龄 17.6 年，名下 65 个仓库构成了一条完整的产品链：`jquery.com`（官网内容）、`api.jquery.com`（API 文档）、`jquery-dist`（发布分发）、`codeorigin.jquery.com`（CDN）、`healthyweb.org`（版本健康检查服务）、`jquery-migrate`（迁移工具）、`jquery-wp-content`（WordPress 站点托管）。

创始人 John Resig 的关键背景知识来自 Prototype.js——他 2006 年写的《Pro JavaScript》系统剖析了 Prototype 的 DOM 扩展思路，并批评它「和浏览器 DOM 混在一起分不清边界」。jQuery 的答案是：**只包 DOM，不重造 DOM**。这个取舍直接决定了它此后的全部 API 形态（`$()` 返回类数组对象而非真数组、`.each`/`.map` 而非 ES5 迭代协议、`jQuery.fn` 插件机制）。

### 问题判断
**2006 年的时机**不是「JavaScript 很酷」，而是「IE6 与 Firefox 的 DOM 差异让所有人痛苦」。当时 Prototype、Dojo、MooTools 各用一套私有抽象，且都不解决跨浏览器差异。jQuery 的差异化不是「功能更多」，而是把**兼容矩阵由一个人（团队）集中承担，而不是由每个使用者的每次调用承担**。

**2026 年还在做 4.x** 的理由不是加功能，而是三条：

- 偿还技术债的确定性收益——每个 major 净删除而非新增，直接缩小攻击面与 API 表面积；
- 更新安全姿态——JSON 不再自动提升为 JSONP、脚本不再自动执行、异步请求改走 `<script>` 标签以避免 CSP 报错，这是把「隐式执行远端代码」这类反模式从 API 里铲除，而不是加一个开关；
- 模块化构建让「减法」成为可能——`build/tasks/lib/slim-exclude.js` 排除 `ajax/callbacks/deferred/effects/queue` 五个模块，slim 构建降到 19.4KB gzip（实测 `jquery.slim.min.js` 56,030 字节 → gzip 19,387 字节；完整版 `jquery.min.js` 78,965 字节 → gzip 27,491 字节）。这种裁剪在 AMD 时代做不到，因为 AMD 模块的依赖是运行时硬连的。

### 解法哲学
一以贯之的**「减小默认表面积」**，可以在 API 层、构建层、内部层三个层面同时观察到：

- **API 层**：每个 major 净删除而非新增。4.0 移除了 13 个已废弃 API（`jQuery.isArray`/`parseJSON`/`trim`/`type`/`now`/`unique`/`nodeName`/`fx.interval`/`camelCase`/`cssProps`/`isFunction`/`isNumeric`/`isWindow`），并删掉未文档化的原型方法 `push`/`sort`/`splice`——这意味着承认「未文档化 ≠ 不被依赖」，并选择主动断裂而非继续承担。**关键在于节奏**：这批 API 早在 3.0 就被标记废弃，官方整整给了一个 major 版本的预警期才真正移除，中间还配了 jQuery Migrate 做过渡。对比一下——很多库是「发个 minor 就删」，jQuery 是「预告一整个世代再删」。
- **构建层**：`--exclude` 是一等公民。README 详细列出每个模块可排除以及连带移除的依赖图，模块化的真实含义不是把代码拆成文件，而是让依赖关系**可被机器推导**。
- **内部层**：`src/var/` 把 `slice`/`push`/`indexOf`/`sort`/`splice`/`toString` 全抽成单行常量引用，让 minifier 能识别为可重命名的稳定标识符，同时保留 IE11 fallback 的**唯一注入点**。

**明确选择不做什么**（比「做了什么」更能说明价值观）：

- 不在 `.on()` 暴露 `passive`/`capture` 选项——[#2871](https://github.com/jquery/jquery/issues/2871) 从 2016 年 open 至今，因为塞进 `EventListenerOptions` 会让 API 表面积扩张。这是一次「**用不支持来避免膨胀**」的取舍。
- 不提供 Deferred 的替代方案——4.0 的 slim 构建直接删掉 callbacks/deferred/queue 这套异步编排能力，官方只提示「用原生 Promise」。这是「不因为自己的 API 被淘汰而焦虑」。
- 不追 CSS4 `:is` 的完整支持——[#4886](https://github.com/jquery/jquery/issues/4886) 自 2021 年 open 至今，官方没有为了补齐而重开自研引擎。

### 战略意图
jQuery 本身是 MIT 无付费层，**不是 open-core**。但官方 README 已把旧版本商业支持明确外包给 [HeroDevs](https://www.herodevs.com/support/jquery-nes) 与 [TuxCare](https://tuxcare.com/lp/click-jquery-support/)（4.1.0 的 changelog 还专门新增了 TuxCare 条目）。这意味着：

> **「维护一个跨世代遗留库」本身已经被当成一门生意在经营**——免费的是当前版本，旧版本支持是付费服务。

2026-11-17 的 4.1.0 / 3.8.0 联合发布，官方博客标题是《Passing the Torch》（移交火炬）：**3.8.0 是 3.x 分支最后一个计划中的功能版本**，此后 3.x 只收 critical 安全/缺陷修复，活跃开发全部落在 4.x。同时刻意不给 5.0 时间表——既避免制造「必须立刻升级」的恐慌，又保留了「IE11 在 5.0 移除」的选项（官方 [browser-support 页面](https://jquery.com/browser-support/) 当前仍列出 IE11 支持，但限定标准模式与 Edge IE 模式；IE10 及更早已终止）。

## 核心价值提炼

### 创新之处

1. **构建期虚拟文件覆盖实现模块裁剪**（新颖度 4/5，实用性 5/5，可迁移性 5/5）
   用一个 30 行的 Rollup 插件 `build/tasks/lib/rollupFileOverridesPlugin.js` 把被排除模块的源码替换成空字符串，把 `selector.js` 替换为 `selector-native.js`。依赖关系用声明式 `removeWith` 表推导，而非硬编码：

```js
const removeWith = {
    ajax: [ "manipulation/_evalUrl", "deprecated/ajax-event-alias" ],
    callbacks: [ "deferred" ],
    css: [ "effects", "dimensions", "offset" ],
    deferred: {
        remove: [ "ajax", "effects", "queue", "core/ready" ],
        include: [ "core/ready-no-deferred" ]
    },
    selector: [ "css/hiddenVisibleSelectors", "effects/animatedSelector" ]
};
```

   注意 `deferred` 那条：移除 Deferred 会连带移除 ajax/effects/queue，并**自动换上 `core/ready-no-deferred`**——这是源码层面的「接口替换」，不是运行时降级。同一份源码由此产出 8 种发行变体（complete/slim × script/esm × normal/factory），`package.json` 的 `exports` 字段用 `node`/`module`/`import`/`default` 四路精确映射。
   **适用场景**：任何需要「核心 + 可选插件组」多形态发行的库。

2. **用社区官方一致性测试套件验证自研异步原语**（新颖度 4/5，实用性 5/5，可迁移性 5/5）
   jQuery Deferred 推出于 2010 年，比原生 Promise 早 4 年。4.x 让它的 `then()` 严格对齐 Promises/A+，代码里逐条标注条款号与规范链接：

```js
// Support: Promises/A+ section 2.3.3.3.3.3
// https://promisesaplus.com/#point-59
```

   更关键的是验证方式——不是自写测试，而是把它包装成 adapter 接入社区官方套件（`test/promises_aplus_adapters/deferred.cjs`），由 `npm run test:promises_aplus` 在 CI 中运行。**把「我说我兼容」变成「第三方套件证明我兼容」**。
   **适用场景**：任何自研的、声称兼容某个既有标准的实现（序列化格式、协议栈、加密算法）。

3. **原生优先 + 能力探测闸门 + 自研 fallback 的三轨选择器引擎**（新颖度 3/5，实用性 4/5，可迁移性 5/5）
   4.x 把 `querySelectorAll` 作为快路径，但没丢掉自研层：

```js
// qSA considers elements outside a scoping root when evaluating child or
// descendant combinators, which is not what we want.
// In such cases, we work around the behavior by prefixing every selector in the
// list with an ID selector referencing the scope context.
```

   IE 11 不支持 `:scope` 可靠工作，改用「临时给 context 挂 expando id、用完移除」的技巧。配套还有 `rbuggyQSA` 能力探测闸门（匹配到已知有问题的选择器就跳过快路径）和 `nonnativeSelectorCache`（记住失败选择器并回退自研引擎）。4.1.0 最后一刀彻底弃用 `getElementsBy{Tag,Class}Name`（[#3642](https://github.com/jquery/jquery/issues/3642)，commit `53a2bcf9`）——理由是 IE 11 的 gEBTN 在克隆节点上找不到 MathML 元素，且 gEBTN 返回 live collection 必须 snapshot 成静态数组，而 qSA 直接返回静态 NodeList。
   **适用场景**：任何「自研实现 → 平台原生」迁移中不可一次性切换的场景。

4. **`special` 钩子表：把浏览器行为差异数据化**（新颖度 4/5，实用性 4/5，可迁移性 5/5）
   `jQuery.event.special[type]` 支持 `setup`/`teardown`/`preDispatch`/`postDispatch`/`handle`/`_default`/`delegateType`/`bindType` 七个钩子，把「哪些事件在哪些浏览器上行为不同」从散落的 `if (isIE)` 变成一张可查表。`setup` 返回 `false` 即接管标准路径。
   **适用场景**：事件系统、消息总线、ORM 的类型适配层、多云 SDK 的服务差异抽象、支付网关的渠道差异处理。

5. **`support` 探测表 + 惰性测量 + 真实布局验证**（新颖度 4/5，实用性 4/5，可迁移性 4/5）
   jQuery 的探测值是**函数**而非布尔，调用时才执行探测（探测本身有成本）。判据不是查文档，而是构造离屏 table 做真实布局测量，用 `table = null` 做已探测哨兵：

```js
reliableTrDimensionsVal = Math.round( parseFloat( trStyle.height ) +
    parseFloat( trStyle.borderTopWidth ) +
    parseFloat( trStyle.borderBottomWidth ) ) === tr.offsetHeight;
```

   注释里详列了 Firefox 135+ 恒把 `span` 宽度算作 1、Safari 18.3+ `col` 计算宽度恒为 0 的具体缺陷。IE 的处理尤其诚实——直接写「因缺乏可行 workaround，我们接受这个限制，把 IE 视作通过测试」（`isIE ||`）。**把已知无解的限制显式写进注释并接受，比假装支持更诚实**。

6. **安全收紧通过改默认传输而非加开关**（新颖度 3/5，实用性 4/5，可迁移性 5/5）
   4.0 把「隐式执行远端代码」从 API 里铲除：异步脚本改走 `<script>` 标签（commit `07a8e4a1` 的原话是「makes it also used for all async requests to avoid CSP errors arising from usage of inline scripts」）、JSON 不再自动提升为 JSONP、`parseHTML` 默认用 `DOMParser` 构造惰性文档不执行脚本、`DOMEval` 保留 `nonce`/`noModule`/`crossOrigin` 属性。**全程没有新增任何配置项**。
   遗留问题是同步脚本加载仍走 XHR+eval——因为 `<script>` 标签无法同步，commit message 直接承认「For sync requests such a change is impossible」。

7. **`uniqueSort` 的双指针原地压缩去重**（新颖度 2/5，实用性 5/5，可迁移性 5/5）
   4.1.0 把去重从「循环内反复 splice + 辅助数组」改为单趟扫描把唯一元素压到数组前部 + 一次截断，O(N²) → O(N)，额外空间 O(N) → O(1)：

```js
// Pack the first instance of each unique element into the start of
// results (starting at index 1 because index 0 is always kept), then
// splice away the tail of duplicates.
for ( i = 1; i < results.length; i++ ) {
    if ( results[ i ] !== results[ i - 1 ] ) {
        results[ j++ ] = results[ i ];
    }
}
```

### 可复用的模式与技巧

1. **构建期虚拟模块覆盖**——多形态发行的库（可选插件组、subpath export、slim/full 双版本）
2. **声明式依赖级联表**——`removeWith` 让裁剪规则可读、可审、可自动推导
3. **运行时能力探测替代 UA 嗅探**——jQuery 从来不嗅探 UA，这是它能活 20 年的根本原因
4. **真实布局测量判定能力可靠性**——文档说不清的行为只能实测
5. **行为差异钩子表**——`special[type]` / `cssHooks[name]` / `attrHooks[name]` 三张表让新增差异不污染主流程
6. **`setup` 返回 false 即接管**——一个返回值承担「已处理 / 请走标准路径」的分支
7. **惰性探测 + 一次性哨兵**——有成本的启动期探测的标准写法
8. **临时环境变换测量**（`swap`）——IE 的 `display:none` 元素测不出尺寸，标准浏览器能测；jQuery 不做 UA 判断，而是临时改变环境让浏览器暴露正确答案
9. **第三方一致性测试套件接入**——把自研实现包装成官方套件的 adapter
10. **双通道私有数据存储**——同一 `Data` 机制的两个实例（`dataUser` / `dataPriv`），cache 用 `Object.create(null)` 从结构上消除原型污染
11. **标志位组合的回调列表状态机**——`Callbacks("once memory")` 用两个布尔组合出四种语义，Deferred 直接建立在它之上
12. **单 dispatch 入口 + 分区数组**——每个元素只挂一个原生监听器，委托 handler 插在数组前部，dispatch 时切片跳过
13. **多形态参数归一化器**——`src/core/access.js` 一个函数处理 get / set / bulk-set / callback-value 四种调用形态
14. **体积预算内建到构建流程**——`build/tasks/lib/compareSize.js` 每次构建自动对比各分支历史体积，红色标记增长

### 关键设计决策

**决策 1：用「构建期裁剪」而不是「运行时开关」实现 slim 构建**

- 问题：slim 与完整版历史上是两份手工维护的代码，bug 要改两处
- 方案：一份排除清单 + `removeWith` 依赖级联表 + `core/ready-no-deferred` 替代实现
- Trade-off：slim **不是**完整功能的严格子集——它换了一套 ready 实现，等于多维护一条代码路径；且因为 ESM 的 `import` 是静态的，「不含某功能」只能在构建期决定，非官方自定义构建不受测试覆盖
- 可迁移性：高

**决策 2：事件系统用「单 eventHandle + delegateCount 分区」**

- 问题：同一元素上多种事件类型只挂一个原生监听器，否则内存与性能爆炸
- 方案：委托 handler 插在数组前部并递增 `delegateCount`，直接绑定 handler 在后部，dispatch 时 `handlers.slice(delegateCount)` 跳过委托区
- Trade-off：所有回调都要经过一次 `jQuery.Event` 包装 + `dispatch` 分发，比原生 `addEventListener` 有固定开销；`special` 表复杂度随浏览器差异增长
- 可迁移性：高

**决策 3：数据存储用 `Data` 类 + user/priv 双通道**

- 问题：3.5.0 修 `Object.prototype` 污染时把 `hasOwnProperty` 换成原型安全的 `in`/`Object.hasOwn`，打断了 bootstrap-select 等插件的既有调用（[#4665](https://github.com/jquery/jquery/issues/4665)，社区反弹「Such change should not be introduced as a minor version upgrade」）
- 方案：抽出 `Data` 类，两个实例分别承载公开与内部数据；元素走直接属性赋值、非元素走 `Object.defineProperty`
- Trade-off：`Object.create(null)` 的 cache 不能用普通对象方法；每个元素挂 expando 属性可能与其他库冲突（expando 因此带上随机数）
- 可迁移性：高

**决策 4：`jQuery.extend` 深拷贝只处理「直接自引用」**

- 问题：深拷贝最怕循环引用
- 方案：`if ( name === "__proto__" || target === copy ) continue;`——自引用跳过而非 seen-set 追踪
- Trade-off：**真正的循环引用（A→B→A）深拷贝仍会栈溢出**；`isPlainObject` 判定虽精细（用 `fnToString.call(Ctor) === ObjectFunctionString` 排除 class 实例与跨 realm 对象），但非 plain object 在深拷贝时按引用传递
- 可迁移性：中——分支处理是通用模式，但循环引用的实现约束必须写进文档

**决策 5：兼容性差异用「三件套」建模**

- 问题：浏览器差异有三类——能力有无、能力有无但语义不同、能力有但不可靠
- 方案：能力有无 → `support` 表 + `src/var/` 层 fallback 注入点；语义不同 → `special`/`cssHooks`/`attrHooks` 钩子表；不可靠 → `swap` 环境变换 + 真实布局测量
- Trade-off：每一处差异都要写 hook，代码量持续增长（`src/event.js` 884 行，`src/css.js` 380 行里大半是兼容逻辑），维护者必须持续跟进浏览器行为变化（changelog 里满是「Work around a Safari 27 regex interpreter bug」这类修复）
- 可迁移性：**高——这是本次分析中最值得迁移的模式**

## 套利机会分析

- **信息差**：jQuery 的「star 数」与其「真实装机量」严重背离。60,022 star 看起来平平无奇，但 npm 月下载 7,141 万次、W3Techs 全网覆盖率 62.9%——它其实是全球装机量最大的前端库。同时 4.x 版本在 W3Techs 的版本分布里**尚未出现**（1.x 16.8% / 2.x 4.2% / 3.x 79.0%），说明 4.0.0 发布近一年，升级红利几乎没被吃到。
- **技术借鉴**：构建期虚拟模块覆盖、声明式依赖级联表、第三方一致性测试套件接入、真实布局测量探测、四件套兼容层建模——这五个模式可以直接搬进任何长期维护的库或 SDK。
- **生态位**：jQuery 在生态中的角色不是「流行的库」，而是**「跨世代遗留层 / 迁移缓冲层」**。它承接 React/Vue 时代之前的历史代码，同时是 WordPress 生态的默认 DOM 层——事实上成了全球最大 CMS 的「运行时契约」。
- **趋势判断**：**存量在收缩，但收缩是缓慢且不可逆的**。W3Techs 数据显示 jQuery 在全网网站的使用率已从 72.1%（2025-11）跌至 62.9%（2026-11-19），一年多掉了约 9 个百分点；同期 Bootstrap 从 19.4% 涨到 25.8%，Next.js 从 2.0% 翻倍到 4.0%。**旧世界的收缩速度几乎等于新世界的扩张速度**。但存量不会断崖——WordPress 与企业 CMS 的替换成本极高，jQuery 3.x 的 critical-only 维护线还会存在很多年。
- **一个反直觉的细节**：jQuery 的**版本分布比总量更健康**。3.x 占比从 64.4%（2023 Q4）一路升到 79.0%（2026-11），1.x 从 29.1% 降到 16.8%，2.x 降到 4.2%。也就是说——**留下来的那批人正在认真升级，正在离开的那批人不升级**。这对存量维护者是好消息（依赖的 jQuery 越新，漏洞越少），但对 4.x 是坏消息：4.0.0 发布已近一年，W3Techs 的版本分布里**依然看不到 4.x 的任何份额**。升级红利尚未兑现。

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | jQuery 4.x | 原生 DOM API | React | htmx | Cash |
|------|-----------|-----------|--------|------|------|
| 体积 | 27.5KB gzip（slim 19.4KB，均为实测 min+gzip） | 0 KB | ~45KB + 构建链 | ~16KB | ~6KB |
| 全网覆盖率 | 62.9%（W3Techs 2026-11） | 内建，无统计 | — | — | ~0.2% |
| 批量 DOM 链式 ergonomics | 强 | 弱（需手写循环） | 不适用（声明式） | 不适用 | 中（API 兼容） |
| Ajax 抽象 | `$.ajax` + 全局 `ajaxSetup` + jqXHR | 需自写（fetch） | 不覆盖 | 由服务端承担 | 无 |
| 异步编排 | Deferred（Promises/A+ 合规，有 progress 通道） | 原生 Promise（无 progress） | 不适用 | 不适用 | 无 |
| 动画 | 完整队列 + easing | 需自写 / Web Animations | 不覆盖 | 不覆盖 | 无 |
| 迁移成本 | — | 逐 API 重写 | 视图层全量重写 | 需重构服务端 | 低（仅 DOM 子集） |
| 增长趋势 | −9.2pp/年 | 内建能力，持续扩张 | 持平（6.1%→6.0%） | 翻倍（2.0%→4.0%） | 平稳 |

### 差异化护城河

- **信任护城河（最强）**：jQuery 承载的是生产系统的运行稳定性。20 年的 API 稳定性承诺（每次 major 净删除而非新增）、6,874 次提交的连续性、OpenJS Foundation 的 CNA 协调披露流程（`SECURITY.md` 定义了私密上报渠道与 6/14 天响应时限）。企业选 jQuery 不是因为它技术领先，而是因为「**它不会突然坏掉**」。这是 Cash、htmx 无法在短期内复制的。
- **生态护城河（次强）**：数千个插件 + WordPress（全球最大 CMS，核心仍捆绑 jQuery 3.7.1）+ 大量企业 CMS。这些不是 jQuery 的资产，但确实是它的护城河。
- **技术护城河（最弱）**：几乎为零。原生 API 在功能与性能上全面超越；Cash 在体积上超越；htmx 在心智负担上超越。唯一的准技术护城河是「跨浏览器兼容层的完备性」——而这份完备性本身是负债。

### 竞争风险

**最可能被替代的不是 jQuery，而是「jQuery 的使用场景」。**

- 短中期（1–3 年）：新项目几乎不会选 jQuery（原生 API + Vite 生态 + React/Vue/Svelte）。存量基数缓慢下降但**不会断崖**。
- 长期风险：**htmx 这类「HTML 超媒体」范式如果继续增长**，会从「jQuery 的替代品」变成「jQuery 存在理由的消解」——因为 htmx 证明了大部分 jQuery 用途（Ajax + DOM 片段替换 + 少量交互）可以用 20 行 HTML 属性完成，连「选择器引擎 + 事件系统 + Ajax 抽象」这套复杂度都不需要。
- 官方自己的动作印证了这个判断：3.8.0 是 3.x 最后一个功能版本，4.x 的价值主张已从「改变前端写法」转为「维护存量代码的最短路径」。**官方在主动把 jQuery 定义为「遗留代码的官方维护通道」，而非「有生命力的库」。**

### 生态定位

- **向上**：承接 React/Vue 时代之前的历史代码，直到它们被重写或被 htmx 类范式简化。
- **旁侧**：WordPress 生态的默认 DOM 层——事实上成为全球最大 CMS 的运行时契约。
- **向下**：作为版本治理与安全维护的业务——旧版本商业支持外包给 HeroDevs/TuxCare，说明「维护」本身已经可变现。
- jQuery 的终极形态可能不是「继续演进的库」，而是**「一个被良好维护的、有限的、会慢慢缩小但不会消失的兼容层」**。4.1.0 的发布标题《Passing the Torch》精准描述了这个状态转移。

## 风险与不足

1. **增长故事已经结束**：W3Techs 全网份额一年掉约 9 个百分点，4.0.0 发布近一年在版本分布里看不到踪迹。官方自己在劝退新项目采用。
2. **技术债是永久性的**：兼容层模式本质要求「每个浏览器版本变化都要跟进」。changelog 里全是 Safari 27 / Firefox 135 的 workaround。`#4886`（CSS4 选择器）与 `#2871`（passive 事件）两个关键 issue 从 2021 和 2016 年 open 至今，说明抽象层在浏览器能力演进时会持续产生「滞后税」。
3. **循环引用深拷贝会栈溢出**：`jQuery.extend` 只处理「直接自引用」，真正的 A→B→A 循环仍会导致栈溢出。这是个已知但未被彻底修复的约束。
4. **Deferred 是非规范的 Promise**：`resolve` 保留 `this` 与多参数是 jQuery 特有行为，代码里明确注释为「non-spec behavior」，意味着它与原生 Promise 不能完全互换。
5. **安全修复与下游生态的持续冲突**：3.5.0 的原型污染修复直接打断 bootstrap-select 等插件的调用，社区反弹情绪明显（[#4665](https://github.com/jquery/jquery/issues/4665)）。官方随后用「4.0 升级指南单列 Data 章节 + jQuery Migrate 4.x 定位问题」的方式收场——代价是 4.0 升级指南细到需要九大类章节，迁移摩擦相当高。
6. **依赖自身 API 的隐性成本高**：数千插件依赖 jQuery，任何一次 major 的删除决策都要考虑整个生态。3.5.0 的教训直接导致 4.0 延后到 2026-01 才发布。
7. **同步脚本加载仍走 XHR+eval**：因为 `<script>` 标签无法同步，这条路径在严格 CSP 下依然违规，官方承认「such a change is impossible」并留作未解问题。

## 行动建议

- **如果你要用它**：新项目**不要**选 jQuery（官方自己也是这个建议）。已有 jQuery 存量代码可以放心升到 4.x——官方提供了 jQuery Migrate 4.x 作为迁移桥梁，路径是「升 4.x → 挂未压缩版 Migrate → 跑测试消警告 → 摘掉 Migrate 再验证」。如果只需要 DOM + 事件这一层且能接受 API 兼容层的粗糙，Cash（约 6KB）是个体面的替代；但一旦用到 Ajax / 动画 / Deferred 就会卡住。3.x 已降级为 critical-only，**不要再新接入 3.x**。
- **如果你要学它**：重点看这五个文件/模块——
  - `build/tasks/build.js` + `build/tasks/lib/rollupFileOverridesPlugin.js`（构建期虚拟文件覆盖 + `removeWith` 级联表）
  - `build/tasks/lib/slim-exclude.js` + `src/core/ready-no-deferred.js`（一份源码多形态发行 + 替代实现模块）
  - `src/css/support.js` + `src/css/var/swap.js`（惰性真实布局测量 + 环境变换探测）
  - `src/event.js` 的 `special` 表与 focus/blur 模拟（行为差异数据化）
  - `src/deferred.js` + `test/promises_aplus_adapters/deferred.cjs`（自研异步原语 + 第三方一致性套件）
- **如果你要 fork 它**：**别 fork 核心库**——它没有巴士因子问题（核心 Top 4 占 65%），也没有明显的待修 bug 池。真正值得 fork 的是它的**模式**：把「构建期裁剪」「能力探测表」「钩子表」「一致性套件接入」这四件事抽成模板套到你自己的多形态库上。注意 README 里明确警告「Non-official custom builds are not regularly tested」——如果你要做定制构建，得自己补上 `test:slim` / `test:no-deprecated` 这类裁剪后测试。

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | [deepwiki.com/jquery/jquery](https://deepwiki.com/jquery/jquery)（探测时返回 HTTP 429，无法确认收录状态） |
| Zread.ai | [zread.ai/jquery/jquery](https://zread.ai/jquery/jquery)（已收录） |
| 关联论文 | [Thou Shalt Not Depend on Me: Analysing the Use of Outdated JavaScript Libraries on the Web](https://arxiv.org/abs/1811.00918)（NDSS 2020，13.3 万站点实证，37% 站点至少引入一个含已知漏洞的 JS 库）<br>[Precise and Scalable Static Analysis of jQuery Using a Regular Expression Domain](https://dl.acm.org/doi/abs/10.1145/2989225.2989228)（DLS 2016）<br>[The State of Disappearing Frameworks in 2023](https://arxiv.org/html/2309.4188)（以 jQuery 时代为对照）<br>[From One to Hundreds: Multi-Licensing in the JavaScript Ecosystem](https://arxiv.org/html/2012.05016v1)（以 jquery 为样本的再分发合规） |
| 在线 Demo | 无官方 playground（jsbin/codepen/jquery.com-try 均不可用）；可用 [jQuery Learning Center](https://learn.jquery.com/) 与 [api.jquery.com](https://api.jquery.com/) |
| 官方文档 | [api.jquery.com](https://api.jquery.com/) / [jquery.com/support](https://jquery.com/support/) / [jquery.com/browser-support](https://jquery.com/browser-support/) / [contribute.jquery.org](https://contribute.jquery.org/) |
| 官方博客 | [blog.jquery.com](https://blog.jquery.com/)（关键文章：《jQuery 4.1.0 and 3.8.0 Released: Passing the Torch》2026-11-17） |
| 迁移工具 | [jquery-migrate](https://github.com/jquery/jquery-migrate)（2,091★） |
| 升级指南 | [jquery.com/upgrade-guide/4.0](https://jquery.com/upgrade-guide/4.0)（九大类：Ajax/Attributes/Core/CSS/Data/Deferred/Event/Manipulation/Selector） |
| 兼容性看板 | [healthyweb.org](https://www.healthyweb.org/)（检测你的站点 jQuery 是否过期） |
| 会议纪要 | [meetings.jquery.org](https://meetings.jquery.org/category/core/)（核心团队的公开决策记录） |
