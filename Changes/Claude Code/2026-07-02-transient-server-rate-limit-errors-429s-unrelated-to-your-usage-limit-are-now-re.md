---
card_id: claude-code-2026-07-02-964eea
date: '2026-07-02'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|chatgpt-2022-12-15-9c6f9c]]'
  lag_days: 1295
  role: follower
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-06-20-the-stream-stall-hint-now-reads-waiting-for-api-response-will-retry-in-instead-o|claude-code-2026-06-20-ef4f72]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 844b3ecff845f52c975de87a5803a177dd272c5b44a704d4dc9e8dccd2cbaeb0
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-06-17-improved-auto-retry-api-connection-drops-mid-thinking-now-automatically-retry-in|claude-code-2026-06-17-acfb36]]'
- '[[Changes/Cursor/2026-06-17-your-environment-is-captured-in-a-reusable-snapshot-so-future-cloud-agents-start|cursor-2026-06-17-efeb40]]'
- '[[Changes/Claude Code/2026-06-20-the-stream-stall-hint-now-reads-waiting-for-api-response-will-retry-in-instead-o|claude-code-2026-06-20-ef4f72]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-02-v2-1-199-github-348195313-a8a76d9f|claude-code-2026-07-02-v2-1-199-github-348195313-a8a76d9f]]'
theme: reliability-performance
type: change
---

# Transient server rate-limit errors (429s unrelated to your usage limit) are now

<!-- chronolog:begin region="description" -->
Transient server rate-limit errors (429s unrelated to your usage limit) are now retried automatically with backoff for subscribers instead of failing the turn
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Transient server rate-limit errors (429s unrelated to your usage limit) are now retried automatically with backoff for subscribers instead of failing the turn
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.199
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-06-20-the-stream-stall-hint-now-reads-waiting-for-api-response-will-retry-in-instead-o|claude-code-2026-06-20-ef4f72]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: reliability-performance
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|chatgpt-2022-12-15-9c6f9c]]
- Lag Days: 1295
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes