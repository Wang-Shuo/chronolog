---
card_id: claude-code-2026-04-13-cf1492
date: '2026-04-13'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]'
  lag_days: 1117
  role: follower
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-04-13-added-background-monitor-support-for-plugins-via-a-top-level-monitors-manifest-k|claude-code-2026-04-13-8f75bf]]'
extractor_version: fallback-v2
impact: significant
machine_hash: 327185ca8277e532479c7933ca5038e7b50f512792e6d9a052155ec7ed72c190
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Cursor/2026-04-08-it-looks-at-reactions-and-replies-to-bugbot-comments-and-comments-from-human-rev|cursor-2026-04-08-6f2fda]]'
- '[[Changes/Cursor/2026-04-08-this-release-introduces-updates-to-bugbot-including-the-ability-to-self-improve|cursor-2026-04-08-f29812]]'
- '[[Changes/Claude Code/2026-04-13-added-background-monitor-support-for-plugins-via-a-top-level-monitors-manifest-k|claude-code-2026-04-13-8f75bf]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-13-v2-1-105-github-308569432-65a12cd3|claude-code-2026-04-13-v2-1-105-github-308569432-65a12cd3]]'
theme: apps-integrations
type: change
---

# Added PreCompact hook support: hooks can now block compaction by exiting with co

<!-- chronolog:begin region="description" -->
Added PreCompact hook support: hooks can now block compaction by exiting with code 2 or returning `{"decision":"block"}`
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added PreCompact hook support: hooks can now block compaction by exiting with code 2 or returning `{"decision":"block"}`
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.105
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-04-13-added-background-monitor-support-for-plugins-via-a-top-level-monitors-manifest-k|claude-code-2026-04-13-8f75bf]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: apps-integrations
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]
- Lag Days: 1117
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes