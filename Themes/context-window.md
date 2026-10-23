---
created: '2023-05-04'
date: '2026-10-22'
description: 'Research question: how much material can each product bring into a conversation,
  and how does it handle the limit?'
machine_hash: 1d6b6ea5f813966b0d73f676b28f9ff3e7e965df567a49a0fa7d47a5b0b5cc83
modified: '2026-10-22'
products_involved:
- ChatGPT
- Claude Code
- Cursor
publication: active
status: official
tags:
- theme
- moc
theme: context-window
title: Context Window
---

<!-- chronolog:begin region="header" -->
# Context Window

133 tracked changes across ChatGPT, Claude Code and Cursor · 2023-05-04 → 2026-10-22 · Claude Code averages 7.0 cards per release, Cursor 4.0, ChatGPT 1.7
<!-- chronolog:end -->

## Research summary
<!-- chronolog:begin region="narrative" -->
**Research question: how much material can each product bring into a conversation, and how does it handle the limit?**

ChatGPT's [2026-02-13 update](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#chatgpt-updates-better-file-uploads-easier-copying-and-more-reliable-long-chats) ([[Releases/ChatGPT/chatgpt-2026-02-13-chatgpt-updates-better-file-uploads-easier-copying-and-more-reli-e2c69aa0|archived]]) raises attachments to 20 files per message (previously 10), and the [2026-02-20 note](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#expanded-context-window-for-thinking) ([[Releases/ChatGPT/chatgpt-2026-02-20-expanded-context-window-for-thinking-31f2c4c2|archived]]) sets a total context window of 256k tokens (128k input and 128k maximum output) when users manually select Thinking, up from 196k total tokens. The [2026-03-25 note](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#large-pastes-are-now-handled-as-attachments) ([[Releases/ChatGPT/chatgpt-2026-03-25-large-pastes-are-now-handled-as-attachments-6bacf64e|archived]]) converts pastes over 5k characters into attachments for Plus, Pro and Business users so that large pastes do not consume the whole context window, and the [2026-06-22 note](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#large-pastes-are-now-handled-as-attachments-for-more-plans) ([[Releases/ChatGPT/chatgpt-2026-06-22-large-pastes-are-now-handled-as-attachments-for-more-plans-64db97b0|archived]]) extends this to Free and Go users at a 10k-character threshold.

Cursor's [Codebase Context v1 on 2023-06-06](https://cursor.com/changelog/0-2-26) ([[Releases/Cursor/cursor-2023-06-06-0-2-26-https-cursor-com-changelog-0-2-26-1b7664cb|archived]]) brings context from the full codebase into chat responses, and the [2024-04-01 Long Context Chat beta](https://cursor.com/changelog/0-31-x) ([[Releases/Cursor/cursor-2024-04-01-0-31-x-https-cursor-com-changelog-0-31-x-f88ca4c9|archived]]) lets users talk with many files at once. The [2025-05-15 release](https://cursor.com/changelog/0-50) ([[Releases/Cursor/cursor-2025-05-15-0-50-https-cursor-com-changelog-0-50-dc290998|archived]]) lets @folders add an entire codebase to context, the [2025-07-29 release](https://cursor.com/changelog/1-3) ([[Releases/Cursor/cursor-2025-07-29-1-3-https-cursor-com-changelog-1-3-d153efc3|archived]]) shows how much of the context window a conversation uses, and the [2025-09-12 release](https://cursor.com/changelog/1-6) ([[Releases/Cursor/cursor-2025-09-12-1-6-https-cursor-com-changelog-1-6-f33fb3ea|archived]]) adds on-demand summarization alongside automatic summarization at the context-window limit. [Cursor Projects on 2026-09-10](https://cursor.com/changelog/projects) ([[Releases/Cursor/cursor-2026-09-10-cursor-projects-https-cursor-com-changelog-projects-105aab75|archived]]) keep a shared set of files that every agent in a project can read and extend.

Claude Code's [v2.1.7 on 2026-01-14](https://github.com/anthropics/claude-code/releases/tag/v2.1.7) ([[Releases/Claude Code/claude-code-2026-01-14-v2-1-7-github-276555327-bf21dc80|archived]]) defers MCP tool descriptions to a search tool by default once they exceed 10% of the context window, and [v2.1.51 on 2026-02-24](https://github.com/anthropics/claude-code/releases/tag/v2.1.51) ([[Releases/Claude Code/claude-code-2026-02-24-v2-1-51-github-289665343-b4bbdd9c|archived]]) persists tool results over 50K characters to disk to reduce context window usage. [v2.1.197 on 2026-06-30](https://github.com/anthropics/claude-code/releases/tag/v2.1.197) ([[Releases/Claude Code/claude-code-2026-06-30-v2-1-197-github-346856026-11e4aa1f|archived]]) makes Claude Sonnet 5, with a native 1M-token context window, the default model, and [v2.1.247 on 2026-08-26](https://github.com/anthropics/claude-code/releases/tag/v2.1.247) ([[Releases/Claude Code/claude-code-2026-08-26-v2-1-247-github-377320078-fc507178|archived]]) sets Sonnet 5's default auto-compact window to that full 1M context.

**Uncertainty and scope:** the record covers the three tracked products only and Claude Code coverage starts on 2025-12-19; token limits, file counts and summarization rules are each product's own measures under plan and model qualifications, so these figures do not compare capacity across products.
<!-- chronolog:end -->

## Key moments
<!-- chronolog:begin region="moments" -->
Auto-selected; edit `key_moments` in editorial.yaml to curate.

| Quarter | ChatGPT | Claude Code | Cursor |
| --- | --- | --- | --- |
| 2026 Q4 | · | 2026-10-14 [[Changes/Claude Code/2026-10-14-added-usage-warnings-for-max-effort-workflows-always-on-context-and-large-tool-r\|Added /usage warnings for max effort, workflows, always-on context and large tool…]] | · |
| 2026 Q3 | · | 2026-09-04 [[Changes/Claude Code/2026-09-04-added-skill-doctor-to-show-which-loaded-skills-go-unused-and-what-they-cost-in-c\|Added /skill-doctor to show which loaded skills go unused and what they cost…]] | 2026-09-10 [[Changes/Cursor/2026-09-10-you-shouldn-t-have-to-onboard-an-agent-every-time-you-start-a-task-each-project\|Shared context]]<br>2026-07-17 [[Changes/Cursor/2026-07-17-cross-channel-workflows\|Cross-channel workflows]]<br>2026-07-10 [[Changes/Cursor/2026-07-10-side-chats\|Side chats]] |
| 2026 Q2 | · | 2026-06-08 [[Changes/Claude Code/2026-06-08-added-cd-command-to-move-a-session-to-a-new-working-directory-without-breaking-t\|Added /cd command to move a session to a new working directory without breaking…]] | 2026-06-04 [[Changes/Cursor/2026-06-04-this-release-introduces-design-mode-for-faster-canvas-editing-new-ways-to-unders\|Cursor introduces Design Mode for faster canvas editing, new ways to understand…]]<br>2026-05-13 [[Changes/Cursor/2026-05-13-compact-chat-responses\|Compact chat responses]] |
| 2025 Q4 | · | · | 2025-12-18 [[Changes/Cursor/2025-12-18-conversation-insights-2efafc\|Conversation insights]] |
| 2025 Q3 | · | · | 2025-09-12 [[Changes/Cursor/2025-09-12-cursor-automatically-summarizes-long-conversation-for-you-when-reaching-the-cont\|Summarization triggers]]<br>2025-07-29 [[Changes/Cursor/2025-07-29-at-the-end-of-a-conversation-you-can-now-see-how-much-of-the-context-window-is-u\|View context usage in Chat]] |
| 2025 Q2 | · | · | 2025-05-15 [[Changes/Cursor/2025-05-15-include-your-entire-codebase-in-context\|Include your entire codebase in context]] |
| 2023 Q4 | · | · | 2023-11-24 [[Changes/Cursor/2023-11-24-you-can-now-folder-in-the-chat-to-chat-with-a-folder-let-us-know-what-you-think\|@folder]] |
| 2023 Q3 | · | · | 2023-09-08 [[Changes/Cursor/2023-09-08-long-files-in-chat\|Long files in chat]] |
| 2023 Q2 | · | · | 2023-06-06 [[Changes/Cursor/2023-06-06-codebase-context-v1-bd6ee5\|Codebase Context v1]] |
<!-- chronolog:end -->

<!-- chronolog:begin region="scope" -->
> [!info]- How to read this timeline
> Scope: tracked-products-only. Entries show same-theme chronology; they do not establish equivalent capabilities, adoption, or causation.
<!-- chronolog:end -->

## Timeline
<!-- chronolog:begin region="timeline" -->
### 2026 · 91 entries (ChatGPT 8 · Claude Code 71 · Cursor 12)

#### 2026-10

- 2026-10-22 · **Claude Code** · [[Changes/Claude Code/2026-10-22-updated-the-claude-api-skill-service-account-keys-and-workload-identity-federati|Updated the /claude-api skill]]
- 2026-10-19 · **Claude Code** · [[Changes/Claude Code/2026-10-19-3-context-window-changes-in-v2-1-304|3 Context Window changes in v2.1.304]] · Digest
- 2026-10-16 · **Claude Code** · [[Changes/Claude Code/2026-10-16-2-context-window-changes-in-v2-1-302|2 Context Window changes in v2.1.302]] · Digest
- 2026-10-15 · **Claude Code** · [[Changes/Claude Code/2026-10-15-improved-switching-to-a-model-with-a-smaller-context-window-a-conversation-too-l|Improved switching to a model with a smaller context window]]
- 2026-10-14 · **Claude Code** · [[Changes/Claude Code/2026-10-14-added-cache-creation-5m-tokens-and-cache-creation-1h-tokens-to-the-opentelemetry|Added cache_creation_5m_tokens and cache_creation_1h_tokens to the OpenTelemetry…]]
- 2026-10-14 · **Claude Code** · [[Changes/Claude Code/2026-10-14-2-context-window-changes-in-v2-1-299|2 Context Window changes in v2.1.299]] · Digest
- 2026-10-14 · **Claude Code** · [[Changes/Claude Code/2026-10-14-added-usage-warnings-for-max-effort-workflows-always-on-context-and-large-tool-r|Added /usage warnings for max effort, workflows, always-on context and large tool…]]
- 2026-10-09 · **Claude Code** · [[Changes/Claude Code/2026-10-09-2-context-window-changes-in-v2-1-296|2 Context Window changes in v2.1.296]] · Digest
- 2026-10-08 · **Claude Code** · [[Changes/Claude Code/2026-10-08-improved-token-counts-behind-a-claude-apps-gateway-on-amazon-bedrock-which-conte|Improved token counts behind a Claude apps gateway on Amazon Bedrock…]]
- 2026-10-02 · **Claude Code** · [[Changes/Claude Code/2026-10-02-changed-autocompact-to-save-the-auto-compact-window-per-model-so-each-model-keep|Changed /autocompact to save the auto-compact window per model, so each model…]]
- 2026-10-01 · **Claude Code** · [[Changes/Claude Code/2026-10-01-changed-opus-4-7-and-fable-to-use-a-1m-context-window-by-default-on-bedrock-vert|Changed Opus 4.7+ and Fable to use a 1M context window by default on Bedrock…]]

#### 2026-09

- 2026-09-30 · **Claude Code** · [[Changes/Claude Code/2026-09-30-improved-the-model-fallback-notice-and-the-autocompact-thrashing-error-to-say-wh|Improved the model fallback notice and the autocompact-thrashing error to say…]]
- 2026-09-29 · **Claude Code** · [[Changes/Claude Code/2026-09-29-2-context-window-changes-in-v2-1-285|2 Context Window changes in v2.1.285]] · Digest
- 2026-09-25 · **Claude Code** · [[Changes/Claude Code/2026-09-25-2-context-window-changes-in-v2-1-283|2 Context Window changes in v2.1.283]] · Digest
- 2026-09-15 · **Claude Code** · [[Changes/Claude Code/2026-09-15-added-x-claude-code-request-class-x-claude-code-agent-type-x-claude-code-prev-to|Added x-claude-code-request-class, x-claude-code-agent-type…]]
- 2026-09-14 · **Claude Code** · [[Changes/Claude Code/2026-09-14-improved-the-spinner-status-during-long-thinking-it-now-reads-deep-in-thought-af|Improved the spinner status during long thinking]]
- 2026-09-10 · **Cursor** · [[Changes/Cursor/2026-09-10-you-shouldn-t-have-to-onboard-an-agent-every-time-you-start-a-task-each-project|Shared context]] · Launch
- 2026-09-10 · **Cursor** · [[Changes/Cursor/2026-09-10-today-we-re-launching-projects-in-cursor-projects-lets-you-take-on-larger-bodies-51d06c|Cursor launches Projects]] · Launch
- 2026-09-09 · **Claude Code** · [[Changes/Claude Code/2026-09-09-improved-prompt-cache-stability-subagents-and-sessions-started-with-system-promp|Improved prompt-cache stability]]
- 2026-09-04 · **Claude Code** · [[Changes/Claude Code/2026-09-04-changed-context-token-counting-to-use-a-local-estimate-when-the-token-counting-a|Changed /context token counting to use a local estimate when the token-counting…]]
- 2026-09-04 · **Claude Code** · [[Changes/Claude Code/2026-09-04-added-skill-doctor-to-show-which-loaded-skills-go-unused-and-what-they-cost-in-c|Added /skill-doctor to show which loaded skills go unused and what they cost…]]
- 2026-09-03 · **Claude Code** · [[Changes/Claude Code/2026-09-03-2-context-window-changes-in-v2-1-260|2 Context Window changes in v2.1.260]] · Digest

#### 2026-08

- 2026-08-28 · **Claude Code** · [[Changes/Claude Code/2026-08-28-improved-retry-when-the-model-s-tool-call-is-malformed-the-broken-output-is-now|Improved retry when the model's tool call is malformed]]
- 2026-08-27 · **Claude Code** · [[Changes/Claude Code/2026-08-27-improved-the-workflow-tool-s-prompt-footprint-its-description-is-now-about-1k-to|Improved the Workflow tool's prompt footprint]]
- 2026-08-26 · **Claude Code** · [[Changes/Claude Code/2026-08-26-changed-sonnet-5-s-default-auto-compact-window-to-its-full-1m-context-so-session|Changed Sonnet 5's default auto-compact window to its full 1M context, so sessions…]]
- 2026-08-21 · **Claude Code** · [[Changes/Claude Code/2026-08-21-improved-the-reminder-shown-after-compaction-so-a-skill-s-original-arguments-are|Improved the reminder shown after compaction so a skill's original arguments are not…]]
- 2026-08-18 · **Claude Code** · [[Changes/Claude Code/2026-08-18-improved-the-context-limit-error-to-say-when-auto-compact-is-off-and-point-to-co|Improved the context-limit error to say when auto-compact is off and point…]]
- 2026-08-17 · **Claude Code** · [[Changes/Claude Code/2026-08-17-2-context-window-changes-in-v2-1-234|2 Context Window changes in v2.1.234]] · Digest
- 2026-08-14 · **Claude Code** · [[Changes/Claude Code/2026-08-14-improved-apps-gateway-error-forwarding-400-413-errors-from-vertex-foundry-and-cl|Improved apps gateway error forwarding]]
- 2026-08-12 · **Claude Code** · [[Changes/Claude Code/2026-08-12-improved-prompt-is-too-long-errors-to-explain-why-automatic-compaction-could-not|Improved "prompt is too long" errors to explain why automatic compaction could not…]]
- 2026-08-11 · **Claude Code** · [[Changes/Claude Code/2026-08-11-improved-compaction-progress-the-retry-countdown-and-stall-hint-now-appear-durin|Improved compaction progress]]
- 2026-08-06 · **Claude Code** · [[Changes/Claude Code/2026-08-06-2-context-window-changes-in-v2-1-223|2 Context Window changes in v2.1.223]] · Digest
- 2026-08-04 · **ChatGPT** · [[Changes/ChatGPT/2026-08-04-if-you-paste-more-than-10k-characters-into-the-composer-chatgpt-will-automatical-1bd022|If you paste more than 10k characters into the composer, ChatGPT will automatically…]]
- 2026-08-04 · **Claude Code** · [[Changes/Claude Code/2026-08-04-improved-stats-panel-to-count-cache-tokens-in-its-token-totals-with-a-breakdown|Improved Stats panel to count cache tokens in its token totals, with a breakdown…]]

#### 2026-07

- 2026-07-22 · **Claude Code** · [[Changes/Claude Code/2026-07-22-changed-skills-with-context-fork-to-run-in-the-background-by-default-opt-out-per|Changed skills with context: fork to run in the background by default]]
- 2026-07-20 · **Claude Code** · [[Changes/Claude Code/2026-07-20-context-now-shows-an-explicit-warning-when-the-conversation-exceeds-the-context|/context now shows an explicit warning when the conversation exceeds the context…]]
- 2026-07-17 · **Cursor** · [[Changes/Cursor/2026-07-17-cross-channel-workflows|Cross-channel workflows]] · Launch
- 2026-07-10 · **Cursor** · [[Changes/Cursor/2026-07-10-side-chats|Side chats]] · Launch
- 2026-07-08 · **Claude Code** · [[Changes/Claude Code/2026-07-08-improved-auto-mode-to-ask-before-running-rm-rf-on-a-variable-it-can-t-resolve-fr|Improved auto mode to ask before running rm -rf on a variable it can't resolve…]]
- 2026-07-01 · **Claude Code** · [[Changes/Claude Code/2026-07-01-subagents-and-context-compaction-now-inherit-the-session-s-extended-thinking-con|Subagents and context compaction now inherit the session's extended thinking…]]

#### 2026-06

- 2026-06-22 · **ChatGPT** · [[Changes/ChatGPT/2026-06-22-starting-today-for-chatgpt-free-and-go-users-long-pastes-are-handled-differently|Large pastes are now handled as attachments for more plans]]
- 2026-06-22 · **Claude Code** · [[Changes/Claude Code/2026-06-22-bash-commands-now-trigger-claude-to-respond-to-the-output-automatically-set-resp|! bash commands now trigger Claude to respond to the output automatically]]
- 2026-06-12 · **Claude Code** · [[Changes/Claude Code/2026-06-12-vscode-added-usage-attribution-to-the-account-usage-dialog-usage-showing-cache-m|VSCode Added usage attribution to the Account & usage dialog (/usage) showing…]]
- 2026-06-08 · **Claude Code** · [[Changes/Claude Code/2026-06-08-the-claude-md-is-too-long-warning-threshold-now-scales-with-the-model-s-context|The "CLAUDE.md is too long" warning threshold now scales with the model's context window]]
- 2026-06-08 · **Claude Code** · [[Changes/Claude Code/2026-06-08-added-cd-command-to-move-a-session-to-a-new-working-directory-without-breaking-t|Added /cd command to move a session to a new working directory without breaking…]]
- 2026-06-04 · **Cursor** · [[Changes/Cursor/2026-06-04-this-release-introduces-design-mode-for-faster-canvas-editing-new-ways-to-unders|Cursor introduces Design Mode for faster canvas editing, new ways to understand…]] · Launch
- 2026-06-04 · **Cursor** · [[Changes/Cursor/2026-06-04-context-usage-report-in-canvas-d08e2a|Context usage report in canvas]] · Launch

#### 2026-05

- 2026-05-28 · **Claude Code** · [[Changes/Claude Code/2026-05-28-claude-now-reserves-the-multiple-choice-question-prompt-for-decisions-it-genuine|Claude now reserves the multiple-choice question prompt for decisions it genuinely…]]
- 2026-05-27 · **Claude Code** · [[Changes/Claude Code/2026-05-27-added-pluginsuggestionmarketplaces-managed-setting-admins-can-allowlist-org-mark|Added pluginSuggestionMarketplaces managed setting]]
- 2026-05-22 · **Claude Code** · [[Changes/Claude Code/2026-05-22-improved-feedback-reports-to-include-the-conversation-that-happened-before-conte|Improved /feedback reports to include the conversation that happened before…]]
- 2026-05-19 · **Claude Code** · [[Changes/Claude Code/2026-05-19-improved-the-read-tool-to-return-a-truncated-first-page-with-a-partial-view-noti|Improved the Read tool to return a truncated first page with a "PARTIAL view" notice…]]
- 2026-05-19 · **Claude Code** · [[Changes/Claude Code/2026-05-19-the-post-survey-follow-up-hint-now-appears-after-every-non-dismiss-survey-respon|The post-survey follow-up hint now appears after every non-dismiss survey response…]]
- 2026-05-14 · **Claude Code** · [[Changes/Claude Code/2026-05-14-improved-reactive-compaction-the-first-summarize-attempt-now-seeds-from-the-orig|Improved reactive compaction]]
- 2026-05-13 · **Claude Code** · [[Changes/Claude Code/2026-05-13-rewind-menu-added-summarize-up-to-here-to-compress-earlier-context-while-keeping|Rewind menu: added "Summarize up to here" to compress earlier context while keeping…]]
- 2026-05-13 · **Cursor** · [[Changes/Cursor/2026-05-13-compact-chat-responses|Compact chat responses]] · Launch
- 2026-05-11 · **Claude Code** · [[Changes/Claude Code/2026-05-11-context-all-per-skill-token-estimates-now-account-for-the-model-s-tokenizer-and|/context all per-skill token estimates now account for the model's tokenizer…]]
- 2026-05-06 · **Cursor** · [[Changes/Cursor/2026-05-06-you-can-now-see-a-breakdown-of-your-agent-s-context-usage-e005b2|Context Usage Breakdown]]

#### 2026-04

- 2026-04-28 · **Claude Code** · [[Changes/Claude Code/2026-04-28-vscode-context-now-opens-a-native-token-usage-dialog|VSCode /context now opens a native token usage dialog]]
- 2026-04-15 · **Claude Code** · [[Changes/Claude Code/2026-04-15-added-option-to-show-claude-s-last-response-as-commented-context-in-the-ctrl-g-e|Added option to show Claude's last response as commented context in the Ctrl+G…]]
- 2026-04-14 · **Claude Code** · [[Changes/Claude Code/2026-04-14-2-context-window-changes-in-v2-1-108|2 Context Window changes in v2.1.108]] · Digest
- 2026-04-10 · **Claude Code** · [[Changes/Claude Code/2026-04-10-improved-tool-not-available-errors-to-explain-why-and-how-to-proceed-when-the-mo|Improved tool-not-available errors to explain why and how to proceed when the model…]]
- 2026-04-09 · **Claude Code** · [[Changes/Claude Code/2026-04-09-added-exclude-dynamic-system-prompt-sections-flag-to-print-mode-for-improved-cro|Added --exclude-dynamic-system-prompt-sections flag to print mode for improved…]]
- 2026-04-08 · **Claude Code** · [[Changes/Claude Code/2026-04-08-improved-context-low-warning-to-show-as-a-transient-footer-notification-instead|Improved context-low warning to show as a transient footer notification instead…]]
- 2026-04-04 · **Claude Code** · [[Changes/Claude Code/2026-04-04-pro-users-now-see-a-footer-hint-when-returning-to-a-session-after-the-prompt-cac|Pro users now see a footer hint when returning to a session after the prompt cache…]]
- 2026-04-02 · **Claude Code** · [[Changes/Claude Code/2026-04-02-2-context-window-changes-in-v2-1-91|2 Context Window changes in v2.1.91]] · Digest
- 2026-04-01 · **Claude Code** · [[Changes/Claude Code/2026-04-01-changed-hook-output-over-50k-characters-to-be-saved-to-disk-with-a-file-path-pre|Changed hook output over 50K characters to be saved to disk with a file path…]]

#### 2026-03

- 2026-03-27 · **Claude Code** · [[Changes/Claude Code/2026-03-27-3-context-window-changes-in-v2-1-86|3 Context Window changes in v2.1.86]] · Digest
- 2026-03-26 · **Claude Code** · [[Changes/Claude Code/2026-03-26-reduced-ui-stutter-when-compaction-triggers-on-large-sessions|Reduced UI stutter when compaction triggers on large sessions]]
- 2026-03-26 · **Claude Code** · [[Changes/Claude Code/2026-03-26-2-context-window-changes-in-v2-1-84|2 Context Window changes in v2.1.84]] · Digest
- 2026-03-25 · **ChatGPT** · [[Changes/ChatGPT/2026-03-25-starting-today-for-chatgpt-plus-pro-and-business-users-long-pastes-are-handled-d|Large pastes are now handled as attachments]]
- 2026-03-20 · **Claude Code** · [[Changes/Claude Code/2026-03-20-changed-plan-mode-to-hide-the-clear-context-option-by-default-restore-with-showc|Changed plan mode to hide the "clear context" option by default…]]
- 2026-03-14 · **Claude Code** · [[Changes/Claude Code/2026-03-14-added-postcompact-hook-that-fires-after-compaction-completes|Added PostCompact hook that fires after compaction completes]]
- 2026-03-11 · **Claude Code** · [[Changes/Claude Code/2026-03-11-improved-the-remote-control-spawn-mode-selection-prompt-with-better-context|Improved the Remote Control spawn mode selection prompt with better context]]
- 2026-03-05 · **ChatGPT** · [[Changes/ChatGPT/2026-03-05-gpt-5-4-brings-together-the-best-of-our-recent-advances-in-reasoning-coding-and|GPT-5.4 Thinking in ChatGPT]]
- 2026-03-05 · **Claude Code** · [[Changes/Claude Code/2026-03-05-3-context-window-changes-in-v2-1-69|3 Context Window changes in v2.1.69]] · Digest
- 2026-03-03 · **Cursor** · [[Changes/Cursor/2026-03-03-2-context-window-changes-in-2-6|2 Context Window changes in 2.6]] · Digest

#### 2026-02

- 2026-02-25 · **ChatGPT** · [[Changes/ChatGPT/2026-02-25-ad-hoc-text-sources-paste-notes-briefs-or-reference-material-directly-to-capture|Ad-hoc text sources]]
- 2026-02-25 · **ChatGPT** · [[Changes/ChatGPT/2026-02-25-projects-now-make-it-easy-to-build-a-living-knowledge-base-by-adding-sources-whe|Projects now make it easy to build a living knowledge base by adding sources…]]
- 2026-02-24 · **Claude Code** · [[Changes/Claude Code/2026-02-24-tool-results-larger-than-50k-characters-are-now-persisted-to-disk-previously-100|Tool results larger than 50K characters are now persisted to disk (previously 100K)]]
- 2026-02-20 · **ChatGPT** · [[Changes/ChatGPT/2026-02-20-chatgpt-now-has-a-total-context-window-length-of-256k-tokens-128k-input-and-128k|Expanded context window for Thinking]]
- 2026-02-20 · **Claude Code** · [[Changes/Claude Code/2026-02-20-2-context-window-changes-in-v2-1-50|2 Context Window changes in v2.1.50]] · Digest
- 2026-02-18 · **Cursor** · [[Changes/Cursor/2026-02-18-cli-now-stores-conversation-transcripts-that-the-agent-can-use-as-context|CLI now stores conversation transcripts that the agent can use as context]]
- 2026-02-17 · **Cursor** · [[Changes/Cursor/2026-02-17-agents-can-now-search-past-conversations-and-use-chat-history-as-context|Agents can now search past conversations and use chat history as context]]
- 2026-02-13 · **ChatGPT** · [[Changes/ChatGPT/2026-02-13-attach-up-to-20-files-in-a-single-message-you-can-now-upload-up-to-20-files-at-o|Attach up to 20 files in a single message]]
- 2026-02-13 · **Claude Code** · [[Changes/Claude Code/2026-02-13-improved-rename-to-auto-generate-session-name-from-conversation-context-when-cal|Improved /rename to auto-generate session name from conversation context…]]
- 2026-02-05 · **Claude Code** · [[Changes/Claude Code/2026-02-05-2-context-window-changes-in-v2-1-32|2 Context Window changes in v2.1.32]] · Digest
- 2026-02-03 · **Claude Code** · [[Changes/Claude Code/2026-02-03-added-pages-parameter-to-the-read-tool-for-pdfs-allowing-specific-page-ranges-to|Added pages parameter to the Read tool for PDFs, allowing specific page ranges…]]

#### 2026-01

- 2026-01-22 · **Cursor** · [[Changes/Cursor/2026-01-22-agents-can-now-read-pdfs-which-you-can-attach-in-chats-as-context|Agents can now read PDFs, which you can attach in chats as context]]
- 2026-01-16 · **Claude Code** · [[Changes/Claude Code/2026-01-16-added-auto-n-syntax-for-configuring-the-mcp-tool-search-auto-enable-threshold-wh|Added auto:N syntax for configuring the MCP tool search auto-enable threshold…]]
- 2026-01-14 · **Claude Code** · [[Changes/Claude Code/2026-01-14-enabled-mcp-tool-search-auto-mode-by-default-for-all-users-when-mcp-tool-descrip|Enabled MCP tool search auto mode by default for all users]]
- 2026-01-13 · **Claude Code** · [[Changes/Claude Code/2026-01-13-added-context-window-used-percentage-and-context-window-remaining-percentage-fie|Added context_window.used_percentage and context_window.remaining_percentage…]]

### 2025 · 17 entries (Claude Code 1 · Cursor 16)

#### 2025-12

- 2025-12-19 · **Claude Code** · [[Changes/Claude Code/2025-12-19-improved-context-command-visualization-with-grouped-skills-and-agents-by-source|Improved /context command visualization with grouped skills and agents by source…]]
- 2025-12-18 · **Cursor** · [[Changes/Cursor/2025-12-18-conversation-insights-2efafc|Conversation insights]] · Launch

#### 2025-11

- 2025-11-21 · **Cursor** · [[Changes/Cursor/2025-11-21-rules-in-home-folder-cursor-rules-will-be-included-in-context|Rules in home folder (~/.cursor/rules) will be included in context]]

#### 2025-10

- 2025-10-29 · **Cursor** · [[Changes/Cursor/2025-10-29-improved-prompt-ui|Improved Prompt UI]]

#### 2025-09

- 2025-09-12 · **Cursor** · [[Changes/Cursor/2025-09-12-cursor-automatically-summarizes-long-conversation-for-you-when-reaching-the-cont|Summarization triggers]] · Launch

#### 2025-08

- 2025-08-21 · **Cursor** · [[Changes/Cursor/2025-08-21-context-usage-is-always-shown-in-the-chat-input|Context usage is always shown in the chat input]]
- 2025-08-06 · **Cursor** · [[Changes/Cursor/2025-08-06-admin-api-for-blocklists-block-specific-files-or-directories-from-being-indexed|Admin API for blocklists]]

#### 2025-07

- 2025-07-29 · **Cursor** · [[Changes/Cursor/2025-07-29-at-the-end-of-a-conversation-you-can-now-see-how-much-of-the-context-window-is-u|View context usage in Chat]] · Launch
- 2025-07-03 · **Cursor** · [[Changes/Cursor/2025-07-03-pr-indexing-search|PR indexing & search]] · Launch

#### 2025-05

- 2025-05-15 · **Cursor** · [[Changes/Cursor/2025-05-15-include-your-entire-codebase-in-context|Include your entire codebase in context]] · Launch

#### 2025-04

- 2025-04-15 · **Cursor** · [[Changes/Cursor/2025-04-15-automated-and-improved-rules-15afc6|Automated and improved rules]] · Launch
- 2025-04-15 · **Cursor** · [[Changes/Cursor/2025-04-15-project-structure-in-context-beta|Project structure in context (Beta)]] · Launch

#### 2025-03

- 2025-03-23 · **Cursor** · [[Changes/Cursor/2025-03-23-added-input-token-count-for-chat-messages-click-the-three-dots-to-view-we-re-con|Added input token count for chat messages (click the three dots to view)]]

#### 2025-02

- 2025-02-19 · **Cursor** · [[Changes/Cursor/2025-02-19-ui-refresh-phase-one-of-a-fresh-coat-of-paint-with-new-default-cursor-themes-des|UI refresh: Phase one of a fresh coat of paint with new default Cursor themes…]]

#### 2025-01

- 2025-01-23 · **Cursor** · [[Changes/Cursor/2025-01-23-fusion-model-we-ve-trained-a-new-tab-model-that-is-substantially-better-at-jumps|Fusion Model: We've trained a new Tab Model that is substantially better at jumps…]]
- 2025-01-23 · **Cursor** · [[Changes/Cursor/2025-01-23-summarize-previous-composers-when-conversations-grow-too-long-you-can-start-a-ne|Summarize Previous Composers]]
- 2025-01-23 · **Cursor** · [[Changes/Cursor/2025-01-23-optional-long-context-when-tagging-long-files-users-have-the-option-to-request-a|Optional Long Context]]

### 2024 · 6 entries (Cursor 6)

#### 2024-11

- 2024-11-24 · **Cursor** · [[Changes/Cursor/2024-11-24-early-version-of-an-agent-in-composer-that-can-pick-its-own-context-and-use-the-1228de|Early version of an agent in composer that can pick its own context and use the terminal]]

#### 2024-10

- 2024-10-09 · **Cursor** · [[Changes/Cursor/2024-10-09-composer-now-only-applies-files-that-are-in-context-to-prevent-hallucinations|Composer now only applies files that are in context to prevent hallucinations]]

#### 2024-08

- 2024-08-22 · **Cursor** · [[Changes/Cursor/2024-08-22-we-ve-also-trained-a-new-cursor-tab-model-that-s-smarter-and-more-context-aware-56db10|We've also trained a new Cursor Tab model that's smarter and more context-aware]]

#### 2024-06

- 2024-06-08 · **Cursor** · [[Changes/Cursor/2024-06-08-adds-context-pills-to-chat-messages-so-you-can-see-what-will-be-was-used-a324a3|Adds context pills to chat messages, so you can see what will be/was used]]

#### 2024-04

- 2024-04-12 · **Cursor** · [[Changes/Cursor/2024-04-12-cursorrules-you-can-write-down-repo-level-rules-for-the-ai-by-creating-a-cursorr|.cursorrules: You can write down repo-level rules for the AI by creating…]]
- 2024-04-01 · **Cursor** · [[Changes/Cursor/2024-04-01-long-context-chat-beta-this-is-a-new-experimental-feature-that-lets-you-talk-wit|Long Context Chat (Beta)]]

### 2023 · 19 entries (ChatGPT 1 · Cursor 18)

#### 2023-11

- 2023-11-30 · **Cursor** · [[Changes/Cursor/2023-11-30-better-context-chat-in-particular-followups-are-now-smarter|Better context chat: in particular, followups are now smarter!]]
- 2023-11-27 · **Cursor** · [[Changes/Cursor/2023-11-27-folders-you-can-now-use-the-symbol-to-reference-specific-folders-we-ll-try-to-pi|@ folders: You can now use the @ symbol to reference specific folders!]]
- 2023-11-24 · **Cursor** · [[Changes/Cursor/2023-11-24-you-can-now-folder-in-the-chat-to-chat-with-a-folder-let-us-know-what-you-think|@folder]]
- 2023-11-21 · **Cursor** · [[Changes/Cursor/2023-11-21-integrates-gpt-v-into-chat-for-the-editor-this-means-you-can-take-screenshots-im|GPT-V Support]]
- 2023-11-10 · **Cursor** · [[Changes/Cursor/2023-11-10-copilot-beta-this-is-an-add-on-to-copilot-that-suggests-diffs-around-your-cursor|Copilot++ (beta): this is an "add-on" to Copilot that suggests diffs around…]]

#### 2023-09

- 2023-09-10 · **Cursor** · [[Changes/Cursor/2023-09-10-ask-a-question-about-an-edit-that-the-model-with-option-enter-or-bring-in-contex|Quick question and @chat in cmd+k]]
- 2023-09-08 · **Cursor** · [[Changes/Cursor/2023-09-08-long-files-in-chat|Long files in chat]] · Launch

#### 2023-08

- 2023-08-30 · **Cursor** · [[Changes/Cursor/2023-08-30-for-with-codebase-chats-you-can-now-see-the-codebase-context-that-cursor-shows-g|For "with codebase" chats, you can now see the codebase context that Cursor shows GPT-4]]
- 2023-08-26 · **Cursor** · [[Changes/Cursor/2023-08-26-have-the-advanced-context-button-show-up-for-non-git-repos|Advanced Button]]
- 2023-08-22 · **Cursor** · [[Changes/Cursor/2023-08-22-follow-up-chat-messages-to-with-codebase-will-keep-the-codebase-context|Follow-up chat messages to "with codebase" will keep the codebase context]]
- 2023-08-22 · **Cursor** · [[Changes/Cursor/2023-08-22-if-you-reference-a-long-file-that-will-be-cutoff-by-the-context-limit-you-ll-be|If you @ reference a long file that will be cutoff by the context limit, you'll…]]

#### 2023-07

- 2023-07-19 · **Cursor** · [[Changes/Cursor/2023-07-19-advanced-context-controls-only-show-up-if-you-have-indexed-your-codebase|Advanced context controls only show up if you have indexed your codebase]]
- 2023-07-19 · **Cursor** · [[Changes/Cursor/2023-07-19-more-control-of-context-building-abilities-for-codebase-wide-chat|More control of context building abilities for codebase-wide chat]]

#### 2023-06

- 2023-06-06 · **Cursor** · [[Changes/Cursor/2023-06-06-we-ve-improved-codebase-context|Cursor improves codebase context!]]
- 2023-06-06 · **Cursor** · [[Changes/Cursor/2023-06-06-codebase-context-v1-bd6ee5|Codebase Context v1]] · Launch
- 2023-06-06 · **Cursor** · [[Changes/Cursor/2023-06-06-following-this-you-ll-be-able-to-see-an-improved-version-of-codebase-context-in|Following this, you'll be able to see an improved version of codebase context…]]

#### 2023-05

- 2023-05-17 · **Cursor** · [[Changes/Cursor/2023-05-17-better-jupyter-support|Better Jupyter Support]]
- 2023-05-12 · **ChatGPT** · [[Changes/ChatGPT/2023-05-12-for-more-information-on-our-rollout-process-please-check-out-the-article-here-in|For more information on our rollout process, please check out the article here]]
- 2023-05-04 · **Cursor** · [[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2 Context Window changes in 0.2.9]] · Digest
<!-- chronolog:end -->