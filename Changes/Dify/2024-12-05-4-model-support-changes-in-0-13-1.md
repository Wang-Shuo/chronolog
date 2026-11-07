---
card_id: dify-2024-12-05-26c584
date: '2024-12-05'
description: 'Dify · 2024-12-05 · Model Support: 4 changes in v0.13.1 — **Improved
  Bedrock Model Message Handling**: Working with Bedrock models just got smoother.
  We''ve…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 696
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a17e3bd15acd3de94978ea0ee5ef11a284d42ee1309805c317bf7bc2f60f6f57
product: dify
product_name: Dify
record:
  card_id: dify-2024-12-05-26c584
  comparison: ''
  date: '2024-12-05'
  description: 'Dify — v0.13.1: 4 Model Support changes'
  evidence:
  - quote: '**Improved Bedrock Model Message Handling**: Working with Bedrock models
      just got smoother. We''ve merged consecutive messages from the same role to
      reduce frustrating errors. Thanks to @yihong0618 for the fix in `fix: better
      bedrock message handler` (#11317).'
    source_release: https://github.com/langgenius/dify/releases/tag/0.13.1
  - quote: '**Multi-Model Debugging**: We''ve fixed the problem where sending messages
      was not possible during debugging with multiple models and conversations, thanks
      to @xuzuodong in #11333.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.13.1
  - quote: 'chore: improve zhipu LLM by @hjlarry in https://github.com/langgenius/dify/pull/11321'
    source_release: https://github.com/langgenius/dify/releases/tag/0.13.1
  - quote: update pricing for bedrock nova LLM models by @ybalbert001 in https://github.com/langgenius/dify/pull/11336
    source_release: https://github.com/langgenius/dify/releases/tag/0.13.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 4-model-support-changes-in-0-13-1
  source_release: dify-2024-12-05-0-13-1-github-189107355-84bcd3da
  source_type: github_releases
  theme: model-support
  title: 4 Model Support changes in 0.13.1
  type: change
related_changes:
- '[[Changes/Aider/2024-12-01-pdf-support-for-sonnet-and-gemini-models|PDF support
  for Sonnet and Gemini models]]'
- '[[Changes/Dify/2024-12-03-2-model-support-changes-in-0-13-0|2 Model Support changes
  in 0.13.0]]'
- '[[Changes/Ollama/2024-12-04-3-model-support-changes-in-v0-5-0|3 Model Support changes
  in v0.5.0]]'
source_release: '[[Releases/Dify/dify-2024-12-05-0-13-1-github-189107355-84bcd3da|dify-2024-12-05-0-13-1-github-189107355-84bcd3da]]'
source_type: github_releases
theme: model-support
title: 4 Model Support changes in 0.13.1
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Model Support changes in 0.13.1

**Dify** · 2024-12-05 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/0.13.1) · from [[Releases/Dify/dify-2024-12-05-0-13-1-github-189107355-84bcd3da|v0.13.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **Improved Bedrock Model Message Handling**: Working with Bedrock models just got smoother. We've merged consecutive messages from the same role to reduce frustrating errors. Thanks to @yihong0618 for the fix in `fix: better bedrock message handler` (#11317).

> **Multi-Model Debugging**: We've fixed the problem where sending messages was not possible during debugging with multiple models and conversations, thanks to @xuzuodong in #11333.

> chore: improve zhipu LLM by @hjlarry in https://github.com/langgenius/dify/pull/11321

> update pricing for bedrock nova LLM models by @ybalbert001 in https://github.com/langgenius/dify/pull/11336

Source: https://github.com/langgenius/dify/releases/tag/0.13.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2024-12-05-stop-the-service-command-please-execute-in-the-docker-directory|Stop the service，Command, please execute in the docker directory]] · Developer Workflow
- [[Changes/Dify/2024-12-05-25-other-changes-in-0-13-1|25 other changes in 0.13.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2024-12-04 · Ollama · [[Changes/Ollama/2024-12-04-3-model-support-changes-in-v0-5-0|3 Model Support changes in v0.5.0]]
- Later: 2024-12-06 · Aider · [[Changes/Aider/2024-12-06-support-for-new-amazon-bedrock-nova-models|Support for new Amazon Bedrock Nova models]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2024-12-05-26c584&body=Card%3A%20Changes%2FDify%2F2024-12-05-4-model-support-changes-in-0-13-1.md%0ACard%20ID%3A%20dify-2024-12-05-26c584%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F0.13.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->