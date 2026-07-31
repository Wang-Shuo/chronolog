---
card_id: claude-code-2026-06-03-cc3caf
date: '2026-06-03'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  lag_days: 1144
  role: follower
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-05-22-fixed-a-powershell-permission-bypass-built-in-cd-functions-cd-cd-cd-x-changed-th|claude-code-2026-05-22-e2e039]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: ff4dc2ddd08fa570a142695745dbf18375f9c43b69360f37c833a95f3bb979c1
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Cursor/2026-05-29-auto-review-applies-to-shell-mcp-and-fetch-tool-calls-allowlisted-calls-run-imme|cursor-2026-05-29-e786d9]]'
- '[[Changes/ChatGPT/2026-06-02-review-first-party-openai-sessions-from-settings-security-active-sessions-with-a|chatgpt-2026-06-02-61d936]]'
- '[[Changes/ChatGPT/2026-06-02-we-re-rolling-out-active-sessions-a-new-security-feature-in-chatgpt-that-helps-u|chatgpt-2026-06-02-afa8b4]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-03-v2-1-162-github-333906405-cdc7c67c|claude-code-2026-06-03-v2-1-162-github-333906405-cdc7c67c]]'
theme: safety-privacy
type: change
---

# `claude agents --json` now includes `waitingFor` showing what a waiting session

<!-- chronolog:begin region="description" -->
`claude agents --json` now includes `waitingFor` showing what a waiting session is blocked on (e.g. permission prompt)
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> `claude agents --json` now includes `waitingFor` showing what a waiting session is blocked on (e.g. permission prompt)
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.162
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-05-22-fixed-a-powershell-permission-bypass-built-in-cd-functions-cd-cd-cd-x-changed-th|claude-code-2026-05-22-e2e039]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: safety-privacy
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]
- Lag Days: 1144
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes