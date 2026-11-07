---
card_id: claude-code-2026-10-02-c68645
date: '2026-10-02'
description: 'Claude Code · 2026-10-02 · Safety and Privacy: 6 changes in v2.1.288
  — Added a screen reader mode announcement of the new permission mode when you approve
  a…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2257
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 5400ca2639628b9351f16ad42bc3c68bf02343364422c2f0cfd82e5d1a644ade
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
- '[[Changes/Codex CLI/2026-10-01-7-safety-and-privacy-changes-in-rust-v0-160-0|7
  Safety and Privacy changes in rust-v0.160.0]]'
- '[[Changes/GitHub Copilot CLI/2026-10-01-2-safety-and-privacy-changes-in-v1-0-91|2
  Safety and Privacy changes in v1.0.91]]'
- '[[Changes/Lovable/2026-10-01-keep-your-workspace-s-ai-processing-in-the-eu|Keep
  your workspace''s AI processing in the EU]]'
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

- Earlier: 2026-10-01 · Lovable · [[Changes/Lovable/2026-10-01-keep-your-workspace-s-ai-processing-in-the-eu|Keep your workspace's AI processing in the EU]]
- Later: 2026-10-02 · Devin · [[Changes/Devin/2026-10-02-select-all-findings-of-a-severity|Select All Findings of a Severity]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-02-c68645&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-02-6-safety-and-privacy-changes-in-v2-1-288.md%0ACard%20ID%3A%20claude-code-2026-10-02-c68645%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.288%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->