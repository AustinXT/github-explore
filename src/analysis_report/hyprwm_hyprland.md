# GitHub 推荐：39K star 的 Hyprland：稳定还是好看，它偏要都要

> GitHub: https://github.com/hyprwm/hyprland

## 一句话总结

一个由单人架构师主导、彻底自建图形栈的 Wayland 动态平铺合成器——它把**「稳定」和「好看」做成了同一件事**，用 16 万行 C++、52 个自研着色器和一套 spring/bezier 动画系统，把 Linux 桌面的视觉上限又往前推了一档。

## 值得关注的理由

- **最完整的「从零自建图形栈」公开样本**：2024 年作者把 wlroots 彻底拆掉——协议层用 C++ 重写（65 个 `.cpp`），KMS/DRM/libinput 下沉成自研的 aquamarine。全世界愿意公开走完这条路、还做到 39K star 的项目几乎没有。
- **一套可以直接抄的现代 C++ 渲染与配置架构**：声明式 Pass 元素 + 反向遮挡分析、变换器链几何预规划、Lua 脚本宿主看门狗、配置项一行声明 + 位掩码增量刷新——每一条都能迁移到别的项目。
- **一个反常识的样本结构**：791 位贡献者，但 61.3% 的提交来自同一个人；测试不在 CI 门禁上，重构类 commit 只占 1.5%。它既是最好的学习材料，也是最好的「单人主导开源项目」风险教材。

## 项目展示

![Hyprland 官方 banner](https://raw.githubusercontent.com/hyprwm/Hyprland/main/assets/header.svg)

（官方 banner。README 第一句话就是它的全部主张：a 100% independent, dynamic tiling Wayland compositor **that doesn't sacrifice on its looks**）

![Hyprland 官方社交卡](https://hypr.land/imgs/og-img.png)

![Hyprland 桌面预览 A](https://raw.githubusercontent.com/hyprwm/Hyprland/main/assets/prev1.png)

![Hyprland 桌面预览 B](https://raw.githubusercontent.com/hyprwm/Hyprland/main/assets/prev2.png)

（两则官方 rice 预览：圆角 + 渐变边框 + 背景模糊 + 阴影 + 动画，是它区别于 sway / i3 系最直观的地方）

[End-4 rice 演示视频](https://hypr.land/videos/end_4_rice_intro.mp4)

（官方 rice 演示视频，配套封面 https://hypr.land/videos/end_4_thumbnail.webp）

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/hyprwm/hyprland |
| Star / Fork | 39,437 / 2,132（watcher 142） |
| 代码行数 | 160,874（C++ 78.5% + C++ Header 14.7% ≈ 93%，GLSL 2.0%，XML 2.2%） |
| 许可证 | BSD 3-Clause（宽松许可，允许商业分发与再打包） |
| 项目年龄 | 55.6 个月（2022-03-16 首次提交，仓库创建日同） |
| 开发阶段 | 密集开发（近 30 天 129 commit / 近 90 天 304 / 近 365 天 1,444） |
| 贡献模式 | 单人主导 + 社区执行（主作者占 61.3%，历史贡献者 791 人） |
| 热度定位 | 大众热门（Wayland 合成器赛道第一，约为 niri 的 1.4 倍） |
| 质量评级 | 代码[良好] 文档[一般] 测试[基本] |

## 作者视角：为什么存在这个项目

### 创始人/作者背景

Vaxry（GitHub ID `vaxerski`，2018 年建号），无公司雇员，全职做 Hyprland，靠赞助生活。bio 写着自嘲梗（You'll only go insane），location 填的是玩梗用的「Acheron, Hades」——整体人设是**「技术驱动、反 IDE、反社区政治」的独立开发者**。

但真正有分量的是他的博客 `vaxry.net`：20+ 篇长文，包括用户普查（Census）、wlroots 捆绑批评、trampoline hooks、own-malloc、以及与 freedesktop.org 的治理冲突。作者本人**既是产品经理，也是布道者**——他的第四次 Census 显示用户画像是「mostly young dudes」，Arch + Nix 系占 85%，70% 的人拿它当唯一桌面。

### 问题判断

**来自自身痛点，不是学术研究。** 这解释了为什么「特效」和「工程严谨性」能同时存在于一个项目里——**产品判断和代码实现是同一个人的直觉**，不会像「先做对、再做好看」那样分裂。

**时机选得很准。** 2022 年前后是 Wayland 生态的转折点：`wlr-layer-shell` 稳定、`xdg-shell` 落地、NV/AMD/Intel 三家驱动都上了 GBM、`wayland-protocols` 逐渐冻结。自建图形栈的「机会成本」从「不可能」降到「可行但昂贵」。作者选在这个窗口期做全量重写（2024 年正式与 wlroots 分家），而不是跟着 wlroots 迭代——等于用一次大手术，换一个不再受上游节奏约束的长期位置。

### 解法哲学

核心主张是「**独立性本身就是卖点**」。README 里那句「no wlroots, no libweston, no kwin, no mutter」不是技术炫耀，而是产品定位。

但独立不等于重复造轮子。hyprwm 组织下的 aquamarine（图形后端）、hyprutils（工具库）、hyprlang（旧配置语言）、hyprgraphics（色彩管理）、hyprcursor、hyprwayland-scanner 组成了一套「全家桶」，其中藏着一条清晰的策略分界线：

- **协议层共享、后端层独立**。协议实现留在 Hyprland 仓库内，因为协议是「和别人对话的语言」，必须全世界用同一份（Hyprland 和 Sway 共用同一份 wlr-layer-shell 定义）。
- **后端私有**。aquamarine 只对外暴露「与 Vulkan/OpenGL 无关」的 API（`Aquamarine::IBackendImplementation` / `IOutput` / `IBuffer`），内部可以是 DRM、Wayland 嵌套、Headless、Null。结果是全家桶共享底座，但每个项目**独立发布、各自定节奏**——hyprlock、hyprpaper、hyprpicker 都可以单独发版，不必等 Hyprland。

**不做什么，比做什么更清晰：**

| 明确不做 | 代价 |
|---|---|
| 不做 i3 配置兼容（`grep -rn "i3\b" src/` 零命中） | sway 用户零成本迁移的优势主动放弃 |
| 不做桌面级混合模式系统（全项目 `blend` 只命中一个 GL 开关） | 有 52 个自研 shader，却没有通用混合模型；相对 KWin / macOS 合成模式是功能缺口 |
| 不做色彩管理（issue #9064 三年 open、标 `0: low prio`） | 协议已实现、lcms2 加载器已写好，就是没做完 |
| 不做 `using namespace std`、不用 C 风格指针 | AGENTS.md 强制 SP/WP/UP + rc/sc/cc，抬高新人门槛但换来内存安全纪律 |

**性能 vs 易用性**：明显偏性能——`Pass.cpp` 的 `simplify()` 做逐元素遮挡分析，`DamageRing.hpp` 维护 3 帧历史做损伤追踪。但**易用性被小心保留**：配置保存即热重载，`debug:pass` 配置项能把整条 pass 链的遮挡层、live blur 区域、每个元素的 bb/opaque 标志全部画出来。

### 战略意图

**当前状态（2026-11）：genuinely open，不是 open-core。** 2026-08-21 DHH 成立 Omacom Foundation（8 位创始 patron 各捐 100 万美元，共 800 万，后续增至 1,000 万），成为 Hyprland **独家赞助方**，约 800 万美元级种子 + 3 年期（可续 2 年），2026-10-10 生效。同时 **Hyprperks（5€/月付费订阅）终止，全部功能免费开放**，官网承诺「will remain free and open source, features will not be locked behind a paywall」。个人捐赠（Ko-fi）保留，vaxry 得以全职开发。

**但风险没有消失，只是换了形态。** 赞助方 Omarchy 本身就是以 Hyprland 为默认合成器的最大下游用户——典型的「上游给下游打工」。资金稳定性上升，路线决策的独立性却在下降。而真正无解的那条——61.3% 的提交集中在一个人身上——不会因为赞助商变化而改变。

## 核心价值提炼

### 创新之处

按新颖度 × 实用性排序：

1. **声明式 Pass 元素管线 + 反向遮挡分析**（新颖 3 / 实用 5 / 可迁移 5）
   每种视觉元素实现 `IPassElement`，自报 `boundingBox` / `opaqueRegion` / `needsLiveBlur` / `requiresFullDamage` 等 14 个虚函数；`CRenderPass` 渲染前反向遍历元素列表，用 `opaqueRegion` 从累积 damage 中扣除遮挡区域。**新增特效 = 新增一个类，而不是改核心渲染循环**。

2. **变换器链的几何预规划（Plan / Execute 两阶段）**（新颖 4 / 实用 4 / 可迁移 4）
   `CWindowTransformerList::plan()` 先正推每级的 fullInputBox/fullOutputBox，再反推实际 outputBox/inputBox，最后 `transform()` 按优先级执行。多变换器叠加（网格变形 + motion blur）时，各自的采样区域仍然正确。`blocksDirectScanout()` 显式声明了「特效 vs 直通扫描」的取舍点。

3. **Lua 脚本宿主的三档防护**（新颖 3 / 实用 5 / 可迁移 5）
   `CLuaCaller` 用 Lua debug hook 做 10000 指令间隔的看门狗，按调用场景分 7 档超时（config_reload 1500ms / keybind 100ms / layout 50ms / event 50ms……），`MAX_CALL_DEPTH=32` 防递归，再用 weak table 做「同函数同错误只报一次」。**用户脚本搞不挂合成器**。

4. **配置项一行声明 + 位掩码增量刷新**（新颖 4 / 实用 5 / 可迁移 5）
   ```cpp
   MS<Int>("general:border_size", "size of the border around windows", 1,
           {.min = 0, .max = 20, .refresh = REFRESH_WINDOW_STATES});
   ```
   一行同时给出名称、描述、默认值、范围校验和热刷新依赖。刷新用 `PropRefreshBits` 位掩码精确触发，且支持组合（`REFRESH_WINDOW_STATES = (1 << 5) | REFRESH_RULES`）。**校验器也是值对象**（`vec2Range(-250,-250,250,250)`、`strChoice`）。

5. **Blur 的 Provider / Material 双层拆解**（新颖 3 / 实用 4 / 可迁移 4）
   `IBlurProvider` 管语义（是否动画、是否 live blur、damage 怎么外扩），`IGLBlurMaterial` 管绘制（需要什么 fragment）。10 个特效通过继承 `CDualKawaseBlurProvider` + 注入 Material 复用降采样/升采样链。`CRippleBlurMaterial` 甚至在构造函数里就订阅了鼠标事件，把「按住拖动产生涟漪」做成材质级副作用。

6. **GPU 上的实时流体求解驱动 UI 特效**（新颖 4 / 实用 2 / 可迁移 2）
   `FluidJar.cpp`（34KB）+ 9 个 `fluidjar*.frag`（init / step / resample / historyresample / trackingresample / graph / visual / finish）把 Navier-Stokes 求解器接进「窗口圆角处的液体晃动」。这是从游戏图形搬来的。

7. **网格变形 + Spring 积分的 CPU 侧 UI 物理**（新颖 3 / 实用 4 / 可迁移 3）
   `CDeformableMesh` 用 （N×N） 网格，每点存 displacement + velocity，用 `Hyprutils::Animation::SSpringCurve` 积分推进，输出带 UV 的顶点直接进 GPU。

8. **Damage 追踪的事务化**（新颖 3 / 实用 5 / 可迁移 5）
   `CDamageRing::CTransaction` 在 RAII 析构时自动 rollback——**异步 GPU 提交失败时 damage 不丢**。`COutputCommitCoordinator` 统一管理同步/异步提交与 direct scanout 分支。

9. **x86-64 RIP-relative 感知的函数 trampoline hook**（新颖 4 / 实用 2 / 可迁移 2）
   `HookSystem.cpp` 用 udis86 探测最小跳转长度，并手工反算、改写 RIP 相对位移，让被覆盖的指令在新 trampoline 位置仍指向正确的绝对地址。逆向工程手法搬进插件系统。

10. **「选择器」式场景抽象替代通用 Scene Graph**（新颖 3 / 实用 4 / 可迁移 4）
    `eSceneMode` + 纯函数 `sceneSelectsWindow(mode, SSceneWindowState)`，场景是一组选择规则而不是一棵可变的图层树。快照渲染复用同一套逻辑，且可单测（`tests/render/SceneSelection.cpp`）。

### 可复用的模式与技巧

1. **一行声明式配置项** — 桌面应用、CLI 工具、插件系统的配置层通用
2. **位掩码增量刷新依赖** — 热重载系统、配置驱动的 UI 框架
3. **配置值的类型化多语言桥** — 一个 `IValue` 抽象 + 多个语言绑定实现，`data()`/`parse()`/`push()` 三虚函数完成双向
4. **Pass 元素元信息契约** — 2D 合成器、图表渲染、文档排版
5. **变换器链 + 几何预规划** — 可组合后处理管线（图像编辑器、视频滤镜链）
6. **语义/绘制双层特效抽象** — 特效系统、样式库
7. **脚本宿主分档超时看门狗** — 任何把脚本语言嵌入主进程的宿主（游戏 Mod、CI 流水线 DSL、编辑器插件）
8. **RAII 渲染事务** — 带异步 GPU 提交和部分重绘的系统
9. **纯函数场景选择器** — 多视图渲染、快照、测试友好的渲染逻辑
10. **错误用 `std::expected` 传播、不变量用断言** — 系统级 C++（全项目无 `try`/`catch`，不跨 C 边界抛异常）
11. **AI 协作规范文件（AGENTS.md）** — 任何接受 AI PR 的开源项目
12. **「不许写注释」的副作用** — AGENTS.md 要求「flag silent config breakage」，反过来养成了「配置项变更 = 行为变更 = 必须显式说明」的文化

### 关键设计决策

**决策一：渲染用「元素列表 + 遮挡分析」，而不是硬编码的绘制序列**

- **问题**：特效越多、装饰层越多，绘制顺序和裁剪逻辑越难维护；同时必须支持「只重绘损坏区域」。
- **方案**：`IPassElement` 抽象 + `CRenderPass::simplify()` 反向遍历做 damage 扣除。
- **Trade-off**：每个元素类型要实现 8+ 个虚函数（样板代码多）；换来的是新增特效不碰核心循环，外加 `debug:pass` 全链路可视化。
- **可迁移性**：**高**——任何「多 pass + 局部重绘」系统的通用骨架。

**决策二：Lua 化配置，但配一道看门狗**

- **问题**：用户 Lua 跑在合成器主线程上，一个死循环就能冻结整个桌面。
- **方案**：debug hook 指令计数 + 7 档分场景超时 + 深度上限 32 + 错误去重。
- **Trade-off**：用户的复杂计算可能被误杀（50ms 的 layout 回调对重布局来说偏紧）；换来的是「用户脚本无法搞挂合成器」。
- **可迁移性**：**高**。

**决策三：布局算法定接口，实现交给 Lua**

- **问题**：布局是用户最想改的部分，但 C++ 插件改布局要重编译。
- **方案**：`Layout::ITiledAlgorithm`（10 个纯虚方法），`CLuaTiledAlgorithm` 实现它；C++ 侧 `pushLayoutContext` 把 targets 和 area 推给 Lua，Lua 侧 `target:place(box)` 回写几何。
- **Trade-off**：Lua 布局每帧跨语言往返且受 50ms 超时限制；换来 `example/layouts/{grid,columns,manual,spiral}.lua` 这样的用户可写布局。
- **可迁移性**：**高**——「核心算法定接口 + 脚本语言做实现」是插件系统的经典分层。失败时优雅降级（`callRecalculate()` 返回 false 就 `applyDefaultGrid`），**Lua 布局写错不会让窗口消失**。

**决策四：动画配置建成一棵树**

- **问题**：「所有窗口动画」「所有工作区动画」「边框角度」天然有层级关系，声明式配置里手写重复难维护。
- **方案**：`AnimationTree.cpp` 显式建树（global → {windows, layers, fade, border, workspaces, ...}；fade → {fadeIn, fadeOut, fadeSwitch, ...}）。
- **Trade-off**：树的形状硬编码在 C++ 里，新增节点要改代码——这与「新增配置项只要加一行」形成鲜明对比，**Hyprland 的可扩展性在不同维度上并不均衡**。
- **可迁移性**：**高**——层级化配置继承是通用模式。

**决策五：插件允许挂钩任意 C++ 内部函数**

- **问题**：硬编码的回调注册表无法覆盖「我想改一个已有函数的某个分支」。
- **方案**：udis86 定位函数 + jmp rel32 + RIP 相对寻址手工修正。
- **Trade-off**：**这是明确的架构负债**——`PluginAPI.hpp` 开头就警告「no ABI compatibility is guaranteed」；插件崩溃 = 合成器崩溃；编译器优化可能让 hook 目标失效；x86-64 独占（`#if !defined(__x86_64__) return false`）。
- **可迁移性**：**低**——属于「能做到但不推荐」的极端手段。它的价值在于证明「受限的回调 API 真的不够用」这个需求是存在的。

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | **Hyprland** | niri | sway | wayfire |
|------|---------|--------|--------|--------|
| Star（2026-11） | **39.4K** | 28.8K | 17.5K | 3.1K |
| 许可证 | **BSD 3-Clause** | GPL-3.0 | MIT | MIT |
| 技术底座 | C++ 160K 行，**自建图形栈**（aquamarine） | Rust + Smithay，**不用 wlroots** | C + **wlroots** | C++ + **wlroots** |
| 渲染特效 | 11 种模糊 + 52 个自研 shader + spring/bezier 动画 | 无特效管线（明确不做） | 无 | 成熟的插件特效体系 |
| 混合模式 / 通用效果模型 | 无（特效逐个 shader 硬写） | 无 | 无 | 有（Compiz 传统） |
| 配置 | **Lua**（0.55 起）/ hyprlang | KDL 声明式 | i3 风格文本 + shell | wayfire.ini |
| 布局可编程 | `ITiledAlgorithm` 接口，Lua 可实现 | 内置滚动布局 | 内置 | 插件实现 |
| 插件系统 | hyprpm + 函数级 hook（38 个 API） | 无 | 无 | 成熟插件生态 |
| 协议实现 | 自研 C++，65 个协议 | Smithay | wlroots | wlroots |
| 发布节奏 | 月度 minor + 周级 patch，**滚动发行** | 中速 | 慢而稳 | 中速 |
| 从 sway 迁移成本 | 高（配置需全部重写） | 高 | **零** | 中 |

### 差异化护城河

**技术护城河（真实且可验证）**：不是「特效多」这件事本身，而是**特效、平铺、动画、配置四者深度咬合**的产物。竞品可以抄任何单项——niri 可以加模糊，wayfire 可以加平铺——但要凑齐这套组合，得重写渲染架构。而 aquamarine 的「与图形 API 无关」分层进一步降低了复制成本：**既是护城河，也是护城河的泄密口**。

**生态护城河（中等）**：hyprpm + 官方插件仓库（1.5K star）+ Lua 配置生态（Lua 化的配置比 hyprlang 时代更容易分享）。但插件数量相对 niri / sway 的用户基数并不大。另外许可证是一张被低估的牌：BSD 3-Clause 比 niri 的 GPL-3.0 更宽松，意味着**商业分发、闭源再打包、企业内嵌定制都无需承担 copyleft 义务**——在「独家赞助方本身就是商业发行版」的当下，这一点对潜在的二次开发者有实际吸引力。

**信任护城河（正在被侵蚀）**：作者个人品牌 + 20+ 篇博客 + 快速响应曾经是强信任来源。2025-04 清掉约 1,300 个 issue 改为 discussion-first、PR 需 vouch 且未 vouch 自动关闭、2024 年与 freedesktop.org 治理冲突被封禁——**治理收紧是以社区规模换维护者负担**。再加上 Omacom Foundation 独家赞助、而 Omarchy 本身就是最大下游用户，「上游独立性」这个品牌资产正在被稀释。

### 竞争风险

- **最可能被部分替代者：niri**。基数已接近，单维护者 bus factor 相同但代码量小一个数量级，Rust + Smithay 的架构趋势更强，若 niri 加入「可选特效插件」就会同时具备 Hyprland 的两项优势。Hyprland 的窗口是：niri 先在「极简 + 干净」上建立认知，再靠「特效」守住差异化象限。
- **最可能的「稳定替代者」：sway**。若 Wayland 生态的稳定性焦虑上升、或用户要一个「能放三年不动的桌面」，sway 会赢。
- **真正的最大威胁不是竞品，是自伤**。中位 release 间隔约 24 天 + 破坏性变更常态化（0.55 直接把配置语言换成 Lua）+ 单人主导 61.3% + 色彩管理三年 low prio——**项目自身的持续破坏性创新会消耗用户耐心，而这一点竞品既无法复制也无需担心**。

### 生态定位

Hyprland 是 **Wayland 桌面「效果与交互创新」的震中**，而不是「最稳定的 Wayland 桌面」。它的真实角色是双重的：

1. **前沿特性先行者**——把「合成器可以长什么样」的可能性推到最远，并让这些可能性被大众配置复现。
2. **下游产品底座**——aquamarine、hyprutils、hyprlang、hyprgraphics、hyprcursor 构成的 hyprwm 全家桶被 14+ 个项目共享（Hyprland 只是旗舰），而 Hyprland 自己又是 Omarchy 的默认合成器。

从「谁在用」看：Arch/Nix 社区的默认选择、YouTube 桌面内容创作者（发现渠道占比从 22% 涨到 33%）、以及大量基于 Hyprland 配置的「桌面美化」教程形成的自发传播网络。**它不只是软件，还是一个内容生态的圆心。**

## 套利机会分析

- **信息差**：star 维度上没有洼地——39K star 早就是大众项目。但**文档维度上有**：它有 39K star，却几乎没有内部架构文档。wiki 全是「怎么配」不讲「怎么实现」，DeepWiki 只覆盖到 Core Architecture / Rendering System 这一层，aquamarine、hyprgraphics、效果着色器管线基本没有中文解读。**高 star + 低文档密度**，这对读者是真金白银的价值。
- **技术借鉴**：配置注册表一行声明 + 位掩码刷新、Lua 宿主看门狗、Pass 元素元信息契约、RAII 渲染事务、纯函数场景选择器——这五条是通用模式，与图形无关，任何桌面应用、编辑器、CI 工具都能用。插件 hook 那条**不建议抄**，但值得读懂它为什么存在。
- **生态位**：它填的空白是「Linux 桌面的视觉表达层」。KDE 有特效但平铺弱，sway 有平铺但没特效，niri 有干净的滚动平铺但主动放弃特效——**Hyprland 在「动态平铺 × 视觉特效 × 可编程配置」这个交叉象限里没有同级对手**。
- **趋势判断**：还在涨，但增速在放缓。103 天 +2,390 star ≈ 23/天 ≈ 700/月（区间涨幅 6.5%），远低于 2025-07 单周 +1,426 的爆发峰。技术上符合趋势——Wayland 取代 X11 是确定性方向，桌面级特效是 macOS/Windows 用户迁移到 Linux 的最大心理门槛，而 Hyprland 正在做的是「把迁移的最大心理门槛拆掉」。相比 niri，Hyprland 的后发优势不在架构（Rust 更现代），而在**它把「用户是否愿意留下」这件事解决得更好**。

## 风险与不足

1. **Bus factor 实质为 1**。`vaxerski`（2,848 commits）与 `Vaxry`（2,054 commits）是同一人（作者改名 + 换邮箱，GitHub 按名+邮箱分别聚合），合并后占全部 7,993 次提交的 **61.3%**。他一个人比第二名到第十名加起来（3,058）还多。关键影响是：**重构只有唯一懂全局设计意图的人能安全执行，所以重构被无限期推迟**——低 refactor 率不是意识问题，是人力结构问题。
2. **重构欠账与上帝文件**。重构类 commit 仅占 1.5%（200 条样本口径），注释率仅 3.9%（1:25.5，对 16 万行而言明确偏低）。`Renderer.cpp` 3,777 行、`OpenGL.cpp` 2,722 行、`Monitor.cpp` 2,758 行。代码里留着 `// FIXME: why does this break on * 1.F ?` 和 `// eh, this is not the correct solution, but it will do`——**这些注释标记的正是渲染正确性这个最脆弱的地方**。
3. **测试不在 CI 门禁上**。有 gtest 单元测试（`tests/` 13 个子目录）和独立集成测试子项目 `hyprtester/`，但 `make test` 需要 Debug + `-DTESTS=true`，而 CI 的 `ci.yaml` **只做构建和 clang-format 检查**。也就是说：任何 PR 只要能编译、格式对，就能合入，哪怕它破坏了渲染正确性。考虑到破坏性变更常态化，这个缺口风险不低。
4. **破坏性变更常态化**。中位 release 间隔约 24 天，0.55 直接把配置系统换成 Lua。滚动发行（Arch/Nix 跟随 git main）让 SemVer 事实上失去用户契约意义——**它有语义化版本号，但用户拿到的永远是昨天的未发布主干**。
5. **色彩管理三年未做**。`wp-color-management-v1` 协议已实现、lcms2 ICC 加载器已写好、shader 里有 `cm_helpers.glsl` / `tonemap.glsl`、DRM `CTM`/`GAMMA_LUT`/`HDR_OUTPUT_METADATA` 都已开工，但 issue #9064 仍标 `0: low prio`。一个色彩正确性的桌面用了三年还没做完。
6. **没有通用混合模式系统**。52 个自研 shader 特效并存，却 grep 不到任何 `blend_mode` / `hybrid` 抽象。相对 KWin 与 macOS 合成模式是明确的功能缺口——架构后果是「特效靠 shader 硬写，不走通用混合模型」。
7. **GPU 恢复路径不牢固**。issue #804（挂起恢复崩溃，165 条评论，全项目最大 issue 线程）、#6967（`m_pAqBackend couldn't start`，105 条）、#4744（GPU fix 后花屏，89 条）构成同一类问题。**这是「自建图形栈必须自己扛下的全部代价，而 wlroots 用户不用扛」。**
8. **插件 hook 无 ABI 保证**，插件崩溃即合成器崩溃，且 x86-64 独占。
9. **文档完全外置**。仓库内只有 2 个 man page 和 1 个 ISSUE_GUIDELINES.md，无架构文档、无 ADR、无 CHANGELOG、无 CONTRIBUTING（全部在 wiki.hypr.land）。对 compositor 来说合理（配置项数以百计且随版本滚动），但代价是**长期知识只存在于项目外的 wiki 与维护者脑中**，新人入门成本被推高。
10. **赞助集中度**。独家赞助 + 赞助方即最大下游用户，叠加既有的单人主导，风险从「资金」转移到「治理集中 + 关键人依赖」。

## 行动建议

### 如果你要用它

**选它的场景**：你是 Arch/Nix 用户，愿意把桌面当作品经营；你要的是「既有 Wayland 的正确性，又有 macOS 的观感」；你享受自己写 Lua 配置和自定义布局。

**别选它的场景**：你需要「装完三年不动」的稳定桌面——滚动发行 + 24 天中位 release + 破坏性变更是它的设计，不是缺陷；你依赖 i3/sway 的配置生态（迁移成本高）；你的机器有 Intel 核显 + NVIDIA 双显卡且关心挂起恢复稳定性；你在意色彩准确性（CM 还没做完）。

**从谁迁**：从 sway 迁 = 配置全重写 + 肌肉记忆重建，成本最高；从 niri 迁 = 布局思维要从滚动切到 dwindle/master，但视觉能力是净赚；从 GNOME/KDE 迁 = 心智负担最轻但要接受「一切都要自己配置」。

### 如果你要学它

按这个顺序读，五条核心模式：

1. **`src/render/pass/PassElement.hpp` + `Pass.cpp`** — 元素元信息契约与反向遮挡分析。这是全项目最值得抄的一块。
2. **`src/render/transformer/TransformerList.cpp`** — Plan/Execute 两阶段几何预规划。
3. **`src/config/values/ConfigValues.cpp` + `types/IValue.hpp`** — 一行声明一个配置项的注册表模式（与图形无关，纯工程价值）。
4. **`src/config/lua/LuaCaller.cpp`** — 嵌入不可信脚本的看门狗/超时/错误去重三件套。
5. **`src/output/DamageRing.hpp`** — RAII 事务化的渲染损伤管理。

补充阅读：**`AGENTS.md`**（AI 协作规范模板，可以直接借鉴）；**`src/plugins/HookSystem.cpp`**（读懂它为什么存在即可，别抄）；**`src/render/gl/blur/FluidJar.cpp`**（GPU 流体求解，纯看热闹）。

### 如果你要 fork 它

- **最值得做的方向**：色彩管理补完（`src/helpers/cm/` + `src/render/shaders/glsl/cm_helpers.glsl` 已有地基，issue #9064 有完整讨论）——这是全项目最大的一块功能缺口，且原作者自己也承认它被排在了低优先级。
- **第二方向**：把 `Renderer.cpp`（3,777 行）和 `OpenGL.cpp`（2,722 行）拆开。风险极低（重构比例低说明有大量「本可以更早拆开」的历史债），收益是让社区能真正分担渲染层——而渲染层现在恰好是社区最不敢碰的部分。
- **第三方向**：补一个通用的混合模式 / 效果模型层，把现在的「一个效果一个 shader」变成「效果 + 通用混合模型」，顺便追平 KWin / macOS 的合成模式能力。
- **先别碰的**：协议层（65 个 .cpp 已经是社区分工区，再加协议只会增加维护面）；插件 hook 机制（没有 ABI 承诺就是没有承诺）。
- **如果只是想用**：别 fork，去写配置和 Lua 插件，成本低两个数量级。

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | [deepwiki.com/hyprwm/Hyprland](https://deepwiki.com/hyprwm/Hyprland)（已收录，含 Core Architecture / Rendering System / Surface Management 多页，另有 [hyprwm/hyprland-wiki](https://deepwiki.com/hyprwm/hyprland-wiki) 与 [hyprwm/aquamarine](https://deepwiki.com/hyprwm/aquamarine)） |
| Zread.ai | [zread.ai/hyprwm/hyprland](https://zread.ai/hyprwm/hyprland)（疑似已收录，但 Cloudflare Challenge 拦截无法验证） |
| 官方 Wiki | [wiki.hypr.land](https://wiki.hypr.land)（配置与使用文档；架构文档缺失） |
| 官方博客 | [hypr.land/news](https://hypr.land/news)（26 篇发布与公告，带 RSS） |
| 作者博客 | [vaxry.net](https://vaxry.net)（20+ 篇长文，含第四次 [Census](https://blog.vaxry.net/articles/2024-fourth-census)、[全职开发说明](https://blog.vaxry.net/articles/2023-workingFullTime)） |
| 架构里程碑文章 | [Hyprland is now fully independent!](https://hypr.land/news/independentHyprland)（2024-07-21，与 wlroots 分家的全过程） |
| 赞助公告 | [Omacom Foundation to be exclusive Hyprland sponsor](https://omarchy.org/news/2026/08/omacom-foundation-to-be-exclusive-hyprland-sponsor/) |
| 独立评测（对比） | [Hyprland vs Sway vs River](http://www.bigiron.cc/guides/hyprland-vs-sway-vs-river-tiling-wm-comparison) —「用 Hyprland 是你在组装一个 DE，不是在装一个 DE」 |
| 独立评测（批评） | [Why I'm Eyeing FHT-Compositor as a Hyprland Alternative](https://axos-project.com/blog/fht-compositor/) —「依赖意大利面轮盘」「允许插件挂钩任意 C++ 函数在结构上就不可能稳定」 |
| 硬件侧印证 | [Patching Aquamarine for an LG UltraFine 5K](https://zhengnanli.gitlab.io/blog/lg-ultrafine-5k/) — 从输出 tiling 视角印证 aquamarine 的分层价值，同时暴露多 head 原子提交与雷电带宽问题 |
| 关联论文 | 无（arXiv / Semantic Scholar 上不存在 Hyprland 相关论文或学位论文；搜索命中的 `HyParLyVe`、`HyLaR` 均为字符串巧合。另有内容农场把 man page 套进伪造的「论文模板」并附会虚假作者与引用，属 SEO 投毒，不应引用） |
| 在线 Demo | 无（可交互的替代物是官网 [hypr.land/videos/](https://hypr.land/videos/) 下的 rice 演示视频与 Hall of Fame） |
