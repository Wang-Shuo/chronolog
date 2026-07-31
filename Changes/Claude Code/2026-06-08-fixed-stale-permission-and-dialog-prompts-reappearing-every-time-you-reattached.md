---
card_id: claude-code-2026-06-08-d4c97e
date: '2026-06-08'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  lag_days: 1149
  role: follower
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-06-08-added-safe-mode-flag-and-claude-code-safe-mode-to-start-claude-code-with-all-cus|claude-code-2026-06-08-55bad2]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 3f2dd876b0ca9be3019535c6634d6201a1d32964eb12d8600f79145db085e72e
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Cursor/2026-06-04-you-can-now-hand-the-local-agent-your-own-tools-by-passing-function-definitions|cursor-2026-06-04-020531]]'
- '[[Changes/Claude Code/2026-06-06-hardened-cross-session-messaging-messages-relayed-via-sendmessage-from-other-cla|claude-code-2026-06-06-931934]]'
- '[[Changes/Claude Code/2026-06-08-added-safe-mode-flag-and-claude-code-safe-mode-to-start-claude-code-with-all-cus|claude-code-2026-06-08-55bad2]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-08-v2-1-169-github-336158564-d513d69d|claude-code-2026-06-08-v2-1-169-github-336158564-d513d69d]]'
theme: safety-privacy
type: change
---

# Fixed stale permission and dialog prompts reappearing every time you reattached

<!-- chronolog:begin region="description" -->
Fixed stale permission and dialog prompts reappearing every time you reattached to a remote session whose worker had died while waiting on them
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Fixed stale permission and dialog prompts reappearing every time you reattached to a remote session whose worker had died while waiting on them
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.169
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-06-08-added-safe-mode-flag-and-claude-code-safe-mode-to-start-claude-code-with-all-cus|claude-code-2026-06-08-55bad2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: safety-privacy
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]
- Lag Days: 1149
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes