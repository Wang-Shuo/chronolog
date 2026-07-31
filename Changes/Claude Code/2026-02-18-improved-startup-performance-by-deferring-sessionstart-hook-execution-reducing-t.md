---
card_id: claude-code-2026-02-18-91c0ec
date: '2026-02-18'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|chatgpt-2022-12-15-9c6f9c]]'
  lag_days: 1161
  role: follower
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-02-18-improved-memory-usage-by-trimming-agent-task-message-history-after-tasks-complet|claude-code-2026-02-18-7be345]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 6ea416a72d65ab5d2e7173947340c587d4c3e54582bf2f46bfc240873fcf950a
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-01-14-improved-typing-responsiveness-by-reducing-memory-allocation-overhead-in-termina|claude-code-2026-01-14-59caaf]]'
- '[[Changes/Claude Code/2026-01-21-improved-ui-rendering-performance-with-react-compiler|claude-code-2026-01-21-5000b9]]'
- '[[Changes/Claude Code/2026-02-18-improved-memory-usage-by-trimming-agent-task-message-history-after-tasks-complet|claude-code-2026-02-18-7be345]]'
source_release: '[[Releases/Claude Code/claude-code-2026-02-18-v2-1-47-github-287886320-98b6e931|claude-code-2026-02-18-v2-1-47-github-287886320-98b6e931]]'
theme: reliability-performance
type: change
---

# Improved startup performance by deferring SessionStart hook execution, reducing

<!-- chronolog:begin region="description" -->
Improved startup performance by deferring SessionStart hook execution, reducing time-to-interactive by ~500ms.
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Improved startup performance by deferring SessionStart hook execution, reducing time-to-interactive by ~500ms.
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.47
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-02-18-improved-memory-usage-by-trimming-agent-task-message-history-after-tasks-complet|claude-code-2026-02-18-7be345]]
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