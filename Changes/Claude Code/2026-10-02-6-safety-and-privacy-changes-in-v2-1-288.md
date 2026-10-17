---
card_id: claude-code-2026-10-02-c68645
date: '2026-10-02'
description: 'Claude Code · 2026-10-02 · Safety and Privacy: 6 changes in v2.1.288
  — Added a screen reader mode announcement of the new permission mode when you approve
  a…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1265
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d90e7d9e1d432cafc29186e83b8eec990eb8a97261ef560ae4e4c5c5e200f8fb
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-02-c68645
  comparison: ''
  date: '2026-10-02'
  description: 'Claude Code — v2.1.288: 6 Safety and Privacy changes'
  evidence:
  - quote: Added a screen reader mode announcement of the new permission mode when
      you approve a plan, including with Shift+Tab
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.288
  - quote: Fixed auto mode denials pointing Claude at a Bash permission rule when
      the blocked tool was not Bash
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.288
  - quote: Fixed Cowork cloud sessions staying marked as waiting for input after a
      WebFetch permission prompt for an unapproved URL went unanswered for five minutes
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.288
  - quote: Fixed Bash tool permission check to prompt before a `BASHPID` assignment
      whose value the shell would evaluate as arithmetic, instead of allowing it silently
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.288
  - quote: Fixed permission asks that ended unanswered, in `-p` or on an interrupted
      turn, emitting no `tool_decision` event
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.288
  - quote: Improved Bash permission prompts to give a shorter reason when part of
      a command can't be checked before it runs
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.288
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 6-safety-and-privacy-changes-in-v2-1-288
  source_release: claude-code-2026-10-02-v2-1-288-github-402056988-39eb9ac6
  source_type: github_releases
  theme: safety-privacy
  title: 6 Safety and Privacy changes in v2.1.288
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-29-9-safety-and-privacy-changes-in-v2-1-285|9 Safety
  and Privacy changes in v2.1.285]]'
- '[[Changes/Claude Code/2026-09-30-4-safety-and-privacy-changes-in-v2-1-286|4 Safety
  and Privacy changes in v2.1.286]]'
- '[[Changes/Claude Code/2026-10-01-6-safety-and-privacy-changes-in-v2-1-287|6 Safety
  and Privacy changes in v2.1.287]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-02-v2-1-288-github-402056988-39eb9ac6|claude-code-2026-10-02-v2-1-288-github-402056988-39eb9ac6]]'
source_type: github_releases
theme: safety-privacy
title: 6 Safety and Privacy changes in v2.1.288
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Safety and Privacy changes in v2.1.288

**Claude Code** · 2026-10-02 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.288) · from [[Releases/Claude Code/claude-code-2026-10-02-v2-1-288-github-402056988-39eb9ac6|v2.1.288]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added a screen reader mode announcement of the new permission mode when you approve a plan, including with Shift+Tab

> Fixed auto mode denials pointing Claude at a Bash permission rule when the blocked tool was not Bash

> Fixed Cowork cloud sessions staying marked as waiting for input after a WebFetch permission prompt for an unapproved URL went unanswered for five minutes

> Fixed Bash tool permission check to prompt before a `BASHPID` assignment whose value the shell would evaluate as arithmetic, instead of allowing it silently

> Fixed permission asks that ended unanswered, in `-p` or on an interrupted turn, emitting no `tool_decision` event

> Improved Bash permission prompts to give a shorter reason when part of a command can't be checked before it runs

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
- [[Changes/Claude Code/2026-10-02-4-agent-mode-changes-in-v2-1-288|4 Agent Mode changes in v2.1.288]] · Agent Mode
- [[Changes/Claude Code/2026-10-02-added-ui-selection-for-mods-returns-the-text-you-last-selected-in-fullscreen-mod|Added $.ui.selection() for mods]] · Interface Experience
- [[Changes/Claude Code/2026-10-02-improved-the-usage-credits-message-shown-to-team-and-enterprise-members-whose-or|Improved the /usage-credits message shown to Team and Enterprise members whose…]] · Pricing Model
- [[Changes/Claude Code/2026-10-02-4-other-changes-in-v2-1-288|4 other changes in v2.1.288]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-10-01 · Claude Code · [[Changes/Claude Code/2026-10-01-6-safety-and-privacy-changes-in-v2-1-287|6 Safety and Privacy changes in v2.1.287]]
- Later: 2026-10-05 · Claude Code · [[Changes/Claude Code/2026-10-05-19-safety-and-privacy-changes-in-v2-1-290|19 Safety and Privacy changes in v2.1.290]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-02-c68645&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-02-6-safety-and-privacy-changes-in-v2-1-288.md%0ACard%20ID%3A%20claude-code-2026-10-02-c68645%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.288%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->