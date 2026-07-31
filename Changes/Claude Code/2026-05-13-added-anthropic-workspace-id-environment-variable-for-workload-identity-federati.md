---
card_id: claude-code-2026-05-13-fdd0e0
date: '2026-05-13'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-27-enterprise-support|cursor-2023-07-27-4d0704]]'
  lag_days: 1021
  role: follower
  scope: tracked-products-only
  theme: enterprise-admin
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-05-08-added-claude-code-enable-feedback-survey-for-otel-to-re-enable-the-session-quali|claude-code-2026-05-08-cbfe28]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: ed8c43caeb8d061a73a7317879d588a273d0ff2c8737ab61565cf5e9010f3497
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-05-07-added-parentsettingsbehavior-admin-tier-key-first-wins-merge-to-let-admins-opt-s|claude-code-2026-05-07-db2677]]'
- '[[Changes/Claude Code/2026-05-08-added-claude-code-enable-feedback-survey-for-otel-to-re-enable-the-session-quali|claude-code-2026-05-08-cbfe28]]'
- '[[Changes/Cursor/2026-05-11-teams-admins-and-individual-plan-users-can-now-customize-the-effort-level-bugbot|cursor-2026-05-11-91c39e]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-13-v2-1-141-github-322186176-9f8e2e22|claude-code-2026-05-13-v2-1-141-github-322186176-9f8e2e22]]'
theme: enterprise-admin
type: change
---

# Added `ANTHROPIC_WORKSPACE_ID` environment variable for workload identity federa

<!-- chronolog:begin region="description" -->
Added `ANTHROPIC_WORKSPACE_ID` environment variable for workload identity federation — scopes the minted token to a specific workspace when the federation rule covers more than one
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `ANTHROPIC_WORKSPACE_ID` environment variable for workload identity federation — scopes the minted token to a specific workspace when the federation rule covers more than one
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.141
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-05-08-added-claude-code-enable-feedback-survey-for-otel-to-re-enable-the-session-quali|claude-code-2026-05-08-cbfe28]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: enterprise-admin
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-07-27-enterprise-support|cursor-2023-07-27-4d0704]]
- Lag Days: 1021
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes