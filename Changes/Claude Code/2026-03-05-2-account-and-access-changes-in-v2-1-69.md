---
card_id: claude-code-2026-03-05-c4de9c
date: '2026-03-05'
description: 'Claude Code · 2026-03-05 · Account and Access: 2 changes in v2.1.69
  — Added policy limit fetching (e.g., remote control restrictions) for Team plan
  OAuth…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1071
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 4ab8801376e65f2d58a2f3a4f414decb1fb4bf3d60d406b020601a3443d2f9ae
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-03-05-c4de9c
  comparison: ''
  date: '2026-03-05'
  description: 'Claude Code — v2.1.69: 2 Account and Access changes'
  evidence:
  - quote: Added policy limit fetching (e.g., remote control restrictions) for Team
      plan OAuth users, not just Enterprise
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.69
  - quote: Added `oauth.authServerMetadataUrl` config option for MCP servers to specify
      a custom OAuth metadata discovery URL when standard discovery fails
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.69
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-account-and-access-changes-in-v2-1-69
  source_release: claude-code-2026-03-05-v2-1-69-github-293216328-162b2e44
  source_type: github_releases
  theme: account-access
  title: 2 Account and Access changes in v2.1.69
  type: change
related_changes:
- '[[Changes/Claude Code/2026-02-13-added-claude-auth-login-claude-auth-status-and-claude-auth-logout-cli-subcommand|Added
  claude auth login, claude auth status, and claude auth logout CLI subcommands]]'
- '[[Changes/Claude Code/2026-02-19-improved-performance-by-caching-authentication-failures-for-http-and-sse-mcp-ser|Improved
  performance by caching authentication failures for HTTP and SSE MCP…]]'
- '[[Changes/Claude Code/2026-02-28-added-manual-url-paste-fallback-during-mcp-oauth-authentication-if-the-automatic|Added
  manual URL paste fallback during MCP OAuth authentication]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-05-v2-1-69-github-293216328-162b2e44|claude-code-2026-03-05-v2-1-69-github-293216328-162b2e44]]'
source_type: github_releases
theme: account-access
title: 2 Account and Access changes in v2.1.69
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Account and Access changes in v2.1.69

**Claude Code** · 2026-03-05 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.69) · from [[Releases/Claude Code/claude-code-2026-03-05-v2-1-69-github-293216328-162b2e44|v2.1.69]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added policy limit fetching (e.g., remote control restrictions) for Team plan OAuth users, not just Enterprise

> Added `oauth.authServerMetadataUrl` config option for MCP servers to specify a custom OAuth metadata discovery URL when standard discovery fails

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.69
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-03-05-2-agent-mode-changes-in-v2-1-69|2 Agent Mode changes in v2.1.69]] · Agent Mode
- [[Changes/Claude Code/2026-03-05-changed-sonnet-4-5-users-on-pro-max-team-premium-to-be-automatically-migrated-to|Changed Sonnet 4.5 users on Pro/Max/Team Premium to be automatically migrated…]] · Model Support
- [[Changes/Claude Code/2026-03-05-9-reliability-and-performance-changes-in-v2-1-69|9 Reliability and Performance changes in v2.1.69]] · Reliability and Performance
- [[Changes/Claude Code/2026-03-05-added-reload-plugins-command-to-activate-pending-plugin-changes-without-restarti|Added /reload-plugins command to activate pending plugin changes without restarting]] · Apps and Integrations
- [[Changes/Claude Code/2026-03-05-3-interface-experience-changes-in-v2-1-69|3 Interface Experience changes in v2.1.69]] · Interface Experience
- [[Changes/Claude Code/2026-03-05-improved-macos-startup-for-claude-ai-enterprise-team-users-by-skipping-an-unnece|Improved macOS startup for Claude.ai enterprise/team users by skipping…]] · Enterprise and Administration
- [[Changes/Claude Code/2026-03-05-3-voice-and-audio-changes-in-v2-1-69|3 Voice and Audio changes in v2.1.69]] · Voice and Audio
- [[Changes/Claude Code/2026-03-05-5-safety-and-privacy-changes-in-v2-1-69|5 Safety and Privacy changes in v2.1.69]] · Safety and Privacy
- [[Changes/Claude Code/2026-03-05-7-apps-and-integrations-changes-in-v2-1-69|7 Apps and Integrations changes in v2.1.69]] · Apps and Integrations
- [[Changes/Claude Code/2026-03-05-2-mobile-and-desktop-changes-in-v2-1-69|2 Mobile and Desktop changes in v2.1.69]] · Mobile and Desktop
- [[Changes/Claude Code/2026-03-05-6-developer-workflow-changes-in-v2-1-69|6 Developer Workflow changes in v2.1.69]] · Developer Workflow
- [[Changes/Claude Code/2026-03-05-3-context-window-changes-in-v2-1-69|3 Context Window changes in v2.1.69]] · Context Window
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-02-28 · Claude Code · [[Changes/Claude Code/2026-02-28-added-manual-url-paste-fallback-during-mcp-oauth-authentication-if-the-automatic|Added manual URL paste fallback during MCP OAuth authentication]]
- Later: 2026-03-06 · Claude Code · [[Changes/Claude Code/2026-03-06-vscode-added-native-mcp-server-management-dialog-use-mcp-in-the-chat-panel-to-en|VSCode Added native MCP server management dialog]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-03-05-c4de9c&body=Card%3A%20Changes%2FClaude%20Code%2F2026-03-05-2-account-and-access-changes-in-v2-1-69.md%0ACard%20ID%3A%20claude-code-2026-03-05-c4de9c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.69%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->