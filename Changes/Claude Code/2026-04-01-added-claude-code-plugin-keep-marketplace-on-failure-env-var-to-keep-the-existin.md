---
card_id: claude-code-2026-04-01-5bb86f
date: '2026-04-01'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]'
  lag_days: 1105
  role: follower
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-04-01-added-mcp-connection-nonblocking-true-for-p-mode-to-skip-the-mcp-connection-wait|claude-code-2026-04-01-210067]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 992238398c01418628114a4ddbcf094e1e6265c4265c649dc9368f933e4aba91
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/ChatGPT/2026-03-27-if-you-already-use-these-apps-in-chatgpt-reconnect-the-app-to-start-using-the-up|chatgpt-2026-03-27-5c362d]]'
- '[[Changes/Claude Code/2026-03-27-reduced-startup-event-loop-stalls-when-many-claude-ai-mcp-connectors-are-configu|claude-code-2026-03-27-dcb91e]]'
- '[[Changes/Claude Code/2026-04-01-added-mcp-connection-nonblocking-true-for-p-mode-to-skip-the-mcp-connection-wait|claude-code-2026-04-01-210067]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-01-v2-1-90-github-304453197-996aad1b|claude-code-2026-04-01-v2-1-90-github-304453197-996aad1b]]'
theme: apps-integrations
type: change
---

# Added `CLAUDE_CODE_PLUGIN_KEEP_MARKETPLACE_ON_FAILURE` env var to keep the exist

<!-- chronolog:begin region="description" -->
Added `CLAUDE_CODE_PLUGIN_KEEP_MARKETPLACE_ON_FAILURE` env var to keep the existing marketplace cache when `git pull` fails, useful in offline environments
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `CLAUDE_CODE_PLUGIN_KEEP_MARKETPLACE_ON_FAILURE` env var to keep the existing marketplace cache when `git pull` fails, useful in offline environments
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.90
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-04-01-added-mcp-connection-nonblocking-true-for-p-mode-to-skip-the-mcp-connection-wait|claude-code-2026-04-01-210067]]
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