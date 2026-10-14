---
card_id: claude-code-2026-03-26-3c8e42
date: '2026-03-26'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|chatgpt-2023-01-09-5af3d4]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1172
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v3
impact: significant
machine_hash: fc5e508847c44721e27a8d4fecf4734841054fd853a086932efb70efac2fe537
product: claude-code
product_name: Claude Code
record:
  ai_generated: true
  card_id: claude-code-2026-03-26-3c8e42
  comparison: ''
  confidence: low
  date: '2026-03-26'
  description: 'Claude Code — v2.1.84: Added `ANTHROPIC_DEFAULT_{OPUS,SONNET,HAIKU}_MODEL_SUPPORTS`
    env vars to override effort/thinking capability detection for pinned default models
    for 3p (Bedrock, Vertex, Foundry), and `_MODEL_NAME`/`_DESCRIPTION` to customize
    the `/model` picker label'
  evidence:
  - quote: Added `ANTHROPIC_DEFAULT_{OPUS,SONNET,HAIKU}_MODEL_SUPPORTS` env vars to
      override effort/thinking capability detection for pinned default models for
      3p (Bedrock, Vertex, Foundry), and `_MODEL_NAME`/`_DESCRIPTION` to customize
      the `/model` picker label
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.84
  extractor_version: fallback-v3
  impact: significant
  product: claude-code
  product_name: Claude Code
  slug: added-anthropic-default-opus-sonnet-haiku-model-supports-env-vars-to-override-ef
  source_release: claude-code-2026-03-26-v2-1-84-github-301540101-d02104aa
  source_type: github_releases
  theme: model-support
  theme_matches:
  - matched_terms:
    - model
    - models
    - opus
    - sonnet
    score: 200
    theme: model-support
  - matched_terms:
    - picker
    score: 50
    theme: interface-experience
  theme_resolution: manual-semantic-rule-v2
  title: Added `ANTHROPIC_DEFAULT_{OPUS,SONNET,HAIKU}_MODEL_SUPPORTS` env vars to
    overrid
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-03-18-we-re-rolling-out-gpt-5-4-mini-in-chatgpt-gpt-5-4-mini-is-available-to-free-and|chatgpt-2026-03-18-64ffa1]]'
- '[[Changes/Claude Code/2026-03-19-added-effort-frontmatter-support-for-skills-and-slash-commands-to-override-the-m|claude-code-2026-03-19-9f5e79]]'
- '[[Changes/Cursor/2026-03-25-self-hosted-cloud-agents-offer-the-same-capabilities-as-cursor-hosted-cloud-agen|cursor-2026-03-25-6db779]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-26-v2-1-84-github-301540101-d02104aa|claude-code-2026-03-26-v2-1-84-github-301540101-d02104aa]]'
source_type: github_releases
theme: model-support
title: Added ANTHROPIC_DEFAULT{OPUS,SONNET,HAIKU}MODEL_SUPPORTS env vars to overrid
type: change
---

# Added `ANTHROPIC_DEFAULT_{OPUS,SONNET,HAIKU}_MODEL_SUPPORTS` env vars to overrid

<!-- chronolog:begin region="description" -->
Claude Code — v2.1.84: Added `ANTHROPIC_DEFAULT_{OPUS,SONNET,HAIKU}_MODEL_SUPPORTS` env vars to override effort/thinking capability detection for pinned default models for 3p (Bedrock, Vertex, Foundry), and `_MODEL_NAME`/`_DESCRIPTION` to customize the `/model` picker label
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `ANTHROPIC_DEFAULT_{OPUS,SONNET,HAIKU}_MODEL_SUPPORTS` env vars to override effort/thinking capability detection for pinned default models for 3p (Bedrock, Vertex, Foundry), and `_MODEL_NAME`/`_DESCRIPTION` to customize the `/model` picker label
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.84
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
- Lag Days: 1172
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes