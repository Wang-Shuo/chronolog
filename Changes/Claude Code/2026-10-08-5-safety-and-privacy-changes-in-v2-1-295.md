---
card_id: claude-code-2026-10-08-c7b7cd
date: '2026-10-08'
description: 'Claude Code · 2026-10-08 · Safety and Privacy: 5 changes in v2.1.295
  — Fixed Bash permission checks for for-loops over glob patterns, improving…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1271
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 1942c303eb536e87c23a101ec3ea790b346d6ff8135b7468bf640c780efa8629
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-08-c7b7cd
  comparison: ''
  date: '2026-10-08'
  description: 'Claude Code — v2.1.295: 5 Safety and Privacy changes'
  evidence:
  - quote: Fixed Bash permission checks for for-loops over glob patterns, improving
      permission-check accuracy
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.295
  - quote: Fixed cloud sessions hanging when a mod's `session.receive` hook asked
      for permission before passing a message on
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.295
  - quote: Improved the status shown in Remote Control, claude.ai and the desktop
      app for a session waiting on a permission prompt to name an MCP tool by its
      server and readable name instead of its `mcp__server__tool` identifier
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.295
  - quote: Changed the Artifact tool's permission prompts with telemetry disabled
      to the same five questions other installs get, instead of asking before each
      read of someone else's artifact and each data edit
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.295
  - quote: '[VSCode] Fixed Ctrl+Shift+Tab, Cmd+Shift+Tab and Alt+Shift+Tab in the
      chat input also switching the permission mode, and Ctrl+Tab accepting the suggested
      prompt'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.295
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 5-safety-and-privacy-changes-in-v2-1-295
  source_release: claude-code-2026-10-08-v2-1-295-github-407134589-d5c87510
  source_type: github_releases
  theme: safety-privacy
  title: 5 Safety and Privacy changes in v2.1.295
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-06-6-safety-and-privacy-changes-in-v2-1-292|6 Safety
  and Privacy changes in v2.1.292]]'
- '[[Changes/Claude Code/2026-10-06-fixed-a-regression-in-2-1-290-where-cloud-sessions-could-drop-answers-to-permiss|Fixed
  a regression in 2.1.290 where cloud sessions could drop answers to permission…]]'
- '[[Changes/Claude Code/2026-10-07-3-safety-and-privacy-changes-in-v2-1-293|3 Safety
  and Privacy changes in v2.1.293]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-08-v2-1-295-github-407134589-d5c87510|claude-code-2026-10-08-v2-1-295-github-407134589-d5c87510]]'
source_type: github_releases
theme: safety-privacy
title: 5 Safety and Privacy changes in v2.1.295
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Safety and Privacy changes in v2.1.295

**Claude Code** · 2026-10-08 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.295) · from [[Releases/Claude Code/claude-code-2026-10-08-v2-1-295-github-407134589-d5c87510|v2.1.295]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Fixed Bash permission checks for for-loops over glob patterns, improving permission-check accuracy

> Fixed cloud sessions hanging when a mod's `session.receive` hook asked for permission before passing a message on

> Improved the status shown in Remote Control, claude.ai and the desktop app for a session waiting on a permission prompt to name an MCP tool by its server and readable name instead of its `mcp__server__tool` identifier

> Changed the Artifact tool's permission prompts with telemetry disabled to the same five questions other installs get, instead of asking before each read of someone else's artifact and each data edit

> [VSCode] Fixed Ctrl+Shift+Tab, Cmd+Shift+Tab and Alt+Shift+Tab in the chat input also switching the permission mode, and Ctrl+Tab accepting the suggested prompt

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.295
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-08-3-agent-mode-changes-in-v2-1-295|3 Agent Mode changes in v2.1.295]] · Agent Mode
- [[Changes/Claude Code/2026-10-08-added-a-line-on-stderr-when-it-is-a-terminal-that-says-what-a-claude-p-run-is-wa|Added a line on stderr, when it is a terminal, that says what a claude -p run…]] · Developer Workflow
- [[Changes/Claude Code/2026-10-08-improved-token-counts-behind-a-claude-apps-gateway-on-amazon-bedrock-which-conte|Improved token counts behind a Claude apps gateway on Amazon Bedrock…]] · Context Window
- [[Changes/Claude Code/2026-10-08-changed-ctrl-c-at-the-idle-prompt-of-an-attached-background-session-to-leave-a-p|Changed Ctrl+C at the idle prompt of an attached background session to leave…]] · Automation and Scheduling
- [[Changes/Claude Code/2026-10-08-14-apps-and-integrations-changes-in-v2-1-295|14 Apps and Integrations changes in v2.1.295]] · Apps and Integrations
- [[Changes/Claude Code/2026-10-08-added-support-for-forceloginmethod-gateway-and-forcelogingatewayurl-in-your-own|Added support for forceLoginMethod: "gateway" and forceLoginGatewayUrl…]] · Account and Access
- [[Changes/Claude Code/2026-10-08-changed-tab-stops-to-count-from-where-a-text-starts-instead-of-from-the-screen-s|Changed tab stops to count from where a text starts instead of from the screen's left edge]] · Editor Experience
- [[Changes/Claude Code/2026-10-08-2-model-support-changes-in-v2-1-295|2 Model Support changes in v2.1.295]] · Model Support
- [[Changes/Claude Code/2026-10-08-2-interface-experience-changes-in-v2-1-295|2 Interface Experience changes in v2.1.295]] · Interface Experience
- [[Changes/Claude Code/2026-10-08-2-mobile-and-desktop-changes-in-v2-1-295|2 Mobile and Desktop changes in v2.1.295]] · Mobile and Desktop
- [[Changes/Claude Code/2026-10-08-claude-tag-changed-claude-s-notice-that-a-channel-shared-across-enterprise-grid|Claude Tag Changed Claude's notice that a channel shared across Enterprise Grid…]] · Enterprise and Administration
- [[Changes/Claude Code/2026-10-08-15-other-changes-in-v2-1-295|15 other changes in v2.1.295]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-10-07 · Claude Code · [[Changes/Claude Code/2026-10-07-3-safety-and-privacy-changes-in-v2-1-293|3 Safety and Privacy changes in v2.1.293]]
- Later: 2026-10-09 · Claude Code · [[Changes/Claude Code/2026-10-09-4-safety-and-privacy-changes-in-v2-1-296|4 Safety and Privacy changes in v2.1.296]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-08-c7b7cd&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-08-5-safety-and-privacy-changes-in-v2-1-295.md%0ACard%20ID%3A%20claude-code-2026-10-08-c7b7cd%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.295%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->