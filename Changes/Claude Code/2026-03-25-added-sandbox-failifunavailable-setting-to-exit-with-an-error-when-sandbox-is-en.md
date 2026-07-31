---
card_id: claude-code-2026-03-25-7d730c
date: '2026-03-25'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  lag_days: 1074
  role: follower
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-03-20-fixed-unnecessary-permission-prompts-for-bash-commands-containing-dashes-in-stri|claude-code-2026-03-20-c0b999]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 0eb592ff6bb659337f7b94f3cba7a7bee43d7ae82ac446cec000215e11d2f12a
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-03-18-fixed-custom-status-line-showing-nothing-when-workspace-trust-is-blocking-it|claude-code-2026-03-18-88ccc1]]'
- '[[Changes/Claude Code/2026-03-20-added-channels-permission-relay-channel-servers-that-declare-the-permission-capa|claude-code-2026-03-20-35235c]]'
- '[[Changes/Claude Code/2026-03-20-fixed-unnecessary-permission-prompts-for-bash-commands-containing-dashes-in-stri|claude-code-2026-03-20-c0b999]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-25-v2-1-83-github-301019202-ba6a8317|claude-code-2026-03-25-v2-1-83-github-301019202-ba6a8317]]'
theme: safety-privacy
type: change
---

# Added `sandbox.failIfUnavailable` setting to exit with an error when sandbox is

<!-- chronolog:begin region="description" -->
Added `sandbox.failIfUnavailable` setting to exit with an error when sandbox is enabled but cannot start, instead of running unsandboxed
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `sandbox.failIfUnavailable` setting to exit with an error when sandbox is enabled but cannot start, instead of running unsandboxed
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.83
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-03-20-fixed-unnecessary-permission-prompts-for-bash-commands-containing-dashes-in-stri|claude-code-2026-03-20-c0b999]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: safety-privacy
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]
- Lag Days: 1074
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes