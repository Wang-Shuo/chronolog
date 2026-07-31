---
card_id: claude-code-2026-06-24-4529fd
date: '2026-06-24'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]'
  lag_days: 1189
  role: follower
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-06-24-improved-mcp-error-messages-http-404-errors-now-show-the-url-and-point-to-your-m|claude-code-2026-06-24-19fdcd]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 3057211f5f24cea2f83665a70847e63c28b46f95c5d71805e909a16c57747fee
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Cursor/2026-06-22-plugins-skills-and-mcps-let-you-customize-cursor-for-your-workflows-the-new-cust|cursor-2026-06-22-f6fbff]]'
- '[[Changes/Claude Code/2026-06-23-improved-install-github-app-github-actions-workflow-setup-is-now-optional-you-ca|claude-code-2026-06-23-d8051b]]'
- '[[Changes/Claude Code/2026-06-24-improved-mcp-error-messages-http-404-errors-now-show-the-url-and-point-to-your-m|claude-code-2026-06-24-19fdcd]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-24-v2-1-191-github-344307226-67cdfb27|claude-code-2026-06-24-v2-1-191-github-344307226-67cdfb27]]'
theme: apps-integrations
type: change
---

# Improved MCP server reliability: capability discovery (`tools/list`, `prompts/li

<!-- chronolog:begin region="description" -->
Improved MCP server reliability: capability discovery (`tools/list`, `prompts/list`, `resources/list`) now retries transient network errors with short backoff
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Improved MCP server reliability: capability discovery (`tools/list`, `prompts/list`, `resources/list`) now retries transient network errors with short backoff
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.191
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-06-24-improved-mcp-error-messages-http-404-errors-now-show-the-url-and-point-to-your-m|claude-code-2026-06-24-19fdcd]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: apps-integrations
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]
- Lag Days: 1189
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes