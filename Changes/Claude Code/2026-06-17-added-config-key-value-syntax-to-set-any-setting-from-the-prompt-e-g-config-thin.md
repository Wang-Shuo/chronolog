---
card_id: claude-code-2026-06-17-32b61f
date: '2026-06-17'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]'
  lag_days: 1182
  role: follower
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-06-16-improved-plugin-loading-performance-in-remote-sessions|claude-code-2026-06-16-e5e65a]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 7f14ae80f55e15871eb8d2784916cf1fcaed5e441182d6ae18be9cb60a2c383f
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-06-15-skills-in-nested-claude-skills-directories-now-load-when-working-on-files-there|claude-code-2026-06-15-05b30a]]'
- '[[Changes/Claude Code/2026-06-16-improved-plugin-loading-performance-in-remote-sessions|claude-code-2026-06-16-e5e65a]]'
- '[[Changes/ChatGPT/2026-06-17-monitoring-tasks-can-search-the-web-and-check-connected-apps-for-changes-and-not|chatgpt-2026-06-17-8bf603]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-17-v2-1-181-github-340975229-c771c493|claude-code-2026-06-17-v2-1-181-github-340975229-c771c493]]'
theme: apps-integrations
type: change
---

# Added `/config key=value` syntax to set any setting from the prompt (e.g. `/conf

<!-- chronolog:begin region="description" -->
Added `/config key=value` syntax to set any setting from the prompt (e.g. `/config thinking=false`) — works in interactive, `-p`, and Remote Control
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `/config key=value` syntax to set any setting from the prompt (e.g. `/config thinking=false`) — works in interactive, `-p`, and Remote Control
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.181
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-06-16-improved-plugin-loading-performance-in-remote-sessions|claude-code-2026-06-16-e5e65a]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: apps-integrations
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]
- Lag Days: 1182
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes