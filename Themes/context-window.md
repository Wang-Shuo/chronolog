---
created: '2023-05-04'
date: '2026-11-06'
description: 'Research question: how much material can each product bring into a conversation,
  and how does it handle the limit?'
machine_hash: 447d2e33410800b64b8818eb18caedfcd0b949dde67d8cc76a4f13e6a35e7102
modified: '2026-11-06'
products_involved:
- Aider
- ChatGPT
- Claude Code
- Cline
- Codex CLI
- Cursor
- Gemini CLI
- GitHub Copilot CLI
- OpenHands
- Windsurf
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

420 tracked changes across Aider, ChatGPT, Claude Code, Cline, Codex CLI, Cursor, Gemini CLI, GitHub Copilot CLI, OpenHands and Windsurf · 2023-05-04 → 2026-11-06 · Codex CLI averages 8.0 cards per release, Gemini CLI 7.5, Claude Code 7.0, GitHub Copilot CLI 6.3, Cursor 4.0, OpenHands 3.8, Aider 3.7, Cline 3.0, Windsurf 2.6, ChatGPT 1.7
<!-- chronolog:end -->

## Research summary
<!-- chronolog:begin region="narrative" -->
**Research question: how much material can each product bring into a conversation, and how does it handle the limit?**

ChatGPT's [2026-02-13 update](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#chatgpt-updates-better-file-uploads-easier-copying-and-more-reliable-long-chats) ([[Releases/ChatGPT/chatgpt-2026-02-13-chatgpt-updates-better-file-uploads-easier-copying-and-more-reli-e2c69aa0|archived]]) raises attachments to 20 files per message (previously 10), and the [2026-02-20 note](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#expanded-context-window-for-thinking) ([[Releases/ChatGPT/chatgpt-2026-02-20-expanded-context-window-for-thinking-31f2c4c2|archived]]) sets a total context window of 256k tokens (128k input and 128k maximum output) when users manually select Thinking, up from 196k total tokens. The [2026-03-25 note](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#large-pastes-are-now-handled-as-attachments) ([[Releases/ChatGPT/chatgpt-2026-03-25-large-pastes-are-now-handled-as-attachments-6bacf64e|archived]]) converts pastes over 5k characters into attachments for Plus, Pro and Business users so that large pastes do not consume the whole context window, and the [2026-06-22 note](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#large-pastes-are-now-handled-as-attachments-for-more-plans) ([[Releases/ChatGPT/chatgpt-2026-06-22-large-pastes-are-now-handled-as-attachments-for-more-plans-64db97b0|archived]]) extends this to Free and Go users at a 10k-character threshold.

Cursor's [Codebase Context v1 on 2023-06-06](https://cursor.com/changelog/0-2-26) ([[Releases/Cursor/cursor-2023-06-06-0-2-26-https-cursor-com-changelog-0-2-26-1b7664cb|archived]]) brings context from the full codebase into chat responses, and the [2024-04-01 Long Context Chat beta](https://cursor.com/changelog/0-31-x) ([[Releases/Cursor/cursor-2024-04-01-0-31-x-https-cursor-com-changelog-0-31-x-f88ca4c9|archived]]) lets users talk with many files at once. The [2025-05-15 release](https://cursor.com/changelog/0-50) ([[Releases/Cursor/cursor-2025-05-15-0-50-https-cursor-com-changelog-0-50-dc290998|archived]]) lets @folders add an entire codebase to context, the [2025-07-29 release](https://cursor.com/changelog/1-3) ([[Releases/Cursor/cursor-2025-07-29-1-3-https-cursor-com-changelog-1-3-d153efc3|archived]]) shows how much of the context window a conversation uses, and the [2025-09-12 release](https://cursor.com/changelog/1-6) ([[Releases/Cursor/cursor-2025-09-12-1-6-https-cursor-com-changelog-1-6-f33fb3ea|archived]]) adds on-demand summarization alongside automatic summarization at the context-window limit. [Cursor Projects on 2026-09-10](https://cursor.com/changelog/projects) ([[Releases/Cursor/cursor-2026-09-10-cursor-projects-https-cursor-com-changelog-projects-105aab75|archived]]) keep a shared set of files that every agent in a project can read and extend.

Claude Code's [v2.1.7 on 2026-01-14](https://github.com/anthropics/claude-code/releases/tag/v2.1.7) ([[Releases/Claude Code/claude-code-2026-01-14-v2-1-7-github-276555327-bf21dc80|archived]]) defers MCP tool descriptions to a search tool by default once they exceed 10% of the context window, and [v2.1.51 on 2026-02-24](https://github.com/anthropics/claude-code/releases/tag/v2.1.51) ([[Releases/Claude Code/claude-code-2026-02-24-v2-1-51-github-289665343-b4bbdd9c|archived]]) persists tool results over 50K characters to disk to reduce context window usage. [v2.1.197 on 2026-06-30](https://github.com/anthropics/claude-code/releases/tag/v2.1.197) ([[Releases/Claude Code/claude-code-2026-06-30-v2-1-197-github-346856026-11e4aa1f|archived]]) makes Claude Sonnet 5, with a native 1M-token context window, the default model, and [v2.1.247 on 2026-08-26](https://github.com/anthropics/claude-code/releases/tag/v2.1.247) ([[Releases/Claude Code/claude-code-2026-08-26-v2-1-247-github-377320078-fc507178|archived]]) sets Sonnet 5's default auto-compact window to that full 1M context.

**Uncertainty and scope:** this editorial summary covers ChatGPT, Claude Code and Cursor; the timeline includes all tracked products and Claude Code coverage starts on 2025-12-19; token limits, file counts and summarization rules are each product's own measures under plan and model qualifications, so these figures do not compare capacity across products.
<!-- chronolog:end -->

## Key moments
<!-- chronolog:begin region="moments" -->
Selected automatically from launches and standalone announcements.

| Quarter | Aider | ChatGPT | Claude Code | Cline | Codex CLI | Cursor | Gemini CLI | GitHub Copilot CLI | OpenHands | Windsurf |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **First in archive** | <time datetime="2023-06-07">2023-06-07</time> [[Changes/Aider/2023-06-07-2-context-window-changes-in-v0-5-0\|2 Context Window changes in v0.5.0]] | <time datetime="2023-05-12">2023-05-12</time> [[Changes/ChatGPT/2023-05-12-for-more-information-on-our-rollout-process-please-check-out-the-article-here-in\|For more information on our rollout process, please check out the article here]] | <time datetime="2025-12-19">2025-12-19</time> [[Changes/Claude Code/2025-12-19-improved-context-command-visualization-with-grouped-skills-and-agents-by-source\|Improved /context command visualization with grouped skills and agents by source…]] | <time datetime="2024-07-28">2024-07-28</time> [[Changes/Cline/2024-07-28-updated-max-output-tokens-to-8192-so-less-lazy-coding-rest-of-code-here\|Updated max output tokens to 8192 so less lazy coding (// rest of code here...)]] | <time datetime="2025-08-12">2025-08-12</time> [[Changes/Codex CLI/2025-08-12-https-github-com-openai-codex-pull-2200-send-prompt-cache-key-for-better-caching\|(source link) send prompt cache key for better caching…]] | <time datetime="2023-05-04">2023-05-04</time> [[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9\|2 Context Window changes in 0.2.9]] | <time datetime="2025-07-19">2025-07-19</time> [[Changes/Gemini CLI/2025-07-19-2-context-window-changes-in-v0-1-13\|2 Context Window changes in v0.1.13]] | <time datetime="2025-10-03">2025-10-03</time> [[Changes/GitHub Copilot CLI/2025-10-03-added-a-warning-when-conversation-context-approaches-20-remaining-of-the-model-s\|Added a warning when conversation context approaches ≤20% remaining of the model's…]] | <time datetime="2024-07-27">2024-07-27</time> [[Changes/OpenHands/2024-07-27-fix-colima-use-a-docker-context-specific-to-runner-prevent-duplicate-start-by-to\|(fix) colima: use a docker context specific to runner; prevent duplicate start]] | <time datetime="2025-07-17">2025-07-17</time> [[Changes/Windsurf/2025-07-17-mentioning-conversations\|mentioning conversations]] |
| 2026 Q4 | · | · | <time datetime="2026-10-14">2026-10-14</time> [[Changes/Claude Code/2026-10-14-added-usage-warnings-for-max-effort-workflows-always-on-context-and-large-tool-r\|Added /usage warnings for max effort, workflows, always-on context and large tool…]] | · | · | · | · | · | · | · |
| 2026 Q3 | · | · | <time datetime="2026-09-04">2026-09-04</time> [[Changes/Claude Code/2026-09-04-added-skill-doctor-to-show-which-loaded-skills-go-unused-and-what-they-cost-in-c\|Added /skill-doctor to show which loaded skills go unused and what they cost…]] | · | · | <time datetime="2026-09-10">2026-09-10</time> [[Changes/Cursor/2026-09-10-you-shouldn-t-have-to-onboard-an-agent-every-time-you-start-a-task-each-project\|Shared context]]<br><time datetime="2026-07-17">2026-07-17</time> [[Changes/Cursor/2026-07-17-cross-channel-workflows\|Cross-channel workflows]]<br><time datetime="2026-07-10">2026-07-10</time> [[Changes/Cursor/2026-07-10-side-chats\|Side chats]] | · | · | · | · |
| 2026 Q2 | · | · | <time datetime="2026-06-08">2026-06-08</time> [[Changes/Claude Code/2026-06-08-added-cd-command-to-move-a-session-to-a-new-working-directory-without-breaking-t\|Added /cd command to move a session to a new working directory without breaking…]] | · | · | <time datetime="2026-06-04">2026-06-04</time> [[Changes/Cursor/2026-06-04-this-release-introduces-design-mode-for-faster-canvas-editing-new-ways-to-unders\|Cursor introduces Design Mode for faster canvas editing, new ways to understand…]]<br><time datetime="2026-05-13">2026-05-13</time> [[Changes/Cursor/2026-05-13-compact-chat-responses\|Compact chat responses]] | · | · | · | · |
| 2026 Q1 | · | · | · | · | · | · | · | · | · | · |
| 2025 Q4 | · | · | archive begins <time datetime="2025-12-19">2025-12-19</time> | · | · | <time datetime="2025-12-18">2025-12-18</time> [[Changes/Cursor/2025-12-18-conversation-insights-2efafc\|Conversation insights]] | · | · | · | <time datetime="2025-12-24">2025-12-24</time> [[Changes/Windsurf/2025-12-24-context-window-indicator\|Context Window Indicator]]<br><time datetime="2025-11-21">2025-11-21</time> [[Changes/Windsurf/2025-11-21-fast-context\|Fast Context]]<br><time datetime="2025-11-04">2025-11-04</time> [[Changes/Windsurf/2025-11-04-cascade-summarization-fix\|Cascade Summarization Fix]] |
| 2025 Q3 | · | · | <span class="not-archived">not archived</span> | · | · | <time datetime="2025-09-12">2025-09-12</time> [[Changes/Cursor/2025-09-12-cursor-automatically-summarizes-long-conversation-for-you-when-reaching-the-cont\|Summarization triggers]]<br><time datetime="2025-07-29">2025-07-29</time> [[Changes/Cursor/2025-07-29-at-the-end-of-a-conversation-you-can-now-see-how-much-of-the-context-window-is-u\|View context usage in Chat]] | · | archive begins <time datetime="2025-09-26">2025-09-26</time> | · | <time datetime="2025-07-17">2025-07-17</time> [[Changes/Windsurf/2025-07-17-mentioning-conversations\|mentioning conversations]] |
| 2025 Q2 | · | · | <span class="not-archived">not archived</span> | · | archive begins <time datetime="2025-06-30">2025-06-30</time> | <time datetime="2025-05-15">2025-05-15</time> [[Changes/Cursor/2025-05-15-include-your-entire-codebase-in-context\|Include your entire codebase in context]] | archive begins <time datetime="2025-06-28">2025-06-28</time> | <span class="not-archived">not archived</span> | · | archive begins <time datetime="2025-04-02">2025-04-02</time> |
| 2025 Q1 | <time datetime="2025-03-13">2025-03-13</time> [[Changes/Aider/2025-03-13-added-think-tokens-command-to-set-thinking-token-budget-with-support-for-human-r\|Added /think-tokens command to set thinking token budget with support…]] | · | <span class="not-archived">not archived</span> | · | <span class="not-archived">not archived</span> | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | · | <span class="not-archived">not archived</span> |
| 2024 Q4 | · | · | <span class="not-archived">not archived</span> | <time datetime="2024-12-18">2024-12-18</time> [[Changes/Cline/2024-12-18-you-can-now-specify-custom-instructions-for-your-project-by-adding-a-root-level\|Specify custom instructions for your project by adding a root-level .clinerules file]] | <span class="not-archived">not archived</span> | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | · | <span class="not-archived">not archived</span> |
| 2024 Q3 | · | · | <span class="not-archived">not archived</span> | <time datetime="2024-09-19">2024-09-19</time> [[Changes/Cline/2024-09-19-you-can-now-use-in-the-textarea-to-add-context\|Use @ in the textarea to add context!]] | <span class="not-archived">not archived</span> | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | · | <span class="not-archived">not archived</span> |
| 2024 Q1 → 2024 Q2 | · | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | archive begins <time datetime="2024-06-04">2024-06-04</time> | <span class="not-archived">not archived</span> |
| 2023 Q4 | · | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <time datetime="2023-11-24">2023-11-24</time> [[Changes/Cursor/2023-11-24-you-can-now-folder-in-the-chat-to-chat-with-a-folder-let-us-know-what-you-think\|@folder]] | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> |
| 2023 Q3 | · | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <time datetime="2023-09-08">2023-09-08</time> [[Changes/Cursor/2023-09-08-long-files-in-chat\|Long files in chat]] | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> |
| 2023 Q2 | archive begins <time datetime="2023-06-07">2023-06-07</time> | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <time datetime="2023-06-06">2023-06-06</time> [[Changes/Cursor/2023-06-06-codebase-context-v1-bd6ee5\|Codebase Context v1]] | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> |

First in archive: each product's earliest tracked change in this theme. "·" marks a quarter without a key moment, and "not archived" a quarter before the product's archive begins. Archives begin: Aider 2023-06-07 · ChatGPT 2022-12-15 · Claude Code 2025-12-19 · Cline 2024-07-28 · Codex CLI 2025-06-30 · Cursor 2023-03-14 · Gemini CLI 2025-06-28 · GitHub Copilot CLI 2025-09-26 · OpenHands 2024-06-04 · Windsurf 2025-04-02.
<!-- chronolog:end -->

<!-- chronolog:begin region="scope" -->
<details class="disclosure">
<summary>How to read this timeline</summary>

Scope: tracked-products-only. Entries show same-theme chronology; they do not establish equivalent capabilities, adoption, or causation.

</details>
<!-- chronolog:end -->

## Timeline
<!-- chronolog:begin region="timeline" -->
<div class="timeline">

Launches, expansions, pricing and policy changes and standalone announcements come first in each year; fixes, digests and other changes are folded beneath them.

<fieldset class="timeline-filter">
<legend>Show</legend>
<label><input type="radio" name="timeline-product" id="tl-only-all" checked> All</label>
<label><input type="radio" name="timeline-product" id="tl-only-1"> Aider</label>
<label><input type="radio" name="timeline-product" id="tl-only-2"> ChatGPT</label>
<label><input type="radio" name="timeline-product" id="tl-only-3"> Claude Code</label>
<label><input type="radio" name="timeline-product" id="tl-only-4"> Cline</label>
<label><input type="radio" name="timeline-product" id="tl-only-5"> Codex CLI</label>
<label><input type="radio" name="timeline-product" id="tl-only-6"> Cursor</label>
<label><input type="radio" name="timeline-product" id="tl-only-7"> Gemini CLI</label>
<label><input type="radio" name="timeline-product" id="tl-only-8"> GitHub Copilot CLI</label>
<label><input type="radio" name="timeline-product" id="tl-only-9"> OpenHands</label>
<label><input type="radio" name="timeline-product" id="tl-only-10"> Windsurf</label>
</fieldset>

<details class="disclosure">
<summary>2026 · 255 entries (ChatGPT 9 · Claude Code 73 · Cline 22 · Codex CLI 67 · Cursor 12 · Gemini CLI 16 · GitHub Copilot CLI 50 · OpenHands 5 · Windsurf 1)</summary>

**2026-10**

- 2026-10-14 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-14-added-usage-warnings-for-max-effort-workflows-always-on-context-and-large-tool-r|Added /usage warnings for max effort, workflows, always-on context and large tool…]] · Change

**2026-09**

- 2026-09-10 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-09-10-you-shouldn-t-have-to-onboard-an-agent-every-time-you-start-a-task-each-project|Shared context]] · Launch
- 2026-09-10 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-09-10-today-we-re-launching-projects-in-cursor-projects-lets-you-take-on-larger-bodies-51d06c|Cursor launches Projects]] · Launch
- 2026-09-04 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-04-added-skill-doctor-to-show-which-loaded-skills-go-unused-and-what-they-cost-in-c|Added /skill-doctor to show which loaded skills go unused and what they cost…]] · Change

**2026-07**

- 2026-07-17 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-07-17-cross-channel-workflows|Cross-channel workflows]] · Launch
- 2026-07-10 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-07-10-side-chats|Side chats]] · Launch

**2026-06**

- 2026-06-08 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-06-08-added-cd-command-to-move-a-session-to-a-new-working-directory-without-breaking-t|Added /cd command to move a session to a new working directory without breaking…]] · Change
- 2026-06-04 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-06-04-this-release-introduces-design-mode-for-faster-canvas-editing-new-ways-to-unders|Cursor introduces Design Mode for faster canvas editing, new ways to understand…]] · Launch
- 2026-06-04 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-06-04-context-usage-report-in-canvas-d08e2a|Context usage report in canvas]] · Launch

**2026-05**

- 2026-05-13 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-05-13-compact-chat-responses|Compact chat responses]] · Launch
- 2026-05-06 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-05-06-you-can-now-see-a-breakdown-of-your-agent-s-context-usage-e005b2|Context Usage Breakdown]] · Change

**2026-04**

- 2026-04-16 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-16-add-statusline-command-with-footer-alias-to-customize-which-items-appear-in-the|Add /statusline command (with /footer alias) to customize which items appear…]] · Policy

<details class="disclosure">
<summary>Fixes, digests and other changes · 243 (ChatGPT 9 · Claude Code 70 · Cline 22 · Codex CLI 67 · Cursor 4 · Gemini CLI 16 · GitHub Copilot CLI 49 · OpenHands 5 · Windsurf 1)</summary>

**2026-11**

- 2026-11-06 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-11-06-8-context-window-changes-in-rust-v0-167-0|8 Context Window changes in rust-v0.167.0]] · Digest
- 2026-11-06 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-11-06-17-context-window-changes-in-v1-0-106|17 Context Window changes in v1.0.106]] · Digest

**2026-10**

- 2026-10-29 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-29-13-context-window-changes-in-rust-v0-166-0|13 Context Window changes in rust-v0.166.0]] · Digest
- 2026-10-27 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-27-changed-a-subagent-s-autocompactwindow-to-lower-the-window-set-by-claude-code-au|Changed a subagent's autoCompactWindow to lower the window set…]] · Change
- 2026-10-27 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-27-2-context-window-changes-in-rust-v0-165-0|2 Context Window changes in rust-v0.165.0]] · Digest
- 2026-10-26 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-26-2-context-window-changes-in-v2-1-311|2 Context Window changes in v2.1.311]] · Digest
- 2026-10-26 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-10-26-auto-compaction-no-longer-runs-for-models-with-an-unknown-context-limit-and-it-n|Auto-compaction no longer runs for models with an unknown context limit, and it no…]] · Change
- 2026-10-23 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-23-18-context-window-changes-in-rust-v0-164-0|18 Context Window changes in rust-v0.164.0]] · Digest
- 2026-10-22 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-22-updated-the-claude-api-skill-service-account-keys-and-workload-identity-federati|Updated the /claude-api skill]] · Change
- 2026-10-20 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-20-switching-only-reasoning-effort-no-longer-forces-compaction-in-over-budget-sessi|Switching only reasoning effort no longer forces compaction in over-budget sessions]] · Change
- 2026-10-19 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-19-3-context-window-changes-in-v2-1-304|3 Context Window changes in v2.1.304]] · Digest
- 2026-10-19 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-19-avoid-false-context-exhaustion-and-rollover-refusal-when-tool-definitions-are-de|Avoid false context exhaustion and rollover refusal when tool definitions are deferred]] · Change
- 2026-10-19 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-10-19-chore-lint-remove-context-color-spec-bookkeeping-by-enyst-in-https-github-com-op|chore(lint): remove context color spec bookkeeping]] · Change
- 2026-10-16 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-16-2-context-window-changes-in-v2-1-302|2 Context Window changes in v2.1.302]] · Digest
- 2026-10-16 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-10-16-auto-compact-and-its-strategy-setting-sit-together-again-in-feature-settings|Auto Compact and its strategy setting sit together again in Feature settings]] · Change
- 2026-10-15 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-15-improved-switching-to-a-model-with-a-smaller-context-window-a-conversation-too-l|Improved switching to a model with a smaller context window]] · Change
- 2026-10-15 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-15-16-context-window-changes-in-rust-v0-163-0|16 Context Window changes in rust-v0.163.0]] · Digest
- 2026-10-14 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-14-added-cache-creation-5m-tokens-and-cache-creation-1h-tokens-to-the-opentelemetry|Added cache_creation_5m_tokens and cache_creation_1h_tokens to the OpenTelemetry…]] · Change
- 2026-10-14 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-14-2-context-window-changes-in-v2-1-299|2 Context Window changes in v2.1.299]] · Digest
- 2026-10-13 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-10-13-2-context-window-changes-in-v4-1-24|2 Context Window changes in v4.1.24]] · Digest
- 2026-10-09 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-09-2-context-window-changes-in-v2-1-296|2 Context Window changes in v2.1.296]] · Digest
- 2026-10-09 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-09-context-now-applies-to-new-and-resumed-acp-sessions-instead-of-silently-using-th|--context now applies to new and resumed ACP sessions instead of silently using…]] · Change
- 2026-10-08 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-08-improved-token-counts-behind-a-claude-apps-gateway-on-amazon-bedrock-which-conte|Improved token counts behind a Claude apps gateway on Amazon Bedrock…]] · Change
- 2026-10-08 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-08-10-context-window-changes-in-rust-v0-162-0|10 Context Window changes in rust-v0.162.0]] · Digest
- 2026-10-07 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-07-9-context-window-changes-in-rust-v0-161-0|9 Context Window changes in rust-v0.161.0]] · Digest
- 2026-10-07 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-07-honor-context-long-context-at-startup-and-show-accurate-context-allowance-in-con|Honor --context long_context at startup and show accurate context allowance in /context]] · Change
- 2026-10-05 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-05-2-context-window-changes-in-v1-0-92|2 Context Window changes in v1.0.92]] · Digest
- 2026-10-02 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-02-changed-autocompact-to-save-the-auto-compact-window-per-model-so-each-model-keep|Changed /autocompact to save the auto-compact window per model, so each model…]] · Change
- 2026-10-01 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-01-changed-opus-4-7-and-fable-to-use-a-1m-context-window-by-default-on-bedrock-vert|Changed Opus 4.7+ and Fable to use a 1M context window by default on Bedrock…]] · Change
- 2026-10-01 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-01-3-context-window-changes-in-rust-v0-160-0|3 Context Window changes in rust-v0.160.0]] · Digest

**2026-09**

- 2026-09-30 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-30-improved-the-model-fallback-notice-and-the-autocompact-thrashing-error-to-say-wh|Improved the model fallback notice and the autocompact-thrashing error to say…]] · Change
- 2026-09-30 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-09-30-reasoning-tokens-are-no-longer-counted-twice-in-token-usage-cost-is-unchanged|Reasoning tokens are no longer counted twice in token usage]] · Change
- 2026-09-30 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-09-30-compaction-now-returns-a-summary-even-when-instructions-ask-for-tool-use|Compaction now returns a summary even when instructions ask for tool use]] · Change
- 2026-09-29 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-29-2-context-window-changes-in-v2-1-285|2 Context Window changes in v2.1.285]] · Digest
- 2026-09-29 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-29-4-context-window-changes-in-rust-v0-159-0|4 Context Window changes in rust-v0.159.0]] · Digest
- 2026-09-28 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-28-17-context-window-changes-in-rust-v0-158-0|17 Context Window changes in rust-v0.158.0]] · Digest
- 2026-09-25 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-25-2-context-window-changes-in-v2-1-283|2 Context Window changes in v2.1.283]] · Digest
- 2026-09-25 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-25-6-context-window-changes-in-rust-v0-157-0|6 Context Window changes in rust-v0.157.0]] · Digest
- 2026-09-25 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-09-25-refactor-remove-test-conversation-id-fallbacks-in-websocket-context-add-state-up|refactor: remove test-conversation-id fallbacks in websocket context + add…]] · Change
- 2026-09-24 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-09-24-long-replies-on-local-models-llama-cpp-ollama-lm-studio-that-hit-the-output-toke|Long replies on local models (llama.cpp, Ollama, LM Studio) that hit…]] · Change
- 2026-09-22 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-09-22-2-context-window-changes-in-v4-1-20|2 Context Window changes in v4.1.20]] · Digest
- 2026-09-22 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-22-17-context-window-changes-in-rust-v0-156-0|17 Context Window changes in rust-v0.156.0]] · Digest
- 2026-09-17 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-09-17-long-tasks-now-compact-when-they-actually-need-to-rather-than-running-out-of-roo|Long tasks now compact when they actually need to rather than running out of room]] · Change
- 2026-09-17 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-17-20-context-window-changes-in-rust-v0-155-0|20 Context Window changes in rust-v0.155.0]] · Digest
- 2026-09-16 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-09-16-3-context-window-changes-in-v1-0-85|3 Context Window changes in v1.0.85]] · Digest
- 2026-09-16 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-09-16-test-cover-conversation-context-menu-by-aivong-openhands-in-https-github-com-ope|test: cover conversation context menu]] · Change
- 2026-09-15 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-15-added-x-claude-code-request-class-x-claude-code-agent-type-x-claude-code-prev-to|Added x-claude-code-request-class, x-claude-code-agent-type…]] · Change
- 2026-09-14 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-14-improved-the-spinner-status-during-long-thinking-it-now-reads-deep-in-thought-af|Improved the spinner status during long thinking]] · Change
- 2026-09-09 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-09-improved-prompt-cache-stability-subagents-and-sessions-started-with-system-promp|Improved prompt-cache stability]] · Change
- 2026-09-09 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-09-17-context-window-changes-in-rust-v0-154-0|17 Context Window changes in rust-v0.154.0]] · Digest
- 2026-09-04 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-04-changed-context-token-counting-to-use-a-local-estimate-when-the-token-counting-a|Changed /context token counting to use a local estimate when the token-counting…]] · Change
- 2026-09-03 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-03-3-context-window-changes-in-v2-1-260|3 Context Window changes in v2.1.260]] · Digest
- 2026-09-03 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-03-6-context-window-changes-in-rust-v0-153-0|6 Context Window changes in rust-v0.153.0]] · Digest
- 2026-09-01 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-01-9-context-window-changes-in-rust-v0-152-0|9 Context Window changes in rust-v0.152.0]] · Digest

**2026-08**

- 2026-08-31 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-08-31-bring-your-browser-into-work-and-codex-mention-open-tabs-to-use-them-as-context-af2c3a|Bring your browser into Work and Codex]] · Change
- 2026-08-28 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-28-improved-retry-when-the-model-s-tool-call-is-malformed-the-broken-output-is-now|Improved retry when the model's tool call is malformed]] · Change
- 2026-08-27 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-27-improved-the-workflow-tool-s-prompt-footprint-its-description-is-now-about-1k-to|Improved the Workflow tool's prompt footprint]] · Change
- 2026-08-27 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-08-27-2-context-window-changes-in-rust-v0-150-1|2 Context Window changes in rust-v0.150.1]] · Digest
- 2026-08-27 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-08-27-hooks-can-now-receive-the-current-opentelemetry-trace-context-and-emit-correlate|Hooks can now receive the current OpenTelemetry trace context and emit correlated spans]] · Change
- 2026-08-26 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-26-changed-sonnet-5-s-default-auto-compact-window-to-its-full-1m-context-so-session|Changed Sonnet 5's default auto-compact window to its full 1M context, so sessions…]] · Change
- 2026-08-26 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-08-26-14-context-window-changes-in-rust-v0-150-0|14 Context Window changes in rust-v0.150.0]] · Digest
- 2026-08-25 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-08-25-ssr-agent-issue-fix-19239-update-clear-command-docs-to-include-context-reset-by|SSR Agent Issue Fix (19239): Update /clear command docs to include context reset]] · Change
- 2026-08-21 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-21-improved-the-reminder-shown-after-compaction-so-a-skill-s-original-arguments-are|Improved the reminder shown after compaction so a skill's original arguments are not…]] · Change
- 2026-08-21 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-08-21-only-treat-an-anthropic-invalid-request-error-as-a-context-overflow-when-its-mes|Only treat an Anthropic invalid_request_error as a context-overflow…]] · Change
- 2026-08-20 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-08-20-9-context-window-changes-in-rust-v0-149-0|9 Context Window changes in rust-v0.149.0]] · Digest
- 2026-08-18 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-18-improved-the-context-limit-error-to-say-when-auto-compact-is-off-and-point-to-co|Improved the context-limit error to say when auto-compact is off and point…]] · Change
- 2026-08-18 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-08-18-13-context-window-changes-in-rust-v0-148-0|13 Context Window changes in rust-v0.148.0]] · Digest
- 2026-08-17 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-17-2-context-window-changes-in-v2-1-234|2 Context Window changes in v2.1.234]] · Digest
- 2026-08-14 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-14-improved-apps-gateway-error-forwarding-400-413-errors-from-vertex-foundry-and-cl|Improved apps gateway error forwarding]] · Change
- 2026-08-13 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-08-13-feat-context-window-usage-meter-usage-drawer-and-manual-compaction-by-georgeglar|feat: context window usage meter, usage drawer, and manual compaction]] · Change
- 2026-08-12 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-12-improved-prompt-is-too-long-errors-to-explain-why-automatic-compaction-could-not|Improved "prompt is too long" errors to explain why automatic compaction could not…]] · Change
- 2026-08-11 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-11-improved-compaction-progress-the-retry-countdown-and-stall-hint-now-appear-durin|Improved compaction progress]] · Change
- 2026-08-11 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-08-11-respect-your-configured-max-output-tokens-when-the-compaction-summarizer-request|Respect your configured max output tokens when the compaction summarizer requests…]] · Change
- 2026-08-11 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-08-11-refactor-exclude-transient-ci-configuration-files-from-workspace-context-by-davi|Refactor: exclude transient CI configuration files from workspace context]] · Change
- 2026-08-10 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-08-10-compute-context-attribution-against-the-auto-resolved-model-so-token-totals-are|Compute /context attribution against the Auto-resolved model so token totals…]] · Change
- 2026-08-09 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-08-09-2-context-window-changes-in-v4-1-7|2 Context Window changes in v4.1.7]] · Digest
- 2026-08-07 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-08-07-10-context-window-changes-in-rust-v0-147-0|10 Context Window changes in rust-v0.147.0]] · Digest
- 2026-08-06 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-06-2-context-window-changes-in-v2-1-223|2 Context Window changes in v2.1.223]] · Digest
- 2026-08-05 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-08-05-recover-from-running-out-of-context-instead-of-failing-with-a-raw-provider-error|Recover from running out of context instead of failing with a raw provider error]] · Change
- 2026-08-04 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-08-04-if-you-paste-more-than-10k-characters-into-the-composer-chatgpt-will-automatical-1bd022|If you paste more than 10k characters into the composer, ChatGPT will automatically…]] · Change
- 2026-08-04 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-04-improved-stats-panel-to-count-cache-tokens-in-its-token-totals-with-a-breakdown|Improved Stats panel to count cache tokens in its token totals, with a breakdown…]] · Change

**2026-07**

- 2026-07-30 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-30-restore-the-early-warning-when-unreclaimable-system-and-tool-context-nears-the-l|Restore the early warning when unreclaimable system and tool context nears…]] · Change
- 2026-07-29 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-07-29-5-context-window-changes-in-rust-v0-146-0|5 Context Window changes in rust-v0.146.0]] · Digest
- 2026-07-24 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-07-24-add-claude-opus-5-across-the-anthropic-claude-code-bedrock-vertex-cline-and-open|Add Claude Opus 5 across the Anthropic, Claude Code, Bedrock, Vertex, Cline…]] · Change
- 2026-07-22 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-07-22-changed-skills-with-context-fork-to-run-in-the-background-by-default-opt-out-per|Changed skills with context: fork to run in the background by default]] · Change
- 2026-07-22 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-07-22-refactor-exclude-transient-ci-configuration-files-from-workspace-context-by-davi|Refactor: exclude transient CI configuration files from workspace context]] · Change
- 2026-07-21 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-07-21-12-context-window-changes-in-rust-v0-145-0|12 Context Window changes in rust-v0.145.0]] · Digest
- 2026-07-20 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-07-20-context-now-shows-an-explicit-warning-when-the-conversation-exceeds-the-context|/context now shows an explicit warning when the conversation exceeds the context…]] · Change
- 2026-07-20 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-20-2-context-window-changes-in-v1-0-72|2 Context Window changes in v1.0.72]] · Digest
- 2026-07-16 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-16-2-context-window-changes-in-v1-0-71|2 Context Window changes in v1.0.71]] · Digest
- 2026-07-10 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-10-press-tab-to-switch-the-context-window-in-model|Press Tab to switch the context window in /model]] · Change
- 2026-07-09 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-07-09-3-context-window-changes-in-rust-v0-144-0|3 Context Window changes in rust-v0.144.0]] · Digest
- 2026-07-08 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-07-08-improved-auto-mode-to-ask-before-running-rm-rf-on-a-variable-it-can-t-resolve-fr|Improved auto mode to ask before running rm -rf on a variable it can't resolve…]] · Change
- 2026-07-08 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-07-08-12-context-window-changes-in-rust-v0-143-0|12 Context Window changes in rust-v0.143.0]] · Digest
- 2026-07-07 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-07-warn-when-static-context-uses-most-of-the-prompt-budget-and-block-requests-when|Warn when static context uses most of the prompt budget and block requests…]] · Change
- 2026-07-06 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-07-06-test-pltf-1269-replace-test-should-naming-with-test-verb-noun-context-convention|test: PLTF-1269 replace test_should naming with test_verb_noun_context convention]] · Change
- 2026-07-01 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-07-01-subagents-and-context-compaction-now-inherit-the-session-s-extended-thinking-con|Subagents and context compaction now inherit the session's extended thinking…]] · Change
- 2026-07-01 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-01-2-context-window-changes-in-v1-0-68|2 Context Window changes in v1.0.68]] · Digest

**2026-06**

- 2026-06-30 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-30-keep-session-store-searches-and-context-lookups-responsive|Keep session-store searches and context lookups responsive]] · Change
- 2026-06-25 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-25-2-context-window-changes-in-rust-v0-142-2|2 Context Window changes in rust-v0.142.2]] · Digest
- 2026-06-23 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-23-3-context-window-changes-in-v1-0-64|3 Context Window changes in v1.0.64]] · Digest
- 2026-06-22 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-06-22-starting-today-for-chatgpt-free-and-go-users-long-pastes-are-handled-differently|Large pastes are now handled as attachments for more plans]] · Change
- 2026-06-22 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-06-22-bash-commands-now-trigger-claude-to-respond-to-the-output-automatically-set-resp|! bash commands now trigger Claude to respond to the output automatically]] · Change
- 2026-06-22 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-22-10-context-window-changes-in-rust-v0-142-0|10 Context Window changes in rust-v0.142.0]] · Digest
- 2026-06-18 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-18-2-context-window-changes-in-rust-v0-141-0|2 Context Window changes in rust-v0.141.0]] · Digest
- 2026-06-15 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-15-7-context-window-changes-in-rust-v0-140-0|7 Context Window changes in rust-v0.140.0]] · Digest
- 2026-06-13 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-13-honor-max-output-tokens-for-byok-responses-providers|Honor max_output_tokens for BYOK Responses providers]] · Change
- 2026-06-12 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-06-12-vscode-added-usage-attribution-to-the-account-usage-dialog-usage-showing-cache-m|VSCode Added usage attribution to the Account & usage dialog (/usage) showing…]] · Change
- 2026-06-09 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-09-3-context-window-changes-in-rust-v0-139-0|3 Context Window changes in rust-v0.139.0]] · Digest
- 2026-06-08 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-06-08-the-claude-md-is-too-long-warning-threshold-now-scales-with-the-model-s-context|The "CLAUDE.md is too long" warning threshold now scales with the model's context window]] · Change
- 2026-06-08 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-08-4-context-window-changes-in-rust-v0-138-0|4 Context Window changes in rust-v0.138.0]] · Digest
- 2026-06-06 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2026-06-06-improved-handling-of-file-context-in-devin-local-agent|Improved handling of file context in Devin Local agent]] · Change
- 2026-06-05 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-05-2-context-window-changes-in-v1-0-60|2 Context Window changes in v1.0.60]] · Digest
- 2026-06-04 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-04-3-context-window-changes-in-rust-v0-137-0|3 Context Window changes in rust-v0.137.0]] · Digest
- 2026-06-03 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-06-03-feat-context-complete-simplification-work-by-joshualitt-in-https-github-com-goog|feat(context): Complete simplification work]] · Change
- 2026-06-01 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-01-9-context-window-changes-in-rust-v0-136-0|9 Context Window changes in rust-v0.136.0]] · Digest

**2026-05**

- 2026-05-29 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-29-2-context-window-changes-in-v1-0-56|2 Context Window changes in v1.0.56]] · Digest
- 2026-05-28 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-05-28-claude-now-reserves-the-multiple-choice-question-prompt-for-decisions-it-genuine|Claude now reserves the multiple-choice question prompt for decisions it genuinely…]] · Change
- 2026-05-28 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-05-28-show-prompt-cache-support-for-qwen-3-7-max-in-the-cline-provider|Show prompt-cache support for Qwen 3.7 Max in the Cline provider]] · Change
- 2026-05-28 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-05-28-4-context-window-changes-in-rust-v0-135-0|4 Context Window changes in rust-v0.135.0]] · Digest
- 2026-05-28 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-28-2-context-window-changes-in-v1-0-55|2 Context Window changes in v1.0.55]] · Digest
- 2026-05-27 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-05-27-added-pluginsuggestionmarketplaces-managed-setting-admins-can-allowlist-org-mark|Added pluginSuggestionMarketplaces managed setting]] · Change
- 2026-05-26 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-05-26-5-context-window-changes-in-rust-v0-134-0|5 Context Window changes in rust-v0.134.0]] · Digest
- 2026-05-23 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-23-4-context-window-changes-in-v1-0-52|4 Context Window changes in v1.0.52]] · Digest
- 2026-05-22 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-05-22-improved-feedback-reports-to-include-the-conversation-that-happened-before-conte|Improved /feedback reports to include the conversation that happened before…]] · Change
- 2026-05-22 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-05-22-3-context-window-changes-in-v0-43-0|3 Context Window changes in v0.43.0]] · Digest
- 2026-05-21 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-05-21-5-context-window-changes-in-rust-v0-133-0|5 Context Window changes in rust-v0.133.0]] · Digest
- 2026-05-20 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-20-customizable-status-line-in-the-terminal-footer-displays-session-info-such-as-mo|Customizable status line in the terminal footer displays session info such as model…]] · Change
- 2026-05-19 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-05-19-improved-the-read-tool-to-return-a-truncated-first-page-with-a-partial-view-noti|Improved the Read tool to return a truncated first page with a "PARTIAL view" notice…]] · Change
- 2026-05-19 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-05-19-the-post-survey-follow-up-hint-now-appears-after-every-non-dismiss-survey-respon|The post-survey follow-up hint now appears after every non-dismiss survey response…]] · Change
- 2026-05-19 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-19-document-attachment-paths-are-included-in-context-so-the-agent-can-reference-pas|Document attachment paths are included in context so the agent can reference pasted…]] · Change
- 2026-05-18 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-05-18-7-context-window-changes-in-rust-v0-131-0|7 Context Window changes in rust-v0.131.0]] · Digest
- 2026-05-14 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-05-14-improved-reactive-compaction-the-first-summarize-attempt-now-seeds-from-the-orig|Improved reactive compaction]] · Change
- 2026-05-14 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-14-context-shows-correct-token-limits-for-all-models-instead-of-always-showing-128k|/context shows correct token limits for all models instead of always showing 128k]] · Change
- 2026-05-13 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-05-13-rewind-menu-added-summarize-up-to-here-to-compress-earlier-context-while-keeping|Rewind menu: added "Summarize up to here" to compress earlier context while keeping…]] · Change
- 2026-05-11 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-05-11-context-all-per-skill-token-estimates-now-account-for-the-model-s-tokenizer-and|/context all per-skill token estimates now account for the model's tokenizer…]] · Change
- 2026-05-08 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-05-08-2-context-window-changes-in-rust-v0-130-0|2 Context Window changes in rust-v0.130.0]] · Digest
- 2026-05-07 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-05-07-7-context-window-changes-in-rust-v0-129-0|7 Context Window changes in rust-v0.129.0]] · Digest
- 2026-05-01 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-01-remote-session-statusline-shows-the-remote-working-directory-and-branch-instead|Remote session statusline shows the remote working directory and branch instead…]] · Change

**2026-04**

- 2026-04-30 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-30-19805-add-multiagentv2-root-and-subagent-context-hints-jif-oai|♯19805 Add MultiAgentV2 root and subagent context hints @jif-oai]] · Change
- 2026-04-28 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-04-28-vscode-context-now-opens-a-native-token-usage-dialog|VSCode /context now opens a native token usage dialog]] · Change
- 2026-04-28 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-28-add-compact-context-usage-and-env-slash-commands-for-acp-sessions|Add /compact, /context, /usage, and /env slash commands for ACP sessions]] · Change
- 2026-04-24 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-24-2-context-window-changes-in-rust-v0-125-0|2 Context Window changes in rust-v0.125.0]] · Digest
- 2026-04-23 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-23-18794-organize-context-fragments-pakrym-oai|♯18794 Organize context fragments @pakrym-oai]] · Change
- 2026-04-23 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-23-2-context-window-changes-in-rust-v0-124-0|2 Context Window changes in rust-v0.124.0]] · Digest
- 2026-04-23 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-23-2-context-window-changes-in-v1-0-35|2 Context Window changes in v1.0.35]] · Digest
- 2026-04-20 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-20-10-context-window-changes-in-rust-v0-122-0|10 Context Window changes in rust-v0.122.0]] · Digest
- 2026-04-17 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-17-3-context-window-changes-in-v1-0-32|3 Context Window changes in v1.0.32]] · Digest
- 2026-04-15 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-04-15-added-option-to-show-claude-s-last-response-as-commented-context-in-the-ctrl-g-e|Added option to show Claude's last response as commented context in the Ctrl+G…]] · Change
- 2026-04-15 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-15-4-context-window-changes-in-rust-v0-121-0|4 Context Window changes in rust-v0.121.0]] · Digest
- 2026-04-14 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-04-14-2-context-window-changes-in-v2-1-108|2 Context Window changes in v2.1.108]] · Digest
- 2026-04-14 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-04-14-2-context-window-changes-in-v0-38-0|2 Context Window changes in v0.38.0]] · Digest
- 2026-04-14 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-14-4-context-window-changes-in-v1-0-26|4 Context Window changes in v1.0.26]] · Digest
- 2026-04-11 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-11-3-context-window-changes-in-rust-v0-120-0|3 Context Window changes in rust-v0.120.0]] · Digest
- 2026-04-10 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-04-10-improved-tool-not-available-errors-to-explain-why-and-how-to-proceed-when-the-mo|Improved tool-not-available errors to explain why and how to proceed when the model…]] · Change
- 2026-04-10 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-10-4-context-window-changes-in-rust-v0-119-0|4 Context Window changes in rust-v0.119.0]] · Digest
- 2026-04-09 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-04-09-added-exclude-dynamic-system-prompt-sections-flag-to-print-mode-for-improved-cro|Added --exclude-dynamic-system-prompt-sections flag to print mode for improved…]] · Change
- 2026-04-08 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-04-08-improved-context-low-warning-to-show-as-a-transient-footer-notification-instead|Improved context-low warning to show as a transient footer notification instead…]] · Change
- 2026-04-08 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-04-08-5-context-window-changes-in-v0-37-0|5 Context Window changes in v0.37.0]] · Digest
- 2026-04-06 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-06-slash-command-timeline-entries-now-include-the-command-name-e-g-review-plan-for|Slash command timeline entries now include the command name (e.g., "Review", "Plan")…]] · Change
- 2026-04-04 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-04-04-pro-users-now-see-a-footer-hint-when-returning-to-a-session-after-the-prompt-cac|Pro users now see a footer hint when returning to a session after the prompt cache…]] · Change
- 2026-04-02 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-04-02-2-context-window-changes-in-v2-1-91|2 Context Window changes in v2.1.91]] · Digest
- 2026-04-01 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-04-01-changed-hook-output-over-50k-characters-to-be-saved-to-disk-with-a-file-path-pre|Changed hook output over 50K characters to be saved to disk with a file path…]] · Change
- 2026-04-01 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-04-01-feat-core-cap-jit-context-upward-traversal-at-git-root-by-sandytao520-in-https-g|feat(core): cap JIT context upward traversal at git root]] · Change

**2026-03**

- 2026-03-31 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-31-16286-auth-generalize-external-auth-tokens-for-bearer-only-sources-bolinfest|♯16286 auth: generalize external auth tokens for bearer-only sources @bolinfest]] · Change
- 2026-03-27 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-03-27-3-context-window-changes-in-v2-1-86|3 Context Window changes in v2.1.86]] · Digest
- 2026-03-26 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-03-26-reduced-ui-stutter-when-compaction-triggers-on-large-sessions|Reduced UI stutter when compaction triggers on large sessions]] · Change
- 2026-03-26 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-03-26-2-context-window-changes-in-v2-1-84|2 Context Window changes in v2.1.84]] · Digest
- 2026-03-26 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-03-26-add-repeated-tool-call-loop-detection-to-prevent-infinite-loops-wasting-tokens|Add repeated tool call loop detection to prevent infinite loops wasting tokens]] · Change
- 2026-03-26 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-26-5-context-window-changes-in-rust-v0-117-0|5 Context Window changes in rust-v0.117.0]] · Digest
- 2026-03-25 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-03-25-starting-today-for-chatgpt-plus-pro-and-business-users-long-pastes-are-handled-d|Large pastes are now handled as attachments]] · Change
- 2026-03-24 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-03-24-2-context-window-changes-in-v0-35-0|2 Context Window changes in v0.35.0]] · Digest
- 2026-03-20 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-03-20-changed-plan-mode-to-hide-the-clear-context-option-by-default-restore-with-showc|Changed plan mode to hide the "clear context" option by default…]] · Change
- 2026-03-19 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-03-19-respect-user-configured-context-window-in-litellm-getmodel|Respect user-configured context window in LiteLLM getModel()]] · Change
- 2026-03-19 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-19-14829-stack-3-4-add-current-thread-context-to-realtime-startup-aibrahim-oai|♯14829 stack 3/4 Add current thread context to realtime startup @aibrahim-oai]] · Change
- 2026-03-17 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-17-add-subagentstart-hook-that-fires-when-a-subagent-is-spawned-with-support-for-in|Add subagentStart hook that fires when a subagent is spawned, with support…]] · Change
- 2026-03-16 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-16-2-context-window-changes-in-rust-v0-115-0|2 Context Window changes in rust-v0.115.0]] · Digest
- 2026-03-14 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-03-14-added-postcompact-hook-that-fires-after-compaction-completes|Added PostCompact hook that fires after compaction completes]] · Change
- 2026-03-13 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-13-add-precompact-hook-to-run-commands-before-context-compaction-starts|Add preCompact hook to run commands before context compaction starts]] · Change
- 2026-03-11 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-03-11-improved-the-remote-control-spawn-mode-selection-prompt-with-better-context|Improved the Remote Control spawn mode selection prompt with better context]] · Change
- 2026-03-11 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-11-2-context-window-changes-in-rust-v0-114-0|2 Context Window changes in rust-v0.114.0]] · Digest
- 2026-03-11 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-03-11-feat-cli-invert-context-window-display-to-show-usage-by-keithguerin-in-https-git|feat(cli): invert context window display to show usage]] · Change
- 2026-03-11 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-11-status-line-context-window-percentage-no-longer-inflates-across-turns-by-using-t|Status line context window percentage no longer inflates across turns by using…]] · Change
- 2026-03-10 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-10-4-context-window-changes-in-rust-v0-113-0|4 Context Window changes in rust-v0.113.0]] · Digest
- 2026-03-06 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-06-improve-explore-agent-precision-and-large-repository-support-with-better-context|Improve explore agent precision and large repository support with better context sharing]] · Change
- 2026-03-05 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-03-05-gpt-5-4-brings-together-the-best-of-our-recent-advances-in-reasoning-coding-and|GPT-5.4 Thinking in ChatGPT]] · Change
- 2026-03-05 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-03-05-3-context-window-changes-in-v2-1-69|3 Context Window changes in v2.1.69]] · Digest
- 2026-03-05 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-05-resuming-a-thread-now-preserves-its-stored-git-context-and-keeps-apps-enabled-av|Resuming a thread now preserves its stored git context and keeps apps enabled…]] · Change
- 2026-03-05 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-05-3-context-window-changes-in-rust-v0-110-0|3 Context Window changes in rust-v0.110.0]] · Digest
- 2026-03-05 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-05-session-usage-metrics-requests-tokens-code-changes-are-now-persisted-to-events-j|Session usage metrics (requests, tokens, code changes) are now persisted…]] · Change
- 2026-03-04 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-03-04-2-context-window-changes-in-v3-70-0|2 Context Window changes in v3.70.0]] · Digest
- 2026-03-03 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-03-03-trigger-auto-compaction-on-openrouter-context-overflow-errors|Trigger auto-compaction on OpenRouter context overflow errors]] · Change
- 2026-03-03 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-03-03-2-context-window-changes-in-2-6|2 Context Window changes in 2.6]] · Digest
- 2026-03-02 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-02-12947-feat-add-local-date-timezone-to-turn-environment-context-celia-oai|♯12947 feat: add local date/timezone to turn environment context @celia-oai]] · Change

**2026-02**

- 2026-02-27 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-02-27-resolve-could-not-find-the-file-context-error-in-explain-changes|Resolve "Could not find the file context" error in Explain Changes]] · Change
- 2026-02-27 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-02-27-feat-telemetry-add-context-breakdown-to-api-response-event-by-sandytao520-in-htt|feat(telemetry): Add context breakdown to API response event]] · Change
- 2026-02-25 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-02-25-ad-hoc-text-sources-paste-notes-briefs-or-reference-material-directly-to-capture|Ad-hoc text sources]] · Change
- 2026-02-25 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-02-25-projects-now-make-it-easy-to-build-a-living-knowledge-base-by-adding-sources-whe|Projects now make it easy to build a living knowledge base by adding sources…]] · Change
- 2026-02-25 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-25-5-context-window-changes-in-rust-v0-105-0|5 Context Window changes in rust-v0.105.0]] · Digest
- 2026-02-25 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-02-25-2-context-window-changes-in-v0-30-0|2 Context Window changes in v0.30.0]] · Digest
- 2026-02-24 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-02-24-tool-results-larger-than-50k-characters-are-now-persisted-to-disk-previously-100|Tool results larger than 50K characters are now persisted to disk (previously 100K)]] · Change
- 2026-02-20 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-02-20-chatgpt-now-has-a-total-context-window-length-of-256k-tokens-128k-input-and-128k|Expanded context window for Thinking]] · Change
- 2026-02-20 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-02-20-2-context-window-changes-in-v2-1-50|2 Context Window changes in v2.1.50]] · Digest
- 2026-02-18 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-18-2-context-window-changes-in-rust-v0-104-0|2 Context Window changes in rust-v0.104.0]] · Digest
- 2026-02-18 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-02-18-cli-now-stores-conversation-transcripts-that-the-agent-can-use-as-context|CLI now stores conversation transcripts that the agent can use as context]] · Change
- 2026-02-18 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-02-18-3-context-window-changes-in-v0-29-0|3 Context Window changes in v0.29.0]] · Digest
- 2026-02-17 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-17-4-context-window-changes-in-rust-v0-102-0|4 Context Window changes in rust-v0.102.0]] · Digest
- 2026-02-17 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-02-17-agents-can-now-search-past-conversations-and-use-chat-history-as-context|Agents can now search past conversations and use chat history as context]] · Change
- 2026-02-14 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-14-shell-mode-pastes-raw-text-instead-of-paste-tokens|Shell mode pastes raw text instead of paste tokens]] · Change
- 2026-02-13 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-02-13-attach-up-to-20-files-in-a-single-message-you-can-now-upload-up-to-20-files-at-o|Attach up to 20 files in a single message]] · Change
- 2026-02-13 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-02-13-improved-rename-to-auto-generate-session-name-from-conversation-context-when-cal|Improved /rename to auto-generate session name from conversation context…]] · Change
- 2026-02-12 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-12-3-context-window-changes-in-rust-v0-100-0|3 Context Window changes in rust-v0.100.0]] · Digest
- 2026-02-11 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-11-6-context-window-changes-in-rust-v0-99-0|6 Context Window changes in rust-v0.99.0]] · Digest
- 2026-02-11 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-11-expose-session-context-in-session-list-sdk-response|Expose session context in session.list SDK response]] · Change
- 2026-02-05 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-02-05-2-context-window-changes-in-v2-1-32|2 Context Window changes in v2.1.32]] · Digest
- 2026-02-05 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-05-10692-fix-remote-compaction-estimator-payload-instruction-small-mismatch-charley|♯10692 Fix remote compaction estimator/payload instruction small mismatch @charley-oai]] · Change
- 2026-02-04 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-04-2-context-window-changes-in-rust-v0-95-0|2 Context Window changes in rust-v0.95.0]] · Digest
- 2026-02-03 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-02-03-added-pages-parameter-to-the-read-tool-for-pdfs-allowing-specific-page-ranges-to|Added pages parameter to the Read tool for PDFs, allowing specific page ranges…]] · Change
- 2026-02-02 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-02-2-context-window-changes-in-rust-v0-94-0|2 Context Window changes in rust-v0.94.0]] · Digest

**2026-01**

- 2026-01-31 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-31-6-context-window-changes-in-rust-v0-93-0|6 Context Window changes in rust-v0.93.0]] · Digest
- 2026-01-30 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-01-30-new-model-added-kimi-k2-5-model-to-moonshot-provider-262k-context-image-support|_New model: Added Kimi-K2.5 model to Moonshot provider…]] · Change
- 2026-01-30 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-01-30-new-model-added-kimi-k2-5-model-to-moonshot-provider-262k-context-image-support-53f1f0|_New model: Added Kimi-K2.5 model to Moonshot provider…]] · Change
- 2026-01-30 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-01-30-new-model-added-kimi-k2-5-model-to-moonshot-provider-262k-context-image-support-9b8adb|_New model: Added Kimi-K2.5 model to Moonshot provider…]] · Change
- 2026-01-29 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-29-compaction-messages-show-clearer-command-hints-to-view-checkpoint-summaries|Compaction messages show clearer command hints to view checkpoint summaries]] · Change
- 2026-01-28 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-01-28-feat-core-enhanced-anchored-iterative-context-compression-with-self-verification|feat(core): enhanced anchored iterative context compression with self-verification]] · Change
- 2026-01-27 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-01-27-strip-notebook-cell-outputs-when-extracting-text-content-from-jupyter-notebooks|Strip notebook cell outputs when extracting text content from Jupyter notebooks…]] · Change
- 2026-01-27 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-27-simplify-compaction-timeline-entries|Simplify compaction timeline entries]] · Change
- 2026-01-24 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-24-3-context-window-changes-in-v0-0-394|3 Context Window changes in v0.0.394]] · Digest
- 2026-01-23 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-23-show-conversation-compaction-status-as-timeline-messages-instead-of-header-indic|Show conversation compaction status as timeline messages instead of header indicator]] · Change
- 2026-01-22 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-01-22-agents-can-now-read-pdfs-which-you-can-attach-in-chats-as-context|Agents can now read PDFs, which you can attach in chats as context]] · Change
- 2026-01-22 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-22-preserve-extended-thinking-after-compaction|Preserve extended thinking after compaction]] · Change
- 2026-01-20 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-20-skill-tool-handles-large-directories-without-exceeding-context-limits|Skill tool handles large directories without exceeding context limits]] · Change
- 2026-01-19 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-19-enable-infinite-sessions-with-automatic-long-running-context-management-through|Enable infinite sessions with automatic long-running context management through…]] · Change
- 2026-01-19 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-19-background-compaction-preserves-tool-call-sequences-correctly|Background compaction preserves tool call sequences correctly]] · Change
- 2026-01-16 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-01-16-added-auto-n-syntax-for-configuring-the-mcp-tool-search-auto-enable-threshold-wh|Added auto:N syntax for configuring the MCP tool search auto-enable threshold…]] · Change
- 2026-01-16 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-16-2-context-window-changes-in-rust-v0-87-0|2 Context Window changes in rust-v0.87.0]] · Digest
- 2026-01-14 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-01-14-enabled-mcp-tool-search-auto-mode-by-default-for-all-users-when-mcp-tool-descrip|Enabled MCP tool search auto mode by default for all users]] · Change
- 2026-01-14 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-01-14-2-context-window-changes-in-v0-24-0|2 Context Window changes in v0.24.0]] · Digest
- 2026-01-13 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-01-13-added-context-window-used-percentage-and-context-window-remaining-percentage-fie|Added context_window.used_percentage and context_window.remaining_percentage…]] · Change
- 2026-01-13 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-13-auto-compaction-runs-in-background-without-blocking-the-conversation|Auto-compaction runs in background without blocking the conversation]] · Change
- 2026-01-07 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-01-07-add-core-tool-that-adds-all-context-from-the-core-package-by-jacob314-in-https-g|Add core tool that adds all context from the core package]] · Change
- 2026-01-06 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-06-2-context-window-changes-in-rust-v0-78-0|2 Context Window changes in rust-v0.78.0]] · Digest
- 2026-01-02 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-02-add-auto-compaction-at-95-token-limit-and-compact-command|Add auto-compaction at 95% token limit and /compact command]] · Change

</details>

</details>

<details class="disclosure">
<summary>2025 · 114 entries (Aider 9 · Claude Code 1 · Cline 33 · Codex CLI 21 · Cursor 16 · Gemini CLI 17 · GitHub Copilot CLI 5 · OpenHands 5 · Windsurf 7)</summary>

**2025-12**

- 2025-12-24 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2025-12-24-context-window-indicator|Context Window Indicator]] · Launch
- 2025-12-18 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-12-18-conversation-insights-2efafc|Conversation insights]] · Launch

**2025-11**

- 2025-11-21 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2025-11-21-fast-context|Fast Context]] · Launch
- 2025-11-04 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2025-11-04-cascade-summarization-fix|Cascade Summarization Fix]] · Launch

**2025-09**

- 2025-09-12 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-09-12-cursor-automatically-summarizes-long-conversation-for-you-when-reaching-the-cont|Summarization triggers]] · Launch

**2025-07**

- 2025-07-29 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-07-29-at-the-end-of-a-conversation-you-can-now-see-how-much-of-the-context-window-is-u|View context usage in Chat]] · Launch
- 2025-07-17 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2025-07-17-mentioning-conversations|mentioning conversations]] · Launch
- 2025-07-03 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-07-03-pr-indexing-search|PR indexing & search]] · Launch

**2025-05**

- 2025-05-15 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-05-15-include-your-entire-codebase-in-context|Include your entire codebase in context]] · Launch

**2025-04**

- 2025-04-15 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-04-15-automated-and-improved-rules-15afc6|Automated and improved rules]] · Launch
- 2025-04-15 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-04-15-project-structure-in-context-beta|Project structure in context (Beta)]] · Launch

**2025-03**

- 2025-03-13 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2025-03-13-added-think-tokens-command-to-set-thinking-token-budget-with-support-for-human-r|Added /think-tokens command to set thinking token budget with support…]] · Change

<details class="disclosure">
<summary>Fixes, digests and other changes · 102 (Aider 8 · Claude Code 1 · Cline 33 · Codex CLI 21 · Cursor 9 · Gemini CLI 17 · GitHub Copilot CLI 5 · OpenHands 5 · Windsurf 3)</summary>

**2025-12**

- 2025-12-24 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2025-12-24-multiple-fixes-to-the-model-context-protocol-implementation|Multiple fixes to the Model Context Protocol implementation]] · Change
- 2025-12-19 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2025-12-19-improved-context-command-visualization-with-grouped-skills-and-agents-by-source|Improved /context command visualization with grouped skills and agents by source…]] · Change
- 2025-12-19 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-12-19-add-context-command-to-visualize-token-usage|Add /context command to visualize token usage]] · Change
- 2025-12-18 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-12-18-7935-exec-server-additional-context-for-errors|♯7935 exec-server: additional context for errors]] · Change
- 2025-12-17 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-12-17-added-support-for-dynamic-tool-instructions-that-adapt-based-on-runtime-context|Added support for dynamic tool instructions that adapt based on runtime context…]] · Change
- 2025-12-11 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-12-11-2-context-window-changes-in-v3-41-0|2 Context Window changes in v3.41.0]] · Digest
- 2025-12-09 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-12-09-general-fixes-parallel-tool-call-chat-now-returns-correctly-ghost-snapshot-token|General fixes: parallel tool-call chat now returns correctly, ghost snapshot tokens…]] · Change
- 2025-12-09 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-12-09-feat-core-implement-jit-context-manager-and-setting-by-sandytao520-in-https-gith|feat(core): Implement JIT context manager and setting]] · Change
- 2025-12-04 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-12-04-2-context-window-changes-in-v3-40-0|2 Context Window changes in v3.40.0]] · Digest
- 2025-12-04 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-12-04-3-context-window-changes-in-rust-v0-65-0|3 Context Window changes in rust-v0.65.0]] · Digest
- 2025-12-02 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-12-02-2-context-window-changes-in-v3-39-0|2 Context Window changes in v3.39.0]] · Digest
- 2025-12-02 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-12-02-5-context-window-changes-in-rust-v0-64-0|5 Context Window changes in rust-v0.64.0]] · Digest

**2025-11**

- 2025-11-27 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-11-27-feat-context-add-context-window-error-detection-for-vercel-ai-gateway-by-shaper|feat(context): add context window error detection for vercel ai gateway]] · Change
- 2025-11-21 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-11-21-rules-in-home-folder-cursor-rules-will-be-included-in-context|Rules in home folder (~/.cursor/rules) will be included in context]] · Change
- 2025-11-20 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-11-20-ux-fixes-corrected-reasoning-display-preserved-review-footer-context-after-revie|UX fixes: corrected reasoning display, preserved review footer context after…]] · Change
- 2025-11-19 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-11-19-6-context-window-changes-in-rust-v0-59-0|6 Context Window changes in rust-v0.59.0]] · Digest
- 2025-11-18 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-11-18-feat-bedrock-add-context-window-error-detection-and-retry-handling-by-arafatkatz|feat(bedrock): add context window error detection and retry handling]] · Change
- 2025-11-17 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-11-17-support-adding-images-to-context-via-drag-dropping-and-pasting-paths-to-image-fi|Support adding images to context via drag & dropping and pasting paths to image files]] · Change
- 2025-11-13 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-11-13-reduce-next-gen-model-context-window-anxiety-by-canvrno-in-https-github-com-clin|Reduce next-gen model context window anxiety]] · Change
- 2025-11-13 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-11-13-6597-feat-proxy-context-left-after-compaction-2a417c47a|♯6597 — feat: proxy context left after compaction (2a417c47a)]] · Change
- 2025-11-07 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-11-07-remove-context-percentage-in-footer-by-default-by-abhipatel12-in-https-github-co|Remove context percentage in footer by default]] · Change
- 2025-11-06 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-11-06-use-context-aware-task-manager-for-quick-auth-by-canvrno-in-https-github-com-cli|Use context-aware task manager for quick auth]] · Change
- 2025-11-04 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-11-04-6161-include-reasoning-tokens-in-the-context-window-calculation-6161|♯6161 Include reasoning tokens in the context window calculation (♯6161)]] · Change

**2025-10**

- 2025-10-30 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-10-30-2-context-window-changes-in-rust-v0-52-0|2 Context Window changes in rust-v0.52.0]] · Digest
- 2025-10-29 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-10-29-improved-prompt-ui|Improved Prompt UI]] · Change
- 2025-10-29 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-10-29-pass-whole-extensions-rather-than-just-context-files-by-zbirkenbuel-in-https-git|Pass whole extensions rather than just context files]] · Change
- 2025-10-24 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-10-24-to-conserve-context-window-space-we-ve-limited-the-list-of-tools-available-to-th|To conserve context window space, we've limited the list of tools available…]] · Change
- 2025-10-23 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-10-23-auto-compact-updates-by-0xtoshii-in-https-github-com-cline-cline-pull-6909|auto compact updates]] · Change
- 2025-10-23 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-10-23-auto-compact-at-90-by-aibrahim-oai-in-https-github-com-openai-codex-pull-5292|Auto compact at ~90%]] · Change
- 2025-10-23 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2025-10-23-improvements-to-fast-context-enterprises-can-opt-in-using-the-windsurf-team-sett|Improvements to Fast Context]] · Change
- 2025-10-22 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-10-22-2-context-window-changes-in-v0-10-0|2 Context Window changes in v0.10.0]] · Digest
- 2025-10-16 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-10-16-fixing-issue-where-checkpoint-restore-doesn-t-work-with-auto-compact-by-0xtoshii|fixing issue where checkpoint restore doesn't work with auto-compact]] · Change
- 2025-10-16 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2025-10-16-fast-context-introduced-fast-context-subagent-powered-by-swe-grep-enabling-agent|Fast Context: Introduced Fast Context subagent powered by SWE-grep, enabling…]] · Change
- 2025-10-09 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-10-09-make-context-line-permanent-by-dedrisian-oai-in-https-github-com-openai-codex-pu|Make context line permanent]] · Change
- 2025-10-06 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-10-06-4706-fix-command-output-truncation-that-sometimes-used-too-much-of-the-context-w|♯4706 Fix command output truncation that sometimes used too much of the context window]] · Change
- 2025-10-06 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-10-06-updated-the-context-truncation-message-s-color-from-an-error-color-to-a-warning|Updated the context truncation message's color from an error color to a warning color]] · Change
- 2025-10-03 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-10-03-2-context-window-changes-in-rust-v0-44-0|2 Context Window changes in rust-v0.44.0]] · Digest
- 2025-10-03 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-10-03-added-a-warning-when-conversation-context-approaches-20-remaining-of-the-model-s|Added a warning when conversation context approaches ≤20% remaining of the model's…]] · Change

**2025-09**

- 2025-09-29 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-09-29-disk-ts-replace-uses-of-context-globalstorageuri-with-hostprovider-get-globalsto|disk.ts Replace uses of context.globalStorageUri…]] · Change
- 2025-09-28 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-09-28-tasks-directory-replace-uses-of-context-globalstorageuri-with-hostprovider-get-g|Tasks directory Replace uses of context.globalStorageUri…]] · Change
- 2025-09-25 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-09-25-replace-vscode-context-globalstoragepath-with-hostprovider-globalstoragefspath-b|Replace vscode context.globalStoragePath with HostProvider.globalStorageFsPath]] · Change
- 2025-09-24 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-09-24-2-context-window-changes-in-v0-6-0|2 Context Window changes in v0.6.0]] · Digest
- 2025-09-23 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-09-23-4093-chore-enable-auto-compaction-for-gpt-5-codex-4093|♯4093 chore: enable auto-compaction for gpt-5-codex (♯4093)]] · Change
- 2025-09-18 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-09-18-pass-max-tokens-to-moonshot-provider-by-canvrno-in-https-github-com-cline-cline|Pass max_tokens to moonshot provider]] · Change
- 2025-09-18 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-09-18-3857-make-esc-button-work-when-auto-compaction-3857|♯3857 Make ESC button work when auto-compaction (♯3857)]] · Change
- 2025-09-17 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-09-17-2-context-window-changes-in-v0-5-3|2 Context Window changes in v0.5.3]] · Digest
- 2025-09-15 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-09-15-3-context-window-changes-in-rust-v0-36-0|3 Context Window changes in rust-v0.36.0]] · Digest
- 2025-09-11 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-09-11-added-per-provider-thinking-tokens-configurability|Added per-provider thinking tokens configurability]] · Change
- 2025-09-09 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-09-09-feat-cli-create-base-class-for-handling-tokens-stored-in-files-by-shishu314-in-h|feat(cli) - Create base class for handling tokens stored in files]] · Change
- 2025-09-08 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-09-08-3221-move-token-usage-context-information-to-session-level|♯3221 Move token usage/context information to session level]] · Change
- 2025-09-05 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-09-05-2-context-window-changes-in-rust-v0-30-0|2 Context Window changes in rust-v0.30.0]] · Digest
- 2025-09-04 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-09-04-update-colors-tokens-for-inputer-footer-by-miguelsolorio-in-https-github-com-goo|Update colors tokens for inputer/footer]] · Change

**2025-08**

- 2025-08-29 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-08-29-add-200k-context-window-variant-for-claude-sonnet-4-to-openrouter-and-cline-prov|Add 200k context window variant for Claude Sonnet 4 to OpenRouter and Cline providers]] · Change
- 2025-08-27 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-08-27-2-context-window-changes-in-rust-v0-25-0|2 Context Window changes in rust-v0.25.0]] · Digest
- 2025-08-21 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-08-21-added-telemetry-for-auto-compact-toggle-in-menu-by-0xtoshii-in-https-github-com|added telemetry for auto compact toggle in menu]] · Change
- 2025-08-21 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-08-21-next-gen-context-management-method-switch-by-0xtoshii-in-https-github-com-cline|next gen context management method switch]] · Change
- 2025-08-21 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-08-21-context-usage-is-always-shown-in-the-chat-input|Context usage is always shown in the chat input]] · Change
- 2025-08-20 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-08-20-2-context-window-changes-in-rust-v0-23-0|2 Context Window changes in rust-v0.23.0]] · Digest
- 2025-08-18 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-08-18-5-context-window-changes-in-v0-1-22|5 Context Window changes in v0.1.22]] · Digest
- 2025-08-16 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-08-16-2-context-window-changes-in-v3-25-3|2 Context Window changes in v3.25.3]] · Digest
- 2025-08-15 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-08-15-auto-compact-context-management-by-0xtoshii-in-https-github-com-cline-cline-pull|auto compact - context management]] · Change
- 2025-08-14 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-08-14-6-context-window-changes-in-v0-1-21|6 Context Window changes in v0.1.21]] · Digest
- 2025-08-13 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-08-13-5-context-window-changes-in-v3-24-0|5 Context Window changes in v3.24.0]] · Digest
- 2025-08-13 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2025-08-13-2-context-window-changes-in-0-52-0|2 Context Window changes in 0.52.0]] · Digest
- 2025-08-12 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-08-12-https-github-com-openai-codex-pull-2200-send-prompt-cache-key-for-better-caching|(source link) send prompt cache key for better caching…]] · Change
- 2025-08-12 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-08-12-3-context-window-changes-in-v0-1-19|3 Context Window changes in v0.1.19]] · Digest
- 2025-08-06 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-08-06-admin-api-for-blocklists-block-specific-files-or-directories-from-being-indexed|Admin API for blocklists]] · Change
- 2025-08-06 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-08-06-3-context-window-changes-in-v0-1-18|3 Context Window changes in v0.1.18]] · Digest
- 2025-08-05 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-08-05-3-context-window-changes-in-v0-1-17|3 Context Window changes in v0.1.17]] · Digest
- 2025-08-02 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-08-02-3-context-window-changes-in-v0-1-16|3 Context Window changes in v0.1.16]] · Digest

**2025-07**

- 2025-07-30 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-07-30-2-context-window-changes-in-v0-1-15|2 Context Window changes in v0.1.15]] · Digest
- 2025-07-26 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-07-26-change-the-claude-code-max-output-tokens-by-barreirot-in-https-github-com-cline|Change the CLAUDE_CODE_MAX_OUTPUT_TOKENS]] · Change
- 2025-07-25 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-07-25-2-context-window-changes-in-v0-1-14|2 Context Window changes in v0.1.14]] · Digest
- 2025-07-22 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-07-22-change-available-cerebras-models-modify-context-window-by-arafatkatze-in-https-g|Change available Cerebras models + modify context window]] · Change
- 2025-07-19 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-07-19-2-context-window-changes-in-v0-1-13|2 Context Window changes in v0.1.13]] · Digest

**2025-06**

- 2025-06-27 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2025-06-27-enhanced-thinking-tokens-support-can-now-be-disabled-by-setting-to-0-and-improve|Enhanced thinking tokens support]] · Change
- 2025-06-20 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2025-06-20-2-context-window-changes-in-0-43-0|2 Context Window changes in 0.43.0]] · Digest
- 2025-06-10 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-06-10-prioritize-active-files-open-tabs-at-the-top-of-the-file-context-menu-when-using|Prioritize active files (open tabs) at the top of the file context menu when using…]] · Change

**2025-05**

- 2025-05-30 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2025-05-30-2-context-window-changes-in-v0-84-0|2 Context Window changes in v0.84.0]] · Digest
- 2025-05-21 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-05-21-add-support-for-gemini-2-5-flash-preview-05-20-model-to-vertex-ai-provider-with|Add support for Gemini 2.5 Flash Preview 05-20 model to Vertex AI provider…]] · Change
- 2025-05-21 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-05-21-add-support-for-gemini-2-5-flash-preview-05-20-model-to-vertex-ai-provider-with-d2d830|Add support for Gemini 2.5 Flash Preview 05-20 model to Vertex AI provider…]] · Change
- 2025-05-09 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2025-05-09-2-context-window-changes-in-v0-83-0|2 Context Window changes in v0.83.0]] · Digest

**2025-04**

- 2025-04-14 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-04-14-2-context-window-changes-in-v3-12-2|2 Context Window changes in v3.12.2]] · Digest
- 2025-04-13 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-04-13-use-improved-context-management|Use improved context management]] · Change
- 2025-04-10 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2025-04-10-display-microagent-context-in-the-ui-by-xingyaoww-in-https-github-com-all-hands|Display microagent context in the UI]] · Change
- 2025-04-08 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-04-08-make-context-shortening-more-intelligent-when-model-hits-context-window-now-old|Make context shortening more intelligent when model hits context window–now old file…]] · Change

**2025-03**

- 2025-03-25 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2025-03-25-added-a-new-context-command-that-automatically-identifies-which-files-need-to-be|Added a new /context command that automatically identifies which files need…]] · Change
- 2025-03-23 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-03-23-add-add-to-cline-as-an-option-when-you-right-click-selected-text-in-a-file-or-th|Add Add to Cline as an option when you right-click selected text in a file…]] · Change
- 2025-03-23 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-03-23-added-input-token-count-for-chat-messages-click-the-three-dots-to-view-we-re-con|Added input token count for chat messages (click the three dots to view)]] · Change
- 2025-03-15 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-03-15-prevent-cline-from-reading-extremely-large-files-into-context-that-would-overloa|Prevent Cline from reading extremely large files into context that would overload…]] · Change
- 2025-03-13 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2025-03-13-2-context-window-changes-in-v0-77-0|2 Context Window changes in v0.77.0]] · Digest
- 2025-03-07 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2025-03-07-2-context-window-changes-in-0-28-0|2 Context Window changes in 0.28.0]] · Digest

**2025-02**

- 2025-02-24 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2025-02-24-by-default-openhands-truncates-history-by-half-when-it-hits-llm-context-limit-by|By default, OpenHands truncates history by half when it hits LLM context limit]] · Change
- 2025-02-19 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-02-19-new-advanced-setting-to-disable-the-browser-tool-improved-support-for-aws-bedroc|New advanced setting to disable the browser tool, improved support for AWS Bedrock…]] · Change
- 2025-02-19 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-02-19-ui-refresh-phase-one-of-a-fresh-coat-of-paint-with-new-default-cursor-themes-des|UI refresh: Phase one of a fresh coat of paint with new default Cursor themes…]] · Change
- 2025-02-06 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2025-02-06-dynamically-changes-the-ollama-context-window-to-hold-the-current-chat|Dynamically changes the Ollama context window to hold the current chat]] · Change

**2025-01**

- 2025-01-31 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2025-01-31-improved-handling-of-context-window-size-limits-with-better-messaging-and-ollama|Improved handling of context window size limits, with better messaging…]] · Change
- 2025-01-30 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-01-30-new-context-window-progress-bar-in-the-task-header-to-understand-increased-cost|New Context Window progress bar in the task header to understand increased…]] · Change
- 2025-01-23 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-01-23-fusion-model-we-ve-trained-a-new-tab-model-that-is-substantially-better-at-jumps|Fusion Model: We've trained a new Tab Model that is substantially better at jumps…]] · Change
- 2025-01-23 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-01-23-summarize-previous-composers-when-conversations-grow-too-long-you-can-start-a-ne|Summarize Previous Composers]] · Change
- 2025-01-23 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-01-23-optional-long-context-when-tagging-long-files-users-have-the-option-to-request-a|Optional Long Context]] · Change
- 2025-01-10 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2025-01-10-increased-max-chat-history-tokens-limit-from-4k-to-8k|Increased max chat history tokens limit from 4k to 8k]] · Change

</details>

</details>

<details class="disclosure">
<summary>2024 · 25 entries (Aider 10 · Cline 6 · Cursor 6 · OpenHands 3)</summary>

**2024-12**

- 2024-12-18 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2024-12-18-you-can-now-specify-custom-instructions-for-your-project-by-adding-a-root-level|Specify custom instructions for your project by adding a root-level .clinerules file]] · Change

**2024-09**

- 2024-09-19 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2024-09-19-you-can-now-use-in-the-textarea-to-add-context|Use @ in the textarea to add context!]] · Change

<details class="disclosure">
<summary>Fixes, digests and other changes · 23 (Aider 10 · Cline 4 · Cursor 6 · OpenHands 3)</summary>

**2024-12**

- 2024-12-13 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-12-13-copy-context-instructions-now-takes-optional-instructions-when-copying-code-cont|/copy-context instructions now takes optional "instructions" when copying code…]] · Change
- 2024-12-10 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-12-10-new-copy-context-command|New /copy-context command]] · Change

**2024-11**

- 2024-11-26 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-11-26-ollama-models-now-default-to-an-8k-context-window|Ollama models now default to an 8k context window]] · Change
- 2024-11-24 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2024-11-24-early-version-of-an-agent-in-composer-that-can-pick-its-own-context-and-use-the-1228de|Early version of an agent in composer that can pick its own context and use the terminal]] · Change
- 2024-11-15 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2024-11-15-truncate-agent-history-when-context-window-is-exceeded-by-enyst-in-https-github|Truncate agent history when context window is exceeded]] · Change
- 2024-11-01 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-11-01-save-fname-command-will-make-a-file-of-add-and-read-only-commands-that-recreate|/save fname command will make a file of /add and /read-only commands…]] · Change

**2024-10**

- 2024-10-17 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2024-10-17-display-in-the-logs-the-prompt-cache-hit-or-miss-for-deepseek-chat-by-enyst-in-h|Display in the logs the prompt cache hit or miss for Deepseek Chat]] · Change
- 2024-10-09 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2024-10-09-composer-now-only-applies-files-that-are-in-context-to-prevent-hallucinations|Composer now only applies files that are in context to prevent hallucinations]] · Change

**2024-09**

- 2024-09-21 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-09-21-improvements-to-prompt-cache-chunking-strategy|Improvements to prompt cache chunking strategy]] · Change

**2024-08**

- 2024-08-27 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-08-27-keep-your-prompt-cache-from-expiring-https-aider-chat-docs-usage-caching-html-pr|Keep your prompt cache…]] · Change
- 2024-08-26 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2024-08-26-implement-sliding-window-context-management-to-keep-tasks-going-past-200k-tokens|Implement sliding window context management to keep tasks going past 200k tokens]] · Change
- 2024-08-22 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2024-08-22-we-ve-also-trained-a-new-cursor-tab-model-that-s-smarter-and-more-context-aware-56db10|We've also trained a new Cursor Tab model that's smarter and more context-aware]] · Change
- 2024-08-13 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-08-13-bug-fix-for-chat-history-size-in-tokens|Bug fix for chat history size in /tokens]] · Change
- 2024-08-10 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-08-10-add-read-only-files-to-the-chat-context-with-read-and-read-including-from-outsid|Add read-only files to the chat context with /read and --read, including…]] · Change

**2024-07**

- 2024-07-30 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2024-07-30-export-tasks-to-markdown-files-useful-as-context-for-future-tasks|Export tasks to markdown files (useful as context for future tasks)]] · Change
- 2024-07-28 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2024-07-28-updated-max-output-tokens-to-8192-so-less-lazy-coding-rest-of-code-here|Updated max output tokens to 8192 so less lazy coding (// rest of code here...)]] · Change
- 2024-07-28 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2024-07-28-claude-now-has-context-about-vscode-s-visible-editors-and-opened-tabs|Claude now has context about vscode's visible editors and opened tabs]] · Change
- 2024-07-27 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2024-07-27-fix-colima-use-a-docker-context-specific-to-runner-prevent-duplicate-start-by-to|(fix) colima: use a docker context specific to runner; prevent duplicate start]] · Change

**2024-06**

- 2024-06-24 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-06-24-improved-error-info-for-token-limit-errors|Improved error info for token limit errors]] · Change
- 2024-06-17 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-06-17-2-context-window-changes-in-v0-38-0|2 Context Window changes in v0.38.0]] · Digest
- 2024-06-08 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2024-06-08-adds-context-pills-to-chat-messages-so-you-can-see-what-will-be-was-used-a324a3|Adds context pills to chat messages, so you can see what will be/was used]] · Change

**2024-04**

- 2024-04-12 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2024-04-12-cursorrules-you-can-write-down-repo-level-rules-for-the-ai-by-creating-a-cursorr|.cursorrules: You can write down repo-level rules for the AI by creating…]] · Change
- 2024-04-01 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2024-04-01-long-context-chat-beta-this-is-a-new-experimental-feature-that-lets-you-talk-wit|Long Context Chat (Beta)]] · Change

</details>

</details>

<details class="disclosure">
<summary>2023 · 26 entries (Aider 7 · ChatGPT 1 · Cursor 18)</summary>

**2023-11**

- 2023-11-24 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2023-11-24-you-can-now-folder-in-the-chat-to-chat-with-a-folder-let-us-know-what-you-think|@folder]] · Change

**2023-09**

- 2023-09-08 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2023-09-08-long-files-in-chat|Long files in chat]] · Launch

**2023-06**

- 2023-06-06 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2023-06-06-codebase-context-v1-bd6ee5|Codebase Context v1]] · Launch

<details class="disclosure">
<summary>Fixes, digests and other changes · 23 (Aider 7 · ChatGPT 1 · Cursor 15)</summary>

**2023-11**

- 2023-11-30 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2023-11-30-better-context-chat-in-particular-followups-are-now-smarter|Better context chat: in particular, followups are now smarter!]] · Change
- 2023-11-27 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2023-11-27-folders-you-can-now-use-the-symbol-to-reference-specific-folders-we-ll-try-to-pi|@ folders: You can now use the @ symbol to reference specific folders!]] · Change
- 2023-11-21 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2023-11-21-integrates-gpt-v-into-chat-for-the-editor-this-means-you-can-take-screenshots-im|GPT-V Support]] · Change
- 2023-11-10 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2023-11-10-copilot-beta-this-is-an-add-on-to-copilot-that-suggests-diffs-around-your-cursor|Copilot++ (beta): this is an "add-on" to Copilot that suggests diffs around…]] · Change
- 2023-11-07 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2023-11-07-2-context-window-changes-in-v0-17-0|2 Context Window changes in v0.17.0]] · Digest

**2023-09**

- 2023-09-10 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2023-09-10-ask-a-question-about-an-edit-that-the-model-with-option-enter-or-bring-in-contex|Quick question and @chat in cmd+k]] · Change

**2023-08**

- 2023-08-30 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2023-08-30-for-with-codebase-chats-you-can-now-see-the-codebase-context-that-cursor-shows-g|For "with codebase" chats, you can now see the codebase context that Cursor shows GPT-4]] · Change
- 2023-08-26 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2023-08-26-have-the-advanced-context-button-show-up-for-non-git-repos|Advanced Button]] · Change
- 2023-08-22 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2023-08-22-follow-up-chat-messages-to-with-codebase-will-keep-the-codebase-context|Follow-up chat messages to "with codebase" will keep the codebase context]] · Change
- 2023-08-22 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2023-08-22-if-you-reference-a-long-file-that-will-be-cutoff-by-the-context-limit-you-ll-be|If you @ reference a long file that will be cutoff by the context limit, you'll…]] · Change
- 2023-08-08 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2023-08-08-automatically-summarize-chat-history-to-avoid-exhausting-context-window|Automatically summarize chat history to avoid exhausting context window]] · Change
- 2023-08-02 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2023-08-02-automatically-summarize-chat-history-to-avoid-exhausting-context-window|Automatically summarize chat history to avoid exhausting context window]] · Change

**2023-07**

- 2023-07-19 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2023-07-19-advanced-context-controls-only-show-up-if-you-have-indexed-your-codebase|Advanced context controls only show up if you have indexed your codebase]] · Change
- 2023-07-19 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2023-07-19-more-control-of-context-building-abilities-for-codebase-wide-chat|More control of context building abilities for codebase-wide chat]] · Change

**2023-06**

- 2023-06-26 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2023-06-26-graceful-handling-of-context-window-exhaustion-including-helpful-tips|Graceful handling of context window exhaustion, including helpful tips]] · Change
- 2023-06-26 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2023-06-26-graceful-handling-of-context-window-exhaustion-including-helpful-tips-d31722|Graceful handling of context window exhaustion, including helpful tips]] · Change
- 2023-06-25 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2023-06-25-graceful-handling-of-context-window-exhaustion-including-helpful-tips|Graceful handling of context window exhaustion, including helpful tips]] · Change
- 2023-06-07 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2023-06-07-2-context-window-changes-in-v0-5-0|2 Context Window changes in v0.5.0]] · Digest
- 2023-06-06 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2023-06-06-we-ve-improved-codebase-context|Cursor improves codebase context!]] · Change
- 2023-06-06 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2023-06-06-following-this-you-ll-be-able-to-see-an-improved-version-of-codebase-context-in|Following this, you'll be able to see an improved version of codebase context…]] · Change

**2023-05**

- 2023-05-17 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2023-05-17-better-jupyter-support|Better Jupyter Support]] · Change
- 2023-05-12 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2023-05-12-for-more-information-on-our-rollout-process-please-check-out-the-article-here-in|For more information on our rollout process, please check out the article here]] · Change
- 2023-05-04 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2 Context Window changes in 0.2.9]] · Digest

</details>

</details>

</div>
<!-- chronolog:end -->