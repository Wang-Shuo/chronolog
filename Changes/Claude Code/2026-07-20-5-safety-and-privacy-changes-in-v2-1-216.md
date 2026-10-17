---
card_id: claude-code-2026-07-20-198876
date: '2026-07-20'
description: 'Claude Code · 2026-07-20 · Safety and Privacy: 5 changes in v2.1.216
  — Added `sandbox.filesystem.disabled` setting to skip filesystem isolation while
  keeping…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1191
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b4614c9d2df424b39b169891900e77750bf4239877f9ab0bdbed180e9b5fd286
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-07-20-198876
  comparison: ''
  date: '2026-07-20'
  description: 'Claude Code — v2.1.216: 5 Safety and Privacy changes'
  evidence:
  - quote: Added `sandbox.filesystem.disabled` setting to skip filesystem isolation
      while keeping network egress control
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.216
  - quote: Fixed Bash command permission checking for compound statements with redirects
      inside `&&` lists or negations
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.216
  - quote: Fixed read-only commands on Windows accessing network paths without a permission
      prompt
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.216
  - quote: Fixed PowerShell tool permission validation of commands containing invisible
      Unicode characters
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.216
  - quote: 'Fixed telemetry misreporting permission denials: failed permission-prompt
      requests no longer count as user rejections, and user interrupts are now reported
      as user aborts instead of rejections'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.216
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 5-safety-and-privacy-changes-in-v2-1-216
  source_release: claude-code-2026-07-20-v2-1-216-github-356972381-87e422ae
  source_type: github_releases
  theme: safety-privacy
  title: 5 Safety and Privacy changes in v2.1.216
  type: change
related_changes:
- '[[Changes/Claude Code/2026-07-15-2-safety-and-privacy-changes-in-v2-1-211|2 Safety
  and Privacy changes in v2.1.211]]'
- '[[Changes/Claude Code/2026-07-17-3-safety-and-privacy-changes-in-v2-1-212|3 Safety
  and Privacy changes in v2.1.212]]'
- '[[Changes/Claude Code/2026-07-18-9-safety-and-privacy-changes-in-v2-1-214|9 Safety
  and Privacy changes in v2.1.214]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-20-v2-1-216-github-356972381-87e422ae|claude-code-2026-07-20-v2-1-216-github-356972381-87e422ae]]'
source_type: github_releases
theme: safety-privacy
title: 5 Safety and Privacy changes in v2.1.216
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Safety and Privacy changes in v2.1.216

**Claude Code** · 2026-07-20 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.216) · from [[Releases/Claude Code/claude-code-2026-07-20-v2-1-216-github-356972381-87e422ae|v2.1.216]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `sandbox.filesystem.disabled` setting to skip filesystem isolation while keeping network egress control

> Fixed Bash command permission checking for compound statements with redirects inside `&&` lists or negations

> Fixed read-only commands on Windows accessing network paths without a permission prompt

> Fixed PowerShell tool permission validation of commands containing invisible Unicode characters

> Fixed telemetry misreporting permission denials: failed permission-prompt requests no longer count as user rejections, and user interrupts are now reported as user aborts instead of rejections

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.216
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-07-20-context-now-shows-an-explicit-warning-when-the-conversation-exceeds-the-context|/context now shows an explicit warning when the conversation exceeds the context…]] · Context Window
- [[Changes/Claude Code/2026-07-20-background-sessions-mcp-and-install-github-app-now-park-a-needs-input-request-in|Background sessions: /mcp and /install-github-app now park…]] · Apps and Integrations
- [[Changes/Claude Code/2026-07-20-improved-the-ultrareview-diff-too-large-error-to-show-configured-limits-measured|Improved the /ultrareview diff-too-large error to show configured limits, measured…]] · Editor Experience
- [[Changes/Claude Code/2026-07-20-2-developer-workflow-changes-in-v2-1-216|2 Developer Workflow changes in v2.1.216]] · Developer Workflow
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-07-18 · Claude Code · [[Changes/Claude Code/2026-07-18-9-safety-and-privacy-changes-in-v2-1-214|9 Safety and Privacy changes in v2.1.214]]
- Later: 2026-07-21 · Claude Code · [[Changes/Claude Code/2026-07-21-fixed-remote-control-sessions-not-showing-a-pending-permission-prompt-or-dialog|Fixed Remote Control sessions not showing a pending permission prompt or dialog…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-07-20-198876&body=Card%3A%20Changes%2FClaude%20Code%2F2026-07-20-5-safety-and-privacy-changes-in-v2-1-216.md%0ACard%20ID%3A%20claude-code-2026-07-20-198876%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.216%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->