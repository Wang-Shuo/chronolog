---
card_id: dify-2024-12-18-ebe2a6
date: '2024-12-18'
description: 'Dify · 2024-12-18 · Model Support: 8 changes in v0.14.1 — **Gemini Models**:
  Gemini models have received a robust upgrade. With integrated response metadata…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 709
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9393875bb7de8c61779ece84ce8160a579aabf818d28eaa48f30f098614ed86a
product: dify
product_name: Dify
record:
  card_id: dify-2024-12-18-ebe2a6
  comparison: ''
  date: '2024-12-18'
  description: 'Dify — v0.14.1: 8 Model Support changes'
  evidence:
  - quote: '**Gemini Models**: Gemini models have received a robust upgrade. With
      integrated response metadata, you can manage token counting more efficiently,
      thanks to enhancements by @totsukash in #11743.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.14.1
  - quote: '**OpenAI O1 Model**: Take advantage of the new OpenAI O1 model with updated
      pricing and a larger token limit, providing even greater flexibility for your
      projects, courtesy of @laipz8200 in #11780.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.14.1
  - quote: 'feat: add gitee ai vl models by @fchange in https://github.com/langgenius/dify/pull/11697'
    source_release: https://github.com/langgenius/dify/releases/tag/0.14.1
  - quote: 'feat: enhance gemini models by @hjlarry in https://github.com/langgenius/dify/pull/11497'
    source_release: https://github.com/langgenius/dify/releases/tag/0.14.1
  - quote: 'feat: use Gemini response metadata for token counting by @totsukash in
      https://github.com/langgenius/dify/pull/11743'
    source_release: https://github.com/langgenius/dify/releases/tag/0.14.1
  - quote: 'chore: improve gemini models by @hjlarry in https://github.com/langgenius/dify/pull/11745'
    source_release: https://github.com/langgenius/dify/releases/tag/0.14.1
  - quote: 'feat: add openai o1 & update pricing and max_token of other models by
      @laipz8200 in https://github.com/langgenius/dify/pull/11780'
    source_release: https://github.com/langgenius/dify/releases/tag/0.14.1
  - quote: feat:add hunyuan model(hunyuan-role, hunyuan-large, hunyuan-large-rol…
      by @xander-art in https://github.com/langgenius/dify/pull/11766
    source_release: https://github.com/langgenius/dify/releases/tag/0.14.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 8-model-support-changes-in-0-14-1
  source_release: dify-2024-12-18-0-14-1-github-191377353-1e563ad0
  source_type: github_releases
  theme: model-support
  title: 8 Model Support changes in 0.14.1
  type: change
related_changes:
- '[[Changes/Dify/2024-12-16-9-model-support-changes-in-0-14-0|9 Model Support changes
  in 0.14.0]]'
- '[[Changes/Gemini/2024-12-17-priority-access-with-gemini-advanced-try-our-latest-2-0-experimental-advanced-mo|Priority
  access with Gemini Advanced: Try our latest 2.0 Experimental Advanced model]]'
- '[[Changes/Ollama/2024-12-17-falcon3-https-ollama-com-library-falcon3-a-family-of-efficient-ai-models-under-1|Falcon3((source
  link) A family of efficient AI models under…]]'
source_release: '[[Releases/Dify/dify-2024-12-18-0-14-1-github-191377353-1e563ad0|dify-2024-12-18-0-14-1-github-191377353-1e563ad0]]'
source_type: github_releases
theme: model-support
title: 8 Model Support changes in 0.14.1
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Model Support changes in 0.14.1

**Dify** · 2024-12-18 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/0.14.1) · from [[Releases/Dify/dify-2024-12-18-0-14-1-github-191377353-1e563ad0|v0.14.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **Gemini Models**: Gemini models have received a robust upgrade. With integrated response metadata, you can manage token counting more efficiently, thanks to enhancements by @totsukash in #11743.

> **OpenAI O1 Model**: Take advantage of the new OpenAI O1 model with updated pricing and a larger token limit, providing even greater flexibility for your projects, courtesy of @laipz8200 in #11780.

> feat: add gitee ai vl models by @fchange in https://github.com/langgenius/dify/pull/11697

> feat: enhance gemini models by @hjlarry in https://github.com/langgenius/dify/pull/11497

> feat: use Gemini response metadata for token counting by @totsukash in https://github.com/langgenius/dify/pull/11743

> chore: improve gemini models by @hjlarry in https://github.com/langgenius/dify/pull/11745

> feat: add openai o1 & update pricing and max_token of other models by @laipz8200 in https://github.com/langgenius/dify/pull/11780

> feat:add hunyuan model(hunyuan-role, hunyuan-large, hunyuan-large-rol… by @xander-art in https://github.com/langgenius/dify/pull/11766

Source: https://github.com/langgenius/dify/releases/tag/0.14.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2024-12-18-4-reliability-and-performance-changes-in-0-14-1|4 Reliability and Performance changes in 0.14.1]] · Reliability and Performance
- [[Changes/Dify/2024-12-18-make-login-lockout-duration-configurable-by-kazuhisa-wada-in-https-github-com-la|make login lockout duration configurable]] · Account and Access
- [[Changes/Dify/2024-12-18-opendal-integration-introducing-apache-opendal-https-github-com-apache-opendal-t|OpenDAL Integration: Introducing Apache…]] · Apps and Integrations
- [[Changes/Dify/2024-12-18-stop-the-service-command-please-execute-in-the-docker-directory|Stop the service，Command, please execute in the docker directory]] · Developer Workflow
- [[Changes/Dify/2024-12-18-33-other-changes-in-0-14-1|33 other changes in 0.14.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2024-12-17 · Ollama · [[Changes/Ollama/2024-12-17-falcon3-https-ollama-com-library-falcon3-a-family-of-efficient-ai-models-under-1|Falcon3((source link) A family of efficient AI models under…]]
- Later: 2024-12-19 · ElevenLabs · [[Changes/ElevenLabs/2024-12-19-model|Model]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2024-12-18-ebe2a6&body=Card%3A%20Changes%2FDify%2F2024-12-18-8-model-support-changes-in-0-14-1.md%0ACard%20ID%3A%20dify-2024-12-18-ebe2a6%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F0.14.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->