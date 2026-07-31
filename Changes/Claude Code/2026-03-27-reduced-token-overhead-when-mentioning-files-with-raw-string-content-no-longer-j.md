---
card_id: claude-code-2026-03-27-09cfad
date: '2026-03-27'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-extended-prompt-length-for-project-generation|cursor-2023-05-04-00d3b7]]'
  lag_days: 1058
  role: follower
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-03-14-added-postcompact-hook-that-fires-after-compaction-completes|claude-code-2026-03-14-603f55]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: aae68e637962bbc9d829be01f739be0629bf9b1414cd046743b69a8a50d8268a
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Cursor/2026-03-19-standard-0-50-m-input-2-50-m-output-tokens|cursor-2026-03-19-2ef7b6]]'
- '[[Changes/Cursor/2026-03-19-fast-default-1-50-m-input-7-50-m-output-tokens|cursor-2026-03-19-425e73]]'
- '[[Changes/ChatGPT/2026-03-25-starting-today-for-chatgpt-plus-pro-and-business-users-long-pastes-are-handled-d|chatgpt-2026-03-25-60882a]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-27-v2-1-86-github-302569462-d6b30859|claude-code-2026-03-27-v2-1-86-github-302569462-d6b30859]]'
theme: context-window
type: change
---

# Reduced token overhead when mentioning files with `@` — raw string content no lo

<!-- chronolog:begin region="description" -->
Reduced token overhead when mentioning files with `@` — raw string content no longer JSON-escaped
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Reduced token overhead when mentioning files with `@` — raw string content no longer JSON-escaped
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.86
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-03-14-added-postcompact-hook-that-fires-after-compaction-completes|claude-code-2026-03-14-603f55]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: context-window
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-05-04-extended-prompt-length-for-project-generation|cursor-2023-05-04-00d3b7]]
- Lag Days: 1058
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes