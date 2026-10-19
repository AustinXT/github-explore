# GitHub 推荐：Google Android 官方 AI Skills 集合：6 月 8.7K stars 跨四平台分发

> GitHub: https://github.com/android/skills

## 一句话总结

Google Android DevRel 把官方开发者文档重新打包成「agent-first」的结构化 skills 集合——一个仓库同时在 Codex、Claude Code、Antigravity、Gemini CLI 四个 AI agent runtime 分发，填补「Android 领域 LLM 上下文贫瘠」的空白。

## 值得关注的理由

- **官方权威 + 跨平台稀缺性**：Google 官方出品的多 agent runtime 一仓库分发方案，是当前唯一同时覆盖 Codex/Claude/Gemini CLI/Antigravity 的 Android 垂直 skills 集合。
- **范式可迁移**：跨 runtime plugin manifest 三件套 + 业务域目录组织 + references 镜像官方文档——这套 docs-as-code 工程模式可直接被 Apple、Microsoft、JetBrains 等复制。
- **填补真实痛点**：Wear OS / Android XR / Navigation 3 / Compose Adaptive / Play Billing 升级 / R8 性能等长尾 Android 领域，通用 LLM 普遍输出质量低，官方 skills 让 agent 在这些场景直接吃 DevRel 知识。

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/android/skills |
| Star / Fork / Watcher | 8,768 / 568 / 92 |
| 代码规模 | 10,056 行（不含注释），实际是 45 个 Kotlin 样本；references 含 76K 行 markdown 镜像 developer.android.com |
| 语言分布 | Kotlin 57.1%（samples）、Python 26.6%（CI/codegen）、JSON 11.6%（manifest）、XML 4.8%（示例 layout） |
| 项目年龄 | 6.8 个月（2026-03-16 创建，2026-10-16 最近推送） |
| 开发阶段 | 稳定维护（v1.0.15 GA，27 个 tag） |
| 贡献模式 | 核心少数 + 社区（14 人，bot 主导 46.9% + 9 名 DevRel 真人） |
| 热度定位 | 大众热门（stars 体量），但价值不在 stars 而在生态入口 |
| 质量评级 | 代码 A / 文档 A+ / 测试 B（gotcha-protocol 替代）/ CI A / 错误处理 A |

## 作者视角：为什么存在这个项目

### 创始人/作者背景

仓库所有者是 Organization「android」（Google Android 官方组织账号，9 年账号龄、19,628 followers、147 公开仓库）。9 名核心真人来自 Android Developer Relations 团队——Simona（18 commits）、Jose Alcérreca（13）、Ben Trengrove（6）、Saswat Anand（3）等——都是既写 Android 代码也写开发者文档的工程师。自动化由 `android-devrel-github-bot` 主导（45/96 commits = 46.9%），负责从 dl.google.com 内部 `dac_skills.zip` 同步文档、刷新三个 plugin manifest、提交 codegen PR。

### 问题判断

Android DevRel 看到三个不可调和的矛盾：
1. **通用 LLM 在 Android 长尾领域质量差**——基础 Compose 写得出来，但 Wear OS 3D Glimmer、Navigation 3 Scenes、Play Billing 升级合规、R8 性能诊断等长尾高门槛领域产出烂。
2. **developer.android.com 是给人读的 HTML/SPA**，缺乏 LLM 友好的结构化 markdown；文档树太大、噪声多，agent 抓不到要点。
3. **各 agent 平台（Codex/Claude/Gemini/Antigravity）各自为政**，单仓库难以同时分发；社区 skills 质量参差、缺乏官方权威背书。

### 解法哲学

- **Unix 哲学**：「做一件事做好」——不试图替代 developer.android.com，只为高频任务提供「compressed ground truth」+ 让 agent 主动调 `android docs` 查 live 知识。
- **开放 vs 封闭的取舍**：明确选「开放拥抱」——公开声明遵循 open-standard agent skills（agentskills.io）、Apache-2.0、公开仓库但暂不接 PR（控制质量与发布节奏）。这不是 open-core，而是「官方权威 + 开放协议」组合。
- **性能 vs 易用性**：偏向易用性——一次 `android skills add --all` 装全所有 skill，三阶段渐进披露（Discovery → Activation → Execution）让 LLM 上下文不被膨胀。
- **明确不做什么**：不做 PDF/PPTX/XLSX 等通用办公文档技能（anthropics/skills 的领域）；不做完整 Laravel/Spring 生态集成；专注「Android 垂直 + agent 可执行指令」。

### 战略意图

这是 Android 团队 AI agent 战略的「manifest + skill 集合层」入口，与 Android Studio Gemini Agent Mode、Android CLI、Antigravity 联动形成完整 Android × AI 工具链。不是 SaaS 商业化，而是平台生态控制点——通过官方 skills 占据「Android 任务上下文首选来源」位置，类似 Apple/Microsoft 的官方 framework skills。

## 核心价值提炼

### 创新之处

1. **一仓多 runtime plugin manifest 三件套**（`.codex-plugin/` + `.claude-plugin/` + `.agents/plugins/`）
   - 同一仓库同时承载 Codex / Claude Code / Antigravity / Gemini CLI 四个 agent runtime 的 plugin 入口，CI 自动同步 skill 列表到各 manifest 的 `skills` 字段；marketplace 与 plugin 严格分离（Claude 端 `strict:false` 不能带 component 字段否则报 `MARKETPLACE_ENTRY_INLINE_MANIFEST`）。
   - 新颖度 4/5 | 实用性 5/5 | 可迁移性 5/5

2. **业务域优先目录组织**（xr/、wear/、navigation/、play/、camera/、identity/、performance/……）
   - 一级目录按 Android 产品线而非技术栈（ui/data/network）组织，因为 LLM agent 在「帮我做一个 Wear OS 手表 App」这种用户意图下激活 skill，业务域路径比技术抽象路径更符合意图匹配。
   - 新颖度 4/5 | 实用性 5/5 | 可迁移性 5/5

3. **`SKILL.md` + `references/` 双层结构 + 镜像 developer.android.com**
   - 主 SKILL.md 放「执行步骤 + 关键决策 + checklist」；`references/` 子目录镜像官方 developer.android.com 文档树（如 `navigation-3/references/android/guide/navigation/navigation-3/recipes/basic.md`），按需被 LLM read；45 个 Kotlin 样本以 `.kt.md` 后缀直接存放。
   - 新颖度 4/5 | 实用性 5/5 | 可迁移性 5/5

4. **`android` CLI 一站式安装抽象**
   - 提供 `android skills add/update/list/find/remove` 子命令，屏蔽「Codex 装哪、Claude 装哪、Antigravity 装哪」的 runtime 差异；`~/.gemini/antigravity/skills` 是默认落地路径。
   - 新颖度 4/5 | 实用性 5/5 | 可迁移性 4/5

5. **三阶段渐进披露协议（Discovery / Activation / Execution）+ auto vs manual 双触发**
   - SKILL.md frontmatter `description` 字段承担 Discovery（短句给 agent 决定是否激活）；`metadata.keywords` 关键词触发；正文给 Activation；references 按需给 Execution。
   - 新颖度 3/5 | 实用性 5/5 | 可迁移性 5/5

### 可复用的模式与技巧

- **跨 agent runtime plugin manifest 三件套**：一个仓库对应三个隐藏目录，每个 runtime 一个 manifest，CI 同步 skill 列表——避免在每个 runtime 各开 repo 导致内容漂移。
- **业务域优先目录组织**：一级目录按产品线（xr/wear/play/...）而非技术栈，让 LLM 激活匹配更准。
- **`SKILL.md` + `references/` 双层结构**：主文档放执行步骤 + checklist，references 镜像上游官方文档树，让 LLM 按需 read。
- **`.kt.md` 直接存放代码样本**：不抽到独立 SDK repo，样本即 markdown，agent 直接读。
- **自动化 bot 主导 + DevRel review PR 模式**：`android-devrel-github-bot` 跑 sync+manifest update，真人只 review 而不写 PR。
- **plugin.json `skills` 字段作为 SoR**：自动发现所有 `**/SKILL.md` 写入三个 manifest，避免手动维护 skill 列表漂移。

### 关键设计决策

1. **多 agent plugin manifest 三件套并列**
   - 问题：同一仓库如何同时在四个 runtime 分发？
   - 方案：每个 runtime 一个 plugin manifest，CI 自动扫描 `SKILL.md` 同步 skill 列表；marketplace 与 plugin 严格分离。
   - Trade-off：牺牲「单一真相源」的优雅，换取「一次发布多平台分发」的实用价值。
   - 可迁移性：**高**——任何想做跨 agent 分发的官方/组织级 skills 集都该这么干。

2. **业务域组织 vs 技术栈组织**
   - 问题：是按 `ui/data/network` 技术抽象，还是按 `wear/navigation/play` 业务域？
   - 方案：选业务域——LLM agent 在用户意图（业务域）下激活 skill，路径匹配更准。
   - Trade-off：牺牲「跨产品线技术抽象一致性」，换取「skill 发现性更符合用户意图」。
   - 可迁移性：**高**——任何垂直领域官方 skills 集合都建议按业务线组织。

3. **`android skills add` CLI 而非单纯 plugin.json**
   - 问题：plugin.json 只解决「agent 怎么发现」，不解决「skill 内容怎么落到 `~/.claude/skills/`、`~/.gemini/antigravity/skills/`」。
   - 方案：提供独立 `android` CLI，统一管理多 runtime 落地。
   - Trade-off：牺牲「纯 markdown repo」的零依赖美感，换取「一键全平台安装」的 UX。
   - 可迁移性：**中**——适合生态控制点强的官方方。

4. **自动化管道主导 + 严格 manifest schema 同步**
   - 问题：多 runtime manifest 字段（version / skills 列表 / keywords）易漂移，docs 镜像易过期。
   - 方案：`android-devrel-github-bot` 跑 update-skills.yml（拉 dl.google.com/dac/dac_skills.zip + git archive github-skills 分支 + 重写三个 plugin.json）。
   - Trade-off：牺牲「真人每个改动可 review」的纯粹，换取「docs 永远新鲜 + manifest 永远同步」。
   - 可迁移性：**高**——任何 docs-as-code + 多 manifest 项目都该这么做。

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | android/skills | anthropics/skills | laravel/boost | spring-ai Skills | google-ai-edge/gallery |
|------|----------------|-------------------|---------------|------------------|------------------------|
| Stars | 8,768 | ~177k | ~3.6k | ~3.4k | ~1k |
| 垂直领域 | Android（深） | 通用（广） | Laravel（深） | Spring（深） | on-device AI |
| Runtime 覆盖 | 4 路（Codex/Claude/Gemini/Antigravity） | 多家通用 | Laravel 主 | Java/Spring 主 | Gemini |
| 文档载体 | SKILL.md + references 镜像 docs | SKILL.md | 框架自有 | SKILL.md | Demo app |
| 安装方式 | `android skills add` CLI | `claude skill add` | `boost install` | Spring 配置 | APK |
| 自动化程度 | 高（bot 主导 47%） | 中 | 中（社区 vendor 化后） | 中 | 低 |
| 官方权威 | Google DevRel | Anthropic 官方 | Laravel 团队 | VMware/Broadcom | Google |

### 差异化护城河

- **Google DevRel 官方权威**：仅此一家有 Android 垂直领域的官方 DevRel 背书。
- **多 agent runtime 一仓库分发**：4 路分发是当前最广。
- **`android` CLI 抽象安装**：屏蔽 runtime 差异，降低用户接入成本。
- **plugin.json schema 27 版本稳定迭代**：manifest 协议已经过实战验证。
- **业务域目录 + 镜像 references**：组织结构最贴合 agent 意图匹配。

### 竞争风险

- **Anthropic 官方扩展 skills 反向侵入垂直**：iOS/SwiftUI/各框架官方 skills 可能蚕食。
- **社区 vendor 化风险**：laravel/boost 被 Laravel 团队接管是反面教材，android/skills 不接 PR 是否影响生态扩张存疑。
- **跨 agent 兼容性问题未解**：Issue #47（Antigravity 不识别 android-cli skill）、#48（gh skill install 找不到）、#200（WSL mincore not implemented）反映跨平台一致性仍在修复。
- **stars 增长曲线难测**：recent_stars 数据采集失败（gh API 403），6.8 个月获 8.7K stars 按体量算中等偏快，但缺乏精准增长曲线。

### 生态定位

填补「Android 领域 LLM agent 上下文贫瘠」的空白，是 Android AI agent 战略的「manifest + skill 集合层」入口；与 Android Studio Gemini Agent Mode、Android CLI、Antigravity 共同构成 Android × AI 工具链。同类「框架官方 skills 集合」范式（laravel/boost、spring-ai）已证明这是 2026 年新方向，android/skills 是其中跨平台覆盖最深的一家。

## 套利机会分析

- **信息差**：stars 8.7K 不算被低估（Google 官方项目本来就会被大牛 star）；价值点是**生态入口稀缺性**——目前唯一 Android 官方 skills 集合，跨四 agent runtime。
- **技术借鉴**：
  - 「业务域目录组织」可直接迁移到任何垂直领域 skills 集（iOS/Swift、AWS 服务等）。
  - 「`.kt.md` 样本即 markdown」可被任何 SDK 借鉴——给 agent 看「正确用法」的最低成本方式。
  - 「跨 runtime plugin manifest 三件套 + CI 同步」是「一次发布多平台分发」的工程范式。
- **生态位**：填补 Android × AI agent 工具链的「manifest + skill 集合层」空白；与 Android Studio Gemini Agent Mode 形成「上游 skills + 下游 IDE agent」完整闭环。
- **趋势判断**：
  - **趋势增长**：agent skills 协议 2025-2026 才稳定，多平台同时支持窗口已打开，本项目仍在放量阶段。
  - **比竞品后发优势**：anthropics/skills 走通用路线，覆盖深不及垂直项目；laravel/boost、spring-ai 偏单 runtime。
  - **风险信号**：跨 agent 兼容性问题（#47/#48/#200）若不解决，跨平台分发优势可能被替代。

## 风险与不足

- **跨 agent 平台兼容性未解**：Antigravity 2.0.x reference 不到 android-cli skill（#47）；`gh skill install` 找不到仓库（#48）；WSL 文档检索内核不支持（#200）。这是核心分发通道的稳定性问题。
- **stars 增长数据缺失**：gh API 403 限流导致无法精确计算增长曲线，套利判断缺乏定量支撑。
- **commit 类型分布 87.7% 是 other**：不遵循 conventional commits 规范，影响第三方脚本解析历史。
- **不接外部 PR**：控制发布节奏但限制社区贡献，生态扩张速度受限。
- **深度依赖 Google 内部 dac_skills.zip**：外部贡献者无法直接同步 references 文档。

## 行动建议

### 如果你要用它

- **场景**：用 AI 编码助手做 Android 长尾领域开发（Wear OS / Android XR / Navigation 3 / Compose Adaptive / Play Billing 升级 / R8 性能）时，安装本仓库 skills 可让 agent 输出质量显著提升。
- **命令**：
  - 全装：`android skills add --all`（落地到 `~/.gemini/antigravity/skills`）
  - 单独装：`android skills add r8-analyzer --project=.`
  - 更新：`android skills update --all`
- **优先级**：先用 `devtools/android-cli` skill 装好 CLI，再按需装其他。

### 如果你要学它

- **核心文件**：
  - `.codex-plugin/plugin.json`（改得最多 20 次 — manifest schema 演进史）
  - `devtools/android-cli/SKILL.md`（核心 CLI skill，最佳范例）
  - `wear/wear-compose-m3/SKILL.md`（长尾领域 skill 范例，带 gotcha-protocol）
  - `navigation/navigation-3/SKILL.md`（Navigation 3 这种「新范式」skill 范例）
  - `.github/workflows/update-skills.yml`（自动化同步管线范例）
- **重点关注**：
  - `references/` 镜像官方文档树的设计模式（如何版本锁定 references）
  - frontmatter 字段（`description` / `keywords` / `last-updated` / `author`）
  - bot 主导 release 流程（`create-release.yml`）

### 如果你要 fork 它

- **可改进方向**：
  - 修正 Antigravity / Codex / Claude Code 跨平台一致性问题（参考 issue #47/#48）。
  - 引入 `kotlin/.skmd` Kotlin DSL 让 SKILL.md 可被 IDE 解析。
  - 增加「deprecation」与「compatibility」矩阵字段，让多 runtime 兼容性可机器验证。
  - 增加 agent 可调用的 `android benchmark` 命令评估 skill 触发准确性。
  - 支持 references 文档的 per-skill 版本锁定（防止 upstream developer.android.com 改动破坏现有 skill）。
- **范式迁移方向**：把同一套「业务域目录 + 跨 runtime manifest + bot 同步」范式应用到 iOS/Swift、AWS 服务、Web 框架等任何垂直领域。

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | 未收录 |
| Zread.ai | 未收录 |
| 官方文档 | https://developer.android.com/tools/agents/android-skills |
| Agent Skills 规范 | https://agentskills.io/home |
| Android CLI | https://developer.android.com/tools/agents/android-cli |
| Android Studio Gemini Skills | https://developer.android.com/studio/gemini/skills |
| 关联论文 | 无（docs/skill 集合，无学术论文）；相关 Android agent 研究见 arXiv：AndroidLab (2410.24024)、GradleFixer (2510.08640) |
| 在线 Demo | 官方 docs 内嵌 `gemini_cli_skills_demo.gif`（未直链） |
| 外部深度视角 | 「给 AI 装上 Android 手艺:Tool Use 与 Skills 的深度工程实践」（腾讯云开发者社区） — 把 Skills 与 Tool Use 工程取舍做对比 |

> **Demo 缺失说明**：README 与官网均无静态展示图（media.candidates = 0），仅官方 docs 内嵌一张 `gemini_cli_skills_demo.gif`（CLI 调用 skill 演示），故省略「项目展示」节。