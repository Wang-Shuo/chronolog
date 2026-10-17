# W2 PR 3 验收记录：主题页、月度归档与节奏面板 — 2026-10-17

**范围：** [设计评审](../design-review-2026-10-15.md) P5 / U5 / U6（主题页 Key moments 分道表、折叠的范围声明、按年月分组的全量时间线）、P2（月度归档页）、P7（产品发布节奏面板与常驻沉默状态）。交付分支 `codex/w2-theme-pages`，叠加在 W2 PR 2（`codex/w2-uncategorized`）之上。

- 代码基线：`codex/w2-uncategorized` / `2ccc934`（main `b5b62c1` + PR 2）。
- 执行日期与时区：2026-10-17，Asia/Shanghai。实施：Opus 5.5 子 agent（两轮）；验收：Claude Fable 5.1（受 Wang-Shuo 委托）；最终人工批准：Wang-Shuo。
- 输入：[运行 38668187171 的原始采集包](m3-evidence/live-generation-38668187171/generation/collection.json.gz)，`input_kind: replay`。
- 运行 ID：`w2-pages-20261017-r2`（应用）与 `w2-pages-20261017-r2-idem`（幂等复跑）；第一轮 `w2-pages-20261017` 的产物已被第二轮覆盖。

## 变更内容

- **主题页。** 新骨架：头部（显示名、计数、覆盖区间、按 `verbosity_baseline` 的粒度说明）→ Research summary → Key moments（按季度 × 产品的表格）→ 折叠的 "How to read this timeline" callout → Timeline（按年分组并计数，年内按月分组，产品名加粗，仅 Launch / Pricing / Policy / Digest 显示 kind）。旧骨架通过 `SKELETON_HEADINGS["theme"]` 迁移，渲染幂等。
- **Key moments 选取。** `editorial.yaml` 可配置 `key_moments: {theme: [card_id, …]}`（未知 id 记入 manifest 的 `editorial_warnings`，不阻塞）；未配置时自动选取：仅 `launch` 卡与独立公告卡（B+），每 Release 一张，每产品按季度分散优先、上限 12，总上限 30；摘要卡、修复卡与 Other changes 永不入选；表格标注 "Auto-selected"。影响等级不参与排序（评审 P4）。
- **月度归档。** 新目录 `Archive/`：每个有活动卡的月份一页（`Archive/2026-10.md`，按产品列出当月卡片，附上一月 / 下一月 / 全部月份链接）与文件夹页 `Archive/index.md`（按年列出各月及三产品计数）。`Archive` 加入 `VAULT_DIRECTORIES`、发布范围允许列表、质量报告分类与发布审计；空月份在暂存库中删除并由事务移除；首页 Latest changes 末尾链接 Archive。新增 `_scripts/folder_content.tsx` 避免 Quartz 在文件夹页重复列出月份。
- **节奏面板。** `silence_monitor.cadence_summary`：以不晚于执行日的最新归档发布日为锚（与时钟无关，保证跨日幂等），给出最近一次发布距锚日天数、近 90 天发布数、近 12 个月逐月计数（文本条形）、基线（监控窗口内每整月平均发布数）与状态 normal / quiet / silent / not-tracked；告警逻辑不变。产品页在 Research summary 之后插入 `## Release cadence` 区域（产品骨架未迁移，按既有插入规则加入）；首页产品行追加 "cadence: normal"；About 方法说明补一句。
- 文档：`docs/m3-operations.md` 第 2 节增加归档、节奏锚点与 `key_moments` 三条说明。

## 验收项与结果

| 项目 | 预期 | 实际 |
| --- | --- | --- |
| `pytest -q` | 全部通过 | 432 passed（PR 2 基线 409） |
| 应用回放 | candidate-applied，0 冲突，0 DLQ | 第一轮新增 48（47 个月份页 + 归档索引）、修改 30；第二轮（选取规则修订）修改 24；四项门禁 passed；见 [quality.json](w2-evidence/pages/quality.json)、[publication.json](w2-evidence/pages/publication.json)：3,488 个活动页面、47 个归档月份 |
| 幂等复跑 | no-change | 见 [idem/quality.json](w2-evidence/pages/idem/quality.json)；另在副本上以 `today=2026-11-20` 运行亦为 no-change（节奏锚点与时钟无关） |
| 主题页 | Key moments 不含 "Improved / Removed" 类条目；时间线按年月分组；声明折叠 | agent-mode 19 个节点（Cursor 12、Claude Code 5、ChatGPT 2）覆盖 2025 Q1–2026 Q4；构建产物中 callout 为 `is-collapsed`；25 个主题页全部迁移，0 待人工迁移 |
| 归档 | 每个有卡月份一页，首页可达 | 47 个月份页，`Archive/index` 按年列出；发布审计校验月份计数与链接 |
| 节奏面板 | 三个产品页均有近 12 月计数与状态 | ChatGPT 基线 6.2 / 月、近 90 天 69 次；Claude Code 基线 23.1、74 次（2025-11 标 "not archived"）；Cursor 基线 5.9、14 次；状态均 normal |
| 卡片与 Release | 不变 | Changes / Releases 0 变化 |

## 已知限制

- 自动精选在 9 个主题下少于 5 个节点（accessibility-localization、artifact-creation 为 0），需要策展或词表修订；agent-mode 未选中 2025-05 的 "Background Agent (Preview)"（同季度有更新的 launch 卡），应通过 `editorial.yaml` 的 `key_moments` 策展，属于 W2 P6 / C5 的内容工作。
- pricing-model 的自动精选含三条近似的 "ChatGPT Go now available in …" 条目（不同 Release）。
- `operations.code_snapshot` 不哈希 `.tsx` 文件（`feed.tsx`、`site_title.tsx`、`folder_content.tsx` 不在 `code_sha256` 内），属既有限制。
- 产品页骨架仍未迁移（P6）。

## 结论

工程验收通过。待 PR 2 合并后 rebase 到 main 开交付 PR；待 Wang-Shuo 批准最终 head、`quality` 通过后合并部署。
