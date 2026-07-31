---
card_id: claude-code-2026-02-18-9dd752
date: '2026-02-18'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|chatgpt-2022-12-15-9c6f9c]]'
  lag_days: 1161
  role: follower
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-02-18-improved-startup-performance-by-deferring-sessionstart-hook-execution-reducing-t|claude-code-2026-02-18-91c0ec]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 4efb46ea41d8f4cf888b15863ace3bbb29687cd80e3b39104ea37bc6c6305d54
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-01-21-improved-ui-rendering-performance-with-react-compiler|claude-code-2026-01-21-5000b9]]'
- '[[Changes/Claude Code/2026-02-18-improved-memory-usage-by-trimming-agent-task-message-history-after-tasks-complet|claude-code-2026-02-18-7be345]]'
- '[[Changes/Claude Code/2026-02-18-improved-startup-performance-by-deferring-sessionstart-hook-execution-reducing-t|claude-code-2026-02-18-91c0ec]]'
source_release: '[[Releases/Claude Code/claude-code-2026-02-18-v2-1-47-github-287886320-98b6e931|claude-code-2026-02-18-v2-1-47-github-287886320-98b6e931]]'
theme: reliability-performance
type: change
---

# Improved performance of `@` file mentions - file suggestions now appear faster b

<!-- chronolog:begin region="description" -->
Improved performance of `@` file mentions - file suggestions now appear faster by pre-warming the index on startup and using session-based caching with background refresh.
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Improved performance of `@` file mentions - file suggestions now appear faster by pre-warming the index on startup and using session-based caching with background refresh.
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.47
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-02-18-improved-startup-performance-by-deferring-sessionstart-hook-execution-reducing-t|claude-code-2026-02-18-91c0ec]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: reliability-performance
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|chatgpt-2022-12-15-9c6f9c]]
- Lag Days: 1161
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes