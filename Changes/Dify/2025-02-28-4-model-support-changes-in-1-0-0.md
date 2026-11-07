---
card_id: dify-2025-02-28-35f8de
date: '2025-02-28'
description: 'Dify · 2025-02-28 · Model Support: 4 changes in v1.0.0 — Through this
  system, we''ve decoupled tools and models that can be expanded from Dify, enabling
  you to…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 781
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 1516fc7ff4c732fe5bd97db47f137000142370a1655629b11fad32817fd45521
product: dify
product_name: Dify
record:
  card_id: dify-2025-02-28-35f8de
  comparison: ''
  date: '2025-02-28'
  description: 'Dify — v1.0.0: 4 Model Support changes'
  evidence:
  - quote: Through this system, we've decoupled tools and models that can be expanded
      from Dify, enabling you to install them in a truly plug-and-play manner.
    source_release: https://github.com/langgenius/dify/releases/tag/1.0.0
  - quote: This command extracts all models and tools used in the current environment.
      The workers parameter determines the number of parallel processes during extraction;
      adjust it according to your needs.
    source_release: https://github.com/langgenius/dify/releases/tag/1.0.0
  - quote: This command will prefix existing model and tool vendors in the database
      with langgenius, such as converting openai to langgenius/openai/openai. This
      operation may affect the functioning of the older Dify version, so back up your
      database before running this command to prevent unwanted issues.
    source_release: https://github.com/langgenius/dify/releases/tag/1.0.0
  - quote: '**Unified Reasoning Model**: Standardized the think tag with `<think></think>`
      by @junjiem for enhanced compatibility.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.0.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 4-model-support-changes-in-1-0-0
  source_release: dify-2025-02-28-1-0-0-github-202962689-d5695ce1
  source_type: github_releases
  theme: model-support
  title: 4 Model Support changes in 1.0.0
  type: change
related_changes:
- "[[Changes/Open WebUI/2025-02-27-reliable-model-imports-from-the-community-platform-resolved-import-failures-allo|\U0001F504
  Reliable Model Imports from the Community Platform]]"
- "[[Changes/Open WebUI/2025-02-27-models-now-display-correctly-with-enable-forward-user-info-headers-addressed-a-b|\U0001F6E0️
  Models Now Display Correctly with ENABLE_FORWARD_USER_INFO_HEADERS]]"
- '[[Changes/OpenHands/2025-02-27-allow-selecting-the-claude-3-7-model-from-via-the-anthropic-provider-by-amanape|Allow
  selecting the Claude 3.7 model from via the Anthropic provider]]'
source_release: '[[Releases/Dify/dify-2025-02-28-1-0-0-github-202962689-d5695ce1|dify-2025-02-28-1-0-0-github-202962689-d5695ce1]]'
source_type: github_releases
theme: model-support
title: 4 Model Support changes in 1.0.0
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Model Support changes in 1.0.0

**Dify** · 2025-02-28 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.0.0) · from [[Releases/Dify/dify-2025-02-28-1-0-0-github-202962689-d5695ce1|v1.0.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Through this system, we've decoupled tools and models that can be expanded from Dify, enabling you to install them in a truly plug-and-play manner.

> This command extracts all models and tools used in the current environment. The workers parameter determines the number of parallel processes during extraction; adjust it according to your needs.

> This command will prefix existing model and tool vendors in the database with langgenius, such as converting openai to langgenius/openai/openai. This operation may affect the functioning of the older Dify version, so back up your database before running this command to prevent unwanted issues.

> **Unified Reasoning Model**: Standardized the think tag with `<think></think>` by @junjiem for enhanced compatibility.

Source: https://github.com/langgenius/dify/releases/tag/1.0.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2025-02-28-we-ve-introduced-a-new-agent-node-in-workflow-where-the-agent-s-behavior-can-now|We've introduced a new Agent node in Workflow, where the agent's behavior can now…]] · Agent Mode
- [[Changes/Dify/2025-02-28-we-are-glad-to-share-that-we-re-launching-dify-v1-0-0|We are glad to share that we're launching Dify v1.0.0]] · Collaboration
- [[Changes/Dify/2025-02-28-2-developer-workflow-changes-in-1-0-0|2 Developer Workflow changes in 1.0.0]] · Developer Workflow
- [[Changes/Dify/2025-02-28-9-apps-and-integrations-changes-in-1-0-0|9 Apps and Integrations changes in 1.0.0]] · Apps and Integrations
- [[Changes/Dify/2025-02-28-hnsw-vector-index-now-available-for-tidb-vector-store-with-tiflash-optimizing-ho|HNSW Vector Index]] · Other changes
- [[Changes/Dify/2025-02-28-13-other-changes-in-1-0-0|13 other changes in 1.0.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2025-02-27 · OpenHands · [[Changes/OpenHands/2025-02-27-allow-selecting-the-claude-3-7-model-from-via-the-anthropic-provider-by-amanape|Allow selecting the Claude 3.7 model from via the Anthropic provider]]
- Later: 2025-02-28 · Lovable · [[Changes/Lovable/2025-02-28-all-lovable-users-are-now-using-sonnet-3-7-for-the-main-workflow-which-means-tha|All Lovable users are now using Sonnet 3.7 for the main workflow, which means…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2025-02-28-35f8de&body=Card%3A%20Changes%2FDify%2F2025-02-28-4-model-support-changes-in-1-0-0.md%0ACard%20ID%3A%20dify-2025-02-28-35f8de%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.0.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->