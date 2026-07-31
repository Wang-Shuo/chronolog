---
card_id: claude-code-2026-06-17-acfb36
date: '2026-06-17'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|chatgpt-2022-12-15-9c6f9c]]'
  lag_days: 1280
  role: follower
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-06-12-improved-bedrock-credential-caching-credentials-from-awscredentialexport-are-now|claude-code-2026-06-12-c6b174]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 504c098c668b1b9c71d93eaf3266370fad7face64a08f987cf54aea7f64e74f0
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-06-12-improved-bedrock-credential-caching-credentials-from-awscredentialexport-are-now|claude-code-2026-06-12-c6b174]]'
- '[[Changes/ChatGPT/2026-06-17-with-scheduled-tasks-users-can-ask-chatgpt-to-send-reminders-handle-recurring-wo|chatgpt-2026-06-17-09675e]]'
- '[[Changes/ChatGPT/2026-06-17-all-tasks-are-faster-and-more-reliable|chatgpt-2026-06-17-281370]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-17-v2-1-181-github-340975229-c771c493|claude-code-2026-06-17-v2-1-181-github-340975229-c771c493]]'
theme: reliability-performance
type: change
---

# Improved auto-retry: API connection drops mid-thinking now automatically retry i

<!-- chronolog:begin region="description" -->
Improved auto-retry: API connection drops mid-thinking now automatically retry instead of showing "Connection closed while thinking"
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Improved auto-retry: API connection drops mid-thinking now automatically retry instead of showing "Connection closed while thinking"
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.181
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-06-12-improved-bedrock-credential-caching-credentials-from-awscredentialexport-are-now|claude-code-2026-06-12-c6b174]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: reliability-performance
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|chatgpt-2022-12-15-9c6f9c]]
- Lag Days: 1280
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes