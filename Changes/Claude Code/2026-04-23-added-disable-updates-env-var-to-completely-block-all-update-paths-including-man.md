---
card_id: claude-code-2026-04-23-85de42
date: '2026-04-23'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-27-enterprise-support|cursor-2023-07-27-4d0704]]'
  lag_days: 1001
  role: follower
  scope: tracked-products-only
  theme: enterprise-admin
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-04-23-from-pr-now-accepts-gitlab-merge-request-bitbucket-pull-request-and-github-enter|claude-code-2026-04-23-098176]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 9485b2bfa44423284830894eb87df852ee1fe0ae9ed149f616d4414617682041
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-04-10-added-os-ca-certificate-store-trust-by-default-so-enterprise-tls-proxies-work-wi|claude-code-2026-04-10-efc05f]]'
- '[[Changes/ChatGPT/2026-04-16-we-re-beginning-to-rollout-ads-for-users-on-free-and-go-plans-in-australia-new-z|chatgpt-2026-04-16-ab1b3a]]'
- '[[Changes/Claude Code/2026-04-23-from-pr-now-accepts-gitlab-merge-request-bitbucket-pull-request-and-github-enter|claude-code-2026-04-23-098176]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-23-v2-1-118-github-312487295-b3c6b04c|claude-code-2026-04-23-v2-1-118-github-312487295-b3c6b04c]]'
theme: enterprise-admin
type: change
---

# Added `DISABLE_UPDATES` env var to completely block all update paths including m

<!-- chronolog:begin region="description" -->
Added `DISABLE_UPDATES` env var to completely block all update paths including manual `claude update` — stricter than `DISABLE_AUTOUPDATER`
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `DISABLE_UPDATES` env var to completely block all update paths including manual `claude update` — stricter than `DISABLE_AUTOUPDATER`
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.118
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-04-23-from-pr-now-accepts-gitlab-merge-request-bitbucket-pull-request-and-github-enter|claude-code-2026-04-23-098176]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: enterprise-admin
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-07-27-enterprise-support|cursor-2023-07-27-4d0704]]
- Lag Days: 1001
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes