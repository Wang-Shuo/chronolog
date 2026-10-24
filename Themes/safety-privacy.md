---
created: '2023-04-16'
date: '2026-10-23'
description: 'Research question: which safeguards and privacy controls do the tracked
  products add, and for whom?'
machine_hash: 60c64e50c68053891d18a81ec32a753fe24f7d85b4d78411b3d66977d2eaa2c1
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
theme: safety-privacy
title: Safety and Privacy
---

<!-- chronolog:begin region="header" -->
# Safety and Privacy

187 tracked changes across ChatGPT, Claude Code and Cursor · 2023-04-16 → 2026-10-23 · Claude Code averages 7.0 cards per release, Cursor 4.0, ChatGPT 1.7
<!-- chronolog:end -->

## Research summary
<!-- chronolog:begin region="narrative" -->
**Research question: which safeguards and privacy controls do the tracked products add, and for whom?**

ChatGPT's [2023-08-28 Enterprise launch](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#introducing-chatgpt-enterprise) ([[Releases/ChatGPT/chatgpt-2023-08-28-introducing-chatgpt-enterprise-eb7127e6|archived]]) offers enterprise-grade security and privacy. The [2025-09-29 note](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#parental-controls) ([[Releases/ChatGPT/chatgpt-2025-09-29-parental-controls-8b95b69a|archived]]) rolls out parental controls globally, with teen accounts connected to a parent's account, and the [2026-01-20 note](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#rolling-out-age-prediction) ([[Releases/ChatGPT/chatgpt-2026-01-20-rolling-out-age-prediction-2382655a|archived]]) adds an age prediction model on consumer plans that estimates whether an account likely belongs to someone under 18. [Lockdown Mode on 2026-06-04](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#lockdown-mode-is-now-available-to-all-logged-in-users) ([[Releases/ChatGPT/chatgpt-2026-06-04-lockdown-mode-is-now-available-to-all-logged-in-users-f7dcb357|archived]]) becomes available to all logged-in users as an opt-in setting that limits web and external-service access to reduce the risk of data exfiltration from prompt injection, and the [2026-09-21 Privacy Center](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#privacy-center-in-chatgpt) ([[Releases/ChatGPT/chatgpt-2026-09-21-privacy-center-in-chatgpt-ecef9fba|archived]]) gathers information about chat privacy, memory, data use, connected apps and account security for Free, Go, Plus and Pro users.

Cursor's [2023-04-16 release](https://cursor.com/changelog/0-2-4) ([[Releases/Cursor/cursor-2023-04-16-0-2-4-https-cursor-com-changelog-0-2-4-1ed55ed8|archived]]) adds Ghost mode for opting out of storing any kind of data on Cursor's servers. The [2025-09-29 release](https://cursor.com/changelog/1-7) ([[Releases/Cursor/cursor-2025-09-29-1-7-https-cursor-com-changelog-1-7-0a03c0ae|archived]]) runs non-allowlisted commands in a sandbox with read/write access to the workspace and no internet access, which [Cursor 2.0 on 2025-10-29](https://cursor.com/changelog/2-0) ([[Releases/Cursor/cursor-2025-10-29-2-0-https-cursor-com-changelog-2-0-66a8e76e|archived]]) makes the default for agent commands on macOS, and the [2026-02-17 release](https://cursor.com/changelog/2-5) ([[Releases/Cursor/cursor-2026-02-17-2-5-https-cursor-com-changelog-2-5-82892320|archived]]) adds granular network and filesystem access controls to the sandbox. The [2026-04-30 release](https://cursor.com/changelog/04-30-26) ([[Releases/Cursor/cursor-2026-04-30-cursor-security-review-https-cursor-com-changelog-04-30-26-640898b1|archived]]) adds a Security Reviewer, in beta for Teams and Enterprise, that checks every pull request for security vulnerabilities, privacy and data-handling risks and prompt injection.

Claude Code's [v2.1.83 on 2026-03-25](https://github.com/anthropics/claude-code/releases/tag/v2.1.83) ([[Releases/Claude Code/claude-code-2026-03-25-v2-1-83-github-301019202-ba6a8317|archived]]) adds a setting that strips Anthropic and cloud-provider credentials from subprocess environments, and [v2.1.136 on 2026-05-08](https://github.com/anthropics/claude-code/releases/tag/v2.1.136) ([[Releases/Claude Code/claude-code-2026-05-08-v2-1-136-github-319609716-58f21368|archived]]) adds auto mode classifier rules that block actions unconditionally. [v2.1.187 on 2026-06-23](https://github.com/anthropics/claude-code/releases/tag/v2.1.187) ([[Releases/Claude Code/claude-code-2026-06-23-v2-1-187-github-343665388-744f9775|archived]]) blocks sandboxed commands from reading credential files and secret environment variables, [v2.1.200 on 2026-07-03](https://github.com/anthropics/claude-code/releases/tag/v2.1.200) ([[Releases/Claude Code/claude-code-2026-07-03-v2-1-200-github-348415228-64d6d68d|archived]]) renames the “default” permission mode to “Manual”, and [v2.1.284 on 2026-09-28](https://github.com/anthropics/claude-code/releases/tag/v2.1.284) ([[Releases/Claude Code/claude-code-2026-09-28-v2-1-284-github-398457074-cbb49e49|archived]]) starts interactive terminal and VS Code sessions in auto mode when no permission mode is configured, on every plan and provider.

**Uncertainty and scope:** the record covers the three tracked products only and Claude Code coverage starts on 2025-12-19; the controls serve different users, from families and workspace admins to developers running agents, and rollouts vary by plan and region, so the announcements neither measure how well a safeguard works nor compare protection across products.
<!-- chronolog:end -->

## Key moments
<!-- chronolog:begin region="moments" -->
Auto-selected; edit `key_moments` in editorial.yaml to curate.

| Quarter | ChatGPT | Claude Code | Cursor |
| --- | --- | --- | --- |
| 2026 Q3 | 2026-09-25 [[Changes/ChatGPT/2026-09-25-we-re-introducing-security-history-a-new-way-to-review-recent-security-activity-6f32cc\|Security history in ChatGPT]] | · | 2026-09-23 [[Changes/Cursor/2026-09-23-today-we-re-launching-two-cursor-bots-for-the-last-mile-of-shipping-code-rollout-af394f\|Cursor launches two Cursor bots for the last mile of shipping code]] |
| 2026 Q2 | 2026-06-04 [[Changes/ChatGPT/2026-06-04-lockdown-mode-is-now-available-to-all-logged-in-users-across-account-types-and-w\|Lockdown Mode is now available to all logged-in users]] | 2026-04-16 [[Changes/Claude Code/2026-04-16-added-less-permission-prompts-skill-scans-transcripts-for-common-read-only-bash\|Added /less-permission-prompts skill]] | 2026-06-10 [[Changes/Cursor/2026-06-10-run-bugbot-before-you-push-3e5964\|Run Bugbot before you push]]<br>2026-06-04 [[Changes/Cursor/2026-06-04-custom-tools-056918\|Custom tools]]<br>2026-05-13 [[Changes/Cursor/2026-05-13-environment-governance-and-security-controls\|Environment governance and security controls]]<br>2026-04-30 [[Changes/Cursor/2026-04-30-security-reviewer-checks-every-pr-for-security-vulnerabilities-auth-regressions\|Security Reviewer]] |
| 2026 Q1 | · | · | 2026-02-17 [[Changes/Cursor/2026-02-17-sandbox-network-access-controls\|Sandbox network access controls]] |
| 2025 Q4 | · | · | 2025-10-29 [[Changes/Cursor/2025-10-29-sandboxed-terminals-ga\|Sandboxed Terminals (GA)]] |
| 2025 Q3 | · | · | 2025-09-29 [[Changes/Cursor/2025-09-29-sandboxed-terminals\|Sandboxed terminals]] |
| 2023 Q3 | 2023-08-28 [[Changes/ChatGPT/2023-08-28-today-we-re-launching-chatgpt-enterprise-which-offers-enterprise-grade-security-4958cf\|Introducing ChatGPT Enterprise]] | · | · |
<!-- chronolog:end -->

<!-- chronolog:begin region="scope" -->
> [!info]- How to read this timeline
> Scope: tracked-products-only. Entries show same-theme chronology; they do not establish equivalent capabilities, adoption, or causation.
<!-- chronolog:end -->

## Timeline
<!-- chronolog:begin region="timeline" -->
### 2026 · 173 entries (ChatGPT 8 · Claude Code 146 · Cursor 19)

#### 2026-10

- 2026-10-23 · **Claude Code** · [[Changes/Claude Code/2026-10-23-4-safety-and-privacy-changes-in-v2-1-310|4 Safety and Privacy changes in v2.1.310]] · Digest
- 2026-10-22 · **Claude Code** · [[Changes/Claude Code/2026-10-22-8-safety-and-privacy-changes-in-v2-1-309|8 Safety and Privacy changes in v2.1.309]] · Digest
- 2026-10-21 · **Claude Code** · [[Changes/Claude Code/2026-10-21-added-the-claude-code-safety-event-opentelemetry-event-for-each-tool-call-a-perm|Added the claude_code.safety_event OpenTelemetry event for each tool call…]]
- 2026-10-20 · **Claude Code** · [[Changes/Claude Code/2026-10-20-3-safety-and-privacy-changes-in-v2-1-305|3 Safety and Privacy changes in v2.1.305]] · Digest
- 2026-10-19 · **Claude Code** · [[Changes/Claude Code/2026-10-19-added-decider-person-to-a-mod-s-tool-check-answer-only-the-permission-dialog-or|Added decider: "person" to a mod's tool.check answer: only the permission dialog…]]
- 2026-10-16 · **Claude Code** · [[Changes/Claude Code/2026-10-16-2-safety-and-privacy-changes-in-v2-1-302|2 Safety and Privacy changes in v2.1.302]] · Digest
- 2026-10-15 · **Claude Code** · [[Changes/Claude Code/2026-10-15-5-safety-and-privacy-changes-in-v2-1-301|5 Safety and Privacy changes in v2.1.301]] · Digest
- 2026-10-14 · **Claude Code** · [[Changes/Claude Code/2026-10-14-2-safety-and-privacy-changes-in-v2-1-300|2 Safety and Privacy changes in v2.1.300]] · Digest
- 2026-10-14 · **Claude Code** · [[Changes/Claude Code/2026-10-14-6-safety-and-privacy-changes-in-v2-1-299|6 Safety and Privacy changes in v2.1.299]] · Digest
- 2026-10-13 · **Cursor** · [[Changes/Cursor/2026-10-13-origin-now-integrates-with-over-20-apps-for-deployments-ci-code-review-security|Origin now integrates with over 20 apps for deployments, CI, code review, security…]]
- 2026-10-09 · **Claude Code** · [[Changes/Claude Code/2026-10-09-4-safety-and-privacy-changes-in-v2-1-296|4 Safety and Privacy changes in v2.1.296]] · Digest
- 2026-10-08 · **Claude Code** · [[Changes/Claude Code/2026-10-08-5-safety-and-privacy-changes-in-v2-1-295|5 Safety and Privacy changes in v2.1.295]] · Digest
- 2026-10-07 · **Claude Code** · [[Changes/Claude Code/2026-10-07-3-safety-and-privacy-changes-in-v2-1-293|3 Safety and Privacy changes in v2.1.293]] · Digest
- 2026-10-06 · **Claude Code** · [[Changes/Claude Code/2026-10-06-6-safety-and-privacy-changes-in-v2-1-292|6 Safety and Privacy changes in v2.1.292]] · Digest
- 2026-10-06 · **Claude Code** · [[Changes/Claude Code/2026-10-06-fixed-a-regression-in-2-1-290-where-cloud-sessions-could-drop-answers-to-permiss|Fixed a regression in 2.1.290 where cloud sessions could drop answers to permission…]]
- 2026-10-05 · **Claude Code** · [[Changes/Claude Code/2026-10-05-19-safety-and-privacy-changes-in-v2-1-290|19 Safety and Privacy changes in v2.1.290]] · Digest
- 2026-10-02 · **Claude Code** · [[Changes/Claude Code/2026-10-02-6-safety-and-privacy-changes-in-v2-1-288|6 Safety and Privacy changes in v2.1.288]] · Digest
- 2026-10-01 · **Claude Code** · [[Changes/Claude Code/2026-10-01-6-safety-and-privacy-changes-in-v2-1-287|6 Safety and Privacy changes in v2.1.287]] · Digest

#### 2026-09

- 2026-09-30 · **Claude Code** · [[Changes/Claude Code/2026-09-30-4-safety-and-privacy-changes-in-v2-1-286|4 Safety and Privacy changes in v2.1.286]] · Digest
- 2026-09-29 · **Claude Code** · [[Changes/Claude Code/2026-09-29-9-safety-and-privacy-changes-in-v2-1-285|9 Safety and Privacy changes in v2.1.285]] · Digest
- 2026-09-28 · **Claude Code** · [[Changes/Claude Code/2026-09-28-4-safety-and-privacy-changes-in-v2-1-284|4 Safety and Privacy changes in v2.1.284]] · Digest
- 2026-09-25 · **ChatGPT** · [[Changes/ChatGPT/2026-09-25-we-re-introducing-security-history-a-new-way-to-review-recent-security-activity-6f32cc|Security history in ChatGPT]] · Launch
- 2026-09-25 · **Claude Code** · [[Changes/Claude Code/2026-09-25-3-safety-and-privacy-changes-in-v2-1-283|3 Safety and Privacy changes in v2.1.283]] · Digest
- 2026-09-24 · **Claude Code** · [[Changes/Claude Code/2026-09-24-4-safety-and-privacy-changes-in-v2-1-282|4 Safety and Privacy changes in v2.1.282]] · Digest
- 2026-09-23 · **Claude Code** · [[Changes/Claude Code/2026-09-23-12-safety-and-privacy-changes-in-v2-1-281|12 Safety and Privacy changes in v2.1.281]] · Digest
- 2026-09-23 · **Cursor** · [[Changes/Cursor/2026-09-23-2-safety-and-privacy-changes-in-rollouts-and-security-review|2 Safety and Privacy changes in Rollouts and Security Review]] · Digest
- 2026-09-23 · **Cursor** · [[Changes/Cursor/2026-09-23-today-we-re-launching-two-cursor-bots-for-the-last-mile-of-shipping-code-rollout-af394f|Cursor launches two Cursor bots for the last mile of shipping code]] · Launch
- 2026-09-23 · **Cursor** · [[Changes/Cursor/2026-09-23-security-review|Security Review]] · Launch
- 2026-09-23 · **Cursor** · [[Changes/Cursor/2026-09-23-findings|Findings]] · Launch
- 2026-09-22 · **Claude Code** · [[Changes/Claude Code/2026-09-22-2-safety-and-privacy-changes-in-v2-1-280|2 Safety and Privacy changes in v2.1.280]] · Digest
- 2026-09-21 · **ChatGPT** · [[Changes/ChatGPT/2026-09-21-privacy-center-is-rolling-out-to-signed-in-chatgpt-free-go-plus-and-pro-users-it-0d2f36|Privacy Center in ChatGPT]]
- 2026-09-18 · **Claude Code** · [[Changes/Claude Code/2026-09-18-4-safety-and-privacy-changes-in-v2-1-277|4 Safety and Privacy changes in v2.1.277]] · Digest
- 2026-09-17 · **Claude Code** · [[Changes/Claude Code/2026-09-17-7-safety-and-privacy-changes-in-v2-1-275|7 Safety and Privacy changes in v2.1.275]] · Digest
- 2026-09-17 · **Claude Code** · [[Changes/Claude Code/2026-09-17-3-safety-and-privacy-changes-in-v2-1-274|3 Safety and Privacy changes in v2.1.274]] · Digest
- 2026-09-15 · **Claude Code** · [[Changes/Claude Code/2026-09-15-5-safety-and-privacy-changes-in-v2-1-273|5 Safety and Privacy changes in v2.1.273]] · Digest
- 2026-09-14 · **ChatGPT** · [[Changes/ChatGPT/2026-09-14-if-you-make-no-changes-to-your-plugins-settings-the-default-permission-setting-i|If you make no changes to your Plugins settings, the default permission setting…]]
- 2026-09-14 · **Claude Code** · [[Changes/Claude Code/2026-09-14-7-safety-and-privacy-changes-in-v2-1-271|7 Safety and Privacy changes in v2.1.271]] · Digest
- 2026-09-12 · **Claude Code** · [[Changes/Claude Code/2026-09-12-fixed-read-only-git-commands-in-bash-unexpectedly-asking-for-permission-after-a|Fixed read-only git commands in Bash unexpectedly asking for permission after…]]
- 2026-09-11 · **Claude Code** · [[Changes/Claude Code/2026-09-11-5-safety-and-privacy-changes-in-v2-1-269|5 Safety and Privacy changes in v2.1.269]] · Digest
- 2026-09-10 · **Claude Code** · [[Changes/Claude Code/2026-09-10-8-safety-and-privacy-changes-in-v2-1-268|8 Safety and Privacy changes in v2.1.268]] · Digest
- 2026-09-09 · **Claude Code** · [[Changes/Claude Code/2026-09-09-2-safety-and-privacy-changes-in-v2-1-267|2 Safety and Privacy changes in v2.1.267]] · Digest
- 2026-09-08 · **Claude Code** · [[Changes/Claude Code/2026-09-08-3-safety-and-privacy-changes-in-v2-1-265|3 Safety and Privacy changes in v2.1.265]] · Digest
- 2026-09-04 · **Claude Code** · [[Changes/Claude Code/2026-09-04-4-safety-and-privacy-changes-in-v2-1-261|4 Safety and Privacy changes in v2.1.261]] · Digest
- 2026-09-03 · **Claude Code** · [[Changes/Claude Code/2026-09-03-7-safety-and-privacy-changes-in-v2-1-260|7 Safety and Privacy changes in v2.1.260]] · Digest
- 2026-09-02 · **Claude Code** · [[Changes/Claude Code/2026-09-02-4-safety-and-privacy-changes-in-v2-1-259|4 Safety and Privacy changes in v2.1.259]] · Digest
- 2026-09-01 · **Claude Code** · [[Changes/Claude Code/2026-09-01-fixed-remote-and-scheduled-sessions-failing-with-user-messages-must-have-non-emp|Fixed remote and scheduled sessions failing…]]
- 2026-09-01 · **Claude Code** · [[Changes/Claude Code/2026-09-01-10-safety-and-privacy-changes-in-v2-1-257|10 Safety and Privacy changes in v2.1.257]] · Digest

#### 2026-08

- 2026-08-28 · **Claude Code** · [[Changes/Claude Code/2026-08-28-6-safety-and-privacy-changes-in-v2-1-251|6 Safety and Privacy changes in v2.1.251]] · Digest
- 2026-08-27 · **Claude Code** · [[Changes/Claude Code/2026-08-27-4-safety-and-privacy-changes-in-v2-1-248|4 Safety and Privacy changes in v2.1.248]] · Digest
- 2026-08-26 · **Claude Code** · [[Changes/Claude Code/2026-08-26-2-safety-and-privacy-changes-in-v2-1-247|2 Safety and Privacy changes in v2.1.247]] · Digest
- 2026-08-25 · **Claude Code** · [[Changes/Claude Code/2026-08-25-6-safety-and-privacy-changes-in-v2-1-246|6 Safety and Privacy changes in v2.1.246]] · Digest
- 2026-08-21 · **Claude Code** · [[Changes/Claude Code/2026-08-21-fixed-fullscreen-mode-answering-a-permission-prompt-or-pressing-a-button-when-yo|Fixed fullscreen mode answering a permission prompt or pressing a button when you…]]
- 2026-08-20 · **Claude Code** · [[Changes/Claude Code/2026-08-20-3-safety-and-privacy-changes-in-v2-1-238|3 Safety and Privacy changes in v2.1.238]] · Digest
- 2026-08-19 · **Claude Code** · [[Changes/Claude Code/2026-08-19-2-safety-and-privacy-changes-in-v2-1-236|2 Safety and Privacy changes in v2.1.236]] · Digest
- 2026-08-18 · **Claude Code** · [[Changes/Claude Code/2026-08-18-2-safety-and-privacy-changes-in-v2-1-235|2 Safety and Privacy changes in v2.1.235]] · Digest
- 2026-08-17 · **Claude Code** · [[Changes/Claude Code/2026-08-17-8-safety-and-privacy-changes-in-v2-1-234|8 Safety and Privacy changes in v2.1.234]] · Digest
- 2026-08-14 · **Claude Code** · [[Changes/Claude Code/2026-08-14-3-safety-and-privacy-changes-in-v2-1-233|3 Safety and Privacy changes in v2.1.233]] · Digest
- 2026-08-13 · **Claude Code** · [[Changes/Claude Code/2026-08-13-9-safety-and-privacy-changes-in-v2-1-232|9 Safety and Privacy changes in v2.1.232]] · Digest
- 2026-08-12 · **Claude Code** · [[Changes/Claude Code/2026-08-12-improved-sandbox-ipv6-literals-in-network-domain-lists-are-now-bracketed-1-443-a|Improved sandbox: IPv6 literals in network domain lists are now bracketed…]]
- 2026-08-08 · **Claude Code** · [[Changes/Claude Code/2026-08-08-2-safety-and-privacy-changes-in-v2-1-225|2 Safety and Privacy changes in v2.1.225]] · Digest
- 2026-08-07 · **Claude Code** · [[Changes/Claude Code/2026-08-07-2-safety-and-privacy-changes-in-v2-1-224|2 Safety and Privacy changes in v2.1.224]] · Digest
- 2026-08-06 · **Claude Code** · [[Changes/Claude Code/2026-08-06-3-safety-and-privacy-changes-in-v2-1-223|3 Safety and Privacy changes in v2.1.223]] · Digest
- 2026-08-04 · **Claude Code** · [[Changes/Claude Code/2026-08-04-improved-auto-mode-safety-messages-sent-to-other-agent-sessions-via-sendmessage|Improved auto mode safety]]
- 2026-08-04 · **Claude Code** · [[Changes/Claude Code/2026-08-04-7-safety-and-privacy-changes-in-v2-1-221|7 Safety and Privacy changes in v2.1.221]] · Digest

#### 2026-07

- 2026-07-24 · **Claude Code** · [[Changes/Claude Code/2026-07-24-2-safety-and-privacy-changes-in-v2-1-219|2 Safety and Privacy changes in v2.1.219]] · Digest
- 2026-07-23 · **ChatGPT** · [[Changes/ChatGPT/2026-07-23-health-is-built-with-layered-privacy-and-security-safeguards-connected-medical-r|Health is built with layered privacy and security safeguards]]
- 2026-07-22 · **Claude Code** · [[Changes/Claude Code/2026-07-22-3-safety-and-privacy-changes-in-v2-1-218|3 Safety and Privacy changes in v2.1.218]] · Digest
- 2026-07-21 · **Claude Code** · [[Changes/Claude Code/2026-07-21-fixed-remote-control-sessions-not-showing-a-pending-permission-prompt-or-dialog|Fixed Remote Control sessions not showing a pending permission prompt or dialog…]]
- 2026-07-20 · **Claude Code** · [[Changes/Claude Code/2026-07-20-5-safety-and-privacy-changes-in-v2-1-216|5 Safety and Privacy changes in v2.1.216]] · Digest
- 2026-07-18 · **Claude Code** · [[Changes/Claude Code/2026-07-18-9-safety-and-privacy-changes-in-v2-1-214|9 Safety and Privacy changes in v2.1.214]] · Digest
- 2026-07-17 · **Claude Code** · [[Changes/Claude Code/2026-07-17-3-safety-and-privacy-changes-in-v2-1-212|3 Safety and Privacy changes in v2.1.212]] · Digest
- 2026-07-15 · **Claude Code** · [[Changes/Claude Code/2026-07-15-2-safety-and-privacy-changes-in-v2-1-211|2 Safety and Privacy changes in v2.1.211]] · Digest
- 2026-07-14 · **Claude Code** · [[Changes/Claude Code/2026-07-14-3-safety-and-privacy-changes-in-v2-1-210|3 Safety and Privacy changes in v2.1.210]] · Digest
- 2026-07-14 · **Claude Code** · [[Changes/Claude Code/2026-07-14-fixed-multi-second-per-turn-slowdowns-in-sessions-with-many-permission-deny-ask|Fixed multi-second per-turn slowdowns in sessions with many permission deny/ask rules]]
- 2026-07-11 · **Claude Code** · [[Changes/Claude Code/2026-07-11-2-safety-and-privacy-changes-in-v2-1-207|2 Safety and Privacy changes in v2.1.207]] · Digest
- 2026-07-10 · **Claude Code** · [[Changes/Claude Code/2026-07-10-fixed-permission-prompt-tool-pointing-at-an-mcp-server-crashing-with-mcp-tool-no|Fixed --permission-prompt-tool pointing at an MCP server crashing…]]
- 2026-07-08 · **Claude Code** · [[Changes/Claude Code/2026-07-08-background-task-notifications-now-explicitly-state-that-no-human-input-has-occur|Background task notifications now explicitly state that no human input has occurred…]]
- 2026-07-07 · **Claude Code** · [[Changes/Claude Code/2026-07-07-added-a-grey-badge-to-the-footer-when-in-manual-permission-mode-making-the-activ|Added a grey ⏸ badge to the footer when in manual permission mode, making the active…]]
- 2026-07-06 · **Claude Code** · [[Changes/Claude Code/2026-07-06-fixed-remote-control-sessions-showing-the-wrong-permission-mode-in-the-mobile-an|Fixed /remote-control sessions showing the wrong permission mode in the mobile…]]
- 2026-07-03 · **Claude Code** · [[Changes/Claude Code/2026-07-03-changed-the-default-permission-mode-to-manual-across-the-cli-help-vs-code-and-je|Changed the "default" permission mode to "Manual" across the CLI, --help, VS Code…]]

#### 2026-06

- 2026-06-29 · **Claude Code** · [[Changes/Claude Code/2026-06-29-security-claude-mcp-list-get-no-longer-spawn-mcp-json-servers-that-a-repo-self-a|Security: claude mcp list/get no longer spawn .mcp.json servers that a repo…]]
- 2026-06-26 · **Claude Code** · [[Changes/Claude Code/2026-06-26-fixed-external-plugins-enabled-only-by-project-claude-settings-json-not-requirin|Fixed external plugins enabled only by project .claude/settings.json not requiring…]]
- 2026-06-24 · **Claude Code** · [[Changes/Claude Code/2026-06-24-improved-sandbox-network-permission-dialog-hosts-you-allow-with-yes-are-now-reme|Improved sandbox network permission dialog]]
- 2026-06-23 · **Claude Code** · [[Changes/Claude Code/2026-06-23-2-safety-and-privacy-changes-in-v2-1-187|2 Safety and Privacy changes in v2.1.187]] · Digest
- 2026-06-22 · **Claude Code** · [[Changes/Claude Code/2026-06-22-2-safety-and-privacy-changes-in-v2-1-186|2 Safety and Privacy changes in v2.1.186]] · Digest
- 2026-06-18 · **ChatGPT** · [[Changes/ChatGPT/2026-06-18-app-permission-controls-you-can-now-choose-when-chatgpt-asks-before-using-connec|App permission controls: You can now choose when ChatGPT asks before using connected apps]]
- 2026-06-17 · **Claude Code** · [[Changes/Claude Code/2026-06-17-added-sandbox-allowappleevents-opt-in-setting-that-lets-sandboxed-commands-send|Added sandbox.allowAppleEvents opt-in setting that lets sandboxed commands send…]]
- 2026-06-15 · **Claude Code** · [[Changes/Claude Code/2026-06-15-2-safety-and-privacy-changes-in-v2-1-178|2 Safety and Privacy changes in v2.1.178]] · Digest
- 2026-06-10 · **Claude Code** · [[Changes/Claude Code/2026-06-10-2-safety-and-privacy-changes-in-v2-1-172|2 Safety and Privacy changes in v2.1.172]] · Digest
- 2026-06-10 · **Cursor** · [[Changes/Cursor/2026-06-10-run-bugbot-before-you-push-3e5964|Run Bugbot before you push]] · Launch
- 2026-06-08 · **Claude Code** · [[Changes/Claude Code/2026-06-08-2-safety-and-privacy-changes-in-v2-1-169|2 Safety and Privacy changes in v2.1.169]] · Digest
- 2026-06-06 · **Claude Code** · [[Changes/Claude Code/2026-06-06-hardened-cross-session-messaging-messages-relayed-via-sendmessage-from-other-cla|Hardened cross-session messaging]]
- 2026-06-04 · **ChatGPT** · [[Changes/ChatGPT/2026-06-04-lockdown-mode-is-now-available-to-all-logged-in-users-across-account-types-and-w|Lockdown Mode is now available to all logged-in users]] · Launch
- 2026-06-04 · **Claude Code** · [[Changes/Claude Code/2026-06-04-fixed-org-managed-permission-rules-not-applying-for-the-entire-session-when-the|Fixed org-managed permission rules not applying for the entire session…]]
- 2026-06-04 · **Cursor** · [[Changes/Cursor/2026-06-04-custom-tools-056918|Custom tools]] · Launch
- 2026-06-03 · **Claude Code** · [[Changes/Claude Code/2026-06-03-4-safety-and-privacy-changes-in-v2-1-162|4 Safety and Privacy changes in v2.1.162]] · Digest
- 2026-06-03 · **Cursor** · [[Changes/Cursor/2026-06-03-enterprise-customers-can-now-manage-multiple-cursor-teams-from-one-place-with-di|Enterprise customers can now manage multiple Cursor teams from one place…]]
- 2026-06-02 · **ChatGPT** · [[Changes/ChatGPT/2026-06-02-we-re-rolling-out-active-sessions-a-new-security-feature-in-chatgpt-that-helps-u-51e977|ChatGPT rolls out Active sessions, a new security feature that helps users review…]]

#### 2026-05

- 2026-05-29 · **Claude Code** · [[Changes/Claude Code/2026-05-29-2-safety-and-privacy-changes-in-v2-1-157|2 Safety and Privacy changes in v2.1.157]] · Digest
- 2026-05-28 · **Claude Code** · [[Changes/Claude Code/2026-05-28-2-safety-and-privacy-changes-in-v2-1-153|2 Safety and Privacy changes in v2.1.153]] · Digest
- 2026-05-27 · **Claude Code** · [[Changes/Claude Code/2026-05-27-2-safety-and-privacy-changes-in-v2-1-152|2 Safety and Privacy changes in v2.1.152]] · Digest
- 2026-05-22 · **Claude Code** · [[Changes/Claude Code/2026-05-22-2-safety-and-privacy-changes-in-v2-1-149|2 Safety and Privacy changes in v2.1.149]] · Digest
- 2026-05-19 · **Claude Code** · [[Changes/Claude Code/2026-05-19-fixed-a-permission-prompt-bypass-where-bare-variable-assignments-to-non-allowlis|Fixed a permission-prompt bypass where bare variable assignments to non-allowlisted…]]
- 2026-05-19 · **Claude Code** · [[Changes/Claude Code/2026-05-19-fixed-skill-tool-failing-with-permission-error-in-headless-mode-regression-in-v2|Fixed Skill tool failing with permission error in headless mode (regression in v2.1.141)]]
- 2026-05-15 · **Claude Code** · [[Changes/Claude Code/2026-05-15-3-safety-and-privacy-changes-in-v2-1-143|3 Safety and Privacy changes in v2.1.143]] · Digest
- 2026-05-14 · **Claude Code** · [[Changes/Claude Code/2026-05-14-added-new-claude-agents-flags-add-dir-settings-mcp-config-plugin-dir-permission|Added new claude agents flags]]
- 2026-05-13 · **Claude Code** · [[Changes/Claude Code/2026-05-13-5-safety-and-privacy-changes-in-v2-1-141|5 Safety and Privacy changes in v2.1.141]] · Digest
- 2026-05-13 · **Cursor** · [[Changes/Cursor/2026-05-13-environment-governance-and-security-controls|Environment governance and security controls]] · Launch
- 2026-05-11 · **Claude Code** · [[Changes/Claude Code/2026-05-11-fixed-skill-name-permission-rules-the-wildcard-form-now-works-as-a-prefix-match|Fixed Skill(name ) permission rules]]
- 2026-05-08 · **Claude Code** · [[Changes/Claude Code/2026-05-08-2-safety-and-privacy-changes-in-v2-1-136|2 Safety and Privacy changes in v2.1.136]] · Digest
- 2026-05-07 · **ChatGPT** · [[Changes/ChatGPT/2026-05-07-over-the-coming-weeks-we-ll-be-rolling-out-trusted-contact-an-optional-safety-fe|Trusted contact in ChatGPT]]
- 2026-05-07 · **Claude Code** · [[Changes/Claude Code/2026-05-07-added-sandbox-bwrappath-and-sandbox-socatpath-managed-settings-linux-wsl-to-spec|Added sandbox.bwrapPath and sandbox.socatPath managed settings (Linux/WSL)…]]
- 2026-05-06 · **Claude Code** · [[Changes/Claude Code/2026-05-06-fixed-permission-mode-flag-being-ignored-when-resuming-a-plan-mode-session-with|Fixed --permission-mode flag being ignored when resuming a plan-mode session…]]
- 2026-05-06 · **Claude Code** · [[Changes/Claude Code/2026-05-06-fixed-session-title-chip-from-rename-disappearing-while-a-permission-or-other-di|Fixed session title chip from /rename disappearing while a permission or other…]]
- 2026-05-04 · **Claude Code** · [[Changes/Claude Code/2026-05-04-sdk-hosts-now-receive-a-persistent-localsettings-suggestion-for-bash-permission|SDK hosts now receive a persistent localSettings suggestion for Bash permission…]]
- 2026-05-01 · **Claude Code** · [[Changes/Claude Code/2026-05-01-3-safety-and-privacy-changes-in-v2-1-126|3 Safety and Privacy changes in v2.1.126]] · Digest
- 2026-05-01 · **Cursor** · [[Changes/Cursor/2026-05-01-default-off-users-can-discover-and-opt-in|Default Off: users can discover and opt in]]

#### 2026-04

- 2026-04-30 · **Cursor** · [[Changes/Cursor/2026-04-30-cursor-security-review-is-now-in-beta-on-teams-and-enterprise-plans-you-can-run|Cursor Security Review is now in beta on Teams and Enterprise plans]]
- 2026-04-30 · **Cursor** · [[Changes/Cursor/2026-04-30-security-reviewer-checks-every-pr-for-security-vulnerabilities-auth-regressions|Security Reviewer]] · Launch
- 2026-04-30 · **Cursor** · [[Changes/Cursor/2026-04-30-vulnerability-scanner-b19b70|Vulnerability Scanner]] · Launch
- 2026-04-23 · **Claude Code** · [[Changes/Claude Code/2026-04-23-fixed-mcp-step-up-authorization-silently-refreshing-instead-of-prompting-for-re|Fixed MCP step-up authorization silently refreshing instead of prompting…]]
- 2026-04-23 · **Claude Code** · [[Changes/Claude Code/2026-04-23-4-safety-and-privacy-changes-in-v2-1-119|4 Safety and Privacy changes in v2.1.119]] · Digest
- 2026-04-20 · **Claude Code** · [[Changes/Claude Code/2026-04-20-security-sandbox-auto-allow-no-longer-bypasses-the-dangerous-path-safety-check-f|Security: sandbox auto-allow no longer bypasses the dangerous-path safety check…]]
- 2026-04-18 · **Claude Code** · [[Changes/Claude Code/2026-04-18-fixed-a-crash-in-the-permission-dialog-when-an-agent-teams-teammate-requested-to|Fixed a crash in the permission dialog when an agent teams teammate requested tool…]]
- 2026-04-17 · **Claude Code** · [[Changes/Claude Code/2026-04-17-6-safety-and-privacy-changes-in-v2-1-113|6 Safety and Privacy changes in v2.1.113]] · Digest
- 2026-04-16 · **Claude Code** · [[Changes/Claude Code/2026-04-16-added-less-permission-prompts-skill-scans-transcripts-for-common-read-only-bash|Added /less-permission-prompts skill]]
- 2026-04-16 · **Claude Code** · [[Changes/Claude Code/2026-04-16-2-safety-and-privacy-changes-in-v2-1-111|2 Safety and Privacy changes in v2.1.111]] · Digest
- 2026-04-14 · **Claude Code** · [[Changes/Claude Code/2026-04-14-2-safety-and-privacy-changes-in-v2-1-108|2 Safety and Privacy changes in v2.1.108]] · Digest
- 2026-04-13 · **Claude Code** · [[Changes/Claude Code/2026-04-13-fixed-bash-tool-suggesting-acceptedits-permission-mode-when-exiting-plan-mode-wo|Fixed Bash tool suggesting acceptEdits permission mode when exiting plan mode…]]
- 2026-04-10 · **Claude Code** · [[Changes/Claude Code/2026-04-10-fixed-a-command-injection-vulnerability-in-the-posix-which-fallback-used-by-lsp|Fixed a command injection vulnerability in the POSIX which fallback used by LSP…]]
- 2026-04-09 · **Claude Code** · [[Changes/Claude Code/2026-04-09-6-safety-and-privacy-changes-in-v2-1-98|6 Safety and Privacy changes in v2.1.98]] · Digest
- 2026-04-08 · **Claude Code** · [[Changes/Claude Code/2026-04-08-3-safety-and-privacy-changes-in-v2-1-97|3 Safety and Privacy changes in v2.1.97]] · Digest
- 2026-04-07 · **Claude Code** · [[Changes/Claude Code/2026-04-07-vscode-added-a-warning-banner-when-settings-json-files-fail-to-parse-so-users-kn|VSCode Added a warning banner when settings.json files fail to parse, so users…]]
- 2026-04-04 · **Claude Code** · [[Changes/Claude Code/2026-04-04-linux-sandbox-now-ships-the-apply-seccomp-helper-in-both-npm-and-native-builds-r|Linux sandbox now ships the apply-seccomp helper in both npm and native builds…]]
- 2026-04-02 · **Claude Code** · [[Changes/Claude Code/2026-04-02-fixed-plan-mode-in-remote-sessions-losing-track-of-the-plan-file-after-a-contain|Fixed plan mode in remote sessions losing track of the plan file after a container…]]
- 2026-04-01 · **Claude Code** · [[Changes/Claude Code/2026-04-01-2-safety-and-privacy-changes-in-v2-1-89|2 Safety and Privacy changes in v2.1.89]] · Digest
- 2026-04-01 · **Claude Code** · [[Changes/Claude Code/2026-04-01-4-safety-and-privacy-changes-in-v2-1-90|4 Safety and Privacy changes in v2.1.90]] · Digest

#### 2026-03

- 2026-03-27 · **Claude Code** · [[Changes/Claude Code/2026-03-27-fixed-official-marketplace-plugin-scripts-failing-with-permission-denied-on-maco|Fixed official marketplace plugin scripts failing…]]
- 2026-03-26 · **Claude Code** · [[Changes/Claude Code/2026-03-26-fixed-the-allow-claude-to-edit-its-own-settings-for-this-session-permission-opti|Fixed the "allow Claude to edit its own settings for this session" permission option…]]
- 2026-03-26 · **Claude Code** · [[Changes/Claude Code/2026-03-26-2-safety-and-privacy-changes-in-v2-1-85|2 Safety and Privacy changes in v2.1.85]] · Digest
- 2026-03-25 · **Claude Code** · [[Changes/Claude Code/2026-03-25-2-safety-and-privacy-changes-in-v2-1-83|2 Safety and Privacy changes in v2.1.83]] · Digest
- 2026-03-20 · **Claude Code** · [[Changes/Claude Code/2026-03-20-2-safety-and-privacy-changes-in-v2-1-81|2 Safety and Privacy changes in v2.1.81]] · Digest
- 2026-03-18 · **Claude Code** · [[Changes/Claude Code/2026-03-18-fixed-custom-status-line-showing-nothing-when-workspace-trust-is-blocking-it|Fixed custom status line showing nothing when workspace trust is blocking it]]
- 2026-03-17 · **Claude Code** · [[Changes/Claude Code/2026-03-17-2-safety-and-privacy-changes-in-v2-1-78|2 Safety and Privacy changes in v2.1.78]] · Digest
- 2026-03-17 · **Claude Code** · [[Changes/Claude Code/2026-03-17-3-safety-and-privacy-changes-in-v2-1-77|3 Safety and Privacy changes in v2.1.77]] · Digest
- 2026-03-14 · **Claude Code** · [[Changes/Claude Code/2026-03-14-3-safety-and-privacy-changes-in-v2-1-76|3 Safety and Privacy changes in v2.1.76]] · Digest
- 2026-03-12 · **Claude Code** · [[Changes/Claude Code/2026-03-12-fixed-voice-mode-silently-failing-on-the-macos-native-binary-for-users-whose-ter|Fixed voice mode silently failing on the macOS native binary for users whose…]]
- 2026-03-11 · **Claude Code** · [[Changes/Claude Code/2026-03-11-fixed-freezes-and-100-cpu-loops-triggered-by-permission-prompts-for-complex-bash|Fixed freezes and 100% CPU loops triggered by permission prompts for complex bash commands]]
- 2026-03-10 · **Claude Code** · [[Changes/Claude Code/2026-03-10-6-safety-and-privacy-changes-in-v2-1-72|6 Safety and Privacy changes in v2.1.72]] · Digest
- 2026-03-07 · **Claude Code** · [[Changes/Claude Code/2026-03-07-fixed-false-positive-permission-prompts-for-compound-bash-commands-containing-he|Fixed false-positive permission prompts for compound bash commands containing…]]
- 2026-03-05 · **Claude Code** · [[Changes/Claude Code/2026-03-05-5-safety-and-privacy-changes-in-v2-1-69|5 Safety and Privacy changes in v2.1.69]] · Digest
- 2026-03-05 · **Cursor** · [[Changes/Cursor/2026-03-05-when-invoked-the-agent-spins-up-a-cloud-sandbox-and-follows-your-instructions-us|When invoked, the agent spins up a cloud sandbox and follows your instructions using…]]
- 2026-03-03 · **Cursor** · [[Changes/Cursor/2026-03-03-fixed-team-permission-and-access-control-inconsistencies-across-organization-set|Fixed team permission and access control inconsistencies across organization setups]]

#### 2026-02

- 2026-02-28 · **Claude Code** · [[Changes/Claude Code/2026-02-28-fixed-listener-leak-in-interactive-permission-handler-during-auto-approvals|Fixed listener leak in interactive permission handler during auto-approvals]]
- 2026-02-24 · **Claude Code** · [[Changes/Claude Code/2026-02-24-3-safety-and-privacy-changes-in-v2-1-51|3 Safety and Privacy changes in v2.1.51]] · Digest
- 2026-02-19 · **Claude Code** · [[Changes/Claude Code/2026-02-19-3-safety-and-privacy-changes-in-v2-1-49|3 Safety and Privacy changes in v2.1.49]] · Digest
- 2026-02-18 · **Claude Code** · [[Changes/Claude Code/2026-02-18-2-safety-and-privacy-changes-in-v2-1-47|2 Safety and Privacy changes in v2.1.47]] · Digest
- 2026-02-18 · **Cursor** · [[Changes/Cursor/2026-02-18-7-safety-and-privacy-changes-in-cli-improvements-and-mermaid-ascii|7 Safety and Privacy changes in CLI Improvements and Mermaid ASCII…]] · Digest
- 2026-02-17 · **Claude Code** · [[Changes/Claude Code/2026-02-17-vscode-improved-permission-destination-choice-project-user-session-to-persist-ac|VSCode Improved permission destination choice (project/user/session) to persist…]]
- 2026-02-17 · **Cursor** · [[Changes/Cursor/2026-02-17-sandbox-network-access-controls|Sandbox network access controls]] · Launch
- 2026-02-17 · **Cursor** · [[Changes/Cursor/2026-02-17-3-safety-and-privacy-changes-in-2-5|3 Safety and Privacy changes in 2.5]] · Digest
- 2026-02-13 · **Claude Code** · [[Changes/Claude Code/2026-02-13-2-safety-and-privacy-changes-in-v2-1-41|2 Safety and Privacy changes in v2.1.41]] · Digest
- 2026-02-10 · **Claude Code** · [[Changes/Claude Code/2026-02-10-2-safety-and-privacy-changes-in-v2-1-38|2 Safety and Privacy changes in v2.1.38]] · Digest
- 2026-02-06 · **Claude Code** · [[Changes/Claude Code/2026-02-06-fixed-a-bug-where-commands-excluded-from-sandboxing-via-sandbox-excludedcommands|Fixed a bug where commands excluded from sandboxing…]]
- 2026-02-03 · **Claude Code** · [[Changes/Claude Code/2026-02-03-fixed-permission-dialogs-stealing-focus-while-actively-typing|Fixed permission dialogs stealing focus while actively typing]]

#### 2026-01

- 2026-01-30 · **Claude Code** · [[Changes/Claude Code/2026-01-30-permissions-now-respect-content-level-ask-over-tool-level-allow-previously-allow|Permissions now respect content-level ask over tool-level allow]]
- 2026-01-29 · **Claude Code** · [[Changes/Claude Code/2026-01-29-fixed-per-user-temp-directory-isolation-to-prevent-permission-conflicts-on-share|Fixed per-user temp directory isolation to prevent permission conflicts on shared systems]]
- 2026-01-27 · **Claude Code** · [[Changes/Claude Code/2026-01-27-2-safety-and-privacy-changes-in-v2-1-20|2 Safety and Privacy changes in v2.1.20]] · Digest
- 2026-01-22 · **Cursor** · [[Changes/Cursor/2026-01-22-unified-cli-permissions-with-the-editor-including-run-everything-auto-run-in-san|Unified CLI permissions with the editor, including Run Everything, Auto-Run…]]
- 2026-01-14 · **Claude Code** · [[Changes/Claude Code/2026-01-14-2-safety-and-privacy-changes-in-v2-1-7|2 Safety and Privacy changes in v2.1.7]] · Digest
- 2026-01-13 · **Claude Code** · [[Changes/Claude Code/2026-01-13-fixed-permission-bypass-via-shell-line-continuation-that-could-allow-blocked-com|Fixed permission bypass via shell line continuation that could allow blocked…]]
- 2026-01-09 · **Claude Code** · [[Changes/Claude Code/2026-01-09-2-safety-and-privacy-changes-in-v2-1-2|2 Safety and Privacy changes in v2.1.2]] · Digest
- 2026-01-09 · **Claude Code** · [[Changes/Claude Code/2026-01-09-2-safety-and-privacy-changes-in-v2-1-3|2 Safety and Privacy changes in v2.1.3]] · Digest

### 2025 · 8 entries (ChatGPT 3 · Cursor 5)

#### 2025-12

- 2025-12-22 · **Cursor** · [[Changes/Cursor/2025-12-22-improved-stability-around-how-the-agent-respects-auto-run-preferences-to-prevent|Improved stability around how the agent respects auto-run preferences to prevent…]]

#### 2025-10

- 2025-10-29 · **Cursor** · [[Changes/Cursor/2025-10-29-sandboxed-terminals-ga|Sandboxed Terminals (GA)]] · Launch

#### 2025-09

- 2025-09-29 · **ChatGPT** · [[Changes/ChatGPT/2025-09-29-we-re-rolling-out-parental-controls-globally-in-chatgpt-to-help-families-guide-h-289d0a|ChatGPT rolls out parental controls globally to help families guide how ChatGPT…]] · Policy
- 2025-09-29 · **Cursor** · [[Changes/Cursor/2025-09-29-sandboxed-terminals|Sandboxed terminals]] · Launch

#### 2025-07

- 2025-07-29 · **Cursor** · [[Changes/Cursor/2025-07-29-2-safety-and-privacy-changes-in-1-3|2 Safety and Privacy changes in 1.3]] · Digest

#### 2025-06

- 2025-06-04 · **Cursor** · [[Changes/Cursor/2025-06-04-team-admins-can-now-disable-privacy-mode|Team admins can now disable Privacy Mode]]

#### 2025-03

- 2025-03-18 · **ChatGPT** · [[Changes/ChatGPT/2025-03-18-more-clear-and-private-incognito-keyboard-for-temporary-chats|More clear and private Incognito keyboard for Temporary Chats]]
- 2025-03-18 · **ChatGPT** · [[Changes/ChatGPT/2025-03-18-new-ui-for-temporary-chats-we-ve-made-accessing-and-viewing-these-private-conver|New UI for Temporary Chats]]

### 2024 · 2 entries (Cursor 2)

#### 2024-10

- 2024-10-09 · **Cursor** · [[Changes/Cursor/2024-10-09-update-0-42-1-0-42-5-fixes-the-following-upstream-security-issue-cve-2024-43601|UPDATE (0.42.1 - 0.42.5): Fixes the following upstream security issue: CVE-2024-43601]]

#### 2024-09

- 2024-09-17 · **Cursor** · [[Changes/Cursor/2024-09-17-this-update-fixes-the-following-security-issue-cve-2024-45599|This update fixes the following security issue: CVE-2024-45599]]

### 2023 · 4 entries (ChatGPT 1 · Cursor 3)

#### 2023-08

- 2023-08-30 · **Cursor** · [[Changes/Cursor/2023-08-30-api-key-input-box-is-now-a-password-type|API Key input box is now a password type]]
- 2023-08-28 · **ChatGPT** · [[Changes/ChatGPT/2023-08-28-today-we-re-launching-chatgpt-enterprise-which-offers-enterprise-grade-security-4958cf|Introducing ChatGPT Enterprise]] · Launch

#### 2023-06

- 2023-06-27 · **Cursor** · [[Changes/Cursor/2023-06-27-cursor-is-now-based-on-version-1-79-2-of-vscodium-which-comes-with-security-upda|Cursor is now based on version 1.79.2 of VSCodium, which comes with security updates…]]

#### 2023-04

- 2023-04-16 · **Cursor** · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->