# GitHub 推荐：Claude 赏金包：83 个技能实测提升为 0，凭什么火

> GitHub: https://github.com/elementalsouls/claude-bughunter

## 一句话总结
一个把「漏洞赏金方法论」拆成 83 个可自动加载的 Claude Code 技能、433 条可逐条点击验证的公开报告引用、以及一层确定性安全引擎的知识包——它的价值不在于让 AI 更会打洞（作者自己的消融实验实测 delta = 0），而在于让 AI 打得**可审计、不越界、不幻觉**。

## 值得关注的理由

1. **Agent Skills 生态里第一个把「内容工程」当产品做的项目**：不只是写 markdown，而是建了一条完整的内容供应链——采集（`harvest_h1.py`）→ 分类（`classify_reports.py`）→ 覆盖缺口检测（`report_coverage.py`）→ 内容级引用核验（`verify_citations.py`）→ 客户标识泄漏扫描（`scan_identifiers.py`）→ CI 绑定。同类项目（Claude-Red 等）只有索引生成，没有引用验证。
2. **罕见地公开了对自己不利的实验结果**：`eval/BASELINE.md` 明确写明 skills-on 与 skills-off 在 Juice Shop 上都是 3/3，delta = +0%，且 skills-on 反而多花 1 轮、贵 $0.076；作者据此把引擎派 agent 时的 `skills_on` 默认值直接改成 `False`（`engine/agent.py:26`）。这是本仓库工程态度最好的一段。
3. **「确定性优先 + 人在环」的安全工程范式值得单独抄**：范围判定是代码层的 deny-wins allowlist（`engine/scope.py`），不是 prompt 里的一句话；agent 失败明确**不算**覆盖完成（`engine/closure.py`），报告尾部自动生成「Not tested — do not read as passing」段；验证由独立第二 agent 复验，且**以验证方的校准严重度为准**。

## 项目展示

![claude-bughunter banner](https://raw.githubusercontent.com/elementalsouls/claude-bughunter/main/assets/banner-v2.svg)

项目主页横幅 — 83 个技能 + 15 个 slash command + 确定性引擎的技能包

![architecture overview](https://raw.githubusercontent.com/elementalsouls/claude-bughunter/main/assets/architecture-overview.svg)

架构总览 — 知识层（skills）/ 编排层（commands）/ 执行层（engine）三层分离

![capability map](https://raw.githubusercontent.com/elementalsouls/claude-bughunter/main/assets/capability-map.svg)

能力地图 — 按漏洞类型、企业平台、交付流程切分的技能矩阵

![engagement flow](https://raw.githubusercontent.com/elementalsouls/claude-bughunter/main/assets/engagement-flow.svg)

engagement 流程 — SCOPE → RECON → HUNT → VALIDATE → CAPTURE → REPORT 六阶段

![harness routing](https://raw.githubusercontent.com/elementalsouls/claude-bughunter/main/assets/harness-routing.svg)

多 harness 分发 — Claude Code / OpenCode / Codex CLI / Hermes Agent / AntiGravity 一套内容多运行时

![star history](https://raw.githubusercontent.com/elementalsouls/claude-bughunter/main/assets/star-history-light.svg)

Star 增长曲线 — 2026-11-16 至 11-18 三天涨约 4,600 star（占当前总量的 44%），由 Trending 日榜与 v2.1 发布触发

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/elementalsouls/claude-bughunter |
| Star / Fork | 11,186 / 1,499（Watcher 58） |
| 代码行数 | 13,941 行（Python 74.9% / SVG 13.2% / PowerShell 5.2% / Shell 3.7%），注释 28,609 行 |
| 内容规模 | 83 个 SKILL.md（29,871 行）+ 36 个 pattern library + 15 个 slash command + 48 篇文档（47,739 行） |
| 项目年龄 | 6.5 个月（创建 2026-05-05，最近推送 2026-11-18） |
| 开发阶段 | 密集开发（346 commits，近 90 天 183 个；周末占比 25.1%，深夜占比 23.7%，属职业项目） |
| 贡献模式 | 小团队（17 位贡献者，主作者占 45.1%，Top 贡献者 28.4%） |
| 热度定位 | 大众热门但内核小众精品（3 天涨 44% 是 Trending 脉冲，非口碑积累） |
| 依赖 | 运行时零第三方依赖（`dependencies = []`，`requests` 仅为可选 extra） |
| 质量评级 | 代码[良好] 文档[优秀] 测试[基本] |

## 作者视角：为什么存在这个项目

### 创始人/作者背景
Sachin Sharma（elementalsouls），印度独立安全研究者，GitHub 账号 7.6 年、41 个公开仓库、549 粉丝。Bio 自述 Adversary Simulation / Automated Reconnaissance——一线 offensive security 从业者。本项目在其最近活跃的仓库中排第 1，是绝对主导项目；姊妹项目 Claude-OSINT（3,086 stars）由本项目 re-export 两个 recon skill 派生，README 明说两者「byte-identical」，即 bughunter 是母本。

作者的自述经历高度具体：Bugcrowd 报告话术、on-prem SharePoint 农场、CVE 链、Android APK 逆向。这些不是转述的二手经验，而是 skill 里那些具名事故复盘的来源。

### 问题判断
作者看到的问题不是「AI 不会打洞」，而是**AI 打洞的过程不受控**。README「Why this exists」逐条列出的四个赏金侧缺口（无 hypothesis 纪律、无 per-program 报告策略、无 engagement 协调、无 evidence 卫生）与五个红队侧缺口（保守默认提前收手、无 mid-engagement 态势感知、无企业平台攻击链、无客户交付物格式、无 post-credential 升级模型），全部来自自己跑过的 engagement。

最关键的一层判断藏在 `engine/README.md` 末段：作者的消融实验证明 skill 对模型能力增益约 0，却让 agent 多花 12–15k token。于是项目的存在理由被明确定义为「**把裸能力变成安全、确定性、技能路由、人在环的引擎**」，而不是「skill 越多越强」。这是全仓库最清醒的一句话。

时机为什么是现在？三件事同时成立：Claude Code skills 机制与插件市场成熟（`.claude-plugin/plugin.json` 用的是较新的 `userConfig` + `mcpServers` schema）；模型基线已强到「skill 不加能力」——这恰恰是敢于把价值定位在知识与纪律层的前提；HackerOne 公开 GraphQL 可用且报告页 `<meta description>` 暴露约 400 字摘要，使「用公开披露报告喂养 skill」第一次在合规与工程上可行。

### 解法哲学
- **确定性优先（Deterministic-first）**：`engine/README.md` 五条设计原则第一条——广度性工作（recon、参数发现、secret 扫描、指纹识别）是纯 Python + 被动工具，**$0、无 agent、不烧速率配额**；LLM 只留给少数判断题。
- **映射优先、狩猎可选**：默认 phases 是 `["recon", "rank", "map"]`（`engine/engine.py:57`），产物是 `arsenal.md`——每个 endpoint/参数对应哪些 hunt-* skill + 第一条 curl，由人决定往哪投 agent。`--hunt` 才启动 agent。
- **安全由构造保证**：scope 是代码里的 allowlist，不是 prompt；agent 默认 read-only（`--allow-intrusive` 才放开）；确认的 finding 还会跑一次确定性 scope-audit 检查 PoC 是否碰过越界 host。
- **明确不做什么**：README「Out of scope (deliberate — not gaps, design decisions)」逐条排除——内网 AD（Kerberoasting/DCSync）、C2 框架、后渗透/持久化/横向、AV/EDR 绕过、iOS/硬件/RF/ICS、二进制内核。对比偏 agent 化的竞品，作者选的是知识 + 纪律 + 人机分工这条窄路。
- **策展由人做**：`research/reports/README.md` 一句话点破——工具只做采集、找覆盖缺口、起草骨架，「**You own the curation**」。

### 战略意图
**商业模式是「赞助 + 声誉」而非 SaaS**：README 顶部有 ApiSmart / ThreatWatch360 两个 sponsor logo + `.github/FUNDING.yml`，两个赞助商的业务（LLM API 聚合、AI 攻防平台）恰好与本项目互补。没有托管版、没有企业版；代码 MIT、技能方法论与文档 CC BY 4.0（`LICENSE` + `LICENSE-CONTENT` 双许可证），明确允许商业复用。

**开源策略是 genuinely open**：v3 的 20 个 community skill 来自外部 PR，贡献者 17 人。路线图里的 Autopilot Ledger 记忆系统、确定性编排、多 harness 支持、HackerOne MCP 已全部落地，只剩「program-rules-parser skill（自动生成 scope.md）」仍 open。

一个战略隐忧：作者的姊妹项目 Claude-OSINT 已在抢同一个生态位（recon 段），而本项目的上游来源 `shuvonsec/claude-bug-bounty` 已 301 重定向为 `awarexone/Agentic-Bug-Hunter`（5,991 stars），正在原地长成一个有 CLI + 9 个 agent + 35 个工具 + MCP + pytest 的完整产品。

## 核心价值提炼

### 创新之处

1. **「引用数 = 可 grep 数 + 内容级核验 + 主动下调虚高数字」的知识库可信度三元组**（新颖度 4/5 | 实用性 5/5 | 可迁移性 5/5）
   `docs/disclosed-reports/README.md` 把 `report_count` 定义为「该 skill 引用库中唯一 H1 report URL 数」，并给出 grep 命令让任何读者自行验证；`research/reports/verify_citations.py` 逐条抓取公开标题 + `<meta>` 摘要、重跑分类器，判定 MISMATCH / WEAK / OK，当前 433 条 0 mismatch 0 weak。作者甚至主动把 `hunt-source-leak` 的引用数从 31 下调到 7，并在 CHANGELOG 写明「honesty, not lost coverage」。
   *适用场景*：任何以「引用 N 篇论文/报告」为卖点的知识库、评测集、benchmark 文档。

2. **「blocked 不算 covered」——把 agent 的不确定性与阴性结论分开记账**（新颖度 4/5 | 实用性 5/5 | 可迁移性 5/5）
   `engine/closure.py` 的 `COVERED = {"clean","finding","not_applicable","out_of_scope"}` 刻意排除了 `blocked`；`engine/engine.py:hunt()` 中 agent 硬错误时**不** mark_tested，item 留在 worklist 待重试并记 `blocked`；报告尾部由 ledger 自动生成「Not tested — do not read as passing」段。代码注释写明了动机：「A report that lists only findings silently implies everything else was checked and clean, which is the most dangerous default a pentest deliverable can have」。
   *适用场景*：任何自动化审计 / 扫描 / agent 执行系统的覆盖率声明。

3. **「分层顺序陷阱」——验证错误不证明鉴权通过**（新颖度 5/5 | 实用性 5/5 | 可迁移性 4/5）
   `skills/triage-validation/SKILL.md` 的 THE LAYER-ORDERING TRAP：sanitiser / body parser 可能跑在 auth middleware 之前，畸形 body 的 400 与「过了鉴权的 400」响应形状完全一致。必须用**格式良好的最小 body**（`{}`）重测，只有第二个响应能告诉你 auth 层在哪。作者记录了一次真实 engagement：大批端点返回 validation 形状的 400，若读成 auth bypass 就是一整批针对生产金融/管理操作面的 False Critical。
   *适用场景*：任何 AI 驱动的漏洞检测——这类「证据形状歧义」是 LLM 最高频的假阳性来源。

4. **「不可验证 ≠ 假设为真」的三态可选依赖探测**（新颖度 3/5 | 实用性 4/5 | 可迁移性 5/5）
   `engine/skill_map.py:_present()` 在 `os.listdir` 抛 `OSError` 时返回 `None`（与空集显式区分），`_filter()` 遇 `None` 返回 `[]`。宁可路由到零个 skill，也不路由到不存在的 skill——路由到不存在的 skill 会诱导 agent 幻觉。
   *适用场景*：插件/技能系统、运行时可选依赖、多安装路径。

5. **404 baseline 三元组（status + byte length + body hash）作枚举前置闸**（新颖度 4/5 | 实用性 5/5 | 可迁移性 5/5）
   `skills/hunt-dispatch/SKILL.md` step 0 强制执行：现代 SPA/Next.js 对不存在路径返回 200 + 应用 shell，状态码不能证明路径存在。规则是「no path is 'found' until its response differs from the control」，且需按 host、按路径深度分别重建基线（作者记录过同应用不同 host 的 soft-404 body 大小差异巨大）。
   *适用场景*：SPA / Next.js / React + CDN 资产枚举、资产管理系统、监控系统健康检查。

6. **「凭据决定工具可见性」的 MCP 设计**（新颖度 3/5 | 实用性 5/5 | 可迁移性 5/5）
   `mcp/hackerone/server.py:_tools()`：只有当 `HACKERONE_API_USERNAME` + `HACKERONE_API_TOKEN` 都在环境里，`tools/list` 才追加登录态工具。模型看不到这些工具就不会瞎调。纯标准库手写 JSON-RPC over stdio，含协议版本协商、双重分页上限（`_MAX_PAGES = 50` + 一页零新记录即停）、错误分级（ToolError→isError、InvalidParams→-32602、LookupError→-32601、兜底 -32603）。
   *适用场景*：所有需要可选凭据的 MCP server；也适合 API 工具的权限分级设计。

7. **「参数有效性」用 marker 归一化 body diff 实测，而非靠参数名推断**（新颖度 3/5 | 实用性 5/5 | 可迁移性 5/5）
   `engine/recon.py:prune_inert_params()`：取无参基线，再带 `?param=zq9k7xp` 请求，把响应体里的 marker **先替换掉**（避免 canonical/og:url 回显陷阱），然后比对长度与前 6000 字节；HTTP ≥400 判 dead，**探测失败（code==0）一律保留**（「不能判定 ≠ 已判死」）。
   *适用场景*：fuzzing 语料清洗、参数模糊测试、爬虫参数抽取。

8. **「OOB-Or-It-Didn't-Happen」+ 逐参数 payload 归因 + 阴性对照入报告**（新颖度 4/5 | 实用性 5/5 | 可迁移性 4/5）
   `skills/hunt-ssrf/SKILL.md`：明确列出「什么不算 SSRF 确认」（服务器回显 URL ≠ 出站请求）；因为 Burp 按 **payload ID** 而非子域名键控交互，必须每个候选参数一个新 payload、每次一个请求，无回调的参数**也要写进报告**作为证据。作者的真实案例：配置里用的是 `apiUrl` 但真正生效的是 `url`，批量打两个参数会得出错误归因。
   *适用场景*：OOB 型漏洞验证（SSRF/XXE/命令注入）、多候选路径归因。

9. **「公开自己消融实验结果为 0」的评测诚实度**（新颖度 4/5 | 实用性 4/5 | 可迁移性 5/5）
   `eval/BASELINE.md` 公布 skills-on/off 各 3/3、delta +0%、skills-on 反而多花 $0.076，并解释天花板效应；`engine/agent.py` 据此把 `skills_on` 默认设为 `False`——即**用自己的实验结论反过来改产品默认行为**。
   *适用场景*：任何声称「我们的知识库让 AI 更强」的团队——这是唯一能证伪的表述方式。

10. **哈希 denylist + 全树扫描 + fail-closed CI 的客户数据防泄露**（新颖度 4/5 | 实用性 4/5 | 可迁移性 5/5）
    `scripts/scan_identifiers.py` 扫所有被跟踪的文本文件（含 SVG / CHANGELOG / tests），禁用名单存 **SHA-256 哈希**而非明文（明文覆盖放 gitignored 本地文件，运行时哈希），CI `leak-guard.yml` 每次 push/PR 跑且**无路径过滤**，denylist 缺失时 fail closed。「不把客户名字提交进公开仓库」这条硬规则因此可执行。
    *适用场景*：任何有客户数据的开源项目（咨询、渗透、外包）。

11. **「一引擎多 harness 的描述裁剪」**（新颖度 3/5 | 实用性 5/5 | 可迁移性 5/5）
    `scripts/install.sh:283-330` 内嵌 Python，仅在 `~/.agents/skills` 副本把超长 description 截到 ≤1024 字符（Codex CLI 硬限），`~/.claude` / `~/.hermes` 保留全文；`scripts/lint_skills.py` 另加 YAML-safety 检查抓未加引号的 `: ` 值——这条正是真实多 harness 测试暴露的（`hunt-ntlm-info` 因 `WWW-Authenticate: NTLM` 被 Codex 拒绝，而 Claude/OpenCode/Hermes 容忍）。
    *适用场景*：一份内容多运行时分发（Agent Skills / MCP / 插件市场）。

12. **「manifest + JSON Schema + 生产者/消费者声明表」的跨项目数据契约**（新颖度 3/5 | 实用性 4/5 | 可迁移性 5/5）
    `docs/recon-manifest.schema.json` v1.0（`required: [schema_version, target, generated_at, assets, ranked_surface]`），每个 section 明确由谁写、被谁读，「A producer that doesn't discover a section leaves it empty — never absent」。
    *适用场景*：多 agent / 多工具 / 多仓库协作的中间产物交接。

### 可复用的模式与技巧

1. **规则表 + 自检 + CI 阻断的「确定性路由」**：把「该用哪段知识」写成纯字典表，附自检脚本（映射到的必须存在、存在的必须可达），CI 失败即阻断 —— 任何 LLM 应用的「知识选择层」
2. **三态可选依赖探测（present set / empty set / None）**：不可读时返回 None 而非空集 —— 插件系统、运行时可选依赖
3. **代码层 scope allowlist（deny-wins + default-deny）+ 四类 pattern（apex/裸域名/wildcard/CIDR/正则）+ suffix-confusion guard 自测** —— 任何会主动发请求的 agent 工具
4. **三层安全防线：规则层闸门 + prompt 层把范围展开成具体 host 列表 + 事后 scope-audit 扫 PoC 里的越界 host** —— 自动化安全评估
5. **「发现者 ≠ 判定者」双 agent 对抗复验，且以判定方的校准严重度为准** —— 自动安全检测的确认环节
6. **7 问硬闸 + 三档结论（PASS / DOWNGRADE / KILL）+ Q7 反向语义**：「If you CANNOT write step 2 as a real HTTP request → KILL IT」—— 评审模板
7. **方法论与出处分目录**（skills/ 写怎么做，docs/ 写凭什么这么判断）+ 两层 grounding 分离 —— 「方法论 + 证据」型知识产品
8. **「dead-class」skip 策略**：只在可证明浪费时跳过 + 有复活机制 + 每次 skip 必须 log；JSONL 追加用文件锁且轮转在锁内 —— 跨会话 agent 成本压缩
9. **自评分 oracle + 单变量消融 + 模型固定 + 公开不利结果 + 用实验结论反改产品默认** —— 任何声称「知识库让 AI 更强」的团队
10. **确定性优先（$0 无 agent）+ 映射优先狩猎可选 + 显式 `--allow-intrusive` 才放开副作用** —— 默认面向「人在环」的高风险 agent 流程

### 关键设计决策

**决策 1：skill 自动触发靠 frontmatter 的 `description` 语义匹配，slash command 走显式强制加载**
- 问题：83 个 skill 全量塞进上下文既贵又会互相污染（hunt-ssrf / hunt-lfi 的 payload 表会打架）
- 方案：`CONTRIBUTING.md` 定死 frontmatter 契约（`name` 小写连字符 + `description` ≤1024 字符 + `sources` 必填 + hunt-* 另需 `report_count` 整数 + body ≤500 行）。description 里把触发词写成自然散文，并塞入具体 bounty 金额抢占语义空间——`hunt-ssrf` 的 description 直接列出 Capital One 106M breach、Shopify Exchange $25k 等真实披露
- Trade-off：语义匹配有误触发/漏触发风险。作者的对策是**收窄 description 归属**——CHANGELOG 记「Dispatch dedup (description-scoping only — bodies unchanged)」，把 `hunt-jwt-crypto` 定为 JWT-crypto 的唯一 owner，`hunt-sqli`↔`hunt-nosqli`、`hunt-auth-bypass`↔`hunt-saml` 等互相 defer。代价是改 description 时要手工维护互斥关系
- 可迁移性：**高**。「description 归属表 + body 不动 + lint 强制长度上限」是任何 skill/插件库项目的通用解法

**决策 2：路由与范围判定用确定性代码（字典表 + 正则 allowlist），LLM 只留给少数判断题**
- 问题：安全关键约束若交给模型判断，会出现「模型认为自己在范围内」
- 方案：`engine/skill_map.py` 三张纯字典表（48 个 attack class → skill、24 个技术栈 → skill、48 条 curl-first 首探）；`engine/scope.py` 的 `Scope` 类支持 apex/裸域名/`*.example.com`/CIDR/`re:` 五种 pattern，**deny-wins + default-deny**，自检里带 suffix-confusion guard（`notexample.com`、`example.com.evil.com` 必须判越界）；`engine/engine.py:CLASS_WEIGHT` 给 48 个 class 确定性权重（rce 100 → ntlm-info 25）
- Trade-off：字典表需人工维护，但自检会双向报错（「映射到但未安装」/「已装的 hunt-* 无法被任何映射到达」）；换来路由可审计、可 diff、可 CI 化，且**路由错误只会漏检不会越界**
- 可迁移性：**高**。「规则表 + 自检 + CI 失败即阻断」是任何「LLM + 确定性护栏」系统的通用骨架

**决策 3：把「范围/只读」做成三层防线，且在代码层而非 prompt 层**
- 方案：(a) `engine/scope.py` 确定性 allowlist，recon 与 hunt dispatch 两处都过滤，越界直接 `mark_tested(coverage="out_of_scope")`；(b) `engine/engine.py:_roe()` 把授权范围**展开成具体 host 列表**写进每个 agent prompt，并禁止「为证明发现而请求第三方 host」；(c) `engine/engine.py:_scope_audit()` 对确认的 finding 再扫一遍 PoC 里的 host，越界打 ⚠ 旗标
- Trade-off：closure 硬闸会让很多 engagement 无法「干净收尾」——宁可交一份带 caveat 的报告，也不交一份看起来干净却悄悄漏项的报告
- 可迁移性：**高**

**决策 4：验证阶段用第二个对抗性 agent 复验，且以验证方的严重度为准**
- 方案：`engine/engine.py:validate()` + `_validate_agent()`，prompt 明写「be skeptical — default to false positive if unproven」「If the only proof would require an out-of-scope host or an intrusive action, treat the impact as UNPROVEN and lower the severity」；返回后 `c["severity"] = v["severity"]`
- Trade-off：验证 agent 的调用成本翻倍；换来 confirmed 列表可信
- 可迁移性：**高**

**决策 5：VRT 映射不硬编码严重度，而是给「搜索层级 + 常见映射 + fallback + 手动覆盖话术」**
- 方案：`skills/bugcrowd-reporting/SKILL.md` §1 的五级搜索顺序（bug 主类 → 数据类别 → 被绕过的控制 → 端点类型 → 通用父节点）+ 七行映射表 + 两个 fallback + 「没有好 VRT 就选 Other 并在正文首段写 mapping note」
- Trade-off：不是机器可执行的映射表（无 `vrt.json`），靠模型读表；换来对 VRT 版本漂移的鲁棒。且 `bugcrowd-reporting/SKILL.md:19` 明确免责——「always read the severity the current form actually auto-suggests for this program rather than assuming the value here」
- 可迁移性：**中**（VRT 是 Bugcrowd 专属概念，思路可迁移但内容不可）

**决策 6：安装器用 manifest + 跨 bundle 共有所有权做幂等与干净卸载**
- 方案：`scripts/install.sh` 写 `~/.claude/.skill-manifests/claude-bughunter.txt` 记录足迹；卸载时遍历其他 manifest，共享资源保留并计数；安装时对已存在且**字节相同**的 skill 直接跳过（注释：「e.g. a sibling bundle installed the same shared skill → skip; no needless backup, no 'last installer wins'」），不同的则 `mv` 到 `~/.claude/install-backups/<ts>/`——**备份放在加载路径之外**
- Trade-off：manifest 需维护；「字节相同就跳过」意味着上游更新后本地不会被覆盖
- 可迁移性：**高**

**决策 7：不开源 skill 正文里的 payload 攻击字符串（vendored 的 `security-arsenal` 除外）**
- 问题：`CONTRIBUTING.md` 明令「Skills that include actual exploitation payloads against specific targets — keep things abstract / class-based」
- Trade-off：弱化「复制即用」；换来贡献门槛低、法律风险低、社区更愿意贡献（20 个 community skill 来自 v3 PR）
- 可迁移性：**中**（合规取舍，依项目而定）

**决策 8：知识内容与知识出处分成两个目录**
- 方案：`docs/disclosed-reports/README.md` 开宗明义——「The SKILL.md holds the methodology an operator runs; these files hold the *public disclosures that prove the patterns are real*」；`cbh classify` 的输出直接把两条路都指出来（`📖 Pattern Library` + `📋 Skill`）
- Trade-off：读者需跨目录对照；换来 SKILL.md 保持可加载、pattern library 保持可审计
- 可迁移性：**高**

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | claude-bughunter | Agentic-Bug-Hunter（原上游） | Claude-Red | Strix |
|------|---------|--------|--------|--------|
| Star / Fork | 11,186 / 1,499 | 5,991 / 1,096 | 11,211 / 1,538 | 76,504 / ~8,700 |
| 形态 | Claude Code 技能包 + 确定性引擎 + MCP | 独立 CLI + 9 个 agent + 35 工具 + MCP | 纯 SKILL.md 集合（78 skills） | Docker 自主渗透 agent |
| 知识资产 | **433 条 content-verified 引用 + 36 个 pattern library** | 26 个 Web2 漏洞类 skill，无引用体系 | 广度目录（AD/无线/IoT/exploit-dev） | 无知识库引用层 |
| 执行能力 | 无（教模型打，自己不动手） | 有（scanner pipeline + autopilot loop） | 无 | **有（可运行 PoC + CVSS + fix 建议）** |
| 安全护栏 | **代码层 scope deny-wins + 覆盖账本 + 7-Question Gate** | 未见同等覆盖强制 | 无 | 沙箱隔离 |
| 模型后端 | Claude/Anthropic 系 | **多后端（Ollama 本地 / Groq / DeepSeek / Claude / OpenAI）** | Claude | 自有 |
| 报告层 | **Bugcrowd VRT 映射 + OOS 反驳 + 证据脱敏** | 通用报告写作 | 无 | 开发者导向报告 |
| 企业平台覆盖 | **8 个（M365/Okta/vCenter/VPN/SharePoint/Cloud-IAM/APK/iOS/supply-chain）** | 以 Web2/Web3/凭据/逆向为主 | 云 1 个、移动 1 个 | 通用 |
| 评测证据 | **有消融实验（结论为 delta=0，诚实公开）** | pytest 回归套件 | 无 | 无公开数字 |
| 定位 | 知识密度最高、执行能力最弱 | 自动化管道产品 | 攻击技法广度目录 | 执行体 |

### 差异化护城河
- **技术护城河：中等偏弱。** 核心资产是**内容**而非技术壁垒——433 条引用、36 个 pattern library、83 个 skill 的规范化 10 段模板都可以被任何人用相同方法论复制。`research/reports/` 下的四个脚本（harvest / classify / verify / coverage）方法论是公开的、竞争者可以照做，但**代码量不大**（stdlib only），不构成壁垒。`engine/` 3,168 行编排质量不错，但 `docs/architecture.md` 自己写明「No automated exploitation tooling」「No CI/CD integration」。
- **生态护城河：弱。** 17 位贡献者，Top 1 贡献者占 51%（含 bot 后作者实际约 71%），**单点依赖风险极高**。2 个 tag vs 346 commits 说明项目仍处在「个人项目」阶段。
- **信任护城河：中等偏强——这是唯一真实的护城河。** 三项难以快速复制：① 433 条 content-verified 引用（需要时间 + 网络成本，且**还没人做**）；② 真实授权项目的私有知识（`hunt-sharepoint` 的 EoL on-prem SharePoint 2013 farm 与 ToolShell CVE-2025-53770 前置链、`hunt-aspnet` 的 ViewState 反序列化与双解析器 MAC bypass、`m365-entra-attack` 的 AADSTS 错误码枚举与 Smart Lockout 数学、`apk-redteam-pipeline` 的硬编码 JWT 恢复）——这些公开渠道拿不到；③ 负向案例入库（SharePoint 软 404 误报的 38 payload / 0 回连、`apiUrl` vs `url` sink 归因错误），是「我踩过的坑」，不可批量生成。
- **综合判断：护城河属于「先发的知识资产 + 个人经验」，不是结构性壁垒。**

### 竞争风险
**最可能的替代者：`awarexone/Agentic-Bug-Hunter`**——注意它同时是本项目的**上游**（`shuvonsec/claude-bug-bounty` 已 301 重定向到它）。触发条件有三：① 它把本项目 vendored 的 8 skills + 12 commands 继续演进并加入引用验证层；② 它的 9 个专职 agent（尤其 `autopilot` + `recon-ranker`）跑通端到端结果——本项目 `commands/autopilot.md:56` 引用的 `recon-ranker agent` **在仓库里根本不存在**（没有 `agents/` 目录），这是明确的执行层缺口；③ 它的多模型后端（Ollama / Groq / DeepSeek）解决了本项目 issue #51 暴露的分类器拒绝问题。**它拥有强得多的分发与工程基础设施**，3–6 个月内侵蚀差异化是合理预期。

次可能是 `SnailSploit/Claude-Red`：star 数几乎相同（11,211 vs 11,186）但仅 54 commits——说明 Claude-Red 是**内容型爆发式增长**，本项目是**工程型稳步推进**。若 Claude-Red 补上企业层与流程层，会用同样的 star 基数碾压。

`usestrix/strix`（76K stars，执行体）与 `NVIDIA/SkillSpector`（26.8K，防御侧 skill 扫描器）属不同赛道，不构成直接替代。

一个可预见的失败路径：作者在 issue #152 面对的「从覆盖面转向命中率」张力，若通过**砍 skill 数 + 加深度**解决（58 → 30，每个 1,500 行带引用），能保住知识护城河但缩小与上游的表面差距；若通过**继续扩覆盖面**解决，则必然被上游的自动化 pipeline 碾压——覆盖面是那个项目的天然优势，它有自动化 pipeline 来兑现覆盖面，本项目没有。

### 生态定位
在 AI 安全工具生态里，本项目占据「**知识密度最高 / 执行能力最弱**」的象限。

它是 **Agent Skills 生态中第一个把「内容工程」当产品做**的项目：不只是写 markdown，而是建了「采集 → 分类 → 覆盖缺口 → 内容验证 → leak-guard → CI 绑定」的完整内容供应链。同类的 Claude-Red 有 `regen_index.py`，但那是索引生成，不是引用验证。

它的位置在「Claude Code 插件生态」这个新市场里，而非「渗透测试工具」这个老市场。生态位上它扮演 **「Claude Code 安全插件的 reference implementation + 规范化者」**——6-phase 模型、10 段 skill 模板、7-Question Gate、分层引用结构，实际上在定义「一个 AI 安全 skill 包应该长什么样」。这个规范影响力可能比它的直接使用量更有价值。风险是：**上游更可能成为规范制定者**，因为它有 CLI + agent + 测试 + 更大社区，可以把同样的规范做成可执行的 pipeline。

## 套利机会分析
- **信息差**：低关注度但高质量？**不是**——11K stars、Trending 日榜 #1、3 天涨 44%，热度已被充分定价，不是套利标的。真正的信息差在**内容层**：433 条引用、8 个企业平台 skill（尤其 EoL on-prem SharePoint / ASP.NET ViewState / NTLM 指纹）、以及 7-Question Gate 的 Layer-Ordering Trap 这些细节，**在 star 数和 README 里完全看不出来**，必须读完 47,739 行文档才能获得。
- **技术借鉴**：本报告「可复用的模式与技巧」10 条 + 「关键设计决策」8 条几乎与安全领域无关，可直接搬到任何「LLM + 确定性护栏」系统：blocked 不算 covered、发现者 ≠ 判定者、三态依赖探测、rule table + self-test + CI 阻断、哈希 denylist + fail-closed leak guard、manifest + 跨 bundle 共享所有权安装器、公开自己的消融结果。
- **生态位**：填补了「LLM 做安全研究」这一层的**方法论与交付层**空白——执行层已被 Strix 占据（能真的打），知识层被 Claude-Red 部分占据（广度目录），中间这块「有纪律的作战手册 + 提交流程」目前只有它做得完整。
- **趋势判断**：符合 Agent Skills 生态扩张趋势（插件市场刚出现，`.claude-plugin/` 是新格式），且 2026-11-18 仍在 push。但**后发优势不成立**——它比上游晚 2 个月出生，却已经需要靠「知识深度」而非「产品形态」竞争。

## 风险与不足

1. **发版治理严重滞后**：346 commits 只有 2 个 tag（v2.0 / v2.1），`pyproject.toml` 与 `plugin.json` 仍写 `2.1.0`，而 CHANGELOG 顶部的 `[Unreleased]` 已含 plugin 市场、多 harness、20+ 新 skill。**多数用户实际跑的是 main 滚动状态**，想 pin 一个「安全版本」只能 pin 到可能落后数月的 v2.1——这与 SECURITY.md 建议的「pin to a reviewed tag/commit」直接冲突。**没有 release workflow**。
2. **唯一量化评测结果是 delta = 0**：v0（Juice Shop）只有 3 个 challenge、2×3 的设计无统计意义，skills-on 反而多 1 turn + $0.076；v1（PortSwigger）因缺 PS Academy 账号**从未跑通**。CI 里 `eval-harness.yml` 只做 network-free sanity，不跑真 eval。GitTrending 评测批评的「未给可复现证据、误报率与对比」**在这一点上成立**——作者自己写了批评的答案，只是答案还没跑出来。
3. **「确定性路由 ≠ 确定性且安全的行为」**：OffSec Blog 的批评成立。`engine/` 里的 scope / 只读 / 审计全是围绕**引擎自己派出的 agent** 设计的，对 Claude Code 交互式会话中被自动加载的 83 个 skill **没有等效的代码层护栏**——那些 skill 的约束全是 prompt 文本。外部评测同时指出「自然语言触发会加载冲突指引」「脱敏被强调而证据来源与完整性没被强调」。
4. **供应链信任面**：83 份 SKILL.md（29,871 行）+ shell/python 直接进 agent 上下文，且 `--all` 模式会同时注入 **4 个 harness**（`~/.claude` / `~/.agents` / `~/.hermes` / `~/.gemini/config/skills`）。作者自己在 SECURITY.md 引 Snyk ToxicSkills 研究提醒「treat them like any dependency you run」，但**没有 skill 签名/哈希清单，安装器不 pin 版本也不校验内容，且未接入第三方 prompt-injection 扫描**——而这个项目本身就含大量攻击性 payload 与绕过技术，正是最该被扫的对象。
5. **归属链失效 + 自相矛盾**：`NOTICE` 写「The repository does NOT redistribute upstream community skills directly」，`docs/credits.md` 却写「Vendored foundation skills | 8 | shuvonsec/claude-bug-bounty (MIT)」——而 `skills/` 下确实躺着 `bug-bounty` / `bb-methodology` / `security-arsenal` / `web2-recon` / `web3-audit` / `meme-coin-audit` / `triage-validation` / `report-writing` 这些上游副本。上游重命名后，MIT 归属链的指向路径已失效，两处都需要更新。
6. **文档与现实脱节**：`CONTRIBUTING.md:78` 仍写「There's no automated test suite」——实际有 86 个通过的 unittest 测试（engine/ 34 + tests/ 52）；README 的 credits 行写「43 original skills + 8 vendored」，与 `docs/credits.md` 的「55 original / 20 community / 8 vendored」不一致，而 `doc-count-check.yml` 只检查三个 ground-truth 总数、不检查这个拆分。
7. **工程规范缺口**：无 ruff / black / flake8 / pre-commit 配置（`.githooks/pre-commit` 存在但需手动 `git config core.hooksPath .githooks`，当前为空即默认不启用）；无 type hints（部分函数）；`except Exception` 偏多；`engine/state.py:42,50` 有 ResourceWarning（未用 `with` 管理文件句柄）；无 examples/ 目录、无 demo 脚本、无可运行的端到端示例。
8. **内容覆盖偏斜**：`research/reports/report_coverage.py` 生成的覆盖缺口报告（`gaps.md`）**被 gitignore**——「哪些 H1 报告尚未被策展」这一持续收敛的证据不在公共仓库里。分类器与 skill 目录也存在口径漂移：`engine/recon.py:PARAM_NOISE` 把 `ref` 列为噪声参数，而 `hunt-idor` 的 pattern library 又把 `ref` 列为 IDOR 参数候选。
9. **11 个 skill 超过 500 行**（`osint-methodology` 1,704 行、`bug-bounty` 1,604 行、`bb-local-toolkit` 1,558 行、`security-arsenal` 912 行……），`scripts/lint_skills.py:202-203` 对超限只发 warning 不 fail；只有 `offensive-osint` 一个 skill 真正用了 progressive disclosure。
10. **平台分类器冲突（issue #51）**：交付的攻击性知识撞模型供应商的网络安全分类器，导致「防御者自用」这一最重要场景反而不流畅；目前没有解法。
11. **VRT 覆盖有限**：7 行映射表 + 5 级搜索层级 + 2 个 fallback，对 Bugcrowd 提交够用，但不是完整 VRT 树（100+ 叶子节点）；且 VRT 是 Bugcrowd 专属概念，对 HackerOne / Intigriti / Immunefi 各有各的体系。

## 行动建议

- **如果你要用它**：
  - **先确认你的运行时**。Claude Code 插件路径（`/plugin marketplace add elementalsouls/Claude-BugHunter`）比 copy-install 更安全——它按 release 钉到具体 commit SHA 并跑 Anthropic 的自动审查。**但不要用 README 推荐的 `pipx install git+...` 从 main 装**，那没有 SHA pin。
  - **只用它的知识层与流程层，不要指望它提高检出率**。它的价值在「不打越界、不幻觉、报告能过 triager」，这三点能实打实提高你的**有效提交率（validity ratio）**；它不提高你找到漏洞的数量。想提高检出率，用 Strix 类的执行体，两者可以并用（Strix 打洞，本项目的 triage/report 流程交付）。
  - **务必先做版本固定与指令层审计**。企业部署前，扫描这 83 份 SKILL.md 的指令层风险（第三方扫描曾报 Snyk Fail / Socket Warn），并 pin 到具体 commit。**特别提醒**：PR #140（2026-11-16 合入）修复了默认 OpenAPI 侦察会向受保护路由发送 POST/PUT/PATCH/DELETE——11-16 之前用默认配置跑过活目标的用户需立即升级。
  - **如果你有 EoL 内网 SharePoint / ASP.NET ViewState / NTLM 指纹识别需求**，这 8 个企业平台 skill 是全网独一份的，竞品完全空白，值得单独读。
- **如果你要学它**：**重点看这 7 个地方**
  1. `engine/closure.py` —— 「blocked 不算 covered」与报告尾部 caveat 自动生成（本仓库最可迁移的一条设计）
  2. `engine/scope.py` + `engine/skill_map.py` —— deny-wins allowlist、suffix-confusion guard、三态依赖探测（`None` vs 空集）、字典表自检
  3. `research/reports/verify_citations.py` —— 引用内容级核验（MISMATCH / WEAK / OK 三档判定），以及 `docs/disclosed-reports/README.md` 的双层 grounding 口径分离
  4. `skills/triage-validation/SKILL.md` 的 THE LAYER-ORDERING TRAP 与 7-Question Gate —— LLM 假阳性治理的教科书案例
  5. `skills/hunt-ssrf/SKILL.md` 的 OOB 归因规范（每参数一 payload + 阴性对照入报告）与 `skills/hunt-dispatch/SKILL.md` 的 404 baseline 三元组
  6. `scripts/install.sh:170-190` 与 `scripts/scan_identifiers.py` —— 字节级幂等安装、备份移出加载路径、哈希 denylist + fail-closed CI
  7. `eval/BASELINE.md` + `engine/agent.py:26` —— 如何用实验结论反过来改产品默认值
- **如果你要 fork 它**：
  - **先修发版治理**（加 release workflow，tag 与 CHANGELOG 同步），这是它最明显的短板，也是任何 fork 的第一前提。
  - **接一个第三方 skill 安全扫描器**（NVIDIA SkillSpector 支持 SARIF + 稳定 exit code + `--fail-on-findings`）作为 CI 步骤，补上 SECURITY.md 自己承认的短板——这是明确可执行、尚未做的改进。
  - **补 ruff/black + pytest 配置 + coverage**，并更新 `CONTRIBUTING.md:78` 与 README 的 credits 数字。
  - **修 `commands/autopilot.md:56` 悬空的 `recon-ranker agent` 引用**——要么实现 `agents/` 目录，要么删掉这句承诺。issue #89 已经在讨论这件事。
  - **更新 `docs/credits.md` 与 `NOTICE`** 指向 `awarexone/Agentic-Bug-Hunter`，消除「不重分发」与「vendored 8+12」的矛盾。
  - **想做差异化，别扩覆盖面**——那条路已经被上游的自动化 pipeline 占领。要往「引用深度 + 企业平台私有经验 + 交付质量」三个方向加深，或把 eval 的 PortSwigger 对照组真正跑通并公开一个非零数字。

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | [deepwiki.com/elementalsouls/claude-bughunter](https://deepwiki.com/elementalsouls/claude-bughunter)（探测时连续 4 次 HTTP 429 限流，未能确认收录状态） |
| Zread.ai | [zread.ai/elementalsouls/claude-bughunter](https://zread.ai/elementalsouls/claude-bughunter)（已收录） |
| 官方文档站 | [elementalsouls.github.io/Claude-BugHunter](https://elementalsouls.github.io/Claude-BugHunter)（Just-the-Docs 静态站，含架构文档与 skill 索引） |
| 关联论文 | 无 |
| 在线 Demo | 无（本地安装型 bundle；提供 DVWA / OWASP Juice Shop / Hacker101 / testphp.vulnweb.com 靶场，`eval/` 下含 PortSwigger 消融实验框架） |
| 外部评测 | [OffSec Blog — Structured Bug Hunting](https://www.offsecblog.com/2026/10/claude-bughunter-for-structured.html) · [GitTrending 深度评测](https://www.gittrending.com/article/claude-bughunter-a-new-era-in-bug-hunting) |
