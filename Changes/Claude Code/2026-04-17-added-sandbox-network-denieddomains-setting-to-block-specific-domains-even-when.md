---
card_id: claude-code-2026-04-17-856cba
date: '2026-04-17'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  lag_days: 1097
  role: follower
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-04-14-the-model-can-now-discover-and-invoke-built-in-slash-commands-like-init-review-a|claude-code-2026-04-14-eb6e81]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: f2ad7d2f4ef409e3de6db32ca5e8308373f549dc22526e7b3a7cbda0faafae8f
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-04-02-fixed-plan-mode-in-remote-sessions-losing-track-of-the-plan-file-after-a-contain|claude-code-2026-04-02-76e8e8]]'
- '[[Changes/Claude Code/2026-04-09-added-subprocess-sandboxing-with-pid-namespace-isolation-on-linux-when-claude-co|claude-code-2026-04-09-5db0ee]]'
- '[[Changes/Claude Code/2026-04-14-the-model-can-now-discover-and-invoke-built-in-slash-commands-like-init-review-a|claude-code-2026-04-14-eb6e81]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-17-v2-1-113-github-310525785-1b5293ba|claude-code-2026-04-17-v2-1-113-github-310525785-1b5293ba]]'
theme: safety-privacy
type: change
---

# Added `sandbox.network.deniedDomains` setting to block specific domains even whe

<!-- chronolog:begin region="description" -->
Added `sandbox.network.deniedDomains` setting to block specific domains even when a broader `allowedDomains` wildcard would otherwise permit them
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `sandbox.network.deniedDomains` setting to block specific domains even when a broader `allowedDomains` wildcard would otherwise permit them
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.113
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-04-14-the-model-can-now-discover-and-invoke-built-in-slash-commands-like-init-review-a|claude-code-2026-04-14-eb6e81]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: safety-privacy
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]
- Lag Days: 1097
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes