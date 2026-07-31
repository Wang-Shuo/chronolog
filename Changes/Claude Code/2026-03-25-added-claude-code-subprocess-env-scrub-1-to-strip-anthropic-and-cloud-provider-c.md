---
card_id: claude-code-2026-03-25-502a32
date: '2026-03-25'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]'
  lag_days: 1098
  role: follower
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-03-20-improved-mcp-read-search-tool-calls-to-collapse-into-a-single-queried-server-lin|claude-code-2026-03-20-a75158]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 06a627cab9058ec5e8accf458a41bb1966cef20bcd5d3ffd740b07f6de257ea1
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-03-19-added-cli-tool-usage-detection-to-plugin-tips-in-addition-to-file-pattern-matchi|claude-code-2026-03-19-90d169]]'
- '[[Changes/Claude Code/2026-03-20-improved-mcp-read-search-tool-calls-to-collapse-into-a-single-queried-server-lin|claude-code-2026-03-20-a75158]]'
- '[[Changes/ChatGPT/2026-03-25-google-s-file-connectors-in-chatgpt-are-now-unified-under-google-drive-providing|chatgpt-2026-03-25-6c2ae6]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-25-v2-1-83-github-301019202-ba6a8317|claude-code-2026-03-25-v2-1-83-github-301019202-ba6a8317]]'
theme: apps-integrations
type: change
---

# Added `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB=1` to strip Anthropic and cloud provider

<!-- chronolog:begin region="description" -->
Added `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB=1` to strip Anthropic and cloud provider credentials from subprocess environments (Bash tool, hooks, MCP stdio servers)
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB=1` to strip Anthropic and cloud provider credentials from subprocess environments (Bash tool, hooks, MCP stdio servers)
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.83
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-03-20-improved-mcp-read-search-tool-calls-to-collapse-into-a-single-queried-server-lin|claude-code-2026-03-20-a75158]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: apps-integrations
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]
- Lag Days: 1098
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes