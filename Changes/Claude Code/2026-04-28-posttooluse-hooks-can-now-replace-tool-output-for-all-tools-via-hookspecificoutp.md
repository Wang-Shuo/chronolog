---
card_id: claude-code-2026-04-28-cd9249
date: '2026-04-28'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]'
  lag_days: 1132
  role: follower
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-04-28-added-alwaysload-option-to-mcp-server-config-when-true-all-tools-from-that-serve|claude-code-2026-04-28-c60884]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 53680794a2b64ec5fc21cfeadcf7b6c147dc66fd777b52ebad02035722e4dbd7
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-04-28-added-anthropic-bedrock-service-tier-environment-variable-to-select-a-bedrock-se|claude-code-2026-04-28-4ff006]]'
- '[[Changes/Claude Code/2026-04-28-mcp-now-shows-claude-ai-connectors-hidden-by-a-manually-added-server-with-the-sa|claude-code-2026-04-28-ae0713]]'
- '[[Changes/Claude Code/2026-04-28-added-alwaysload-option-to-mcp-server-config-when-true-all-tools-from-that-serve|claude-code-2026-04-28-c60884]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-28-v2-1-121-github-314262096-ff31d5ce|claude-code-2026-04-28-v2-1-121-github-314262096-ff31d5ce]]'
theme: apps-integrations
type: change
---

# PostToolUse hooks can now replace tool output for all tools via `hookSpecificOut

<!-- chronolog:begin region="description" -->
PostToolUse hooks can now replace tool output for all tools via `hookSpecificOutput.updatedToolOutput` (previously MCP-only)
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> PostToolUse hooks can now replace tool output for all tools via `hookSpecificOutput.updatedToolOutput` (previously MCP-only)
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.121
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-04-28-added-alwaysload-option-to-mcp-server-config-when-true-all-tools-from-that-serve|claude-code-2026-04-28-c60884]]
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