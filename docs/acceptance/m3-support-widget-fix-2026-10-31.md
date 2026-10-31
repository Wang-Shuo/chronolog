# 首次正式采集与支持组件解析修复 — 2026-10-31

PR #22 的最终提交获人工批准后合并为 `de2c71f3`。[部署 41167226543](https://github.com/Wang-Shuo/chronolog/actions/runs/41167226543)成功，公开站点的提交、索引摘要与 RSS 已核验。新流程已在主分支启用。

[首次正式生成 41167236557](https://github.com/Wang-Shuo/chronolog/actions/runs/41167236557)自动完成三源采集、全部工程门禁和内容 PR #23 创建，无需人工快照交接。ChatGPT 使用普通 Chrome，于 `2026-10-31T04:08:55Z`（北京时间 12:08:55）自动获取官方页面，HTTP 200；Claude Code / Cursor 均通过 HTTP 获取，各 257 条发布。快照 SHA-256 为 `88daaa65ffd76032df107c9404230ff1d32063228e4bdbea14aef13c53620ede`。

## 实际发现与修复

内容核对发现，官网在 `<article>` 内、发布正文之后注入了 `ai-voice-help-contact` 支持组件。旧解析器把其 h2 标题“Need more help? Contact us…”继承到最后一个日期 2022-12-15，误生成一条 Release 和一个待审项。该记录只进入 PR #23，没有合并或部署。

解析器现在按该组件的 DOM class 跳过其整棵子树，不按“联系支持”等文本黑名单过滤正式公告。深度处理覆盖嵌套标签、无结束标签的 img/br 及自闭合 SVG 元素；组件后面的正式内容仍可正常解析。新增回归测试证明真实公告中的 Contact support 文本保留。

对同一份自动获取的原始 HTML 重解析：**305 → 304 条 ChatGPT 发布，仅移除支持组件伪记录，其余 304 条的所有字段完全一致**，见[解析比较](m3-evidence/support-widget-20261031/parser-comparison.json)。原文、真实获取时间和摘要没有修改，均归档在同一证据目录。

## 正确内容与验证

复用上述正式运行的原始输入，仅用修复后的解析器替换 ChatGPT 解析结果，在隔离 Vault 全量生成并通过全部门禁后写入本交付分支。该验证标识为 `input_kind: replay`，不声称是新的实时采集或连续日常运行。

- 两条真实新增 Release：ChatGPT 的 2026-10-30 Account switching on iOS and Android；Claude Code 的 2026-10-31 v2.1.316。
- 新增 10 张卡片；总计 **818 条 Release、2,751 张卡片、3,647 个活动页面**。待审维持 63 条，不含支持组件生成的伪待审项。
- 相对已发布主分支新增 12 个文件、修改 26 个，删除和退役均为 0。
- **473 项测试通过**；Vault 链接、Quartz 构建、HTML / 索引 / 图谱 / RSS 校验通过，RSS 30 项。
- [质量报告](m3-evidence/support-widget-20261031/quality.json)、[发布审计](m3-evidence/support-widget-20261031/publication.json)、[证据摘要](m3-evidence/support-widget-20261031/sha256.json)。源码以质量报告中的 `code_sha256` 为准，报告的 commit 是本地验证时的已发布基线。

本交付把解析修复和两条真实发布放在同一个待审 PR，替代含伪记录的 PR #23；#23 已转为草稿，待本交付合并后关闭。最终 head 的 Quality 和人工批准仍为合并条件。快照无需单独审批，日常自动生成流程保持不变。
