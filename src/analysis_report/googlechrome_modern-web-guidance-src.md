# GitHub 推荐：252 篇 Web 指南喂 AI Agent：Chrome 怎么证明知识注入有效

> GitHub: https://github.com/googlechrome/modern-web-guidance-src

## 一句话总结

Google Chrome 团队联合 Edge、Firefox 与 MDN，把「现代 Web 平台该怎么做」写成 252 篇可被 AI 编码 Agent 按需检索的指南，并用一套「有指引 vs 无指引」的浏览器内 A/B 评测体系证明了它的有效性——**它表面是文档合集，实质是一整套「如何为 AI 生产、检索、校准、度量并持续剪枝知识」的内容基础设施**。

## 值得关注的理由

1. **它是目前唯一一家「厂商级 + 跨浏览器中立 + 有公开证据链」的 Agent 知识包**。通用 Agent Skills（如 addyosmani/agent-skills，11.7 万 star）没有浏览器兼容性数据，也没有浏览器内评测；MWG 的 Owners 席位里 Chrome 2 席、Edge 1 席、Firefox/MDN 1 席、独立专家 2 席——内容权威性来自利益无关的第三方席位，而不是厂商的嗓门。
2. **它把「知识对 AI 到底有没有用」变成了一个可测量、可回归、可剪枝的工程问题**。每篇指南的 KPI 不是字数、不是覆盖度，而是 `有指引通过率 − 无指引通过率`；模型已经会的主动删掉。这是所有维护「喂给 LLM 的内部知识库」的团队都逃不掉的取舍问题，而它给出了完整的答案和代码。
3. **真正的技术富矿在 `src/` 而不在 `guides/`**。离线语义检索（teacher 模型蒸馏成 29,165 词静态查找表，查询嵌入 ~30µs、零依赖零网络）、OS 级沙箱评测隔离（bwrap/Seatbelt）、Playwright grader 的双向校准铁律、`legacy-scan` 的声明式规则 DSL + 精度准入阈值——这些几乎没有人写过深度解析，却是整套方法论最值钱的部分。

## 项目展示

![Modern Web Guidance](https://raw.githubusercontent.com/googlechrome/modern-web-guidance-src/main/.github/img/modern-web-guidance.svg)

Chrome / Edge / Firefox / MDN 四方共同维护的 Web 平台知识包，本仓库是它的「源码仓」（工厂），产物发布在 `GoogleChrome/modern-web-guidance`（1.45 万 star）

**唯一值得看的「活体 Demo」是官方 Eval Dashboard**（[googlechrome.github.io/modern-web-guidance-src](https://googlechrome.github.io/modern-web-guidance-src/)）——它实时展示 Claude Code / Codex CLI / Antigravity CLI 在「有指引 vs 无指引」两种模式下的通过率对比、无障碍检查通过率、中位任务耗时与 token 消耗，可下钻到单条指南。这是全网极少数「把自家产品的效果证据直接摊开给公众看」的 AI 项目。

无需安装即可试用 CLI：

```shell
npx modern-web-guidance@latest search "animate a dialog modal backdrop"
npx modern-web-guidance@latest retrieve "animate-to-from-top-layer"
npx modern-web-guidance@latest legacy-scan .
```

**它自己的效果证据（README 的官方 eval 快照，每晚重跑）：**

| 日期 | Agent + 模型 | 任务 / 检查 | 无指引 → 有指引（uplift） |
|---|---|---|---|
| Nov 8 | antigravity_cli (gemini-4-argon) | 214 / 1673 | 58% → 94%（**+36pp**） |
| Nov 8 | claude_code (opus-5-5) | 215 / 1801 | 57% → 88%（**+31pp**） |
| Nov 8 | codex_cli (gpt-6.1-sol) | 215 / 1795 | 54% → 82%（**+28pp**） |
| Nov 6 | codex_cli (gpt-6.1-sol) | 212 / 1773 | 53% → 86%（**+33pp**） |
| Nov 6 | claude_code (opus-5-5) | 212 / 1773 | 56% → 90%（**+34pp**） |
| Nov 6 | antigravity_cli (gemini-4-argon) | 212 / 1722 | 60% → 96%（**+36pp**） |
| Nov 4 | codex_cli (gpt-6.1-sol) | 209 / 1743 | 52% → 85%（**+33pp**） |
| Nov 4 | claude_code (opus-5-5) | 209 / 1743 | 57% → 90%（**+33pp**） |
| Nov 4 | antigravity_cli (gemini-4-argon) | 207 / 1722 | 60% → 96%（**+36pp**） |
| Nov 2 | codex_cli (gpt-6.1-sol) | 205 / 1729 | 55% → 82%（**+27pp**） |

三个不同厂商的 Agent 家族，同一批任务、同一天、每晚重跑，**uplift 稳定在 +27pp ~ +36pp**。注意无指引基线长期停在 52%–60%——这正是这套方法论的立足点：**不是「Agent 不会」，而是「Agent 会但不用」**。

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/googlechrome/modern-web-guidance-src |
| Star / Fork | 5,791 / 357（分发仓 `GoogleChrome/modern-web-guidance` 另有 14,469 / 527） |
| 代码行数 | 201,637（TypeScript 75.2%、HTML 8.1%、JavaScript 6.2%、JSON 4.9%、YAML 2.9%） |
| 项目年龄 | 11.1 个月（首次提交 2025-12-11；GitHub 建仓 2026-01-27） |
| 开发阶段 | 密集开发（近 30 天 463 commit，近 90 天 729 commit，占总量 45%） |
| 贡献模式 | 社区协作 + 厂商主导（88 位贡献者，主贡献者 Paul Irish 占 30%；四厂商 Owners 席位制度） |
| 热度定位 | 大众热门（v1.0 发布当天冲上 HN 首页 + GitHub Trending #1） |
| License | 代码 Apache-2.0；`guides/` 内容 CC-BY-4.0（部分派生自 MDN / W3C / WHATWG / IETF） |
| 质量评级 | 代码优秀 文档优秀 测试充分（156 个 test 文件） |

**内容规模**：本仓实际有 **252 个 `guide.md`**、213 个 `expectations.md`、191 个 `demo.html`，分布在 **17 个主题类别**下（ui-behaviors 45、performance 29、ui-components 28、forms 27、visual-design 27、css 20、security 17、ui-atoms 14、html 11、pwa 10、js 6、user-experience 5、accessibility 4、built-in-ai 4、webmcp 3、privacy 1、wasm 1）。README 的官方口径是「**250 个现代 Web 特性 + 203 个真实开发者使用场景**」——250 指的是 `features/` 特性注册表（`BASELINE_STATUS` 等宏的数据源），203 指的是已发布到分发仓的指南，其余为草稿态（`stub` / `wip` / `blocked`）。三个数字指向不同的东西，读仓库时别混。

**一个容易被忽略的细节**：GitHub 建仓时间是 2026-01-27，但首个提交日期是 2025-12-11——说明这个项目先在 Google 内部开发了约五周，成熟后才开源。这类「先内部验证再公开」的项目通常比「边写边开源」的质量高一档。

## 作者视角：为什么存在这个项目

### 创始人/作者背景

作者不是个人，而是 **GoogleChrome 组织账号**，背后是一个四厂商联合的委员会：

| 角色 | 席位 |
|---|---|
| Google Chrome | 2 席（Kadir Topal、Rick Viscomi） |
| Microsoft Edge | 1 席（Patrick Brosset） |
| Mozilla Firefox / MDN | 1 席（Jake Archibald） |
| 独立社区专家 | 2 席（Lea Verou 等） |

贡献者名单本身就是这个项目的权威性说明书：Paul Irish（Web 性能社区布道者）、Philip Walton（Baseline / `web-features` 生态核心）、Lea Verou（CSS 与 MDN 社区领袖）、Jake Archibald（Google 性能团队）、Rick Viscomi（Chrome 团队）。`GOVERNANCE.md` 把它制度化为 Contributor / Peer / Content ATL / Owner 四级角色，`CODEOWNERS` 保护关键路径，`docs/ATLS.md` 定义了逐领域签字的 Content Tech Lead 制度。

**这个结构决定了项目的性质**：它不是「Google 说 Web 应该这么写」，而是「Chrome、Firefox、Edge、MDN 共同说」。要复制这个护城河，竞品得先说服 Firefox 和 Edge 加入——这是结构性壁垒，不是工程量壁垒。

### 问题判断

作者看到的是一个**具体的、可量化的**问题，而不是模糊的「AI 写的代码不行」。

README 把问题拆成两层：

**第一层（表象）**：LLM 训练数据里塞满了 Web 平台的历史遗产——jQuery、滚动条定制伪元素、`setTimeout` 轮询、AOS / ScrollReveal 之类的滚动动画库。Agent 拿到「做一张卡片轮播」这种需求时，会写出语法正确但架构过时的代码。

**第二层（更隐蔽）**：即使模型**知道**某个现代 API 存在，它也缺少「生产级现代实现模式的密度」。模型知道 `popover` 这个属性，但不知道 `popover` + `interesttarget` 能替代整层 tooltip 库；知道 `field-sizing` 存在，但不知道 `interpolate-size: allow-keywords` 能配 `transition: height` 做尺寸动画。

**为什么是现在？** 三条曲线在 2026 年交汇：

1. **Baseline 生态机器可读了**。`web-features` 包提供 `status.baseline: 'low' | 'high' | false` 与 `baseline_low_date`。「这个特性在 2026-08 达到 Baseline Newly」从此是可程序化查询的事实，而不是需要人工查表维护的注释——这是整个项目能自动化的地基。
2. **Agent Skills 机制成型**。skill 常驻上下文极小（全量知识按需检索），「加一套 Web 知识」从「每轮对话都涨价」变成「按需付费」。
3. **Agent 能力恰好越过临界点**。实测无指引基线在 52%–60%——模型「大概知道」现代 API 但就是不用。**100% 会了就不需要引导，0% 会了引导也救不回来，54% 正好是引导最有价值的区间。**

### 解法哲学

**AGENTS.md 里的三个词**是全仓库信息密度最高的一段：

> 「Because `guide.md` is the **only** file retrieved by external coding agents at runtime (`demo.html`, `expectations.md`, and `targets/` are used within this repo for validation and evaluation), all guidance must be self-contained, deterministic, and command-oriented.」

- **自包含（self-contained）**：指南不能引用外部 URL 让 Agent 自己去读。所有 fallback 必须内联——`FEATURE_FALLBACKS` 宏展开的 `#fallbacks` 段如果为空，**构建直接失败**。
- **确定性（deterministic）**：正文里不能有「通常建议」「一般而言」。`src/core/guide-validation.ts` 做 frontmatter 校验与 draft 状态机（`stub` / `wip` / `blocked` + 必填 `draft-reason`）。
- **命令导向（command-oriented）**：写「用 `popover` 属性」，不写「建议考虑使用 Popover API」。

**更狠的一条是反向剪枝**。README 写得很直白：

> 「if models already succeed without guidance, we prune redundant advice; where agents struggle, we refine guides to maximize uplift.」

一篇指南的 KPI 是 `(guided pass rate − unguided pass rate)`。如果模型无指引时已经能通过评测，那这篇指南就是纯 token 浪费，应该被删掉。**这不是「写更多文档」，是「写有边际收益的文档」**——把它当成一个带 ROI 约束的内容投资决策。

**明确不做什么**（有代码/文档证据）：

| 不做 | 原因 |
|---|---|
| 不做常驻大上下文 | skill pack 常驻仅 ~205 tokens（README 官方口径），全量指南库按需检索拉取——**加指南不会让每次会话的 prompt 变大** |
| 不做网络调用 / 不要 API key | CLI 完全离线本地运行，npm 包自包含零额外依赖，供应链面被主动收窄 |
| 不提供 `legacy-scan --fix` | Agent 会误删**有意为之的 fallback**。40+ 规则的 `dropWhen` 里明确列着「已声明 color-scheme」「已用 light-dark()」「位于 `@supports` fallback 块内」 |
| 不做 SSR / 常驻服务 | `src/harness/lib/reporting.ts` 明确写死「Skills (CLI) is the only supported serving approach」 |
| 不做企业版 / 托管服务 | Apache-2.0 + CC-BY-4.0，全内容与全部评测数据公开，无 open-core 成分 |

### 战略意图

**定位是基础设施，不是产品**。本仓库 `private: true`，真正对外分发的是 npm 包与各家 plugin marketplace 里的 skill。

**无直接商业化，但有清晰的间接价值捕获**：让更多代码使用原生 Web API → 浏览器能力更强 → Chrome 生态更有粘性。同时把 Firefox / Edge / MDN 拉进同一套内容标准，等于用治理成本换取整个 Web 平台的共识度。

**开源策略是 genuinely open**：四厂商联合治理、无 CLA bot、社区可直接提 PR、完整的 Peer / ATL 晋升制度、所有评测数据与 dashboard 公开。它更像是**给整个 Web 平台做公共品**。

## 核心价值提炼

### 创新之处

1. **「机会 = 100% − 无指引基线」的反向剪枝策展模型**
   把指南写作变成一个有反馈回路的优化问题：模型已经会的 → 剪掉；教了也不会的 → 重写；教了就会的 → 加厚。配套多 Agent golden solution 生成、grader 双向校准、nightly 每日重测。
   新颖度 4/5 · 实用性 5/5 · 可迁移性 高

2. **对称编码「锥塌缩」的定量诊断与非对称检索配方**
   最初 query 和 document 用同一模型同一 task type 编码，实测发现：把 ~300 词的 markdown chunk 做平均 embedding，会把所有文档向量拉向英语词频质心，在单位球面上塌缩进一个 **0.970 余弦锥**——结果 `"best pizza in new york"` 与 `<dialog>` 指南的相似度高达 **0.899**，检索彻底失效。处方是让 query 侧走「词级蒸馏 + 短查询锐利（mean pairwise cosine 0.28）」，document 侧走「完整 transformer + 长文本」，**故意不对称**。
   新颖度 4/5 · 实用性 4/5 · 可迁移性 高

3. **Grader 双向校准铁律：golden patch 必须 100% 通过，未改动的起始应用必须 100% 失败**
   两者同时满足才算校准成功；额外检测「所有 golden solution 都挂在同一批测试上」→ 判定为 grader 自身的 bug 并 fail-fast。这是 SWE-bench 那套 fail-to-pass 校验思想，被搬到「自然语言 expectations → 浏览器内行为断言」的转换上。
   新颖度 3/5 · 实用性 5/5 · 可迁移性 高

4. **OS 级文件系统沙箱下的 AI Agent 能力评测**
   Linux 用 bubblewrap `--tmpfs` 覆盖仓库根目录，macOS 用 Seatbelt SBPL 规则 deny，并额外隐藏 `~/.gemini` / `~/.claude` / `~/.codex` / `~/.pi` / `~/.guidance_logs`、重挂整个 `/tmp`、用 `--ro-bind /dev/null` 遮蔽 `grade.mjs` / `run.mjs`。找不到沙箱工具时**响亮失败**（抛异常终止），只有显式设 `GD_UNSAFE_NO_SANDBOX=1` 才允许裸跑。还解掉了 bwrap 用户命名空间的 UID 陷阱（unprivileged namespace 里只有当前 UID 被映射，host 上 root 拥有的目录显示为 `nobody`，某些工具会拒绝这种路径）。
   新颖度 4/5 · 实用性 4/5 · 可迁移性 高

5. **`.mwgrc` 把「AI 该不该用新特性」从模型判断转成项目配置 + 组织治理**
   只在单一引擎（Blink / Gecko / WebKit）稳定发布的特性视为 volatile，从该引擎首次稳定发布起 3 个月窗口期后才自动进入默认集；Owners 可逐特性推翻。特性**仍可被 search 发现**（可发现性不损失），但 retrieve 被门禁。更妙的是**门禁的错误信息是写给 Agent 的行为契约**：明确告知「不要改 `.mwgrc`、不要自己跑 CLI、不要从磁盘读原始 .md」，即使 Agent 没查指南就写了该特性，也**必须**在最终输出的 `### Modern Web Guidance` 段落里加一条带解锁命令的 bullet。
   新颖度 4/5 · 实用性 4/5 · 可迁移性 高

6. **SNR 指标：把 token 成本写进检索质量的目标函数**
   `SNR = 0.7·Recall + 0.3·Leaf nDCG − TokenTax`。TokenTax 对无关指南的 token 消耗递增惩罚（每 100 token 1.4 分，超 500 token 后每 100 token 4.5 分），并额外惩罚「可答查询返回 `[]` 导致 Agent 转而 dump 整个目录」的 1,500 token 兜底。这让「检索更准」和「检索更省」变成同一个可优化目标。
   新颖度 4/5 · 实用性 4/5 · 可迁移性 高

7. **`legacy-scan` 的双轴 triage + 声明式 rubric + 精度准入阈值**
   每条规则被显式建模到两个正交轴上：**Detection**（`direct-token` 0–3% 静态误报 / `structural-ast` 3–10% / `needs-verifier` >50% / `no-legacy-pattern`）× **UpdateScope**（`local-swap` / `cross-layer-refactor` / `widget-recipe`）。这个分类**直接决定规则能否进入默认发布集**：准入阈值是 Post-Verifier Precision ≥ 90%，且 Static Matcher Precision ≥ 80% @ n≥10（稀有模式 ≥ 90% @ n≥5）。规则的判定语义被抽成 `keepWhen` / `dropWhen` 两个字符串数组，可以喂给 LLM Verifier 做第二阶段判别。LLM Verifier 的默认策略是**不确定时 KEEP**——宁可多报也不漏报。
   新颖度 4/5 · 实用性 4/5 · 可迁移性 高

8. **CLI 主动感知 harness 的 stdout 截断行为**
   Claude Code / Codex CLI 等 harness 会把超过 ~10 KB 的内联工具输出**静默中间截断**（显示 `<truncated ... bytes>`），而 76.6% 的指南单篇在 9.5 KB 以下——超限的指南等于没读到。CLI 检测 `fstatSync(1).isFile()` 区分管道与重定向，超限时自动 spill 到 `/tmp/mwg-guide-<pid>-<ts>.md` 并打印两行指令：「用文件读取工具读全，**不要用 cat 或 head**」。
   新颖度 3/5 · 实用性 4/5 · 可迁移性 高

### 可复用的模式与技巧

1. **「静态查表 + 预烘焙向量」的离线语义检索**：把 embedding 模型蒸馏成静态词表 + 预烘焙文档向量，运行时零模型加载、零网络、~30µs 查询。适用：CLI 工具、浏览器端、内网离线助手。
2. **非对称检索（query 短而锐 / doc 长而全）**：适用：长文档 RAG、chunk 平均导致相关性坍塌时。
3. **RRF（Reciprocal Rank Fusion）融合异构排序**：k=60 只用排名不用分数，规避余弦与 BM25 的量纲校准问题。适用：融合任何量纲不可比的排序信号。
4. **「词法命中豁免稠密门」的降级策略**：BM25 有命中时，低于 0.3 的稠密候选作为救援保留；BM25 零命中且 dense top-1 < 0.3 时干净返回 `[]`。适用：既要精确拒绝越界查询、又不让字面精确匹配被语义门槛误杀的检索系统。
5. **Grader 双向校准 + 共享失败测试检测**：适用：任何自动生成测试、LLM-as-judge、benchmark 构建。
6. **OS 级沙箱评测隔离 + 缺工具时响亮失败**：适用：AI agent benchmark、防止 benchmark 污染、代码 agent 的红队测试。
7. **「不确定时默认 KEEP」的保守 verifier 策略**：适用：静态分析 + LLM 兜底的两阶段扫描器。
8. **双轴 triage（可检测性 × 改造范围）**：适用：规则系统准入评估、迁移项目的批次规划。
9. **声明式 rubric（keepWhen / dropWhen）作为规则的语义契约**：适用：让规则可被 LLM 消费、可被人类 review、可被精度指标度量。
10. **「有指引 vs 无指引」成对 A/B + prompt 不提及工具**：适用：评测任何「知识注入对 AI 行为的影响」。关键在于 Agent 必须**自己决定**要不要去查，否则测的是「听不听话」而不是「内容好不好」。
11. **反向剪枝（opportunity = 100% − 无指引基线）**：适用：维护任何「喂给 LLM 的知识库」——内部编码规范库、SDK 最佳实践、领域 jargon 表。
12. **构建期宏展开 + 空内容构建失败**：适用：文档工程，保证兼容性数据永不腐烂。
13. **「遥测即未来评测集」的闭环**：CLI 上报的真实搜索查询经匿名化 + PII 筛查后成为评测集（`wild-v2` 4,000 条），但训练时严格排除评测 split。适用：需要真实分布数据的检索系统。
14. **隔离 HOME + shim 劫持 npx + `.npmrc` 消毒 + shell profile 强制 PATH 顺序**：适用：需要「Agent 用本地构建而非 registry 版本」的评测。
15. **「拒绝信息写成给 LLM 的行为契约」**：适用：任何 feature gate / 权限不足 / 配额受限的错误提示设计。

### 关键设计决策

#### 1. 离线 RAG：蒸馏成静态词表，而不是运行时加载模型

- **问题**：CLI 要在 Agent 每次查询时做语义检索。可选：（a） 运行时加载 MiniLM ONNX/TF.js（23.4 MB，冷启动数百 ms）；（b） 调云端 embedding API（违反零网络承诺）；（c） 纯 BM25（丢语义）。
- **方案**（`src/rag/`）：构建期用 teacher 模型 `gemini-embedding-001`（`RETRIEVAL_DOCUMENT`，768-d → MRL 截断 256-d → L2 归一化）嵌入 2,016 个 guide chunk，量化成 Int8 + per-row scale 后提交进 git（`guide-chunk-cache.{json,i8,scale.f32}`，合计约 665 KB）。词表蒸馏用 Model2Vec + Tokenlearn 配方（12 epochs Adagrad），把 teacher 的词级 embedding 蒸馏成一张 **29,165 词的静态查找表**（7.5 MB）。运行时：查询 → BM25 分词 → 查表 → 加权累加 256-d 行 → L2 归一化 → 线性余弦扫描 2,016 个 chunk 向量，**~30 µs**。量化保真度有硬验证：`Float32 → Int8` 余弦保真度 **> 0.999**。
- **Trade-off**：牺牲了词序与长距离依赖（查询向量本质是「词的加权和」），OOV 查询只能退回 BM25——这正是 hybrid 的必要性所在。换来的是：CLI 冷启动从「加载模型」变成「读文件」，npm 包不需要携带原生二进制，供应链面极小。
- **可迁移性**：**高**。

#### 2. Hybrid 检索 = 稠密余弦 + Okapi BM25 + RRF 融合

- **问题**：纯稠密检索会「模糊字面术语」——`user-invalid` 这种 API 名、`LCP` 这种缩写检索不到；纯 BM25 又丢掉语义。
- **方案**：① **Chunk Header 富化**——每个 chunk 的 embedding 输入前置 `title\nid (category)\nFeatures: <name>, <alias>, <slug>` 头，保证字面标识符的词法召回；② 稠密侧按 guide id 做 max-pooling（每篇指南保留最佳块）；③ BM25 侧同样按 id max-pooling；④ `reciprocalRankFusion([denseIds, bm25Ids], k=60)` 融合；⑤ **BM25 感知的降级门**——0.3 阈值只在 BM25 零命中时作为硬门。
- **关于 0.3 这个阈值**：代码注释给出了实测分布（`src/rag/search.ts:42-48`）——域内单词查询 top-1 余弦最低 0.475，域内多词查询跨度 0.636–0.899（中位 0.821）。0.30 被选为「非零下限」：保证 100% 域内查询都能用上稠密向量，同时让零向量 / 未知查询返回 `[]`。
- **Trade-off**：牺牲了可解释性（RRF 分数不直观，「为什么这条排第一」说不清），且两个索引都要维护。换来语义泛化与字面精确率兼得，OOS 查询还能干净拒绝。
- **可迁移性**：**高**。

#### 3. Grader 的双向校准铁律

- **问题**：一个只会「检测到 `<dialog>` 元素就算通过」的 grader，会让所有方案（包括什么都没做的）都满分。
- **方案**（`src/grading/run-grader.ts`）：每个 target 目录有多份 golden solution patch（`antigravity` / `jetski` / `claude` / `codex`）+ 一份 `zero-passrate.patch`（anti-pattern 基线，通常是空 patch）。正向校准要求 `unexpected == 0 && expected > 0`；反向校准要求 `passed == 0`。两者并行执行。golden patch 的生成被隔离——solution agent **只拿到 `task.md` 和 `guide.md`，永远看不到 `expectations.md`**。
- **Trade-off**：校准成本极高（每改一次 `expectations.md` 就要重跑所有 solution agent + grader）。换来的是「grader 是有意义的」这一前提。
- **可迁移性**：**高**。

#### 4. 构建期展开兼容性数据，指南正文不手写兼容性

- **问题**：如果指南正文里手写「Chrome 105+ 支持」，BCD 一更新就全部过期，252 篇指南要人肉同步。
- **方案**（`src/core/macros.ts`）：宏系统 `BASELINE_STATUS` / `FEATURE` / `FEATURE_FALLBACKS` / `FEATURE_ISSUES` / `INCLUDE` / `GUIDE_REF`，数据来自 `web-features` + `@mdn/browser-compat-data` + `features/pending-web-features.json`（`tmp-*` 待上游落地特性，带上游 issue 链接）。构建期展开，双 target（`skills-cli` 给 Agent 消费 / `devsite` 给网站展示），`GUIDE_REF` 会校验目标已发布且有标题，防死链。CI 里 `update-web-features.yml` 在上游更新后强制列出所有还在用 `tmp-*` ID 的文件。
- **Trade-off**：牺牲了「指南是纯 Markdown、任何工具都能直接读」的简洁性。换来兼容性数据永不腐烂。
- **可迁移性**：**高**。

#### 5. 评测 prompt 不提及指引 + 事后追踪是否真的用了

- **问题**：如果 prompt 说「请使用 modern-web-guidance 指南」，测出来的是「Agent 听不听话」，不是「指南好不好」。
- **方案**：`task.md` 是纯开发需求描述（「让我的图片加载更快」），README 明确写「*Prompts avoid naming APIs or features, testing whether the agent can naturally discover and apply the right guides.*」 配套 `src/harness/lib/guide-usage.ts` 从 `trajectory_summary.json` + 本地 `modern-web.log` 两路收集 Agent 实际检索过的 guide ID，并有**泄漏检测**（`hasTrajectoryGuideLeak`）——检查 Agent 是否通过读文件 / URL 泄漏答案，还专门排除了「只搜没开」和「打开失败」的探索步骤。
- **Trade-off**：Agent 可能不检索 → uplift 接近 0，无法区分「指南无用」和「Agent 没查」。靠 guide-usage 追踪 + 泄漏检测补上这个洞。
- **可迁移性**：**高**。

#### 6. 多层反过拟合护栏写进评测框架本身

- **问题**：用真实 telemetry 查询训词表，再用同一批查询评测 = 自我欺骗。
- **方案**：`wild-v2` 4,000 条查询 50/50 切分成 dev/test，**跨 split 不共享任何 stemmed bag-of-words**；`agent` 集 1,029 条查询按目标 guide ID 的**连通分量**分组（70 个 test cluster），**零 guide 共享**，bootstrap CI 按整个 guide cluster 重采样；训练时精确匹配 + stemmed 签名匹配双重排除所有评测 split；LLM judge（`gemini-3.8-flash`）用 69 条盲评人工标注验证过——quadratic-weighted Cohen's κ = **0.78**，binary hit agreement 93.3%。
- **可迁移性**：**高**。

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | Modern Web Guidance | addyosmani/agent-skills | MDN content | shadcn/improve | vercel-labs/agent-browser |
|------|---------------------|----------------------|--------------|----------------|--------------------------|
| Star / Fork | 14,469 / 527（分发仓） | 117,513 / — | 11,138 / — | — | 51,125 / — |
| 定位 | Web 平台 API + 兼容性 + 浏览器内评测 | 通用工程纪律（25 技能 + 9 命令） | Web 平台事实标准文档（人读） | UI 审美与组件改善 | Agent 浏览器自动化 |
| 内容粒度 | 252 个 `guide.md`（21 类目，官方发布口径 203 个场景 / 250 个特性） | 通用 skill | 按 API 组织的 API 参考 | UI 组件层 | 运行时能力 |
| 兼容性数据 | 有（构建期从 web-features / BCD 展开，按 `.mwgrc` 的 Baseline 目标裁剪 fallback） | 无 | 有（但为人类设计） | 无 | 无 |
| 效果证据 | 公开：每日 nightly，3 家 Agent × 有/无指引，214–215 任务 × 1673–1801 检查 | 无 | 无 | 无 | 无 |
| 厂商中立性 | 四厂商联合治理 + 独立专家席位 | 个人维护 | Mozilla + 社区 | 个人 / 小团队 | Vercel |
| 常驻 token 成本 | ~205 tokens（README 官方口径，按需检索） | 未核实 | N/A（人工查阅） | 未核实 | N/A |
| 与本项目关系 | — | 竞品（但正交） | 上游参照 / 对照物 | 部分重叠 | 正交（Agent 的手） |

### 差异化护城河

1. **信任护城河（最强）**：四厂商联合治理 + 独立专家席位 + 三层审阅制度 + 公开可审计的评测数据。这不是「Google 说 Web 该这么写」，而是「Chrome / Firefox / Edge / MDN 共同说」。竞品要复制，需要先说服 Firefox 和 Edge 加入——结构性壁垒。
2. **数据护城河**：`wild-v2`（4,000 条匿名真实查询）+ `agent` 集（1,029 条 nightly 查询）+ 2 个真实 base app + 约 2,000 个已校准 grader + 每天重跑的 pass-rate 面板。这套数据资产抄代码抄不出来。
3. **工程护城河（中等）**：蒸馏词表检索 + 非对称配方 + RRF + SNR 指标、OS 级沙箱、grader 双向校准、宏系统。这些是「能做，但要花 1–2 年做对」的活。
4. **生态护城河（较弱）**：star 数与社区规模远不及通用套件；多宿主支持（Claude Code / Codex / Antigravity / Cursor / Gemini / Copilot / JetBrains 等 70+ 端）做得好，但那是分发面而非锁定。

### 竞争风险

**最根本的风险：反向剪枝机制会自动让内容枯萎。** 项目的价值来自「模型的当前弱点」——如果无指引基线从 54% 涨到 80%，opportunity 就被压缩到不值得维护，这个项目写给自己的墓志铭就在路上了。这不是管理问题，是结构问题：**它为会移动的靶子写作**。

次要风险：模型厂商把 Web 平台知识直接内化进权重或 system prompt，不需要外部检索时，CLI 的价值归零。

**不太可能被替代的部分**：跨浏览器治理结构 + 公开的 A/B 评测方法论。即使模型变强，「如何证明知识注入对 AI 有效」这件事依然稀缺——**这才是这个仓库真正的长期价值所在**。

### 生态定位

- **在 Web 平台生态**：站在「规范（WHATWG/W3C）→ 浏览器实现 → 框架 → 开发者」这条链上的**知识翻译层 + 质量度量层**。它消费 `web-features` / BCD（站在规范之上），输出可直接运行的 Web 代码（在框架之下）。
- **在 AI 编码生态**：是「Agent Skill」范式的一个**垂直领域范例**——把领域知识做成 skill、用 eval 证明有效、用检索控制 token 成本、用项目配置管治理。云 SDK、数据库、后端框架完全可以照抄这套模板。
- **在评测生态**：更像是**评测基础设施供应商**，而不只是一个 skill 包。

## 套利机会分析

- **信息差**：**存在，且位置很明确**。5,791 star 的「热度」主要落在 `guides/`（内容层），而 `src/` 里那 20 万行工程——蒸馏检索、锥塌缩诊断、沙箱威胁模型、双向校准、声明式规则 DSL——**几乎没人写过深度解析**。第三方拆解也普遍停留在「这是什么产品」的层面。这是典型的「高热度资产 + 低曝光技术层」结构，套利空间在技术层而非内容层。
- **技术借鉴**：可迁移性最高的三件事——① **离线语义检索的蒸馏方案**（任何不能带模型的场景）；② **Grader 双向校准铁律**（任何 LLM 生成测试的系统）；③ **反向剪枝的 KPI 定义**（任何维护 LLM 知识库的组织）。这三件事可以下周就用在自己项目里。
- **生态位**：填的是「Web 平台规范 → AI 编码 Agent」之间那层空白。MDN 是给人的、agent-skills 是给通才的、它是给 Web 专精且要证据的。
- **趋势判断**：**在增长**。v1.0 发布当天 HN 首页 + Trending #1，star 从 2k 级跳到 5.8k；月 commit 从 2026-06 的 38 个回落到 2026-10 的 288、2026-11 的 313，说明热度不是发布效应而是团队产能的真实爬升。**后发优势明显**——它比通用 skill 套件晚两年入场，但用「有评测证据」直接跨过了信任门槛；2026-10 那次目录级 reorg 把它从「内容仓库」升级成「产品化 monorepo」，1.1 计划（per-feature 特性开关）说明路线图清晰。

## 风险与不足

1. **内容层的价值随模型能力衰减**——这是结构性的，不是执行问题。项目需要持续把「模型已经会了」的内容剪掉以维持 ROI，但也意味着它的内容资产会不断缩小。
2. **它管 API 正确，不管视觉品质**。第三方评价一针见血：**「Guides get the API right. They don't make the result look good.」** 官方 Issue #1415（仍 open）也承认这个断层：评测方法是「Playwright 断言某特性是否被正确使用」，而 UX 品质是涌现性的、难以写成断言的。
3. **「装了就用」是伪命题**。评测 prompt 刻意不提示指引，实测显示 Agent 常常不会主动调用 skill。真实收益需要「安装 + 显式提示 + Chrome DevTools 闭环」三件套齐备——这与 README 的乐观叙事之间存在落差。
4. **评测是厂商自证的**。对照设计（同一批任务、每晚、成对运行、真实浏览器断言）确实可信，但数据由项目方自己跑自己发，且 88% 的通过率不等于「代码正确」——无障碍与安全响应头仍需人工核。
5. **遥测默认开启且上报搜索查询文本**。README 明确采集「CLI 搜索查询」，这属于用户意图片段，虽声明不采集原始 prompt 并提供 `DISABLE_TELEMETRY=1` 退出，但对企业部署是需要在合规层面对齐的一项。
6. **`legacy-scan` 覆盖率只有约 20%**。这是有意的范围限定（无法静态检测的模式被归入 `needs-verifier`），不是未完成——但也意味着它不是「一键现代化」工具。
7. **文档密度极高，认知门槛不低**。`.mwgrc`、volatile 特性门禁、search/retrieve 两段式调用、Baseline 目标横幅——对新用户是需要消化的概念。
8. **代码库有明显的「生成物混进热点目录」问题**：历史上 `harness/results` + `evaluator/results` 累计 7,447 次改动其实是 eval 结果文件进出 git，`.gitignore` 已经把它们排除，但老提交仍在库里，会让任何基于 git 历史的分析得出偏差结论。

## 行动建议

### 如果你要用它

- **不要只装就完事**。至少要做到：安装 skill + 在 `CLAUDE.md` / `AGENTS.md` 里显式写明你的 Baseline 支持策略（哪些特性要 fallback、哪些不要）+ 配好 `.mwgrc`。第三方实测显示，不提示时 Agent 主动调用的比例并不高。
- **先读 `.mwgrc` 的语义再决定用不用 volatile 特性**。这个项目把「用不用新特性」做成了组织决策而不是模型决策，这恰恰是你应该自己拍板的事。门禁触发时按它给的指令走，不要绕。
- **用 `legacy-scan` 做体检，不要用 `--fix` 做改造**（它本来也没有 `--fix`）。输出里的 `Keep when:` / `Drop when:` rubric 就是给你（或你的 Agent）做判断用的。
- **和 `addyosmani/agent-skills` 一起用**，不冲突：一个管通用工程纪律，一个管 Web 平台 API。
- **对比同类方案**：如果你只需要「Web 最佳实践 prompt」而不在乎兼容性与证据，MDN + 自建 prompt 更轻；如果你需要「可度量的知识注入效果」，MWG 目前没有替代品。

### 如果你要学它

按这个顺序读，收益递减：

1. **`src/rag/README.md`** —— 整个仓库最高信息密度的文档。有数据格式表、训练配方、精确重训命令，以及「Why Retrieval is Asymmetric」一节对锥塌缩的完整诊断。这份文档本身就是可以直接抄的模板。
2. **`src/rag/search.ts` + `src/rag/bm25.ts` + `src/rag/train-query-words.ts`** —— 离线检索三件套。核心是「teacher 蒸馏成静态词表」和「BM25 感知的降级门」。
3. **`src/harness/lib/sandbox.ts`** —— OS 级沙箱。`appendRunDirMounts` 里 bwrap UID 陷阱的解法、`defaultExtraHiddenPaths` 里那份隐藏路径清单，都是踩过坑才写得出来的东西。
4. **`src/grading/run-grader.ts`（`testTargetGrader`）+ `src/authoring/dev-prompts.ts`** —— 双向校准铁律与「solution agent 永远看不到 expectations」的隔离。
5. **`src/analyzing/schema.ts` + `src/analyzing/rules/index.ts`** —— 声明式 matcher + 声明式 rubric + 双轴 triage + 精度准入阈值。这套规则系统设计可以直接搬到任何 lint / 静态分析项目。
6. **`src/core/feature-gates.ts` + `src/rag/retrieve.ts`** —— 「拒绝信息写成给 LLM 的行为契约」这一模式，迁移成本最低、见效最快。
7. **`AGENTS.md` + `docs/ATLS.md` + `GOVERNANCE.md`** —— 知识库内容规范与多厂商治理制度。如果你也在做团队级的 AI 知识库，这三份是治理模板。

### 如果你要 fork 它

- **换检索层**：把 `gemini-embedding-001` 换成你领域更合适的模型，注意保持「两侧共享 256-d 归一化空间 + task type 非对称」这个结构——不要为了省事改成对称。
- **扩 `legacy-scan` 覆盖率**：优先补 `needs-verifier` 那一档（当前 >50% 误报的那类），用 LLM Verifier 兜底，而不是硬写一条高误报率的静态规则。注意准入阈值：Post-Verifier Precision 必须 ≥ 90% 才能进默认发布集。
- **补 UX 维度的评测**：Issue #1415 仍未解决，可以从「把涌现性体验拆成可断言的分项」入手（比如「焦点管理是否正确」「动效是否尊重 prefers-reduced-motion」这类仍然可断言的子目标）。
- **改 volatile 策略**：把全局开关改成 per-feature 正是官方 1.1 的计划（Issue #3198），你可以提前做，但那意味着要背下「每一项特性的单引擎稳定时间 + 3 个月窗口」的维护成本。
- **别碰 grader 校准流程**：那是整个评测体系的信任根。改 `expectations.md` 之后一定要重跑完整校准，否则 dashboard 上的数字就不可信了。

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | https://deepwiki.com/GoogleChrome/modern-web-guidance-src （探测返回 429 限流，未能确认是否收录） |
| Zread.ai | https://zread.ai/GoogleChrome/modern-web-guidance-src （探测返回 403，未能确认） |
| 官方文档 | https://developer.chrome.com/docs/modern-web-guidance （`goo.gle/modern-web-guidance` 跳转至此） |
| Eval Dashboard | https://googlechrome.github.io/modern-web-guidance-src/ （实时有指引 vs 无指引通过率对比） |
| 分发仓（npm 包） | https://github.com/GoogleChrome/modern-web-guidance （14,469 star） |
| 关联论文 | 无（工程实践项目，非研究项目） |
| 在线 Demo | `npx modern-web-guidance@latest search "..."` / `retrieve` / `legacy-scan` |
