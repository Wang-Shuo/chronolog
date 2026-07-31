---
card_id: claude-code-2026-07-17-ec921c
date: '2026-07-17'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-browsing-an-experimental-model-that-knows-when-and-how-to-browse-the-internet|chatgpt-2023-03-23-c03c55]]'
  lag_days: 1212
  role: follower
  scope: tracked-products-only
  theme: search-browsing
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-05-19-the-plugin-browse-and-discover-panes-now-show-when-a-plugin-was-last-updated|claude-code-2026-05-19-077873]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 477e5e2c88eb416c8d5cef38292222900e61de736700f3b33457645f5ee2cbc9
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/ChatGPT/2026-04-08-the-outlook-email-and-calendar-apps-for-chatgpt-can-now-help-with-delegated-or-s|chatgpt-2026-04-08-733761]]'
- '[[Changes/Claude Code/2026-05-19-the-plugin-browse-and-discover-panes-now-show-when-a-plugin-was-last-updated|claude-code-2026-05-19-077873]]'
- '[[Changes/ChatGPT/2026-06-01-chatgpt-can-now-help-with-more-of-the-job-search-process-from-finding-relevant-l|chatgpt-2026-06-01-d9a25a]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-17-v2-1-212-github-355310036-d94b4e11|claude-code-2026-07-17-v2-1-212-github-355310036-d94b4e11]]'
theme: search-browsing
type: change
---

# Added a session-wide limit on WebSearch tool calls (default 200, tunable via `CL

<!-- chronolog:begin region="description" -->
Added a session-wide limit on WebSearch tool calls (default 200, tunable via `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION`) to stop runaway search loops
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added a session-wide limit on WebSearch tool calls (default 200, tunable via `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION`) to stop runaway search loops
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.212
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-05-19-the-plugin-browse-and-discover-panes-now-show-when-a-plugin-was-last-updated|claude-code-2026-05-19-077873]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: search-browsing
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-03-23-browsing-an-experimental-model-that-knows-when-and-how-to-browse-the-internet|chatgpt-2023-03-23-c03c55]]
- Lag Days: 1212
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes