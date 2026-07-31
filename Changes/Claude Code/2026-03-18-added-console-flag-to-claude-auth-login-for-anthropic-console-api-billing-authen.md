---
card_id: claude-code-2026-03-18-43d796
date: '2026-03-18'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|cursor-2023-03-30-3bf00d]]'
  lag_days: 1084
  role: follower
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-03-11-added-actionable-guidance-when-oauth-login-or-connectivity-checks-fail-due-to-ss|claude-code-2026-03-11-5a9b80]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 499e613168b1ac2beb7daa1c75c48550c6d85576a413c6c9337408b30193b460
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-02-19-improved-performance-by-caching-authentication-failures-for-http-and-sse-mcp-ser|claude-code-2026-02-19-e831c2]]'
- '[[Changes/Claude Code/2026-02-24-bashtool-now-skips-login-shell-l-flag-by-default-when-a-shell-snapshot-is-availa|claude-code-2026-02-24-30f423]]'
- '[[Changes/Claude Code/2026-03-11-added-actionable-guidance-when-oauth-login-or-connectivity-checks-fail-due-to-ss|claude-code-2026-03-11-5a9b80]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-18-v2-1-79-github-298704791-2ebf4bbd|claude-code-2026-03-18-v2-1-79-github-298704791-2ebf4bbd]]'
theme: account-access
type: change
---

# Added `--console` flag to `claude auth login` for Anthropic Console (API billing

<!-- chronolog:begin region="description" -->
Added `--console` flag to `claude auth login` for Anthropic Console (API billing) authentication
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `--console` flag to `claude auth login` for Anthropic Console (API billing) authentication
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.79
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-03-11-added-actionable-guidance-when-oauth-login-or-connectivity-checks-fail-due-to-ss|claude-code-2026-03-11-5a9b80]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: account-access
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-03-30-ai-now-requires-login|cursor-2023-03-30-3bf00d]]
- Lag Days: 1084
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes