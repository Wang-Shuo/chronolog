---
created: '2023-04-16'
date: '2026-11-06'
description: 'Research question: which safeguards and privacy controls do the tracked
  products add, and for whom?'
machine_hash: d2684b891b56be17c9773dc84d19e36fd1a9402ff67e7a7d7ef06a3d8051638a
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
theme: safety-privacy
title: Safety and Privacy
---

<!-- chronolog:begin region="header" -->
# Safety and Privacy

462 tracked changes across Aider, ChatGPT, Claude Code, Cline, Codex CLI, Cursor, Gemini CLI, GitHub Copilot CLI, OpenHands and Windsurf · 2023-04-16 → 2026-11-06 · Codex CLI averages 8.0 cards per release, Gemini CLI 7.5, Claude Code 7.0, GitHub Copilot CLI 6.3, Cursor 4.0, OpenHands 3.8, Aider 3.7, Cline 3.0, Windsurf 2.6, ChatGPT 1.7
<!-- chronolog:end -->

## Research summary
<!-- chronolog:begin region="narrative" -->
**Research question: which safeguards and privacy controls do the tracked products add, and for whom?**

ChatGPT's [2023-08-28 Enterprise launch](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#introducing-chatgpt-enterprise) ([[Releases/ChatGPT/chatgpt-2023-08-28-introducing-chatgpt-enterprise-eb7127e6|archived]]) offers enterprise-grade security and privacy. The [2025-09-29 note](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#parental-controls) ([[Releases/ChatGPT/chatgpt-2025-09-29-parental-controls-8b95b69a|archived]]) rolls out parental controls globally, with teen accounts connected to a parent's account, and the [2026-01-20 note](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#rolling-out-age-prediction) ([[Releases/ChatGPT/chatgpt-2026-01-20-rolling-out-age-prediction-2382655a|archived]]) adds an age prediction model on consumer plans that estimates whether an account likely belongs to someone under 18. [Lockdown Mode on 2026-06-04](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#lockdown-mode-is-now-available-to-all-logged-in-users) ([[Releases/ChatGPT/chatgpt-2026-06-04-lockdown-mode-is-now-available-to-all-logged-in-users-f7dcb357|archived]]) becomes available to all logged-in users as an opt-in setting that limits web and external-service access to reduce the risk of data exfiltration from prompt injection, and the [2026-09-21 Privacy Center](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#privacy-center-in-chatgpt) ([[Releases/ChatGPT/chatgpt-2026-09-21-privacy-center-in-chatgpt-ecef9fba|archived]]) gathers information about chat privacy, memory, data use, connected apps and account security for Free, Go, Plus and Pro users.

Cursor's [2023-04-16 release](https://cursor.com/changelog/0-2-4) ([[Releases/Cursor/cursor-2023-04-16-0-2-4-https-cursor-com-changelog-0-2-4-1ed55ed8|archived]]) adds Ghost mode for opting out of storing any kind of data on Cursor's servers. The [2025-09-29 release](https://cursor.com/changelog/1-7) ([[Releases/Cursor/cursor-2025-09-29-1-7-https-cursor-com-changelog-1-7-0a03c0ae|archived]]) runs non-allowlisted commands in a sandbox with read/write access to the workspace and no internet access, which [Cursor 2.0 on 2025-10-29](https://cursor.com/changelog/2-0) ([[Releases/Cursor/cursor-2025-10-29-2-0-https-cursor-com-changelog-2-0-66a8e76e|archived]]) makes the default for agent commands on macOS, and the [2026-02-17 release](https://cursor.com/changelog/2-5) ([[Releases/Cursor/cursor-2026-02-17-2-5-https-cursor-com-changelog-2-5-82892320|archived]]) adds granular network and filesystem access controls to the sandbox. The [2026-04-30 release](https://cursor.com/changelog/04-30-26) ([[Releases/Cursor/cursor-2026-04-30-cursor-security-review-https-cursor-com-changelog-04-30-26-640898b1|archived]]) adds a Security Reviewer, in beta for Teams and Enterprise, that checks every pull request for security vulnerabilities, privacy and data-handling risks and prompt injection.

Claude Code's [v2.1.83 on 2026-03-25](https://github.com/anthropics/claude-code/releases/tag/v2.1.83) ([[Releases/Claude Code/claude-code-2026-03-25-v2-1-83-github-301019202-ba6a8317|archived]]) adds a setting that strips Anthropic and cloud-provider credentials from subprocess environments, and [v2.1.136 on 2026-05-08](https://github.com/anthropics/claude-code/releases/tag/v2.1.136) ([[Releases/Claude Code/claude-code-2026-05-08-v2-1-136-github-319609716-58f21368|archived]]) adds auto mode classifier rules that block actions unconditionally. [v2.1.187 on 2026-06-23](https://github.com/anthropics/claude-code/releases/tag/v2.1.187) ([[Releases/Claude Code/claude-code-2026-06-23-v2-1-187-github-343665388-744f9775|archived]]) blocks sandboxed commands from reading credential files and secret environment variables, [v2.1.200 on 2026-07-03](https://github.com/anthropics/claude-code/releases/tag/v2.1.200) ([[Releases/Claude Code/claude-code-2026-07-03-v2-1-200-github-348415228-64d6d68d|archived]]) renames the “default” permission mode to “Manual”, and [v2.1.284 on 2026-09-28](https://github.com/anthropics/claude-code/releases/tag/v2.1.284) ([[Releases/Claude Code/claude-code-2026-09-28-v2-1-284-github-398457074-cbb49e49|archived]]) starts interactive terminal and VS Code sessions in auto mode when no permission mode is configured, on every plan and provider.

**Uncertainty and scope:** this editorial summary covers ChatGPT, Claude Code and Cursor; the timeline includes all tracked products and Claude Code coverage starts on 2025-12-19; the controls serve different users, from families and workspace admins to developers running agents, and rollouts vary by plan and region, so the announcements neither measure how well a safeguard works nor compare protection across products.
<!-- chronolog:end -->

## Key moments
<!-- chronolog:begin region="moments" -->
Selected automatically from launches and standalone announcements.

| Quarter | Aider | ChatGPT | Claude Code | Cline | Codex CLI | Cursor | Gemini CLI | GitHub Copilot CLI | OpenHands | Windsurf |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **First in archive** | <time datetime="2023-07-24">2023-07-24</time> [[Changes/Aider/2023-07-24-encourage-gpt-to-use-language-like-add-files-to-the-chat-to-ask-users-for-permis\|Encourage GPT to use language like "add files to the chat" to ask users…]] | <time datetime="2023-08-28">2023-08-28</time> [[Changes/ChatGPT/2023-08-28-today-we-re-launching-chatgpt-enterprise-which-offers-enterprise-grade-security-4958cf\|Introducing ChatGPT Enterprise]] | <time datetime="2026-01-09">2026-01-09</time> [[Changes/Claude Code/2026-01-09-2-safety-and-privacy-changes-in-v2-1-2\|2 Safety and Privacy changes in v2.1.2]] | <time datetime="2024-12-18">2024-12-18</time> [[Changes/Cline/2024-12-18-cline-s-most-requested-feature-is-here-you-can-now-let-cline-work-more-autonomou\|Cline's most requested feature is here 🎉 You can now let Cline work more…]] | <time datetime="2025-07-08">2025-07-08</time> [[Changes/Codex CLI/2025-07-08-adds-support-for-a-sandbox-flag-and-makes-some-breaking-changes-to-config-toml-a\|Adds support for a --sandbox flag and makes some breaking changes to config.toml…]] | <time datetime="2023-04-16">2023-04-16</time> [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers\|Ghost mode for opting out of storing any kind of data on our servers]] | <time datetime="2025-07-01">2025-07-01</time> [[Changes/Gemini CLI/2025-07-01-esc-to-exit-privacy-screen-in-error-state-by-scidomino-in-https-github-com-googl\|Esc to exit privacy screen in error state]] | <time datetime="2025-09-26">2025-09-26</time> [[Changes/GitHub Copilot CLI/2025-09-26-improved-the-error-message-received-when-using-a-pat-that-is-missing-the-copilot\|Improved the error message received when using a PAT that is missing…]] | <time datetime="2024-06-04">2024-06-04</time> [[Changes/OpenHands/2024-06-04-2-safety-and-privacy-changes-in-0-6-1\|2 Safety and Privacy changes in 0.6.1]] | <time datetime="2026-09-10">2026-09-10</time> [[Changes/Windsurf/2026-09-10-devin-cloud\|Devin Cloud]] |
| 2026 Q3 | · | <time datetime="2026-09-25">2026-09-25</time> [[Changes/ChatGPT/2026-09-25-we-re-introducing-security-history-a-new-way-to-review-recent-security-activity-6f32cc\|Security history in ChatGPT]] | · | · | · | <time datetime="2026-09-23">2026-09-23</time> [[Changes/Cursor/2026-09-23-today-we-re-launching-two-cursor-bots-for-the-last-mile-of-shipping-code-rollout-af394f\|Cursor launches two Cursor bots for the last mile of shipping code]] | · | · | · | <time datetime="2026-09-10">2026-09-10</time> [[Changes/Windsurf/2026-09-10-devin-cloud\|Devin Cloud]] |
| 2026 Q2 | · | <time datetime="2026-06-04">2026-06-04</time> [[Changes/ChatGPT/2026-06-04-lockdown-mode-is-now-available-to-all-logged-in-users-across-account-types-and-w\|Lockdown Mode is now available to all logged-in users]] | <time datetime="2026-04-16">2026-04-16</time> [[Changes/Claude Code/2026-04-16-added-less-permission-prompts-skill-scans-transcripts-for-common-read-only-bash\|Added /less-permission-prompts skill]] | · | · | <time datetime="2026-06-10">2026-06-10</time> [[Changes/Cursor/2026-06-10-run-bugbot-before-you-push-3e5964\|Run Bugbot before you push]]<br><time datetime="2026-06-04">2026-06-04</time> [[Changes/Cursor/2026-06-04-custom-tools-056918\|Custom tools]]<br><time datetime="2026-05-13">2026-05-13</time> [[Changes/Cursor/2026-05-13-environment-governance-and-security-controls\|Environment governance and security controls]]<br><time datetime="2026-04-30">2026-04-30</time> [[Changes/Cursor/2026-04-30-security-reviewer-checks-every-pr-for-security-vulnerabilities-auth-regressions\|Security Reviewer]] | · | <time datetime="2026-04-27">2026-04-27</time> [[Changes/GitHub Copilot CLI/2026-04-27-location-based-permission-persistence-is-now-enabled-by-default-so-approvals-car\|Location-based permission persistence is now enabled by default, so approvals carry…]] | · | · |
| 2026 Q1 | · | · | · | · | · | <time datetime="2026-02-17">2026-02-17</time> [[Changes/Cursor/2026-02-17-sandbox-network-access-controls\|Sandbox network access controls]] | · | · | <time datetime="2026-03-30">2026-03-30</time> [[Changes/OpenHands/2026-03-30-added-clear-command-for-v1-conversations-typing-clear-in-the-chat-creates-a-new\|Added /clear command for V1 conversations]] | · |
| 2025 Q4 | · | · | archive begins <time datetime="2025-12-19">2025-12-19</time> | · | · | <time datetime="2025-10-29">2025-10-29</time> [[Changes/Cursor/2025-10-29-sandboxed-terminals-ga\|Sandboxed Terminals (GA)]] | · | · | · | · |
| 2025 Q3 | · | · | <span class="not-archived">not archived</span> | · | · | <time datetime="2025-09-29">2025-09-29</time> [[Changes/Cursor/2025-09-29-sandboxed-terminals\|Sandboxed terminals]] | · | archive begins <time datetime="2025-09-26">2025-09-26</time> | · | · |
| 2023 Q4 → 2025 Q2 | · | · | <span class="not-archived">not archived</span> | archive begins <time datetime="2024-07-28">2024-07-28</time> | archive begins <time datetime="2025-06-30">2025-06-30</time> | · | archive begins <time datetime="2025-06-28">2025-06-28</time> | <span class="not-archived">not archived</span> | archive begins <time datetime="2024-06-04">2024-06-04</time> | archive begins <time datetime="2025-04-02">2025-04-02</time> |
| 2023 Q3 | · | <time datetime="2023-08-28">2023-08-28</time> [[Changes/ChatGPT/2023-08-28-today-we-re-launching-chatgpt-enterprise-which-offers-enterprise-grade-security-4958cf\|Introducing ChatGPT Enterprise]] | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> |

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
<summary>2026 · 366 entries (ChatGPT 10 · Claude Code 149 · Cline 8 · Codex CLI 76 · Cursor 19 · Gemini CLI 26 · GitHub Copilot CLI 64 · OpenHands 12 · Windsurf 2)</summary>

**2026-09**

- 2026-09-25 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-09-25-we-re-introducing-security-history-a-new-way-to-review-recent-security-activity-6f32cc|Security history in ChatGPT]] · Launch
- 2026-09-23 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-09-23-today-we-re-launching-two-cursor-bots-for-the-last-mile-of-shipping-code-rollout-af394f|Cursor launches two Cursor bots for the last mile of shipping code]] · Launch
- 2026-09-23 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-09-23-security-review|Security Review]] · Launch
- 2026-09-23 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-09-23-findings|Findings]] · Launch
- 2026-09-10 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2026-09-10-devin-cloud|Devin Cloud]] · Launch

**2026-06**

- 2026-06-10 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-06-10-run-bugbot-before-you-push-3e5964|Run Bugbot before you push]] · Launch
- 2026-06-04 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-06-04-lockdown-mode-is-now-available-to-all-logged-in-users-across-account-types-and-w|Lockdown Mode is now available to all logged-in users]] · Launch
- 2026-06-04 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-06-04-custom-tools-056918|Custom tools]] · Launch

**2026-05**

- 2026-05-13 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-05-13-environment-governance-and-security-controls|Environment governance and security controls]] · Launch

**2026-04**

- 2026-04-30 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-04-30-security-reviewer-checks-every-pr-for-security-vulnerabilities-auth-regressions|Security Reviewer]] · Launch
- 2026-04-30 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-04-30-vulnerability-scanner-b19b70|Vulnerability Scanner]] · Launch
- 2026-04-27 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-27-location-based-permission-persistence-is-now-enabled-by-default-so-approvals-car|Location-based permission persistence is now enabled by default, so approvals carry…]] · Change
- 2026-04-16 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-04-16-added-less-permission-prompts-skill-scans-transcripts-for-common-read-only-bash|Added /less-permission-prompts skill]] · Change

**2026-03**

- 2026-03-30 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-03-30-added-clear-command-for-v1-conversations-typing-clear-in-the-chat-creates-a-new|Added /clear command for V1 conversations]] · Change

**2026-02**

- 2026-02-17 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-02-17-sandbox-network-access-controls|Sandbox network access controls]] · Launch

<details class="disclosure">
<summary>Fixes, digests and other changes · 351 (ChatGPT 8 · Claude Code 148 · Cline 8 · Codex CLI 76 · Cursor 10 · Gemini CLI 26 · GitHub Copilot CLI 63 · OpenHands 11 · Windsurf 1)</summary>

**2026-11**

- 2026-11-06 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-11-06-57985-skip-read-only-volume-root-expansion-in-the-mxc-sandbox-iceweasel-oai|♯57985 Skip read-only volume-root expansion in the MXC sandbox @iceweasel-oai]] · Change
- 2026-11-06 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-11-06-34-safety-and-privacy-changes-in-v1-0-106|34 Safety and Privacy changes in v1.0.106]] · Digest
- 2026-11-04 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-11-04-fix-acp-include-mcp-server-and-tool-metadata-in-permission-requests-by-duvanka-p|fix(acp): include MCP server and tool metadata in permission requests]] · Change

**2026-10**

- 2026-10-30 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-30-10-safety-and-privacy-changes-in-v2-1-314|10 Safety and Privacy changes in v2.1.314]] · Digest
- 2026-10-29 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-29-10-safety-and-privacy-changes-in-rust-v0-166-0|10 Safety and Privacy changes in rust-v0.166.0]] · Digest
- 2026-10-28 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-10-28-texting-your-dot-is-starting-to-roll-out-in-beta-to-pro-users-in-the-u-s|Texting your dot]] · Change
- 2026-10-27 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-27-changed-claude-code-to-stop-sending-the-claude-code-safety-event-opentelemetry-e|Changed Claude Code to stop sending the claude_code.safety_event OpenTelemetry event]] · Change
- 2026-10-27 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-27-3-safety-and-privacy-changes-in-rust-v0-165-0|3 Safety and Privacy changes in rust-v0.165.0]] · Digest
- 2026-10-27 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-10-27-fix-ci-remove-unsupported-members-permission-in-unassign-inactive-assignees-work|fix(ci): remove unsupported members permission in unassign-inactive-assignees workflow]] · Change
- 2026-10-27 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-10-27-feat-sidebar-start-a-new-conversation-in-the-row-s-sandbox-ohe-3689-by-hieptl-in|feat(sidebar): start a new conversation in the row's sandbox (OHE-3689)]] · Change
- 2026-10-26 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-26-changed-startup-warnings-about-permission-rules-in-settings-files-to-show-once-p|Changed startup warnings about permission rules in settings files to show once per…]] · Change
- 2026-10-26 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-10-26-starting-or-resuming-a-cloud-sandbox-shows-a-progress-card-with-the-repo-branch|Starting or resuming a cloud sandbox shows a progress card with the repo, branch…]] · Change
- 2026-10-23 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-23-4-safety-and-privacy-changes-in-v2-1-310|4 Safety and Privacy changes in v2.1.310]] · Digest
- 2026-10-23 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-23-15-safety-and-privacy-changes-in-rust-v0-164-0|15 Safety and Privacy changes in rust-v0.164.0]] · Digest
- 2026-10-23 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2026-10-23-electron-42-11-16-and-node-js-24-22-1-for-the-remote-server-with-the-october-202|Electron 42.11.16 and Node.js 24.22.1 for the remote server, with the October 2026…]] · Change
- 2026-10-22 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-22-8-safety-and-privacy-changes-in-v2-1-309|8 Safety and Privacy changes in v2.1.309]] · Digest
- 2026-10-22 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-22-3-safety-and-privacy-changes-in-v1-0-103|3 Safety and Privacy changes in v1.0.103]] · Digest
- 2026-10-21 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-21-added-the-claude-code-safety-event-opentelemetry-event-for-each-tool-call-a-perm|Added the claude_code.safety_event OpenTelemetry event for each tool call…]] · Change
- 2026-10-21 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-21-subagents-honor-custom-and-mcp-tool-approvals-avoiding-duplicate-permission-prom|Subagents honor custom and MCP tool approvals, avoiding duplicate permission prompts…]] · Change
- 2026-10-20 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-20-3-safety-and-privacy-changes-in-v2-1-305|3 Safety and Privacy changes in v2.1.305]] · Digest
- 2026-10-20 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-20-permission-approval-prompts-explain-escalation-causes-and-show-a-request-specifi|Permission approval prompts explain escalation causes and show a request-specific…]] · Change
- 2026-10-19 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-19-added-decider-person-to-a-mod-s-tool-check-answer-only-the-permission-dialog-or|Added decider: "person" to a mod's tool.check answer: only the permission dialog…]] · Change
- 2026-10-19 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-19-6-safety-and-privacy-changes-in-v1-0-100|6 Safety and Privacy changes in v1.0.100]] · Digest
- 2026-10-19 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-10-19-fix-theme-make-consent-backend-scope-readable-by-enyst-in-https-github-com-openh|fix(theme): make consent backend scope readable]] · Change
- 2026-10-16 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-16-2-safety-and-privacy-changes-in-v2-1-302|2 Safety and Privacy changes in v2.1.302]] · Digest
- 2026-10-16 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-10-16-cline-cloud-sessions-rolling-out-gradually-run-a-task-in-a-hosted-sandbox-on-a-g|Cline Cloud sessions, rolling out gradually]] · Change
- 2026-10-15 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-15-5-safety-and-privacy-changes-in-v2-1-301|5 Safety and Privacy changes in v2.1.301]] · Digest
- 2026-10-15 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-15-18-safety-and-privacy-changes-in-rust-v0-163-0|18 Safety and Privacy changes in rust-v0.163.0]] · Digest
- 2026-10-14 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-14-2-safety-and-privacy-changes-in-v2-1-300|2 Safety and Privacy changes in v2.1.300]] · Digest
- 2026-10-14 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-14-6-safety-and-privacy-changes-in-v2-1-299|6 Safety and Privacy changes in v2.1.299]] · Digest
- 2026-10-14 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-14-resuming-a-session-now-respects-abandoned-pending-permission-work-and-continues|Resuming a session now respects abandoned pending-permission work and continues only…]] · Change
- 2026-10-13 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-10-13-origin-now-integrates-with-over-20-apps-for-deployments-ci-code-review-security-99509e|Origin now integrates with over 20 apps for deployments, CI, code review, security…]] · Change
- 2026-10-13 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-13-3-safety-and-privacy-changes-in-v1-0-97|3 Safety and Privacy changes in v1.0.97]] · Digest
- 2026-10-12 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-12-3-safety-and-privacy-changes-in-v1-0-96|3 Safety and Privacy changes in v1.0.96]] · Digest
- 2026-10-12 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-10-12-fix-telemetry-retry-automation-consent-sync-by-enyst-in-https-github-com-openhan|fix(telemetry): retry automation consent sync]] · Change
- 2026-10-09 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-09-4-safety-and-privacy-changes-in-v2-1-296|4 Safety and Privacy changes in v2.1.296]] · Digest
- 2026-10-09 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-09-copilot-config-supports-sandbox-credential-injecthosts-keys-with-key-completion|copilot config supports sandbox credential injectHosts keys, with key completion…]] · Change
- 2026-10-08 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-08-5-safety-and-privacy-changes-in-v2-1-295|5 Safety and Privacy changes in v2.1.295]] · Digest
- 2026-10-08 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-08-13-safety-and-privacy-changes-in-rust-v0-162-0|13 Safety and Privacy changes in rust-v0.162.0]] · Digest
- 2026-10-08 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-08-2-safety-and-privacy-changes-in-v1-0-94|2 Safety and Privacy changes in v1.0.94]] · Digest
- 2026-10-07 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-07-3-safety-and-privacy-changes-in-v2-1-293|3 Safety and Privacy changes in v2.1.293]] · Digest
- 2026-10-07 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-07-9-safety-and-privacy-changes-in-rust-v0-161-0|9 Safety and Privacy changes in rust-v0.161.0]] · Digest
- 2026-10-07 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-07-2-safety-and-privacy-changes-in-v1-0-93|2 Safety and Privacy changes in v1.0.93]] · Digest
- 2026-10-06 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-06-6-safety-and-privacy-changes-in-v2-1-292|6 Safety and Privacy changes in v2.1.292]] · Digest
- 2026-10-06 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-06-fixed-a-regression-in-2-1-290-where-cloud-sessions-could-drop-answers-to-permiss|Fixed a regression in 2.1.290 where cloud sessions could drop answers to permission…]] · Fix
- 2026-10-06 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-10-06-fix-consume-consent-aware-website-posthog-handoff-by-malhotra5-in-https-github-c|fix: consume consent-aware website PostHog handoff]] · Fix
- 2026-10-05 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-05-19-safety-and-privacy-changes-in-v2-1-290|19 Safety and Privacy changes in v2.1.290]] · Digest
- 2026-10-05 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-05-4-safety-and-privacy-changes-in-v1-0-92|4 Safety and Privacy changes in v1.0.92]] · Digest
- 2026-10-02 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-02-6-safety-and-privacy-changes-in-v2-1-288|6 Safety and Privacy changes in v2.1.288]] · Digest
- 2026-10-01 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-01-6-safety-and-privacy-changes-in-v2-1-287|6 Safety and Privacy changes in v2.1.287]] · Digest
- 2026-10-01 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-01-7-safety-and-privacy-changes-in-rust-v0-160-0|7 Safety and Privacy changes in rust-v0.160.0]] · Digest
- 2026-10-01 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-01-2-safety-and-privacy-changes-in-v1-0-91|2 Safety and Privacy changes in v1.0.91]] · Digest

**2026-09**

- 2026-09-30 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-30-4-safety-and-privacy-changes-in-v2-1-286|4 Safety and Privacy changes in v2.1.286]] · Digest
- 2026-09-30 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-30-2-safety-and-privacy-changes-in-rust-v0-159-3|2 Safety and Privacy changes in rust-v0.159.3]] · Digest
- 2026-09-30 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-09-30-permission-prompts-remain-answerable-after-resuming-interrupted-sessions|Permission prompts remain answerable after resuming interrupted sessions]] · Change
- 2026-09-29 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-29-9-safety-and-privacy-changes-in-v2-1-285|9 Safety and Privacy changes in v2.1.285]] · Digest
- 2026-09-29 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-29-3-safety-and-privacy-changes-in-rust-v0-159-0|3 Safety and Privacy changes in rust-v0.159.0]] · Digest
- 2026-09-28 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-28-4-safety-and-privacy-changes-in-v2-1-284|4 Safety and Privacy changes in v2.1.284]] · Digest
- 2026-09-28 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-28-9-safety-and-privacy-changes-in-rust-v0-158-0|9 Safety and Privacy changes in rust-v0.158.0]] · Digest
- 2026-09-28 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-09-28-2-safety-and-privacy-changes-in-v1-0-89|2 Safety and Privacy changes in v1.0.89]] · Digest
- 2026-09-25 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-25-3-safety-and-privacy-changes-in-v2-1-283|3 Safety and Privacy changes in v2.1.283]] · Digest
- 2026-09-25 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-25-2-safety-and-privacy-changes-in-rust-v0-157-0|2 Safety and Privacy changes in rust-v0.157.0]] · Digest
- 2026-09-25 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-09-25-fix-mcp-keep-oauth-credentials-on-cloud-saves-and-skip-consent-when-tokens-still|fix(mcp): keep OAuth credentials on cloud saves and skip consent when tokens still work]] · Change
- 2026-09-24 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-24-4-safety-and-privacy-changes-in-v2-1-282|4 Safety and Privacy changes in v2.1.282]] · Digest
- 2026-09-24 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-09-24-raised-the-minimum-js-yaml-version-to-4-3-2-to-pick-up-a-security-fix-in-the-par|Raised the minimum js-yaml version to 4.3.2 to pick up a security fix in the parser…]] · Change
- 2026-09-23 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-23-12-safety-and-privacy-changes-in-v2-1-281|12 Safety and Privacy changes in v2.1.281]] · Digest
- 2026-09-23 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-09-23-2-safety-and-privacy-changes-in-rollouts-and-security-review|2 Safety and Privacy changes in Rollouts and Security Review]] · Digest
- 2026-09-22 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-22-2-safety-and-privacy-changes-in-v2-1-280|2 Safety and Privacy changes in v2.1.280]] · Digest
- 2026-09-22 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-22-50-safety-and-privacy-changes-in-rust-v0-156-0|50 Safety and Privacy changes in rust-v0.156.0]] · Digest
- 2026-09-22 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-09-22-2-safety-and-privacy-changes-in-v1-0-88|2 Safety and Privacy changes in v1.0.88]] · Digest
- 2026-09-21 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-09-21-privacy-center-is-rolling-out-to-signed-in-chatgpt-free-go-plus-and-pro-users-it-0d2f36|Privacy Center in ChatGPT]] · Change
- 2026-09-21 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-09-21-2-safety-and-privacy-changes-in-v1-0-87|2 Safety and Privacy changes in v1.0.87]] · Digest
- 2026-09-18 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-18-4-safety-and-privacy-changes-in-v2-1-277|4 Safety and Privacy changes in v2.1.277]] · Digest
- 2026-09-17 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-17-7-safety-and-privacy-changes-in-v2-1-275|7 Safety and Privacy changes in v2.1.275]] · Digest
- 2026-09-17 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-17-3-safety-and-privacy-changes-in-v2-1-274|3 Safety and Privacy changes in v2.1.274]] · Digest
- 2026-09-17 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-17-7-safety-and-privacy-changes-in-rust-v0-155-0|7 Safety and Privacy changes in rust-v0.155.0]] · Digest
- 2026-09-17 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-09-17-sandbox-policy-now-reports-local-network-access-using-your-configured-setting|/sandbox policy now reports local-network access using your configured setting]] · Change
- 2026-09-16 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-09-16-17-safety-and-privacy-changes-in-v1-0-85|17 Safety and Privacy changes in v1.0.85]] · Digest
- 2026-09-16 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-09-16-test-cover-telemetry-consent-banner-by-aivong-openhands-in-https-github-com-open|test: cover telemetry consent banner]] · Change
- 2026-09-15 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-15-5-safety-and-privacy-changes-in-v2-1-273|5 Safety and Privacy changes in v2.1.273]] · Digest
- 2026-09-15 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-09-15-2-safety-and-privacy-changes-in-v0-60-0|2 Safety and Privacy changes in v0.60.0]] · Digest
- 2026-09-14 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-09-14-if-you-make-no-changes-to-your-plugins-settings-the-default-permission-setting-i|If you make no changes to your Plugins settings, the default permission setting…]] · Change
- 2026-09-14 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-14-7-safety-and-privacy-changes-in-v2-1-271|7 Safety and Privacy changes in v2.1.271]] · Digest
- 2026-09-12 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-12-fixed-read-only-git-commands-in-bash-unexpectedly-asking-for-permission-after-a|Fixed read-only git commands in Bash unexpectedly asking for permission after…]] · Fix
- 2026-09-11 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-11-5-safety-and-privacy-changes-in-v2-1-269|5 Safety and Privacy changes in v2.1.269]] · Digest
- 2026-09-10 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-10-8-safety-and-privacy-changes-in-v2-1-268|8 Safety and Privacy changes in v2.1.268]] · Digest
- 2026-09-09 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-09-2-safety-and-privacy-changes-in-v2-1-267|2 Safety and Privacy changes in v2.1.267]] · Digest
- 2026-09-09 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-09-25-safety-and-privacy-changes-in-rust-v0-154-0|25 Safety and Privacy changes in rust-v0.154.0]] · Digest
- 2026-09-08 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-08-3-safety-and-privacy-changes-in-v2-1-265|3 Safety and Privacy changes in v2.1.265]] · Digest
- 2026-09-08 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-09-08-fix-core-enforce-fail-closed-workspace-trust-and-filter-mcpservers-in-restricted|fix(core): enforce fail-closed workspace trust and filter mcpServers in restricted mode]] · Change
- 2026-09-04 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-04-4-safety-and-privacy-changes-in-v2-1-261|4 Safety and Privacy changes in v2.1.261]] · Digest
- 2026-09-04 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-09-04-5-safety-and-privacy-changes-in-v1-0-83|5 Safety and Privacy changes in v1.0.83]] · Digest
- 2026-09-03 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-03-7-safety-and-privacy-changes-in-v2-1-260|7 Safety and Privacy changes in v2.1.260]] · Digest
- 2026-09-03 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-03-6-safety-and-privacy-changes-in-rust-v0-153-0|6 Safety and Privacy changes in rust-v0.153.0]] · Digest
- 2026-09-02 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-02-4-safety-and-privacy-changes-in-v2-1-259|4 Safety and Privacy changes in v2.1.259]] · Digest
- 2026-09-01 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-01-fixed-remote-and-scheduled-sessions-failing-with-user-messages-must-have-non-emp|Fixed remote and scheduled sessions failing…]] · Fix
- 2026-09-01 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-01-10-safety-and-privacy-changes-in-v2-1-257|10 Safety and Privacy changes in v2.1.257]] · Digest
- 2026-09-01 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-01-41227-use-compatible-powershell-for-elevated-windows-sandbox-commands-copyberry|♯41227 Use compatible PowerShell for elevated Windows sandbox commands @copyberry]] · Change

**2026-08**

- 2026-08-29 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-08-29-5-safety-and-privacy-changes-in-rust-v0-151-0|5 Safety and Privacy changes in rust-v0.151.0]] · Digest
- 2026-08-28 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-28-6-safety-and-privacy-changes-in-v2-1-251|6 Safety and Privacy changes in v2.1.251]] · Digest
- 2026-08-27 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-27-4-safety-and-privacy-changes-in-v2-1-248|4 Safety and Privacy changes in v2.1.248]] · Digest
- 2026-08-27 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-08-27-5-safety-and-privacy-changes-in-v1-0-81|5 Safety and Privacy changes in v1.0.81]] · Digest
- 2026-08-26 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-26-2-safety-and-privacy-changes-in-v2-1-247|2 Safety and Privacy changes in v2.1.247]] · Digest
- 2026-08-26 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-08-26-12-safety-and-privacy-changes-in-rust-v0-150-0|12 Safety and Privacy changes in rust-v0.150.0]] · Digest
- 2026-08-25 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-25-6-safety-and-privacy-changes-in-v2-1-246|6 Safety and Privacy changes in v2.1.246]] · Digest
- 2026-08-25 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-08-25-ssr-agent-issue-fix-26120-clarify-privacy-notice-wording-and-selection-options-b|SSR Agent Issue Fix (26120): Clarify privacy notice wording and selection options]] · Change
- 2026-08-21 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-21-fixed-fullscreen-mode-answering-a-permission-prompt-or-pressing-a-button-when-yo|Fixed fullscreen mode answering a permission prompt or pressing a button when you…]] · Fix
- 2026-08-20 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-20-3-safety-and-privacy-changes-in-v2-1-238|3 Safety and Privacy changes in v2.1.238]] · Digest
- 2026-08-20 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-08-20-18-safety-and-privacy-changes-in-rust-v0-149-0|18 Safety and Privacy changes in rust-v0.149.0]] · Digest
- 2026-08-19 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-19-2-safety-and-privacy-changes-in-v2-1-236|2 Safety and Privacy changes in v2.1.236]] · Digest
- 2026-08-18 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-18-2-safety-and-privacy-changes-in-v2-1-235|2 Safety and Privacy changes in v2.1.235]] · Digest
- 2026-08-18 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-08-18-17-safety-and-privacy-changes-in-rust-v0-148-0|17 Safety and Privacy changes in rust-v0.148.0]] · Digest
- 2026-08-17 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-17-8-safety-and-privacy-changes-in-v2-1-234|8 Safety and Privacy changes in v2.1.234]] · Digest
- 2026-08-14 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-14-3-safety-and-privacy-changes-in-v2-1-233|3 Safety and Privacy changes in v2.1.233]] · Digest
- 2026-08-14 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-08-14-reclaim-idle-plugin-sandbox-processes-instead-of-leaving-them-running-for-the-li|Reclaim idle plugin sandbox processes instead of leaving them running for the life…]] · Change
- 2026-08-13 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-13-9-safety-and-privacy-changes-in-v2-1-232|9 Safety and Privacy changes in v2.1.232]] · Digest
- 2026-08-13 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-08-13-fix-the-claude-code-provider-being-unusable-for-agentic-work-it-now-runs-its-own|Fix the Claude Code provider being unusable for agentic work]] · Change
- 2026-08-12 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-12-improved-sandbox-ipv6-literals-in-network-domain-lists-are-now-bracketed-1-443-a|Improved sandbox: IPv6 literals in network domain lists are now bracketed…]] · Change
- 2026-08-11 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-08-11-fix-a2a-server-enforce-workspace-trust-and-task-isolation-to-prevent-rce-by-luis|fix(a2a-server): enforce workspace trust and task isolation to prevent RCE]] · Change
- 2026-08-10 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-08-10-11-safety-and-privacy-changes-in-v1-0-79|11 Safety and Privacy changes in v1.0.79]] · Digest
- 2026-08-09 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-08-09-never-run-a-foreign-compiled-plugin-sandbox-bootstrap-for-a-source-host|Never run a foreign compiled plugin-sandbox bootstrap for a source host]] · Change
- 2026-08-08 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-08-2-safety-and-privacy-changes-in-v2-1-225|2 Safety and Privacy changes in v2.1.225]] · Digest
- 2026-08-07 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-07-2-safety-and-privacy-changes-in-v2-1-224|2 Safety and Privacy changes in v2.1.224]] · Digest
- 2026-08-07 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-08-07-9-safety-and-privacy-changes-in-rust-v0-147-0|9 Safety and Privacy changes in rust-v0.147.0]] · Digest
- 2026-08-06 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-06-3-safety-and-privacy-changes-in-v2-1-223|3 Safety and Privacy changes in v2.1.223]] · Digest
- 2026-08-05 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-08-05-apply-safer-automatic-review-defaults-for-cyber-capable-models-and-explain-permi|Apply safer automatic-review defaults for cyber-capable models and explain…]] · Change
- 2026-08-04 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-04-improved-auto-mode-safety-messages-sent-to-other-agent-sessions-via-sendmessage|Improved auto mode safety]] · Change
- 2026-08-04 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-04-7-safety-and-privacy-changes-in-v2-1-221|7 Safety and Privacy changes in v2.1.221]] · Digest
- 2026-08-03 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-08-03-3-safety-and-privacy-changes-in-v1-0-78|3 Safety and Privacy changes in v1.0.78]] · Digest

**2026-07**

- 2026-07-30 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-30-5-safety-and-privacy-changes-in-v1-0-76|5 Safety and Privacy changes in v1.0.76]] · Digest
- 2026-07-30 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-30-2-safety-and-privacy-changes-in-v1-0-77|2 Safety and Privacy changes in v1.0.77]] · Digest
- 2026-07-29 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-07-29-6-safety-and-privacy-changes-in-rust-v0-146-0|6 Safety and Privacy changes in rust-v0.146.0]] · Digest
- 2026-07-29 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-07-29-fix-revive-local-telemetry-consent-banner-by-malhotra5-in-https-github-com-openh|fix: Revive local telemetry consent banner]] · Fix
- 2026-07-28 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-07-28-fix-a2a-server-enforce-workspace-trust-and-task-isolation-to-prevent-rce-by-luis|fix(a2a-server): enforce workspace trust and task isolation to prevent RCE]] · Change
- 2026-07-24 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-07-24-2-safety-and-privacy-changes-in-v2-1-219|2 Safety and Privacy changes in v2.1.219]] · Digest
- 2026-07-23 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-07-23-health-is-built-with-layered-privacy-and-security-safeguards-connected-medical-r|Health is built with layered privacy and security safeguards]] · Change
- 2026-07-23 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-23-show-a-first-run-splash-to-opt-into-the-default-sandbox|Show a first-run splash to opt into the default sandbox]] · Change
- 2026-07-22 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-07-22-3-safety-and-privacy-changes-in-v2-1-218|3 Safety and Privacy changes in v2.1.218]] · Digest
- 2026-07-21 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-07-21-fixed-remote-control-sessions-not-showing-a-pending-permission-prompt-or-dialog|Fixed Remote Control sessions not showing a pending permission prompt or dialog…]] · Fix
- 2026-07-21 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-07-21-17-safety-and-privacy-changes-in-rust-v0-145-0|17 Safety and Privacy changes in rust-v0.145.0]] · Digest
- 2026-07-20 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-07-20-5-safety-and-privacy-changes-in-v2-1-216|5 Safety and Privacy changes in v2.1.216]] · Digest
- 2026-07-20 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-20-4-safety-and-privacy-changes-in-v1-0-72|4 Safety and Privacy changes in v1.0.72]] · Digest
- 2026-07-18 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-07-18-9-safety-and-privacy-changes-in-v2-1-214|9 Safety and Privacy changes in v2.1.214]] · Digest
- 2026-07-17 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-07-17-3-safety-and-privacy-changes-in-v2-1-212|3 Safety and Privacy changes in v2.1.212]] · Digest
- 2026-07-16 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-16-2-safety-and-privacy-changes-in-v1-0-71|2 Safety and Privacy changes in v1.0.71]] · Digest
- 2026-07-15 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-07-15-2-safety-and-privacy-changes-in-v2-1-211|2 Safety and Privacy changes in v2.1.211]] · Digest
- 2026-07-14 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-07-14-3-safety-and-privacy-changes-in-v2-1-210|3 Safety and Privacy changes in v2.1.210]] · Digest
- 2026-07-14 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-07-14-fixed-multi-second-per-turn-slowdowns-in-sessions-with-many-permission-deny-ask|Fixed multi-second per-turn slowdowns in sessions with many permission deny/ask rules]] · Fix
- 2026-07-11 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-07-11-2-safety-and-privacy-changes-in-v2-1-207|2 Safety and Privacy changes in v2.1.207]] · Digest
- 2026-07-10 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-07-10-fixed-permission-prompt-tool-pointing-at-an-mcp-server-crashing-with-mcp-tool-no|Fixed --permission-prompt-tool pointing at an MCP server crashing…]] · Fix
- 2026-07-10 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-10-5-safety-and-privacy-changes-in-v1-0-70|5 Safety and Privacy changes in v1.0.70]] · Digest
- 2026-07-09 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-07-09-on-desktop-work-can-use-local-files-and-desktop-apps-with-your-permission-the-bu-1e4d11|On desktop, Work can use local files and desktop apps with your permission]] · Change
- 2026-07-09 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-07-09-4-safety-and-privacy-changes-in-rust-v0-144-0|4 Safety and Privacy changes in rust-v0.144.0]] · Digest
- 2026-07-08 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-07-08-background-task-notifications-now-explicitly-state-that-no-human-input-has-occur|Background task notifications now explicitly state that no human input has occurred…]] · Change
- 2026-07-08 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-07-08-13-safety-and-privacy-changes-in-rust-v0-143-0|13 Safety and Privacy changes in rust-v0.143.0]] · Digest
- 2026-07-07 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-07-07-added-a-grey-badge-to-the-footer-when-in-manual-permission-mode-making-the-activ|Added a grey ⏸ badge to the footer when in manual permission mode, making the active…]] · Change
- 2026-07-07 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-07-8-safety-and-privacy-changes-in-v1-0-69|8 Safety and Privacy changes in v1.0.69]] · Digest
- 2026-07-06 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-07-06-fixed-remote-control-sessions-showing-the-wrong-permission-mode-in-the-mobile-an|Fixed /remote-control sessions showing the wrong permission mode in the mobile…]] · Fix
- 2026-07-06 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-07-06-4-safety-and-privacy-changes-in-1-9-0|4 Safety and Privacy changes in 1.9.0]] · Digest
- 2026-07-03 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-07-03-changed-the-default-permission-mode-to-manual-across-the-cli-help-vs-code-and-je|Changed the "default" permission mode to "Manual" across the CLI, --help, VS Code…]] · Change
- 2026-07-01 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-01-4-safety-and-privacy-changes-in-v1-0-68|4 Safety and Privacy changes in v1.0.68]] · Digest

**2026-06**

- 2026-06-30 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-30-disabling-the-sandbox-for-the-rest-of-the-session-now-takes-effect-immediately-s|Disabling the sandbox for the rest of the session now takes effect immediately…]] · Change
- 2026-06-30 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-30-3-safety-and-privacy-changes-in-v1-0-66|3 Safety and Privacy changes in v1.0.66]] · Digest
- 2026-06-29 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-06-29-security-claude-mcp-list-get-no-longer-spawn-mcp-json-servers-that-a-repo-self-a|Security: claude mcp list/get no longer spawn .mcp.json servers that a repo…]] · Change
- 2026-06-26 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-06-26-fixed-external-plugins-enabled-only-by-project-claude-settings-json-not-requirin|Fixed external plugins enabled only by project .claude/settings.json not requiring…]] · Fix
- 2026-06-25 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-25-2-safety-and-privacy-changes-in-rust-v0-142-2|2 Safety and Privacy changes in rust-v0.142.2]] · Digest
- 2026-06-24 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-06-24-improved-sandbox-network-permission-dialog-hosts-you-allow-with-yes-are-now-reme|Improved sandbox network permission dialog]] · Change
- 2026-06-24 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-24-commands-with-slash-prefixed-string-arguments-e-g-body-azp-run-no-longer-trigger|Commands with slash-prefixed string arguments (e.g. --body "/azp run") no longer…]] · Change
- 2026-06-23 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-06-23-2-safety-and-privacy-changes-in-v2-1-187|2 Safety and Privacy changes in v2.1.187]] · Digest
- 2026-06-23 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-23-6-safety-and-privacy-changes-in-v1-0-64|6 Safety and Privacy changes in v1.0.64]] · Digest
- 2026-06-22 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-06-22-2-safety-and-privacy-changes-in-v2-1-186|2 Safety and Privacy changes in v2.1.186]] · Digest
- 2026-06-22 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-22-12-safety-and-privacy-changes-in-rust-v0-142-0|12 Safety and Privacy changes in rust-v0.142.0]] · Digest
- 2026-06-18 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-06-18-app-permission-controls-you-can-now-choose-when-chatgpt-asks-before-using-connec|App permission controls: You can now choose when ChatGPT asks before using connected apps]] · Change
- 2026-06-18 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-18-7-safety-and-privacy-changes-in-rust-v0-141-0|7 Safety and Privacy changes in rust-v0.141.0]] · Digest
- 2026-06-17 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-06-17-added-sandbox-allowappleevents-opt-in-setting-that-lets-sandboxed-commands-send|Added sandbox.allowAppleEvents opt-in setting that lets sandboxed commands send…]] · Change
- 2026-06-15 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-06-15-2-safety-and-privacy-changes-in-v2-1-178|2 Safety and Privacy changes in v2.1.178]] · Digest
- 2026-06-15 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-15-27490-remove-tui-legacy-windows-sandbox-dependency-etraut-openai|♯27490 Remove TUI legacy Windows sandbox dependency @etraut-openai]] · Change
- 2026-06-13 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-13-2-safety-and-privacy-changes-in-v1-0-62|2 Safety and Privacy changes in v1.0.62]] · Digest
- 2026-06-10 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-06-10-2-safety-and-privacy-changes-in-v2-1-172|2 Safety and Privacy changes in v2.1.172]] · Digest
- 2026-06-10 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-06-10-users-can-select-the-sandbox-grouping-strategy-by-tofarr-in-https-github-com-ope|Users can select the sandbox grouping strategy]] · Change
- 2026-06-09 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-09-5-safety-and-privacy-changes-in-rust-v0-139-0|5 Safety and Privacy changes in rust-v0.139.0]] · Digest
- 2026-06-09 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-09-pasted-images-no-longer-leak-into-the-main-prompt-after-a-permission-dialog-clos|Pasted images no longer leak into the main prompt after a permission dialog closes]] · Change
- 2026-06-08 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-06-08-2-safety-and-privacy-changes-in-v2-1-169|2 Safety and Privacy changes in v2.1.169]] · Digest
- 2026-06-08 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-08-6-safety-and-privacy-changes-in-rust-v0-138-0|6 Safety and Privacy changes in rust-v0.138.0]] · Digest
- 2026-06-06 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-06-06-hardened-cross-session-messaging-messages-relayed-via-sendmessage-from-other-cla|Hardened cross-session messaging]] · Change
- 2026-06-05 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-05-2-safety-and-privacy-changes-in-v1-0-60|2 Safety and Privacy changes in v1.0.60]] · Digest
- 2026-06-04 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-06-04-fixed-org-managed-permission-rules-not-applying-for-the-entire-session-when-the|Fixed org-managed permission rules not applying for the entire session…]] · Fix
- 2026-06-04 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-04-8-safety-and-privacy-changes-in-rust-v0-137-0|8 Safety and Privacy changes in rust-v0.137.0]] · Digest
- 2026-06-03 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-06-03-4-safety-and-privacy-changes-in-v2-1-162|4 Safety and Privacy changes in v2.1.162]] · Digest
- 2026-06-03 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-06-03-update-vs-code-extension-dependencies-to-resolve-security-issues-in-xmldom-xmldo|Update VS Code extension dependencies to resolve security issues…]] · Change
- 2026-06-03 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-06-03-enterprise-customers-can-now-manage-multiple-cursor-teams-from-one-place-with-di|Enterprise customers can now manage multiple Cursor teams from one place…]] · Change
- 2026-06-02 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-06-02-we-re-rolling-out-active-sessions-a-new-security-feature-in-chatgpt-that-helps-u-51e977|ChatGPT rolls out Active sessions, a new security feature that helps users review…]] · Change
- 2026-06-01 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-01-11-safety-and-privacy-changes-in-rust-v0-136-0|11 Safety and Privacy changes in rust-v0.136.0]] · Digest

**2026-05**

- 2026-05-29 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-05-29-2-safety-and-privacy-changes-in-v2-1-157|2 Safety and Privacy changes in v2.1.157]] · Digest
- 2026-05-28 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-05-28-2-safety-and-privacy-changes-in-v2-1-153|2 Safety and Privacy changes in v2.1.153]] · Digest
- 2026-05-28 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-05-28-7-safety-and-privacy-changes-in-rust-v0-135-0|7 Safety and Privacy changes in rust-v0.135.0]] · Digest
- 2026-05-27 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-05-27-2-safety-and-privacy-changes-in-v2-1-152|2 Safety and Privacy changes in v2.1.152]] · Digest
- 2026-05-27 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-05-27-4-safety-and-privacy-changes-in-v0-44-0|4 Safety and Privacy changes in v0.44.0]] · Digest
- 2026-05-26 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-05-26-7-safety-and-privacy-changes-in-rust-v0-134-0|7 Safety and Privacy changes in rust-v0.134.0]] · Digest
- 2026-05-23 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-23-2-safety-and-privacy-changes-in-v1-0-52|2 Safety and Privacy changes in v1.0.52]] · Digest
- 2026-05-22 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-05-22-2-safety-and-privacy-changes-in-v2-1-149|2 Safety and Privacy changes in v2.1.149]] · Digest
- 2026-05-22 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-05-22-docs-add-vi-mode-shortcuts-and-clarify-mcp-custom-sandbox-setup-by-chrisjcthomas|docs: add vi mode shortcuts and clarify MCP/custom sandbox setup]] · Change
- 2026-05-21 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-05-21-17-safety-and-privacy-changes-in-rust-v0-133-0|17 Safety and Privacy changes in rust-v0.133.0]] · Digest
- 2026-05-20 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-05-20-5-safety-and-privacy-changes-in-rust-v0-132-0|5 Safety and Privacy changes in rust-v0.132.0]] · Digest
- 2026-05-20 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-20-add-security-review-slash-command-to-review-code-changes-for-security-vulnerabil|Add /security-review slash command to review code changes for security…]] · Change
- 2026-05-19 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-05-19-fixed-a-permission-prompt-bypass-where-bare-variable-assignments-to-non-allowlis|Fixed a permission-prompt bypass where bare variable assignments to non-allowlisted…]] · Fix
- 2026-05-19 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-05-19-fixed-skill-tool-failing-with-permission-error-in-headless-mode-regression-in-v2|Fixed Skill tool failing with permission error in headless mode (regression in v2.1.141)]] · Fix
- 2026-05-19 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-19-memory-permission-prompts-now-name-who-can-see-a-stored-memory-user-scope-or-the|Memory permission prompts now name who can see a stored memory]] · Change
- 2026-05-18 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-05-18-17-safety-and-privacy-changes-in-rust-v0-131-0|17 Safety and Privacy changes in rust-v0.131.0]] · Digest
- 2026-05-15 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-05-15-3-safety-and-privacy-changes-in-v2-1-143|3 Safety and Privacy changes in v2.1.143]] · Digest
- 2026-05-14 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-05-14-added-new-claude-agents-flags-add-dir-settings-mcp-config-plugin-dir-permission|Added new claude agents flags]] · Change
- 2026-05-13 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-05-13-5-safety-and-privacy-changes-in-v2-1-141|5 Safety and Privacy changes in v2.1.141]] · Digest
- 2026-05-12 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-05-12-3-safety-and-privacy-changes-in-v0-42-0|3 Safety and Privacy changes in v0.42.0]] · Digest
- 2026-05-11 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-05-11-fixed-skill-name-permission-rules-the-wildcard-form-now-works-as-a-prefix-match|Fixed Skill(name ) permission rules]] · Fix
- 2026-05-11 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-11-sessions-with-extension-permission-prompts-can-be-resumed-without-a-session-file|Sessions with extension permission prompts can be resumed without…]] · Change
- 2026-05-08 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-05-08-2-safety-and-privacy-changes-in-v2-1-136|2 Safety and Privacy changes in v2.1.136]] · Digest
- 2026-05-08 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-05-08-2-safety-and-privacy-changes-in-rust-v0-130-0|2 Safety and Privacy changes in rust-v0.130.0]] · Digest
- 2026-05-08 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-08-pressing-ctrl-c-while-a-permission-prompt-is-pending-no-longer-causes-the-cli-to|Pressing Ctrl+C while a permission prompt is pending no longer causes the CLI to hang]] · Change
- 2026-05-07 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-05-07-over-the-coming-weeks-we-ll-be-rolling-out-trusted-contact-an-optional-safety-fe|Trusted contact in ChatGPT]] · Change
- 2026-05-07 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-05-07-added-sandbox-bwrappath-and-sandbox-socatpath-managed-settings-linux-wsl-to-spec|Added sandbox.bwrapPath and sandbox.socatPath managed settings (Linux/WSL)…]] · Change
- 2026-05-07 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-05-07-11-safety-and-privacy-changes-in-rust-v0-129-0|11 Safety and Privacy changes in rust-v0.129.0]] · Digest
- 2026-05-06 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-05-06-fixed-permission-mode-flag-being-ignored-when-resuming-a-plan-mode-session-with|Fixed --permission-mode flag being ignored when resuming a plan-mode session…]] · Fix
- 2026-05-06 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-05-06-fixed-session-title-chip-from-rename-disappearing-while-a-permission-or-other-di|Fixed session title chip from /rename disappearing while a permission or other…]] · Fix
- 2026-05-06 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-06-protect-against-rce-from-malicious-bare-repositories-nested-inside-a-project-for|Protect against RCE from malicious bare repositories nested inside a project…]] · Change
- 2026-05-05 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-05-05-feat-cli-secure-env-loading-and-enforce-workspace-trust-in-headless-mode-by-ehed|feat(cli): secure .env loading and enforce workspace trust in headless mode]] · Change
- 2026-05-05 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-05-memory-tool-confirmation-prompt-now-shows-the-scope-repository-or-user-when-requ|Memory tool confirmation prompt now shows the scope (repository or user)…]] · Change
- 2026-05-04 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-05-04-sdk-hosts-now-receive-a-persistent-localsettings-suggestion-for-bash-permission|SDK hosts now receive a persistent localSettings suggestion for Bash permission…]] · Change
- 2026-05-01 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-05-01-3-safety-and-privacy-changes-in-v2-1-126|3 Safety and Privacy changes in v2.1.126]] · Digest
- 2026-05-01 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-05-01-default-off-users-can-discover-and-opt-in|Default Off: users can discover and opt in]] · Change
- 2026-05-01 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-05-01-added-sandbox-kvm-enabled-environment-variable-to-enable-passing-dev-kvm-to-sand|Added SANDBOX_KVM_ENABLED environment variable to enable passing /dev/kvm to sandbox…]] · Change

**2026-04**

- 2026-04-30 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-30-21-safety-and-privacy-changes-in-rust-v0-128-0|21 Safety and Privacy changes in rust-v0.128.0]] · Digest
- 2026-04-30 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-04-30-cursor-security-review-is-now-in-beta-on-teams-and-enterprise-plans-you-can-run|Cursor Security Review is now in beta on Teams and Enterprise plans]] · Change
- 2026-04-28 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-04-28-feat-sandbox-resolve-custom-seatbelt-profiles-from-home-gemini-first-by-mvanhorn|feat(sandbox): resolve custom seatbelt profiles from $HOME/.gemini first]] · Change
- 2026-04-28 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-28-allow-acp-clients-to-toggle-allow-all-permission-mode-via-session-configuration|Allow ACP clients to toggle allow-all permission mode via session configuration]] · Change
- 2026-04-24 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-24-9-safety-and-privacy-changes-in-rust-v0-125-0|9 Safety and Privacy changes in rust-v0.125.0]] · Digest
- 2026-04-23 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-04-23-fixed-mcp-step-up-authorization-silently-refreshing-instead-of-prompting-for-re|Fixed MCP step-up authorization silently refreshing instead of prompting…]] · Fix
- 2026-04-23 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-04-23-4-safety-and-privacy-changes-in-v2-1-119|4 Safety and Privacy changes in v2.1.119]] · Digest
- 2026-04-23 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-23-17-safety-and-privacy-changes-in-rust-v0-124-0|17 Safety and Privacy changes in rust-v0.124.0]] · Digest
- 2026-04-23 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-23-6-safety-and-privacy-changes-in-rust-v0-123-0|6 Safety and Privacy changes in rust-v0.123.0]] · Digest
- 2026-04-23 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-04-23-6-safety-and-privacy-changes-in-v0-39-0|6 Safety and Privacy changes in v0.39.0]] · Digest
- 2026-04-23 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-23-permission-prompts-appear-correctly-in-remote-sessions-for-the-cli-tui|Permission prompts appear correctly in remote sessions for the CLI TUI]] · Change
- 2026-04-20 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-04-20-security-sandbox-auto-allow-no-longer-bypasses-the-dangerous-path-safety-check-f|Security: sandbox auto-allow no longer bypasses the dangerous-path safety check…]] · Change
- 2026-04-20 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-20-9-safety-and-privacy-changes-in-rust-v0-122-0|9 Safety and Privacy changes in rust-v0.122.0]] · Digest
- 2026-04-18 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-04-18-fixed-a-crash-in-the-permission-dialog-when-an-agent-teams-teammate-requested-to|Fixed a crash in the permission dialog when an agent teams teammate requested tool…]] · Fix
- 2026-04-17 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-04-17-6-safety-and-privacy-changes-in-v2-1-113|6 Safety and Privacy changes in v2.1.113]] · Digest
- 2026-04-16 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-04-16-2-safety-and-privacy-changes-in-v2-1-111|2 Safety and Privacy changes in v2.1.111]] · Digest
- 2026-04-16 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-16-2-safety-and-privacy-changes-in-v1-0-28|2 Safety and Privacy changes in v1.0.28]] · Digest
- 2026-04-15 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-15-10-safety-and-privacy-changes-in-rust-v0-121-0|10 Safety and Privacy changes in rust-v0.121.0]] · Digest
- 2026-04-14 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-04-14-2-safety-and-privacy-changes-in-v2-1-108|2 Safety and Privacy changes in v2.1.108]] · Digest
- 2026-04-14 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-04-14-3-safety-and-privacy-changes-in-v0-38-0|3 Safety and Privacy changes in v0.38.0]] · Digest
- 2026-04-14 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-14-permission-prompt-notification-hook-only-fires-when-a-prompt-is-actually-shown-t|Permission prompt notification hook only fires when a prompt is actually shown to the user]] · Change
- 2026-04-13 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-04-13-fixed-bash-tool-suggesting-acceptedits-permission-mode-when-exiting-plan-mode-wo|Fixed Bash tool suggesting acceptEdits permission mode when exiting plan mode…]] · Fix
- 2026-04-11 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-11-4-safety-and-privacy-changes-in-rust-v0-120-0|4 Safety and Privacy changes in rust-v0.120.0]] · Digest
- 2026-04-10 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-04-10-fixed-a-command-injection-vulnerability-in-the-posix-which-fallback-used-by-lsp|Fixed a command injection vulnerability in the POSIX which fallback used by LSP…]] · Fix
- 2026-04-10 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-10-8-safety-and-privacy-changes-in-rust-v0-119-0|8 Safety and Privacy changes in rust-v0.119.0]] · Digest
- 2026-04-09 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-04-09-7-safety-and-privacy-changes-in-v2-1-98|7 Safety and Privacy changes in v2.1.98]] · Digest
- 2026-04-09 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-09-permission-checks-and-other-hooks-now-work-correctly-when-using-anthropic-models|Permission checks and other hooks now work correctly when using Anthropic models…]] · Change
- 2026-04-08 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-04-08-3-safety-and-privacy-changes-in-v2-1-97|3 Safety and Privacy changes in v2.1.97]] · Digest
- 2026-04-08 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-04-08-16-safety-and-privacy-changes-in-v0-37-0|16 Safety and Privacy changes in v0.37.0]] · Digest
- 2026-04-07 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-04-07-vscode-added-a-warning-banner-when-settings-json-files-fail-to-parse-so-users-kn|VSCode Added a warning banner when settings.json files fail to parse, so users…]] · Change
- 2026-04-04 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-04-04-linux-sandbox-now-ships-the-apply-seccomp-helper-in-both-npm-and-native-builds-r|Linux sandbox now ships the apply-seccomp helper in both npm and native builds…]] · Change
- 2026-04-04 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-04-add-notification-hook-event-that-fires-asynchronously-on-shell-completion-permis|Add notification hook event that fires asynchronously on shell completion…]] · Change
- 2026-04-02 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-04-02-fixed-plan-mode-in-remote-sessions-losing-track-of-the-plan-file-after-a-contain|Fixed plan mode in remote sessions losing track of the plan file after a container…]] · Fix
- 2026-04-02 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-02-add-permissionrequest-hook-to-allow-scripts-to-programmatically-approve-or-deny|Add PermissionRequest hook to allow scripts to programmatically approve or deny tool…]] · Change
- 2026-04-01 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-04-01-2-safety-and-privacy-changes-in-v2-1-89|2 Safety and Privacy changes in v2.1.89]] · Digest
- 2026-04-01 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-04-01-4-safety-and-privacy-changes-in-v2-1-90|4 Safety and Privacy changes in v2.1.90]] · Digest
- 2026-04-01 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-04-01-7-safety-and-privacy-changes-in-v0-36-0|7 Safety and Privacy changes in v0.36.0]] · Digest

**2026-03**

- 2026-03-31 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-31-7-safety-and-privacy-changes-in-rust-v0-118-0|7 Safety and Privacy changes in rust-v0.118.0]] · Digest
- 2026-03-31 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-31-2-safety-and-privacy-changes-in-v1-0-14|2 Safety and Privacy changes in v1.0.14]] · Digest
- 2026-03-30 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-30-mcp-servers-using-microsoft-entra-id-authentication-no-longer-show-the-consent-s|MCP servers using Microsoft Entra ID authentication no longer show the consent…]] · Change
- 2026-03-27 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-03-27-fixed-official-marketplace-plugin-scripts-failing-with-permission-denied-on-maco|Fixed official marketplace plugin scripts failing…]] · Fix
- 2026-03-26 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-03-26-fixed-the-allow-claude-to-edit-its-own-settings-for-this-session-permission-opti|Fixed the "allow Claude to edit its own settings for this session" permission option…]] · Fix
- 2026-03-26 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-03-26-2-safety-and-privacy-changes-in-v2-1-85|2 Safety and Privacy changes in v2.1.85]] · Digest
- 2026-03-26 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-26-5-safety-and-privacy-changes-in-rust-v0-117-0|5 Safety and Privacy changes in rust-v0.117.0]] · Digest
- 2026-03-25 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-03-25-2-safety-and-privacy-changes-in-v2-1-83|2 Safety and Privacy changes in v2.1.83]] · Digest
- 2026-03-24 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-03-24-5-safety-and-privacy-changes-in-v0-35-0|5 Safety and Privacy changes in v0.35.0]] · Digest
- 2026-03-20 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-03-20-2-safety-and-privacy-changes-in-v2-1-81|2 Safety and Privacy changes in v2.1.81]] · Digest
- 2026-03-19 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-19-8-safety-and-privacy-changes-in-rust-v0-116-0|8 Safety and Privacy changes in rust-v0.116.0]] · Digest
- 2026-03-18 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-03-18-fixed-custom-status-line-showing-nothing-when-workspace-trust-is-blocking-it|Fixed custom status line showing nothing when workspace trust is blocking it]] · Fix
- 2026-03-17 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-03-17-2-safety-and-privacy-changes-in-v2-1-78|2 Safety and Privacy changes in v2.1.78]] · Digest
- 2026-03-17 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-03-17-3-safety-and-privacy-changes-in-v2-1-77|3 Safety and Privacy changes in v2.1.77]] · Digest
- 2026-03-17 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-03-17-3-safety-and-privacy-changes-in-v0-34-0|3 Safety and Privacy changes in v0.34.0]] · Digest
- 2026-03-16 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-16-9-safety-and-privacy-changes-in-rust-v0-115-0|9 Safety and Privacy changes in rust-v0.115.0]] · Digest
- 2026-03-16 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-16-extension-tools-now-work-with-the-permissions-system-use-skippermission-per-tool|Extension tools now work with the permissions system, use skipPermission per-tool…]] · Change
- 2026-03-14 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-03-14-3-safety-and-privacy-changes-in-v2-1-76|3 Safety and Privacy changes in v2.1.76]] · Digest
- 2026-03-12 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-03-12-fixed-voice-mode-silently-failing-on-the-macos-native-binary-for-users-whose-ter|Fixed voice mode silently failing on the macOS native binary for users whose…]] · Fix
- 2026-03-12 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-03-12-markdown-image-loading-now-requires-user-consent|Markdown image loading now requires user consent]] · Change
- 2026-03-11 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-03-11-fixed-freezes-and-100-cpu-loops-triggered-by-permission-prompts-for-complex-bash|Fixed freezes and 100% CPU loops triggered by permission prompts for complex bash commands]] · Fix
- 2026-03-11 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-11-2-safety-and-privacy-changes-in-rust-v0-114-0|2 Safety and Privacy changes in rust-v0.114.0]] · Digest
- 2026-03-11 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-03-11-refactor-cli-fully-remove-react-anti-patterns-improve-type-safety-and-fix-ux-ove|refactor(cli): fully remove React anti patterns, improve type safety and fix UX…]] · Change
- 2026-03-11 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-11-2-safety-and-privacy-changes-in-v1-0-4|2 Safety and Privacy changes in v1.0.4]] · Digest
- 2026-03-10 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-03-10-6-safety-and-privacy-changes-in-v2-1-72|6 Safety and Privacy changes in v2.1.72]] · Digest
- 2026-03-10 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-10-10-safety-and-privacy-changes-in-rust-v0-113-0|10 Safety and Privacy changes in rust-v0.113.0]] · Digest
- 2026-03-09 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-09-reset-allowed-tools-now-fully-undoes-allow-all-and-re-triggers-the-autopilot-per|/reset-allowed-tools now fully undoes /allow-all and re-triggers the autopilot…]] · Change
- 2026-03-08 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-08-6-safety-and-privacy-changes-in-rust-v0-112-0|6 Safety and Privacy changes in rust-v0.112.0]] · Digest
- 2026-03-07 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-03-07-fixed-false-positive-permission-prompts-for-compound-bash-commands-containing-he|Fixed false-positive permission prompts for compound bash commands containing…]] · Fix
- 2026-03-05 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-03-05-5-safety-and-privacy-changes-in-v2-1-69|5 Safety and Privacy changes in v2.1.69]] · Digest
- 2026-03-05 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-05-4-safety-and-privacy-changes-in-rust-v0-110-0|4 Safety and Privacy changes in rust-v0.110.0]] · Digest
- 2026-03-05 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-03-05-when-invoked-the-agent-spins-up-a-cloud-sandbox-and-follows-your-instructions-us|When invoked, the agent spins up a cloud sandbox and follows your instructions using…]] · Change
- 2026-03-03 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-03-03-fixed-team-permission-and-access-control-inconsistencies-across-organization-set|Fixed team permission and access control inconsistencies across organization setups]] · Fix
- 2026-03-03 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-03-autopilot-permission-dialog-appears-on-first-prompt-submission-instead-of-on-mod|Autopilot permission dialog appears on first prompt submission instead of on mode switch]] · Change
- 2026-03-02 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-02-8-safety-and-privacy-changes-in-rust-v0-107-0|8 Safety and Privacy changes in rust-v0.107.0]] · Digest

**2026-02**

- 2026-02-28 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-02-28-fixed-listener-leak-in-interactive-permission-handler-during-auto-approvals|Fixed listener leak in interactive permission handler during auto-approvals]] · Fix
- 2026-02-27 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-02-27-6-safety-and-privacy-changes-in-v0-31-0|6 Safety and Privacy changes in v0.31.0]] · Digest
- 2026-02-26 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-26-12800-fix-enforce-sandbox-envelope-for-zsh-fork-execution-bolinfest|♯12800 fix: enforce sandbox envelope for zsh fork execution @bolinfest]] · Change
- 2026-02-25 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-25-9-safety-and-privacy-changes-in-rust-v0-105-0|9 Safety and Privacy changes in rust-v0.105.0]] · Digest
- 2026-02-25 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-02-25-refactor-core-adopt-coretoolcallstatus-enum-for-type-safety-by-jerop-in-https-gi|refactor(core): adopt CoreToolCallStatus enum for type safety]] · Change
- 2026-02-24 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-02-24-3-safety-and-privacy-changes-in-v2-1-51|3 Safety and Privacy changes in v2.1.51]] · Digest
- 2026-02-21 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-21-show-permission-elevation-dialog-when-accepting-a-plan-with-autopilot-to-prevent|Show permission elevation dialog when accepting a plan with autopilot to prevent…]] · Change
- 2026-02-19 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-02-19-3-safety-and-privacy-changes-in-v2-1-49|3 Safety and Privacy changes in v2.1.49]] · Digest
- 2026-02-18 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-02-18-2-safety-and-privacy-changes-in-v2-1-47|2 Safety and Privacy changes in v2.1.47]] · Digest
- 2026-02-18 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-02-18-7-safety-and-privacy-changes-in-cli-improvements-and-mermaid-ascii|7 Safety and Privacy changes in CLI Improvements and Mermaid ASCII…]] · Digest
- 2026-02-18 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-02-18-5-safety-and-privacy-changes-in-v0-29-0|5 Safety and Privacy changes in v0.29.0]] · Digest
- 2026-02-17 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-02-17-vscode-improved-permission-destination-choice-project-user-session-to-persist-ac|VSCode Improved permission destination choice (project/user/session) to persist…]] · Change
- 2026-02-17 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-17-9-safety-and-privacy-changes-in-rust-v0-102-0|9 Safety and Privacy changes in rust-v0.102.0]] · Digest
- 2026-02-17 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-02-17-3-safety-and-privacy-changes-in-2-5|3 Safety and Privacy changes in 2.5]] · Digest
- 2026-02-13 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-02-13-2-safety-and-privacy-changes-in-v2-1-41|2 Safety and Privacy changes in v2.1.41]] · Digest
- 2026-02-12 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-12-5-safety-and-privacy-changes-in-rust-v0-100-0|5 Safety and Privacy changes in rust-v0.100.0]] · Digest
- 2026-02-12 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-12-permission-prompts-with-long-diffs-are-scrollable-in-alt-screen-mode|Permission prompts with long diffs are scrollable in alt-screen mode]] · Change
- 2026-02-11 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-11-8-safety-and-privacy-changes-in-rust-v0-99-0|8 Safety and Privacy changes in rust-v0.99.0]] · Digest
- 2026-02-10 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-02-10-2-safety-and-privacy-changes-in-v2-1-38|2 Safety and Privacy changes in v2.1.38]] · Digest
- 2026-02-10 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-02-10-3-safety-and-privacy-changes-in-v0-28-0|3 Safety and Privacy changes in v0.28.0]] · Digest
- 2026-02-06 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-02-06-fixed-a-bug-where-commands-excluded-from-sandboxing-via-sandbox-excludedcommands|Fixed a bug where commands excluded from sandboxing…]] · Fix
- 2026-02-05 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-05-2-safety-and-privacy-changes-in-rust-v0-97-0|2 Safety and Privacy changes in rust-v0.97.0]] · Digest
- 2026-02-05 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-05-2-safety-and-privacy-changes-in-v0-0-403|2 Safety and Privacy changes in v0.0.403]] · Digest
- 2026-02-04 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-04-6-safety-and-privacy-changes-in-rust-v0-95-0|6 Safety and Privacy changes in rust-v0.95.0]] · Digest
- 2026-02-04 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-02-04-security-hooks-wrap-hook-injected-context-in-distinct-xml-tags-by-yunaseoul-in-h|security(hooks): Wrap hook-injected context in distinct XML tags]] · Change
- 2026-02-03 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-02-03-fixed-permission-dialogs-stealing-focus-while-actively-typing|Fixed permission dialogs stealing focus while actively typing]] · Fix
- 2026-02-02 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-02-02-2-safety-and-privacy-changes-in-1-3-0|2 Safety and Privacy changes in 1.3.0]] · Digest

**2026-01**

- 2026-01-31 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-31-4-safety-and-privacy-changes-in-rust-v0-93-0|4 Safety and Privacy changes in rust-v0.93.0]] · Digest
- 2026-01-30 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-01-30-permissions-now-respect-content-level-ask-over-tool-level-allow-previously-allow|Permissions now respect content-level ask over tool-level allow]] · Change
- 2026-01-30 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-30-acp-server-support-permission-flags-yolo-allow-all-etc-and-permissions-config|ACP server support permission flags: --yolo, --allow-all, etc. and permissions config]] · Change
- 2026-01-29 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-01-29-fixed-per-user-temp-directory-isolation-to-prevent-permission-conflicts-on-share|Fixed per-user temp directory isolation to prevent permission conflicts on shared systems]] · Fix
- 2026-01-28 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-01-28-3-safety-and-privacy-changes-in-v0-26-0|3 Safety and Privacy changes in v0.26.0]] · Digest
- 2026-01-27 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-01-27-2-safety-and-privacy-changes-in-v2-1-20|2 Safety and Privacy changes in v2.1.20]] · Digest
- 2026-01-27 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-27-2-safety-and-privacy-changes-in-rust-v0-92-0|2 Safety and Privacy changes in rust-v0.92.0]] · Digest
- 2026-01-25 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-25-4-safety-and-privacy-changes-in-rust-v0-90-0|4 Safety and Privacy changes in rust-v0.90.0]] · Digest
- 2026-01-22 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-22-2-safety-and-privacy-changes-in-rust-v0-89-0|2 Safety and Privacy changes in rust-v0.89.0]] · Digest
- 2026-01-22 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-01-22-unified-cli-permissions-with-the-editor-including-run-everything-auto-run-in-san|Unified CLI permissions with the editor, including Run Everything, Auto-Run…]] · Change
- 2026-01-21 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-21-3-safety-and-privacy-changes-in-rust-v0-88-0|3 Safety and Privacy changes in rust-v0.88.0]] · Digest
- 2026-01-15 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-15-revert-linux-sandboxing-now-falls-back-to-landlock-only-restrictions-when-user-n|revert Linux sandboxing now falls back to Landlock-only restrictions when user…]] · Change
- 2026-01-14 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-01-14-2-safety-and-privacy-changes-in-v2-1-7|2 Safety and Privacy changes in v2.1.7]] · Digest
- 2026-01-14 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-14-5-safety-and-privacy-changes-in-rust-v0-81-0|5 Safety and Privacy changes in rust-v0.81.0]] · Digest
- 2026-01-14 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-01-14-7-safety-and-privacy-changes-in-v0-24-0|7 Safety and Privacy changes in v0.24.0]] · Digest
- 2026-01-13 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-01-13-fixed-permission-bypass-via-shell-line-continuation-that-could-allow-blocked-com|Fixed permission bypass via shell line continuation that could allow blocked…]] · Fix
- 2026-01-13 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-13-provide-inline-feedback-when-rejecting-tool-permission-requests-so-agents-don-t|Provide inline feedback when rejecting tool permission requests so agents don't have…]] · Change
- 2026-01-09 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-01-09-2-safety-and-privacy-changes-in-v2-1-2|2 Safety and Privacy changes in v2.1.2]] · Digest
- 2026-01-09 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-01-09-2-safety-and-privacy-changes-in-v2-1-3|2 Safety and Privacy changes in v2.1.3]] · Digest
- 2026-01-09 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-09-2-safety-and-privacy-changes-in-rust-v0-80-0|2 Safety and Privacy changes in rust-v0.80.0]] · Digest
- 2026-01-07 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-07-allow-global-exec-flags-model-json-sandbox-toggles-etc-to-be-passed-after-codex|Allow global exec flags (model/json/sandbox toggles, etc.) to be passed after…]] · Change
- 2026-01-06 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-06-3-safety-and-privacy-changes-in-rust-v0-78-0|3 Safety and Privacy changes in rust-v0.78.0]] · Digest

</details>

</details>

<details class="disclosure">
<summary>2025 · 77 entries (Aider 1 · ChatGPT 3 · Cline 1 · Codex CLI 29 · Cursor 5 · Gemini CLI 24 · GitHub Copilot CLI 6 · OpenHands 8)</summary>

**2025-11**

- 2025-11-20 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-11-20-docs-remove-references-to-deprecated-flags-checkpointing-sandbox-image-by-nayong|docs: remove references to deprecated flags (--checkpointing, --sandbox-image)]] · Policy

**2025-10**

- 2025-10-29 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-10-29-sandboxed-terminals-ga|Sandboxed Terminals (GA)]] · Launch

**2025-09**

- 2025-09-29 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-09-29-we-re-rolling-out-parental-controls-globally-in-chatgpt-to-help-families-guide-h-289d0a|ChatGPT rolls out parental controls globally to help families guide how ChatGPT…]] · Policy
- 2025-09-29 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-09-29-sandboxed-terminals|Sandboxed terminals]] · Launch

<details class="disclosure">
<summary>Fixes, digests and other changes · 73 (Aider 1 · ChatGPT 2 · Cline 1 · Codex CLI 29 · Cursor 3 · Gemini CLI 23 · GitHub Copilot CLI 6 · OpenHands 8)</summary>

**2025-12**

- 2025-12-22 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-12-22-improved-stability-around-how-the-agent-respects-auto-run-preferences-to-prevent|Improved stability around how the agent respects auto-run preferences to prevent…]] · Change
- 2025-12-21 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-12-21-2-safety-and-privacy-changes-in-rust-v0-77-0|2 Safety and Privacy changes in rust-v0.77.0]] · Digest
- 2025-12-19 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-12-19-2-safety-and-privacy-changes-in-rust-v0-76-0|2 Safety and Privacy changes in rust-v0.76.0]] · Digest
- 2025-12-19 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-12-19-add-url-permission-controls-which-affect-common-shell-commands-which-access-the|Add URL permission controls which affect common shell commands which access the web]] · Change
- 2025-12-18 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-12-18-3-safety-and-privacy-changes-in-rust-v0-74-0|3 Safety and Privacy changes in rust-v0.74.0]] · Digest
- 2025-12-16 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-12-16-2-safety-and-privacy-changes-in-v0-21-0|2 Safety and Privacy changes in v0.21.0]] · Digest
- 2025-12-15 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-12-15-3-safety-and-privacy-changes-in-rust-v0-73-0|3 Safety and Privacy changes in rust-v0.73.0]] · Digest
- 2025-12-13 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-12-13-3-safety-and-privacy-changes-in-rust-v0-72-0|3 Safety and Privacy changes in rust-v0.72.0]] · Digest
- 2025-12-10 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-12-10-5-safety-and-privacy-changes-in-rust-v0-69-0|5 Safety and Privacy changes in rust-v0.69.0]] · Digest
- 2025-12-09 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-12-09-3-safety-and-privacy-changes-in-rust-v0-66-0|3 Safety and Privacy changes in rust-v0.66.0]] · Digest
- 2025-12-09 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-12-09-add-consent-flag-to-link-command-by-kevinjwang1-in-https-github-com-google-gemin|Add consent flag to Link command]] · Change
- 2025-12-02 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-12-02-9-safety-and-privacy-changes-in-rust-v0-64-0|9 Safety and Privacy changes in rust-v0.64.0]] · Digest
- 2025-12-02 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-12-02-improve-code-coverage-for-cli-src-ui-privacy-package-by-megha1188-in-https-githu|Improve code coverage for cli/src/ui/privacy package]] · Change

**2025-11**

- 2025-11-27 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-11-27-maint-npm-audit-fix-for-glob-package-vulnerability-by-canvrno-in-https-github-co|maint: npm audit fix for glob package vulnerability]] · Change
- 2025-11-20 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-11-20-shell-reliability-and-sandbox-warnings-fallback-shell-selection-is-hardened-and|Shell reliability and sandbox warnings]] · Change
- 2025-11-19 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-11-19-7-safety-and-privacy-changes-in-rust-v0-59-0|7 Safety and Privacy changes in rust-v0.59.0]] · Digest
- 2025-11-18 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-11-18-fix-file-operations-timing-out-while-waiting-for-user-permission|Fix file operations timing out while waiting for user permission]] · Change
- 2025-11-17 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-11-17-2-safety-and-privacy-changes-in-v0-0-359|2 Safety and Privacy changes in v0.0.359]] · Digest
- 2025-11-13 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-11-13-6480-use-codex-linux-sandbox-in-unified-exec-6c36318bd|♯6480 — Use codex-linux-sandbox in unified exec (6c36318bd)]] · Change
- 2025-11-07 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-11-07-2-safety-and-privacy-changes-in-rust-v0-56-0|2 Safety and Privacy changes in rust-v0.56.0]] · Digest
- 2025-11-07 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-11-07-migrate-console-error-to-coreevents-debugger-for-sandbox-logger-chatrecordingser|migrate console.error to coreEvents/debugger for sandbox, logger, chatRecordingService]] · Change
- 2025-11-04 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-11-04-3-safety-and-privacy-changes-in-rust-v0-54-0|3 Safety and Privacy changes in rust-v0.54.0]] · Digest
- 2025-11-04 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-11-04-fix-infra-simplify-cancel-in-progress-and-add-permission-to-set-status-step-by-s|fix(infra) - Simplify cancel in progress and add permission to set status step]] · Change

**2025-10**

- 2025-10-30 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-10-30-3-safety-and-privacy-changes-in-rust-v0-52-0|3 Safety and Privacy changes in rust-v0.52.0]] · Digest
- 2025-10-29 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2025-10-29-3-safety-and-privacy-changes-in-0-60-0|3 Safety and Privacy changes in 0.60.0]] · Digest
- 2025-10-25 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-10-25-5536-added-model-summary-and-risk-assessment-for-commands-that-violate-sandbox-p|♯5536 — Added model summary and risk assessment for commands that violate sandbox policy]] · Change
- 2025-10-23 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-10-23-2-safety-and-privacy-changes-in-rust-v0-48-0|2 Safety and Privacy changes in rust-v0.48.0]] · Digest
- 2025-10-22 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-10-22-2-safety-and-privacy-changes-in-v0-10-0|2 Safety and Privacy changes in v0.10.0]] · Digest
- 2025-10-22 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-10-22-ensure-that-environment-variables-are-expanded-before-running-path-permission-ch|Ensure that environment variables are expanded before running path permission checks]] · Change
- 2025-10-17 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-10-17-2-safety-and-privacy-changes-in-rust-v0-47-0|2 Safety and Privacy changes in rust-v0.47.0]] · Digest
- 2025-10-07 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-10-07-3-safety-and-privacy-changes-in-v0-8-0|3 Safety and Privacy changes in v0.8.0]] · Digest
- 2025-10-06 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-10-06-codex-login-api-key-was-replaced-with-codex-login-with-api-key-that-reads-the-ke|codex login --api-key was replaced with codex login --with-api-key that reads…]] · Change
- 2025-10-03 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-10-03-3-safety-and-privacy-changes-in-rust-v0-44-0|3 Safety and Privacy changes in rust-v0.44.0]] · Digest
- 2025-10-01 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-10-01-4-safety-and-privacy-changes-in-v0-7-0|4 Safety and Privacy changes in v0.7.0]] · Digest
- 2025-10-01 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-10-01-improved-how-we-extract-paths-from-shell-commands-for-permission-handling-might|Improved how we extract paths from shell commands for permission handling…]] · Change
- 2025-10-01 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2025-10-01-significantly-improved-the-security-of-the-openhands-enterprise-docker-image-by|Significantly improved the security of the OpenHands enterprise Docker image…]] · Change

**2025-09**

- 2025-09-26 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-09-26-2-safety-and-privacy-changes-in-rust-v0-42-0|2 Safety and Privacy changes in rust-v0.42.0]] · Digest
- 2025-09-26 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-09-26-improved-the-error-message-received-when-using-a-pat-that-is-missing-the-copilot|Improved the error message received when using a PAT that is missing…]] · Change
- 2025-09-24 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-09-24-4-safety-and-privacy-changes-in-v0-6-0|4 Safety and Privacy changes in v0.6.0]] · Digest
- 2025-09-23 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-09-23-3880-add-non-sandbox-test-helper-3880|♯3880 Add non_sandbox_test helper (♯3880)]] · Change
- 2025-09-17 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-09-17-2-safety-and-privacy-changes-in-v0-5-3|2 Safety and Privacy changes in v0.5.3]] · Digest
- 2025-09-15 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-09-15-3-safety-and-privacy-changes-in-rust-v0-36-0|3 Safety and Privacy changes in rust-v0.36.0]] · Digest
- 2025-09-10 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-09-10-ci-build-faster-tests-with-nextest-add-shear-minor-macos-permission-adjustment|CI/Build: faster tests with nextest, add shear; minor macOS permission adjustment]] · Change
- 2025-09-09 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-09-09-2-safety-and-privacy-changes-in-v0-4-0|2 Safety and Privacy changes in v0.4.0]] · Digest
- 2025-09-05 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-09-05-3128-mcp-sandbox-call|♯3128 MCP sandbox call]] · Change
- 2025-09-04 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-09-04-2-safety-and-privacy-changes-in-v0-3-0|2 Safety and Privacy changes in v0.3.0]] · Digest

**2025-08**

- 2025-08-26 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-08-26-2587-do-not-show-timeouts-as-sandbox-error-s|♯2587 do not show timeouts as "sandbox error"s]] · Change
- 2025-08-20 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-08-20-2464-https-github-com-openai-codex-pull-2464-docs-document-writable-roots-for-sa|♯2464((source link) docs: document writable_roots…]] · Change
- 2025-08-14 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-08-14-7-safety-and-privacy-changes-in-v0-1-21|7 Safety and Privacy changes in v0.1.21]] · Digest
- 2025-08-13 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-08-13-ensure-sandbox-build-script-is-cross-platform-by-wldoooon-in-https-github-com-go|ensure sandbox build script is cross-platform]] · Change
- 2025-08-12 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-08-12-2-safety-and-privacy-changes-in-v0-1-19|2 Safety and Privacy changes in v0.1.19]] · Digest
- 2025-08-07 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-08-07-new-onboarding-flow-that-uses-sandbox-workspace-write-and-ask-for-approval-on-re|new onboarding flow that uses…]] · Change
- 2025-08-06 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-08-06-4-safety-and-privacy-changes-in-v0-1-18|4 Safety and Privacy changes in v0.1.18]] · Digest
- 2025-08-05 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-08-05-4-safety-and-privacy-changes-in-v0-1-17|4 Safety and Privacy changes in v0.1.17]] · Digest
- 2025-08-02 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-08-02-https-github-com-openai-codex-pull-1705-security-fix-to-ensure-apply-patch-is-ru|(source link) security fix to ensure apply_patch…]] · Change
- 2025-08-02 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-08-02-4-safety-and-privacy-changes-in-v0-1-16|4 Safety and Privacy changes in v0.1.16]] · Digest

**2025-07**

- 2025-07-30 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-07-30-migrate-privacy-to-new-architecture-by-abhipatel12-in-https-github-com-google-ge|Migrate /privacy to new architecture]] · Change
- 2025-07-29 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-07-29-2-safety-and-privacy-changes-in-1-3|2 Safety and Privacy changes in 1.3]] · Digest
- 2025-07-25 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-07-25-migrate-privacy-to-new-architecture-by-abhipatel12-in-https-github-com-google-ge|Migrate /privacy to new architecture]] · Change
- 2025-07-19 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-07-19-migrate-privacy-to-new-architecture-by-abhipatel12-in-https-github-com-google-ge|Migrate /privacy to new architecture]] · Change
- 2025-07-11 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-07-11-update-terms-of-service-and-privacy-notice-for-clarity-by-jkcinouye-in-https-git|Update Terms of Service and Privacy Notice for clarity]] · Change
- 2025-07-08 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-07-08-adds-support-for-a-sandbox-flag-and-makes-some-breaking-changes-to-config-toml-a|Adds support for a --sandbox flag and makes some breaking changes to config.toml…]] · Change
- 2025-07-01 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-07-01-esc-to-exit-privacy-screen-in-error-state-by-scidomino-in-https-github-com-googl|Esc to exit privacy screen in error state]] · Change

**2025-06**

- 2025-06-20 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2025-06-20-daytona-runtime-sandbox-handling-by-idagelic-in-https-github-com-all-hands-ai-op|Daytona Runtime sandbox handling]] · Change
- 2025-06-20 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2025-06-20-support-for-dev-container-networking-without-host-mode-by-llamantino-in-https-gi|Support for dev container networking without host mode by @llamantino…]] · Change
- 2025-06-20 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2025-06-20-enhanced-security-by-ensuring-redirect-uri-is-https-unless-it-is-for-localhost-b|Enhanced security by ensuring redirect URI is HTTPS unless it is for localhost]] · Change
- 2025-06-04 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-06-04-team-admins-can-now-disable-privacy-mode|Team admins can now disable Privacy Mode]] · Change

**2025-05**

- 2025-05-12 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2025-05-12-simplified-workspace-mounting-with-sandbox-volumes-by-xingyaoww-in-https-github|Simplified workspace mounting with SANDBOX_VOLUMES]] · Change

**2025-04**

- 2025-04-23 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2025-04-23-enabled-custom-sandbox-for-resolver-by-tetsu-is-in-https-github-com-all-hands-ai|Enabled custom sandbox for resolver]] · Change

**2025-03**

- 2025-03-19 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2025-03-19-feat-microagents-add-security-microagent-by-h55nick-in-https-github-com-all-hand|feat(microagents): Add security microagent]] · Change
- 2025-03-18 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-03-18-more-clear-and-private-incognito-keyboard-for-temporary-chats|More clear and private Incognito keyboard for Temporary Chats]] · Change
- 2025-03-18 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-03-18-new-ui-for-temporary-chats-we-ve-made-accessing-and-viewing-these-private-conver|New UI for Temporary Chats]] · Change
- 2025-03-13 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2025-03-13-added-ignore-permission-denied-option-to-file-watcher-to-prevent-errors-when-acc|Added ignore_permission_denied option to file watcher to prevent errors…]] · Change

</details>

</details>

<details class="disclosure">
<summary>2024 · 14 entries (Aider 1 · Cline 1 · Cursor 2 · OpenHands 10)</summary>

**2024-12**

- 2024-12-18 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2024-12-18-cline-s-most-requested-feature-is-here-you-can-now-let-cline-work-more-autonomou|Cline's most requested feature is here 🎉 You can now let Cline work more…]] · Change
- 2024-12-04 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2024-12-04-support-custom-sandbox-for-resolver-by-malhotra5-in-https-github-com-all-hands-a|Support custom sandbox for resolver]] · Change

**2024-10**

- 2024-10-17 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2024-10-17-add-modal-sandbox-support-as-a-new-runtime-by-pawalt-in-https-github-com-all-han|Add Modal sandbox support as a new runtime]] · Change
- 2024-10-09 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2024-10-09-update-0-42-1-0-42-5-fixes-the-following-upstream-security-issue-cve-2024-43601|UPDATE (0.42.1 - 0.42.5): Fixes the following upstream security issue: CVE-2024-43601]] · Change

**2024-09**

- 2024-09-17 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2024-09-17-this-update-fixes-the-following-security-issue-cve-2024-45599|This update fixes the following security issue: CVE-2024-45599]] · Change

**2024-08**

- 2024-08-23 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2024-08-23-3-safety-and-privacy-changes-in-0-9-0|3 Safety and Privacy changes in 0.9.0]] · Digest
- 2024-08-01 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2024-08-01-2-safety-and-privacy-changes-in-0-8-3|2 Safety and Privacy changes in 0.8.3]] · Digest

**2024-07**

- 2024-07-31 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-07-31-resolved-permission-issues-when-using-docker-run-user-xxx|Resolved permission issues when using docker run --user xxx]] · Change
- 2024-07-27 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2024-07-27-fix-update-swebenchsshbox-after-global-config-was-removed-from-sandbox-by-rajwor|FIX Update SWEBenchSSHBox after global config was removed…]] · Change
- 2024-07-19 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2024-07-19-2-safety-and-privacy-changes-in-0-8-1|2 Safety and Privacy changes in 0.8.1]] · Digest
- 2024-07-13 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2024-07-13-6-safety-and-privacy-changes-in-0-8-0|6 Safety and Privacy changes in 0.8.0]] · Digest
- 2024-07-05 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2024-07-05-2-safety-and-privacy-changes-in-0-7-1|2 Safety and Privacy changes in 0.7.1]] · Digest

**2024-06**

- 2024-06-29 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2024-06-29-12-safety-and-privacy-changes-in-0-7-0|12 Safety and Privacy changes in 0.7.0]] · Digest
- 2024-06-04 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2024-06-04-2-safety-and-privacy-changes-in-0-6-1|2 Safety and Privacy changes in 0.6.1]] · Digest

</details>

<details class="disclosure" open>
<summary>2023 · 5 entries (Aider 1 · ChatGPT 1 · Cursor 3)</summary>

**2023-08**

- 2023-08-28 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2023-08-28-today-we-re-launching-chatgpt-enterprise-which-offers-enterprise-grade-security-4958cf|Introducing ChatGPT Enterprise]] · Launch

<details class="disclosure">
<summary>Fixes, digests and other changes · 4 (Aider 1 · Cursor 3)</summary>

**2023-08**

- 2023-08-30 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2023-08-30-api-key-input-box-is-now-a-password-type|API Key input box is now a password type]] · Change

**2023-07**

- 2023-07-24 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2023-07-24-encourage-gpt-to-use-language-like-add-files-to-the-chat-to-ask-users-for-permis|Encourage GPT to use language like "add files to the chat" to ask users…]] · Change

**2023-06**

- 2023-06-27 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2023-06-27-cursor-is-now-based-on-version-1-79-2-of-vscodium-which-comes-with-security-upda|Cursor is now based on version 1.79.2 of VSCodium, which comes with security updates…]] · Change

**2023-04**

- 2023-04-16 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]] · Change

</details>

</details>

</div>
<!-- chronolog:end -->