---
card_id: claude-code-2026-07-20-47c44c
date: '2026-07-20'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  lag_days: 1191
  role: follower
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-07-18-fixed-bash-permission-checks-to-fail-closed-on-file-descriptor-redirect-forms-th|claude-code-2026-07-18-e06205]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 2883e8098d5995427f04401377d4d40241ff87d6fbefb90c37139532101ba894
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-07-18-fixed-bash-permission-checks-to-no-longer-auto-approve-certain-help-and-man-comm|claude-code-2026-07-18-aa1dd6]]'
- '[[Changes/Claude Code/2026-07-18-fixed-bash-permission-checks-misjudging-very-long-commands-commands-over-10-000|claude-code-2026-07-18-c7cc5a]]'
- '[[Changes/Claude Code/2026-07-18-fixed-bash-permission-checks-to-fail-closed-on-file-descriptor-redirect-forms-th|claude-code-2026-07-18-e06205]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-20-v2-1-216-github-356972381-87e422ae|claude-code-2026-07-20-v2-1-216-github-356972381-87e422ae]]'
theme: safety-privacy
type: change
---

# Fixed telemetry misreporting permission denials: failed permission-prompt reques

<!-- chronolog:begin region="description" -->
Fixed telemetry misreporting permission denials: failed permission-prompt requests no longer count as user rejections, and user interrupts are now reported as user aborts instead of rejections
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Fixed telemetry misreporting permission denials: failed permission-prompt requests no longer count as user rejections, and user interrupts are now reported as user aborts instead of rejections
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.216
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-07-18-fixed-bash-permission-checks-to-fail-closed-on-file-descriptor-redirect-forms-th|claude-code-2026-07-18-e06205]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: safety-privacy
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]
- Lag Days: 1191
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes