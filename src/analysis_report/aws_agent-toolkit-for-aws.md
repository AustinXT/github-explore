# GitHub 推荐：195 份提示词、0 个 release：AWS 官方 agent 工具箱

> GitHub: https://github.com/aws/agent-toolkit-for-aws

## 一句话总结
AWS 官方把「让 AI 编码 agent 用好 AWS」这件事做成了一个内容分发仓库——**195 份 `SKILL.md` 提示词资产 + 5 个插件包 + 一套校验工具链**，把 AWS 的领域知识与运维 SOP 产品化交付给 Claude Code / Codex / Cursor 等任意 agent。

## 值得关注的理由
1. **它是 AWS 在 agent 时代的「官方答案」，架构参考价值远大于代码复用价值。** 「Skills（渐进式披露的领域知识）+ 托管 MCP（工具面）+ Plugins（分发）+ Rules（宿主级行为约束）」这套四件套，是目前厂商级 agent 工具链最完整的落地样本之一。想做 agent 基础设施、IaC 工具、skill 生态的团队，应该把它当参考系读，而不是当依赖引入。
2. **「内容工程」这门手艺被完整演示了一遍。** 全仓 146,777 行「代码」里真正的运行时实现很少，绝大多数是提示词资产；而围绕这些提示词，AWS 建了一套 9 个 workflow 的 CI、多层 frontmatter 校验、字节级同步门禁、路径包含性安全基线——**LLM 写的文档也是需要编译检查的源代码**，这个视角可以直接搬走。
3. **它是观察「AWS 把 agent 调用当成 IAM 一等公民」这件事的唯一一手材料。** AWS 托管的 MCP Server 用条件上下文键把「agent 调的」和「人调的」区分开，让 IAM 策略能只对 agent 生效——这套设计思路大概率会被整个行业抄走。

## 项目展示

![Agent Toolkit 产品视频缩略图](https://img.youtube.com/vi/d1GHVtEFy2A/maxresdefault.jpg)
AWS 官方产品演示视频入口

![AWS MCP Server 能力示意](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/agents/gradial/agent-toolkit-features-aws-mcp-server-v5.8cf379e3c63f78ea3e96af749135af263000da9c.png)
托管 MCP Server：一个通用 API 工具覆盖 15,000+ AWS API，另有 `run_script` 沙箱执行与免凭据的文档检索工具

![Agent Skills 渐进式披露机制](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/agents/gradial/agent-toolkit-features-agent-skills-v5.bb9b47f40d30883b524b89541d1fbbb18e18bb64.png)
Skills 层：SKILL.md → references/ → assets/ 三层按需加载（图中写 75+，仓库实际已有 195 个，素材滞后于演进）

![Agent Plugins 清单](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/agents/gradial/agent-toolkit-features-agent-plugins-v5.e6242a370a0f3b79c32df326833dafcc09c99c52.png)
Plugins 层：5 个插件把 MCP 配置与精选 skill 打包成一键安装

![Rules Files 行为约束](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/agents/gradial/agent-toolkit-features-rule-files-v5.98c1fb5df1a89ff1afb983737e33bd44370fb659.png)
Rules 层：5 条持久指令决定 agent 是否主动调用 skill

> 四张代码卡合起来正好是官方四层架构（Server / Skills / Plugins / Rules）的一一图解，与 User Guide 的 Components 表完全对应。**注意仓库 README 里一张图都没有**——一个「四层架构 + 15,000+ API + 195 个 skill」的系统，所有架构理解成本都被转嫁给了 AWS 文档站。

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/aws/agent-toolkit-for-aws |
| Star / Fork | 3,192 / 403（fork 率 12.6%，高于典型内容仓 3%~8%） |
| 许可证 | Apache-2.0（另有 `NOTICE` 与 `CODE_OF_CONDUCT.md`） |
| 代码行数 | 146,777（Python 69.9%, JSON 18.6%, TypeScript 4.4%；含 markdown 提示词资产的 tokei 口径） |
| 项目年龄 | 6.1 个月（2026-04-23 首次提交，2026-05-06 GA，2026-10-23 最近推送） |
| 开发阶段 | 密集开发（近 30 天 110 commits ≈ 3.7 次/天；feature 占 50.0%，refactor 仅 1.0%） |
| 贡献模式 | 公司团队驱动 + 社区协作（133 位贡献者，Top 1 仅占 10.3%，但 195 份 skill 由十几个 AWS 服务团队各写各的） |
| 热度定位 | 中等热度（发布期上 GitHub Trending 日榜 #19、周榜 #17；当前 +7~10 star/天，进入长尾稳态） |
| 质量评级 | 代码[良好] 文档[优秀] 测试[不足] |

## 作者视角：为什么存在这个项目

### 创始人/作者背景
Amazon Web Services 官方组织账号（14.2 年老号，17,247 粉丝，559 个公开仓库），GA 由 AWS News Blog 于 2026-05-06 正式发布。但真正决定内容质量的不是组织账号，而是贡献者画像——`arnewouters`（AWS 首席架构师 Principal SA）、`mmehrten`（Well-Architected 框架作者之一）、`kelvinau`（Terraform 布道师）、`rshevchuk-git`（CDK/Python 生态）、`bfreiberg`（CDK 与 IaC 核心布道者）。

**这直接推导出两个结论**：其一，**每个 skill 由最懂那个服务的团队写**，质量参差是结构性的而非偶然的；其二，它**没有个人作者的护城河**——靠 vendor 背书吸引 star，vendor 一旦转向（就像 AWS 已经对 AWS Labs MCP servers 做过的那样），整套资产随时可弃用。

### 问题判断
作者把「agent 操作 AWS 时的缺口」拆成三块，其中第三块最核心：

1. **知识缺口** —— 模型训练数据里的 AWS 知识会过时（服务限额、定价、GA 状态、特性支持），而 AWS 有 300+ 服务、15,000+ API action。解法双轨：`skills/` 里 195 份 SKILL.md 固化「怎么选服务、怎么排障、怎么写 IaC」，`aws___search_documentation` / `aws___read_documentation` 提供实时文档兜底。
2. **执行缺口** —— agent 面对 AWS 只有两条路：让模型自己拼 `aws` CLI 字符串（慢、脆、每步一个往返、无法归因），或接社区/自建 MCP server（无 IAM 语义、无 CloudTrail 归因、无文档实时性）。解法是一个托管端点 + 沙箱脚本 `aws___run_script`。
3. **治理缺口** —— 「让 agent 拿到 IAM 权限」和「让 agent 能用 IAM 权限」是两件事。解法是 AWS 托管 MCP Server 里的两个全局条件上下文键，让 IAM 策略能只对 agent 调用生效。

**时机为什么是现在**：git 历史给了清晰答案——首次提交 2026-04-23，GA 公告 2026-05-06，中间只有 13 天。这 13 天里做的不是开发，而是「产品化定型」：commit 记录全是 `chore: copy analytics skills into general skills folder`、`feat: add 13 GA-approved skills (non-default)`、`docs: Update READMEs for Agent Toolkit for AWS launch`。**这是一个早已存在的内部资产被一次性开源出来的瞬间，不是从零开始的项目。**

「GA-approved skills (non-default)」这个措辞尤其关键：发布有审批闸门，默认插件 `aws-core` 只装 GA-approved 的 skill，非默认的放在 `skills/` 里——这是内容治理的证据。

### 解法哲学
作者明确选择了「不做什么」，而且这些选择都能在代码里验证：

1. **不替换 agent，只做加法。** 官方原话是 「You keep the agent, editor, and workflow you have.」。技术代价是同一份内容要在 4 种宿主 manifest 格式里各写一遍。
2. **不扩权，只暴露已有权限。** 规则文件写明 「It does not add permissions... If your policies deny a call, the Agent Toolkit for AWS does not work around the denial.」——它是 IAM 身份的 API 代理，不是提权通道。
3. **用沙箱换单次往返。** `aws___run_script` 服务端跑 Python，继承 IAM 权限，无网络、无本地文件系统、无 shell。代价是丢掉了「只允许这一条 CLI 命令」的细粒度表达力——这正是 issue #294 的核心张力。
4. **工具面持续收缩。** `aws___call_aws` 2026-07-15 废弃 → 08-31 移除；2026-10-03 起只读模式剔除未标 `readOnlyHint: true` 的工具。方向明确：从「通用 API 代理」向「任务导向」收缩。
5. **不承诺版本。** 0 tag、0 release，版本只写在 manifest 里。刻意的设计，但代价是无法 pin、无法回滚。

最值得学的一条洞见写在 `plugins/aws-agents/skills/agents-pay/scripts/x402_policy.py` 的模块 docstring 里：

> 「Instructions to a model are not an access control. This module makes the payment rules executable, so the guarantee holds even when the model is wrong or hostile.」

以及那句更狠的实现注释：「Nothing in this module reads model output, chat history, or publisher content as authorization.」

### 战略意图
**基础设施，不是核心产品。** 它不含模型、不含 IDE、不含对话界面。存在意义是**让 AWS 在 agent 时代不被绕过**——如果 agent 只用 CLI + boto3，AWS 就失去了「谁在调用、调用了什么、是否合规」的控制点，也会丢掉这一层流量。

**商业化意图明确存在**：`aws-startup-advisor` 里大篇幅涉及 AWS Activate 积分、startup offers、付费计划检查、`aws freetier get-account-plan-state`；`rules/aws-starter-rules.md` 里专门写「用户可能有 spend limit」「如果资源突然不可访问，问用户是不是触发了 spend limit」。这些不是技术文档，是销售转化路径——把一个解决方案架构师塞进编码助手里，本身就是一条 lead-gen 漏斗。

**开源策略：产品化开源，不是社区开源。** Apache-2.0 全量开源，但 `CONTRIBUTING.md` 第 3 行明写 「This project is not accepting external code contributions at this time.」，只收 bug / feature / security 报告。另外两条证据：`.github/workflows/skill-frontmatter-check.yml` 会**自动关闭**含 `stages` 字段或 `owner_` 前缀字段的 PR（对外隐藏内部编排元数据）；`SUPPORT.md` 明确划线——AWS 服务本身的问题走 Support Center，**toolkit 自身不在 Support Plan 保障范围内**。

## 核心价值提炼

### 创新之处

按「新颖度 × 实用性」排序：

1. **把安全断言从提示词降级到可执行 gate（且 gate 完全不读模型输出）** — 新颖度 4/5，实用性 5/5，可迁移性 5/5
   `x402_policy.py` 实现了一套完整的授权策略：配置文件必须是 regular file、属主为当前用户、mode 0600、父目录不可组可写、无符号链接；`allowed_recipients` 白名单默认拒绝未知收款方；**单笔上限与 session 累计预算是两个独立天花板**（代码注释写明理由：只有 session 预算时，一次恶意 challenge 就能清空余额）；`allowed_recipients` 与 `allow_any_recipient` 互斥；「Absent keys deny rather to allow. There is no implicit wildcard.」
   同一原则在 `plugins/aws-core/com.anthropic.claude-code/hooks/secret-safety.py` 落地（PreToolUse hook 拦截 AWS CLI / SDK / 本地 SMA daemon 三种取密形态，返回 MCP 协议标准的 `permissionDecision = "deny"`），并且**考虑了超时 fail-open 的风险**——hook 有 5 秒超时，所以 flag 正则必须线性、无歧义解析（注释原话：「an ambiguous flag pattern here backtracks catastrophically on long flag runs, and because the hook has a 5s timeout in hooks.json, a hang would let the tool call through (fail-open)」）。

2. **路由 skill + 语义类别注册表 + 四档决策分类** — 新颖度 4/5，实用性 5/5，可迁移性 5/5
   `aws-database`、`aws-serverless`、`amazon-elasticache` 是三个 router skill。注册表把每个子技能拆成 `ID | Name | Domain | Semantic Categories | Upstream | Downstream` 五到七列，其中 **Semantic Categories 是一整列自然语言触发短语**（如 `migration` 行写 「migrate, Redis OSS to Valkey, node-based to serverless, version upgrades, zero-downtime cutover, rollback」），匹配方式是 match on meaning, not exact wording。
   最精细的是 `aws-serverless` 的**四档决策分类**：Decided（请求已给出区分事实 → 承诺并追问）/ Leaning（只有定性暗示 → 给暂定方案 + 明确说出「哪个答案会翻转路由」）/ Open（无线索 → 收窄问题）/ Unraised（未提出 → 走默认不问），并硬约束 「ask no more than 3–4 questions overall, and never reply with questions alone」。
   配套的是**双向责任边界声明**：router 与 leaf 互相声明归属，避免两个 skill 同时声称拥有同一问题。`aws-serverless` 里甚至预判了模型最容易犯的具体错误——「Lambda Web Adapter is NOT a substitute for Web Functions on a Node.js HTTP app」。

3. **把「散文状态机」当可编译对象** — 新颖度 4/5，实用性 4/5，可迁移性 5/5
   skill 之间的引用是散文里的字符串（「Load `references/phases/design/design-ai.md`」），agent 照做，文件改名就是死路。`plugins/aws-startup-advisor` 下的 `check-skill-refs.py` 把这些字符串**当代码引用解析**：正则识别路径形态 token（`references/`、`knowledge/`、`scripts/`、`phases/`、`shared/` 等根前缀 + 8 种扩展名），按 **5 级解析顺序**尝试解析，解析不到即 `MISSING_REF`。关键设计是显式前缀具有权威性——注释写明：「An explicit prefix is authoritative: the agent runs `<SKILL_BASE>/scripts/x.py` as written. A same-named file under the skill root does not make a wrong relative path exist, and none of the fallbacks below apply.」。baseline 机制记录已知死链并附原因，且**baseline 中的陈旧条目会导致失败**，防止死链被永久豁免。

4. **声明式 freshness 契约** — 新颖度 4/5，实用性 4/5，可迁移性 5/5
   `model-staleness.py` 不硬编码「模型注册表该多久更新一次」，而是**读取注册表自己声明的 `**Last updated:**` 与 `**Staleness window:** N days` 行**再比对。关键在失败语义分级：**drift（副本不一致）与契约缺失永远失败；staleness（快照过期）只在 `--strict` 下失败**——把「正确性问题」与「时间问题」在 CI 里分离。

5. **artifact 契约的双来源 + 显式开放路径** — 新颖度 4/5
   `artifact-contracts.json` 把每个产出 artifact 映射到契约来源，可以是 JSON Schema，也可以是 **markdown 里的 JSON 示例块**（`shape` 指向文档路径 + `root_heading` 选块 + `sections` 把子标题映射到它细化的 key 路径）。规则是「schema 权威处听 schema，schema 没说的用 shape 兜」。更精巧的是 `open_paths`——显式列出「schema 未覆盖、不可判为未知」的路径并附 `_open_paths_why` 理由。

6. **否定式边界声明作为路由压缩手段** — 新颖度 3/5，实用性 4/5
   195 份 SKILL.md 的 description 合计 **63,446 字符（≈15,861 tokens）**，长度分布高度顶格：**15 个 ≥1000 字符**，最长 `aws-storage` 达 1,023 字符（规范上限 1024，仍在限内）。作者在固定预算里用**否定式边界声明**压缩语义密度——`aws-elasticache` 的 description 同时写 「Activate when……」（6 类触发场景）与 「**Do not trigger for** browser caches, CDN/CloudFront, HTTP Cache-Control, CPU caches」；`agents-pay` 写 「Not for BUILDING payment capability for end users…… For non-paid APIs via Gateway use agents-connect. For inbound auth use agents-harden.」
   **「我不负责什么」比「我负责什么」更能省 token**——这是可直接抄的写法。

7. **插件即包：文件系统解析后的路径包含性 + 全面禁符号链接** — 新颖度 3/5
   `validate_spec.py` 的 `check_containment` 注释写明：「Resolution matters: a lexical check passes a path that reaches outside the root through a symlink.」——先 `resolve()` 再判 `target != root and root not in target.parents`。另有 `reject_symlinks` 全面禁止 `plugins/` 下出现符号链接（理由：「A plugin tree of Markdown and JSON has no use for symlinks」）。

8. **vendored 规范 schema** — 新颖度 3/5，几乎零成本
   两份 schema 复制进 `tools/schemas/1.0.0/`，docstring 写明理由：「They are vendored because the spec forbids retrieving a schema while loading a plugin (§7.2.1), and CI should not need network access.」

9. **熔断闸门作为内容资产的紧急制动** — 新颖度 3/5
   `.github/workflows/merge-prevention.yml` 实现两个正交闸门：`do-not-merge` 标签（可用 `vars.DO_NOT_MERGE_LABEL` 覆盖）阻断合并；仓库变量 `HALT_MERGES` 三态（`0` = 关闭 / `<N>` = 只允许 PR #N 合并 / `-1` = 全部阻断）。配套的 `skill-frontmatter-check.yml` 会**自动评论并自动关闭**违规 PR。

10. **双层 frontmatter 校验：零依赖快检 + 严格规范慢检** — 新颖度 3/5
    `tools/validate.py`（stdlib-only，手写 YAML 子集解析）保证任何人 clone 下来 `python3 tools/validate.py` 就能跑；`tools/validate_spec.py`（jsonschema + pyyaml）保证规范严格一致。两者解析器的差异被显式记录（手写行扫描器看不见 block scalar 里的空行会终止块，把下一行散文变成伪顶层键）。

### 可复用的模式与技巧

1. **canonical 源 + vendored 副本 + 字节级同步门禁**：内容只写一份，分发时复制，用 `filecmp.cmp(shallow=False)` 逐文件比对 + `--check` 模式进 CI。适用场景：monorepo 里需要「可独立安装的子包」但又不想建包管理系统的场景。
2. **README 映射表双向完整性**：vendored 副本目录放一张 `| Vendored path | Canonical source |` 表，CI 校验「表里每行存在 + 磁盘每文件有行」。适用场景：任何「同一份内容在多处独立可分发」的 monorepo。
3. **路由 skill + 语义类别注册表 + 上游/下游依赖图**：把「模型不知道选哪个」显式化成一张表。适用场景：数据库选型、支付通道选型、ML 框架选型等任何多候选方案的 agent 产品。
4. **四档决策分类（Decided / Leaning / Open / Unraised）**：把「什么时候该问、什么时候不该问」写成显式规则，并约束提问总数上限。适用场景：需要控制 agent 打断频率的交互式 agent。
5. **安全断言下沉到代码**：把「模型不许做 X」翻译成代码里的 gate，并让 gate **完全不读模型输出**。适用场景：任何 agent 触及资金、密钥、生产资源的场景。
6. **配置文件按密钥对待**：regular file / 属主 / mode 0600 / 父目录不可组可写 / 无符号链接。适用场景：存放授权策略的本地配置文件。
7. **双天花板（单笔上限 + 累计预算）**：任何配额系统都不应只有一个总量上限。适用场景：支付、API 配额、token 预算。
8. **声明式 freshness 契约**：数据文件自己声明有效期，校验器只做 drift 检查；正确性失败与时效性失败分级。适用场景：价格表、模型列表、漏洞库、区域可用性。
9. **文件名 ↔ 内容名双向一致性断言**：`SKILL.md` 的 `name` 必须等于其父目录名（经 NFKC 归一化）。适用场景：任何「目录即标识」的资产布局。
10. **多宿主分发的一致性门禁**：N 种 manifest 格式下，validator 逐字段比对 name/version/description。适用场景：一份内容要同时支持多个 IDE/CLI/插件宿主。
11. **spec 之外补「schema 表达不了的规则」**：JSON Schema 之外单独用代码检查路径包含性、HTTPS、占位符白名单、header 重复，并注释说明这些规则来自规范第几节。
12. **知识卡片（`assets/*.md`）作为第三层渐进式披露**：把速查事实做成 20 行结构化卡片（如 `rds-db2.md` 列出 Docs / llms.txt / Data model / Serverless / Scale to zero / Free Tier / Not for 等维度），并指向服务方的 `llms.txt` 文档索引。
13. **「先查实时文档、再答」的决策序写进全局规则**：明确优先级——(a) MCP `read_documentation`/`search_documentation` → （b） 服务方 `llms.txt` → (c) AWS 文档 URL；并要求「如果不能确认，就说不能确认」。
14. **CI 权限默认全关 + job 级最小授予 + action 锁 SHA**：标准做法，可直接照抄。配套 OSSF Scorecard 每周自动验证。
15. **按 paths 过滤器拆分重 CI 与轻 CI**：`startup-advisor.yml` 只在 `plugins/aws-startup-advisor/**` 变更时触发，让一个插件的 38 个测试文件不拖累全仓 PR。
16. **mise 任务图作为唯一检查入口**：`lint` → `validate` → `build` 三级聚合，CI 只调 `mise run`，本地与 CI 跑同一套命令。

### 关键设计决策

**决策 1：为 4 种宿主格式各写一份 manifest**
- **问题**：Claude Code / Codex / Cursor / Devin 各有自己的插件清单格式与必填字段，再叠加跨厂商规范 `agent-plugins.org` v1.0.0。一份 description 与 keywords 数组要复制 6 遍。
- **方案**：`tools/validate.py` 把「跨 manifest 元数据一致性」当硬门禁——Devin 读 `.devin-plugin/plugin.json` 优先于 Claude manifest，所以 validator 逐字段比对 `name`/`version`/`description` 是否完全相等。注释原话：「Devin reads .devin-plugin/plugin.json in preference to the Claude manifest, so a version bump that misses it ships stale metadata.」 同时检查 Devin 声明的 `skills`/`mcpServers` 路径必须留在 plugin 目录内。
- **Trade-off**：牺牲 DRY（`aws-core` 的 description 出现 4 次，keywords 数组 ~120 项出现 4 次，marketplace.json 里再出现 2 次），换取每个宿主都是「原生」插件、用户零心智负担。
- **可迁移性**：高。「N 个宿主格式 + 一致性门禁 + 路径包含性检查」可直接搬到任何「一份内容、多端分发」的项目。

**决策 2：内容双份拷贝 + 自动同步门禁，而非引用或构建时生成**
- **问题**：`skills/core-skills/aws-serverless/SKILL.md` 与 `plugins/aws-core/skills/aws-serverless/SKILL.md` 内容完全相同（实测 `aws-serverless/SKILL.md` 在 Top 10 变更中出现 14 次和 13 次两次）。但插件必须自包含——用户从 marketplace 装的是 `plugins/aws-core/` 这个目录。
- **方案**：`tools/sync-plugin-skills.py` 按目录名自动发现 canonical 源，逐目录做逐文件字节比对，不一致就 `rmtree` + `copytree` 全量覆盖；CI 跑 `--check`，不一致直接失败并提示 `Run 'python3 tools/sync-plugin-skills.py' to fix.`。`aws-startup-advisor/tools/sync-vendored.py` 更进一步：要求每个 vendored 目录的 README 维护映射表并**双向完整**。
- **Trade-off**：牺牲「单一真相」理想（Git 里确实存了两份），换取每个插件目录可独立分发、独立安装、独立打包。代价直接体现在 git 历史里——任何一次内容修改都产生 2 个 commit 差异。
- **可迁移性**：高。这是「可独立分发子树」的通用方案。

**决策 3：把「渐进式披露」做成物理目录结构**
- **问题**：195 份 skill 全塞进 context 不可能，且 description 在会话启动时就全量进 context。
- **方案**：`SKILL.md`（决策流程 + 路由表）→ `references/*.md`（深度内容，按需 file-read）→ `assets/*.md`（知识卡片），配合 router skill 与子技能注册表管理激活歧义。
- **Trade-off**：牺牲描述的自然可读性（15 个 description ≥1000 字符，明显是顶到 1024 上限后写的），换来「一个 skill = 一份可独立复制的知识包」，且不依赖中心索引就能被 agent 发现。
- **可迁移性**：很高。是领域知识打包给 LLM 的通用范式。

**决策 4：把「安全控制」下沉到代码与 hook，而不是写在提示词里**
- **问题**：模型可能犯错，模型也可能被 prompt injection。规则文件里写「不要读 secret」只是一句请求，不是访问控制。
- **方案**：三层防御——PreToolUse hook 拦截取密、规则文件给出唯一允许的替代路径（`{{resolve:secretsmanager:secret-id:SecretString:json-key}}` 配合 `asm-exec`，让 secret 在运行时解析而不进 context）、`x402_policy.py` 把支付授权做成完全独立的可执行策略。
- **Trade-off**：hook 只在 Claude Code 宿主生效（Cursor / Codex / Devin 无对应机制），是平台相关的纵深防御而非全覆盖。
- **可迁移性**：很高。

**决策 5：零版本化——刻意的设计，也是最大的技术债**
- **问题**：分发形态是「市场安装」与「按需拉取」，不是 `git checkout v1.2.0`。但 skill 指令是会被 agent 执行的提示词资产，改一个词就可能改变行为。
- **方案**：版本写在 3 份 `marketplace.json` 与 5 份 `plugin.json` 里（`aws-core` 1.2.0、`aws-data-analytics` 1.5.0、`aws-startup-advisor` 2.0.3、`aws-agents` 1.0.0、`aws-agents-for-devsecops` 1.0.0）。仓库 0 tag、0 GitHub release。
- **Trade-off**：用户**无法锁定 skill 的行为版本**，环境不可复现。skill 的 `metadata.version`（109 份 SKILL.md 有此字段）只能标内容版本，不能用于 pin——因为 skill 独立分发，不随 plugin 版本走。
- **可迁移性**：低（反面教材）。任何「提示词即代码」的项目都应该从这里学到：一旦 skill 会改变 agent 的实际行为，就必须有 release/tag 机制。

**决策 6：mise.toml 作为唯一任务入口，CI 只调 `mise run`**
- **问题**：391 个 Python 文件、4 个子项目各带工具链（uv / node / pytest / markdownlint-cli2 / node --test），版本需要统一。
- **方案**：根 `mise.toml` 固定 `node = "24"`、`python = "3.12"`、`gitleaks`、`uv`、`markdownlint-cli2 = "0.18"`，任务组织成 `lint` / `validate` / `build` 三级图；CI 通过 `jdx/mise-action` 安装。
- **Trade-off**：引入 mise 作为硬依赖，对非 mise 用户有门槛；换来「本地能过 = CI 能过」。
- **可迁移性**：中高。

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | 本项目 aws/agent-toolkit-for-aws | awslabs/mcp（前身） | 社区自建 AWS MCP server | 裸用 AWS CLI / SDK |
|------|---------|--------|--------|--------|
| Star | 3,192 | 9,829 | 分散（单个多在百量级） | 不适用 |
| 领域知识广度 | 195 份 SKILL.md + 15,000+ API 单端点 | per-service 粒度，无统一 skill 分发 | 通常 1~2 个服务 | 无 |
| IAM 人机归因 | 有（托管 MCP Server 侧的条件上下文键） | 无 | 无 | 无（进程内调用） |
| 实时文档检索 | 有（免凭据 `search_documentation`） | 部分 server 自带 | 少有 | 需自建 |
| 可自托管 | 否（托管端点） | 是 | 是 | 是（天然） |
| 版本化 / 可 pin | **否**（0 tag / 0 release） | 是 | 是 | 是（lock file） |
| 上下文成本 | 高（skill 索引 ≈15,861 tokens） | 低（按 server 装） | 低 | 无额外成本 |
| 社区 | 133 位贡献者，但仅内部/受邀 | 更大、更开放 | 个人维护者居多 | 生态成熟 |

### 差异化护城河

四层，**全部来自 AWS 而非代码本身**：

1. **厂商背书与域名** —— `aws/` 组织账号 + Anthropic 官方 marketplace 上架 + `docs.aws.amazon.com/agent-toolkit/` 官方文档。
2. **IAM 原生治理** —— 条件上下文键 + CloudTrail + CloudWatch `AWS-MCP` 命名空间。这是社区方案**在架构上**无法复刻的（需要在 IAM 服务端实现全局条件键）。
3. **单端点服务广度** —— 300+ 服务 / 15,000+ action 托管在一个端点，含免凭据文档工具。
4. **服务团队领域知识** —— 195 份 skill 由十几个服务团队各自写。这是**组织资产**而非代码资产。

> ⚠️ **一个必须说清楚的事实**：护城河第 2 层的**代码不在这个仓库里**。全文检索确认 `aws:ViaAWSMCPService` / `aws:CalledViaAWSMCP` 在本仓库中**一次都没有出现**——它们实现于 AWS 托管的 MCP Server（`https://aws-mcp.us-east-1.api.aws/mcp`，闭源托管服务）。仓库里与治理直接相关的只有 `rules/` 两份规则文件、`aws-core` 的 PreToolUse hook 和 `agents-pay` 的 `x402_policy.py`。换句话说，**这个仓库贡献的是「内容与分发层」，而护城河的主体在闭源服务端**。这既解释了为什么第三方评测说它「成熟度 3/5」，也说明了这个仓库的可复用边界在哪里。

### 竞争风险

- **护城河与风险同源**：四层护城河全部来自 AWS。个人项目的护城河是「作者本人」（随作者流失而流失），本项目的护城河是「vendor 路线」（随 vendor 转向而倾覆）——后者失效更快，因为它是战略决策而非自然减员。
- **社区采纳验证不足**：195 份 skill 的质量是**结构性参差**（每个 skill 由最懂那个服务的团队写，而非统一标准）。第三方评测的 Setup 3/5、Maturity 3/5 印证了这一点。
- **协议前端跟不上 spec（正在发生的失败）**：issue #265 显示公共 AWS MCP gateway 不带版本的 `tools/list` 被拒（`-32602`），**标准官方 SDK 客户端无法完成 handshake、无法 list tools**；同一服务器在 2026-07-28 revision 下失败 9 项还多出 `server/discover` 失败。而协议前端封装在不可自托管的托管服务里，**用户零 workaround 余地**。
- **不可 pin / 不可复现**：0 tag、0 release + skill 指令隔日可变。
- **skill 索引的 context 成本已失控**：issue #54 实测装 `aws-core` 后，13 个 skill 的 description 每个 session 都注入 context，合计 1,606 tokens ≈ Claude Code 默认 1% skill listing 预算的 **73%**，harness 发出 `Skill listing will be truncated / 11 descriptions dropped` 警告，**11 个 skill 的描述被静默丢弃**。全仓 195 份 description 合计 ≈15,861 tokens 印证了这个量级。
- **细粒度治理能力被沙箱化收走**：issue #294 里企业合规要求「把 tool call 限制在特定 CLI 命令上」，而 IAM 条件键只能按服务/动作粗粒度过滤，无法表达这种约束。
- **安装碎片化**：六种客户端六种姿势（Claude Code 走官方 marketplace、Codex 加 AWS 仓库、Cursor 导 team marketplace、Kiro/fx 手写 MCP 配置、CLI 走 `aws configure agent-toolkit`、`npx skills add`）。

### 生态定位
品类定义上，它是**「厂商官方的 agent 侧云依赖注入层」**——这个格子几乎没有直接竞品。真正的竞争关系是三条：

1. `awslabs/mcp` 的存量迁移（AWS 官方自己承认的收敛过程，README 明说 best-of-breed 组件将逐步迁入）；
2. 社区自建 server 的替代压力；
3. **「裸用 CLI」这条零信任基线——这才是最需要认真对待的对手**，因为它是默认值，而本仓需要用户主动改变工作流。

战略上，这是 AWS 在 agent 时代的**控制点保卫战**：如果 agent 只用 CLI，AWS 就失去「谁在调用、是否合规」的可见性。**这个项目的产品价值可能大于它的技术含量。**

## 套利机会分析

- **信息差**：**star 数本身没有低估**——3,192★ 已是 GitHub Trending 级曝光，AWS 官方账号自带媒体放大效应，不存在「未被发现的钻石」红利。**但它的「战略观察价值」被严重低估**：所有做 AI agent 基础设施、IaC 工具、skill 生态的团队都需要知道 AWS 把赌注押在了「skills + 托管 MCP + IAM 条件键」这套架构上——这个仓库是观察 AWS 官方 agent 路线的最佳一手材料，其信号价值 > 代码复用价值。**反向套利风险**：0 release 意味着它现在不适合作为生产依赖引入，想抄作业可以，想 pin 版本做企业管控得等它出 release 策略。
- **技术借鉴**：可直接搬走的有 4 条 —— ① 「Instructions to a model are not an access control」这条原则 + 完整落地形态（策略文件权限校验、白名单默认拒绝、单笔/累计双天花板、gate 完全不读模型输出）；② 路由 skill + 语义类别注册表 + 四档决策分类；③ canonical + vendored + 字节级门禁 + README 映射表双向完整性；④ 把「散文状态机」当可编译对象（引用解析器 + artifact 契约 + 声明式 freshness）。
- **生态位**：它填补的是「**云厂商侧的 agent 知识与治理层**」这个空白——通用 skill 工具（skills.sh、context7）解决「拉上下文」，社区 MCP server 解决「调 API」，但没有一家解决「这个 agent 调的是不是云厂商的云、能不能被云厂商的策略管住」。这个缝隙是结构性的。
- **趋势判断**：处于**发布红利已过、进入长尾稳态**的曲线（当前 +7~10 star/天、+200/月），单靠 star 增速看已无爆发力。但后发优势明显——它站在「AWS 官方 + 195 个 skill + 4 种宿主 + 治理」的位置上，后来者要同时拿到厂商信任、领域知识和分发矩阵，几乎不可能。而它自己相对 `awslabs/mcp`（9,829★）是**后发者**，用 GA 服务端 + IAM 条件键 + 统一分发完成了正面超越——说明在这个赛道，后发 + 做对架构 > 先发 + 摊大饼。

## 风险与不足

1. **最大的认知陷阱：把它当代码库读。** 146,777 行「代码」里真正的运行时实现很少，注释率 192% 不是文档过度注释，而是因为 **SKILL.md 与 references 文档被 tokei 归类为注释**。真实资产是 195 份提示词 + 数百份 reference 文档 + 一套校验工具链。按「软件工程」标准评价它会得出完全错误的结论。
2. **零版本化是硬伤，不是特性。** 一个「已 GA」的项目有 0 tag、0 release，skill 指令可隔日变更。**它可以是优秀的参考实现，但绝不能当生产依赖。** 第三方评测把「无版本化」列为头号问题，代码证实属实。
3. **项目比任何人都清楚「提示词不是控制」，却没把这个原则贯彻到 IAM 治理层。** 这是本项目最深刻的自省：它在支付授权这一处做到了极致（`x402_policy.py` 完全不读模型输出），但它最大的护城河（IAM 条件键）恰恰**只是一个更细粒度的提示词级控制，不是最小权限本身**。第三方评测的批评——「IAM context conditions and CloudTrail/CloudWatch records help distinguish and monitor agent behavior, but they do not create least privilege. Broad create/delete/modify permissions remain broad merely because actions are logged.」（有日志 ≠ 有最小权限）——正指出了这个断层。
4. **「渐进式披露」的官方叙事在索引层面从未成立。** 渐进式披露只作用于正文，不作用于索引——description 在会话启动时就全量进 context。这解释了为什么 195 个 description 写得如此拥挤、如此充满否定式边界声明：那是**在 1024 字符里做路由表的挤压产物**。issue #54 报告的「11 个 skill 描述被静默丢弃」不是 bug，是架构的必然结果。
5. **质量结构性参差。** 每个 skill 由不同服务团队各写各的，没有统一的内容质量标准（194 份 skill 的内容质量零自动测试，只有 frontmatter 结构性校验）。`aws-serverless`、`aws-well-architected-review` 这类会非常好，某些冷门服务的 skill 可能只是把 API 列表抄了一遍。
6. **工程纪律短板清单**：**无 CHANGELOG**（1/5）、**0 tag / 0 release**（2/5）、**无 Python linter/formatter**（391 个 .py 靠约定，`.gitignore` 里有 `.ruff_cache/` 却无 ruff 配置）、`uv run --with jsonschema --with pyyaml` 无版本约束（依赖会随时间漂移）、**194 份 skill 的内容时效性只靠人肉 review**（只有 startup-advisor 有 freshness 契约）、**不接受外部代码贡献**（产品化开源，非社区开源）。
7. **结构性冗余尚未收敛。** `skills/core-skills`（940 次变更）与 `plugins/aws-core/skills`（969 次变更）几乎相等，`aws-serverless/SKILL.md` 在 Top 10 中出现两次（14 / 13）——同一内容双份拷贝，靠 `tools/sync-plugin-skills.py` 维持。这是 6 个月内必然要收敛的技术债。
8. **单点过热。** `plugins/aws-startup-advisor` 独占约 56,481 行 Python（全仓 Python 一半）、1,931 次目录级变更，是唯一有完整测试目录 + 自身 `mise.toml` 的子项目。它正从「插件集合」升级为「有 CLI、有 fixtures、有 38 个测试文件、有工具链的独立产品」——但这也意味着**全仓的内容工程能力只有这一个插件真正做到了位**。
9. **README 无图、topics 为空、homepage 为空。** 一个「四层架构 + 15,000+ API + 195 个 skill」的系统，README 里一张架构图都没有；GitHub topics 为空数组——这是可发现性的直接损失（也是 `ecosystem.competitor_candidates` 采集为空的根因）。

## 行动建议

- **如果你要用它**：
    - **只当参考系，不要当依赖。** 0 release + skill 指令隔日可变，无法 pin，无法复现，**绝不要进生产依赖清单**。
    - **选它**：你的团队已经在用 Claude Code / Codex / Cursor，需要 agent 在 AWS 上干活且**可审计**，愿意接受「托管端点不可自托管」和「六种客户端六种安装姿势」。
    - **别选它**：环境离线或网络隔离、需要合规白名单、需要自定 MCP 实现、需要跨云中立——这些场景社区自建 server 或裸用 CLI/boto3 都是更好的选择。裸用 CLI 的真实优势常被低估：**零信任边界、可 pin 版本、已有成熟 CI/CD 集成**。
    - **上手顺序**：`aws configure agent-toolkit` 或 `/plugin install aws-core@claude-plugins-official` 先只装 `aws-core`（25 个 skill），**不要一次装满 5 个插件**——索引成本会立刻失控。
    - **治理起步姿势**（第三方评测的建议值得采纳）：先建只读角色 → 验证 CloudTrail 能看到 agent 的身份 → 再收窄写权限 → 关键操作强制人工审阅。别一上来就给写权限。

- **如果你要学它**：
    - **必读 1**：`plugins/aws-agents/skills/agents-pay/scripts/x402_policy.py` —— 「让 gate 完全不读模型输出」的完整实现范式，含配置文件权限校验、白名单默认拒绝、单笔/累计双天花板。
    - **必读 2**：`plugins/aws-startup-advisor/tools/check-skill-refs.py` —— 把散文引用当代码引用解析的 5 级解析器 + baseline 陈旧即失败。
    - **必读 3**：`plugins/aws-startup-advisor/tools/model-staleness.py` —— 声明式 freshness 契约与「正确性失败 vs 时效性失败」分级。
    - **必读 4**：`skills/core-skills/aws-serverless/SKILL.md` —— 四档决策分类（Decided / Leaning / Open / Unraised）与语义类别注册表的完整样本。
    - **必读 5**：`tools/validate.py` + `tools/validate_spec.py` —— 双层校验器（零依赖快检 / 严格规范慢检）与跨 manifest 一致性门禁。
    - **必读 6**：`plugins/aws-core/com.anthropic.claude-code/hooks/secret-safety.py` —— PreToolUse hook 拦截 + 「超时 fail-open」驱动的正则设计约束。
    - **必读 7**：`rules/aws-agent-rules.md` —— 7 条宿主级行为约束的写法样本（含 Secret Safety 段）。
    - **必读 8**：`plugins/aws-startup-advisor/tools/artifact-contracts.json` —— artifact 契约的双来源建模与显式 open_paths。

- **如果你要 fork 它**：
    - **不要 fork 全部**。fork 的价值在于**那套校验与内容工程工具链**（`tools/` + `plugins/aws-startup-advisor/tools/`），而不是 195 份 skill 内容。
    - **优先补的三个洞**：① **加 tag / release 机制**——这是最大的技术债，也是最该被 fork 修掉的东西；② **补 Python linter/formatter**（ruff）+ 锁 `jsonschema`/`pyyaml` 版本；③ **给 skill 内容加 freshness 契约**——把 startup-advisor 的 `model-staleness.py` 模式推广到全部 194 份 skill。
    - **架构上可动刀的地方**：① **消除 canonical/vendored 双份拷贝**——改用构建期生成或 symlink（注意该仓的 `reject_symlinks` 是有意的安全策略，改造需重新论证）；② **收敛 description 预算**——195 份 description 合计 ≈15,861 tokens 是一次会话的固定税，可以做两级索引（先检索描述符再加载 skill），这是当前架构最痛的点；③ **补一个 `CHANGELOG.md`**——对用户侧变更叙事是零成本的。

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | https://deepwiki.com/aws/agent-toolkit-for-aws （已收录，本次未取到内容） |
| Zread.ai | https://zread.ai/aws/agent-toolkit-for-aws （已收录，页面存在但需 JS/鉴权） |
| 关联论文 | 无 —— 这是产品发布而非研究项目，arXiv 上没有对应论文 |
| 在线 Demo | 无官方 playground。但有三条真实验证路径：`aws configure agent-toolkit` 一条命令接上本地 AWS 账号；AWS Lambda 的 [Agent setup guide](https://docs.aws.amazon.com/lambda/latest/userguide/agent-setup-guide.html)；Kiro / Cursor 的插件面板可即时浏览已装 skill |
| 官方文档（最权威，建议从这里入门） | [概念与边界](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/what-is-agent-toolkit.html) · [Skills 机制](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/skills.html) · [MCP 工具全量参考](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/understanding-mcp-server-tools.html) · [IAM 与条件键](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/security-iam.html) · [OAuth 2.1 直连](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/oauth-authentication.html) |
| GA 公告 / 产品页 | [AWS News Blog GA 公告](https://aws.amazon.com/blogs/aws/the-aws-mcp-server-is-now-generally-available)（2026-05-06） · [产品页](https://aws.amazon.com/products/developer-tools/agent-toolkit-for-aws/) |
| 外部评测（值得一读，且需过滤细节） | [MCP meets IAM in our Agent Toolkit for AWS review](https://mrkeyoor.com/repos/agent-toolkit-for-aws)（实验室评测，Setup 3/5、Maturity 3/5，指出「有日志 ≠ 有最小权限」） · [Agent Toolkit for AWS: What the Official MCP Servers and Skills Actually Install](https://hysenlabs.com/projects/aws-agent-toolkit-for-aws)（批判性编辑视角，无版本化 + 安装碎片化 + README 缺少沙箱边界定义） |

> **阅读第三方评测的一个提醒**：部分评测（如 hysenlabs）声称 MCP proxy 用 `@latest` 未固定版本——**与代码不符**。`plugins/aws-core/mcp.json` 实际写死 `mcp-proxy-for-aws-cli==1.7.0`，全仓五个插件的 mcp.json 均如此。读第三方评测时这类未核对源码的细节需要过滤。
