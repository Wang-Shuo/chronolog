---
card_id: claude-code-2026-07-20-b887a9
date: '2026-07-20'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  lag_days: 1191
  role: follower
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-07-20-fixed-telemetry-misreporting-permission-denials-failed-permission-prompt-request|claude-code-2026-07-20-47c44c]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 28a9f50c535ac2ee5cb9ef1a7796f761eda67cf72152823d07aa41bc200e4dcb
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-07-18-fixed-bash-permission-checks-misjudging-very-long-commands-commands-over-10-000|claude-code-2026-07-18-c7cc5a]]'
- '[[Changes/Claude Code/2026-07-18-fixed-bash-permission-checks-to-fail-closed-on-file-descriptor-redirect-forms-th|claude-code-2026-07-18-e06205]]'
- '[[Changes/Claude Code/2026-07-20-fixed-telemetry-misreporting-permission-denials-failed-permission-prompt-request|claude-code-2026-07-20-47c44c]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-20-v2-1-216-github-356972381-87e422ae|claude-code-2026-07-20-v2-1-216-github-356972381-87e422ae]]'
theme: safety-privacy
type: change
---

# Added `sandbox.filesystem.disabled` setting to skip filesystem isolation while k

<!-- chronolog:begin region="description" -->
Added `sandbox.filesystem.disabled` setting to skip filesystem isolation while keeping network egress control
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `sandbox.filesystem.disabled` setting to skip filesystem isolation while keeping network egress control
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.216
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-07-20-fixed-telemetry-misreporting-permission-denials-failed-permission-prompt-request|claude-code-2026-07-20-47c44c]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: safety-privacy
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]
- Lag Days: 1191
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes