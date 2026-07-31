---
card_id: claude-code-2026-02-03-1c4ec2
date: '2026-02-03'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|cursor-2023-03-30-3bf00d]]'
  lag_days: 1041
  role: follower
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-01-22-vscode-added-ability-for-oauth-users-to-browse-and-resume-remote-claude-sessions|claude-code-2026-01-22-5b6a2e]]'
extractor_version: fallback-v2
impact: significant
machine_hash: 177248a8ee6945266aebf555fa55aa7429a6bbefa224a1cda05208d32b6b0c81
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Cursor/2023-09-01-you-should-now-be-able-to-sign-in-with-github-again|cursor-2023-09-01-272a25]]'
- '[[Changes/ChatGPT/2024-04-01-we-re-making-it-easier-for-people-to-experience-the-benefits-of-ai-without-needi|chatgpt-2024-04-01-9d75a2]]'
- '[[Changes/Claude Code/2026-01-22-vscode-added-ability-for-oauth-users-to-browse-and-resume-remote-claude-sessions|claude-code-2026-01-22-5b6a2e]]'
source_release: '[[Releases/Claude Code/claude-code-2026-02-03-v2-1-30-github-282673902-7b2e46f2|claude-code-2026-02-03-v2-1-30-github-282673902-7b2e46f2]]'
theme: account-access
type: change
---

# Added pre-configured OAuth client credentials for MCP servers that don't support

<!-- chronolog:begin region="description" -->
Added pre-configured OAuth client credentials for MCP servers that don't support Dynamic Client Registration (e.g., Slack). Use `--client-id` and `--client-secret` with `claude mcp add`.
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added pre-configured OAuth client credentials for MCP servers that don't support Dynamic Client Registration (e.g., Slack). Use `--client-id` and `--client-secret` with `claude mcp add`.
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.30
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-01-22-vscode-added-ability-for-oauth-users-to-browse-and-resume-remote-claude-sessions|claude-code-2026-01-22-5b6a2e]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: account-access
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-03-30-ai-now-requires-login|cursor-2023-03-30-3bf00d]]
- Lag Days: 1041
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes