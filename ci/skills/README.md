# Vendored Skills

本目录是 GitHub Actions runner 上使用的 Claude Code skill 副本，避免 CI 时依赖 42plugin 平台。

## 来源

| Skill | 上游 | 协议 |
|---|---|---|
| `repo-miner/` | `opc/starlight/repo-miner` v1.0.1（42plugin） | MIT |
| `md2wechat/` | `zhiping/creator/md2wechat` v1.0.1（42plugin） | MIT |
| `opensource-weekly/` | 本仓库自建（开源周刊） | MIT |
| `resource-miner/` | 本仓库自建（资源类仓库分析：awesome / 学习资料 / 非典型非代码） | MIT |

每个子目录都保留了 `LICENSE` 文件，符合 MIT 协议要求。

`opensource-weekly` 是本项目自建 skill（非 42plugin 上游），直接维护在本目录；它调用
脚本 `src/scripts/{collect_weekly_facts,dedup_weekly,record_weekly}.py` 与配置
`src/data/opensource-weekly/*`（AI 判定 / 评分 rubric / 去重 / 核验规则）。

`resource-miner` 也是本项目自建 skill，与 repo-miner 并列用于「没有代码架构」的资源类仓库
（套 repo-miner 会得「近零代码行=已放弃」的错误结论）。它**自包含打包**了采集脚本
`scripts/collect_resource_facts.py` + 其依赖的 `scripts/collect_repo_facts.py`（与
`src/scripts/` 下的同名文件保持字节一致，参照 repo-miner 自带 `collect_repo_facts.py` 的做法）。
canonical 源仍在 `src/scripts/collect_resource_facts.py`；改动后需同步回本目录的副本。

## 同步策略

**42plugin 上游 skill**（repo-miner / md2wechat）：本地用 `42plugin install` / `update`
跟进上游版本后，运行：

```bash
cp -RL .claude/skills/repo-miner ci/skills/
cp -RL .claude/skills/md2wechat ci/skills/
git add ci/skills && git commit -m "chore: 同步 vendored skills"
```

**本仓库自建 skill**（opensource-weekly）：直接在本目录编辑即可；
若想本地用 `/opensource-weekly-*` 调用，可反向 symlink 到 `.claude/skills/`：

```bash
ln -s "$PWD/ci/skills/opensource-weekly" .claude/skills/opensource-weekly
```

若想本地用 `/resource-miner` 调用，可反向 symlink 到 `.claude/skills/`（与 opensource-weekly 同理）：

```bash
ln -s "$PWD/ci/skills/resource-miner" .claude/skills/resource-miner
```

CI 启动时由 `src/scripts/setup_ci_env.sh` 把全部 4 个 skill 拷贝到 runner 的 `~/.claude/skills/`。

AI 周刊已迁往 `~/proj.xt.com/ai-info`，不再由本项目安装或生成。
