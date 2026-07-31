---
card_id: claude-code-2026-07-20-cdef23
date: '2026-07-20'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  lag_days: 1191
  role: follower
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-07-20-fixed-read-only-commands-on-windows-accessing-network-paths-without-a-permission|claude-code-2026-07-20-bb1a4e]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 94e16db8abc81e467d035bca185ca5e9fbcde1563bc56d1e046a5b4c5745206a
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-07-20-fixed-telemetry-misreporting-permission-denials-failed-permission-prompt-request|claude-code-2026-07-20-47c44c]]'
- '[[Changes/Claude Code/2026-07-20-added-sandbox-filesystem-disabled-setting-to-skip-filesystem-isolation-while-kee|claude-code-2026-07-20-b887a9]]'
- '[[Changes/Claude Code/2026-07-20-fixed-read-only-commands-on-windows-accessing-network-paths-without-a-permission|claude-code-2026-07-20-bb1a4e]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-20-v2-1-216-github-356972381-87e422ae|claude-code-2026-07-20-v2-1-216-github-356972381-87e422ae]]'
theme: safety-privacy
type: change
---

# Fixed Bash command permission checking for compound statements with redirects in

<!-- chronolog:begin region="description" -->
Fixed Bash command permission checking for compound statements with redirects inside `&&` lists or negations
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Fixed Bash command permission checking for compound statements with redirects inside `&&` lists or negations
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.216
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-07-20-fixed-read-only-commands-on-windows-accessing-network-paths-without-a-permission|claude-code-2026-07-20-bb1a4e]]
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