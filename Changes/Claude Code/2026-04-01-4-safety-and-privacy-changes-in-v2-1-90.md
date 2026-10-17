---
card_id: claude-code-2026-04-01-867c26
date: '2026-04-01'
description: 'Claude Code · 2026-04-01 · Safety and Privacy: 4 changes in v2.1.90
  — Added `.husky` to protected directories (acceptEdits mode)'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1081
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9c89c7106512b1a3fca729d37a023dd9d9bcb286fa1f9bc54a381f594ffecf77
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-04-01-867c26
  comparison: ''
  date: '2026-04-01'
  description: 'Claude Code — v2.1.90: 4 Safety and Privacy changes'
  evidence:
  - quote: Added `.husky` to protected directories (acceptEdits mode)
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.90
  - quote: Fixed UI crash when malformed tool input reached the permission dialog
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.90
  - quote: 'Hardened PowerShell tool permission checks: fixed trailing `&` background
      job bypass, `-ErrorAction Break` debugger hang, archive-extraction TOCTOU, and
      parse-fail fallback deny-rule degradation'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.90
  - quote: Removed `Get-DnsClientCache` and `ipconfig /displaydns` from auto-allow
      (DNS cache privacy)
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.90
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 4-safety-and-privacy-changes-in-v2-1-90
  source_release: claude-code-2026-04-01-v2-1-90-github-304453197-996aad1b
  source_type: github_releases
  theme: safety-privacy
  title: 4 Safety and Privacy changes in v2.1.90
  type: change
related_changes:
- '[[Changes/Claude Code/2026-03-26-2-safety-and-privacy-changes-in-v2-1-85|2 Safety
  and Privacy changes in v2.1.85]]'
- '[[Changes/Claude Code/2026-03-27-fixed-official-marketplace-plugin-scripts-failing-with-permission-denied-on-maco|Fixed
  official marketplace plugin scripts failing…]]'
- '[[Changes/Claude Code/2026-04-01-2-safety-and-privacy-changes-in-v2-1-89|2 Safety
  and Privacy changes in v2.1.89]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-01-v2-1-90-github-304453197-996aad1b|claude-code-2026-04-01-v2-1-90-github-304453197-996aad1b]]'
source_type: github_releases
theme: safety-privacy
title: 4 Safety and Privacy changes in v2.1.90
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Safety and Privacy changes in v2.1.90

**Claude Code** · 2026-04-01 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.90) · from [[Releases/Claude Code/claude-code-2026-04-01-v2-1-90-github-304453197-996aad1b|v2.1.90]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `.husky` to protected directories (acceptEdits mode)

> Fixed UI crash when malformed tool input reached the permission dialog

> Hardened PowerShell tool permission checks: fixed trailing `&` background job bypass, `-ErrorAction Break` debugger hang, archive-extraction TOCTOU, and parse-fail fallback deny-rule degradation

> Removed `Get-DnsClientCache` and `ipconfig /displaydns` from auto-allow (DNS cache privacy)

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.90
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-04-01-2-reliability-and-performance-changes-in-v2-1-90|2 Reliability and Performance changes in v2.1.90]] · Reliability and Performance
- [[Changes/Claude Code/2026-04-01-added-powerup-interactive-lessons-teaching-claude-code-features-with-animated-de|Added /powerup — interactive lessons teaching Claude Code features with animated demos]] · Learning Tools
- [[Changes/Claude Code/2026-04-01-changed-resume-picker-to-no-longer-show-sessions-created-by-claude-p-or-sdk-invo|Changed --resume picker to no longer show sessions created by claude -p or SDK…]] · Interface Experience
- [[Changes/Claude Code/2026-04-01-2-apps-and-integrations-changes-in-v2-1-90|2 Apps and Integrations changes in v2.1.90]] · Apps and Integrations
- [[Changes/Claude Code/2026-04-01-improved-resume-all-projects-view-to-load-project-sessions-in-parallel-improving|Improved /resume all-projects view to load project sessions in parallel, improving…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-04-01 · Claude Code · [[Changes/Claude Code/2026-04-01-2-safety-and-privacy-changes-in-v2-1-89|2 Safety and Privacy changes in v2.1.89]]
- Later: 2026-04-02 · Claude Code · [[Changes/Claude Code/2026-04-02-fixed-plan-mode-in-remote-sessions-losing-track-of-the-plan-file-after-a-contain|Fixed plan mode in remote sessions losing track of the plan file after a container…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-04-01-867c26&body=Card%3A%20Changes%2FClaude%20Code%2F2026-04-01-4-safety-and-privacy-changes-in-v2-1-90.md%0ACard%20ID%3A%20claude-code-2026-04-01-867c26%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.90%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->