---
card_id: claude-code-2026-05-01-a5bb2e
date: '2026-05-01'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|cursor-2023-03-30-3bf00d]]'
  lag_days: 1128
  role: follower
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-04-28-clarified-the-mcp-message-shown-when-an-mcp-server-is-still-unauthorized-after-t|claude-code-2026-04-28-77f3f4]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 281df5618344b51a6477cba426600f58598f5668414658f44961211c6f3ff438
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/ChatGPT/2026-04-22-we-re-launching-chatgpt-for-clinicians-a-free-version-of-chatgpt-for-verified-cl|chatgpt-2026-04-22-432031]]'
- '[[Changes/Claude Code/2026-04-28-clarified-the-mcp-message-shown-when-an-mcp-server-is-still-unauthorized-after-t|claude-code-2026-04-28-77f3f4]]'
- '[[Changes/ChatGPT/2026-04-30-we-re-rolling-out-advanced-account-security-an-optional-setting-for-personal-cha|chatgpt-2026-04-30-139382]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-01-v2-1-126-github-316244540-de18d9bb|claude-code-2026-05-01-v2-1-126-github-316244540-de18d9bb]]'
theme: account-access
type: change
---

# `claude auth login` now accepts the OAuth code pasted into the terminal when the

<!-- chronolog:begin region="description" -->
`claude auth login` now accepts the OAuth code pasted into the terminal when the browser callback can't reach localhost (WSL2, SSH, containers)
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> `claude auth login` now accepts the OAuth code pasted into the terminal when the browser callback can't reach localhost (WSL2, SSH, containers)
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.126
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-04-28-clarified-the-mcp-message-shown-when-an-mcp-server-is-still-unauthorized-after-t|claude-code-2026-04-28-77f3f4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: account-access
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-03-30-ai-now-requires-login|cursor-2023-03-30-3bf00d]]
- Lag Days: 1128
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes