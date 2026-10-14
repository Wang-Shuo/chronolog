# M3 Actions 临时凭据改造 — 2026-10-14

**实现、本地和首轮远端验证完成；合并前须确认最终 head 的 Quality 通过并由人工批准。默认分支合并前仍使用原工作流；M3 整体验收未完成。**

## 改造范围

- 每日 `generate` 只读；依赖安装、三来源采集、pytest、Vault 校验和 Quartz 构建均在该任务执行。
- 通过门禁后将候选提交封装为 Git bundle，交给同一运行的独立 `publish` 任务。发布任务只执行工作流启动提交中的代码，不运行候选代码或项目安装脚本。
- 发布任务校验主分支基线、内容类型、PR 状态和远端 commit lease，只允许 Vault 内普通 Markdown 变化，保留已有 PR 人工编辑，拒绝并发覆盖。
- 使用任务级 `GITHUB_TOKEN` 推送分支、创建/更新机器人 PR，再显式派发只读 Quality，传入候选提交 SHA。无须机器人账号、PAT 或仓库 secret。
- 新增内容为空且没有待审 PR 时不创建 PR；已有待审 PR 的 no-change 运行仍同步主分支并补派发 Quality。派发失败后应启动完整新运行，刷新分支和 PR 状态。
- 通用 `Open delivery PR` 支持已有 `codex/` 分支，以机器人身份交付实现和文档，并显式触发 Quality。它不批准或合并 PR。
- 人工批准、分支保护及审核后 Pages 部署门禁保持有效。首次公开部署的历史报告随本次交付一同归档。

## 已完成验证

| 项目 | 结果 | 证据 |
| --- | --- | --- |
| Python 全量回归 | 160 项通过 | [tests.log](m3-evidence/ephemeral-credentials-local/tests.log) |
| 真实本地 Git 多工作目录验证 | 候选打包/导入、人工编辑保留、并发拒绝、删除、空批、非内容文件及符号链接/可执行文件拒绝、失败派发后 no-change 恢复、PR 状态变化与基线不匹配拒绝 | `tests/test_rolling_pr.py`，包含在全量测试中；GitHub 调用使用 mock |
| 工作流静态校验 | actionlint 1.7.7 通过（未运行 shellcheck）；Python 同时校验权限和提交检查约束 | `.github/workflows/{generate,quality,open-delivery-pr}.yml` |
| 生产地址构建 | pytest、Vault、Quartz、发布集合与 RSS 门禁全部通过 | [quality.json](m3-evidence/ephemeral-credentials-local/quality.json)、[publication.json](m3-evidence/ephemeral-credentials-local/publication.json) |

本地质量报告运行时 HEAD 是 `d8a7b71`，改造尚在工作区；报告中的 `code_sha256` 记录实际验证文件摘要，不应把报告解释为该旧提交已经包含本次改造。线上证据以交付 PR 最终 head 的 Actions 检查为准。

## 远端临时凭据验证

- [Open delivery PR 38584767963](https://github.com/Wang-Shuo/chronolog/actions/runs/38584767963) 成功，以 `github-actions[bot]` 身份创建 [PR #3](https://github.com/Wang-Shuo/chronolog/pull/3)，并使用自身的临时 `GITHUB_TOKEN` 派发 Quality。没有配置长期 bot secret。
- [Quality 38584794898](https://github.com/Wang-Shuo/chronolog/actions/runs/38584794898) 是实际 `workflow_dispatch` 事件，head 为 `c104650e8cbaacdc5f03493ffce8640a0c40b8a7`。提交核对通过，160 项测试及构建、Vault、发布集合、RSS 门禁全部成功。报告和摘要见[归档清单](m3-evidence/ephemeral-quality-38584794898/archive.json)。
- GitHub REST check-runs 返回该 head 的 `quality: success`，关联 PR #3。主分支仍要求 `quality`、一名批准人和更新后撤销旧批准，管理员也受规则约束。合并时须再次检查最终 head，不以此归档替代后续提交的 CI。
- 本节及远端归档在上述首轮检查后追加；后续文档提交也须重新派发 Quality。真实日常 `generate → publish` 的远端执行仍待改造合并至默认分支后验证；本次机器人交付不能替代该验收。

## 合并后的验收与操作

1. 确认机器人交付 PR 的最终 head 通过 `quality`，由 Wang-Shuo 人工批准后合并。
2. 从 `main` 手动启动 Generate review candidate，检查 read-only generate 与独立 publish。若 ChatGPT 403 且缺少有效快照，应保留失败报告并跳过 publish；补充有效官方快照后启动完整新运行。
3. 有真实内容变化时确认 PR 作者是 `github-actions[bot]`，只有一个 `codex/chronolog-updates` PR，Quality 自动派发到最新 head，主分支规则识别该检查。
4. 审核真实内容 PR 并部署，核对公开提交和 RSS；继续收集七次真实 schedule、恢复演练和交接证据。手动运行或本地重放不计为七次调度。

操作细节、权限、artifact 保留和故障恢复见[运行手册](../m3-operations.md)。本记录不宣称已完成真实日常采集或 C1–C5 全部验收。
