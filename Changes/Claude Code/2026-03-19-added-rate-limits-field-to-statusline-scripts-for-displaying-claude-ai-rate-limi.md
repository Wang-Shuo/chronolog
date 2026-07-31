---
card_id: claude-code-2026-03-19-5110e3
date: '2026-03-19'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|chatgpt-2023-01-09-254e7f]]'
  lag_days: 1165
  role: follower
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-03-18-added-show-turn-duration-toggle-to-the-config-menu|claude-code-2026-03-18-dd12a8]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 3ab99810115379de9e58d4c77ca47a319a408a4792b0aba7e07f3a7ed50766bc
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-03-17-copy-now-accepts-an-optional-index-copy-n-copies-the-nth-latest-assistant-respon|claude-code-2026-03-17-4c7440]]'
- '[[Changes/Claude Code/2026-03-17-response-text-now-streams-line-by-line-as-it-s-generated|claude-code-2026-03-17-cd3956]]'
- '[[Changes/Claude Code/2026-03-18-added-show-turn-duration-toggle-to-the-config-menu|claude-code-2026-03-18-dd12a8]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-19-v2-1-80-github-299176707-1bfcfc3a|claude-code-2026-03-19-v2-1-80-github-299176707-1bfcfc3a]]'
theme: interface-experience
type: change
---

# Added `rate_limits` field to statusline scripts for displaying Claude.ai rate li

<!-- chronolog:begin region="description" -->
Added `rate_limits` field to statusline scripts for displaying Claude.ai rate limit usage (5-hour and 7-day windows with `used_percentage` and `resets_at`)
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `rate_limits` field to statusline scripts for displaying Claude.ai rate limit usage (5-hour and 7-day windows with `used_percentage` and `resets_at`)
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.80
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-03-18-added-show-turn-duration-toggle-to-the-config-menu|claude-code-2026-03-18-dd12a8]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: interface-experience
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|chatgpt-2023-01-09-254e7f]]
- Lag Days: 1165
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes