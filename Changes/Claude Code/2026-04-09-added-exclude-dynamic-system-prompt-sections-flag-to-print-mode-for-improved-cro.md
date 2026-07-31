---
card_id: claude-code-2026-04-09-ea27a8
date: '2026-04-09'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-extended-prompt-length-for-project-generation|cursor-2023-05-04-00d3b7]]'
  lag_days: 1071
  role: follower
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-03-27-reduced-token-overhead-when-mentioning-files-with-raw-string-content-no-longer-j|claude-code-2026-03-27-09cfad]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: b84084fd18855fab74d396c3d066508dc0ab92418cd37b489adc319013a43e0f
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Cursor/2026-03-19-fast-default-1-50-m-input-7-50-m-output-tokens|cursor-2026-03-19-425e73]]'
- '[[Changes/ChatGPT/2026-03-25-starting-today-for-chatgpt-plus-pro-and-business-users-long-pastes-are-handled-d|chatgpt-2026-03-25-60882a]]'
- '[[Changes/Claude Code/2026-03-27-reduced-token-overhead-when-mentioning-files-with-raw-string-content-no-longer-j|claude-code-2026-03-27-09cfad]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-09-v2-1-98-github-307232194-a0774436|claude-code-2026-04-09-v2-1-98-github-307232194-a0774436]]'
theme: context-window
type: change
---

# Added `--exclude-dynamic-system-prompt-sections` flag to print mode for improved

<!-- chronolog:begin region="description" -->
Added `--exclude-dynamic-system-prompt-sections` flag to print mode for improved cross-user prompt caching
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `--exclude-dynamic-system-prompt-sections` flag to print mode for improved cross-user prompt caching
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.98
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-03-27-reduced-token-overhead-when-mentioning-files-with-raw-string-content-no-longer-j|claude-code-2026-03-27-09cfad]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: context-window
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-05-04-extended-prompt-length-for-project-generation|cursor-2023-05-04-00d3b7]]
- Lag Days: 1071
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes