# GitHub 推荐：947 组配对实验：NVIDIA 证明静态扫描测不准 Skill

> GitHub: https://github.com/nvidia/skillevaluator

## 一句话总结

NVIDIA 官方的 Agent Skill 评测器，用「三层门禁 + 配对 A/B 差分」把「这个 skill 到底有没有用」从一句断言变成**一个可复算的数字（Skill Lift）**——并用 947 组配对实验证明，结构扫描和 LLM judge 打分与真实表现几乎不相关（**Spearman ρ = 0.14**）。

## 值得关注的理由

1. **它给出了一个反直觉的硬结论**：论文《Evaluating Skills, Not Just Agents》（arXiv:2608.20614） 在 145 个真实 skill、947 个配对 case、4 个 harness 上测出，**静态结构扫描与 LLM judge 和真实表现的相关系数只有 0.14**——这等于否定了「靠 lint 规则和 judge 打分就能判断 skill 好坏」这条主流路线，也正是本项目存在的理由。
2. **「跑不动 ≠ 通过」的三态证据契约，是本项目最值得抄的工程约定**：外部扫描器缺失、超时、崩溃、输出畸形时，状态记为独立的 `INCOMPLETE` 而非 `PASSED`，并强制非零退出码——这条链路从 `mark_scan_incomplete()` 一路传播到 CI 门禁退出码，任何扫描型工具都该照抄。
3. **方法论有 arXiv 论文背书，代码作者就是论文作者**：Christopher Kevin + Narendran Raghavan 双核占 81% 实质提交，另有 NVIDIA 研究院的 Jean-Francois Puget、Rama Akkiraju 等署名——这是研究院级正式项目，不是市场部外包。
4. **生态位置尴尬得值得注意**：同厂的 NVIDIA/SkillSpector 有 27,042★，本项目只有 4,242★；一篇 2026 年 7 月讨论「agent skill 评估」品类的英文技术博客**完全没提到它**——方法论领先，触达落后。

## 项目展示

![SkillEvaluator 字标](https://raw.githubusercontent.com/NVIDIA/SkillEvaluator/647bd47062f9a9b07c3bf5c478e5271c0e0d8913/docs/assets/skillevaluator-wordmark.svg)

SkillEvaluator 字标 — NVIDIA 官方的 Agent Skill 评测工具。

![三层流水线](https://raw.githubusercontent.com/NVIDIA/SkillEvaluator/647bd47062f9a9b07c3bf5c478e5271c0e0d8913/docs/assets/three-tier-overview.svg)

三层流水线概览 — 静态校验、语义去重、live evaluation 三层递进，产出报告。这是理解整个项目架构的关键一张图。

![CLI 使用](https://raw.githubusercontent.com/NVIDIA/SkillEvaluator/647bd47062f9a9b07c3bf5c478e5271c0e0d8913/docs/assets/get-started-cli.svg)

终端直接运行 CLI — Tier1 零 key、零 Docker、零 GPU 即可跑完并给出 0-100 分。

![CI 接入](https://raw.githubusercontent.com/NVIDIA/SkillEvaluator/647bd47062f9a9b07c3bf5c478e5271c0e0d8913/docs/assets/get-started-ci.svg)

通过 CI 接入仓库 — `skillevaluator ci init` 直接生成 setup PR，把评测做成合并门禁。

![Agent 运行时接入](https://raw.githubusercontent.com/NVIDIA/SkillEvaluator/647bd47062f9a9b07c3bf5c478e5271c0e0d8913/docs/assets/get-started-agent.svg)

接入 agent 运行时 — 工具本身也能作为 skill 装进 Claude Code / Codex，让 agent 自我评测。

> 视频：[Ask the Experts: Evaluating Agent Skills（NVIDIA 官方直播）](https://www.youtube.com/watch?v=4rI0zATFxYI)

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/nvidia/skillevaluator |
| Star / Fork | 4,242 / 550（Watcher 仅 8；open issues 20 / open PR 46） |
| 代码行数 | 52.8 万行 Python 92.6%（**其中测试 30.3 万行占 57%，核心实现约 20 万行 / 371 个文件**） |
| 项目年龄 | 3.9 个月（仓库创建 2026-06-24，首提交 2026-07-26） |
| 开发阶段 | 密集开发（705 commit，**近 30 天 506 个占 72%**，11 月单月 462 个；1.0.0 与 1.0.1 同日发布） |
| 贡献模式 | NVIDIA 官方组织仓库 + 双核主导（Christopher Kevin 42.5% + Narendran Raghavan 38.9% = 81%，48 人中仅约 12 人有实质提交） |
| 热度定位 | 中等热度（细分赛道头部，但远低于同厂 SkillSpector 的 27,042★） |
| 质量评级 | 代码[优秀] 文档[优秀] 测试[充分] |
| 许可证 | Apache-2.0 |
| 版本发布 | v1.0.1（13 个 release，16 个 tag，2026-11-17） |

> ⚠️ 两个数据修正：① 10 月做过 squash 历史重写，旧 tag `archive/main-before-oct-squash` 指向 **900 commits**，当前 HEAD 只有 705，真实工作量被低估；② `gh stargazers` API 返回 403，**star 增长曲线无法采样**，本报告不对增长形态做任何判断。

## 作者视角：为什么存在这个项目

### 创始人/作者背景

这不是个人项目，而是 **NVIDIA Corporation 组织仓库**，背后是研究院级的双核团队：Christopher Kevin（arXiv 论文第一作者）与 Narendran Raghavan。提交记录里的同名 695 / 571 commits 与论文署名一一对应，另有 Jean-Francois Puget、Rama Akkiraju、Subodh Prabhu、Wei Luo 等 NVIDIA 研究员参与。仓库配有完整的 `GOVERNANCE.md` / `SUPPORT.md` / `SECURITY.md` / `CITATION.cff`。

### 问题判断

**推断成立**：SkillEvaluator 是 NVIDIA skills 战略的第三步。

- 第一步：`NVIDIA/skills`（4,096★）—— skill 的目录与分发
- 第二步：`NVIDIA/SkillSpector`（27,042★）—— skill 的安全扫描
- 第三步：`NVIDIA/skillevaluator`（4,242★）—— skill 的**质量与效果度量**

前两步产出的 skill 目录此前无法回答「装了到底有没有用」。通用 eval 框架（promptfoo / DeepEval / Ragas / LangSmith / Braintrust）**完全 skill-unaware**——不理解 skill 目录结构、不做 skill 激活验证、不做 harness 加载检查；SkillSpector 只答「危不危险」；harbor 有沙箱和轨迹但 **skill 不是一等公民**，没有配对 A/B 协议、不产 Lift。

时机也讲得通：Agent Skill 在 2026 年才形成真正的生态（ClawHub / Skills.sh / Hermes Hub 渠道铺开），「skill 质量」才第一次成为需要被度量的对象。

### 解法哲学

1. **逐级从「便宜确定性」走向「真实行为」**：Tier1 静态检查（零 key、零 Docker、零 GPU）→ Tier2 语义去重（需 embedding）→ Tier3 真实 A/B（需 provider + Docker）。每层独立可选，各自可 gating。
2. **「跑不动 ≠ 通过」**——本项目最刚性的工程约定。`ValidationResult.mark_scan_incomplete()`（`src/skillevaluator/models/result.py:701`）把「扫描器缺失/超时/崩溃/输出畸形」记入 `metadata['incomplete_scans']` 并置 `passed=False`，与真实 finding 走完全不同的状态通道。
3. **开发者优先**：`EVAL.md` 可覆盖 LLM judge；`grader-validation` 让用户能用独立标注反向验证内置 grader。
4. **结果是均值而非通过概率**：`pass@k` 另设，headline 是配对 lift 的均值。
5. **明确不做什么**：不做 skill 市场与分发（NVIDIA/skills 做）、不做通用 eval 框架、不做 IDE 集成——落地形态只有三个：CLI、可复用 CI 模板、可装进 Claude Code/Codex 的 skill 本身。
6. **不追通用 LLM 库**：litellm 只在 `llm` extra 里做 provider 统一；Tier3 沙箱直接钉死 `harbor[gke]==0.25.0`，不自造沙箱。

### 战略图景

**基础设施定位，但包装成了 CI-as-a-product**：22 个 workflow、`ci/bundles/{version}/`（含 `SHA256SUMS.txt`、`verification-receipt.json`、可下载 zip）、`ci/templates/`、`skillevaluator ci init` 直接开 setup PR、OCI 镜像发布 + stable 通道晋升 + `ci/verify_provenance.py` 用 GitHub OIDC JWKS 验签执行回执。

**开源策略：genuinely open**。Apache-2.0、13 个 release、官方明写 `Support level: Experimental. Community-supported, best-effort, with no SLA or NVIDIA enterprise support entitlement`。无付费墙、无企业版、无 hosted SaaS 收费路径。商业意图更像是**为 NVIDIA 的 agent 产品线建立标准与生态锁定**（README 点名「NVIDIA product teams」是目标用户之一）。

## 核心价值提炼

### 创新之处

1. **「跑不动 ≠ 通过」的三态证据契约**（新颖度 3/5 | 实用性 5/5 | 可迁移性 5/5）
   `Status` 枚举 6 态（`src/skillevaluator/reporting/run_status.py:34`），合并序为 FAILED > INCOMPLETE > NEUTRAL > PASSED > SKIPPED；`resolve_run_status()`（同文件 `:149`）的 headline 规则是「全部 failing 都是 INCOMPLETE → headline = INCOMPLETE，否则 FAILED」；`cli.py:3141` 的 `gate_failed = resolve_run_status(...).headline != Status.PASSED` 决定退出码。**「部分证据」永远不能塌缩成「通过」**——这是任何调用外部工具的评测/扫描/门禁系统都该抄的设计。

2. **同 case 对齐的差分测量 + 排除原因记账**（新颖度 4/5 | 实用性 5/5 | 可迁移性 5/5）
   `src/skillevaluator/tier3/harbor/lift_basis.py::pair_metric_scores` 按 case id 对齐两臂，每个 metric 只保留两臂都评分的 case；6 类排除原因分别记账（`not_applicable` / `no_value` / `no_shared_case` / `load_failed` / `judge_mixed` / `unidentified_case`），并区分 metric 级与 case 级；`basis` 块写进 JSON 报告供用户自行复算。这是 issue #61「数字毫无意义」的正面回答。

3. **Hesterberg expanded percentile bootstrap：小样本自纠偏**（新颖度 4/5 | 实用性 4/5 | 可迁移性 4/5）
   5–10 个 case 的普通 percentile bootstrap 覆盖度只有约 82%，会给出过窄的假区间。`stats.py:553 expanded_tail` 用 `Φ(-√(n/(n-1))·t_{α/2,n-1})` 替换 `α/2`；`_incomplete_beta_fraction`（modified Lentz 连分式）自实现不完全 Beta 导 t 分布，二分求分位点；固定 seed 保证可复现；`_effective_resamples` 保证每个界至少由固定数量的重采样均值支撑。零 scipy 依赖（base install 不带科学计算库）。

4. **声明式 harness 规则档案 + AST 白名单表达式求值**（新颖度 4/5 | 实用性 5/5 | 可迁移性 5/5）
   `src/skillevaluator/harness/profiles/*.yaml` 用 `when:` 加一段表达式描述 Claude Code / Codex / Copilot CLI / OpenCode / Hermes / OpenClaw 六个 loader 的行为差异；`overlay.py:801 _Rule.evaluate` 用 `ast.parse` 后**白名单校验节点类型**，只允许 BoolOp / Compare / Name / Constant / Attribute / List / Tuple，禁止 Call，从而在**不使用 `eval`** 的前提下求值表达式。兼顾了可读性与不执行任意代码。

5. **把污点分析从源代码迁移到 agent 运行时轨迹**（新颖度 5/5 | 实用性 4/5 | 可迁移性 3/5）
   Tier3 要判断 agent 实际执行了什么危险操作，但 agent 的行为是「跑出来的 shell 命令」，没有 AST 可分析。`eval_core/checks.py` 自建了完整 shell 语义层——词法（`_rm_shell_words` / `_compound_keywords` / `_shell_text_regions`）、apply_patch 补丁解析、curl/httpie/xh 网络客户端语义、rm 的 heredoc/xargs/命令替换/argv 数组边界——加上约 1,300 行独立实现的**凭据 span 级脱敏器**（`_SpanIndex` / `_MaskedSpans` / `_AssignmentValues`），对 agent **实际执行过的**命令做 secret→网络外传的污点传播。这是 semgrep/bandit 污点分析思路向 agent 运行时的一次原创迁移。

6. **loose-parts 消融臂：分离「内容价值」与「打包机制价值」**（新颖度 5/5 | 实用性 3/5 | 可迁移性 4/5）
   `src/skillevaluator/tier3/loose_parts.py` 构造第三臂：同样的 skills / rules / MCP servers / subagents / commands / hooks，但**以 Claude Code 能独立加载的方式摆放**（无插件外壳），用内容哈希证明两臂能力等价。Lift 被拆成四级阶梯，Integration lift = 完整插件臂 − loose parts 臂。回答了「插件比裸 skill 好，好多少，是内容好还是机制好」。

7. **grader 资格认证：先验证尺子，再用尺子**（新颖度 3/5 | 实用性 5/5 | 可迁移性 5/5）
   LLM judge 本身可能不可靠——用不可靠的尺子量 skill。用**独立人工标注**的 suite 跑真实发布的 verifier，测 `false_pass_rate` / `false_fail_rate` / `unjudgeable_rate`，输出 qualification policy 门禁；`grader_policy.py` 拒绝重复键（`object_pairs_hook=unique_fields`）以防 last-wins 造成策略歧义。

8. **Requirement Ledger：需求→代码→文档→测试→证据逐条对账**（新颖度 4/5 | 实用性 4/5 | 可迁移性 5/5）
   `docs/superpowers/specs/2026-11-16-requirement-ledger-*.md` 每条需求一行表格，含具体 commit hash、live run 观察，以及诚实的 `Partly met` / `Blocked: needs human reviewers; model-made labels do not count` 判定。

9. **「每个数字都可复算」的文档契约**（新颖度 3/5 | 实用性 5/5 | 可迁移性 5/5）
   `docs/metrics-reference.mdx` 给每个指标写明公式（带源码位置链接）、值域、单位、产生者、如何从 JSON 复算，并明写「如果公式与代码不一致，以代码为准，本页即 bug」。

### 可复用的模式与技巧

1. **三态证据契约（PASSED / FAILED / INCOMPLETE）**：外部工具未产出可信结果时，状态必须独立于通过与失败，且必须导致非零退出码 —— 适用场景：SAST、依赖审计、secret 扫描、覆盖率工具、agent 评测
2. **受限 AST 表达式求值的规则引擎**：YAML 声明规则 + `ast.parse` 白名单校验 + 自写求值器，替代 `eval` 和硬编码 —— 适用场景：policy-as-code、多版本兼容矩阵
3. **配对差分的同 case 对齐 + 排除原因记账**：把「两臂平均相减」升级为「同 case 集合上的配对均值」，并机器可读地解释每个排除 —— 适用场景：任何 A/B 对照实验
4. **小样本统计自纠偏**：expanded percentile bootstrap + precision 三档分级 + 固定 seed —— 适用场景：agent/LLM 评测、n<20 的对照实验
5. **证据优先级契约**：确认失败 > 不完整证据 > 通过；advisory 结果保留自身状态但不改变门禁 —— 适用场景：多检查聚合
6. **「跑不动」的错误文案分流**：区分「没配 provider」「配了 provider 但没 key」「`--no-llm` 显式禁用」，三种原因三种文案 —— 适用场景：依赖外部服务的 CLI
7. **事务性 no-follow staging**：描述符相对遍历 + `O_NOFOLLOW` + 前后身份校验 + 私有暂存 + 最终暴露 —— 适用场景：把用户目录送进容器/沙箱
8. **声明式后端插件（entry-point）**：`import_path` 字符串 + 延迟 import + 严格参数校验 + 总开关 —— 适用场景：多运行时/多云后端
9. **消融臂（ablation arm）**：构造能力等价但剥离某一机制的第三臂 —— 适用场景：框架增益归因
10. **执行回执签名验证**：OIDC JWKS 验签 + 镜像 digest pin + 匿名拉取验证 —— 适用场景：CI 资产分发、供应链安全

### 关键设计决策

1. **决策：三层递进，每层独立可选**

    - 问题：评测工具常把「贵且慢」当默认门槛，导致作者根本跑不起来
    - 方案：Tier1 零 key 零 Docker 直接给 0-100 分；每层结果带 `metadata['gating'] = {tier, blocking}`，是否进最终门禁由 flag 决定（`cli.py:3039` `block_on_dedup_effective`、`cli.py:3064` `block_on_agent_eval_effective`）
    - Trade-off：用户可能只跑 Tier1 就以为通过了 —— 用 `Publication eligibility: Incomplete` 强制暴露这一点
    - 可迁移性：高（任何「能力分级评测」都适用）

2. **决策：配对差分 + 同 case 对齐 + 排除原因记账**

    - 问题：with-skill 和 baseline 两臂各自平均，覆盖的 case 集合可能不同（某臂缺 case、某 metric 记为 N/A、load evidence 失败）—— 直接相减是错的
    - 方案：见上文创新点 2
    - Trade-off：报告体积增大、排除逻辑复杂（`_CASE_LEVEL_REASONS` 与 metric 级并存）
    - 可迁移性：高 —— 任何 A/B 评测框架都缺这一层

3. **决策：`precision` 三档分级，把「样本量不足」显式编码进结果**

    - 问题：5 个 case 的 lift 数值看着漂亮，但统计上不可用
    - 方案：`lift_precision(n_cases, ci_low, ci_high)` → `LIFT_CI_MIN_PAIRED_CASES` / `LIFT_CI_ADEQUATE_MIN_CASES=10` / `LIFT_CI_LOW_PRECISION_WIDTH`；报告里 `ci_includes_zero` 与 `precision` 一起给
    - Trade-off：大量小规模跑会显示 low/insufficient，可能「劝退」用户
    - 可迁移性：极高

4. **决策：沙箱后端做成 entry-point 插件式**

    - 问题：Docker / local / native / GKE / Kata / ACK / 各类云沙箱持续增加，硬编码会僵化
    - 方案：`src/skillevaluator/tier3_environments.py:267` 定义 frozen dataclass `EnvironmentBackendSpec`（`import_path` / `environment_kwargs` / `host_env_vars` / `agent_import_paths` / `prerequisites`……），通过 `skillevaluator.env_modes` entry-point group 注册，后端模块**只在选中时才 import**；另有 `DISABLE_CUSTOM_BACKENDS` 总开关与 `EnvironmentBackendError` 校验
    - Trade-off：entry-point 机制在 editable install / 打包场景下易出问题；参数校验逻辑冗长
    - 可迁移性：高

5. **决策：不可信输入的事务性 staging**

    - 问题：Tier3 要把作者写的 skill 目录复制进沙箱 —— 攻击者控制的路径可能含 symlink / hardlink / 特殊文件
    - 方案：POSIX 路径用描述符相对操作 + `O_NOFOLLOW`；其他平台用 lstat/fstat 前后身份校验（`stat_is_link_or_reparse`）；三段顺序稳定性检测捕获扫描期间的偶发变更；私有目录暂存直到最终暴露步骤；文件头明写「不提供对同 UID 并发变更的安全保证」
    - Trade-off：大量平台分支代码、性能开销
    - 可迁移性：中高（任何「把用户目录送进容器」的工具都需要）

6. **决策：`harbor[gke]==0.25.0` 精确钉死**

    - 问题：Harbor 是活跃开发中的框架，Tier3 的沙箱契约、ATIF 轨迹格式、agent adapter 都依赖它
    - 方案：精确版本 + `pyproject.toml` 注释标注 CVE 修复下限（`mcp>=1.28.1,<2` 修 CVE-2026-59950/52870/52869；`pyjwt[crypto]>=2.13.0` 修 CVE-2026-48522~48526；`oauthlib>=4.0.0` 修 GHSA-hj66-6f7g-4r5v / GHSA-xpv3-w29h-x7cv）
    - Trade-off：升级滞后；但对 CI 门禁产品而言，行为可复现比新特性更重要
    - 可迁移性：中

7. **决策：CI 资产带签名与摘要**

    - 问题：用户从 GitHub 抄 workflow YAML 到自己仓库，本身就是供应链攻击面
    - 方案：`ci/bundles/1.0.1/` 含 `SHA256SUMS.txt`、`verification-receipt.json`（镜像 sha256、source revision、官方构建 run URL、匿名拉取验证结果、smoke case 的 summary 哈希）；workflow 引用 pinned commit SHA + pinned 镜像 digest；`ci/verify_provenance.py` 验签执行回执
    - Trade-off：复杂度高；**且 issue #603 指出其 docs 里的 CI recipe 比它自己的 workflow 更松（空摘要也能过、action 不 pin、gitleaks 下载不校验）**——这条线尚未完工
    - 可迁移性：中高

## 竞品格局与定位

### 竞品对比矩阵

Stars 为 2026-11-20 gh api 实测。

| 维度 | SkillEvaluator | microsoft/waza | agent-skills-eval | SkillSpector | harbor | 通用 eval 框架 |
|------|---------|--------|--------|--------|--------|--------|
| Star 数 | 4,242 | 1,516 | 819 | 27,042 | 7,301 | 19k–27k |
| 核心机制 | 三层门禁 + 配对 A/B 差分 | YAML benchmark + grader | schema 校验 + baseline 差分 | AST/taint/YARA 安全扫描 | 沙箱 + ATIF 轨迹 | 断言库 + RAG 度量 |
| 产出量化收益指标 | **是**（Skill Lift + CI + precision） | 否 | 否 | 否 | 否 | 否（测回答质量） |
| 理解 skill 目录结构 | 是 | 部分 | 是（规范层） | 是 | **否** | **否** |
| harness 兼容性检查 | 是（6 个 harness 档案） | 否 | 否 | 否 | 30+ agent 适配器 | 否 |
| 安全扫描 | 内嵌 SkillSpector | 无 | 无 | **专精** | 否 | 极少 |
| 方法论背书 | arXiv 2608.20614 | 无 | 无 | SkillTrustBench 横评 | Terminal-Bench 事实标准 | 社区生态 |
| 语言/部署 | Python 3.12–3.14 | Go 单二进制 | TypeScript | Python | Python | 各异 |

### 差异化护城河

- **技术护城河（中等）**：配对差分 + 统计严谨性 + harness 规则引擎 + agent 运行时污点分析——都不易抄，但也都可被针对性实现
- **生态护城河（弱，最大短板）**：27,042★ 的同厂 SkillSpector、19k+★ 的通用框架、7,301★ 的 harbor 知名度都远高于它；一篇讨论该品类的英文技术博客完全没提它，说明它**尚未进入英文技术博客圈的主流视野**
- **信任护城河（强且在增长）**：NVIDIA 官方组织 + Apache-2.0 + arXiv 论文 + 论文作者即代码作者（双核 81%）+ 23 个 release + 22 个 CI workflow + 签名发布资产 + 「Experimental 但明说不给 SLA」的诚实。**信任资产是它最硬的护城河，且不是靠 star 数衡量的**

### 竞争风险

1. **最可能被替代者：SkillSpector 的演进版**——同厂、同团队、6.4 倍星数、已有 AST/taint/YARA 能力。若 NVIDIA 把「有没有用」的度量能力塞进 SkillSpector，本项目将被降格为它的评测前端
2. **次可能：harbor 社区把 skill 提升为一等公民**（加 skill 身份 + 配对协议）——一旦 harbor 原生支持配对 A/B，本项目的差异化收窄为「资产契约 + 静态规则库」
3. **通用框架加一个 skill 插件**（promptfoo / Braintrust）——生态与文档优势会迅速碾压
4. 最小风险：waza（生态规模小一个数量级，且缺静态规则与论文背书）

### 生态定位

**NVIDIA Verified Skills 管线的第三块拼图**，也是 agent skill 领域唯一把「发布门禁」（CI 模板 + setup PR + OCI 镜像 + 签名回执）和「效果度量」（配对 Lift + 论文）合在一起的工具。扮演的是**基础设施 / 标准制定者**角色——不是又一个 eval 框架，而是 skill 供应链的信任层。

## 套利机会分析

- **信息差**：一个 2026 年才出现的新品类（agent skill 评估），方法论定义者却只有 4.2k★，且同厂安全扫描器有 27k★。**关注度与生态位严重不匹配**——技能作者群体需要一个「发布前自检 + 效果量化」的标准工具，而 SkillEvaluator 事实上已经在扮演这个角色，只是没人知道。
- **技术借鉴**：本报告列出的 10 条可复用模式（三态证据契约、受限 AST 规则引擎、配对差分对齐、小样本自纠偏、事务性 staging、消融臂、grader 资格认证）几乎全部可以脱离 NVIDIA 语境直接搬到自己的评测/扫描/门禁系统里。其中「INCOMPLETE 语义」和「受限 AST 规则引擎」两条性价比最高。
- **生态位**：填补了「skill 安全」与「skill 效果」之间的空白。SkillSpector 已占住前者且是红海（SkillTrustBench 已有十来个扫描器横评），后者仍是蓝海（waza 1.5k、agent-skills-eval 0.8k）。这是全文最确定的机会窗口。
- **趋势判断**：仓库 3.9 个月 705 commit（真实 ≥900），3.5 个月从 0 走到 1.0，13 个 release，Docker/PyPI/GitLab 三条发布通道 + stable 晋升机制。Agent Skills 规范（agentskills.io）已落地、ClawHub / Skills.sh / Hermes Hub 渠道铺开——**品类本身在快速起量，工具链需求随之而来**。同厂两个兄弟项目（skills 4.1k、SkillSpector 27k）的存在本身就是需求验证。
- **时机信号**：issue #61（用户问「这数字到底有没有意义」）促成了 `metrics-reference.mdx` 与 `grader-validation.mdx` 两个产品化页面——**质疑本身被当成需求接住了**，这是一个工具从「炫技」走向「可被信任」的典型拐点。

## 风险与不足

1. **官方支持等级是 Experimental，无 SLA**。但实际工程强度远超 Experimental 的通常含义（22 workflow、SHA256SUMS、签名回执、CVE 修复下限、O_NOFOLLOW staging）。真正的生产风险在别处——见下条。
2. **issue #603 仍 open：它教用户装的 CI 门禁配方比自己仓库的 workflow 更松**（空摘要能过、action 不 pin、gitleaks 下载不校验）。一个卖「安全的 CI 门禁」的项目，其文档里的门禁示例是新的供应链入口——这个自洽性裂缝且是安全相关的。
3. **issue #510：`nv_build` 返回 404 导致 LLM 安全验证静默不执行，而报告可能显示通过**。INCOMPLETE 这条边界在多层被反复击穿——设计对了，但实现仍有漏。
4. **issue #461：Tier1 token 计数用 `len(SKILL.md)//4` 估算**，未标注为估计值，且缺 tokenizer 或比率替代。指标本身带未标注的近似。
5. **27.2% 的配对 case 没有正收益**——即**相当一部分 skill 本身是负担**。这个结论对 skill 生态是坏消息，也让「写 skill 就该有收益」的默认假设站不住。
6. **`eval_core/checks.py` 单文件 15,732 行是明确技术债**。需要澄清：这不是「巨型规则表」（9 个 `check_*` 函数只占约 1,900 行），而是一个**自制的完整 shell 语义分析引擎**（词法、heredoc、xargs、命令替换、argv 数组、apply_patch、curl/httpie/xh 语义）加约 1,300 行手写凭据脱敏器。技术债的性质是**能力债**（放弃了复用成熟 shell 解析器的机会）而非组织债。对照 semgrep 用独立 rule DSL 把规则从引擎剥离、让两者独立演进，本项目把规则与引擎混在同一文件。**正确解法是把 shell 语义层拆成独立模块**（`shell_lexer.py` / `shell_semantics.py` / `redaction.py`），让 checks.py 降到约 2,000 行——中等优先级重构，不是推倒重来。
7. **测试占比 57%（1.48:1）的信号两面性**。判断是**重视测试而非臃肿，但已过度倾斜**：测试不是为覆盖率写的，而是为「边界语义」写的——`test_baseline_dimension_applicability.py`、`test_harbor_unscored_grading_policy.py`、`test_skill_metric_applicability.py` 都在钉死「N/A 不是 0」「unscored 不是 0」「负例不算失败」这类极易写错的语义，无法压缩。但比例本身是警报：根因不是测试多，是**语义多**——状态机是复杂度的主要来源。
8. **生态位尴尬是最实际的风险**：方法论领先，触达落后。英文技术博客圈几乎没提它。
9. **小样本统计缺陷**：多 skill 交互指标缺置信区间与显著性检验，小样本易被单次翻转带偏；`--skip-baseline` 可省一半算力但算不出 Lift；local 模式隔离性弱。
10. **静态检查看不到运行时问题**：路由、触发、工具使用等只有 Tier3 才知道，而 Tier3 成本高。10 月做过 squash 历史重写，旧 tag `archive/main-before-oct-squash` 指向 900 commits，当前 HEAD 只有 705——**历史可追溯性有断裂**。

## 行动建议

- **如果你要用它**：

    - **Tier1 可以直接进生产 CI**（配合 `--no-llm` 与自备扫描器）——零 key、零 Docker，秒级出分，INCOMPLETE 语义干净可用
    - **Tier2/Tier3 暂不建议做硬门禁**——官方自己就把 `--block-on-agent-eval` 默认设为 false，且 Tier3 的 FAIL verdict 默认 exit 0
    - 先跑 Tier1 看静态问题，再决定要不要为 Tier3 付 Docker + provider 的成本；`--skip-baseline` 只在你确信不需要 Skill Lift 时用
    - **务必先修 issue #603 和 #510 描述的坑**，再把生成的 CI recipe 引入自有仓库

- **如果你要学它**：

    - `src/skillevaluator/models/result.py`（`mark_scan_incomplete` 附近）——三态证据契约的源头
    - `src/skillevaluator/reporting/run_status.py`——状态合并序与 headline 规则
    - `src/skillevaluator/tier3/harbor/lift_basis.py::pair_metric_scores`——配对差分的正确实现范式
    - `src/skillevaluator/tier3/harbor/stats.py:553` 起的 `expanded_tail` / `_incomplete_beta_fraction`——零依赖的小样本统计
    - `src/skillevaluator/harness/overlay.py:801` 的 `_Rule.evaluate`——受限 AST 求值的完整实现
    - `src/skillevaluator/tier3/loose_parts.py`——消融臂设计
    - `docs/metrics-reference.mdx` 与 `docs/grader-validation.mdx`——「每个数字都可复算」与「先验证尺子」的文档范式
    - 反面样本：`src/skillevaluator/tier3/eval_core/checks.py`——15,732 行单文件如何成为技术债的完整样本

- **如果你要 fork 它**：

    1. **优先重构 `eval_core/checks.py`**：把 shell 语义层拆成 `shell_lexer.py` / `shell_semantics.py` / `redaction.py`，让 `check_*` 规则回归独立 DSL（可参考 semgrep 的 YAML rule 格式）。这是最有价值、风险最低的一次改造
    2. **补多 skill 交互的统计严谨性**：给交互指标补置信区间与显著性检验，而不是只给点估计
    3. **修 Tier1 的 token 估算**：接入真实 tokenizer，或把当前值明确标注为 estimate（对应 issue #461）
    4. **把 tier3 沙箱从 harbor 解耦**：保留 ATIF 兼容，但让 harbor 从硬依赖降为可选后端（当前 `harbor[gke]==0.25.0` 精确钉死，升级滞后是长期成本）
    5. **英文触达是最大的商业性缺口**：方法论已经写进 arXiv 论文了，但社区没看到——这是纯传播问题，不需要动代码

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | 无法判定（`https://deepwiki.com/nvidia/skillevaluator` 返回 429，被 Vercel 安全网关拦截，非「未收录」信号） |
| Zread.ai | 无法判定（`https://zread.ai/nvidia/skillevaluator` 返回 504/403，同样受网关拦截） |
| 关联论文 | [Evaluating Skills, Not Just Agents: Agentic Continuous Evaluation of Skills (ACES)](https://arxiv.org/abs/2608.20614) — Christopher Kevin, Narendran Raghavan, Jean-Francois Puget 等 12 人；mean composite Skill Lift 0.2134（95% CI [0.1967, 0.2301]），947 个配对 case，72.8% 为正；核心负面发现：静态扫描与真实表现 Spearman ρ = 0.14 |
| 官方文档 | https://docs.nvidia.com/skills/skillevaluator/ |
| 在线 Demo | 无浏览器 playground。官方路径 = CLI：`pip install skillevaluator` → `skillevaluator quality-check ./my-skill`（免 key、免 GPU、免 Docker），或用 NVIDIA Build 免费 key 跑全三层；仓库自带参考 skill `src/skillevaluator/tier3/reference_skills/text-analyzer` |
| 兄弟项目 | NVIDIA/skills（4,096★，被评测的技能目录）、NVIDIA/SkillSpector（27,042★，内嵌的 Tier1 安全扫描组件）、harbor-framework/harbor（7,301★，Tier3 沙箱底座） |
