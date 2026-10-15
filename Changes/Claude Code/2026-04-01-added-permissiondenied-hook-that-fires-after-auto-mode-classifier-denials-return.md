---
card_id: claude-code-2026-04-01-e43a95
date: '2026-04-01'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|cursor-2023-07-06-d7057e]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1000
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v4
impact: significant
machine_hash: fa6dc0774936f4922a6aff83c7e06a45b94953a14461cc687a3addf30a0fc757
product: claude-code
product_name: Claude Code
record:
  ai_generated: true
  card_id: claude-code-2026-04-01-e43a95
  comparison: ''
  confidence: low
  date: '2026-04-01'
  description: 'Claude Code — v2.1.89: Added `PermissionDenied` hook that fires after
    auto mode classifier denials — return `{retry: true}` to tell the model it can
    retry'
  evidence:
  - quote: 'Added `PermissionDenied` hook that fires after auto mode classifier denials
      — return `{retry: true}` to tell the model it can retry'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.89
  extractor_version: fallback-v4
  impact: significant
  product: claude-code
  product_name: Claude Code
  slug: added-permissiondenied-hook-that-fires-after-auto-mode-classifier-denials-return
  source_release: claude-code-2026-04-01-v2-1-89-github-303967782-358023f0
  source_type: github_releases
  theme: agent-mode
  theme_matches:
  - matched_terms:
    - auto mode
    score: 60
    theme: agent-mode
  - matched_terms:
    - model
    score: 50
    theme: model-support
  theme_resolution: manual-semantic-rule-v1
  title: Added `PermissionDenied` hook that fires after auto mode classifier denials
  type: change
related_changes:
- '[[Changes/Cursor/2026-03-25-your-codebase-build-outputs-and-secrets-all-stay-on-internal-machines-running-in|cursor-2026-03-25-6430ab]]'
- '[[Changes/Cursor/2026-03-25-cursor-now-supports-self-hosted-cloud-agents-that-keep-your-code-and-tool-execut|cursor-2026-03-25-ef9cb1]]'
- '[[Changes/Claude Code/2026-03-26-added-taskcreated-hook-that-fires-when-a-task-is-created-via-taskcreate|claude-code-2026-03-26-484bd3]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-01-v2-1-89-github-303967782-358023f0|claude-code-2026-04-01-v2-1-89-github-303967782-358023f0]]'
source_type: github_releases
theme: agent-mode
title: Added PermissionDenied hook that fires after auto mode classifier denials
type: change
---

# Added `PermissionDenied` hook that fires after auto mode classifier denials

<!-- chronolog:begin region="description" -->
Claude Code — v2.1.89: Added `PermissionDenied` hook that fires after auto mode classifier denials — return `{retry: true}` to tell the model it can retry
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `PermissionDenied` hook that fires after auto mode classifier denials — return `{retry: true}` to tell the model it can retry
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.89
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
No evidence-backed evolution relationship assigned.
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: agent-mode
- Relation: same-theme-chronology
- Inference: No adoption, equivalence, or causation claim.
- Scope: tracked-products-only
- Role: later-observed
- First In Tracked: [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|cursor-2023-07-06-d7057e]]
- Lag Days: 1000
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes