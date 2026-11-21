# GitHub推荐：11,912 star 的 OpenVINO：动态 LLM 怎么塞进 NPU

> GitHub: https://github.com/openvinotoolkit/openvino

## 一句话总结

Intel 官方的通用 AI 推理运行时，用一套版本化 IR 把「训练框架里的模型」变成「跨 CPU/GPU/NPU 可部署的产物」；真正让它在 2026 年重新变得值钱的，是 NPUW —— 一套把动态形状 LLM 拆成 Prefill/Generate 两个静态子图、再按 prompt 长度编译 KV 容量变体阶梯的软硬件协同方案，这是 llama.cpp、TensorRT、ONNX Runtime 都做不到的那一块。

## 值得关注的理由

1. **14 个月来首次登上 Trending，且还在加速**：本仓库自建的 Trending 归档（2025-09-22 ~ 2026-11-20，11,502 条记录、1,440 个不同仓库）显示，OpenVINO 在 **2026-11-18 才第一次**出现在 Trending 榜上，此后连续三天在榜（排名 #14 → #8 → #8），48 小时 star 从 11,285 涨到 11,737（+452）。而月度榜排名仍是 #97——它才刚刚回来。11,912 star 这个数字是「重新起跑前的存量」，不是增长曲线的终点。
2. **NPUW 是一道结构性护城河**：Intel NPU 的 blob 形状是固定的、**完全不支持动态形状**，而 LLM 的输入形状天然动态。OpenVINO 的解法不是「等硬件支持」，而是**在 IR 层把动态拆成静态**——同一份权重编译出 Prefill（seq_len=1024）和 Generate（seq_len=1）两个独立子模型，再按 prompt 长度编译 1K/2K/4K/8K 的 KV 容量变体阶梯，运行时选择、必要时中途升级并零拷贝迁移 KV。llama.cpp 没有 NPU 路径，TensorRT 直接拒绝动态形状，ONNX Runtime 虽有动态 shape engine 但没有 NPU 上跑 LLM 的能力。
3. **仓库里藏着一套「用 AI agent 半自动化造算子」的完整流水线**：`.github/agents-prototype/` 用 13 个 agent 定义（2,665 行）+ 9 个 skill 目录（30+ step 文件）+ 确定性 fallback 脚本，把「加一个 PyTorch 算子要动前端规则/core op spec/CPU kernel/GPU kernel/NPU 变体/测试六个技术栈」这件人力最难规模化的知识型工作，变成了可编排的流水线。这不是 demo——它直指 issue #29696 暴露的真实 op-parity 债务。

## 项目展示

![OpenVINO 全景架构图](https://raw.githubusercontent.com/openvinotoolkit/openvino/master/docs/articles_en/assets/images/openvino-overview-diagram.jpg)
IR 为中心的分层结构：前端归约到统一 IR，插件从 IR 编译出各硬件 blob

![GenAI 架构图](https://raw.githubusercontent.com/openvinotoolkit/openvino/master/docs/articles_en/assets/images/genai_main_diagram.svg)
GenAI 层的推理流水线，与下层编译时优化解耦

![开发流程图](https://raw.githubusercontent.com/openvinotoolkit/openvino/master/docs/articles_en/assets/images/DEVELOPMENT_FLOW_V3_crunch.svg)
从模型接入到算子落地的开发流程——这张图解释了 issue #29696 为什么会反复发生

![低精度转换流水线](https://raw.githubusercontent.com/openvinotoolkit/openvino/master/docs/articles_en/assets/images/low_precision_transformation_pipeline.svg)
LPT 的 markup 打标 → transformation 变换两阶段量化管线

![Physical AI](https://raw.githubusercontent.com/openvinotoolkit/openvino/master/docs/articles_en/physical-ai/assets/physicalai.svg)
2026.3 起新增的机器人 VLA 方向，是 OpenVINO 开辟的新战场

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/openvinotoolkit/openvino |
| Star / Fork / Watcher | 11,912 / 3,650 / 193（open issues 412，open PRs 780） |
| 代码行数 | 2,412,968（C++ 65.9% + C++ Header 10.4%、Python 6.6%、JSON 5.7%、CMake 1.3%；16,588 文件） |
| 项目年龄 | 97.3 个月（2018-10-15 首次提交，至今） |
| 开发阶段 | 密集开发（近 30 天 425 commits、近 90 天 1,131、近 365 天 3,471） |
| 贡献模式 | Intel 官方组织 + 社区协作（915 名贡献者，Top 1 仅占 4.6%，Top 10 中含 2 个 bot） |
| 热度定位 | 大众热门 · 近期二次加速（14 个月来首次 Trending，48h +452 star） |
| 版本 | 2026.4.1（日期版本 YYYY.M.P，90 tag / 65 Release） |
| License | Apache-2.0（纯开源，无 open-core 附加条款） |
| 质量评级 | 代码[优秀] 文档[优秀] 测试[充分] CI[完善] |

## 作者视角：为什么存在这个项目

### 创始人/作者背景

OpenVINO 不是个人项目，是 **Intel 官方开源组织**（`openvinotoolkit`，7.2 年账号，1,932 粉丝，47 个公开仓库）。它的前身是 Intel 的 CVSDK / MKL-DNN 血统：OV1 时代（2018-10 至 2020-03）几乎是休眠状态，**2019 全年只有 11 个 commit**——那时它还叫 OpenVINO Toolkit，只是个「Intel CPU 上的 OpenCV DNN 加速器」。

真正让它活过来的是 **2020-04 的 OV1→OV2 重写**：单月 commit 从 20 跳到 142，2020-05 达到 346，此后稳定在 200~470/月。这次重写把 OV1 的「一个巨大的 CPU 推理器」切成「独立 IR + 插件化后端」，**一次性付清了架构债**——今天 `src/core/src` 的改动量在热点目录里垫底（1,485 次，排在第 10），`refactor` 类 commit 只占 0.5%，`Fix:Feature ≈ 1.9:1`。这是一个已定型、仍在持续加固的工业产品，不是还在快速改头的实验。

团队形态从数据上一目了然：915 名贡献者，Top 1（Ilya Lavrenov，1,287 commits）只占 4.6%，Top 10 里有两个 bot（dependabot 665、github-actions 655）。**真人核心贡献者分布平坦**——Ilya Churaev（OV 编译器主设计者）、Maxim Vafin、Sebastian Golebiewski、Roman Kazantsev、Karol Błaszczyk、Pawel Raasz、Vladimir Paramuzov 各自数百次提交，没有单点依赖。周末提交占比仅 3.4%、深夜 11.4%，是典型企业团队作息。

### 问题判断

**作者看到的不是「缺一个算子」，而是「算子覆盖率永远追不上」。**

issue #29696（`aten::fractional_max_pool2d`，69 条评论）把完整模式暴露了出来：开发者提 issue → 维护者评估「这个算子可能无法分解」→ 长期无人认领 → 重开 → 再分配。这是一条**组织化的 op-parity 债务**，不是 bug。

于是问题被重新定义为：「如果加一个 PyTorch 算子到 OpenVINO 的成本是 3 人周（前端转换规则 + core op spec + CPU kernel + GPU kernel + NPU 变体 + 测试 + opset 文档），那么 AI 辅助能不能把这个成本降到 1 天？」

**时机选择的三个拐点：**

1. **2020-04 的 OV2 重写** —— 留下 `src/plugins/template/` 这个「活的扩展点」（1,317 次改动），说明「加新硬件后端」是真实且持续的需求，不是一次性设计。
2. **2023 起的 LLM 转型** —— 从「CV 推理器」变成「LLM 运行时」，催生了 NPUW。NPU 不支持动态形状这条硬件约束，逼出了 Prefill/Generate 静态子图这个核心设计。
3. **2025-26 的 NPU / Physical AI 转向** —— 2026 年 10 月 commit 重回 403，NPUW 目录 83 个文件，`src/frontends/gguf/` 单独以 1,265 次改动入榜（主动切入 llama.cpp 生态的权重格式），新增机器人 VLA 运行时文档。

**2026 年最新的一层信号**：Intel 把 agentic workflow 引进了自身 CI。`.github/workflows/ci-doctor*.md` 用 GitHub 的 `gh-aw` 框架让 agent 自动分析失败的 pipeline 并给修复建议；`agents-prototype/` 则用 agent 补算子。issue #38425 里反复出现 `agent_failure` / `detector_execution_failure`，说明这套自动化自身还不稳——但方向明确：**用一个 agent 去修 CI，用另一个 agent 去补算子**。

### 解法哲学

**明确选择了什么：**

1. **「开放 IR + 多后端插件」而非「单一硬件极致优化」**。核心是 `ov::Model`——一个可序列化、有 opset 版本、有 schema 的中间表示。8 个前端（ONNX/PyTorch/TF/TFLite/Paddle/JAX/GGUF/IR）全部归约到它，8 个后端（CPU/GPU/NPU/template/hetero/auto/auto_batch/proxy）全部从它出发。
2. **「编译时优化、运行时极简」**。layout 重排、算子融合、常量折叠、量化、16B 对齐全在 `compile_model()` 里做完；运行时只做「喂数据 → 拿结果」。这是 OpenVINO 与 ONNX Runtime 最本质的分野。
3. **「开放的插件契约」**。`iplugin.hpp` 只有 12 个纯虚方法，而 `src/plugins/template/` 是一个**可编译可运行的官方插件模板**——plugin / compiled_model / sync_infer_request / async_infer_request / remote_context / variable_state / HSM blob 读写 handler 全套骨架都在。

**明确不做什么**：不做训练（仓库里没有任何 autograd、optimizer、backward pass）；不做动态图 JIT 运行时（IR 是完全静态声明式的）；不做私有二进制格式垄断（IR 是人可读的 XML + BIN，可 diff、可版本化）。

**代价是真实的**：TensorRT 的 GPU 峰值性能约为 OpenVINO 的 7 倍（7,500 vs 1,100 FPS），且原生支持 INT4。这个差距来自「为单一硬件写极致 kernel」，通用性必然稀释每个后端的极致程度。OpenVINO 的应对不是硬追 GPU 峰值，而是**把 NPU 变成一等公民**——当 NPU 成为 AI PC 的默认推理设备时，「NPU 独占 + NPUW 独占 LLM 支持」这个组合是 TensorRT 结构上无法复制的。

### 战略意图

**在 Intel 更大图景中的位置：**

```
Intel AI Stack
├── openvino.genai        ← 何时推理（pipeline、采样器、chat template）
├── openvino              ← 怎么推理（IR、编译、后端）  ← 本仓库
│   └── npu_compiler      ← 硬件执行什么（MLIR lowering 到 NPU）
├── openvino.model_server ← 服务化
├── NNCF                  ← 训练后压缩
└── physicalai            ← 机器人运行时（2026.3 新增）
```

Intel 的算盘很清楚：**AI PC 换机周期（2024-2026）+ NPU 从「可选加速器」变成「必选部件」+ Gaudi 数据中心**。开源推理栈是硬件出货的配套软件——这是 OpenVINO 存在的根本商业逻辑。

**开源策略是 genuinely open，不是 open-core。** 纯 Apache-2.0，无 BSL、无 use-restriction；代码完整公开；**NPUW 最有价值的部分全开源**（83 个文件、2,364 行的核心编译逻辑）——这在硬件厂商里相当罕见，通常 NPU 专属推理优化会藏起来，因为它绑定硬件。OpenVINO 把 NPUW 全开源，等于用「NPU 上也能跑开源 LLM」反向推动 NPU 出货。唯一的「闭源」是真正的 NPU 编译器 `npu_compiler`，那是独立仓库。

Apache-2.0 对 Intel 而言不是「友好」，而是**必要**——企业 IT 采购需要无 copyleft、无专利授权风险、可商用修改。这是这个规模的工业软件能进企业采购清单的前提。

## 核心价值提炼

### 创新之处

按新颖度 × 实用性排序：

1. **NPUW 的 Prefill/Generate 双静态图 + KV Cache 变体金字塔**
   把动态形状 LLM 拆成两个静态子模型共享 KV cache，并按 prompt 长度编译 1K/2K/4K/8K 多个 KV 容量变体，运行时选择、必要时中途升级并零拷贝迁移 KV。核心代码在 `src/plugins/intel_npu/src/plugin/npuw/llm_compiled_model.cpp`（2,364 行）的 `create_generate_model_variants`：变体按 `base_size` 翻倍增长，解码中当前变体满了就 `try_switch_to_larger_variant()` 升级并重绑 KV tensor。
   新颖度 4/5 · 实用性 5/5 · 可迁移性 4/5 —— 思想可迁移到任何固定形状加速器，但具体实现（按输入名猜语义、BNSD 布局转换）耦合太深。

2. **KV Cache 策略的「生命周期钩子契约」**
   `LLMKVCacheStrategy` 用 10 个虚方法定义完整生命周期（initialize / reset / prefill_begin / prefill_done / generate_init / generate_done / variant_switch / rerotate / continue_prefill）。**接口注释直接写明失败语义**——`rerotate_longrope_keys` 约定「all or nothing」，`continue_prefill` 约定「验证阶段无副作用、验证失败后 cache 原样；越过验证后失败则状态未定义，调用方必须 reset + 完整 prefill」。两阶段失败语义写进接口契约，这在 C++ 推理引擎里很罕见。
   新颖度 4/5 · 实用性 5/5 · 可迁移性 5/5。

3. **用 AI Agent 编排半自动化造算子**（OpenVINO 特有）
   13 个 agent 定义 + 30+ skill step 文件 + 确定性 fallback 脚本 + 集中 PR 所有权 + 双闸门验证 + 迭代熔断，构成一条「报错 → 分类 → 并行实现 → 验证 → 开 PR」的完整流水线。详见下方可复用模式。
   新颖度 5/5 · 实用性 4/5 · 可迁移性 5/5。

4. **拓扑序重写引擎带来的「免费级联折叠」**
   `GraphRewrite` 按拓扑序遍历 + 节点 ID 单调，使得前面 pass 的成果自动让后面的 pass 触发：`m1` 把 `Abs2(Constant1)` 折叠成常量 → `m2` 把 `Neg3(Constant1)` 折叠 → `m3` 走到 `Add4` 时发现两者已是常量，`Add4` 自动也能折叠。同时约束「只能替换拓扑序靠前的节点」，保证不漏处理新产生的节点。
   新颖度 3/5 · 实用性 4/5 · 可迁移性 5/5。

5. **ONNX 前端的「版本区间注册」翻译表**
   `{domain: {op_type: {version: {func}}}}` 四层结构 + `OPSET_RANGE/SINCE/IN` 宏。`ONNX_OP("Abs", OPSET_RANGE(1, 5), ai_onnx::opset_1::abs)` 与 `ONNX_OP("Abs", OPSET_SINCE(13), ai_onnx::opset_1::abs)` —— **opset 1-5 和 13+ 复用同一个实现体**，新版本只写差异，让 ONNX opset 的历史演进几乎零成本。
   新颖度 3/5 · 实用性 5/5 · 可迁移性 5/5。

6. **「能力声明 + 贪心切分 + 回滚」的 HETERO 异构编排**
   插件声明支持的 op 类型（affinity），HETERO 贪心合并相邻节点，检测到间接自引用就回滚最后一个节点并加入 rejected 列表。README 用 11 步 mermaid 推演完整算法。
   新颖度 3/5 · 实用性 4/5 · 可迁移性 4/5。

7. **LPT 的「markup 打标 + transformation 变换」两阶段量化**
   markup pass 只打标记决定「哪个节点将以什么精度被量化」（不改图），transformation pass 再把标记变成实际的 FakeQuantize/Convert 节点。决策与实现解耦，markup 结果可被 NNCF 等外部工具复用。源码 60+ 文件，含测试共 295 个。
   新颖度 3/5 · 实用性 4/5 · 可迁移性 4/5。

### 可复用的模式与技巧

按可直接迁移价值排序：

1. **Agent 流水线四件套** —— `agents/*.agent.md`（角色 + 输入输出契约 + 约束）+ `skills/<name>/stepN-*.md`（可复用步骤）+ `pipeline_state.json`（跨 agent 共享记忆）+ 确定性 fallback 脚本。适用场景：任何多 agent 协作系统。
2. **路由信号带置信度 + 低置信度退回确定性脚本** —— LLM 分类结果附 `confidence: high|medium|low`，low 时走 `classify_component.py` 的 `error_class → component` 映射表。**知道什么时候不该信自己**，是 agent 系统可靠性的关键。
3. **集中 PR 所有权 + 子 agent 只出 patch** —— 所有子 agent 带 `pr_mode: delegated_to_orchestrator`，禁止自己开 PR；只有编排器在最后一阶段开一个集中 draft PR（含分支命名、已有 PR 去重、fork 创建的 helper）。适用场景：并行 agent 改同一仓库。
4. **迭代上限 + 「有进展就不熔断」** —— `invocation_count >= 5` **且**尚无任何 patch 才提前退出；一旦有 patch 就允许跑完。注释里说明 5 故意比完整流程的 7 次调用宽松，只在「完全没进展」时熔断。
5. **双闸门验证** —— Phase 5 build+ctest+推理 sanity，Phase 6 E2E 转换 + 数值检查（新架构清单：FP16/BF16 精度、共享 KV cache、IR 正确性、测试覆盖）。任一失败 → 带着编译错误重新派发给负责的 agent，不开 PR。
6. **诚实的 non-blocking 标注** —— 明确标出「NPU is always non-blocking (agent currently non-functional)」，编排器里三处强调。**渐进式引入 agent 的团队最需要这个**：标明哪些还不行，比假装都能用更可靠。
7. **生命周期钩子契约（Lifecycle Hook Contract）** —— 抽象基类用一组虚方法定义组件完整生命周期，接口注释写明调用顺序与失败语义。适用场景：复杂状态机、多策略实现、跨阶段数据交接的子系统，尤其适合 C++ 这类没有编译期约束的语言。
8. **拓扑序 + 级联重写引擎** —— 按拓扑序遍历 + 「只能替换靠前节点」的约束 → 前面 pass 的成果自动级联；需要多次融合时提供显式 `register_new_node` 逃生口。
9. **版本区间注册表（Version-Range Registry）** —— 翻译函数按 `{domain: {op: {version_range: fn}}}` 注册，同语义跨版本复用实现体。
10. **插件化的元插件（Meta-plugin over Plugins）** —— 把「设备调度 / 异构切分 / 自动批处理」实现成和普通插件同契约的插件，复用同一套加载与协商机制。
11. **两阶段决策-执行分离（Markup → Transformation）** —— 先打标后变形，标记可被外部工具消费。
12. **IR 层的「编译期约束反向传播」** —— 把 NPU 的整数/静态形状约束在 IR 变换层解决（`ReshapeToStatic`、`convert_kvcache_to_precision`、`fold_scalar_dq`、`broadcast_u2_zero_point`），而不是等编译失败才报错。
13. **切片的零拷贝视图 + 显式 layout 转换** —— KV cache 交接用 `make_tensor_slice` 做零拷贝视图，只有 prefill↔generate 的布局差异（BNSD vs BSHD）才做显式 `copy_tensor_by_dim`。
14. **「API 契约即文档」的 C++ 接口注释风格** —— `kv_cache_block_manager.hpp` 里 `release(keep_warm_count)` 的注释直接给出性能推理：「NPU 重新分配会增加新会话首个 prefill chunk 的延迟，保留 ceil(prompt_len/block_size) 个热 block 可避免该延迟」。
15. **结构化调试 skill** —— `.agents/skills/ov-debug-matcher-pass/` 专门解决「MatcherPass 不触发、pattern 不匹配、callback 不执行」这个图优化框架最常见的调试困境。
16. **命名启发式 + 断言兜底的模型适配层** —— NPUW 通过 `input_name.find("input_ids")` 等判断输入语义，对不确定情况用 `NPUW_ASSERT` 而不是静默降级。

### 关键设计决策

**决策 1：IR 是不可变的、opset 版本化的、有 schema 的**

- **问题**：8 个前端、几十种框架版本、4 种真实硬件，要交换同一个东西。
- **方案**：`ov::Node` 是图的原子；每个 op 按 opset 版本分 namespace（`ov::op::v1::Relu` 与 `ov::op::v16::Relu` 是**不同的 C++ 类型**，IR 里共存），这是 OpenVINO 能同时支持老 ONNX opset 1 和新 opset 20 的原因。变换**永远不改原节点**：`clone_with_new_inputs()` 是纯虚函数，所有 op 必须实现，变换造新节点换输入后 `replace_node()`。序列化是 XML（结构/属性/opset 版本）+ BIN（权重）。
- **Trade-off**：牺牲编译期内存（每次变换都 clone 节点，issue #13601「Model compilation takes too much memory in cpp」57 条评论是长期痛点）；换来变换是纯函数式的、可组合可测试可并行，IR 是稳定的交换格式。
- **可迁移性**：**高**。「不可变 IR + clone 变换 + 版本化注册表」是编译器（MLIR/LLVM）和推理引擎（TVM、IREE）的通用范式。

**决策 2：Pass Manager 是「有序 pass 列表 + 拓扑序重写引擎」两段式**

- **问题**：一次编译要跑几百个变换，它们有依赖顺序，一个变换的结果会影响另一个能否触发。
- **方案**：`ov::pass::Manager` 持有**有序** pass 列表逐个执行，并只在某个 pass 真的改了图时才启用下一轮的 IR 结构校验（避免 O(N) 校验打爆编译时间）；模型是动态形状时自动跳过依赖静态形状的 pass。`ov::pass::GraphRewrite` 按拓扑序（args before users）遍历，对每个节点依次尝试已注册的 MatcherPass。模式匹配 DSL 提供 `wrap_type<T>` / `any_output<T>` / `label` / `optional` / `any_of` / `or` / `block` 配合 `has_class<T>()` / `shape_matches("1,3,224,224")` / `attrs_match()` 等 predicate。
- **Trade-off**：DSL 写错时是**静默不匹配**（不报错），调试困难——这正是 OpenVINO 专门写了 `ov-debug-matcher-pass` skill 的原因；换来融合 pass 可独立开发、独立测试、独立开关（PassConfig 的 enable/disable + callback）。
- **可迁移性**：**高**。

**决策 3：NPUW 把动态形状 LLM 拆成两个静态子模型**（本报告技术含量最高的部分）

- **问题**：NPU 的 blob 形状固定，**完全不支持动态形状**；而 LLM 的 prompt 长度、生成长度、KV cache 长度天然动态。
- **方案**：同一份权重编译出两个独立子模型——Prefill（`input_size = m_prefill_chunk_size`，默认 1024，批量处理 prompt 产出 KV cache）和 Generate（`input_size = 1`，单 token 解码，复用 prefill 的 KV）。切分由 `ov::npuw::ReshapeToStatic` 在 IR 层完成。KV cache 交接由 `LLMKVCacheStrategy` 抽象出两个实现：连续 buffer（chunk 边界 copy）和**固定大小 block 池 + 零拷贝 prefill**（`KVCacheBlockManager` 按 block 分配设备 tensor，`release(keep_warm_count)` 保留热 block 避免新会话首个 prefill 的分配延迟）。此外还有 chunked prefill、前缀缓存（`m_block_hash` + `m_parent_block_hash` 哈希链）、SWA 环形布局、GQA/MoE/LoRA/Eagle3/speculative decoding 各自的专门 pass。
- **Trade-off**：牺牲内存（每个变体是一份独立编译产物，四个变体四份 blob）、代码复杂度（两个核心文件 2,364 + 2,278 行）、正确性风险（prefill/generate 的 KV 布局不同，每次交接都要转置；`duplicate_shared_kv_concat` 这个 pass 的存在本身就是证据——GQA 模型共享 ReadValue/Assign 状态时权重折叠会重复应用导致 state 损坏，npu agent 里专门写了一段「NPUW Idempotency Guard」）、以及耦合到具体模型（`input_name.find("input_ids")` 这类启发式判断，Deepstack、PLE、Eagle3、Gemma3 token_type_ids、Qwen3-VL position_ids 各有特例）；换来 NPU 上真的能跑 LLM，且因为拆成两个静态图，NPU 编译器可以对 prefill（compute-bound，多 token GEMM 走 DPU 的 DPAS）和 generate（memory-bound，需读整个 KV cache）做不同优化。
- **可迁移性**：**中**。

**决策 4：Snippets 走运行时 JIT kernel 生成，而非 AOT**

- **问题**：绝大多数算子是 memory-bound（计算带宽增长快于内存带宽），优化点在于「每次 load 尽可能多复用」，需要针对具体 ISA（AVX2/AVX-512/AMX）生成不同机器码。
- **方案**：`src/common/snippets/`（174 cpp + 169 hpp）用 `MemoryAccess` 基类统一抽象 load/store，用 `PortDescriptor{count, offset, stride, index}` 描述访问模式；`lowered/pass/solve_buffer_memory.cpp` 解决 vertical fusion 后的 buffer 内存求解——这是融合的核心难点（融合改变了 buffer 的生命周期和复用关系）。设计指南开篇就把「计算带宽增长快于内存带宽 ⇒ 多数算子 memory-bound ⇒ 要做 vertical fusion 提高每次 load 的数据复用」讲清楚了。
- **Trade-off**：JIT 有首次编译延迟、生成代码调试困难、无法静态分析寄存器压力；换来**同一份 IR 在不同 CPU 上得到不同的最优 kernel**——AOT 方案（TVM 预编译 wheel、TensorRT 引擎）要么放弃 ISA 特化，要么维护多套预编译产物。
- **可迁移性**：**中**（思想通用，但完整的 buffer solver + emitter 体系工程量巨大）。

**决策 5：后端是可插拔的「插件」契约，元插件复用同一契约**

- **问题**：Intel 有 CPU/iGPU/独显/NPU 四种硬件，还有第三方和企业自研加速器。
- **方案**：`iplugin.hpp` 只有 12 个纯虚方法；插件通过 `plugin.xml` 声明式注册、运行时动态加载；特性协商用 `ov::Any`（类型擦除容器，能装任何 property 并直接暴露到 Python）。**hetero / auto / auto_batch / proxy 全是「用插件契约实现的元插件」**——正交设计。
- **Trade-off**：插件边界本身有成本（跨 so 边界的 `Any` 装箱、虚函数调用、无法内联），Intel CPU/GPU/NPU 三个性能敏感插件内部确实大量绕开插件接口直接调内部 API；换来加新硬件后端**不需要碰 core 任何一行代码**。
- **可迁移性**：**高**。

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | OpenVINO | TensorRT | ONNX Runtime | ncnn | llama.cpp |
|------|---------|--------|--------------|------|-----------|
| Star | 11,912 | 13,476 | ~22,300（主仓已下线） | 24,084 | ~136,000 |
| 硬件覆盖 | CPU(x86/ARM)+iGPU+独显+**NPU** | 仅 NVIDIA GPU | CPU/CUDA/ROCm/… EP 制 | 移动 ARM 为主 | CPU 为主，CUDA/Metal/Vulkan 为社区分支 |
| 动态形状 | CPU 完全 / GPU 部分 / NPU 靠 NPUW 拆分 | 需为每 shape 多 engine | 运行时解释执行，原生支持 | 有限 | 原生支持 |
| LLM 能力 | **NPUW + GenAI 全栈** | TensorRT-LLM | 弱 | 几乎无 | 极强（量化矩阵最全） |
| IR 形态 | XML（可 diff）+ BIN，opset 版本化 | 私有二进制 | ONNX 图 | 自定义 layer/param | GGUF |
| 生产部署 | blob 导入导出、异构调度、auto_batch、model_server | 需自建服务层 | 轻量 | 轻量 | server 模式简洁 |
| 许可 | Apache-2.0 | NVIDIA 专有 | MIT | BSD | MIT |
| 机器人/VLA | **有**（Physical AI，2026.3 起） | 无 | 无 | 无 | 无 |

### 差异化护城河

1. **NPUW 是结构性护城河，不是功能护城河**。llama.cpp、TensorRT、ORT 在固定形状 NPU 上都做不了 LLM——要么不支持 NPU，要么不支持动态形状。Intel 自己掌握 NPU 硬件设计 + npu_compiler + NPUW 三件套，**这是别人复制不了的**。
2. **Intel 全线硬件 + IR + 插件契约的组合**。CPU（AVX-512/AMX/oneDNN）、iGPU（OpenCL/Vulkan）、NPU 三条产品线共享同一 IR——「一次编写随处部署」是真实实现，不是口号。
3. **Apache-2.0 的 genuinely open + Intel 官方背书**。企业采购需要的「可商用、可审计、可修改、有厂商支持」四件事，OpenVINO 是少数全部满足的。
4. **Physical AI / 机器人运行时开辟的新战场**——连 llama.cpp 都还没入场。
5. **Agent 化造算子是工程效率护城河**：op-parity 债务是所有竞品的共同痛点，谁先还清谁就有更多模型可跑。

### 竞争风险

1. **GPU 性能 7 倍差距是最大风险**。如果 LLM 部署的主战场从 NPU/AI PC 转向数据中心 GPU，OpenVINO 会从「Intel 硬件的默认选择」变成「边缘设备的专用工具」。
2. **ONNX Runtime 主仓从 GitHub 下线**（2026-11-17，本报告已独立复核：`gh api` 返回 404、HTTP 404、微软组织仓库列表与搜索中均已消失；同期至少 7 个微软仓库一同下线；PyPI 1.32.0、NuGet/Maven 与文档站仍可访问）。短期对 OpenVINO 构成利好——ORT 的 OpenVINO EP 集成路径面临失效，而 OpenVINO 本体由 Intel 官方维护不受影响。**但信号不好**：说明大厂可能收缩推理运行时投入，整个品类的市场预期都可能下调。
3. **llama.cpp 的生态虹吸**。本地 LLM 圈的默认选择是 llama.cpp，OpenVINO 的 GGUF 前端是「防守性跟进」而非引领——43+ op 覆盖度 vs llama.cpp 的完整 ggml op 集有差距。
4. **Agent 流水线的不稳定性**。issue #38425 里反复 `agent_failure`；`agents-prototype/` 只有 7 次提交、名字里就写着 prototype、还明确标注 NPU agent non-functional。如果不能稳定产生高质量 PR，它就只是「看起来在用 AI」。
5. **NPUW 的代码复杂度债**。两个 2,000+ 行的核心文件 + 30+ 个 `npuw_transformations/` + 基于输入名的启发式判断，每接一个新模型家族都在加特例。Phase 2 的「Fix:Feature ≈ 1.9:1」健康度可能正被侵蚀。
6. **单一厂商绑定**。OpenVINO 的路线节奏跟随 Intel 硬件节奏，Intel AI PC 出货不及预期时，OpenVINO 的最大差异化场景（NPU）会同步缩水。

### 生态定位

> **OpenVINO 是「Intel 硬件的官方推理操作系统」，不是「最好的推理引擎」。**

它的竞争维度不是「谁的单卡吞吐最高」，而是「谁能让一个团队在 Intel 的异构机队上，用一套代码、一套 IR、一套部署流程，管好从 CV 到 LLM 到机器人策略的所有模型」。TensorRT 在「单卡 NVIDIA 吞吐」这一维上赢；llama.cpp 在「单机跑 LLM」这一维上赢；ONNX Runtime 在「快速原型」这一维上赢。OpenVINO 赢在**跨代际、跨硬件、跨模型类型、跨部署形态的工业治理**。

2026.3 起它把自己包装成四合一（Base + GenAI + Physical AI + Model Server），这个叙事把 OpenVINO 从「一个 runtime」升级为「Intel AI 的入口层」——不再和 TensorRT 比推理速度，而是成为 Intel 侧 AI 部署的默认控制面。

**生态上游**：被 🤗 Optimum Intel、ONNX Runtime 的 OpenVINO EP、vLLM 的 OpenVINO backend、LangChain/LlamaIndex/LLMWare、PyTorch `torch.compile()`、ExecuTorch、Keras 3、KServe/Triton/OVMS 集成。

## 套利机会分析

- **信息差**：**最明确的一处**。11,912 star 这个数字仍停留在「CV 时代老牌推理引擎」的公众认知上，但项目已转型为「Intel NPU 上的 LLM 端侧运行时」+「机器人 VLA 栈」。同赛道的 llama.cpp 已有约 136K star。本报告用本仓库自建的 Trending 归档独立验证了一个信号：**在 14 个月、11,502 条记录、1,440 个不同仓库的数据里，OpenVINO 是 2026-11-18 才首次上榜**，且 48 小时 +452 star、排名 #14→#8→#8、月度榜仍是 #97——它才刚刚回到牌桌。「新叙事 / 旧 star 锚」的认知差是真实存在的。
- **技术借鉴**：IR + pass 管线的设计（不可变 IR、opset 版本化注册表、拓扑序级联重写、版本区间翻译表、markup→transformation 两阶段量化）是任何「多前端多后端」系统都能直接抄的；`.github/agents-prototype/` 的 agent 编排约定（状态文件即记忆、置信度路由、集中 PR 所有权、双闸门、迭代熔断、诚实 non-blocking 标注）是任何多 agent 协作系统都能抄的。
- **生态位**：**「Intel NPU 上跑 LLM 且能进企业采购清单」这个格子，目前只有 OpenVINO 占着**。llama.cpp 没有 NPU、没有工业部署形态；TensorRT 没有非 NVIDIA 硬件；ORT 没有 NPU 上跑 LLM 的能力，而且它的主仓刚刚从 GitHub 消失。
- **趋势判断**：符合趋势。NPU 从「可选加速器」变 AI PC 必选部件是硬件侧的既定趋势；LLM 端侧化让 NPU 从「只能跑 CV」变成「能跑生成式模型」；2026.4 已落地 speculative decoding → NPU、MoE 双路径、chunked prefill、prefix/sliding-window KV cache、LoRA、Eagle3、GGUF 前端；下半年新增跨 AI PC 集群的分布式 LLM 推理（论文 arXiv 2608.19147 把 70B 分片到 4 台 Lunar Lake，双节点 1.79× 吞吐）。**后发优势明显**：OpenVINO 是在「LLM 已成为主流负载」这个前提下重新设计 NPU 路径的，而 TensorRT/ORT 的 NPU 支持都是从 CV 时代继承来的。

## 风险与不足

1. **GPU 性能不是它的战场**。TensorRT 7 倍的 GPU 优势意味着，如果你的部署目标是数据中心 GPU，OpenVINO 没有理由被选中。把 OpenVINO 当「通用 TensorRT 替代品」是最常见的误判。
2. **NPUW 的复杂度债正在累积**。2,364 + 2,278 行的核心文件、30+ 个专用变换 pass、基于输入名的启发式判断（Deepstack、PLE、Eagle3、Gemma3 token_type_ids、Qwen3-VL position_ids 各有特例）。每接一个新模型家族都在加 if-else，这是典型的长尾技术债。
3. **agent 流水线仍处 prototype 阶段**。目录名就叫 `agents-prototype`，只有 7 次提交（集中在 2026-05 ~ 2026-10），NPU agent 被明确标注 non-functional，CI doctor 自己在 issue 里反复报 `agent_failure`。**它现在更像一个正确方向的架构示范，而不是一条已经在生产跑通的流水线。**
4. **编译期内存开销是长期痛点**。IR 变换的 clone 语义导致编译大模型吃内存，issue #13601 开了很多年仍反复出现。
5. **编译期心智负担**。ONNX Runtime 的 `InferenceSession` 五行代码就能跑；OpenVINO 要理解 `read_model → compile_model → infer` 的编译期概念、`AnyMap` 配置、以及「编译产物与源模型的版本对应」这套模型资产管理理念。从 ORT 迁移过来的人常低估这一层。
6. **上手门槛与分发体积**。Python wheel 数百 MB，ncnn 只有几 MB；移动端和轻量边缘场景不是它的目标。
7. **无根级 CHANGELOG**。changelog 只存在于 `cmake/developer_package/packaging/{debian,rpm}/`，release notes 散在 `docs/articles_en/about-openvino/release-notes-openvino/`。对 8 年、65 个 Release 的项目来说这是文档治理上的明显缺口。
8. **单一厂商绑定的周期性风险**。它的价值主张高度依赖 Intel NPU 的出货量。Intel AI PC 换机周期一旦放缓，OpenVINO 最大的差异化场景会同步缩水。
9. **依赖 ORT 生态的悬空风险**。ONNX Runtime 主仓消失后，作为其 OpenVINO EP 的上游被依赖方已断链——短期利好 OpenVINO，但也意味着「依赖链断裂」这个先例已经发生。

## 行动建议

- **如果你要用它**：
  - **选它**：部署目标包含 **Intel NPU**（AI PC / 边缘设备 / 机器人）；需要 CPU+iGPU+NPU 混合调度；需要模型资产化（blob 可导入导出、可缓存、可版本化、可进制品库）；企业采购需要 Apache-2.0 无 copyleft；做机器人 VLA。
  - **别选它**：只有 NVIDIA GPU（用 TensorRT / TensorRT-LLM）；只是要快速验证一个 ONNX 模型（用 ONNX Runtime，`ov.convert_model()` 也行但没必要绕）；单机跑 7B 追求极致轻量（用 llama.cpp——它的量化矩阵和内存占用都赢）；手机 App 内嵌一个 CV 模型（用 ncnn）。
  - **上手顺序**：先 `core.compile_model(model, "AUTO")` 拿到默认体验 → 再按需开 LPT 量化 → 部署前把 `compile_model` 的产物缓存成 blob，别在每次启动时重编译（issue #13601 的内存问题主要来自这里）→ 涉及 LLM 就直接上 `openvino.genai` 而不要自己拼 `ov::LLMPipeline`。
  - **迁移成本**：从 ONNX Runtime 迁入**低**（`core.read_model(onnx_path)` 即可，主要成本是重新校准精度）；从 TensorRT 迁入**很高**（要重写 TensorRT-LLM pipeline、自定义 plugin 换 `IPlugin`、精度配置全部重做）。

- **如果你要学它**：
  - **必读**：`src/core/include/openvino/core/node.hpp` + `src/core/src/pass/graph_rewrite.cpp`（IR 不可变 + 拓扑序级联重写，这是全项目最值得抄的部分）
  - **必读**：`src/plugins/intel_npu/src/plugin/npuw/llm_kvcache_strategy.hpp`（生命周期钩子契约 + 两阶段失败语义，写 C++ 状态机必看）
  - **必读**：`src/plugins/intel_npu/src/plugin/npuw/llm_compiled_model.cpp:739` 的 `create_generate_model_variants`（变体阶梯的实现）
  - **必读**：`.github/agents-prototype/enable-operator.agent.md`（647 行，一份写得极好的 agent 编排规格书）
  - **参考**：`src/plugins/template/`（官方插件模板——要加新硬件后端就照着抄）、`src/common/snippets/docs/snippets_design_guide.md`（kernel codegen 设计）、`src/plugins/hetero/README.md`（异构切分算法的完整推演）
  - **可直接抄的四件套**：`agents/*.agent.md` + `skills/<name>/stepN-*.md` + `pipeline_state.json` + 确定性 fallback 脚本；配合「置信度路由」「子 agent 不许开 PR」「迭代上限 + 有进展就不熔断」「双闸门验证」「诚实标注 non-blocking」五条纪律。

- **如果你要 fork 它**：
  - **最现实的 fork 动机是加一个硬件后端**，那就用 `src/plugins/template/`，不要动 core。
  - **想做非 Intel 硬件的 LLM 运行时**：NPUW 的核心思想（动态形状 → 静态子图 + 运行时状态交接 + 容量阶梯变体）值得移植，但要重写的是那套按输入名猜语义的适配层。
  - **想清理 NPUW 复杂度债**：把「输入名启发式」换成显式的模型能力声明（每个模型家族注册自己的输入语义与布局转换），这是最有价值也最难的一块重构。
  - **想让 agent 流水线真的能用**：优先补 NPU agent（它被明确标为 non-functional），并把 CI doctor 的 `agent_failure` 率压下去；同时把 `agents-prototype` 改名——叫 prototype 的东西很难让人认真对待。
  - **注意 license**：Apache-2.0 保留声明，Intel 商标（OpenVINO™、Intel 徽标）不可复用。

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | https://deepwiki.com/openvinotoolkit/openvino （已收录，含 NPUW Compiled Model and Partitioning 分册） |
| Zread.ai | https://zread.ai/openvinotoolkit/openvino （已收录） |
| 关联论文 | [Pre-Compiled Pipeline Shards for Distributed LLM Inference on Intel AI PC Fleets](https://arxiv.org/abs/2608.19147)（70B 分片到 4 台 Lunar Lake，双节点 1.79× 吞吐）<br>[NNCF: Neural Network Compression Framework](https://arxiv.org/abs/2002.08679)<br>[RISC-V CPUs within OpenVINO](https://link.springer.com/10.1007/978-3-031-80457-1_6) |
| 在线 Demo | 无官方托管浏览器 playground。替代路径：[Live Object Detection](https://docs.openvino.ai/2024/notebooks/object-detection-with-output.html) · [Live Human Pose Estimation](https://docs.openvino.ai/2024/notebooks/pose-estimation-with-output.html) · [Intel Model Hub](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/model-hub.html) |
| 官方文档 | https://docs.openvino.ai （2026.3 起为 Base + GenAI + Physical AI + Model Server 四合一工具箱） |

---

*分析数据采集于 2026-11-21；代码统计基于 master 分支 HEAD `6ed280ed68`。中间产物见 `tmp/repo-facts-openvino.json`、`tmp/openvino-phase-{1,2,3}-analysis.md`。*
