---
card_id: claude-code-2026-01-13-00ffe3
date: '2026-01-13'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-extended-prompt-length-for-project-generation|cursor-2023-05-04-00d3b7]]'
  lag_days: 985
  role: follower
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v2
impact: incremental
machine_hash: 20ca8966e9837c7077cfe2b84362aa0415fb1aff9e2d56f53cfcd2daca45f9ae
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Cursor/2025-09-12-summarization-triggers|cursor-2025-09-12-1d0b7f]]'
- '[[Changes/Cursor/2025-09-12-cursor-automatically-summarizes-long-conversation-for-you-when-reaching-the-cont|cursor-2025-09-12-7d0a07]]'
- '[[Changes/Cursor/2025-12-18-cursor-can-now-analyze-the-code-and-context-in-each-agent-session-to-understand|cursor-2025-12-18-becfd8]]'
source_release: '[[Releases/Claude Code/claude-code-2026-01-13-v2-1-6-github-276206295-e2719d9a|claude-code-2026-01-13-v2-1-6-github-276206295-e2719d9a]]'
theme: context-window
type: change
---

# Added `context_window.used_percentage` and `context_window.remaining_percentage`

<!-- chronolog:begin region="description" -->
Added `context_window.used_percentage` and `context_window.remaining_percentage` fields to status line input for easier context window display
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `context_window.used_percentage` and `context_window.remaining_percentage` fields to status line input for easier context window display
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.6
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
No prior tracked change.
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: context-window
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-05-04-extended-prompt-length-for-project-generation|cursor-2023-05-04-00d3b7]]
- Lag Days: 985
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes