---
card_id: claude-code-2026-03-18-f2102f
date: '2026-03-18'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|chatgpt-2022-12-15-9c6f9c]]'
  lag_days: 1189
  role: follower
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-03-18-improved-startup-memory-usage-by-18mb-across-all-scenarios|claude-code-2026-03-18-545a2b]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 81afb5538a6e0f4a5ecc88f4831713625921eb84d03a41ccad2d909319c6cc53
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-03-06-improved-compaction-to-preserve-images-in-the-summarizer-request-allowing-prompt|claude-code-2026-03-06-520da5]]'
- '[[Changes/Claude Code/2026-03-11-improved-ide-detection-speed-at-startup|claude-code-2026-03-11-0796c1]]'
- '[[Changes/Claude Code/2026-03-18-improved-startup-memory-usage-by-18mb-across-all-scenarios|claude-code-2026-03-18-545a2b]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-18-v2-1-79-github-298704791-2ebf4bbd|claude-code-2026-03-18-v2-1-79-github-298704791-2ebf4bbd]]'
theme: reliability-performance
type: change
---

# Improved non-streaming API fallback with a 2-minute per-attempt timeout, prevent

<!-- chronolog:begin region="description" -->
Improved non-streaming API fallback with a 2-minute per-attempt timeout, preventing sessions from hanging indefinitely
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Improved non-streaming API fallback with a 2-minute per-attempt timeout, preventing sessions from hanging indefinitely
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.79
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-03-18-improved-startup-memory-usage-by-18mb-across-all-scenarios|claude-code-2026-03-18-545a2b]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: reliability-performance
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|chatgpt-2022-12-15-9c6f9c]]
- Lag Days: 1189
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes