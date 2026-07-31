---
card_id: claude-code-2026-04-20-7582bc
date: '2026-04-20'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|chatgpt-2022-12-15-9c6f9c]]'
  lag_days: 1222
  role: follower
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-04-13-improved-stalled-api-stream-handling-streams-now-abort-after-5-minutes-of-no-dat|claude-code-2026-04-13-c9394b]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: d8cfb6fa1e1d9f49f87cdd037103cdc9c4ef4aab4c653b2399044aef3423034d
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-03-26-added-claude-stream-idle-timeout-ms-env-var-to-configure-the-streaming-idle-watc|claude-code-2026-03-26-33b65d]]'
- '[[Changes/Claude Code/2026-04-10-improved-brief-mode-to-retry-once-when-claude-responds-with-plain-text-instead-o|claude-code-2026-04-10-b7511d]]'
- '[[Changes/Claude Code/2026-04-13-improved-stalled-api-stream-handling-streams-now-abort-after-5-minutes-of-no-dat|claude-code-2026-04-13-c9394b]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-20-v2-1-116-github-311446114-3b24dc7e|claude-code-2026-04-20-v2-1-116-github-311446114-3b24dc7e]]'
theme: reliability-performance
type: change
---

# `/resume` on large sessions is significantly faster (up to 67% on 40MB+ sessions

<!-- chronolog:begin region="description" -->
`/resume` on large sessions is significantly faster (up to 67% on 40MB+ sessions) and handles sessions with many dead-fork entries more efficiently
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> `/resume` on large sessions is significantly faster (up to 67% on 40MB+ sessions) and handles sessions with many dead-fork entries more efficiently
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.116
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-04-13-improved-stalled-api-stream-handling-streams-now-abort-after-5-minutes-of-no-dat|claude-code-2026-04-13-c9394b]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: reliability-performance
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|chatgpt-2022-12-15-9c6f9c]]
- Lag Days: 1222
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes