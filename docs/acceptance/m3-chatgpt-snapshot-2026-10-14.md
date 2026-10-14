# ChatGPT 官方浏览器快照交付 — 2026-10-14

用户提供 `~/Downloads/chatgpt-release-notes.html`，并声明真实获取时间为 `2026-10-14T23:26:11+0800`。本次交付补充日常采集所需的备用输入；合并快照本身不代表新内容已经采集、审核或发布。

## 输入核验

- HTML 标题：`ChatGPT release notes | OpenAI Help Center`。
- canonical URL：`https://help.openai.com/en/articles/6825453-chatgpt-release-notes`，与配置的官方来源一致。
- 原始 HTML 大小：809,694 bytes。
- 原始 HTML SHA-256：`9601c0d938715c586eecca02c102c585bc7c86d5d2fdb14a185bdc311e16c4c9`。
- 通过现有解析器获得 292 条 ChatGPT 更新，日期覆盖 `2022-12-15` 至 `2026-10-07`；与既有 ChatGPT 覆盖范围一致。
- 快照包为 `_inputs/chatgpt/capture.json` 和 `_inputs/chatgpt/chatgpt.html.gz`；已调用 `load_bundle` 校验来源、类型、时间、解压内容和摘要。
- 36 小时有效期截至 **2026-10-16 11:26:11 Asia/Shanghai**。以采集任务实际使用时刻判断是否过期；不得改写时间延长有效期。

## 本地完整预检

将本快照与真实采集运行 `38587902325` 中的 Claude Code/Cursor 输入组合，运行隔离生成预检，明确标为 `input_kind: replay`；未重新宣称这些输入是本地实时抓取，也不计为日常 schedule。

结果为 `ready`：160 项测试、Vault 校验、Quartz 构建及发布集合/RSS 检查均通过；DLQ 与冲突均为 0。隔离候选包含 2,764 个活动页面和 30 项 RSS；原站点 Vault 未应用这些变化。远端日常采集会重新获取来源并重新执行门禁。

证据：[质量报告](m3-evidence/snapshot-20261014-preflight/quality.json)、[测试日志](m3-evidence/snapshot-20261014-preflight/tests.log)、[发布集合](m3-evidence/snapshot-20261014-preflight/publication.json)。

## 交付范围与下一步

本 PR 包含快照、运行文档，以及 PR #3 合并后的实际部署/失败采集证据。没有把本地生成候选直接写入站点 Vault。

合并至 `main` 后，从默认分支启动 Generate review candidate：先尝试官方 HTTP，阻止访问时使用该快照；三个来源通过后执行内容门禁、滚动 PR 和自动 Quality。真实新增内容仍需要单独审核，不自动发布。

若审核或运行延迟到过期时间之后，需重新从官方页面保存 HTML 并提供真实获取时间。运行步骤见[运维手册](../m3-operations.md#3-chatgpt-http-403-与人工快照)。
