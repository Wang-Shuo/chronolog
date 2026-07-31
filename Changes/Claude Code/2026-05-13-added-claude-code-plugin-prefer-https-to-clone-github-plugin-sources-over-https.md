---
card_id: claude-code-2026-05-13-e49017
date: '2026-05-13'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]'
  lag_days: 1147
  role: follower
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-05-13-added-terminalsequence-field-to-hook-json-output-so-hooks-can-emit-desktop-notif|claude-code-2026-05-13-df56c4]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 911c3a82e85e4200f80c3dd4c1dfc7dcff028d12c3ebd3d1f4f3979cac62f54c
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Cursor/2026-05-11-get-started-by-installing-the-integration-in-the-cursor-dashboard-learn-more-in|cursor-2026-05-11-df0e2b]]'
- '[[Changes/Claude Code/2026-05-12-plugins-now-warn-when-a-default-component-folder-e-g-commands-is-silently-ignore|claude-code-2026-05-12-abb705]]'
- '[[Changes/Claude Code/2026-05-13-added-terminalsequence-field-to-hook-json-output-so-hooks-can-emit-desktop-notif|claude-code-2026-05-13-df56c4]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-13-v2-1-141-github-322186176-9f8e2e22|claude-code-2026-05-13-v2-1-141-github-322186176-9f8e2e22]]'
theme: apps-integrations
type: change
---

# Added `CLAUDE_CODE_PLUGIN_PREFER_HTTPS` to clone GitHub plugin sources over HTTP

<!-- chronolog:begin region="description" -->
Added `CLAUDE_CODE_PLUGIN_PREFER_HTTPS` to clone GitHub plugin sources over HTTPS instead of SSH, for environments without a GitHub SSH key
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `CLAUDE_CODE_PLUGIN_PREFER_HTTPS` to clone GitHub plugin sources over HTTPS instead of SSH, for environments without a GitHub SSH key
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.141
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-05-13-added-terminalsequence-field-to-hook-json-output-so-hooks-can-emit-desktop-notif|claude-code-2026-05-13-df56c4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: apps-integrations
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]
- Lag Days: 1147
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes