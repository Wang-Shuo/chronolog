# M3 运行与交接手册

M3 使用 GitHub Actions 采集并生成一个持续更新的待审 PR，经人工审核、合并后部署到 GitHub Pages。2026-10-14 已确认仓库为 [Wang-Shuo/chronolog](https://github.com/Wang-Shuo/chronolog)，并配置本地 `origin`；部署目标为 GitHub Pages，预期 URL 为 `https://wang-shuo.github.io/chronolog/`。远端启用与正式验收仍需按[开发计划](development-plan-2026-10-13.md)的 C1–C5 完成。

## 1. 首次启用

1. 将本项目推送到选定的 GitHub 仓库，默认分支使用 `main`。保留 M1、M2 及其验收产物；新增工作流和依赖配置应一起提交。如果默认分支使用其他名字，同步修改 `.github/workflows/deploy.yml` 的触发分支。
2. 在仓库 **Settings → Pages** 选择 **GitHub Actions**。部署流程从 `configure-pages` 的真实 URL 读取 baseUrl，不把本地预览地址用于生产。使用自定义域名时同时设置仓库变量 `CHRONOLOG_BASE_URL`（格式为 `host[/path]`，不含 `https://`）。默认 PR 校验地址为 `OWNER.github.io/REPOSITORY`；用户主页仓库 `OWNER.github.io` 请设置变量为 `OWNER.github.io`，避免多余路径。
3. 在 **Settings → Actions → General → Workflow permissions** 允许 Actions 创建 PR。GitHub 将此项与允许批准 PR 绑定；本仓库已由维护者明确授权开启。工作流使用 Actions 自动签发、任务结束后失效的 `GITHUB_TOKEN`，不需要独立机器人账号、PAT 或 `CHRONOLOG_BOT_TOKEN` secret。日常发布任务只创建/更新 PR，不批准或合并；部署门禁仍拒绝机器人批准。
4. 设置 `main` 分支规则：要求通过 PR 合并、至少一名人工批准、更新后撤销旧批准，并将 **Quality / quality** 设为 required check。不得让生成机器人绕过此规则。部署脚本另行检查合并 commit 对应 PR 的最终 head 获人工批准，拒绝直接推送、旧 head 批准和 bot 批准。
5. 先手工运行 Quality，再运行 Generate review candidate。确认报告和 artifact 可下载，新的真实来源更新进入 `codex/chronolog-updates`，无需第二个并行 PR。

当前仓库地址及部署目标已确认，GitHub CLI 已登录；Pages 来源、base URL 和主分支规则已配置。PR #2 已经最终 head 人工批准、合并并成功上线，见[2026-10-14 公开部署记录](acceptance/m3-live-2026-10-14.md)。日常工作流改为临时凭据；改造须经新的交付 PR 审核合并后才在默认分支生效。连续运行与恢复交接仍待验收。

GitHub Release 采集使用工作流的只读 `github.token`，通过 `CHRONOLOG_GITHUB_READ_TOKEN` 注入，避免匿名共享 IP 限流；不会使用 PR 写入 token。令牌仅用于固定 `api.github.com` 请求，带认证时不跟随重定向。仓库迁移导致 3xx 时应修正 `sources.yaml`。本地未设置该变量时仍使用匿名请求，限流会留下失败记录并停止该批发布。

### 1.1 临时凭据与任务权限

凭据由 Actions 自动提供，不需要在聊天或仓库设置中输入 token，也不需要 OpenAI、Anthropic 或 Cursor API key。

| 任务 | 权限与行为 |
| --- | --- |
| `generate` | `contents: read`、`pull-requests: read`。准备滚动分支，执行采集、测试、构建，提交本地候选并上传 Git bundle；没有远端写权限。只允许在默认分支运行。 |
| `publish` | 前一任务成功后才运行。`contents: write`、`pull-requests: write`、`actions: write`，用于推送内容、维护 PR、显式触发 Quality。 |
| `Quality / quality` | `contents: read`。按派发时的精确提交执行检查，不获得发布权限。 |

发布任务检出工作流启动时的可信提交，不检出或执行候选 bundle 中的代码，也不安装项目依赖。它验证基线提交、PR 状态、远端分支 lease、历史继承及内容范围；相对主分支只允许 Vault 内普通、不可执行的 Markdown 文件。滚动分支中修改脚本、工作流或其他非内容文件会被拒绝，应通过独立交付 PR 处理。整个仓库含 Git 历史的候选 bundle 保留 7 天；运行报告保留 90 天。

`GITHUB_TOKEN` 创建/更新 PR 通常不会触发 `pull_request` 工作流，因此发布任务显式 `workflow_dispatch` Quality，并传入 `expected_head`。Quality 核对实际检查提交；分支发生竞态时检查失败，重新运行生成任务即可。主分支仍要求名为 `quality` 的检查和最新 head 的人工批准。

在 [Generate review candidate](https://github.com/Wang-Shuo/chronolog/actions/workflows/generate.yml) 点击 **Run workflow**，选择 `main`。真实内容变化会更新 `codex/chronolog-updates`；没有待审 PR 且没有变化时不会新建 PR。已有待审 PR 时，无内容变化也会同步主分支并补触发 Quality，以恢复先前的检查触发失败。人工审核者为 `Wang-Shuo`，PR 作者为 `github-actions[bot]`。

Quality 派发成功只表示检查已排队，不代表检查通过；合并前在 PR 中确认该 head 的 `quality` 成功。如果发布阶段失败，请从 **Run workflow** 启动完整新运行，重新获取 PR/分支状态；不要用旧候选覆盖并发编辑。之后按每天北京时间 09:15 调度。

普通实现和文档交付可使用 **Open delivery PR**：传入已推送的 `codex/` 分支、标题和正文，由 Actions 创建机器人 PR 并派发 Quality。该流程不修改分支、不审批或合并；已合并的分支不会重复创建 PR。

凭据成功不代表三个来源都会采集成功。ChatGPT HTTP 仍可能返回 403，需要下一节的有效官方浏览器快照；缺失或过期时整批应明确失败。

## 2. 每日流程与报告

生成调度为每天 **09:15 Asia/Shanghai（01:15 UTC）**，GitHub 可能延迟执行。调度不会直接部署。

- 生成操作先复制 Vault，执行全量三来源采集及 reconcile，再跑全部 pytest（包含固定黄金样本）、Vault 校验、Quartz 构建、HTML/索引/图谱/RSS 校验。
- 构建内容位于独立临时目录，避免 Quartz 的 `_pipeline` 忽略规则把候选内容全部过滤。即使构建进程返回成功，活动集合不匹配仍会失败。
- 任一采集、内容、链接或构建门禁失败时，不写回待审 Vault，不推送新候选。报告中保留成功和失败来源，以及未运行的检查。
- 全部门禁通过才把候选文件写入生成分支。已有 PR 上的人工编辑会随历史读取和 M1 所有权保护保留；与主分支合并冲突或机器区冲突时停止。推送使用精确的远端 commit lease，拒绝覆盖并发修改。
- 只有获取时间发生变化不创建或更新内容 PR。本次成功采集时间仍保存到 Actions artifact；站点展示上一次审核发布包含的获取时间，两者可能不同。

每次生成的核心文件：

| 文件 | 用途 |
| --- | --- |
| `quality.json` / `quality.md` | 来源状态与覆盖、文件增改废弃、候选数、DLQ、冲突、门禁及错误摘要 |
| `collection.json.gz` | 本次标准化输入、官方来源原文及来源状态；输入模式注明 live 或 replay |
| `tests.log` / `build.log` | 自动化评测与构建输出 |
| `vault-validation.json` / `publication.json` | 实际链接与发布集合、RSS 校验 |
| `evidence-sha256.json` | 运行证据摘要；`quality.json` 另存执行代码摘要 |
| `rolling-pr.json` | 独立 `publication-<run>-<attempt>` artifact 中的 PR 更新、Quality 派发结果或发布阶段错误 |
| `candidate/_pipeline/<run-id>/manifest.json` | 采集、抽取、合并、对账的诊断记录 |

状态含义：`no-change` 为获取成功且没有内容变化；`candidate-applied` 为候选已通过本地门禁并写入生成分支；`rolling-pr.json` 的 `review-required` 才表示 PR 创建/更新且 Quality 派发成功（检查本身仍可能失败）。`failed` 必须查看具体阶段；不能把它解释为产品没有发布。依赖或权限等前置步骤失败时，工作流也会生成 `phase: setup` 的失败记录。

## 3. ChatGPT HTTP 403 与人工快照

默认始终尝试官方 HTTP 采集。失败后仅允许使用具有获取时间和 SHA-256 的官方浏览器快照；其他来源失败仍按 M1 门禁拒绝整批发布。

1. 在浏览器打开官方 [ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)，保存完整渲染 HTML。确认没有工具输出截断，并记录实际获取时间及其时区。
2. 创建新的交接包，时间必须是本次实际获取时间，不能使用重放时间或文件 mtime：

   ```bash
   .venv/bin/python -m _scripts.snapshot_bundle \
     --html /absolute/path/chatgpt.html \
     --captured-at 'YYYY-MM-DDTHH:MM:SS+08:00' \
     --output /tmp/chronolog-new-capture
   ```

3. 包含 `chatgpt.html.gz` 与 `capture.json`。核对后将两者放入仓库 `_inputs/chatgpt/`，通过 PR 审核合并，或由受控操作更新已有待审分支，再手动重跑生成流程。该目录不会进入公开站点。
4. 快照有效期为 **36 小时**；未来时间超过五分钟、摘要不匹配、文件缺失、异常短文档或无法解析都会失败。过期后需要重新获取，不得修改旧包时间来续期。

页面与报告明确标识 `browser-snapshot`；即使当日使用新快照，也不记为自动 HTTP 成功。原 HTTP 错误保留在来源记录的 `http_error` 中。

## 4. 人工审核与发布

在 Rolling PR 中查看摘要、实际 Markdown diff、143 张既有待审候选中的变化和新增的候选。重点核对事实修正、被废弃记录、主题归属与叙事引用。不要把自动通过等同于内容审批；`_review` 的候选不会自动晋升。

审核最新 PR head 后合并至 `main`。Deploy reviewed site 会：

1. 用 GitHub API 验证合并 commit 和最终 head 的人工批准。
2. 对该提交重跑全部门禁，并使用 Pages 真实地址构建。
3. 上传完整站点 artifact，交给 Pages 部署。
4. 检查公共首页、`deployment.json`、搜索索引和 RSS，确认提交与构建摘要相符。

`deployment.json` 记录提交、运行 ID、baseUrl、索引与 RSS 摘要。公开检查的报告存于 `public-verification-<run>-<attempt>` artifact。工作流不支持从 PR 分支或本地未提交内容直接部署。

## 5. 失败恢复

| 故障 | 保留内容与恢复操作 |
| --- | --- |
| ChatGPT 403 / 单源或全源失败 | 不推送该批候选；查看来源错误，补充新快照或等待上游恢复，再重新运行生成任务。 |
| DLQ / 黄金样本 / 链接失败 | 查看相应记录，在实现 PR 中修复并通过 Quality 后重跑；不要跳过失败门禁。 |
| 机器区或主分支合并冲突 | 保留远端 PR；在待审分支中处理冲突或将人工修改迁移到正确的人类区域，再重跑。 |
| Quality 派发失败 / 发布凭据权限不足 | 查看 `publication` 报告和发布任务日志；确认 Actions 的创建 PR 设置，重新启动完整生成运行以刷新状态。已有 PR 的 no-change 运行也会补派发检查。 |
| push lease 拒绝 | 表示有并发编辑；不要强制覆盖。重新运行以获取最新远端分支。 |
| 构建失败 | 不上传新的 Pages 部署 artifact；上一版站点保持可用。 |
| Pages 部署请求失败 | 查看 Pages 作业状态和旧站点；失败操作不视为已发布。恢复服务后重跑部署作业。 |
| 部署成功但公共校验失败 | 不宣称发布验收通过。检查缓存/域名/路径；需要回滚时重跑最近一次确认成功的部署 workflow run，使其按原提交重建和发布，再检查公共 `deployment.json`。 |

每个运行使用新的 run-id 和输出目录；不要删除失败证据后复用原 run-id。主 pipeline 的中断恢复仍使用 README 中的 `--recover-only`，随后再运行新的批次。

## 6. 归档与保留

- Quality、生成输入/诊断和部署证据 artifact 保留 **90 天**；Pages 站点包保留 **14 天**。期限内可通过 Actions UI 或 `gh run download` 下载。
- 关键验收报告下载到 `docs/acceptance/` 并随验收 PR 保存，不依赖临时 runner 或开发机 `_pipeline/`。90 天届满前，将需长期保留的证据移入仓库的验收目录或已批准的长期存储位置。
- 输入及诊断只进入具有仓库访问权限的 artifact；活动站点只发出通过发布过滤的内容。M2 历史证据摘要保留当时版本，不随 M3 修改重写。

## 7. 本地复现与正式验收

只检查当前 Vault（不会更新内容）：

```bash
.venv/bin/python -m _scripts.operations --mode check \
  --run-id local-quality-001 --output _pipeline/local-quality-001 \
  --base-url localhost:8080
```

真实历史输入的离线全链路演练（候选留在输出目录，不写回正式 Vault）：

```bash
.venv/bin/python -m _scripts.operations --mode generate \
  --run-id m3-replay-001 --output _pipeline/m3-replay-001 \
  --collection docs/acceptance/m2-evidence/collection.json.gz \
  --base-url preview.example.org/chronolog
```

预览路径只是本地构建配置，不代表已有公共站点。`--apply` 仅用于干净的自动生成分支；正常审核/部署使用 GitHub 工作流。

C1 要求七次真实连续日常调度，不接受七次本地重放。七天证据齐备后运行：

```bash
python -m _scripts.verify_schedule --repo OWNER/REPOSITORY \
  --output /tmp/chronolog-seven-daily-runs
```

脚本检查真实 `schedule` 事件、连续日期、每源状态和 live 标记。同一 run 有多个 attempt 时，从 GitHub API 读取当前已完成的最新 attempt，只下载其精确名称对应的 artifact，并在 `scheduled-runs.json` 记录 `selectedAttempt` 和 `artifactName`；不会混用旧 attempt 的报告或以旧成功覆盖最新失败。若正在重跑或该 attempt 的 artifact 缺失，采集失败，待完成或恢复证据后重新运行。C2 还需至少一批真实新增内容的 PR、批准、合并、部署链路；C3 补充实际部署失败恢复演练；C4 保存公共 URL 验证报告；C5 由验收人依本文独立操作后确认。
