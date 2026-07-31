---
card_id: claude-code-2026-04-13-467b16
date: '2026-04-13'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]'
  lag_days: 1122
  role: follower
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-04-08-added-workspace-git-worktree-to-the-status-line-json-input-set-when-the-current|claude-code-2026-04-08-cfa4a0]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 32957c9ff7801868bd87bdd94336cc7d34689cfdfee9355b3ed7763fd78be083
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Cursor/2026-04-02-the-new-cursor-interface-allows-you-to-run-many-agents-in-parallel-across-repos|cursor-2026-04-02-57045c]]'
- '[[Changes/Claude Code/2026-04-08-added-workspace-git-worktree-to-the-status-line-json-input-set-when-the-current|claude-code-2026-04-08-cfa4a0]]'
- '[[Changes/Cursor/2026-04-08-bugbot-can-now-learn-from-feedback-on-pull-requests-and-turn-those-signals-into|cursor-2026-04-08-c2b592]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-13-v2-1-105-github-308569432-65a12cd3|claude-code-2026-04-13-v2-1-105-github-308569432-65a12cd3]]'
theme: developer-workflow
type: change
---

# Added `path` parameter to the `EnterWorktree` tool to switch into an existing wo

<!-- chronolog:begin region="description" -->
Added `path` parameter to the `EnterWorktree` tool to switch into an existing worktree of the current repository
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `path` parameter to the `EnterWorktree` tool to switch into an existing worktree of the current repository
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.105
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-04-08-added-workspace-git-worktree-to-the-status-line-json-input-set-when-the-current|claude-code-2026-04-08-cfa4a0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: developer-workflow
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]
- Lag Days: 1122
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes