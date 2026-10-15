---
card_id: claude-code-2026-08-08-f19c8f
date: '2026-08-08'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1210
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v4
impact: significant
machine_hash: 94ceaee0971d7a7309158ba69894a73a56b2d7795459eb3755a0a7956a8567f9
product: claude-code
product_name: Claude Code
record:
  ai_generated: true
  card_id: claude-code-2026-08-08-f19c8f
  comparison: ''
  confidence: low
  date: '2026-08-08'
  description: 'Claude Code — v2.1.225: Fixed auto mode counting a safety-filter refusal
    of its own permission check toward the consecutive-block limit; the action is
    still denied, but the model is now told to move on rather than retry'
  evidence:
  - quote: Fixed auto mode counting a safety-filter refusal of its own permission
      check toward the consecutive-block limit; the action is still denied, but the
      model is now told to move on rather than retry
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.225
  extractor_version: fallback-v4
  impact: significant
  product: claude-code
  product_name: Claude Code
  slug: fixed-auto-mode-counting-a-safety-filter-refusal-of-its-own-permission-check-tow
  source_release: claude-code-2026-08-08-v2-1-225-github-367046190-ccb40049
  source_type: github_releases
  theme: safety-privacy
  theme_matches:
  - matched_terms:
    - auto mode
    score: 60
    theme: agent-mode
  - matched_terms:
    - model
    score: 50
    theme: model-support
  - matched_terms:
    - safety
    score: 50
    theme: safety-privacy
  theme_resolution: manual-semantic-rule-v2
  title: Fixed auto mode counting a safety-filter refusal of its own permission check
    toward…
  type: change
related_changes:
- '[[Changes/Claude Code/2026-08-06-fixed-a-bash-permission-bypass-where-a-crafted-command-could-hide-parts-of-itsel|claude-code-2026-08-06-4346f9]]'
- '[[Changes/Claude Code/2026-08-06-fixed-permission-prompts-so-commands-padded-with-tabs-or-invisible-unicode-can-n|claude-code-2026-08-06-c063c5]]'
- '[[Changes/Claude Code/2026-08-08-added-a-workspace-trust-prompt-to-claude-agents-for-untrusted-directories-matchi|claude-code-2026-08-08-d35e2a]]'
source_release: '[[Releases/Claude Code/claude-code-2026-08-08-v2-1-225-github-367046190-ccb40049|claude-code-2026-08-08-v2-1-225-github-367046190-ccb40049]]'
source_type: github_releases
theme: safety-privacy
title: Fixed auto mode counting a safety-filter refusal of its own permission check
  toward…
type: change
---

# Fixed auto mode counting a safety-filter refusal of its own permission check toward…

<!-- chronolog:begin region="description" -->
Claude Code — v2.1.225: Fixed auto mode counting a safety-filter refusal of its own permission check toward the consecutive-block limit; the action is still denied, but the model is now told to move on rather than retry
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Fixed auto mode counting a safety-filter refusal of its own permission check toward the consecutive-block limit; the action is still denied, but the model is now told to move on rather than retry
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.225
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
- Lag Days: 1210
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes