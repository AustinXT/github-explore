# GitHub推荐：9K stars 的 NVIDIA 语义层：文档和代码打架的三处

> GitHub: https://github.com/nvidia/auto-ontology

## 一句话总结

NVIDIA 把 2026 年 2 月收购的以色列语义层公司 Illumex 的商业产品内核重写成开源项目，用「Postgres 关系表 + UNION ALL 视图做图遍历」「用真实数据库反证生成的 SQL」「MCP 工具面做语义允许列表」三套确定性机制，替 Agent 补上企业数据最缺的那层语义——但 README 承诺的「人工认证才可信」在代码里根本没被执行。

## 值得关注的理由

1. **它是本季度工程成熟度最高的开源 text-to-SQL 基础设施**：22.6 万行代码、159 个 Python 测试文件（约 4.5 万行测试对 8 万行生产代码）、13 条 CI workflow、每个非显然决策都写清了「失效场景 + 为什么不那样做」。
2. **「用真实数据库反证 SQL」是可以直接抄走的确定性范式**：不读声明的 schema，只用生成的 SQL 的 AST 加对真实库的只读探针推导事实，只修近邻错误、无近邻就放行——这比任何 prompt 工程都硬。
3. **三处「文档说一套、代码做另一套」是可验证的事实，不是猜测**：认证标志（certified）在 `semantic/` 与 `retrieval/` 全域零引用；「答不了就别硬答」的兜底会把被拒绝的 SQL 原样塞回答案；单列主键从不参与列唯一性推断。这三条都有明确的代码位置。

## 项目展示

![Auto Ontology 架构图](https://raw.githubusercontent.com/nvidia/auto-ontology/main/docs/assets/arch.png)

> 官方架构图：Postgres（public + frontend 双 schema）承载目录、本体与向量；FastAPI 后端（3001）+ ingestion worker（3002）+ FastMCP 侧车（3003）+ Next.js 网关（3000）。

![Wide World Importers 本体语义图谱](https://raw.githubusercontent.com/nvidia/auto-ontology/main/docs/assets/ontology-graph.png)

> 本体在 UI 上是一张可交互的语义图谱：选中的 Order 术语连向它涉及的表、审定过的 SQL attribute 与关系边——这正是「本体是知识图谱而非指标目录」的直观证据。

![Chat 问答与生成的 SQL](https://raw.githubusercontent.com/nvidia/auto-ontology/main/docs/assets/qa-example.png)

> 官方问答示例：自然语言问题 → 生成的 SQL → 营收图表。README 里的另两个例子同样值得看——「USB food flash drive - sushi roll 在 Pennsylvania 2015 年 6 月营收」答出 $588.80，而「广告 ROI」被明确回答为「本数据源没有广告数据」。

- 官方发布材料：[NVIDIA Agent Toolkit Expands, Grounding Enterprise Agents in Company Data](https://blogs.nvidia.com/blog/enterprise-platforms-agent-toolkit)（2026-10-21，Auto Ontology 被定位为 Agent Knowledge Foundation 的「业务概念层」）
- 评测仓库：[NVIDIA/ontology-sql-eval](https://github.com/NVIDIA/ontology-sql-eval)（BIRD 等 text-to-SQL 基准，含 schema-only 对照组设计）
- 可复现 Demo：Docker Compose + Wide World Importers 样例库（种子脚本见 [NVIDIA/auto-ontology-eval](https://github.com/NVIDIA/auto-ontology-eval) 的 `seed_wwi.py`），无官方托管 demo

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/nvidia/auto-ontology |
| Star / Fork | 9,065 / 730 |
| 代码行数 | 226,301 行（Python 45.7%、JSON 20.9%、SQL 14.2%、TSX 10.1%、TypeScript 4.3%） |
| 项目年龄 | 7 个月（首次提交 2026-04-06，仓库创建 2026-04-27） |
| 开发阶段 | 密集开发（近 30 天 127 commits，近 90 天 470 commits，日均 4.2 commits，2026-06 单月 295 commits） |
| 贡献模式 | 小团队主导（19 名贡献者，Top 1 占 36.8%，13/19 为 NVIDIA 内部账号，仅 3 位外部贡献者） |
| 热度定位 | 大众热门（GTC Berlin 2026 发布后 6 天从 2.4K 涨到 9K，HN 首页当日约 175–223 分） |
| 质量评级 | 代码 优秀 / 文档 良好 / 测试 充分（后端 159 文件约 4.5 万行，前端 0） |
| 许可证 | Apache-2.0 |

> 代码体量口径：tokei 统计，含 `docs/openapi/*.json` 生成的 API 契约（4.7 万行 / 仅 14 个文件）与 `alembic/versions/` 迁移脚本（3.2 万行 / 3 个文件）。JSON 占 20.9% 这个数字本身就是信号——**API 契约先行**是项目的架构信条。

## 作者视角：为什么存在这个项目

### 创始人/作者背景

Auto Ontology 不是个人项目，也不是从零开始的论文项目，而是 **NVIDIA 2026 年 2 月收购的以色列语义层创业公司 Illumex（GSF 团队）的商业产品内核开源化重写**。Illumex 创始人 Inna Tokarev Sela 是前 Sisense AI 负责人，收购价约 6000 万美元。

代码里到处是这次「移植」留下的痕迹：

- `frontend/lib/answerMessages.ts` 写着「One agent answer renders as up to two assistant bubbles (illumex-style)」；`frontend/components/chatPage/MessageBubble.tsx` 注释「illumex Message 2」。
- `auto_ontology/dal/session.py:49` 保留着从 Neo4j 迁移到 Postgres 的对照记录——「in the same range illumex used for the equivalent Neo4j writes」。
- `auto_ontology/dal/schema.py:1122` 写着「Illumex loads the same idea from Frontegg (id, name, description, color, roles, users, and the permissions those roles expand to). There is no Frontegg here, so the group is a row this schema owns.」——把商业 SaaS 的外部依赖**内化为自有关系模型**的典型手法。
- 早期提交有 Neo4j / DataTree 架构痕迹（2026-04-13「getting all data from Neo4j, and fix logica in DataTree」），2026-09-23 的 PR #295「Rename GSF to Auto Ontology」把 `gsf/` 整包改名为 `auto_ontology/`。

贡献者名单也印证这一点：Dina Laptii、Yuval Shkolar、Liav Nave、Tomer Levin——清一色以色列名字。

### 问题判断

Illumex 做的是 BI 语义层（Sisense 那一脉的心智模型），它看到的是一个具体且昂贵的问题：**同一个业务概念在不同系统里定义不同**。`tier` 在一个系统里是套餐等级、在另一个系统里是流量档位；`plan` 是商业计划还是技术蓝图？LLM 面对 300 列业务表时会把 `tier` 和 `plan` 当成不同概念，产出**语法正确、语义错误、且不抛异常**的答案——这类错误比崩溃危险得多，因为流水线全程绿灯。

Illumex 的答案是「建本体 + 人工审定」。NVIDIA 收购后保留了这条主线，但换了一个问题陈述：不是「怎么给人做看板」，而是「**怎么让 Agent 知道企业数据是什么意思**」。README 第一句就把命题立死：「a revenue metric answered faster is worth nothing if the number is wrong」。

时机为什么是 2026 年？三个条件同时成立：(a) Agent 开始进入企业生产，text-to-SQL 从玩具变成基础设施；(b) 主流 text-to-SQL 栈的校验器普遍只做语法检查与 LLM 语义打分，**没有一个「用真实数据库反证 SQL」的确定性闸门**；(c) NVIDIA 正好握着一支被收购来的、做过多年企业语义层的团队。

### 解法哲学

贯穿代码的价值观是四句话：**语义优先、检索先于生成、确定性校验优于语法校验、只读接口 + 人工写路径分离**。

代码里能逐一找到落点：

- **确定性优先于 LLM 判断**：`auto_ontology/retrieval/text_to_sql/db_probe/` 整个包（约 3000 行）就是「用真实数据库反证 SQL」的校验器群。注释写得很清楚：makes no assumptions about the incoming database——它们**不读声明的 schema**，只从生成的 SQL AST 加运行时只读探针推导事实。
- **主动输出「我答不了」**：`check_answerable` 不是营销词，它是一个真实的确定性计算——「被 embedding 检索覆盖的实体数 ÷ 问题中实体总数」，纯算术，无 LLM 判定。
- **只读接口，不给裸 schema 浏览**：MCP 从 87 个 API operation 里手工挑出 9 个工具，模块 docstring 里的理由是「agent tool-selection degrades well before that count」以及「a tool that lists schemas or columns invites an agent to bypass it and reason about raw tables instead」。`describe_table` 是唯一例外，因为它返回的是「该表参与的 terms 和 SQL attributes」，不是列清单。
- **性能/易用性偏向可靠性**：单题最多 16 条 SQL（7 次重建 × 2 轮流水线 + 主路径），宁可慢也不给错答案。

明确**不做什么**，同样清晰：不做人工语义建模 UI（Cube 的强项）、不做 dashboard/图表产出链（WrenAI 的强项）、不做 LLM-as-judge 评测、**不做裸 schema 浏览工具**。

### 战略意图

- **位置**：NVIDIA Agent Knowledge Foundation 的**业务概念层**。同批发布的还有 CUDA-X、Nemotron Retriever（检索）、Kumo Structured（预测）、OpenShell（安全）、NemoClaw（运行时）。Auto Ontology 解决「Agent 如何知道企业数据是什么意思」。
- **商业意图明确存在**：Helm chart、Docker Compose、NGC 多架构镜像（`nvcr.io/nvidiasw-auto-ontology`）、Better Auth SSO + API token、Per-connection Vault 凭据托管、KumoRFM 托管预测集成——这是一套**企业级私有化部署**的完整交付形态。
- **开源策略：source-available 而非 open-core**。Apache-2.0 是真开源（无 copyleft），但 CONTRIBUTING.md 明确「does not accept external pull requests」，走 integration request 模板（Issue 模板 `integration.yml`）。这是**「接口标准化 + 实现封闭」**策略：把语义层的接口面（MCP 工具清单、Ossie YAML 格式、REST 路径）标准化，把实现锁定在 NVIDIA 手里。
- **标准化意图已被验证**：Apache Ossie（厂商中立的语义模型交换标准）已经为 auto-ontology 增加了专用转换器（`apache/ossie-converters` 的 `nvidia` 目录），`pyproject.toml` 直接依赖 `apache-ossie-nvidia-auto-ontology`。**这是全项目最硬的一条护城河**——Cube 与 WrenAI 都没有进入这个标准生态。

## 核心价值提炼

### 创新之处

按「新颖度 × 实用性」排序：

1. **运行时反证式 SQL 修复（Database-Grounded Repair）** — 新颖度 4/5 · 实用性 4/5 · 可迁移性 4/5
   不读声明的 schema，只用「生成的 SQL 的 AST」+「对真实数据库的只读探针」推导事实。三个检查器：字面量近邻检查（`difflib` 相似度阈值 0.6）、JOIN 路径合法性检查、JSONB 键路径检查。两条保守性设计比机制本身更值得抄：**只修近邻错误**——「A literal with no close real counterpart is left alone, because an empty result can be the correct answer」；**重叠显著就放行**——值重叠探针阈值 0.2 刻意宽松，因为「误判为真的代价远小于误判为假的代价」。

2. **关系型存储上的最短 join 路径图引擎** — 新颖度 4/5 · 实用性 4/5 · 可迁移性 4/5
   把 Column / ColumnAttribute / Table 四类边 UNION 成一张 `join_path_edge(src_kind, src_id, dst_kind, dst_id)` 视图，在 SQL 层跑 BFS，**每条边携带确切的 join 列对**。方向性有讲究：FK→owner 双向都算，但 owner→FK **只在 owner 列是该表声明主键时**才加，否则两个引用同一非主键的 FK 列会被读成「彼此可 join」——那是捏造的 join。

3. **MCP 工具面的语义允许列表** — 新颖度 4/5 · 实用性 5/5 · 可迁移性 5/5
   从 87 个 operation 里挑 7 个 + 2 个折叠工具，其余 EXCLUDE。四个细节全都可迁移：路径正则**锚定**（否则 `/api/terms` 会顺带匹配 `/api/terms/{term_id}`）；tool description **覆写** spec 里的开发者文档式描述（tool description 是 prompt，不是 API 文档）；启动期 `missing_from_spec(spec)` 校验（上游改名会静默丢工具，转成启动失败）；**故意不给裸 schema 浏览**。

4. **覆盖率作为可回答性的确定性代理** — 新颖度 3/5 · 实用性 4/5 · 可迁移性 5/5
   不用 LLM 判断「我能不能答」，而是算「问题抽出的实体里有多少被语义层检索覆盖」，距离阈值 `DEFAULT_MAX_DISTANCE = 0.75`。配套 `_AMBIGUITY_MAX_GAP = 0.25` 区分「真歧义」（0.30 vs 0.32）与「自信的最优 + 勉强及格的次优」（0.10 vs 0.64）。这是廉价且可解释的置信度代理。

5. **「已知缺陷显式保留」的工程文化** — 新颖度 3/5 · 实用性 3/5 · 可迁移性 4/5
   `semantic/sql_attribute_suggester.py` 里 usage scorer 永远返回 0.0（正则 `^count_monthly_(\d{4})_(\d{2})$` 与写入端 `count_{month}_{year}` 永不相交），代码用 `.. warning:: **Known bug, preserved on purpose. Do not "fix" this in passing.**` 完整记录成因、后果、验证方式，并说明为什么「不修」比「顺手修」更好（改了会让排序行为变化，需配套评测）。

6. **「不确定即 PII」的保守分类 + 只用元数据** — 新颖度 3/5 · 实用性 4/5 · 可迁移性 4/5
   规则优先：模式必须描述**整个列名**（`customer_email` 命中，`user` + `name` 不命中）；规则判不了的才走 LLM，prompt 明写「If context is insufficient or you are unsure whether the column is PII, classify it as 'pii'」，代码里 `REVIEW` 状态被强制升级为 `PII`。且 classifier **只用元数据、绝不采样值**——避免把 PII 送进模型。

### 可复用的模式与技巧

1. **Meaning-Based Tool Allow-List** — 从大 API 面上按语义意义而非存储位置挑工具，其余 EXCLUDE；描述按「调用者的问题语言」重写；路径正则锚定；启动期校验 allow-list 与 spec 一致。适用：MCP server、LLM 工具注册、Agent API 网关。
2. **Runtime-Grounded Repair** — 用真实数据库的只读探针反证生成的 SQL，而非用声明元数据反证；只修近邻错误，无近邻即放行；探针走单一收口（只读 + LIMIT + 预算 + 关键词黑名单）。适用：text-to-SQL、SQL 修复、数据质量校验。
3. **Deterministic Coverage Grading** — 用「检索覆盖率 = 被覆盖实体数 / 实体总数」作为可回答性的可解释代理，替代 LLM 自评。适用：RAG 门控、成本前置判断。
4. **Relational Graph Traversal** — 多类边 UNION 成一张视图 + BFS + 每边携带确切连接列；视图放独立 `MetaData` 以免污染 Alembic autogenerate。适用：schema linking、数据血缘、实体关系抽取。
5. **Two-Phase Model Config Resolution** — `prefix_FIELD` → `DEFAULT_MODELS_FIELD` → 按 API key 前缀选组的内建默认；保留 legacy 变量名兼容。适用：多角色模型配置。
6. **Nested Scoped Concurrency Limit** — `limit_inflight` context manager，维护活跃 block 列表而非单个全局信号量，最严者生效，退出按身份移除。注释解释了为什么不能用栈式 save/restore：「两个重叠但不嵌套的 block 会以相反顺序退出……并永久留下一个陈旧的 bound」。适用：嵌套 fan-out 的 LLM 调用限流。
7. **Parallel Work / Ordered Commit** — 并行做无序工作（3 worker）+ 按规范序提交 + 可乱序取消的队列（`_OrderedCommitQueue`）。取消时 `skip()` 不等待就放弃轮次，因为「等待会让池 worker 被前面慢的表占住，而取消时所有排队表同时放弃，这个成本必须恰好落在要快速停止的时刻」。适用：批量生成共享命名空间资源。
8. **Bounded Semantics Correction Chain** — 三级 fallback（声明元数据 → LLM+向量语义相似 → 运行时值探针），每级有明确弃权条件（LLM prompt 明写「Do NOT guess. If unsure, return null」）；事后「零重叠即剪枝」清洗（`prune_disjoint_semantic_fks`）。适用：schema 匹配、实体链接、列语义推断。
9. **Same-Shape Failure Output** — 失败路径返回与成功路径**完全同构**的结构（同样键集，空值占位），消费方无需为失败写特例。适用：任何有「无法完成」分支的 Agent 流水线。
10. **Hard vs Soft Check Routing** — 语义正确性检查走硬上限（每轮都跑），尽力而为的检查走软上限（超 5 次放行），两者用不同 router。适用：带修复循环的 Agent 流水线。
11. **Structural Placeholder for Unknowns** — `catalog_table.pk` 与 `catalog_column.is_unique` 分开存并在 `find_table_key_columns` 里**显式分开返回**，不静默合并。适用：「多个来源的同一概念」的元数据建模。
12. **Deterministic-First, LLM-Fallback Rule Engine** — 正则规则判不了的才走 LLM；LLM 侧禁止使用敏感数据；不确定时升级为更保守的判定。
13. **Idempotent Single-Transaction Import** — `imported_id OR id` 匹配 + 整个导入一个事务，「a failure part-way leaves nothing behind rather than a catalog with half its semantics on top」。
14. **Baked-Code Comment as Engineering Ledger** — 把「为什么这样」写进代码注释而不是 issue，包括已知 bug、schema 陷阱、autogenerate 漂移原因。

### 关键设计决策

**决策 1：把「知识图谱」压成 Postgres 关系表 + 一个 UNION ALL 视图**
- **问题**：本体需要表达 Column → ColumnAttribute → Table → Column 的多跳关系和桥表，用于生成 SQL 时规划 join；但不想为图遍历单独运维一个图数据库（Illumex 早期用的就是 Neo4j）。
- **方案**：`dal/schema.py` 定义 `column__has_attribute`、`column__semantic_fk`、`column__foreign_key` 等关联表；`JOIN_PATH_EDGE_VIEW_SQL` 把四类边 UNION 成 `join_path_edge` 视图；`dal/attributes.py::_find_table_join_hops` 把有向语义关系转成无向表边，再用 BFS 搜最短路径，**保留每条边上的确切 join 列**。路径深度上限 `MAX_PATH_DEPTH = 30`（注释解释了「一个 hop 是 4 条边，4-hop 路径是 14 条边，上限 10 会静默返回无路径」）。
- **Trade-off**：牺牲图数据库的边属性扩展性与复杂图查询能力；换来零额外运维、事务一致性、「删一个 database 就是一条带 ON DELETE CASCADE 的语句」。
- **可迁移性**：**高**。

**决策 2：确定性 SQL 修复层，且故意不读声明的 schema**
- **问题**：LLM 生成的 SQL 有三类错误——filter 字面量不存在（大小写/拼写近邻）、JOIN 列是幻觉的（两列都存在、类型匹配、能返回行，**语法和语义都合法**，只是数据是错的）、JSONB 键路径不存在。第三类上游没有任何校验器会捕获。
- **方案**：见上文创新点 1。额外一条：数值尺度检查——字面量落在真实 MIN/MAX 之外但 `/100` 后落在区间内 → 判定为百分比/分数尺度错配，且**只作为 evidence 报告，不自动改写**。
- **Trade-off**：每次检查都要打数据库（`DB_PROBE_MAX_CALLS`/`DB_PROBE_MAX_ROWS` 预算）；且这些检查**默认不开**（`DB_PROBE_PROACTIVE` / `DB_PROBE_JOIN_PATH_CHECK` / `DB_PROBE_JSONB_PATH_CHECK` 三个 feature flag）——官方自己也把它当「高成本可选增强」而非默认路径。
- **可迁移性**：**高**。

**决策 3：探针执行器是单一收口，强制只读 + LIMIT + 调用预算**
- **问题**：探针会打生产库。一条 `UPDATE` 或一条全表 `SELECT` 就够出事。
- **方案**：`db_probe/executor.py::is_read_only_select` 做四重校验——必须以 `SELECT`/`WITH` 开头、内部不能有 `;`（拒多语句）、正则黑名单拦 `insert|update|delete|drop|alter|create|replace|truncate|grant|revoke|attach|detach|pragma|vacuum|reindex|merge|call|exec|execute|copy|into`、自动补 `LIMIT`；再加每题调用预算计数器。
- **Trade-off**：正则黑名单是启发式，不是 SQL 解析器。作者在注释里坦承：「per-dialect statement timeouts ... are the right tool once Phase 2 runs arbitrary model-authored SQL」——即当前只跑自己生成的探针 SQL，所以够用。
- **可迁移性**：**高**。任何「让 LLM 生成的 SQL 触碰真实数据库」的场景都应该抄这一层。

**决策 4：MCP 工具面 = 从 OpenAPI spec 生成的显式允许列表**
- **Trade-off**：手工维护的 allow-list 会在 spec 演进时需要同步（靠 CI 的 OpenAPI 漂移检查兜底）；且**故意不暴露写能力**，所以 agent 无法自主改进本体。
- **可迁移性**：**高**。「MCP/OpenAPI 工具面做 allow-list 而非 deny-list」是任何要把内部 API 暴露给 LLM 的项目的通用做法。

**决策 5：`check_answerable` 用纯算术覆盖率，不用 LLM 判定**
- **Trade-off**：实体抽取那一步仍是 LLM（不可避免），所以「无覆盖」的判定继承了抽取的误差；覆盖率是**启发式代理指标**，不是真值。
- **可迁移性**：**高**。

**决策 6：认证（certified）是人工治理标记，不参与运行时检索与 SQL 构造**
- **方案（代码验证）**：`certified` 字段（`_certified()` 工厂，`NOT NULL DEFAULT false`）存在 `term.name_certified`、`term.description_certified`、`column_attribute.certified`、`sql_attribute.certified` 上。检索侧 `dal/search.py::_certified_text()` 只把它算成 UI 三态徽章（certified/partial/pending）。**在 `auto_ontology/semantic/` 和 `auto_ontology/retrieval/` 全目录下 grep `certified` 只命中 `literal_check.py` 里一个无关的字符串示例**——运行时路径完全不读它。
- **Trade-off**：治理状态与执行行为解耦，代价是「人审定过的东西」在 agent 眼里和「机器猜的」权重相同。
- **可迁移性**：**低**（不宜照抄），但它揭示的模式「治理标记 vs 执行策略」值得警惕。

**决策 7：关系推断（SEMANTIC_FK）走三级 fallback 链**
- **Trade-off**：每一级都会引入误判。事后有 `prune_disjoint_semantic_fks` 做剪枝——「一个七位学区代码被当成旁边那个十四位 CDS code」是典型误判，剪枝规则是「值完全无重叠」且「源列全 NULL 也剪」，注释明说「real references in loaded data can still miss most of their target, so a low share is no proof」（只剪零重叠，低重叠留着）。
- **可迁移性**：**高**。

**决策 8：编译期并行处理、串行提交**
- **Trade-off**：一个慢表会挡住后面所有表的提交（顺序保证的代价）；但 LLM 部分仍全并行，墙钟时间主要取决于最后一个慢表。
- **可迁移性**：**高**。

**决策 9：模型配置用三元组，逐字段回退，且按 key 前缀分叉内建默认**
- **方案**：`utils/model_config.py::resolve(prefix, field)` 三级回退 `<PREFIX>_<FIELD>` → `DEFAULT_MODELS_<FIELD>` → 内建默认。内建默认按 API key 前缀选组：`sk-` 前缀走 inference-api（Claude），`nvapi-` 前缀走 integrate.api.nvidia.com（Nemotron 3.5）。
- **Trade-off**：三层回退的**实际生效值**不直观（要读代码才知道最终用了哪个模型）。
- **可迁移性**：**高**。

**决策 10：MCP 侧车不持有任何凭据**
- **方案**：`mcp/auto_ontology_mcp/server.py` 只知道 `AUTO_ONTOLOGY_API_URL`，用户通过 Auto-Ontology 自己的登录页签入，token 由客户端管理。文档原话：「a session can do exactly what the person behind it can do — a viewer gets a viewer's answers」。
- **Trade-off**：MCP server 不能离线工作、不能直连数据库；但身份与权限只有一处实现。
- **可迁移性**：**高**。

**决策 11：Next.js 作为唯一公网入口**
- **问题**：`server/identity.py::resolve_internal_user` 直接信任 `x-auto-ontology-user-id` 头，**该头没有独立认证**。
- **方案**：README 明写「FastAPI trusts the user identity the frontend forwards in the `x-auto-ontology-user-id` header, and the ingestion service's endpoints (ingest, delete, reset, compile) have no authentication of their own. Clients go through the web app on port 3000.」CORS 只允许 `localhost:3000`。
- **Trade-off**：这是**已知的、文档化的**信任边界，不是疏忽——但 3001/3002 若意外暴露公网，就是完整越权。
- **可迁移性**：**低**（部署形态绑定），但「把信任边界写进文档」这个做法值得抄。

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | Auto Ontology (9.1k) | WrenAI (18.1k) | Cube (21.2k) | Dataherald (3.7k) | Defog SQLCoder (4.0k) |
|------|---|---|---|---|---|
| 本体 / 知识图谱层 | 有（terms + 审定 SQL attributes + 桥表关系） | 无（语义建模层） | 无（指标目录） | 无 | 无 |
| 自动本体生成 | 有（表级 LLM 提取 + 三级 FK 推断 + 桥表 SQL attribute 生成） | 无，人工建模 | 无，治理模型全人工 | 无 | 不适用（模型侧） |
| 跨系统定义调和 | 有（tier vs plan 是 Illumex 老本行） | 无 | 无 | 无 | 不适用 |
| 认证工作流 | 有（certified / partial / pending 三态） | 无 | 无 | 无 | 不适用 |
| 确定性查询修复 | 有（字面量近邻 + JOIN 路径 + JSONB 路径，只读探针） | 无 | 无 | 无 | 无 |
| MCP 兼容 | 核心出口（9 工具语义允许列表） | 支持 | 部分 | 无 | 不适用 |
| 数据源广度 | 10 种引擎（Postgres/MySQL/Databricks/Snowflake/ClickHouse/Trino/Kyuubi/HeavyDB/DuckDB/SQLite） | 20+ | 多 | 多 | 不适用 |
| 开源治理 | Apache-2.0，**不接受外部 PR** | 开放 | 开放 | 开放 | 开放 |
| 维护状态 | 密集开发（v1.2.0，日均 4.2 commits） | 活跃 | 活跃 | 2024-07 后基本停更 | 活跃 |
| 标准生态 | **Apache Ossie 官方转换器** | 无 | 无 | 无 | 无 |

> 另一个参照物：Vanna AI（23.8k★）**仓库已归档**（最后推送 2026-02-02）。它是「纯 NL→SQL 库」形态的天花板信号——恰好佐证 Auto Ontology 选择「平台 + 上下文层」形态的判断。

### 差异化护城河

- **生态护城河（最硬）**：Apache Ossie 已为 auto-ontology 提供官方转换器，`pyproject.toml` 直接依赖它。Auto Ontology 已经进入**厂商中立**的语义模型标准生态——Cube、WrenAI 都没有。这是「标准先行」的护城河，比功能护城河更耐久。
- **技术护城河（真实但非排他）**：database-grounded repair 那套确定性校验器 + `join_path_edge` 最短路径图 + 桥表 SQL attribute 自动生成。竞争者可以抄，但抄要理解「为什么一个 hop 是 4 条边」这类细节。
- **信任护城河（被削弱）**：「certified」不参与执行，削弱了「人工审定让答案可信」的核心叙事；加上「不接受外部 PR」，社区信任无法积累。NVIDIA 品牌 + GTC 发布 + 合作伙伴名单（Palantir / Databricks / Snowflake / AWS / ClickHouse / SAP / ServiceNow / OpenSearch）部分弥补，但这是**商业信任**而非**开源信任**。

### 竞争风险

- **最可能的替代者不是另一个开源项目，而是「企业已有 Palantir Ontology 或自建语义层」这个选项**——如果企业已经在 Palantir 上，「业务概念层 + Agent 编排」是买而不是建。
- **短期最可能的侵蚀者是 Cube / WrenAI 加上各自的 MCP 适配层**。Auto Ontology 的接口优势会被稀释；它的真护城河在「本体自动生成 + 确定性修复」，而这两点 Cube/WrenAI 都不强做——但它们有社区和存量用户。
- **内部最可能的失败模式是评测数字拿不出来**（见下节）。

### 生态定位

**企业语义层的「参考实现 + 事实标准之一」**，三头位置：

1. 对 Agent 生态：是「让 Agent 理解企业数据」的**可选上下文提供者**（MCP 是接入点，不绑定任何 harness）。
2. 对 BI/语义层生态：是 **Ossie 标准的旗舰实现 + 转换器宿主**，与 Cube/dbt 形成「Ossie ↔ 各自模型」的桥。
3. 对 NVIDIA 战略：是 Agent Knowledge Foundation 的**业务概念层**，与 Nemotron Retriever（检索）、Kumo（预测）、CUDA-X（算力）分工。

战略判断：开源是**接口标准化**的手段（让 Agent 生态依赖 Ossie 而非依赖某家语义层），实现保持封闭是**有意的**。这不是 open-core，是「标准开源 + 实现封闭」。

## 套利机会分析

- **信息差**：**不存在**。9K star、HN 首页、GTC 发布会、第三方深度拆解文章都已有，信息差已被充分定价。真正的信息差在**代码层**——三条「文档 vs 代码」的裂缝需要读 `auto_ontology/semantic/`、`auto_ontology/retrieval/text_to_sql/`、`main.py` 才能挖到，这个项目值的钱在这里，不在 star 数上。
- **技术借鉴**：**极高**。database-grounded repair、meaning-based tool allow-list、coverage grading、ordered commit queue、nested scoped concurrency limit、same-shape failure output 六条可以直接搬到任何 LLM 数据系统的项目里。
- **生态位**：填的是「传统 BI 语义层（Cube/dbt，人工定义、面向看板）与纯 RAG-on-schema（Vanna/Dataherald，无本体层）之间」的空白——**面向 Agent 的、可自动构建的、带确定性校验的企业语义层**。
- **趋势判断**：方向正确（Agent 进入企业数据场景是确定性趋势），但**本体层不是终点而是新起点**——真正的竞争会发生在「本体如何与权限、血缘、治理编排合流」这一层，而 Auto Ontology 明确不做治理编排（只读 MCP、单向接受合作）。它的后发优势在于领域知识（Illumex 的语义层积累）+ 标准位（Ossie），劣势在于**开源治理模型封闭、社区贡献无法沉淀**。

## 风险与不足

### 一、文档与代码的三处硬伤（均有代码位置，已验证）

**A. 「认证」目前只是 UI 徽章，不影响任何运行时行为**
`certified` 字段存在于 `dal/`（存储与聚合）与前端（徽章与编辑），但**在 `auto_ontology/semantic/` 与 `auto_ontology/retrieval/` 全目录 grep `certified` 只命中 `literal_check.py` 里一个无关示例字符串**。运行时检索排序、SQL 构造、answerability 判定全部不读它。README 的三段式（Generate → Certify → Answer）目前只有 Generate 与 Answer 是真的，Certify 是装饰。这对财务/风控场景尤其要紧：人工审定的定义与机器猜的定义在 agent 眼里权重相同。

**B. 「问不了就别硬答」的承诺在最后一环漏了**
链路定位：`sql_parse_validation.py:1127` 在 intent 校验失败时把被拒的 SQL 记进 `path_state["last_intent_rejected_sql"]` → `main.py:316` 的 `_apply_last_deterministic_sql_fallback` 在两轮完整流水线都耗尽后，**把这个被 intent 拒绝过的 SQL 原样放进 `final_response["sql_code"]`**，只打一条 warning。这个 helper 只返回、不执行，所以不会真的跑错数据——但**用户会看到一段从未通过意图校验的 SQL 挂在答案里**，且「能答/不能答」的判断被这个 fallback 吞掉了。对应官方 issue [#257](https://github.com/NVIDIA/auto-ontology/issues/257)（Open，标注 partially fixed）。

**C. 单列主键 ≠ 列唯一性，直接损伤关系推断**
`catalog_column.is_unique` **只**由 `semantic/visit_enter.py` 的采样观测写入（基于 ≤1000 行样本）；声明的主键另存于 `catalog_table.pk`，`find_table_key_columns` 把两者**分开返回**（`{"pk": [...], "unique": [...]}`），从不合并。而 `semantic/semantic_fk.py:496` 的 VDB 候选过滤用的是 `where: {..., "is_unique": True}`——**只认观测唯一性，不认声明主键**。对应 issue [#272](https://github.com/NVIDIA/auto-ontology/issues/272)（Open）。

### 二、评测数字的可信度问题

官方从未公布任何可核实的 text-to-SQL 准确率增益数字。流传最广的 76.5% 来自评测仓库 PR #42（2026-10-13）：去掉一条无效 gold SQL 后 1533 题，本体组 76.5%（1172/1533）vs schema-only 组 70.4%（1079/1533），净 +6.1 点。问题在于：

- **实验非对称**：本体组多拿 5 条结构化 SQL 示例 + 预计算数据库值锚点，对照组无任何工具——少样本提示与本体贡献被混为一谈。
- **模型不一致**：评测用 Claude，主仓库默认 Nemotron。
- **分层收益倒挂**：Easy +5.6 / Medium +8.4 / **Hard 仅 +1.4**——恰好是最难的题上收益最小，而 Hard 才是企业场景。
- **上下文本身也是噪声源**：本体组「修好 161 道错题的同时改错 68 道原正确题」。

### 三、默认部署路径本身有 bug

issue [#440](https://github.com/NVIDIA/auto-ontology/issues/440)（Open）：官方托管 NIM 端点拒绝 `nvext.guided_json` 结构化输出信封（400），OpenAI `response_format` 返回空内容。**默认配置下 text-to-SQL 管线直接不通**——这与 issue #403（`docs/mcp.md` 仍称仓库为 NVIDIA-internal）一起说明「对外发布」的准备度低于「内部生产」的准备度。

### 四、运维成本随表数线性膨胀

约每表 3 次结构化 LLM 调用，1 万表湖仓估算约 28 小时编译期成本；叠加单题最多 16 次生成，限流暴露面大。官方评测记录里 1126 次 HTTP 调用中 747 次撞 429、37 条空 SQL，一轮 60 题得分仅 13.3%——为此 issue #262 才立项做「低调用次数」的执行策略并加了 5% 失败率熔断。

### 五、其他短板

| 维度 | 问题 |
|---|---|
| 前端测试 | **0**。`vitest 4.1.11` 已装但零测试文件，1448 行的 `SinglePageComposer.tsx` 无测试 |
| 开源治理 | **不接受外部 PR**（CONTRIBUTING.md 明写），Issue 走 integration request 模板。社区 star 无法转化为生态沉淀——19 位贡献者里只有 3 位外部 |
| 文档 | 无 ADR 目录，`docs/` 里没有一篇解释设计权衡的文档（权衡全散在代码注释里，对读者不友好）；无 CHANGELOG.md，变更史只能靠 Git 历史 |
| 示例 | 无 `examples/` 目录，示例以 README 问答 + Wide World Importers 种子脚本形式给出 |
| 安全 | 未配置 Vault 时连接凭据明文存 Postgres 目录表；`x-auto-ontology-user-id` 头无独立认证（依赖前端网关不暴露） |
| 发布流程 | 主分支仅 1 个 tag（`pre-main-merge-backup`），版本走 `release/vX.Y` 分支 + 手动 dispatch workflow，GitHub Releases 为空 |
| 错误处理 | 大量 `except Exception` + `logger.exception` 的降级路径（设计上刻意，因为「读失败应当降级而非抛出」），但确实会掩盖真实缺陷；`sql_parse_validation.py` 的 intent 校验仍是 LLM 判定，与「确定性校验优于语法校验」的哲学存在张力 |

## 行动建议

- **如果你要用它**：适合**已有企业语义层、想让 Agent 读懂数据、且愿意自己维护一份确定性校验层**的团队；不适合「想要开箱即用、稳定可托管的 NL2SQL 产品」的团队——因为版本发布走手动 dispatch、默认 NIM 端点下管线有 400 报错、前端零测试、认证不生效。上生产前必做三件事：①自建评测集，把「本体组 vs schema-only 组」的提示条件对齐，重测 Hard 题；②在 query graph 里补上 certified 读取逻辑（否则「审过就更可信」是假的）；③把 `x-auto-ontology-user-id` 换成带签名的断言，并把 3001/3002 锁在私网。若你的组织已有 Cube/WrenAI 语义模型，走 Ossie 导入比重建省事得多。
- **如果你要学它**：**重点看四个文件**——`auto_ontology/retrieval/text_to_sql/db_probe/`（整套确定性反证层，三千行，最值得抄）、`mcp/auto_ontology_mcp/tools.py`（语义允许列表，通用性最高）、`auto_ontology/dal/attributes.py` + `dal/schema.py` 的 `JOIN_PATH_EDGE_VIEW_SQL`（关系型存储上的图遍历）、`auto_ontology/utils/llm_invoke.py::limit_inflight`（嵌套并发限流）。另外通读 `pyproject.toml`——每条依赖 pin 后面都写了「为什么不能动」的理由，是被生产事故教育过的痕迹，比代码本身更能说明团队水平。
- **如果你要 fork 它**：三个最有价值的方向——①**把 certified 接进检索排序与 SQL 构造**，这是 README 已经承诺但没做的事，也是最小成本的信任修复；②**补前端测试**（vitest 已配好，缺口明显）；③**把 `join_path_edge` 抽成独立包**，它是这个仓库里可迁移性最高的技术资产，与 NVIDIA 语义层本身无关。

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | 未收录 |
| Zread.ai | 未收录 |
| 关联论文 | 无（官方从未发布 arXiv 论文，评测方法与数字全沉淀在 GitHub 的两个评测仓库 + PR/issue 历史） |
| 在线 Demo | 无官方托管 Demo；但有可本地一键复现的完整 Demo（Docker Compose + Wide World Importers 样例库） |

> 知识入口的缺失本身就是一条结论：**没有论文 = 没有可复现的方法论叙述 = 76.5% 这类数字只能靠扒 PR 核实**。这比「star 数」更能说明这个项目的真实成熟度。

### 关键 Issue 信号

1. [#257 Enforce material query constraints before execution](https://github.com/NVIDIA/auto-ontology/issues/257) — 揭示「语义正确性」这条产品主线在工程上并未被强制执行（详见「风险与不足」B）
2. [#262 Evaluate adaptive low-call Q&A execution](https://github.com/NVIDIA/auto-ontology/issues/262)（已关闭）— 揭示成本/可靠性的显式取舍：单题最多 16 条 SQL 换可靠性，代价是 1126 次调用中 747 次撞 429
3. [#272 Single-column primary keys are not reflected in column uniqueness](https://github.com/NVIDIA/auto-ontology/issues/272) + [#267 Model import ID and natural-name conflicts return HTTP 500](https://github.com/NVIDIA/auto-ontology/issues/267) — 揭示 Ossie/YAML 互操作路径成熟度不足，以及关系推断地基的缺陷
4. [#440 Text-to-SQL pipeline broken against hosted NVIDIA API](https://github.com/NVIDIA/auto-ontology/issues/440) — 默认部署路径下 text-to-SQL 管线直接不通
5. [#403 docs/mcp.md still says the repo is NVIDIA-internal](https://github.com/NVIDIA/auto-ontology/issues/403) — 文档滞后，与 #440 一起说明对外发布准备度不足
