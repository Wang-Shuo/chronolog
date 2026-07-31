---
card_id: claude-code-2026-04-08-cfa4a0
date: '2026-04-08'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]'
  lag_days: 1117
  role: follower
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-03-27-added-x-claude-code-session-id-header-to-api-requests-so-proxies-can-aggregate-r|claude-code-2026-03-27-358253]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 8cbe1467f07588b03dc6884999876e3e43a4aa90e2ac756809c5f82c03eff81b
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-03-26-added-worktreecreate-hook-support-for-type-http-return-the-created-worktree-path|claude-code-2026-03-26-b1182f]]'
- '[[Changes/Claude Code/2026-03-27-added-x-claude-code-session-id-header-to-api-requests-so-proxies-can-aggregate-r|claude-code-2026-03-27-358253]]'
- '[[Changes/Cursor/2026-04-02-the-new-cursor-interface-allows-you-to-run-many-agents-in-parallel-across-repos|cursor-2026-04-02-57045c]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-08-v2-1-97-github-306811434-0f57bf33|claude-code-2026-04-08-v2-1-97-github-306811434-0f57bf33]]'
theme: developer-workflow
type: change
---

# Added `workspace.git_worktree` to the status line JSON input, set when the curre

<!-- chronolog:begin region="description" -->
Added `workspace.git_worktree` to the status line JSON input, set when the current directory is inside a linked git worktree
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `workspace.git_worktree` to the status line JSON input, set when the current directory is inside a linked git worktree
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.97
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-03-27-added-x-claude-code-session-id-header-to-api-requests-so-proxies-can-aggregate-r|claude-code-2026-03-27-358253]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: developer-workflow
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]
- Lag Days: 1117
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes