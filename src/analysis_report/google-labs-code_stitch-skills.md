# GitHub 推荐：4,724 行代码凭什么拿到 9,942 星：Google Stitch 技能包的提示词工程

> GitHub: https://github.com/google-labs-code/stitch-skills

## 一句话总结
Google 官方把 Stitch 这个 AI 设计画布的能力封装成 16 个 Agent Skill，用**「可执行断言 + 门禁判据 + 接力棒协议」**把散文式提示词改造成可判定的工作流，是目前最完整的一份 Google 官方 Agent Skill 写作范式样本。

## 值得关注的理由

1. **提示词工程被当产品做了**：全仓 4,724 行代码，注释 5,292 行，16 个 SKILL.md 独占 3,243 行 Markdown。真正的资产不是代码，是「怎么把风格规则写成 Agent 能执行的断言」——这套分层法（能自动判定的写脚本 / 半自动的写清单 / 剩下的才写散文）可以原样搬走。
2. **4,724 行代码换来 9,942 星 + 1,299 fork + 47.8 万次安装**：skills.sh 上 18 个技能累计安装 477.8K，安装量与 star 比约 48:1，说明真实使用深度远超 star 数暗示的水平。这类「提示词即产品」的仓库在中文社区还很少被拆解。
3. **它是一个反常的商业姿态样本**：Google 把 proprietary 的 Stitch 后端开放给了 Claude Code / Cursor / Codex 三个竞争对手的 Agent——v0、Anima、Galileo、Builder.io 都没这么做。读懂为什么，比学会用它的价值更大。

## 项目展示

![Stitch 官方 Hero 视觉](https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Stitch_Keyword_Hero_Visual.width-200.format-webp.webp)

Stitch 官方 hero 视觉，本仓库所有技能都围绕这个画布的能力展开（图片来源：blog.google 官方博客）

![AI-native 无限画布界面](https://storage.googleapis.com/gweb-uniblog-publish-prod/images/ainativecanvas.width-1200.format-webp.webp)

Stitch 的 AI-native 无限画布：`generate-design` 技能里四种 flow（text / image / edit / variants）对应的就是画布上的四种操作

![DESIGN.md 格式示例](https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Inline_image_-2.width-1200.format-webp.webp)

DESIGN.md 是本仓库 skills 的产物格式，也是整个组织矩阵里最值钱的那块地基

> README 本身 0 张图片 0 个视频，仓库内也没有任何截图。上面的素材全部来自 Google 官方博客的静态资源桶（已逐一验证可访问）。

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/google-labs-code/stitch-skills |
| Star / Fork | 9,942 / 1,299（fork/star 13%，高粘性的「被改造型」社区） |
| 许可证 | Apache License 2.0（但 README 明确「非官方支持的 Google 产品」，不适用 Google OSS 漏洞赏金计划） |
| 代码行数 | 4,724（TypeScript 53.4% / TSX 20.2% / JSON 15.1% / Python 5.0% / Shell 3.3% / JavaScript 3.1%），另有 8,018 行 Markdown |
| 项目年龄 | 10 个月（2026-01-16 首次提交） |
| 开发阶段 | 低维护（2026-08-17 后零提交，距今 92 天；近 30/90 天均 0 commit） |
| 贡献模式 | Google 内部工程师 + 社区协作（19 位提交者，主作者 jilinxia 占 46.6%） |
| 热度定位 | 大众热门（star 维度已是头部，安装量维度 477.8K 远超 star 隐含价值） |
| 质量评级 | 代码[良好] 文档[优秀] 测试[无]（但有 CI 对 gold-standard 示例做断言） |

## 作者视角：为什么存在这个项目

### 创始人/作者背景
作者是 **Google Labs Code** 这个实验性开源组织（不是 Google 官方支持的产品，不适用 Google OSS 漏洞赏金计划）。组织的仓库矩阵就是一条完整的「Agent 时代工具链」：`design.md`（28,915 star，DESIGN.md 格式规范）→ `stitch-skills`（本仓库，工作流层）→ `stitch-sdk`（1,856 star，可编程层，11 月仍在推送）→ `stax`。另有 jules-sdk / jules-skills / jules-awesome-list 构成 Jules 代理线。

个人贡献者里两个名字最能说明问题：**David East**（前 Firebase DevRel 负责人，Google 内部 MCP / Agent Skills 方向布道者，提交 13 次）与 **Dion Almaer**（前 Google Engineering Director、Mozilla Labs Bespin 作者、Pragmatic Ajax 合著者，提交 5 次）。这两个人在仓库里留下的痕迹非常直白——README 主打「follow the Agent Skills open standard」，`.agents/plugins/marketplace.json` 用 OpenAI/Codex 的 marketplace schema，`.codex-plugin/plugin.json` 用 Codex 的 plugin schema，`plugin.json` 用通用 schema：**三份 manifest 服务三种宿主的分发格式**。叙事主体是「开放标准 + 跨厂商兼容」，而不是 Gemini 独占。

### 问题判断
Google 看到的缺口不在「AI 会不会画 UI」，而在**设计意图没有 agent-readable 的载体**。

当时的业界做法是把风格指南粘进 prompt。但唯一有研究数据支持的结论恰恰相反——「给 agent 现成组件」优于「把 style guide 粘进 prompt」。所以 Google 把 `DESIGN.md` 从 Stitch 的内部特性升格成了独立仓库（4 月开源，28.9K star），让它成为跨工具规范；本仓库则是这份规范的**生产者与套用器**：`manage-design-system` 管项目级 token、`extract-design-md` 从源码反向抽取、`taste-design` 提供一套预设品味、`design-md` 做项目分析。

时机也在这里：Stitch 本身在 2026-03-18 官方博客宣布 MCP + SDK + skills 三件套，2026-05-20 I/O 上线实时设计代理与多人协同。skills 是这套分发里唯一能让**编码 Agent**（而不是设计师）直接驱动设计工作流的那一环。

### 解法哲学
仓库自称 **「Executable enforcers」**（可执行执法者），这是整套方法论的题眼。风格规则不能只是散文，因为模型会无视散文。三层证据链：

- `resources/style-guide.json` —— 从当前项目 HTML `<head>` 反解出的 token 快照
- `scripts/validate.js` —— SWC AST 遍历断言：组件有 `[Name]Props` 接口、`className` 里没有硬编码 hex
- `resources/architecture-checklist.md` —— 散文规则里无法自动判定的部分（monolithic 文件、逻辑未抽 hook、数据未解耦），退化为人工核对清单

作者**明确不做什么**：不做生成模型（仓库 0 行模型代码，全部能力走 Stitch MCP server）；不做 UI 按钮（官方称之为「vibe design」——从意图而非线框起步，把 AI 当交互式回音板，所有技能都被设计成 Agent 可调用的模块）；不做全托管（脚本要在用户机器上、由 Agent 通过 Bash 现场执行）。

### 战略意图
组织矩阵是一条完整链路：`design.md`（格式规范）→ `stitch-skills`（工作流层）→ `stitch-sdk`（可编程层）→ `stax`。本仓库自 2026-08-17 停更，而同组织的 design.md（11-06）、stitch-sdk（11-05）、stax（11-13）都还在推送——**这不是组织收缩，是这一条线被降级**。它被定位为 v1.0 的稳定快照，结构冻结、生态继续演进。

真正的战略意图藏在「把 Stitch 后端开放给竞品 Agent」这个反常姿态里：**Google 想要的是 Agent Skills 成为事实标准，而成为标准的唯一办法是让竞争对手的 Agent 也用它。** 本仓库是标准之争的棋子，不是产品护城河。

## 核心价值提炼

### 创新之处

1. **把散文式提示词降级为三段证据链**（新颖度 4/5 | 实用性 5/5 | 可迁移性 5/5）
   不是把提示词写得更长，而是**把它换成可判定形式**：token 快照 → AST 断言 → 人工清单。配 Phase GATE 强制「必须先更新 token 快照才能进入下一阶段」。任何「Agent 生成代码需要质量约束」的场景都能直接抄。

2. **Baton 文件：跨 Agent 迭代的状态传递协议**（新颖度 4/5 | 实用性 4/5 | 可迁移性 5/5）
   `.stitch/next-prompt.md` 是个带 YAML frontmatter（`page: <name>`）+ 正文的文件，正文强制包含 **DESIGN SYSTEM (REQUIRED)** 块（从 DESIGN.md Section 6 复制）和编号页面结构。每次迭代读 baton → 查 SITE.md（sitemap 防重复 + roadmap 选题）→ 生成 → 集成 → 更新 SITE.md 的 `[x]` 标记 → 写下一个 baton。最后一步被标为 **Critical**。这是「文件即状态机」，可用于任何需要跨会话续跑的多步工作流。

3. **Puppeteer 快照的「脏数据手术」**（新颖度 3/5 | 实用性 5/5 | 可迁移性 4/5）
   `snapshot.ts` 是全仓最长的脚本（1,470 行），真正难的都不是教科书内容：**CSSOM 物化**（Vite dev 模式与 CSS-in-JS 注入的样式在 `<style>` 的 textContent 里根本拿不到，必须遍历 `document.styleSheets` 重新序列化）、六家框架的 dev overlay 清除（vite-error-overlay / nextjs-portal / webpack-dev-server / parcel / v-inspector / VeloUI）、同源 iframe 原生内联并提升 `data-theme` 等 html 属性、esbuild 产物的 `__name` helper mock、**全高度截图不是 `fullPage: true` 而是扫描所有滚动容器找最大 `scrollHeight`** 再把 `vh`/`h-screen` 高度锁死为 `auto`。

4. **SSRF + TOCTOU + 重定向循环三重防护**（新颖度 3/5 | 实用性 4/5 | 可迁移性 4/5）
   `extract_inline_html.ts` 要从用户 HTML 里抓 URL 发起请求，于是拦截 127/8、10/8、172.16/12、192.168/16、169.254/16 与非 http 协议，限制 5 次重定向，失败降级为 1×1 透明 GIF。`post_process.ts` 用同一个 fd 做 open/fstat/read/write 消除 TOCTOU。**处理用户输入的工具做到这个程度，成本并不高。**

5. **`upload_to_stitch.py` 的「绕过模型输出上限」论证 + 零依赖约束**（新颖度 3/5 | 实用性 5/5 | 可迁移性 5/5）
   文件头用具体数字论证必要性：53KB PNG 的 base64 约 71K 字符，而 MCP 工具参数属于模型输出，受 ~16K token 上限截断——所以文件上传必须走脚本绕过模型。技术上只用 Python 标准库（`urllib.request` + `base64` + `argparse`），`certifi` 是可选降级。**深层理由是部署约束**：脚本要在用户机器上由 Agent 通过 Bash 现场执行，可能是个只装了 Python 的干净沙箱。判据值得抄：**必经路径的脚本零依赖**。

6. **AST 断言替代正则规则**（新颖度 3/5 | 实用性 5/5 | 可迁移性 5/5）
   `validate.js` 用 SWC（Rust 实现，比 @babel/parser 快且无重运行时依赖）解析 AST，手写 `walk()` 找 `TsInterfaceDeclaration`（id 以 `Props` 结尾）与 `className` 中的 hex 色值（`/#[0-9A-Fa-f]{3,8}\b/`）。commit `9a6ea47` 修过一次性能坑：原实现会递归进每个节点附带的 `span` 元数据（`{start,end,ctxt}`），访问对象数是 AST 节点数的 2–4 倍，修复后降到 25–46%。

7. **`taste-design` 把「品味」编码化为四条 dial + 25 条禁令**（新颖度 4/5 | 实用性 3/5 | 可迁移性 3/5）
   Creativity / Density / Variance / Motion Intent 四条 1–10 数值轴，各配语义刻度（「1–3 = Art Gallery Airy, 4–7 = Daily App Balanced, 8–10 = Cockpit Dense」），默认 9/5/8/6。禁令部分包含非常具体的工程细节：premium 场景禁用 `Inter`、通用 serif 禁用、用 `min-h-[100dvh]` 而非 `h-screen`（iOS Safari 地址栏跳变）、只用 `transform`/`opacity` 动画、禁 `calc(33% - 1rem)` 这类 flexbox 百分比 hack。其中一条把「反 AI 味」从审美扩展到了诚信层面——**禁止编造指标数据**，要求用 `[metric]` 占位符。

8. **框架差异隔离到 `references/`，主技能退化为路由器**（新颖度 3/5 | 实用性 4/5 | 可迁移性 5/5）
   `extract-design-md` 要支持 React/Vue/Svelte/Angular/纯 CSS 五种栈。正文只放一张「Signal File → Framework」探测表，然后说「Consult the appropriate reference」，5 份 `references/*.md` 各 101–161 行。主技能**从「知识百科」变成「框架无关的路由器」**。

### 可复用的模式与技巧

| 模式 | 说明 | 适用场景 |
|---|---|---|
| 三段式规则降级 | 能自动判定的写脚本 → 半自动的写清单 → 剩下的才写散文 | Agent 质量约束体系设计 |
| Phase GATE 门禁 | 每阶段开头用引用块声明唯一判据，措辞是 AND 连接的可观测事件 | 多阶段 Agent 工作流 |
| Anti-patterns 负面清单 | 每阶段配一份 ❌ 清单，堵住「看起来跳过了」的路径 | 阻止 Agent 静默降级行为 |
| 必经脚本零依赖 | 关键路径只用标准库，可选路径才引重依赖 | 下发到用户机器执行的工具 |
| Baton 文件协议 | YAML frontmatter + 强制内容块的 markdown 做跨迭代交接 | 长任务续跑、批量迁移 |
| Gold Standard 双用示例 | 同一份 examples 既作 few-shot 素材，又作 CI 回归基准 | 生成类 skill |
| AST 断言替代正则 | 用 SWC/Babel AST 检查代码风格约束 | 代码生成类 skill |
| 编排者技能 | 薄技能只做「委派 + 相对路径引用」，不重复实现子能力 | 组合式 skill |
| 单一事实源 + 冲突禁令 | 指定唯一 token 权威源，显式禁止别处重复 | 设计系统 / 主题管理 |
| 能力探测式降级 | `list_tools` 探测可选 MCP，缺失则跳过，不硬依赖 | 可选增强能力 |
| 溯源标记 | 上传时打 `generated-by`，让服务端能区分资产来源 | 多来源资产的服务端治理 |

### 关键设计决策

**决策 1：用 `.stitch/` 目录做跨技能的共享状态协议**

- 问题：四个技能要共享设计系统，`stitch-loop` 要跨迭代保存状态
- 方案：固定目录约定 `.stitch/{DESIGN.md, SITE.md, next-prompt.md, metadata.json, designs/}`，每文件配一份 schema 文档
- Trade-off：与用户项目文件混在同一工作区，可能误提交；无版本化 / schema 校验器（`baton-schema.md` 里的校验规则只是手工 checklist 不是脚本）
- 可迁移性：高

**决策 2：`code-to-design` 用「编排者」模式而非自己实现**

- 问题：extract-static-html → extract-design-md → upload-to-stitch 三步有先后依赖，重实现必然重复
- 方案：正文只有 78 行，核心是一句「This skill orchestrates three other skills in sequence」，每步说「Delegate to the X skill... Read [skills/X/SKILL.md](../X/SKILL.md)」，跨技能引用用相对路径链接保证目录整体移动后仍有效
- Trade-off：依赖多个技能同时安装（README 明确警告 inter-dependencies）；某个子技能改路径会打断编排
- 可迁移性：高

**决策 3：`generate-design` 强制「生成提示词中禁止包含颜色 / 字体 token」**

- 问题：prompt 里既说「蓝色按钮」又说「主色 #0EA5E9」，Stitch 会用 prompt 的颜色覆盖项目级 design system，导致同项目内颜色漂移
- 方案：技能正文用 `> [!CAUTION]` 显式警告——**生成提示词里不要放 hex / 字体名 / 色板 / 圆角值**，这些由 manage-design-system 在项目级施加，重复即冲突；但 **edit 流程允许 hex**（精确微调需要）。同时把「检查项目是否已有 design system」作为流水线第一步
- Trade-off：Agent 需要跨技能理解「生成」与「编辑」在 token 语义上不同，这个区分靠自然语言而非类型系统保证
- 可迁移性：高

**决策 4：`name` 字段用 `stitch::` 命名空间，且与目录名不一致**

- 问题：`stitch::generate-design` 的 name 与目录 `generate-design` 不匹配
- 方案：命名空间用于冲突规避（避免与用户自写同名 skill 或其他插件的 `generate-design` 撞名）。但代价被转嫁给用户——OpenCode 要求 skill `name` 必须是小写 kebab-case 且与目录名严格匹配，README 只好写明「Skills that use `stitch::…` names need the `name` field and folder renamed before OpenCode will load them」。16 个 skill 里 9 个用了 `stitch::` 前缀，另外 7 个（remotion / shadcn-ui / react-vite-dashboard / design-md / enhance-prompt / site-md / stitch-loop）没加——**命名规则本身不一致，且没有文档解释**
- Trade-off：命名冲突风险 vs 分发器兼容性。仓库的答案是「在 README 里写清楚，让用户自己改」
- 可迁移性：高（**作为反面教材**）——跨宿主分发时，标识符格式必须由最严格的宿主定义，不能由作者按需命名

**决策 5：三份 plugin manifest 服务三种宿主**

- 问题：Codex 用 `.codex-plugin/plugin.json`（需要 `skills: 「./skills/」` 和 `interface` 展示字段），Claude Code / Cursor 用 `npx plugins` 读 `plugin.json`，Codex marketplace 用 `.agents/plugins/marketplace.json`
- 方案：三份文件并存，`plugin.json` 与 `.codex-plugin/plugin.json` 内容基本重复，后者多了 `interface`（displayName / defaultPrompt 数组 / brandColor / capabilities）；`marketplace.json` 声明三个 plugin 的 local path 与 `policy.installation: AVAILABLE`
- Trade-off：三处手工同步（改 description 要改两个文件），无生成脚本。skills.sh 上已出现 README 未收录的 `site-md` 技能，说明线上版本已漂移
- 可迁移性：中（思路通用，字段名是各家私有格式）

**决策 6：`extract-static-html` 三段式拆分**

- 问题：「把一个网页变成自包含 HTML」有三种输入形态（JSX 源码 / 活着的 dev server / 已构建产物），失败模式完全不同（JSX 解析失败 / dev overlay 污染 / CSS 图片外链），**塞进一个脚本会变成 if-else 泥球**
- 方案：`extract_inline_html.ts`（离线，Babel AST 解析 JSX → 渲染 HTML，找 `export default` 的 return，失败则回退到「最大 JSX 树的 return」）→ `snapshot.ts`（在线，Puppeteer 抓全渲染 DOM + 脏数据手术）→ `post_process.ts`（只处理本地相对路径的图片，远端已在快照阶段内联）
- Trade-off：三份脚本间有代码重复（`extractCssUrls` 在三处各抄了一遍）——因为技能目录要能独立分发，不能跨目录 import
- 可迁移性：中（思路通用，代码不会直接复用）

## 竞品格局与定位

### 竞品对比矩阵

先回答一个关键判断：**本仓库的真正竞品不是「另一个把设计转代码的 Agent Skill」，而是 Stitch 这个产品本身的其他入口 + Figma 生态的 MCP 路线。** 理由：仓库内 0 行生成模型代码，全部能力通过 Stitch MCP server 获取，本质是「Stitch 的官方 Agent 端分发层」。

| 维度 | stitch-skills | Figma MCP（官方） | Figma-Context-MCP | superdesign-skill | stitch-sdk（同组织） |
|------|-------------|------------------|------------------|-------------------|--------------------|
| Star / 体量 | 9,942 | 官方 MCP 非独立仓库（指南仓库 ~2.2K） | 16,228 | 1,020 | 1,856 |
| 数据源 | Stitch AI 画布 | Figma（团队 system of record） | Figma（只读布局） | 无（纯提示词技巧） | Stitch API |
| 方向 | 双向（code↔design） | 双向 | 只读 | 单向 | 双向 |
| 设计契约 | DESIGN.md（git 可 diff 的文本） | Figma 变量（云端不可版本化） | 无 | 风格 skill | DESIGN.md |
| 质量验证 | validate.js AST 断言 + 清单 | Code Connect 确定性映射 | 无 | 无 | 单元测试 |
| 分发 | Codex/Claude Code/Cursor + Antigravity/OpenCode 手工装 | Figma 客户端白名单 | 多客户端 | 手工拷贝 | npm |
| 成本 | Stitch MCP + API key | 读取按 seat 计费且限速 | 免费 | 免费 | Stitch API |
| 活跃度 | 2026-08 停更（92 天） | 持续 | 持续 | 原仓已停更 | 2026-11 仍推送 |

### 差异化护城河
**很薄。** 真正的护城河在 Stitch 产品本身和 `design.md` 规范，不在这个仓库。仓库自身几乎没有代码壁垒——所有能力通过 Stitch MCP 获取，**16 个 SKILL.md 是纯提示词资产，任何人读一周就能复刻一套**。它真正的护城河是三样非技术资产：**官方背书、分发位（占据 Agent 里的设计工作流入口）、以及与 design.md / stitch-sdk 的组织级协同**。

### 竞争风险
1. **官方文档与实际分发器不一致**：README 教用户跑 `npx plugins add --target antigravity`，而 `@vercel-labs/plugins` 的硬编码 target 只有 claude-code / cursor / codex——用户直接撞上 `Unknown target: antigravity`（#76）。同类还有 #53、#70、#63。这直接消耗信任。
2. **底层 MCP 资源鉴权**（#94）：Stitch MCP 返回的 `htmlCode.downloadUrl` 指向 `contribution.usercontent.google.com`，带 API key 的 MCP 客户端没有 cookie，302 跳登录页。更糟的是 `curl -f` 只看状态码，**会静默把登录页 HTML 当成设计稿存下来**。社区建议改用内联 `htmlCode.content` 或新增 `get_screen_code` 工具。**编排层的脆弱性完全继承自底层 API 的资源鉴权设计，技能越依赖下载链接越危险。**
3. **停更 90 天而生态仍在演进**：skills.sh 上已出现 README 未收录的 `site-md`，线上版本正在脱离本仓库。官方随时可能弃用或把能力并入 SDK。
4. **提示词效果无任何公开评测**：477.8K 安装量没有转化为一份 benchmark。

### 生态定位
组织矩阵里的**「工作流原语层」**——MCP 之上的编排层，介于 `design.md`（格式规范）与 `stitch-sdk`（编程接口）之间。它的价值主张不是技术独占，而是**跨厂商标准兼容性**：Google 用它把 Stitch 推向 Claude Code / Cursor / Codex，反过来把 Agent Skills 推向事实标准。**它是标准之争的棋子，不是产品护城河。**

## 套利机会分析

- **信息差**：star 维度它已是头部（9.9K），但「4,724 行代码 / 47.8 万次安装 / 16 个技能怎么组织」这件事在中文互联网几乎没人拆过。更值钱的发现是：`design.md`（28.9K star）才是流量入口，stitch-skills 是它的落地执行层——但 28.9K 的声量远高于 9.9K，说明**规范层比执行层更值钱**这个判断很少被说清。
- **技术借鉴**：最该抄的三件事——① 风格规则的三段证据链（脚本 → 清单 → 散文）；② Phase GATE 用 AND 连接的可观测事件写判据，配 ❌ Anti-patterns 堵住静默跳过；③ baton 文件协议做跨会话续跑。第四件也值得抄：必经路径脚本零依赖。
- **生态位**：它填补的是「MCP 之上的有状态编排」这一层。Agent Skills 标准由 Anthropic 主导、Skill 作为「有状态的编排原语」这一定义，目前最有规模的参考实现就在这里。
- **趋势判断**：Agent Skills 开放标准正在成形（agentskills.io），Google 用官方身份推动它，这个仓库是标准的活体样本。但增长故事在 2026-08 已经断档，**赌「标准红利」而不是赌「这个仓库继续更新」**才是正确姿势。

## 风险与不足

1. **架构性风险：技能层没有状态所有权**。#94 那类问题（签名 URL 需要 cookie、302 到登录页）不是 bug 而是把底层 API 的鉴权模型暴露在了最外层。技能越依赖下载链接越危险，而当前 16 个技能里相当一部分（react-components、react-native、stitch-loop……）的唯一数据通路就是这些下载链接。
2. **「标准」与「分发器」之间没有契约**。#66 里维护者的回复是「等 PR 合并先用 `#refactor` 分支」——**修复方式是把用户分流到 git ref，而不是修发布流程**。加上 #76/#53/#70/#63，README 承诺的 6 个 Agent 兼容矩阵里有一半（Antigravity、OpenCode）实际需要手工拷贝目录。
3. **命名规则自身不一致**。16 个 skill 里 9 个用 `stitch::` 前缀、7 个不用，且没有一个 skill 用裸 kebab-case 全名。OpenCode 加载不了带命名空间的那批，作者的解法是让用户自己改。
4. **质量防护形同虚设的边缘**：CI 名字叫 `validate-skills.yml`，但它**不校验任何结构**——不检查 frontmatter 字段合法性、不检查 name 是否 kebab-case、**不检查 `stitch::` 命名空间与目录名是否一致**（而这正是 #66 的根因）。workflow 实际内容只是 `npm ci` + 跑一遍 `validate.js` 断言 gold-standard 示例。test 类 commit = 0。
5. **「官方」身份的代价**：README 明确写「This is not an officially supported Google product. This project is not eligible for the Google Open Source Software Vulnerability Rewards Program.」加上「使用需把源码与素材上传 Google 服务器」的 MCP 架构，使用者承担的是**无 SLA、无 VRP、无兼容性承诺**的三无风险。
6. **美学主观性**：`taste-design` 编码的是特定审美偏好（编辑风、非对称、大留白），对「企业后台、密集数据表」场景是错的。它自己也承认口味单一——禁令只能消除模式，不能创造个性。
7. **代码重复**：`extractCssUrls` 在三处逐字重复，因为技能目录要能独立分发、不能跨目录 import。这是「技能可独立安装」这个好设计的必然代价。

## 行动建议

- **如果你要用它**：值得装，但它更像「架构参考实现」而非「生产工具」。装法上直接用 `npx plugins add google-labs-code/stitch-skills --target claude-code` 装整包，别选装（README 明确警告 inter-dependencies，跨技能是相对路径链接，装漏一个就断链）。**务必先确认 Stitch MCP 能通**，然后优先只读三个文件：`plugins/stitch-build/skills/react-components/SKILL.md`（Phase GATE + Anti-patterns 的范式样板）、`plugins/stitch-design/skills/extract-design-md/`（references 隔离法）、`plugins/stitch-utilities/skills/stitch-loop/resources/baton-schema.md`（接力棒协议）。**不要**把它当成「让 AI 生成高保真 UI」的银弹——外部评论已经指出 vendor 发布的公开设计技能都没有评测数据，本仓库同样如此。
- **如果你要学它**：重点看四样东西。① `plugins/stitch-build/skills/react-components/scripts/validate.js` —— AST 断言怎么写，以及 `9a6ea47` 那次 span 元数据性能修复。② `plugins/stitch-design/skills/extract-static-html/scripts/snapshot.ts` —— CSSOM 物化与 dev overlay 清单，1,470 行里全是从真实世界踩出来的细节。③ `plugins/stitch-design/skills/upload-to-stitch/scripts/upload_to_stitch.py` 的文件头 —— 「MCP 工具参数是模型输出所以有 16K token 上限」这个根因分析。④ `plugins/stitch-utilities/skills/taste-design/resources/DESIGN.md` 的禁令清单 —— 25 条「NEVER DO」的具体程度，是判断一份提示词写得够不够细的标尺。
- **如果你要 fork 它**：三处最值得下手。① **补一条真正的结构校验 CI** —— 校验 frontmatter 字段合法性、`name` 与目录名一致性、相对路径链接可达性（这三个都能静态判定，脚本能写）；这是最直接堵住 #66 那类 issue 的办法。② **把 `stitch::` 命名空间全量统一成 kebab-case**，或反过来全量去掉——半吊子状态是 OpenCode 不兼容的直接原因。③ **三份 manifest 改由脚本生成**，消除手工同步漂移。再加一条：给 SKILL.md 引入 eval（哪怕是最小集），把 47.8K 安装量变成可引用的效果数据。

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | 未能确认（deepwiki.com/google-labs-code/stitch-skills 持续返回 HTTP 429，被反爬拦截，无法区分未收录与已收录） |
| Zread.ai | https://zread.ai/google-labs-code/stitch-skills |
| skills.sh（第三方收录） | https://www.skills.sh/google-labs-code/stitch-skills —— 18 个 skill，477.8K 总安装量，是最硬的第三方使用量指标 |
| 关联论文 | 无（`site:arxiv.org` 未找到任何以 stitch-skills 或 Agent Skills 标准为对象的论文；arXiv 上名为 STITCH 的论文均为同名不同项目） |
| 在线 Demo | 无独立 Demo 站点；Stitch 产品本体可在线试用（https://stitch.withgoogle.com/） |
| 官方文档 | https://stitch.withgoogle.com/docs/mcp/setup（MCP 配置，技能全部依赖它） |
| 组织姊妹仓库 | `design.md`（28,915★，DESIGN.md 规范）· `stitch-sdk`（1,856★，官方 Node SDK，1.0，11 月仍推送） |
