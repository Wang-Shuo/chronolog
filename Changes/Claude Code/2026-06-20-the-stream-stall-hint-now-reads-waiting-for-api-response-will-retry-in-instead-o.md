---
card_id: claude-code-2026-06-20-ef4f72
date: '2026-06-20'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|chatgpt-2022-12-15-9c6f9c]]'
  lag_days: 1283
  role: follower
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-06-17-improved-auto-retry-api-connection-drops-mid-thinking-now-automatically-retry-in|claude-code-2026-06-17-acfb36]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 3da793397ba7f9f488078be4e1e0ea5c141596f7fd552d0d3b7be37416672fe9
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/ChatGPT/2026-06-17-all-tasks-are-faster-and-more-reliable|chatgpt-2026-06-17-281370]]'
- '[[Changes/Claude Code/2026-06-17-improved-auto-retry-api-connection-drops-mid-thinking-now-automatically-retry-in|claude-code-2026-06-17-acfb36]]'
- '[[Changes/Cursor/2026-06-17-your-environment-is-captured-in-a-reusable-snapshot-so-future-cloud-agents-start|cursor-2026-06-17-efeb40]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-20-v2-1-185-github-342367004-9ddb0cf9|claude-code-2026-06-20-v2-1-185-github-342367004-9ddb0cf9]]'
theme: reliability-performance
type: change
---

# The stream-stall hint now reads "Waiting for API response · will retry in …" ins

<!-- chronolog:begin region="description" -->
The stream-stall hint now reads "Waiting for API response · will retry in …" instead of "No response from API · Retrying in …", and triggers after 20s of silence instead of 10s
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> The stream-stall hint now reads "Waiting for API response · will retry in …" instead of "No response from API · Retrying in …", and triggers after 20s of silence instead of 10s
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.185
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-06-17-improved-auto-retry-api-connection-drops-mid-thinking-now-automatically-retry-in|claude-code-2026-06-17-acfb36]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: reliability-performance
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|chatgpt-2022-12-15-9c6f9c]]
- Lag Days: 1283
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes