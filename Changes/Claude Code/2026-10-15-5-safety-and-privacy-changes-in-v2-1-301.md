---
card_id: claude-code-2026-10-15-2735a2
date: '2026-10-15'
description: 'Claude Code · 2026-10-15 · Safety and Privacy: 5 changes in v2.1.301
  — Added `classifier_verdict` and `permission_mode` to OpenTelemetry `tool_decision`…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1278
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 4786d6851ca8c18586d441612fdd81b55b641d20e0cca04dcdb68bd89ffc58e6
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-15-2735a2
  comparison: ''
  date: '2026-10-15'
  description: 'Claude Code — v2.1.301: 5 Safety and Privacy changes'
  evidence:
  - quote: Added `classifier_verdict` and `permission_mode` to OpenTelemetry `tool_decision`
      events, so auto mode classifier decisions can be told apart from permission
      rules
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.301
  - quote: Fixed a tool call cut off by a message sent mid-turn during its permission
      check being reported to the model as rejected by the user
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.301
  - quote: Fixed the permission prompt for a plugin or skill hook's `ask` decision
      not showing which plugin or skill the hook comes from
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.301
  - quote: Fixed workflow scripts asking for permission or being refused when read,
      edited or re-run after a Bash `cd` in the same session
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.301
  - quote: '[VSCode] Fixed the native dictation audio module being loaded, to check
      microphone permission, where dictation is not offered (non-claude.ai sign-ins,
      remote windows)'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.301
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 5-safety-and-privacy-changes-in-v2-1-301
  source_release: claude-code-2026-10-15-v2-1-301-github-413913133-a3fb5b4e
  source_type: github_releases
  theme: safety-privacy
  title: 5 Safety and Privacy changes in v2.1.301
  type: change
related_changes:
- '[[Changes/Cursor/2026-10-13-origin-now-integrates-with-over-20-apps-for-deployments-ci-code-review-security|Origin
  now integrates with over 20 apps for deployments, CI, code review, security…]]'
- '[[Changes/Claude Code/2026-10-14-2-safety-and-privacy-changes-in-v2-1-300|2 Safety
  and Privacy changes in v2.1.300]]'
- '[[Changes/Claude Code/2026-10-14-6-safety-and-privacy-changes-in-v2-1-299|6 Safety
  and Privacy changes in v2.1.299]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-15-v2-1-301-github-413913133-a3fb5b4e|claude-code-2026-10-15-v2-1-301-github-413913133-a3fb5b4e]]'
source_type: github_releases
theme: safety-privacy
title: 5 Safety and Privacy changes in v2.1.301
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Safety and Privacy changes in v2.1.301

**Claude Code** · 2026-10-15 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.301) · from [[Releases/Claude Code/claude-code-2026-10-15-v2-1-301-github-413913133-a3fb5b4e|v2.1.301]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `classifier_verdict` and `permission_mode` to OpenTelemetry `tool_decision` events, so auto mode classifier decisions can be told apart from permission rules

> Fixed a tool call cut off by a message sent mid-turn during its permission check being reported to the model as rejected by the user

> Fixed the permission prompt for a plugin or skill hook's `ask` decision not showing which plugin or skill the hook comes from

> Fixed workflow scripts asking for permission or being refused when read, edited or re-run after a Bash `cd` in the same session

> [VSCode] Fixed the native dictation audio module being loaded, to check microphone permission, where dictation is not offered (non-claude.ai sign-ins, remote windows)

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.301
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-15-2-interface-experience-changes-in-v2-1-301|2 Interface Experience changes in v2.1.301]] · Interface Experience
- [[Changes/Claude Code/2026-10-15-2-mobile-and-desktop-changes-in-v2-1-301|2 Mobile and Desktop changes in v2.1.301]] · Mobile and Desktop
- [[Changes/Claude Code/2026-10-15-improved-switching-to-a-model-with-a-smaller-context-window-a-conversation-too-l|Improved switching to a model with a smaller context window]] · Context Window
- [[Changes/Claude Code/2026-10-15-added-rows-to-a-mod-s-input-a-text-field-of-several-lines-in-the-terminal-where|Added rows to a mod's Input]] · Developer Workflow
- [[Changes/Claude Code/2026-10-15-7-other-changes-in-v2-1-301|7 other changes in v2.1.301]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-10-14 · Claude Code · [[Changes/Claude Code/2026-10-14-6-safety-and-privacy-changes-in-v2-1-299|6 Safety and Privacy changes in v2.1.299]]
- Later: 2026-10-16 · Claude Code · [[Changes/Claude Code/2026-10-16-2-safety-and-privacy-changes-in-v2-1-302|2 Safety and Privacy changes in v2.1.302]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-15-2735a2&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-15-5-safety-and-privacy-changes-in-v2-1-301.md%0ACard%20ID%3A%20claude-code-2026-10-15-2735a2%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.301%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->