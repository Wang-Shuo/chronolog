---
card_id: claude-code-2026-04-01-210067
date: '2026-04-01'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]'
  lag_days: 1105
  role: follower
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-03-27-reduced-startup-event-loop-stalls-when-many-claude-ai-mcp-connectors-are-configu|claude-code-2026-03-27-dcb91e]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 3767827cb03f3fec119bcf55bc588e952b77a523638000fde2d9635118dcab6e
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/ChatGPT/2026-03-27-we-re-rolling-out-updated-box-notion-linear-and-dropbox-apps-in-chatgpt-these-up|chatgpt-2026-03-27-5201f1]]'
- '[[Changes/ChatGPT/2026-03-27-if-you-already-use-these-apps-in-chatgpt-reconnect-the-app-to-start-using-the-up|chatgpt-2026-03-27-5c362d]]'
- '[[Changes/Claude Code/2026-03-27-reduced-startup-event-loop-stalls-when-many-claude-ai-mcp-connectors-are-configu|claude-code-2026-03-27-dcb91e]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-01-v2-1-89-github-303967782-358023f0|claude-code-2026-04-01-v2-1-89-github-303967782-358023f0]]'
theme: apps-integrations
type: change
---

# Added `MCP_CONNECTION_NONBLOCKING=true` for `-p` mode to skip the MCP connection

<!-- chronolog:begin region="description" -->
Added `MCP_CONNECTION_NONBLOCKING=true` for `-p` mode to skip the MCP connection wait entirely, and bounded `--mcp-config` server connections at 5s instead of blocking on the slowest server
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `MCP_CONNECTION_NONBLOCKING=true` for `-p` mode to skip the MCP connection wait entirely, and bounded `--mcp-config` server connections at 5s instead of blocking on the slowest server
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.89
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-03-27-reduced-startup-event-loop-stalls-when-many-claude-ai-mcp-connectors-are-configu|claude-code-2026-03-27-dcb91e]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: apps-integrations
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]
- Lag Days: 1105
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes