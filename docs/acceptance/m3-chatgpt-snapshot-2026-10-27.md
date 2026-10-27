# ChatGPT 官方浏览器快照交付 — 2026-10-27

## 恢复范围

10 月 25、26 日定时生成失败。26 日运行 [40278529698](https://github.com/Wang-Shuo/chronolog/actions/runs/40278529698) 的报告确认：ChatGPT 官方 HTTP 受阻，10 月 23 日快照过期；Claude Code 与 Cursor 采集成功。现有公开版本为 `5dff1a70`，内容更新 [PR #19](https://github.com/Wang-Shuo/chronolog/pull/19) 的 head `cb029850` 已通过 `quality`，仍待人工审核。

本交付更新备用输入并验证恢复候选。快照合并与内容发布是两个步骤，快照验收不代表批准生成内容；不修改采集、分类、36 小时有效期或审核门禁。

## 获取与完整性

- 来源：<https://help.openai.com/en/articles/6825453-chatgpt-release-notes>。
- 实际获取时间：`2026-10-27T02:32:46.149Z`，即北京时间 **10 月 27 日 10:32:46**。
- 有效期截至：北京时间 **10 月 28 日 22:32:46**；以任务实际读取时刻为准。
- 浏览器渲染 DOM 共 913,294 字符，分 10 个不超过 100,000 字符的块保存，拼接长度与 DOM 一致；结束标签完整，没有 `[Truncated]` 标记。
- 添加 doctype 后 HTML 为 916,070 bytes，SHA-256：`21c239abbe7fd28556c1622c2386b38ec2f6610b39841665165849d445ac4a0b`。
- 当前解析器得到 **300 条 Release**，覆盖 **2022-12-15 至 2026-10-26**。上一快照的 298 个 ID 全部保留，同 ID 字段变化为 0。
- 新增：2026-10-21 **MoMo payments in Vietnam**；2026-10-26 **GPT-6.1 Terra**。
- 交接包：`_inputs/chatgpt/chatgpt.html.gz`、`_inputs/chatgpt/capture.json`。

## 隔离预检

预检以 `5dff1a70` 为基线，在独立候选 Vault 中生成，不写回正式内容。第一次匿名 GitHub 请求遭遇 403 rate limit，失败产物保留在本地 `/tmp/chronolog-recovery-20261027-preflight`；没有推送候选。第二次使用已登录 GitHub CLI 的认证，仅在子进程环境中传给固定 GitHub API，请求不跟随认证重定向，凭据不写入报告。

带认证运行 `recovery-20261027-auth-preflight` 的三个来源均成功：ChatGPT 300 条（最新 10-26）、Claude Code 254 条（最新 10-26）、Cursor 257 条（最新 10-20），合计 811 条 Release。此次三个来源均为 **HTTP**；ChatGPT 在第一次预检需要备用快照，第二次 HTTP 恢复成功，因此第二次未消费快照。备用包另行通过 `load_bundle` 校验，不能把 HTTP 成功写成浏览器快照成功。

最终状态 **ready**，`applied_files: 0`；活动卡 2,717，较主分支新增 28 张；待审仍为 63 条。458 项测试、Vault 链接、Quartz 构建及实际 HTML / 搜索 / 图谱 / RSS 校验全部通过，没有退役或删除记录。差异为新增 33 个文件、修改 861 个文件；HTTP 与浏览器输入的章节锚点差异会引起历史来源链接更新，文件改动量不等于新事实数量。

新增 28 张卡的 60 条证据引文均可在对应采集正文中找到，此检查不代替语义审核。证据：[质量报告](m3-evidence/snapshot-20261027-preflight/quality.json)、[发布集合](m3-evidence/snapshot-20261027-preflight/publication.json)、[快照比较](m3-evidence/snapshot-20261027-preflight/snapshot-comparison.json)、[浏览器获取记录](m3-evidence/snapshot-20261027-preflight/browser-capture.json)、[证据引文核验](m3-evidence/snapshot-20261027-preflight/candidate-evidence-check.json)、[归档摘要](m3-evidence/snapshot-20261027-preflight/archive.json)。

后续生成仍通过滚动 PR #19 更新，保留该 PR 的已有内容和审核流程。最新候选包括其 v2.1.310 更新，以及 v2.1.311、Cursor Agent SDK 和两条 ChatGPT 公告。

### 内容复核提示

本次恢复沿用现有提取规则。内容审核应特别检查 MoMo 支付被分到 `mobile-desktop`、Claude Code 运行内存优化被分到 `memory`，以及 Cursor Agent SDK 末尾引导句单独成卡的问题。它们属于内容提取与分类改进，不通过修改原始快照掩盖。

## 后续交付

快照 PR 的最终 head 通过 Quality 并获人工批准后合并，再从 `main` 运行 Generate review candidate。核验三来源成功和最新内容 PR 的精确 head 检查，完成内容审核后部署，并对公共 `deployment.json` 验证提交。隔离预检不计入连续七次真实日常调度验收；过期后必须重新获取官方页面。
