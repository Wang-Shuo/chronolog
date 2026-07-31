---
card_id: claude-code-2026-02-19-e831c2
date: '2026-02-19'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|cursor-2023-03-30-3bf00d]]'
  lag_days: 1057
  role: follower
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-02-13-added-claude-auth-login-claude-auth-status-and-claude-auth-logout-cli-subcommand|claude-code-2026-02-13-19875c]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: ae82d74c43482a68a35b7b9ec4f5ab97c5b81245af1cefc4ac776657ca44c9dd
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-01-22-vscode-added-ability-for-oauth-users-to-browse-and-resume-remote-claude-sessions|claude-code-2026-01-22-5b6a2e]]'
- '[[Changes/Claude Code/2026-02-03-added-pre-configured-oauth-client-credentials-for-mcp-servers-that-don-t-support|claude-code-2026-02-03-1c4ec2]]'
- '[[Changes/Claude Code/2026-02-13-added-claude-auth-login-claude-auth-status-and-claude-auth-logout-cli-subcommand|claude-code-2026-02-13-19875c]]'
source_release: '[[Releases/Claude Code/claude-code-2026-02-19-v2-1-49-github-288498923-7c27a140|claude-code-2026-02-19-v2-1-49-github-288498923-7c27a140]]'
theme: account-access
type: change
---

# Improved performance by caching authentication failures for HTTP and SSE MCP ser

<!-- chronolog:begin region="description" -->
Improved performance by caching authentication failures for HTTP and SSE MCP servers, avoiding repeated connection attempts to servers requiring auth
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Improved performance by caching authentication failures for HTTP and SSE MCP servers, avoiding repeated connection attempts to servers requiring auth
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.49
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-02-13-added-claude-auth-login-claude-auth-status-and-claude-auth-logout-cli-subcommand|claude-code-2026-02-13-19875c]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: account-access
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-03-30-ai-now-requires-login|cursor-2023-03-30-3bf00d]]
- Lag Days: 1057
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes