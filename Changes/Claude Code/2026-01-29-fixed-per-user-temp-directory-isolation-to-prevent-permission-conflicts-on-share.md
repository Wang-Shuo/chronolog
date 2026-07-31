---
card_id: claude-code-2026-01-29-fc6c51
date: '2026-01-29'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  lag_days: 1019
  role: follower
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-01-14-fixed-security-vulnerability-where-wildcard-permission-rules-could-match-compoun|claude-code-2026-01-14-a0bfb2]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: d5fe8c59768c322c59b54eb43f85dead9eba665f13d3e592f3c09abea4ad18e6
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-01-09-added-detection-and-warnings-for-unreachable-permission-rules-with-warnings-in-d|claude-code-2026-01-09-b5be29]]'
- '[[Changes/Claude Code/2026-01-14-added-ability-to-provide-feedback-when-accepting-permission-prompts|claude-code-2026-01-14-835bd2]]'
- '[[Changes/Claude Code/2026-01-14-fixed-security-vulnerability-where-wildcard-permission-rules-could-match-compoun|claude-code-2026-01-14-a0bfb2]]'
source_release: '[[Releases/Claude Code/claude-code-2026-01-29-v2-1-23-github-280926274-b1e77a6a|claude-code-2026-01-29-v2-1-23-github-280926274-b1e77a6a]]'
theme: safety-privacy
type: change
---

# Fixed per-user temp directory isolation to prevent permission conflicts on share

<!-- chronolog:begin region="description" -->
Fixed per-user temp directory isolation to prevent permission conflicts on shared systems
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Fixed per-user temp directory isolation to prevent permission conflicts on shared systems
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.23
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-01-14-fixed-security-vulnerability-where-wildcard-permission-rules-could-match-compoun|claude-code-2026-01-14-a0bfb2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: safety-privacy
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]
- Lag Days: 1019
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes