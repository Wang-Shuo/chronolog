---
card_id: claude-code-2026-08-04-95e070
date: '2026-08-04'
description: 'Claude Code · 2026-08-04 · Developer Workflow: 3 changes in v2.1.221
  — Improved `/ultrareview` error messages when a repo shares no history with its
  base: a…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1235
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b5d39221c05caf7497c9ee4fe01aa39dc6bbeac1f1ffadb2131a7025014e0f50
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-08-04-95e070
  comparison: ''
  date: '2026-08-04'
  description: 'Claude Code — v2.1.221: 3 Developer Workflow changes'
  evidence:
  - quote: 'Improved `/ultrareview` error messages when a repo shares no history with
      its base: a checkout with no branches is now refused up front with advice to
      create one, and refusal hints no longer suggest `git fetch --unshallow` on clones
      that are already complete'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.221
  - quote: Changed background sessions to commit and push to preserve work, open a
      draft PR only when the task calls for one, follow your CLAUDE.md git instructions,
      and always end by reporting where the work lives
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.221
  - quote: Changed sessions forked with `/fork` to create a new worktree of their
      own instead of working in the original session's checkout
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.221
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-developer-workflow-changes-in-v2-1-221
  source_release: claude-code-2026-08-04-v2-1-221-github-364520051-d6a656ce
  source_type: github_releases
  theme: developer-workflow
  title: 3 Developer Workflow changes in v2.1.221
  type: change
related_changes:
- '[[Changes/Claude Code/2026-07-20-2-developer-workflow-changes-in-v2-1-216|2 Developer
  Workflow changes in v2.1.216]]'
- '[[Changes/Claude Code/2026-07-21-improved-footer-pr-badge-links-to-be-clickable-hyperlinks-even-when-terminal-sup|Improved
  footer PR badge links to be clickable hyperlinks even when terminal support…]]'
- '[[Changes/Claude Code/2026-07-22-changed-code-review-to-run-as-a-background-subagent-so-review-work-no-longer-fil|Changed
  /code-review to run as a background subagent, so review work no longer…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-08-04-v2-1-221-github-364520051-d6a656ce|claude-code-2026-08-04-v2-1-221-github-364520051-d6a656ce]]'
source_type: github_releases
theme: developer-workflow
title: 3 Developer Workflow changes in v2.1.221
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Developer Workflow changes in v2.1.221

**Claude Code** · 2026-08-04 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.221) · from [[Releases/Claude Code/claude-code-2026-08-04-v2-1-221-github-364520051-d6a656ce|v2.1.221]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Improved `/ultrareview` error messages when a repo shares no history with its base: a checkout with no branches is now refused up front with advice to create one, and refusal hints no longer suggest `git fetch --unshallow` on clones that are already complete

> Changed background sessions to commit and push to preserve work, open a draft PR only when the task calls for one, follow your CLAUDE.md git instructions, and always end by reporting where the work lives

> Changed sessions forked with `/fork` to create a new worktree of their own instead of working in the original session's checkout

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.221
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-08-04-improved-stats-panel-to-count-cache-tokens-in-its-token-totals-with-a-breakdown|Improved Stats panel to count cache tokens in its token totals, with a breakdown…]] · Context Window
- [[Changes/Claude Code/2026-08-04-4-apps-and-integrations-changes-in-v2-1-221|4 Apps and Integrations changes in v2.1.221]] · Apps and Integrations
- [[Changes/Claude Code/2026-08-04-changed-emoji-autocomplete-to-accept-common-alternate-shortcodes-like-thumbsup-t|Changed emoji autocomplete to accept common alternate shortcodes like :thumbsup:…]] · Editor Experience
- [[Changes/Claude Code/2026-08-04-3-model-support-changes-in-v2-1-221|3 Model Support changes in v2.1.221]] · Model Support
- [[Changes/Claude Code/2026-08-04-vscode-added-focus-view-a-chat-menu-toggle-that-hides-tool-activity-behind-an-ex|VSCode Added Focus view]] · Interface Experience
- [[Changes/Claude Code/2026-08-04-changed-fast-mode-to-report-on-the-stream-when-usage-credits-run-out-mid-session|Changed fast mode to report on the stream when usage credits run out mid-session…]] · Pricing Model
- [[Changes/Claude Code/2026-08-04-7-safety-and-privacy-changes-in-v2-1-221|7 Safety and Privacy changes in v2.1.221]] · Safety and Privacy
- [[Changes/Claude Code/2026-08-04-3-other-changes-in-v2-1-221|3 other changes in v2.1.221]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-07-22 · Claude Code · [[Changes/Claude Code/2026-07-22-changed-code-review-to-run-as-a-background-subagent-so-review-work-no-longer-fil|Changed /code-review to run as a background subagent, so review work no longer…]]
- Later: 2026-08-06 · Claude Code · [[Changes/Claude Code/2026-08-06-2-developer-workflow-changes-in-v2-1-223|2 Developer Workflow changes in v2.1.223]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-08-04-95e070&body=Card%3A%20Changes%2FClaude%20Code%2F2026-08-04-3-developer-workflow-changes-in-v2-1-221.md%0ACard%20ID%3A%20claude-code-2026-08-04-95e070%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.221%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->