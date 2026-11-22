# GitHub 推荐：15K star、93% 一个人写的下载器：真资产是 32 篇 ADR

> GitHub: https://github.com/XiaoYouChR/Ghost-Downloader-3

## 一句话总结

一个武汉独立开发者用 Python + PySide6 写了 39 个月的「下载器集大成者」，把 **7 种协议、4 个站点特化、浏览器深度接管、14 个插件包和 Windows/macOS/Linux/Android 四端原生**塞进一个应用；15K star 之外，**真正稀缺且可被任何人抄走的东西，是它那 32 篇 ADR 和一份把「代码品味」写成宪法的 `CLAUDE.md`**。

## 值得关注的理由

1. **一份中文开源界少见的「工程方法论开源」样本**：32 篇 ADR 统一采用「决策 / 被否决的选项 + 为什么 / 代价 / 落在哪些接口」四段式，把「为什么这样设计」变成可检索、可 code review、可交接给 AI 的资产；配套 `CLAUDE.md`（项目宪法，含 30+ 动词表规范副作用语义）、19KB `GLOSSARY.md` 术语表、`GROK.md`（AI 设计评审协议）。这套东西与下载器功能无关，可以直接迁到任何长期维护的项目。
2. **「多协议全栈 + 浏览器深度集成 + 站点特化 + 插件化 + 四端原生」这组能力，目前只有它同时满足**：官方对比表 10 项能力中它在 5 项拿到唯一或并列第一，其中「浏览器深度集成」是唯一的 ✅（IDM/NDM/Gopeed/FDM 全是 ⚠️，Motrix 是 ❌）。在通用下载器已是红海（Motrix 58.7K / Gopeed 27.9K / AB DM 19.5K）的背景下，这是一块被验证过的细分蓝海。
3. **一次濒死重启后的架构跃迁样本**：2025-08 至 2026-02 项目近乎停摆（半年仅 7 次提交），2026-03 单月暴增 248 次提交完成浏览器扩展侧从零建设，此后连续 5 个月维持 150+ 高位——近 365 天 1,377 次提交占了全历史 77%。一个 39 个月大的项目「越老越快」，在开源里相当罕见。
4. **反面教材同样值钱**：93.7% 的提交来自一个人（巴士因子 1）、所谓「智慧/AI 加速」实为没有闭环反馈的启发式规则、默认不校验 TLS 证书、百度网盘官方客户端身份模拟的合规边界未在文档中说明。作者用公开 benchmark 保留自己的败绩，是少见的诚信样本。

## 项目展示

![Ghost Downloader 3 项目 Banner](https://raw.githubusercontent.com/XiaoYouChR/Ghost-Downloader-3/main/.github/assets/banner.webp)

> 项目 hero 图：一个应用同时覆盖 HTTP/BT/磁力/FTP/M3U8/DASH/eD2k 七种协议。

![浏览器扩展嗅探 Demo](https://github.com/user-attachments/assets/6763c9e0-cd5d-450e-80f5-1e22adcff36e)

> 浏览器扩展嗅探 Demo：页面内浮出下载按钮，认证态（cookie/header/UA）随任务带进桌面端——这是官方对比表里它唯一拿到 ✅ 的一栏。

![官网主视觉](https://gd.xychr.com/shots/light/shot-01.webp)

> 官网主视觉：文件下载、直播录制、任务排队三种形态同屏。

![浏览器扩展浮出下载按钮](https://gd.xychr.com/shots/light/shot-02.webp)

> 扩展在视频页内浮出的下载按钮——深度集成不只是「接管链接」，而是把浏览器里的媒体变成桌面端的一等任务。

![Android 端直播录制](https://raw.githubusercontent.com/XiaoYouChR/Ghost-Downloader-3/main/.github/assets/android-recording-light.webp)

> Android 端直播录制：四端共用同一套引擎（非 Electron 壳），后台录制是桌面端之外的真实增量。

[官方演示视频（YouTube）](https://www.youtube.com/watch?v=QQRa8nDmNbc)

> 官方演示视频；README 另提供 Windows/macOS/Linux/Android 四端安装包，Windows/macOS 有代码签名，macOS 通过 Apple 公证。

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/XiaoYouChR/Ghost-Downloader-3 |
| Star / Fork | 14,966 / 901 |
| 代码行数 | 62,193 行手写源码（Python 65% / TypeScript+TSX 16% / C 2% / JS 1%） |
| 项目年龄 | 39.3 个月（2023-08-16 起） |
| 开发阶段 | 密集开发且仍在加速（近 30 天 228 commit / 近 90 天 507 / 近 365 天 1,377，占全历史 77%） |
| 贡献模式 | 独立开发（21 位贡献者，主作者占 93.7%，其余多为 bot） |
| 热度定位 | 大众热门 · 爆发型第二波（2026-11-21 单日 +774，Trending 冲到 #6，在榜 69 天） |
| 质量评级 | 代码[优秀] 文档[优秀] 测试[良好] |

> **两个容易被 GitHub 标签误导的口径**：
> ① **代码行数要打折看**：tokei 全仓口径给出 166,356 行、TypeScript 占 65.6%——这是因为 `app/assets/i18n/gd3.*.ts` 这 16 份 **Qt Linguist 翻译目录**（Crowdin 机器生成，每份约 6,390 行，合计 102,080 行）用了 `.ts` 扩展名，被当成了 TypeScript 代码。剔除后**真实手写源码 62,193 行**（tokei 口径 64,427 行，含 12,229 行 JSON——主要是 `package-lock.json` 等锁文件）：**Python 40,402 行（65%）、TypeScript+TSX 10,054 行（16%）、C 1,063 行、JavaScript 339 行**。也就是说 **Python 是绝对主体，浏览器扩展的 10K 行只占真实代码的约 1/6**——GitHub linguist 标的 Python 81.2% 才是更接近真相的口径。仓库 97MB 的体积主要来自 `dist/packs/*.zip` 与 `.qm` 编译产物，不是代码。
> ② 提交类型统计显示 `Test` 仅占 1.0%，这是**按 commit message 前缀分类造成的假象**：`fix(m3u8): …` 这类「顺手在 tests/ 里补了断言」的修复全被归到 Fix。实际有 **474 个测试函数、53 个测试文件，覆盖全部 12 个协议 pack**（bili 44 / m3u8 42 / bittorrent 30 / http 28 / ffmpeg 18 / zip 16 / ed2k 16 / arxiv 8 / wrapped_link 6 / huggingface 6 / yt_dlp 5 / github 5）+ 平台层 250 项（`test_coroutine_runner` / `test_name_conflict` / `test_seeding` / `test_port_listener` / `test_websocket_stream` / `test_cli` ……——**ADR 里的关键决策几乎都有对应的测试文件**），`tests/` 目录被 182 次提交触及，CI 在三平台 + Android Kotlin 单测上强制跑测试并卡住构建。
> License: GPL-3.0（引擎开源，通过 CLA 允许贡献进入闭源 Android 版；自建 FFmpeg 为 LGPL，已消除 GPL 授权风险）。

## 作者视角：为什么存在这个项目

### 创始人/作者背景

**Halcyon Chen**（GitHub ID: `XiaoYouChR`），湖北武汉，无公司，账号 2021-07 注册，419 粉丝、47 个公开仓库。绝对核心项目排在其最近 push 仓库的第 1 位。

从三条线索能反推他的技术底色：

- 自述长期在 **Qt/PySide6 跨端与嵌入式**方向深耕——写过《在 Android 设备上部署 PySide6 程序》《基于 ESP-IDF 的 Rust + Slint + ESP32-S3 快速上手》；
- 项目起点极小：README 自述 *Started as a passion project to help a Bilibili creator manage resources*——最初只是帮一位 B 站创作者管理资源；
- 生态位是「自己造轮子型」：伴生项目里自建了 Go 写的 eD2k 引擎 **Kelpie**、自建极简 LGPL **Ghost-Downloader-FFmpeg**、自建 MDX 官网，还反向贡献上游 PyQt-Fluent-Widgets 生态。

早年国内媒体（煎蛋网）称其为「高中生写的开源下载器」——这个标签今天已被事实推翻：39 个月、1,780 次提交、95 个版本、四端原生、32 篇 ADR。

### 问题判断

作者把命题写成两句话并贯穿全项目：*Every downloader is fast on a good connection. The real test is a bad one.* 与 *authentication state carries over*。

这个判断有三个层次：

1. **弱网稳健性 > 好网速下的峰值速度**。绝大多数下载器的性能叙事建立在理想链路上，作者把战场换到受限网络——于是有了直写偏移、稀疏预分配、分片合并与重分配、带宽自适应控制环这一整套设计。
2. **浏览器的才是「真身」**。浏览器里的视频带着登录态、加密签名、临时 URL，而桌面下载器看到的是一个失效链接。作者认为「能不能把浏览器里看到的东西完整地拿到桌面端」才是真问题——这直接催生了 2026-03 的浏览器扩展架构跃迁。
3. **没人同时做了所有事**。IDM 闭源且无 BT/磁力；Motrix 是 Electron 壳且无嗅探；Gopeed 无嗅探无 HLS；AB DM 只做纯 HTTP。作者要的不是「更好的下载器」，而是**下载器的集大成者**，正面替代 IDM。

**时机判断很准**：让「真实浏览器 TLS 指纹伪装」在 Python 里第一次变得可行的，是 `wreq`（Rust reqwest + BoringSSL）的出现（`pyproject.toml:19`）。README 把它列为第一卖点：*Real-browser TLS fingerprints, invisible to anti-bot checks.*——这不是渐进优化，是**整个 HTTP 栈的替换**。为什么不是 2 年前：那时 wreq 不存在，TLS 指纹只能靠 curl-impersonate 这类外挂进程，跨端与打包都不成立。

### 解法哲学

**① 选了「功能完整」，但用一种极特殊的方式化解「大而全」的复杂度——不是靠抽象，而是靠「宪法」。**

`CLAUDE.md` 是一份完整的项目宪法，融合 Zen（Python/Perl 传统）与 Ousterhout（《A Philosophy of Software Design》）：

```plain
- Simple is better than complex. (Zen)
- Flat is better than nested. (Zen)：函数优于类、内联优于跳转、三行重复优于过早抽象
- Explicit is better than implicit. (Zen)：依赖显式传入、配置显式注入
- Signal-driven actors. Service 拥有私有状态，对外仅通过信号通信；Service 不持有 View 引用
- General-purpose modules are deeper. (Ousterhout)
- YAGNI: trust internals, validate at boundaries. 不写 hypothetical 防御
- If the implementation is hard to explain, it's a bad idea. (Zen)
```

这不是口号而是**可执行的规则**。`GLOSSARY.md`（19KB）为每个概念写出 `_Avoid_` 清单（例如 Task 的 Avoid 是 download/job，Name 不叫 title 或 filename）。最狠的一条是**动词表**（`CLAUDE.md:59-95`）——用 30+ 个动词规范副作用语义：`load` 读本地持久化 / `fetch` 一次网络请求 / `probe` 只查能力不建任务 / `remove` 脱离不删盘 / `delete` 破坏性删除。作者的配套自检极为精准：*名字难取是设计的信号*——只能用 `handle`、`process`、`resolve` 这类看不出副作用的动词时，说明职责不清或 seam 划错了。

**② 性能与稳健性优先，且判断标准是弱网表现**。分片直接写入成品文件偏移（免去合并阶段，省一半磁盘 IO 与临时空间）、带宽自适应控制环、全局令牌桶限速（所有 pack 共享）。

**③ 开放，但开放得极其彻底**：引擎 GPL v3 全量开源（通过 CLA 允许进入闭源 Android 版）；插件机制目录即插件；第三方二进制（yt-dlp / FFmpeg / QuickJS）**全部运行时安装不塞进发行包**；翻译只经 Crowdin 一个写入方（`ADR-0035`，README 明确拒绝翻译 PR）。

**④ 明确选择不做什么**——Roadmap 只有两条（「公开插件 API」「增强任务编辑」），没有「支持 XXX 格式」的许愿单。ADR-0002 明确写下：*No call site ever transcodes audio or video.* 不做转码、不做云端账号、不做多端同步、不做内嵌播放器。

### 战略图景

这是作者**唯一**的核心项目——它不是基础设施、不是 SDK、不是课程，**它就是产品本身**。

**没有商业化意图的证据**：无账号体系、无云服务、无付费墙。README 的赞助位是 SignPath.io 提供免费代码签名 + 个人提供免费签名——作者把「签名」这件商业服务换成了赞助，但代码本身完全免费无限制。

开源策略是**有意识的「引擎开放 + 宿主闭源」**：Android 端仓库 `XiaoYouChR/Ghost-Downloader-Android` 不公开，仅在 CI 中 checkout 跑 Kotlin 单测（`.github/workflows/test.yml:47-52`）。

值得单独记录的是作者的**AI 治理姿态**：`CONTRIBUTING.md` 含 AI 工具使用政策（PR 需声明辅助/主要生成），PR 模板把「AI 工具使用」设为必填项，而 **Issue 模板明令禁止 AI 代写**（*请用自己的话写清现象、复现步骤和原始日志*）。同时 `GROK.md` 专门定义「AI 参与设计评审」的协议——一边用 AI 一边给它立规矩，这在开源项目里相当独特。

**但最大的战略缺口在这里**：Issue #347（28 条评论后被作者关闭）中，社区正式提议角色分工——一人写码、一人做翻译、一人做验证、一人做发布。作者讨论后**没有接受制度化的贡献者分工**。配合 93.7% 的单人提交占比，这是项目最大的结构性风险，也印证了作者「把工程质量内化为个人纪律」而非「制度」的风格。

## 核心价值提炼

### 创新之处

按「新颖度 × 实用性」排序：

1. **纯 Python 的 MP4/WebM 容器解析器 + HTTP Range 裁剪**（`features/ffmpeg_pack/container.py`，1,274 行，**全仓最大的手写源文件**——第二名是 1,070 行的 `app/view/components/setting_cards.py`）
   自己遍历顶层 box 找 `moov`，解析 `stsd`/`stts`/`ctts`/`stsz`/`stco`/`co64`/`stss` 得到逐样本时长、CTS 偏移、大小、文件偏移与关键帧表，再解析 `sidx` 分段索引（WebM 侧解析 EBML）。由此实现：**用户要视频的某一分钟，GD 只用 Range 请求拉取 `moov` + `sidx` + 目标区间字节，自己拼出可播放的文件——不下载整片，也不转码**。
   新颖度 4/5 · 实用性 4/5 · 可迁移性 4/5。用「用 Range 读 moov 做 seek」在播放器领域是常识，但「解析 sample table 自己重建文件」是播放器级别的活，把它放进下载器做片段裁剪是新鲜的组合。可迁移到云端点播预览、远程审片、日志视频抽帧。
   *（该模块有 18 个测试，`tests/ffmpeg_pack/test_container.py`。）*

2. **浏览器 MSE 字节级归因系统**（`browser_extension/app/src/page-media/attribution/`，2150 行 TS）
   扩展不只嗅探 `<video src>`，而是在 MAIN world 注入脚本 hook `MediaSource.prototype` 的**每个实例**（注释写明原因：*Hook each MediaSource instance, never MediaSource.prototype: CCTV's player stops decrypting video when its prototype methods are not native*），记录 `addSourceBuffer` 的 mime、`appendBuffer` 的字节流与 fetch 的 URL，再通过**字节级指纹**把「页面上正在播的视频」和「网络上真实存在的媒体 URL」对应起来。两个工程化技巧：**mdat 尾字节比对**（remux 型播放器如 TikTok 逐字节复制 sample，其 fetch 到的 MP4 head 能指明样本来源）与**区分度过滤**（*Repeated silent AAC frames are byte-identical across unrelated videos*，故要求尾字节足够多不同值）。
   新颖度 4/5 · 实用性 4/5 · 可迁移性 3/5。「归因账本 + 站点策略接口」的抽象可迁移到任何「观测到的行为要映射回某个网络资源」的场景。

3. **「宪法 + 动词表 + 术语表」驱动的代码品味工程**（`CLAUDE.md` + 19KB `GLOSSARY.md` + `GLOSSARY-MAP.md` + `GROK.md` + 32 篇 ADR）
   把「代码品味」显式化、可机器检查（目前主要靠 AI 与人工共同执行，尚未落地为 ruff 规则或 pre-commit 钩子——这是缺口）。ADR 模板本身就是可以立刻套用的工程实践。
   新颖度 4/5 · 实用性 4/5 · **可迁移性 5/5**。

4. **`SparseView`：让部分下载的压缩包可被标准库解压**（`features/zip_pack/sparse.py`）
   实现 `io.RawIOBase` 子类，把「已下载的字节区间」抽象成可 seek 的稀疏视图——`readinto()` 落在已下载段内就从对应源读，否则抛 `OSError("压缩包的这段数据还没有下载：{position}")`。于是 `zipfile.ZipFile` 可以直接读它：**只下载中央目录与所需条目时，就能解压出那几个文件**。
   新颖度 4/5 · 实用性 4/5 · 可迁移性 3/5。稀疏文件视图不新鲜，但做成 `io.RawIOBase` 从而复用标准库解压器是漂亮的工程复用。

5. **候选端口池 + 客户端 Happy Eyeballs 竞速 + 胜出记忆**（`app/services/port_listener.py` + `browser_extension/app/src/background/desktop-bridge.ts`）
   Windows 的 Hyper-V/WSL（WinNAT）会在 `1024-15000` 与 `49152-65535` 区间**按 100 个连续端口为一块保留**，导致默认端口 `14370` 频繁 `WSAEACCES` 无法绑定（#1028）。方案两端对称：桌面端按候选池 `[14370, 24370, 34370, 44370, 38370]` 顺延绑定并回写配置；扩展端在 150ms 内首选端口没连上就**并发**打开全部候选（不是串行轮询——Windows 上连接未监听端口单次超时可达 500–2000ms），第一个胜出后关闭其余并**记住胜出地址**。过渡期策略很讲究：否决「一步到位改默认端口」，因为旧版扩展写死只连 `14370`，一旦切走存量自管理扩展无法完成 `hello` 握手触发自更新、商店版扩展会全部失联。
   新颖度 3/5 · **实用性 5/5**（在真实 Windows 环境里解决高频、恼人且反直觉的问题）· 可迁移性 4/5。

6. **协议知识留在 Pack 的窄接口设计**（ADR-0011）
   App 只知道 6 个动词：`parse` / `run` / `runSeeding` / `relink` / `reset` / `deleteFiles`。协议专属概念（分享率上限、DHT、AES-128 key、签名 cipher）**不泄漏到 App 层**。ADR-0011 明确否决了「一组 `onCompleted`/`onRemoved`/…… 钩子」的方案，理由是*浅模块，两份实现*。实测收益：`features/arxiv_pack` 只用一个新 pack 就获得完整的 arXiv 论文（PDF + BibTeX + LaTeX source）下载能力。
   新颖度 3/5 · **实用性 5/5** · **可迁移性 5/5**。

7. **差量更新（HDiffPatch）+ 进程外 Updater + 三平台统一的「先改名再替换」**
   CI 用 `hdiffz` 为每个平台生成目录级增量（~6MB vs ~100MB 完整包），交给 C 写的跨平台 `tools/updater/updater.c`（退出码语义化：`0 ok / 1 patch / 2 rename / 3 timeout / 4 launch / 5 args`）。ADR-0017 的原则值得单列：*原地覆盖时 macOS 会杀掉被覆盖的程序，Linux 写入失败，Windows 不能覆盖或删除，但三平台都允许改名*——所以**运行中的程序也能更新**。
   新颖度 3/5 · 实用性 4/5 · 可迁移性 4/5。

### 可复用的模式与技巧

以下 12 条**与「下载器」无关，可直接迁移**（完整 29 条见 `tmp/ghost-downloader-3-phase-3-analysis.md`）：

1. **动词表规范副作用语义**（`CLAUDE.md:59-95`）——同一个意思处处用同一个动词，读者看动词就知道会不会联网、会不会删盘，不必读实现。*适用：任何有副作用的 API 设计。*
2. **ADR 四段式模板**（Decision / Considered Options + Consequences / Implementation seams）——**记录否决了什么以及为什么**，这是把设计决策变成可交接资产的唯一有效方式。*适用：长期维护项目、技术选型记录、新人 onboarding。*
3. **线程归属三分（D / L / J）+ 单一 post 通道**（ADR-0012 + `app/services/coroutine_runner.py:44`/`:98`）——状态所有权按线程划分，回调只经 `post()` 回到 Dispatcher 线程。*适用：Electron + Node worker、Flutter + native 线程、Spring WebFlux + 阻塞 IO。*
4. **文件系统作为唯一事实来源的原子仲裁**（ADR-0014 + `app/services/task_service.py:60-168`）——用 `O_EXCL` 空文件/空目录占位代替「查记录 + 查磁盘」，一次解决重名判定、大小写不敏感、多实例并发。*适用：任何多进程可能同时创建同一路径的场景。*
5. **temp + rename 原子写入**（`app/services/task_service.py:190-200`）——写 `.tmp` 再 `Path.replace()`，避免崩溃时留下半截 `tasks.jsonl`。*适用：任何持久化状态文件。*
6. **标志过滤 vs 集合增删**（ADR-0008）——Step 全量创建、用 `selected` 布尔过滤。代价是状态聚合的每个入口都要过滤（漏掉 `updateStatus` 会导致任务永远无法完成），换来「任意状态下都能改选择」。*适用：多文件下载、播放列表下载、批量任务部分执行。*
7. **library 模式只取解析能力，传输层留给自己**（ADR-0007 yt-dlp + ADR-0002 FFmpeg）——上游大依赖只当「解析器/转码器」，下载、限速、续传、指纹全部自持。*适用：集成 yt-dlp / ffmpeg / exiftool / 上游 SDK 的任何项目。*
8. **按实际调用面裁剪第三方二进制**（ADR-0002 的 `--disable-everything` + 精确白名单，80MB → 4–6MB）。*适用：自建固件/镜像、Electron 应用瘦身、对许可敏感的分发。*
9. **运行时安装外部依赖，不塞进发行包**（FFmpeg / yt-dlp wheel / QuickJS-NG）+ sha256 校验 + 独立版本线。*适用：桌面应用瘦身、需跟随上游快速修复的场景。*
10. **Sans-I/O 协议栈 + 同端口多协议**（ADR-0013 的 `WebSocketStream`）——同一端口同时服务 HTTP POST 与 WebSocket，连接生命周期统一管理。*适用：本地 IPC、需要「一个端口多种协议」的守护进程。*
11. **转发 exe（GUI 应用附带 CLI）**（ADR-0021 + `tools/ghd/ghd.c`）——console 程序转发 argv + std 句柄 + 退出码给主程序。ADR 逐条否决的六个方案都很有说服力，其中 `.cmd` shim 的否决理由值得单独记住：*cmd.exe 参数解析无法可靠转义（BatBadBut, CVE-2024-24576），而 URL 里的 `&`、`%` 正是 `ghd` 的核心输入*。*适用：Windows 上的 CLI 伴随程序。*
12. **为 AI Agent 设计 CLI 输出契约**（`app/cli.py:21-30` 的 `OUTPUT_CONTRACT`）——stdout 恒为一个 JSON 对象，且**刻意在 TTY 下不做表格化**：*有的 Agent 在伪终端里执行命令，按 TTY 切换输出格式会让它们拿不到 JSON*。*适用：任何将被 AI Agent 或脚本调用的 CLI。*

### 关键设计决策

#### 决策 1：线程归属三分，用「归属」而非「加锁」解决跨端竞态

- **问题**：Qt 桌面版与 Android 版共用同一业务引擎，但线程模型根本不同（Qt 主线程 / Android JVM 线程 / asyncio loop 线程）。
- **方案**（ADR-0012）：Dispatcher 线程 D 拥有全部服务状态（桌面 = Qt 主线程，Android = loop 线程）；loop 线程 L 拥有 socket、连接与协程；**Android 的 JVM 线程 J 不持有任何状态**，所有 engine 调用只经 `request` 一个入口切到 D。落地在 `app/services/coroutine_runner.py`：`submit()` 走 `call_soon_threadsafe`，`post()` 是**唯一**能把结果送回 D 的通道，`done`/`failed` 回调一律经 `post` 投递。
- **Trade-off**：牺牲「engine 方法可以随便从任何线程调」的灵活性，换来 **Android 端完全不需要任何锁**。ADR 明确否决了两个直觉方案：「每个 engine 方法自己切线程（漏掉一个就是一个竞态）」与「给服务加锁（锁住的是症状；Signal 同步 emit 会把锁带进 View 和其他服务）」。
- **可迁移性**：**高**。「按归属划分状态所有权 + 单一 post 通道」是比锁更廉价的一致性保证。

#### 决策 2：自建极简 LGPL FFmpeg（精确白名单替代现成大包）

- **问题**：只需三件事——remux（stream-copy）、mux + AES-128 解密、yt-dlp 后处理。但 BtbN 的 GPL 静态包 ~80MB，Android 侧 LGPL 全量包 ~30MB，两者都带着本应用从不调用的完整编码器套件，前者还有 GPL 授权风险。
- **方案**（ADR-0002）：自建 `--disable-everything` + 精确白名单，目标 **4–6MB/平台**。CI 用真实素材冒烟测试卡发布：*a missing demuxer fails CI, not a user download*（覆盖 bv+ba→mp4 remux、HLS AES-128 解密+mux、fmp4/m4s、EAC3、webp→mp4 缩略图、ffprobe duration）。安装链路另遵守 ADR-0017「**安装不是 Task**」——没有 Task、没有 Step、不进 TaskService、不可暂停、对用户不可见。作者明说：*为套用 Task 而付出的必填字段、手写 `stepIndex`、手动 `setStatus(RUNNING)`、速度与 fileSize 维护，全部换不来能力。*
- **Trade-off**：**代价是自己拥有一条 FFmpeg 构建流水线和安全补丁责任**。ADR 自己承认：*Cost: we own a CI build pipeline and FFmpeg security bumps — accepted, and bounded by the smoke-test gate.* 换来 80MB→4-6MB（**~15 倍体积缩减**）+ 消除 GPL 风险 + 版本可脱离 App 独立升级。
- **可迁移性**：中高（只在依赖能自建时适用）。

#### 决策 3：yt-dlp 改 library 模式 + QuickJS-NG（职责边界切到极致干净）

- **问题**：原方案 shell out 到冻结的 yt-dlp 二进制（~30MB）+ deno 运行时（~100MB），**用户要先下 130MB 才能用 YouTube**；且整个 pack 只是一个 ~1049 行的子进程包装器（拼参数、spawn、解析 stdout 进度）。
- **方案**（ADR-0007）：改为 **library 模式、只做 extract**。运行时拉 `yt_dlp` wheel（3–5MB）+ QuickJS-NG `qjs`（~2MB），共 ~7MB，**比原来少 ~123MB**。`extract_info(url, download=False)` 在 `asyncio.to_thread()` 里跑；**下载仍走自家 `FFmpegResourceStep`（继承 `HttpTaskStep`）+ wreq**，以保留全局限速、Range 续传、指纹伪装——yt-dlp 的 `downloader/` 模块从不被调用。隔离上，所有 yt-dlp import 用 `importlib.import_module` 懒加载，**Nuitka 的 AST 扫描器看不到它们**，主二进制体积不变。
- **Task 结构**：固定 4 步（Extract → 视频轨 → 音频轨 → stream-copy 合并），Extract 步骤**幂等**——永远 yield，靠 URL 的 `expire` 参数判断是否重提取（6 小时内续传秒级跳过，超过则重提取 5–10s 后续传）。ADR 明确否决「运行时动态增删 Step」：*step reaching up to mutate task structure is a seam violation…… makes progress calculation unstable (`len(steps)` changes mid-run).*
- **Trade-off**：接受 yt-dlp 作为「每月 1–2 次紧急修复」的持续依赖（用拉最新 wheel 消费），换来 123MB 体积削减 + 下载层完全控制权。ADR 逐条否决了「自己重写 YouTube 提取」：*The YouTube extractor is ~12K lines backed by ~18K lines of shared infrastructure…… A solo maintainer cannot keep up*——这句话本身就是单人项目的现实。
- **可迁移性**：**高**。

#### 决策 4：分片直接写入成品文件偏移（省掉合并阶段）

- **方案**：每个 subworker 持有 `[start, end]` 区间，下载时用 `pwrite(fd, chunk, subworker.position)` **直接写到成品文件对应偏移**（`features/http_pack/task.py:340-345`），文件先 `ftruncate` 预分配大小（Windows 额外用 `FSCTL_SET_SPARSE` 尝试稀疏文件）。三处配套精细处理：① Windows 上 `os.pwrite` 不保证 >4GB 偏移正确，`app/platform/sysio.py:14-25` 用 `OVERLAPPED` + `OffsetHigh` 手工实现；② **分片合并**——慢分片被快分片追上时直接吸收右侧区间并移除右侧 task（`:210-216`）；③ **分片重分配**——剩余量最大的分片从中间劈开重新启动（`:188-208`）。
- **Trade-off**：**这是 Issue #341「暂停按钮不工作」的根因**。直写模式下，暂停/恢复/改 URL/换镜像都必须与已在途的分片写入做一致性协调，解法是 `.ghd` 元数据文件（`<QQQ` 的 start/position/end 三元组）+ `isFinishing` 标志（可从任意线程调用，读循环在下一个数据块或读超时时收尾）。相比「临时文件 + 合并」，直写模式下的暂停语义复杂得多。
- **可迁移性**：**高**。

#### 决策 5：带宽自适应控制环——只有停损，没有止损

- **方案**（`features/http_pack/task.py:227-268` `_autoSpeedUp`）：每秒采样一次速度，保留 **5 点滑动窗口**；算最大相对偏差 `maxDeviation = max(|s - avg| / avg)`，**偏差 > 15% 就直接返回**（网络不稳定时加连接只会加剧抖动）；稳定则**一次最多加 4 条连接**；加完等 5 秒，比较 **workerRatio（分片数增加比）** 与 **speedRatio（速度提升比）**——若 `workerRatio <= 0` 或 `speedRatio < 0.8 * workerRatio`，判定加速无效并**永久停止加速**。
- **独立印证**：TechMoon 那篇源码级分析的描述（*每秒采样、五点均值、波动低于 15% 才加连接，每次最多加 4 条*）与代码**完全吻合**；它的批评「**只有停损线没有止损线**」也完全成立——代码里**没有任何回收已开连接的逻辑**，`_splitSlowest` 只会劈、不会合。这直接对应 Issue #665「下载文件在最后阶段卡死速度为 0」。
- **Trade-off**：这是**启发式规则，不是闭环控制器**。阈值（15%、5 点、4 条、0.8）全是经验值，没有理论依据，也没有针对「最后一个分片」的专门处理。
- **可迁移性**：中（四段骨架可迁移，阈值不可迁移）。

#### 决策 6：浏览器服务三件套

**（a） 不用 `websockets.serve`（ADR-0013）**：Browser Service 与 Aria2 RPC 挂在同一个 Loopback Server 上。理由是 *Aria2 必须在同一端口上同时服务 HTTP POST 和 WebSocket，而 `websockets.serve` 无法处理带 body 的 POST*。否决方案里点出了真实 bug：*这正是 uvloop 下 Aria2 停止后 WebSocket 连接仍然存活的缺陷所在*。
**（b） 候选端口池 + 竞速**（见创新点 5）。另有一条值得学的否决：否决「按端口是否属于候选池隐式决定是否顺延」——*违背「Explicit is better than implicit」，用户在输入框看到固定端口号却被后台静默改写会产生困惑*。因此有明确的「自动选择端口」开关，开启时**禁用手动输入框**（只读展示当前生效值）。
**（c） 认证与配对**：`PROTOCOL_VERSION = 2`、`PairRequest`、`MessageType` 枚举、`pairToken`；扩展拿到的是**本机回环端口上的 token 认证**，不是暴露到局域网的服务。

**Trade-off**：复杂度显著上升（多一套候选端口逻辑、两端都要实现竞速、维护向后兼容的过渡期端口），换来「Windows 上 90%+ 用户开箱即用」。

#### 决策 7：Name Conflict 以磁盘为准，Placeholder 在加入时占住

- **方案**（ADR-0014）：`TaskService.add` 让 Task 用 **`O_EXCL` 语义**为它将产出的每个最终路径创建 Placeholder（空文件或空文件夹），失败即 Name Conflict。**路径是否被占用只看磁盘**，Task 记录只用来识别占用者是不是未完成的 Task。
- **收益**：*#781（文件已删仍加 `(1)`）和 #658（同批任务互相覆盖）由同一条规则解决，Windows/macOS 大小写不敏感和多实例并发也由文件系统原子保证*。ADR 明确否决了「查 store 中其他 Task 的 `outputPath` + 磁盘」：*记录与磁盘两个事实来源，文件被删后记录仍占着路径*。
- **Trade-off**：排队中的 Task 在输出目录**表现为 0 字节文件或空文件夹**（用户会看到一堆 0 字节文件）。ADR 承认这点，并加了「未完成任务的占位不适用 Choice，总是保留两者」的规则。

#### 决策 8：Feature Pack——目录即插件，manifest 即契约

- **方案**：`features/<pack_id>/` 目录 + `manifest.toml`（`entry` / `class` / `dependencies` / `version` / `gdMinVersion`）。`app/loader.py:44-100` 的 `seedPacks()` 按版本号把「出厂 Pack」同步到「运行时 Pack 目录」，`loadPacks()` 按 `dependencies` **拓扑排序**加载并检查 `gdMinVersion`。`PackConfig.__init_subclass__` 允许 Pack 声明自己的配置项并自动挂到 `cfg` 上。
- **Parser 路由**（`app/services/feature_service.py:113-127`）：按 `priority` 排序（`wrapped_link`=10 迅雷链接先解包 → `github`=75 → `m3u8`=80 → `http`=100 兜底）。**已 probe 的链接，前面的 parser 解析失败就继续往后试**——这是 ADR-0025「probe 之后按内容重新分派」的实现。
- **注入点极窄**：`app/models/pack.py:297-306` 的 `FeaturePack` 只有 `parse` / `addTask` / `submit` 三个 callable。**依赖注入而非继承**——且 FFmpeg/yt-dlp 的安装包下载也走同一条 `featureService.parse` 路由，因此自动被 GitHub 镜像加速覆盖，而 `features/ffmpeg_pack/` 与 `features/github_pack/` 互不 import。
- **Trade-off**：**Pack 是在主进程内 `importlib` 导入的 Python，没有沙箱**——一个坏 Pack 能搞崩整个应用。作者在 Roadmap 承认 API 尚未公开稳定。

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | Ghost Downloader 3 | Gopeed | Motrix (Next) | AB Download Manager | IDM（闭源） |
|------|---------|--------|--------|--------|--------|
| Star | 14,966 | 27,899 | 58,684 | 19,462 | 商业（30 年护城河） |
| 技术栈 / 原生度 | Python + PySide6，四端原生 | Go + Flutter | Electron 壳 | Rust + Flutter | 原生 C++ |
| 协议覆盖 | HTTP/BT/磁力/FTP/M3U8/DASH/eD2k | HTTP/BT/磁力/eD2k | HTTP/FTP/BT/磁力/Metalink | **仅 HTTP** | HTTP/FTP（无 BT/磁力） |
| 浏览器接管 | ✅ 唯一（带 cookie/header/UA 迁移） | ⚠️ 仅链接接管 | ⚠️ 4/4 与 GD 持平 | ❌ | ⚠️ |
| 资源嗅探 | ✅ 18 站全支持 + 2 部分 | ❌ | ❌ | ❌ | ✅ 18 站全支持 |
| 站点特化 | YouTube / B 站 / GitHub / HF / arXiv | ❌ | ❌ | ❌ | ❌（DRM 串流除外） |
| 插件 / 可编程 | Feature Pack + `ghd` CLI + aria2 RPC | JS 扩展 + REST API | QuickJS 沙箱 | ❌ | ❌ |
| 平台 | Win/mac/Linux/**Android** | Win/mac/Linux/Android/**iOS** | Win/mac/Linux | Win/mac/Linux | 仅 Windows |
| 维护健康度 | 单人 93.7%，近 30 天 228 commit | 多维护者，持续活跃 | 老仓停滞（~790 open issues） | 96% | 商业团队 |

### 差异化护城河

1. **技术护城河（中等偏强）**：不是单点技术，而是**组合复杂度**——纯 Python 容器解析 + Range 裁剪、MSE 字节级归因、wreq TLS 指纹、跨平台分片直写 + Windows 64 位 `pwrite` + 稀疏文件、自建 LGPL FFmpeg、自研 eD2k 引擎（Kelpie）、Sans-I/O 同端口双协议。**每一项单独看都可被超越，但全部叠加在一起的维护成本极高**。
2. **信任护城河（强且独特）**：32 篇 ADR + 19KB 术语表 + 项目宪法构成的「公开败绩」文化。TechMoon 那篇源码级分析特别肯定了这一点——公开 ADR 让人敢于指出缺陷、也让第三方敢于在其上开发。**这在下载器这个「广告、捆绑、灰色操作」行业里是极稀缺的信任资产。**
3. **隐性护城河（很强）**：**作者本人**。93.7% 的提交占比 + 2026-03 起连续 5 个月 150+ 高位提交，说明这是被持续投入而非被放养的项目——竞品 Motrix 恰恰死在这里。
4. **生态护城河（弱）**：14 个 Feature Pack 是 1,192 次提交累积出来的，但**没有第三方 pack**（API 尚未公开）。这是护城河上的缺口，也是 Roadmap 第一条。

### 竞争风险

- **最可能替代它的不是竞品，而是组合拳**：GD 的能力面太宽，单点能力（BT、HTTP 速度）都打不过垂直玩家；当用户只需要其中一项时，GD 的复杂度就成了负担。「Gopeed + 独立扩展/脚本」或「Motrix + 第三方嗅探扩展」是更现实的替代路径。
- **最现实的风险是作者倦怠，不是被竞品打败**。XDM 的停滞（维护健康度 8%、Chrome 扩展 2025-09 被下架、~850 open issues）说明**这个赛道的死亡方式是「维护者退出」而非「被产品击败」**。而 2025-08~2026-02 的濒死期（半年仅 7 次提交）是**实证过的失败模式**——Issue #347 正是社区对这个风险的制度化预警。
- **技术替代风险（最大的单点依赖）**：wreq 这类 Rust TLS 指纹库若出现更成熟的替代品，或浏览器扩展的 Manifest V3 政策继续收紧（`webRequest` 权限受限），GD 的「浏览器深度集成」这根独苗可能被平台掐断。

### 生态定位

- 在下载器生态里，GD 是**「IDM 的开源、跨平台、可编程替代品」**——红海里的差异化蓝海。它真正在跟 IDM 抢用户，而不是跟 Gopeed 抢：官方对比表与 2026-11 第二波出圈（用户因 IDM 付费 + 迅雷限速而寻找替代）都指向这一点。
- 在更大生态里，它扮演**「下载基础设施 + 浏览器协同层」**：同时是下载器、是 `ghd` CLI、是 aria2 兼容的 RPC 服务端、是可编程的平台。**它正在从「一个应用」变成「一个协议 + 一套运行时」**——32 篇 ADR 里有一半是在定义协议（消息类型、Task 抽象、Pack 契约、CLI 契约）。
- 在「独立开发者造轮子」的谱系里，GD 是**罕见地把工程方法论也开源的案例**。其**方法论价值可能大于产品价值**。

## 套利机会分析

- **信息差**：**已被发现，不再是信息差套利标的**。2026-11-21 单日 +774、Trending 冲到 #6、在榜 69 天，star 从 2025-12 的约 1,000 涨到 14,966（近 90 天 +3,975）。真正的信息差在于**社区普遍以为它「只有 1% 的测试覆盖」**——那是按 commit message 前缀分类的统计假象，实际有 474 个测试函数覆盖 12 个协议 pack，三平台 CI 强制卡构建。同样，**媒体普遍只报道功能复述，几乎没有一篇做源码级分析**（仅 TechMoon 一篇）。
- **技术借鉴**：这是本项目最实在的价值出口。12 条可迁移模式（见上）几乎条条可以直接用——尤其是**线程归属三分 + 单一 post 通道**（解决跨端竞态）、**动词表规范副作用语义**（让 API 自解释）、**library 模式只取解析能力**（集成大依赖）、**文件系统作为唯一事实来源的原子仲裁**、**ADR 四段式模板**、**按实际调用面裁剪第三方二进制**、**为 AI Agent 设计 CLI 输出契约**。此外 `features/ffmpeg_pack/container.py`（纯 Python 容器解析）与 `features/zip_pack/sparse.py`（SparseView）是可以直接拿来用的代码。
- **生态位**：填补了「**多协议全栈 + 浏览器深度集成 + 站点特化 + 插件化 + 四端原生**」这一组合的空白。但要注意这个生态位**依赖作者的持续投入**——它不是一个「一旦发布就稳定存在」的基础设施，插件生态也尚未启动（API 未公开）。
- **趋势判断**：**增长强劲且符合趋势**——近 365 天提交占全历史 77%、仍在加速；技术上踩中了「AI Agent 需要结构化工具接口」这条线（`ghd` 的 JSON 输出契约是明证）与「跨端一致性」这条线。但**它的 star 增速已经见顶信号明显**（11 月三周内从 14.1K 到 14.9K 后进入平台期），而**护城河的深度没有随 star 同步增长**——第二波出圈的驱动力是「IDM 太贵」这一价格事件，不是技术代差。

## 风险与不足

1. **巴士因子 = 1**（最大风险）。93.7% 的提交来自一个人（21 位贡献者，其余多为 bot）。2025-08~2026-02 已有半年停摆的实证失败模式。Issue #347 的社区分工提议被讨论后关闭，意味着这一风险**目前没有任何制度化对冲**。
2. **「智慧加速」名不副实**。`_autoSpeedUp` 是启发式规则而非闭环控制器：只有停损没有止损，连接只加不减（`features/http_pack/task.py:227-268`）。这正是 Issue #665「末段速度卡死 0」的根源，也解释了长任务后期的速度僵持。TechMoon 的独立源码分析已完整印证。
3. **默认不校验 TLS 证书**。`app/config/cfg.py:250` 的 `shouldVerifySsl` 默认 `False`。虽然 `app/client.py:117-125` 用 certifi 而非 wreq 内置根证书的理由很专业（注释里引用了 2026-10 eMudhra 私钥泄露事件），但默认值仍是最不安全的那一侧。
4. **百度网盘官方客户端身份模拟的合规边界未在文档中说明**。`app/config/cfg.py:346-352` 的 `identityPresets` 内置了「百度网盘客户端」预设（`clientProfile: "raw"` + `userAgent: "pan.baidu.com"`，对 `*.pcs.baidu.com` 生效）。这是把反爬对抗做成了一等配置项，但服务条款边界没有任何文档说明。
5. **浏览器扩展的隐私风险与平台依赖**。扩展需在所有站点注入脚本；MSE 归因逻辑强依赖浏览器扩展环境与 MSE 生态，可迁移性受限。Manifest V3 政策若继续收紧，这条独苗会被掐断。
6. **插件 API 半封闭**。Feature Pack 无沙箱（在主进程内 `importlib` 导入），一个坏 Pack 能搞崩整个应用；且 API 尚未公开，第三方 pack 生态未启动。
7. **官方 benchmark 的说服力不足**。样本量小（单机六文件），且 OneDrive 项连接数不对等（GD/Motrix 128 线程 vs IDM/Gopeed 32 线程）——作者主动标注了这一点，但读者仍难以据此判断绝对性能。
8. **质量可观测性的有意缺口**。ADR-0010 明确决定「Compose 命令失败是 View 的 bug，不是用户条件」，**不为 View 的 bug 建错误报告基础设施**。这是有意的架构选择，但代价是生产环境缺少「预期外错误」的上报通道。
9. **测试的真实缺口**（在 474 个测试函数之外）：扩展侧只有 `npm run typecheck`，**无测试框架**；缺少 E2E 与真实网络/多进程的集成测试（`network` marker 存在但需联网）。这与 Issue #341（暂停按钮）这类跨 View/引擎状态同步 bug 恰好是测试盲区。
10. **发布流程有轻微人工不稳定性**：95 个 tag 对 94 个 release，`v4.4.1` 缺失——偶发漏发版本或热修复直接打 tag。
11. **代码规范的规则未机器化**。`CLAUDE.md` 的命名规则、动词表、反模式清单目前靠 AI 与人工共同执行，没有 ruff 自定义规则或 pre-commit 钩子兜底——对一个人维护的项目，这意味着规范会随时间漂移。

## 行动建议

### 如果你要用它

- **选它的场景**：需要**浏览器里的东西完整落到桌面**（带登录态的视频）、需要**多协议一站式**（BT + HTTP + 磁力 + FTP + M3U8）、需要**站点特化**（YouTube/B 站/GitHub/HF/arXiv）、需要**四端**（含 Android 后台录制直播）、需要**CLI/RPC 被脚本或 Agent 接管**。
- **别选它的场景**：只做纯 HTTP 大文件（AB DM 的 32 线程纯 HTTP 更纯粹、体积更小、维护更健康）；需要 Docker/NAS 部署或 iOS（Gopeed 更合适）；需要企业级支持和商业授权（IDM 是商业产品，能养专职团队）。
- **落地建议**：先用 **aria2 兼容 RPC**（默认端口 16800）把它接进你现有的自动化脚本——这是**最低成本的接入方式**，Gopeed 的 `aria2.add` 脚本可以直接指向它；用 `ghd` CLI 时**注意读 stdout 的单个 JSON 对象**而不是表格（这是刻意设计）。装完第一件事：**去设置里打开 TLS 证书校验**（默认关闭）。若只用 HTTP 下载，**先关掉「智慧加速」**——它的启发式在不稳定链路上会先加连接再停损，反而放大抖动。

### 如果你要学它

按「可抄走性」排序，优先读这几处：

1. **`docs/adr/` 全部 32 篇**——不必逐篇读，先读 `CLAUDE.md` 的 ADR 模板（Decision / Considered Options + Consequences / Implementation seams），这就是可以直接套用的方法论。**每篇都记录了否决了什么以及为什么**，这才是资产所在。
2. **`CLAUDE.md:59-95` 的动词表**——30+ 个动词规范副作用语义，附「名字难取是设计的信号」的自检。这套机制可以今天就套进你自己的项目。
3. **`app/services/coroutine_runner.py`（ADR-0012）**——线程归属三分 + 单一 post 通道。你只要做「同一份业务逻辑要同时活在 GUI 框架线程池与事件循环线程里」，这就是现成范式。
4. **`features/http_pack/task.py:227-268` + `:188-216`**——带宽自适应控制环 + 分片合并/重分配。读的时候注意它的**缺陷**：只有停损没有止损、阈值全是经验值——把它当骨架，别当答案。
5. **`app/models/pack.py:297-306` 与 `app/loader.py:44-100`**——插件只声明三个注入点、依赖注入而非继承、依赖拓扑 + 版本门槛 + 运行时覆盖。
6. **`app/services/task_service.py:60-168`（ADR-0014）**——用 `O_EXCL` 占位让文件系统做唯一仲裁。
7. **`app/cli.py:21-30`（ADR-0020）**——为 AI Agent 设计的 CLI 输出契约，及其「argv 交给主实例统一解析」的转发模型。
8. **`features/ffmpeg_pack/container.py` 与 `features/zip_pack/sparse.py`**——纯 Python 容器解析 + 稀疏视图喂标准库解压器，两块可以直接拿走的代码。
9. **`app/client.py:117-125`**——把一个真实安全事件（eMudhra 私钥泄露）写进代码注释的范例。

### 如果你要 fork 它

- **最值得改的地方，按性价比排序**：
  1. **把「智慧加速」改成闭环控制器**——补上止损（带宽饱和时回收已开连接）、对「最后一个分片」单独处理。这是 Issue #665 的根因，也是最容易做出可感知差异的地方。
  2. **把 `CLAUDE.md` 的规则机器化**——写成 ruff 自定义规则或 pre-commit 钩子（命名动词表、禁用词、`_Avoid_` 清单），让规范不依赖执行者的自觉。这对单人维护的项目是复利。
  3. **补浏览器扩展的测试框架**——当前只有 typecheck，扩展侧 2150 行的归因逻辑零覆盖，而它恰好是「浏览器深度集成」这根独苗所在。
  4. **补 E2E 与多进程/真实网络集成测试**——#341 这类跨 View/引擎状态同步 bug 是当前测试体系的盲区。
  5. **给 Feature Pack 加进程隔离**——目前 `importlib` 直接在主进程导入，一个坏 Pack 能搞崩整个应用；至少可以先加「加载失败降级 + 熔断」。
  6. **补一份 `docs/adr/0037` 把「安装不是 Task」的边界扩展到 pack 热更新**，并把 pack 的版本线与 App 版本线的解耦（`seedPacks` 已具备）写清楚。
- **不要改的地方**：`CLAUDE.md` 的原则、ADR 模板、动词表、`post()` 单通道、Pack 的三个注入点、「安装不是 Task」、ADR-0035 的单一翻译写入方——这几处是项目一致性的地基，动它们等于重写。
- **商业化的合规红线要提前想清楚**：百度网盘身份模拟、HLS/DASH 解密、站点特化解析都处在灰色地带，若要商业化必须先过法务。

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | 无法验证（`https://deepwiki.com/XiaoYouChR/Ghost-Downloader-3` 返回 HTTP 429 限流，无法区分「未收录」与「限流」） |
| Zread.ai | 无法验证（`https://zread.ai/XiaoYouChR/Ghost-Downloader-3` 返回 HTTP 403 反爬） |
| 关联论文 | 无（检索 arXiv 无相关结果；项目内有 `features/arxiv_pack`，是下载 arXiv 论文的功能而非论文引用） |
| 在线 Demo | 无在线 Playground；提供四端完整客户端安装包（Win/mac/Linux/Android）+ [官方演示视频](https://www.youtube.com/watch?v=QQRa8nDmNbc) + [官网交互式截图集](https://gd.xychr.com/) |
| **官方文档站** | [gd.xychr.com/en/docs](https://gd.xychr.com/en/docs/) |
| **⭐ 最佳知识入口** | **仓库内 [`docs/adr/` 的 32 篇 ADR](https://github.com/XiaoYouChR/Ghost-Downloader-3/tree/main/docs/adr) + `CLAUDE.md` + `GLOSSARY.md`**——比任何自动生成的 wiki 都更有信息量 |
| 独立深度分析 | [開源下載器 Ghost Downloader 3：加連線有停損點的智慧加速](https://techmoon.xyz/ghost-downloader-3/)（TechMoon，2026-09，唯一一篇有源码级独立视角的长文） |
