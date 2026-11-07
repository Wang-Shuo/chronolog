---
card_id: claude-code-2026-10-02-7236cd
date: '2026-10-02'
description: 'Claude Code · 2026-10-02 · Apps and Integrations: 5 changes in v2.1.288
  — Improved cloud sessions: a new conversation''s first turn no longer waits for
  a stdio…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2849
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 99f823e4c5a004c28f6c8a2a0de8ceb2d53f6aeef04c4e55f92fdd7a52345e47
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-02-7236cd
  comparison: ''
  date: '2026-10-02'
  description: 'Claude Code — v2.1.288: 5 Apps and Integrations changes'
  evidence:
  - quote: 'Improved cloud sessions: a new conversation''s first turn no longer waits
      for a stdio MCP server whose config sets `alwaysLoad: false`'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.288
  - quote: 'Improved Remote Control''s recovery from an expired server credential:
      sessions stay connected during renewal and are kept if it gives up after a server
      outage'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.288
  - quote: Changed the background command time limit to apply only in unattended sessions
      (`-p`, Agent SDK, CI, cloud); terminal, desktop app and VS Code sessions have
      no limit
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.288
  - quote: Changed MCP URL prompts from servers that can't report when you're done
      to wait for "I'm done, continue" before the tool call continues, so you can
      finish in the browser first
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.288
  - quote: '[Claude Tag] Improved Claude to also follow a related Slack thread in
      another channel that it only read, so updates there reach the conversation that
      depends on them'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.288
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 5-apps-and-integrations-changes-in-v2-1-288
  source_release: claude-code-2026-10-02-v2-1-288-github-402056988-39eb9ac6
  source_type: github_releases
  theme: apps-integrations
  title: 5 Apps and Integrations changes in v2.1.288
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-09-30-36-apps-and-integrations-changes-in-v2026-9-7|36
  Apps and Integrations changes in v2026.9.7]]'
- '[[Changes/Claude Code/2026-10-01-11-apps-and-integrations-changes-in-v2-1-287|11
  Apps and Integrations changes in v2.1.287]]'
- '[[Changes/Codex CLI/2026-10-01-4-apps-and-integrations-changes-in-rust-v0-160-0|4
  Apps and Integrations changes in rust-v0.160.0]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-02-v2-1-288-github-402056988-39eb9ac6|claude-code-2026-10-02-v2-1-288-github-402056988-39eb9ac6]]'
source_type: github_releases
theme: apps-integrations
title: 5 Apps and Integrations changes in v2.1.288
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Apps and Integrations changes in v2.1.288

**Claude Code** · 2026-10-02 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.288) · from [[Releases/Claude Code/claude-code-2026-10-02-v2-1-288-github-402056988-39eb9ac6|v2.1.288]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Improved cloud sessions: a new conversation's first turn no longer waits for a stdio MCP server whose config sets `alwaysLoad: false`

> Improved Remote Control's recovery from an expired server credential: sessions stay connected during renewal and are kept if it gives up after a server outage

> Changed the background command time limit to apply only in unattended sessions (`-p`, Agent SDK, CI, cloud); terminal, desktop app and VS Code sessions have no limit

> Changed MCP URL prompts from servers that can't report when you're done to wait for "I'm done, continue" before the tool call continues, so you can finish in the browser first

> [Claude Tag] Improved Claude to also follow a related Slack thread in another channel that it only read, so updates there reach the conversation that depends on them

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.288
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-02-added-a-re-authenticate-prompt-when-an-mcp-server-asks-for-more-oauth-scope-duri|Added a re-authenticate prompt when an MCP server asks for more OAuth scope during…]] · Account and Access
- [[Changes/Claude Code/2026-10-02-3-developer-workflow-changes-in-v2-1-288|3 Developer Workflow changes in v2.1.288]] · Developer Workflow
- [[Changes/Claude Code/2026-10-02-changed-autocompact-to-save-the-auto-compact-window-per-model-so-each-model-keep|Changed /autocompact to save the auto-compact window per model, so each model…]] · Context Window
- [[Changes/Claude Code/2026-10-02-changed-the-client-side-auto-mode-classifier-to-ignore-an-anthropic-default-sonn|Changed the client-side auto mode classifier to ignore…]] · Model Support
- [[Changes/Claude Code/2026-10-02-2-accessibility-and-localization-changes-in-v2-1-288|2 Accessibility and Localization changes in v2.1.288]] · Accessibility and Localization
- [[Changes/Claude Code/2026-10-02-4-agent-mode-changes-in-v2-1-288|4 Agent Mode changes in v2.1.288]] · Agent Mode
- [[Changes/Claude Code/2026-10-02-6-safety-and-privacy-changes-in-v2-1-288|6 Safety and Privacy changes in v2.1.288]] · Safety and Privacy
- [[Changes/Claude Code/2026-10-02-added-ui-selection-for-mods-returns-the-text-you-last-selected-in-fullscreen-mod|Added $.ui.selection() for mods]] · Interface Experience
- [[Changes/Claude Code/2026-10-02-improved-the-usage-credits-message-shown-to-team-and-enterprise-members-whose-or|Improved the /usage-credits message shown to Team and Enterprise members whose…]] · Pricing Model
- [[Changes/Claude Code/2026-10-02-4-other-changes-in-v2-1-288|4 other changes in v2.1.288]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-10-01 · Codex CLI · [[Changes/Codex CLI/2026-10-01-4-apps-and-integrations-changes-in-rust-v0-160-0|4 Apps and Integrations changes in rust-v0.160.0]]
- Later: 2026-10-02 · Devin · [[Changes/Devin/2026-10-02-azure-devops-bitbucket-gerrit-and-perforce|Azure DevOps, Bitbucket, Gerrit and Perforce]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-02-7236cd&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-02-5-apps-and-integrations-changes-in-v2-1-288.md%0ACard%20ID%3A%20claude-code-2026-10-02-7236cd%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.288%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->