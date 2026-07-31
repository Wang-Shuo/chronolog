---
card_id: claude-code-2026-03-27-358253
date: '2026-03-27'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]'
  lag_days: 1105
  role: follower
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-03-26-added-worktreecreate-hook-support-for-type-http-return-the-created-worktree-path|claude-code-2026-03-26-b1182f]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 477fccc1e982dcdeb7981d3c7ea7863d328222991854c921d310dccf45795165
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-03-20-resuming-a-session-that-was-in-a-worktree-now-switches-back-to-that-worktree|claude-code-2026-03-20-c20f4f]]'
- '[[Changes/Claude Code/2026-03-20-added-bare-flag-for-scripted-p-calls-skips-hooks-lsp-plugin-sync-and-skill-direc|claude-code-2026-03-20-d05f5d]]'
- '[[Changes/Claude Code/2026-03-26-added-worktreecreate-hook-support-for-type-http-return-the-created-worktree-path|claude-code-2026-03-26-b1182f]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-27-v2-1-86-github-302569462-d6b30859|claude-code-2026-03-27-v2-1-86-github-302569462-d6b30859]]'
theme: developer-workflow
type: change
---

# Added `X-Claude-Code-Session-Id` header to API requests so proxies can aggregate

<!-- chronolog:begin region="description" -->
Added `X-Claude-Code-Session-Id` header to API requests so proxies can aggregate requests by session without parsing the body
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `X-Claude-Code-Session-Id` header to API requests so proxies can aggregate requests by session without parsing the body
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.86
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-03-26-added-worktreecreate-hook-support-for-type-http-return-the-created-worktree-path|claude-code-2026-03-26-b1182f]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: developer-workflow
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]
- Lag Days: 1105
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes