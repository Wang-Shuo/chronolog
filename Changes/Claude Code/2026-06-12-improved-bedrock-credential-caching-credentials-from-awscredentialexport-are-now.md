---
card_id: claude-code-2026-06-12-c6b174
date: '2026-06-12'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|chatgpt-2022-12-15-9c6f9c]]'
  lag_days: 1275
  role: follower
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-06-12-background-sessions-now-show-clearer-guidance-when-a-window-left-open-across-an|claude-code-2026-06-12-59f62e]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 72ddbbfc5f70ac0b61195f4394e33358f9fdaf2375a21341dd052f2cd4f85453
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Cursor/2026-06-10-these-performance-gains-are-made-possible-by-progress-we-ve-made-training-compos|cursor-2026-06-10-573114]]'
- '[[Changes/Cursor/2026-06-10-the-average-review-time-for-bugbot-is-now-90-seconds-down-from-5-minutes-bugbot|cursor-2026-06-10-a23fef]]'
- '[[Changes/Claude Code/2026-06-12-background-sessions-now-show-clearer-guidance-when-a-window-left-open-across-an|claude-code-2026-06-12-59f62e]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-12-v2-1-176-github-338777362-91e3deb6|claude-code-2026-06-12-v2-1-176-github-338777362-91e3deb6]]'
theme: reliability-performance
type: change
---

# Improved Bedrock credential caching: credentials from `awsCredentialExport` are

<!-- chronolog:begin region="description" -->
Improved Bedrock credential caching: credentials from `awsCredentialExport` are now cached until their `Expiration` instead of a fixed 1 hour
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Improved Bedrock credential caching: credentials from `awsCredentialExport` are now cached until their `Expiration` instead of a fixed 1 hour
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.176
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-06-12-background-sessions-now-show-clearer-guidance-when-a-window-left-open-across-an|claude-code-2026-06-12-59f62e]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: reliability-performance
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|chatgpt-2022-12-15-9c6f9c]]
- Lag Days: 1275
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes