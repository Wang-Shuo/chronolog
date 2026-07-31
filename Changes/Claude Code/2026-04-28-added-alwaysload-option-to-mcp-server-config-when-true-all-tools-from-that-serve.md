---
card_id: claude-code-2026-04-28-c60884
date: '2026-04-28'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]'
  lag_days: 1132
  role: follower
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-04-28-mcp-now-shows-claude-ai-connectors-hidden-by-a-manually-added-server-with-the-sa|claude-code-2026-04-28-ae0713]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 0e94502a68ba19e3b91092dba9ab0aaa4d49495890536ae788c3c0e119669068
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-04-28-added-claude-plugin-prune-to-remove-orphaned-auto-installed-plugin-dependencies|claude-code-2026-04-28-1fc875]]'
- '[[Changes/Claude Code/2026-04-28-added-anthropic-bedrock-service-tier-environment-variable-to-select-a-bedrock-se|claude-code-2026-04-28-4ff006]]'
- '[[Changes/Claude Code/2026-04-28-mcp-now-shows-claude-ai-connectors-hidden-by-a-manually-added-server-with-the-sa|claude-code-2026-04-28-ae0713]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-28-v2-1-121-github-314262096-ff31d5ce|claude-code-2026-04-28-v2-1-121-github-314262096-ff31d5ce]]'
theme: apps-integrations
type: change
---

# Added `alwaysLoad` option to MCP server config — when `true`, all tools from tha

<!-- chronolog:begin region="description" -->
Added `alwaysLoad` option to MCP server config — when `true`, all tools from that server skip tool-search deferral and are always available
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `alwaysLoad` option to MCP server config — when `true`, all tools from that server skip tool-search deferral and are always available
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.121
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-04-28-mcp-now-shows-claude-ai-connectors-hidden-by-a-manually-added-server-with-the-sa|claude-code-2026-04-28-ae0713]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: apps-integrations
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]
- Lag Days: 1132
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes