# GitHub 推荐：4553 星、124 条退件模式：把送审变成一道 CI 闸门

> GitHub: https://github.com/mjmirza/app-store-compliance

## 一句话总结

一个把 App Store 与 Google Play 拒审原因沉淀成可核验规则库、并在 AI 编码工具的提交前 hook 里强制执行的合规闸门——真正的资产不是 124 条规则，而是**让规则不会腐烂的核验基础设施**。

## 值得关注的理由

1. **在正确的时间切入了正确的缝隙**：Apple 一年审 777 万应用、拒 193 万（近 1/4），而 AI 让「一天做一个 App」成为常态——造 App 的速度涨了 60%，审核标准却没松口。能力曲线跌破了合规曲线，两条曲线之间的缺口就是这个项目。
2. **它卖的是「可核验」，不是「规则多」**：112 条全球法规截止日期每条都带 `source_url` + `verified_on`，超过 180 天自动告警；还实现了针对 Apple soft-404（未知 article id 也返回 HTTP 200）的字节级指纹检测——编造的引用在这个项目里过不了关。第三方审计抽 17 条核对官方，11 条相符、5 条有出入，但没有一条编造。
3. **零依赖 + 13 个 AI 工具 hook 分发**：只用 Python 标准库 + Bash 内建，`git clone` 就能跑；一条命令接入 Claude Code / Cursor / Copilot / Gemini 等 13 个工具的提交前检查——把合规从「上线前检查清单」变成「每次 commit 都挡一次」。

## 项目展示

![Reddit 讨论：跑完一次性检查并修复后，首次提交即获批](https://raw.githubusercontent.com/mjmirza/app-store-compliance/main/assets/first-try-approval.png)
真实用户的反馈——跑完检查并修复后首次提交即通过。注意这类截图同时是「误报即特性」立场的实证：能被用户忍受的噪音才叫 guard。

![社区聊天：Aura Text to Speech Reader 通过审核后以德语致谢](https://raw.githubusercontent.com/mjmirza/app-store-compliance/main/assets/app-store-approval-thanks.png)
一个德语市场应用的通过反馈，作者本身就在德国，这解释了项目对欧盟法规的深度。

![Apple 平台标识](https://raw.githubusercontent.com/mjmirza/app-store-compliance/main/assets/apple.png)
![Google Play 平台标识](https://raw.githubusercontent.com/mjmirza/app-store-compliance/main/assets/android.png)
双平台同时覆盖——这是它与三个只做 iOS 的同类 Skill 最直接的分界。

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/mjmirza/app-store-compliance |
| 许可证 | OpenRoots Agent License 2.3（SPDX `LicenseRef-OpenRoots-ORA-2.3`，非 OSI 许可；GitHub 因不识别自定义 SPDX 显示「Other / No license listed」） |
| Star / Fork | 4,553 / 290（Watcher 13） |
| 代码行数 | 25,901（Python 45.6%、Shell 33.8%、JSON 20.5%） |
| 项目年龄 | 5.6 个月（2026-06-06 至今） |
| 开发阶段 | 稳定维护（近 30 天 25 commit，近 90 天 56 commit） |
| 贡献模式 | 独立开发者主导（5 位贡献者，主作者占 82.2% 的 commit） |
| 热度定位 | 大众热门（2026-11-19 至 11-22 连续 4 天 GitHub Trending 日榜 #12，star 1709→3832，当前 4553） |
| 质量评级 | 代码[良好] 文档[优秀] 测试[良好] |

## 作者视角：为什么存在这个项目

### 创始人/作者背景

Mirza Iqbal（@mjmirza），9 年 GitHub 账号、119 个公开仓库，住德国法兰克福。他同时维护 6 个德国本地税务/政务 MCP server 和一批 n8n 工作流——这是一个做「本地自动化集成」的独立开发者，不是大厂员工，也不是纯内容创作者。

这个背景直接塑造了项目的指纹：如果只做一份「通用美式 checklist」，不会有 112 条覆盖 33 个辖区的法规截止日期（其中欧盟占 22 条）。合规审计的证据链思维——主张 → 来源 → 核验日期 → 原文引用——是从德国/欧盟的合规实务里搬过来的。

最耐人寻味的一处矛盾：CI 里跑 `no-ai-attribution.yml`，用正则拒绝任何带 AI 作者或归因的 commit。一个给 AI 编程工具生产守门人的项目，自己禁止 AI 出现在 git 历史里。作者的解释是知识库必须是「真人实践沉淀」——**工具可以帮你查，但不能帮你编规则**。

投入权重上，119 个仓库里这是唯一破千星的，且在他最近 push 的仓库中排第 1。

### 问题判断

时机判断极准，作者自己的表述很锋利：「AI 让人一天能做出一个 App，但商店没为洪水放松规则，反而收紧了。」数据侧：Apple 一年审 777 万应用、拒 193 万（近 1/4），2026 Q1 双商店发布量同比 +60%。

问题的另一半是「规则会过期，而且过期比没有更危险」。5 个可比竞品里 3 个已停更——停更不是因为规则难写，是因为**核验成本高**：每条规则都得找到一手来源、读、确认、记日期。作者的判断是这个成本可以被工程化，于是把核验做成了数据结构里的必填字段 + CI 闸门，而不是一次性的写作负担。

### 解法哲学

Unix 哲学优先：**零运行时依赖**（Python 标准库 + Bash 内建 + grep/sed/awk），`git clone` 后 `bash` 就能跑。核心取舍是**保守而非完备**。

明确「不做什么」的部分：

- 不假装能判 Guideline 4.3（安全与隐私）——原话是 Treat any tool that claims it can with suspicion
- 不假装扫描结果是批准——README 首句就写 It does not guarantee approval
- 不读二进制产物、不做运行时证明、不生成 Data Safety CSV——在 `docs/COMPETITIVE-GAP-ANALYSIS.md` 里被记为 the larger work left for later releases

最反直觉的一条是**宁可误报不可漏报**。Issue #834 里 haptics 规则因 WCAG / EN 301 549 并不强制而误报，作者不但没删规则，还把它降级成 advisory、扩展 SwiftUI 语法、补回归用例，并在文档里明写这个检查不计算对比度、不检查焦点顺序。对一个「误报会烦人」的工具来说，这是罕见的克制。

### 战略图景

**基础设施/护栏，不是产品**。作者自己在 `COMPETITIVE-GAP-ANALYSIS.md` 里承认竞争是「采纳」而非能力差距：What remains is not a capability gap, it is adoption. The most popular repository has the stars.

许可策略值得单独说：OpenRoots Agent License 2.3 不是 OSI 许可，但也不是常见的 open-core。它是**规模豁免型**——年营收 2000 万美元以下免费且无条件（个人、非营利、学校、政府任何规模都免费），超出部分按 0.5% 收权利金、每年上限 25 万美元，AI 训练需单独购买许可。因为「本版本不因时间流逝转换为其他许可」写得极硬，大企业法务会先在这一关卡住。

## 核心价值提炼

### 创新之处

按「新颖度 × 实用性 × 可迁移性」排序：

1. **Soft-404 内容指纹检测**（新颖 4 / 实用 5 / 迁移 5）
   Apple 的 news 页面对任何未知 article id 都返回 HTTP 200 且内容字节完全相同——意味着**一个编造的 URL 能通过任何朴素的链接检查器**，这直接击穿了「引用可验证」的前提。解法在 `scripts/verify-citations.py:30-34, 200-215`：为每个会泛化 fallback 的 host 取一个**故意无效的 control URL**，算 SHA-256 指纹（先剥掉 `?\d{8,}` 这种 cache-buster——Apple 的 news 索引会在 asset URL 上轮换数字后缀，不剥掉会让同一个索引看起来像两个页面），然后每个被引 URL 取指纹，**与 control 相同即判定 FABRICATED**。局限也诚实：只对已知会 soft-404 的 host 生效（目前 2 个）。

2. **把「不确定」显式编码进数据 schema**（4 / 4 / 4）
   Issue #659 定下的规矩：无精确日期就保留当月 1 号作为 placeholder + 保留原文措辞；读到二手来源必须写 `source_note`；抓不到一手来源就列进 Unverified 而不是猜一个。这让「规则库的一部分过期了」成为可表达的状态，而不是靠沉默掩盖。

3. **分级 fail-closed / fail-open，而不是全局一个策略**（4 / 5 / 5）
   这是整个项目最关键也最容易做错的架构决策，分级依据是「**信息丢失的风险**」而不是「方便」：
    - 信息可能藏在没读到的文件里 → **fail closed**。`.app-review-readiness.json` 存在但读不了（非法 JSON / 重复 key / 超 8 MiB / 读超时 / python3 不存在）→ 一律 critical 阻断，理由统一写成 `so a fail inside it cannot be seen`（`guard.sh:1734, 1823, 1847, 1854, 1861, 1870, 1876, 1893`）
    - 信息确定不存在 → **fail open（仅 hook 模式）**。找不到 iOS/Android 项目时 hook 模式 exit 0 放行，但**必须打印 `NOT CHECKED.`**；手动模式 exit 1
    - 扫描中途失败 → 结果未知，**绝不是 CLEAR**（`guard.sh:2091-2096`）。`SCAN_ERROR` 非空时输出 `NOT CHECKED.` 而非 `CLEAR.`
    - 逃生阀是一等公民：`APP_STORE_GUARD_OK=1`（有 critical 也放行但写日志）、`APP_STORE_GUARD_BLOCK_UNCHECKED=1`（把 fail-open 翻成 fail-closed，CI 用）

4. **输出完整性契约 + 显式「不信任」verdict**（3 / 5 / 5）
   `scripts/fleet-sweep.py:110-131` 做六项交叉校验：guard 没跑完 / 退出码不在 （0,2） / Summary 行数 ≠ 1 / Coverage 行数 ≠ 1 / **Summary 计数 ≠ 从 findings 行解析出的计数** / **退出码与 critical 计数矛盾**。任一命中 → 该 app 判 `NOT_CHECKED`，**永远不是 ready**。测试里用一个假 guard（`cat report.txt; exit $(cat exit.txt)`）来验证契约本身。

5. **五级来源信任层级 + 「文本只能降级不能升级」**（4 / 4 / 4）
   P1 官方机构 / P2 通讯社 / P3 学术 / P4 行业博客 / P5 社交媒体与 AI 摘要；P4/P5 必须被同主题的 P1 源逐条佐证才能进 PR。分类器用 **host 域名边界匹配**（`host == d or host.endswith("." + d)`，防 `notftc.gov` 冒充）。最关键的一条规则在 `scripts/monitor-regulatory.py:565-660`：正文里出现「政府」「欧盟」**不能**把一个博客升到 P1——信任只能被文本降低，不能被抬高。

6. **一个 hook 脚本自适配 13 种协议**（4 / 4 / 4）
   13 个 AI 工具的 hook 协议各不相同。做法是反过来的：让所有工具把 payload 喂给同一个 bash 脚本，让脚本自己认。三级解析器（`jq` → `python3` → 纯 awk/grep/sed 正则）每级都用 `tool_ok()` 验证「存在**且能跑**」而不是「存在」。非 shell 工具（Read/Edit/Write）直接静默返回——这是关键的误报控制。三级都失败时**保持沉默而不是瞎猜**。README 还明确列出了**没接线的工具**（Kiro、Cline、Amp、Goose、Crush、Roo Code、Continue、Aider、Copilot for Xcode），每个都给出手工接线片段而不是假装支持。

7. **带 revision 的 attestation 模型**（5 / 4 / 3）
   `data/ruling-register.json`（14 条）把「扫描看不见的法律要求」建模成可引用需求：`standing`（in_force / in_force_later / store_policy / proposed——**proposed 不阻塞**）、`proof`（mixed / owner_attested）、`proof_items[]`、以及每条 source 带 `url` + `checked_on` + **`quote` 原文逐字引用** + `supports[]`——引文必须同时覆盖义务与生效日期，否则不予采信。规则一改版，`revision` 递增，旧 attestation 立即失效。

8. **`grep -q` + `pipefail` 陷阱的系统性规避**（新颖 2 / 实用 5 / 迁移 5）
   `grep -q` 命中后立即退出关闭管道，仍在写的生产者收到 SIGPIPE（141），`pipefail` 把整条管道判为非零——**一个匹配变成一次未命中**。项目用 `grep_q()`（`guard.sh:8`）排空全部输入替代，CHANGELOG 记录它曾在 CI runner 上静默漏检而本地不复现，并用 2 万行尾部输入做了回归。

9. **双缓冲（触发 vs 语义实现）**（3 / 4 / 3）
   `.code` 是全部原始内容（用于触发词匹配），`.impl` 是**剥离注释和配置文本后的源码**（用于「你必须实现了这个功能」类规则）。注释写得很清楚：a `.strings`, plist or json mention never proves an implementation——plist 里出现一个符号名不算你实现了它。缓冲末尾写哨兵行，只有哨兵确实落到文件末尾才置 `CODE_OK=1`，用来防御「缓冲写了一半」这个静默失败。

### 可复用的模式与技巧

以下模式与 App Store 完全无关，任何「规则会变」的场景都能直接搬走：

1. **control-id 指纹验证** — 用一个故意无效的对照 URL 算内容指纹，比对即判定编造。适用：任何有 generic fallback 页面的站点（云厂商文档站、政府门户、API 文档）
2. **host-only 可信度分类 + 文本只降不升** — 适用：任何让 LLM 写规则/文档的流水线
3. **schema 承载不确定性** — 把「未核实 / 待生效 / 已被合并」建模成字段而不是沉默。适用：知识库、依赖清单、许可证追踪
4. **分级 fail-open / fail-closed** — 按信息丢失风险决定闸门方向。适用：任何 linter / gate / policy engine
5. **输出完整性契约** — 下游对上游输出做六项交叉校验，任一不符判 `NOT_CHECKED`。适用：机器消费人类产出的一切场景
6. **单次豁免 + 到期强制复审** — waiver 不是永久豁免，是带到期日的债；SARIF 导出保留 `suppressions[].justification` 作为完整审计轨迹
7. **带 revision 的签到模型** — 规则改版自动作废旧签到。适用：政策引擎、合规声明、审计证据
8. **哨兵行作完成标志** — 用「缓冲末尾的标记行」判断写入是否完整，防御静默截断
9. **生成物投影 + CI 漂移检测** — 生成后 `git diff --quiet`，不一致就 fail 并打印 diff
10. **双方向错误率指标** — eval 把 false pass 和 false block 分开统计（`evals/gold-cases.json` 32 个黄金场景 + `eval-scorecard.py`）。gate 类工具里漏放比误挡危险得多，但多数测试只报一个准确率
11. **三级降级 + 解析不了就沉默** — 适配层要能降级，更要能在完全陌生输入时**不猜**
12. **显式登记已知空白** — 把「我们查不了二进制 / 做不了运行时证明」写进文档，而不是让人误以为覆盖了

### 关键设计决策

**决策 1：把「可验证性」而非「规则数量」当作核心资产**

- 问题：规则库必然过期。竞品里 3/5 停更——停更不是因为规则难写，是因为核验成本高（每条规则都得找到一手来源、读、确认、记日期）
- 方案：把核验成本从「写规则时的一次性负担」变成「数据结构里的必填字段 + CI 闸门」。每条 deadline 必填 `source_url` + `verified_on`；`validate.py:validate_provenance()` 在缺失时报 ERROR、超过 180 天报 WARNING；guard 每次运行打印规则包年龄与新鲜度（`Rule pack. v2.5.1. Its 109 dated sources were verified between ... (newest 0 days ago)`），全部超过 60 天就打 `Rule pack STALE`。实测 `data/regulatory-deadlines.json` 的 112 条**无一条**缺这两个字段
- Trade-off：写一条规则的成本从 10 分钟涨到 40 分钟。**护城河就在这个成本差里**——抄规则容易，抄 112 条带核验日期的 deadline 没法抄
- 可迁移性：**高**

**决策 2：单一写入口 + 生成物投影**

- 问题：124 条 pattern、113 条 recipe、112 条 deadline 要同时出现在 JSON、`docs/`、`references/` 三处，手工同步必然漂移
- 方案：`data/` 是唯一 SoR；`references/` 全部由 `scripts/generate-references.py` 生成；CI 跑一次生成然后 `git diff --quiet -- references/`，不一致就 fail 并打印 diff。`scripts/validate.py`（278 行）做交叉一致性：recipe 必须有对应的 pattern id（否则是「永远不会浮现」的死条目），pattern 有 signals 但没 recipe 则 warning
- Trade-off：生成物进 Git，仓库体积换构建简单性
- 可迁移性：**高**

> 值得单独一说的是这个项目与传统「文档即代码」项目的反转：**JSON 有 schema 校验器，文档没有**。常规项目是文档随代码走，这里是数据随 schema 走。

**决策 3：明确的不做什么，被写进文档而不是被省略**

作者在 `docs/COMPETITIVE-GAP-ANALYSIS.md` 里逐条列明「我们还差什么」：构建产物级检查（IPA/AAB、16KB ELF、ZIP 对齐）、运行时证明（账号删除、恢复购买）、Data Safety CSV 生成器。这是竞争分析文档，也是产品路线图——把空白登记为待办，而不是让人误以为覆盖了。

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | app-store-compliance | RevylAI/greenlight | app-store-preflight-skills | app-store-review-skill (safaiyeh) |
|------|---------|--------|--------|--------|
| Star | 4,553 | 2,489 | 1,431 | 467 |
| 形态 | 规则库 + 可执行 guard + hook | Go 单二进制扫描器 | Agent Skill（纯 prompt） | Agent Skill（按 guideline 切分） |
| 平台覆盖 | iOS + Android + 33 辖区法规 | iOS/Android 二进制 | iOS（含 macOS） | iOS |
| 可核验性 | 每条带 source_url + verified_on + 陈旧告警 | 无 | 无 | 无 |
| 构建产物级检查 | 无 | **有**（IPA/AAB、16KB ELF、ZIP 对齐） | 无 | 无 |
| 测试 | 3,522 行 guard 测试 + 32 黄金场景 | — | — | — |
| 分发 | 13 个 AI 工具 hook + CI | CI | Claude Skill | Claude Skill |
| 维护状态 | 11 月 25 commit | 2026-08-05 停更 | 2026-10 停更 | 2026-10 停更 |
| 许可 | ORA 2.3（规模豁免） | 未核实 | MIT | 未核实 |

> 修正一处数据陷阱：仓库事实采集脚本按 `topic=android + language=Shell` 搜出的「竞品候选」全是噪声（termux-packages、PipePipe、opengapps 等），已全部剔除。上表为人工核实后的真实对位。

### 差异化护城河

**信任护城河最强，工程护城河中等，生态护城河弱。**

抄规则容易，抄 112 条带核验日期的 deadline 做不到——这是最难被绕过的部分。第三方独立审计（[yutuo-tech](https://www.yutuo-tech.com/blog/app-store-rejection-playbook-vs-official-guidelines)）从 123 条里抽 17 条核对官方，结果是 11 相符 / 5 有出入 / 1 排名无依据，而那 5 条出入**全部指向「比官方更严」或引用位置不准，没有一条指向编造规则**。这比任何自述都更能说明规则库的诚实度。

工程上：soft-404 检测、五级信任层级、完整性契约、分级 fail-open/closed——都不算复杂，但都是「想清楚了才写得出」的类型。

生态是短板：只有 GitHub 一个分发渠道，13 个 hook 适配虽好但随时可被复制。

### 竞争风险

**最大的风险不是被某个竞品替代，而是被「通用 agent 直接读原始指南」替代。** 如果底层模型足够强、上下文足够长，一个会读 Apple 官方指南的通用 agent 就能做 80% 的事。

作者押的是另一个命题：**知识会过期，而不是知识难获取**。规则获取容易，但「这条规则现在还成立吗、原文到底怎么说的」才是真问题——核验基础设施不会贬值。

次要风险：`RevylAI/greenlight` 在二进制级检查上是真领先，如果它把法规库和 hook 接上，形态会更完整。以及维护分叉信号——已经出现 `takumi913/app-store-compliance`（0 star）这样的 fork。

### 生态定位

不是 checklist，是**「合规领域的开放规则库 + 参考实现 + 守卫工具链」**三合一。在 agent 生态里，它扮演的是「提交前那道 CI 闸门」的角色——当 AI 编码工具让产出速度提升一个数量级时，审核速度没变，于是需要一个自动化闸门把「必然发生的退审」拦在提交之前。

一个值得注意的判断：**「规则数 ≠ 退件原因数」**。第三方审计发现 124 条里有 6 条是网站 Cookie 规则、10 条是无障碍提醒（后者作者自承不会因此被退稿），另有 4 条委外关键项（4.2.6、5.1.1(ix)、4.8 豁免、3.1.2(c)）未被收录。同一份审计的核心观点是：「协助送审」和「保证通过审核」必须分开写——这个区分在本项目的 README 里也做到了。

## 套利机会分析

- **信息差**：**已充分定价，不是套利标的**。2026-11-19 至 11-22 连续 4 天 GitHub Trending 日榜 #12，star 从 1,709 涨到 3,832，当前 4,553；4 天 +2,844 star。同时热度的维护是兑现的——同窗口发布了 v2.5.0 + v2.5.1，25 次提交。Fork 率 6.4%（290/4,553）远高于文档型项目常见的 1–2%，说明用户真的 clone 下来改造。但真正残留的认知差是「**124 条 ≠ 124 种退件原因**」——这个认知本身有传播价值。
- **技术借鉴**：**这是本项目最实在的价值**。soft-404 指纹验证、分级 fail-open/fail-closed、输出完整性契约、带 revision 的 attestation——这四个模式跟 App Store 一点关系都没有，可以直接搬进任何「规则会变」的系统：安全基线扫描、云厂商策略校验、内部编码规范、许可证合规清单、依赖版本策略。
- **生态位**：填的是「规则库会腐烂」这个空缺。不是没人写规则库，是没人解决规则库的保鲜问题。
- **趋势判断**：符合两条趋势——AI 编码让 App 产出量暴涨，监管合规要求在同步收紧（112 条 deadline 里最近 6,748 天逾期天数这个数字说明监管在加速）。这个项目**没有**后发优势（它是先行者），但它的增长曲线说明这个需求真实存在。

## 风险与不足

1. **8,745 行 Shell 没有静态检查进 CI**——项目自己写了 shellcheck disable 注释，却没把 shellcheck 接进 CI。这是最明显的缺口，也是最容易补的。
2. **Windows 是二等公民**——Issue #2330 / #2332 / #2333 三个 Windows bug 全是外部贡献者报的；作者自承 CI 只跑 Linux，Windows 路径是模拟测试而非原生 runner。其中 #2330 的 locale 读取失败导致「静默全清」（fail open，最危险的失败模式）。
3. **124 条规则的准确性没有自动化回归**——外部审计抽 17 条就发现 5 条有出入。目前只靠人工 review + 偶发的外部审计，规则内容本身没有 CI 级断言。
4. **`counterSignals` 只被 `release-audit.py` 消费，guard.sh 未实现**——57/124 条 pattern 定义了反向信号，主路径仍会误报。数据已备好，只差消费端。
5. **构建产物级检查缺失**——与 greenlight、devsemih 的真实差距，不是暂时落后。「你的 IPA 真的对齐了吗」是纯静态扫描永远答不了的问题。
6. **ORA 2.3 对大企业是采用摩擦**——2000 万美元营收以上要付 0.5% 权利金；再加上 GitHub 因不识别自定义 SPDX 显示「No license listed」，双重要求企业法务先解决许可问题。对比竞品 app-store-preflight-skills 是 MIT。
7. **5.6 个月 0 次 refactor commit**——`guard.sh` 已 2,115 行单体 Bash，`monitor-*.py` 家族 6 个文件结构高度相似，`json_unescape` 与三层 `payload_command` 解析器就是技术债累积的证据。测试也从未作为独立议题排期（test 类型 commit 数为 0，测试永远捆在 feature commit 里）。
8. **宣传严谨度落后于内容严谨度**——规则数宣传跨版本不一致（117 / 123 / 124 三个数）；「124 条规则」被读成「124 种退件原因」；LICENSE 是自定义 SPDX 但 GitHub 显示 Other。这是一个以严谨为卖点的项目在自己宣传口径上留下的破绽。
9. **单人维护风险**——4,553 star、13 个 hook 接入点、112 条需持续核验的 deadline，全压在一个人周末 61.4% 的业余时间上。社区协作质量异常高（4 位外部贡献者全是实质 bug 修复、CHANGELOG 逐条署名、issue 标签体系成熟），但规模仍是 1 个人。

## 行动建议

### 如果你要用它

- **在 CI 里用手动模式（exit 1），不要只挂 hook。** hook 模式在找不到项目时会 fail open 放行——这是刻意的取舍，但 CI 场景应该翻成 fail-closed（`APP_STORE_GUARD_BLOCK_UNCHECKED=1`）。
- **先按平台和严重度筛，别被 124 条吓退。** 数据是 apple 62 / google 43 / both 13 / web 6，critical 38 / high 65 / medium 21。真正拦死人的集中在 Guideline 2.x / 3.x / 4.x 与 Data Safety，网站 Cookie 和无障碍提醒那 16 条基本不会导致退稿。
- **企业场景先过法务。** ORA 2.3 在 2000 万美元营收以上有 0.5% 权利金（年上限 25 万美元），AI 训练另购许可。
- **只想要「跑一遍看看会怎样」**：竞品 `app-store-preflight-skills` 是 MIT、更轻、默认拉真实 ASC metadata，是更安全的起点。
- **需要二进制级检查**（IPA/AAB、16KB ELF、ZIP 对齐）：叠加 `greenlight`，不要指望本项目——这是一个已知且明确的空白。
- **Windows 用户**：先在容器里跑一遍（第三方评测也是这么建议的），别直接放进主开发流程。

### 如果你要学它

优先读这几个文件：

- `scripts/verify-citations.py:30-34, 200-215` — soft-404 指纹检测，一个下午就能抄走
- `agent-os/hooks/app-store-compliance-guard.sh:1734, 1823, 1847-1893` — 分级 fail-closed 的判定与理由文案
- `agent-os/hooks/app-store-compliance-guard.sh:53-95` — 三级 payload 解析器 + `tool_ok()` 的「存在且能跑」验证
- `agent-os/hooks/app-store-compliance-guard.sh:495-528` — 双缓冲 + 注释剥离的 awk 状态机 + 哨兵行
- `agent-os/hooks/app-store-compliance-guard.sh:8, 555-561` — `grep_q()` 与 `pipefail` 陷阱的注释解释
- `scripts/fleet-sweep.py:110-131` — 输出完整性契约的六项交叉校验
- `scripts/monitor-regulatory.py:565-660` — 五级来源信任层级与「文本只降不升」
- `data/regulatory-deadlines.json` — 不确定性进 schema 的样板（`source_note` / `absorbed_into` / `revision`）
- `evals/gold-cases.json` + `evals/eval-scorecard.py` — 双方向错误率指标
- `docs/WHAT-THE-SCAN-PROVES.md` 第 7 节 — 三种退出码含义的表格写法

### 如果你要 fork 它

按性价比排序：

1. **把 shellcheck 接进 CI**——作者都写好 disable 注释了，接一下就能用，是投入产出比最高的一步
2. **加 Windows 原生 runner matrix**——作者自己承认这是最大测试缺口，接三个外部贡献者报的 bug
3. **在 guard.sh 里实现 `counterSignals`**——57/124 条 pattern 的反向信号已经在数据里了，只差消费端，能立刻压掉一批误报
4. **补构建产物级检查**——这是竞品占着的位置，也是本项目最明确的能力缺口
5. **给 124 条规则加准确性回归断言**——抽一批高争议规则，把官方原文固化进测试
6. **注意许可继承**：ORA 2.3 对 fork 出的衍生作品适用什么条款，作者没有明确说明——这一步必须先读 `https://openroots.org/licenses/ora/2.3/legalcode.txt`，别靠 README 摘要判断。

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | [deepwiki.com/mjmirza/app-store-compliance](https://deepwiki.com/mjmirza/app-store-compliance)（已收录） |
| Zread.ai | 未能确认（403 + Cloudflare 拦截，实为访问受限而非未收录） |
| 关联论文 | 无（本项目无论文产出）。相关领域背景研究可参考：[Goodbye Tracking?](https://arxiv.org/abs/2204.03556)（FAccT '22）、[Honesty is the Best Policy](https://www.alphaxiv.org/abs/2306.17063v1)（515,920 个应用，97±30% 的「Data Not Collected」标签与政策矛盾） |
| 在线 Demo | 无官方 playground（作者刻意排斥在线托管）。第三方同类：[ipaShip](https://npmjs.com/package/@async-atharv/ipaship)、[Obelisk Club](http://obelisk.club/?lang=zh)、[VOTLI](https://vot.li/) |
| 官方文档站 | GitHub Pages（仓库内 `docs/` + `llms.txt` + `sitemap`） |
| 独立评测参考 | [yutuo-tech 繁体审计](https://www.yutuo-tech.com/blog/app-store-rejection-playbook-vs-official-guidelines)（最有价值，17 条抽样核对）、[Early Signal](https://earlysignal.news/s/mjmirza/app-store-compliance)（中立视角，指出许可显示矛盾与单人维护风险） |
