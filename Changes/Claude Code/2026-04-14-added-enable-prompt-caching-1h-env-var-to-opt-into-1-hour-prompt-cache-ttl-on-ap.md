---
card_id: claude-code-2026-04-14-4bb7a3
date: '2026-04-14'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-extended-prompt-length-for-project-generation|cursor-2023-05-04-00d3b7]]'
  lag_days: 1076
  role: follower
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-04-09-added-exclude-dynamic-system-prompt-sections-flag-to-print-mode-for-improved-cro|claude-code-2026-04-09-ea27a8]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 0d2f67bf97c36ffd40bed75c5e9ca760a5ebca51d6b1a11859ed4c695465aefb
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/ChatGPT/2026-03-25-starting-today-for-chatgpt-plus-pro-and-business-users-long-pastes-are-handled-d|chatgpt-2026-03-25-60882a]]'
- '[[Changes/Claude Code/2026-03-27-reduced-token-overhead-when-mentioning-files-with-raw-string-content-no-longer-j|claude-code-2026-03-27-09cfad]]'
- '[[Changes/Claude Code/2026-04-09-added-exclude-dynamic-system-prompt-sections-flag-to-print-mode-for-improved-cro|claude-code-2026-04-09-ea27a8]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-14-v2-1-108-github-309009167-35123bd5|claude-code-2026-04-14-v2-1-108-github-309009167-35123bd5]]'
theme: context-window
type: change
---

# Added `ENABLE_PROMPT_CACHING_1H` env var to opt into 1-hour prompt cache TTL on

<!-- chronolog:begin region="description" -->
Added `ENABLE_PROMPT_CACHING_1H` env var to opt into 1-hour prompt cache TTL on API key, Bedrock, Vertex, and Foundry (`ENABLE_PROMPT_CACHING_1H_BEDROCK` is deprecated but still honored), and `FORCE_PROMPT_CACHING_5M` to force 5-minute TTL
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `ENABLE_PROMPT_CACHING_1H` env var to opt into 1-hour prompt cache TTL on API key, Bedrock, Vertex, and Foundry (`ENABLE_PROMPT_CACHING_1H_BEDROCK` is deprecated but still honored), and `FORCE_PROMPT_CACHING_5M` to force 5-minute TTL
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.108
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-04-09-added-exclude-dynamic-system-prompt-sections-flag-to-print-mode-for-improved-cro|claude-code-2026-04-09-ea27a8]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: context-window
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-05-04-extended-prompt-length-for-project-generation|cursor-2023-05-04-00d3b7]]
- Lag Days: 1076
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes