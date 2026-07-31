---
card_id: claude-code-2026-02-19-4f3f6a
date: '2026-02-19'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|chatgpt-2022-12-15-9c6f9c]]'
  lag_days: 1162
  role: follower
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-02-18-improved-memory-usage-in-long-running-sessions-by-releasing-api-stream-buffers-a|claude-code-2026-02-18-a65c80]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: f921c49a9aefa0c37bd27a44297bb6136e37446f333bd533b304bd509bb28f71
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-02-18-improved-startup-performance-by-deferring-sessionstart-hook-execution-reducing-t|claude-code-2026-02-18-91c0ec]]'
- '[[Changes/Claude Code/2026-02-18-improved-performance-of-file-mentions-file-suggestions-now-appear-faster-by-pre|claude-code-2026-02-18-9dd752]]'
- '[[Changes/Claude Code/2026-02-18-improved-memory-usage-in-long-running-sessions-by-releasing-api-stream-buffers-a|claude-code-2026-02-18-a65c80]]'
source_release: '[[Releases/Claude Code/claude-code-2026-02-19-v2-1-49-github-288498923-7c27a140|claude-code-2026-02-19-v2-1-49-github-288498923-7c27a140]]'
theme: reliability-performance
type: change
---

# Improved performance in non-interactive mode (`-p`) by skipping unnecessary API

<!-- chronolog:begin region="description" -->
Improved performance in non-interactive mode (`-p`) by skipping unnecessary API calls during startup
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Improved performance in non-interactive mode (`-p`) by skipping unnecessary API calls during startup
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.49
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-02-18-improved-memory-usage-in-long-running-sessions-by-releasing-api-stream-buffers-a|claude-code-2026-02-18-a65c80]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: reliability-performance
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|chatgpt-2022-12-15-9c6f9c]]
- Lag Days: 1162
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes