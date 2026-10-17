# W2 PR 4 验收记录：产品页重构、研究摘要、Eras 与写作指南 — 2026-10-17

**范围：** [设计评审](../design-review-2026-10-15.md) P6（产品页瘦身与骨架迁移）、C5（五个主题研究摘要、Cursor 与 Claude Code 的 Eras）、C3 / C4（写作指南、叙事改为肯定句加单一范围声明）、P5 的人工策展 Key moments（agent-mode、pricing-model）。交付分支 `codex/w2-narratives`，叠加在 W2 PR 3 之上。本记录只覆盖工程验收；**叙事内容需按 M2 B6 口径人工判定**（发生了什么转折、证据在哪里、哪些结论仍不确定），复核包见 [review-packet-narratives.md](w2-evidence/review-packet-narratives.md)。

- 代码基线：`codex/w2-theme-pages` / `32d1446`。
- 执行日期与时区：2026-10-17，Asia/Shanghai。实施：Opus 5.5 子 agent；工程验收与事实抽查：Claude Fable 5.1（受 Wang-Shuo 委托）；B6 判定与最终批准：Wang-Shuo。
- 输入：[运行 38668187171 的原始采集包](m3-evidence/live-generation-38668187171/generation/collection.json.gz)，`input_kind: replay`。
- 运行 ID：`w2-narratives-20261017`（应用）与 `w2-narratives-20261017-idem`（幂等复跑）。

## 变更内容

- **产品页。** 新骨架：头部（定位语、发布数、区间、About 链接）→ Release cadence → Eras（叙事段 + 各阶段摘要与代表 Release，末尾一句 Scope）→ Themes（前 8 个主题的计数条，Other changes 列最后）→ Recent releases（最近 10 次）→ Coverage → 折叠的 Release archive 与 All tracked changes callout。旧骨架通过 `SKELETON_HEADINGS["product"]` 迁移，渲染幂等；`description` 取定位语。`INSERTED_SECTIONS` 插入机制随产品迁移移除。
- **编辑内容（`_scripts/editorial.yaml`）。** 三个产品的 `positioning`；Cursor 5 个 Eras（2023-03 → 现在）与 Claude Code 3 个 Eras（2025-12-19 → 现在），每个阶段引用真实 `release_id`；新增 `model-support`、`apps-integrations`、`context-window`、`memory`、`safety-privacy` 研究摘要；`agent-mode`、`pricing-model` 摘要与 ChatGPT Eras 改为肯定句、单一范围声明，引用不变并补档案链接；`key_moments` 人工策展 agent-mode 14 张、pricing-model 13 张。
- **管线。** 引用了本次运行不存在的 Release 的主题摘要会被隐藏并记入 `editorial_warnings`（与 Eras 一致）。
- **文档。** `docs/style-guide.md`（写作指南，含 B6 复核清单）；`docs/m3-operations.md` 链接。
- **测试。** 新增 `tests/test_editorial.py`（叙事结构、引用存在、定位语长度、Eras 连续、Key moments 有效且跨产品跨年份）；M2 的 Era 证据测试扩展到三个产品。

## 验收项与结果

| 项目 | 预期 | 实际 |
| --- | --- | --- |
| `pytest -q` | 全部通过 | 458 passed（PR 3 基线 432） |
| 应用回放 | candidate-applied，0 冲突，0 DLQ，`editorial_warnings` 为空 | 修改 10（Products 3、Themes 7），其余 0；四项门禁 passed；见 [quality.json](w2-evidence/narratives/quality.json)、[publication.json](w2-evidence/narratives/publication.json) |
| 幂等复跑 | no-change | 见 [idem/quality.json](w2-evidence/narratives/idem/quality.json) |
| 产品页迁移 | 3 / 3，0 待人工迁移；两个 callout 折叠 | 符合 |
| 事实抽查（验收人） | 叙事中的具体主张能在采集原文中找到 | 抽查 10 处（VSCodium 分叉、Copilot++、GPT-5 默认与 Auto/Fast/Thinking、GPT-4o 退役、Sonnet 5 默认与 1M、Cursor Router、Opus 5.5、fallbackModel、Automations 触发源、Cursor SDK）全部在对应 Release 正文中找到 |
| 引用 | 每段至少一个官方链接与档案链接；全部 `[[Releases/…]]` 存在 | 测试覆盖 |

## 已知限制与待判定

- Claude Code 的 auto mode 在档案中没有"发布"条目（覆盖从 2025-12-19 起，首次出现已是既有功能），Era 边界取 v2.1.111（2026-04-16）；最后一个 "Mods" 阶段仅约两周。
- ChatGPT 在 agent-mode 下只有 4 张卡，摘要中的 ChatGPT 段证据较薄；Claude Code 的定价卡均为客户端计费展示，档案中没有订阅价格公告。
- 个别引用指向的 Release 其卡片归在其他主题（如 Cursor 0.45 的 MCP 支持在 reliability-performance），主张以 Release 正文为准。
- 叙事由模型起草：抽查未发现与原文不符的主张，但 B6 判定前不应视为已验收内容。

## 结论

工程验收通过。**合并条件：** Wang-Shuo 按复核包完成 B6 判定（7 个主题摘要、3 个产品的定位与 Eras、2 个主题的 Key moments），未通过项修订后再批准最终 head；按 PR 2 → PR 3 → PR 4 顺序合并部署。

## B6 判定与上线记录（2026-10-17 补记）

- Wang-Shuo 审阅叙事复核包后批准 [PR #15](https://github.com/Wang-Shuo/chronolog/pull/15) 的最终 head `43d3019`，未报告未通过项；PR 合并为 `d412bb3` 并部署。
- 已知限制保持不变；后续策展修订通过 `editorial.yaml` 与交付 PR 进行。

