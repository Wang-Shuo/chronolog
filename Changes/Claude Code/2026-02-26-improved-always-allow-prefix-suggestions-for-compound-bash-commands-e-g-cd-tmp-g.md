---
card_id: claude-code-2026-02-26-d7531f
date: '2026-02-26'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]'
  lag_days: 1076
  role: follower
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-02-20-added-support-for-startuptimeout-configuration-for-lsp-servers|claude-code-2026-02-20-aba95d]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 0abbc1c29dfb661b86ccc0d8025f83c98a3df9a20cdf729b228a6cac399ae2ed
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/ChatGPT/2026-02-19-review-code-in-split-screen-views|chatgpt-2026-02-19-97cccf]]'
- '[[Changes/Claude Code/2026-02-20-added-worktreecreate-and-worktreeremove-hook-events-enabling-custom-vcs-setup-an|claude-code-2026-02-20-648196]]'
- '[[Changes/Claude Code/2026-02-20-added-support-for-startuptimeout-configuration-for-lsp-servers|claude-code-2026-02-20-aba95d]]'
source_release: '[[Releases/Claude Code/claude-code-2026-02-26-v2-1-59-github-290659389-9e2d6217|claude-code-2026-02-26-v2-1-59-github-290659389-9e2d6217]]'
theme: developer-workflow
type: change
---

# Improved "always allow" prefix suggestions for compound bash commands (e.g. `cd

<!-- chronolog:begin region="description" -->
Improved "always allow" prefix suggestions for compound bash commands (e.g. `cd /tmp && git fetch && git push`) to compute smarter per-subcommand prefixes instead of treating the whole command as one
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Improved "always allow" prefix suggestions for compound bash commands (e.g. `cd /tmp && git fetch && git push`) to compute smarter per-subcommand prefixes instead of treating the whole command as one
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.59
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-02-20-added-support-for-startuptimeout-configuration-for-lsp-servers|claude-code-2026-02-20-aba95d]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: developer-workflow
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]
- Lag Days: 1076
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes