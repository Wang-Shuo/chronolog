---
card_id: claude-code-2026-06-15-47194d
date: '2026-06-15'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1156
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v4
impact: paradigm-shift
machine_hash: 0cb281116686c842c650ebfc9e9013d462d15baa8a04649d71b8250369fb5f28
product: claude-code
product_name: Claude Code
record:
  ai_generated: true
  card_id: claude-code-2026-06-15-47194d
  comparison: ''
  confidence: low
  date: '2026-06-15'
  description: 'Claude Code — v2.1.178: Added `Tool(param:value)` syntax for permission
    rules to match a tool''s input parameters (with `*` wildcard), e.g. `Agent(model:opus)`
    to block Opus subagents'
  evidence:
  - quote: Added `Tool(param:value)` syntax for permission rules to match a tool's
      input parameters (with `*` wildcard), e.g. `Agent(model:opus)` to block Opus
      subagents
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.178
  extractor_version: fallback-v4
  impact: paradigm-shift
  product: claude-code
  product_name: Claude Code
  slug: added-tool-param-value-syntax-for-permission-rules-to-match-a-tool-s-input-param
  source_release: claude-code-2026-06-15-v2-1-178-github-339741361-902bc427
  source_type: github_releases
  theme: safety-privacy
  theme_matches:
  - matched_terms:
    - agent
    - subagents
    score: 100
    theme: agent-mode
  - matched_terms:
    - model
    - opus
    score: 100
    theme: model-support
  theme_resolution: manual-semantic-rule-v2
  title: Added `Tool(param:value)` syntax for permission rules to match a tool's input…
  type: change
related_changes:
- '[[Changes/Claude Code/2026-06-08-fixed-stale-permission-and-dialog-prompts-reappearing-every-time-you-reattached|claude-code-2026-06-08-d4c97e]]'
- '[[Changes/Claude Code/2026-06-10-fixed-webfetch-domain-example-com-wildcard-domain-rules-never-matching-subdomain|claude-code-2026-06-10-c26bef]]'
- '[[Changes/Cursor/2026-06-10-you-can-now-run-bugbot-and-security-review-with-review-before-pushing-code-revie|cursor-2026-06-10-a3d99d]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-15-v2-1-178-github-339741361-902bc427|claude-code-2026-06-15-v2-1-178-github-339741361-902bc427]]'
source_type: github_releases
theme: safety-privacy
title: Added Tool(param:value) syntax for permission rules to match a tool's input…
type: change
---

# Added `Tool(param:value)` syntax for permission rules to match a tool's input…

<!-- chronolog:begin region="description" -->
Claude Code — v2.1.178: Added `Tool(param:value)` syntax for permission rules to match a tool's input parameters (with `*` wildcard), e.g. `Agent(model:opus)` to block Opus subagents
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `Tool(param:value)` syntax for permission rules to match a tool's input parameters (with `*` wildcard), e.g. `Agent(model:opus)` to block Opus subagents
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.178
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
No evidence-backed evolution relationship assigned.
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: safety-privacy
- Relation: same-theme-chronology
- Inference: No adoption, equivalence, or causation claim.
- Scope: tracked-products-only
- Role: later-observed
- First In Tracked: [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]
- Lag Days: 1156
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes