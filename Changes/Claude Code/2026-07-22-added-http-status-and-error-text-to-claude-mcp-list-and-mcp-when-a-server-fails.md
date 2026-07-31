---
card_id: claude-code-2026-07-22-770179
date: '2026-07-22'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]'
  lag_days: 1217
  role: follower
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-07-17-mcp-tool-calls-running-longer-than-2-minutes-now-move-to-the-background-automati|claude-code-2026-07-17-0b1708]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 56e32827205eb24298f48d13fa2a055d4f17f40e652e13dd1a7cb5ba1d99d444
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-07-17-mcp-tool-calls-running-longer-than-2-minutes-now-move-to-the-background-automati|claude-code-2026-07-17-0b1708]]'
- '[[Changes/Cursor/2026-07-17-cursor-in-slack-now-shares-a-plan-before-it-starts-runs-in-multi-repo-environmen|cursor-2026-07-17-39b8ba]]'
- '[[Changes/Cursor/2026-07-17-we-also-refined-how-cursor-s-responses-look-in-slack-in-message-buttons-are-gone|cursor-2026-07-17-40bd59]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-22-v2-1-218-github-358276841-57d73db4|claude-code-2026-07-22-v2-1-218-github-358276841-57d73db4]]'
theme: apps-integrations
type: change
---

# Added HTTP status and error text to `claude mcp list` and `/mcp` when a server f

<!-- chronolog:begin region="description" -->
Added HTTP status and error text to `claude mcp list` and `/mcp` when a server fails to connect, and a warning for MCP config values with hidden leading or trailing whitespace
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added HTTP status and error text to `claude mcp list` and `/mcp` when a server fails to connect, and a warning for MCP config values with hidden leading or trailing whitespace
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.218
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-07-17-mcp-tool-calls-running-longer-than-2-minutes-now-move-to-the-background-automati|claude-code-2026-07-17-0b1708]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: apps-integrations
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]
- Lag Days: 1217
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes