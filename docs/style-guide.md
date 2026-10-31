# ChronoLog 写作指南

适用对象：维护 `_scripts/editorial.yaml` 的策展人与审核人。公开站点用英文写作（[设计评审](design-review-2026-10-15.md) C12），本指南用中文说明规则；英文示例原样引用。机器生成的标题与描述规则见 C1、C2，不在本文范围内。

## 1. 目的

策展文字（主题研究摘要、产品定位、Era、Key moments）回答三个问题（B6 口径）：**发生了什么转折、证据在哪里、哪些结论仍不确定。** 它是带引用的研究笔记，不是营销文案，也不是逐段辩护。

## 2. 口吻与时态（C3）

- 一律第三人称。不写 "we"、"our"、"you"；厂商原文的第一人称只出现在卡片的引用块中。
- 主题研究摘要用一般现在时陈述某次公告做了什么："The 2025-06-04 release expands access to …"。
- Era 摘要中界定边界的那一次公告用一般过去时："Composer arrived on 2024-07-13 as …"；描述这一阶段的特征可用现在时。
- 用肯定句陈述证据支持的事实，用 "introduces"、"adds"、"announces"、"rolls out to"、"describes" 等动词标明信息来自来源；不写 "seems"、"probably"。
- 标题与小标题不用厂商第一人称（不写 "We're introducing …"）。

## 3. 名称、日期、数字

- 产品名固定写法：**ChatGPT**、**Claude Code**、**Cursor**；所有格写作 "Cursor's"、"Claude Code's"。功能与模型名照来源原样写（"Background Agent"、"GPT-4o"、"Claude Opus 4.6"），代码标识符用反引号（`` `/effort` ``）。
- 日期一律 `YYYY-MM-DD`，即 changelog 的公告日期；不写 "Sep 10"、"last week" 或时间戳。
- 版本号照来源写（`v2.1.32`、`0.46`、`Cursor 1.0`）。Claude Code 的链接文字写成 "v2.1.32 on 2026-02-05"，让读者不点开也知道日期。
- 数字与货币照来源写：`$100/month`、`$0.10 per million tokens`、`256k tokens`、`₹649`；不换算、不四舍五入、不补全来源没写的税费或地区。

## 4. 如何引用

每一处事实陈述都要有两个链接，放在同一句里：

1. 官方来源：日期作链接文字，指向 changelog 条目（ChatGPT 用带锚点的 Help Center 地址，Cursor 用 `cursor.com/changelog/…`，Claude Code 用 GitHub release tag）。
2. 归档 Release 页：紧跟其后的 `([[Releases/<产品>/<release_id>|archived]])`。

示例：`Cursor's [2025-05-15 release](https://cursor.com/changelog/0-50) ([[Releases/Cursor/cursor-2025-05-15-0-50-…|archived]]) introduces Background Agent …`

- 先读归档卡片与 Release 原文，再写句子；句子不能超出原文。一个链接只支撑它所在的句子。
- 优先引用上线、扩展、政策与价格变化，不引用修复类条目。
- 主题摘要里引用的 Release 必须在本次运行的归档中；缺失时 pipeline 不显示该摘要并在 `manifest.json` 的 `editorial_warnings` 中列出。Era 的 `releases` 同理：缺一条，整个 Era 不显示。

## 5. 证据支持的结论与推断

| 可以写（证据支持） | 不要写（推断） |
| --- | --- |
| 某日某产品公告了某功能、面向哪些套餐或地区 | 该功能当天对所有用户可用 |
| 同一产品前后两次公告的关系（"expands access to the same agent"） | 一个产品跟随或影响了另一个产品 |
| 来源给出的数字（价格、上限、token 数） | 跨产品的能力、价格或质量比较 |
| "Claude Code's first archived mention is …" | "Claude Code launched X on …"（覆盖从 2025-12-19 开始） |
| 同名概念在各产品中分别指什么 | 同名即同一能力（"plugin"、"agent"、"memory"） |

拿不准时，把推断改写成对来源的描述（"described as …"），或放进范围句。

## 6. 唯一的范围句（C4）

- 每段主题摘要的最后一段以 `**Uncertainty and scope:**` 开头，且**只有一句话**（可以用分号连接）。所有限定——仅覆盖三个产品、Claude Code 覆盖起点 2025-12-19、公告日期不等于可用日期、同名不等于同能力、不构成扩散或因果结论——都集中在这里。
- 正文段落不写 "does not establish"、"not evidence that"、"cannot establish" 这类辩护句。
- 产品的 `limitations` 同样只写一句，渲染为 Eras 区末尾的 "Scope:"。

## 7. 摘要结构

主题研究摘要固定为：

1. `**Research question: …?**`——一句问题，也是页面 description。
2. 每个产品一段，以产品名开头，按时间顺序列 2–5 个带日期的证据点；没有可靠证据的产品不写段落，在范围句中说明。
3. 范围句。

产品条目：`positioning`（≤ 160 字符，一句话说明产品是什么、跟踪哪个官方来源，也是产品页 description）、`summary`（各 Era 的演进一句话）、`limitations`（一句）、`eras`（名称、`from`、`to`、摘要、最多 3 个代表 Release；相邻 Era 首尾相接，`from` 等于最早代表 Release 的日期，最后一个 `to: null`）。

## 8. 该改哪里

| 需求 | 位置 |
| --- | --- |
| 主题研究摘要、产品定位、Era | `_scripts/editorial.yaml` 的 `themes` / `products` |
| 主题页 Key moments | `editorial.yaml` 的 `key_moments: {主题: [card_id, …]}`；10–16 个，三产品与多个年份都要覆盖，选上线与政策/价格变化；id 必须是该主题的活动卡片 |
| 单张卡片的主题更正 | `backfill_review.yaml` 的审核决策（按卡片或条目的稳定 ID）。卡片 frontmatter 的 `human_overrides` 会被保留，但 writer 目前不读取它，标题与主题更正尚不生效（见[全面评审](review-2026-10-31.md)本月清单 ⑧） |
| 卡片页、主题页上的人工批注 | 机器区域之外的人工区域 |
| 生成页面的机器区域 | **不要手改**：`machine_hash` 会报冲突，下一次运行也会覆盖；改 `editorial.yaml` 或 writer |

## 9. 审核清单（B6 口径）

审核人逐条核对，并在复核包的 `判定：` 行写"通过"或"不通过：理由"：

- [ ] 研究问题清楚，正文回答的是这个问题。
- [ ] 每个产品段落写出了一个可识别的转折（发生了什么），而不是功能清单。
- [ ] 每个事实都有官方链接和归档 Release 链接，点开后原文支持该句（证据在哪里）。
- [ ] 日期、版本、价格与原文一致，日期为 `YYYY-MM-DD`。
- [ ] 第三人称、现在时、肯定句；无厂商第一人称。
- [ ] 正文没有辩护句；最后一段是唯一的范围句，写清了哪些结论仍不确定。
- [ ] 没有跨产品的跟随、影响或优劣结论。
- [ ] Key moments 是上线或政策/价格变化，覆盖三产品与多个年份。
- [ ] 回放后 `editorial_warnings` 为空。
