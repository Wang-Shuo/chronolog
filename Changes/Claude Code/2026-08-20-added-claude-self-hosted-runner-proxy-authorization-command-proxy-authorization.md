---
card_id: claude-code-2026-08-20-387cca
date: '2026-08-20'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1251
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v4
impact: incremental
machine_hash: 5be35888e56ffda02d924f0af6904e012b1f0a7a41cb30e5812ff729c2bf28f2
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-08-20-387cca
  comparison: ''
  date: '2026-08-20'
  description: 'Claude Code — v2.1.238: Added `claude self-hosted-runner --proxy-authorization-command`
    / `--proxy-authorization-file` for egress proxies that require a freshly issued
    `Proxy-Authorization` header on every connection'
  evidence:
  - quote: Added `claude self-hosted-runner --proxy-authorization-command` / `--proxy-authorization-file`
      for egress proxies that require a freshly issued `Proxy-Authorization` header
      on every connection
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.238
  extractor_version: fallback-v4
  impact: incremental
  product: claude-code
  product_name: Claude Code
  slug: added-claude-self-hosted-runner-proxy-authorization-command-proxy-authorization
  source_release: claude-code-2026-08-20-v2-1-238-github-373927029-c96744e2
  source_type: github_releases
  theme: developer-workflow
  theme_matches: []
  theme_resolution: manual-semantic-rule-v1
  title: Added `claude self-hosted-runner --proxy-authorization-command`…
  type: change
related_changes:
- '[[Changes/Claude Code/2026-07-22-changed-code-review-to-run-as-a-background-subagent-so-review-work-no-longer-fil|claude-code-2026-07-22-9535c3]]'
- '[[Changes/Claude Code/2026-08-07-added-a-cancel-and-confirm-step-when-removing-an-unavailable-paste-changes-a-com|claude-code-2026-08-07-5f6ac5]]'
- '[[Changes/Claude Code/2026-08-14-added-gitlab-merge-request-url-support-to-the-worktree-flag-and-the-claude-agent|claude-code-2026-08-14-df12a1]]'
source_release: '[[Releases/Claude Code/claude-code-2026-08-20-v2-1-238-github-373927029-c96744e2|claude-code-2026-08-20-v2-1-238-github-373927029-c96744e2]]'
source_type: github_releases
theme: developer-workflow
title: Added claude self-hosted-runner --proxy-authorization-command…
type: change
---

# Added `claude self-hosted-runner --proxy-authorization-command`…

<!-- chronolog:begin region="description" -->
Claude Code — v2.1.238: Added `claude self-hosted-runner --proxy-authorization-command` / `--proxy-authorization-file` for egress proxies that require a freshly issued `Proxy-Authorization` header on every connection
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `claude self-hosted-runner --proxy-authorization-command` / `--proxy-authorization-file` for egress proxies that require a freshly issued `Proxy-Authorization` header on every connection
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.238
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
No evidence-backed evolution relationship assigned.
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: developer-workflow
- Relation: same-theme-chronology
- Inference: No adoption, equivalence, or causation claim.
- Scope: tracked-products-only
- Role: later-observed
- First In Tracked: [[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]
- Lag Days: 1251
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes