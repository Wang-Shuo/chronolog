# ChatGPT 官方浏览器快照交付 — 2026-10-23

本次从官方 [ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) 获取完整浏览器渲染 HTML，恢复 HTTP 访问受阻时的备用输入。快照交付与新内容审核分别进行；合并本快照不表示新内容已发布。

## 输入与完整性核验

- 实际获取时间：`2026-10-23T12:07:22.643Z`，即 **2026-10-23 20:07:22.643 Asia/Shanghai**。
- 获取方式：读取浏览器 `document.documentElement.outerHTML`，按 100,000 字符分块导出，共 10 块，合并后补 HTML doctype。
- 浏览器 DOM 与导出内容均为 907,918 字符；加 doctype 后文件为 907,934 字符、910,690 bytes。未包含工具截断标记，HTML 结束标签完整。
- 原始 HTML SHA-256：`e67d5b8105942a9134c55044491e169eae2323a47b4f6aa24416f1e41e58ff9e`。
- 使用现有解析器获得 **298 条 ChatGPT Release**，覆盖 **2022-12-15 至 2026-10-20**。
- 对比 2026-10-14 快照：旧 292 个 Release ID 全部保留，缺失 **0**；同 ID 的旧正文变化 **0**；新增 **6** 条。
- 浏览器辅助功能视图曾只显示到 2026-05-28，这是工具输出截断；完整 DOM 与解析结果保留了 2022 年起的历史。
- 交接包：`_inputs/chatgpt/chatgpt.html.gz` 与 `_inputs/chatgpt/capture.json`。
- 36 小时有效期截至 **2026-10-25 08:07:22.643 Asia/Shanghai**。以任务实际读取时刻为准；本包可覆盖 10 月 24 日 09:15 调度，但不能覆盖 10 月 25 日 09:15 调度。

### 新增记录

| 日期 | 官方标题 |
| --- | --- |
| 2026-10-15 | Applications for the Rosalind Academic Plan |
| 2026-10-15 | GPT-Live-1.1 and new voices in ChatGPT |
| 2026-10-15 | Site limits (Plus and Pro) |
| 2026-10-16 | Create and collaborate on slides in ChatGPT |
| 2026-10-16 | Updates to GPT-6 Pro model in ChatGPT |
| 2026-10-20 | Introducing locked chats |

### 来源链接变化与限制

287 条旧 Release 的唯一输入变化是 `source_url` 增加了此次浏览器 DOM 中的章节锚点；其余 5 条全字段不变。后续候选可能因此包含较多来源链接变更，这不代表旧正文改写。

官方 DOM 中有 23 个重复的 heading ID，例如 `updates-to-chatgpt`、`gpt-55-instant-update`。这些锚点可能定位到同名章节的首次出现处，不能单独作为发布日期的证明；审核时仍需结合 Release 日期、标题和引文。原始快照保留浏览器实际内容，未人为修改锚点。

## 隔离预检

- 运行：`snapshot-recovery-20261023-preflight`，代码基线 `c67c6f6e`；`input_kind: live`。ChatGPT 使用本次浏览器快照，Claude Code 与 Cursor 于 2026-10-23 实时 HTTP 采集。
- `load_bundle` 的来源、类型、获取时间、36 小时有效期、解压及 SHA-256 校验通过；三个来源均为 `success`。
- 采集：ChatGPT 298 条（最新 10-20）、Claude Code 252 条（最新 10-22）、Cursor 256 条（最新 10-16），共 806 条 Release。
- 结果：`ready`，`applied_files: 0`；新增 16 条 Release、69 张卡，退役 0、删除 0，待审 62 → 63；DLQ 0、冲突 0、`editorial_warnings` 为空。
- 458 项测试通过；Vault 4,862 个文件、69,742 个链接无错误；Quartz 构建及实际 HTML、搜索、图谱与 RSS 校验通过。候选含 3,573 个活动页面、2,689 张卡和 30 项 RSS。
- 证据：[质量报告](m3-evidence/snapshot-20261023-preflight/quality.json)、[测试日志](m3-evidence/snapshot-20261023-preflight/tests.log)、[发布集合](m3-evidence/snapshot-20261023-preflight/publication.json)、[新旧快照比较](m3-evidence/snapshot-20261023-preflight/snapshot-comparison.json)、[归档说明与来源](m3-evidence/snapshot-20261023-preflight/archive.json)、[证据摘要](m3-evidence/snapshot-20261023-preflight/evidence-sha256.json)。
- 这些是隔离预检结果，不计入 C1 的真实日常调度，不代表已通过内容人工审核或正式部署。
隔离预检不会直接更新正式 Vault，也不替代 GitHub 生成流程的实时采集及门禁。

### 候选内容复核边界

新增 Release 分布为 ChatGPT 6、Claude Code 9、Cursor 1；新增卡分布为 13、53、3。只读核验确认 69 张新卡的 148 条证据引文均出现在对应采集正文中，未发现新增事实捏造或历史退役；这不构成人工内容批准。

后续内容 PR 应复核两张仅含引导语的卡（Voice 帮助链接、GPT-6 Pro 列表前言）；Locked chats 的 `mobile-desktop` 分类、Claude 运行内存改善的 `memory` 分类、恢复会话用量警告的 `collaboration` 分类，以及 Cursor 性能改善的低置信度 `paradigm-shift`。Site limits 因 `no_match` 保留在待审，未发布为活动卡。这些提取与分类问题不通过修改原始快照解决。

## 交付与运行

将快照包通过独立 PR 交付；完成 Quality 并保留对最终 head 的人工批准后合并至 `main`，再从 `main` 手动运行 Generate review candidate。生成任务先尝试官方 HTTP；受阻时使用有效快照，并在报告保留 `browser-snapshot` 获取方式、真实获取时间和原 HTTP 错误。

检查实际运行报告中的三来源状态、覆盖范围和内容变化；候选通过门禁后进入 Rolling PR，仍需审核最终内容 head，完成批准、合并与部署，再验证公开站点提交。任何阶段失败应报告具体阶段及原因，不能记为无更新或已发布。

后续按[运维手册](../m3-operations.md#3-chatgpt-http-403-与人工快照)的每日快照交接维护。若审核或执行延迟超过有效期，重新访问官方页面获取新快照；不得只修改旧 `captured_at` 来延长有效期。
