---
card_id: claude-code-2026-04-13-8f75bf
date: '2026-04-13'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]'
  lag_days: 1117
  role: follower
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-04-07-added-keep-coding-instructions-frontmatter-field-support-for-plugin-output-style|claude-code-2026-04-07-f07863]]'
extractor_version: fallback-v2
impact: significant
machine_hash: aad3976eaced5dd3bb541f5847118f78e3b1965e836fb54c3f3c5c35cedeb059
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Cursor/2026-04-08-bugbot-learned-rules|cursor-2026-04-08-597df7]]'
- '[[Changes/Cursor/2026-04-08-it-looks-at-reactions-and-replies-to-bugbot-comments-and-comments-from-human-rev|cursor-2026-04-08-6f2fda]]'
- '[[Changes/Cursor/2026-04-08-this-release-introduces-updates-to-bugbot-including-the-ability-to-self-improve|cursor-2026-04-08-f29812]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-13-v2-1-105-github-308569432-65a12cd3|claude-code-2026-04-13-v2-1-105-github-308569432-65a12cd3]]'
theme: apps-integrations
type: change
---

# Added background monitor support for plugins via a top-level `monitors` manifest

<!-- chronolog:begin region="description" -->
Added background monitor support for plugins via a top-level `monitors` manifest key that auto-arms at session start or on skill invoke
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added background monitor support for plugins via a top-level `monitors` manifest key that auto-arms at session start or on skill invoke
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.105
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-04-07-added-keep-coding-instructions-frontmatter-field-support-for-plugin-output-style|claude-code-2026-04-07-f07863]]
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