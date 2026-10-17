---
card_id: claude-code-2026-02-24-0ae6dc
date: '2026-02-24'
description: 'Claude Code · 2026-02-24 · Safety and Privacy: 3 changes in v2.1.51
  — Fixed a security issue where `statusLine` and `fileSuggestion` hook commands could…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1045
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f98b6daf6ef14f588fc06394603b0507b4e6d67f713ee2ed802b170db778435a
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-02-24-0ae6dc
  comparison: ''
  date: '2026-02-24'
  description: 'Claude Code — v2.1.51: 3 Safety and Privacy changes'
  evidence:
  - quote: Fixed a security issue where `statusLine` and `fileSuggestion` hook commands
      could execute without workspace trust acceptance in interactive mode.
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.51
  - quote: Fixed a security issue where HTTP hooks could interpolate arbitrary environment
      variables from header values. Env var interpolation now requires an explicit
      `allowedEnvVars` list in the hook configuration.
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.51
  - quote: HTTP hooks are now routed through the sandbox network proxy when sandboxing
      is enabled, enforcing the domain allowlist. HTTP hooks are not supported for
      SessionStart/Setup events.
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.51
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-safety-and-privacy-changes-in-v2-1-51
  source_release: claude-code-2026-02-24-v2-1-51-github-289665343-b4bbdd9c
  source_type: github_releases
  theme: safety-privacy
  title: 3 Safety and Privacy changes in v2.1.51
  type: change
related_changes:
- '[[Changes/Claude Code/2026-02-18-2-safety-and-privacy-changes-in-v2-1-47|2 Safety
  and Privacy changes in v2.1.47]]'
- '[[Changes/Cursor/2026-02-18-7-safety-and-privacy-changes-in-cli-improvements-and-mermaid-ascii|7
  Safety and Privacy changes in CLI Improvements and Mermaid ASCII…]]'
- '[[Changes/Claude Code/2026-02-19-3-safety-and-privacy-changes-in-v2-1-49|3 Safety
  and Privacy changes in v2.1.49]]'
source_release: '[[Releases/Claude Code/claude-code-2026-02-24-v2-1-51-github-289665343-b4bbdd9c|claude-code-2026-02-24-v2-1-51-github-289665343-b4bbdd9c]]'
source_type: github_releases
theme: safety-privacy
title: 3 Safety and Privacy changes in v2.1.51
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Safety and Privacy changes in v2.1.51

**Claude Code** · 2026-02-24 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.51) · from [[Releases/Claude Code/claude-code-2026-02-24-v2-1-51-github-289665343-b4bbdd9c|v2.1.51]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Fixed a security issue where `statusLine` and `fileSuggestion` hook commands could execute without workspace trust acceptance in interactive mode.

> Fixed a security issue where HTTP hooks could interpolate arbitrary environment variables from header values. Env var interpolation now requires an explicit `allowedEnvVars` list in the hook configuration.

> HTTP hooks are now routed through the sandbox network proxy when sandboxing is enabled, enforcing the domain allowlist. HTTP hooks are not supported for SessionStart/Setup events.

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.51
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-02-24-bashtool-now-skips-login-shell-l-flag-by-default-when-a-shell-snapshot-is-availa|BashTool now skips login shell (-l flag) by default when a shell snapshot…]] · Developer Workflow
- [[Changes/Claude Code/2026-02-24-4-apps-and-integrations-changes-in-v2-1-51|4 Apps and Integrations changes in v2.1.51]] · Apps and Integrations
- [[Changes/Claude Code/2026-02-24-tool-results-larger-than-50k-characters-are-now-persisted-to-disk-previously-100|Tool results larger than 50K characters are now persisted to disk (previously 100K)]] · Context Window
- [[Changes/Claude Code/2026-02-24-the-model-picker-now-shows-human-readable-labels-e-g-sonnet-4-5-instead-of-raw-m|The /model picker now shows human-readable labels (e.g., "Sonnet 4.5") instead…]] · Model Support
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-02-19 · Claude Code · [[Changes/Claude Code/2026-02-19-3-safety-and-privacy-changes-in-v2-1-49|3 Safety and Privacy changes in v2.1.49]]
- Later: 2026-02-28 · Claude Code · [[Changes/Claude Code/2026-02-28-fixed-listener-leak-in-interactive-permission-handler-during-auto-approvals|Fixed listener leak in interactive permission handler during auto-approvals]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-02-24-0ae6dc&body=Card%3A%20Changes%2FClaude%20Code%2F2026-02-24-3-safety-and-privacy-changes-in-v2-1-51.md%0ACard%20ID%3A%20claude-code-2026-02-24-0ae6dc%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.51%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->