# M3 临时凭据首次运行记录 — 2026-10-14

**PR #3 已审核合并并成功部署。临时凭据准备通过；首次真实采集因 ChatGPT 自动访问被阻止且缺少快照而失败，发布任务按门禁跳过。**

本记录及下载证据在部署后补充，随本次 ChatGPT 快照交付 PR 提交审阅；远端原始记录见以下 Actions 链接。

## 审核与部署

- Wang-Shuo 于 `2026-10-14T15:15:10Z` 批准最终 head `83022285c5c103db8e4097ee699f259056aa1954`，必需的 `quality` 成功。
- [PR #3](https://github.com/Wang-Shuo/chronolog/pull/3) 于 `2026-10-14T15:16:32Z` 合并为 `11f68b4d364b05a6281bd4cb3bb5289a01363f3c`。未绕过保护规则。
- [Deploy reviewed site 38587897153](https://github.com/Wang-Shuo/chronolog/actions/runs/38587897153) 成功。部署重新验证人工批准及 160 项测试、Vault、构建、发布集合与 RSS；[审核门禁](m3-evidence/ephemeral-runtime-20261014/deployment/review-gate.json)、[测试日志](m3-evidence/ephemeral-runtime-20261014/deployment/deploy/tests.log)。
- [公开校验](m3-evidence/ephemeral-runtime-20261014/public-check/public-verification.json) 确认线上 commit 为 `11f68b4`，2,756 个活动页面、30 项 RSS。站点为 [ChronoLog](https://wang-shuo.github.io/chronolog/)。

## 首次真实采集

[Generate review candidate 38587902325](https://github.com/Wang-Shuo/chronolog/actions/runs/38587902325) 使用 `main` 的真实来源输入；事件为手动 `workflow_dispatch`，不计作 C1 的每日 schedule。

| 环节/来源 | 实际结果 |
| --- | --- |
| 临时凭据与分支准备 | 成功，无需长期 bot secret |
| Claude Code | HTTP 成功，242 条，覆盖至 2026-10-14 |
| Cursor | HTTP 成功，255 条，覆盖至 2026-10-13 |
| ChatGPT | 官方 Help Center 阻止自动访问；`_inputs/chatgpt/capture.json` 不存在，备用快照不可用 |
| 整批门禁 | 失败；未打包或推送新候选，独立 `publish` 任务 skipped |

证据：[来源和质量报告](m3-evidence/ephemeral-runtime-20261014/generation/operations/quality.json)、[运行步骤](m3-evidence/ephemeral-runtime-20261014/generation-run.json)、[原始采集输入](m3-evidence/ephemeral-runtime-20261014/generation/operations/collection.json.gz)。成功采集的来源不会掩盖 ChatGPT 的失败，也未把已有站点数据误报为本批更新。

## 后续验收

临时凭据已随已合并工作流启用，每日 09:15 Asia/Shanghai 的调度保留。下一步按[运行手册](../m3-operations.md#3-chatgpt-http-403-与人工快照)补充具有真实获取时间、SHA-256 且未超过 36 小时的官方浏览器快照，经审核进入默认分支，再从 `main` 启动完整生成运行。

实际 daily `publish` 推送、Rolling PR、自动 Quality 与新内容审核部署仍需成功采集后验证。七次真实 schedule、故障恢复和独立交接未完成，M3 不标记为完成。不要重标旧快照时间，也不要为通过本次验收跳过失败来源。
