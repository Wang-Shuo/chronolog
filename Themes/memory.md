---
created: '2023-07-20'
date: '2026-10-23'
description: 'Research question: what do the tracked products remember between sessions,
  and how do users control it?'
machine_hash: c95c192817ecf92394de7089aa9c66db3204de5307162ecd36d3889a83abbefb
modified: '2026-10-23'
products_involved:
- ChatGPT
- Claude Code
- Cursor
publication: active
status: official
tags:
- theme
- moc
theme: memory
title: Memory and Personalization
---

<!-- chronolog:begin region="header" -->
# Memory and Personalization

79 tracked changes across ChatGPT, Claude Code and Cursor · 2023-07-20 → 2026-10-23 · Claude Code averages 7.0 cards per release, Cursor 4.0, ChatGPT 1.7
<!-- chronolog:end -->

## Research summary
<!-- chronolog:begin region="narrative" -->
**Research question: what do the tracked products remember between sessions, and how do users control it?**

ChatGPT's [2023-07-20 custom instructions beta](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#custom-instructions-are-rolling-out-in-beta) ([[Releases/ChatGPT/chatgpt-2023-07-20-custom-instructions-are-rolling-out-in-beta-bf9360b9|archived]]) lets users set preferences once to steer future conversations. The [2024-02-13 memory test](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#memory-and-new-controls-for-chatgpt) ([[Releases/ChatGPT/chatgpt-2024-02-13-memory-and-new-controls-for-chatgpt-2fd43ded|archived]]) remembers things discussed across all chats; users can tell ChatGPT what to remember or forget, ask what it remembers, or turn memory off. The [2025-05-08 note](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#enhanced-memory-in-chatgpt-including-eu-on-pluspro) ([[Releases/ChatGPT/chatgpt-2025-05-08-enhanced-memory-in-chatgpt-including-eu-on-plus-pro-b6107d35|archived]]) rolls out enhanced memory, enabled through the Reference Chat History setting and off by default, to all Plus and Pro users including the EU; the [2025-08-22 note](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#project-only-memory) ([[Releases/ChatGPT/chatgpt-2025-08-22-project-only-memory-3424a221|archived]]) adds project-only memory, which keeps a project's context inside that project; and the [2025-10-15 note](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#chatgpt-can-now-automatically-manage-saved-memories-so-its-even-better-at-remembering-whats-important-to-you) ([[Releases/ChatGPT/chatgpt-2025-10-15-chatgpt-can-now-automatically-manage-saved-memories-so-it-s-even-00bd082a|archived]]) has ChatGPT manage saved memories automatically by keeping the most relevant details prioritized.

Cursor's [1.0 release on 2025-06-04](https://cursor.com/changelog/1-0) ([[Releases/Cursor/cursor-2025-06-04-1-0-https-cursor-com-changelog-1-0-237767ca|archived]]) introduces Memories as a beta: Cursor remembers facts from conversations, stored per project for each individual. The [2025-07-03 release](https://cursor.com/changelog/1-2) ([[Releases/Cursor/cursor-2025-07-03-1-2-https-cursor-com-changelog-1-2-27872f5d|archived]]) makes Memories generally available with user approval for background-generated memories, and the [2026-03-05 Automations release](https://cursor.com/changelog/03-05-26) ([[Releases/Cursor/cursor-2026-03-05-automations-https-cursor-com-changelog-03-05-26-be367422|archived]]) gives automation agents a memory tool that learns from past runs.

Claude Code's [v2.1.32 on 2026-02-05](https://github.com/anthropics/claude-code/releases/tag/v2.1.32) ([[Releases/Claude Code/claude-code-2026-02-05-v2-1-32-github-283457817-0910feb0|archived]]) has Claude record and recall memories automatically as it works, [v2.1.33 on 2026-02-06](https://github.com/anthropics/claude-code/releases/tag/v2.1.33) ([[Releases/Claude Code/claude-code-2026-02-06-v2-1-33-github-283581096-0f5b01a0|archived]]) adds a `memory` frontmatter field that gives agents persistent memory at user, project or local scope, and [v2.1.59 on 2026-02-26](https://github.com/anthropics/claude-code/releases/tag/v2.1.59) ([[Releases/Claude Code/claude-code-2026-02-26-v2-1-59-github-290659389-9e2d6217|archived]]) saves useful context to auto-memory, managed with `/memory`.

**Uncertainty and scope:** the record covers the three tracked products only, Claude Code coverage starts on 2025-12-19 and ChatGPT memory rollouts vary by plan and region; the theme also collects personalization settings and unrelated uses of “memory” such as RAM use, and the announcements do not measure what a product retains or how reliably it recalls it.
<!-- chronolog:end -->

## Key moments
<!-- chronolog:begin region="moments" -->
Auto-selected; edit `key_moments` in editorial.yaml to curate.

| Quarter | ChatGPT | Claude Code | Cursor |
| --- | --- | --- | --- |
| 2026 Q3 | 2026-08-14 [[Changes/ChatGPT/2026-08-14-you-can-now-change-a-project-s-memory-setting-after-you-create-it-open-the-proje-b36ffe\|Edit memory settings for existing projects]] | · | · |
| 2026 Q2 | 2026-06-12 [[Changes/ChatGPT/2026-06-12-you-can-now-delete-the-memories-shown-on-your-memory-summary-page-and-turn-memor-f16782\|Additional controls for memory summary]] | · | 2026-06-18 [[Changes/Cursor/2026-06-18-you-can-now-delete-memory-files-in-the-ui-or-prompt-your-automation-to-delete-ou\|Delete memory files in the UI, or prompt your automation to delete outdated memories…]] |
| 2025 Q4 | 2025-10-29 [[Changes/ChatGPT/2025-10-29-chatgpt-pulse-is-now-available-on-web-and-rolling-out-to-atlas-for-pro-users-wit\|ChatGPT Pulse on Web]] | · | · |
| 2025 Q3 | 2025-09-25 [[Changes/ChatGPT/2025-09-25-we-re-launching-an-early-preview-of-chatgpt-pulse-for-pro-users-on-ios-and-andro-cf8064\|Introducing ChatGPT Pulse for Pro users]]<br>2025-08-22 [[Changes/ChatGPT/2025-08-22-an-improvement-to-projects-is-now-available-when-creating-a-project-users-have-t-87f79a\|An improvement to projects is now available]] | · | 2025-07-03 [[Changes/Cursor/2025-07-03-memories-is-now-ga-since-1-0-we-ve-improved-memory-generation-quality-added-in-e\|Memories (now GA)]] |
| 2025 Q2 | 2025-06-03 [[Changes/ChatGPT/2025-06-03-opt-in-reminders-e08369\|Opt‑in reminders]] | · | 2025-06-04 [[Changes/Cursor/2025-06-04-memories\|Memories]] |
| 2024 Q2 | 2024-04-29 [[Changes/ChatGPT/2024-04-29-memory-is-now-available-to-all-chatgpt-plus-users-except-in-europe-korea-where-w-4db29a\|Memory is now available to Plus users]] | · | · |
| 2023 Q3 | 2023-08-21 [[Changes/ChatGPT/2023-08-21-custom-instructions-are-now-available-to-users-in-the-european-union-united-king-cfc1d5\|Custom instructions are now available to users in the EU & UK]]<br>2023-08-09 [[Changes/ChatGPT/2023-08-09-custom-instructions-are-now-available-to-chatgpt-users-on-the-free-plan-except-f-963d1e\|Custom instructions are now available to free users]] | · | · |
<!-- chronolog:end -->

<!-- chronolog:begin region="scope" -->
> [!info]- How to read this timeline
> Scope: tracked-products-only. Entries show same-theme chronology; they do not establish equivalent capabilities, adoption, or causation.
<!-- chronolog:end -->

## Timeline
<!-- chronolog:begin region="timeline" -->
### 2026 · 45 entries (ChatGPT 15 · Claude Code 27 · Cursor 3)

#### 2026-10

- 2026-10-23 · **Claude Code** · [[Changes/Claude Code/2026-10-23-improved-memory-use-of-non-interactive-sessions-p-agent-sdk-during-compaction-wh|Improved memory use of non-interactive sessions (-p, Agent SDK) during compaction…]]
- 2026-10-19 · **Claude Code** · [[Changes/Claude Code/2026-10-19-improved-memory-use-when-sending-requests-in-long-or-resumed-conversations|Improved memory use when sending requests in long or resumed conversations]]
- 2026-10-14 · **Claude Code** · [[Changes/Claude Code/2026-10-14-improved-memory-and-disk-use-when-pdfs-are-mentioned-their-bytes-are-no-longer-k|Improved memory and disk use when PDFs are @-mentioned]]
- 2026-10-05 · **Claude Code** · [[Changes/Claude Code/2026-10-05-changed-background-sessions-waiting-on-a-scheduled-wakeup-loop-they-are-now-left|Changed background sessions waiting on a scheduled wakeup (/loop)]]
- 2026-10-01 · **ChatGPT** · [[Changes/ChatGPT/2026-10-01-virtually-try-on-clothing-and-accessories-a-try-on-button-will-appear-on-product|Virtually try on clothing and accessories]]
- 2026-10-01 · **Claude Code** · [[Changes/Claude Code/2026-10-01-2-memory-and-personalization-changes-in-v2-1-287|2 Memory and Personalization changes in v2.1.287]] · Digest

#### 2026-09

- 2026-09-29 · **ChatGPT** · [[Changes/ChatGPT/2026-09-29-pages-follow-space-s-availability-and-sharing-settings-sharing-a-page-does-not-g|Pages follow Space’s availability and sharing settings]]
- 2026-09-29 · **ChatGPT** · [[Changes/ChatGPT/2026-09-29-you-can-use-your-chatgpt-account-to-sign-in-to-participating-products-without-cr|Sign in to other products with ChatGPT]]
- 2026-09-29 · **Claude Code** · [[Changes/Claude Code/2026-09-29-changed-memory-so-that-auto-memory-can-no-longer-be-turned-on-from-a-background|Changed /memory so that Auto-memory can no longer be turned on from a background…]]
- 2026-09-28 · **Claude Code** · [[Changes/Claude Code/2026-09-28-2-memory-and-personalization-changes-in-v2-1-284|2 Memory and Personalization changes in v2.1.284]] · Digest
- 2026-09-25 · **Claude Code** · [[Changes/Claude Code/2026-09-25-improved-lists-in-help-hooks-copy-chrome-memory-ide-release-notes-rewind-diff-re|Improved lists in /help, /hooks, /copy, /chrome, /memory, /ide…]]
- 2026-09-17 · **Claude Code** · [[Changes/Claude Code/2026-09-17-vscode-added-viewing-editing-and-deleting-a-saved-memory-inside-the-memory-dialo|VSCode Added viewing, editing and deleting a saved memory inside the Memory dialog]]
- 2026-09-17 · **Claude Code** · [[Changes/Claude Code/2026-09-17-vscode-added-memory-and-instructions-entries-to-the-customize-menu-memory-shows|VSCode Added Memory and Instructions entries to the Customize menu]]
- 2026-09-10 · **Claude Code** · [[Changes/Claude Code/2026-09-10-2-memory-and-personalization-changes-in-v2-1-268|2 Memory and Personalization changes in v2.1.268]] · Digest

#### 2026-08

- 2026-08-27 · **ChatGPT** · [[Changes/ChatGPT/2026-08-27-3-memory-and-personalization-changes-in-more-controls-in-temporary-chat|3 Memory and Personalization changes in More controls in temporary chat]] · Digest
- 2026-08-27 · **ChatGPT** · [[Changes/ChatGPT/2026-08-27-we-re-rolling-out-new-controls-in-temporary-chat-you-can-now-choose-to-personali|ChatGPT rolls out new controls in temporary chat]]
- 2026-08-20 · **Claude Code** · [[Changes/Claude Code/2026-08-20-updated-the-bundled-claude-api-skill-for-the-managed-agents-aug-19-release-web-s|Updated the bundled claude-api skill for the Managed Agents Aug 19 release]]
- 2026-08-18 · **Claude Code** · [[Changes/Claude Code/2026-08-18-improved-the-embedded-grep-in-native-macos-linux-builds-pathological-patterns-no|Improved the embedded grep in native macOS/Linux builds]]
- 2026-08-14 · **ChatGPT** · [[Changes/ChatGPT/2026-08-14-we-ve-made-it-easier-to-study-with-interactive-quizzes-manage-project-memory-and|ChatGPT makes it easier to study with interactive quizzes, manage project memory…]]
- 2026-08-14 · **ChatGPT** · [[Changes/ChatGPT/2026-08-14-you-can-now-change-a-project-s-memory-setting-after-you-create-it-open-the-proje-b36ffe|Edit memory settings for existing projects]]
- 2026-08-14 · **Claude Code** · [[Changes/Claude Code/2026-08-14-added-opt-in-memory-cgroup-support-for-bash-tool-commands-on-linux-claude-code-t|Added opt-in memory cgroup support for Bash tool commands on Linux…]]
- 2026-08-13 · **Claude Code** · [[Changes/Claude Code/2026-08-13-cowork-sessions-no-longer-inline-external-imports-from-user-scope-memory-files|Cowork sessions no longer inline external @-imports from user-scope memory files]]

#### 2026-07

- 2026-07-18 · **Claude Code** · [[Changes/Claude Code/2026-07-18-added-an-iso-modified-timestamp-to-memory-file-frontmatter|Added an ISO modified timestamp to memory file frontmatter]]
- 2026-07-15 · **Claude Code** · [[Changes/Claude Code/2026-07-15-improved-the-memory-index-over-limit-warning-to-measure-only-loaded-content-excl|Improved the memory index over-limit warning to measure only loaded content…]]
- 2026-07-14 · **Claude Code** · [[Changes/Claude Code/2026-07-14-memory-writes-that-leave-a-memory-md-index-over-its-read-limit-now-produce-an-ex|Memory writes that leave a MEMORY.md index over its read limit now produce…]]

#### 2026-06

- 2026-06-24 · **Claude Code** · [[Changes/Claude Code/2026-06-24-reduced-long-session-memory-growth-from-terminal-output-cache|Reduced long-session memory growth from terminal output cache]]
- 2026-06-22 · **Claude Code** · [[Changes/Claude Code/2026-06-22-improved-memory-the-agent-is-now-reminded-to-compact-its-memory-md-index-when-ne|Improved memory: the agent is now reminded to compact its MEMORY.md index…]]
- 2026-06-18 · **Cursor** · [[Changes/Cursor/2026-06-18-you-can-now-delete-memory-files-in-the-ui-or-prompt-your-automation-to-delete-ou|Delete memory files in the UI, or prompt your automation to delete outdated memories…]]
- 2026-06-17 · **Claude Code** · [[Changes/Claude Code/2026-06-17-changed-the-improved-n-memories-line-to-no-longer-list-individual-files-outside|Changed the Improved N memories line to no longer list individual files outside…]]
- 2026-06-12 · **ChatGPT** · [[Changes/ChatGPT/2026-06-12-you-can-now-delete-the-memories-shown-on-your-memory-summary-page-and-turn-memor-f16782|Additional controls for memory summary]]
- 2026-06-04 · **ChatGPT** · [[Changes/ChatGPT/2026-06-04-we-ve-upgraded-memory-so-chatgpt-can-better-keep-your-context-up-to-date-helping-9a48f3|Memory that stays more up to date]]
- 2026-06-04 · **Cursor** · [[Changes/Cursor/2026-06-04-run-correlation-every-send-now-carries-a-platform-generated-requestid-exposed-on|Run correlation: Every send() now carries a platform-generated requestId, exposed…]]

#### 2026-05

- 2026-05-05 · **ChatGPT** · [[Changes/ChatGPT/2026-05-05-starting-today-we-re-rolling-out-memory-improvements-to-chatgpt-plus-and-pro-use|Memory sources and more personalized responses in ChatGPT]]

#### 2026-04

- 2026-04-22 · **ChatGPT** · [[Changes/ChatGPT/2026-04-22-sometimes-you-just-want-the-right-answer-as-quickly-as-possible-we-re-rolling-ou|Fast answers in ChatGPT]]
- 2026-04-02 · **Cursor** · [[Changes/Cursor/2026-04-02-large-file-diff-rendering-is-now-much-faster-smoother-and-less-memory-heavy|Large-file diff rendering is now much faster, smoother, and less memory-heavy]]

#### 2026-03

- 2026-03-27 · **Claude Code** · [[Changes/Claude Code/2026-03-27-memory-filenames-in-the-saved-n-memories-notice-now-highlight-on-hover-and-open|Memory filenames in the "Saved N memories" notice now highlight on hover and open on click]]
- 2026-03-17 · **ChatGPT** · [[Changes/ChatGPT/2026-03-17-we-re-sunsetting-the-preset-nerdy-base-style-to-simplify-options-and-improve-res|Sunsetting the “Nerdy” base style]] · Policy
- 2026-03-12 · **Claude Code** · [[Changes/Claude Code/2026-03-12-2-memory-and-personalization-changes-in-v2-1-74|2 Memory and Personalization changes in v2.1.74]] · Digest

#### 2026-02

- 2026-02-28 · **Claude Code** · [[Changes/Claude Code/2026-02-28-project-configs-auto-memory-now-shared-across-git-worktrees-of-the-same-reposito|Project configs & auto memory now shared across git worktrees of the same repository]]
- 2026-02-26 · **Claude Code** · [[Changes/Claude Code/2026-02-26-claude-automatically-saves-useful-context-to-auto-memory-manage-with-memory|Claude automatically saves useful context to auto-memory]]
- 2026-02-09 · **ChatGPT** · [[Changes/ChatGPT/2026-02-09-we-re-beginning-to-roll-out-a-test-for-ads-in-chatgpt-in-the-u-s-for-logged-in-a|Testing ads in ChatGPT (Free, Go)]]
- 2026-02-06 · **Claude Code** · [[Changes/Claude Code/2026-02-06-added-memory-frontmatter-field-support-for-agents-enabling-persistent-memory-wit|Added memory frontmatter field support for agents, enabling persistent memory…]]
- 2026-02-05 · **Claude Code** · [[Changes/Claude Code/2026-02-05-claude-now-automatically-records-and-recalls-memories-as-it-works|Claude now automatically records and recalls memories as it works]]

#### 2026-01

- 2026-01-15 · **ChatGPT** · [[Changes/ChatGPT/2026-01-15-when-reference-chat-history-is-enabled-chatgpt-can-now-more-reliably-find-specif|Improved memory for finding details from past chats (Plus & Pro)]]
- 2026-01-07 · **ChatGPT** · [[Changes/ChatGPT/2026-01-07-we-re-starting-to-roll-out-health-a-dedicated-space-in-chatgpt-for-health-and-we|We’re starting to roll out Health, a dedicated space in ChatGPT for health…]]

### 2025 · 27 entries (ChatGPT 22 · Cursor 5)

#### 2025-12

- 2025-12-22 · **ChatGPT** · [[Changes/ChatGPT/2025-12-22-today-we-re-rolling-out-your-year-with-chatgpt-an-optional-personalized-end-of-y-740eb1|Your Year with ChatGPT]]
- 2025-12-19 · **ChatGPT** · [[Changes/ChatGPT/2025-12-19-in-addition-to-selecting-a-base-style-and-tone-preset-like-candid-and-friendly-y-21da79|New detailed characteristic controls]]

#### 2025-11

- 2025-11-24 · **ChatGPT** · [[Changes/ChatGPT/2025-11-24-shopping-research-is-a-new-interactive-experience-that-helps-you-find-the-right-0a021d|Shopping research in ChatGPT]]
- 2025-11-07 · **ChatGPT** · [[Changes/ChatGPT/2025-11-07-previously-changes-you-made-to-your-chatgpt-personality-or-custom-instructions-o|Personality and custom instructions now apply to all chats]]

#### 2025-10

- 2025-10-30 · **ChatGPT** · [[Changes/ChatGPT/2025-10-30-longer-memory-for-more-personalized-responses|Longer memory for more personalized responses]]
- 2025-10-29 · **ChatGPT** · [[Changes/ChatGPT/2025-10-29-chatgpt-pulse-is-now-available-on-web-and-rolling-out-to-atlas-for-pro-users-wit|ChatGPT Pulse on Web]]
- 2025-10-29 · **Cursor** · [[Changes/Cursor/2025-10-29-increased-default-memory-for-typescript-language-server|Increased default memory for TypeScript language server]]
- 2025-10-28 · **ChatGPT** · [[Changes/ChatGPT/2025-10-28-longer-memory-for-more-personalized-responses|Longer memory for more personalized responses]]
- 2025-10-15 · **ChatGPT** · [[Changes/ChatGPT/2025-10-15-chatgpt-now-manages-saved-memories-automatically-by-keeping-the-most-relevant-de-997f64|ChatGPT can now automatically manage saved memories so it’s even better…]]
- 2025-10-14 · **ChatGPT** · [[Changes/ChatGPT/2025-10-14-longer-memory-for-more-personalized-responses-775c35|Longer memory for more personalized responses]]
- 2025-10-08 · **ChatGPT** · [[Changes/ChatGPT/2025-10-08-longer-memory-for-more-personalized-responses-8c6877|Longer memory for more personalized responses]]

#### 2025-09

- 2025-09-29 · **ChatGPT** · [[Changes/ChatGPT/2025-09-29-turn-off-memory-so-chatgpt-won-t-save-and-use-memories-when-responding|Turn off memory, so ChatGPT won’t save and use memories when responding]]
- 2025-09-25 · **ChatGPT** · [[Changes/ChatGPT/2025-09-25-we-re-launching-an-early-preview-of-chatgpt-pulse-for-pro-users-on-ios-and-andro-cf8064|Introducing ChatGPT Pulse for Pro users]] · Launch
- 2025-09-22 · **ChatGPT** · [[Changes/ChatGPT/2025-09-22-longer-memory-for-more-personalized-responses|Longer memory for more personalized responses]]
- 2025-09-15 · **ChatGPT** · [[Changes/ChatGPT/2025-09-15-personalization-no-longer-opens-in-a-separate-modal-you-can-manage-personalizati|Personalization settings are now in Settings]]

#### 2025-08

- 2025-08-22 · **ChatGPT** · [[Changes/ChatGPT/2025-08-22-an-improvement-to-projects-is-now-available-when-creating-a-project-users-have-t-87f79a|An improvement to projects is now available]] · Launch
- 2025-08-18 · **ChatGPT** · [[Changes/ChatGPT/2025-08-18-longer-memory-for-more-personalized-responses-4644fd|Longer memory for more personalized responses]]

#### 2025-07

- 2025-07-29 · **ChatGPT** · [[Changes/ChatGPT/2025-07-29-personalize-responses-based-on-your-past-chats-if-memory-is-on-using-examples-an|Personalize responses based on your past chats if memory is on, using examples…]]
- 2025-07-03 · **Cursor** · [[Changes/Cursor/2025-07-03-memories-is-now-ga-since-1-0-we-ve-improved-memory-generation-quality-added-in-e|Memories (now GA)]] · Launch
- 2025-07-03 · **Cursor** · [[Changes/Cursor/2025-07-03-faster-tab|Faster Tab]]

#### 2025-06

- 2025-06-12 · **ChatGPT** · [[Changes/ChatGPT/2025-06-12-improvements-to-memory-to-reference-past-chats-in-a-project|Improvements to memory to reference past chats in a project]]
- 2025-06-04 · **Cursor** · [[Changes/Cursor/2025-06-04-memories|Memories]] · Launch
- 2025-06-03 · **ChatGPT** · [[Changes/ChatGPT/2025-06-03-opt-in-reminders-e08369|Opt‑in reminders]] · Launch

#### 2025-05

- 2025-05-08 · **ChatGPT** · [[Changes/ChatGPT/2025-05-08-saved-memories-and-chat-history-are-offered-only-to-plus-and-pro-accounts-free-t|Saved memories and Chat history are offered only to Plus and Pro…]]
- 2025-05-08 · **ChatGPT** · [[Changes/ChatGPT/2025-05-08-enhanced-memory-rolling-out-to-all-plus-and-pro-users-including-the-eu-the-new-m|Enhanced memory rolling out to all Plus and Pro users (including the EU)]]

#### 2025-04

- 2025-04-16 · **ChatGPT** · [[Changes/ChatGPT/2025-04-16-chatgpt-can-also-use-memories-to-inform-search-queries-when-chatgpt-searches-the|Memory with Search]]

#### 2025-02

- 2025-02-19 · **Cursor** · [[Changes/Cursor/2025-02-19-2-memory-and-personalization-changes-in-0-46-x|2 Memory and Personalization changes in 0.46.x]] · Digest

### 2024 · 2 entries (ChatGPT 2)

#### 2024-04

- 2024-04-29 · **ChatGPT** · [[Changes/ChatGPT/2024-04-29-memory-is-now-available-to-all-chatgpt-plus-users-except-in-europe-korea-where-w-4db29a|Memory is now available to Plus users]]

#### 2024-02

- 2024-02-13 · **ChatGPT** · [[Changes/ChatGPT/2024-02-13-we-re-testing-memory-with-chatgpt-remembering-things-you-discuss-across-all-chat-9872c8|Memory and new controls for ChatGPT]]

### 2023 · 5 entries (ChatGPT 3 · Cursor 2)

#### 2023-09

- 2023-09-08 · **Cursor** · [[Changes/Cursor/2023-09-08-better-state-management-prevents-crashes-from-editor-using-too-much-memory|Better state management - prevents crashes from editor using too much memory]]
- 2023-09-07 · **Cursor** · [[Changes/Cursor/2023-09-07-this-should-reduce-any-significant-memory-issues-that-users-have-been-experienci|This should reduce any significant memory issues that users have been experiencing]]

#### 2023-08

- 2023-08-21 · **ChatGPT** · [[Changes/ChatGPT/2023-08-21-custom-instructions-are-now-available-to-users-in-the-european-union-united-king-cfc1d5|Custom instructions are now available to users in the EU & UK]]
- 2023-08-09 · **ChatGPT** · [[Changes/ChatGPT/2023-08-09-custom-instructions-are-now-available-to-chatgpt-users-on-the-free-plan-except-f-963d1e|Custom instructions are now available to free users]]

#### 2023-07

- 2023-07-20 · **ChatGPT** · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->