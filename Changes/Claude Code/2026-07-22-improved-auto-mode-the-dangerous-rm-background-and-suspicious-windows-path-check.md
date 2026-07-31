---
card_id: claude-code-2026-07-22-56473f
date: '2026-07-22'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  lag_days: 1193
  role: follower
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-07-21-fixed-remote-control-sessions-not-showing-a-pending-permission-prompt-or-dialog|claude-code-2026-07-21-608ceb]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 6a82ab9dadd32f5af8c85906f6a98915819fb289031597eb38d22e83445bc83d
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-07-20-fixed-bash-command-permission-checking-for-compound-statements-with-redirects-in|claude-code-2026-07-20-cdef23]]'
- '[[Changes/Claude Code/2026-07-20-fixed-powershell-tool-permission-validation-of-commands-containing-invisible-uni|claude-code-2026-07-20-e38a9f]]'
- '[[Changes/Claude Code/2026-07-21-fixed-remote-control-sessions-not-showing-a-pending-permission-prompt-or-dialog|claude-code-2026-07-21-608ceb]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-22-v2-1-218-github-358276841-57d73db4|claude-code-2026-07-22-v2-1-218-github-358276841-57d73db4]]'
theme: safety-privacy
type: change
---

# Improved auto mode: the dangerous-rm, background-`&`, and suspicious-Windows-pat

<!-- chronolog:begin region="description" -->
Improved auto mode: the dangerous-rm, background-`&`, and suspicious-Windows-path checks no longer open permission dialogs; the auto-mode classifier adjudicates them instead
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Improved auto mode: the dangerous-rm, background-`&`, and suspicious-Windows-path checks no longer open permission dialogs; the auto-mode classifier adjudicates them instead
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.218
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-07-21-fixed-remote-control-sessions-not-showing-a-pending-permission-prompt-or-dialog|claude-code-2026-07-21-608ceb]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: safety-privacy
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]
- Lag Days: 1193
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes