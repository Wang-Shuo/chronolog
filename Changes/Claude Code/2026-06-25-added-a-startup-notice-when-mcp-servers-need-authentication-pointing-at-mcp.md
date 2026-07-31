---
card_id: claude-code-2026-06-25-b7eec5
date: '2026-06-25'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|cursor-2023-03-30-3bf00d]]'
  lag_days: 1183
  role: follower
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-06-24-improved-mcp-oauth-discovery-and-token-requests-now-retry-once-after-transient-n|claude-code-2026-06-24-e72d98]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 906f8c7862c28e6d100b1657e5af26b03558d7313de65a4d2ad6020d13f3aaef
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-06-22-added-claude-mcp-login-name-and-claude-mcp-logout-name-to-authenticate-mcp-serve|claude-code-2026-06-22-27079a]]'
- '[[Changes/Claude Code/2026-06-22-added-claude-platform-on-aws-refresh-credentials-option-to-login-when-awsauthref|claude-code-2026-06-22-886889]]'
- '[[Changes/Claude Code/2026-06-24-improved-mcp-oauth-discovery-and-token-requests-now-retry-once-after-transient-n|claude-code-2026-06-24-e72d98]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-25-v2-1-193-github-344922230-0655000d|claude-code-2026-06-25-v2-1-193-github-344922230-0655000d]]'
theme: account-access
type: change
---

# Added a startup notice when MCP servers need authentication, pointing at `/mcp`

<!-- chronolog:begin region="description" -->
Added a startup notice when MCP servers need authentication, pointing at `/mcp`
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added a startup notice when MCP servers need authentication, pointing at `/mcp`
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.193
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-06-24-improved-mcp-oauth-discovery-and-token-requests-now-retry-once-after-transient-n|claude-code-2026-06-24-e72d98]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: account-access
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-03-30-ai-now-requires-login|cursor-2023-03-30-3bf00d]]
- Lag Days: 1183
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes