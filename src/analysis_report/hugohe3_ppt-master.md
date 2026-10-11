# GitHub 推荐：10 个月 59K stars：一个人用「AI Skill + SVG 中间语言」把 PPT 生成做到 PowerPoint 原生深度

> GitHub: https://github.com/hugohe3/ppt-master

## 一句话总结

把 AI 生成演示文稿从「一堆截图拼成的 PPTX」提升到「真可在 PowerPoint 里逐对象二次编辑、含 master/layout/native chart/动画/旁白的原生 PPTX」——用 SVG 作为 AI 友好的中间语言，一套**严格合约的 Python 编译器**负责把它翻译成 DrawingML。

## 值得关注的理由

1. **首创 SVG↔DrawingML 中间表示**：在「AI 直出 XML 太脆弱、AI 出图会丢失 native 编辑性」的两难中，**选定 SVG 子集作为 IR**，配 strict-contract + checker + 编译器，实现 master/layout/native chart 全栈可表达——竞品（Slidev/banana-slides/Presenton/PPTAgent）做不到 native depth 这个维度。
2. **把 Agent Skill 当「作品类型」持续经营**:HugoHe 一个人 10 个月写了 **2132 commits / 41 个版本**，GitHub 上 PPT 项目类型里罕见的工业级实践——所有产品边界都有对应 .md 文档，Non-goals/Capability Admission 显式划界，prompt 文件用 rule-owners.md 强制唯一归属。
3. **「Draft you keep editing」产品哲学**：让 AI 拿走 80% 的重复劳动，留 20% 给人在 PowerPoint 里收尾；通过 `pptx_to_svg --roundtrip` 实现 unchanged slides **byte-for-byte 还原**，解决了「AI 帮我改一两页」的最大恐惧。

## 项目展示

![论文阅读型 PPT — Attention Is All You Need](https://raw.githubusercontent.com/hugohe3/ppt-master/main/docs/assets/screenshots/preview_attention_is_all_you_need.webp)
*论文→结构化 PPT：多栏排版、章节锚点、引用块全部可二次编辑*

![企业级品牌模板 — China Telecom 2025 results](https://raw.githubusercontent.com/hugohe3/ppt-master/main/docs/assets/screenshots/preview_china_telecom_2025.webp)
*真实品牌 spec 落地：字体/色块/章节对象都继承自 brand template*

![视觉艺术风格 — Chinese breakfast atlas](https://raw.githubusercontent.com/hugohe3/ppt-master/main/docs/assets/screenshots/preview_pixel_breakfast_atlas.webp)
*pixel art 等 18 种 visual style × 5 种 narrative mode 二维组合，允许 `custom`*

> 完整 70 个分类样例见 https://hugohe3.github.io/ppt-master-examples/

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/hugohe3/ppt-master |
| Star / Fork | 59,567 / 4,697 |
| 关注者 | 116 |
| 代码行数 | 344,536（其中 Python 51.6% / SVG 33.5% / JSON 7.0%) |
| 文件数量 | 12,806 |
| 项目年龄 | 10 个月（2025-12-10 首次提交） |
| 总 commits | 2,132 |
| 最近推送 | 2026-10-08 |
| 开发阶段 | 密集开发（月均 ~213 commit，峰值月 621） |
| 贡献模式 | 独立开发者单人全栈（主作者占比 97.1%,Top 1 占比 95.6%） |
| 当前版本 | v6.7.0（共 41 个 tag，语义化版本，8.4 天/tag) |
| License | MIT |
| 话题标签 | ai-agent, powerpoint, pptx, presentation, slides, ppt |
| 热度定位 | 大众热门（中文 AI PPT 顶流，单作者独立项目头部） |
| 质量评级 | 代码[优秀] 文档[优秀] 测试[基本到充分] CI/CD[基本] |

## 作者视角：为什么存在这个项目

### 创始人/作者背景

HugoHe(Hugo He),1.9 年账号年龄，6 个公开仓库，粉丝 526。个人博客 hehugo.com。从「ppt-master / ppt-master-examples / hugo-skills / 70cityprice」等 6 个 repo 推断，作者是聚焦 **AI Agent + 内容自动化**的独立开发者——5 个次要 repo 平均几十颗星，而 ppt-master 一颗近 6 万，**差距悬殊**，这是他投入绝对重心的项目。自述「investment & finance professional who builds presentations every day」（见 `docs/why-ppt-master.md`)——典型 dogfooding 路径：每天 8 小时做 deck，把自己逼成最挑剔的用户。

### 问题判断

作者识别到三个独立卡点：

1. **AI 工具都没把 argument reasoning 做到版式前面**:Gamma/Slidespeak 等 SaaS 跳过论证与受众推理，直接出图——结果是「看起来不错但**内容空**」的 deck。
2. **AI 工具都没把 PowerPoint 原生对象模型当成 depth 目标**：主流方案要么出图、要么塞扁平模板，真正的 native depth（master/layout/preset shape/connector/freeform/animation/notes/narration/embedded font/equation）是个连续收敛的能力，需要长期投入。
3. **SaaS 把内容+模型+编辑权全部锁死在平台**：商务/咨询/政务用户的隐私诉求与平台利益冲突，没人有动力做"本地 AI 出原生 PPT"。

时机：2025 年底 Claude Code / Codex 等 agent 工具成熟，让 "AI 帮你跑完整工作流" 成为可能——**不是"AI 给你一个静态网页"，而是"AI 拿着工具串起多步工序"**。作者把这个洞察封装成一个可被任意 agent 加载的 Skill 包，而不是又一个 SaaS。

### 解法哲学

显式选了什么、显式没做什么，在 `docs/project-positioning.md` §8 Non-goals 与 §9 Capability Admission 里写得比 feature list 还清楚：

- **做 "draft you keep editing"**:AI 拿走 80% 重复劳动，留 20% 给人在 PowerPoint 里收尾。
- **Native depth 是 north star**：不是 feature list，是 **direction of travel**——每个 release 都朝 PowerPoint 自己的对象模型多迈一步。
- **Logic-first → Visual-design**:Strategist 阶段先核 5 种 narrative mode(pyramid/narrative/instructional/showcase/briefing)，再选 18 种 visual style;5×18=90 种可重用的设计基因组合。
- **Provider-agnostic**：任何 agent-capable 工具（Claude Code/Codex/Cursor）都能跑，任何兼容模型都可用——把工具做成 Skill 反而换来最大兼容性与独立性。
- **不做的事**：零配置 SaaS、通用 office agent、完整 PowerPoint clone、任意 SVG→PPTX 转换——主动划界，反而把产品定位钉得极准。

### 战略意图

5 个商业赞助商带头部（Kimi / PackyCode / APIKEY.FAN / RunAPI / APIMart）,lead $1k+/月 + service $500+/月，**成熟独立开源贡献者画像**。但不直接商业化（无 SaaS、无付费层），通过推荐位+使用门槛下降为模型/服务合作伙伴导流。这是「个人 IP 把 Skill 当成 agent 时代的作品类型持续经营」的样本——一个独立开发者用 v6.7.x 把"内容自动化"做成**可被一万种企业复用的引擎**，而非另一个 to-C 工具。

## 核心价值提炼

### 创新之处（按新颖度×实用性排序）

1. **SVG 作为 AI 友好的 IR（新颖 5/5，实用 5/5，可迁移 5/5)**
   - 用"被自家合约收窄的 SVG 子集"同时承载 AI 生成、人预览、机器编译 DrawingML 三方诉求；拒绝"裸 DrawingML"，也拒绝"位图替代"。**所有竞品都没同等深度的端到端 IR 设计**。

2. **「Draft you keep editing」产品哲学 + 字节保真 roundtrip（新颖 4/5，实用 5/5，可迁移 4/5)**
   - `pptx_to_svg --roundtrip` 让 unchanged slides byte-for-byte 还原，changed slides 只重画被编辑的对象——解决了"AI 帮我改一两页，其他别动"的最大 user pain。LibreOffice 想做 1:1 还原，ppt-master 把 round-trip 限制为"用户做计划的一部分"，哲学更聚焦。

3. **三 route + 多 profile 的可证明路由（新颖 4/5，实用 5/5，可迁移 4/5）**
   - 只承认 3 个真实 artifact lifecycle:Generate / Create Template / Edit Native PPTX。Beautify、Quick、Image-to-PPTX 都是 Generate 内部的 fidelity/generation profile。`workflows/routing.md` 是单一权威，hard rule 写"this file wins for route selection"——避免 LLM 在多入口间迷路。

4. **Narrative mode × Visual style 二维解耦（新颖 4/5，实用 5/5，可迁移 5/5）**
   - **5 种叙事骨架 + 18 种视觉风格 = 90 种组合**，允许 `custom`。McKinsey-Pyramid Principle 与品牌设计的成熟理念，与 AI 编排一起呈现非常少见。

5. **Brand / Style / Layout / Deck 四类模板 + segment-level ownership（新颖 4/5，实用 5/5，可迁移 4/5)**
   - 拒绝"全能 template"，把 reuse 切成 segment，组合而非合并；安装时"每 kind 至多一个，但多 kind 可并存"——一份 brand spec 就能跨 deck 复用，无需复制整个 ppt。

6. **`source_to_md` 输入归一化层双通道（新颖 4/5，实用 5/5，可迁移 5/5）**
   - 把 PDF/DOCX/EPUB/HTML/LaTeX/XLSX/PPTX/URL 一律归一为 markdown（内容契约） + 抽取结构化 facts(.identity / .slide_library / source_profile.json)。下游 Strategist 只看一份"内容契约",PPTX 的几何/图表/SmartArt 不被 markdown 化糊掉。

7. **Prompt 一等公民的工程化（新颖 5/5，实用 5/5，可迁移 5/5）**
   - `docs/rules/prompt-layers.md` + `ownership.md` + `rule-owners.md` 三件套把规则所有权写死。每个跨文件规则只能有一个 owner；其余文件用 `plans-core.md §6.2` 引用。prompt 文件只写 craft + 模型写入的最小合约，enforced grammar 全部放到 `scripts/docs/`——6.7 版本下还能大规模不腐烂，是工程化的证据。

8. **`attribution_guard` 完整性门控（新颖 5/5，实用 4/5，可迁移 3/5）**
   - 每个 CLI 入口第一行校验 LICENSE / SPONSORS / 必需 gate file;SHA 不匹配直接拒绝执行。Skill 包分发时抗裁剪，商业赞助模型必需。

9. **Fail-closed 合约 + 三输入态（Authoring/Compat/Invalid）（新颖 3/5，实用 5/5，可迁移 5/5)**
   - AI 写出"语法对但语义不在 DrawingML 里"的 SVG（masks/styles/foreignObject/animate）由 checker 直接 error 阻断；用户不会被静默伪造产物。canonical/compatible/invalid 三态分流，export 行为完全可预测。

10. **Canvas 单位解耦:viewBox 用 px(1 SVG px = 9,525 EMU)（新颖 5/5，实用 5/5，可迁移 5/5)**
    - AI 不擅长算 EMU，人也不擅长，浏览器不直接渲染 EMU。在中间语言里固定用 px，只在 export 时量化一次——任何 AI IR 都该把"内部空间单位"和"输出格式单位"解耦。

### 可复用的模式与技巧

1. **AI-friendly IR + 确定性编译器**：用一个「AI 训练数据充足 + 与目标格式同维度」的 IR，配套严格合约 + checker + 编译器。适用:**AI 输出 PPTX/DOCX/XLSX/PDF 流程**。
2. **单一权威路由文档 + 三顶层 route + N profile**：多入口 Skill / 多 workflow 工具包不要让多个 entry 文件竞争决定权。
3. **Roles-as-context 的统一串行 agent**：全局决策上下文不要切 sub-agent；角色通过 markdown 上下文切换，而不是拆线程。适用：需要全局一致性的 AI 生成流水线（否则视觉一致性会崩）。
4. **Two-tier runtime（default + quick）而非 flag-only**：把"完整 SOP"与"快速通道"做成两个名字固定的 profile，中间用 hard rule 隔离。Quick 失去持久化 design history 但换真心适合一次性快速出片。
5. **Source normalization 双通道（内容契约 + 结构化事实）**：输入爆炸场景下不要让所有输入变成同一种东西；markdown 当 content contract,intake JSON 当结构化事实。
6. **Source-preserving mutation(roundtrip)**：不重画已有文件；只 patch 用户计划的一部分，其他 byte-for-byte。适用：任意"AI 修改既有文件"的工具。
7. **4 类模板 + segment-level ownership**：把 reuse 切成 segment，组合而非合并；每段独立 ownership。适用:design system / brand automation / i18n 模板。
8. **Fail-closed contract**:AI 输出涉及工业格式时，异常必须 error-block，不允许 silent drop / silent rewrite。
9. **Integrity gate(SHA + 必需文件清单）**:Skill 包/插件分发时，加入完整性 hash + 必需 file 名单，在 CLI 入口调用。适用：任何会分发、被裁剪的 Agent Skill / Plugin。
10. **Prompt 一等公民 + rule-owners 文档**：跨文件共享规则必须单 owner;prompt 文件只写 craft + 最小合约；enforced grammar 放脚本侧。

### 关键设计决策

| 决策 | 问题 | 方案 | 可迁移性 |
|------|------|------|----------|
| 用 SVG 作 IR | AI 不能可靠写 DrawingML，出图会丢 native | SVG 子集 + 严格合约 + 编译 | 高 |
| 三 route + profile | 路由爆炸导致 LLM 选错 | routing.md 是唯一权威 | 高 |
| 单 agent 串行 page-by-page | sub-agent 拿过期快照，视觉一致性崩 | 角色 = markdown 上下文切换，不拆线程 | 极高 |
| Quick 与 Default 双 runtime | 用户同时需要"10 分钟"和"1 分钟" | hard rule 隔离，而非 flags | 高 |
| Canvas 用 px 而非 EMU | AI/人/浏览器都不擅长 EMU | viewBox 中间锁 px,1 SVG px=9,525 EMU | 极高 |
| 4 类模板 + segment ownership | "换品牌色"与"完全结构复用"是两种不同需求 | 组合而非合并，每段独立 owner | 高 |
| `attribution_guard` 完整性 | Skill 包分发时易被裁剪 | SHA + 必需 gate file，失败 stop | 中 |
| `pptx_to_svg --roundtrip` 字节保真 | 用户只改第 3 页，其他别动 | 不变页 byte-for-byte，编辑页只重画被改对象 | 中高 |
| Prompt 一等公民 + rule-owners | 多人改 prompt 文件最常见的腐烂 | 单 owner + 链接 + section 编号引用 | 极高 |
| Sidecar 分层（notes/audio/animations/native-payloads） | SVG 是 2D 矢量页，把行为塞进去跨界又失真 | 单独 sidecar,export 时并入 PPTX package | 极高 |

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | ppt-master | Presenton | PPTAgent | banana-slides | python-pptx | Slidev |
|------|------------|-----------|----------|---------------|-------------|--------|
| Stars | 59.6K | ~4.8K | ~4.2K | ~12K | n/a(lib) | ~43.8K |
| 输出形式 | 真 PPTX native | 真 PPTX native | 真 PPTX | 截图型 PPTX | 真 PPTX 自写 | Web 演示 |
| 可编辑深度 | 高（master/layout/native chart/anim/narration） | 中 | 中 | 低 | 极高（纯库） | 低（导出为图） |
| AI 推理深度 | 高（argument reasoning） | 中 | 高（学术） | 中 | 无（库） | 无 |
| 自托管/隐私 | 是（本地 + 任意 LLM） | 是 | 是 | 是 | 是 | 是 |
| 多语种含 RTL | 是（13+） | 中 | 中 | 中 | 任意 | 中 |
| 输入归一化 | PDF/DOCX/EPUB/XLSX/PPTX/URL 全部 | 部分 | 部分 | 截图 | 库 | Markdown |
| 进入门槛 | 高（需 agent + Python） | 低（浏览器一键） | 中（需安装） | 低（口语） | 高（写代码） | 中（需 Vue 知识） |
| 模板生态 | 70 templates + 70 examples + 987 pages | 弱 | 学术 | 中 | 无 | 多（主题） |

### 差异化护城河

1. **Native depth 不可复制**:v6.7 下 master / layout / native chart / native table / native equation / animation / notes→audio / 6 relationship atoms 全栈覆盖，接近 PowerPoint 全对象模型。
2. **逻辑层（narrative mode × visual style）**：主流 SaaS 几乎不做。
3. **Skill-as-output 模型**：让用户在已有 agent 工具中复用，反而是最强渠道。
4. **强合约 + fail-closed + source-preserving**：让 AI 输出变成"可信可预测的 draft"而非"惊喜或惊吓"。

### 竞争风险

- **SaaS 化对手（Gamma / 2Slides）** 以"浏览器一键 + 实时协作"占领普通用户心智。
- **Microsoft Copilot for PowerPoint** 本身把"AI 出 PPT"塞进 PowerPoint 内，可能吃掉中端用户。
- **GPT-Image-2 等图像模型** 变强后，"截图型 PPTX"门槛继续下降。
- **锁定 Codex 的 Image-to-PPTX profile** 是 host 风险。

### 生态定位

**不是 SaaS、不是 IDE Plugin、不是 LLM、不是 PPT 替代品**——是"在 agent 里跑、可被 vendor、可被分发"的工作流；占住"AI 时代的 native depth + Skill distribution"这一差异化象限。

## 套利机会分析

- **信息差**:6 万星的项目在中文圈已是顶流，但其**架构与工程方法论**（SVG-as-IR、prompt 一等公民、4 类模板 segment ownership、attribution_guard）对绝大多数 AI 工具开发者是陌生领域——**这是"明星项目的设计资产"被低估的一面**。
- **技术借鉴**:SVG-as-IR 模式可以套到海报印刷品、Keynote 转换、Excel→图表自动生成等场景；Roles-as-context 串行 agent 模式可以套到任何需要全局一致性的 AI 流水线；Source-preserving mutation 可以套到任意"AI 编辑既有文件"的工具。
- **生态位**:Agent Skills 这个新品类（Claude Code / Codex / Cursor 都支持）在 2025 年底才成熟，ppt-master 是其中第一个把"复杂长流程"做到工业级的样本——意味着"AI Skill 化的内容自动化"是个全新生态位，ppt-master 是定义者之一。
- **趋势判断**:Agent Skills 生态会持续扩张，但「PPT 这个特定垂直」已被 ppt-master 钉住；真正的机会在"将同一架构泛化到其他文档自动化场景"(Word/Excel/Notion/Confluence/邮件）。

## 风险与不足

1. **单作者风险**:Top 占比 97.1%,**bus factor = 1**；若作者停更，整个维护节奏立即崩。
2. **测试与重构几近为零**:Refactor 0.5% / Test 0.5%（按 commit 类型计）；虽然算法层有 699 个 unittest 方法，但 prompt 驱动层几乎没有自动化 E2E，作者用 dogfood + issue 反馈补足，这是可扩展性风险点。
3. **CI/CD 缺失**：仓库无 `.github/workflows/`,release 没有自动化测试触发；版本号手写在 SKILL.md metadata。
4. **进入门槛高**：需要 Claude Code/Codex/Cursor + Python + 一段学习曲线；普通用户会用，但商务非技术用户用不了。
5. **Image-to-PPTX 锁定 Codex**：把"截图→可编辑 PPTX"这条路径绑死在 Codex 一个 host，是潜在风险。
6. **平台风险**:Microsoft Copilot 持续强化，如果它做到 native depth,ppt-master 的"自托管 native 优势"会被压缩。

## 行动建议

### 如果你要用它

- **你是每天做 deck 的咨询/金融/教育/政务从业者**：直接用 Default 流程，接受 10-20 分钟/10 页的速度，把 AI 输出当 draft 在 PowerPoint 里收尾。
- **你是品牌/模板厂商**：用 Create Template 路径把 brand spec / style / layout 蒸馏成 4 类模板资产，跨 deck 复用。
- **你要批量把旧 PPT 改 1-2 页**：用 Edit Native PPTX 路径，byte-for-byte 不变是核心承诺。
- **不要用它做"截图型 PPTX"**：那是 banana-slides / Gamma 的战场，ppt-master 的存在意义是 native depth。

### 如果你要学它

按这个顺序读，不要从 Python 代码开始：

1. `docs/what-is-ppt.md`（认知框架前置）
2. `docs/why-ppt-master.md`（价值主张与诚实自陈）
3. `docs/project-positioning.md`(Non-goals 与 Capability Admission)
4. `skills/ppt-master/SKILL.md`（入口 + 路由）
5. `skills/ppt-master/workflows/routing.md`（单一权威路由）
6. `skills/ppt-master/references/shared-standards-core.md`(SVG 合约）
7. `skills/ppt-master/scripts/svg_to_pptx/drawingml/converter.py`（编译器）
8. `docs/rules/{prompt-layers,ownership,rule-owners}.md`(prompt 工程化三件套）

### 如果你要 fork 它

最有价值的三个改造方向：

1. **SVG-as-IR 泛化**：把同一架构应用到 Excel chart 生成、Word doc 生成、Keynote 转换——核心是**"找 AI 训练数据足够的、与目标格式同维度的中间语言"**。
2. **多 host 适配**：把 Image-to-PPTX 的 Codex 锁定解开，扩展到 Claude Code / Cursor / 任何 agent。
3. **加 CI/CD + 自动 E2E**：把 dogfood 流程纳入 unittest，补齐 prompt 驱动层的盲区。

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | [已收录](https://deepwiki.com/hugohe3/ppt-master) |
| Zread.ai | [已收录](https://zread.ai/hugohe3/ppt-master) |
| 关联论文 | 无（项目本身不是学术研究，但内部引用 Mayer/Kosslyn/Yates-Orlikowski 等认知科学原文） |
| 在线 Demo | [70 个分类样例](https://hugohe3.github.io/ppt-master-examples/) |
| 作者博客 | [hehugo.com](https://www.hehugo.com/) |