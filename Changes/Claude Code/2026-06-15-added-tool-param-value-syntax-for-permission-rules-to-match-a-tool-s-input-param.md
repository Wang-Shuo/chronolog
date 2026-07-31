---
card_id: claude-code-2026-06-15-47194d
date: '2026-06-15'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  lag_days: 1156
  role: follower
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-06-10-fixed-webfetch-domain-example-com-wildcard-domain-rules-never-matching-subdomain|claude-code-2026-06-10-c26bef]]'
extractor_version: fallback-v2
impact: paradigm-shift
machine_hash: a26948a787f669509649cb6cc987b8ceb244da0804e4bba5a576b95d01e5585d
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-06-08-fixed-stale-permission-and-dialog-prompts-reappearing-every-time-you-reattached|claude-code-2026-06-08-d4c97e]]'
- '[[Changes/Claude Code/2026-06-10-fixed-webfetch-domain-example-com-wildcard-domain-rules-never-matching-subdomain|claude-code-2026-06-10-c26bef]]'
- '[[Changes/Cursor/2026-06-10-you-can-now-run-bugbot-and-security-review-with-review-before-pushing-code-revie|cursor-2026-06-10-a3d99d]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-15-v2-1-178-github-339741361-902bc427|claude-code-2026-06-15-v2-1-178-github-339741361-902bc427]]'
theme: safety-privacy
type: change
---

# Added `Tool(param:value)` syntax for permission rules to match a tool's input pa

<!-- chronolog:begin region="description" -->
Added `Tool(param:value)` syntax for permission rules to match a tool's input parameters (with `*` wildcard), e.g. `Agent(model:opus)` to block Opus subagents
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `Tool(param:value)` syntax for permission rules to match a tool's input parameters (with `*` wildcard), e.g. `Agent(model:opus)` to block Opus subagents
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.178
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-06-10-fixed-webfetch-domain-example-com-wildcard-domain-rules-never-matching-subdomain|claude-code-2026-06-10-c26bef]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: safety-privacy
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]
- Lag Days: 1156
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes