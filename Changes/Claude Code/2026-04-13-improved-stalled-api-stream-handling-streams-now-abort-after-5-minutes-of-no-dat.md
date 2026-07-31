---
card_id: claude-code-2026-04-13-c9394b
date: '2026-04-13'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|chatgpt-2022-12-15-9c6f9c]]'
  lag_days: 1215
  role: follower
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-04-10-improved-brief-mode-to-retry-once-when-claude-responds-with-plain-text-instead-o|claude-code-2026-04-10-b7511d]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 399180b13bd4e1e5fe10670fa2c350f86796d65d79641f78a02f68046d54ebe5
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Cursor/2026-03-19-composer-2-is-now-available-in-cursor-frontier-level-coding-performance-with-str|cursor-2026-03-19-780a40]]'
- '[[Changes/Claude Code/2026-03-26-added-claude-stream-idle-timeout-ms-env-var-to-configure-the-streaming-idle-watc|claude-code-2026-03-26-33b65d]]'
- '[[Changes/Claude Code/2026-04-10-improved-brief-mode-to-retry-once-when-claude-responds-with-plain-text-instead-o|claude-code-2026-04-10-b7511d]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-13-v2-1-105-github-308569432-65a12cd3|claude-code-2026-04-13-v2-1-105-github-308569432-65a12cd3]]'
theme: reliability-performance
type: change
---

# Improved stalled API stream handling: streams now abort after 5 minutes of no da

<!-- chronolog:begin region="description" -->
Improved stalled API stream handling: streams now abort after 5 minutes of no data and retry non-streaming instead of hanging indefinitely
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Improved stalled API stream handling: streams now abort after 5 minutes of no data and retry non-streaming instead of hanging indefinitely
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.105
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-04-10-improved-brief-mode-to-retry-once-when-claude-responds-with-plain-text-instead-o|claude-code-2026-04-10-b7511d]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: reliability-performance
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|chatgpt-2022-12-15-9c6f9c]]
- Lag Days: 1215
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes