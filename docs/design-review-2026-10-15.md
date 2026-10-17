# ChronoLog 产品、UI 与内容设计评审

**评审日期：2026-10-15（Asia/Shanghai）**
**代码基线：`main` / `5280419`**
**线上基线：<https://wang-shuo.github.io/chronolog/>（部署自 PR #5 / #6）**
**状态（更新于 2026-10-16）：W1 已全部上线：[PR #7](https://github.com/Wang-Shuo/chronolog/pull/7) 标题生成、[PR #8](https://github.com/Wang-Shuo/chronolog/pull/8) 页面模板、[PR #9](https://github.com/Wang-Shuo/chronolog/pull/9) 站点布局、首页与 About 页；验收记录见 `acceptance/w1-*.md`。W1 未做：og-image 与站点图标替换、浏览器与移动端截图。W2 P3 已按附录 C 的方案 B（含 B+ 试点）上线（[PR #11](https://github.com/Wang-Shuo/chronolog/pull/11)，`acceptance/w2-card-definition-2026-10-17.md`）；P9 的 `uncategorized` 保留主题见 `acceptance/w2-uncategorized-2026-10-17.md`。实施顺序见第 6 节；与 [开发与验收计划](development-plan-2026-10-13.md) 的衔接见第 7 节。**

本文承接 M1–M3 的工程验收，只评审"读者看到的产品"：信息架构、页面模板、文案与分类质量。管线可靠性、CI 与部署门禁不在本文范围内，已在 M1/M3 记录中覆盖。

## 0. 结论摘要

工程链路（采集、合并、事务发布、审核门禁）可靠且可审计，但站点目前读起来是"管线输出的目录"，不是 [PRD](chronolog-prd.md) 定义的"面向研究者的主题演化档案"。PRD 第 7 章的 L1 信号层、弱信号观察站、主题页对比时间线，以及第 10 章的首页模板，在线上都还没有对应形态。

最影响读者价值的五个问题，按严重程度排列：

1. **卡片标题被硬截断。** 1,949 张活动卡中 1,348 张（69%）标题在第 80 个字符处切断，92% 的标题不以句末标点结束。截断标题同时出现在首页、主题时间线、产品页、Release 页、RSS 条目、浏览器标签和 OG 分享卡上，是读者接触最多的文本。
2. **每次 Release 最多提取 5 张卡，档案实际上是抽样。** Claude Code 有 6,948 条候选变更行，入档 784 张（11%）；69% 的 Claude Code Release 候选行超过 5 条。线上最新的 v2.1.300 在 GitHub 上有 102 条变更，ChronoLog 收录 3 条。站点任何位置都没有说明这一采样规则。
3. **主题页承诺的"跨产品对比"是一张 190 行的扁平列表。** `agent-mode` 页 2026 年一节约 140 行，Claude Code 因变更日志写得细而占据多数；没有按产品分道、没有精选节点、没有筛选。`verbosity_baseline` 已计算但未用于任何展示。
4. **首页与卡片页把运维信息放在读者第一视野。** 首页第一屏是"Official browser snapshot captured: 2026-10-14T23:26:11+0800. Imported snapshot; this is not a successful automatic HTTP fetch."；卡片页有"Lag Days: 1162"、"Role: later-observed"、空的"Editor Notes"标题。读者需要的"最近发生了什么"在任何页面上都没有。
5. **策展覆盖面太窄，差异化能力不可见。** 25 个主题只有 2 个有研究摘要；3 个产品只有 ChatGPT 有阶段叙事；沉默检测的 `Alerts/` 为空且页面上没有节奏信息；`evolves_from` 在全部 1,949 张卡上都是空的。

建议分三波推进：W1 只改 `writer.py`、`quartz.layout.ts` 和首页人类区域，一到两个 PR 可完成；W2 做内容策展与模板重构；W3 才进入 PRD Phase 3 的信号层、弱信号站和交互时间线。第 6 节给出逐项清单。

## 1. 评审范围与方法

| 项目 | 做法 |
| --- | --- |
| 线上站点 | 抓取首页、`Themes/agent-mode`、一张 Cursor 卡片页、`index.xml`，核对渲染后的标题、区块顺序、侧栏组件和 RSS 条目 |
| Vault 内容 | 读取 `index.md`、3 个产品页、`agent-mode` / `pricing-model` 主题页、3 张卡片、2 个 Release 页、1 条 `_review` 草稿；对 1,949 张活动卡做统计（口径见附录 A） |
| 生成逻辑 | `_scripts/extract.py`（切行、主题、影响等级、5 张上限）、`_scripts/writer.py`（各页面模板与区域合并）、`_scripts/editorial.yaml`、`_scripts/themes.yaml` |
| 发布层 | `quartz.config.ts`、`quartz.layout.ts`、`quartz/styles/custom.scss`、`_scripts/publication_filter.ts` |
| 需求基线 | PRD 第 1–3、5.1、7、8、10、12 章；开发计划 M2.7、M3 后续待排项 |

未做的事项：没有在真实浏览器中截图或做移动端实测；没有用户访谈；配色对比度为按 WCAG 公式计算，不是视觉评估。涉及这些方面的建议已标注"待实测"。

## 2. 现状快照

以下数字来自本机 `main` 工作区，与首页 Overview 一致（活动集合，不含 fixture、superseded 与待审）。

| 指标 | 数值 |
| --- | ---: |
| 活动 Change Card | 1,949（ChatGPT 541 / Claude Code 784 / Cursor 624） |
| 活动 Release | 790（ChatGPT 292 / Claude Code 243 / Cursor 255） |
| 没有任何卡片的 Release | 111（ChatGPT 7 / Claude Code 50 / Cursor 54） |
| 标题长度 ≥ 78 字符（截断） | 1,348（69%） |
| 标题不以句末标点结束 | 1,796（92%） |
| 影响等级 | incremental 1,399 / significant 384 / paradigm-shift 166 |
| `ai_generated: true` 且 `confidence: low` | 550（与 significant + paradigm-shift 完全重合） |
| `evolves_from` 非空 | 0 |
| description 原样包含 evidence quote | 1,949（100%） |
| 主题数 / 有研究摘要的主题 | 25 / 2 |
| 产品数 / 有阶段叙事的产品 | 3 / 1 |
| 待审主题候选（`_review/`） | 149 |
| `Alerts/` | 空 |
| 本地 superseded 卡片文件（不发布） | 341 |

候选变更行与入档卡片的关系（候选行按 `split_release_lines` 口径，入档前还会经过跳过规则和每 Release 5 张上限）：

| 产品 | Release | 候选行 | 候选行中位数 / P90 / 最大 | 候选行 > 5 的 Release | 入档卡 | 入档比例 |
| --- | ---: | ---: | --- | ---: | ---: | ---: |
| Claude Code | 243 | 6,948 | 20 / 68 / 190 | 167（69%） | 784 | 11% |
| Cursor | 255 | 1,807 | 3 / 22 / 70 | 88（35%） | 624 | 35% |
| ChatGPT | 292 | 813 | 1 / 6 / 20 | 31（11%） | 541 | 67% |

主题分布（活动卡）：

| 主题 | ChatGPT | Claude Code | Cursor | 合计 |
| --- | ---: | ---: | ---: | ---: |
| apps-integrations | 42 | 159 | 66 | 267 |
| model-support | 96 | 62 | 41 | 199 |
| agent-mode | 3 | 84 | 103 | 190 |
| interface-experience | 26 | 96 | 53 | 175 |
| safety-privacy | 17 | 108 | 22 | 147 |
| developer-workflow | 1 | 85 | 60 | 146 |
| editor-experience | 6 | 22 | 94 | 122 |
| mobile-desktop | 66 | 16 | 13 | 95 |
| reliability-performance | 15 | 39 | 31 | 85 |
| context-window | 9 | 21 | 49 | 79 |
| memory | 56 | 10 | 4 | 70 |
| voice | 42 | 4 | 4 | 50 |
| collaboration | 23 | 4 | 20 | 47 |
| pricing-model | 22 | 7 | 16 | 45 |
| account-access | 9 | 26 | 5 | 40 |
| enterprise-admin | 17 | 10 | 12 | 39 |
| file-data | 28 | 3 | 5 | 36 |
| search-browsing | 27 | 2 | 2 | 31 |
| automation-scheduling | 8 | 6 | 14 | 28 |
| projects-workspaces | 6 | 11 | 8 | 25 |
| image-generation | 16 | 0 | 0 | 16 |
| accessibility-localization | 1 | 6 | 0 | 7 |
| multimodal | 1 | 2 | 2 | 5 |
| learning-tools | 3 | 1 | 0 | 4 |
| artifact-creation | 1 | 0 | 0 | 1 |

## 3. 产品设计建议

### P1 首页没有回答"今天为什么来"

**现状。** 线上首页的区块顺序是 Source coverage → Start exploring → Overview → Products → Themes。第一屏是三段采集说明，主题列表是 25 个连字符 slug。没有任何"最近 7 天 / 30 天发生了什么"的入口。`writer.py` 新模板已把 Start exploring 提到最前并加了一句定位语，但 `index.md` 正文属于人类区域，模板更新不会生效，线上仍是旧顺序。

**建议。**
- 首页重排为：一句定位语 → "最近 30 天"（按日期倒序的新卡片，按产品分组，每产品最多 5 条，附"查看全部"）→ 精选主题（每个一句"为什么值得看"）→ 产品入口（名称、覆盖区间、最近一次发布日期、近 90 天发布次数）→ 折叠的"数据来源与覆盖"。
- 运维细节（快照 SHA、抓取时间戳、"not a successful automatic HTTP fetch"、Pending theme review）移到独立的 `About the data` 页面（见 P8）。
- 首页人类区域需要一次性手动重排并与模板对齐；之后由 writer 维护机器区域。

**落点。** `writer.py` 的 `render_index_markdown` 新增 `recent` 区域；`index.md` 人类区域手动重排一次。

### P2 四类页面扁平并列，缺少按时间进入的路径

**现状。** Product / Release / Change / Theme 四类页面在 Explorer 中以文件夹树并列，`Changes/` 与 `Releases/` 下各有数百到上千个叶子。读者没有"按月浏览"或"某个季度三家都做了什么"的入口。

**建议。**
- 站点导航固定为四项：Themes、Products、Recent（按月归档）、About。Explorer 用 `filterFn` 隐藏 `Changes/` 与 `Releases/`，这两类页面只通过主题页、产品页、Release 页和搜索到达。
- 新增 `Archive/YYYY-MM.md` 月度归档页，由 writer 生成，列出当月三家的卡片，按产品分组；首页"最近 30 天"链接到最近两个月。
- 主题页与产品页的时间线内增加月份小标题（现在只按年分组）。

**落点。** `quartz.layout.ts` 的 `Explorer({ filterFn })`；`writer.py` 新增月度归档渲染。

### P3 卡片粒度与采样规则需要重新定义

**现状。** 一段 changelog 文本就是一张卡；每 Release 最多 5 张（`extract_cards_from_release` 中 `len(cards) >= 5` 即停止）。后果有三种：
- 大段公告被拆成互不独立的碎片。Cursor 2026-09-10 "Projects" 发布被拆成 5 张：其中"Access Projects from the left-hand nav…"、"A Project runs on its own computer in the cloud…"、"You shouldn't have to onboard an agent every time…"是同一功能的三句话。
- 子句独立成卡。"Available in ChatGPT on mobile and web."、"For availability and model selection, see: ChatGPT Work and Codex."、"Start bills monthly with auto-renewal…"、"Standard: $0.50/M input, $2.50/M output tokens"（2026-03-19 与 2026-05-18 两张同文卡）。
- 长 Release 被静默截断。Claude Code 48% 的 Release 卡片数恰好为 5；v2.1.300 的 102 条变更入档 3 条（先经跳过规则，再被上限截断）。

**建议。**
- 明确卡片定义："一次公告中可独立理解的一项能力、机制或策略变化"。连续多段描述同一功能时合并为一张卡，evidence 可包含多段 quote（PRD 5.1 已允许多条 evidence）。
- 取消硬上限 5，改为按 Release 结构分档：有小标题的公告按小标题成卡；纯 bullet 列表（Claude Code）按主题聚合后每主题一张，evidence 列出所有 bullet。这样 v2.1.300 会得到"agent-mode：N 条相关变更"一类的卡，而不是前 3 条。
- 在上限仍存在的过渡期，Release 页必须展示"Tracked 3 of 102 candidate lines"，并在 About 页说明采样规则。
- 增加卡片类型字段 `kind`：launch / expansion（地区或平台扩展）/ pricing / policy / fix。ChatGPT Go 在 pricing-model 时间线中的 7 条地区上线（2025-08-18 至 2025-11-03）应折叠为一条 launch 加多条 expansion。

**落点。** `extract.py` 的 `split_release_lines`、`extract_cards_from_release`；`writer.py` Release 模板；黄金样本需同步更新（见第 7 节）。

### P4 影响等级、置信度与扩散字段表达了不存在的精度

**现状。**
- `impact` 由 5 + 5 个关键词决定（paradigm-shift：agent / autonomous / pricing / 200k / major）。"Added ● N running indicator in /agents…"、"Get native OS notifications when an agent run finishes…"都被标为 paradigm-shift。
- 任何 significant 或 paradigm-shift 卡都被写入 `ai_generated: true, confidence: low`，但卡上没有任何 AI 生成内容。
- 每张卡的 diffusion 区块显示"First In Tracked: cursor-2023-07-06-d7057e"和"Lag Days: 1162"。首条记录是 Cursor 2023 年 nightly 的一句"It comes with agents, which we aren't releasing…"，1,162 天的差值没有研究意义，却以精确数字呈现。
- `evolves_from` 全部为空，但每张卡仍渲染"No evidence-backed evolution relationship assigned."。

**建议。**
- 机器打的 `impact` 不在读者页面展示；只在策展卡（见 C5）由人工确认后显示 significant / paradigm-shift 徽章。或者把关键词等级改名为 `signal_strength` 并明确说明是启发式。
- 移除 `ai_generated` / `confidence` 的自动写入；这两个字段只在真正生成推测内容时出现（PRD 5.1 推测层）。
- diffusion 区块改为一句话："In the tracked set, the earliest same-theme entry is Cursor 2023-07-06 (title)." 不显示 Lag Days、Role、Tracked Products Count；完整字段保留在 frontmatter 供研究者读取。
- 空关系不渲染区块；没有 evolves_from 时不输出"evolution"区域。

**落点。** `extract.py` 的 `choose_impact` 与 `ai_generated` 写入；`writer.py` 的 `render_change_markdown`。

### P5 主题页需要"精选节点 + 分道时间线"，而不是全量列表

**现状。** 主题页结构为研究摘要 → 按年分组的全量时间线 → "Active changes: 190. Use the dated links above to inspect each card."。`agent-mode` 190 条、`apps-integrations` 267 条，Claude Code 因 changelog 粒度细而在数量上压倒 ChatGPT（agent-mode：84 对 3）。PRD 8.2 规划的"多产品对比时间线"和 5.1 的 verbosity 标准化都未落地。

**建议。**
- 主题页分三层：(1) 研究摘要；(2) "Key moments"：策展的 5–15 个节点，三产品分道、按时间对齐，用 Mermaid timeline 或 writer 生成的三列表格渲染；(3) 全量时间线默认折叠（Obsidian `> [!note]-` 折叠 callout，Quartz 支持），并按 年 → 月 分组。
- 时间线条目增加产品色标与计数：年份标题显示"2026 · 142 entries (ChatGPT 3 · Claude Code 60 · Cursor 79)"。
- 页首给出粒度说明："Claude Code averages 4.1 cards per release, ChatGPT 1.9"，直接使用已有的 `verbosity_baseline`。
- 主题标题用 `display_name`（"Agent Mode"），H1 不再是"Theme: agent-mode"。

**落点。** `writer.py` 的 `render_theme_markdown`；`editorial.yaml` 新增 `key_moments` 列表（card_id 清单，策展人维护）。

### P6 产品页是 1,000 行的档案清单

**现状。** `Products/ChatGPT.md` 973 行：Research summary → Source coverage → Summary → Eras → Release Archive（292 条）→ Change Cards（541 条）。Claude Code 与 Cursor 的 Research summary 是"a reviewed phase narrative is not yet available."。`top_themes` 以 25 个 slug 的 YAML 列表存在 frontmatter，页面上没有可视化。

**建议。**
- 产品页只保留：定位一句话 → 节奏面板（见 P7）→ Eras（每个 Era 一段摘要 + 3 个代表 Release）→ 主题分布（前 8 个主题的计数条，链接到主题页）→ 最近 10 次发布。
- Release Archive 与全量 Change Cards 移到 `Products/<name>/releases.md` 与按年拆分的子页，或者进入折叠 callout。
- 为 Cursor（2023-03 起，3.5 年历史、最适合"产品考古"场景）和 Claude Code 补充 Eras；Claude Code 的 Era 边界可用 v2.0.73 → v2.1.x 的功能线（auto mode、agents、mods、workflows）划分。

**落点。** `writer.py` 的 `render_product_markdown`；`editorial.yaml` 补 `products.cursor` 与 `products.claude-code`。

### P7 沉默检测与发布节奏在站点上不可见

**现状。** PRD 2.3 把沉默检测列为最难复制的差异化能力；现在 `Alerts/` 为空，首页只显示"Alert count: 0"。即使没有告警，读者也看不到任何产品的发布节奏。

**建议。**
- 产品页与首页产品入口增加节奏面板：最近一次发布距今天数、近 90 天发布次数、12 个月的月度发布数（纯文本迷你条形图或 Mermaid xychart 即可）。这些数据在合并后的历史中已经存在，不需要新采集。
- 沉默状态常驻展示："Normal cadence" / "Quiet for N weeks (baseline M per month)"，而不是只在触发阈值时产生文件。
- 告警触发时在首页"最近 30 天"顶部显示一条，而非单独的 Alerts 目录。

**落点。** `silence_monitor.py` 输出常驻状态；`writer.py` 产品页与首页新增 `cadence` 区域。

### P8 读者信息与运维信息混在同一页面

**现状。** 首页、产品页 coverage 区块和卡片页都包含运维语句：时间戳混用 `+0800` 与 `Z`、"Imported snapshot; this is not a successful automatic HTTP fetch"、"Pending theme review: 149"、`machine_hash`、`extractor_version`。这些对审核者有价值，对 PRD 3.1 的产品经理与分析师读者是噪音。

**建议。**
- 新建 `About.md`（人类页面 + 机器区域）：数据来源与 URL、覆盖区间、已知缺口、采样与跳过规则、最近成功更新、快照获取方式、术语表（Change Card / Release / Theme / Era）、反馈方式。
- 读者页面上的 coverage 压缩为一行："292 releases · Dec 2022 – Oct 2026 · updated 14 Oct 2026 · [details]"。
- 全站时间统一显示为日期（`2026-10-14`）并统一时区；精确时间戳只留在 About 与 frontmatter。

**落点。** `writer.py` 的 `render_coverage`；新增 About 模板；`index.md` 人类区域。

### P9 待审积压需要产品层面的处理策略

**现状。** `_review/` 有 149 条待审候选（约占活动卡的 7%），它们完全不进入站点。首页把这个数字展示给读者，但读者无法据此做任何事。

**建议。**
- 待审数字移到 About 页或 PR 质量报告，不在首页展示。
- 为长期无法归类的候选增加 `uncategorized` 主题（在 `themes.yaml` 中标 `status: holding`），进入 Release 页但不进入主题时间线，避免 Release 页"Tracked cards"与实际公告脱节。
- 为审核设定节奏：每次 Rolling PR 处理不超过 20 条，`backfill_review.yaml` 记录决策。

**落点。** `themes.yaml`、`backfill_review.yaml`、`writer.py` 首页 overview 区域。

### P10 缺少反馈回路与分发设计

**现状。** PRD 7.2 规划了每条信号的"反馈此信号"链接；现在卡片页没有任何反馈入口。RSS 是 Quartz 默认的"Last 30 notes"，混合卡片、产品页与 Release 页，条目标题被截断。

**建议。**
- 每张卡片页脚增加"Report an issue with this card"链接，指向预填 card_id、source_url 的 GitHub Issue 模板。零基础设施成本。
- RSS 限定为卡片与 Release，标题使用修复后的标题，描述使用 evidence quote；feed 标题改为"ChronoLog · tracked changes in ChatGPT, Claude Code and Cursor"。
- 后续如做 Newsletter，按 PRD 7.2 以 Signal 为素材，而非直接转发 RSS。

**落点。** `writer.py` 卡片模板；`quartz.config.ts` 的 `ContentIndex` 选项或自定义 emitter 过滤。

## 4. UI 设计建议

### U1 站点是零定制的 Quartz 默认皮肤

**现状。** `custom.scss` 只有注释；`sharedPageComponents.header` 为空；页脚链接是占位的 `GitHub: https://github.com`；`PageTitle` 只显示"ChronoLog"，没有标语。PRD 12.3 的琥珀 + 深灰配色已在 `quartz.config.ts` 定义，但没有任何品牌元素承载它。

**建议。**
- 页脚链接指向真实仓库、About 页和 RSS。
- 页头加入一行定位语（PRD 12.2 的"读懂过去，看见拐点"英文版，或"Tracked changes in ChatGPT, Claude Code and Cursor"）。
- 为三个产品固定三种色标（例如 ChatGPT 青、Claude Code 琥珀、Cursor 石墨），在时间线条目、产品入口和图谱节点上一致使用；颜色作为 CSS 自定义属性写入 `custom.scss`。
- 替换默认 `og-image.png` 与 `icon.png`。

**落点。** `quartz.layout.ts`、`quartz/styles/custom.scss`、`quartz/static/`。

### U2 导航组件与内容规模不匹配

**现状。** 左栏 Explorer 展示整个文件夹树；右栏 Graph 在每个页面都渲染，全局模式 `depth: -1` 会加载约 2,500 个节点；列表页右栏为空。

**建议。**
- Explorer 过滤掉 `Changes/`、`Releases/`、`tags`，只剩 Themes、Products、Archive、About，默认展开。
- Graph 只保留在卡片页与主题页的局部模式（`depth: 1`，关闭全局视图按钮）；首页、产品页与列表页移除。
- 列表页右栏放 TOC，便于在 Eras 与年份之间跳转。

**落点。** `quartz.layout.ts` 的 `Explorer({ filterFn })`、`Graph({ globalGraph: undefined })` 或 `ConditionalRender`。

### U3 标题与 H1 不一致，多个页面类型的标题有缺陷

**现状。**
- 卡片页：H1 是截断的句子（见 C1）。
- Release 页：H1 为 `product_name + title`，Cursor 产生"Cursor Cursor Projects"；frontmatter title 为"Cursor — Cursor Projects"。
- 主题页：H1 "Theme: agent-mode"，frontmatter title "Agent Mode"，首页链接文字 "agent-mode"；同一对象三种写法。
- 卡片页 ContentMeta 显示"1 min read"，对两句话的卡片没有意义。

**建议。**
- 统一规则：frontmatter `title` 是唯一展示名，H1 与之相同，所有链接文字使用 `title`。
- Release 标题格式："Cursor · Cursor Projects (2026-09-10)"、"Claude Code · v2.1.300"；当 title 已含产品名时不重复。
- 主题标题使用 `display_name`；首页与产品页的主题链接文字同样使用 `display_name`。
- `ContentMeta({ showReadingTime: false })`。

**落点。** `writer.py` 各 `render_*`；`quartz.layout.ts`。

### U4 卡片页模板需要重做

**现状。** 卡片正文依次是：H1（截断句）→ description（与 quote 100% 重复）→ 引用块 → "No evidence-backed evolution relationship assigned." → diffusion 的 8 行键值对 → 空的 `## Editor Notes`。关联卡片链接的文字是 `cursor-2026-09-02-2a6b87` 一类 ID。侧栏 Backlinks 列出产品页、Release 页、主题页。

**建议。** 卡片页改为固定的五段式：
1. 元信息条：产品色标 · 日期 · 主题（链接）· 类型（kind）· 来源链接。
2. 变化摘要：一到两句编辑摘要（策展卡）或修复后的标题（非策展卡）；不再重复 quote。
3. 官方原文：引用块 + 来源 URL + 所属 Release 标题。
4. 同一 Release 的其他变化：列出兄弟卡片（标题），让碎片在上下文中可读。
5. 同主题前后：前一条与后一条同主题卡片（跨产品），用标题而非 ID。
空区域不渲染；`Editor Notes` 只在人类写入内容时出现。

**落点。** `writer.py` 的 `render_change_markdown`、`relation_link`。

### U5 时间线条目的排版

**现状。** 条目格式为 `- 2026-10-14 · Claude Code: [[…|80 字符截断标题]]`，在窄屏上换行后日期与产品难以对齐；年份标题没有计数；没有产品色标。

**建议。**
- 日期列等宽字体并固定宽度，产品名以色标胶囊展示，标题在 60 字符左右于词边界截断并补省略号（优先用 C1 修复后的完整标题）。
- 年份标题带计数与产品分布；年内按月分组。
- 策展节点（Key moments）在列表中加标记，与普通条目区分。

**落点。** `writer.py` 时间线渲染；`custom.scss` 中为 `.timeline-entry` 定义样式（需要 writer 输出带 class 的 HTML 片段，Quartz 允许内联 HTML）。

### U6 免责声明的呈现方式

**现状。** "Scope: tracked-products-only. Entries show same-theme chronology; they do not establish equivalent capabilities, adoption, or causation."以正文形式出现在每个主题页时间线顶部；卡片 diffusion 区块重复"Inference: No adoption, equivalence, or causation claim."。

**建议。** 全站使用一种折叠 callout `> [!info]- How to read this timeline`，内容集中维护，默认折叠；正文段落只陈述证据支持的内容。PRD 10.2 对推测层已有同样的折叠规范，这里扩展到范围声明。

**落点。** `writer.py` 共用一个 `scope_callout()`。

### U7 浅色模式链接色对比度不足（计算值，待实测）

**现状。** 浅色模式 `secondary: #9b6a19` 在 `light: #f8f7f2` 上的对比度为 4.38:1，低于 WCAG AA 正文 4.5:1；其余配对均达标（tertiary 5.29:1、gray 5.05:1，深色模式各项 6.4:1 以上）。

**建议。** 将浅色 `secondary` 调深到约 `#8a5c12`（对比度约 5.2:1）或仅对链接文字使用更深色，保留琥珀色作强调背景。

**落点。** `quartz.config.ts` 的 `theme.colors.lightMode.secondary`。

### U8 分享与搜索元数据

**现状。** `Description` 插件取正文开头作为 og:description；卡片页得到"Cursor — Cursor Projects: A Project runs…"尚可，首页得到"Archived release dates: 2022-12-15 → …"，主题页得到研究问题第一句。搜索索引以截断标题作为条目名。

**建议。** writer 为每类页面写入 frontmatter `description`：首页一句定位；主题页用研究问题；产品页用定位语；卡片页用修复后的标题 + 产品 + 日期。

**落点。** `writer.py` 各模板的 `fields`。

### U9 移动端（待实测）

**现状。** Quartz 默认响应式；但 80 字符截断标题、8 行 diffusion 键值对和 1,000 行产品页在手机上会显著拉长滚动。

**建议。** 完成 U3–U5 后在 375px 宽度实测首页、主题页、卡片页各一次，记录截图到 `docs/acceptance/`。

## 5. 内容设计建议

### C1 标题生成规则

**现状。** `title = line[:80].rstrip()`，直接截断。示例："Added a dir prop on a mod's Text for right-to-left text: on Windows and in V"、"Among Pro plans, Ultrafast is available only with Pro 500. Buying credits on Pro"。标题首词分布：Added 408、Improved 112、We're 65、Fixed 59、You 57。

**建议。**
- 规则层：取第一句（到句号、冒号或分号），若 ≤ 90 字符直接用；否则在 ≤ 72 字符的最后一个词边界截断并加省略号；去掉"We're introducing"、"You can now"、"This release introduces"等开头并转为第三人称（"ChatGPT introduces…"、"Cursor adds…"）。
- 策展层：significant 以上或进入 Key moments 的卡片由人工在 `editorial.yaml` 覆写标题（`human_overrides` 机制已存在）。
- 回归：黄金样本新增"标题以词边界结束、不含厂商第一人称开头"的断言。

**落点。** `extract.py` 卡片构造；`tests/golden`。

### C2 description 与 evidence 重复

**现状。** description 固定为 `"{product} — {release title}: {quote}"`，与引用块重复，卡片页同一段文字出现两次。

**建议。** description 改为"所属 Release 的一句话上下文"（Release 的 `source_summary` 或版本号），或直接移除；卡片的主体只保留一次原文引用。在 writer 层面把 description 只用于 og:description。

**落点。** `extract.py`、`writer.py`。

### C3 叙述口吻

**现状。** 时间线和标题混用厂商第一人称（"We're introducing dots…"、"You shouldn't have to onboard…"）与档案第三人称。

**建议。** 档案文本（标题、摘要、Era、主题摘要）一律第三人称现在时；厂商原文只出现在引用块。为策展人写一页 `docs/style-guide.md`：时态、人称、产品名写法、日期格式、数字与货币写法、不确定性表述。

### C4 不确定性声明的密度

**现状。** 现有研究摘要与 Era 文本每段都带"does not establish…"、"not evidence that…"、"cannot establish…"，ChatGPT 的 5 个 Era 摘要中每段至少一句。这是正确的认识论态度，但读起来是辩护而不是研究。

**建议。** 每页只保留一处集中的"范围与不确定性"段（见 U6），正文段落改为肯定句陈述证据支持的事实，并用"announced"、"rolled out to"、"described as"这类动词携带来源属性。

### C5 策展覆盖面

**现状。** 研究摘要只有 `agent-mode` 与 `pricing-model`；其余 23 个主题显示"Explore the dated evidence below."。产品 Era 只有 ChatGPT。

**建议。** 按卡片量与读者价值排序，下一批补 5 个：`model-support`（199）、`apps-integrations`（267，含 MCP / 插件 / 连接器演进）、`context-window`（79，PRD 的原型主题）、`memory`（70）、`safety-privacy`（147）。每个摘要遵循 `agent-mode` 的格式：研究问题 → 三产品各一段 → 范围声明。Era 补 Cursor 与 Claude Code（见 P6）。

**落点。** `editorial.yaml`；复核流程沿用 M2 的 B4–B6。

### C6 主题词表需要一次修订

**现状。**
- `interface-experience`（175）与 `developer-workflow`（146）是兜底类，Claude Code 的 `/copy`、`/tui`、prompt footer、模型选择限制都落入前者。
- `safety-privacy` 的 Claude Code 108 张卡抽样多为权限对话框修复、sandbox 设置与 permission 检查，属于"权限与沙箱"而非产品层面的安全 / 隐私策略。
- `apps-integrations` 267 张混合了 MCP、插件、连接器、IDE 集成与第三方应用。
- `artifact-creation` 1 张、`learning-tools` 4 张、`multimodal` 5 张，无法支撑主题页。

**建议。**
- 拆分：`apps-integrations` → `integrations-mcp`（协议与连接器）与 `apps-marketplace`（应用目录、插件商店）；`safety-privacy` → `permissions-sandboxing`（工具权限、沙箱）与 `safety-privacy`（数据、年龄、家长控制、安全漏洞）。
- 合并或降级：`artifact-creation` 并入 `file-data` 或 `editor-experience`；`learning-tools`、`multimodal` 标 `status: emerging`，达到 15 张前不生成独立主题页，只作为标签。
- 利用 `themes.yaml` 已有的 `category`（paradigm / capability / business / workflow / platform / trust / quality / ecosystem）在首页与主题索引分组展示。
- 词表修订会改变历史卡片归属，必须走 `backfill_review.yaml` 决策与黄金样本回归。

**落点。** `themes.yaml`、`backfill_review.yaml`、`tests/golden`。

### C7 Release 页文案

**现状。** GitHub Release 的 `source_summary` 是"What's changed"，作为 Summary 无信息量；Cursor Release 文件名含 `https-cursor-com-changelog-projects`；"Tracked cards: 5"不说明分母。

**建议。** Summary 优先级：官方摘要段 → 第一张卡的标题 → "N tracked changes across themes A, B, C"。显示"Tracked N of M candidate lines"。Release 文件名去掉 URL 片段（仅影响新文件；历史文件保留，避免断链）。

**落点。** `writer.py` 的 `render_release_markdown`；`collect.py` 的 release_id 生成（新记录）。

### C8 覆盖说明文案

**现状。** 首页 coverage 段示例："Official browser snapshot captured: 2026-10-14T23:26:11+0800. Imported snapshot; this is not a successful automatic HTTP fetch."

**建议。** 读者版："ChatGPT · 292 releases · 15 Dec 2022 – 7 Oct 2026 · updated 14 Oct 2026 from the official release notes page. Codex-only entries are not tracked." 其余信息进 About 页。保留 M2 B3 要求的"抓取时间与最新 Release 日期分开展示"，但改成读者能理解的措辞。

### C9 关系与链接文字

**现状。** `related_changes`、`diffusion.first_in_tracked` 的链接文字是 card_id（`cursor-2023-07-06-d7057e`）。

**建议。** `relation_link` 使用目标卡的标题加日期与产品；ID 只留在 frontmatter。

### C10 术语与标签

**现状。** 主题页 tag 为 `#theme #moc`，"MOC"是 Obsidian 圈术语；"Change Card"、"Era"、"tracked-products-only"在站点上没有定义。

**建议。** About 页提供术语表（PRD 附录 G 已有基础）；对读者隐藏 `moc` 标签或改为 `theme` 单一标签；TagList 组件可只保留在卡片页。

### C11 日期与时间格式

**现状。** 同一页面混用 `2026-10-14T23:26:11+0800`、`2026-10-15T01:55:30Z`、`2026-10-14`、"Sep 10, 2026"（Quartz ContentMeta）。

**建议。** 读者页面统一 ISO 日期 `2026-10-14`；Quartz `locale` 保持 en-US 时将 ContentMeta 日期格式改为 ISO（自定义 `Date` 组件格式化），或接受英文长日期但全站一致。

### C12 语言策略

**现状。** 站点为英文，文档与策展流程为中文。

**建议。** 公开站点保持英文（来源与目标读者均以英文为主）；策展人写作指南可以中文。若后续面向中文读者，优先提供主题研究摘要的中文版，而不是翻译 1,949 张卡片。

## 6. 优先级与实施路线

W1 为低成本修正，只涉及 writer、Quartz 配置与首页人类区域，不改变卡片身份与分类；W2 涉及提取规则、词表与策展内容，需要黄金样本与人工复核；W3 对应 PRD Phase 3。

| 波次 | 编号 | 改动 | 主要文件 | 验收方式 |
| --- | --- | --- | --- | --- |
| W1 | C1 | 标题按句子与词边界生成，去厂商第一人称 | `extract.py`、`tests/golden` | 截断标题比例从 69% 降到 < 5%；黄金样本通过 |
| W1 | U3 | H1 与 title 统一；Release / Theme 标题修复 | `writer.py` | 抽查 20 页 H1 = title；无"Cursor Cursor" |
| W1 | U4 / P4 | 卡片模板五段式；空区域不渲染；移除 Lag Days 等展示 | `writer.py` | 卡片页无空标题、无 ID 链接文字、quote 只出现一次 |
| W1 | U2 | Explorer 过滤、Graph 局部化、页脚修正 | `quartz.layout.ts` | 构建通过；Explorer 仅四项 |
| W1 | P1 / P8 | 首页重排：最近 30 天、精选、产品入口；运维信息迁至 About | `writer.py`、`index.md`、`About.md` | 首页第一屏无时间戳与快照说明 |
| W1 | U7 / U8 | 链接色对比度；frontmatter description | `quartz.config.ts`、`writer.py` | 对比度 ≥ 4.5:1；OG 描述抽查 |
| W1 | C7 / C8 | Release 摘要与"Tracked N of M"；coverage 读者化文案 | `writer.py` | Release 页显示分母 |
| W1 | P10 | 卡片反馈链接；RSS 限定卡片与 Release | `writer.py`、`quartz.config.ts` | RSS 条目标题完整 |
| W2 | P3 | 卡片定义修订：合并连续段、取消硬上限、`kind` 字段 | `extract.py`、`writer.py`、`tests/golden` | Claude Code 入档比例可解释；v2.1.300 不再只有 3 条；B4 样本复核 |
| W2 | P5 / U5 | 主题页 Key moments + 分道时间线 + 折叠全量 + 月分组 | `writer.py`、`editorial.yaml` | 两个主题在浏览器中可读（B6 口径） |
| W2 | P6 / C5 | 产品页瘦身；Cursor 与 Claude Code Eras；5 个主题摘要 | `writer.py`、`editorial.yaml` | 复用 M2 B4–B6 复核流程 |
| W2 | C6 | 主题词表修订与回填 | `themes.yaml`、`backfill_review.yaml` | 主题正确率抽样 ≥ 90%（PRD 9.5） |
| W2 | P7 | 节奏面板与常驻沉默状态 | `silence_monitor.py`、`writer.py` | 三个产品页均有近 12 月发布数 |
| W2 | P2 | 月度归档页 | `writer.py` | Archive 页链接校验通过 |
| W2 | C3 / C4 | 写作指南；研究摘要改为肯定句 + 集中声明 | `docs/style-guide.md`、`editorial.yaml` | 策展人按指南复核两页 |
| W3 | PRD 7.2 | L1 信号页与 Signal Generator | 新模块 | 按 PRD 11.1 Tier B 审核 |
| W3 | PRD 7.2 | 弱信号观察站（沉默 + 改写） | 新模块 | 独立页面可访问 |
| W3 | PRD 8.2 | 交互式对比时间线组件 | Quartz 自定义组件 | 替换 Mermaid 版本并保留降级 |

W1 预计两个 PR：一个改提取与 writer 模板（会重写全部 Markdown 的机器区域），一个改 Quartz 布局与首页人类区域。

W1 实际交付（2026-10-15）：C1 与 U3 的卡片部分 → PR #7；U3 其余、U4 / P4、C7、C9、U8、P10 的反馈链接 → PR #8；U2、U1 的标语与色标变量、U7、P1 / P8 / P9、C8、C10 术语表、P10 的 RSS 限定 → PR #9。U9 与 U1 的图标替换未做。

## 7. 与现有计划的衔接与风险

- **机器区域全量重写。** C1、U3、U4 会改变每张卡与每个列表页的机器区域，`machine_hash` 全部更新。这是一次性的大 PR，应在没有待审 Rolling PR 时合并，避免与 `codex/chronolog-updates` 冲突；人类区域与 `human_overrides` 按 M1 所有权模型保留。
- **卡片身份不变。** C1 只改 `title` 与 `slug` 展示，`card_id` 由产品、日期与证据哈希生成，不受影响；现有文件路径含旧 slug，保留即可（`change_card_paths` 优先复用已存在路径），不会产生断链。
- **P3 会改变卡片集合。** 合并碎片与取消上限会新增与废弃卡片，必须走 `--reconcile` 与 M2 的 B4 样本复核；黄金样本 `tests/golden` 需要同步更新并在验收记录中说明口径变化。
- **词表修订影响历史归属。** C6 的拆分会把数百张卡改派主题；按 M2.6 的黄金样本回归和 `backfill_review.yaml` 决策执行，不能直接改 `themes.yaml` 后重跑。
- **首页人类区域。** `index.md` 的正文在机器区域之外，writer 不会重排；P1 需要手动编辑一次，之后再由 writer 维护新增区域。
- **发布过滤不变。** 所有建议都在活动集合内生效，`publication_filter.ts` 的三产品过滤与 superseded 规则不需要改动。
- **与开发计划的关系。** 本文的 W1 可并入 M3 之后的下一个里程碑；W2 对应开发计划"后续待排"中的内容策展；W3 对应 PRD Phase 3。建议在开发计划中新增 M4（读者体验）条目并引用本文编号。

## 附录 A：统计口径

- 活动卡：`Changes/{ChatGPT,Claude Code,Cursor}/*.md` 中 frontmatter 无 `superseded: true` 的文件，共 1,949。
- 截断标题：`len(title) >= 78`；句末标点：`. ! ? ) ]`。
- 候选行：对 `_pipeline/dollar-title-replay-20261015/collection.json.gz` 中每个 Release 的 `body` 调用 `_scripts.extract.split_release_lines`，统计行数；该集合与线上活动集合同源。
- v2.1.300 的 102 条变更来自 GitHub Release 页面的列表项计数；ChronoLog 对应 Release 页 `changes_count: 3`。
- 对比度：WCAG 2.x 相对亮度公式，取 `quartz.config.ts` 中的十六进制值计算。
- 主题分布：按 frontmatter `theme` 与 `product_name` 计数。

## 附录 B：页面逐项检查记录

| 页面 | 观察 |
| --- | --- |
| 首页（线上） | 第一区块为 Source coverage，含 `+0800` 与 `Z` 两种时间戳；Start exploring 2 个主题；Overview 5 个计数含"Pending theme review: 149"；主题列表为 25 个 slug；页脚"Quartz v0.1.0"与 `https://github.com` |
| `Themes/agent-mode`（线上） | H1 "Theme: agent-mode"；研究摘要 4 段；时间线 190 条，2026 年约 140 条；"Change Cards"段只有一句计数；tag `theme`、`moc`；Backlinks 只有首页 |
| `Changes/Cursor/2026-09-10-a-project-runs…`（线上） | H1 为截断句；"Sep 10, 2026 · 1 min read"；description 与 quote 重复；"No evidence-backed evolution relationship assigned."；diffusion 8 行键值对含 Lag days 1162；空"Editor Notes" |
| `index.xml`（线上） | 标题"ChronoLog"，描述"Last 30 notes on ChronoLog"；前 6 条为截断标题的卡片，第 7、8 条为产品页与 Release 页 |
| `Products/ChatGPT.md` | 973 行；5 个 Era 各带免责句；Release Archive 292 条；Change Cards 541 条 |
| `Products/Claude Code.md` | 1,114 行；Research summary 为"not yet available" |
| `Releases/Cursor/cursor-2026-09-10-cursor-projects-…` | H1 "Cursor Cursor Projects"；5 张卡中 3 张为同一功能的连续段落 |
| `Releases/Claude Code/claude-code-2026-10-14-v2-1-300-…` | Summary "What's changed"；Tracked cards: 3；GitHub 原文 102 条 |
| `_review/chatgpt-2023-02-09-e4f9a9.md` | 候选理由 `no_match`，`theme_suggestion: as-we-recently`（由句首词生成，无指导意义） |

## 附录 C：W2 P3 卡片定义方案估算（2026-10-16）

按 2026-10-15 的采集集合（790 个 Release）重新模拟提取，比较三种卡片定义下的卡片规模。数字含待审主题行，因此略高于活动集合的 1,949。

| 方案 | ChatGPT | Claude Code | Cursor | 合计 | 说明 |
| --- | ---: | ---: | ---: | ---: | --- |
| 现状：每行一卡，每 Release 最多 5 张 | 607 | 847 | 690 | 2,144 | Claude Code 候选行 6,948 只入档 11%，v2.1.300 的 102 条变更收录 3 条 |
| 方案 A：取消上限，每行一卡 | 693 | 3,310 | 1,509 | 5,512 | 覆盖完整，但 Claude Code 占六成，主题时间线与首页被配置项级变更淹没 |
| 方案 B：结构化公告按小节成卡；扁平列表按主题聚合 | 592 | 1,170 | 420 | 2,182 | Cursor 与 ChatGPT 的小节即一项能力（碎片消失）；Claude Code 每 Release 每主题一张“摘要卡”，evidence 列出全部条目，不再丢失 |
| 方案 B+：方案 B，另外把 Claude Code 中高信号条目单独成卡 | 592 | 约 1,400–1,600 | 420 | 约 2,400–2,600 | 高信号判定需要新的规则或人工标注，先用关键词（Introducing、now … by default、Added /command）并抽样复核 |

方案 B 的代价：卡片身份改变（聚合卡的 `card_id` 由多条 quote 哈希得到），M2 的 60 张黄金样本中按 `card_id` 定位的用例需要重做口径；`related_changes`、`diffusion.first_in_tracked` 与 `editorial.yaml` 中引用 Release 的 Era 证据不受影响。方案 A 不改变现有身份，只新增卡片，但读者体验会明显退化。

建议：方案 B 作为 W2 P3 的基线，Claude Code 摘要卡的标题形如 "v2.1.300 · Agent Mode: 12 changes" 并在正文逐条列出 bullet；`kind` 字段（launch / expansion / pricing / policy / fix / digest）同步引入；黄金样本改为按 Release 与 quote 定位。实施前需要确认：是否接受聚合卡作为“最小知识单元”的例外，以及 B+ 的高信号规则是否值得先做。
