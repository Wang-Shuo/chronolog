---
card_id: claude-code-2026-06-04-e5de26
date: '2026-06-04'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-27-enterprise-support|cursor-2023-07-27-4d0704]]'
  lag_days: 1043
  role: follower
  scope: tracked-products-only
  theme: enterprise-admin
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-05-13-added-anthropic-workspace-id-environment-variable-for-workload-identity-federati|claude-code-2026-05-13-fdd0e0]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: effc7015d109b93eb2c24a32d64a46858a79579b26386c664a81701dab47e7ce
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-05-13-added-anthropic-workspace-id-environment-variable-for-workload-identity-federati|claude-code-2026-05-13-fdd0e0]]'
- '[[Changes/Cursor/2026-06-03-organizations|cursor-2026-06-03-604006]]'
- '[[Changes/ChatGPT/2026-06-04-we-re-beginning-to-roll-out-ads-for-users-on-free-and-go-plans-in-the-uk-plus-pr|chatgpt-2026-06-04-586af0]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-04-v2-1-163-github-334509318-c6b9f988|claude-code-2026-06-04-v2-1-163-github-334509318-c6b9f988]]'
theme: enterprise-admin
type: change
---

# Added `requiredMinimumVersion` and `requiredMaximumVersion` managed settings — C

<!-- chronolog:begin region="description" -->
Added `requiredMinimumVersion` and `requiredMaximumVersion` managed settings — Claude Code refuses to start if its version is outside the allowed range and directs the user to an approved version
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `requiredMinimumVersion` and `requiredMaximumVersion` managed settings — Claude Code refuses to start if its version is outside the allowed range and directs the user to an approved version
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.163
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-05-13-added-anthropic-workspace-id-environment-variable-for-workload-identity-federati|claude-code-2026-05-13-fdd0e0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: enterprise-admin
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-07-27-enterprise-support|cursor-2023-07-27-4d0704]]
- Lag Days: 1043
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes