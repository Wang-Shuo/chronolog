---
card_id: claude-code-2026-07-02-ebe592
date: '2026-07-02'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|chatgpt-2022-12-15-9c6f9c]]'
  lag_days: 1295
  role: follower
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-07-02-transient-server-rate-limit-errors-429s-unrelated-to-your-usage-limit-are-now-re|claude-code-2026-07-02-964eea]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 8a5280411555c4c29b13dd57713eabd6eff310d311adf4bf5ed51401b5375c7a
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Cursor/2026-06-17-your-environment-is-captured-in-a-reusable-snapshot-so-future-cloud-agents-start|cursor-2026-06-17-efeb40]]'
- '[[Changes/Claude Code/2026-06-20-the-stream-stall-hint-now-reads-waiting-for-api-response-will-retry-in-instead-o|claude-code-2026-06-20-ef4f72]]'
- '[[Changes/Claude Code/2026-07-02-transient-server-rate-limit-errors-429s-unrelated-to-your-usage-limit-are-now-re|claude-code-2026-07-02-964eea]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-02-v2-1-199-github-348195313-a8a76d9f|claude-code-2026-07-02-v2-1-199-github-348195313-a8a76d9f]]'
theme: reliability-performance
type: change
---

# `CLAUDE_CODE_RETRY_WATCHDOG` now raises the default retry count for non-capacity

<!-- chronolog:begin region="description" -->
`CLAUDE_CODE_RETRY_WATCHDOG` now raises the default retry count for non-capacity transient errors to 300 and lifts the cap of 15 on `CLAUDE_CODE_MAX_RETRIES`
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> `CLAUDE_CODE_RETRY_WATCHDOG` now raises the default retry count for non-capacity transient errors to 300 and lifts the cap of 15 on `CLAUDE_CODE_MAX_RETRIES`
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.199
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-07-02-transient-server-rate-limit-errors-429s-unrelated-to-your-usage-limit-are-now-re|claude-code-2026-07-02-964eea]]
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