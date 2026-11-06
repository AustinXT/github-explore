# GitHub推荐：24ms 启动的 Java 模拟器：Floci 接棒 LocalStack

> GitHub: https://github.com/floci-io/floci

## 一句话总结

Floci 是一个用 Java + Quarkus Native 写成的 AWS 本地模拟器，它把启动压到 24ms、空闲内存压到 13MiB、镜像压到 90MB，并用「**真实 AWS SDK 打真实实例、零 mock**」的 8 套契约测试证明兼容性，在 LocalStack 归档并强制注册账号之后，接下了「**永久免费的本地云**」这个位置。

## 值得关注的理由

- **GraalVM Native 与动态 API 形状的化解范式**：AWS API 千变万化，模拟器天然想用反射式 POJO 绑定，而 GraalVM Native 在构建期封闭反射——这是一对天然矛盾。Floci 的解法是入站一律用 Jackson 树模型（`JsonNode`）、出站 1,305 个 model 类显式标注 `@RegisterForReflection`、手写 11 行 `reflect-config.json` 只补 `Map`/`Collection` 的接口方法。任何想在 native image 里跑「形状多变的服务」的项目都能抄这套。
- **兼容层做在配置平面而不是代码平面**：`LocalStackParity` 用 MicroProfile `ConfigSource`（ordinal 299）把 13 个 LocalStack 环境变量翻译成 Floci 变量，显式设置永远优先，一键可关；再加上额外打印一行 LocalStack 风格的 `Ready.` 日志，让 Testcontainers 的 `LocalStackContainer` 默认等待策略直接可用。这是「drop-in 替代品」该有的工程诚意。
- **用真实工具链做兼容性验收**：5 种语言的官方 SDK + AWS CLI + AWS CDK + Terraform + OpenTofu 全部打真实实例、零 mock，已知失败用「只能收缩的 allowlist」管理。这套方法论的价值比任何单个服务实现都高。
- **一个值得盯住的窗口期**：LocalStack 于 2026-03-23 归档，而 Floci 的首个 commit 是 2026-03-15——早 8 天。这个时间差不是巧合。

## 项目展示

![Floci](https://raw.githubusercontent.com/floci-io/floci/main/docs/assets/floci-black.svg) — 项目 Logo（浅色模式）。命名取自 floccus，即形似爆米花的积云，Floci 家族按云拆成四支：floci（AWS/4566）、floci-az（Azure/4577）、floci-gcp（GCP/4588）、floci-oci（OCI/4599）。

![Star History](https://api.star-history.com/chart?repos=floci-io/floci&type=date&legend=top-left) — Star 增长曲线：2026-05 破 1 万、8 月达 27,360、11 月 5 日 30,229，爆发期在 5–8 月，之后进入低速增长期。

![Contributors](https://contrib.rocks/image?repo=floci-io/floci&max=100&columns=20) — 391 位贡献者的头像墙。贡献者结构在 2026-08 发生突变：从 1 人扩到 30 人，这也是当月提交量从 167 跳到 490、9 月再跳到 1,305 的原因。

[Watch it run —— CLI 完整流程演示](https://github.com/user-attachments/assets/b55714dc-ef36-40ae-a734-cd2cadc288a8) — 12 秒视频：`floci start` → `eval $(floci env)` → `aws s3 mb` / `aws dynamodb create-table` → 停止。全流程零配置。

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/floci-io/floci |
| Star / Fork | 30,443 / 3,333（Watcher 92，fork 率约 11%） |
| Docker 累计拉取 | 6,544,223 次（hub.docker.com/r/floci/floci） |
| 代码行数 | 1,748,002 行（Java 93.6%、JSON 2.9%、Python 1.6%、TypeScript 0.5%） |
| 文件数量 | 7,724（主代码 3,115 个 .java，测试侧 3,608 个文件） |
| 项目年龄 | 7.7 个月（GitHub 建仓 2026-02-18，首个 commit 2026-03-15） |
| 总 commit / 贡献者 | 4,917 / 391 人（主作者占 12.7%，Top 10 占 52.7%） |
| 开发阶段 | 密集开发（近 30 天 1,763 commit，9 月 1,305、10 月 1,619） |
| 贡献模式 | 小团队 + 社区驱动（2026-08 起贡献者从 1 人扩到 30 人） |
| 热度定位 | 大众热门（star 增速已从爆发期回落到低速期） |
| 技术栈 | Java 25 + Quarkus 3.40.1（RESTEasy Reactive + Vert.x + Jackson），可编译为 GraalVM Mandrel native binary |
| 最新版本 | v2.4.0（62 个 tag，semantic-release 自动打版） |
| 质量评级 | 代码[A] 文档[A] 测试[A] CI/CD[A] 错误处理[A] |
| 许可证 | MIT（Copyright (c) 2025 Floci and its contributors） |
| 状态 | 未归档、非 fork（`fork:false / parent:null`） |

## 作者视角：为什么存在这个项目

### 创始人/作者背景

主作者是 Hector Ventura（`hectorvent`），德州，2012 年注册 GitHub，2013 年起持续写 Java；2014–2022 年做 Linux 运维讲师，做过 Fonoster VoIP 产品和 Debezium/CDD 演示；2024 年起是 Quarkus 社区的活跃贡献者，自称「**Quarkus Journey 前 1000 名贡献者之一**」，也是多尼加共和国社群（JConf Dominicana 2026 讲师）的核心成员。GitHub bio 只写了「Creator of Floci - Any Cloud. Locally.」。

**他与 LocalStack 没有任何关系。** LocalStack 的创始人是 Thomas Rausch（`thrau`），联合创始人兼 CEO 是 Waldemar Hummer，第三位联合创始人是 Gerta Sheganaku，公司为 LocalStack GmbH。Floci 是从零重写的独立实现——`gh api repos/floci-io/floci` 返回 `fork: false, parent: null`，全仓库 grep 也没有任何 LocalStack 源码版权头。

项目最初的形态是个人仓库 `hectorvent/floci`（`gh api repos/hectorvent/floci` 会 301 重定向到 `floci-io/floci`，字段完全一致，证明是同一仓库改名）。代码包名至今保留 `io.github.hectorvent.floci.*` 的个人时期残留。组织 `floci-io` 于 2026-03-27 创建——**距 LocalStack 归档日仅 4 天**。

### 问题判断

作者看到的是一个**商业模式转折信号**，不是一个 bug。

2025 年 12 月 LocalStack 发布「The Road Ahead for LocalStack」，宣布合并 Community 与 Pro、免费用户需要注册账号。2026-03-23，LocalStack 的 GitHub 仓库被归档为只读；镜像合并为单一版并强制携带 `LOCALSTACK_AUTH_TOKEN` 才能启动，免费层限制为非商业用途，付费起价约 $39/月；2026-04-06 宽限期到期后强制生效。

这里有一个常被说错的细节：**LocalStack 并未把代码改许可为 Elastic License**。`LICENSE.txt` 当前内容仍是 Apache-2.0（Copyright (c) 2017+ LocalStack contributors / 2016 Atlassian Pty Ltd）。闭的是分发渠道与访问控制，不是著作权。所以「Floci 是不是抄袭 LocalStack」这个问题根本不成立——它一行 LocalStack 代码都没用。

Floci 的首个 commit 是 2026-03-15，比归档早 8 天。这说明作者在公告发布时就已经预判了「社区版会被商业化牺牲」这条趋势，并且判断这个窗口会打开。**他赌对了**。

为什么现有方案不够用？moto 是**进程内的 botocore 拦截 mock 库**——它不执行 Lambda、不起服务、不提供「云形状」，它和「本地云」根本不在一个层级；LocalStack Community 停了；ministack / kumo / fakecloud 各有各的短板，但没人做 LocalStack 的**兼容性迁移层**。更深一层的问题是：市面上所有模拟器在「零依赖」和「保真度」之间只能二选一——要么像 moto 那样轻到不真实，要么像 LocalStack 那样重到 CI 里没法用。Floci 的命题是**两者都要**。

### 解法哲学

**① 轻量优先，但只在底层。** Quarkus Native 把 3.3s 的启动压到 24ms（厂商自报），这不是优化出来的，是架构决定的——AOT 编译 + Mandrel 的结果是运行时不再有 JVM 启动和 JIT 预热。代价是放弃 Spring 生态的成熟度（无 Spring DI、无自动装配），以及 native 构建每架构一次约 4 分钟。

**② 真实优先：判据是「客户端是否需要用真实协议跟这个服务说话」。** 这条二元取舍在代码里找到了明确答案：

- **必须真容器**（客户端要建立真实连接）：RDS→PostgreSQL/MySQL、ElastiCache→Redis/Valkey、MSK→Redpanda、MQ→RabbitMQ、Neptune→TinkerPop/Neo4j、EKS→k3s、Flink→真 Flink 集群、Lambda→Docker 容器、Athena→floci-duck 侧车。
- **进程内模拟**（只有管理面 API 被调用）：S3、SQS、SNS、DynamoDB、SSM、IAM、CloudFormation、SecretsManager 等。

每个容器型服务都带一个 `mock` 开关（`FLOCI_SERVICES_RDS_MOCK` 等，共 17 处），`mock: true` 表示「只有 API 元数据，不起容器」。**同一个服务两种模式并存**，用户按保真度需求选——这是比 LocalStack「一个模式打天下」更灵活的设计。

**③ 兼容而非对抗。** 兼容层不是顺手加的边角料，而是一整套刻意设计：`LocalStackParity` 用 MicroProfile `ConfigSource`（ordinal 299，正好卡在环境变量 300 之下、`.env` 295 之上）翻译 13 个 LocalStack 环境变量，显式设置的 Floci 变量永远优先；`EmulatorLifecycle.logReady()` 额外打印一行 LocalStack 风格的 `Ready.`，注释里明写这是给 Testcontainers `LocalStackContainer` 的默认等待策略用的；DNS 后缀 `localhost.localstack.cloud` 和 `localhost.floci.io` 同时注入；`/etc/localstack/init/` 目录照读，同时支持 `/etc/floci/init/`；甚至有独立的 `floci/floci:latest-compat` 镜像预装 Python3 + AWS CLI + boto3 供老 init 脚本使用；连不支持的 `LAMBDA_REMOTE_DOCKER` 都会打印 warn 并指向替代方案。关键洞察是：**兼容层放在配置平面，意味着它对 Docker 镜像 / JVM 启动 / native 二进制三种部署形态一视同仁**（注释明说「The translation happens inside Floci, not in the image's entrypoint」）。

**④ 明确不做什么。** 官方明确承诺 drop-in 只覆盖 **LocalStack Community**，README 全文搜索「pro」「enterprise」零命中，迁移指南也完全未涉及 Pro/Enterprise 功能——多账号/多区域高级隔离、IaC 深度集成、企业 SSO 与审计类能力都不在承诺范围内。这是评估迁移成本时最容易被误读的一点。

**⑤ 不设付费层。** README 明写：「Sponsorship buys gratitude and nothing else: every emulated service is free for everyone, forever, and no sponsor gets features, priority, or roadmap influence.」赞助分 Gold/Silver/Community 三档，只买曝光（logo 位置、release notes 提及），不买功能、不买优先级、不买路线图影响力，已有 IceGuard、Softmax、AutoScout24 等赞助方。这是一条**信任护城河**：LocalStack 刚刚因为「合并 Community/Pro」背刺了社区，一个明确承诺「永远免费、赞助只买曝光」的替代品，本身就是最强的差异化。

### 战略意图

组织动作本身就是路线图。Floci 家族已扩成四云矩阵 + 周边：floci-az（871★）、floci-gcp（509★）、floci-oci（127★）、floci-ui（489★，TypeScript，Docker sidecar 形态的 Web 控制台）、floci-cli（160★）、floci-duck（14★，Rust 写的 DuckDB 侧车，跑 Athena/Firehose）。

这些周边共享同一套 core 抽象——`ResolvedServiceCatalog`、`StorageBackend`、`AwsJson11Controller`、`AwsQueryController`、`EmulatorConfig`——说明内核确实抽到了「云无关的控制平面 + 协议适配」这一层。但**第二个云是否真的能用同一套 core 跑起来，目前还没有被证明**。`docs/ui/console-contract.md` 是这个抽象的明证：console contract v1 是 AWS 专用，v2 加上 `FLOCI_INFO_URL` + `GET /_floci/info` manifest，注释写着「extends this page for every Floci emulator without changing anything below」。

商业化路径目前**不存在明确的公司主体**——组织公开成员仅 2 人，商业模式是 GitHub Sponsors + 品牌曝光。对一个承诺「永远免费」的项目来说，这是最需要持续观察的风险点。

## 核心价值提炼

### 创新之处

1. **用「树模型 + 显式 @RegisterForReflection」化解 GraalVM Native 与动态 API 形状的天然冲突**
    - 描述：入站 handler 签名统一为 `handle(String action, JsonNode request, ...)`，不做反射式 POJO 绑定；1,363 个 model 类中 1,305 个标注 `@RegisterForReflection`（覆盖 96%）；手写的 `reflect-config.json` 只有 11 条，全是 `Map`/`Map$Entry`/`Collection` 的接口方法——因为 Jackson 序列化 `Map<String,V>` 要反射调用 `Map.entrySet()`，而接口方法在 native image 里默认不被保留。
    - 新颖度 4/5 | 实用性 5/5 | 可迁移性 5/5
    - 适用场景：任何用 GraalVM Native 跑「API 形状多变」的服务。最关键的洞察不是某个技巧，而是**「动态分发 ≠ 反射」**：Floci 需要按 `X-Amz-Target` 分发到 65 个 handler、按 `Action` 分发到几十个 Query 服务，但这些分发**全是字符串 switch，不是 `Class.forName`**——把「动态」的实现层面选成 switch，AOT 冲突就消失了一大半。

2. **实现真正的 AWS Lambda Runtime API 服务器，让未修改的官方 Lambda 镜像直接跑**
    - 描述：`services/lambda/runtime/RuntimeApiServer.java` 实现了 `2018-06-01` 的 `/runtime/invocation/next`、`/response`、`/error`、`/init/error`，外加 `2020-01-01` 的 Extensions API。容器里的语言 runtime 通过 `AWS_LAMBDA_RUNTIME_API` 环境变量连回来。`provided` runtime 甚至保留镜像原 entrypoint，转发到 `/var/task/bootstrap`。这不是「模拟 Lambda」，是「真的跑 Lambda，只是把 AWS 换成 Floci」。
    - 新颖度 3/5 | 实用性 5/5 | 可迁移性 3/5
    - 适用场景：任何需要真的执行用户代码的模拟器。并发设计尤其值得学：**单锁块内只做决定，实际的 `ctx.response().end()` 与 `vertx.runOnContext()` 一律在释放锁之后**；长轮询全程 event-loop 非阻塞，因为语言 runtime 的 bootstrap 进程会在整个空闲期持有一个长轮询，阻塞式地占住 Quarkus 默认的 20 个工作线程会在几个热容器内就耗尽。

3. **嵌入式 DNS + AWS endpoint 欺骗，把「通配 DNS」这个在容器网络里无解的问题解了**
    - 描述：自己实现 UDP/53 服务器，作为所有它启动的容器的 DNS resolver；解析 `*.floci` 与（可选）**所有 AWS partition 后缀**到自身 IP，实现「transparent endpoint injection」，让显式写了真实 AWS endpoint 的客户端也落到模拟器上；提供 `DnsRecordSource` / `DnsForwardingRuleSource` 两个 SPI 让 Cloud Map 和 Route 53 Resolver 接入。
    - 新颖度 4/5 | 实用性 5/5 | 可迁移性 4/5
    - 适用场景：多容器模拟器、Service Mesh 测试、需要 DNS 层透明的开发环境。工程细节里有真实的坑：`MAX_DNS_UDP_RESPONSE = 4096`，因为 EDNS0-capable resolver 宣告远大于 512 的 UDP payload，用 512 字节缓冲接收会**静默截断并损坏转发应答**；`FORWARD_TIMEOUT_MS = 1500` 保证逐个试上游也不会超过客户端典型的 5s 超时。

4. **把「静默 bug」变成 CI 可见的计数，且基线只能单向收缩**
    - 描述：Floci 服务全部 8 个 AWS partition，代码里任何硬编码 `arn:aws:` 或 `amazonaws.com` 在 GovCloud/中国区都是**静默 bug**——因为在 us-east-1 里它打印得完全正确。`tools/partition/partition_literals.py` 按 6 类模式（arn-literal / amazonaws-host / hosted-zone-id / 手写正则 / arn-concat / arn-probe / arn-split）逐文件计数，与 checked-in 的 `baseline.tsv` 比对：新增失败、增长失败，**计数下降也失败**——直到重新生成基线，这样「还剩 N 处」的数字保持精确且下降在 PR diff 里可见。豁免必须写理由（allowlist.yaml 或行尾注释），审计时会打印出来复查。当前基线已清空。
    - 新颖度 4/5 | 实用性 4/5 | 可迁移性 5/5
    - 适用场景：任何「多环境/多区域变体」的代码库——硬编码默认值在主流环境下打印正确、在边缘环境下静默出错。

5. **兼容层做在「配置平面」而不是「代码平面」**
    - 描述：见前文解法哲学 ③。核心是用 `ConfigSource.getOrdinal()` 在正确的优先级层注入翻译后的配置，一键可关，且对三种部署形态一视同仁。
    - 新颖度 3/5 | 实用性 5/5 | 可迁移性 5/5
    - 适用场景：任何要做 drop-in 替代的项目。

6. **契约测试 + 「只能收缩」的已知失败 allowlist**
    - 描述：8 套真实工具链测试全部打真实实例、零 mock；已知失败用 allowlist 管理，且 **allowlist 里有一条不再匹配任何失败测试时也会失败**——「the gap is closed: delete the line, so the list only ever shrinks」。
    - 新颖度 3/5 | 实用性 5/5 | 可迁移性 5/5
    - 适用场景：任何「我模拟的东西必须骗过真实客户端」的场景。

7. **`PartitionedFileStorage`：按 key hash 分片的文件存储**
    - 描述：`floorMod(entryKey.hashCode(), shards)` 决定分片，**改一个 entry 只重写它所在的那一个分片文件**，解决「一个大表 + 一个小热表，每次热表变更都要重写大表」的问题；shard count 变更时自动合并重写。
    - 新颖度 3/5 | 实用性 4/5 | 可迁移性 4/5
    - 适用场景：任何「一个 store 里混着大对象和小热对象」的本地持久化场景。

8. **`AccountAwareStorageBackend` 的「回退 + 读时迁移」与「按需付费的 owner 追踪」**
    - 描述：装饰器给所有 key 透明加账户前缀（`111111111111/orders`）；get 未命中时回退到无前缀 key 并在读时迁移，覆盖多账号支持之前创建的存量数据；跨账号查找用 `ownerAccounts` 集合缓存，且**只在第一次跨账号查找之后才开始追踪**，其他 store 每次写只多付一次 volatile read。
    - 新颖度 3/5 | 实用性 4/5 | 可迁移性 4/5
    - 适用场景：任何「给已有系统加租户隔离且不能破坏存量数据」的改造。

### 可复用的模式与技巧

1. **ConfigSource ordinal 做兼容层** — 用 `ConfigSource.getOrdinal()` 在正确的优先级层注入翻译后的配置。适用场景：配置兼容层、环境变量翻译、多环境适配
2. **树模型代替反射绑定以兼容 AOT** — 入参一律 `JsonNode`，出参模型全部 `@RegisterForReflection`。适用场景：GraalVM Native、动态 API、序列化
3. **静默 bug 的「只能收缩基线」** — 按文件计数 + checked-in baseline + 计数下降也失败 + 豁免必须带理由。适用场景：静态检查、多环境代码库、技术债治理
4. **契约 allowlist 且只许收缩** — 已知失败列表里不再失败的条目也导致 CI 失败。适用场景：遗留缺陷管理、CI 门禁、渐进式修复
5. **上游模型驱动的数据生成** — 从官方 botocore 的 `data/` 生成 IAM 动作表、分区表、endpoint 形状、CFN schema，生成器 pin 与生成数据一起提交，CI 用 `aws-data-check` 校验漂移。适用场景：API 追平、大量常量表、数据同步
6. **注释即决策记录** — 代码里写清「为什么这样做」和「我们在哪里故意简化了」。适用场景：AI agent 协作、长期维护、架构决策留存
7. **嵌入式 DNS + endpoint 欺骗** — 自起 UDP/53 做容器内解析器 + SPI 让有 zone 的服务接入。适用场景：多容器模拟器、Service Mesh、DNS 透明测试
8. **协议分发的「识别层」与「格式层」分离** — 线格式交给 JAX-RS/Jackson，识别层（SigV4 credential scope → service、`X-Amz-Target` → handler）自己写。适用场景：多协议网关、RPC 模拟、路由设计
9. **锁内只做决定、锁外做副作用** — 单锁块内决定动作并收集结果，实际 I/O 一律在释放锁后。适用场景：高并发、event loop、细粒度锁
10. **文件系统分片存储** — key hash 分片 + 改一个只重写一个文件 + shard count 变更自动合并。适用场景：本地持久化、大小对象混合的 store
11. **装饰器实现租户隔离 + 读时迁移** — 透明加前缀 + 未命中回退旧 key + 按需付费的 owner 追踪。适用场景：多租户、存量数据兼容
12. **Sidecar 契约先行 + major 版本门禁** — 通用契约（不含领域词汇）+ contract-major 不匹配就 fail fast + 发布顺序强制（sidecar 先发版，Floci PR 再 pin 那个 tag）。适用场景：多语言 sidecar、插件架构、微内核
13. **生成文档而非手写文档** — `docs/services/*.md` 的 Supported Actions 表从 handler 源码的 `case "X" ->` 分支自动生成，手改会 `docs-check` 失败。适用场景：文档同步、API 参考自动生成
14. **PR 数量上限 + bot 强制执行** — 最多 4 个 open PR / 2 个 ready，bot 自动把第 3 个 ready 转回 draft、关掉第 5 个。适用场景：社区项目维护带宽、评审质量

### 关键设计决策

**决策 1：入站一律用 Jackson 树模型，不做反射式 POJO 绑定**

- 问题：GraalVM Native 在构建期封闭反射，而 AWS 的 request shape 每个操作都不一样，通用解析天然就想用反射绑定。
- 方案：所有 `*JsonHandler` 签名统一为 `handle(String action, JsonNode request, String region, String authorization)`，字段用 `request.path("Name").asText()` 取。AGENTS.md 把它写成硬规则：「Types returned directly from controllers must remain compatible with native-image reflection requirements」。
- Trade-off：失去了编译期类型检查与 IDE 补全，换来 native image 里零反射依赖。而且这其实不是将就——JSON 1.1 的 action 本来就是 `X-Amz-Target` 前缀 + 操作名的动态字符串，本来就必须动态分发，树模型恰好同时满足了两件事。
- 可迁移性：高。

**决策 2：出站模型显式登记，手写 reflect-config 只补最小集**

- 问题：1,363 个 model 类全是 Jackson 序列化目标，native image 默认不保留字段元数据。
- 方案：1,305 个类标注 `@RegisterForReflection`；`reflect-config.json` 只有 11 条，全是 `Map`/`Map$Entry`/`Collection` 的接口方法——因为 Jackson 序列化 `Map<String,V>` 要反射调用 `Map.entrySet()`，而接口方法在 native image 里默认不被保留。
- Trade-off：**这是 native 路线唯一真正昂贵的地方**——漏标一个注解，在 JVM 模式下 3,545 个测试全绿，只在 native 运行时才炸；等于把「编译期能发现的类型错误」推迟到了「构建 native 镜像时」。而且这 11 行是可以省掉的：如果字段用 `LinkedHashMap` 具体类型声明而非 `Map` 接口，可能一个注解都不用。**AOT 友好不只是加注解，还是选对静态类型。**
- 可迁移性：高。

**决策 3：资源清单与初始化时机全部手工登记，且按构建目标动态插值**

- 问题：模型目录、IAM 策略目录、价格快照、`*.yaml` 目录都是运行时拼路径读的，Quarkus 的静态资源分析看不到；持有 `SecureRandom` 的服务若在构建期初始化，镜像里的随机序列就是固定的。
- 方案：18 条 `native.resources.includes` 手工列举；`--initialize-at-run-time` 登记 30+ 个类（覆盖 `SecureRandom` 持有者、JNA、docker-java 的 Windows named pipe、snappy、PostgreSQL 的 `PasswordUtil`）；include/exclude 用构建期属性插值做 per-platform 裁剪（`${floci.native.windows-jni-include:none}` 控制 Windows JNA，snappy-java 的 27 个平台 JNI 库逐个排除，只留运行平台那个）。IAM managed-policy 目录 3.5MB **故意不 include**——构建期已解析进镜像堆，再存一份是重复；但 13KB 的 service-linked-role 表**选择 include**——「13 KB 那个体量不值得赌静态初始化器在构建期跑」。**按数据体积和初始化成本分别决策，这是很细的工程判断。**
- Trade-off：任何新增的动态资源路径都要手动加，否则 native 里读不到文件，且同样只在 native 出现。
- 可迁移性：高。

**决策 4：超大 dispatcher 主动放弃 AOT 单调用点内联**

- 问题：CI 里记录了一个真实事故——Quarkus 3.39 在 Mandrel 25.0.4+ 上默认开启 `-H:+AOTSingleCallsiteInline`；`AwsQueryController.dispatch` 与 `AwsJson11Controller.handle` 各自是超大方法的唯一调用点，内联后方法超出 aarch64 条件分支范围，构建直接以 `BranchTargetOutOfBoundsException` 失败。
- 方案：在 CI 的 native 构建里加 `-Ob,-H:-AOTSingleCallsiteInline` 关掉这个优化。因为这个 flag 只存在于 Mandrel，所以放在 CI 而非 `application.yml`。
- Trade-off：native 代码略微膨胀/变慢，换来能编过。根因是「一个服务一个巨型 switch」的 dispatcher 模式——这是可迁移性最需要打折的一个决策。
- 可迁移性：中。

**决策 5：四种 StorageBackend 用同一接口抽象四种持久化语义，且不支持的实现显式拒绝**

- 问题：不同服务对持久化的需求差异巨大——CI 要快、开发时要能重启恢复、CloudWatch Logs 这种高频写入不能每次全量重写。
- 方案：接口 `StorageBackend<K,V>` 下有 `memory`（纯内存）、`persistent`（JSON 文件原子重写）、`hybrid`（内存读 + 异步周期 flush）、`wal`（追加式二进制 WAL + 周期 compaction，自研格式：`PUT=[0x01][keyLen][key][valLen][value]`、`DELETE=[0x02]`、`BATCH=[0x03][mapLen][CBOR map]`）；额外第五种 `PartitionedFileStorage` 按 key hash 分片。`putAllAtomically` / `deleteAllAtomically` 是**默认抛 UnsupportedOperationException 的 opt-in**——不实现原子批的后端明确拒绝，而不是静默降级。
- Trade-off：四种实现 = 四倍测试面。`persistent` 的「每次变更全量重写」在 store 变大后是 O(n)，这正是分片存储和 WAL 存在的原因。**诚实的缺口**：`hybrid` 模式下文档明写「an unflushed batch can still be lost on restart」，只有 persistent/wal 会把写失败报给调用方。
- 可迁移性：高。

**决策 6：协议分发用大 switch，自研的是「路由器」不是「解析器」**

- 问题：AWS 有 6 套 RPC 协议（Query/XML、JSON 1.1、JSON 1.0、REST JSON、REST XML、CBOR），还有 TCP 数据面（ElastiCache/RDS 的原生协议）。
- 方案：线格式本身交给 JAX-RS/Jackson，Floci 只做「哪个 handler」的识别——`AwsQueryController` 从 SigV4 credential scope 推断服务（无 Authorization header 时退化到用 `Action` + `Version` 推断），`AwsJson11Controller` 按 `X-Amz-Target` 前缀分发到 65 个 handler，REST JSON/XML 走 JAX-RS 注解；XML 用自研 `XmlBuilder`（输出）+ `XmlParser`（输入），AGENTS.md 规定「不要用正则解析 XML」。
- Trade-off：大幅降低了实现风险，但 `dispatch` 变成巨型 switch，直接导致了决策 4 的 native 编译事故。
- 可迁移性：高。

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | Floci | LocalStack | MiniStack | moto | fakecloud |
|------|-------|-----------|-----------|------|-----------|
| 语言 / 运行时 | Java 25 + Quarkus Native | Python | Python | Python（进程内） | Rust 单二进制 |
| 启动时延 | ~24ms（自报） | ~3.3s（自报） | <2s | 进程内 | 极快 |
| 空闲内存 | ~13MiB（自报） | ~143MiB（自报） | — | — | 低 |
| 镜像体积 | ~90MB（自报） | ~1.0GB | ~270MB | 无（库） | 无（单文件） |
| 可执行文件 | ~40MB native binary | 需 Python 环境 | 需 Python 环境 | 需 Python 环境 | 单文件 |
| 协议保真度 | 8 套契约测试（真实 SDK） | 十年沉淀最深 | 未见同类体系 | 不起服务 | 宣称 Smithy 100% 一致 |
| 真实容器支持 | RDS/ElastiCache/MSK/MQ/Neptune/EKS/Flink/Lambda/ECS/EC2/CodeBuild | 部分 | 部分 | 无 | Lambda 23 runtime |
| AWS partition | 8 个全覆盖，零硬编码（CI gate 保证） | 支持 | 部分 | 部分 | 部分 |
| License | MIT | Apache-2.0（闭分发非闭许可证） | MIT | Apache-2.0 | AGPL-3.0 |
| 商业化 | 无付费层，赞助只买曝光 | 强制账号，免费层限非商业，$39/月起 | — | — | — |
| Star / 维护状态 | 30,443 / 活跃 | 65,126 / **2026-03-23 已归档只读** | 5,106 / 活跃 | 8,735 / 活跃 | 781 / 活跃 |

> 上表中 Floci 的性能数字均为厂商自报，第三方评测明确指出这些数字未经独立验证；LocalStack 与 ministack 的数字同源，跨项目比较时应谨慎。

### 差异化护城河

1. **技术护城河（中等偏强）**：GraalVM Native AOT 的完整工程化——1,305 个 `@RegisterForReflection`、11 行手写 reflect-config、18 条 native resources include、30+ 条 `--initialize-at-run-time`、per-arch 构建与 snappy JNI 平台裁剪、CI 里解析 GraalVM 的 `*-build-output-stats.json` 把 binary 体积变成 PR 可见指标；自研嵌入式 DNS；自研二进制 WAL（CBOR value + 4 种 op code）；自研 Lambda Runtime API 服务器；自研分片文件存储。这些都不是一两周能复刻的。
2. **生态护城河（强）**：6,544,223 次 Docker pulls（**约为 star 数的 2 倍**，是「真的在跑」而非「只是收藏」的强信号）+ 391 位贡献者 + 8 个语言/工具链的契约测试。第三方生态（Testcontainers、aws-sdk、boto3、CDK、Terraform provider）测试驱动的是「真实客户端能过」这个不变式，任何竞品都要重走一遍这 8 套契约。
3. **信任护城河（强，且最被低估）**：「不设付费层、不设配额、不阉割免费版」的明文承诺。在 LocalStack 刚刚因为合并 Community/Pro 背刺社区的当口，一个明确承诺「永远免费、赞助只买曝光不买功能」的替代品，本身就是最强的差异化。加上 MIT 协议、公开的 MAINTAINERS.md、25KB 的 AGENTS.md 与 CONTRIBUTING.md 带来的治理透明度。
4. **迁移成本护城河（强）**：parity 层做到「改镜像名就能跑」——端口、凭据、SDK 配置、init 脚本目录、Testcontainers 等待策略全部不变。这个成本优势竞品要花几个月追。

### 竞争风险

- **最可能的替代者**：`ministackorg/ministack`——同样 MIT、同样 drop-in、同样走真容器路线，是定位最接近的竞争者。但体量差 6 倍，且没有 native 路线。
- **另一条路线的威胁**：`faiscadev/fakecloud` 的 Rust 单二进制 + Smithy 一致性路线，冷启动与内存理论上更优；若它补上真容器和契约测试，会在「轻量 + 正确」这个维度构成正面威胁。但 AGPL-3.0 对闭源商业集成有传染性风险。
- **上游反转**：如果 LocalStack 复活并保持免费，Floci 的窗口期会收窄。考虑到它背后是 LocalStack GmbH 且底层代码仍是 Apache-2.0，这个可能性不能排除——Floci 吃的正是它的空窗红利。
- **AWS 官方替代品**：AWS SAM CLI 本地模式、SDK 的 mock transport 若成熟，会侵蚀单测场景（但不是集成测试场景）。
- **最脆弱的内在张力**：**「轻量」与「真容器保真度」这两个卖点互相拉扯**。容器化服务的可靠性是当前第一故障源（[#882 Lambda 容器连不上](https://github.com/floci-io/floci/issues/882)，17 条评论，挂 `waiting-contributor`）；同时 CI 吞吐被自己的验证体系卡住（[#3963](https://github.com/floci-io/floci/issues/3963)，1,925~2,506 个兼容测试 + 真容器集成测试把 CI 推到 15 分钟分片上限）。**不是开发停滞，是测试吞吐量成了瓶颈。**

### 生态定位

LocalStack 归档事件后，AWS 开发者「本地云」这条赛道的事实标准承接者。它不是「更好的 LocalStack」，而是**LocalStack 社区版的继任者**——把「社区版」这个产品形态重新定义为「永久免费的完整版」。在整个云模拟生态里，它站在「轻量 + 高保真 + 零迁移成本」这个交叉点上：向上够得着 LocalStack Pro 的功能面（真容器类服务恰好是 Pro 层高价值能力的子集），向下压得过 moto 的能力面。往上一层，它试图把内核抽象成「云无关的控制平面 + 协议适配」，四云矩阵是这个野心最早的证据，但目前只有 AWS 一支被证明。

## 套利机会分析

- **信息差**：Floci 的 star 数已经充分反映甚至超前反映了它的技术含量（30K star vs 8 个月），**它不是被低估的潜力股**。真正的信息差在两处：一是「LocalStack 归档」这件事在中文技术圈还没有被充分讨论（很多团队还在用 3.3s 启动、强制 token 的旧镜像）；二是「GraalVM Native 跑动态 API 形状」这套工程化方法几乎没有中文资料，而它是本项目最硬的技术资产。
- **技术借鉴**：可直接迁移的三件事——(a) AOT 项目的「反射登记表 + 手工 reflect-config + 资源 include 清单 + initialize-at-run-time 清单」四件套；(b) 「用真实客户端做契约测试 + 只能收缩的 allowlist」的缺陷管理；(c) 「分区字面量只能收缩基线」把静默 bug 变成 CI 可见计数的做法。这三条与 AWS 无关，任何多环境/多区域/多租户的服务都适用。
- **生态位**：填补的是「**要跑 CDK/Terraform 的集成测试，但要不起一个 3.3s、1GB 镜像的模拟器**」这个空档。moto 太轻（不执行 Lambda、不起服务），LocalStack 太重，Floci 卡在中间且刻意往「轻」那一侧压。
- **趋势判断**：短期 star 增速已从爆发期回落（8 月 27,360 → 11 月 30,443，近 4 个月只增约 3.1k），增量主要来自新用户而非 LocalStack 存量迁移，**不应按「迁移收割完就结束」来推断**——6.5M pulls 与持续 1,600+/月的提交量说明留存是真的。真正的观察指标是 2026 Q4 的三项：star 增速是否止跌、贡献者是否继续从 30 人扩张、IAM 强制执行等默认值是否被收紧。

## 风险与不足

1. **默认配置下 IAM 强制执行是关闭的，S3 的 `enforce-auth` 默认也是 `false`**（`application.yml:425`）。这意味着**大量「权限拒绝」类测试在默认配置下会假通过**——这是本项目最需要警惕的默认值，也是评测者指出的最尖锐问题。代码里 IAM 求值逻辑本身做得不错（不认识的凭据是被拒绝而不是放行），但默认不开启等于大部分用户不会用到它。
2. **部分服务是 stub 或 inert**：Textract 是 stub、Transcribe 不做真实音频处理、Bedrock Runtime 返回 dummy、FIS 不注入故障、Application Auto Scaling 策略 inert、DLM 无实现。设计文档里明确列了 out-of-scope，属于**有意的范围声明**，但使用者极易把「支持」误读为「可用」。
3. **官方口径自相矛盾**：canonical matrix 列 85 个服务、营销页称 100 个、迁移指南仍写 58 个。第三方评测直接点名这一点。在一个以「文档与代码自动同步」为卖点的项目里，这个不一致格外刺眼。
4. **容器化服务的可靠性是第一故障源**：#882 挂了 `waiting-contributor` 而非立即修复，说明**外部贡献者在补核心维护者留下的坑**——技术债正在被社区稀释，但也意味着核心链路仍由极少数人掌握。
5. **CI 吞吐瓶颈**：#3963 仍然 open。真容器集成测试的耗时由 Docker daemon 的镜像拉取与容器启动决定，压不动。已做的缓解（5 分片 + 完整性门禁、按分片后台预取镜像、只在一个分片 save Maven cache、`compat-timing-report.py` 输出最慢 25 个测试、BATS 文件级并行与超时）都是调度层的，根因未解。
6. **巴士系数偏低**：git 上 410 个作者，但 MAINTAINERS.md 只列 2 人（hectorvent 为 Lead + Priamo Germosen 负责服务模拟），Top1 贡献者占 12.7%。核心架构决策仍由 1 人主导。
7. **商业可持续性不明**：一个承诺「永远免费、不设付费层」的项目，没有明确的公司主体，商业模式是 GitHub Sponsors + 品牌曝光。这本身可能是刻意的价值主张，但也意味着没有收入缓冲去支撑真容器这类高维护成本的服务。
8. **性能数字未经独立验证**：24ms / 13MiB / 90MB 全部是厂商自报，第三方评测明确建议「视为未经独立验证」。同时「零依赖」宣传与部分服务实际依赖 Docker 编排自相矛盾。
9. **安全面**：挂载 Docker socket 在共享 CI runner 上带来 host-level authority 风险——这是「真容器路线」的固有代价，独立评测建议企业先做 PoC 而不是直接切换。
10. **drop-in 的边界只在 Community**：官方迁移指南完全未涉及 Pro/Enterprise，多账号/多区域高级隔离、部分 IaC 深度集成、企业 SSO 与审计能力都不在承诺范围内。**「drop-in replacement」这句话只在 Community 语境下成立**，这是评估迁移成本时最容易被误读的一点。

## 行动建议

- **如果你要用它**：如果你在 CI 里跑 CDK 或 Terraform 的集成测试、且被 LocalStack 的启动时间或强制 token 卡住，Floci 是当前最值得试的替代——换镜像名即可，parity 层会兜住环境变量差异。但迁移前请务必实测三个已知翻车场景：custom-resource Lambda 访问 S3（[#1532](https://github.com/floci-io/floci/issues/1532)，会导致 CDK 的 autoDeleteObjects bucket 失败）、Lambda 容器可达性（[#882](https://github.com/floci-io/floci/issues/882)）、RDS cluster 的返回结构（[#6778](https://github.com/floci-io/floci/issues/6778)，`HostedZoneId=None` 会直接打断 IaC 工具）。如果你只写 Python 单元测试、不需要真服务，moto 仍然更合适——两者是分层关系，不是替代关系。如果你的流水线依赖 `LAMBDA_REMOTE_DOCKER`，Floci 明确不支持，需要改造成 per-function `S3Bucket=hot-reload`。**首次接入务必显式开启 IAM 强制执行**，否则你测的权限拒绝是假的。
- **如果你要学它**：按价值排序读四处——(1) `src/main/java/io/github/hectorvent/floci/config/LocalStackParity.java` 与 `LocalStackParityConfigSource`，看兼容层怎么用 ConfigSource ordinal 做优先级控制；(2) `src/main/resources/META-INF/native-image/io.github.hectorvent/floci/reflect-config.json`（只有 11 行）+ `src/main/resources/application.yml` 里的 `quarkus.native.resources` 与 `--initialize-at-run-time` 段，这是 AOT 工程化的完整清单；(3) `src/main/java/io/github/hectorvent/floci/services/lambda/runtime/RuntimeApiServer.java`，看真正的 Runtime API 服务器怎么实现、怎么用「锁内只决定、锁外做副作用」避开 event loop 阻塞；(4) `compatibility-tests/README.md` 与 `lib/run-bats-with-junit.sh`，看契约测试怎么组织。再加两处工具链：`tools/partition/partition_literals.py`（只能收缩的基线机制）和 `tools/aws/`（从 botocore 生成常量表的 30+ 个 Python 生成器及其 `test_regen_*.py` 配对测试）。最后读一遍 `AGENTS.md`——它把架构意图、硬规则和新增服务的 checklist 全写在里面了，包括那句「Types returned directly from controllers must remain compatible with native-image reflection requirements」。
- **如果你要 fork 它**：值得下手的方向有三个。(a) **补 IAM 强制执行的默认值**——把默认关闭改成默认开启，或至少在首次启动时明确提示，这能立刻消掉整个生态里最大的假阳性来源。(b) **补 CI 吞吐**——#3963 是公开的痛点，真容器测试的耗时瓶颈需要更聪明的分片或镜像预热策略，这是社区最缺人做的贡献。(c) **把契约测试矩阵扩到 Pulumi 和 .NET SDK**——现有 8 套覆盖了 5 种语言的 SDK 与 3 种 IaC 工具，缺 Pulumi 这类 IaC 工具的端到端覆盖，而这正是最容易暴露「返回结构少一个字段」的地方。技术上的门槛很低：MIT 协议、Java 生态、Maven 构建，AGENTS.md 把规则写得极其清楚。

### 知识入口

| 资源 | 链接 |
|------|------|
| 官方文档站 | https://floci.io/floci/ （迁移指南在 `/floci/getting-started/migrate-from-localstack/`） |
| DeepWiki | https://deepwiki.com/floci-io/floci （已收录，含 core architecture、compute services、CI/CD 流程等分卷） |
| Zread.ai | https://zread.ai/floci-io/floci （已收录，含 S3 存储引擎解析、支持服务清单、SDK 集成指南） |
| 关联论文 | 无（该项目无学术论文传统） |
| 在线 Demo | 无官方托管 Demo；README 内嵌 [12 秒 CLI 演示视频](https://github.com/user-attachments/assets/b55714dc-ef36-40ae-a734-cd2cadc288a8)，本地 `docker compose up` 即时体验 |
| 作者架构博客 | 《Standing on Shoulders: The Stack That Makes Floci Start in 24ms》《Why Floci Is Built in Java (and Why That's the Right Call in 2026)》《The Floci Philosophy: Stay Tiny, Feel Like Real AWS》《Floci Storage Modes: Pick the Right Trade-off Per Service》 |
| 姊妹项目 | floci-az（Azure）、floci-gcp（GCP）、floci-oci（OCI）、floci-ui（Web 控制台）、floci-cli、floci-duck（DuckDB 侧车） |
