---
card_id: claude-code-2026-10-02-37b0db
date: '2026-10-02'
description: 'Claude Code · 2026-10-02 · Developer Workflow: 3 changes in v2.1.288
  — Added a built-in `gh api` to cloud sessions whose image has no GitHub CLI, and
  fixed the…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1294
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f4ab71a5a0afc51acebabb198f83bb9109c5dd39109f40984a6872b73c505485
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-02-37b0db
  comparison: ''
  date: '2026-10-02'
  description: 'Claude Code — v2.1.288: 3 Developer Workflow changes'
  evidence:
  - quote: Added a built-in `gh api` to cloud sessions whose image has no GitHub CLI,
      and fixed the built-in sending control characters from file names, jq filters
      or GitHub errors to the terminal
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.288
  - quote: Added `--max-findings <n>|all` to /code-review to report more or fewer
      findings than the usual limit; the choice is reused until you pass `--max-findings
      default`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.288
  - quote: 'Self-hosted runner: Improved the built-in `gh api`: a refused gh command
      now prints its `gh api` equivalent, `--paginate` follows every page of a repository''s
      lists, and a nested `claude` no longer removes it'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.288
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-developer-workflow-changes-in-v2-1-288
  source_release: claude-code-2026-10-02-v2-1-288-github-402056988-39eb9ac6
  source_type: github_releases
  theme: developer-workflow
  title: 3 Developer Workflow changes in v2.1.288
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-29-3-developer-workflow-changes-in-v2-1-285|3 Developer
  Workflow changes in v2.1.285]]'
- '[[Changes/Claude Code/2026-09-30-3-developer-workflow-changes-in-v2-1-286|3 Developer
  Workflow changes in v2.1.286]]'
- '[[Changes/Claude Code/2026-10-01-3-developer-workflow-changes-in-v2-1-287|3 Developer
  Workflow changes in v2.1.287]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-02-v2-1-288-github-402056988-39eb9ac6|claude-code-2026-10-02-v2-1-288-github-402056988-39eb9ac6]]'
source_type: github_releases
theme: developer-workflow
title: 3 Developer Workflow changes in v2.1.288
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Developer Workflow changes in v2.1.288

**Claude Code** · 2026-10-02 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.288) · from [[Releases/Claude Code/claude-code-2026-10-02-v2-1-288-github-402056988-39eb9ac6|v2.1.288]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added a built-in `gh api` to cloud sessions whose image has no GitHub CLI, and fixed the built-in sending control characters from file names, jq filters or GitHub errors to the terminal

> Added `--max-findings <n>|all` to /code-review to report more or fewer findings than the usual limit; the choice is reused until you pass `--max-findings default`

> Self-hosted runner: Improved the built-in `gh api`: a refused gh command now prints its `gh api` equivalent, `--paginate` follows every page of a repository's lists, and a nested `claude` no longer removes it

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.288
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-02-added-a-re-authenticate-prompt-when-an-mcp-server-asks-for-more-oauth-scope-duri|Added a re-authenticate prompt when an MCP server asks for more OAuth scope during…]] · Account and Access
- [[Changes/Claude Code/2026-10-02-changed-autocompact-to-save-the-auto-compact-window-per-model-so-each-model-keep|Changed /autocompact to save the auto-compact window per model, so each model…]] · Context Window
- [[Changes/Claude Code/2026-10-02-5-apps-and-integrations-changes-in-v2-1-288|5 Apps and Integrations changes in v2.1.288]] · Apps and Integrations
- [[Changes/Claude Code/2026-10-02-changed-the-client-side-auto-mode-classifier-to-ignore-an-anthropic-default-sonn|Changed the client-side auto mode classifier to ignore…]] · Model Support
- [[Changes/Claude Code/2026-10-02-2-accessibility-and-localization-changes-in-v2-1-288|2 Accessibility and Localization changes in v2.1.288]] · Accessibility and Localization
- [[Changes/Claude Code/2026-10-02-4-agent-mode-changes-in-v2-1-288|4 Agent Mode changes in v2.1.288]] · Agent Mode
- [[Changes/Claude Code/2026-10-02-6-safety-and-privacy-changes-in-v2-1-288|6 Safety and Privacy changes in v2.1.288]] · Safety and Privacy
- [[Changes/Claude Code/2026-10-02-added-ui-selection-for-mods-returns-the-text-you-last-selected-in-fullscreen-mod|Added $.ui.selection() for mods]] · Interface Experience
- [[Changes/Claude Code/2026-10-02-improved-the-usage-credits-message-shown-to-team-and-enterprise-members-whose-or|Improved the /usage-credits message shown to Team and Enterprise members whose…]] · Pricing Model
- [[Changes/Claude Code/2026-10-02-4-other-changes-in-v2-1-288|4 other changes in v2.1.288]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-10-01 · Claude Code · [[Changes/Claude Code/2026-10-01-3-developer-workflow-changes-in-v2-1-287|3 Developer Workflow changes in v2.1.287]]
- Later: 2026-10-05 · Claude Code · [[Changes/Claude Code/2026-10-05-5-developer-workflow-changes-in-v2-1-290|5 Developer Workflow changes in v2.1.290]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-02-37b0db&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-02-3-developer-workflow-changes-in-v2-1-288.md%0ACard%20ID%3A%20claude-code-2026-10-02-37b0db%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.288%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->