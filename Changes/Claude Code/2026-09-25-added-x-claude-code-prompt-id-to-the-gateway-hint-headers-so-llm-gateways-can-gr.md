---
card_id: claude-code-2026-09-25-7b8fca
date: '2026-09-25'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|chatgpt-2023-01-09-5af3d4]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1355
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v3
impact: incremental
machine_hash: 59064b2a77b1629c7458e9b8695e88c154759856d614353b6e8670f6d195b995
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-25-7b8fca
  comparison: ''
  date: '2026-09-25'
  description: 'Claude Code — v2.1.283: Added `x-claude-code-prompt-id` to the gateway
    hint headers so LLM gateways can group the requests that serve one user prompt;
    opt in with `CLAUDE_CODE_GATEWAY_HINT_HEADERS=1`'
  evidence:
  - quote: Added `x-claude-code-prompt-id` to the gateway hint headers so LLM gateways
      can group the requests that serve one user prompt; opt in with `CLAUDE_CODE_GATEWAY_HINT_HEADERS=1`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.283
  extractor_version: fallback-v3
  impact: incremental
  product: claude-code
  product_name: Claude Code
  slug: added-x-claude-code-prompt-id-to-the-gateway-hint-headers-so-llm-gateways-can-gr
  source_release: claude-code-2026-09-25-v2-1-283-github-396845205-9a5a07f8
  source_type: github_releases
  theme: model-support
  title: Added `x-claude-code-prompt-id` to the gateway hint headers so LLM gateways
    can
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-22-added-claude-opus-5-5-claude-opus-5-5-now-the-default-opus-model-1m-context-4-20|claude-code-2026-09-22-09ab0e]]'
- '[[Changes/Claude Code/2026-09-25-added-availablemodelsmatch-managed-setting-with-exact-an-availablemodels-entry-a|claude-code-2026-09-25-017617]]'
- '[[Changes/Claude Code/2026-09-25-added-deniedmodels-managed-setting-to-block-specific-models-even-when-availablem|claude-code-2026-09-25-0414cd]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-25-v2-1-283-github-396845205-9a5a07f8|claude-code-2026-09-25-v2-1-283-github-396845205-9a5a07f8]]'
source_type: github_releases
theme: model-support
title: Added x-claude-code-prompt-id to the gateway hint headers so LLM gateways can
type: change
---

# Added `x-claude-code-prompt-id` to the gateway hint headers so LLM gateways can

<!-- chronolog:begin region="description" -->
Claude Code — v2.1.283: Added `x-claude-code-prompt-id` to the gateway hint headers so LLM gateways can group the requests that serve one user prompt; opt in with `CLAUDE_CODE_GATEWAY_HINT_HEADERS=1`
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `x-claude-code-prompt-id` to the gateway hint headers so LLM gateways can group the requests that serve one user prompt; opt in with `CLAUDE_CODE_GATEWAY_HINT_HEADERS=1`
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.283
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
- Lag Days: 1355
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes