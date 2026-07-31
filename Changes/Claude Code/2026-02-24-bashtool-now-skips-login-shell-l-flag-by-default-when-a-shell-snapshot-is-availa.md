---
card_id: claude-code-2026-02-24-30f423
date: '2026-02-24'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|cursor-2023-03-30-3bf00d]]'
  lag_days: 1062
  role: follower
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-02-19-improved-performance-by-caching-authentication-failures-for-http-and-sse-mcp-ser|claude-code-2026-02-19-e831c2]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: e32f7953336ff296d8b36f01bf73e02e609ad6ed82b5760c4e24e7e297acb6af
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-02-03-added-pre-configured-oauth-client-credentials-for-mcp-servers-that-don-t-support|claude-code-2026-02-03-1c4ec2]]'
- '[[Changes/Claude Code/2026-02-13-added-claude-auth-login-claude-auth-status-and-claude-auth-logout-cli-subcommand|claude-code-2026-02-13-19875c]]'
- '[[Changes/Claude Code/2026-02-19-improved-performance-by-caching-authentication-failures-for-http-and-sse-mcp-ser|claude-code-2026-02-19-e831c2]]'
source_release: '[[Releases/Claude Code/claude-code-2026-02-24-v2-1-51-github-289665343-b4bbdd9c|claude-code-2026-02-24-v2-1-51-github-289665343-b4bbdd9c]]'
theme: account-access
type: change
---

# BashTool now skips login shell (`-l` flag) by default when a shell snapshot is a

<!-- chronolog:begin region="description" -->
BashTool now skips login shell (`-l` flag) by default when a shell snapshot is available, improving command execution performance. Previously this required setting `CLAUDE_BASH_NO_LOGIN=true`.
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> BashTool now skips login shell (`-l` flag) by default when a shell snapshot is available, improving command execution performance. Previously this required setting `CLAUDE_BASH_NO_LOGIN=true`.
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.51
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-02-19-improved-performance-by-caching-authentication-failures-for-http-and-sse-mcp-ser|claude-code-2026-02-19-e831c2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: account-access
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-03-30-ai-now-requires-login|cursor-2023-03-30-3bf00d]]
- Lag Days: 1062
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes