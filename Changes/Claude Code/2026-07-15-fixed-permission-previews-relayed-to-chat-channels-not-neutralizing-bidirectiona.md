---
card_id: claude-code-2026-07-15-ae07e9
date: '2026-07-15'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  lag_days: 1186
  role: follower
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-07-14-added-a-startup-warning-for-write-path-notebookedit-path-and-glob-path-permissio|claude-code-2026-07-14-f07656]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 5453faa3829f23344f758793253416929878199f90d93f2e65d1dde2cfdb829e
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-07-14-improved-auto-mode-the-permission-classifier-now-defaults-to-sonnet-5-for-extern|claude-code-2026-07-14-de216e]]'
- '[[Changes/Claude Code/2026-07-14-fixed-multi-second-per-turn-slowdowns-in-sessions-with-many-permission-deny-ask|claude-code-2026-07-14-df06b4]]'
- '[[Changes/Claude Code/2026-07-14-added-a-startup-warning-for-write-path-notebookedit-path-and-glob-path-permissio|claude-code-2026-07-14-f07656]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-15-v2-1-211-github-354658856-71e66e57|claude-code-2026-07-15-v2-1-211-github-354658856-71e66e57]]'
theme: safety-privacy
type: change
---

# Fixed permission previews relayed to chat channels not neutralizing bidirectiona

<!-- chronolog:begin region="description" -->
Fixed permission previews relayed to chat channels not neutralizing bidirectional-override, zero-width, and look-alike quote characters, so tool inputs cannot visually alter the approval message
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Fixed permission previews relayed to chat channels not neutralizing bidirectional-override, zero-width, and look-alike quote characters, so tool inputs cannot visually alter the approval message
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.211
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-07-14-added-a-startup-warning-for-write-path-notebookedit-path-and-glob-path-permissio|claude-code-2026-07-14-f07656]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: safety-privacy
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]
- Lag Days: 1186
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes