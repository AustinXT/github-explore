# GitHub 推荐：6840 星、35 万行：Claude 交易技能包为何不给你下单

> GitHub: https://github.com/tradermonty/claude-trading-skills

## 一句话总结
一个把「个人交易决策流程」拆成 74 个可安装 Agent Skill 的 Claude Code 技能包，它真正的差异化不是选股算法，而是给 AI 生成的金融结论加了一套「不可静默出错」的工程保证——代价是 62.5% 的提交都花在修 bug 上。

## 值得关注的理由
1. **AI 时代第一个「领域知识工程化」的大规模样本**：35 万行 Python、13 个月、1098 次提交、529 个测试文件——这个产能人工不可能实现。仓库里有 567 条 commit 署名 Claude 模型（Opus 4.6/4.7/4.8、Opus 5.5、Fable 5）。它真正在回答的问题是：**当代码由 LLM 批量生成时，如何让这些代码配得上信任**。
2. **把分布式系统的契约测试搬进了金融数据管道**：provider 响应契约 + 每周 live canary + 自动开漂移 issue，专门防「HTTP 200 但字段被静默改名」这类 silent failure；再往前一步，`evaluation_coverage` 契约把「评估了 0 个」和「评估了 500 个全不通过」区分开——这套东西在金融之外的场景同样通用。
3. **最反直觉的产品决策：明确不给你下单**。`portfolio-manager` 只调只读 Alpaca，`breakout-trade-planner` 只产出订单模板不下单，`exposure-coach` 只输出 allow/restrict/cash-priority 而非买卖指令。主动放弃执行层这个「最赚钱」的位，换来一条极清晰的安全边界。
4. **一个诚实到刺眼的样本**：#655 披露缺失 OHLC 在 9 个 skill 的 107 处被静默填 0、**会翻转交易信号**；而 `drawdown-circuit-breaker` 和 `pre-trade-discipline-gate` 这两个风险闸门本身至今仍是 beta。这是少见的、能同时看到「工程诚意」和「工程负债」的公开案例。

## 项目展示

![Navigator recommendation for a 15-minute daily market check](https://raw.githubusercontent.com/tradermonty/claude-trading-skills/main/docs/assets/previews/navigator-recommendation.svg)

Navigator 入口决策图 —— 回答「今天该看哪几个 skill」，是整个技能包的门面

![Market Posture Summary](https://raw.githubusercontent.com/tradermonty/claude-trading-skills/main/docs/assets/previews/market-posture.svg)

Market Posture 输出结构 —— 多输入汇总成风险姿态（36% 敞口上限 / REDUCE_ONLY / LOW 置信度），注意输出的是「姿态」而非指令

![Weekly Performance Digest](https://raw.githubusercontent.com/tradermonty/claude-trading-skills/main/docs/assets/previews/weekly-digest.svg)

Weekly Performance Digest —— 复盘闭环产物，把已平仓交易、胜率、实现盈亏结构化

> ⚠️ README 明确声明这三张图使用 **fictional data**（虚构数据），是示意图而非实盘截图或交易指令。

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/tradermonty/claude-trading-skills |
| Star / Fork | 6,840 / 1,404（fork/star ≈ 20.5%，远超正常开源的 3-8%） |
| 代码行数 | 354,724 行 / 2,300 文件（Python 84.0%、JSON 12.7%、YAML 3.1%）；740 个 md、146,863 行文档；529 个 test_*.py |
| 项目年龄 | 13 个月（2025-10-19 首次提交 → 2026-11-17 仍在推送） |
| 开发阶段 | 密集开发（近 90 天 378 commits，2026-11 单月 167 为历史最高） |
| 贡献模式 | 小团队 + 社区协作（40 位贡献者；takusaotome 473 > owner 280，但活跃期几乎不重叠的接力式结构） |
| 热度定位 | 大众热门 + 爆发期（4 天净增 2,799 star，+69%；已登 GitHub Trending 日榜前三） |
| 质量评级 | 代码[优秀] 文档[优秀] 测试[充分] |
| 发布状态 | ⚠️ 无 git tag、无 GitHub Release，CHANGELOG 只有 `[Unreleased]` 一节，pyproject 版本固定 0.1.0 |

## 作者视角：为什么存在这个项目

### 创始人/作者背景
作者 GitHub ID 是 `tradermonty`，但 profile **完全空白**——无姓名、无 bio、无公司、无位置、无博客。账号 2025-03-30 注册（1.6 年），267 followers，15 个公开仓库，本仓以 6,840 star 断层第一，最近推送时间与其他仓库基本同步，说明日常投入几乎全在这里。

但作者并非独自完成。提交历史里 `takusaotome` 提交 473 次，**超过 owner 的 280 次**，且使用企业邮箱 `takusaotome@fujisoft.com`（Fujisoft，日本 IT 公司）。他的早期提交直接是方法论设计——「Update US Market Bubble Detector to v2.1 - Fix confirmation bias」「Revise Bubble Detector skill to v2.0 with mandatory quantitative data collection」——**核心技能的方法论底色来自这位日方工程师，而非作者本人**。到 2026-09 他几乎完全淡出，owner 接管并在 2026-11 单月提交 134 次。

据此推断：作者是**日本市场的个人交易者/量化爱好者**（作者邮箱 `monty.traderesearch@gmail.com` 含「trader research」；README.ja.md 47KB 与 docs/ja 480 次改动量说明日语用户群是真实重心，而非随手翻译）。更准确的定位是「优秀的产品化组织者」，而不是「交易大师」——他的方法论来自外部宗师（Minervini 的 VCP、O'Neil 的 CANSLIM/FTD、Shapiro 的逆势三步、Kanchi 股息五步、Minsky/Kindleberger 泡沫框架），他的贡献是把这些体系工程化。

### 问题判断
作者看到的问题不是「AI 预测不准」，而是两层：

**表层**：兼职交易者做决策时同时被信息过载、情绪失控、缺乏可复盘记录三件事夹击。所以本仓的核心循环是 `Plan → Trade → Record → Review → Improve`，而不是 `Ask → Signal → Trade`——作者自称「a Claude Skills-based trading process OS」（决策流程 OS，不是信号源）。

**深层（也是本项目真正的价值所在）**：作者把「**AI 生成的 skill 是否配得上信任**」当成工程问题而不是提示词问题来解。Issue #293（production skill 有可执行脚本却无测试 → CI 必须失败）、#297（Common Trading Data Contract）、#298（质量看板）、#332（provider 契约测试 + live canary）、#507（冒烟测试「skip 不等于 pass」）这一整批带 `external-review-2026-08` 标签的 issue，是外部审计催生的整改项——**这一批 issue 的存在本身，就是本项目区别于所有竞品的分水岭**。

时机上，项目卡在两个窗口交汇处：Claude Code / Agent Skills 生态成型（`SKILL.md` 成为可分发的提示词单元），以及**模型编程能力跨过可用阈值**（567 条 commit 署名 Claude 模型）。**这个实验只有当模型能写出 3500 行不出错、且能被 CI 逐行 gate 时才成立**。

### 解法哲学
作者的价值观可以用「明确不做什么」来概括：

- **不下单**：`portfolio-manager` 只调只读 Alpaca，`breakout-trade-planner` 只产出 Alpaca 兼容订单模板
- **不给信号、不承诺收益**：README 顶部免责声明 + 每个 SKILL.md 的 `when_not_to_run`
- **不做剥头皮、不做实盘执行**（后者正是竞品 qmt-trading-skill 的定位）
- **空头侧主动暂缓**：PROJECT_VISION §10 把 short-side 列为 deferred（issue #715 跟踪），尽管仓内已有 `parabolic-short-trade-planner`、`options-strategy-advisor`

核心是 **fail-closed**：数据缺失时输出 `REVIEW_REQUIRED` / `PARTIAL` / `HALTED` / `journal_only`，而不是编造一个看起来合理的数字。在金融语境里这是生死线——`drawdown-circuit-breaker` 的规则是「状态不完整 → PARTIAL + HALTED」，宁可全停也不猜。

开源策略是 genuinely open：MIT、无付费墙代码、无遥测。**变现路径在本仓之外**——围绕它有 10 个兄弟仓（`claude-market-agents`、`hermes-trading-research-agent-work-package`、`finviz-mcp-server`、`uptrend-dashboard` 等）。本仓是品牌入口和产品矩阵的根节点，不是产品本身。

### 战略意图
PROJECT_VISION §10 把战略转向写得非常直白：**「From a skill collection to a Trading OS for solo traders」**。§11 给出七层架构（Skills → Skill Inventory/API Matrix(SSoT) → Skillsets → Workflows → Navigator → User Entry Points → Learning Loop），目标是让「不熟悉 GitHub 和工具配置的用户也能一步步用上价值」。

作者同时划了一条清醒的边界：**「与其急于扩大社区，不如优先保持这个工具对作者自己的实用性」**。这解释了为什么 74 个 skill 的宽度是「覆盖已验证的交易体系」而非「功能清单堆砌」——每个 skill 背后都是一个有名字的方法论。

> 官方文档洞察（https://tradermonty.github.io/claude-trading-skills/，已成功抓取）：价值主张是「Empower Solo Traders and Growing Together」；目标用户是兼职波段交易者、想加强风控的成长股投资者、股息长线投资者三类；核心仓 = 长线/ETF/股息，卫星仓 = 纪律化波段。官网无独立 blog，但 developer / planning 文档本身就是架构决策记录（Common Trading Data Contract、Provider Response Contracts、Release & Compatibility Policy、Maintenance Runbook、Strategy Research Bias Checklist）。

## 核心价值提炼

### 创新之处

1. **`evaluation_coverage` 契约：把「0 结果」拆成「不可评估 / 部分评估 / 完整评估」**（新颖度 4/5 | 实用性 5/5 | 可迁移性 5/5）
   版本化 schema 要求选股/回测类 skill 声明 `universe_size` / `evaluated` / `not_evaluated` / 逐终态理由计数 / 三态 verdict。校验器强制 `evaluated + not_evaluated == universe_size`、理由计数之和等于 `not_evaluated`、verdict 必须由计数推导（不能手填）。**缺证据的成员永远不算作 negative decision**。下游 Exposure Coach 通过 `evaluation_input_usable()` 排除声明为 partial / not_evaluable 的上游报告。
   *适用场景*：任何「跑一个筛选器/检索器，输出 N 条结果」的系统。零结果时用户无法区分「没有」和「查不了」——AI 搜索、RAG、代码扫描、招聘筛选都通用。

2. **Provider 响应契约 + live canary + 漂移 issue 持久化**（新颖度 4/5 | 实用性 5/5 | 可迁移性 5/5）
   `config/provider-contracts/<provider>/<endpoint>.v<N>.json` 记录真实响应 shape（`required_fields` 含 types/nullable/finite、`optional_fields`、`legacy_aliases`、`known_gaps`、`non_empty`、`owners` 必须是真实存在的 skill、`fixture` 脱敏真实行）。`scripts/provider_contracts.py` 是纯 stdlib 实现，含 FATAL/DEPRECATION 双严重度与 `RowValidation.summarized()`（同 code 聚合计数，避免 3 万行 CSV 刷屏）。`check` 离线跑（CI），`canary` 每周 live 探测，`notify_provider_drift.py` 把 fatal drift 写成 bot-authored 的 assigned tracking issue。
   docstring 里直接写明防的是什么：**「the provider returns HTTP 200 with a response that silently dropped/renamed a field a consumer reads, and nothing catches it until a downstream report goes quietly empty」**。
   *适用场景*：依赖免费/低价第三方 API 的任何项目。

3. **`read_price` / `find_bar_gaps`：把「缺失 = 0」这一 bug 类变成架构级禁令**（新颖度 3/5 | 实用性 5/5 | 可迁移性 5/5）
   100 行纯 stdlib helper，定义「有效价格」= 真数字（非 bool）、有限、（默认）> 0（volume 允许 0），缺失一律返回 `None`。配套 AST lint 禁止 `bar.get("close", 0)` 和 `bar.get("close") or 0` 两种形态，allowlist 的 count 必须与实际 finding 数**严格相等**（多了少了都不行），只能缩小不能扩大。#655 记录了这个问题在 9 个 skill 的 107 处会**翻转交易信号**。

4. **「源中央 + 生成 vendored + 漂移门」的一体化分发方案**（新颖度 3/5 | 实用性 5/5 | 可迁移性 5/5）
   74 个 skill 要能单独打包成 `.skill` 上传 Claude Web App（不能依赖仓库其他文件），但共享逻辑不能复制 74 份各自漂移。方案：`scripts/fmp_client/core_template.py.tmpl` + `registry.py` 渲染出 24 个 skill 的 `fmp_client.py`，模板用自研的 `# @@IF <flag>` / `# @@ELSE` / `# @@ENDIF` 条件编译；market_calendar、price_bars 同理生成到 7 个 / 多个 consumer。每个生成器都有 `--check` 漂移门 + pre-commit hook + CI step，还额外扫描「野生副本」。issue #115 记录的 9 份 fmp_client.py、2500 行漂移由此被机制性消除。

5. **Workflow replay + golden tree：多步流水线的字节级回归**（新颖度 4/5 | 实用性 5/5 | 可迁移性 4/5）
   14 个 workflow × 2 变体（`required-only` / `full-path`），`replay.yaml` 冻结 `fixed_timestamp` + fictional 输入，执行后逐字节比对生成树与 golden 树，区分「unexpected generated file」/「missing generated file」/「content drift」。CI job 名叫「Workflow replay (Coverage 14/14)」。单元测试只能证明函数对，这个证明「改了 skill B 之后用户拿到的报告还是不是原来那个」。

6. **Navigator 的「双环境字节级一致」契约**（新颖度 4/5 | 实用性 4/5 | 可迁移性 5/5）
   `recommend.py` 的元数据解析顺序是 repo-root SSoT（Claude Code）→ bundled `metadata_snapshot.json`（Claude Web App）。快照由 `build_snapshot.py` 用**同一组 `normalize_*` 函数**从 SSoT 生成，因此两条路径输出字节相同，该不变量由 golden 测试守护。

7. **「豁免只能缩小」的 ratchet 化 lint 机制**（新颖度 4/5 | 实用性 4/5 | 可迁移性 5/5）
   所有 allowlist（CLI 错误约定、price-bar 零默认、security exceptions、coverage waiver）都要求每条带 reason（+ issue + `expires_on`），**count 与实际 finding 严格相等**，不再匹配则判定 stale 并失败，**过期即 fail closed**。这是把 GitHub issue 当技术债数据库的完整实现——开源项目里极罕见。

8. **「零静默绿灯」的 canary 三态设计**（新颖度 4/5 | 实用性 4/5 | 可迁移性 4/5）
   `fmp-contract-canary.yml` 显式区分 `configured`（探测，drift report-only）/ `disabled`（显式 opt-out）/ `not configured`（secret 未配且没 opt-out → **preflight 直接失败，红跑**，以触发 GitHub 定时任务失败通知）。「没配 key」不能既不跑也不报警——这是很多项目忽略的语义空洞。

9. **Git 索引级私人路径守卫**（新颖度 4/5 | 实用性 4/5 | 可迁移性 5/5）
   `check_private_data_paths.py` 读的是 **Git 索引**（`git ls-files --stage`）而非工作区，所以 `git add -f` 也躲不过；白名单只有两个空 `.gitkeep`；`.env*` / `.mcp.json` 单独归类为 credentials 违规；索引不可读时 fail closed。处理个人数据、凭据、客户数据的仓库都该学这个。

10. **「先写报告再失败」的 CI 失败模式**（新颖度 3/5 | 实用性 4/5 | 可迁移性 4/5）
    coverage 聚合步骤先输出 `per-skill-coverage.json` / `.md`，**然后**才对地板违规返回失败——保证 CI 红了仍然留下可行动的证据。

11. **三态 CLI 退出码约定**（新颖度 3/5 | 实用性 4/5 | 可迁移性 5/5）
    AST lint 强制：错误信息走 stderr；缺依赖必须 exit 2 并给出该 skill 的 `requirements.txt` 路径（从脚本位置解析，任何 cwd 下都可用）；网络调用必须有 `timeout=`。自动化脚本因此能可靠区分「环境没配好」和「结论是不通过」。

12. **姿态而非指令的输出契约**（新颖度 3/5 | 实用性 4/5 | 可迁移性 4/5）
    `exposure-coach` 只输出 `exposure_decision` ∈ {allow, restrict, cash-priority}；`contrarian-setup-gate` 用 fail-closed 优先级状态机合成三个上游报告为 `setup_status`（READY_FOR_PLAN / WATCHING_PRICE / CROWDED / REJECTED / INSUFFICIENT_EVIDENCE），且明确「早一步的确定性结论不会被后一步的问题软化」；`pre-trade-discipline-gate` 输出 GO / REVIEW_REQUIRED / NO_GO / NO_ACTIONABLE_ORDERS。

### 可复用的模式与技巧

| 模式 | 说明 | 适用场景 |
|------|------|---------|
| 单一真相源 + 哨兵标记 + `--check` 漂移门 | `skills-index.yaml` 是 SSoT，README 主动让位并明文写「如果本文档与索引不一致，以索引为准」；生成块用 `<!-- name:xxx:start -->` 哨兵包住 | 同一份元数据要在多处呈现（README / 文档站 / API 矩阵 / 多语言同步） |
| 双 ownership 的生成文档 | `generated: true` 归生成器（可覆写、可漂移检查），缺标记归人手写（生成器拒绝覆写，`--force` 是 CI 禁止的逃生门） | 半自动文档站的混合维护 |
| 契约 → 离线 check → live canary → 漂移 issue 四段式 | 第三方 API 集成的标准防 silent failure 流程 | 外部数据源集成 |
| AST lint + 只缩小的 allowlist | 用静态分析禁止特定代码形态，用带 count 的豁免清单管理存量 | 大规模代码库的 API 迁移 |
| 评估覆盖率契约（0 结果 ≠ 不可评估） | `evaluation_coverage` 三态 + 逐成员终态理由 | 筛选器 / 检索 / 扫描类系统 |
| 数据溯源块（provenance） | 强制声明 `adjusted` / `point_in_time` / `survivorship_free` / `corporate_actions_handled`——正好对应回测污染的四个经典来源 | 回测、财报分析、数据管道 |
| 源码中央 + vendored 生成 + 漂移门 | 模板 + registry + 条件编译 → 生成到 consumer + `--check` 门 + 野生副本扫描 | monorepo 里要出「可独立分发子包」 |
| 冻结时间的 golden tree 回归 | 固定时间戳 + fictional 输入 + 逐字节比对 | 多步 agent 流水线 |
| 姿态输出契约（posture ≠ directive） | 决策辅助系统必须区分「建议」和「指令」 | 任何给建议的系统 |
| 三态退出码约定（0 结论 / 1 业务失败 / 2 环境缺失） | 让调用方能区分环境问题与业务结论 | 脚本化 CLI 集合 |
| Git 索引级隐私守卫 | 查索引而非查文件，`git add -f` 逃不掉 | 含个人数据/凭据的仓库 |
| ratchet 式覆盖地板 + 必过期豁免 | 按风险分档设覆盖门槛（普通 70% / 核心风险类 85%），豁免必须带 issue + 过期日，过期 fail closed | 遗留代码库质量治理 |
| 确定性打分 → 阈值触发 LLM → 复评 → 回滚 → 只开 PR | `run_skill_improvement_loop.py`：0-100 确定性打分，低于 90 才调 `claude -p` 改，改完重新打分，**没提升就回滚**，只开 PR 等人审 | 规则/提示词/技能库的自维护 |
| 依赖注入式元数据双路径 | 仓库 SSoT + 内嵌快照，共用同一组 normalize 函数，保证两种分发形态字节一致 | 多形态分发的同一逻辑 |

### 关键设计决策

**1. 让 README 主动让位于 `skills-index.yaml`**
- 问题：74 个 skill 的元数据若散在 SKILL.md frontmatter、README、文档站、Navigator 快照四处，必然漂移
- 方案：`skills-index.yaml` 是唯一权威索引；README catalog、CLAUDE.md API 矩阵、文档站 skill 页、Navigator 快照全部由 `scripts/generate_*.py` 生成；每个生成器都有 `--check` 模式，对应 pre-commit hook + CI step
- Trade-off：牺牲 README 的手写自由度（改描述必须先改 index 再跑生成器），换来单一真相源 + 机械可验证
- 可迁移性：**高**

**2. Workflow manifest 作为「可执行流程的一等公民」**
- 问题：skill 只是一块能力，用户真正需要的是「先做什么、什么条件下才能做下一步、产出什么、下游拿什么」；这逻辑只写在 SKILL.md 里就无法校验、replay、生成文档
- 方案：`workflows/*.yaml` 是版本化 schema（`schema_version: 1`），声明 `required_skills` / `steps[]`（每步 `skill` + `produces` + `consumes` + `decision_gate` + `decision_question`）/ `artifacts[]`（含 `downstream_hints`）/ `manual_review` / `when_not_to_run`（中英双语）；`validate_skills_index.py --strict-workflows` 校验 artifact 交接一致性、required_skills 覆盖、决策门必须有问题、deprecated skill 不得出现在 required_skills
- Trade-off：引入一层 YAML 间接（`workflows/README.md` 专门教怎么读），换来流程本身成为可校验、可生成文档、可 replay 的对象
- 可迁移性：**高**

**3. Fail-closed 的三层语义，且写成可执行契约**
- 问题：金融场景里「数据缺失时给个默认答案」和「数据缺失时停下来问人」的价值差是数量级的
- 方案：`data_provenance`（11 个必填字段 + ISO-8601 带时区时间戳 + bool 严格类型）→ `evaluation_coverage`（三态 + 逐成员终态理由）→ PRICE-bar 零默认禁令（AST lint + 只能缩小的 allowlist）
- Trade-off：严格性带来大量「正常路径也要写防御代码」的噪音，也让报告在数据不全时看起来「什么都没发生」；换来永不静默出错
- 可迁移性：**高**

**4. 按风险分档的覆盖门槛，而不是统一门槛**
- 问题：35 万行代码 + 74 个 skill，覆盖率极易变成形式
- 方案：`config/ci-test-policy.yaml` 定义 aggregate 75%、per-skill 默认 70%、核心风险类（`position-sizer` / `futures-position-sizer` / `trader-memory-core` / `drawdown-circuit-breaker`）85%；豁免必须带 `expires_on` + `issue` + `reason`，过期 fail closed；`allowed_failures` 当前为空且要求目标为 0；**测试存在性本身是 gate**——有可执行脚本的 skill 必须有 `test_*.py`，无脚本的 production skill 必须声明 `knowledge_only: true`（与非测试脚本冲突时报 IDX014）
- Trade-off：多数 skill 只有 70% 地板，深度不够；换来关键路径覆盖远高于平均
- 可迁移性：**高**

**5. `CLAUDE.md`（1013 行）作为「AI 工程师的项目规约」**
- 问题：这个仓库大量内容是给 AI agent 读的（Claude Code 每次进 repo 都读 CLAUDE.md），传统 README 承载不了「怎么加一个新 skill 的完整 6 步 + pre-commit 强制点 + 文档 ownership 规则」
- 方案：覆盖架构分层、渐进式加载规则、**script vs reference 分工**（「Scripts handle I/O; references handle knowledge」）、加 skill 的 6 步流程、TDD-first 规约、production verification 的 8 轴定义、API Key 管理三列表
- Trade-off：与 README/文档站有重叠，靠哨兵标记 + drift gate 防分叉；换来 AI 协作的高吞吐
- 可迁移性：**高**

**6. 双语（EN/JA）作为一等公民，且 JA 不得回退到 EN**
- 问题：目标用户含日语人群，但双语文档极易变成机翻 + 漂移
- 方案：`docs/{en,ja}/` 完全平行，`generate_workflow_docs.py` 要求 JA 必须有完整 `*_ja` 文案，不得回退到 EN（否则报 WF014）；README.md / README.ja.md、PROJECT_VISION.md / .ja.md 并列；Issue/PR 模板全双语
- Trade-off：每个文档改动写两遍（成本翻倍），换来日语用户的完整可用性
- 可迁移性：**高**

**7. launchd 自改进闭环 + 三重闸门**
- 问题：74 个 skill 的质量不可能全靠人工维护，且「哪个 skill 最弱」机器可以判断
- 方案：4 个 macOS launchd plist 驱动 `run_skill_improvement_loop.py` / `run_skill_generation_pipeline.py`：round-robin 选一个 skill → 确定性打分（0-100）→ 低于 90 才调 `claude -p` 改 → 改完重新打分，**没提升就回滚** → 提交并开 PR 等人审。weekly 模式从 session log 挖 skill 想法（`skill-idea-miner`，因隐私敏感，只发脱敏摘要不发原始日志）
- Trade-off：依赖 macOS launchd（非 Linux 友好）；自动改代码天然有风险，所以设「分数门槛 + 回滚 + 只开 PR 不直接推 main」三重闸门
- 可迁移性：**中**（模式可迁移，平台耦合降低通用性）

## 套利机会分析

- **信息差**：项目本身**已无信息差**——6,840 star、4 天涨 69%、已登 Trending 日榜前三、DeepWiki 已收录。真正的信息差在于**读法**：大众读到的印象是「又一个 AI 炒股工具」，而它实际是「用 35 万行代码演示如何给 LLM 生成的金融知识加质量保证」。这个误读本身就是套利空间。
- **技术借鉴**：本仓对技术社区的价值大于对交易者的价值。可直接搬走的四件套：① 契约 → check → canary → 漂移 issue 的外部 API 防 silent failure 流程；② `evaluation_coverage` 的「0 结果 ≠ 不可评估」；③ AST lint + 只缩小的 allowlist ratchet；④ 源码中央 + vendored 生成 + 漂移门。
- **生态位**：它不在「数据源」也不在「信号源」也不在「执行层」，而是位于原始数据与用户决策之间的**流程编排 + 风险闸门 + 可复盘记录 + 质量证据**层。**AI 时代让 LLM 输出可信金融结论的第一个大规模工程化样本**。
- **趋势判断**：符合两个明确趋势——Agent Skills 生态成型（skill-packages 已被 skills.sh 收录 74 条、累计约 233K 安装）、以及「AI 生成代码需要质量工程」这个正在成为共识的议题。宽度迟早被追平，质量护城河短期难破。但当前 star 增长与「AI 荐股」舆论争议话题同期（2026-11-14 中国券商 AI 荐股被骂上新闻的同一天，该项目登热榜），**存在情绪反转风险**：热度回落时的真实留存率才是关键。

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | claude-trading-skills | day-trader-skill | AlphaGBM/skills | staskh/trading_skills | qmt-trading-skill |
|------|----------------------|-------------------|-----------------|----------------------|-------------------|
| Stars | 6,840 | ~6,900 | — | — | — |
| Skill 数 | 74（+6 skillset + 14 workflow） | 单一 skill 集合 | 29 | 25 | 22 |
| 市场 | 美股（ETF/股息/成长股） | 美股日内 | 美股实时 | 美股期权 | A 股实盘 |
| 数据源 | FMP 32 个 / FINVIZ Elite 4 个，另有 32 个 skill 可离线跑 | 免费 Yahoo + SEC + House Clerk | 实时行情集成 | Massive + IBKR | 本地 QMT 券商终端 |
| 自动下单 | ❌ 明确拒绝，只出订单模板 | ✅ 含纸面交易 | ❌ | ✅ 某止损 skill 显式 flag 后可下单 | ✅ 实盘闭环 |
| 风险闸门 | ✅ 三个独立 skill（熔断/纪律门/敞口姿态），核心风险类 85% 覆盖 | 内嵌在主流程 | 部分 | 弱（仅期权/扫描维度） | 未见系统化闸门 |
| 数据可靠性工程 | ✅ provider 契约 + live canary + provenance + evaluation_coverage | ❌ | ❌ | 部分 provider 契约 | ❌ |
| 端到端回归 | ✅ 14 workflow × 2 变体字节级 golden replay | ❌ | ❌ | ❌ | ❌ |
| 语言 | Python | — | — | — | — |
| 文档 | 740 md / 14.7 万行 / EN+JA 平行 | — | — | — | — |

> `agiprolabs/claude-trading-skills` 与本仓**同名但无关**——是加密/DeFi/预测市场方向（67 skills），搜索时常被误配。

### 差异化护城河

- **技术护城河（中等强度，非独占）**：provider 契约 + provenance + evaluation_coverage + fail-closed 三件套构成的「数据可信度工程栈」，需要长期积累（#293 → #800 的演化史不是短期能抄的）。但**每一件的技术门槛都不高，别人可以照抄**。
- **生态护城河（强）**：SSoT 驱动的元数据一致性 + 74 skill 覆盖面 + 14 workflow 操作化 + 6 skillset 目的分组 + Navigator 路由。这是「宽度 + 可维护性」的组合——竞品要么窄（22/25/29），要么宽但无治理。10 个兄弟仓矩阵进一步放大入口优势。
- **信任护城河（最强，也最脆弱）**：**「AI 生成的 skill 是否配得上信任」被当工程问题解**——这是本仓真正的差异化叙事。但它同时是当前最大的负债：#655（107 处 OHLC 静默填 0，会翻转信号）、#800（market cap 解析小 100 万倍）、#332（契约测试尚无 live canary 门禁）都说明**质量保证体系是后建的，正在追赶规模扩张**。更刺眼的是——**风险闸门本身（drawdown breaker、pre-trade discipline gate）至今仍是 beta**，被审视的项目自己最该先审的部分还没毕业。

### 竞争风险

- **最可能被替代的不是本仓，而是「本仓的某个子集」**。最危险的是 `staskh/trading_skills` 这类：25 skill、更聚焦、接真实券商。若用户从「决策纪律」转向「执行效率」，迁移成本虽高但收益路径清晰。
- `Jakeschincariol/day-trader-skill` 是 star 量级上的直接威胁（6,900 vs 6,840），社区更大，上手成本更低。
- **自身风险**：74 skill + 14 workflow 的复杂度正在逼近单人维护上限（近 200 commit 中 fix 125 / feature 21 ≈ 6:1，且 fix 集中在数据正确性）。若质量债务继续累积，「宽度」会从优势变负担——本仓自己在 #502（拆 3 个超大文件）、#501（拆 9 个过长的 SKILL.md）里已经承认这点。
- **合规风险**：美国 SEC 对「自动化投资建议」的界定若收紧，「不给买卖建议」这条护城河价值会上升，但合规成本也会增加。

### 生态定位
位于「原始数据（Yahoo / FMP / SEC / CSV）」与「用户实际决策」之间，提供**流程编排 + 风险闸门 + 可复盘记录 + 质量证据**。它不是数据源，不是信号源，不是执行层。它的独特位置是：**AI agent 时代「让 LLM 输出可信金融结论」的第一个大规模工程化样本**。因此它有两类受众——想改善个人交易纪律的用户，以及**想学「如何给 AI 生成的领域知识加质量保证」的工程师**；后者才是本仓对技术社区的最大价值。

## 风险与不足

1. **fix : feature ≈ 6 : 1**（近 200 commit 中 125 vs 21）。功能广度已经饱和，项目当前最大的风险不是「功能不够」，而是「已有功能是否可靠」。
2. **#655 尚未修复**：缺失 OHLC 在 9 个 skill 的 107 处静默填 0，会翻转交易信号——「fail-closed」承诺在数据入口层被打破。**这是评估「能不能真用」的第一优先级验证点**。
3. **风险闸门自身仍是 beta**：`vcp-screener` 是 production，但 drawdown breaker 和 pre-trade discipline gate 是 beta。用户容易默认「风控已经到位」。
4. **无法 pin 版本**：`git tag` 为空、Release 为 0、CHANGELOG 只有 `[Unreleased]` 一节、pyproject 固定 0.1.0。README 却引导下载「latest GitHub Release」的 `.skill` + `SHA256SUMS`——**文档与实际发布状态不一致**。对 74 个 skill、162 个依赖、且依赖 FMP/FINVIZ 服务端行为的项目，这是真实的可用性风险。
5. **「production」标签与「已验证」之间的落差**：`skills-index.yaml` 中大量技能的 `verification` 八轴仍是 `not_verified`，质量看板却显示 62 production。这是本仓最诚实的一处债务披露，也说明标签体系尚未统一。
6. **权限面与隐私敞口**（外部评测指出）：读持仓未必需要交易权限，但把 live key 接到 MCP server 后未来/意外的订单逻辑就具备执行能力，仓库不强制最小权限；`skill-idea-miner` 挖掘 Claude Code session 日志，而日志里可能含持仓、余额等敏感信息——「读什么、存到哪」未完全澄清。
7. **策略有效性未经独立验证**：GitCode 那篇方法论精读指出，「回测平台层面的污染（插值、低流动性处理、数据对齐错位）是任何外部 grader 都检测不到的失败模式」——作者自己也承认「discretionary traders may not apply」。
8. **数据源脆弱**：`theme-detector` 在 FINVIZ Elite CSV 解析上反复翻车（market cap 小 100 万倍、千分位解析为 0、截断 CSV、BOM 字符），是全仓最常出血的伤口；FMP 按 plan 限速、免费 Basic key 对 screener 端点直接拒答。
9. **复杂度天花板**：74 skill + 15 workflow + 30+ 生成器 + 20+ pre-commit hook，作者本人是单人维护主体（近 30 天 151 commit 对 takusaotome 的 1 commit），bus factor 偏低；`ruff max-complexity = 128` 实质上等于关闭复杂度检查。
10. **热度结构风险**：4 天 +69% 的增长与「AI 荐股」舆论争议同期，fork/star 高达 20.5%（大量 fork 是拿去本地化改造，而非收藏）。这既是真实使用意愿强的信号，也是「热度可逆」的信号。

## 行动建议

### 如果你要用它
- **适合**：美股长线/ETF/股息投资者、有纪律的波段交易者；愿意为 FMP 免费档（多数选股 skill 需要）或 FINVIZ Elite 付费（4 个 skill）买单；**愿意先读方法论再跑工具**的人。
- **不适合**：想要自动下单的、想做日内剥头皮的、需要 A 股/台股本地化数据的（国内评测实测发现台股改造时「指数在高位但仅 55% 个股站上 200 日均线」的背离，本仓是美股数据中心）。
- **上手路径**：先走 README 里的**无 API key 起步路径**（5 个 skill，纯 CSV / 截图 / 本地文件）→ 再用 Navigator（~10 问）定位你的 skillset → 最后才接付费数据源。**注意 32 个 skill 标为 offline，核心风险路径零外部数据源可跑**。
- **先自检三件事**：① 拉一下 #655 的修复状态（107 处静默填 0 会翻转信号）；② 确认你要用的风险闸门 skill 是否还在 beta；③ 由于无 Release，用 git commit SHA 锁定版本，别用 main 分支。
- **对比选择**：想要执行层和更低上手成本 → day-trader-skill；想要实时行情和机会发现 → AlphaGBM/skills；想要期权深度和真实 IBKR 执行 → staskh/trading_skills；需要 A 股实盘 → qmt-trading-skill。**本仓的独占位是「决策纪律 + 质量证据」，不是数据也不是执行。**

### 如果你要学它
按这个顺序读，**五个文件就能抓住它的方法论骨架**：

1. **`PROJECT_VISION.md`**（31.8KB / 17 章）—— 战略转向、七层架构、fail-closed 哲学的原始陈述。§4（核心循环）、§10（从 skill collection 到 Trading OS）、§11（分层架构）必读
2. **`skills-index.yaml`**（76KB）—— SSoT 的实际结构，理解 schema 设计
3. **`CLAUDE.md`**（1013 行）—— 「AI 工程师的项目规约」怎么写：script vs reference 分工、加 skill 的 6 步、production verification 八轴
4. **`scripts/provider_contracts.py` + `config/provider-contracts/`** —— 四段式防 silent failure 的完整实现，这是全仓最值得抄的一段代码
5. **`scripts/price_bars/price_bars.py` + `scripts/check_price_bar_defaults.py`** —— AST lint + 只缩小的 allowlist，一个 100 行 helper 挡住 107 处 bug 类
6. 补充：`scripts/workflow_replay_pkg/`（冻结时间的字节级 golden 回归）、`scripts/validate_skills_index.py`（三层严格校验）、`config/ci-test-policy.yaml`（风险分档覆盖门槛）

### 如果你要 fork 它
- **必做**：不要 fork 后继续在 `main` 上开发——本仓无 tag，靠 SHA 锁定版本；fork 后立即建立自己的版本策略（哪怕只是 tag 每个 merge）
- **值得改的方向**（作者自己列在 issue 里的）：#502 拆 3 个超大文件、#501 拆 9 个过长的 SKILL.md；#332 给 provider 契约加 live canary 门禁；#297 落地 Common Trading Data Contract；#655 补齐 107 处静默填 0；#800 修 theme-detector 的数值解析
- **最省力的改进**：把 `ruff max-complexity = 128` 调到有约束力的数值（作者注释说会随债务减少下调，但当前等于关闭）
- **最有价值的改进**：把风险闸门 skill（drawdown breaker、pre-trade discipline gate）从 beta 推到 production —— 这是整个信任叙事的关键缺口
- **注意隐私红线**：本仓有 `check_private_data_paths.py` 索引级守卫 + `.secrets.baseline`。fork 后若要放自己的持仓/券商数据，**先读 `docs/en/privacy.md`**，别把 `state/` 目录里的东西 commit 进去

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | [deepwiki.com/tradermonty/claude-trading-skills](https://deepwiki.com/tradermonty/claude-trading-skills)（已收录，含单个 skill 的子页） |
| Zread.ai | 未收录（返回 403） |
| 关联论文 | 无（个人 GitHub 项目，非学术产出） |
| 在线 Demo | 无独立 playground。替代路径：官网 [docs/assets/previews/*.svg](https://tradermonty.github.io/claude-trading-skills/) 的虚构数据示例输出、`examples/workflows/*/sample-run/` 的机器可读产物、作者衍生的 Hermes 发行版 [hermes-trading-research-agent-work-package](https://tradermonty.github.io/hermes-trading-research-agent-work-package) |
| 官方站点 | https://tradermonty.github.io/claude-trading-skills/ |
| 外部深度评测 | [2833 星的 Claude 交易技能包：74 个 Skill 覆盖选股到复盘，但它明确说自己不下单](https://blog.mushroom.cv/blog/claude-trading-skills-tradermonty-stock-workflow-toolkit) · [Backtest Expert 方法论精读](https://blog.gitcode.com/18d671e0f724ec8573adb73446b8a605.html) |
