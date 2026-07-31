---
card_id: claude-code-2026-03-26-33b65d
date: '2026-03-26'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|chatgpt-2022-12-15-9c6f9c]]'
  lag_days: 1197
  role: follower
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-03-18-improved-non-streaming-api-fallback-with-a-2-minute-per-attempt-timeout-preventi|claude-code-2026-03-18-f2102f]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 7f74341b5fa99a3e1b7f163c1930644eff33489a2bfa58eeee941a5a8dfd2e55
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-03-18-improved-startup-memory-usage-by-18mb-across-all-scenarios|claude-code-2026-03-18-545a2b]]'
- '[[Changes/Claude Code/2026-03-18-improved-non-streaming-api-fallback-with-a-2-minute-per-attempt-timeout-preventi|claude-code-2026-03-18-f2102f]]'
- '[[Changes/Cursor/2026-03-19-composer-2-is-now-available-in-cursor-frontier-level-coding-performance-with-str|cursor-2026-03-19-780a40]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-26-v2-1-84-github-301540101-d02104aa|claude-code-2026-03-26-v2-1-84-github-301540101-d02104aa]]'
theme: reliability-performance
type: change
---

# Added `CLAUDE_STREAM_IDLE_TIMEOUT_MS` env var to configure the streaming idle wa

<!-- chronolog:begin region="description" -->
Added `CLAUDE_STREAM_IDLE_TIMEOUT_MS` env var to configure the streaming idle watchdog threshold (default 90s)
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `CLAUDE_STREAM_IDLE_TIMEOUT_MS` env var to configure the streaming idle watchdog threshold (default 90s)
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.84
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-03-18-improved-non-streaming-api-fallback-with-a-2-minute-per-attempt-timeout-preventi|claude-code-2026-03-18-f2102f]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: reliability-performance
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|chatgpt-2022-12-15-9c6f9c]]
- Lag Days: 1197
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes