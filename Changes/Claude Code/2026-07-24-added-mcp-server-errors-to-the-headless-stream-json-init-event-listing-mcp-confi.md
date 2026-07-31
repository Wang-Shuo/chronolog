---
card_id: claude-code-2026-07-24-b7c5f4
date: '2026-07-24'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]'
  lag_days: 1219
  role: follower
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-07-22-added-http-status-and-error-text-to-claude-mcp-list-and-mcp-when-a-server-fails|claude-code-2026-07-22-770179]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 84921bc1ab4cc7b941fc1fd16be745eb89856507922c46d578087fb897257677
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Cursor/2026-07-17-cursor-in-slack-now-shares-a-plan-before-it-starts-runs-in-multi-repo-environmen|cursor-2026-07-17-39b8ba]]'
- '[[Changes/Cursor/2026-07-17-we-also-refined-how-cursor-s-responses-look-in-slack-in-message-buttons-are-gone|cursor-2026-07-17-40bd59]]'
- '[[Changes/Claude Code/2026-07-22-added-http-status-and-error-text-to-claude-mcp-list-and-mcp-when-a-server-fails|claude-code-2026-07-22-770179]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-24-v2-1-219-github-359412713-6c14d233|claude-code-2026-07-24-v2-1-219-github-359412713-6c14d233]]'
theme: apps-integrations
type: change
---

# Added `mcp_server_errors` to the headless stream-json init event, listing `--mcp

<!-- chronolog:begin region="description" -->
Added `mcp_server_errors` to the headless stream-json init event, listing `--mcp-config` entries skipped by config validation; terminal runs print a startup warning
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `mcp_server_errors` to the headless stream-json init event, listing `--mcp-config` entries skipped by config validation; terminal runs print a startup warning
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.219
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-07-22-added-http-status-and-error-text-to-claude-mcp-list-and-mcp-when-a-server-fails|claude-code-2026-07-22-770179]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: apps-integrations
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]
- Lag Days: 1219
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes