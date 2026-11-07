---
card_id: dify-2025-01-22-26f2f4
date: '2025-01-22'
description: 'Dify · 2025-01-22 · Model Support: 8 changes in v0.15.2 — **Minimax-Text-01
  Support**: Added support for the new Minimax-Text-01 model by @AAlexDing in #12763.'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 744
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ca00ccee401f7cd737780fa61e5e427f4d3ac562ef9cc2ae98d205bbc676322f
product: dify
product_name: Dify
record:
  card_id: dify-2025-01-22-26f2f4
  comparison: ''
  date: '2025-01-22'
  description: 'Dify — v0.15.2: 8 Model Support changes'
  evidence:
  - quote: '**Minimax-Text-01 Support**: Added support for the new Minimax-Text-01
      model by @AAlexDing in #12763.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.15.2
  - quote: '**Gemini-2.0-Flash-Thinking-Exp-01-21**: New experimental model added
      by @jiandanfeng in #12924.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.15.2
  - quote: '**Doubao 1.5 Model Series**: Support for Doubao 1.5 models in our tooling
      setup by @sinomoe in #12935.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.15.2
  - quote: '**Rerank Model Bug**: Fixed the rerank model and switch issues across
      various tools by @WTW0313 in #12721 and @luckylhb90 in #12774.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.15.2
  - quote: '**OpenAI Bad Request Error**: Cleaned up issues causing bad request errors
      on OpenAI o1 endpoint by @k-zaku in #12839.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.15.2
  - quote: Update deepseek model configuration by @wangiii in https://github.com/langgenius/dify/pull/12899
    source_release: https://github.com/langgenius/dify/releases/tag/0.15.2
  - quote: 'feat: add gemini-2.0-flash-thinking-exp-01-21 by @jiandanfeng in https://github.com/langgenius/dify/pull/12924'
    source_release: https://github.com/langgenius/dify/releases/tag/0.15.2
  - quote: 'feat(ark): support doubao 1.5 series of models by @sinomoe in https://github.com/langgenius/dify/pull/12935'
    source_release: https://github.com/langgenius/dify/releases/tag/0.15.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 8-model-support-changes-in-0-15-2
  source_release: dify-2025-01-22-0-15-2-github-196033249-96b23bc1
  source_type: github_releases
  theme: model-support
  title: 8 Model Support changes in 0.15.2
  type: change
related_changes:
- '[[Changes/Aider/2025-01-20-4-model-support-changes-in-v0-72-0|4 Model Support changes
  in v0.72.0]]'
- '[[Changes/DeepSeek API/2025-01-20-deepseek-reasoner|deepseek-reasoner]]'
- '[[Changes/Cline/2025-01-21-add-vs-code-lm-api-provider-to-run-models-provided-by-other-vs-code-extensions-e|Add
  VS Code LM API provider to run models provided by other VS Code extensions…]]'
source_release: '[[Releases/Dify/dify-2025-01-22-0-15-2-github-196033249-96b23bc1|dify-2025-01-22-0-15-2-github-196033249-96b23bc1]]'
source_type: github_releases
theme: model-support
title: 8 Model Support changes in 0.15.2
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Model Support changes in 0.15.2

**Dify** · 2025-01-22 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/0.15.2) · from [[Releases/Dify/dify-2025-01-22-0-15-2-github-196033249-96b23bc1|v0.15.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **Minimax-Text-01 Support**: Added support for the new Minimax-Text-01 model by @AAlexDing in #12763.

> **Gemini-2.0-Flash-Thinking-Exp-01-21**: New experimental model added by @jiandanfeng in #12924.

> **Doubao 1.5 Model Series**: Support for Doubao 1.5 models in our tooling setup by @sinomoe in #12935.

> **Rerank Model Bug**: Fixed the rerank model and switch issues across various tools by @WTW0313 in #12721 and @luckylhb90 in #12774.

> **OpenAI Bad Request Error**: Cleaned up issues causing bad request errors on OpenAI o1 endpoint by @k-zaku in #12839.

> Update deepseek model configuration by @wangiii in https://github.com/langgenius/dify/pull/12899

> feat: add gemini-2.0-flash-thinking-exp-01-21 by @jiandanfeng in https://github.com/langgenius/dify/pull/12924

> feat(ark): support doubao 1.5 series of models by @sinomoe in https://github.com/langgenius/dify/pull/12935

Source: https://github.com/langgenius/dify/releases/tag/0.15.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2025-01-22-3-files-and-data-changes-in-0-15-2|3 Files and Data changes in 0.15.2]] · Files and Data
- [[Changes/Dify/2025-01-22-stop-the-service-command-please-execute-in-the-docker-directory|Stop the service，Command, please execute in the docker directory]] · Developer Workflow
- [[Changes/Dify/2025-01-22-agent-log-formatting-tweaked-deepseek-s-api-response-handling-to-fix-format-issu|Agent Log Formatting]] · Agent Mode
- [[Changes/Dify/2025-01-22-34-other-changes-in-0-15-2|34 other changes in 0.15.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2025-01-21 · Cline · [[Changes/Cline/2025-01-21-add-vs-code-lm-api-provider-to-run-models-provided-by-other-vs-code-extensions-e|Add VS Code LM API provider to run models provided by other VS Code extensions…]]
- Later: 2025-01-22 · Open WebUI · [[Changes/Open WebUI/2025-01-22-2-model-support-changes-in-v0-5-6|2 Model Support changes in v0.5.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2025-01-22-26f2f4&body=Card%3A%20Changes%2FDify%2F2025-01-22-8-model-support-changes-in-0-15-2.md%0ACard%20ID%3A%20dify-2025-01-22-26f2f4%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F0.15.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->