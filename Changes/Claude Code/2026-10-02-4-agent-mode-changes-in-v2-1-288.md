---
card_id: claude-code-2026-10-02-949130
date: '2026-10-02'
description: 'Claude Code · 2026-10-02 · Agent Mode: 4 changes in v2.1.288 — Added
  Ctrl+F to find a session by name and Alt+↑/↓ to jump between groups in the agents
  view…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1184
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d1012d8f3caeee0a7814e4dbefa24e82193681bc5f8adb62d8f642e070544721
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-02-949130
  comparison: ''
  date: '2026-10-02'
  description: 'Claude Code — v2.1.288: 4 Agent Mode changes'
  evidence:
  - quote: Added Ctrl+F to find a session by name and Alt+↑/↓ to jump between groups
      in the agents view; both, and rename, can be rebound in keybindings.json
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.288
  - quote: 'Improved auto mode: when a conversation grows too long for the client-side
      safety classifier to review, it is now compacted instead of prompting for, or
      failing, every tool call'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.288
  - quote: Improved "You should know" notes to say "we", "the main agent" or "you"
      depending on who was responsible for a decision
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.288
  - quote: Changed the agents view `n:` filter (and Ctrl+F search) so Enter opens
      the session whose name matches best instead of the top row
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.288
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 4-agent-mode-changes-in-v2-1-288
  source_release: claude-code-2026-10-02-v2-1-288-github-402056988-39eb9ac6
  source_type: github_releases
  theme: agent-mode
  title: 4 Agent Mode changes in v2.1.288
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-29-2-agent-mode-changes-in-v2-1-285|2 Agent Mode
  changes in v2.1.285]]'
- '[[Changes/Claude Code/2026-09-30-6-agent-mode-changes-in-v2-1-286|6 Agent Mode
  changes in v2.1.286]]'
- '[[Changes/Claude Code/2026-10-01-4-agent-mode-changes-in-v2-1-287|4 Agent Mode
  changes in v2.1.287]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-02-v2-1-288-github-402056988-39eb9ac6|claude-code-2026-10-02-v2-1-288-github-402056988-39eb9ac6]]'
source_type: github_releases
theme: agent-mode
title: 4 Agent Mode changes in v2.1.288
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Agent Mode changes in v2.1.288

**Claude Code** · 2026-10-02 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.288) · from [[Releases/Claude Code/claude-code-2026-10-02-v2-1-288-github-402056988-39eb9ac6|v2.1.288]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added Ctrl+F to find a session by name and Alt+↑/↓ to jump between groups in the agents view; both, and rename, can be rebound in keybindings.json

> Improved auto mode: when a conversation grows too long for the client-side safety classifier to review, it is now compacted instead of prompting for, or failing, every tool call

> Improved "You should know" notes to say "we", "the main agent" or "you" depending on who was responsible for a decision

> Changed the agents view `n:` filter (and Ctrl+F search) so Enter opens the session whose name matches best instead of the top row

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.288
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-02-added-a-re-authenticate-prompt-when-an-mcp-server-asks-for-more-oauth-scope-duri|Added a re-authenticate prompt when an MCP server asks for more OAuth scope during…]] · Account and Access
- [[Changes/Claude Code/2026-10-02-3-developer-workflow-changes-in-v2-1-288|3 Developer Workflow changes in v2.1.288]] · Developer Workflow
- [[Changes/Claude Code/2026-10-02-changed-autocompact-to-save-the-auto-compact-window-per-model-so-each-model-keep|Changed /autocompact to save the auto-compact window per model, so each model…]] · Context Window
- [[Changes/Claude Code/2026-10-02-5-apps-and-integrations-changes-in-v2-1-288|5 Apps and Integrations changes in v2.1.288]] · Apps and Integrations
- [[Changes/Claude Code/2026-10-02-changed-the-client-side-auto-mode-classifier-to-ignore-an-anthropic-default-sonn|Changed the client-side auto mode classifier to ignore…]] · Model Support
- [[Changes/Claude Code/2026-10-02-2-accessibility-and-localization-changes-in-v2-1-288|2 Accessibility and Localization changes in v2.1.288]] · Accessibility and Localization
- [[Changes/Claude Code/2026-10-02-6-safety-and-privacy-changes-in-v2-1-288|6 Safety and Privacy changes in v2.1.288]] · Safety and Privacy
- [[Changes/Claude Code/2026-10-02-added-ui-selection-for-mods-returns-the-text-you-last-selected-in-fullscreen-mod|Added $.ui.selection() for mods]] · Interface Experience
- [[Changes/Claude Code/2026-10-02-improved-the-usage-credits-message-shown-to-team-and-enterprise-members-whose-or|Improved the /usage-credits message shown to Team and Enterprise members whose…]] · Pricing Model
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-10-01 · Claude Code · [[Changes/Claude Code/2026-10-01-4-agent-mode-changes-in-v2-1-287|4 Agent Mode changes in v2.1.287]]
- Later: 2026-10-05 · Claude Code · [[Changes/Claude Code/2026-10-05-added-claude-api-managed-agents-onboard-url-to-set-up-the-managed-agents-pattern|Added /claude-api managed-agents-onboard url to set up the Managed Agents…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-02-949130&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-02-4-agent-mode-changes-in-v2-1-288.md%0ACard%20ID%3A%20claude-code-2026-10-02-949130%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.288%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->