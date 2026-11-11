# GitHub推荐：上下文压缩不是删，是能还原的折叠：billion-context 三个月 6778 星

> GitHub: https://github.com/ranxianglei/billion-context

## 一句话总结

billion-context 是一个跑在所有 AI 编码 agent 之前的上下文压缩代理：不靠「到阈值就重写整段历史」，而是让模型自己判断、只折叠已被当前任务消费掉的增量、并且**可逆**——被折掉的内容还能原样取回，同时靠 append-only 的前缀设计保住 94% 的 KV 缓存命中率；项目最有价值的部分其实不是这个压缩器本身，而是它附带的「**压缩判断规范（doctrine）**」——一份可版本化、可分节覆盖、跨模型迁移、并用 SMT 求解器做反例验证的公开工件。

---

## 值得关注的理由

- **它回答的是 2026 年最贵的一个问题**。上下文窗口从 128K 一路卷到 1M，但账单和延迟同步上涨，而且**扩窗只是把问题推后**——「200K 有界上下文就够用」这个命题如果成立，等于宣布了「买更大显存」这条路的边际收益递减。项目自报 4,843 个会话、174,327 次调用、18.76B 累计输入 token，是目前公开可读的长会话压缩实证里数据量最大的一份。
- **机制上它和所有主流方案都不是一回事**。Claude Code 的 auto-compact、Codex 的压缩、Mem0/Graphiti 的记忆层、AgentFold 的微调折叠——billion-context 的区分点是四条同时成立：**可逆 + 增量 + 保前缀缓存 + 免训练**。论文用「信息留存率 R_∞」作横轴把这条路线量化了：滑动窗口 R_∞=0，阈值压缩按 ρᵏ 几何衰减（4 轮剩 3–13%，8 轮剩 0.7–1.7%），而它的 fold 恒定在 ~1/8 且**不复利衰减**。
- **但它的宣传数字需要打折，这是最有价值的部分**。README 顶部挂的是「5 倍 token 减少」，而论文自己标注了三个限定：5.3× 是**相对假定的 80% 阈值压缩基线**的建模反事实（标 [A]），**200K 窗口上只有 1.2–1.8×**，**64K 以下净亏**（doctrine 的 ~2K token 固定开销占每 call ~25%）。更关键的是：头条的「re-read 降 63%」里有 **62% 被「零次压缩」的静默对照组独立复现**——也就是说现有证据支持的是「doctrine + ref 标签这套整包有用」，而不是「增量折叠机制本身有用」。作者把这个归因写进了论文正文却没写进 README，这种「自我拆台」的诚实度本身值得读。
- **它更稀缺的资产是工程治理范式**。作者把「一群 AI agent 同时改一个仓库」当成开发团队来治：18 条编号 Key Design Decisions 的 append-only 台账、`verif/` 用 SMT 求解器给真实 TypeScript 代码求反例（自动发现 7 个真 bug）、CI 强制「结构变更必须同 PR 更新文档+图+台账」、CI 失败统一收敛到单个 issue 并明令「禁止另开 CI issue，违例浪费整个舰队的算力」。这套东西**跟压缩毫无关系**，但对任何用 agent 写代码的团队都可直接迁移。

---

## 项目展示

![折叠（fold）布局总览](https://raw.githubusercontent.com/ranxianglei/billion-context/master/docs/how-it-works.en.svg)

> 折叠布局总览：tier-1 折叠消息区间 → tier-2 折叠 blocks → tier-3 折叠 tier-2，形成「散文上的 LSM 树」。

![整体架构图（storage schema v11）](https://raw.githubusercontent.com/ranxianglei/billion-context/master/docs/architecture/assets/architecture-current.en.svg)

> 整体架构：kernel（压缩引擎）→ 九条主机车道 → 代理 → 四条线路；host 永不直接改历史。

![Figure 1: 折叠布局实测 tier 比例（n=116 sessions）](https://raw.githubusercontent.com/ranxianglei/billion-context/master/paper/figures/fig1-fold-layout.png)

> 全仓最值得看的一张图：tier-1 占 92% 驻留空间、tier-2 7%、tier-3 <1%，而 **tier-2+3 承载了 37% 的历史**——分层压缩是真实在发生的，不是画饼。

![Figure 2: 留存率随压缩轮次衰减对比](https://raw.githubusercontent.com/ranxianglei/billion-context/master/paper/figures/fig2-retention.png)

> 核心论点的可视化：阈值压缩按 ρᵏ 几何衰减，fold 恒定在 ~1/8 不复利。

![Figure 3: 两个最长生产会话的每 call 上下文轨迹](https://raw.githubusercontent.com/ranxianglei/billion-context/master/paper/figures/fig3-marathon-trajectories.png)

> 12,049 次调用的上下文轨迹，实测呈现有界振荡带——这是「200K 够用」这个命题最直观的生产证据。

![Web 控制台：缓存命中率折线图 + 逐次归因](https://raw.githubusercontent.com/ranxianglei/billion-context/master/docs/cache-web-session.en.png)

> 内置 Web 面板（`http://127.0.0.1:8787/__bili/`）：缓存命中率、逐次归因、配置编辑器。

---

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/ranxianglei/billion-context |
| Star / Fork | 6,778 / 552（2026-08-06 建仓，三个月从 0 冲到 6,778，爆发型增长） |
| 代码行数 | 502,934（TypeScript 93.0%、JSON 4.4%、JavaScript 1.3%、Python 0.4%）；2,171 文件；注释率 22.2% |
| 项目年龄 | 3.2 个月（首次提交 2026-08-06，最近提交 2026-11-11） |
| 开发阶段 | 密集开发（97 天 8,535 commit ≈ **88 次/天**；近 30 天 4,208；600 open issue + 449 open PR） |
| 贡献模式 | **人类主导 + AI Agent 流水线代写**（机器身份占 58% commit，作者本人 45.3%，GitHub 口径 Top-10 占 92.2%，真正外部人类贡献者几十人量级） |
| 开发模式 | 职业项目（周末提交占比 32.3%、深夜 29.5%——agent 昼夜不停，人工只在工作日审阅合并） |
| 热度定位 | 大众热门（三个多月 6,778 星；npm 73 天发 4,404 个版本，约 62 万下载/周） |
| License | **MIT + 署名附加条款**（GitHub 识别为 `NOASSERTION`，非标准 SPDX；用户可见产品须声明使用并给链接） |
| 版本 | v0.1.213（211 个 tag、100 个 Release；子包 kernel 独立走 0.0.195） |
| 质量评级 | 代码 B+（内核 A / 宿主侧 C+）· 文档 A+ · 测试 A · CI A · 错误处理 B |

---

## 作者视角：为什么存在这个项目

### 创始人/作者背景

Xianglei Ran（`ranxianglei`），GitHub 账号 11.5 年（2015 注册）、198 粉丝、44 个公开仓库，无公司/位置/博客信息。**他不是压缩算法研究者，而是「AI agent 编排 + 工程治理」的实践者**——这个判断有硬证据：贡献者榜上除他本人外，`ework-agent`(1,991)、`awork`(856)、`ci-check`(857)、`ework-daemon`(43) 全是他自建的 agent 角色；仓库根目录的 `AGENTS.md`（51KB）是一份**给 AI agent 读的工程契约**，含 18 条编号 Key Design Decisions、Install-Lane & Update-Ownership Contract、Kernel Contract；`docs/auto-merge-guardrails.md` 从 1,543 条 issue/PR/评论里蒸馏出「让 ~90% 的 bugfix 可自动合并」的护栏，并明写「AI 工作难从作者区分——判断 AI vs 人工要靠 `[bot] 🏷` 前缀 + 标记，不能靠 authorship」。

他也不是在做单个项目，而是在经营一个**多仓库产品矩阵**：`billion-context`(6,778★，本仓) / `billion-context-pi`(284★) / `opencode-acp`(283★) / `acp-kernel`(51★，2026-10-23 已并入本仓 `kernel/`) / `ework`(19★)。矩阵的关系不是「产品线」，而是**一个内核的多个宿主适配 + 一个通用中间件**。

### 问题判断

**dogfooding 是真的，而且是最强的信号源**。作者把 billion-context 当作日常主力——论文 §5 写明是「单一专家用户」，Pi + OpenCode + ework 三个宿主、4.5 个月、174,327 次模型调用、18.76B 累计输入 token。这个数字背后是一个被具体症状推着走的开发过程：issue 编号一路排到 #6132，`#2176`（模型吐标签与异常终止）、`#933→#1039`（早期「传输层剥离标签」的 mask 本身变成静默数据损坏）、`#3011`（快照 409 → 克隆零折叠 → 首轮即 context_length_exceeded）、`#2313`/`#5682`（preflight 卡死/死锁），每一个都对应一次真实生产事故，修复都留在代码里。

**时机为什么是现在**——论文 §2 把设计空间梳理成六条路线，前四条在 2024–2025 都已有代表（MemGPT、LCM、AgentFold 等）。真正的新变量是 2025–2026 年 frontier 模型同时具备了两件事：**长上下文本身够长**（200K–1M 成为主流）**且** **足够强到能零样本执行一份判断规范**。前者让「压缩」从「保命」变成「经济性」，后者让「把判断权交给模型」第一次技术可行——这正是 doctrine 存在的物理前提。

### 解法哲学

作者的取舍高度一致：**凡是不影响「fold 是否正确」的部分一律交出去或明写不支持；凡是影响 fold 正确性的部分做到偏执。**

明确**不做**的：逐字审计/合规/取证类场景（论文自列）；多模态媒体的不可恢复载荷（`hasUnrecoverableMediaPayload` → 该消息拿 BLOCKED ref，永不折叠，因为折了就永久毁掉且无 restore 兜底）；把 model-driven 压缩的发明权据为己有（论文 §2(b) 明引 MemGPT [2310.08560]，坦承「model-initiated 动态压缩不是我们首创」）。

疯狂投入的：**字节保真**（thinking-family block 签名校验后绝不重写；tool-call arguments 必须 byte-exact 转发）、**缓存前缀稳定**、**降级而非猜测**（KDD #13：任何失步整轮回退 legacy，不猜）、**单点裁决**（KDD #12：`projectUnit` 是「是否可折」的唯一定义，recommend 与 apply 绝不各判各的）。

最核心的一条哲学是**把「判断」和「编排」彻底分开**。论文 §3.1 一句话：「the model writes summaries; the library orchestrates everything else」。kernel 拥有全部记账（ref 分配、block 生命周期、保护区、预算），模型只负责写摘要和拒绝。

### 战略意图

**几乎零商业化意图，且不打算变**。LICENSE 是 MIT + 署名条款，不是 copyleft、不是 source-available、不是 open-core；仓库里没有付费墙、没有企业版目录、没有 telemetry 后端（本地 SQLite/MySQL）。唯一的「商业痕迹」是自我更新的 3 分钟 registry check。

真正的战略资产是**信任**：6,778★、600 open issues、449 open PR、73 天 4,404 个 npm 版本，作者靠「CI 失败收敛到单一 issue + 自动合并护栏 + 每条 AI 评论自报模型出处 `(ai: <provider>/<model-id>)`」维持社区信任。这更像是「一个人 + 一群 agent 造出的大型开源基建」，而不是产品公司。

**最大的战略风险是上游收编**——如果 Claude Code / Codex CLI 把模型驱动的可逆折叠做进官方 CLI，这一层的差异化会被侵蚀一半。作者的护城河押在「训练无关、可版本化、跨模型迁移的 doctrine」上，而论文自己写明「controlled quality transfer untested」。这是最脆弱但也最独特的一块资产。

---

## 核心价值提炼

### 创新之处

按「新颖度 × 实用性」排序：

1. **增量 fold 的 LSM 分层结构**（新颖 4/5 · 实用 5/5 · 迁移 4/5）
   `CompressionBlock` 携带 `{tier ∈ {1,2,3}, generation ∈ {young,old}, survivedCount, directMessageIds, effectiveMessageIds, directBlockIds}`。tier-1 折消息区间，质量堆积后 tier-2 折 blocks，tier-3 再折 tier-2。`effectiveMessageIds` 传递性覆盖每条被摘要的原始消息，**血缘在任意次重压缩后依然存活**；`advanceSurvival()` 每次 sync 后把 `survivedCount` 加一，超阈值就把 `generation` 打成 `old`——这是 LSM 的 level 晋升的直接类比，论文自称「an LSM tree over prose」。边界要说清：实测中 tier-2 重蒸馏只触及 1,711 个 block 中的 60 个（3.5%），**分层的价值主要是「结构上允许」而非「天天在用」**。

2. **Compression Doctrine：把「判断」做成可版本化的 prompt 工件**（新颖 4/5 · 实用 5/5 · 迁移 5/5）
   五部分：两种失效模式（过度压缩/压缩不足）→ 单一判据「这段内容当前任务步骤还需要吗」→ 保护区（压缩调用硬保护、recent zone ~5 条/5K 底线、首末用户消息、assistant 不注入 ref tag）→ KEEP/DROP 摘要工艺规则 → 六条交互机制。
   - **KEEP**：带行号路径、签名与承重代码行、精确错误串、**带理由的决策**、精确值、目标演化、message refs
   - **DROP**：结果已提取的冗长日志、重复读取、**保留教训的死胡同探索**、通往结论的过程
   - **优先级**：目标 > 决策+理由 > 产物 > 结论 > 教训
   落在 `kernel/DESIGN-prompts.md` + `kernel/src/compression-rules.ts`，随内核版本走，宿主可分节覆盖（replace/remove/default 三态），核心四条规则覆盖需显式 `acknowledgeRisk` 闸门。**它同时是研究工件**：论文 §9 提出 doctrine → SFT 权重内化，因为 doctrine 机械上就是 (context, task) 对上的一个标注函数，已有生产日志可作 curriculum。

3. **不给模型看填充率**（新颖 4/5 · 实用 5/5 · 迁移 5/5）
   `kernel/src/nudge-text.ts` 的 `renderNudgeText` 只渲染「指令 + 候选区间及其真实 token/消息/tool-text 组成」，**从不出现百分比**。理由：告诉模型「已用 20%」，它会锚定「看起来很健康」而拒绝压缩。措辞是「保持上下文精简的效率提示」而非「溢出警告」；模型可以拒绝，且**拒绝是质量阀门不是失败**。这是全项目最值得抄的一条——它揭示了一个通用陷阱：给模型无法校准的标量会让它锚定而非判断。

4. **decompress-to-file：用文件系统承载全文以保住 KV 前缀**（新颖 3/5 · 实用 5/5 · 迁移 5/5）
   模型想看被折掉的原文细节时，最自然的做法是 inject 回消息历史——但这直接作废整个 KV 前缀缓存，一次回溯就把攒下的 94% cache read share 清零。billion-context 改为写盘，上下文里只留路径指针。**很多团队的「回看细节」实现会直接 inject 历史从而静默毁掉缓存**——这条值得立刻抄。

5. **side-channel decision call：用可缓存前缀的一次廉价 JSON 问答取得模型否决权**（新颖 4/5 · 实用 4/5 · 迁移 5/5）
   `src/nudge-decide.ts`：复用同一会话的已缓存前缀 + 极小输出预算（200 token）+ 15s 超时，问模型「现在压对当前任务净有益吗」，只接受一行 JSON。严格解析（半成形即失败）、range 必须完全包含在 live range 内、失败阶梯（连续 3 次失败后下一轮降级为 advisory nudge 并重置）、**必须剥离 reasoning 字段**（#3004：27B 模型的 reasoning 会在 200 token 预算内烧光导致解析为空）。

6. **SMT 反例验证 + 真代码回放 + 五条「无作弊规则」**（新颖 5/5 · 实用 3/5 · 迁移 4/5）
   `verif/` 把 kernel 里真实的 TypeScript AST 翻译成 SMT 约束（分支用 ITE 值合并不枚举路径），优先 cvc5（经 Python）回退 z3 二进制，**witness 必须在真实 kernel 代码上复现**，不复现 = 翻译器漂移 = 警报而非通过。无作弊规则五条：只调真入口函数；不变量必须是通用性质（幂等/单调/append-only 稳定），绝不在 bug 行号附近写断言；反例必须回放真代码；port 是公开接缝但本地函数名与 import 的真实函数永远优先；每个 SAT 证明必须配一个「已知修好/排除后 UNSAT」的负控制，证明判官不是永真式。**已自动发现 7 个真实 bug**（#3691/#3769/#3676/#3805/#3945/#4052/#4106-4107），其中 #3945 是通用输入 harness 在任意输入下自己发现的新形状。实用性打 3 分是因为它是**有界模型检测**（K=8、N=8）而非完整证明，且无求解器环境时测试自动 skip。

7. **统一身份采集缝 + 自包含适配器 + 整轮退化**（新颖 3/5 · 实用 5/5 · 迁移 5/5）
   7 个 `src/identity-*.ts` 共约 34.7K 行（`identity-harvest.ts` 14.7K 是共享注册表），即**每客户端平均 3–4K 行**。handle 入口按「body 字段 > 盖戳头 > 采集」的优先级取一次快照，消费者只从这道缝取数；适配器自包含（自己的配置目录解析、行过滤、对齐规则）且**整轮退化**——任一环节不判定则整轮回退接线前路径，**绝不做部分映射**。更诚实的是 `identity-sources.ts` 的注释直接列出了**哪些客户端故意不做适配**（crush 的 wire key 是 hash 无法 join、gemini-cli 只有安装级 id、hermes-agent 零 per-session 信号、aider/kimi 无可用 id——content-hash 就是它们的最优解）。

8. **prefix-affinity：把 radix prefix caching 从 KV 层上提到身份层**（新颖 4/5 · 实用 4/5 · 迁移 4/5）
   对完全无状态的客户端（每次重放全历史），把历史哈希成 **append-only 链**（`hᵢ = sha256(hᵢ₋₁ ‖ msgᵢ)`），解析到「存储链是最长严格前缀」的那个 session。**仅头锚定**、截断即 fork、**刻意不分区**（protocol/凭证/上游都会中途变，分区会在用户还在说话时孤立状态）、wire-neutral 投影使协议切换不破链。

9. **snapshot render（快照即会话）：出站前缀由服务端正史渲染**（新颖 4/5 · 实用 4/5 · 迁移 3/5）
   绑定 session id 且统一存储可读的会话，出站**前缀**由服务端按 `seq` 渲染，尾巴保持客户端逐字；任何失步整轮回退 legacy，**永不复活已覆盖行**；观测（`reconcileFoldCoverage`）与渲染**刻意分离**。AGENTS.md 原话：凡讨论「覆盖 id 失配 / destroyed 误诊 / 断缓存」类 bug，先问是否 D 车道——**那类病理在 D 上结构性不存在**。

### 可复用的模式与技巧

1. **「一份裁决，两个消费者」**——把「资格判定」抽成唯一函数，recommend 与 apply 都调它，且 apply 抛出的是同一个错误的字节副本；筛后不重合并以避免震荡；状态标注只做加法。适用：任何有「提议 vs 落地」两条路径的系统。
2. **「降级而非猜测」**——身份匹配、快照渲染、消息指纹三处统一采用「任一环节不判定 ⇒ 整轮回退 legacy」，并把降级写成显式分支而非异常。适用：任何有灰度匹配的系统。
3. **「信封 id，不上模型线」**——宿主稳定 id 作为私有字段在宿主↔中间件间传递，四种传输载体全部在转发上游前剥除；不可信时静默降级为内容 hash，但**单维度 miss 不得级联成全量 unfold**。适用：所有 agent 中间件 / 协议适配层。
4. **「不给模型无法校准的标量」**——不披露填充率/相似度/预算百分比，改用「真实尺寸 + 任务相关判据 + 拒绝权」。适用：任何向模型暴露系统状态的 prompt（RAG 检索别只给相似度分数、agent 规划别只给剩余预算百分比，同理）。
5. **「外置大对象而非内联」**——全文写盘、上下文只留指针，保住 prefix cache。适用：所有带 prefix cache 的 agent 运行时。
6. **「纯函数节点流水线 + 单一写者」**——每个节点一个关注点，ref 映射只有一个写者，tag 在最后统一渲染，禁止中途直改历史。适用：多阶段文本/数据变换管线。
7. **「统一采集缝 + 自包含适配器 + 整轮退化」**——N 个异构上游 → N 个自包含文件 + 一道统一缝；新增上游 = 一个文件 + 一行登记 + 一行文档。适用：异构客户端网关。
8. **「反例必须回放真代码」的形式化验证**——真实代码翻译成 SMT + witness 回放 + 负控制 + 诚实降级登记 + 有界→归纳升级。适用：有隐性字节级不变量的系统。
9. **「文档同 PR 的 CI 闸」**——CI lane 强制全 `src/` 覆盖架构文档，文件级地图声明「会漂移，加删文件时重新生成，别信旧副本」。适用：大项目文档防腐。
10. **「把 agent 群体当开发团队治理」**——单点 CI 汇报 issue（禁止另开）、红即继承性失败（等 master 修复后 rebase，禁止长时间自行排查）、每条 AI 评论自报模型出处、一 issue 一主题、完成 = 证据。适用：多 AI agent 协作仓库。

### 关键设计决策

**决策 1：把压缩内核做成零依赖、平台无关的纯函数库**
- **问题**：同一套压缩逻辑要服务 20+ 客户端、4 种 wire 协议、2 种压缩模式；内核一旦碰 host API（文件系统、网络、宿主对象）就无法复用与测试。
- **方案**：`kernel/` 内联本仓（`"acp-kernel": "file:./kernel"`），契约是 `processTurn(state, messages, config) → (state', rendered, effects)` 单一纯函数入口。Kernel Boundary 七条结构性不变量（零依赖/平台无关/id 不可复用/wire 格式/无损往返/protected 硬排除/节点顺序），CI 强制 `kernel-change:` 声明 + 版本号 bump + golden pin + **永不自动合并**。
- **Trade-off**：牺牲「内核可独立快速发版」的灵活性（KDD #5 明说为此合并了两个仓库并让旧 repo 冻结），换来「改内核必须先论证宿主侧解决不了」的强制审查门。代价是跨仓发布顺序成了经典 bug 源（#772）。
- **可迁移性**：**高**——「核心算法零依赖、宿主适配外置、破坏性改动需预审」可直接套到任何要嵌入 N 个异构宿主的系统。

**决策 2：host 永不直接改历史，全部变更经九段式纯函数流水线**
- **方案**：`kernel/src/compress.ts` 的 `buildNodes()` 固定节点序列（`reconcile-live-ids → stamp-timestamps → assign-refs → sync-blocks → prune → … → recommend → nudge-inject → emergency-truncate → render-refs`），`PipelineNode` 只有 `{name, run(io,ctx), enabled?}` 三个字段。**ref 映射只有一个写者（assign-refs），tag 在最后统一渲染（render-refs）**——注释明说这消除了「双真源」导致的 `stripHallucinations` 补丁。
- **Trade-off**：节点顺序成了隐性契约（被 golden pin 钉死），改动顺序需极强理由；`NodeEffects` 事实上成了跨节点通信总线，类型上有点松散。
- **可迁移性**：**高**。

**决策 3：growth-gated nudge（需求侧触发，只压已消费增量）**
- **方案**：三个门同时成立才注入 nudge（context floor 默认 0.45 + 自上次压缩以来的 growth + 最小区间尺寸）；门限被压到 floor 以下时需求降到 45%（50K → 有效 22.5K）。KDD #8 特别规定 **nudge 节奏固定 50K，不随窗口大小缩放**（窗口百分比缩放被刻意移除）。
- **Trade-off**：论文 §8.1 的关键反例——**确定性引擎臂在重复性负载上便宜 37%，但在 phase-structured 负载上全面反超默认配置**；放松三门（BC-extreme）在重复性负载上成本接近确定性臂、探针分数最好（80/84 vs 78/84），却在 phase-structured 负载上探针掉到 75.7%、执行错误 3 次。即：**可泛化的是「任务条件化的时机与范围判断」，不是压缩频率本身**。另外固定 50K 意味着**小窗口用户默认配置会过度触发**（64K 窗口 50K 门限 → 每轮都触发）。
- **可迁移性**：**中高**（机制可迁移，具体取值别抄）。

**决策 4：两条压缩模式、两种摘要载体**
- **方案**：`pluginMode`（`x-bili-plugin` 头）：宿主拥有压缩权，摘要载体 = **tool call**；`proxy mode`：代理服务端执行，tool call 是 ephemeral，载体 = **`acp_summary` message**，kernel 渲染为 system 后由 `systemToUser` **重新配音为 user** 留在锚点位置——理由有二：兼容 SGLang「恰好一个 system 在 index 0」的硬约束（#377），且头部 system 字节保持稳定以保住 prefix cache。模式按请求判定、按 session 粘滞，**只允许升级**。
- **Trade-off**：**每次改动都必须双模式推演**（`docs/architecture/pipeline.md` 明写「correct-in-one-mode can break the other」）；模式粘滞 + 只升级意味着一生只有一次选择机会，选错长期受罚。
- **可迁移性**：**中**。

**决策 5：资格判定与执行共用单一投影（KDD #12）**
- **问题**：若「推荐哪些区间可压」和「实际执行压缩」是两套代码，就会出现 advertise→reject 循环（`refold.ts` 注释直接点名 #3236 这个失败家族）。
- **方案**：`kernel/src/unit-projection.ts` 的 `projectUnit()` 是唯一裁决点，apply 侧抛出**字节相同**的同一个错误；recommend 侧用同一函数重筛最终合并后的单元，fatal 单元降级为 gap（**筛后不重合并，避免震荡**）。更狠的是 KDD #12 要求判断必须跑在 `applyCompression` 实际执行的那个数组类上——所以 `processTurn` 专门收一个 `applyView` 参数。
- **可迁移性**：**高**——「一份裁决代码，两个消费者，禁止二写」是通用的正确性工程手法。

**决策 6：降级而非猜测（KDD #13 等多处契约）**
- **方案**：snapshot render 任何失步整轮回退 legacy、永不复活已覆盖行，观测与渲染**刻意分离**；`src/prefix-affinity.ts` 匹配是**仅头锚定**，客户端截断历史 → 直接 fork 新会话（#316 的「尾窗重挂」被移除，因为它分不清「截断重放」与「引用共享内容的新对话」），并且**刻意不做分区**（#286 的教训）；`identity-claude.ts` 尾部精确计数对齐 + 4 个边界位置角色抽查，失败则**整轮降级为 null**（「whole-turn or nothing」）。
- **Trade-off**：降级路径本身也要写、要测、要维护；某些场景用户会看到「本来能识别却没识别」的体验损失。
- **可迁移性**：**高**——极其通用的分布式/缓存系统原则。

**决策 7：消息身份用「信封」承载，绝不出现在模型线上**（KDD #11 + KDD #17）
- **方案**：三层裁决 **msgid > 顺序 > hash**。宿主 msgid 作为**私有信封字段**上行（只存在于宿主↔bili 之间）；账本主键是 `(session_id, msg_id, content_hash)` 三元组；「全有全无」——筛查失败或长度不符则静默降级为内容 hash；hash 是**逐格硬门但无全局否决权**（任何单维度 miss 不得级联成全量 unfold）；四种传输载体全部在转发上游前剥除。KDD #17 甚至规定校验规则有**六份镜像副本**（宿主 bundle 禁 import server 模块的结构性约束），并用 `tests/msgid-rule-parity.test.ts` 钉死每份副本的判决。
- **Trade-off**：六份规则副本是**刻意的技术债**，靠 parity test 兜住。
- **可迁移性**：**高**。

---

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | **billion-context** | magic-context | MemGPT / Letta | Zep / Graphiti | Mem0 |
|------|---------|--------|--------|--------|--------|
| 部署形态 | **中间件代理**（不改 agent 运行时） | 常驻记忆层（装上就忘） | 框架/运行时（要重写 agent） | 外挂记忆层 | 通用记忆层 + MCP |
| Star | 6,778 | 2,507 | 25,420 | 5,004 / 32,748 | 68,817 |
| 可逆性 | **有**（decompress / decompress-to-file / search_context + 血缘传递） | 无显式 fold 动作 | 分页换出换入 | **写入时即不可逆** | lossy + 异步写入 |
| KV 前缀缓存 | **一等公民**（append-only + 94% 命中实证） | 无公开论证 | 无论证 | 不涉及 | 不涉及 |
| 触发方式 | **模型自主 + growth-gated**（拒绝权） | 模型自主 | 模型自主 | 写入即抽取 | 后台自动 |
| 训练依赖 | **免训练**（doctrine 可版本化） | 免训练 | 免训练 | 抽取需 LLM | 抽取需 LLM |
| 论文/数据 | 仓库内 preprint + 174,327 次调用实证 | 无 | 学术完整 | 生态成熟 | 生态最广 |
| 维护活跃度 | **极高**（88 commit/天） | 弱 | 中 | 高 | 高 |

> 另有 `headroom` / `Context Mode`（payload 级压缩）——第三方聚合站报 ~79.2K / ~33.7K star，但 `gh api` 查 `neulab/headroom`、`sshar512/context-mode` **均 404，无法核实**，本报告不把它们当作有效竞争情报。

### 差异化护城河

**三层，强度递减：**

1. **工程层（最强，但会被追平）**——增量折叠 + append-only 前缀 + 可逆 + 20+ 客户端适配 + 4 种 wire 协议 + prefix cache 实证。这是 19 万行代码 + 39 万行测试 + 4,404 个 npm 版本堆出来的，追平需要同等工程量。但工程护城河的本质是「时间」，而这个领域正在被加速。
2. **方法层（最独特）**——**doctrine 作为可版本化、可分节覆盖、跨模型迁移的判断规范 + SMT 反例验证的决策核**。这是全项目最难被抄的部分，要求「既懂压缩语义、又能把它形式化」的复合能力。论文自承「controlled quality transfer untested」，但在训练无关的判断规范这个赛道上，它**目前是唯一公开可读的、足够完整的工件**。
3. **产品层（最弱）**——单一维护者、600 open issues、449 open PR、无第三方评测方、无商业化能力。**这是项目最大的结构性风险**：护城河再深，池子里的鱼太少也钓不成大鱼。

### 竞争风险

- **最大风险是上游收编**。如果 Claude Code / Codex CLI 把模型驱动的可逆折叠做进官方 CLI，差异化的一半被侵蚀。但这里有个反直觉点：官方 CLI 做折叠时很可能采用「阈值 + 固定粒度 + 无 doctrine」的简单方案——而那恰恰是论文 §8.1 证明**质量更差**的方案（确定性臂在 phase-structured 负载上全面反超、方差高 4–7 倍）。**真正的机会不是比官方做得更多，而是比官方做得更好且可解释。**
- **次风险是自身复杂度反噬**。2.6 万行 kernel + 16.8 万行 src 已经出现「核心文件超长」问题：`launcher.ts` 7,786 行、`plugin.ts` 5,254 行、`server.ts` 4,826 行、`persist.ts` 4,469 行、`preflight.ts` 3,264 行。作者自己在 `docs/auto-merge-guardrails.md` §3.1 列了「重灾区」清单。**2.6 万行的内核是资产，16.8 万行的宿主层是负债。**

### 生态定位

「**agent 上下文基础设施**」，不是「记忆产品」：

- 与 Mem0 / Graphiti 是**可叠加**的（跨会话记忆 vs 单会话折叠）
- 与 magic-context 是**形态竞争**（中间件 vs 常驻记忆层）
- 与 MemGPT / Letta 是**部署层级错位**（中间件 vs 运行时框架）
- 与 headroom / Context Mode 是**量级不同**（会话级 vs payload 级）

论文 §2 用六个技术家族做了穷举定位（训练侧表示压缩 / 外部记忆 / 训练式自管理 / 引擎侧无损递归 / 生产 harness / 压缩代价评估），并指认最近邻是 LCM（引擎侧无损递归）与 AgentFold（训练式自管理）。

---

## 套利机会分析

- **信息差**：星数维度已充分定价（6,778 星、三个月爆发、npm 60 版本/天），**技术密度被低估**。真正稀缺的三样东西不反映在 star 上：① 4,843 会话 / 174,327 次调用的生产纵向数据 + 随代码开源的论文（论文按 [V]/[A]/[P] 自标证据等级，这种写法在预印本里罕见且诚实）；② agent-first 工程治理范式（18 条 KDD + SMT 反例 + 文档同 PR 强制度 + CI 总控 issue）；③ 「可逆增量 + 保前缀缓存」这一窄位的独占性。**但不是「被低估的潜力股」——它已经是大众热门，且 600 open issues 说明这是重工程项目，不是精品仓库。**
- **技术借鉴**：**doctrine 本身可以脱离这个工具直接抄**。`kernel/DESIGN-prompts.md` 里的 KEEP/DROP 分类、单一判据、「不披露比例」原则、保护区定义——直接进你自己的 agent 提示词设计。其次是「decompress-to-file」（别 inject 回历史毁缓存）、「降级而非猜测」、「一份裁决两个消费者」、`verif/` 的 SMT 反例方法论（这部分与压缩无关，纯工程可迁移）。
- **生态位**：填补了「**单会话内的可逆上下文管理**」这个空白——跨会话记忆层有 Mem0/Graphiti，payload 压缩有 headroom/Context Mode，训练式自管理有 AgentFold，但「不扩窗、压增量、能还原、保缓存、免训练」这一组合在开源里几乎无直接竞品。
- **趋势判断**：符合趋势且明显增长（三个月 0 → 6,778 星，npm 62 万下载/周）。**后发优势在两处**：① 它站在 2026 年 frontier 模型「足够强到能零样本执行判断规范」的窗口上——这个前提 2024 年不存在；② 它的护城河押在「训练无关的 doctrine」上，恰好绕开了 AgentFold 那条需要 30B 微调的路。但趋势的**反面**同样清晰：如果上游把模型驱动的可逆折叠做进官方 CLI，这一层的差异化会被吃掉一大半。

---

## 风险与不足

1. **所有性能数字都是作者自报，且头条数字最不可信**
   README 顶部挂「5 倍 token 减少」，但论文 §7 自己写明：5.3× 是**相对假定的 80% 阈值压缩基线**的建模反事实（标 [A]），那个基线是**从公开 CLI 文档推断的假设**，语料里没有非 BC 会话超过 205K；**200K 窗口上该模型只预测 1.2–1.8×**；64K 以下本项目**净亏**。附录 B 另标：28.6B token / 106 天的单会话上限是**模拟外推，约为实测最大会话的 19×**。
   更关键的是**头条的「re-read 降 63%（2.7×）」被「零次压缩」的静默对照组复现了 62%**（128K 窗口单次运行：模型调用少 14%、re-fetch 少 62%、探针分数完全相同）。论文正文做了这个归因（罕见的学术诚实），**但 README 顶部没有**。读者应把「压缩机制本身」和「doctrine + ref 标签」分开看——前者目前证据很薄。

2. **「独立第三方基准」这个标签站不住**
   `benchmarks/third-party-1500/` 自称「Independent Third-Party Evaluation」，但它在**作者自己仓库里**、无评测方署名、无运行日期，且 full-context 基线臂在 MemoryAgentBench 上 **199/199 全部失败**（因超窗）却**未声明模型窗口多大**——读者无法判断一个合适的长上下文配置是否也会失败，于是那个 71.1% 的成本节省无法解释。论文附录 A 也自认「实验 harness 与 deployment 数据尚未公开」。**引用时应标注为「作者自评基准」。**（值得肯定的是它的负面结果也照报：MemoryAgentBench 上 BC 的 needle QA 从 69.0% 掉到 27.0%。）

3. **「可逆」这个卖点有一半在实践中落空**
   论文 §8.1 明确写：模型**不会自发调用恢复工具**（「spontaneous tool adoption is zero at this model scale」）。恢复在被明确指示时有效，但模型不会自己想到。更尖锐的是 `acp-kernel` #474：**弱模型折叠时会手工抄写标识符并抄错**（`ses_` + 24 字符只抄了 12 字符），「Continue subagent」直接失效——**恰好破坏了压缩本该保护的那种交接能力**。

4. **License 不是标准 MIT**
   实际是 **MIT + 署名附加条款**（用户可见产品须声明使用并给链接），GitHub 识别为 `NOASSERTION`。引用时应引 LICENSE 原文而非 README badge。

5. **安全默认值不够保守**
   TLS MITM 模式意味着**代理可见全部 prompt、代码、工具输出与 API key**；Docker 模式绑 `0.0.0.0` 且**无认证**；默认每 3 分钟查 npm 自动更新。项目有 `src/tunnel-guard.ts` / `src/log-mask.ts` / `src/private-host.ts` 等防护，但「你的全部代码经过一个 MITM 代理」这件事本身是最大的信任门槛，README 提及但不充分强调。

6. **成熟度叙事与工程面互相拉扯**
   论文主张「4.5 个月生产实证、零窗口违规、94% 缓存命中」，工程面却是 **600 open issues + 449 open PR + 73 天 4,404 个 npm 版本**，外部评测甚至直接说 master 分支「可能处于损坏状态」。这两个叙事**同时为真**：一个 agent 群体以极高速度推进必然留下大量未收敛的 PR；同时它的自动化护栏（verif、CI、golden pin）确实是同规模项目里少见的。**读者不应把论文的生产实证读作「工程成熟」，也不应把 600 open issues 读作「质量差」。**

7. **宿主侧代码质量有明确短板**
   `src/` 侧 1,874 处 try/catch 但**零个 `Result<T>` 类型**（错误全靠异常 + 字符串 reason，跨模块断言容易脆）、`any` 出现 59 处（AGENTS.md 明令「no `as any`」但并非零）、核心文件严重超长（见上）。`refactor` 类 commit 仅占全量 1.3%——**作者几乎不主动重构**，改动以打补丁为主，代码里堆积了大量一次性特判。

8. **明确的不适用场景**（论文自列）：逐字审计 / 合规 / 取证 / 约束并集超出摘要容量的多约束重构。

---

## 行动建议

- **如果你要用它**
  - **适合**：每天用 Claude Code / OpenCode / pi / Codex 跑长会话的**个人重度用户**，且确实有「这个会话已经烧掉 20 万上下文、想换任务但不想重开会话」的痛感。窗口 ≥200K、缓存计费显著（cache read 单价通常是 input 的 1/50，本项目实测读比 9.7:1）时收益才显著。
  - **不适合**：≤64K 窗口的模型（**净亏**）；需要逐字审计/合规的场景；不能接受本地 MITM 代理的团队；希望「一键装上就忘」的用户（magic-context 形态更自然）。
  - **姿势**：**pin 版本**（0.1.x 会以破坏性变更升 patch，语义化版本号在这里只是单调计数器）；**关掉自动更新**；Docker 模式**绑 localhost**；先用 `--passthrough` 排障；每接一个新客户端记得**清掉它自己的原生压缩**（双压缩器互斥是持续税负，见 #2411 / #809）；nudge 阈值按你的窗口重算（默认固定 50K 是为 1M 级窗口设计的）。
  - **验证方式**：别信 README 数字，去看论文的 **Appendix B 主张登记表**（标 [V]/[A]/[P]）和 **§8.1 的三条 scope note**，再去 Web 面板看**你自己的**缓存命中率折线。

- **如果你要学它**
  - **优先级最高**：`paper/` 中英双版（这是全仓最高信息密度的文档）→ `kernel/DESIGN-prompts.md`（doctrine 原文，脱离工具也能抄）→ `AGENTS.md` §Key Design Decisions（18 条工程契约，每条带 operative consequence）→ `verif/README.md`（形式化验证方法论，**与本项目主题无关但可独立迁移**）。
  - **其次**：`kernel/src/compress.ts`（节点编排）、`kernel/src/unit-projection.ts`（单点裁决）、`kernel/src/protected.ts`（保护区）、`src/prefix-affinity.ts`（身份层前缀链）、`src/nudge-decide.ts`（旁路否决权）、`src/identity-harvest.ts`（统一采集缝）。
  - **不要**从 `src/` 的 19 万行开始读——那是被 20+ 客户端和 4 种 wire 协议的历史包袱撑起来的，读不出设计意图。先读 kernel（2.6 万行，那才是设计）。

- **如果你要 fork 它**
  - **值得做的方向**：① **跨模型的质量验证**——论文自承「controlled quality transfer untested」，这是最明确的空白；② **把 doctrine 的 KEEP/DROP 规则落成可评估的 rubric**（当前只有 prompt 级规则，没有自动判分）；③ **拆掉宿主侧的巨型文件**——`launcher.ts` 7,786 行 / `plugin.ts` 5,254 行是 review 成本的主要来源，也是 `refactor` 仅 1.3% 的直接后果；④ **补一个真正的第三方基准**——把 `benchmarks/third-party-1500/` 的 harness 和原始数据公开，并**声明基线臂的模型窗口**，这是当前最容易被攻击的点；⑤ **模型自发的恢复工具调用**——论文 §9 的「doctrine → weights」路线，或退一步用 scaffold 强制模型在合适时机调用 `decompress`。

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | [deepwiki.com/ranxianglei/billion-context](https://deepwiki.com/ranxianglei/billion-context)（探测时返回 429 限流，未能确认收录状态） |
| Zread.ai | [zread.ai/ranxianglei/billion-context](https://zread.ai/ranxianglei/billion-context)（探测时返回 403，未能确认收录状态） |
| 关联论文 | **无 arXiv**。论文是仓库内 preprint（paper-as-code），随代码 MIT 开源且是「living document」：[Model-Driven Incremental Hierarchical Compression: Training-Free Multi-Generational Context Management for Long-Lived Coding Agents (Preprint v0.2, 2026-09-07)](https://github.com/ranxianglei/billion-context/blob/master/paper/model-driven-incremental-hierarchical-compression-training-free-multi-generational-context-management-for-long-lived-coding-agents.md)（中英双版） |
| 在线 Demo | **无托管 Demo**。本地代理 + 内置 Web 面板 `http://127.0.0.1:8787/__bili/`（会话列表 / 缓存命中折线图 / 逐次归因 / 配置编辑器 / 上游连通性测试） |
| 外部深度评测 | [andrew.ooo 的评测](https://andrew.ooo/posts/billion-context-review-context-compression-proxy) · [theterminal.space 对第三方基准标签的质疑](https://theterminal.space/ai/billion-context-compression-proxy-third-party-benchmark) |
