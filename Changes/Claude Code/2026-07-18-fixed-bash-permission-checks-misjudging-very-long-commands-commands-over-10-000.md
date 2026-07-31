---
card_id: claude-code-2026-07-18-c7cc5a
date: '2026-07-18'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  lag_days: 1189
  role: follower
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-07-18-fixed-bash-permission-checks-to-no-longer-auto-approve-certain-help-and-man-comm|claude-code-2026-07-18-aa1dd6]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: beca5ddf0c5e061de0f543c8c1830f3feeb11975c600479f3c90fe7adc0bb101
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-07-18-fixed-a-permission-check-bypass-affecting-commands-run-in-windows-powershell-5-1|claude-code-2026-07-18-70feaa]]'
- '[[Changes/Claude Code/2026-07-18-fixed-bash-permission-checks-treating-zsh-variable-subscripts-and-modifiers-in-c|claude-code-2026-07-18-75dc36]]'
- '[[Changes/Claude Code/2026-07-18-fixed-bash-permission-checks-to-no-longer-auto-approve-certain-help-and-man-comm|claude-code-2026-07-18-aa1dd6]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-18-v2-1-214-github-355973317-478680c5|claude-code-2026-07-18-v2-1-214-github-355973317-478680c5]]'
theme: safety-privacy
type: change
---

# Fixed Bash permission checks misjudging very long commands — commands over 10,00

<!-- chronolog:begin region="description" -->
Fixed Bash permission checks misjudging very long commands — commands over 10,000 characters now always prompt instead of running automatically
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Fixed Bash permission checks misjudging very long commands — commands over 10,000 characters now always prompt instead of running automatically
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.214
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-07-18-fixed-bash-permission-checks-to-no-longer-auto-approve-certain-help-and-man-comm|claude-code-2026-07-18-aa1dd6]]
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