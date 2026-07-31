---
card_id: claude-code-2026-07-18-e06205
date: '2026-07-18'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  lag_days: 1189
  role: follower
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-07-18-fixed-bash-permission-checks-misjudging-very-long-commands-commands-over-10-000|claude-code-2026-07-18-c7cc5a]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: b7d33c5d1f3887eaa1b0e16f189c34a01481e25ad4fa9de52d71f4c25f51dc1e
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-07-18-fixed-bash-permission-checks-treating-zsh-variable-subscripts-and-modifiers-in-c|claude-code-2026-07-18-75dc36]]'
- '[[Changes/Claude Code/2026-07-18-fixed-bash-permission-checks-to-no-longer-auto-approve-certain-help-and-man-comm|claude-code-2026-07-18-aa1dd6]]'
- '[[Changes/Claude Code/2026-07-18-fixed-bash-permission-checks-misjudging-very-long-commands-commands-over-10-000|claude-code-2026-07-18-c7cc5a]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-18-v2-1-214-github-355973317-478680c5|claude-code-2026-07-18-v2-1-214-github-355973317-478680c5]]'
theme: safety-privacy
type: change
---

# Fixed Bash permission checks to fail closed on file-descriptor redirect forms th

<!-- chronolog:begin region="description" -->
Fixed Bash permission checks to fail closed on file-descriptor redirect forms that bash parses differently than the permission analyzer
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Fixed Bash permission checks to fail closed on file-descriptor redirect forms that bash parses differently than the permission analyzer
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.214
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-07-18-fixed-bash-permission-checks-misjudging-very-long-commands-commands-over-10-000|claude-code-2026-07-18-c7cc5a]]
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