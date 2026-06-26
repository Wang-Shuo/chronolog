# ChronoLog 产品需求文档（PRD）

**版本**：v1.8 | **最后更新**：2026-06-12 | **状态**：MVP 设计阶段

| 版本 | 主要变更摘要 |
|------|------------|
| v1.1 | 数据模型三层化、主题词表、两段式审核 gate、管线数据流明确 |
| v1.2 | evidence 溯源、evolves_from/diffusion、派生查询索引、快照改写检测 |
| v1.3 | 词量偏差、Analyzer-A/B 拆分、沉默检测移出 LLM、LLM→JSON→Markdown |
| v1.4 | Signal 实体与 Signal Generator、Analyzer-B 增量 diff、附录矛盾修复 |
| v1.5 | writer.py 双向合并、死信队列 DLQ 局部容错 |
| v1.6 | 质量控制指标（9.5）、metrics.py、三阶段质量门禁 |
| v1.7 | 全文一致性修订（见附录 F 修订记录） |
| v1.8 | 评审修订：历史回填策略、Writer 所有权模型（替代双向合并）、卡片身份与重处理协议、审核分级（Review Tiers）、Mermaid 对比时间线前置、Evals 回归、弱信号产品化 |

> 完整版本历史请见**附录 F：修订记录**。

---

## 目录

- [1. 产品概述](#1-产品概述)
- [2. 核心理念与差异化](#2-核心理念与差异化)
- [3. 目标用户与使用场景](#3-目标用户与使用场景)
- [4. 系统架构](#4-系统架构)
- [5. 数据模型与 Obsidian 集成](#5-数据模型与-obsidian-集成)
- [6. LLM 处理管线（Pipeline）](#6-llm-处理管线pipeline)
- [7. 信息架构与内容分层](#7-信息架构与内容分层)
- [8. 可视化与交互设计](#8-可视化与交互设计)
- [9. 技术实现规范](#9-技术实现规范)
- [10. 发布层设计（Quartz 定制）](#10-发布层设计quartz-定制)
- [11. 自动化工作流](#11-自动化工作流)
- [12. 品牌与命名](#12-品牌与命名)
- [13. MVP 路线图](#13-mvp-路线图)
- [14. 风险与对策](#14-风险与对策)
- [15. 范围边界（Out of Scope）](#15-范围边界out-of-scope)
- [16. 产品成功指标（KPI）](#16-产品成功指标kpi)
- [17. 外部依赖清单](#17-外部依赖清单)
- [18. 待决问题（Open Questions）](#18-待决问题open-questions)
- [附录 A：Extractor Prompt 模板](#附录-a extractor-prompt-模板示例)
- [附录 B：Analyzer Prompt 模板](#附录-b-analyzer-prompt-模板示例)
- [附录 C：Synthesizer Prompt 模板](#附录-c-synthesizer-prompt-模板示例)
- [附录 D：技术栈版本锁定](#附录-d-技术栈版本锁定)
- [附录 E：Signal Generator Prompt 模板](#附录-e-signal-generator-prompt-模板示例)
- [附录 F：修订记录](#附录-f-修订记录)
- [附录 G：术语表（Glossary）](#附录-g-术语表glossary)

---

## 1. 产品概述

### 1.1 一句话定义

ChronoLog 是一个以「主题演化」为组织核心的产品 changelog 档案馆。它自动追踪多个产品的更新历史，通过 LLM 将其解构为可关联、可对比、可探索的知识网络，最终发布为面向研究者和决策者的趋势探索站点。

### 1.2 核心命题

产品的演化不是随机事件的堆积，而是围绕关键主题（如定价模式、AI 集成、架构重构）的渐进式博弈。当把多个同行产品的 changelog 放在一起，按「主题」而非「时间」重新折叠时，行业趋势会自然浮现。

### 1.3 设计哲学

- **大道至简**：整个技术栈只有三层——Python 采集脚本、Markdown 文本库、Quartz 静态站点
- **Markdown 是最终事实来源**：Vault 中的 Markdown 文件是唯一持久化的事实来源（SSOT），可被
  Git 版本控制，可被 Obsidian 直接打开。LLM 各阶段的中间产物以 JSON 格式流转，仅在
  `writer.py` 渲染步骤后才落地为最终 Markdown（见 6.4）
- **LLM 只做增量价值**：机器负责采集、提取、关联，人类（或人工审核）负责最终洞察与叙事
- **Obsidian 即后台**：编辑者的工作界面就是 Obsidian，发布的用户界面就是 Obsidian 知识库的公开版本
- **人机协作 = 所有权分区**：人工在 Obsidian 中对 Markdown 所做的精修不会被 Pipeline 覆盖；
  机器内容写在显式标记区块内、人类内容在区块外，`writer.py` 只重写自己拥有的区块
  （Ownership over Merge，见 4.3、6.5）

---

## 2. 核心理念与差异化

### 2.1 从「时间线」到「主题演化」

传统 changelog 工具以「产品」为首要维度，按时间罗列更新。ChronoLog 的首要维度是**主题（Theme）**。

**不要问**：Cursor 在 2026 年 3 月更新了什么？  
**要问**：「AI 编程助手的上下文窗口之争」这个主题，在 2026 Q1-Q2 跨越 Cursor、Windsurf、GitHub Copilot 是如何演化的？

**实现方式**：
- 在 LLM 提取阶段，为每个更新自动打上「演化主题标签」（如 `#context-window` `#pricing-model` `#agent-mode`）
- 在 Obsidian 中，每个主题是一个 MOC（Map of Content），自动聚合不同产品的相关更新
- 用户进入网站后，首先看到的是「主题演化」视图，而非「产品时间线」

### 2.2 「差异卡片」（Change Card）作为知识原子

一个 release 往往包含多个独立变化主题，混在一起会丢失粒度。ChronoLog 的最小数据单元不是「Release」，而是「Change」。

**Change Card 定义**：
- 描述一个产品在单次发布中围绕**单一主题**的具体变化
- 可独立双链，可跨产品聚合对比
- 包含：差异描述、战略意图推测、在行业坐标中的位置

**示例**：一次 Cursor v0.30 的发布可能被拆分为 3 张 Change Card：
1. 「上下文窗口扩展至 200K」（主题：#context-window）
2. 「引入 Agent 模式自动执行 Shell 命令」（主题：#agent-mode）
3. 「Pro 计划价格调整」（主题：#pricing-model）

### 2.3 追踪「沉默」（Silence Detection）

行业研究不仅要关注「发生了什么」，还要关注「没发生什么」以及「谁没有发声」。

- 一个曾经月更 2 次的产品突然沉默 3 个月 → 可能在重构、被收购或战略收缩
- 整个行业在某项关键技术突破后，某个头部玩家没有跟进 → 可能技术路线不同或存在战略定力

**实现方式**：由纯 Python 统计脚本 `silence_monitor.py`（不调用 LLM）计算每个产品的更新频率
基线，当实际频率低于可配置阈值时，自动生成 `Alerts/{date}-{product}-silence.md` 告警文件，
在趋势分析中把「跟进者」和「不跟进者」分开讨论（详见 6.3）。

---

## 3. 目标用户与使用场景

### 3.1 核心用户画像

| 用户类型 | 诉求 | 使用层级 |
|---------|------|---------|
| **产品经理（竞品研究）** | 快速了解竞品的演化节奏和战略重心转移 | L1 信号 + L2 档案 |
| **投资人/行业分析师** | 识别行业拐点、技术扩散周期、竞争格局变化 | L2 档案 + L3 洞察 |
| **开发者/技术决策者** | 追踪工具链演进，判断技术采纳时机 | L1 信号 + L2 档案 |
| **内容创作者** | 获取结构化素材，生成行业分析内容 | L2 档案 + L3 洞察 |

### 3.2 关键使用场景

1. **竞品节奏对比**：我想知道过去一年，Notion、ClickUp、Linear 分别在「AI 集成」主题上做了什么，谁快谁慢
2. **拐点识别**：我想知道「定价模式从订阅制转向按量计费」这个趋势，是从哪个产品开始的，后续谁跟进了，谁没有
3. **技术扩散追踪**：我想知道「Agent 模式」这个概念，从出现到被主流产品采纳，经历了多长时间，跨越了哪些产品类别
4. **产品考古**：我想回溯一个产品从 0.1 到 3.0 的完整演化路径，识别其战略转折点

---

## 4. 系统架构

### 4.1 整体架构图

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  数据采集层  │ ──▶ │  LLM 处理层  │ ──▶ │ Obsidian 层 │
│  (Python)   │     │  (Pipeline) │     │ (Markdown)  │
└─────────────┘     └─────────────┘     └──────┬──────┘
                                               │
                    ┌─────────────┐           │
                    │  发布层       │ ◀─────────┘
                    │(Quartz)     │     自动同步
                    └─────────────┘
```

### 4.2 技术栈选型

| 层级 | 选型 | 理由 |
|------|------|------|
| 采集 | Python + `httpx` / `feedparser` | 脚本式，无框架负担 |
| 存储 | Markdown + YAML Frontmatter | Obsidian 原生，Git 友好 |
| 中间态 | JSON（LLM 阶段）→ Markdown（Writer 渲染后） | LLM 各阶段输出结构化 JSON（schema 可机器校验）；`writer.py` 确定性渲染为最终 Markdown；人类和 Obsidian 直接与 Markdown 交互 |
| 处理 | Python + LLM API (OpenAI/Claude) | 文件输入，文件输出 |
| 站点 | **Quartz v4** | 专为 Obsidian 知识库发布设计，支持双链、图谱、搜索 |
| 部署 | Cloudflare Pages / GitHub Pages | 零成本，全球 CDN |

### 4.3 架构原则

- **无持久化数据库**：所有状态存在文件系统和 Git 历史中
- **无后端服务**：Python 脚本在 GitHub Actions 中运行，纯静态输出
- **LLM 输出即文件**：LLM 不直接操作 API，而是生成 Markdown 文件到指定目录
- **可回滚**：因为一切都是 Git 管理的文本，任何错误都可以 `git revert`
- **唯一事实来源（SSOT）与派生索引分离**：Markdown 是唯一事实来源；查询用的
  结构化索引在构建时从 Markdown 派生（见 4.4），用完即弃、不入库、不破坏极简原则
- **人机协作（Ownership over Merge，所有权优于合并）**：既然「Obsidian 即后台」，人类
  编辑在 Markdown 中做的精修、错别字修正、人工洞察不可被 Pipeline 无情覆盖。但「智能
  双向合并」难以做对（缺少三方合并的 base 版本、冲突语义模糊）。因此 v1.8 起改为
  **所有权分区**：机器内容位于显式标记区块（machine region）与机器持有的 frontmatter
  字段中，由 Pipeline 幂等重写；区块之外全部属于人类，Pipeline 永不触碰（规格见 6.5）。
  机器掌握增量逻辑，人类掌握叙事控制权。

### 4.4 派生查询索引（Derived Query Index）

「无数据库」哲学很优雅，但**趋势分析需要大量聚合查询**：按时间/主题/产品聚合、
计算扩散时间差（`diffusion.lag_days`）、画更新频率基线、串联演化链（`evolves_from`）。
若每次都靠遍历几千个 Markdown 文件 + 解析 frontmatter，会很慢且易错。

**解法**：保持 Markdown 为**唯一事实来源**，但在 pipeline 阶段从所有 frontmatter
派生一个**只读查询索引**：

```
_pipeline/
└── index/
    ├── index.sqlite          # 构建时生成的只读索引（changes / products / themes / relations 表）
    └── index.json            # 供前端组件消费的轻量派生数据
```

**增量 diff + 主题预过滤（解决 Analyzer-B 上下文窗口瓶颈）**：

Analyzer-B 若每次运行都输入「全部历史 Change Cards」，在追踪 50+ 产品时极易超出
LLM 上下文窗口（数万张卡片 + prompt + 输出 JSON）。因此索引同时承担**增量上下文
裁剪**职责：

1. **增量识别**：每次 pipeline 运行时，索引先标记出「本次新增的 Change Cards」
   和「自上次 Analyzer-B 运行以来发生变化的主题」
2. **主题预过滤**：只对**活跃主题**（过去 N 天内有新卡片落入的主题）触发 Analyzer-B；
   沉寂主题跳过，不消耗 token
3. **上下文裁剪**：对每个活跃主题，从索引中检索该主题下**最相关的 K 张历史卡片**
   （K≈20，按时间近邻 + embedding 相似度混合排序），而非全量历史。这让 Analyzer-B
   的输入从 O(全部历史) 降至 O(活跃主题 × K)
4. **Embedding 索引**：`index.sqlite` 中维护 Change Card 的文本 embedding（由本地
   轻量模型 `all-MiniLM-L6-v2` 经 ONNX 运行时生成，如 `fastembed`——避免在 CI 中安装
   完整 PyTorch，见附录 D），用于跨主题语义相似度检索和 evolves_from 候选召回。
   **embedding 按卡片内容 hash 缓存**：内容未变不重算；模型版本变更
   （`EMBEDDING_MODEL_VERSION`）时全量重建——既是增量、又保持「100% 可从 Markdown
   重建」哲学（对应 OQ-2 的决策）

> 这一设计让系统可以平滑扩展：新增产品或历史积累不会线性增加 Analyzer-B 的token 消耗，只增加活跃主题的上下文量。

**关键约束（确保不破坏「无数据库」哲学）**：

- 索引是 **100% 可从 Markdown 重建**的派生产物，**不进 Git**（加入 `.gitignore`）
- 任何写操作只发生在 Markdown，**绝不直接写索引**——索引每次构建时全量重建
- Analyzer / Synthesizer 与前端定制组件统一通过索引做查询，而非遍历文件
- 删除索引不丢任何信息，`git revert` 仍然完全有效

这样既保留「文本优先 / Git 友好 / 可回滚」的核心哲学，又让趋势分析、扩散计算、
演化链串联等重查询场景高效可行——是低成本、不破坏极简原则的折中。

---

## 5. 数据模型与 Obsidian 集成

### 5.1 核心实体

#### 实体一：产品档案（Product）

```markdown
---
aliases: []
tags:
  - product
  - saas
  - ai-writing
category: 生产力工具
status: active
founded: 2021-03-15
website: https://example.com
github: org/repo
themes:
  - ai-integration
  - collaboration
first_tracked_release: 2026-01-10
last_updated: 2026-04-23
related_products:
  - "[[Notion]]"
  - "[[Cursor]]"
# verbosity_baseline 由 Analyzer-A 计算：该产品历史上平均每次 release 产出的
# Change Card 数。用于在跨产品趋势对比时对卡片数做标准化，消除"详细写手"与
# "简短写手"之间的词量偏差（词量偏差机制见 5.1「实体二：差异卡片」章节正文）。
verbosity_baseline: 2.3            # 平均每次 release 产出 Change Cards 数（Analyzer-A 回填）
# eras 由 Analyzer-A 阶段识别并回填：将零散 release 折叠为有叙事的演化阶段
eras:
  - name: "编辑器时代"
    from: 2022-01-10
    to: 2023-06-30
    summary: "以代码补全为核心的智能编辑器"
  - name: "Agent 平台时代"
    from: 2023-07-01
    to: null              # null 表示当前阶段
    summary: "从补全工具转向自主执行的 Agent 平台"
---

# Product Name

## 产品定位
（此处填入：一句话描述产品核心功能与定位）

## 演化阶段（Eras，由 Analyzer 回填）
产品的演化不是流水账，而是若干战略阶段的更替。本节将零散 release 折叠为有叙事的「时代」，用于支撑「单产品演化」视图。

### 编辑器时代（2022-01 ~ 2023-06）
该阶段围绕代码补全能力迭代……（含本阶段关键 Change Cards 链接）
- [[2022-01-10 v1.0 初始发布]]
- [[2022-06-15 v2.0 引入 AI 功能]]

### Agent 平台时代（2023-07 ~ 至今）
战略转折点：[[2023-07 引入 Agent 模式]] ……

## 演化概览（自动生成的 Change Card 时间线链接）
- [[2022-01-10 v1.0 初始发布]]
- [[2022-06-15 v2.0 引入 AI 功能]]
```

#### 实体二：差异卡片（Change Card）

Change Card 的字段按**生成阶段**与**可信度**分为三层，避免把客观事实与
AI 主观推断混为一谈：

- **事实层（Extractor 生成，单卡片内可确定）**：差异描述、主题标签、影响等级、日期、**证据溯源（`evidence`）**
- **关联层（Analyzer 阶段回填，需全局视图）**：`related_changes`、`evolves_from`（产品内演化链）、`diffusion`（跨产品扩散）、行业坐标
- **推测层（标注 `ai_generated`，含 `confidence`）**：战略意图推测

> 注意：关联层字段**不能**在 Extractor 阶段生成——逐条 release 提取时无法预知
> 后续其他产品的卡片（鸡生蛋问题）。这些字段一律在 Analyzer 拿到全局 Change
> Card 集合后**回填**。

**为什么需要 `evidence`（证据溯源）**：研究者/分析师最在意的不是「AI 怎么说」，
而是「凭什么这么说、原文在哪」。每个事实层判断都必须可一键回溯到 Release 原文的
具体片段，这让事实层可被验证、推测层与证据分离，是「可审计的演化档案」这一差异
化的核心。`quote`（原文短引用）为**必填主定位手段**；`anchor` 为可选——多数
changelog 没有稳定锚点，缺失时以 quote 文本匹配定位。

**主题单值约定**：`theme` 为单值。一次发布中横跨两个主题的变化（如「Agent 模式的
按量计费」）按定义拆分为两张卡片，各自归属单一主题、可共享 evidence。这是为「主题
聚合」优化的刻意取舍：宁可多一张卡片，不可让一张卡片污染两个主题的时间线。

**推测层按需生成**：战略意图推测仅对 `impact ∈ {significant, paradigm-shift}` 的
卡片生成（见 6.4），且在站点 UI 中默认折叠展示（见 10.2）——对分析师受众，「可审计
的事实档案」必须是第一印象，规模化的 AI 推测即便有标注也应保持低姿态。

**词量偏差（Verbosity Bias）警告**：不同产品的 changelog 写作风格差异巨大。
Cursor 的一次 release 可能被拆成 5 张 Change Cards，某竞品描述相同量级的变化只有
1 张。若直接用卡片数做跨产品比较，changelog 写得详细的产品会看起来更活跃——这是
写作风格差异，而非真实产品节奏差异。

对策：

- 每个 Product 档案维护 `verbosity_baseline`（历史平均每次 release 产出的卡片数，
  由 Analyzer-A 计算回填）
- 在趋势分析和主题页的跨产品对比中，使用**标准化变化量**（实际卡片数 /
  verbosity_baseline × 100）而非原始卡片数
- 在主题页跨产品时间线上显示数据粒度说明（如"Cursor 数据基于 GitHub Releases，
  平均每版本 2.3 张卡片"），让用户了解各产品数据来源的粒度差异

**为什么需要两类关系字段**：「单产品演化」与「多产品趋势」时间语义不同，需要两套
关系结构：

- `evolves_from`（**产品内·纵向因果链**）：本次变化是产品内哪次变化的延续/迭代，
  用于画出单产品的演化主干（支撑「看出演化过程」）
- `diffusion`（**跨产品·横向扩散**）：标注本卡片在某理念扩散中的角色，以及相对
  最早记录的时间差。**重要约束**：`role` 的判断范围严格限定在 **ChronoLog 已追踪
  的产品集合之内**——只比较系统收录的产品，而非声称行业意义上的首创。详见
  `diffusion` 字段的 `scope` 子字段。

```markdown
---
type: change
card_id: cursor-20260315-a3f8e2  # 确定性身份：由代码（非 LLM）按 product + release 日期 + 证据哈希生成（见 9.6）
extractor_version: v3            # 生成本卡片的 Extractor Prompt 版本（重处理协议用，见 9.6）
product: "[[Cursor]]"
source_release: "[[2026-03 v0.30]]"
date: 2026-03-15
# —— 事实层（Extractor 生成）——
theme: "context-window"          # 必须取自受控主题词表（见 5.3）；单值，跨主题变化拆为多张卡片
impact: paradigm-shift           # incremental / significant / paradigm-shift
evidence:                        # 溯源：指向 Release 原文的具体证据片段
  - source_release: "[[Releases/Cursor/2026-03-15-v0.30]]"
    quote: "Context window expanded from 32K to 200K tokens."  # 必填：原文短引用为主定位手段
    anchor: "#context-window"    # 可选：多数 changelog 无稳定锚点，缺失时以 quote 文本匹配定位
# —— 关联层（Analyzer 阶段回填，初始为空）——
related_changes:
  - "[[Copilot 2026-02 context-expansion]]"
  - "[[Windsurf 2026-03 tab-context]]"
evolves_from:                    # 产品内演化链：本次是哪次变化的延续
  - "[[Cursor 2025-11 context-32k]]"
diffusion:                       # 跨产品扩散：角色 + 相对首发时间差
  theme: context-window
  scope: tracked-products-only  # 固定值：仅在已追踪产品集内判断，不声称行业首创
  role: follower                 # originator（已追踪产品中最早）/ follower / variant
  first_in_tracked: "[[Copilot 2026-01 context-100k]]"  # 已追踪产品中最早的记录
  lag_days: 60                   # 相对已追踪集合中最早记录的时间差（天）
  tracked_products_count: 8      # 判断时已追踪产品总数（影响结论可信度）
# —— 推测层（AI 主观推断，须显式标注）——
ai_generated: true
confidence: medium               # low / medium / high
---

# Cursor 引入 200K 上下文窗口

## 差异描述（事实层）
从之前的 32K 提升到 200K，支持整个代码库作为上下文。

## 证据溯源（事实层 · evidence）
> 「Context window expanded from 32K to 200K tokens.」
> —— 原文：[[Releases/Cursor/2026-03-15-v0.30]]

## 演化链（关联层 · evolves_from）
本次扩展是 [[Cursor 2025-11 context-32k]] 的直接延续。

## 行业坐标（关联层 · diffusion）
> 以下对比范围：ChronoLog 当前已追踪的 8 个产品，不代表全行业首创判断。

在已追踪产品中，「上下文窗口竞赛」的扩散顺序如下（Cursor 为 follower，落后
已追踪集合中最早记录 60 天）：
1. Copilot 最早记录到 100K 扩展（[[2026-01]]）——在已追踪产品中首个
2. Cursor 跟进到 200K（本条目，follower，+60d）
3. Windsurf 随后推出 Tab 级上下文（variant，[[2026-03]]）

## 🤖 战略意图推测（AI 推测 · confidence: medium）
> 以下为 LLM 推断，非官方事实，仅供参考。
Cursor 此更新可能是对 Windsurf 社区版策略的防御性回应...
```

#### 实体三：主题演化（Theme / MOC）

```markdown
---
tags:
  - theme
  - moc
status: official              # official / candidate（候选主题，见 5.3）
created: 2026-01-15
products_involved:
  - "[[Cursor]]"
  - "[[GitHub Copilot]]"
  - "[[Windsurf]]"
---

# 主题：上下文窗口竞赛（Context Window Wars）

## 演化时间线（事实层）
- [[2026-01 Copilot 扩展至 100K]]
- [[2026-03 Cursor 扩展至 200K]]
- [[2026-03 Windsurf 推出 Tab 级上下文]]

## 跨产品对比时间线（构建时生成）
（此处由 writer.py 在机器区块内生成 Mermaid timeline/gantt 图，见 8.2——
零前端开发即可获得核心对比视图）

## 竞争格局分析（关联层）
（此处填入：Analyzer-B 回填的跨产品竞争态势分析）

## 🤖 下一步预测（AI 推测）
> 以下为 LLM 推断，非官方事实，仅供参考。

（此处填入：Synthesizer 生成的趋势预测，标注 ai_generated + confidence）
```

#### 实体四：发布记录（Release）

```markdown
---
tags:
  - release
  - product-name
date: 2026-01-15
version: "2.5.0"
product: "[[Product Name]]"
source_url: https://example.com/changelog/2.5.0   # 原文链接：引导回源，不全文转载
changes_count: 3
---

# Product Name v2.5.0

## 摘要与原文（版权友好）
（此处填入：Extractor 生成的 2-3 句**中性转述**摘要，不全文转载官方 changelog）

> 原文请见：[官方 Release Notes](https://example.com/changelog/2.5.0)。
> 关键短引用以 Change Card 的 `evidence.quote` 形式保留（合理引用范围内）；
> 完整原始快照仅存于 `_pipeline/snapshots/`（不入 Git、不公开发布），供改写检测与人工核查。

## 包含的差异卡片
- [[Change: 引入新功能 A]]
- [[Change: 架构调整 B]]
- [[Change: 定价策略 C]]

## 综合影响评级
（此处填入：LLM 对本次 Release 所有变化的整体影响等级评估）
```

#### 实体五：信号卡片（Signal）

**定位**：L1 信号层是用户进入网站后看到的第一屏内容，是产品价值的门面。Signal 不是
L2 档案的重复，而是**从每日新增 Change Cards + Alerts 中提炼出的叙事**——回答
"今天这个行业发生了什么值得注意的事"。

Signal 由 LLM 自动生成草稿，**必经人工审核**（属审核分级中的 Tier B，见 11.1）后
发布到首页。每张 Signal 是一个可独立消费的判断单元：

```markdown
---
type: signal
date: 2026-04-23
status: published        # draft / reviewed / published
generated_by: llm         # llm / human
themes:
  - agent-mode
products_involved:
  - "[[Cursor]]"
  - "[[Windsurf]]"
  - "[[GitHub Copilot]]"
change_cards_cited:
  - "[[Cursor 2026-04-23 agent-shell]]"
  - "[[Windsurf 2026-04-23 agent-approval]]"
  - "[[Copilot 2026-04-23 agent-preview]]"
impact: paradigm-shift     # 取所引用 Change Cards 中的最高 impact
source_alerts:
  - "[[Alerts/2026-04-23-agent-spike]]"
---

# Signal：三家产品同日发布 Agent 功能

## 发生了什么
Cursor、Windsurf、GitHub Copilot 在同一天发布了各自的 Agent 模式相关功能：
- Cursor：支持自动执行 Shell 命令（[[Cursor 2026-04-23 agent-shell]]）
- Windsurf：引入审批式 Agent 工作流（[[Windsurf 2026-04-23 agent-approval]]）
- Copilot：开放 Agent 预览版（[[Copilot 2026-04-23 agent-preview]]）

## 为什么值得关注
这是「Agent 模式」在 AI 编程助手领域首次出现**同日集中发布**，表明该方向已从
早期探索进入主流产品的战略共识阶段。三家采取了不同路线（自动执行 vs 审批式 vs
预览），竞争格局正在分化。

## 🤖 AI 生成说明
> 本 Signal 由 LLM 从当日新增 Change Cards 自动生成，经人工审核后发布。
```

**Signal 与 L3 洞察报告的区别**：

| | Signal | L3 洞察报告 |
|--|--------|-------------|
| 时效性 | 当日/当周 | 月度/季度 |
| 触发源 | 每日新增事实的自动聚合 | 主题积累到一定厚度后的深度分析 |
| 形态 | 3 句话摘要 + 3-5 条 bullet | 长文 + 竞争格局矩阵 + 预测 |
| 人工介入 | 必经人工审核（Tier B，见 11.1） | 必须人工精修 |
| 消费场景 | 首页、Newsletter、RSS | 专题报告页、PDF 下载 |

### 5.2 Obsidian Vault 目录结构

```
chronolog-vault/
├── _assets/                    # 产品 Logo、截图等
├── _templates/                 # Obsidian 模板
│   ├── product-template.md
│   ├── change-template.md
│   ├── release-template.md
│   └── theme-template.md
├── _scripts/                   # Python 自动化脚本
│   ├── sources.yaml            # 声明式数据源配置
│   ├── themes.yaml             # 受控主题词表（见 5.3）
│   ├── collect.py              # 数据采集（快照 + diff）
│   ├── extract.py              # LLM 提取（生成 Change Cards JSON，仅事实层）
│   ├── analyze_a.py            # LLM Analyzer-A（单产品：Eras / evolves_from / verbosity_baseline）
│   ├── analyze_b.py            # LLM Analyzer-B（跨产品：聚类 / diffusion / 关联回填）
│   ├── silence_monitor.py      # Python 统计脚本（沉默检测，无 LLM）
│   ├── synthesize.py           # LLM 综合（生成 Theme MOC JSON）
│   ├── writer.py               # JSON → Markdown 渲染器（确定性，无 LLM）
│   ├── validate.py             # Schema 校验（在 Writer 渲染前运行）
│   ├── signal_generator.py     # LLM Signal 生成器（从当日变化提炼首页 Signal）
│   ├── metrics.py              # 运行指标汇总（从各阶段输出生成质量报告，见 9.5）
│   ├── run_evals.py            # Prompt 回归评估（黄金样本集，见 9.7）
├── Products/                   # 产品档案
│   ├── Cursor.md
│   ├── Notion.md
│   └── Linear.md
├── Changes/                    # 差异卡片（按产品分子目录；theme 仅存 frontmatter，路径不含可变维度，见 9.6）
│   ├── Cursor/
│   ├── Notion/
│   └── Linear/
├── Releases/                   # 发布记录（按产品分子目录）
│   ├── Cursor/
│   │   ├── 2026-01-15-v0.25.md
│   │   └── 2026-03-20-v0.30.md
│   └── Notion/
├── Themes/                     # 主题演化 MOC
│   ├── context-window.md
│   ├── pricing-model.md
│   └── agent-mode.md
├── Signals/                    # L1 信号卡片（每日首页内容）
│   ├── 2026-04-23-agent-spike.md
│   └── 2026-04-22-pricing-shift.md
├── Alerts/                     # 弱信号：沉默检测 + 改写检测
│   ├── 2026-04-23-cursor-silence.md   # 格式：YYYY-MM-DD-{product}-silence.md
│   └── 2026-03-22-cursor-rewrite.md
├── _metrics/                   # 运行质量指标报告（入 Git，可审计，见 9.5）
│   └── 2026-04-23-report.json  # 格式：YYYY-MM-DD-report.json
├── _evals/                     # Prompt 回归黄金样本集 + 审核修正回流（入 Git，见 9.7）
│   ├── extractor/              # 输入 release 原文 → 期望 Change Cards JSON
│   └── review-edits/           # PR 审核修正 diff 归集（few-shot 素材库）
└── quartz.config.ts            # Quartz 站点配置
```

### 5.3 主题词表治理（Theme Vocabulary Governance）

「多产品行业趋势」这一目标**完全依赖主题标签的一致性**。若放任 LLM 在 Extractor 阶段自由命名主题，会产生标签碎片化（`context-window` / `context-length` / `long-context`），导致同一趋势无法跨产品聚合——这会直接摧毁趋势分析能力。

因此引入**受控主题词表**机制：

**1. 规范词表（`_scripts/themes.yaml`）**

```yaml
themes:
  - slug: context-window
    display_name: 上下文窗口
    aliases: [context-length, long-context, context-expansion]
    category: capability
    status: official
  - slug: agent-mode
    display_name: Agent 模式
    aliases: [autonomous-agent, agentic]
    category: paradigm
    status: official
  - slug: pricing-model
    display_name: 定价模式
    aliases: [pricing, billing, usage-based-pricing]
    category: business
    status: official
```

**2. Extractor 约束**：提取时**必须**从 `themes.yaml` 的 `slug` 中选择；命中
`aliases` 时自动归一化到规范 `slug`。

**3. 候选主题晋升机制**：当一个变化无法匹配任何现有主题时，Extractor 将其标
为 `theme: __candidate__` 并附带建议名称，写入候选区，**不直接进入正式主题**。
由 Analyzer 汇总候选主题，经**人工审核 gate**（见第 11 节）确认后，才追加到
`themes.yaml` 成为 `status: official`，并回填相关 Change Cards（仅更新 frontmatter
的 `theme` 字段，零文件移动、零链接重写，见 9.6）。

**4. 初版词表 Bootstrap（第一版词表从哪来）**：词表初始质量直接决定 Extractor 的
提取质量，不应凭空编写。流程：

1. 对历史回填数据（见 6.2.2）先跑一轮**自由打标模式**的 Extractor（不注入词表，
   允许 LLM 自由命名主题）
2. 对产生的自由标签做聚类（embedding + 频次统计），输出候选主题簇与各簇示例卡片
3. 人工从聚类结果中筛选、命名、合并出初版 `themes.yaml`（含 aliases），再以正式
   词表重跑正式提取
4. 自由打标的结果仅用于 bootstrap，不进入正式 Vault

这一机制天然契合「自动生成 + 人工审核 gate」的整体策略：词表演进本身（从 bootstrap
到候选晋升）也是受控、可审计、可回滚的。

---

## 6. LLM 处理管线（Pipeline）

### 6.1 管线总览

```
┌──────────┐   ┌──────────┐   ┌────────────┐   ┌────────────┐   ┌──────────────┐
│ Collector│──▶│ Extractor│──▶│ Analyzer-A │──▶│ Analyzer-B │──▶│ Synthesizer  │
│  采集器   │   │  提取器   │   │ 单产品分析  │   │ 跨产品分析  │   │   综合器      │
└──────────┘   └──────────┘   └────────────┘   └────────────┘   └──────┬───────┘
                                    ▲                                   │
                               ┌────┴─────┐                     ┌──────┴──────┐
                               │ Silence  │                     │   Writer    │
                               │ Monitor  │                     │ JSON→Markdown│
                               │(Python脚本)                    │   写入器     │
                               └──────────┘                     └──────┬──────┘
                                                                        │
                                                                 ┌──────┴──────┐
                                                                 │Signal Gen.  │
                                                                 │  信号生成器   │
                                                                 │  (LLM→JSON)  │
                                                                 └─────────────┘
```

**管线拆分说明**：

原单一 Analyzer 因职责过重（同时处理单产品分析、跨产品聚类、沉默检测、扩散分析、候选
主题汇总等多类任务），会导致 LLM 在所有方向都做得平庸。v1.3 起拆分为四个独立单元：

- **Analyzer-A**（per-product，可并行）：处理单产品内部逻辑，输入有界
- **Analyzer-B**（cross-product，需全局视图）：处理跨产品聚类与扩散，在 A 完成后运行
- **Silence Monitor**（Python 脚本，无 LLM）：纯统计逻辑，零 token 成本，结果可复现
- **Signal Generator**（LLM，增量输入，v1.4 加入）：从每日新增 Change Cards + Alerts 中
  生成 L1 信号卡片，在 Writer 渲染后运行，直接消费已渲染摘要

### 6.2 各阶段职责与 Prompt 策略

| 阶段 | 类型 | 输入 | 输出 | 职责 |
|------|------|------|------|------|
| **Collector** | Python 脚本 | 数据源 API / RSS / GitHub | 原始文本快照 + 改写 diff | 拉取并保存**时间戳快照**；与上次快照做差分，识别新增/改写（见 6.2.1）。无需 LLM |
| **Extractor** | LLM | 原始 Changelog 文本 | Change Cards JSON 草稿（**仅事实层**） | LLM 将单次 Release 拆分为多张 Change Card，填充差异描述、主题标签（须取自受控词表）、影响等级、evidence。**不**生成跨卡片关联。**输出 JSON**，由 Writer 渲染 |
| **Analyzer-A** | LLM（per-product，可并行） | 单产品全量 Change Cards | Eras + evolves_from + verbosity_baseline | ① 识别**单产品演化阶段（Eras）**与战略转折点；② 构建**产品内演化链**（`evolves_from`）；③ 计算 `verbosity_baseline`（历史平均每版本卡片数）。输入有界，可按产品并行运行。**仅对本次有新增卡片的产品触发**：Eras 持久化复用，新证据仅触发受影响阶段边界的重评估（OQ-1 决策） |
| **Analyzer-B** | LLM（cross-product，增量视图） | 本次新增/更新的 Change Cards + 活跃主题的历史上下文（K≈20/主题）+ Analyzer-A 结果 + 派生索引 | 主题聚类 + 关联回填 + diffusion + 候选主题 | ① 只处理**活跃主题**（增量预过滤）；② 对每个活跃主题取 top-K 历史上下文（embedding + 时间近邻混合排序）；③ **回填** `related_changes`、`diffusion`（已追踪产品集内的扩散角色与时间差）、「行业坐标」；④ 汇总候选主题待审。输入从 O(全部历史) 降至 O(活跃主题 × K)
| **Silence Monitor** | Python 脚本（**无 LLM**） | 各产品频率基线 + 配置 | 沉默信号 Alerts | 纯统计逻辑：按各产品 `silence_window/periods/factor` 配置计算更新频率，低于阈值则生成 Alert。从 LLM 移出，零 token 成本，结果完全可复现 |
| **Synthesizer** | LLM | Analyzer-B 聚类 + Eras | Theme MOC JSON + 推测层 | LLM 生成主题演化叙事（时间线、竞争格局），以及标注 `ai_generated` 的战略意图/预测。**输出 JSON** |
| **Writer** | Python 脚本 | 各阶段输出的 **JSON** + **现存 Markdown 状态** | 最终 Markdown 文件 | 按**所有权分区**幂等渲染（见 6.5）：只重写机器标记区块与机器 frontmatter 字段，区块外的人类内容结构上不可能被覆盖；检测到机器区被人工修改时保留人工版本并标记 `merge_conflict` 入 DLQ。渲染前按 `card_id` 对账，决定就地更新还是新建（见 9.6）。格式由代码确定性控制 |
| **Signal Generator** | LLM | 当日新增 Change Cards + Alerts + Theme MOC 摘要 | Signal JSON（首页叙事） | 从每日新增事实中提炼 3-5 条首页 Signal，每条含「发生了什么」「涉及哪些产品」「为什么值得关注」。**输出 JSON**，由 Writer 渲染为首页 `Signals/` 下的 Markdown |

> **Signal 生成时机**：Signal Generator 在 Writer 渲染完全部档案内容后运行，直接消费
> Writer 已生成的摘要（而非重新喂原始文本给 LLM），避免重复 token 消耗。首页 `index.md`
> 中的「本周信号」列表由 `writer.py` 构建时生成到首页的机器标记区块中（见 6.5）——
> Quartz 没有 Dataview 式的运行时查询聚合，「自动」必须发生在构建时而非运行时。

> **关键数据流说明**：
> 1. `collect.py` 采集快照 → `extract.py` 产出事实层 JSON
> 2. `validate.py` 校验 JSON（见 9.2.1），失败项进入 DLQ，成功项继续
> 3. `analyze_a.py` 补充单产品关联（**多进程并行**，每个产品独立进程）
> 4. `silence_monitor.py` **独立于 LLM 阶段**，可与 Analyzer-A 并行运行，
>    在 Collector 完成后即可执行，不阻塞 LLM 管线
> 5. `analyze_b.py` 补充跨产品关联（需 Analyzer-A 全部完成）
> 6. `synthesize.py` 生成叙事 JSON → `writer.py` 按所有权分区幂等渲染 Markdown（见 6.5）
> 7. `signal_generator.py` 生成首页 Signal → `validate.py` 第二轮（链接完整性）
>    → `metrics.py` 汇总质量报告
>
> 所有 LLM 阶段输出 JSON 而非直接 Markdown，由 `writer.py` 负责最终渲染（见 6.4、6.5）。

### 6.2.1 采集快照与改写检测（Snapshot & Rewrite Detection）

我们追踪的是「演化」，那么**变化本身就是数据**。很多产品会**悄悄改写历史
changelog**——删项、改措辞、调日期、下线某功能却不公告。这种「修订」恰恰是高价值
信号，是别人都不做的独特来源。因此 Collector 不是「拉取最新」，而是「**快照 +
差分**」：

**1. 时间戳快照**：每次抓取保存原始内容的不可变快照，按抓取时间归档：

```
_pipeline/
└── snapshots/
    └── Cursor/
        ├── 2026-03-15T06-00Z.raw.md      # 每次抓取的原始快照
        ├── 2026-03-22T06-00Z.raw.md
        └── latest.hash                    # 内容指纹，用于快速判断是否变化
```

**2. 差分与分类**：与上一次快照比对，把变化分为三类，分别下游处理：

| 变化类型 | 含义 | 处理 |
|---------|------|------|
| **新增（added）** | 出现新的 release / 条目 | 正常进入 Extractor 生成 Change Card |
| **改写（modified）** | 已存在的历史条目被修改 | 生成「改写检测」记录，作为信号告警 |
| **删除（removed）** | 历史条目被悄悄移除 | 高优先级信号——可能是功能下线/战略收缩 |

**3. 改写检测输出**：对 modified / removed，生成 `Alerts/{date}-{product}-rewrite.md`，
包含 before/after diff、改动类型、时间，并标注「🤖 可能含义」（AI 推测）。这与
6.3「沉默检测」并列，构成 ChronoLog 的两类独特弱信号源：**「没发声」（沉默）**与
**「偷偷改口」（改写）**。两类弱信号在站点上产品化为一级版块「弱信号观察站」（见 7.2）。

**4. 归一化与降噪（防止误报洪水）**：直接对原始页面快照做 diff 会被噪音淹没——相对
时间戳（"3 days ago"）、浏览计数、推荐位、跟踪参数的变化都会触发假「改写」告警，而
误报会迅速摧毁这一信号的可信度。因此差分在**归一化文本**上进行：

- 先做正文抽取（readability 类算法，剥离导航/页脚/侧栏/评论区）
- 再做文本归一化（去除相对时间、计数器、空白差异、URL 跟踪参数）
- `latest.hash` 与三类差分均基于归一化文本计算；原始快照仍完整保留供人工核查

> 实现注意：快照仅保留原始文本，不入 Git（体积可能大），但 `latest.hash` 与生成的
> Alert 入库以保留审计痕迹；改写检测同样定位为「信号非结论」。

### 6.2.2 历史回填（Historical Backfill）

「主题演化」「扩散分析」「Eras 叙事」的价值全部依赖**时间纵深**。若只从接入之日起
向前采集，上线后数月内站点几乎没有可看的演化内容，北极星指标（研究者回访）无从谈起，
沉默检测也没有基线可用。而 tier-1 数据源（GitHub Releases API / RSS 存档）天然自带
完整历史——**回填是成本最低的冷启动手段**，是 Phase 1 的一等任务而非可选优化。

**机制**：

- `sources.yaml` 按产品声明回填策略：`backfill: full`（拉取全部可得历史，tier-1
  默认）/ `backfill: {since: <date>}` / `backfill: none`
- 产品**接入时**执行一次回填（`python _scripts/collect.py --backfill <product>`，
  CI 中经 `workflow_dispatch` 手动触发），之后转入每日增量采集
- 回填数据走与增量**完全相同**的管线（Extractor → Analyzer → Writer → PR），仅在
  PR 中按产品分批呈现（每批 1 个产品），避免一次性数千张卡片压垮审核
- 回填收益：tier-1 产品接入当天即拥有 ≥12 个月历史——沉默检测基线直接可用（见 6.3）、
  Eras 识别有足够素材、`diffusion` 判断可信度显著提升、上线首日站点即有可探索的纵深

**回填的连锁效应（常态而非边缘情况）**：后接入的产品会带着**更早的历史**进入系统，
可能改写已有主题的扩散顺序（出现更早的 originator）。Analyzer-B 的「扩散时间线修正」
（附录 B-2 要求 5）正是为此设计，修正补丁同样走 PR 审核。`diffusion` 结论应理解为
「基于当前已追踪集合、当前时点的判断」——`tracked_products_count` 字段正是供读者
评估这一可信度的。

### 6.3 沉默检测机制

**实现方式**：`silence_monitor.py`——纯 Python 统计脚本，**不调用 LLM**。沉默检测
是纯频率统计，不需要语义理解，从 LLM 移出后：① 零 token 成本；② 结果完全可复现，
不受 LLM 随机性影响；③ 可在每次 Collector 运行后立即执行，不依赖 LLM 阶段完成。

**定位**：产出的是**信号（signal）而非结论**。changelog 不更新的原因极多（合并到
月报、改用站内通知、小团队随机性、节假日），因此 Alert 只提示「值得关注」，不下
「该产品在收缩」这类断言。

**频率基线计算**：
- 对每个产品，统计过去 12 个月的更新频率（平均每月 release 数）
- 建立动态基线，允许季节性波动（如年底通常较慢）

**异常触发条件（阈值按产品可配置）**：
- 默认：当前周期更新数 < 基线 × 50%，且连续 N 个周期为 0
- `silence_window`（周期长度）与 `silence_periods`（连续周期数）在 `sources.yaml`
  中按产品配置——周更产品与月更产品应使用不同阈值，避免对月更产品误报或对周更
  产品反应迟钝

```yaml
# sources.yaml 中的产品级配置示例
track_silence: true
silence_window: month        # week / month / quarter
silence_periods: 2           # 连续多少个 window 触发
silence_baseline_factor: 0.5 # 低于基线的比例阈值
```

**冷启动基线**：tier-1 产品经历史回填（见 6.2.2）后，接入当天通常即拥有 ≥12 个月
历史，可直接计算正式基线；冷启动逻辑仅适用于**无可回填历史**的数据源。对追踪时间
不足 12 个月的产品，使用**已有数据的实际均值**作为基线；若不足 4 周，则暂停沉默检测
（标记为 `silence_tracking: pending`），避免误报。

**输出**：自动生成 `Alerts/{date}-{product}-silence.md`（日期格式 YYYY-MM-DD，与全文
命名规范一致），内容包含：
- 沉默时长统计与历史对比
- 🤖 可能原因推测（标注为 AI 推测，仅供参考）
- 「值得关注的替代信号」（如该产品的 GitHub 分支活跃度、创始人推特等）

### 6.4 Prompt 设计原则

- **LLM 输出 JSON，Writer 渲染为 Markdown**：所有 LLM 阶段统一输出结构化 JSON，由
  `writer.py` 确定性渲染为 Obsidian Markdown。理由：① LLM 直接输出 YAML 格式不稳定；
  ② JSON schema 校验（`validate.py`）在渲染前执行；③ Markdown 格式由代码控制，可预测
- **双链由 Writer 注入**：LLM JSON 中用笔记 ID 引用，`writer.py` 渲染时统一转换为
  `[[双链]]` 格式，避免 LLM 拼接 Markdown 语法导致转义问题
- **推测层按需生成**：战略意图推测仅对 `impact ∈ {significant, paradigm-shift}` 的卡片
  生成；`incremental` 卡片跳过推测——既省 token，也避免低价值推测稀释整体可信度
- **所有权分区渲染（规格见 6.5）**：`writer.py` 不做「双向合并」，只幂等重写机器拥有的
  标记区块与 frontmatter 机器字段；人类内容在区块之外，结构上不可能被覆盖
- **主题受控**：Extractor Prompt 中注入 `themes.yaml` 词表，强制 LLM 从受控词表选主题 slug
- **中间产物可审查**：JSON 输出先落到 `_pipeline/` 暂存区，`validate.py` 校验通过后渲染
- **版本化 Prompt**：Prompt 文本放在 Git 仓库中，与代码一起版本管理

### 6.5 Writer 所有权模型（Ownership over Merge）

> **为什么放弃双向合并**：v1.7 及以前的「machine_hash 全文件比对 + 字段级双向合并」
> 存在两个缺陷：① 记录的是 JSON 内容的 hash，却拿渲染后文件内容的 hash 去比对，二者
> 永不相等，按字面实现会把所有文件误判为「已被人工修改」；② 「机器控制区始终覆盖」与
> 「冲突时保留人工版本」两条规则互相矛盾；且没有 base 版本就无法做真正的三方合并。
> v1.8 起改为**所有权分区**，从结构上消灭合并问题——不需要 base 版本，合并逻辑退化为
> 「区域替换」。

**1. 正文：标记区块所有权（machine region）**

机器生成的正文一律写在显式标记之间，`writer.py` 每次运行只替换标记内的区域（幂等
渲染），标记之外的一切（人工小节、批注、错别字修正）天然不受影响——这是 codegen
工具的成熟做法：

```markdown
## 行业坐标（关联层 · diffusion）
<!-- chronolog:begin region="diffusion" -->
（机器区块：每次运行由 writer.py 整体重写）
<!-- chronolog:end -->

## 编辑笔记
（人类自由书写区：writer.py 永不触碰标记之外的内容）
```

**2. Frontmatter：字段所有权分区**

- **机器字段**（始终由 Pipeline 写入；人工直接修改会在下次运行被重写）：
  `related_changes`、`diffusion`、`evolves_from`、`eras`、`verbosity_baseline`、
  `card_id`、`extractor_version`、`machine_hash` 等事实层/关联层/管线元数据字段
- **人类字段**（Pipeline 永不写入）：`human_notes` 及人工新增的任意自定义字段
- **人工覆盖机制（`human_overrides`）**：人类若不认同某个机器字段的值（如想剔除一条
  错误的 `related_changes`），**不要直接改机器字段**，而是写入 `human_overrides:` 块。
  该块由人类独占，站点渲染时优先于同名机器字段，Pipeline 读取但永不修改：

```yaml
human_overrides:
  related_changes:             # 展示以此为准；机器判断仍保留在机器字段中，可对比审计
    - "[[Copilot 2026-02 context-expansion]]"
  reason: "Windsurf 那条关联判断有误，已人工剔除"
```

**3. 改动检测（`machine_hash` 的新定义）**

`machine_hash` = 全部机器区块渲染内容 + 机器 frontmatter 字段（归一化后、不含该字段
本身）的 SHA-256。`writer.py` 运行时若发现当前文件的机器区域 hash 与记录值不一致，
说明有人**在机器区域内**做了修改：

- **默认策略（保守）**：本次跳过该文件的机器更新、保留人工版本，标记
  `merge_conflict: true` 入 DLQ，并在 PR body 中列出 diff，提示「请将修改移至人类区
  或 `human_overrides`，或恢复机器区后重跑」
- 人类区的任何修改**不会**触发该机制（hash 不覆盖人类区）——这是与旧方案的本质区别：
  绝大多数人工精修不再产生任何冲突，`merge_conflict` 预期趋近于零

**4. 各实体的默认区块划分**

| 实体 | 机器区块 | 人类区 |
|------|---------|--------|
| Change Card | 差异描述、证据溯源、演化链、行业坐标、推测层 | 「编辑笔记」小节 + `human_overrides` |
| Product 档案 | Eras、演化概览时间线、frontmatter 元数据 | 「产品定位」精修、自由批注 |
| Theme MOC | 演化时间线、Mermaid 对比时间线、竞争格局、预测 | 「编辑观点」小节 |
| Signal | what_happened / why_it_matters（仅生成一次，发布后 Pipeline 不再重写） | 全文均可在 PR 审核中人工修订 |
| 首页 index.md | 「本周信号」列表区块 | 其余全部内容 |

---

## 7. 信息架构与内容分层

### 7.1 三层信息结构

ChronoLog 面向用户的内容不是单一平面的「所有更新」，而是有层次的信息架构：

| 层级 | 名称 | 内容 | 受众 | 更新频率 |
|------|------|------|------|---------|
| **L1** | **信号**（Signal） | 本周/本月行业关键变化精选，人工/LLM 摘要 | 所有访客 | 每周 |
| **L2** | **档案**（Archive） | 每个产品的完整演化时间线 + 所有 Change Cards | 研究者 | 实时 |
| **L3** | **洞察**（Insight） | 跨产品主题演化分析报告、预测、竞争格局解读 | 深度用户 | 每月 |

### 7.2 各层形态

**L1 信号层**：
- 网站首页为「本周信号」视图
- 每条信号包含：发生了什么、涉及哪些产品、为什么值得关注（3 句话以内）
- **生成方式**：由 Signal Generator 从当日新增的 high-impact Change Cards（`paradigm-shift`
  或 `significant`）+ 异常 Alerts（沉默、改写、主题突然升温）中自动提炼，输出 JSON
  草稿，经人工审核（Tier B，见 11.1）后发布到 `Signals/`
- **编辑 SLA**：理想情况下每日更新；审核者可在 PR 中编辑 Signal 文案或拒绝发布；
  审核者缺席时 Signal 顺延至下次审核（Rolling PR 累积，见 11.1），不自动发布
- **Newsletter 来源**：Signal 是 Newsletter 的素材底座，L3 报告是 Newsletter 的深度内容
- 用户反馈：每条 Signal 页脚提供「🚩 反馈此信号」链接，跳转至预填内容的 GitHub Issue

**L2 档案层**：
- 产品页：完整时间线 + 按主题筛选的 Change Cards
- 主题页：跨产品同一主题的对比时间线
- 搜索：全文检索所有 Change Cards

**弱信号观察站（Silence & Revisions，横跨 L1/L2）**：

沉默检测与改写检测是 ChronoLog 最难被复制的差异化能力（见 2.3、6.2.1），不应只是
埋在 `Alerts/` 目录里的告警文件，而应产品化为站点的一级版块：

- 独立页面 `/weak-signals`：「谁沉默了」（按沉默时长排序的产品列表 + 历史对比）与
  「谁悄悄改口」（最近的改写记录，含 before/after diff 摘要）
- 该版块是 Signal Generator 的常规素材源：异常沉默与高价值改写默认进入当日 Signal 候选
- 叙事价值：「我们连产品悄悄改写历史都帮你盯着」远比「又一个 changelog 聚合器」有说服力

**L3 洞察层**：
- 定期发布的「主题演化报告」（如《2026 Q1：AI 编程助手的 Agent 模式竞赛》）
- 包含：事件时间线、竞争格局矩阵、战略意图分析、下一步预测
- 形态：长文 + Canvas 可视化图谱

### 7.3 用户旅程示例

1. **访客** → 看到 L1 首页「本周 5 个值得关注的变化」 → 点击感兴趣的信号
2. **研究者** → 进入 L2 产品页 / 主题页 → 浏览 Change Cards → 点击双链跳转到关联产品
3. **深度用户** → 阅读 L3 洞察报告 → 下载 PDF / 订阅邮件获取更新

---

## 8. 可视化与交互设计

### 8.1 Obsidian Canvas：演化博弈图谱

Obsidian 的 Canvas 功能（`.canvas` 文件为 JSON 格式）可以用来构建**交互式演化图谱**。

**应用场景**：「2026 上下文窗口竞赛」
- 三个节点：Cursor、Copilot、Windsurf
- 每个节点伸出箭头指向各自的关键 Change Card
- 箭头标注时间差（如 Copilot 先发 → 2 周后 Cursor 跟进）
- 中心节点为「主题」本身

**面向用户的产品形态**：
- 在 Quartz 网站上，通过自定义 React 组件渲染 `.canvas` 文件
- 用户可点击任意节点，展开对应的 Change Card 详情
- 支持缩放、拖拽探索

### 8.2 时间线对比视图

在主题页面（Theme MOC）中，提供一个**多产品对比时间线**：

```
2026-01 ──┬── Copilot: 100K 上下文
          │
2026-03 ──┼── Cursor: 200K 上下文
          │
2026-03 ──┴── Windsurf: Tab 级上下文
```

**实现方式（两阶段，核心 aha 视图不等待 Phase 4）**：

- **Phase 1 起（零前端开发）**：Quartz v4 原生支持 Mermaid。`writer.py` 渲染 Theme MOC
  时，从该主题下的 Change Cards **构建时生成 Mermaid timeline/gantt 代码块**（纵向按
  产品分组、横向按日期排列，节点链接到对应卡片）。「跨产品对比时间线」这一招牌视图
  在 MVP 即可交付，成本几乎为零
- **Phase 4（验证后升级）**：替换为可交互的自定义 React 组件（点击节点展开 Change
  Card、缩放、按影响等级筛选），Mermaid 版本保留为降级方案

### 8.3 关系图谱（Graph View）

Quartz 原生支持基于双链的关系图谱。对于 ChronoLog，这尤其有价值：
- 节点类型：产品（大节点）、Change（中节点）、主题（大节点）、发布（小节点）
- 颜色编码：按主题标签着色
- 交互：点击节点聚焦，显示其直接关联网络

---

## 9. 技术实现规范

### 9.1 声明式数据源配置

新增追踪产品无需改代码，只需修改 `_scripts/sources.yaml`：

```yaml
products:
  - name: Cursor
    display_name: Cursor
    feed_type: github_releases      # tier-1：结构稳定，MVP 首选
    repo: getcursor/cursor
    backfill: full                  # 接入时拉取全部可得历史（tier-1 默认，见 6.2.2）
    themes: [ai-coding, context-window, agent-mode, pricing]
    track_silence: true
    silence_window: month
    silence_periods: 2
    language: en

  - name: Notion
    display_name: Notion
    feed_type: blog_rss             # tier-1：RSS 稳定
    url: https://www.notion.so/release-notes/rss
    backfill: full
    themes: [productivity, ai-integration, database, collaboration]
    track_silence: true
    silence_window: month
    silence_periods: 2
    language: en

  - name: Linear
    display_name: Linear
    feed_type: changelog_page       # tier-2：HTML 爬取，best-effort
    url: https://linear.app/changelog
    css_selector: ".changelog-entry"
    backfill: none                  # tier-2 页面通常无可靠历史存档
    themes: [project-management, workflow-automation]
    track_silence: true
    language: en
```

**数据源分级策略（重要）**：

数据采集是这类产品最常见的失效点。网页结构爬取极易因改版失效，且很多产品的
更新分散在 Discord / Twitter / blog / in-app notes，没有统一 changelog。因此
按可靠性分级，并据此安排实施优先级：

| 级别 | 类型 | 可靠性 | 策略 |
|------|------|--------|------|
| **tier-1** | `github_releases`、`blog_rss` | 高（结构稳定） | **MVP 首选**，优先选取此类产品 |
| **tier-2** | `changelog_page`（HTML + CSS selector） | 低（随改版失效） | best-effort，后置；采集失败仅告警不阻断管线 |
| **tier-3** | 社交媒体 / 散落来源 | 不可靠 | 暂不纳入，明确标注为数据覆盖盲区 |

→ MVP 阶段刻意**只选 tier-1 产品**（AI 编程助手领域多有 GitHub Releases），把
tier-2 列为 Phase 2+ 能力，并在产品页明示数据覆盖率的局限。

### 9.2 管线中间产物规范

Pipeline 各阶段的输出格式：LLM 阶段输出 JSON，Writer 渲染后输出 Markdown，
Silence Monitor 和 metrics.py 直接输出告警文件或报告文件：

```
_pipeline/
├── 2026-04-23/
│   ├── 01-collected/          # 原始文本快照
│   ├── 02-extracted/          # Extractor 输出 JSON（Change Cards 事实层草稿）
│   ├── 03a-analyzed-per/      # Analyzer-A 输出 JSON（单产品：Eras / evolves_from / verbosity_baseline）
│   ├── 03b-analyzed-cross/    # Analyzer-B 输出 JSON（跨产品：聚类 / diffusion / 关联回填）
│   ├── 03c-silence/           # Silence Monitor 输出（Python 生成，无 LLM）
│   ├── 04-synthesized/        # Synthesizer 输出 JSON（Theme MOC + 推测层）
│   ├── 05-rendered/           # Writer 渲染的 Markdown（validate.py 校验通过后生成）
│   ├── 06-signals/            # Signal Generator 输出 JSON（首页 Signal 草稿）
│   ├── 07-metrics/            # metrics.py 输出的运行报告（见 9.5）
│   └── index/                 # 派生查询索引（index.sqlite + index.json + embedding）
```

只有依次通过 **validate.py 第一轮校验**（JSON schema）→ **Writer 渲染**
（JSON→Markdown）→ **validate.py 第二轮校验**（关联层 + 链接完整性，见 9.2.1）
→ **人工审核 gate**（见第 11 节）的内容才会从 `_pipeline/` 移动到 Vault 正式目录。

### 9.2.1 输出验收 Checklist 与死信队列（DLQ）

**`validate.py` 的运行时机与覆盖范围**：在 Extractor 输出 JSON 之后、Writer 渲染之前
运行。校验范围涵盖所有 LLM 阶段的 JSON 输出（Extractor、Analyzer-A/B、Synthesizer），
包括 diffusion 字段（来自 Analyzer-B）。校验分两轮：
- **第一轮**（Extractor 后）：校验基础 schema 和事实层字段
- **第二轮**（Writer 渲染后、PR 创建前）：校验关联层字段（含 `diffusion.scope`、
  `evolves_from` 有效性），并对渲染产物做**链接完整性校验**：全 Vault 双链可解析、
  Signal 引用的 Change Card 存在且未被拒、`evolves_from` 不指向 `superseded` 卡片

**局部容错原则**：任一项不通过时，**不应中断整个 Pipeline**，而是将该条 JSON 隔离
入死信队列（DLQ），其余验证通过的数据继续后续阶段。

**DLQ 存储路径**：`_pipeline/dlq/{date}-{product}-failed.json`（不入 Git）

**DLQ 生命周期**：
1. DLQ 条目**不阻塞**同一产品后续 release 的处理
2. 每次 pipeline 运行时，`validate.py` 自动重试上次 DLQ 中的条目（最多重试 3 次）
3. 重试成功则移出 DLQ；超过 3 次仍失败则标记 `status: abandoned`，并在周报中提示人工介入
4. 人工修复后可手动触发 `python _scripts/validate.py --retry-dlq` 重新校验

**校验规则列表**：
- [ ] **Schema 合规（JSON）**：含全部必填字段（`type`/`product`/`date`/`theme`/`impact`/`evidence`）
- [ ] **主题合规**：`theme` 取自 `themes.yaml` 的 `slug`，或为 `__candidate__`（带建议名）
- [ ] **影响等级合规**：`impact ∈ {incremental, significant, paradigm-shift}`
- [ ] **diffusion.scope**：若含 diffusion 字段，`scope` 必须为 `tracked-products-only`
- [ ] **推测标注**：含主观推断的字段必须有 `ai_generated: true` + `confidence`
- [ ] **无空壳卡片**：`description` 非空且非纯复述标题
- [ ] **evidence 非空**：事实层每张卡片必须含至少一条 `evidence`（含 `source_release` + `quote`；`anchor` 可选）
- [ ] **card_id 确定性**：`card_id` 存在且符合 9.6 生成规则（重跑同一 release 不变）
- [ ] **链接完整性（第二轮）**：渲染产物中全部 `[[双链]]` 可解析；Signal 引用的卡片存在
- [ ] **主题离群软标记**：卡片 embedding 距其主题质心过远时标注 `theme_outlier: true`（仅提示审核注意，不入 DLQ，见 9.7）

**人工审核抽查点**：主题归类是否准确（优先核对带 `theme_outlier` 标记的卡片）、是否
存在幻觉事实、影响等级是否合理、`diffusion.role` 中的 originator 判定是否合理、机器
区块是否被误改（`merge_conflict` 标记，见 6.5）。

### 9.2.2 LLM 成本粗估

便于评估可持续性（按提取用轻量模型、综合用强模型的分层策略）：

| 项 | 估算 | 说明 |
|----|------|------|
| 单 release token | 输入 ~2K + 输出 ~1.5K | Extractor |
| 每日新 release（10 产品）| ~5-15 条 | |
| Extractor（轻量模型）| 约 $0.01-0.05 / 天 | |
| Analyzer-A（轻量模型，per-product 并行）| 约 $0.02-0.08 / 天 | 只处理增量卡片，可并行 |
| Analyzer-B（强模型，需全局视图，按主题批处理）| 约 $0.05-0.15 / 天 | |
| Silence Monitor | $0 / 天 | 纯 Python，**无 LLM 调用** |
| Synthesizer（强模型）| 约 $0.05-0.15 / 天 | |
| **月度量级** | **个位数美元**（10 产品规模）| 拆分后 Analyzer-A 改用轻量模型，总成本略降 |

成本主要随产品数线性增长。沉默检测移出 LLM 后，高频运行场景（如增加追踪频率）
不产生额外 token 成本。降本手段：原始文本预过滤（小更新不送 LLM）、分层模型（轻量
做提取，强模型做综合）、低频产品降低采集频率（见第 14 节风险对策）。

### 9.3 Quartz 增量构建策略

当 Vault 规模增长（追踪 100+ 产品）时，全量构建会变慢。

**分站策略**：
- **主站**：只构建最近 2 年的活跃内容，保证构建速度与首屏体验
- **历史归档**：2 年前的内容用 Quartz `ignorePatterns` 从主站排除，构建为独立的
  归档子站（`/archive`），按需访问
- **完整 Vault 下载**：提供打包下载，供用户本地用 Obsidian 打开完整历史——这既是
  「完整档案」目标的兜底，也是产品差异化（可离线、可二次研究）

### 9.4 文件命名规范

| 类型 | 命名规则 | 示例 |
|------|---------|------|
| 产品档案 | `Products/{PascalCase}.md` | `Products/Cursor.md` |
| 差异卡片 | `Changes/{product}/{date}-{slug}.md`（路径不含 theme；slug 首次创建后冻结，见 9.6） | `Changes/Cursor/2026-03-15-200k-context.md` |
| 发布记录 | `Releases/{product}/{date}-{version}.md` | `Releases/Cursor/2026-03-15-v0.30.md` |
| 主题 MOC | `Themes/{kebab-case}.md` | `Themes/context-window.md` |
| 沉默警报 | `Alerts/{date}-{product}-silence.md` | `Alerts/2026-04-23-cursor-silence.md` |
| 改写警报 | `Alerts/{date}-{product}-rewrite.md` | `Alerts/2026-03-22-cursor-rewrite.md` |
| 信号卡片 | `Signals/{date}-{slug}.md` | `Signals/2026-04-23-agent-spike.md` |
| 运行报告 | `_metrics/{date}-report.json` | `_metrics/2026-04-23-report.json` |

### 9.5 质量控制与运营指标

系统上线后需要回答「我做得怎么样」——而不是等用户抱怨才发现问题。
以下指标由 `metrics.py` 在每次 pipeline 运行结束后汇总生成，
写入 `_pipeline/metrics/{date}-report.json`，并随 PR 呈递给审核者。

**9.5.1 指标定义**

| 维度 | 指标 | 定义 | 数据来源 | 期望值 |
|------|------|------|---------|--------|
| **提取质量** | 卡片拒绝率 | 人工审核中被编辑或标注错误的 Change Card 数 / 当次 PR 总卡片数（粒度为卡片，非 PR） | 审核者在 PR 中打标记 | < 10%（Phase 1-2），< 5%（Phase 3+） |
| | Schema 合规率 | 通过 validate.py 的记录数 / 总 JSON 记录数 | validate.py | > 98% |
| | DLQ 记录数 | 每次运行进入死信队列的 JSON 条数 | DLQ 目录计数 | < 2 条/天 |
| | 主题精度抽样 | 每周随机抽 20 张卡片人工核对主题归类正确率 | 人工抽样，metrics.py 记录（见 9.7） | > 90% |
| | 断链数 | 渲染产物中无法解析的双链/引用数 | validate.py 第二轮 | 0 |
| **数据源健康** | 采集成功率 | 成功采集的产品数 / 应采集产品数 | collect.py 报告 | > 95% |
| | 失效数据源 | 连续 3 次采集失败的 tier-1 产品数 | 取状态快照 | 0 |
| | 改写检出数 | 每次运行时 detected modified/removed 条目数 | diff 分析 | N/A（信号型指标） |
| **管线健康** | 总运行时长 | pipeline 从 start 到 PR open 的时间 | GitHub Actions 统计 | < 15 min |
| | LLM token 消耗 | 各阶段 tokens 数（输入 + 输出） | LLM API 返回 | 在预算内（参考 9.2.2） |
| | 阶段失败次数 | 各阶段因异常 crash 的次数 | workflow logs | 0 |
| **内容覆盖** | 活跃主题数 | 过去 30 天内有新 Change Card 的主题数 | 派生索引查询 | 取决于追踪产品数 |
| | 产品覆盖率 | 有 > 10 张 Change Card 的产品数 / 总追踪产品数 | 派生索引查询 | > 80% |
| | 主题标签密度 | 平均每个产品覆盖的主题数 | 派生索引查询 | > 3 |
| **审核效率** | 审核周期中位数 | PR open → merge 的时间 | PR 元数据 | < 24 h |
| | 积压 PR 数 | 未合并的 pipeline PR 数 | PR 列表 | < 3 |
| | Tier A 抽查不合格率 | 自动通道抽查样本中需人工修正的比例 | 抽查清单标记 | < 5%（回升则降回全量人审，见 11.1） |

**9.5.2 运行报告**

每次 pipeline 运行结束后，`metrics.py` 生成一份结构化 JSON 报告：

```json
{
  "run_id": "2026-04-23",
  "timestamp": "2026-04-23T06:15:00Z",
  "duration_minutes": 8.3,
  "status": "success",
  "extraction_quality": {
    "total_records": 47,
    "passed": 46,
    "dlq": 1,
    "schema_compliance": 0.979
  },
  "source_health": {
    "total_products": 8,
    "success": 8,
    "warning": 0,
    "failed": 0,
    "rewrites_detected": 2
  },
  "pipeline_stages": {
    "collect": {"status": "ok", "duration_sec": 12},
    "extract": {"status": "ok", "tokens_in": 9500, "tokens_out": 4200},
    "analyze_a": {"status": "ok", "duration_sec": 45},
    "analyze_b": {"status": "ok", "duration_sec": 30},
    "synthesize": {"status": "ok", "duration_sec": 25},
    "writer": {"status": "ok", "files_rendered": 52}
  },
  "coverage": {
    "active_themes": 6,
    "total_themes": 12,
    "product_coverage_rate": 1.0,
    "avg_tags_per_product": 3.4
  },
  "alerts": {
    "silence": 1,
    "rewrite": 2
  }
}
```

**metrics.py 与 PR 的集成方式**：

1. `metrics.py` 将运行报告写入 `_pipeline/{date}/07-metrics/report.json`（临时）
2. 同时写入 `_metrics/{date}-report.json`（入 Git，长期存档，可审计回溯）
3. `metrics.py` 生成一份 Markdown 摘要表（`_pipeline/{date}/07-metrics/summary.md`）
4. `create-pull-request` action 通过模板将摘要表内嵌到 PR description body 中
   （使用 `peter-evans/create-pull-request` 的 `body-path` 参数指定 summary.md）

这样审核者打开 PR 即可直接看到本次运行的质量指标，无需手动查找文件。

**9.5.3 质量门禁进化**

指标的价值在于驱动决策。随着产品成熟，质量门禁的门槛逐步收紧：

- **Phase 1（人工主导）**：不设自动门禁，指标仅供观察。审核者手动判断 PR 质量
- **Phase 2（半自动）**：Schema 合规率 < 95% 时自动在 PR 中标记「⚠️ 需重点审」；
  采集成功率 < 90% 时自动跳过该产品（不阻挡管线）
- **Phase 3（面向用户）**：卡片拒绝率 > 10%（连续 3 次运行）时自动触发上一版发布回滚；
  审核周期中位数 > 48h 时向维护者发通知

### 9.6 卡片身份与重处理协议（Card Identity & Reprocessing）

必须回答的问题：**改进了 Prompt 之后，对历史 release 重新提取会发生什么？** 若无
协议，重提取会产生新文件名 → 重复卡片 → `evolves_from` / `related_changes` /
Signal 引用全面断链。协议如下：

**1. 确定性卡片身份（`card_id`）**

- 格式：`{product-slug}-{release-date}-{hash6}`，`hash6` 为该卡片**首要 evidence
  quote 归一化文本**的 SHA-256 前 6 位
- 由 `extract.py` 的**确定性代码**（非 LLM）生成：LLM 只产出卡片内容，身份由代码
  绑定到「(release, 证据片段)」这一客观锚点；重跑同一 release 时，指向相同证据的
  卡片得到相同 `card_id`

**2. 文件路径与 slug 稳定性**

- 路径**不含可变维度**：`Changes/{product}/{date}-{slug}.md`。v1.7 的
  `Changes/{theme}/...` 设计已废弃——候选主题晋升或主题修正会导致文件跨目录移动、
  全部反向链接失效
- `theme` 仅存于 frontmatter；主题维度的浏览/聚合由派生索引与 Theme MOC 承担
- `slug` 在卡片**首次创建时**由 LLM 建议、之后**永久冻结**：`writer.py` 渲染前先按
  `card_id` 在现有 Vault 中查找（经派生索引加速），命中则**原路径就地更新**——标题
  变化只改 H1 与 frontmatter，不改文件名
- 候选主题晋升时**只回填 frontmatter 的 `theme` 字段**：零文件移动、零链接重写

**3. 重处理（Reprocess）流程**

- 每张卡片 frontmatter 记录 `extractor_version`（Prompt 版本号，随 Git 管理）
- `extract.py --reprocess <product>[@<date-range>]` 对指定范围重新提取，结果与旧卡片
  按 `card_id` 对账：
  - **命中** → 就地更新机器区块与机器字段（人类区与 `human_overrides` 照常保留，见 6.5）
  - **旧卡片无对应**（证据片段在新提取中消失/被合并）→ 标记 `superseded: true`，
    **不物理删除**（保护入链），在 PR 中列出待人工确认归档
  - **新增卡片** → 正常创建
- 重处理走与日常运行相同的 PR 审核 gate，PR body 单列「重处理对账报告」
  （命中 / 新增 / superseded 数量与清单）

**4. 链接完整性（持续防腐）**

`validate.py` 第二轮对渲染产物做全 Vault 链接检查（见 9.2.1）：任何不可解析的双链、
Signal 引用的已拒卡片、指向 `superseded` 卡片的 `evolves_from`，都会在 PR 中标红。

### 9.7 Prompt 评估与回归（Evals）

9.5 的「卡片拒绝率」是滞后指标——审核者发现问题时，坏输出已经生成。Prompt / 模型 /
词表的任何改动都需要**前置回归验证**，否则改 Prompt 全凭感觉：

**1. 黄金样本集（Golden Set）**

- `_evals/extractor/` 维护「输入 release 原文 → 期望 Change Cards JSON」样本对（初期
  10-20 个，覆盖典型形态：多主题混合 release、候选主题、纯 bugfix 无卡片、营销话术
  干扰）
- `run_evals.py` 对黄金集运行当前 Prompt，按字段比对评分：theme 命中率、卡片拆分数
  偏差、impact 一致性、evidence quote 重合度
- **触发时机**：Prompt 文件、`themes.yaml`、模型版本发生 Git 变更时在 CI 强制运行；
  总分低于上一版本则阻止合并

**2. 审核修正回流（最便宜的训练信号）**

- 审核者在 PR 中对卡片的每次修改（改主题、改 impact、改描述）就是最高质量的标注
  数据。PR 合并后 `metrics.py` 归集这些 diff 到 `_evals/review-edits/`
- 每月从修正集中：① 挑典型错误补入黄金集；② 更新 Extractor few-shot 示例；③ 复盘
  高频错误主题，修订词表 aliases

**3. 主题误分类的主动监控**

全部价值链（聚合、扩散、Signal、趋势）压在 Extractor 的主题分类上，等聚合出错再
发现就晚了：

- **抽样核对**：每周随机抽 20 张卡片人工核对主题归类（9.5.1「主题精度抽样」指标）
- **离群检测**：复用既有 embedding（见 4.4），卡片向量距其主题质心过远时标注
  `theme_outlier: true` 进入审核注意清单（见 9.2.1）——零额外模型成本

---

## 10. 发布层设计（Quartz 定制）

### 10.1 为什么选择 Quartz

Quartz 是专门为将 Obsidian 知识库发布为网站而设计的工具（v4 基于 Node.js + React），天然支持：
- **双链解析**：`[[笔记名]]` 自动转为站内链接
- **关系图谱**：Fuse.js 搜索 + D3.js 图谱可视化
- **标签系统**：与 Obsidian 标签完全兼容
- **自定义主题**：可以完全定制 CSS 以匹配品牌

### 10.2 定制页面

#### 首页：`index.md`

```markdown
---
title: ChronoLog — 产品演化档案馆
---

欢迎来到 ChronoLog。

这里追踪了 **N 个产品** 的 **M 次关键变化**，覆盖 **X 个演化主题**。

## 本周信号（L1）
> 以下 Signal 由 Signal Generator 从当日新增 Change Cards + Alerts 自动生成，
> 经审核后发布。点击条目查看完整叙事与引用的证据卡片。

<!-- chronolog:begin region="weekly-signals" -->
- [[2026-04-23 Signal: 三家产品同日发布 Agent 功能]]
- [[2026-04-22 Signal: 知名工具宣布转向免费增值]]
<!-- chronolog:end -->

## 弱信号观察站
- [谁沉默了 / 谁悄悄改口](/weak-signals)（见 7.2）

## 热门演化主题（L2）
- [[Theme: Agent Mode 竞赛]]
- [[Theme: 从订阅到按量计费的定价转型]]

## 深度洞察（L3）
- [[2026 Q1 报告：AI 编程助手的商业模式博弈]]
```

#### 产品页模板

每个产品页包含：
1. 产品元信息卡片（YAML Frontmatter 渲染）
2. 演化时间线（自动生成的 Change Cards 列表）
3. 主题分布图（该产品涉及的主题标签云）
4. 相关竞品（双链连接）

#### 主题页模板

每个主题页包含：
1. 主题定义与背景
2. **多产品对比时间线**（Phase 1 起为构建时生成的 Mermaid 图，Phase 4 升级为可交互组件，见 8.2）
3. 涉及的所有 Change Cards（按时间排序）
4. 涉及的所有产品（双链）
5. L3 洞察报告链接

#### 推测层展示规范

所有 `ai_generated` 内容（战略意图推测、下一步预测）在站点上以**默认折叠的 callout**
渲染（Quartz 支持 Obsidian 可折叠 callout 语法，如 `> [!ai]- 🤖 AI 推测（点击展开）`），
读者主动展开才可见；事实层与 evidence 永远是页面的视觉主体。这是「可审计的事实档案
必须是第一印象」的落地手段（见 5.1 推测层按需生成）。

### 10.3 搜索与导航增强

按实现成本分两档，与「交互式可视化后置」原则（第 13 节）保持一致：

**Phase 3（Quartz 原生能力即可承载）**：
- **按主题浏览**：首页主题标签云 → Theme MOC 页（原生标签页 + 双链）
- **高影响精选页**：`writer.py` 构建时生成「仅 paradigm-shift」静态精选列表
- **全文搜索**：Quartz 原生 Fuse.js 搜索
- **弱信号观察站**：沉默 + 改写专题页（见 7.2，构建时生成）

**Phase 4（需自定义组件，验证后实施）**：
- **多维组合筛选**：影响等级 × 时间范围 × 产品（faceted search）
- **Canvas 图谱入口**：从标签云进入主题演化图谱

---

## 11. 自动化工作流

### 11.1 两段式工作流：生成 + 审核 gate + 发布

「自动生成」与「自动发布」是两件事。LLM 输出存在幻觉与误分类风险，直接 push 到
线上会损害对研究者/分析师的可信度。因此**内容生成**与**站点发布**拆为两个独立
workflow，中间隔一道**人工审核 gate（Pull Request）**：

```
[Workflow A: 内容生成] 定时触发
  collect → extract → validate(第一轮,隔离坏数据至DLQ) → analyze_a → silence_monitor
    → analyze_b → synthesize → writer(所有权分区渲染) → signal_generator
    → validate(第二轮:关联层+链接完整性) → metrics(汇总指标)
    ↓ 写入 staging（_pipeline/ 或 staging 分支）
  自动校验（schema / 主题词表 / 双链 / 推测标注，见 9.2.1）
    ↓ DLQ 隔离与正常数据通过
  自动开 Pull Request（包含成功数据、DLQ 告警、质量报告）
        │
        ▼
[人工审核 gate]  审核者在 PR 中检查 → 合并到 main
        │
        ▼
[Workflow B: 发布]  push 到 main 触发
  Quartz build → 部署到 Cloudflare Pages
```

#### 审核分级（Review Tiers）：把人工审核花在刀刃上

逐卡全量审核在规模化后必然失败：按 9.5.2 的量级（日均约 47 张卡片），审核疲劳 →
橡皮图章 → 质量门禁名存实亡。因此审核按风险分级，**「按例外审核」是目标状态，全量
审核只是校准期的临时形态**：

| Tier | 内容 | 处理方式 |
|------|------|---------|
| **Tier A（低风险 · 自动通道）** | 事实层 Change Cards（schema 通过、evidence 完整、主题命中词表）、Release 记录 | Phase 1-2 全量人审（校准期）；Phase 3 起满足切换门禁后**自动合并 + 每日随机抽查 10%** |
| **Tier B（高风险 · 必经人审）** | 推测层内容、候选主题晋升、Eras / 扩散修正补丁、Alerts（沉默/改写）、`merge_conflict` 文件、Signal、重处理对账报告 | 始终走 PR 人工审核 |

**切换门禁**（与 9.5.3 质量门禁联动）：卡片拒绝率连续 10 次运行 < 5% 且 Schema
合规率 > 98% 时，Tier A 开启自动通道；任一指标回落（含 Tier A 抽查不合格率 > 5%，
见 9.5.1）即自动降回全量人审。Tier A 自动合并使用独立分支 `auto/facts-{date}`，
校验全绿后由 CI 自动合并（保留 PR 痕迹供审计与抽查），与 Tier B 的人审 PR 互不阻塞。

#### Rolling PR 语义（避免审核单元不可控膨胀）

每日 PR 若未及时合并，必须定义后续运行的行为：

- 固定分支 `auto/daily-update` 采用 **Rolling PR**：每次运行从最新 `main` 重建分支、
  重新生成全部 staging 内容（管线幂等，重建无副作用），更新同一个 PR
- PR body 按日期累积各次运行的摘要（来自 `metrics.py`），审核者可见「该 PR 累积了
  哪几天的内容」
- 积压超过 3 天（9.5.1 积压指标）自动提醒维护者；Tier A 自动通道开启后，积压内容
  只剩 Tier B，体量可控

#### Workflow A：内容生成（产出 PR，不发布）

```yaml
# .github/workflows/generate.yml
name: ChronoLog Content Generation

on:
  schedule:
    - cron: '0 6 * * *'      # 每天早 6 点（UTC）
  workflow_dispatch:

jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: pip install -r _scripts/requirements.txt

      - name: Collect & Snapshot
        run: python _scripts/collect.py

      - name: Extract (LLM → JSON)
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        run: python _scripts/extract.py

      - name: Validate extracted JSON (DLQ separation)
        run: python _scripts/validate.py   # 校验失败项进入 DLQ，成功项继续后续阶段

      - name: Analyzer-A (per-product, LLM → JSON, multiprocess)
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        # 内部使用 Python multiprocessing，每个产品独立进程并行处理
        # 并发数由 ANALYZER_A_WORKERS 环境变量控制（默认 4）
        run: python _scripts/analyze_a.py

      - name: Silence Monitor (Python, no LLM, runs in parallel with Analyzer-A)
        # 不依赖 LLM 阶段，在 Collector 完成后即可运行；此处顺序执行仅为简化 CI 配置
        # 如需并行可将 Silence Monitor 拆为单独 job 并设 needs: [collect]
        run: python _scripts/silence_monitor.py

      - name: Analyzer-B (cross-product, LLM → JSON)
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        run: python _scripts/analyze_b.py  # 跨产品聚类/diffusion/关联回填

      - name: Synthesize (LLM → JSON)
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        run: python _scripts/synthesize.py

      - name: Render Markdown (Writer, no LLM)
        run: python _scripts/writer.py     # JSON → Obsidian Markdown，确定性渲染

      - name: Generate Signals (LLM → JSON)
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        run: python _scripts/signal_generator.py  # 消费已渲染的摘要，生成首页 Signal

      - name: Validate round 2 (rendered output)
        # 关联层字段 + 全 Vault 链接完整性 + Signal 引用检查（见 9.2.1）
        run: python _scripts/validate.py --round 2

      - name: Generate metrics report
        # 将质量报告写入 _metrics/{date}-report.json（入 Git）
        # 同时生成 _pipeline/{date}/07-metrics/summary.md 供 PR body 使用
        run: python _scripts/metrics.py

      - name: Open Pull Request
        uses: peter-evans/create-pull-request@v6
        with:
          branch: auto/daily-update
          title: "daily: ${{ github.run_id }} 内容更新（待审核）"
          body-path: _pipeline/summary.md   # 包含质量报告摘要 + DLQ 告警 + Signal 列表
          labels: auto-generated, needs-review
```

#### Workflow B：发布（合并到 main 后触发）

```yaml
# .github/workflows/deploy.yml
name: ChronoLog Deploy

on:
  push:
    branches: [main]          # 只有审核合并后才发布
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install Quartz
        run: npm install

      - name: Build site
        run: npx quartz build

      - name: Deploy to Cloudflare Pages
        uses: cloudflare/pages-action@v1
        with:
          apiToken: ${{ secrets.CLOUDFLARE_API_TOKEN }}
          accountId: ${{ secrets.CLOUDFLARE_ACCOUNT_ID }}
          projectName: chronolog
          directory: public
```

> 审核分级（见上文 Review Tiers）取代了早期版本「可选轻量模式」的表述：自动通道
> 不再是可选优化，而是 Phase 3 的明确目标状态（对应 OQ-4 的决策，见第 18 节）。

### 11.2 本地开发工作流

```bash
# 1. 克隆仓库
git clone https://github.com/yourname/chronolog.git
cd chronolog

# 2. 安装 Python 依赖
pip install -r _scripts/requirements.txt

# 3. 安装 Quartz
npm install

# 4. 运行 pipeline（单步或全量）
python _scripts/collect.py
python _scripts/collect.py --backfill Cursor   # 新产品接入时执行一次历史回填（见 6.2.2）
python _scripts/extract.py
python _scripts/extract.py --reprocess Cursor  # Prompt 升级后按 card_id 对账重提取（见 9.6）

# 5. 本地预览 Quartz
npx quartz build --serve

# 6. 在 Obsidian 中打开 Vault 进行编辑
# （假设本地已安装 Obsidian）
```

---

## 12. 品牌与命名

### 12.1 候选命名方向

| 命名 | 含义 | 适配度 |
|------|------|--------|
| **ChronoLog** | 编年志（Chrono + Log） | ★★★★★ 直接、易记、有档案感 |
| **EvoLog** | 演化志（Evolution + Log） | ★★★★★ 更强调动态演化 |
| **Strata** | 地层（地质沉积层） | ★★★★☆ 寓意历史沉积，但不够直观 |
| **Annals** | 编年史 | ★★★★☆ 古典感，但技术圈可能觉得太文 |
| **Chronicle** | 纪事/编年史 | ★★★★☆ 与 ChronoLog 接近，稍长 |

**推荐**：**ChronoLog** 作为产品名，**EvoLog** 作为副品牌/ newsletter 名。

### 12.2 Slogan 选项

- 「产品的演化不是随机的，它遵循某种逻辑。」
- 「读懂过去，看见拐点。」
- 「追踪每一次变化，发现下一个趋势。」

### 12.3 视觉调性建议

- **色彩**：深灰 + 琥珀/金色点缀（档案馆的庄重感 + 洞察的「发现感」）
- **字体**：正文使用 Inter / Source Sans，等宽代码使用 JetBrains Mono
- **图谱配色**：按主题标签分配颜色，产品节点为实心圆，Change 节点为菱形

---

## 13. MVP 路线图

### Phase 1：内核验证（Week 1-3）

**目标**：同时验证两个核心价值——单产品演化叙事可读、跨产品主题聚合正确；并通过
历史回填让验证基于真实的时间纵深

- [ ] 搭建 Obsidian Vault 标准目录结构
- [ ] 编写 `sources.yaml`，选取 5-8 个**tier-1（GitHub Releases / RSS）**的同领域产品（建议：AI 编程助手方向，产品少且变化密集）
- [ ] 实现 `collect.py`（含 `--backfill`），对全部入选产品执行**历史回填**（目标：上线即有 ≥2 年纵深，见 6.2.2）
- [ ] 通过 Bootstrap 流程产出初版 `themes.yaml`（对回填数据自由打标 → 聚类 → 人工筛选，见 5.3）
- [ ] 实现 `extract.py`（仅事实层 + `card_id` 确定性生成，见 9.6），运行生成第一批 Change Cards
- [ ] 实现 `validate.py` 第一轮校验（Extractor 输出 schema 合规）
- [ ] 实现 `analyze_a.py`（单产品：Eras / evolves_from / verbosity_baseline）
- [ ] 实现 `analyze_b.py` 最小版本（跨产品主题聚类 + diffusion + 关联回填）
- [ ] 实现 `silence_monitor.py`（纯 Python，不调用 LLM）
- [ ] 实现 `writer.py`（JSON → Markdown：标记区块所有权 + machine_hash 改动检测 + card_id 对账，见 6.5、9.6）
- [ ] `writer.py` 在 Theme MOC 构建时生成 **Mermaid 跨产品对比时间线**（见 8.2）
- [ ] 人工审核 LLM 输出，调整 Prompt 与词表
- [ ] 配置 Quartz 基础站点，本地可访问（暂用原生功能 + Mermaid，不做定制组件）

**成功标准（三重验证）**：
1. **单产品演化**：进入任一产品页，能看到其 Change Cards 被折叠为有叙事的演化阶段（Eras），而非流水账
2. **多产品趋势**：进入一个主题页（如 `#agent-mode`），多个产品的 Change Cards 被正确聚合，Mermaid 对比时间线可直观看出谁先谁后
3. **时间纵深**：回填完成后，任选一个产品可看到 ≥2 年历史卡片与至少 2 个 Era

### Phase 2：自动化管线 + 审核 gate（Week 4）

**目标**：实现自动生成 + 人工审核 gate 的可持续运转

- [ ] 完成 `synthesize.py`（自动生成 Theme MOC + 标注推测层）
- [ ] 完成 `signal_generator.py`（首页 L1 Signal）
- [ ] 完成 `metrics.py`（运行质量报告，见 9.5；含审核修正 diff 归集到 `_evals/review-edits/`）
- [ ] 完善 `validate.py` 第二轮校验（关联层字段 + 全 Vault 链接完整性 + Signal 引用检查）
- [ ] 建立 `_evals/` 黄金样本集初版 + `run_evals.py`（Prompt 回归在 CI 强制运行，见 9.7）
- [ ] 配置两段式 GitHub Actions：生成→Rolling PR（Workflow A）、合并→发布（Workflow B）
- [ ] 配置 PR body 使用 `_pipeline/summary.md`（含质量报告 + DLQ 告警）
- [ ] 开启 RSS 输出（Quartz 原生能力——面向分析师受众的最低成本分发渠道）
- [ ] 部署到 Cloudflare Pages，拥有公开 URL

**成功标准**：每日定时自动生成 PR（含质量摘要），审核合并后网站同步；DLQ 机制能隔离错误记录不阻断管线；改 Prompt 时 evals 回归在 CI 强制运行。

### Phase 3：面向用户（Week 5-7）

**目标**：从「个人工具」进化为「面向用户的产品」

- [ ] 定制 Quartz 主题（色彩、字体、首页布局）
- [ ] 实现 L1 信号层首页（编辑精选视图）
- [ ] 实现「弱信号观察站」页面（沉默 + 改写，见 7.2、10.3）
- [ ] 实现 Phase 3 档导航（主题标签云、高影响精选页，见 10.3；多维筛选组件留待 Phase 4）
- [ ] 推测层默认折叠展示（见 10.2）
- [ ] 满足切换门禁后开启 Tier A 自动合并通道（见 11.1 审核分级）
- [ ] 上线 Newsletter（以 Signal 为素材底座；工具选型见 OQ-6）
- [ ] 配置自定义域名
- [ ] 小规模种子用户测试，收集反馈

> **交互式可视化后置**：可交互的对比时间线 React 组件、Canvas 演化图谱等高成本
> 可视化项，**在核心数据价值被种子用户验证之后**再实施（见 Phase 4）。此前用 Quartz
> 原生能力（双链、原生 Graph View、标签）+ 构建时生成的 Mermaid 时间线（见 8.2）
> 承载——核心 aha 视图不等待 Phase 4。

**成功标准**：非技术用户可以在 30 秒内理解网站价值，并在 3 分钟内找到感兴趣的趋势。

### Phase 4：可视化与规模化（Week 8-12）

- [ ] 将 Mermaid 对比时间线升级为可交互 React 组件（见 8.2，验证通过后启动）
- [ ] 实现多维组合筛选（影响等级 × 时间 × 产品，见 10.3）
- [ ] 尝试 Canvas 可视化渲染（选 1-2 个主题做演示）
- [ ] 扩展到更多行业领域（从 AI 编程助手扩展到 SaaS 生产力工具、云服务等）
- [ ] 引入 tier-2（HTML 爬取）数据源，扩大覆盖
- [ ] 引入 L3 洞察层，定期发布人工精修的行业报告
- [ ] 优化 LLM 成本（对高流量产品使用缓存，对低频产品降低更新频率）
- [ ] Newsletter 增长运营（专题策划、转载合作；基础设施已在 Phase 3 上线）
- [ ] 建立内容质量评估机制（基于用户停留时长、点击热图）

---

## 14. 风险与对策

| 风险 | 可能性 | 影响 | 对策 |
|------|--------|------|------|
| 数据源失效/被封/限流 | **高** | **高** | 这是此类产品最常见死因。MVP 只用 tier-1（GitHub Releases/RSS）；tier-2 HTML 采集失败仅告警不阻断；明示数据覆盖盲区 |
| 主题标签碎片化（趋势无法聚合） | 中 | 高 | 受控主题词表（5.3）+ 别名归一化 + 候选主题人工审核晋升 |
| AI 推测内容可信度受质疑 | 中 | 高 | 事实/关联/推测三层分离；**每个事实层判断附 `evidence` 原文溯源**；推测层强制 `ai_generated` + `confidence` 标注；UI 显式标识「🤖 AI 推测」 |
| 快照存储体积膨胀 | 中 | 低 | 快照不入 Git，仅留 `latest.hash` 与 Alert；旧快照定期归档/清理（保留 diff 记录即可） |
| LLM 提取质量不稳定 | 中 | 高 | 验收 checklist 自动校验（9.2.1）+ 人工审核 gate（第 11 节）+ 输出可回滚 |
| 沉默检测误报 | 中 | 中 | 阈值按产品可配置；定位为「信号」非「结论」；只提示不断言 |
| Vault 规模过大导致构建慢 | 中 | 中 | 主站近 2 年 + 历史归档子站 + 提供 Vault 下载 |
| 内容噪音过多 | 高 | 中 | L1 信号层人工/LLM 精选过滤；影响等级机制 |
| 竞品直接复制 | 低 | 中 | 壁垒不在数据而在「主题折叠」方法论 + 演化阶段叙事 + 洞察 |
| LLM API 成本过高 | 中 | 低 | 原始文本预过滤（小更新不送 LLM）；分层模型（轻量做提取，强模型做综合）；低频产品降频 |
| 人工编辑与机器输出冲突 | 低 | 中 | v1.8 起采用标记区块所有权（6.5）：人类区修改结构上不可能被覆盖；仅人工误改机器区时标记 `merge_conflict: true` 入 DLQ 并在 PR 列出 diff，不静默覆盖 |
| 重处理/Prompt 升级导致卡片重复与链接断裂 | 中 | 高 | 卡片身份与重处理协议（9.6）：card_id 确定性对账、slug 冻结、superseded 标记不物理删除、第二轮链接完整性校验 |
| 审核疲劳导致橡皮图章 | 高 | 高 | 审核分级（11.1）：Phase 3 起事实层走自动通道 + 10% 抽查，人审只覆盖高风险内容；Rolling PR 控制积压；Tier A 抽查不合格率回升自动降级 |
| 改写检测误报（页面噪音触发假告警） | 高 | 中 | diff 基于正文抽取 + 归一化文本（6.2.1）；改写 Alert 定位为「信号非结论」 |
| 转载版权风险 | 低 | 中 | Release 页只存中性转述摘要 + 原文链接（5.1 实体四）；原始快照仅内部留存不发布；evidence 限于合理引用的短引文 |
| metrics.py 崩溃导致 PR 无质量报告 | 低 | 中 | metrics.py 失败不阻断 PR 创建，PR body 降级为静态模板并标注「⚠️ 质量报告生成失败」；metrics 失败独立告警 |
| embedding 索引陈旧或损坏 | 中 | 中 | 每次 pipeline 运行时对比 `index.sqlite` schema version 与代码版本，不匹配则全量重建；embedding 模型版本变更时强制重建（通过 `EMBEDDING_MODEL_VERSION` 环境变量跟踪） |

---

## 15. 范围边界（Out of Scope）

以下内容**明确不在** ChronoLog 当前版本的设计范围内，避免范围蔓延：

| 类别 | 不做的内容 | 原因 |
|------|-----------|------|
| **数据源** | tier-3（社交媒体、Discord、Twitter） | 结构混乱，数据质量无法保证 |
| **数据源** | 实时 API / Webhook 推送 | 与「无后端服务」架构原则冲突 |
| **用户功能** | 用户账号、个性化收藏、评论 | 超出静态站点能力边界 |
| **用户功能** | 付费订阅、内容墙 | 商业模式尚未确定，不在 MVP 范围 |
| **内容** | 行业新闻、融资动态（非 changelog 来源）| 超出「changelog 为基础」的核心命题 |
| **多语言** | 非英文 changelog 的提取与分析 | 主题词表、Prompt 均以英文设计；多语言为 Phase 4+ |
| **可视化** | Canvas 演化图谱、可交互对比时间线 React 组件 | 高开发成本，Phase 4 验证后实施；构建时生成的 Mermaid 时间线**不在此列**（Phase 1 即交付，见 8.2） |
| **AI 功能** | 多模态（图像/视频分析）| Phase 4+ 能力，当前 Extractor 仅处理文本 |

---

## 16. 产品成功指标（KPI）

与第 9.5 节的运营指标（衡量系统健康度）不同，以下 KPI 衡量**产品对用户的价值**：

| 指标 | 定义 | 目标（Phase 3 结束） | 数据采集方式 |
|------|------|---------------------|------------|
| **月活用户（MAU）** | 每月访问网站的唯一用户数 | > 200 | Plausible / Umami |
| **回访率** | 30 天内再次访问的用户比例 | > 30% | Plausible |
| **核心页面停留时长** | 主题页 / 产品页平均停留时间 | > 90 秒 | Plausible |
| **Newsletter 订阅数** | 邮件订阅列表规模 | > 100 | Mailchimp / Buttondown |
| **Newsletter 打开率** | 发送后 48h 内打开的比例 | > 35% | 邮件服务商统计 |
| **种子用户满意度** | 用户访谈 NPS 或 1-5 评分 | > 4.0 | 手动问卷（n≥10） |
| **内容引用数** | Signal / L3 报告被外部文章引用次数 | > 5 次/月 | 手动监控 |

**北极星指标**：**每月主动返回研究某一主题的研究者数**——反映内容是否真正有价值，
而非偶然流量。

---

## 17. 外部依赖清单

| 依赖项 | 用途 | 版本约束 | 失效 fallback |
|-------|------|---------|--------------|
| **LLM API（OpenAI / Anthropic）** | Extractor / Analyzer-A/B / Synthesizer / Signal Generator | 经 `litellm` 统一抽象，`LLM_PROVIDER` 环境变量切换；密钥 `OPENAI_API_KEY` / `ANTHROPIC_API_KEY` | 任一提供商故障时改环境变量即切换，无需改代码 |
| **GitHub Actions** | 定时 pipeline 触发、PR 创建、部署 | 免费计划每月 2000 分钟 | 本地手动运行（`python _scripts/collect.py` 等） |
| **Cloudflare Pages** | 静态站点托管 | 免费计划 | GitHub Pages（备选，性能略低） |
| **Quartz v4** | Obsidian Vault → 网站 | v4.x，Node.js 20 LTS | 无直接替代，需评估 Hugo/Astro |
| **`peter-evans/create-pull-request`** | Workflow A 创建 PR | v6 | 手动 `gh pr create` 命令 |
| **`fastembed`（ONNX）+ `all-MiniLM-L6-v2`** | Change Card embedding，供 Analyzer-B 语义检索与主题离群检测 | 模型版本经 `EMBEDDING_MODEL_VERSION` 锁定；CI 缓存模型文件（约 30 MB，无 PyTorch 依赖） | 降级为 TF-IDF 关键词检索（准确率下降） |
| **Obsidian** | 人工编辑后台 | 任意版本 | 直接编辑 Markdown 文件（VSCode 等） |

**API 密钥管理**：`OPENAI_API_KEY`、`ANTHROPIC_API_KEY`、`CLOUDFLARE_API_TOKEN`、
`CLOUDFLARE_ACCOUNT_ID` 均存储为 GitHub Actions Secrets，不得硬编码在任何文件中。
定期轮换周期建议 90 天。

---

## 18. 待决问题（Open Questions）

以下设计决策尚未最终确认，需在对应 Phase 启动前完成：

| # | 问题 | 影响范围 | 需要决定的时间 | 当前默认假设 |
|---|------|---------|--------------|------------|
| OQ-1 | `analyze_a.py` 历史窗口：处理「单产品全量历史」还是「滚动 N 个月」？ | Eras 识别质量 / token 成本 | **已决（v1.8）** | 仅对**有新增卡片的产品**触发；Eras 持久化，新证据仅触发受影响阶段边界的重评估（见 6.2 表） |
| OQ-2 | embedding 索引是全量重建还是增量更新？增量时如何处理 Change Card 内容变更？ | Analyzer-B 语义检索质量 / CI 时长 | **已决（v1.8）** | 按卡片内容 hash 缓存（内容不变不重算）；`EMBEDDING_MODEL_VERSION` 变更时全量重建（见 4.4） |
| OQ-3 | writer.py 机器字段清单（6.5 所有权分区）是否需要按实体类型/产品差异化配置？ | 灵活性 vs 实现复杂度 | Phase 2 启动前 | 全局统一清单（不按产品区分） |
| OQ-4 | L1 Signal 是否需要人工每日审核，还是可自动通过？ | 运营负担 / 内容可信度 | **已决（v1.8）** | 并入审核分级（11.1）：Signal 属 Tier B 必经人审；事实层卡片 Phase 3 起走自动通道 + 抽查 |
| OQ-5 | 多语言支持：何时引入非英文 changelog 的处理？需要独立的主题词表吗？ | 产品扩展方向 | Phase 4 启动前 | 暂不支持，明确标注数据覆盖范围 |
| OQ-6 | Newsletter 发送频率与工具选型（Mailchimp / Buttondown / 自建）？ | Phase 3 运营成本（Newsletter 已前置至 Phase 3，见 13） | Phase 3 启动前 | 待定 |

---

## 19. 附录

### 附录 A：Extractor Prompt 模板（示例）

```
你是一个专业的技术产品分析师。你的任务是将以下产品发布说明（Release Notes）
拆解为若干张「差异卡片」（Change Cards）。你只负责提取【事实层】，不要做任何
跨产品关联或趋势判断（那是后续 Analyzer 阶段的工作）。

输入：
产品名：{product}
版本：{version}
日期：{date}
受控主题词表（必须从中选择 theme）：
{themes_yaml}        # slug 列表 + 别名，见 themes.yaml
发布说明原文：
{raw_text}

要求：
1. 将发布说明拆分为 1-5 张 Change Cards，每张围绕一个独立的主题
2. **输出 JSON**（非 Markdown）。每张卡片为 JSON 对象，字段对应 Change Card Schema：
   - `theme`: **必须**从受控词表的 slug 中选择；命中别名时归一化到对应 slug；
     若没有任何主题匹配，填 `"__candidate__"` 并在 `theme_suggestion` 给出建议名
   - `impact`: 影响等级（"incremental" / "significant" / "paradigm-shift"）
   - `date`: 发布日期（ISO 格式）
   - `evidence`: 数组，每项含 `source_release`（笔记 ID）与 `quote`（**必填**，原文
     短引用，为主定位手段）；`anchor` 可选（多数 changelog 无稳定锚点）
3. 卡片内容字段：
   - `description`: 差异描述（2-3 句话，**只陈述客观事实**）
   - `comparison`: 与之前版本的对比（如有，且为已知事实）
4. **不要**输出 `related_changes` / `evolves_from` / `diffusion`（留空，由 Analyzer 回填）
5. **不要**在 Extractor 阶段编写「行业坐标」或跨产品叙事
6. 仅对 impact 为 "significant" 或 "paradigm-shift" 的卡片生成战略意图等主观推断，
   incremental 卡片一律不生成（见 6.4）；推断必须在 JSON 中用独立对象承载，并标注
   `"ai_generated": true` 与 `"confidence": "low|medium|high"`
7. 用笔记 ID（如 `"product_ref": "cursor"`）引用关联实体，**不要**在 JSON 中
   拼接 `[[双链]]` 语法，双链由 Writer 渲染时统一注入

输出格式：JSON 数组，每个元素为一张 Change Card 的结构化数据。
```

### 附录 B：Analyzer Prompt 模板（示例）

Analyzer 已拆分为 A（单产品）和 B（跨产品），分别对应不同输入范围和职责。

**附录 B-1：Analyzer-A Prompt（单产品，可并行）**
```
你是一个产品分析师。基于以下单个产品的全量 Change Cards 时间线，分析其内部演化结构。

输入：
产品名：{product}
该产品全量 Change Cards（JSON）：{change_cards}

要求：
1. 【演化阶段（Eras）识别】识别产品的战略转折点，将 Change Cards 折叠为若干有叙事
   的演化阶段，输出每个阶段的 name / from / to / summary / pivot_change（标志转折的
   关键卡片 ID）
2. 【产品内演化链（evolves_from）】为每张卡片标注它延续/迭代自哪张历史卡片（若存在）
3. 【词量基线（verbosity_baseline）】计算该产品历史上平均每次 release 产出的卡片数

注意：只分析该产品自身，不做跨产品比较（那是 Analyzer-B 的工作）。

输出格式：JSON，含 eras 数组、各卡片 evolves_from 补丁、verbosity_baseline 值。
对所有主观判断（如转折点动因）标注 ai_generated 与 confidence。
```

**附录 B-2：Analyzer-B Prompt（跨产品，增量视图）**
```
你是一个行业趋势分析师，负责分析 ChronoLog 当前追踪的产品集合中**近期有活动的主题**。

输入：
已追踪产品列表（含 verbosity_baseline）：{products}
**本次新增/更新的 Change Cards**（本次 pipeline 运行新产生）：{new_change_cards}
各活跃主题的**历史上下文卡片**（每个主题取最相关的 K≈20 张，按时间近邻 + embedding
相似度排序）：{theme_context_cards}
受控主题词表：{themes_yaml}

重要约束：
- 你**不**会收到全部历史卡片，只收到增量卡片 + 活跃主题的裁剪上下文。这是为了控制
  输入规模。如果某个主题需要更多历史上下文才能判断扩散顺序，请在输出中标注
  "needs_more_context": true 并说明所需主题
- 对未出现在活跃主题列表中的历史主题，本次不处理，保持之前的状态

要求：
1. 【活跃主题识别】从 new_change_cards 中识别哪些主题在过去 N 天内有新活动
2. 【关联回填】为本次新增的卡片填写 related_changes，并撰写「行业坐标」，说明该变化在
   主题演化中的位置（第几波、谁先谁后）
3. 【扩散分析（diffusion）】对每个活跃主题，判断在已追踪产品中的扩散顺序：
   - role：originator（已追踪产品中日期最早）/ follower / variant
   - first_in_tracked：已追踪产品中最早的卡片 ID
   - lag_days：相对 first_in_tracked 的天数差
   - tracked_products_count：当前已追踪产品总数
   - 重要：**不声称行业首创**，scope 固定为 tracked-products-only；
     originator 含义为「在 ChronoLog 已追踪的 {N} 个产品中最早记录到此变化的」
4. 【候选主题汇总】收集所有 theme=__candidate__ 的卡片及建议名，列为待审列表
5. 【扩散时间线修正】如果新增卡片改变了某个主题已知的扩散顺序（如发现更早的
   originator），输出修正补丁

注意：沉默检测由独立 Python 脚本处理，本 Prompt 不负责。

输出格式：JSON，含各卡片的 related_changes / diffusion 补丁、候选主题列表、
needs_more_context 标注。对所有主观判断标注 ai_generated 与 confidence。
```

### 附录 C：Synthesizer Prompt 模板（示例）

Synthesizer 有两种模式，分别服务于两个核心目标：

**模式一：单产品演化叙事**
```
你是一个产品史学家。基于以下某产品的全部 Change Cards 与已识别的演化阶段（Eras），
撰写该产品的「演化概览」叙事。

输入：
产品名：{product}
演化阶段：{eras}
Change Cards 时间线：{change_cards}

要求：
1. 为每个演化阶段写 2-3 句叙事，串联其关键 Change Cards
2. 标出阶段之间的「战略转折点」（哪张卡片标志了转折）
3. 转折点的动因解读须标注 ai_generated: true 与 confidence

输出：JSON，含 `product_id`、`eras` 数组（每个 era 含 narrative 文本与 pivot_change_id）、
`ai_generated` 与 `confidence` 标注。由 Writer 渲染为 Product 档案的「演化阶段」小节 Markdown。
```

**模式二：跨产品主题趋势报告**
```
你是一个行业趋势分析师。基于以下某主题下的跨产品聚类，撰写 Theme MOC。

输入：
主题：{theme}
涉及产品与卡片：{clustered_cards}

要求：
1. 演化时间线（事实层）：按时间列出各产品在该主题上的关键动作
2. 竞争格局分析（关联层）：谁引领、谁跟进、谁缺席
3. 下一步预测（推测层）：必须置于独立小节，标注 🤖 AI 推测 + confidence

输出：JSON，含 `theme_id`、`timeline` 数组、`competitive_landscape` 文本、
`prediction` 对象（ai_generated + confidence）。由 Writer 渲染为 Theme MOC Markdown。
```

### 附录 D：技术栈版本锁定

| 工具 | 建议版本 | 备注 |
|------|---------|------|
| Python | 3.11+ | 类型提示、multiprocessing 支持 |
| Quartz | v4.x | Obsidian 原生兼容 |
| Node.js | 20.x LTS | Quartz 构建需要 |
| `fastembed`（ONNX 运行时） | `all-MiniLM-L6-v2` | 本地 embedding，无 PyTorch 依赖（CI 安装快、缓存约 30 MB），模型版本经 `EMBEDDING_MODEL_VERSION` 锁定 |
| `litellm` | 最新稳定版 | LLM 提供商统一抽象，OpenAI / Anthropic 互为 fallback（见 17） |
| LLM API（提取层） | GPT-4o-mini / Claude Haiku | 轻量模型，成本优先 |
| LLM API（综合层） | GPT-4o / Claude Sonnet | 强模型，质量优先 |
| `peter-evans/create-pull-request` | v6 | Workflow A PR 创建，需 `body-path` 参数支持 |

### 附录 E：Signal Generator Prompt 模板（示例）

```
你是一个行业新闻编辑。基于以下当日新增的产品变化与异常信号，为 ChronoLog 首页
生成 3-5 条 Signal 卡片。

输入：
当日新增的 high-impact Change Cards（impact=significant 或 paradigm-shift）：
{new_high_impact_cards}
当日活跃的 Alerts（沉默、改写、主题升温）：{new_alerts}
当日更新的 Theme MOC 摘要：{theme_summaries}
已追踪产品列表：{products}

要求：
1. 从输入中筛选最值得首页展示的 3-5 个事件，优先选择：
   - 多产品在同一主题上的集中动作
   - 单个产品的 paradigm-shift 级别变化
   - 异常信号（沉默、改写）与行业动态的关联
2. 每条 Signal 输出 JSON 对象：
   - `title`: 信号标题（20 字以内）
   - `what_happened`: 发生了什么（2-3 句话）
   - `why_it_matters`: 为什么值得关注（2-3 句话）
   - `products_involved`: 涉及产品 ID 数组
   - `themes`: 涉及主题 slug 数组
   - `cited_change_cards`: 引用的 Change Card ID 数组
   - `cited_alerts`: 引用的 Alert ID 数组（如有）
   - `impact`: 最高影响等级
   - `ai_generated`: true
   - `confidence`: low|medium|high
3. 如果当日没有值得展示的高价值事件，输出空数组 `[]`，不强行凑数
4. 措辞保持中立、客观，不煽动情绪

输出格式：JSON 数组，每个元素为一条 Signal。由 Writer 渲染为 `Signals/{date}-{slug}.md`。
```

### 附录 F：修订记录

| 版本 | 日期 | 主要变更 |
|------|------|---------|
| v1.0 | 2026-04-23 | 初始 PRD 草稿 |
| v1.1 | 2026-04-23 | 数据模型三层化、主题词表、两段式审核 gate |
| v1.2 | 2026-04-23 | evidence 溯源、evolves_from/diffusion、派生查询索引、快照改写检测 |
| v1.3 | 2026-04-23 | 词量偏差、Analyzer-A/B 拆分、沉默检测移出 LLM、LLM→JSON→Markdown |
| v1.4 | 2026-04-23 | Signal 实体与生成器、Analyzer-B 增量 diff、附录矛盾修复 |
| v1.5 | 2026-04-23 | writer.py 双向合并机制、DLQ 局部容错管线 |
| v1.6 | 2026-04-23 | 质量控制指标（9.5）、metrics.py、三阶段质量门禁 |
| v1.7 | 2026-04-23 | 全文一致性修订：修复 47 个文档问题（内容矛盾、可执行性漏洞、格式导航、缺失章节）；新增 TOC、15-18 节（范围边界/KPI/外部依赖/待决问题）、附录 F/G |
| v1.8 | 2026-06-12 | 评审修订：① 新增 6.2.2 历史回填（冷启动策略 + `sources.yaml` backfill 配置）；② 新增 6.5 Writer 所有权模型，替代双向合并（修复 machine_hash 规格矛盾，引入标记区块 + `human_overrides`）；③ 新增 9.6 卡片身份与重处理协议（card_id、路径去 theme 化、slug 冻结、superseded）；④ 新增 9.7 Evals（黄金样本集 + 审核修正回流 + 主题离群检测）；⑤ 11.1 审核分级（Review Tiers）与 Rolling PR 语义；⑥ 跨产品对比时间线以 Mermaid 形式前置至 Phase 1（8.2）；⑦ 弱信号观察站产品化（7.2）+ 改写检测归一化降噪（6.2.1）；⑧ 词表 Bootstrap 流程（5.3）；⑨ Release 页版权调整（5.1）；⑩ 推测层按需生成 + 默认折叠（5.1、6.4、10.2）；⑪ 依赖更新：fastembed 替代 sentence-transformers、litellm 统一 LLM 抽象；⑫ OQ-1/2/4 决策落地；RSS 前置至 Phase 2、Newsletter 前置至 Phase 3 |

### 附录 G：术语表（Glossary）

**术语命名约定**：以下术语在文档中优先使用英文原词（组件名、脚本名、字段名始终使用
反引号格式化）。

| 术语 | 定义 |
|------|------|
| **Change Card（差异卡片）** | 数据最小单元。描述一个产品在单次发布中围绕**单一主题**的具体变化，包含事实层/关联层/推测层三类字段 |
| **Signal（信号卡片）** | L1 首页内容单元。从每日新增高 impact Change Cards + Alerts 中提炼的叙事摘要，含「发生了什么」「为什么值得关注」 |
| **Era（演化阶段）** | 由 `analyze_a.py` 识别的产品战略阶段，将零散 release 折叠为有叙事的时代划分 |
| **Theme MOC（主题演化）** | Map of Content，跨产品同一主题的聚合视图，包含演化时间线、竞争格局、扩散分析 |
| **Vault** | 基于 Obsidian 的 Markdown 文件库，是 ChronoLog 的唯一事实来源（SSOT） |
| **SSOT（Single Source of Truth）** | 唯一事实来源。Vault 中的 Markdown 是 SSOT；JSON 中间产物和派生索引均可从 SSOT 重建 |
| **DLQ（Dead Letter Queue，死信队列）** | 校验失败的 JSON 记录的隔离区。存储在 `_pipeline/dlq/`，不入 Git，最多自动重试 3 次 |
| **diffusion（扩散）** | 某一理念在已追踪产品集中的传播角色（originator/follower/variant）和时间差 |
| **verbosity_baseline（词量基线）** | 某产品历史上平均每次 release 产出的 Change Card 数，用于跨产品趋势对比时消除写作风格差异 |
| **tier-1/2/3** | 数据源可靠性分级。tier-1：GitHub Releases/RSS（高可靠）；tier-2：HTML 爬取（易失效）；tier-3：社交媒体（暂不纳入） |
| **machine_hash** | `writer.py` 写入 frontmatter 的**机器区块渲染内容**（归一化、不含该字段本身）SHA-256 摘要，用于检测机器区块内的人工改动；人类区修改不影响该值（见 6.5） |
| **Analyzer-A** | 单产品分析模块，识别 Eras、构建 evolves_from 链、计算 verbosity_baseline。可多进程并行；仅对本次有新增卡片的产品触发，Eras 持久化复用（OQ-1 决策） |
| **Analyzer-B** | 跨产品分析模块，执行主题聚类、diffusion 分析、related_changes 回填。需全局视图，使用增量 diff 策略 |
| **Signal Generator** | 从当日新增 Change Cards + Alerts 提炼首页 Signal 的 LLM 阶段，在 `writer.py` 之后运行 |
| **PR gate（人工审核门禁）** | Pipeline 生成内容以 Pull Request 形式提交，审核者合并后才触发部署，确保 LLM 输出不直接上线 |
| **evidence（证据溯源）** | Change Card 必填字段，包含 `source_release`（Release 文件 ID）、`quote`（原文短引用，必填主定位手段）、`anchor`（段落锚点，可选），使每个事实可回溯验证 |
| **Pipeline** | 从 Collector 到 Signal Generator 的完整自动化数据处理流程，以 GitHub Actions 定时触发 |
| **card_id（卡片身份）** | 由代码确定性生成的卡片唯一标识（product + release 日期 + 证据内容哈希前 6 位），与 LLM 输出解耦，重处理时用于对账（见 9.6） |
| **machine region（机器区块）** | 正文中由 `<!-- chronolog:begin/end -->` 标记包裹的区域，Pipeline 幂等重写；区块之外属于人类（见 6.5） |
| **human_overrides** | frontmatter 中人类独占的覆盖块：人工不认同机器字段值时在此声明，站点展示时优先于机器字段，Pipeline 永不修改（见 6.5） |
| **Backfill（历史回填）** | 产品接入时一次性拉取数据源全部可得历史并走完整管线，使站点上线即具备时间纵深（见 6.2.2） |
| **Review Tier（审核分级）** | 按风险分级的审核策略：Tier A（事实层，Phase 3 起自动通道 + 抽查）/ Tier B（推测层、候选主题、Alerts、Signal 等，必经人审）（见 11.1） |
| **Golden Set（黄金样本集）** | `_evals/` 中维护的「输入 → 期望输出」样本集，Prompt/词表/模型变更时在 CI 跑回归，防止质量回退（见 9.7） |
| **superseded** | 重处理后失去对应证据的旧卡片标记：不物理删除以保护入链，待人工确认归档（见 9.6） |
| **theme_outlier（主题离群标记）** | 卡片 embedding 距其主题质心过远时的软标记，提示审核优先核对主题归类，不入 DLQ（见 9.7） |
| **弱信号观察站（Silence & Revisions）** | 站点一级版块，聚合沉默检测与改写检测两类弱信号（「谁沉默了」+「谁悄悄改口」），见 7.2 |
