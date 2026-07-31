---
card_id: claude-code-2026-07-21-5131b9
date: '2026-07-21'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|chatgpt-2022-12-15-9c6f9c]]'
  lag_days: 1314
  role: follower
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-07-08-auto-update-binary-downloads-now-stream-to-disk-instead-of-buffering-in-memory-c|claude-code-2026-07-08-bf6c5c]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 0d25f8cd4ef540282fca3c2078d914c647759a0fb6f5bdebbef07df2bcbdc93e
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-07-03-improved-the-install-script-to-explain-when-installation-is-killed-by-the-system|claude-code-2026-07-03-39f603]]'
- '[[Changes/Claude Code/2026-07-07-improved-responsiveness-while-long-responses-stream-live-preview-updates-no-long|claude-code-2026-07-07-8a4dff]]'
- '[[Changes/Claude Code/2026-07-08-auto-update-binary-downloads-now-stream-to-disk-instead-of-buffering-in-memory-c|claude-code-2026-07-08-bf6c5c]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-21-v2-1-217-github-357601516-b5c19f5d|claude-code-2026-07-21-v2-1-217-github-357601516-b5c19f5d]]'
theme: reliability-performance
type: change
---

# Added warnings when transcript writes are failing (e.g. disk full) or when sessi

<!-- chronolog:begin region="description" -->
Added warnings when transcript writes are failing (e.g. disk full) or when session saving is off due to an inherited environment variable, instead of losing transcripts silently
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added warnings when transcript writes are failing (e.g. disk full) or when session saving is off due to an inherited environment variable, instead of losing transcripts silently
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.217
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-07-08-auto-update-binary-downloads-now-stream-to-disk-instead-of-buffering-in-memory-c|claude-code-2026-07-08-bf6c5c]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: reliability-performance
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|chatgpt-2022-12-15-9c6f9c]]
- Lag Days: 1314
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes