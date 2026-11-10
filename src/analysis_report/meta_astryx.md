# GitHub推荐：22K stars：Meta 设计系统给 AI 写 UI 打分

> GitHub: https://github.com/meta/astryx

## 一句话总结

Meta 把内部用了八年的设计系统开源出来，真正值得看的不是那 148 个组件，而是它把「AI 生成的 UI 质量」当成 nightly 回归测试指标来运营——同一批 prompt 跑四套方案，用零 LLM 的静态评分器 + tsc 幻觉检测 + 双模型盲评打分，并把这套评测方法开源出来。

## 值得关注的理由

1. **全网几乎没有第二家把「AI 写 UI 的准确率」当作工程指标来运营**。`internal/vibe-tests/` 用 70 个 prompt × 4 个 target（Astryx / Astryx+Tailwind / 真 shadcn/ui / 纯 HTML）× 3 种人设（新手 / 老手 / 恶意）跑对照实验，评测公平性被写成 5 条不变量，连「哪些评分对 Tailwind 更宽松」这种对自己不利的偏差都主动写进 README。这不是营销词，是一套可复现的实验装置。
2. **Meta 八年内部 review 经验被完整制度化成公开的「知识契约」体系**。`docs/specs/` 下 83 个 AST-xxx 规范目录、297 份规格文档、21 份架构记录，每份带 `authority: draft|current|archived` + `approved_by` + `verified_by`；`review-signal.yml` 靠 diff 内容分类器自动路由 reviewer，并用 required status check 做硬门禁。这套「决策如何留痕、如何被机器检索」的制度，比组件本身更难复制。
3. **同时占住了竞品都没站的中间位**：vendor-owned 的上游修复（不像 shadcn 复制源码后各自为战）+ swizzle 源码所有权出口（不像 MUI 无法 escape）+ shadcn registry 分发通道。22.1K stars、1,774 fork、npm 单包月下载 140 万次，开源 4.7 个月就冲到 GitHub Trending #2。

## 项目展示

![Astryx Banner](https://lookaside.facebook.com/assets/astryx/Astryx-Banner.png)
官方 Banner：README 中唯一的展示性图片

![Preview Watch](https://astryx.atmeta.com/neutral/preview-watch.png)
neutral 主题渲染预览：主题即一组 CSS 变量覆盖，组件代码完全不动

![Butter Theme Preview Watch](https://astryx.atmeta.com/images/butter/preview-watch.png)
butter 主题预览：8 套官方主题共用同一份组件源码，证明「外观由主题负责」的分工

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/meta/astryx |
| Star / Fork | 22,118 / 1,774 |
| 代码行数 | 1,719,188（TSX 37.9% / TypeScript 28.0% / JavaScript 26.1%；含 monorepo 样例与 locale，真实产品规模远小于此） |
| 项目年龄 | 10 个月（2026-01 首次提交；2026-06-18 公开开源，约 4.7 个月） |
| 开发阶段 | 密集开发（近 30 天 2,741 commit，近 90 天 4,286 commit，10–11 月月化近 4,500） |
| 贡献模式 | 核心少数 + 社区（138 位贡献者，Top 1 占 50.9%，Meta 官方组织主导） |
| 热度定位 | 大众热门（npm 单包月下载 140 万次） |
| 质量评级 | 代码[优秀] 文档[优秀] 测试[充分] |

## 作者视角：为什么存在这个项目

### 创始人/作者背景

Meta 组织账号，非个人项目。仓库 bio 写的是「We are working to build community through open source technology」，官网带 ©2026 Meta Platforms, Inc.，MIT 协议。这个设计系统在公司内部用了八年，支撑 13,000+ 应用，是 Meta 内部规模最大、使用最广的设计系统。

关键背景是 Meta 的开源哲学与个人项目截然不同：Meta 开源 React、Relay、PyTorch 时带着「回馈社区」的目的，但很少直接把内部基础设施整套搬出来。这次愿意把整个设计系统开源并配齐 CLI、MCP server、agent 文档，说明团队认为「agent 编程」这件事需要一个被上游维护的标准答案，而这个答案只能来自有 13,000 个内部应用背书的系统。

### 问题判断

作者看到的是一件别人没重视的事：**设计系统的消费者变了**。

旧式设计系统的产物是「给人读的散文文档 + 给 agent 猜的 API」。这两头在 2026 年同时失效——agent 看不见散文里隐含的约定（哪些 prop 存在、variant 叫什么、哪些组合是禁止的），于是它开始编造 `--color-accent-hover` 这种不存在的 token、用 Ant Design 风格的 `filled`/`outlined` 去调 Astryx 的 `primary`/`secondary`/`ghost`；而人类则被 agent 产出的代码淹没在幻觉 prop 里，只能靠人肉 review 兜底。

时机也踩得很准：2026-01 私有起步，2026-03 起月均 400+ commit，2026-06-18 公开开源——正好卡在 agent 编程从「尝鲜」变成「默认工作流」的拐点上。commit 曲线上 10 月和 11 月两次暴增（月化近 4,500），对应的是 Layer 栈和列表虚拟化两条主线同时收敛，这不像「顺手开源一个内部库」，更像公司级基础设施立项后的集中产出。

### 解法哲学

README 里四条原则把取舍写死了：

- **Guidance over enforcement**（给能力不给护栏）：「if you pass a value, the component renders it」，拒绝 MUI 式的「我替你决定」。
- **Strong documented conventions**（强约定）：用文档 + lint + spec 三重手段落地约定，而不是靠运行时警告。
- **One system for humans and AI**：同一条命令同时服务人和 agent（`astryx docs` / `astryx component --dense` / `astryx manifest --json`）。
- **Earned by measurement**（约定靠实测赢得）：每条约定都要有证据，没证据就改。

作者明确选择**不做**的事，从代码能反推出来：不做 headless（不走 Base UI 路线）；不做 CSS-in-JS runtime（`@astryxdesign/core` 的 runtime 依赖只有 `intl-messageformat` 一个，StyleX 是 peer 且对消费者不可见）；不把「复制源码进你仓库」当主分发路径（`swizzle` 是第五级逃生舱）；不用运行时拦截强制设计（焦点环、禁用态 hover 这些交给 38 条 eslint 规则）。

### 战略图景

**基础设施，不是核心产品**。11 个包用 changesets 的 fixed 组一起发版；`packages/lab` 是 private 不发 npm，`packages/vega`（0.1.3）/`packages/charts`（0.1.9）只发 canary tag，`packages/native`（0.1.0）是 Swift 原生探索支线。

**genuinely open，不是 open-core**：MIT 协议，无功能墙，`packages/core` 的 173 个 export 子路径全部公开，没有 telemetry、没有付费层、没有企业版。变现路径只剩两条——内部 dogfooding 保住组织地位，以及生态影响力。

治理上有个成熟细节值得注意：`.github/ENGOWNERS` 与 `DESIGNOWNERS` 把代码 review 和视觉 review 分权，`review-signal.yml` 自动贴 `needs:code-review` / `needs:design-review` 标签，但**代码 review 是硬门禁（required status check），设计 review 是建议性的**。这个切分很清醒——设计讨论不该阻塞合并，代码规范必须阻塞。

## 核心价值提炼

### 创新之处

**1. 把「LLM 生成 UI 质量」变成可回归的工程指标（新颖度 5/5）**

`internal/vibe-tests/` 是一套完整的离线评测工厂，不是几个 prompt 脚本：

- 70 个分层 prompt（带 category / complexity / expectedComponents）跑 4 个 target：`project-astryx`、`project-astryx-tailwind`、`project-baseline`（真拉一份 shadcn/ui 源码进来）、`project-html`（纯 HTML + 内联 CSS）
- 3 种 persona（naive / experienced / adversarial）交叉，覆盖「agent 什么水平时最容易崩」
- 静态评分器 `universal-eval.ts` 是**纯函数、零 LLM**，5 个维度（Correctness / Accessibility / Code Quality / Efficiency / Maintainability）；正确性用 `tsc` 错误数每个扣 15 分，外加 **phantom prop 检测**——专门抓 `onPress`/`onLongPress`、`button` 上的 `onChange` 这类「编译通过但永不触发」的静默 bug
- 视觉保真度另走多模态盲评：Claude 3 passes 取中位数 + Gemini 2.5 Pro Vision 双后端互验，对齐人工提供的参考截图，5 个子信号加权（布局 25% / 层级 25% / 间距对齐 20% / 组件 15% / 色彩主题 15%）
- 评测公平性写成 5 条不变量：Fair Evaluators / Only the System Under Test Varies / Never Leak the Answer / Representative Environment / Context-Free Sub-Agents
- 甚至有 degradation mode：多轮对话注入 filler / distractor / recovery，探测第 0/6/8/10 轮，画出质量衰减曲线

**2. 知识契约体系：让「决策」成为带权威等级、可被 diff 路由的机器可读资产（新颖度 4/5）**

每份规格文档带 `authority: draft|current|archived`（只有 `current` 有约束力）、`approved_by`、`applies_to`、`verified_by`、`deciding_specs`，再加一段 `<!-- review-applicability:v1 -->` JSON 声明「哪些变更语义会路由到哪些不变量」。配套工具 `pnpm specs:for <path>` 查某路径的当前记录，`pnpm specs:for --diff origin/main` 列出本次改动触发的 claim。写规格还要过 `docs/contributing/spec-writing.md` 的 rubric 并把结果贴进 PR 描述。

**3. StyleX class prefix 分离（新颖度 4/5，实用性 5/5）**

StyleX 的原子 CSS 是「相同声明 = 相同 class 名」，库里和业务里同一条声明必然撞 class，结果是两者没法分进不同 `@layer`，主题覆盖就失效。`@astryxdesign/build` 给库编 `astryx` 前缀、给业务编 `x` 前缀，把两组分别塞进自己的 layer。这是一条典型的「用编译器特性解决级联问题」的思路，别的 atomic CSS 库遇到同样的坑时很少有人从编译期入手。

**4. 跨副本 Context 共享（新颖度 4/5）**

swizzle 出的组件副本和原包同时存在时，Context 必须互通，否则 swizzled 的 Button 放进原包的 ButtonGroup 就失去分组语义。实现用 `realmValue(sharedKey(name, version))` + WeakMap keyed by `createContext`，**按 React 实例隔离而非按模块实例**——理由写得很清楚：服务端可能加载两个 React，流式渲染只会恢复自己的 context，两个 React 之间绝不能共享。

**5. 公开 `data-*` 属性按公共 API 治理（新颖度 3/5）**

主题基于 `data-*` 生成选择器，所以新增一个 `data-*` 就等于新增一条公开契约。动态样式改走 StyleX 的动态 style 写私有 CSS 变量，**不为喂 CSS 而加 data 属性**；内部用途一律 `data-astryx-*` 私有前缀。

**6. 规范驱动的领域 lint + baseline 冻结（新颖度 3/5，实用性 5/5）**

`internal/eslint-plugin-astryx/` 有 38 条规则，每条对应一条领域不变式（`no-hover-on-disabled`、`no-physical-properties`（为 RTL）、`no-unguarded-ime-keydown`……），每条带 baseline JSON 把存量违规冻结，新代码不许新增。

规则注释里保留着真实 bug 的完整教学案例。`no-classname-clobber` 记录了一次：Breadcrumbs 里两个 spread 各带 className，后者静默覆盖前者，导致**已文档化、已注册、属于公开 theming surface 的 target 一个元素都没渲染**——而 `themingTargets.test.ts` 因为只断言「文档化目标是源码注册目标的子集」而恰好放过了它。这类「规则解释了为什么现有测试不够」的注释，本身就是设计系统质量的说明书。

**7. manifest-as-API（新颖度 3/5）**

`astryx manifest --json` 直接内省活的 Commander program 对象，输出所有 command / flag / 返回类型。代码注释特别说明了它**故意放在 CLI 层而非 `api/` 目录**——提取到 api 会造成 `api → cli` 的循环依赖。

**8. 唯一 windowing 引擎 + 架构不变量（新颖度 3/5）**

`packages/core/src/virtualization/` 一个模块算 row/gap 半开区间 segment + overscan ±4 行，Table / Selector / Chat 共享。架构记录 INV1 直接写「Reject a second windowing implementation in Core」，review 时看到第二份实现直接拒。

### 可复用的模式与技巧

1. **评测公平性五不变量**——任何多方案对照评测（选框架、选 ORM、选编辑器插件）都能直接套用
2. **已知不对称显式登记**——把「哪些评分对某方案更宽松」写进 README，并声明「这些不对称让我们的胜出更可信」
3. **Authority 三态 + 显式批准**——`draft`/`current`/`archived`，晋升需 owner 显式签字并留痕
4. **Concern → Claim 路由**——用 JSON 声明「哪些语义触发哪些不变量」，让 diff 自动路由到相关 claim，不用人工翻文档
5. **同茎强类型描述符 + manifest 只定位不编目**——`<source-stem>.doc.mjs` 是唯一权威（spec:AST-039 FR11 记载了 0.6 版误发中央 catalog 只能 breaking 移除的教训）
6. **Baseline 冻结的领域 lint**——规则可以逐年收紧而不阻塞存量代码
7. **Swizzle 逃生舱 + 版本化 helper 文件名**——`helper.v0.7.9.ts` 避免版本升级时和用户已有副本冲突
8. **原子 CSS class prefix 分离以支持 layer 分层**
9. **语义 token + 单一解析图**——`tokenVar` / `resolveThemeToken` / `resolveThemeTokens` 让 canvas / SVG / charts / 测试 / 构建工具共用同一份 token 图
10. **PR 快 lane / main 重 lane 分离**——视觉回归、a11y、RTL 审计不上 PR（要 build Storybook + Chromium，PR 上跑会爆 15 分钟预算并产生噪音），改为 main 上每 3 小时跑一次并对 main tip 门禁，失败「向前修复」不回滚
11. **夜间性能以自身 7 天中位数为基线**——每晚 5 个 perf scene、5 次采样取中位数，劣化超 10% 且超过 floor 时自动开 issue 并附上劣化前的 commit
12. **CLI 分层**——`api/` 只出结构化 receipt，人类文案只在 `clients/cli/` 的 renderer 里

### 关键设计决策

**决策一：用 CSS cascade layers 管理与消费者 CSS 的优先级**

- **问题**：设计系统要被消费者覆盖，又不能陷入 `!important` 军备竞赛；而且库 CSS 与业务 CSS 可能撞 class。
- **方案**：每个 Astryx 样式表自我声明 layer 顺序（`@layer reset, astryx-base, astryx-theme;`），因此在任意加载顺序下都成立；reset 全用 `:where()` 保持零特异度；未分层的消费者样式天然压过所有 Astryx layer。再叠加 `packages/build/` 的 class prefix 分离，让两层能并存于同一 atomic CSS 空间。
- **Trade-off**：牺牲了「Astryx 样式永远赢」的简单性。已有全局 CSS / Tailwind / reset 的项目必须显式理解 layer 顺序——这被第三方评测列为最大集成陷阱；class prefix 分离还要求项目走特定构建配置。
- **可迁移性**：高。「库层 + 主题层 + 应用层」三层模型可以直接搬到任何 CSS-in-JS 或 utility-first 系统。

**决策二：主题 = 一组 CSS 自定义属性覆盖 + `@scope` 化的组件级覆盖**

- **问题**：让设计师做出「明显是自己的」产品，又不想 fork 源码或包一层 wrapper。
- **方案**：`defineTheme()` 把作者输入归一化成 `DefinedTheme`；token 走 CSS 变量，组件级覆盖走 `@scope` + 稳定的 `.astryx-*` 类 + 反射的 `data-*` 属性。**运行时挂载和静态构建消费同一份归一化结果**（架构不变量要求 web 运行时与 build-time 产出同样的 CSS 行为）。
- **Trade-off**：主题作者只能逐个设置 token 并「祈祷它们彼此协调」。这正是 issue #958 暴露的天花板——作者本人在评论里提出借鉴参数化 CAD 的约束求解思路：作者表达视觉意图（「这个圆角等于壁厚」），系统反解具体数值。配置是声明式的，但一致性保证目前仍是手工的。
- **可迁移性**：高。

**决策三：把「AI 生成 UI 质量」当作回归指标**

- **问题**：号称 agent-ready 却没有任何客观证据。而且 agent 幻觉形态是系统性的，不是零星错误。
- **方案**：见上文创新点 1。
- **Trade-off**：建设成本极高（prompt 库 + 4 个 fixture 环境 + 截图流水线 + 双 judge + 人工理想图）。而且静态分析评分器本质是启发式的，不可能完全无偏；换 prompt 集可能改变排名结论。
- **可迁移性**：高——「把 LLM 产出质量当回归指标 + 多 target 对照 + 盲评 + 显式公平性不变量」这套方法可以直接搬到任何文档质量对 LLM 友好度敏感的项目。

**决策四：用 spec-first 的知识契约体系管理共享系统变更**

- **问题**：「什么行为人已经决定过」「这个 PR 是否在做一个需要人来定的新决定」——这两个问题不该靠翻旧 PR。
- **方案**：分层记录类型 + `authority` 审批 + `review-applicability:v1` 路由声明 + `pnpm specs:for --diff` + required status check 硬门禁。
- **Trade-off**：仪式成本极重——83 个 spec 目录、每组件一份 `.spec.md`、写记录要过 rubric 并贴进 PR 描述。新贡献者无法自己写 spec（文档明确「外部贡献者走正常流程，维护者负责缺失的权威」）。这对社区参与度是实打实的门槛。
- **可迁移性**：中。方法可迁移，但成本决定了它只适合有专职团队长期维护的系统。

**决策五：`swizzle` 采用「复制源码 + 版本化 helper 文件名」而非「wrapper 覆盖」**

- **问题**：需要突破组件内部结构时的最深层定制方式。
- **方案**：eject 组件完整源码及其依赖的内部模块，owner 包改为从副本 import；共享 helper 以 `helper.v0.7.9.ts` / `helper.v0.7.9-2.ts` 形式版本化。`assertWithin` 做路径安全，swizzle 后自动生成给维护者的 issue 反馈链接。
- **Trade-off**：官方自己称之为「one-way door」——一旦 eject，升级路径就断了，源码副本会脱离上游修复和无障碍维护。
- **可迁移性**：高。

**决策六：交互模态是全局状态，焦点环由组件所有权决定谁来画**

`docs/architecture/interaction-modality.md` 把键盘 / 指针 / 触摸 / 笔统一成一个 modality 状态，焦点环是否可见由全局状态决定。这是「13,000 个 app × 数亿用户」的教训——焦点环不能每个组件各判各的，否则同一屏里会出现 N 种焦点环策略。配套还有 `IME_GUARD_DESIGN.md`：`isImeKeyEvent` 是全库唯一真源，7 处调用点统一，文档明确写着「keyCode===229 仍然 load-bearing，drop 会回归」——这是中文/日文输入法场景在 Meta 全球产品上倒逼出来的产物。

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | Astryx | shadcn/ui | MUI | Base UI |
|------|---------|--------|-----|---------|
| Stars | 22,118 | 127,828 | 99,316 | 11,356 |
| 源码所有权 | 上游维护 + 可 swizzle eject | 复制进仓库即自有 | vendor 闭源 | vendor 闭源 |
| 上游无障碍修复 | ✅ 150+ 组件共用一份实现 + CI 证明 | ❌ 各团队各自为战 | ✅ 多年投入 + 外部审计 | ✅ hooks 打磨细致 |
| Agent 可消费性 | manifest --json + 1,594 个 .doc.mjs + MCP | ❌ 散装源码无 manifest | ❌ 仅 TS 类型 | ❌ 仅 TS 类型 |
| 可量化评测 | ✅ vibe-tests 四 target 对照 | ❌ | ❌ | ❌ |
| 运行时依赖 | 1 个（StyleX 编译期） | Radix + Tailwind | emotion runtime | ~0 |
| 视觉可换肤 | 8 套主题 + 任意自建 | 全靠你自己写 | Material 语言强绑定 | 无视觉层 |
| 上手成本 | 装 core + theme + StyleX peer + CLI，要懂 layer 顺序 | 复制文件即可 | 中 | 最低 |

### 差异化护城河

- **信任护城河（强）**：21 份架构记录 + AST-xxx 系统规范 + 每组件 spec + `authority` 审批 + `verified_by` 证据链 + 153 个真实浏览器交互证明 + 夜间性能门禁 + baseline lint。这套「决策留痕 + 证据绑定」的制度是唯一真正难复制的部分——Meta 八年内部 review 经验被制度化公开了。
- **技术护城河（中等偏强）**：编译期样式 + layer 分层 + 语义 token 图 + 唯一 windowing 引擎 + 交互模态全局状态。这些不是「组件列表」能追的，但复刻需要数年。
- **生态护城河（弱）**：4.7 个月、22K stars vs shadcn 的 127K。生态是 Astryx 当前最大的短板，且短期内无法建立。

### 竞争风险

1. **最可能的替代者是 shadcn/ui + 一个成熟的 agent 文档层**。如果 Cursor / Claude Code 原生内建了「组件系统 manifest 协议」，shadcn 生态就能用社区规模碾压 Astryx 的 agent 优势——Astryx 的差异化会被**工具层吸收**，而不是被另一个设计系统打败。
2. **Meta 自身战略风险**：Meta 若内部放弃维护或转向仅内部使用，外部生态会迅速失去信心（对比 React Native / Relay 的历史）。
3. **契约尚未冻结**：官方 v1 时间表未公布，v0.7.x 仍在破坏性变更（`useTableRowsVirtualization.viewportHeight` 在第一个稳定 release 前就改名了；v0.6.0 改了 `useStepperContext`）。现在接入有返工风险。

### 生态定位

端到端的完整系统（foundation + 组件 + 模式 + 主题 + 模板 + CLI + 集成协议 + agent 契约 + 评测），**不是**组件库、不是原语库、不是 headless。它在 agent 编程时代扮演的角色是「**可被 agent 消费的、有上游维护的完整设计系统**」这一细分的定义者。

中间路线最有价值：**vendor-owned 的上游修复 + swizzle 的源码所有权出口 + shadcn registry 分发通道**，这三者同时存在，此前没人占过这个位置。

## 套利机会分析

- **信息差**：项目本身热度已充分定价（22K stars、140 万/月下载量，中文社区大量翻译转载），**发现它没有套利空间**。但有三个具体痛点尚无社区共识答案：token 命名幻觉（#3164 里 agent 编造 `--color-accent-hover`）、density 体系缺位（#839 被作者以「We're not ready for a DensityProvider」驳回，理由是没有主流系统把 density 与 size 作为独立轴）、edge compensation 推导缺失（#958，作者自提参数化 CAD 约束求解思路）。这些是外部采用者最可能踩坑、也最有价值提前研究的领域。
- **技术借鉴**：vibe-tests 的评测方法论（多 target 对照 + 盲评 + 公平性不变量 + degradation mode）几乎可以原样搬到任何做 AI 工具的团队；领域 lint + baseline 冻结机制适合任何想逐步收紧既有代码库约定的项目；class prefix 分离 + cascade layer 的组合是 atomic CSS 库做运行时主题的完整解法。
- **生态位**：填补了「有上游维护的完整设计系统」和「复制源码自有的社区方案」之间的空白，且是第一个把 agent 契约（manifest、.doc.mjs、MCP server）做成一等公民的设计系统。
- **趋势判断**：符合 agent 编程的大趋势，且在后发优势上占位极好——竞品要么没有 agent 契约（shadcn/MUI），要么没有视觉系统（Base UI/Radix），要么没有上游（shadcn）。但**契约未冻结 + 生态薄**是实打实的短板，建议以「观察者 + 试点项目」姿态接入，而非全量押注。

## 风险与不足

1. **Beta 期 API 不稳定**：v0.7.13 仍在小版本迭代，v1 时间表未公布，破坏性变更持续存在（`useTableRowsVirtualization.viewportHeight` 改名、`useStepperContext` 改签名）。
2. **生态与社区体量差距悬殊**：22K stars vs shadcn 的 127K，第三方教程、blocks、社区组件、Stack Overflow 答案量级都不在一个数量级。`packages/vega`（0.1.3）/`packages/charts`（0.1.9）只在 canary tag，`packages/lab`（0.1.9）根本没发 npm，`packages/native`（0.1.0）是未成形的 Swift 支线。
3. **集成成本被官方叙事淡化**：`@layer` 不遵守特异度规则，已有全局 CSS / reset / Tailwind 的项目必须显式管理层序，否则 Astryx 样式会被意外覆盖或反过来压掉业务样式。另外 CLI 的裸 `astryx` 命令会解析到 npm 上的无关同名包，应使用 scoped 调用。
4. **bus factor**：Top 贡献者 cixzhang 一人占 50.9% 提交，多方评测都独立指出了「两人维护」的担忧。
5. **主题一致性仍靠手工**：issue #958 揭示的核心短板——主题是声明式的，但 token 之间的协调目前只能靠作者「祈祷」。
6. **社区参与门槛高**：spec 体系写明外部贡献者无法自己写 spec，需维护者负责缺失的权威，这对社区规模扩张是负向的。
7. **密度系统缺失**：#839 被明确驳回，若产品需要紧凑/宽松双密度，只能自己在 token 层做。

## 行动建议

- **如果你要用它**：
  - 适合：需要一整套无障碍实现 + 主题能力 + agent 友好 API，且团队愿意接受「先吃一轮上游升级」的团队。典型场景是内部平台、要批量生成后台界面的团队。
  - 不适合：只要「复制粘贴几个组件」就能解决的轻量项目（shadcn 更省事）；需要 MUI X 级别的数据网格 / 日期时间选择器 / TreeView 的场景；或者需要「代码完全在我手里」以过合规审计的团队（虽然有 swizzle，但 eject 后就是单向门）。
  - 落地姿势：先用产品里最难搞的 2–3 个组件试点，验证「主题 token + className 覆写」够不够用，再决定要不要 swizzle。提前读懂 layer 顺序。锁定精确版本，别跟着 latest 走。
- **如果你要学它**：
  - `internal/vibe-tests/`（README + `universal-eval.ts` + `design-judge.ts`）——把 LLM 产出质量当回归指标的全套方法
  - `internal/eslint-plugin-astryx/`（38 条规则 + baseline 机制 + `no-classname-clobber` 里的真实 bug 案例）
  - `packages/build/` 的 class prefix 分离实现
  - `packages/core/src/utils/sharedContext.ts`（realm 跨副本 Context 共享）
  - `packages/core/src/virtualization/`（唯一 windowing 引擎 + INV1 不变量写法）
  - `docs/architecture/`（21 份架构记录，尤其是 `interaction-modality.md` 和 `public-component-api`）
  - `docs/specs/` 的 `authority` 字段与 `review-applicability:v1` 路由声明
  - `packages/cli/clients/cli/lib/manifest.mjs`（CLI 自省出 manifest）
- **如果你要 fork 它**：
  - 优先补三件官方还没做的事：① 主题 token 的一致性求解（#958 的参数化 CAD 思路，做成 lint 而非 runtime）；② 密度系统（#839，参考 Material 的 density scale 但按作者「size 撑不住时再补」的原则走）；③ agent 幻觉的直接拦截——把 vibe-tests 里的 phantom prop 检测从评测挪进 lint。
  - 上游合并策略：follow `main` 但只 cherry-pick `packages/core` 与 `packages/cli`；`packages/build` 的 prefix 逻辑改动频繁，落后要重做测试。

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | [deepwiki.com/meta/astryx](https://deepwiki.com/meta/astryx)（已收录，最后索引 2026-11-09，覆盖 workspace 结构、AST-xxx 规范体系、组件与动效架构、主题系统、CLI、CI/CD 与视觉回归门禁） |
| Zread.ai | [zread.ai/facebook/astryx](https://zread.ai/facebook/astryx)（已收录，但挂在改名前的 `facebook/astryx` 路径下，`zread.ai/meta/astryx` 走 Cloudflare 403；含中文深度解析与 monorepo 包边界说明） |
| 关联论文 | 无（设计系统无 arXiv 预印本；arXiv 上的 ASTERYX 2206.11900 是同名的可解释 AI 方法，与本项目无关） |
| 在线 Demo | [Playground](https://astryx.atmeta.com/playground) · [Sandbox](https://astryx.atmeta.com/sandbox/) · [Storybook](https://astryx.atmeta.com/storybook/) |
| 官方文档 | [astryx.atmeta.com](https://astryx.atmeta.com) · [博客：Introducing Astryx](https://astryx.atmeta.com/blog/introducing-astryx) · [How Astryx works](https://astryx.atmeta.com/blog/how-astryx-works) · [One Month of Astryx](https://astryx.atmeta.com/blog/one-month-of-astryx) |
| 第三方深度评测 | [OpenReplay: A First Look at Astryx](https://blog.openreplay.com/first-look-astryx-meta-design-system) · [andrew.ooo: Astryx Review](https://andrew.ooo/posts/astryx-meta-open-source-agent-ready-design-system-review) |
