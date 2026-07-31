---
card_id: claude-code-2026-05-04-da7dd3
date: '2026-05-04'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|cursor-2023-03-30-3bf00d]]'
  lag_days: 1131
  role: follower
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-05-01-claude-auth-login-now-accepts-the-oauth-code-pasted-into-the-terminal-when-the-b|claude-code-2026-05-01-a5bb2e]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: dafc2bc69c5b2c19c88269a92a59d3dac5f33fef49b6351f494825d54af49e4e
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-04-28-clarified-the-mcp-message-shown-when-an-mcp-server-is-still-unauthorized-after-t|claude-code-2026-04-28-77f3f4]]'
- '[[Changes/ChatGPT/2026-04-30-we-re-rolling-out-advanced-account-security-an-optional-setting-for-personal-cha|chatgpt-2026-04-30-139382]]'
- '[[Changes/Claude Code/2026-05-01-claude-auth-login-now-accepts-the-oauth-code-pasted-into-the-terminal-when-the-b|claude-code-2026-05-01-a5bb2e]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-04-v2-1-128-github-317391175-a20e13a2|claude-code-2026-05-04-v2-1-128-github-317391175-a20e13a2]]'
theme: account-access
type: change
---

# `--channels` now works with console (API key) authentication — console orgs with

<!-- chronolog:begin region="description" -->
`--channels` now works with console (API key) authentication — console orgs with managed settings must set `channelsEnabled: true` to enable
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> `--channels` now works with console (API key) authentication — console orgs with managed settings must set `channelsEnabled: true` to enable
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.128
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-05-01-claude-auth-login-now-accepts-the-oauth-code-pasted-into-the-terminal-when-the-b|claude-code-2026-05-01-a5bb2e]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: account-access
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-03-30-ai-now-requires-login|cursor-2023-03-30-3bf00d]]
- Lag Days: 1131
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes