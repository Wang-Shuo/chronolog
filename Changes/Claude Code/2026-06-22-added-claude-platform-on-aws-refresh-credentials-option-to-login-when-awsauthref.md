---
card_id: claude-code-2026-06-22-886889
date: '2026-06-22'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|cursor-2023-03-30-3bf00d]]'
  lag_days: 1180
  role: follower
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-06-22-added-claude-mcp-login-name-and-claude-mcp-logout-name-to-authenticate-mcp-serve|claude-code-2026-06-22-27079a]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: c9d866e8c533bc9893ab09c2a504c3860cabf7cb533658e33c6e5df0a9c9cc56
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/ChatGPT/2026-06-02-log-out-of-individual-sessions-or-all-sessions-from-active-sessions|chatgpt-2026-06-02-a6ea70]]'
- '[[Changes/Claude Code/2026-06-02-added-a-prompt-before-writing-to-shell-startup-files-zshenv-zlogin-bash-login-an|claude-code-2026-06-02-8214a8]]'
- '[[Changes/Claude Code/2026-06-22-added-claude-mcp-login-name-and-claude-mcp-logout-name-to-authenticate-mcp-serve|claude-code-2026-06-22-27079a]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-22-v2-1-186-github-343079393-93ecc37b|claude-code-2026-06-22-v2-1-186-github-343079393-93ecc37b]]'
theme: account-access
type: change
---

# Added "Claude Platform on AWS - refresh credentials" option to `/login` when `aw

<!-- chronolog:begin region="description" -->
Added "Claude Platform on AWS - refresh credentials" option to `/login` when `awsAuthRefresh` is configured
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added "Claude Platform on AWS - refresh credentials" option to `/login` when `awsAuthRefresh` is configured
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.186
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-06-22-added-claude-mcp-login-name-and-claude-mcp-logout-name-to-authenticate-mcp-serve|claude-code-2026-06-22-27079a]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: account-access
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-03-30-ai-now-requires-login|cursor-2023-03-30-3bf00d]]
- Lag Days: 1180
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes