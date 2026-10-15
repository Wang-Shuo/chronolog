# M3 首次成功真实采集与临时凭据发布 — 2026-10-15

**快照 PR #4 已审核合并部署；三来源采集、内容门禁和临时凭据发布成功。内容抽查曾报告 API 符号显示问题；用户随后批准 PR #5 的最终 head，现已合并部署，见[发布验收](m3-first-reviewed-content-release-2026-10-15.md)。该发布提交仍含显示问题；后续[修复交付](m3-dollar-title-fix-2026-10-15.md)待批准发布，M3 整体验收未完成。**

本记录及下载证据在运行后补充，并与标题修复一同纳入本次审阅提交。远端原始证据见以下运行链接。

## 已完成

1. Wang-Shuo 于 `2026-10-15T01:53:36Z` 批准 PR #4 的最终 head `2ce3bc34c8ae2560d864a98a8b76c260576f9504`。必需 `quality` 通过后合并为 `54ab03055aa64c11df7e03c1d3e6723ae1cc23b3`。
2. [Deploy reviewed site 38668183904](https://github.com/Wang-Shuo/chronolog/actions/runs/38668183904) 成功，[公开校验](m3-evidence/live-generation-38668187171/public-check/public-verification.json) 确认线上仍为已审核内容：2,756 个活动页面、30 项 RSS，提交为 `54ab030`。
3. [Generate review candidate 38668187171](https://github.com/Wang-Shuo/chronolog/actions/runs/38668187171) 的只读 `generate` 与独立 `publish` 均成功。该次事件是手动 `workflow_dispatch`，不计入七次真实 schedule。
4. ChatGPT 成功使用用户于 `2026-10-14T23:26:11+0800` 获取的官方快照；Claude Code、Cursor 分别于 `2026-10-15T01:55:15Z`、`2026-10-15T01:55:30Z` 成功 HTTP 获取。仍保留 ChatGPT 原 HTTP 访问错误，不将快照误报为 HTTP 成功。
5. 160 项测试、Vault、Quartz、发布集合/RSS 全部通过；DLQ 为 0、冲突为 0。隔离候选有 2,768 个活动页面、30 项 RSS、39,448 个 HTML 链接通过检查。
6. 临时 `GITHUB_TOKEN` 推送 `codex/chronolog-updates`，创建 [PR #5](https://github.com/Wang-Shuo/chronolog/pull/5)，作者为 `github-actions[bot]`，head 为 `7afb4fbb521ca82da18df8272412ea4a00771a5f`。显式派发的 [Quality 38668404264](https://github.com/Wang-Shuo/chronolog/actions/runs/38668404264) 成功；PR 自动检查最初为 `action_required`，经允许只读工作流执行后，[Quality 38668405719](https://github.com/Wang-Shuo/chronolog/actions/runs/38668405719) 成功，`gh pr checks --required` 返回通过。允许工作流执行不是批准 PR 内容。

证据：[质量报告](m3-evidence/live-generation-38668187171/generation/quality.json)、[发布结果](m3-evidence/live-generation-38668187171/publication/rolling-pr.json)、[运行步骤](m3-evidence/live-generation-38668187171/run.json)、[PR 状态](m3-evidence/live-generation-38668187171/pr.json)、[归档清单](m3-evidence/live-generation-38668187171/archive.json)。

## 新内容审核摘要

本批新增 18 个文件：3 篇 Release、9 张活动 Change 卡片、6 条待审候选。发布记录包括 Claude Code `v2.1.299`、`v2.1.300` 和 Cursor `Origin App Marketplace`。另修改 884 个文件，没有删除或废弃记录。待审主题候选总数为 149。

对 817 个修改的 ChatGPT Release/Change 文件逐一比较，排除派生 machine_hash 并归一化来源锚点后，其余内容一致：这些文件的变化来自证据链接从原段落锚点变为官方更新日志页地址。样例为 2022-12-15 Conversation history 卡片，正文事实未变，链接定位精度有所变化。需要结合完整 diff 审核，不能把全部 884 项修改一概视为时间戳更新。

### 实际发现：API 名称标题显示

新增 Claude Code 卡片的来源 API 为 `$.prompt.media` 和 `$.ui.view`，生成标题却显示为 `USD .prompt.media` 和 `USD .ui.view`。`_scripts/writer.py` 的 `wiki_label` 将所有 `$` 替换为 `USD `，适用于金额的替换也影响了技术标识符。这是现有渲染规则在新内容中的可见问题；工程检查通过不代表语义或标题已经人工批准。

后续实现已修正通用标签规则，并加入 wiki 链接和标题回归验证；使用本次原始采集数据回放，将代码、重生成内容与验收文档一起提交新的交付 PR，审核最终 head。见[修复验收](m3-dollar-title-fix-2026-10-15.md)。

## 后续

- PR #5 已按用户最终 head 批准合并、部署并通过公开校验，C2 完成。上述标题问题的后续修复待本次交付 PR 批准发布。
- 快照有效期截至北京时间 **2026-10-16 11:26:11**；若之后 HTTP 仍被阻止，需要新的真实快照。
- C1 的七次真实连续 schedule、C3 恢复演练、C5 独立交接仍待完成。保留本次手动运行证据，但不把它算作日常 schedule。
