# W2 PR 2 验收记录：`uncategorized` 保留主题与 kind 微调 — 2026-10-17

**范围：** [设计评审](../design-review-2026-10-15.md) P9：无主题的列表条目不再滞留待审队列，而是按 Release 发布为 "Other changes" 摘要卡，不进入主题页、首页最新变化与跨产品关系；"Improved / Faster / Updated …" 类功能小节的 `kind` 改为 `change`；补记 PR #11 的 B4 判定。交付分支 `codex/w2-uncategorized`。

- 代码基线：`main` / `b5b62c1`。
- 执行日期与时区：2026-10-17，Asia/Shanghai。实施：Opus 5.5 子 agent；验收：Claude Fable 5.1（受 Wang-Shuo 委托）；最终人工批准：Wang-Shuo。
- 输入：[运行 38668187171 的原始采集包](m3-evidence/live-generation-38668187171/generation/collection.json.gz)，`input_kind: replay`。
- 运行 ID：`w2-holding-20261017`（应用）与 `w2-holding-20261017-idem`（幂等复跑）。

## 变更内容

- `_scripts/themes.yaml` 新增 `uncategorized`（显示名 Other changes，`status: holding`，无别名）；词表加载对 holding 主题不生成匹配词，审核决策不能指向 holding 主题。
- 提取：仅列表模式（通用小标题下、长前言列表、GitHub Release）中无主题的条目改派 `uncategorized`，按既有规则成卡（单条普通卡、B+ 独立卡、其余为 "N other changes in {版本}" 摘要卡）；散文段落、功能小节、短列表与平台条目无主题时仍进入待审。跳过规则补充 "版本: Bug fixes" 形式（3 行）。
- 校验：卡片主题接受 official ∪ holding。分析：`analyze_b` 忽略 holding 卡（无扩散、无关联）；`analyze_a` 的 `top_themes` 排除 holding。
- 页面：不生成 `Themes/uncategorized.md`；首页主题分组、主题计数与 "Latest changes" 排除 holding 卡；卡片头部显示纯文本 "Other changes"，nearby / relations 为空；Release 页把 holding 卡列在最后并标注 "· Other changes · Digest"，摘要句增加 "; N in Other changes"；About 的方法说明与术语表更新。
- `kind`：功能小节标题以 Improved / Improvement(s) / Improving / Better / Faster / Updated / Update(s) 开头时为 `change`（20 张活动卡由 launch 改为 change）。
- 文档：`w2-card-definition-2026-10-17.md` 补记 B4 判定与上线。

## 验收项与结果

| 项目 | 预期 | 实际 |
| --- | --- | --- |
| `pytest -q` | 全部通过 | 409 passed（基线 378） |
| 应用回放 | candidate-applied，0 冲突，0 DLQ | 见 [quality.json](w2-evidence/holding/quality.json)：新增 765（165 张卡 + 600 个 `_review/resolved`）、修改 1,465、退役 0、删除 600（队列迁入 resolved）；四项门禁 passed；[publication.json](w2-evidence/holding/publication.json) 3,440 个活动页面 |
| 幂等复跑 | no-change | 见 [idem/quality.json](w2-evidence/holding/idem/quality.json) |
| 待审队列 | 明显下降，剩余为非列表条目 | 662 → 62（ChatGPT 37、Claude Code 0、Cursor 25） |
| Other changes 卡 | 不进主题页 / 首页 | 165 张（105 摘要 + 60 单卡）共 597 行；`Themes/` 仍为 25 页；首页主题分组与 Latest changes 区域与上一版逐字节相同 |
| 活动卡片 | 仅新增 holding 卡 | 2,455 → 2,620，各产品有主题卡片数不变 |
| 黄金样本 | ≥ 55 / 56，4 个 skip 不发布 | 55 / 56；skip 样本均未进入 Other changes |
| v2.1.300 | 待审行进入 Release 页 | "Tracked 13 cards from 88 candidate lines."，新增 "Added /advisor on Claude Platform on AWS · Other changes" 与 "5 other changes in v2.1.300 · Other changes · Digest" |

## 已知限制

- Cursor 日期形式的 changelog slug（如 `04-08-26`）会被当作版本号 "04.08.26" 用于摘要卡标题（6 张）。
- 剩余 62 条待审主要是无主题的散文段落与功能小节，需要词表修订（C6）或人工决策。
- Other changes 摘要会收纳表述模糊的条目（如 "Bugbot's resolution rate is now 78%."），这是保留主题的设计目的；后续词表修订会逐步把它们派到正式主题。

## 结论

工程验收通过。待 Wang-Shuo 批准最终 head、`quality` 通过后合并部署。
