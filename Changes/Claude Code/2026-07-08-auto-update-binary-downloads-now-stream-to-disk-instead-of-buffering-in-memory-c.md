---
card_id: claude-code-2026-07-08-bf6c5c
date: '2026-07-08'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|chatgpt-2022-12-15-9c6f9c]]'
  lag_days: 1301
  role: follower
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-07-07-improved-responsiveness-while-long-responses-stream-live-preview-updates-no-long|claude-code-2026-07-07-8a4dff]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 303a512ec90577a22f317cbdf67e97b7d4ad2a0ba3011018921d28a68df70835
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-07-02-claude-code-retry-watchdog-now-raises-the-default-retry-count-for-non-capacity-t|claude-code-2026-07-02-ebe592]]'
- '[[Changes/Claude Code/2026-07-03-improved-the-install-script-to-explain-when-installation-is-killed-by-the-system|claude-code-2026-07-03-39f603]]'
- '[[Changes/Claude Code/2026-07-07-improved-responsiveness-while-long-responses-stream-live-preview-updates-no-long|claude-code-2026-07-07-8a4dff]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-08-v2-1-205-github-351140412-aeced5ba|claude-code-2026-07-08-v2-1-205-github-351140412-aeced5ba]]'
theme: reliability-performance
type: change
---

# Auto-update binary downloads now stream to disk instead of buffering in memory,

<!-- chronolog:begin region="description" -->
Auto-update binary downloads now stream to disk instead of buffering in memory, cutting the updater's peak memory usage by roughly 400 MB
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Auto-update binary downloads now stream to disk instead of buffering in memory, cutting the updater's peak memory usage by roughly 400 MB
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.205
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-07-07-improved-responsiveness-while-long-responses-stream-live-preview-updates-no-long|claude-code-2026-07-07-8a4dff]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: reliability-performance
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|chatgpt-2022-12-15-9c6f9c]]
- Lag Days: 1301
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes