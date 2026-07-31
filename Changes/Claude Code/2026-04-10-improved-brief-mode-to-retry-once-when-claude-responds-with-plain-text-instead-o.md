---
card_id: claude-code-2026-04-10-b7511d
date: '2026-04-10'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|chatgpt-2022-12-15-9c6f9c]]'
  lag_days: 1212
  role: follower
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-03-26-added-claude-stream-idle-timeout-ms-env-var-to-configure-the-streaming-idle-watc|claude-code-2026-03-26-33b65d]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: fec0aa141902baad88c3b28f18f4542d33794dfb4fd04803a9a9f0bbf25bbe6c
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-03-18-improved-non-streaming-api-fallback-with-a-2-minute-per-attempt-timeout-preventi|claude-code-2026-03-18-f2102f]]'
- '[[Changes/Cursor/2026-03-19-composer-2-is-now-available-in-cursor-frontier-level-coding-performance-with-str|cursor-2026-03-19-780a40]]'
- '[[Changes/Claude Code/2026-03-26-added-claude-stream-idle-timeout-ms-env-var-to-configure-the-streaming-idle-watc|claude-code-2026-03-26-33b65d]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-10-v2-1-101-github-307692858-ffcdf642|claude-code-2026-04-10-v2-1-101-github-307692858-ffcdf642]]'
theme: reliability-performance
type: change
---

# Improved brief mode to retry once when Claude responds with plain text instead o

<!-- chronolog:begin region="description" -->
Improved brief mode to retry once when Claude responds with plain text instead of a structured message
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Improved brief mode to retry once when Claude responds with plain text instead of a structured message
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.101
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-03-26-added-claude-stream-idle-timeout-ms-env-var-to-configure-the-streaming-idle-watc|claude-code-2026-03-26-33b65d]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: reliability-performance
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|chatgpt-2022-12-15-9c6f9c]]
- Lag Days: 1212
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes