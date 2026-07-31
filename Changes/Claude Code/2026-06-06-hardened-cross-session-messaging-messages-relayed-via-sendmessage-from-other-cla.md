---
card_id: claude-code-2026-06-06-931934
date: '2026-06-06'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  lag_days: 1147
  role: follower
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-06-03-claude-agents-json-now-includes-waitingfor-showing-what-a-waiting-session-is-blo|claude-code-2026-06-03-cc3caf]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 309dc2a8297aec76d97af74aa72b044dd5e5049fb5662bf936470c25f6d56353
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Cursor/2026-06-03-enterprise-customers-can-now-manage-multiple-cursor-teams-from-one-place-with-di|cursor-2026-06-03-812ca7]]'
- '[[Changes/Cursor/2026-06-03-teams-are-the-operating-unit-for-a-department-region-or-subsidiary-this-is-what|cursor-2026-06-03-df00e8]]'
- '[[Changes/Cursor/2026-06-04-you-can-now-hand-the-local-agent-your-own-tools-by-passing-function-definitions|cursor-2026-06-04-020531]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-06-v2-1-166-github-335118845-ef990727|claude-code-2026-06-06-v2-1-166-github-335118845-ef990727]]'
theme: safety-privacy
type: change
---

# Hardened cross-session messaging: messages relayed via `SendMessage` from other

<!-- chronolog:begin region="description" -->
Hardened cross-session messaging: messages relayed via `SendMessage` from other Claude sessions no longer carry user authority — receivers refuse relayed permission requests, and auto mode blocks them
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Hardened cross-session messaging: messages relayed via `SendMessage` from other Claude sessions no longer carry user authority — receivers refuse relayed permission requests, and auto mode blocks them
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.166
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-06-03-claude-agents-json-now-includes-waitingfor-showing-what-a-waiting-session-is-blo|claude-code-2026-06-03-cc3caf]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: safety-privacy
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]
- Lag Days: 1147
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes