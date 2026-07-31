---
card_id: claude-code-2026-07-21-608ceb
date: '2026-07-21'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  lag_days: 1192
  role: follower
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-07-20-fixed-powershell-tool-permission-validation-of-commands-containing-invisible-uni|claude-code-2026-07-20-e38a9f]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: ea2ffb49a30bd8b5682a4748f10595dac66a7f4ea855910a4c39b496a17697dd
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-07-20-fixed-read-only-commands-on-windows-accessing-network-paths-without-a-permission|claude-code-2026-07-20-bb1a4e]]'
- '[[Changes/Claude Code/2026-07-20-fixed-bash-command-permission-checking-for-compound-statements-with-redirects-in|claude-code-2026-07-20-cdef23]]'
- '[[Changes/Claude Code/2026-07-20-fixed-powershell-tool-permission-validation-of-commands-containing-invisible-uni|claude-code-2026-07-20-e38a9f]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-21-v2-1-217-github-357601516-b5c19f5d|claude-code-2026-07-21-v2-1-217-github-357601516-b5c19f5d]]'
theme: safety-privacy
type: change
---

# Fixed Remote Control sessions not showing a pending permission prompt or dialog

<!-- chronolog:begin region="description" -->
Fixed Remote Control sessions not showing a pending permission prompt or dialog to viewers that connected after it appeared
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Fixed Remote Control sessions not showing a pending permission prompt or dialog to viewers that connected after it appeared
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.217
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-07-20-fixed-powershell-tool-permission-validation-of-commands-containing-invisible-uni|claude-code-2026-07-20-e38a9f]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: safety-privacy
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]
- Lag Days: 1192
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes