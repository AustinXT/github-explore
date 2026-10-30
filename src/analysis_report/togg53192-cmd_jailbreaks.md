# GitHub 推荐：9,838 star、0 行代码：这个越狱仓库卖的是时效性

> GitHub: https://github.com/togg53192-cmd/jailbreaks

## 一句话总结

一个独立开发者用 4 个月、39 个纯 Markdown 文件、**一行代码都不写**，靠「谁家今天发新模型，我今天就出对应提示词」的滚动追踪，做出了 9,838 star / 1,382 fork 的细分赛道头部；它的真实资产不是内容而是**时效性**，而内容本身已被一个 524 star 的仓库逐字节抄走并挂上了付费 API 的推广位。

## 值得关注的理由

- **一个反常识的样本**：GitHub 语言统计为空、tokei 实测代码行数 0、无 LICENSE、无 CI、无测试、无 release，却做到了 9,838 star。它证明了一件事——**在「信息产品」这个品类里，时效性和策展判断力可以完全替代工程化投入**。
- **可验证的「策展方法论」**：README 把提示词按**注入载体**（system prompt / `AGENTS.md` / operating specification / Ollama Modelfile / 配置块）而非主题分类，每份工件自带「该粘到哪」的声明，版本用「新增 `v2.md` 而非覆盖」表达。这套「文件即数据库、文件名即主键、README 即 schema」的极简架构，对任何做小规模知识资产库的人都可直接迁移。
- **一个正在发生的版权事故**：我逐文件校验了 `Alejandros17487/ai-jailbreaks`（524 star），**33 个共有文件在做空白归一化后哈希完全一致**——它不是 fork（不在本仓库的 fork 列表里），是直接抄走，然后在 README 顶部挂了 `7api.st` 的付费 API 引流位。而原仓库没有 LICENSE，所以这份复制在法律上畅通无阻。
- **一个仍在爬坡的窗口**：star-history 周采样显示 9/15→9/23 十天内从 198 涨到 1,994（约 10 倍），10/22 已达 7,541，今天 9,838——**增长不是历史的，是当下的**。

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/togg53192-cmd/jailbreaks |
| Star / Fork | 9,838 / 1,382（Watcher 97；Fork/Star 14.0%，绝大多数 star 者「复制走用」） |
| 代码行数 | **0 行可执行代码**；Markdown 6,091 行（39 个文件：37×`.md` + 1×`.txt`），GitHub 语言统计为空——这是事实而非采集失败 |
| 许可证 | 无（未声明 LICENSE，默认保留全部权利——本仓库最要紧的一处缺陷） |
| 项目年龄 | 4.4 个月（首次提交 2026-06-18） |
| 开发阶段 | 密集开发（80 commits，近 30 天 43 个，10 月单月 36 个；commit 计数按作者时间口径，按提交者时间则近 30 天 38 个） |
| 贡献模式 | 独立开发者主导（作者本人 70/80 = 87.5% 的提交，与 GitHub API 贡献者统计口径一致；共 5 位贡献者，其余 4 位合计 10 个） |
| 热度定位 | 大众热门（细分赛道头部，但与生态头部 L1B3RT4S 的 22,805 star 差一个量级） |
| 质量评级 | 内容 良好 / 文档 良好 / 索引 一般 / 测试 无 / CI 无 / 许可 **缺失** |

## 作者视角：为什么存在这个项目

> 本仓库**无官方文档、无博客、无 wiki、无 `.github/` 目录、作者 bio/company/location/blog 四项全空**。以下全部由 README 措辞、commit 历史、issue 响应模式与文件结构反推，属推断而非官方自述。

### 创始人/作者背景

`togg53192-cmd`，2025-07-25 注册，1.27 年账号，300 followers，14 个公开仓库。真正有热度的只有这一个（repo_rank = 1）。其余 13 个是 0–20 star 的无关小项目（OSINT 聚合器、图像编辑器、Chrome 扩展、IP 追踪、CS2 外挂、4 个空 HTML 壳）——**不是批量铺开的矩阵号，jailbreaks 是孤例式爆发**，既说明作者没有团队、也没有在做矩阵化运营。

更值得注意的是 **git 历史里的第一条线索**：仓库首日 2026-06-18 的前 4 次提交是「Add guidelines for writing adult fiction」「Establish collaboration guidelines for adult fiction」「Create collaboration guidelines for dark fiction writing」「Introduce author's insights on dark fiction and collaboration」，对应 `opus v1/v2`、`sonnet v1`、`Sonnet v2` 四个文件——**本仓库最早的四份工件，commit message 与内容都是第一人称的成人/暗黑文学作者人设铺垫**。`opus v1.md` 至今仍是一段完整的虚构作家自述，与 README 现标的「Conversational groundwork persona」完全对得上。后来 `fe77207 Revise content policy and boundary definitions` 把这条线重新叙事化为「研究/教育」。

这个细节决定了对本项目的所有解读：**它不是安全研究者的工具集，而是一个创作者把自己的「定制 agent 行为契约」方法沉淀下来之后，顺手做成了索引。**

### 问题判断

作者的问题意识是**自用中长出来的**，不是外部观察来的。证据是完整的时间线闭环：

| 时间 | 事件 | 含义 |
|------|------|------|
| 2026-06-18 | 建仓，一天内 13 次批量上传，随后把无扩展名文件统一重命名 | 「先有货、后整理」——作者手上已有一批成品，只是找了个地方放 |
| 2026-06 ~ 08-16 | star 停在 11–12，**零 fork** | 纯自用阶段，无外部关注 |
| 2026-08-19 | 第一个 fork 出现（8 月共 3 个） | 社区开始发现 |
| 2026-09-08 起 | fork 批量出现（9 月 333 个、10 月 1,066 个；全量翻页快照口径，GitHub 页面计数为 1,382） | 被当成该赛道「默认收件箱」 |
| 2026-09-15 → 09-23 | star 198 → 1,994（10 天约 10 倍） | 第一次爆发 |
| 2026-09 / 10 | commit 各 26 / 36 个，模型清单同步换成 GLM 5.3、Step-5、Gemini 4 Argon、Mistral Large 4、Muse Wonder、Kimi K3.1、Nemotron 3 Ultra | **作者在 star 涨起来之后，加大了更新频率** |

**为什么是 2026 年 6 月**：前置条件是 2025H2 之后新一代模型与 agent harness 的密集发布；但更直接的答案是——**作者自己第一次需要这类工件的时候**。这是典型的自用型项目时间点：需求先于市场。

而 17 个 open issue 里排着一条按版本号编号的追新队列（Gemini 3.8 / GPT-6 Luna / Kimi 3.1 / Nemotron 3 Ultra / Qwen 3.8），说明**社区已经把「模型发布」当成了这个仓库的更新信号**——作者更新频率直接由上游模型发布节奏决定。

### 解法哲学

README 的「Contributing」五条是这个项目唯一的宪法，也是理解作者取舍的钥匙。逐条对照「做」与「不做」：

**明确做的**：一文件一提示词；内容完整（`complete and paste-ready. No summaries. No partial excerpts`）；声明注入面（明文列举 system prompt / `AGENTS.md` / Modelfile / configuration slot）；版本不覆盖（「Significant revisions should receive a new version rather than silently replacing an older prompt」）；描述准确（「Avoid claiming compatibility with versions or models that have not been tested」）。

**明确不做的**——这部分比做的更能说明作者是谁：

| 不做 | 证据 |
|------|------|
| 不建社区网络 | Issue #19 是外部 JB 制作人上门求互推（从我这取一条 + 标注我），**0 回复至今 open** |
| 不做多渠道分发 | Issue #31 请求建 Telegram 频道（「if it got removed from GitHub then it show telegram」），未落地；作者把 GitHub 当唯一权威副本，并接受「被删仓」风险 |
| 不做版本化发布 | 0 tag / 0 release / 0 CHANGELOG，版本只活在文件名里 |
| 不做治理文件 | 无 `CONTRIBUTING.md` / `CODE_OF_CONDUCT.md` / `SECURITY.md` / issue 模板 / PR 模板 / `.github/`；README 的 Contributing 一节是唯一规范来源 |
| 不做工程化 | 无 CI、无脚本、无 schema 校验、无哈希、无回归测试 |
| 不做商业化 | README 无任何指向自家产品、Discord、Telegram、Sponsor 的链接 |

**从 PR 审查反推的接受标准**：#23（附完整结构说明）、#13（剔除 Discord 水印）、#10（纯 housekeeping 补扩展名 + 拆 macOS 大小写冲突）全部合并；#28「taking a course about git and github」至今 open。

把这些放在一起看，作者的策展立场是清晰的：**他要的是一本目录清晰、可在 GitHub 里并排 diff 的「模型提示词样本册」，并且坚持自己作为策展者的身份。** README 的一节 Contributing 实际承担了 CHANGELOG / CONTRIBUTING / SECURITY 三份文件的职责——这是本项目最核心的一次取舍：**规范停留在散文层面，没有 CI 或 schema 校验兜底**，于是它既保住了零依赖，也付出了索引漂移与命名混乱的代价（见下方第 5 条）。

### 战略图景

判定：**这是一个内容产品 / 流量位，不是一个软件项目。**

证据是三零一强：**零商业化**（无自家产品导流）、**零平台化**（拒绝 Telegram、拒绝互推、拒绝模板——拒绝一切把读者变成关系的动作）、**零持续性承诺**（0 tag、0 roadmap、2026-07 整月零提交）；**却有最强的持续性行为**（9/10 月 26+36 次提交，严格对应当月新发布模型）。

作者在运营的是一个**模型版本追踪位**。README 的模型清单本身就是按发布顺序滚动更新的版本追踪表——这个清单天然是一份「模型时代的提示词形态」历史切片，因为同一模型的两版提示词（`qwen-3.7.md` 的 740 行 XML 式 vs `qwen-3.8.md` 的 120 行 operating-spec 式）会并列留在仓库里。

内容上分双轨：**闭源前沿**（10 月主力：Gemini 4 Argon / Mistral Large 4 / Muse / Step-5 / Nemotron 3 Ultra）与**开源及免费 stealth 模型**（9 月主力：GLM 5.3 / Kimi K3 / LongCat / MiMo / DeepSeek 4.1 / OpenCode Zen 一族）。**后者是真正的差异化资产**——竞品几乎无人跟进 OpenCode Zen 这条线。

## 核心价值提炼

### 创新之处

1. **载体原生（carrier-native）的工件封装** — 新颖度 3/5 | 实用性 5/5 | 可迁移性 5/5
   别的仓库给「提示词」，这个仓库给**部署工件**。每份文件自带注入面声明，且声明写进了工件的语法里而非外挂文档：Ollama Modelfile 体真的带 `FROM` + `SYSTEM """…"""` + `PARAMETER`，可以直接 `ollama create gemma4-jb -f gemma4.md` 跑起来；`grok-config.txt` 是带 `<ctx>/<priority>/<router>/<interpret>/<reasoning>/<voice>` 子标签的 `<CFG>` 块；另有 9 份以 `# Assistant Operating Specification` 起手、若干份以 `<system-reminder>` 开头模拟 harness 注入。
   *so what*：把「放哪里用」编码进工件语法，意味着投放可以机械化，而不是靠人肉记忆。这是从「提示词」到「部署工件」的关键跃迁。

2. **按注入面而非按主题的索引分类学** — 新颖度 3/5 | 实用性 4/5 | 可迁移性 4/5
   README 表格三列 `Model | File | Type`，`Type` 列就是**载体声明的规范化表述**（「System prompt」/「Assistant operating specification」/「Workspace operating profile」/「`FROM` + `SYSTEM` block」/「`<CFG>` priority and routing configuration」）。分类依据是「应该投放到哪个面」，对使用者正交；每类有稳定形态特征（Modelfile 必带 `FROM`/`SYSTEM`，`<CFG>` 必带子标签，operating spec 必带编号章节 + Boundaries + 决策函数，纯 system prompt 无标题散文起手）。
   *so what*：这是一条任何「需要投放到多种接口的配置/模板/示例库」都能直接抄走的索引轴。

3. **非破坏式版本化（additive versioning）** — 新颖度 3/5 | 实用性 5/5 | 可迁移性 4/5
   不打 tag、不覆盖旧文件，而是新增 `opus v2.md` / `Sonnet v2.md` / `Muse-spark-1-3-v2.md` / `deepseek v4.md`。副作用是：同一模型两版提示词可以在 GitHub 里直接 `?diff=split` 并排对照——**这是本仓库最被低估的能力**。代价是版本谱系不可机读（v2 是修订还是针对另一模型版本重写，无 metadata），同模型文件数随版本线性膨胀（Anthropic 一家占 4 个链接）。

4. **模型追踪作为策展单位** — 新颖度 4/5 | 实用性 5/5 | 可迁移性 3/5
   索引键 = 厂商 + 模型版本，不是主题、不是技巧、不是难度。仓库索引等价于一份滚动版本追踪表，天然承载历史切片。**这是本项目唯一无法被一次性复制的资产**（见「竞品格局」）。

5. **把「拒绝即失败」写成可执行决策函数** — 新颖度 4/5 | 实用性 3/5 | 可迁移性 4/5
   `grok-4.7.md` 里写成可执行伪代码 `resolve(request): if matches one of the five boundaries: decline ... else: build(request, fidelity=FULL)`，并附「误判自检清单」（哪些内心独白属于推理错误、应丢弃）。`Unified.md` 与 `kimik3.1.md` 把同一套论证重构成「Operating Policy + 六条 Boundaries + 分类决策函数」。
   *so what*：**这套文档工程手法可以完全脱离越狱语境使用**——任何需要写「agent 行为契约」「内容策略」「路由规则」文档的人都能照搬：散文规则 → 判定器 + 反例清单。

6. **纯 Markdown + GitHub 原生 diff 的并排对照** — 新颖度 3/5 | 实用性 4/5 | 可迁移性 4/5
   刻意不用 ZIP / JSON / 数据库，换来的是零安装零运行时、记事本可改、PR 友好，以及「在 GitHub 里直接 diff 两个模型的 system prompt」这个任何 JSON 方案都要自己实现的能力。

### 可复用的模式与技巧

1. **文件名即主键**（file-as-DB）：每个资产一文件，文件名承担唯一标识与元数据。适用：零依赖内容资产库。⚠️ 前提是**命名规范必须在第一天就存在**——见下方「关键设计决策」第 5 条的反面教训。
2. **载体原生封装**：把「放哪里用」写进工件语法而非外挂文档。适用：需投放到多种接口的配置/模板/示例库。
3. **按注入面而非按主题分区**：索引键 = 部署位置/消费面。适用：配置库、SDK 示例库、插件库。
4. **非破坏式版本化 + 并排对照**：版本摊平成并列文件，旧版不被 git history 埋掉。适用：会迭代但旧版仍有参考价值的资产。
5. **单一索引文件 = 文档 + schema + 使用手册三重身份**：README 同时是索引、规范、使用说明，零依赖。适用：小规模策展型仓库。⚠️ 代价是索引必然漂移（本仓库已漂移 5 个文件）。
6. **规则写成判定器 + 反例清单**：散文规则 → 可判定决策函数 + 误判自检表。适用：agent 行为规范、内容策略、路由策略文档。
7. **研究叙事作为免责护栏**：研究框架 + 边界声明 + 保留全部权利三层叠加。适用：灰区知识发布。⚠️ **注意这是声誉措施不是技术控制**——外部评论已准确指出这点。
8. **反向内容作为诊断样本**（源自 Issue #14 信号）：社区最想要的其实是「模型拒绝时的原始输出」，用来当失败诊断样本读。这是比「正向提示词」更稀缺、也更接近真实评测需求的数据。
9. **模型版本追踪表作为索引**：随时间滚动的版本清单。适用：快速迭代的外部依赖追踪。

### 关键设计决策

1. **README 作为唯一 schema 与索引——「无 schema 时代的 schema」**
   - 问题：39 个平铺文件，用户怎么知道哪个对应哪个模型、该粘到哪、是否完整？
   - 方案：三列表格做索引，`Type` 列是载体声明的规范化表述；README 同时承担使用指南（5 个投放子节）、贡献规范（5 条）、免责声明。
   - Trade-off：换来零学习成本、零依赖、GitHub 原生渲染、浏览器内直接 diff；牺牲机器可读性——无 frontmatter、无 sidecar，索引一致性全靠人工维护，必然漂移。
   - 可迁移性：**高**

2. **「一文件一提示词」= 文件即数据库，文件名即主键**
   - 方案：不用数据库/frontmatter/目录层级。`opus v1.md`/`opus v2.md` 天然成版本序列；`glm-zcode-5.3.md` + `glm-zcode-5.3-AGENTS.md` 天然成「同模型两载体」一对。
   - Trade-off：换来 `ls` 就是一次检索、IDE/fzf 直接可用；牺牲文件名承载不了的关系——同模型多载体只能靠 `-AGENTS` 后缀表达，且无法表达「这版是为哪个模型版本适配的」。
   - 可迁移性：**高**

3. **载体声明机制——让工件可被机械投放**
   - Trade-off：文件内声明做到零歧义 + 可直接投放（Modelfile 真能跑）；代价是**不机器可解析**——6 种标记语法，要自动化投放得写 5+ 套解析分支。**这正是竞品 `gpt-instruct` 能做 SHA-256 + 回归套件而这里不能的根因。**
   - 可迁移性：**高**

4. **非破坏式版本化**
   - Trade-off：与 git tag 相比，tag 让「同一文件新旧」有明确谱系；本方案把版本摊平成 N 个文件，好处是浏览器内直接并排 diff 且旧版不被 git history 埋掉，代价是**版本谱系不可机读**，且同模型文件数随版本线性膨胀。
   - 可迁移性：**中–高**

5. **命名规范晚于存量——「文件名即主键」设计的最大脆弱面（反面教材）**
   - 规范：Contributing 第 1 条要求「lowercase names with hyphens and no spaces」，示例 `model-name.md`。
   - 实际：**规范发布于 2026-10-13，而仓库 90% 的文件在此之前已存在**。现状是规范与存量错位：6 个带空格文件名（`Grok build.md`/`Muse spark 1.3.md`/`Sonnet v2.md`/`opus v1.md`/`opus v2.md`/`sonnet v1.md`）；版本号两套语法并存（`opus v1` 空格点分 vs `Muse-spark-1-3-v2` 连字符点分）；曾缺 `.md` 扩展名；曾有 `GLM ZCODE.md` vs `Glm Zcode.md` 大小写冲突（macOS 上致命）。
   - PR #10 的修补：两个 commit（13 文件 + 6 文件 R100，**内容零改动**）补齐 `.md` 扩展名、拆掉大小写冲突、给无版本号文件补版本号。
   - **PR #10 还漏了**：6 个空格文件名全保留（README 里要写 `%20` 编码，脚本容易踩坑）、命名风格未统一、同模型多载体关系看不出（`muse-ai-AGENTS.md` 与 `Muse spark 1.3.md` 同模型却看不出）、`qwen-preferences.md` 空占位未清理。
   - **根因：规范只能靠人读 README 执行，没有 CI 或 schema 校验兜底。** 若规范在 2026-06 建仓当天就存在，本可一次 rename commit 全部统一。
   - 可迁移性：**高**（教训极其直接）

6. **提交工作流：25 次网页上传 + 本地改名**
   - 事实：80 个提交里有 **25 个（31.3%）是 `Add files via upload`**，即 GitHub 网页端上传。上传时平台把文件名强制为 `AGENTS.md`（或 `AGENTS.txt`），作者随后必须本地 `git mv` 改名。全库 40 个 R100 重命名里，至少 14 对是这套「占位名 → 语义名」的两段式提交（`AGENTS.md → kimik3.1.md`、`AGENTS.md → Unified.md`、`AGENTS.txt → Beam.md`、`AGENTS.md → Muse-wonder.md`、`AGENTS.md → Gemini-4-Argon.md`……）。
   - **这解释了为什么「被修改最多的文件」是 `AGENTS.md`（14 次）——它不是被反复修订的核心文件，而是同一个占位文件名被 14 份不同内容依次复用。** 按时间顺序读这 14 个目标文件名，等于一份维护者的模型追踪清单：DeepSeek 4.1 → GLM Zcode 5.3 → Muse Spark 1.3 → Grok Build → GLM 5.3 Flash → Step-5 → Mistral Large 4 → Muse Spark 1.3 v2 → Gemini 4 Argon → Muse Wonder → Unified → Kimi K3.1。
   - 作者本人从未把仓库 clone 到本地做内容版本管理（无 tag、无 changelog、无分支流），但确实用了本地 git 做重命名与合并；**社区贡献者走的则是完全规范的 PR 流程**——只有主维护者自己用网页上传。
   - 可迁移性：**高**

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | toggg53192-cmd/jailbreaks | YuJunZhiXue/dsh-purge | MDX-Tom/gpt-instruct | elder-plinius/L1B3RT4S | Alejandros17487/ai-jailbreaks |
|------|---|---|---|---|---|
| Star | 9,838 | 13,556 | 10,957 | 22,805 | 524 |
| 形态 | 纯 Markdown 语料库 | DeepSeek Harness 运行时补丁插件 | Codex 提示词 + 测试包 | 提示词大杂烩 + token 技巧 | 原仓库的逐字节镜像 + API 引流 |
| 覆盖广度 | 37 工件 / 9 家厂商 / 30 行索引 | 锁定单一 harness | 锁定单一方案 | 广但浅 | 与原仓库全同步（落后 3 个新模型） |
| Commit 数 | 80 | 24 | 84 | 254 | 5 |
| 载体标注 | **5 类载体，每类文件内自证** | 注入面固定 | 单一形态 | 无 | 抄原仓库（较规范） |
| 可验证性 | 无 | 版本化 release（v1.1.83）+ Apply/Restore | **SHA-256 + 回归套件 + A/B/C 发布闸门** | 254 commits | 无 |
| 许可 | **无 LICENSE** | Apache-2.0 + 署名要求 | MIT | AGPL-3.0 | 无 |
| 版本化 | 文件名内嵌版本号（0 tag/0 release） | 语义化 release | 语义化 release | git 历史 | 补了 CHANGELOG（但 0 tag） |
| 失效治理 | 无（#5 开 6 评论仍 open） | 可 Apply/Restore | 回归测试 | 无 | 无 |
| 可发现性 | 0 topics | — | — | — | **6 topics，反超原仓库** |

### 差异化护城河

**技术层：弱。** 载体标注是一套可被照抄的规范，且已被证明可抄。

**生态层：中偏弱，而且正在变弱。** 一个真实但需要精确表述的事实：本仓库的 fork 列表里确实有 `YuJunZhiXue/jailbreaks`（2026-09-08）和 `MDX-Tom/jailbreaks`（2026-10-26）——两位头部竞品作者都曾 fork 过本仓库。**但必须指出因果方向**：他们各自的旗舰仓库 `dsh-purge`（2026-08-19）和 `gpt-instruct`（2026-07-11）**都创建于各自 fork 之前**。所以 fork 记录证明的是「他们来消费过这个库」，**不能证明「他们是从这个库长出来的」**。这两个头部项目是本仓库的**下游消费者与背书**，不是它的派生。

**信任层：弱。** 无 LICENSE / 无 release / 无回归测试 / 无协调披露，README 的免责声明在外部评论中被准确评价为「a norm, not a control」。

**真正稀缺的只有两样**，而且都只依赖作者个人劳作、没有被任何机制固化：

1. **滚动模型追踪的持续性**——竞品都没有：dsh-purge 锁定单一 harness，gpt-instruct 是单一方案。**时效性是唯一无法被一次性复制的资产。**
2. **OpenCode Zen 免费 stealth 模型这条线**（Big Pickle / Space Bunny / LongCat / MiMo / Step-5）——竞品几乎完全没跟。

### 竞争风险

1. **内容已被整体复制，且复制方在变现**（最高优先级）：`Alejandros17487/ai-jailbreaks` 的 33 个共有文件**在做空白归一化后哈希完全一致**。它**不在本仓库的 fork 列表里**——也就是说它连 fork 都没走，直接把内容整体搬走，然后在 README 顶部加了 `7api.st` 的付费 API 引流位（「up to 99% off, including Uncensored and Abliterated models that never refuse」）+ Telegram 频道 + 带 `?start=github2` 返利参数的 bot 链接。它还顺手补了 `CHANGELOG.md` / `CONTRIBUTING.md` / `SECURITY.md`、加了 6 个 topics、把 6 个带空格文件名全部规范化、**把原仓库自己都漏收的 `beam.md` / `unified.md` / `muse-wonder.md` 收进了索引**。原仓库 README **完全没有提到这个镜像**。
2. **无 LICENSE 让这一切畅通无阻**：默认保留全部权利，但内容已被整体搬运并挂上商业推广位，原仓库既无收益也无护城河。
3. **治理度被反超**：镜像者补齐了本仓库一直没补的治理文件，搜索可见性也反超（本仓库 0 topics）。
4. **失效治理缺失导致「star 数 ≠ 有效性」**：无兼容矩阵、无失效标记、无 CI 校验，唯一的处置是 README 里一句「If a file appears outdated, open an issue」。#5 开 6 评论至今 open，#9、#8、#12 同类。**在无版本化发布、无回归测试的前提下，9,838 star 和免责声明都无法推断任何一份工件当前是否有效。**
5. **作者单点依赖**：87.5% 提交集中度 + 2026-07 整月零提交的先例 + 14 个仓库分散注意力。

### 生态定位

**上游原料节点（upstream feedstock node），而非产品。**

真实功能有三层：① 给下游竞品与镜像者供料；② 作为「模型版本追踪位」提供低成本查阅基准；③ 为该细分赛道提供默认收件箱（issue #31/#32 反映用户已把它当成默认收件箱，并自发建立 Telegram 备灾渠道）。

用 npm 类比：**它更像一个早期的 registry 镜像，而不是一个 npm 包本身。**

## 套利机会分析

- **信息差**：**低**。9,838 star 的可发现性溢价已经兑现，这个位置没有留给新人的套利空间。但有一个**反向信息差**值得注意——多数人看到「9,838 star 的越狱仓库」会以为它是一个成熟项目；实际上它 0 行代码、0 测试、0 CI、0 release、**连 LICENSE 都没有**，且**已有 33 份文件被整体复制并挂上商业推广位**。也就是说，**star 数与工程成熟度、与权利归属完全脱钩**。读这个仓库的人如果按 star 数分配信任，会分配错。
- **技术借鉴**：这是本仓库最实在的价值所在，而且**与它的内容毫无关系**——是它的策展架构。「文件即数据库 / 文件名即主键 / 单一索引文件承担 schema + 索引 + 手册三重身份 / 按注入面而非按主题分区 / 非破坏式版本化 + 并排对照 / 载体原生封装」这一整套，是任何做小规模知识资产库、配置库、示例库、模板库的人可以直接照搬的。
- **生态位**：填补的是「模型发布 → 提示词工件」这条链上的**时效性空档**。这个空档不是技术空档而是**人力空档**——没有人愿意持续做「每天跟一遍各家模型发布」这件没有技术含量但极耗时间的事。
- **趋势判断**：**符合趋势，且仍在爬坡**。star 曲线最后 8 天净增约 2,300，尚未见顶。但「后发优势」在这里是**反过来的**：本项目没有后发优势，因为头部竞品在工程化、许可、可验证三个维度全面超越，而它唯一的优势是「更早、更全、更新更快」的时间差——**而时间差每天在缩小**。真正的机会不在于追赶头部，而在于**把时效性这个唯一资产机制化**（见「行动建议」）。

## 风险与不足

1. **许可缺失是硬伤，不是瑕疵**：无 LICENSE = 默认保留全部权利。但内容已被整体复制并挂上付费 API 引流位，**权利归属与实际流通状态完全脱节**。机构/企业连「内部使用是否合法」都无法确认；社区也无从把它的内容接进自己的红队平台。IndieKings 的评价很准确：**被 fork 的一方拿到了许可证，留下的这一方反而没有。**
2. **完整性契约有三处例外**：抽样验证 37 份工件中的 20 份（54%），均为完整可投放文本，无「节选」、无省略号截断、无「（以下略）」，文件尾普遍是收束句或完整的 Ollama `PARAMETER` 块，符合 `paste-ready` 契约。**例外 3 处**：`qwen-preferences.md` 是 1 字节空占位（内容已于 2026-06-18 删除，残留未清理）；`opus v2.md` 首字损坏（`aaI want to...`）；`Muse spark 1.3.md` 的 H1 写成了 `# \# Muse Spark 1.3`（转义残留）。`deepseek v4.md` 结尾还混入了与提示词无关的拼接内容。
3. **索引漂移且数量口径三套不自洽**：README 的 33 个链接**全部有效，0 失效链接**；但有 **5 个文件未被收录**——`Unified.md`（97 行，全库最完整的 operating policy 骨架之一）、`Beam.md`（230 行，同骨架的另一实现）、`Muse-wonder.md`、`kimik3.1.md`（作者 `fe77207` 唯一改动过的文件）、以及空占位 `qwen-preferences.md`。**遗漏的不是边角料，是高价值资产。** 同时数量口径三套对不上：badge 与正文称「32 prompts / 26+ targets」，README 表格实际 30 行 / 33 链接，磁盘实际 37 份内容工件。**偏差方向是「索引落后于内容」，不是「内容虚标」**——作者更新内容快于维护索引，这是纯手工索引 + 无 CI 校验的必然结果。
4. **零可验证性**：无哈希、无签名、无回归套件、无 CI、无依赖清单。第三方无法验证工件是否被篡改，维护者无法验证工件当前是否有效。对照 `gpt-instruct` 的 SHA-256 + 回归套件 + 分级发布闸门，差距最大——**但这也是最容易补齐的一项**。
5. **失效治理完全缺失**：#5「Muse.ai jailbreak doesnt work」开 6 评论至今 open，#9、#8、#12 同类。没有兼容矩阵、没有「最后验证时间」标记、没有失效下架机制。用户读到一份 2026-06 的提示词时，无法知道它是否还对 2026-10 的模型有效。
6. **协作机制原始**：无 issue 模板、无 PR 模板、无 CI、无 lint 规范（虽然内容型仓库没有 lint 也很正常）；「PR 格式对了就合并」全靠人眼判断，#28 至今卡着。2026-07 整月零提交也说明维护者可能随时消失。
7. **零运营素材**：README 全部 4 个图片都是 shields.io 徽章，仓库无任何二进制媒体文件，无截图、无架构图、无 Demo、无视频。对一个要靠 star 与信任吃饭的内容产品来说，这是曝光效率上的浪费。

## 行动建议

### 如果你要用它

- **把它当「模型版本追踪表」，别当「提示词库」**。真正值钱的不是里面某一份提示词，而是「某家模型某版本发布时，社区普遍在用什么形态的 system prompt」这份切片。
- **按载体取用，不要按模型名取用**。这个仓库最有价值的组织方式是按注入面分类：需要 API system 字段就去 system prompt 一节，需要 agent 长期行为约束就用 `AGENTS.md` / operating specification 一节，需要本地模型就直接用 Modelfile 体（`ollama create <name> -f <file>`）。
- **用之前先做版本自检**。这个仓库没有兼容矩阵，README 的版本承诺是「Avoid claiming compatibility with versions or models that have not been tested」——**作者自己都没测**。请把它当作待验证的候选，而不是可直接投产的配置。
- **安全立场**：如果你的目标是防御侧（做 prompt injection 评测、训练抗攻击模型），这个仓库是相当有价值的**手法分类样本**（人设锁定 / 指令层级覆盖 / 语境重定义 / 伪造授权文件 / 模拟系统提醒 等家族），但请注意它**没有版本化发布、没有回归测试、没有协调披露**——它是一份语料，不是一份漏洞报告。
- **合规上注意**：原仓库无 LICENSE，默认保留全部权利，商用与再分发需自行取得授权；同时请自行核对你所用平台的 ToS。

### 如果你要学它

按这个顺序读（这 6 个文件覆盖了全部设计决策）：

1. **`README.md`（221 行）** — 唯一的设计文档。精读三处：① `Collection` 表的 `Type` 列（载体声明的规范化表述）；② `How to Use` 的 5 个投放子节（**把「文件」翻译成「动作」的投放手册**）；③ `Contributing` 的 5 条（一个内容型仓库的「宪法」该长什么样）。
2. **`gemma4.md` / `gpt-oss-20b.md`** — 载体原生封装的样本。看 `FROM` + `SYSTEM """…"""` + `PARAMETER` 的 Ollama 语法如何让工件**自证可投放**。
3. **`grok-config.txt`（40 行）** — 配置块体的样本。XML 式 `<CFG>` 与子标签分层，把「一个配置要覆盖哪些维度」显式列出来。
4. **`opus v1.md` vs `opus v2.md`、`sonnet v1.md` vs `Sonnet v2.md`** — 非破坏式版本化的对照读法。同一模型两版在 GitHub 里并排 diff，是这个仓库最被低估的能力。
5. **`Unified.md`（97 行）/ `muse-ai-AGENTS.md`** — operating specification 的成熟骨架（身份 → 边界 → 分类决策 → 推理协议 → 表达规范 → 交付标准）。**这是最值得抄的部分，也是原仓库自己漏收了索引的资产。**
6. **`grok-4.7.md`** — 看规则怎么被写成可执行判定函数 `resolve(request)` + 误判自检清单。这套手法可脱离越狱语境直接迁移到任何 agent 行为契约文档。

**顺带读一遍反面教材**：`git log --name-status` 里那 14 对 `AGENTS.md → X.md` 的 R100 重命名——它是「维护者不用规范流程管理内容」的活标本，也是本仓库 6 个空格文件名和 1 字节空占位的根因。

### 如果你要 fork 它

**最有价值的改进方向**（按 ROI 排序）：

1. **补 `LICENSE`**（MIT / Apache-2.0）——成本 5 分钟，收益是立刻堵住「被整体复制并变现」的漏洞，同时让机构能合法引用与再分发。**这是本仓库当前最紧要的一步。**
2. **补索引一致性**：把 `Unified.md` / `Beam.md` / `Muse-wonder.md` / `kimik3.1.md` 收进 README 表格，删掉 `qwen-preferences.md` 空占位，让 badge 数量与实际工件数对齐（当前 32 / 33 / 37 三套口径）。
3. **补命名规范化**：一次性 rename commit 清掉 6 个空格文件名、统一版本号语法（小写连字符点分）、把同模型多载体关系编码进文件名（如 `glm-zcode-5.3-AGENTS.md` 已经是好例子）。
4. **补「最后验证时间 + 兼容矩阵」**：每份文件加一行 `Verified against <model-version> on <date>`，README 加一张兼容表。这直接解决 #5/#8/#9/#12 这类失效 issue 的根因，也是把时效性资产化的最小成本路径。
5. **补可验证性**：`checksums.txt` + 一个 CI workflow（GitHub Actions 跑 checksum diff）。这是竞品 `gpt-instruct` 已经做到、而这里完全空缺的能力，也是最容易补齐的一项。
6. **补「反向内容」**：按 Issue #14 的信号，把「模型拒绝时的原始输出」也作为诊断样本入库。这比再收 10 份正向提示词更有价值，因为它直接支撑排障与回归评测。
7. **补 topic 标签**：0 topics 是可发现性的直接损失（镜像者补了 6 个就反超了）。
8. **补 `SECURITY.md` 与协调披露流程**：明确「发现问题 → 通知维护者 → 修复窗口」的路径，把「发布可用提示词」与「发布漏洞报告」区分开——外部评论已指出这个区分是当前最大的叙事漏洞。

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | https://deepwiki.com/togg53192-cmd/jailbreaks （已收录；探测时返回 429 限流，非 404） |
| Zread.ai | 未收录（探测返回 403） |
| 关联论文 | 无直接引用本仓库的论文。主题相邻坐标：[Don't Listen To Me](https://arxiv.org/pdf/2403.17336v1)（448 条越狱提示的体裁分类学）、[MLCommons Jailbreak Benchmark v1.0](https://arxiv.org/abs/2610.02827)、[SoK: Systematizing LLM Prompt Security](https://arxiv.science/abs/2510.15476) |
| 在线 Demo | 无（仓库无任何可运行代码、playground 或验证器；下游 `dsh-purge` 有 Drill 实验台、`gpt-instruct` 有 dry-run / 回滚） |
| 逐字镜像 | https://github.com/Alejandros17487/ai-jailbreaks （524 star，33 个共有文件哈希一致，README 顶部挂有付费 API 引流位；不在本仓库 fork 列表中） |
| 外部深度分析 | [cn-sec：七层手法从身份层打到部署层](https://cn-sec.com/archives/5535549.html) · [IndieKings：32 Prompts and a Research-Only Warning](https://www.indiekings.com/2026/10/jailbreaks-repo-32-prompts-and-research.html) |
