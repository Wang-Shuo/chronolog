---
card_id: claude-code-2026-05-07-db2677
date: '2026-05-07'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-27-enterprise-support|cursor-2023-07-27-4d0704]]'
  lag_days: 1015
  role: follower
  scope: tracked-products-only
  theme: enterprise-admin
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-04-28-pasting-a-pr-url-into-the-resume-search-box-now-finds-the-session-that-created-t|claude-code-2026-04-28-318ef9]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 7855b4bd1f904f3aa1938d3383c9906b3363e2a4ea7d1e86ffd5e347be949d45
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-04-23-added-disable-updates-env-var-to-completely-block-all-update-paths-including-man|claude-code-2026-04-23-85de42]]'
- '[[Changes/Claude Code/2026-04-28-pasting-a-pr-url-into-the-resume-search-box-now-finds-the-session-that-created-t|claude-code-2026-04-28-318ef9]]'
- '[[Changes/Cursor/2026-05-04-this-release-introduces-updates-for-enterprise-admins-a-new-system-for-model-con|cursor-2026-05-04-3db092]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-07-v2-1-133-github-319164825-08653677|claude-code-2026-05-07-v2-1-133-github-319164825-08653677]]'
theme: enterprise-admin
type: change
---

# Added `parentSettingsBehavior` admin-tier key (`'first-wins' | 'merge'`) to let

<!-- chronolog:begin region="description" -->
Added `parentSettingsBehavior` admin-tier key (`'first-wins' | 'merge'`) to let admins opt SDK `managedSettings` (parent tier) into the policy merge
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `parentSettingsBehavior` admin-tier key (`'first-wins' | 'merge'`) to let admins opt SDK `managedSettings` (parent tier) into the policy merge
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.133
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-04-28-pasting-a-pr-url-into-the-resume-search-box-now-finds-the-session-that-created-t|claude-code-2026-04-28-318ef9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: enterprise-admin
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-07-27-enterprise-support|cursor-2023-07-27-4d0704]]
- Lag Days: 1015
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes