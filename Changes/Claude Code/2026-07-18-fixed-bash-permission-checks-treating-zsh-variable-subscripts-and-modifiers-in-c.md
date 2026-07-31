---
card_id: claude-code-2026-07-18-75dc36
date: '2026-07-18'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  lag_days: 1189
  role: follower
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-07-18-fixed-a-permission-check-bypass-affecting-commands-run-in-windows-powershell-5-1|claude-code-2026-07-18-70feaa]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 51e6d917bc4013fd5bbf91dde6158e1c7f9e93e29131940537b93383f45aeaf0
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-07-14-added-a-startup-warning-for-write-path-notebookedit-path-and-glob-path-permissio|claude-code-2026-07-14-f07656]]'
- '[[Changes/Claude Code/2026-07-15-fixed-permission-previews-relayed-to-chat-channels-not-neutralizing-bidirectiona|claude-code-2026-07-15-ae07e9]]'
- '[[Changes/Claude Code/2026-07-18-fixed-a-permission-check-bypass-affecting-commands-run-in-windows-powershell-5-1|claude-code-2026-07-18-70feaa]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-18-v2-1-214-github-355973317-478680c5|claude-code-2026-07-18-v2-1-214-github-355973317-478680c5]]'
theme: safety-privacy
type: change
---

# Fixed Bash permission checks treating zsh variable subscripts and modifiers in `

<!-- chronolog:begin region="description" -->
Fixed Bash permission checks treating zsh variable subscripts and modifiers in `[[ ]]` comparisons as inert text — these commands now prompt for approval
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Fixed Bash permission checks treating zsh variable subscripts and modifiers in `[[ ]]` comparisons as inert text — these commands now prompt for approval
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.214
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-07-18-fixed-a-permission-check-bypass-affecting-commands-run-in-windows-powershell-5-1|claude-code-2026-07-18-70feaa]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: safety-privacy
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]
- Lag Days: 1189
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes