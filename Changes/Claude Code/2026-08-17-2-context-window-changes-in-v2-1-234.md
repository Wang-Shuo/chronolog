---
card_id: claude-code-2026-08-17-5ed35d
date: '2026-08-17'
description: 'Claude Code · 2026-08-17 · Context Window: 2 changes in v2.1.234 — Reduced
  the context cost of loading the built-in `claude-api` skill from ~200k+ tokens to…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2
    Context Window changes in 0.2.9]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1201
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: c0be450578275a93520038f78050a8332cb01142899b8c8db9e8c179c4dd9d1b
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-08-17-5ed35d
  comparison: ''
  date: '2026-08-17'
  description: 'Claude Code — v2.1.234: 2 Context Window changes'
  evidence:
  - quote: Reduced the context cost of loading the built-in `claude-api` skill from
      ~200k+ tokens to ~25k by loading reference docs on demand
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.234
  - quote: '`/goal` now clears itself with a notice when a turn dies on an unrecoverable
      error (e.g. revoked auth, an exhausted credit balance, or a context overflow)
      instead of staying armed'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.234
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-context-window-changes-in-v2-1-234
  source_release: claude-code-2026-08-17-v2-1-234-github-371864218-2ca32673
  source_type: github_releases
  theme: context-window
  title: 2 Context Window changes in v2.1.234
  type: change
related_changes:
- '[[Changes/Claude Code/2026-08-11-improved-compaction-progress-the-retry-countdown-and-stall-hint-now-appear-durin|Improved
  compaction progress]]'
- '[[Changes/Claude Code/2026-08-12-improved-prompt-is-too-long-errors-to-explain-why-automatic-compaction-could-not|Improved
  "prompt is too long" errors to explain why automatic compaction could not…]]'
- '[[Changes/Claude Code/2026-08-14-improved-apps-gateway-error-forwarding-400-413-errors-from-vertex-foundry-and-cl|Improved
  apps gateway error forwarding]]'
source_release: '[[Releases/Claude Code/claude-code-2026-08-17-v2-1-234-github-371864218-2ca32673|claude-code-2026-08-17-v2-1-234-github-371864218-2ca32673]]'
source_type: github_releases
theme: context-window
title: 2 Context Window changes in v2.1.234
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Context Window changes in v2.1.234

**Claude Code** · 2026-08-17 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.234) · from [[Releases/Claude Code/claude-code-2026-08-17-v2-1-234-github-371864218-2ca32673|v2.1.234]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Reduced the context cost of loading the built-in `claude-api` skill from ~200k+ tokens to ~25k by loading reference docs on demand

> `/goal` now clears itself with a notice when a turn dies on an unrecoverable error (e.g. revoked auth, an exhausted credit balance, or a context overflow) instead of staying armed

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.234
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-08-17-2-model-support-changes-in-v2-1-234|2 Model Support changes in v2.1.234]] · Model Support
- [[Changes/Claude Code/2026-08-17-2-apps-and-integrations-changes-in-v2-1-234|2 Apps and Integrations changes in v2.1.234]] · Apps and Integrations
- [[Changes/Claude Code/2026-08-17-8-safety-and-privacy-changes-in-v2-1-234|8 Safety and Privacy changes in v2.1.234]] · Safety and Privacy
- [[Changes/Claude Code/2026-08-17-3-interface-experience-changes-in-v2-1-234|3 Interface Experience changes in v2.1.234]] · Interface Experience
- [[Changes/Claude Code/2026-08-17-removed-the-redundant-allowed-by-auto-mode-classifier-line-that-auto-mode-showed|Removed the redundant "Allowed by auto mode classifier" line that auto mode showed…]] · Agent Mode
- [[Changes/Claude Code/2026-08-17-removed-the-default-teammate-model-setting-from-config-agent-team-teammates-now|Removed the "Default teammate model" setting from /config]] · Collaboration
- [[Changes/Claude Code/2026-08-17-2-account-and-access-changes-in-v2-1-234|2 Account and Access changes in v2.1.234]] · Account and Access
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-08-14 · Claude Code · [[Changes/Claude Code/2026-08-14-improved-apps-gateway-error-forwarding-400-413-errors-from-vertex-foundry-and-cl|Improved apps gateway error forwarding]]
- Later: 2026-08-18 · Claude Code · [[Changes/Claude Code/2026-08-18-improved-the-context-limit-error-to-say-when-auto-compact-is-off-and-point-to-co|Improved the context-limit error to say when auto-compact is off and point…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-04 · Cursor · [[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2 Context Window changes in 0.2.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-08-17-5ed35d&body=Card%3A%20Changes%2FClaude%20Code%2F2026-08-17-2-context-window-changes-in-v2-1-234.md%0ACard%20ID%3A%20claude-code-2026-08-17-5ed35d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.234%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->