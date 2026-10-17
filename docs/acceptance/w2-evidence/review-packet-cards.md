# W2 卡片定义人工复核包 — 2026-10-17

状态：**待人工复核。** 由 `w2-cards-20261017-r2` 回放生成（输入：`docs/acceptance/m3-evidence/live-generation-38668187171/generation/collection.json.gz`，reconcile 开启）。本文件只列样本与规模，不代表人工结论。

## 判定口径

卡片定义（设计评审 P3，方案 B + B+ 关键词试点）：一张卡是“一次公告中可独立理解的一项变化”。

- 有功能小标题的公告：一个小标题及其正文为一张卡，标题取小标题，证据为该节全部段落与条目；`kind` 默认 `launch`。
- 平台或套餐小标题（Web、iOS、Plus 等）下的条目、前言中不超过 8 条的列表：每条一张卡，平台写入 `scope`。以冒号结尾的段落后紧跟的列表条目，若无主题或与该段主题相同，并入该段的卡。
- 前言或无小标题正文中的连续段落：同一主题（主题互在对方的匹配列表中即可；无主题段落不打断）合并为一张卡；若整个 Release 只得到一张这类卡且 Release 标题有信息量，卡片标题取 Release 标题。
- 列表模式（“What’s changed”“Bug fixes”“Improvements (N)↓↑”等通用小标题下、超过 8 条的前言列表、GitHub Release）：逐条分类并应用跳过规则；无主题条目进入待审；匹配高信号规则（`Introducing `、`Added /命令`、`… now on/enabled by default`、`is now generally available`、`You can now `、`New: `、≥ 60 字符的 `now available`）的条目单独成卡；其余按主题聚合为每 Release 每主题一张摘要卡（`kind: digest`），只有一条时按普通卡呈现。
- 前言中的上市或推送段落（以 Available、Rolling out、Now available 开头，或形如“X is/are (now) rolling out/available”）并入前一张有主题的卡；没有这样的卡时按普通段落处理。小节中的同类文字仍留在该小节。
- 摘要卡标题中的 Release 名：GitHub 用版本号；Cursor 在 changelog URL 为版本时用版本（如 0.48.x）；其余取标题，超过 40 字符时在词边界截断并加“…”。
- 取消每 Release 5 张上限。`card_id` 由产品、日期、Release 与全部证据 quote 依次拼接后哈希得到；单证据卡的 id 与原来相同。

抽样：三个产品各 20 张，按 `(date, card_id)` 排序活动卡后等距选取（第 i 张取下标 ⌊(i+0.5)·n/20⌋），前 7 张为 early、中 7 张为 middle、后 6 张为 recent。B+ 样本为固定种子（20261017）随机抽取的 15 张；摘要卡取证据条数最多的 10 张。

判定方法：在每条 `判定：` 后填写“通过”或“不通过：理由”。关注：卡片是否可独立理解、证据是否属于同一变化、标题是否可读、主题与 kind 是否合理、摘要卡是否值得作为单元、B+ 条目是否值得单独成卡。

## 规模

| 产品 | 活动卡 | launch | expansion | pricing | policy | fix | digest | change |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| ChatGPT | 485 | 53 | 22 | 11 | 21 | 0 | 4 | 374 |
| Claude Code | 1,199 | 7 | 3 | 18 | 7 | 35 | 490 | 639 |
| Cursor | 771 | 253 | 1 | 12 | 4 | 1 | 87 | 413 |

- 摘要卡 581 张，内含 1,912 条；B+ 独立卡 52 张（Claude Code 45，Cursor 7）。
- 候选行覆盖（出现在任一活动卡证据中的候选行 / 候选行）：ChatGPT 606/813（74.5%），Claude Code 2,356/6,948（33.9%），Cursor 1,231/1,807（68.1%）。
- 待审行：ChatGPT 61，Claude Code 463，Cursor 171。

## 一、卡片样本（60 张）

### S01 · chatgpt · 2023-03-14 · early

- ID：`chatgpt-2023-03-14-7153e9`
- kind：`launch`；主题：`model-support`
- 标题：Announcing GPT-4 in ChatGPT
- 来源 Release：[Announcing GPT-4 in ChatGPT](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- 卡片文件：`Changes/ChatGPT/2023-03-14-we-re-excited-to-bring-gpt-4-our-latest-model-to-our-chatgpt-plus-subscribers-gp-7153e9.md`

**证据（5 条）：**

> We’re excited to bring GPT-4, our latest model, to our ChatGPT Plus subscribers.GPT-4 has enhanced capabilities in:

> Advanced reasoning

> Complex instructions

> More creativity

> To give every Plus subscriber a chance to try the model, we'll dynamically adjust the cap for GPT-4 usage based on demand. You can learn more about GPT-4 here.For this release, there are no updates to free accounts.

判定：

### S02 · chatgpt · 2023-08-09 · early

- ID：`chatgpt-2023-08-09-963d1e`
- kind：`expansion`；主题：`memory`
- 标题：Custom instructions are now available to free users
- 来源 Release：[Custom instructions are now available to free users](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- 卡片文件：`Changes/ChatGPT/2023-08-09-custom-instructions-are-now-available-to-chatgpt-users-on-the-free-plan-except-f-963d1e.md`

**证据（1 条）：**

> Custom instructions are now available to ChatGPT users on the free plan, except for in the EU UK where we will be rolling it out soon!Customize your interactions with ChatGPT by providing specific details and guidelines for your chats.To add your instructions:

判定：

### S03 · chatgpt · 2024-11-19 · early

- ID：`chatgpt-2024-11-19-3d4db6`
- kind：`change`；主题：`mobile-desktop`
- 标题：Advanced Voice for ChatGPT Web
- 来源 Release：[Advanced Voice for ChatGPT Web](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- 卡片文件：`Changes/ChatGPT/2024-11-19-starting-today-we-re-beginning-to-roll-out-advanced-voice-mode-on-web-already-av-3d4db6.md`

**证据（1 条）：**

> Starting today, we’re beginning to roll out Advanced Voice Mode on web (already available on mobile and desktop apps). You can now start a voice chat on chatgpt.com on your desktop and have real-time, natural conversations with ChatGPT while doing tasks like shopping, planning, writing, and brainstorming.We’re starting to roll out to all paid (Plus, Team, Enterprise, and Edu) users today, and expect it to take a few days.

判定：

### S04 · chatgpt · 2025-02-28 · early

- ID：`chatgpt-2025-02-28-a40c3f`
- kind：`change`；主题：`mobile-desktop`
- 标题：Long press to select text on iOS and moved the message quick actions to always…
- 来源 Release：[- General - iOS - Long press to select text on iOS and moved the message quick actions to always be visible below the me](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- 卡片文件：`Changes/ChatGPT/2025-02-28-long-press-to-select-text-on-ios-and-moved-the-message-quick-actions-to-always-b-a40c3f.md`

**证据（1 条）：**

> Long press to select text on iOS and moved the message quick actions to always be visible below the message:

判定：

### S05 · chatgpt · 2025-05-08 · early

- ID：`chatgpt-2025-05-08-ad2e25`
- kind：`change`；主题：`search-browsing`
- 标题：GitHub connector for deep research for Plus/Pro/Team
- 来源 Release：[GitHub connector for deep research for Plus/Pro/Team](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- 卡片文件：`Changes/ChatGPT/2025-05-08-chatgpt-deep-research-with-github-is-available-globally-to-team-users-it-is-also-ad2e25.md`

**证据（1 条）：**

> ChatGPT deep research with GitHub is available globally to Team users. It is also gradually rolling out to Plus and Pro users, except for those in the EEA, Switzerland, and the UK. Enterprise user access will be announced at a later date.See: Connecting GitHub to ChatGPT deep research.

判定：

### S06 · chatgpt · 2025-06-12 · early

- ID：`chatgpt-2025-06-12-cd0103`
- kind：`change`；主题：`memory`
- 标题：Improvements to memory to reference past chats in a project*
- 来源 Release：[Adding More Capabilities to Projects](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- 卡片文件：`Changes/ChatGPT/2025-06-12-improvements-to-memory-to-reference-past-chats-in-a-project.md`

**证据（1 条）：**

> Improvements to memory to reference past chats in a project*

判定：

### S07 · chatgpt · 2025-08-11 · early

- ID：`chatgpt-2025-08-11-196b01`
- kind：`change`；主题：`collaboration`
- 标题：Pro: Microsoft Teams and GitHub
- 来源 Release：[Additional connectors for Plus and Pro](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- 卡片文件：`Changes/ChatGPT/2025-08-11-pro-microsoft-teams-and-github.md`

**证据（1 条）：**

> Pro: Microsoft Teams and GitHub

判定：

### S08 · chatgpt · 2025-09-22 · middle

- ID：`chatgpt-2025-09-22-6c0a54`
- kind：`change`；主题：`memory`
- 标题：Longer memory for more personalized responses
- 来源 Release：[ChatGPT Go now available in Indonesia](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- 卡片文件：`Changes/ChatGPT/2025-09-22-longer-memory-for-more-personalized-responses.md`

**证据（1 条）：**

> Longer memory for more personalized responses

判定：

### S09 · chatgpt · 2025-10-28 · middle

- ID：`chatgpt-2025-10-28-0fda81`
- kind：`expansion`；主题：`pricing-model`
- 标题：ChatGPT launches ChatGPT Go, our low cost subscription plan, in Brazil
- 来源 Release：[ChatGPT Go now available in Brazil](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- 卡片文件：`Changes/ChatGPT/2025-10-28-we-re-launching-chatgpt-go-our-low-cost-subscription-plan-in-brazil-chatgpt-go-p.md`

**证据（1 条）：**

> We're launching ChatGPT Go, our low cost subscription plan, in Brazil. ChatGPT Go provides everything included in the Free plan, and:

判定：

### S10 · chatgpt · 2025-12-18 · middle

- ID：`chatgpt-2025-12-18-34e422`
- kind：`launch`；主题：`apps-integrations`
- 标题：Introducing the app directory in ChatGPT
- 来源 Release：[Introducing the app directory in ChatGPT](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- 卡片文件：`Changes/ChatGPT/2025-12-18-you-can-now-browse-and-add-approved-apps-in-the-new-app-directory-apps-let-you-w.md`

**证据（1 条）：**

> You can now browse and add approved apps in the new app directory. Apps let you work with your tools and data directly inside a conversation—from interactive in-chat experiences to secure connections that allow ChatGPT to search and reference information from third-party services.As part of this update, connectors now appear in the directory as apps, making it easier to manage all your tools in one place. References across the Help Center have been updated to reflect this new terminology.Apps are available to all logged-in ChatGPT users, with availability and functionality varying by plan and region. Some apps or capabilities may not be available in certain regions or may require specific plan tiers.Additionally, developers can submit apps for review and publication in the app directory, making approved apps available to a broader set of ChatGPT users.

判定：

### S11 · chatgpt · 2026-02-13 · middle

- ID：`chatgpt-2026-02-13-b72ef5`
- kind：`change`；主题：`reliability-performance`；范围：iOS
- 标题：Performance improvements
- 来源 Release：[ChatGPT updates: Better file uploads, easier copying, and more reliable long chats](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- 卡片文件：`Changes/ChatGPT/2026-02-13-performance-improvements-we-ve-made-multiple-performance-enhancements-to-improve.md`

**证据（1 条）：**

> Performance improvements. We’ve made multiple performance enhancements to improve responsiveness and overall speed throughout the app.

判定：

### S12 · chatgpt · 2026-03-17 · middle

- ID：`chatgpt-2026-03-17-09905d`
- kind：`policy`；主题：`memory`
- 标题：Sunsetting the “Nerdy” base style
- 来源 Release：[Sunsetting the “Nerdy” base style](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- 卡片文件：`Changes/ChatGPT/2026-03-17-we-re-sunsetting-the-preset-nerdy-base-style-to-simplify-options-and-improve-res.md`

**证据（1 条）：**

> We’re sunsetting the preset Nerdy base style to simplify options and improve response quality. Users who selected it will be moved to the default personality. You can manage personality settings anytime in ChatGPT under Settings → Personalization.

判定：

### S13 · chatgpt · 2026-04-22 · middle

- ID：`chatgpt-2026-04-22-432031`
- kind：`launch`；主题：`account-access`
- 标题：ChatGPT for Clinicians
- 来源 Release：[ChatGPT for Clinicians](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- 卡片文件：`Changes/ChatGPT/2026-04-22-we-re-launching-chatgpt-for-clinicians-a-free-version-of-chatgpt-for-verified-cl.md`

**证据（1 条）：**

> We’re launching ChatGPT for Clinicians, a free version of ChatGPT for verified clinicians in the United States. It’s designed to support real clinical work at the time of care, including evidence review, documentation, and medical research, with trusted clinical search, citations, reusable skills, deep research across medical literature, and support for earning CME credits on eligible clinical questions.If you already have a ChatGPT account, you can use that same account to sign up. After signup, ChatGPT for Clinicians appears as a separate workspace under the same login, and your existing ChatGPT workspace remains available.For more information, please see our help article ChatGPT for Clinicians or our blog post Making ChatGPT better for clinicians.

判定：

### S14 · chatgpt · 2026-06-08 · middle

- ID：`chatgpt-2026-06-08-725bc9`
- kind：`change`；主题：`mobile-desktop`；范围：Android
- 标题：Cleaner edit-message flow
- 来源 Release：[ChatGPT app experience updates](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- 卡片文件：`Changes/ChatGPT/2026-06-08-cleaner-edit-message-flow-android-now-makes-it-clearer-when-you-re-editing-a-pre.md`

**证据（1 条）：**

> Cleaner edit-message flow: Android now makes it clearer when you’re editing a previous message.

判定：

### S15 · chatgpt · 2026-06-18 · recent

- ID：`chatgpt-2026-06-18-55d7b8`
- kind：`change`；主题：`interface-experience`；范围：Web
- 标题：Easier pinning and sidebar organization
- 来源 Release：[ChatGPT app experience updates](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- 卡片文件：`Changes/ChatGPT/2026-06-18-easier-pinning-and-sidebar-organization-it-s-now-easier-to-keep-important-work-c.md`

**证据（1 条）：**

> Easier pinning and sidebar organization: It’s now easier to keep important work close in ChatGPT. You can pin chats and projects directly from the sidebar, and your Pinned section now includes both chats and projects. You can also organize Recents as one combined list, or group chats by project so related work stays together.

判定：

### S16 · chatgpt · 2026-07-09 · recent

- ID：`chatgpt-2026-07-09-ed8dc0`
- kind：`change`；主题：`mobile-desktop`
- 标题：Beginning July 9, users on web, iOS, and Android will no longer be able to create…
- 来源 Release：[Retiring group chats in ChatGPT](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- 卡片文件：`Changes/ChatGPT/2026-07-09-beginning-july-9-users-on-web-ios-and-android-will-no-longer-be-able-to-create-n.md`

**证据（1 条）：**

> Beginning July 9, users on web, iOS, and Android will no longer be able to create new group chats, turn existing conversations into group chats, or join a group chat through an invite link.

判定：

### S17 · chatgpt · 2026-08-13 · recent

- ID：`chatgpt-2026-08-13-513ff2`
- kind：`change`；主题：`enterprise-admin`
- 标题：Computer History for macOS
- 来源 Release：[Computer History for macOS](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- 卡片文件：`Changes/ChatGPT/2026-08-13-computer-history-is-an-optional-feature-in-the-chatgpt-macos-app-that-lets-chatg.md`

**证据（1 条）：**

> Computer History is an optional feature in the ChatGPT macOS app that lets ChatGPT and Codex reference selected activity from apps and websites, helping users continue work without re-explaining every detail. It records interaction events—not screenshots, screen recordings, microphone input, or system audio—and private browsing is not included.Computer History is off by default and available to Pro, Business, and Enterprise users. Business and Enterprise admins must grant access before members can opt in. Users can pause Computer History, choose included apps and sites, and inspect or delete timeline items. Note that Computer History is not currently available in the EEA, UK or Switzerland.

判定：

### S18 · chatgpt · 2026-08-27 · recent

- ID：`chatgpt-2026-08-27-44247e`
- kind：`digest`；主题：`memory`
- 标题：3 Memory and Personalization changes in More controls in temporary chat
- 来源 Release：[More controls in temporary chat](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- 卡片文件：`Changes/ChatGPT/2026-08-27-3-memory-and-personalization-changes-in-more-controls-in-temporary-chat.md`

**证据（3 条）：**

> Personalized: When you create a temporary chat, you can choose to have personalized responses. Personalized temporary chats can use your memories, custom instructions, and plugins to tailor responses. They do not create new memories and remain out of your chat history unless you save them. Personalization can be set only when you start a temporary chat and cannot be changed after the conversation begins.

> Non-personalized: By default, temporary chats are not personalized. Non-personalized temporary chats do not use memory, custom instructions, or plugins, and they do not create new memories.

> Saving a temporary chat: When a conversation becomes useful for the future, you can add it to your chat history. Saving converts it into a regular chat, so it then follows your account-level personalization settings and model-improvement preferences. For example, if you have memory enabled and save a temporary chat, this will become part of your chat history and can be referenced to personalized future responses.

判定：

### S19 · chatgpt · 2026-09-10 · recent

- ID：`chatgpt-2026-09-10-aacea7`
- kind：`change`；主题：`apps-integrations`
- 标题：Data plugin in ChatGPT Work and Codex
- 来源 Release：[Data plugin in ChatGPT Work and Codex](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- 卡片文件：`Changes/ChatGPT/2026-09-10-the-data-plugin-helps-you-analyze-connected-business-data-in-chatgpt-work-and-co.md`

**证据（1 条）：**

> The Data plugin helps you analyze connected business data in ChatGPT Work and Codex. Ask a business question, investigate changes, or create an interactive dashboard or report. You can refine the analysis with follow-up questions and bring in your team’s metric definitions and other business context.To get started, install Data from the plugin directory, then start a conversation with @Data. Connected sources may require setup or authorization, and queries use your connected account’s existing permissions. Learn more.

判定：

### S20 · chatgpt · 2026-09-29 · recent

- ID：`chatgpt-2026-09-29-5ed430`
- kind：`pricing`；主题：`pricing-model`
- 标题：Pro 200 subscriptions
- 来源 Release：[Pro 200 subscriptions](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- 卡片文件：`Changes/ChatGPT/2026-09-29-pro-200-is-available-for-new-subscriptions-again-at-200-month-5ed430.md`

**证据（2 条）：**

> Pro 200 is available for new subscriptions again at $200/month.

> Included usage allowances are changing. Users affected by these changes will receive an email with additional details. The monthly price remains $200.

判定：

### S21 · claude-code · 2026-01-14 · early

- ID：`claude-code-2026-01-14-1c7708`
- kind：`change`；主题：`agent-mode`
- 标题：Added inline display of agent's final response in task notifications, making…
- 来源 Release：[v2.1.7](https://github.com/anthropics/claude-code/releases/tag/v2.1.7)
- 卡片文件：`Changes/Claude Code/2026-01-14-added-inline-display-of-agent-s-final-response-in-task-notifications-making-it-e.md`

**证据（1 条）：**

> Added inline display of agent's final response in task notifications, making it easier to see results without reading the full transcript file

判定：

### S22 · claude-code · 2026-02-05 · early

- ID：`claude-code-2026-02-05-b2014f`
- kind：`change`；主题：`memory`
- 标题：Claude now automatically records and recalls memories as it works
- 来源 Release：[v2.1.32](https://github.com/anthropics/claude-code/releases/tag/v2.1.32)
- 卡片文件：`Changes/Claude Code/2026-02-05-claude-now-automatically-records-and-recalls-memories-as-it-works.md`

**证据（1 条）：**

> Claude now automatically records and recalls memories as it works

判定：

### S23 · claude-code · 2026-03-05 · early

- ID：`claude-code-2026-03-05-029012`
- kind：`digest`；主题：`agent-mode`
- 标题：2 Agent Mode changes in v2.1.69
- 来源 Release：[v2.1.69](https://github.com/anthropics/claude-code/releases/tag/v2.1.69)
- 卡片文件：`Changes/Claude Code/2026-03-05-2-agent-mode-changes-in-v2-1-69.md`

**证据（2 条）：**

> Added `agent_id` (for subagents) and `agent_type` (for subagents and `--agent`) to hook events

> Reduced token usage on multi-agent tasks with more concise subagent final reports

判定：

### S24 · claude-code · 2026-03-17 · early

- ID：`claude-code-2026-03-17-4c7440`
- kind：`change`；主题：`interface-experience`
- 标题：`/copy` now accepts an optional index: `/copy N` copies the Nth-latest assistant response
- 来源 Release：[v2.1.77](https://github.com/anthropics/claude-code/releases/tag/v2.1.77)
- 卡片文件：`Changes/Claude Code/2026-03-17-copy-now-accepts-an-optional-index-copy-n-copies-the-nth-latest-assistant-respon.md`

**证据（1 条）：**

> `/copy` now accepts an optional index: `/copy N` copies the Nth-latest assistant response

判定：

### S25 · claude-code · 2026-04-01 · early

- ID：`claude-code-2026-04-01-071170`
- kind：`digest`；主题：`apps-integrations`
- 标题：3 Apps and Integrations changes in v2.1.89
- 来源 Release：[v2.1.89](https://github.com/anthropics/claude-code/releases/tag/v2.1.89)
- 卡片文件：`Changes/Claude Code/2026-04-01-3-apps-and-integrations-changes-in-v2-1-89.md`

**证据（3 条）：**

> Added `MCP_CONNECTION_NONBLOCKING=true` for `-p` mode to skip the MCP connection wait entirely, and bounded `--mcp-config` server connections at 5s instead of blocking on the slowest server

> Improved `@`-mention typeahead to rank source files above MCP resources with similar names

> Documented `TaskCreated` hook event and its blocking behavior

判定：

### S26 · claude-code · 2026-04-13 · early

- ID：`claude-code-2026-04-13-d48da1`
- kind：`digest`；主题：`developer-workflow`
- 标题：2 Developer Workflow changes in v2.1.105
- 来源 Release：[v2.1.105](https://github.com/anthropics/claude-code/releases/tag/v2.1.105)
- 卡片文件：`Changes/Claude Code/2026-04-13-2-developer-workflow-changes-in-v2-1-105.md`

**证据（2 条）：**

> Added `path` parameter to the `EnterWorktree` tool to switch into an existing worktree of the current repository

> Improved stale agent worktree cleanup to remove worktrees whose PR was squash-merged instead of keeping them indefinitely

判定：

### S27 · claude-code · 2026-04-23 · early

- ID：`claude-code-2026-04-23-d0548b`
- kind：`digest`；主题：`agent-mode`
- 标题：2 Agent Mode changes in v2.1.119
- 来源 Release：[v2.1.119](https://github.com/anthropics/claude-code/releases/tag/v2.1.119)
- 卡片文件：`Changes/Claude Code/2026-04-23-2-agent-mode-changes-in-v2-1-119.md`

**证据（2 条）：**

> `--print` mode now honors the agent's `tools:` and `disallowedTools:` frontmatter, matching interactive-mode behavior

> `--agent <name>` now honors the agent definition's `permissionMode` for built-in agents

判定：

### S28 · claude-code · 2026-05-11 · middle

- ID：`claude-code-2026-05-11-f9ade4`
- kind：`change`；主题：`interface-experience`
- 标题：Added transcript view navigation
- 来源 Release：[v2.1.139](https://github.com/anthropics/claude-code/releases/tag/v2.1.139)
- 卡片文件：`Changes/Claude Code/2026-05-11-added-transcript-view-navigation-for-keyboard-shortcuts-to-jump-between-user-pro.md`

**证据（1 条）：**

> Added transcript view navigation: `?` for keyboard shortcuts, `{`/`}` to jump between user prompts, `v` to toggle shortcut panel

判定：

### S29 · claude-code · 2026-05-27 · middle

- ID：`claude-code-2026-05-27-db0b19`
- kind：`change`；主题：`reliability-performance`
- 标题：The `/usage` breakdown now includes large session files
- 来源 Release：[v2.1.152](https://github.com/anthropics/claude-code/releases/tag/v2.1.152)
- 卡片文件：`Changes/Claude Code/2026-05-27-the-usage-breakdown-now-includes-large-session-files-files-are-scanned-with-a-st.md`

**证据（1 条）：**

> The `/usage` breakdown now includes large session files; files are scanned with a streaming read so memory usage stays flat

判定：

### S30 · claude-code · 2026-06-08 · middle

- ID：`claude-code-2026-06-08-212874`
- kind：`change`；主题：`context-window`
- 标题：The "CLAUDE.md is too long" warning threshold now scales with the model's context window
- 来源 Release：[v2.1.169](https://github.com/anthropics/claude-code/releases/tag/v2.1.169)
- 卡片文件：`Changes/Claude Code/2026-06-08-the-claude-md-is-too-long-warning-threshold-now-scales-with-the-model-s-context.md`

**证据（1 条）：**

> The "CLAUDE.md is too long" warning threshold now scales with the model's context window

判定：

### S31 · claude-code · 2026-06-25 · middle

- ID：`claude-code-2026-06-25-321283`
- kind：`change`；主题：`editor-experience`
- 标题：Added live file path autocomplete to bash mode (`!`)
- 来源 Release：[v2.1.193](https://github.com/anthropics/claude-code/releases/tag/v2.1.193)
- 卡片文件：`Changes/Claude Code/2026-06-25-added-live-file-path-autocomplete-to-bash-mode.md`

**证据（1 条）：**

> Added live file path autocomplete to bash mode (`!`)

判定：

### S32 · claude-code · 2026-07-11 · middle

- ID：`claude-code-2026-07-11-73bf42`
- kind：`digest`；主题：`agent-mode`
- 标题：2 Agent Mode changes in v2.1.207
- 来源 Release：[v2.1.207](https://github.com/anthropics/claude-code/releases/tag/v2.1.207)
- 卡片文件：`Changes/Claude Code/2026-07-11-2-agent-mode-changes-in-v2-1-207.md`

**证据（2 条）：**

> Improved agent view: blocked session peeks now lead with the question and show a worded staleness clock (`waiting 3m`) instead of the same timestamp twice

> Changed auto mode to no longer read `autoMode` from `.claude/settings.local.json` (repo-resident); use `~/.claude/settings.json` instead

判定：

### S33 · claude-code · 2026-07-24 · middle

- ID：`claude-code-2026-07-24-6f2546`
- kind：`digest`；主题：`model-support`
- 标题：3 Model Support changes in v2.1.219
- 来源 Release：[v2.1.219](https://github.com/anthropics/claude-code/releases/tag/v2.1.219)
- 卡片文件：`Changes/Claude Code/2026-07-24-3-model-support-changes-in-v2-1-219.md`

**证据（3 条）：**

> Added Claude Opus 5 (`claude-opus-5`), now the default Opus model — 1M context, fast mode at $10/$50 per Mtok

> Removed Opus 4.7 from fast mode; `/fast` now applies to Opus 5 and Opus 4.8

> Updated the claude-api skill to default to Claude Opus 5, with a migration path from Opus 4.8

判定：

### S34 · claude-code · 2026-08-14 · middle

- ID：`claude-code-2026-08-14-943fd4`
- kind：`change`；主题：`agent-mode`
- 标题：Improved `claude self-hosted-runner` session start time
- 来源 Release：[v2.1.233](https://github.com/anthropics/claude-code/releases/tag/v2.1.233)
- 卡片文件：`Changes/Claude Code/2026-08-14-improved-claude-self-hosted-runner-session-start-time-the-session-branch-is-now.md`

**证据（1 条）：**

> Improved `claude self-hosted-runner` session start time: the session branch is now created without rewriting the working tree, and two server round trips no longer block the agent's launch

判定：

### S35 · claude-code · 2026-08-27 · recent

- ID：`claude-code-2026-08-27-053af9`
- kind：`change`；主题：`developer-workflow`
- 标题：Changed Anthropic telemetry export failures to log at debug level…
- 来源 Release：[v2.1.248](https://github.com/anthropics/claude-code/releases/tag/v2.1.248)
- 卡片文件：`Changes/Claude Code/2026-08-27-changed-anthropic-telemetry-export-failures-to-log-at-debug-level-as-anthropic-t.md`

**证据（1 条）：**

> Changed Anthropic telemetry export failures to log at debug level as `[Anthropic telemetry]` instead of `[3P telemetry] OTEL diag error`, so they are not mistaken for your OTel collector failing

判定：

### S36 · claude-code · 2026-09-08 · recent

- ID：`claude-code-2026-09-08-f57b1e`
- kind：`change`；主题：`agent-mode`
- 标题：Improved `/workflows` agent detail
- 来源 Release：[v2.1.265](https://github.com/anthropics/claude-code/releases/tag/v2.1.265)
- 卡片文件：`Changes/Claude Code/2026-09-08-improved-workflows-agent-detail-tool-calls-are-marked-running-failed-or-done-the.md`

**证据（1 条）：**

> Improved `/workflows` agent detail: tool calls are marked running, failed or done, the subagent's task list is shown when it has one, and Enter unfolds the listed calls with their inputs and results

判定：

### S37 · claude-code · 2026-09-17 · recent

- ID：`claude-code-2026-09-17-3f047e`
- kind：`policy`；主题：`account-access`
- 标题：Improved Claude apps gateway sign-in rate limit errors
- 来源 Release：[v2.1.274](https://github.com/anthropics/claude-code/releases/tag/v2.1.274)
- 卡片文件：`Changes/Claude Code/2026-09-17-improved-claude-apps-gateway-sign-in-rate-limit-errors-login-now-explains-the-re.md`

**证据（1 条）：**

> Improved Claude apps gateway sign-in rate limit errors: `/login` now explains the refusal, and the gateway log says which limit was hit and which setting to change

判定：

### S38 · claude-code · 2026-09-24 · recent

- ID：`claude-code-2026-09-24-b8440f`
- kind：`digest`；主题：`apps-integrations`
- 标题：8 Apps and Integrations changes in v2.1.282
- 来源 Release：[v2.1.282](https://github.com/anthropics/claude-code/releases/tag/v2.1.282)
- 卡片文件：`Changes/Claude Code/2026-09-24-8-apps-and-integrations-changes-in-v2-1-282.md`

**证据（8 条）：**

> Added the `allowClaudeInChromeWithManagedMcp` managed setting to let `claude --chrome` run alongside an exclusive `managed-mcp.json`; the error shown when Chrome is blocked now names it

> Added `store.readiness_grace_seconds` to the Claude apps gateway so `/readyz` can stay ready through a short Postgres outage such as a database failover

> Changed `Skill(anthropic-skills:*)` and `Skill(claude-ai:*)` allow rules to cover only skills synced from claude.ai, not plugins or other skills that merely use such a name

> Changed skill folders, command files and workflow commands in the `anthropic-skills` or `claude-ai` namespace to no longer load; a plugin so named still loads but yields name ties to synced skills

> Changed MCP servers configured under the name `anthropic-skills` or `claude-ai` to list no skills or prompts (their tools still work); rename the server in your MCP configuration to list them again

> [Cloud sessions] Added Claude GitHub App status to Settings › Connectors › GitHub: whether the app is installed and reachable for your account, plus steps to connect, install or reconnect

> [Cloud sessions] Added attaching a repository from a different GitHub owner, such as a fork's upstream, to a running cloud session that already has one, including sessions started from Slack

> [Claude Tag] Changed the bordered cards Claude uses in Slack replies for plans, tables and details to render wide by default instead of a narrow width

判定：

### S39 · claude-code · 2026-10-02 · recent

- ID：`claude-code-2026-10-02-37b0db`
- kind：`digest`；主题：`developer-workflow`
- 标题：3 Developer Workflow changes in v2.1.288
- 来源 Release：[v2.1.288](https://github.com/anthropics/claude-code/releases/tag/v2.1.288)
- 卡片文件：`Changes/Claude Code/2026-10-02-3-developer-workflow-changes-in-v2-1-288.md`

**证据（3 条）：**

> Added a built-in `gh api` to cloud sessions whose image has no GitHub CLI, and fixed the built-in sending control characters from file names, jq filters or GitHub errors to the terminal

> Added `--max-findings <n>|all` to /code-review to report more or fewer findings than the usual limit; the choice is reused until you pass `--max-findings default`

> Self-hosted runner: Improved the built-in `gh api`: a refused gh command now prints its `gh api` equivalent, `--paginate` follows every page of a repository's lists, and a nested `claude` no longer removes it

判定：

### S40 · claude-code · 2026-10-09 · recent

- ID：`claude-code-2026-10-09-9252d3`
- kind：`pricing`；主题：`pricing-model`
- 标题：Updated `/cost`, the status line, `--max-budget-usd` and the SDK's cost figures…
- 来源 Release：[v2.1.296](https://github.com/anthropics/claude-code/releases/tag/v2.1.296)
- 卡片文件：`Changes/Claude Code/2026-10-09-updated-cost-the-status-line-max-budget-usd-and-the-sdk-s-cost-figures-to-price.md`

**证据（1 条）：**

> Updated `/cost`, the status line, `--max-budget-usd` and the SDK's cost figures to price Sonnet 5.5 cache reads at $0.10 per million tokens (was $0.20)

判定：

### S41 · cursor · 2023-04-14 · early

- ID：`cursor-2023-04-14-1f7f6d`
- kind：`change`；主题：`editor-experience`
- 标题：Hover over an error to have the AI explain it/fix it
- 来源 Release：[Enhanced Error Handling (2023-04-14)](https://cursor.com/changelog/0-2-3)
- 卡片文件：`Changes/Cursor/2023-04-14-hover-over-an-error-to-have-the-ai-explain-it-fix-it.md`

**证据（1 条）：**

> Hover over an error to have the AI explain it/fix it

判定：

### S42 · cursor · 2023-06-27 · early

- ID：`cursor-2023-06-27-2d16b7`
- kind：`change`；主题：`apps-integrations`
- 标题：cursor:// deep linking works now, so you should be able to log in to extensions
- 来源 Release：[Hotfixes](https://cursor.com/changelog/0-2-36)
- 卡片文件：`Changes/Cursor/2023-06-27-cursor-deep-linking-works-now-so-you-should-be-able-to-log-in-to-extensions.md`

**证据（1 条）：**

> cursor:// deep linking works now, so you should be able to log in to extensions

判定：

### S43 · cursor · 2023-08-12 · early

- ID：`cursor-2023-08-12-e1c4d2`
- kind：`change`；主题：`editor-experience`
- 标题：Followups in edits
- 来源 Release：[Followups in edits](https://cursor.com/changelog/0-7-8-nightly)
- 卡片文件：`Changes/Cursor/2023-08-12-the-cmd-k-edits-now-support-followups-this-is-an-early-preview-please-let-us-kno.md`

**证据（1 条）：**

> The cmd-k edits now support followups! This is an early preview — please let us know of any annoyances or bugs, or if you preferred the no-followup mode. Please please send all feedback you have in the Discord channel!

判定：

### S44 · cursor · 2023-10-01 · early

- ID：`cursor-2023-10-01-3b67a3`
- kind：`change`；主题：`developer-workflow`
- 标题：Ask about git commits and PRs using @git in chat!
- 来源 Release：[Indexing, cmd-k in terminal, @git, /edit, bugfixes](https://cursor.com/changelog/0-12-0)
- 卡片文件：`Changes/Cursor/2023-10-01-ask-about-git-commits-and-prs-using-git-in-chat.md`

**证据（1 条）：**

> Ask about git commits and PRs using @git in chat!

判定：

### S45 · cursor · 2024-01-06 · early

- ID：`cursor-2024-01-06-3c3785`
- kind：`change`；主题：`developer-workflow`
- 标题：Better Remote Support
- 来源 Release：[Better Remote Support](https://cursor.com/changelog/0-21-6-nightly)
- 卡片文件：`Changes/Cursor/2024-01-06-wsl-and-dev-containers-should-now-work-properly.md`

**证据（1 条）：**

> WSL and Dev Containers should now work properly.

判定：

### S46 · cursor · 2024-05-03 · early

- ID：`cursor-2024-05-03-78eee8`
- kind：`change`；主题：`reliability-performance`
- 标题：UPDATE (0.33.1–0.33.3): Fix to settings toggles, fix to Copilot++ diffbox…
- 来源 Release：[Networking Stability, Command-K Autoselect](https://cursor.com/changelog/0-33-x)
- 卡片文件：`Changes/Cursor/2024-05-03-update-0-33-1-0-33-3-fix-to-settings-toggles-fix-to-copilot-diffbox-performance.md`

**证据（1 条）：**

> UPDATE (0.33.1–0.33.3): Fix to settings toggles, fix to Copilot++ diffbox performance, onboarding tweaks.

判定：

### S47 · cursor · 2024-11-24 · early

- ID：`cursor-2024-11-24-5c27a3`
- kind：`change`；主题：`interface-experience`
- 标题：Composer UI in the sidebar with inline diffs
- 来源 Release：[New Composer UI, Agent, Commit Messages](https://cursor.com/changelog/0-43-x)
- 卡片文件：`Changes/Cursor/2024-11-24-composer-ui-in-the-sidebar-with-inline-diffs.md`

**证据（1 条）：**

> Composer UI in the sidebar with inline diffs

判定：

### S48 · cursor · 2025-03-23 · middle

- ID：`cursor-2025-03-23-abe67c`
- kind：`pricing`；主题：`pricing-model`
- 标题：Usage-based cost visibility
- 来源 Release：[Chat tabs, Custom modes & Faster indexing](https://cursor.com/changelog/0-48-x)
- 卡片文件：`Changes/Cursor/2025-03-23-usage-based-cost-visibility.md`

**证据（1 条）：**

> For usage-based models, you can now view the cost and breakdown per chat from the history.

判定：

### S49 · cursor · 2025-06-12 · middle

- ID：`cursor-2025-06-12-082e6b`
- kind：`change`；主题：`agent-mode`
- 标题：Launch Background Agents directly from Slack by mentioning @Cursor
- 来源 Release：[Background Agents in Slack](https://cursor.com/changelog/1-1)
- 卡片文件：`Changes/Cursor/2025-06-12-you-can-now-launch-background-agents-directly-from-slack-by-mentioning-cursor-ag.md`

**证据（1 条）：**

> You can now launch Background Agents directly from Slack by mentioning @Cursor. Agents can read the thread, understand what's going on, and create PRs in GitHub, all without leaving the conversation.

判定：

### S50 · cursor · 2025-08-21 · middle

- ID：`cursor-2025-08-21-927f5c`
- kind：`launch`；主题：`agent-mode`
- 标题：Run Agents in Linear
- 来源 Release：[Linear integration, improved Agent terminal, and OS notifications](https://cursor.com/changelog/1-5)
- 卡片文件：`Changes/Cursor/2025-08-21-you-can-now-start-background-agents-directly-from-linear-delegate-tasks-to-curso.md`

**证据（1 条）：**

> You can now start Background Agents directly from Linear. Delegate tasks to Cursor without leaving your issue. We've written a longer blog post with more details.

判定：

### S51 · cursor · 2025-10-29 · middle

- ID：`cursor-2025-10-29-0631ff`
- kind：`launch`；主题：`developer-workflow`
- 标题：Improved Code Review
- 来源 Release：[New Coding Model and Agent Interface](https://cursor.com/changelog/2-0)
- 卡片文件：`Changes/Cursor/2025-10-29-improved-code-review.md`

**证据（1 条）：**

> It's now easier to view all changes from Agent across multiple files without needing to jump between individual files.

判定：

### S52 · cursor · 2025-12-18 · middle

- ID：`cursor-2025-12-18-714e2a`
- kind：`launch`；主题：`agent-mode`
- 标题：Linux sandboxing for agents
- 来源 Release：[Enterprise Insights, Billing Groups, Service Accounts, and Improved Security Controls](https://cursor.com/changelog/enterprise-dec-2025)
- 卡片文件：`Changes/Cursor/2025-12-18-linux-sandboxing-for-agents.md`

**证据（2 条）：**

> Sandboxing for agents supports Linux in addition to macOS.

> This allows agents to work effectively within appropriate boundaries. Access is scoped to your workspace and can be configured to block unauthorized network and filesystem access.

判定：

### S53 · cursor · 2026-01-22 · middle

- ID：`cursor-2026-01-22-2664a4`
- kind：`launch`；主题：`image-generation`
- 标题：Image generation
- 来源 Release：[Subagents, Skills, and Image Generation](https://cursor.com/changelog/2-4)
- 卡片文件：`Changes/Cursor/2026-01-22-image-generation.md`

**证据（2 条）：**

> Generate images directly from Cursor's agent. Describe the image in text or upload a reference to guide the underlying image generation model (Google Nano Banana Pro).

> Images are returned as an inline preview and saved to your project's assets/ folder by default. This is useful for creating UI mockups, product assets, and visualizing architecture diagrams.

判定：

### S54 · cursor · 2026-02-24 · middle

- ID：`cursor-2026-02-24-c922e9`
- kind：`change`；主题：`agent-mode`
- 标题：Cloud Agents with Computer Use
- 来源 Release：[Cloud Agents with Computer Use](https://cursor.com/changelog/02-24-26)
- 卡片文件：`Changes/Cursor/2026-02-24-cloud-agents-can-now-use-the-software-they-create-to-test-changes-and-demo-their-c922e9.md`

**证据（4 条）：**

> Cloud agents can now use the software they create to test changes and demo their work.

> After onboarding onto your codebase, each agent runs in its own isolated VM with a full development environment. Cloud agents produce merge-ready PRs with artifacts (videos, screenshots, and logs) that make it possible to quickly review their changes.

> Cloud agents are available anywhere you use Cursor, including web, desktop, mobile, Slack, and GitHub.

> Get started at cursor.com/onboard to watch the agent configure itself and record a demo. Or read more in our announcement.

判定：

### S55 · cursor · 2026-04-02 · recent

- ID：`cursor-2026-04-02-eb0a5c`
- kind：`digest`；主题：`apps-integrations`
- 标题：2 Apps and Integrations changes in 3.0
- 来源 Release：[New Cursor Interface](https://cursor.com/changelog/3-0)
- 卡片文件：`Changes/Cursor/2026-04-02-2-apps-and-integrations-changes-in-3-0.md`

**证据（2 条）：**

> MCP Apps now support structured content, enabling richer tool outputs.

> Third-party plugin imports now default to off for Enterprises when unset, while preserving explicit Admin overrides.

判定：

### S56 · cursor · 2026-05-04 · recent

- ID：`cursor-2026-05-04-62e185`
- kind：`launch`；主题：`editor-experience`
- 标题：Updated usage analytics tab
- 来源 Release：[Model controls, spend management, and usage analytics](https://cursor.com/changelog/05-04-26)
- 卡片文件：`Changes/Cursor/2026-05-04-updated-usage-analytics-tab.md`

**证据（1 条）：**

> Admins can now filter usage by specific users, or break it down by product surface: clients, Cloud Agents, automations, Bugbot, and Security Review.

判定：

### S57 · cursor · 2026-05-19 · recent

- ID：`cursor-2026-05-19-af93f5`
- kind：`change`；主题：`apps-integrations`
- 标题：Install the integration from Cursor integrations
- 来源 Release：[Cursor in Jira](https://cursor.com/changelog/05-19-26)
- 卡片文件：`Changes/Cursor/2026-05-19-install-the-integration-from-cursor-integrations-you-need-cursor-admin-access-an.md`

**证据（1 条）：**

> Install the integration from Cursor integrations. You need Cursor admin access and Jira Commercial Cloud with Rovo enabled. Learn more in our docs.

判定：

### S58 · cursor · 2026-06-17 · recent

- ID：`cursor-2026-06-17-db6899`
- kind：`launch`；主题：`agent-mode`
- 标题：Handoff between local and cloud
- 来源 Release：[Cloud Environment Setup and Cloud Subagents in Agents Window](https://cursor.com/changelog/cloud-in-agents-window)
- 卡片文件：`Changes/Cursor/2026-06-17-handoff-between-local-and-cloud.md`

**证据（1 条）：**

> Move agent sessions more reliably between your local computer and the cloud. You can offload long-running work from your machine and run as many cloud agents in parallel as you want. Pull a cloud agent back down to local to test changes yourself.

判定：

### S59 · cursor · 2026-07-28 · recent

- ID：`cursor-2026-07-28-457de6`
- kind：`pricing`；主题：`pricing-model`
- 标题：Local pricing at ₹649 per month, tax inclusive, billed in INR with UPI or card
- 来源 Release：[Cursor Start](https://cursor.com/changelog/cursor-start)
- 卡片文件：`Changes/Cursor/2026-07-28-local-pricing-at-649-per-month-tax-inclusive-billed-in-inr-with-upi-or-card.md`

**证据（1 条）：**

> Local pricing at ₹649 per month, tax inclusive, billed in INR with UPI or card.

判定：

### S60 · cursor · 2026-09-23 · recent

- ID：`cursor-2026-09-23-12694d`
- kind：`launch`；主题：`apps-integrations`
- 标题：Integrations
- 来源 Release：[Rollouts and Security Review](https://cursor.com/changelog/rollouts-and-security-reviewer)
- 卡片文件：`Changes/Cursor/2026-09-23-integrations.md`

**证据（1 条）：**

> Rollouts connects to Origin or GitHub for source control, to your continuous delivery system for deploy events, and to Datadog and other telemetry providers for signals. Feature flag integration is coming soon.

判定：

## 二、B+ 高信号独立卡（15 张随机样本）

### B01 · claude-code · 2026-05-19

- ID：`claude-code-2026-05-19-215520`
- kind：`change`；主题：`agent-mode`
- 标题：Added `/resume` support for background sessions
- 来源 Release：[v2.1.144](https://github.com/anthropics/claude-code/releases/tag/v2.1.144)
- 卡片文件：`Changes/Claude Code/2026-05-19-added-resume-support-for-background-sessions-sessions-started-via-claude-bg-or-a.md`

**证据（1 条）：**

> Added `/resume` support for background sessions — sessions started via `claude --bg` or agent view now appear alongside interactive ones, marked with `bg`

判定：

### B02 · claude-code · 2026-02-03

- ID：`claude-code-2026-02-03-ea4a44`
- kind：`change`；主题：`developer-workflow`
- 标题：Added `/debug` for Claude to help troubleshoot the current session
- 来源 Release：[v2.1.30](https://github.com/anthropics/claude-code/releases/tag/v2.1.30)
- 卡片文件：`Changes/Claude Code/2026-02-03-added-debug-for-claude-to-help-troubleshoot-the-current-session.md`

**证据（1 条）：**

> Added `/debug` for Claude to help troubleshoot the current session

判定：

### B03 · claude-code · 2026-07-01

- ID：`claude-code-2026-07-01-67b585`
- kind：`launch`；主题：`apps-integrations`
- 标题：Claude in Chrome is now generally available
- 来源 Release：[v2.1.198](https://github.com/anthropics/claude-code/releases/tag/v2.1.198)
- 卡片文件：`Changes/Claude Code/2026-07-01-claude-in-chrome-is-now-generally-available.md`

**证据（1 条）：**

> Claude in Chrome is now generally available

判定：

### B04 · claude-code · 2026-04-16

- ID：`claude-code-2026-04-16-90cd9d`
- kind：`expansion`；主题：`model-support`
- 标题：Auto mode is now available for Max subscribers when using Opus 4.7
- 来源 Release：[v2.1.111](https://github.com/anthropics/claude-code/releases/tag/v2.1.111)
- 卡片文件：`Changes/Claude Code/2026-04-16-auto-mode-is-now-available-for-max-subscribers-when-using-opus-4-7.md`

**证据（1 条）：**

> Auto mode is now available for Max subscribers when using Opus 4.7

判定：

### B05 · claude-code · 2026-10-05

- ID：`claude-code-2026-10-05-5bff1d`
- kind：`change`；主题：`agent-mode`
- 标题：Added `/claude-api managed-agents-onboard <quickstart-name>` to build a Console…
- 来源 Release：[v2.1.290](https://github.com/anthropics/claude-code/releases/tag/v2.1.290)
- 卡片文件：`Changes/Claude Code/2026-10-05-added-claude-api-managed-agents-onboard-quickstart-name-to-build-a-console-quick.md`

**证据（1 条）：**

> Added `/claude-api managed-agents-onboard <quickstart-name>` to build a Console quickstart template, such as `deep-researcher`, with the `ant` CLI

判定：

### B06 · claude-code · 2026-03-14

- ID：`claude-code-2026-03-14-1eba17`
- kind：`change`；主题：`model-support`
- 标题：Added `/effort` slash command to set model effort level
- 来源 Release：[v2.1.76](https://github.com/anthropics/claude-code/releases/tag/v2.1.76)
- 卡片文件：`Changes/Claude Code/2026-03-14-added-effort-slash-command-to-set-model-effort-level.md`

**证据（1 条）：**

> Added `/effort` slash command to set model effort level

判定：

### B07 · claude-code · 2026-08-13

- ID：`claude-code-2026-08-13-bbdff3`
- kind：`change`；主题：`agent-mode`
- 标题：Subagent forking is now on by default
- 来源 Release：[v2.1.232](https://github.com/anthropics/claude-code/releases/tag/v2.1.232)
- 卡片文件：`Changes/Claude Code/2026-08-13-subagent-forking-is-now-on-by-default-a-subagent-type-fork-subagent-inherits-the.md`

**证据（1 条）：**

> Subagent forking is now on by default: a `subagent_type: "fork"` subagent inherits the full conversation and prompt cache, and non-teammate agent spawns in interactive sessions now run in the background by default

判定：

### B08 · claude-code · 2026-08-26

- ID：`claude-code-2026-08-26-10b266`
- kind：`change`；主题：`model-support`
- 标题：Added `/claude-api cost-optimize` to profile an existing project's Claude API spend…
- 来源 Release：[v2.1.247](https://github.com/anthropics/claude-code/releases/tag/v2.1.247)
- 卡片文件：`Changes/Claude Code/2026-08-26-added-claude-api-cost-optimize-to-profile-an-existing-project-s-claude-api-spend.md`

**证据（1 条）：**

> Added `/claude-api cost-optimize` to profile an existing project's Claude API spend and work through cost levers (caching, token hygiene, batch, effort, model choice) one measured change at a time

判定：

### B09 · claude-code · 2026-10-14

- ID：`claude-code-2026-10-14-ac0dab`
- kind：`change`；主题：`context-window`
- 标题：Added `/usage` warnings for max effort, workflows, always-on context and large tool…
- 来源 Release：[v2.1.299](https://github.com/anthropics/claude-code/releases/tag/v2.1.299)
- 卡片文件：`Changes/Claude Code/2026-10-14-added-usage-warnings-for-max-effort-workflows-always-on-context-and-large-tool-r.md`

**证据（1 条）：**

> Added `/usage` warnings for max effort, workflows, always-on context and large tool results

判定：

### B10 · claude-code · 2026-10-14

- ID：`claude-code-2026-10-14-8f0fcb`
- kind：`change`；主题：`interface-experience`
- 标题：Added `/effort` and `/fast` in agent view to set what new sessions start with
- 来源 Release：[v2.1.299](https://github.com/anthropics/claude-code/releases/tag/v2.1.299)
- 卡片文件：`Changes/Claude Code/2026-10-14-added-effort-and-fast-in-agent-view-to-set-what-new-sessions-start-with-a-bare-m.md`

**证据（1 条）：**

> Added `/effort` and `/fast` in agent view to set what new sessions start with; a bare `/model`, `/effort` or `/fast` there now opens a picker

判定：

### B11 · claude-code · 2026-09-03

- ID：`claude-code-2026-09-03-e75dba`
- kind：`change`；主题：`apps-integrations`
- 标题：Added `/reload-plugins` to headless sessions, so it appears in the Claude Code…
- 来源 Release：[v2.1.260](https://github.com/anthropics/claude-code/releases/tag/v2.1.260)
- 卡片文件：`Changes/Claude Code/2026-09-03-added-reload-plugins-to-headless-sessions-so-it-appears-in-the-claude-code-deskt.md`

**证据（1 条）：**

> Added `/reload-plugins` to headless sessions, so it appears in the Claude Code Desktop and SDK command lists

判定：

### B12 · claude-code · 2026-10-05

- ID：`claude-code-2026-10-05-19cf28`
- kind：`change`；主题：`agent-mode`
- 标题：Added `/claude-api managed-agents-onboard <url>` to set up the Managed Agents…
- 来源 Release：[v2.1.290](https://github.com/anthropics/claude-code/releases/tag/v2.1.290)
- 卡片文件：`Changes/Claude Code/2026-10-05-added-claude-api-managed-agents-onboard-url-to-set-up-the-managed-agents-pattern.md`

**证据（1 条）：**

> Added `/claude-api managed-agents-onboard <url>` to set up the Managed Agents pattern a page describes as `ant apply` files

判定：

### B13 · claude-code · 2026-06-04

- ID：`claude-code-2026-06-04-ddcc08`
- kind：`change`；主题：`apps-integrations`
- 标题：Added `/plugin list` command to list installed plugins…
- 来源 Release：[v2.1.163](https://github.com/anthropics/claude-code/releases/tag/v2.1.163)
- 卡片文件：`Changes/Claude Code/2026-06-04-added-plugin-list-command-to-list-installed-plugins-with-enabled-disabled-filter.md`

**证据（1 条）：**

> Added `/plugin list` command to list installed plugins, with `--enabled`/`--disabled` filters

判定：

### B14 · claude-code · 2026-09-11

- ID：`claude-code-2026-09-11-5bf521`
- kind：`change`；主题：`apps-integrations`
- 标题：Added `/output-style [name]` to list and switch output styles, including over Remote…
- 来源 Release：[v2.1.269](https://github.com/anthropics/claude-code/releases/tag/v2.1.269)
- 卡片文件：`Changes/Claude Code/2026-09-11-added-output-style-name-to-list-and-switch-output-styles-including-over-remote-c.md`

**证据（1 条）：**

> Added `/output-style [name]` to list and switch output styles, including over Remote Control and in cloud and other headless sessions

判定：

### B15 · cursor · 2026-01-08

- ID：`cursor-2026-01-08-9a16db`
- kind：`change`；主题：`apps-integrations`
- 标题：Added /mcp enable, /mcp disable commands to manage MCP servers
- 来源 Release：[New CLI Features and Improved CLI Performance](https://cursor.com/changelog/cli-jan-08-2026)
- 卡片文件：`Changes/Cursor/2026-01-08-added-mcp-enable-mcp-disable-commands-to-manage-mcp-servers.md`

**证据（1 条）：**

> Added /mcp enable, /mcp disable commands to manage MCP servers.

判定：

## 三、证据最多的 10 张摘要卡

### D01 · claude-code · 2026-10-05 · 19 条

- ID：`claude-code-2026-10-05-1d1a15`
- kind：`digest`；主题：`safety-privacy`
- 标题：19 Safety and Privacy changes in v2.1.290
- 来源 Release：[v2.1.290](https://github.com/anthropics/claude-code/releases/tag/v2.1.290)
- 卡片文件：`Changes/Claude Code/2026-10-05-19-safety-and-privacy-changes-in-v2-1-290.md`

**证据（19 条）：**

> Added `agentId` to the `tool.check` event of plugin hooks, so a hook can tell a subagent's permission check from the main session's

> Added a /status and doctor warning when managed settings ignore user-configured sandbox allowRead paths or allowed domains

> Fixed `claude agents` sessions in manual permission mode asking for approval to read an image pasted into a reply or a new agent's prompt

> Fixed auto mode denials suggesting a permission rule that would skip the classifier for a whole tool or that Claude Code would ignore

> Fixed `--channels` permission relay: a reply ID that repeats within a session is now ignored instead of approving a different prompt

> Fixed Bash permission checks auto-approving some read-only commands (such as `rg` or `git grep`) whose arguments the shell would still expand as wildcards; these now prompt for approval

> Fixed Bash permission checks auto-approving certain commands whose variable names zsh reads differently from bash; these now prompt for approval

> Fixed sandboxed Monitor tool commands skipping the permission prompt under sandbox auto-allow; they now follow your permission rules

> Fixed a freeze when the secret scan or a permission prompt met long token-like text

> Fixed Bash permission checks not applying Read deny rules or the outside-directory read block to a wildcard in some option values of read-only commands

> Fixed some permission rules and safety checks not being applied to a tool call after a PreToolUse hook rewrote its input

> Fixed file names containing line breaks being displayed incorrectly in file tool errors and permission prompts

> Fixed edits to the file a symlinked settings file points at running without the settings-file permission question

> Improved permission prompts from background agents to show the Ctrl+X Ctrl+K shortcut that stops all background agents

> Changed the Bash tool to ask for permission before running `pyright`, which is no longer treated as a read-only command

> Changed Bash permission checks so that more forms of the `ps` command ask for approval instead of running without asking

> Changed the `claude-api` skill's Managed Agents examples to turn off the web tools unless the agent needs them and to use the `auto` permission policy

> [VSCode] Fixed a permission prompt that arrived behind an open dialog taking keyboard focus, so a key pressed in the dialog could answer it

> [Claude Tag] Fixed members with the Claude Tag Admin permission getting "Couldn't load memory files" on the Activity page's Memory tab; they can now read workspace and channel memory

判定：

### D02 · claude-code · 2026-10-14 · 19 条

- ID：`claude-code-2026-10-14-23bbb3`
- kind：`digest`；主题：`apps-integrations`
- 标题：19 Apps and Integrations changes in v2.1.299
- 来源 Release：[v2.1.299](https://github.com/anthropics/claude-code/releases/tag/v2.1.299)
- 卡片文件：`Changes/Claude Code/2026-10-14-19-apps-and-integrations-changes-in-v2-1-299.md`

**证据（19 条）：**

> Added `--shutdown-drain-sec` to `claude self-hosted-runner orchestrator`: on SIGTERM it stops polling and gives the poll in flight and running spawn hooks up to that many seconds to finish

> Added the skill's frontmatter, source, plugin name and file path to what a mod's `skill.prompt` hook receives

> Added `--disallow-tools` and a `disallowed_tools` case field to `claude plugin eval` to keep specific built-in tools, such as Agent, out of eval runs

> Added a field to the attribution block in Claude Code sessions behind a Claude apps gateway; remove the block with `CLAUDE_CODE_ATTRIBUTION_HEADER=0`

> Added a note in `/plugin` and `claude plugin validate` naming a mod's hooks that are skipped where an organization manages Claude Code

> Improved the plugin-authoring skill's steps for sharing a mod: Claude asks public or private and checks the files before creating a GitHub repository

> Changed plugin hooks and workflow scripts to refuse values they hand back that nest deeper than 28,000 levels, with an error naming the limit (workflow scripts allowed 100,000)

> Changed actions a plugin hook can block to be refused, not let through, when the hook cannot be handed them or cannot hand back its answer; a tool that already ran has its result withheld

> Changed requests to claude.ai's connector proxy and to Anthropic-hosted MCP servers to no longer follow HTTP redirects; redirects by a connector's own server are unaffected

> Changed MCP requests in cloud and self-hosted runner sessions to no longer follow HTTP redirects from the session's MCP proxy

> Changed `ui.render` trees in `claude plugin test`: each mod's Box or Text root now carries `part: { plugin }` naming the mod, so exact-tree assertions must include it

> Changed `claude plugin test` to fail a call to a mod's served `$` method that has not answered within ten seconds, as a session does

> Changed MCP allow rules to reach only the server they name: `mcp__a` no longer allows a server named `a__b` or `a_`; write `mcp__<server>__*` with the server's whole normalized name

> Changed agent `tools:` lists to take only the named MCP server's tools; list a server whose name contains `__` as `mcp__<whole name>__*`

> Changed cloud session and Remote Control MCP connectors to negotiate MCP protocol version 2026-07-28 by default on installs that fetch no flags; `MCP_PROTOCOL_NEGOTIATION=legacy` opts out

> Changed MCP tool descriptions and server instructions from Anthropic's first-party MCP servers at `api.anthropic.com` to reach Claude in full instead of being cut at 4,096 characters

> Changed `UserPromptSubmit` hooks to run before a skill or custom slash command expands, so a hook that blocks the prompt now also stops its embedded shell commands

> [Claude Tag] Changed how Claude in Slack corrects a message it got wrong: it edits the message in place and adds a short "Edited" note instead of striking through the old text

> [Claude Tag] Changed Claude in Slack to join channels with more than 100 members quietly, with no intro message

判定：

### D03 · claude-code · 2026-09-23 · 18 条

- ID：`claude-code-2026-09-23-b6b1f4`
- kind：`digest`；主题：`apps-integrations`
- 标题：18 Apps and Integrations changes in v2.1.281
- 来源 Release：[v2.1.281](https://github.com/anthropics/claude-code/releases/tag/v2.1.281)
- 卡片文件：`Changes/Claude Code/2026-09-23-18-apps-and-integrations-changes-in-v2-1-281.md`

**证据（18 条）：**

> Added `assume_role` on Claude apps gateway Bedrock upstreams: the gateway calls Bedrock as an IAM role it assumes through STS, in another AWS account if needed, optionally one session per developer

> Added `guardrail: {id, version}` on Claude apps gateway Bedrock upstreams to apply an Amazon Bedrock guardrail to every request sent through them (set it on all Bedrock upstreams or none)

> Added MCP URL-mode elicitation on 2026-07-28 protocol connections, so servers can ask Claude Code to open a browser-based flow; no waiting dialog is left on screen when the server has no way to confirm completion

> Added MCP server checks to `claude plugin validate`: it reports `.mcp.json` entries that would be silently dropped at load, undeclared `${user_config.*}` references, and insecure URLs

> Added a scrollbar to the `/skills`, `/mcp` and `/plugin` Installed lists in fullscreen mode, like the one `/workflows` now has: it appears while the mouse is over the list and can be clicked or dragged

> Improved the time to resume very long sessions that have been compacted, most noticeably through the Agent SDK and Claude Desktop

> Improved plugin hook-failure errors to name the offending plugin, and added a `claude plugin validate` warning when a shell-form hook leaves `${CLAUDE_PLUGIN_ROOT}` unquoted (it breaks on plugin paths with spaces)

> Improved the `/` menu, `/skills`, `/context` and the `/plugin` Installed list to show skills synced from claude.ai by their short name when no other command uses it, not `anthropic-skills:<name>`

> Improved `/install-github-app`, `/desktop`, the `/permissions` auto mode environment prompts, and the `/plugin` "Add marketplace?" and "Run this command?" prompts: they now use the standard dialog frame with key hints, and Ctrl+C or Ctrl+D cancels them on the second press like other dialogs

> Improved the `/workflows` and `/mcp` lists: they page (PgUp/PgDn, Home/End) and take j/k and the mouse like other lists, their arrows follow `select:previous`/`select:next` rebinds, and `x` in `/workflows` stops the run the pointer is on

> Improved the `/plugin` plugin and marketplace details menus and the `/remote-control` already-connected menu: they now support Home/End and clicking a row

> Improved the /plugin Installed list: rows now line up in columns (status, name, type, details) across every section

> Improved `/hooks`: a hook's detail screen now says what kind of hook it is and where to change it, instead of always pointing at settings.json, and the hooks-disabled, safe mode and managed-hooks-only notices each say what is happening in one plain sentence

> Changed /mcp: each server's row now starts with its status icon and name, says its state once, and in a narrow terminal drops trailing facts like "managed" before shortening the name

> Changed Remote Control attachment downloads to reuse connections and to skip files already downloaded in the session

> Changed MCP resource lists (the resource list tool and @-mention suggestions) to skip MCP Apps UI resources; reading one by URI still works

> Changed `claude plugin uninstall --json` and the /plugin dialog to say a plugin's data was kept when its folder stays because another installed plugin uses it or install records cannot be read

> [Claude Tag] Added a short line in the Slack thread after someone presses Stop, naming who stopped Claude's response and saying to mention @Claude to continue

判定：

### D04 · claude-code · 2026-09-25 · 14 条

- ID：`claude-code-2026-09-25-1e0680`
- kind：`digest`；主题：`apps-integrations`
- 标题：14 Apps and Integrations changes in v2.1.283
- 来源 Release：[v2.1.283](https://github.com/anthropics/claude-code/releases/tag/v2.1.283)
- 卡片文件：`Changes/Claude Code/2026-09-25-14-apps-and-integrations-changes-in-v2-1-283.md`

**证据（14 条）：**

> Added MCP tool, WebFetch and WebSearch outputs to the `tool.output` OpenTelemetry span event when `OTEL_LOG_TOOL_CONTENT=1`

> Added `path` to `--plugin-dir` load-failure entries in the stream-json `system/init` `plugin_errors`, naming the directory that did not load

> Added an opt-in `load_test_mode` block to the Claude apps gateway config: requests are built and signed but not sent upstream, and clients get a canned reply, so a deployment can be load tested

> Added a `mantle` upstream provider to the Claude apps gateway for Amazon Bedrock's Mantle endpoint

> Improved the `/mcp` tool list: it shows more tools at once, scrolls with the page keys and mouse, and marks tools your organization blocked with a warning icon

> Improved MCP tool results: images returned by MCP tools are now also saved to a file, so Bash, Read and other tools can open them

> Improved the browser page shown after signing in to an MCP server: centered layout, dark mode, and new artwork

> Improved the Skill tool's reply when a skill belongs to a plugin that failed to load, so Claude tells you the plugin could not be loaded instead of calling the skill uninstalled

> Improved recovery from an `installed_plugins.json` that cannot be read at all: its contents are kept in a file beside it before it is rebuilt, and `claude plugin list` names that file

> Changed `Skill(anthropic-skills:<name>)` deny rules to also block that skill when Claude Desktop delivers it as a plugin, and `Skill(skill:<name>)` denies to match the skill's alias and display name

> Changed `claude plugin eval` to require git 2.31 or later when git is installed; a run on an older git is refused with a message naming the version

> Self-hosted runner: Changed lifecycle hooks' git to skip a repository's Git LFS `pre-push` hook, ignore a writable system `core.hooksPath`, and not sign commits without `--configure-git`

> [Claude Tag] Added a "Channels Claude can search" admin setting that limits Claude's Slack search to public channels it has been added to, set per organization, workspace or channel

> [Claude Tag] Added a Back to Slack button on the page shown after connecting your Claude account, returning you to the thread you started from

判定：

### D05 · claude-code · 2026-09-29 · 14 条

- ID：`claude-code-2026-09-29-6b1e05`
- kind：`digest`；主题：`apps-integrations`
- 标题：14 Apps and Integrations changes in v2.1.285
- 来源 Release：[v2.1.285](https://github.com/anthropics/claude-code/releases/tag/v2.1.285)
- 卡片文件：`Changes/Claude Code/2026-09-29-14-apps-and-integrations-changes-in-v2-1-285.md`

**证据（14 条）：**

> Added `claude plugin configure <plugin>` to show a plugin's options and which are unset, or save new values read from stdin with `--values-stdin`

> Added `<server>.<key>=<value>` to `claude plugin install --config`, so a bundled `.mcpb` MCP server's own settings can be set at install time and it starts without visiting `/plugin` → Configure

> Improved plugin marketplace errors to name why a git address is refused instead of citing enterprise policy

> Improved validation of git URLs for plugins, marketplaces and the current repository's remote

> Improved pictures Claude sends as BMP, HEIC, HEIF, AVIF or TIFF files: the Claude apps now show a preview where Claude Code can convert them

> Improved SDK liveness during a non-streaming fallback request: with partial messages on, a `ping` stream event is now sent every 30 seconds on the Anthropic API, Claude Platform on AWS and gateways

> Changed MCP tools so a tool that sets its own `_meta['anthropic/alwaysLoad']` to false stays deferred when its `--mcp-config`, Agent SDK or plugin server is set to `alwaysLoad`

> Changed the MCP server name `widgets` to be reserved in cloud sessions and on self-hosted runners: your own server under it, or a close spelling such as `widgets_`, no longer loads, so rename it

> Changed `claude mcp get` to hide the command, arguments, and environment values of stdio MCP servers provided by plugins; variable names are still shown

> Changed `/claude-api` so it can no longer be run from Remote Control clients

> [VSCode] Added a plugin options form to Manage plugins: installing a plugin that has options asks for the unset ones, and a gear on its row changes them later

> [VSCode] Improved the Manage plugins dialog: a failed plugin action now opens a popup that explains it and, where there is one, offers the fix

> [VSCode] Changed the Manage plugins dialog to ask before removing a marketplace or turning off a plugin that your project's shared `.claude/settings.json` turns on

> [Cloud sessions] Changed `MCP_DISCOVERY_CACHE=1`, when set in your cloud environment's variables rather than a settings file, to reuse your connectors' tool lists after a session restart; other MCP servers are no longer cached and connect at startup

判定：

### D06 · claude-code · 2026-10-05 · 14 条

- ID：`claude-code-2026-10-05-d0014b`
- kind：`digest`；主题：`apps-integrations`
- 标题：14 Apps and Integrations changes in v2.1.290
- 来源 Release：[v2.1.290](https://github.com/anthropics/claude-code/releases/tag/v2.1.290)
- 卡片文件：`Changes/Claude Code/2026-10-05-14-apps-and-integrations-changes-in-v2-1-290.md`

**证据（14 条）：**

> Added `ThemeKey` and `Color` types to the plugin hooks typings, so an editor lists the theme colors a mod's drawing can name

> Added to `claude plugin validate`: each hook a mod registers at a gating site is listed with whether it has a `.catch` (`gatingHooks` under `--json`)

> Improved MCP startup behind a network proxy: a server the proxy blocks (HTTP 403) is no longer retried three times

> Improved the built-in `plugin-authoring` skill: Claude now gives the one command another person runs to install a mod you made, and writes it in a README's install section

> Improved the reply to `/plugin` in the desktop app's Code tab: it now says where to install and manage plugins there

> Improved the Claude apps gateway's log when an upstream's cloud credentials or connection fail: the warning now ends with the underlying cause

> Improved the Claude apps gateway to log a warning during the last 30 days before the certificate it presents to the identity provider expires

> Changed what a mod's `$.process.spawn` rejects with when another mod denies it after the child ran: it now says the call ran and a plugin withheld its result

> Changed plugin hooks so long text is clipped and logged instead of being refused or dropped silently

> Changed the Claude apps gateway's minimum supported PostgreSQL version from 14 to 11

> Changed `claude plugin update` on a plugin loaded from a directory to print just its reason, without the "Failed to update plugin" prefix, as for built-in plugins

> [VSCode] Added a way to review and run a plugin marketplace's install or update command from the Manage plugins dialog

> [VSCode] Improved Continue After Reload: tabs reopened after VS Code restarts its extensions now also finish a step the restart interrupted

> [Claude Tag] Improved the earlier Claude in Slack app's reply when it can't start a session: it now says what failed and who can fix it, in full only once per thread

判定：

### D07 · claude-code · 2026-10-08 · 14 条

- ID：`claude-code-2026-10-08-70f161`
- kind：`digest`；主题：`apps-integrations`
- 标题：14 Apps and Integrations changes in v2.1.295
- 来源 Release：[v2.1.295](https://github.com/anthropics/claude-code/releases/tag/v2.1.295)
- 卡片文件：`Changes/Claude Code/2026-10-08-14-apps-and-integrations-changes-in-v2-1-295.md`

**证据（14 条）：**

> Added `onFailure: "block"` for command and HTTP hooks: a hook that can't start, times out, or exits with an unexpected code blocks the action instead of letting it through

> Added a warning to `claude plugin install`, `enable`, `disable` and `marketplace add` when the settings file they write to does not load

> Added support for `timeouts.upstream_ttfb_ms` on the Claude apps gateway's Bedrock, Vertex, Foundry and other cloud upstreams: a value you set now limits how long a stream may take to start there, after which it fails over or gets a 502

> Added advice to `claude plugin validate` when a plugin's README has no install line: it prints the line to paste and never changes the exit code, even with `--strict`

> Added `upstream_request_id` to the Claude apps gateway's `inference` audit event: the request ID from Amazon Bedrock, the Anthropic API or another upstream, for support cases

> Added a `request-id` header to the Claude apps gateway's successful inference responses, so `request_id` in Claude Code telemetry matches the gateway's audit log

> Improved the Claude apps gateway to log a warning every 30 seconds while its PostgreSQL database is read-only, saying what fails and how to recover

> Improved the built-in `plugin-authoring` skill: it no longer tells a session with no terminal to run terminal commands, and explains sharing a mod only when asked

> Improved `claude plugin validate` and plugin loading: when a hooks module is refused over a rebound top-level `var`, the error now names the line that rebinds it, the cause, and a fix

> Changed MCP tool descriptions the model loads through tool search to be cut at 16,384 characters instead of 2,048

> Changed claude.ai connectors to negotiate MCP protocol version 2026-07-28 by default on installs that fetch no flags; `MCP_PROTOCOL_NEGOTIATION=legacy` opts out

> Changed what Claude and you read when a mod denies a tool call after the tool ran: it now says the tool ran and a plugin withheld its result

> Changed WebSocket (`ws`) MCP servers: a message over 16 MiB is no longer parsed and closes the connection, the limit the other transports already have

> [Claude Tag] Changed the settings confirmation cards Claude posts in a Slack channel to stay open for 30 minutes instead of 10

判定：

### D08 · claude-code · 2026-09-23 · 12 条

- ID：`claude-code-2026-09-23-e456b4`
- kind：`digest`；主题：`safety-privacy`
- 标题：12 Safety and Privacy changes in v2.1.281
- 来源 Release：[v2.1.281](https://github.com/anthropics/claude-code/releases/tag/v2.1.281)
- 卡片文件：`Changes/Claude Code/2026-09-23-12-safety-and-privacy-changes-in-v2-1-281.md`

**证据（12 条）：**

> Added an auto mode recommendation to `/insights` that estimates how many permission prompts auto mode could have handled in your recent sessions

> Fixed a session resumed after a restart during a pending permission prompt sending a different history than before, which broke the prompt cache from that point

> Fixed permission dialogs and attachment checks reading a path under macOS's `/.vol`, `/.nofollow` or `/.resolve` (which can reach a network mount) before approval

> Fixed a permission rule containing a NUL byte being expanded into a wildcard match; such a rule now matches nothing

> Fixed `claude --bg` starting a background session, and running its project hooks, in a directory that had not passed the workspace trust prompt; it now asks for trust first, or exits when not run interactively

> Fixed remote sessions staying on "needs approval" with a stale prompt after a permission prompt and a sandbox network-access prompt overlapped and both were answered

> Fixed pressing Shift+Tab twice quickly landing on the wrong permission mode

> Windows: Fixed Bash commands that write to `$TMPDIR/…` failing with "Permission denied"

> Improved auto mode after resuming a session in a new process: the permission classifier can now reuse its earlier prompt cache instead of rewriting it

> Improved sandbox guidance on macOS: when a local dev server can't bind a port, Claude now points to `sandbox.network.allowLocalBinding`

> Improved `/help` and `/sandbox`: ←/→ and Tab switch tabs from inside a tab's list, and ↓ on an empty Custom commands tab in `/help` no longer leaves the keys stuck until Esc

> [Claude Code on the web] Improved the file card shown when a cloud session can't open a file: it now says whether the file no longer exists or the session's permission settings block reading it

判定：

### D09 · claude-code · 2026-09-30 · 11 条

- ID：`claude-code-2026-09-30-67fd04`
- kind：`digest`；主题：`apps-integrations`
- 标题：11 Apps and Integrations changes in v2.1.286
- 来源 Release：[v2.1.286](https://github.com/anthropics/claude-code/releases/tag/v2.1.286)
- 卡片文件：`Changes/Claude Code/2026-09-30-11-apps-and-integrations-changes-in-v2-1-286.md`

**证据（11 条）：**

> Improved slash command suggestion responsiveness while typing when many skills or plugin commands are installed; command descriptions now match by word prefix

> Improved `/hooks`: the closing line of a hook's detail screen now says "this hook" instead of "it"

> Improved responsiveness of SDK and `-p` sessions when a host re-sends an MCP server enable for a server that is already connected

> Improved the protocol page a Claude apps gateway serves at `/protocol`: it now says not to reject unknown input and matches what Claude Code sends today

> Changed `--bare` to connect only the MCP servers named on the command line, send the model no system reminders, and start no background tasks; under `--bare`, a shell command that reaches its timeout now stops instead of moving to the background

> Changed plugin installs to refuse npm sources that are git repositories or folders, and to install plugin dependencies only from registry packages

> Changed list screens (`/artifacts`, `/mcp`, `/skills`, `/hooks` and others) to always line up each row's details in one column after the names

> Changed `/hooks` to open on one list of your configured hooks grouped by event, so viewing a hook takes one Enter instead of three

> [VSCode] Improved the Manage plugins dialog: it says when a turned-off plugin is still on because of other settings, and explains a plugin folder clash

> [Claude Tag] Added an Add channel button to Claude Tag's spend limits page in admin settings, so a limit can be set on any channel, including a private one, from its channel ID or Slack link

> [Claude Tag] Improved the titles of sessions started from Slack as shown on claude.ai: they now read as the words you typed, without Slack user IDs or escape codes

判定：

### D10 · claude-code · 2026-10-01 · 11 条

- ID：`claude-code-2026-10-01-62a9e3`
- kind：`digest`；主题：`apps-integrations`
- 标题：11 Apps and Integrations changes in v2.1.287
- 来源 Release：[v2.1.287](https://github.com/anthropics/claude-code/releases/tag/v2.1.287)
- 卡片文件：`Changes/Claude Code/2026-10-01-11-apps-and-integrations-changes-in-v2-1-287.md`

**证据（11 条）：**

> Added Claude Mods: plugins may now modify deeper behavior

> Added You should know, a built-in mod where a side agent watches your back and flags things you or Claude might miss. Turn it on with `/plugin enable cc-plugin-you-should-know@builtin` (for first-party sessions with telemetry on)

> Improved plugin marketplace errors to say in plain words why a marketplace was ignored or refused, and what to do

> Improved plugin listings to note when a plugin's dependencies were not installed, and updating a plugin now retries an install that did not finish

> Improved delivery of files Claude sends from cloud sessions and Remote Control: an upload that fails on a timeout, a network error or a 502, 503 or 504 is now retried once

> Improved MCP startup in headless mode: a remote server whose first connect fails transiently is now retried without waiting for the slowest server to finish connecting

> Improved the explanation Claude gives when the server refuses a file it sends from a Remote Control or cloud session, such as an oversized image

> Changed whole-tool `Bash` allow rules and allowing hooks to prompt for, not run, shell writes to files Claude Code's file tools refuse outright (the Anthropic profile store, the host credentials file)

> Changed MCP server `alwaysLoad: false` to defer all of that server's tools behind tool search

> [VSCode] Improved the Manage plugins dialog: a failed marketplace add, remove or refresh now says what went wrong

> [Claude Tag] Improved Claude's task list in long Slack threads: background work no longer reposts it as a new message on its own, so people following the thread aren't notified

判定：
