---
card_id: claude-code-2026-01-09-b218b1
date: '2026-01-09'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]'
  lag_days: 1023
  role: follower
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2025-12-19-added-search-filtering-to-the-plugin-discover-screen-type-to-filter-by-name-desc|claude-code-2025-12-19-f245b1]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 4873f7e7542ba043c0b4ed360bdb4e000196f95ce2d8cd685f485f58a541b324
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Cursor/2025-12-22-cursor-now-separates-processes-running-for-user-installed-extensions-and-built-i|cursor-2025-12-22-cfd447]]'
- '[[Changes/Cursor/2026-01-08-rules-generation-and-management|cursor-2026-01-08-830639]]'
- '[[Changes/Cursor/2026-01-08-this-release-introduces-new-cli-controls-for-models-mcp-management-rules-and-com|cursor-2026-01-08-cc6cf4]]'
source_release: '[[Releases/Claude Code/claude-code-2026-01-09-v2-1-2-github-275344737-27089666|claude-code-2026-01-09-v2-1-2-github-275344737-27089666]]'
theme: apps-integrations
type: change
---

# Added `FORCE_AUTOUPDATE_PLUGINS` environment variable to allow plugin autoupdate

<!-- chronolog:begin region="description" -->
Added `FORCE_AUTOUPDATE_PLUGINS` environment variable to allow plugin autoupdate even when the main auto-updater is disabled
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `FORCE_AUTOUPDATE_PLUGINS` environment variable to allow plugin autoupdate even when the main auto-updater is disabled
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.2
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2025-12-19-added-search-filtering-to-the-plugin-discover-screen-type-to-filter-by-name-desc|claude-code-2025-12-19-f245b1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: apps-integrations
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]
- Lag Days: 1023
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes