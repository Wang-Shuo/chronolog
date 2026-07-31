---
card_id: claude-code-2026-06-10-c26bef
date: '2026-06-10'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  lag_days: 1151
  role: follower
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-06-08-fixed-stale-permission-and-dialog-prompts-reappearing-every-time-you-reattached|claude-code-2026-06-08-d4c97e]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 85cf0934274c9874e757274c144dc84e7d74c33a00cc894709ff90522c64efa1
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-06-06-hardened-cross-session-messaging-messages-relayed-via-sendmessage-from-other-cla|claude-code-2026-06-06-931934]]'
- '[[Changes/Claude Code/2026-06-08-added-safe-mode-flag-and-claude-code-safe-mode-to-start-claude-code-with-all-cus|claude-code-2026-06-08-55bad2]]'
- '[[Changes/Claude Code/2026-06-08-fixed-stale-permission-and-dialog-prompts-reappearing-every-time-you-reattached|claude-code-2026-06-08-d4c97e]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-10-v2-1-172-github-337412034-dc68562c|claude-code-2026-06-10-v2-1-172-github-337412034-dc68562c]]'
theme: safety-privacy
type: change
---

# Fixed `WebFetch(domain:*.example.com)` wildcard domain rules never matching subd

<!-- chronolog:begin region="description" -->
Fixed `WebFetch(domain:*.example.com)` wildcard domain rules never matching subdomains in allow, deny, and ask position, and file permission rules with mid-pattern wildcards (e.g. `Read(secrets-*/config.json)`) being rejected at startup
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Fixed `WebFetch(domain:*.example.com)` wildcard domain rules never matching subdomains in allow, deny, and ask position, and file permission rules with mid-pattern wildcards (e.g. `Read(secrets-*/config.json)`) being rejected at startup
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.172
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-06-08-fixed-stale-permission-and-dialog-prompts-reappearing-every-time-you-reattached|claude-code-2026-06-08-d4c97e]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: safety-privacy
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]
- Lag Days: 1151
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes