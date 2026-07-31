---
card_id: claude-code-2026-06-24-e72d98
date: '2026-06-24'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|cursor-2023-03-30-3bf00d]]'
  lag_days: 1182
  role: follower
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-06-22-added-claude-platform-on-aws-refresh-credentials-option-to-login-when-awsauthref|claude-code-2026-06-22-886889]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 3cee68916d4ad396eb0213d3d58b09b9364549c5c83263511681ec80f32ca77d
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-06-02-added-a-prompt-before-writing-to-shell-startup-files-zshenv-zlogin-bash-login-an|claude-code-2026-06-02-8214a8]]'
- '[[Changes/Claude Code/2026-06-22-added-claude-mcp-login-name-and-claude-mcp-logout-name-to-authenticate-mcp-serve|claude-code-2026-06-22-27079a]]'
- '[[Changes/Claude Code/2026-06-22-added-claude-platform-on-aws-refresh-credentials-option-to-login-when-awsauthref|claude-code-2026-06-22-886889]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-24-v2-1-191-github-344307226-67cdfb27|claude-code-2026-06-24-v2-1-191-github-344307226-67cdfb27]]'
theme: account-access
type: change
---

# Improved MCP OAuth: discovery and token requests now retry once after transient

<!-- chronolog:begin region="description" -->
Improved MCP OAuth: discovery and token requests now retry once after transient network errors, and headless environments skip the browser popup and go straight to the paste-the-URL prompt
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Improved MCP OAuth: discovery and token requests now retry once after transient network errors, and headless environments skip the browser popup and go straight to the paste-the-URL prompt
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.191
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-06-22-added-claude-platform-on-aws-refresh-credentials-option-to-login-when-awsauthref|claude-code-2026-06-22-886889]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: account-access
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-03-30-ai-now-requires-login|cursor-2023-03-30-3bf00d]]
- Lag Days: 1182
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes