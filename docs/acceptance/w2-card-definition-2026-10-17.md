# W2 PR 1 验收记录：卡片定义（设计评审 P3）— 2026-10-17

**范围：** [设计评审](../design-review-2026-10-15.md) P3 与附录 C 的方案 B（含 B+ 关键词试点）：按公告结构成卡、扁平列表按主题聚合为摘要卡、取消每 Release 5 张上限、新增 `kind` 与 `scope` 字段、黄金样本改为按 Release 与原文定位。本记录只覆盖工程验收；**卡片集合发生变化，合并前必须完成 M2 B4 口径的人工判定**（60 张样本至少 55 张通过），复核包见 [review-packet-cards.md](w2-evidence/review-packet-cards.md)。

- 代码基线：`main` / `59cff60`。交付分支 `codex/w2-card-definition-r2`。
- 执行日期与时区：2026-10-17，Asia/Shanghai。实施：Opus 5.5 子 agent（两轮）；工程验收：Claude Fable 5.1（受 Wang-Shuo 委托）；B4 判定与最终批准：Wang-Shuo。
- 输入：[运行 38668187171 的原始采集包](m3-evidence/live-generation-38668187171/generation/collection.json.gz)，`input_kind: replay`。
- 运行 ID：`w2-cards-20261017-r2`（应用）与 `w2-cards-20261017-r2-idem`（幂等复跑）。第一轮 `w2-cards-20261017` 的结果被第二轮在全新 worktree 中重新生成覆盖。

## 卡片定义（已写入复核包“判定口径”与 About 页）

- 有功能小标题的公告：一个小标题及其正文为一张卡，证据为该节全部段落。
- 平台 / 套餐小标题下的条目和前言中不超过 8 条的列表：每条一张卡，平台写入 `scope`。
- 前言或无小标题正文：连续同主题段落合并为一张卡；整个 Release 只得一张卡且标题有信息量时，卡片标题取 Release 标题。
- 列表模式（通用小标题下、GitHub Release）：逐条分类；无主题条目进入待审；高信号条目（`Introducing`、`Added /命令`、`now … by default`、`is now generally available`、`You can now`、`New:`、长句 `now available`）单独成卡；其余按主题聚合为每 Release 每主题一张摘要卡（`kind: digest`）。
- 前言中的上市 / 推送段落并入前一张有主题的卡；`Available in …` 一类纯可用性句子跳过。
- `card_id` 由产品、日期、Release 与全部证据 quote 拼接后哈希；单证据卡的 id 与原来相同。`extractor_version` 升为 `fallback-v5`，校验器对 v2–v4 保持首条 quote 的身份算法。

## 验收项与结果

| 项目 | 预期 | 实际 |
| --- | --- | --- |
| `pytest -q` | 全部通过 | 378 passed（基线 289） |
| 应用回放 | candidate-applied，0 冲突，0 DLQ | 见 [quality.json](w2-evidence/quality.json)：新增 2,067、修改 1,935、退役 927、删除 66（`_review` 迁入 resolved）；四项门禁 passed；[publication.json](w2-evidence/publication.json) 3,275 个活动页面；[vault-validation.json](w2-evidence/vault-validation.json) 0 errors |
| 幂等复跑 | no-change | 见 [idem/quality.json](w2-evidence/idem/quality.json) |
| 黄金样本 | ≥ 55 / 56（非 skip）按 (Release, quote) 定位且主题一致；4 个 skip 不出现在任何已发布卡 | 55 / 56；唯一不一致为 `cursor-2025-12-10-33f1a4`，其原文现位于以小标题定主题的功能卡 "Browser layout and style editor"（editor-experience） |
| 活动卡片 | 规模可解释 | 1,949 → 2,455（ChatGPT 485、Claude Code 1,199、Cursor 771）；摘要卡 581 张，内含 1,912 行；多证据非摘要卡 240；B+ 独立卡 52 |
| 候选行覆盖 | 高于 W1 | ChatGPT 74.5%、Claude Code 33.9%（W1 为 11%）、Cursor 68.1%；其余为跳过的修复 / 说明行与待审行 |
| v2.1.300 | 不再只有 3 条 | 11 张卡（5 张摘要含 17 行 + 6 张单卡）；页面显示 "Tracked 11 cards from 88 candidate lines; 6 lines pending review." |
| 碎片卡 | 评审列举的例子消失 | "Available in ChatGPT on mobile and web" 跳过；"Start bills monthly…" 并入前卡证据；dots 的推送段落并入 "ChatGPT introduces dots" |
| 资源内存误归类 | v2.1.69 的内存占用行不在 Memory 主题 | 已移至 "9 Reliability and Performance changes in v2.1.69"；共 13 行改派 |
| 标题质量 | 不低于 W1 | ≥ 78 字符 589（W1 876）；厂商口吻 19（W1 64）；最长 90 |
| 身份与路径 | 单证据卡 id 不变；旧卡退役而非删除 | 约 1,047 张原卡保留 id；superseded 341 → 1,257（退役 927，恢复 11 张 2023–2025 的 ChatGPT 旧卡） |

## 已知限制与后续

- 待审队列从 149 增至 662（Claude Code 463）：取消上限后无主题的列表条目全部进入待审。按设计评审 P9，建议下一步引入 `uncategorized` 保留主题，让这些条目以摘要形式进入 Release 页而不进入主题时间线；在此之前 Release 页以 "N lines pending review" 如实说明。
- 早期 ChatGPT 的引导句加列表（"Default: …"、"Turbo: …"）仍按条目各自成卡；Cursor Start 的计费说明合并到相邻卡而非主卡。
- `kind` 为关键词启发式：功能小标题默认 `launch`，"Improved Code Review" 一类改进型小节也会标为 launch；随 C6 词表修订一起细化。
- 摘要卡以主题聚合，是“最小知识单元”原则的例外，已在 About 页术语表说明。
- 产品页、主题页结构未变（P5 / P6 在后续 PR）。

## 结论

工程验收通过。**合并条件：** Wang-Shuo 按复核包完成 B4 判定（60 张中至少 55 张“主题正确、事件可独立理解、无明显重复”），并在 PR 中批准最终 head；判定结果与未通过样本记录到本文件后再合并部署。

## B4 判定与上线记录（2026-10-17 补记）

- Wang-Shuo 审阅复核包后于 2026-10-17 批准 PR #11 的最终 head `99826af`，未报告未通过样本，B+ 高信号规则保留；PR 合并为 `b5b62c1` 并部署。
- 本 PR（W2 PR 2）处理已知限制中的待审队列：无主题的列表条目改为按 Release 发布为 "Other changes" 摘要卡。
