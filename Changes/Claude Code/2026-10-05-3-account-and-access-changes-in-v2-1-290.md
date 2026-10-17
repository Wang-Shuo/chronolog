---
card_id: claude-code-2026-10-05-6b68dd
date: '2026-10-05'
description: 'Claude Code · 2026-10-05 · Account and Access: 3 changes in v2.1.290
  — Added a Deny button to the Claude apps gateway''s sign-in approval page: it ends
  the…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1285
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 58f376d4a354db0d2e0de59624a1f556d1d88fbbea4d17d7f46d3898f84759d8
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-05-6b68dd
  comparison: ''
  date: '2026-10-05'
  description: 'Claude Code — v2.1.290: 3 Account and Access changes'
  evidence:
  - quote: 'Added a Deny button to the Claude apps gateway''s sign-in approval page:
      it ends the pending sign-in, so the waiting terminal stops within seconds'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
  - quote: 'Improved the error shown when a cloud session is started without a claude.ai
      sign-in: it now names `claude auth login` and /login and no longer blames API-key
      authentication'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
  - quote: 'Improved the Claude apps gateway''s browser sign-in pages: brand fonts,
      centered layout, and dark mode'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-account-and-access-changes-in-v2-1-290
  source_release: claude-code-2026-10-05-v2-1-290-github-403993621-ae06f2b6
  source_type: github_releases
  theme: account-access
  title: 3 Account and Access changes in v2.1.290
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-29-changed-team-and-enterprise-sessions-and-sessions-whose-sign-in-plan-claude-code|Changed
  Team and Enterprise sessions, and sessions whose sign-in plan Claude Code…]]'
- '[[Changes/Claude Code/2026-10-01-added-url-prompts-from-mcp-servers-on-the-2025-11-25-protocol-for-example-to-sig|Added
  URL prompts from MCP servers on the 2025-11-25 protocol, for example to sign in]]'
- '[[Changes/Claude Code/2026-10-02-added-a-re-authenticate-prompt-when-an-mcp-server-asks-for-more-oauth-scope-duri|Added
  a re-authenticate prompt when an MCP server asks for more OAuth scope during…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-05-v2-1-290-github-403993621-ae06f2b6|claude-code-2026-10-05-v2-1-290-github-403993621-ae06f2b6]]'
source_type: github_releases
theme: account-access
title: 3 Account and Access changes in v2.1.290
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Account and Access changes in v2.1.290

**Claude Code** · 2026-10-05 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.290) · from [[Releases/Claude Code/claude-code-2026-10-05-v2-1-290-github-403993621-ae06f2b6|v2.1.290]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added a Deny button to the Claude apps gateway's sign-in approval page: it ends the pending sign-in, so the waiting terminal stops within seconds

> Improved the error shown when a cloud session is started without a claude.ai sign-in: it now names `claude auth login` and /login and no longer blames API-key authentication

> Improved the Claude apps gateway's browser sign-in pages: brand fonts, centered layout, and dark mode

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-05-changed-background-sessions-waiting-on-a-scheduled-wakeup-loop-they-are-now-left|Changed background sessions waiting on a scheduled wakeup (/loop)]] · Memory and Personalization
- [[Changes/Claude Code/2026-10-05-added-claude-api-managed-agents-onboard-url-to-set-up-the-managed-agents-pattern|Added /claude-api managed-agents-onboard url to set up the Managed Agents…]] · Agent Mode
- [[Changes/Claude Code/2026-10-05-19-safety-and-privacy-changes-in-v2-1-290|19 Safety and Privacy changes in v2.1.290]] · Safety and Privacy
- [[Changes/Claude Code/2026-10-05-added-claude-api-managed-agents-onboard-quickstart-name-to-build-a-console-quick|Added /claude-api managed-agents-onboard quickstart-name to build a Console…]] · Agent Mode
- [[Changes/Claude Code/2026-10-05-vscode-added-a-screen-reader-announcement-message-queued-when-you-send-a-message|VSCode Added a screen reader announcement, "Message queued.", when you send…]] · Accessibility and Localization
- [[Changes/Claude Code/2026-10-05-changed-the-interactive-session-s-websearch-budget-to-refill-over-time-100-calls|Changed the interactive session's WebSearch budget to refill over time (100 calls/hour]] · Search and Browsing
- [[Changes/Claude Code/2026-10-05-14-apps-and-integrations-changes-in-v2-1-290|14 Apps and Integrations changes in v2.1.290]] · Apps and Integrations
- [[Changes/Claude Code/2026-10-05-4-agent-mode-changes-in-v2-1-290|4 Agent Mode changes in v2.1.290]] · Agent Mode
- [[Changes/Claude Code/2026-10-05-2-model-support-changes-in-v2-1-290|2 Model Support changes in v2.1.290]] · Model Support
- [[Changes/Claude Code/2026-10-05-5-developer-workflow-changes-in-v2-1-290|5 Developer Workflow changes in v2.1.290]] · Developer Workflow
- [[Changes/Claude Code/2026-10-05-changed-background-sessions-whose-scheduled-task-is-gone-they-now-move-to-comple|Changed background sessions whose scheduled task is gone]] · Automation and Scheduling
- [[Changes/Claude Code/2026-10-05-improved-responsiveness-while-resuming-large-sessions-timers-input-and-rendering|Improved responsiveness while resuming large sessions]] · Reliability and Performance
- [[Changes/Claude Code/2026-10-05-18-other-changes-in-v2-1-290|18 other changes in v2.1.290]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-10-02 · Claude Code · [[Changes/Claude Code/2026-10-02-added-a-re-authenticate-prompt-when-an-mcp-server-asks-for-more-oauth-scope-duri|Added a re-authenticate prompt when an MCP server asks for more OAuth scope during…]]
- Later: 2026-10-08 · Claude Code · [[Changes/Claude Code/2026-10-08-added-support-for-forceloginmethod-gateway-and-forcelogingatewayurl-in-your-own|Added support for forceLoginMethod: "gateway" and forceLoginGatewayUrl…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-05-6b68dd&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-05-3-account-and-access-changes-in-v2-1-290.md%0ACard%20ID%3A%20claude-code-2026-10-05-6b68dd%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.290%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->