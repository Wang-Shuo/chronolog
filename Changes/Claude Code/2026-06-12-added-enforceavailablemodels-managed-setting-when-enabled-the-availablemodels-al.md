---
card_id: claude-code-2026-06-12-f8c57e
date: '2026-06-12'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|chatgpt-2023-01-09-5af3d4]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1250
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v3
impact: significant
machine_hash: 36eb7c28a5e0c7245645d6d512f7f2476c9597c3d9721045f4153518fcddec28
product: claude-code
product_name: Claude Code
record:
  ai_generated: true
  card_id: claude-code-2026-06-12-f8c57e
  comparison: ''
  confidence: low
  date: '2026-06-12'
  description: 'Claude Code — v2.1.175: Added `enforceAvailableModels` managed setting
    — when enabled, the `availableModels` allowlist also constrains the Default model
    (a Default that would resolve to a disallowed model now falls back to the first
    allowed model), and user or project settings can no longer widen a managed `availableModels`
    list'
  evidence:
  - quote: Added `enforceAvailableModels` managed setting — when enabled, the `availableModels`
      allowlist also constrains the Default model (a Default that would resolve to
      a disallowed model now falls back to the first allowed model), and user or project
      settings can no longer widen a managed `availableModels` list
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.175
  extractor_version: fallback-v3
  impact: significant
  product: claude-code
  product_name: Claude Code
  slug: added-enforceavailablemodels-managed-setting-when-enabled-the-availablemodels-al
  source_release: claude-code-2026-06-12-v2-1-175-github-338335820-6f3a7124
  source_type: github_releases
  theme: model-support
  title: Added `enforceAvailableModels` managed setting — when enabled, the `availableMod
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-06-10-pro-standard-pro-plans-only|chatgpt-2026-06-10-c9cf00]]'
- '[[Changes/Claude Code/2026-06-10-added-model-attribute-to-the-claude-code-lines-of-code-count-otel-metric|claude-code-2026-06-10-2a22f5]]'
- '[[Changes/ChatGPT/2026-06-12-as-of-june-12-2026-gpt-5-2-models-are-no-longer-available-in-chatgpt-this-applie|chatgpt-2026-06-12-a53a9d]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-12-v2-1-175-github-338335820-6f3a7124|claude-code-2026-06-12-v2-1-175-github-338335820-6f3a7124]]'
source_type: github_releases
theme: model-support
title: Added enforceAvailableModels managed setting — when enabled, the availableMod
type: change
---

# Added `enforceAvailableModels` managed setting — when enabled, the `availableMod

<!-- chronolog:begin region="description" -->
Claude Code — v2.1.175: Added `enforceAvailableModels` managed setting — when enabled, the `availableModels` allowlist also constrains the Default model (a Default that would resolve to a disallowed model now falls back to the first allowed model), and user or project settings can no longer widen a managed `availableModels` list
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `enforceAvailableModels` managed setting — when enabled, the `availableModels` allowlist also constrains the Default model (a Default that would resolve to a disallowed model now falls back to the first allowed model), and user or project settings can no longer widen a managed `availableModels` list
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.175
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
No evidence-backed evolution relationship assigned.
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: model-support
- Relation: same-theme-chronology
- Inference: No adoption, equivalence, or causation claim.
- Scope: tracked-products-only
- Role: later-observed
- First In Tracked: [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|chatgpt-2023-01-09-5af3d4]]
- Lag Days: 1250
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes