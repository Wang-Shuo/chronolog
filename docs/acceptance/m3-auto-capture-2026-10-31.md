# 自动采集与单源故障隔离 — 2026-10-31

## 交付行为

日常采集先尝试官方 HTTP，ChatGPT 失败后启动普通 Chromium 浏览器，在 GitHub Ubuntu runner 上使用 Xvfb。完整 DOM 两次解析一致、旧 Release ID 无缺失时，自动生成带实际时间和 SHA-256 的快照，并立即消费。原文和诊断随 generation artifact 保留 90 天，不再依赖 `_inputs/chatgpt` 的每日快照 PR。人工内容批准和部署门禁保留。

日常任务显式启用 `--allow-partial`。失败来源必须有历史基线，其 Release、卡片事实和待审项全部保留，不参与对账删除；产品页、首页和 About 提示采集延迟，停止对此来源推断发布沉默。其他完整成功来源继续更新。全源失败、无基线、不完整成功输入和内容/构建失败仍拒绝应用候选。未启用该参数的命令保持严格整批门禁。

新增 `preview` 手动输入可在实现分支进行只读真实预演：跳过滚动分支准备、`--apply`、候选打包和发布任务。正式定时发布仍仅允许默认分支。采集、测试和构建任务只有仓库读取权限；有写权限的发布任务不执行输入包中的代码。

## 本地真实验证

- 无界面 Chrome：官方页面 HTTP 403；等待结束后明确失败，没有生成可用快照。
- 普通 Chrome：官方页面 HTTP 200，实际获取于 `2026-10-31T02:13:47Z`（北京时间 10:13:47），解析到 304 条发布。原有 303 个 ID 全部保留，新增 10 月 30 日 Account switching on iOS and Android。
- 快照原文 SHA-256：`1f4a2e66a7d535514b7d70227d224a708aa72ddb3de7063c65e067d5cf61aa56`。
- 对比证据：[普通浏览器结果](m3-evidence/auto-capture-20261031/local-headed-capture.json)、[历史覆盖比较](m3-evidence/auto-capture-20261031/local-headed-comparison.json)、[无界面失败结果](m3-evidence/auto-capture-20261031/local-headless-capture.json)。浏览器类型、模式和网络环境会影响结果，单次本地成功不代表连续无人值守可靠性。

另运行了完整的真实降级流程 `auto-recovery-live-20261031`：ChatGPT HTTP 和无界面浏览器都失败，Claude Code / Cursor 均成功，各 257 条发布。

- 候选 817 条 Release、2,750 张卡片、3,645 个活动页面；新增 10 个文件、修改 23 个，删除和退役均为 0。
- ChatGPT 的 **303 条 Release、507 张卡片记录、38 个待审记录**与原 Vault 完全一致，前后规范化记录摘要相同，见[保留证明](m3-evidence/auto-capture-20261031/history-preservation.json)。导航可随其他产品更新，事实与人工备注保留。
- 471 项测试、Vault 链接、Quartz、120,162 条 HTML 链接检查、搜索集合/图谱和 30 项 RSS 审计全部通过，状态为 `ready`、`collection_health: degraded`。
- 构建后的首页、ChatGPT 产品页和 About 均包含采集延迟提示。候选保持隔离，没有写回或部署这些新内容。
- 证据：[质量报告](m3-evidence/auto-capture-20261031/local-degraded-quality.json)、[摘要](m3-evidence/auto-capture-20261031/local-degraded-quality.md)、[发布审计](m3-evidence/auto-capture-20261031/local-degraded-publication.json)。本地运行发生在实现提交前，报告中的 commit 是当时基线；实际执行源码摘要在报告的 `code_sha256` 中。

回归覆盖还包括：重复故障不产生页面变化、来源恢复清除延迟状态、失败来源待审项与人工文字保留、全源失败/缺少基线停止、部分模式仍拒绝重复 ID/混入失败来源数据/不完整输入、空白或截断页面不成为快照，以及预演不会进入发布任务。接入普通浏览器环境变量和预演分支后，相关 43 项测试通过；最终提交的全部检查见 PR Quality。

## GitHub 验证与验收边界

[只读真实预演 41159532798](https://github.com/Wang-Shuo/chronolog/actions/runs/41159532798) 使用实现提交 `d1bfd139`。查看其中 `generation-41159532798-1` artifact 的 `quality.json`、`browser/browser-capture.json` 和原文 bundle，可分别判断工程门禁与来源采集状态；不能只凭 workflow 绿色就宣称三个来源均健康。

本交付之后的日常采集不需要单独快照审批，但新内容仍须审核。现有 `_inputs/chatgpt` 仅保留为旧交付记录，不再被日常工作流自动读取。七次连续真实日常运行、长期浏览器稳定性与交接验收仍需累积，单次预演不计作完成。
