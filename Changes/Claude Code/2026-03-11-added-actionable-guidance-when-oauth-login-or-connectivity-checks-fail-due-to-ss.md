---
card_id: claude-code-2026-03-11-5a9b80
date: '2026-03-11'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|cursor-2023-03-30-3bf00d]]'
  lag_days: 1077
  role: follower
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-02-24-bashtool-now-skips-login-shell-l-flag-by-default-when-a-shell-snapshot-is-availa|claude-code-2026-02-24-30f423]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: a222af6889fab11ed0250992cbc735d8932dff9af925c2fbc185d4ae09c0d50c
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-02-13-added-claude-auth-login-claude-auth-status-and-claude-auth-logout-cli-subcommand|claude-code-2026-02-13-19875c]]'
- '[[Changes/Claude Code/2026-02-19-improved-performance-by-caching-authentication-failures-for-http-and-sse-mcp-ser|claude-code-2026-02-19-e831c2]]'
- '[[Changes/Claude Code/2026-02-24-bashtool-now-skips-login-shell-l-flag-by-default-when-a-shell-snapshot-is-availa|claude-code-2026-02-24-30f423]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-11-v2-1-73-github-295814700-0abb054f|claude-code-2026-03-11-v2-1-73-github-295814700-0abb054f]]'
theme: account-access
type: change
---

# Added actionable guidance when OAuth login or connectivity checks fail due to SS

<!-- chronolog:begin region="description" -->
Added actionable guidance when OAuth login or connectivity checks fail due to SSL certificate errors (corporate proxies, `NODE_EXTRA_CA_CERTS`)
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added actionable guidance when OAuth login or connectivity checks fail due to SSL certificate errors (corporate proxies, `NODE_EXTRA_CA_CERTS`)
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.73
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-02-24-bashtool-now-skips-login-shell-l-flag-by-default-when-a-shell-snapshot-is-availa|claude-code-2026-02-24-30f423]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: account-access
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-03-30-ai-now-requires-login|cursor-2023-03-30-3bf00d]]
- Lag Days: 1077
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes