# GitHub 推荐：AI 搜索黑马 XERJ：3.5 个月 7700 stars，Agent 输出 token 省 2.7 倍

> GitHub: https://github.com/xerj-org/xerj

## 一句话总结

XERJ（发音「search」）是一个用 Rust 写的「为 AI Agent 而生」搜索引擎，3.5 个月发到 v1.0.0-rc.96，靠「Elasticsearch 8.13 兼容 + 一行命令 autoindex + tree-sitter AST 检索 + 自研列存 codec」五件套，让 Agent 在拿到相同答案时比 grep+Python 路线少输出 2.7 倍 token。

## 值得关注的理由

- **3.5 个月 7700 stars + 124 个 RC tag**：判断一个 Rust 新项目是否进入主流曲线，这条数据几乎不需要别的证据；每周 ≈ 550 stars 是同体量搜索/RAG 项目 5-10 倍的成长速度。
- **「五件套」组合定位超出单点能力**：ES 兼容（Kibana 直接用）+ AST 级代码搜索（36 语言）+ autoindex 嗅探 13 格式家族 + `/_memory` Agent 长记忆 + HNSW+exact rescoring（recall 1.00）——任何一个都是独立项目，但 xerj-org 把它们装进了同一个 Rust 二进制。
- **工程诚实度极高**：README 主动列出 4 个输给 ES 的 read-under-write p99 单元，并附 re-run playbook；绝大多数同档项目要么不发数字，要么只发胜场。xerj-org 把败场发在了产品落地页，是「值得在生产侧复盘」的工程文化信号。

## 项目展示

> README 与官网均偏文字 + badge + ASCII 终端块，视觉素材有限；下方为唯一有信息增量的可用图片。

1. ![XERJ demo poster](https://raw.githubusercontent.com/xerj-org/xerj/main/docs/media/demo-poster.png) — 类型：demo（README hero 图）
2. [公开 Playground](https://xerj.org/playground/) — 类型：在线 demo，无需部署即可体验
3. [基准对比页](https://xerj.org/benchmarks) — 类型：benchmark（ES / Qdrant / Meili 横评，含诚实失败清单）

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/xerj-org/xerj |
| Star / Fork | 7,771 / 414 |
| 关注者 | 21 |
| Open Issues / PRs | 92 / 活跃 RC 中 |
| 主语言 | Rust 67.6%（含完整 git 仓库分布：Rust 57.4%，其余为 JSON 14.8% / HTML 9.1% / YAML 6.6% / JavaScript 5.5% / Python 4.5%） |
| License | Apache-2.0 |
| 代码行数 | 718,829 行（含 21.7% 注释；裸代码约 393K 行 Rust） |
| 文件数 | 2,491（含 739 个 .md 文档，2,491 源码文件） |
| 项目年龄 | 3.6 个月（首次提交 2026-06-29，最新提交 2026-10-17） |
| 总 commit | 3,302（近 30 天 1,245，占 37.7%） |
| 贡献者 | 55 人（主作者占 81.5%，第二名 buger 仅 125 commits） |
| 开发阶段 | 密集开发（v1.0.0-rc.96，1.0 正式版仍未发布） |
| 开发模式 | 职业项目（周末 34.8%、深夜 29.3%，但单人主导 = bus factor 高） |
| 热度定位 | 大众热门（周均 ≈ 550 stars，99% 同类项目达不到） |
| Release 节奏 | 124 个 tag、100+ release（语义化版本，平均 1.1 个 tag/天） |
| 质量评级 | 代码 优秀 / 文档 优秀 / 测试 充分 / CI 完善 / 错误处理 一般（unwrap 13087、expect 2974，autoindex 占 3842） |

## 作者视角：为什么存在这个项目

### 创始人/作者背景

`xerj-org` 是一个匿名组织账号，2026-06-28 创建（仅比主仓库早 2 天，明显为本项目而建的专用组织号）。账号无名、无 bio、无公司、无 location、无 blog；除本仓库外另设 41 个 `corpus-*` 仓库，0 stars，全是配套测试语料。这种「刻意匿名 + 集中性投入 + corpus 仓库群」的组合 + 同步上线的 funding.json manifest 与公开招聘「100k+ 粉丝开发者布道者型 CEO」信号，几乎可以确认是 VC 早期支持 / 创始人刻意低调的新创公司开局。代码节奏（rc.0 → rc.96 / 124 个 tag / 1245 commits/30 天 / 自研 4 个 codec family + wire conformance suite）排除了「个人玩票」，但缺乏公开履历链是个真实的「作者可信度」风险信号。

### 问题判断

市场痛点的真实形状：

- AI Coding agent 跑陌生代码库时，单 GitHub repo 就动辄百万行（WordPress 5.2M tokens 级别），上下文窗口根本装不下；
- 工程师退而求其次用 grep+Python 做 RAG：召回质量差（grep 给行不给符号，结果还需打开整文件读）、token 利用率低（命中段常带大量无关内容）、Agent 上下文反复被打断；
- ES 生态成熟但 onboarding 沉重——需要 JVM、schema、Kibana、Logstash pipeline，Agent 不能自己「点几下」就接好。

### 解法哲学

xerj-org 在 `docs/WHY_XERJ.md` 与多篇架构博客中复述了一条清晰的「不做什么」清单：

- **不追全功能 vs ES**：把 ES 8.13 wire 定位成「adoption bridge」，类比 CockroachDB/Neon 走 Postgres wire 的策略——Kibana 等官方 client 不用换，但 agent 内部走精简 12-endpoint native REST；省下来的是「不陷入兼容性军备竞赛」的心智负担。
- **不堆协议**：只暴露一个 9200 端口 + HTTP/JSON；多协议多分流会让 agent debug 噩梦，xerj-org 选了简单。
- **不藏短**：bench 跑出来就发——4 个输给 ES 的 read-under-write p99 单元写在 README 末尾，每个附 re-run playbook。
- **不抢通用 IR 路线**：自研列存 codec 家族 ZBS2/ZNV2/ZFM5/ZPS2，把「agent 反复扫同一类小文档」这个垂直 workload 优化到极致（极端可达 397×，v2 取 random-access-friendly 子集）。
- **不绑死商业化叙事**：5 件套中只有 HNSW+rerank「发送文本出节点」的边是用 opt-in + provider key + 红字 banner 隔离——「默认安全、显式打开」是其 RAG 时代最有价值的设计原则之一。

### 战略意图

三层递进的产品叙事：

1. **agent-readable docs** —— llms.txt、MCP tool schemas、JSON-LD 都按「第一读者是 AI crawler」格式写，让 AI agent 无需 HTML 爬取就能发现/调用能力；
2. **engine surface** —— `/_search` + `/_memory` + `/_graph` + `autoindex` 四个工作流级 endpoint，把 ES 表达不出的「Onboarding / Orientation / Continuity」三难显式落到产品骨架；
3. **adoption bridge** —— ES 8.13 wire compatibility（CI 跑 1366/1369 conformance suite，autogen），让既有 ES 用户/Kibana 直接迁移。

商业化路径已开：Apache-2.0 + funding.json + 公开招 CEO + `POST /v1/systemone` 把「labelled history weighted KNN → 本地 ModernBERT head → flywheel cache」做成 TypeSafe/Jev 兼容的本地化 decide 接口——是为后续 to-agents 产品化铺路。

## 核心价值提炼

### 创新之处

按新颖度 × 实用性排序（本项目垂直评测，非通用排行榜）：

1. **「五件套同二进制」架构（ES 兼容 + autoindex + AST + agent memory + hybrid）** — 任何一个分开看都有先例，但 17 个 Rust crate + 单二进制 + 共享 engine 内部同时实现，是 2026 年最新颖的「AI-native search」产品形态。
2. **zero-config autoindex**（13+ 格式家族 sniffing）——从不信任后缀：magic bytes → binary check → text heuristics 顺序嗅探；失败按 family → txt → junk-with-metadata 三级降级，并记录降级次数便于后续调优。`xerj-autoindex/src/lib.rs` 注释明确「纯 ES-compat HTTP client，不链接 xerj-engine，工作于任何 endpoint，绝不 destabilize server」——这是「agent 自助 onboard」的关键约束。
3. **AST 级代码检索 + per-declaration 独立索引**（36 语言 tree-sitter）——每个 declaration 输出 `{name, kind, line, code}` 放在唯一 `code:<line>:<name>` locator 下，单次命中能精确定位到 40-80 字节的声明行；grammar 失败回退 txt 路径不致命；`.m` 多所有权（Obj-C vs MATLAB）由 content probe 仲裁。issue #500 已 closure，团队选了 symbol 路线。
4. **HNSW + 强制 exact rescoring**（recall@10 = 1.00 vs ES 8.13.4 同协议 0.937）——选候选后用 brute-force 算精确分；flat-slab 重构消除 RwLock 链（5× beam-search 加速）；Aldous–Lyons diversity heuristic 替代 plain closest-M。排序可解释性优先于吞吐。
5. **自研列存 codec 家族**（ZBS2/ZNV2/ZFM5/ZPS2）——字典编码 + bitpack + cross-column mode/exceptions + frame-of-reference + sparse-present sidecar + 5 代 FST metadata 演进 + 训练型 zstd 字典——对标 tantivy 但全部自写，最终数据目录 6.3% 原始 NDJSON 体积。
6. **诚实 benchmark 政策**——4 处败场发在落地页、HNSW 胜场发在 GitHub——「bench 透明度」反而是 GTM 武器。
7. **Cargo.toml 注释即 ADR**——RUSTSEC-2026-0258 / GHSA-2gh3-rmm4-6rq5 / aws-lc-rs cross-compile / prometheus protobuf parser 反复递归等 CV/坑写在依赖版本旁，新人下次 `cargo update` 时自带 review trail。

### 可复用的模式与技巧

- **Cargo workspace 4-profile 制度**：`release`（fat-LTO + codegen-units=1 + panic=abort）/ `quick` / `ci-test`（`panic=unwind` + 不做 fat-LTO）/ `profiling(-final)`——每 profile 在注释里写清「USE IT FOR / NEVER USE IT FOR」；比 README 文本好查。适用于所有发布级二进制 vs CI/dev 迭代分层的 Rust 项目。
- **全局 jemalloc + Linux 专属配置**（`background_thread:true, dirty_decay_ms:1000, muzzy_decay_ms:1000`，macOS 显式屏蔽 background_thread pthread 告警）——解决 glibc malloc 多 arena 长期 ingest 不还页、RSS 单调上涨问题。关键配置通过 `_rjem_malloc_conf` 导出符号（注意是 `_rjem_` 前缀，普通 `MALLOC_CONF` 不生效）。适用于所有长寿命 + 大 allocation churn 的 Rust 服务。
- **Trust Boundary 当 README 开篇红字**——`--insecure` / `127.0.0.1` only / cleartext refuse-on-shared：先讲清楚「这个标志是边界，不是形式」比安全建议段落有用百倍。
- **fail-closed by 静态二进制 SHA-256**（用 ring 同 TLS 栈零新 native dep 做下载验签）——所有「分发单二进制且可审计」的项目适用。
- **parse failure 必须可降级 + 计数**——每个降级单独 `record_junk_skipped`，让 batch ingest 不被单文件 bug 拖死。
- **per-target `target-cpu` baseline**（放弃 `native`，用 `x86-64-v3` 等可分发基线 + 显式注释解释为何不用 native）——所有给异构用户分发二进制的 Rust 项目适用。
- **4 行为 inline code review checklist**——`docs/DECISIONS.md` / `SECRET_HASH` / `CORPUS_HUB_V2` / `CONTRIBUTING` / `SECURITY_MODEL` / `OBJECT_STORAGE` 一档「长文 + line-cited code links」——帮 contributor onboarding 流畅。
- **rerank opt-in + provider-key gated + 「sends text off the node」红 banner**——让 hot 默认安全；外部调用能力必须「显式打开」——RAG 时代所有 AI 增强功能都应该这样。

### 关键设计决策

1. **决策**：4 套 cargo profile + per-profile 注释
   - 问题：`release` CI 76m05s、cargo test 强制 recompile 全部 dep graph
   - 方案：`release`（fat-LTO + codegen-units=1 + panic=abort）/ `quick` / `ci-test`（`panic=unwind` + 不做 fat-LTO）/ `profiling(-final)`
   - Trade-off：profile 多了新人认知负担，但用注释自我证明比 README 好查
   - 可迁移性：高

2. **决策**：双 HTTP 监听同时打 native REST（:8080）+ ES-compat（:9200）+ gRPC h2c（:8081），同 binary 跑三个协议
   - 问题：ES 生态锁定客户的迁移成本 + agent 想要精简 12-endpoint API
   - 方案：`build_native_router` + `build_es_compat_router` 共享 `AppState`；engine 内部零差别，差异只在 wire 翻译层；es-yaml-runner 在 CI 跑 1366/1369 conformance gate
   - Trade-off：维护两套路由 + 字段命名约定（#361 bool 折叠 bug 影响「换 URL 就能用」承诺）
   - 可迁移性：高

3. **决策**：autoindex 完全脱离 engine，只通过 ES wire HTTP 客户端跟 server 对话；parse 失败 family → txt → junk 三级降级 + 单 extractor 限内存流式
   - 问题：agent 自己跑 autoindex 不能污染 server 状态机，不能让一个 OOM 文档让整批 ingest 崩
   - 方案：纯 HTTP 客户端，不链 xerj-engine；可工作于任何 endpoint；catalog split 防 OOM；throttling 节流等 600s
   - Trade-off：HTTP 比 inline 慢，换来副作用可控（autoindex unwrap 3842 最多，正是降级 + retry + wait 路径密集）
   - 可迁移性：高

4. **决策**：HNSW + brute-force rescoring 把 recall@10 锁到 1.00
   - 问题：单纯 HNSW 近似返回的 score 与真实 L2/cosine 不一致，排序不可解释
   - 方案：flat-slab 改造（`Vec<f32>` + slot slab 替代 `HashMap<u64, Arc<RwLock<Node>>>`）+ Aldous–Lyons diversity heuristic
   - Trade-off：全内存 HNSW 限制单机向量规模（通过 HNSW_FORMAT_VERSION = 2 持久化解决重启）
   - 可迁移性：中

5. **决策**：`Cargo.toml` 用注释作 ADR 承载 CV/坑决议（漏洞 ID → 影响路径 → 我们选的解）
   - 问题：rust 供应链漏洞升级决议需要在新成员下次 upgrade 时可见
   - 方案：注释结构 = 漏洞 ID → 影响路径 → 我们选的解（floor 版本 / 关闭 feature / 替换 crate）
   - Trade-off：PR diff 长，但每次 `cargo update` 跑回归 review = 自带审计轨
   - 可迁移性：极高

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | XERJ | Qdrant | Meilisearch | Typesense | Tantivy（库） |
|------|------|--------|-------------|-----------|---------------|
| 语言 | Rust | Rust | Rust | C++/Rust | Rust |
| 全文 + 向量 hybrid | 内置（BM25 + HNSW + exact rescore） | 仅向量，hybrid 需自堆 | 全文 + 向量，量化弱 | 全文 + 向量 | 仅全文/库 |
| ES 兼容（Kibana 直接用） | 1366/1369 wire | 不兼容 | 不兼容 | 不兼容 | 不兼容 |
| AST 代码检索（tree-sitter） | 36 语言，per-declaration | 无 | 无 | 无 | 无 |
| zero-config autoindex | 13+ 格式家族嗅探 | 无 | 无 | 无 | 无 |
| Agent long memory API | `/_memory/{ns}` 原生一等公民 | 无 | 无 | 无 | 无 |
| Knowledge graph API | `/_graph` 原生 | 无 | 无 | 无 | 无 |
| 单二进制无 JVM | ✅（含 TLS、含 MCP stdio） | ✅ | ✅ | ✅ | 仅库 |
| 公开诚实失败清单 | ✅（README 4 处 + re-run playbook） | ❌ | ❌ | ❌ | ❌ |
| 自研 codec family | ZBS2/ZNV2/ZFM5/ZPS2（5 代 FST 演进） | 无 | tantivy 内嵌 | 无 | 标准 |
| 部署门槛 | `curl | sh` 单行（含 Windows PowerShell） | Docker / 集群 | Docker | Docker | Cargo dep |
| 年龄 | 3.5 个月 | 4+ 年 | 5+ 年 | 5+ 年 | 6+ 年 |
| 营销生态成熟度 | 弱（landing/compare 322 次修改，营销矩阵在补） | 强（云服务齐全） | 强（DX 极佳） | 中（Algolia 兼容 API） | 仅库 |

### 差异化护城河

- **五件套整体 = 「超集」而非「加强型矢量 DB」**——单 binary 同时输出 ES wire + 精简 native + gRPC + MCP stdio，4 种接入形态共享同 engine。要复刻这一点至少要打包 Qdrant + tantivy + tree-sitter + ingest pipeline + wire gateway 五条独立栈。
- **HNSW + 强制 exact rescoring** 把 recall@10 钉死在 1.00，这是 Qdrant（默认近似）、Meilisearch（量化近似）等所有 hybrid 替代都未承诺的「排序可解释性」指标。
- **「诚实失败清单」本身就是 GT M 武器**——ES 8.13.4 recall@10 仅 0.937 vs XERJ 1.00 已经把最关键的 benchmark 写在落地页；败场同步发出来反而消解了「benchmark selection bias」的质疑，agent 选型时是首选信任对象。
- **AST 代码检索粒度**（per-declaration 而非 file-level）——grep/ripgrep 给行不给符号；Agent 做「`User.save` 在哪里定义」类问题时，XERJ 直接返回 40-80 字节的声明行，而不是整文件 BM25 命中。
- **llms.txt + JSON-LD + MCP tool schemas agent-first 文档协议**——AI crawler 一抓就能发现能力，比传统 docs site 早一截布道。
- **Apache-2.0 + funding.json + 公招 CEO**——商业化路径已开，「open-core」风险较小。

### 竞争风险

- **ES wire gap 持续威胁「换 URL 就能用」承诺**：#361 bool 折叠 bug 揭示 ES 用户对 _score 行为极敏感；1366/1369 conformance 数字给的安全感掩盖了「评分语义陷阱」。Qdrant / OpenSearch 不会主动修；xerj-org 自己必须持续修补。
- **单人主导 81.5% + 仅 263 followers**：bus factor 高 + 企业采购风险信号弱。重型 ES 替换案仍是大客户博弈，采购方对「匿名组织号 + 单一账号 80% commits」存天然警惕。
- **自研 5 代 codec family 让 correctness 风险集中**：tantivy/lucene 的 bug 修复靠整个开源社区扩散，xerj-org 修一次只能自己发版；HNSW v2 format 显式 break 已经埋下「演进兼容」的隐性债务。
- **rc.96 仍处密集收敛期**：1.0 正式版前任何一个 hot loop 的性能回退都会成为下一轮 marketing 的反噬点。

### 生态定位

在「ES 替代/兼容 + hybrid + AI-native」这条细分赛道内暂无同档对手——Meilisearch/Typesense 走 SaaS 体验，不搅 agent 战场；Qdrant 是「向量优先的 ML 后端」，不沾 ES；OpenSearch 是 ES 延续，不沾 autoindex / AST。在「AI 时代的本地 search 基础设施」叙事下，xerj-org 与 es-yaml-runner（conformance 检验）+ tree-sitter（AST 能力）+ Cerbos（authorisation）+ Cloudflare Vectorize（managed HNSW）等组件互补。**整体定位接近「如果 PostgreSQL/Lucene 是上一代基础设施，XERJ 想做 AI 时代的底层」——独立的赛道占位，真正的对手是「Agent 该选谁做复杂检索」。**

## 套利机会分析

- **信息差**：3.5 个月 7700 stars 已让市场快速定价，「被低估」窗口基本关闭；但 ES 兼容 + 0 配置 autoindex + Agent memory 这套组合的「技术整合样板」仍然领先 Qdrant+tantivy+meilisearch stack 半年到一年——后者更适合作为「参考架构组合」借鉴而非 fork。
- **技术借鉴**：
  - 复刻 per-target `target-cpu` baseline + 4-profile cargo 制度 → 任何要发 release 二进制的 Rust 项目
  - 复刻 autoindex「family → txt → junk」三级降级 + record_junk_skipped → 任何 batch ingestion agent
  - 复刻 trust boundary 红字 + doc/dual-layer 叙述 → 任何 dev-machine default 工具型服务
  - 复刻 Cargo.toml 注释即 ADR（CV/坑写进 dep 版本旁）→ 所有 long-lived Rust 项目
  - 复刻 rerank opt-in + provider-key gated + 红 banner → 所有做 AI 增强的服务
- **生态位**：「Agent-native 本地 search」+「ES replacement layer」双轨——前者是 6-12 个月可见增长的窗口期，后者是 18 个月+ 才会验证的长期赌注。
- **趋势判断**：增长曲线在加速（10 月反弹到 896 commits，1.0 前最后一波功能冻结）；商业化 CEO 在招 = 即将从「工程驱动」切换到「GT M 驱动」；同档未出现竞品 = 12 个月内仍是「投资而非比较」时机。一旦 1.0 正式发版 + cloud 版本上线，竞争格局会快速重塑。

## 风险与不足

- **unwrap/expect 债务偏重**：全仓 13087 个 unwrap + 2974 个 expect，autoindex 占 3842；生产热路径虽靠 `?` 链 + XerjError enum 收口，但裸 unwrap 频次高于 production-grade 项目应有的标准；建议引入 sat-driven lint。
- **#1183 finalize-catalog 死锁 + post-kill resume 「谎报 searchable 实际 500」**——分布式恢复语义风险尚未像 autoindex resilience 一样有同等 harness；cluster failover 路径未经实战压力。
- **#361 bool 折叠**只是 ES 评分语义陷阱之一，1366/1369 conformance 数字暗示的「ES compat 已稳」与实际 edge-case 复杂度之间仍有 gap。
- **ES-Compat YAML runner 在 release rc 阶段报告的「（passing + skipped） 变化」含义对外部读者并不清晰**——docs/STUB.md / stub audit 的数字变化缺乏 changelog 同步。
- **bus factor 81.5%**：第三方接手或企业采购的「作者风险」极高，招募 CEO 不能解决工程连续性问题。
- **商业化叙事「公招 CEO + funding.json」开源侧听起来像 open-core 切 SaaS 路径**：需关注后续是否出现「开源版限制关键 5 件套中某一环」的情况。
- **评测可复现性**：2.7× 输出 token 数据来自 README 公开案例 + 自主选样本，外部完整复现路径长；建议每篇 bench 都附完整 harness JSON。

## 行动建议

- **如果你要用它**：在 greenfield 「agent 自助 onboard 本地文件夹」场景下首选；ES 替换场景下先用「逐步 mirror 流量」做功能对齐验证（ES 评分语义 edge-case 多），2.7× token 优势在「agent 反复扫相似语料」的 workload 下真正显现。重写 RAG ingestion 全栈时它是「整合样板」，比 Qdrant+tantivy+meilisearch 三栈搭建快得多。
- **如果你要学它**：建议精读这些文件/章节——
  - `engine/crates/xerj-engine/src/index.rs`（403 次修改，索引核心热点）
  - `engine/crates/xerj-engine/src/es_compat.rs`（276 次修改，wire 翻译层）
  - `engine/crates/xerj-autoindex/src/lib.rs`（150 次修改，零配置嗅探）
  - `engine/Cargo.toml`（4-profile 制度 + ADR-as-comment）
  - `docs/ZERO_TOKEN_DIRECTION.md`（设计哲学第一手来源）
  - `docs/WHY_XERJ.md`（vs ES/Lucene 六轴独立对照）
  - `engine/crates/xerj-vector/src/hnsw.rs`（flat-slab 改造 + Aldous–Lyons heuristic）
- **如果你要 fork 它**：可以从这几个方向入手——
  - 把 unwrap/expect 治理成 lint 规则（autoindex 子 crate 优先）
  - 给 cluster failover 加 recovery harness（对标 #1183）
  - 补 ES scoring 语义测试 fixture（系统性覆盖 #361 类陷阱）
  - 把 `/_memory` 抽象成可插拔 backend（现在绑定 xerj-engine）
  - 写 distribution/channel 渠道打包（deb / brew / winget）

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | https://deepwiki.com/xerj-org/xerj — 已收录，给出 17 crate workspace + ES 8.13 兼容 + AST 36 语言抽取 + RRF/Linear 融合的完整架构概览 |
| Zread.ai | 未收录（Cloudflare 403） |
| 关联论文 | 无（项目方未发表 arXiv；技术披露以博客《Cutting the index 28%: dissect first, write Rust second》2026-09-27 为主） |
| 在线 Demo | 已上线：https://xerj.org/playground/（公共 Playground）+ https://xerj.org/aise-demo.html（案例演示）+ https://xerj.org/benchmarks（基准页） |
| 官方博客 | https://xerj.org/blog/（含《Cutting the index 28%》《Honest benchmark policy》等） |
| 架构文档 | https://xerj.org/docs/（27 篇设计/操作文档）+ 仓库内 `docs/` 目录（27 篇） |
| 设计哲学 | `docs/WHY_XERJ.md`（vs ES/Lucene 六轴独立对照）+ `docs/ZERO_TOKEN_DIRECTION.md`（设计哲学第一手来源） |

---

*报告生成时间：2026-10-17；分析基于 3.5 个月仓库历史（3302 commits / 124 RC tags / 7700+ stars）+ Phase 1 网络 + Phase 2 元分析 + Phase 3 内容分析三层证据。*
