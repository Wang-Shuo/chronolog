---
card_id: ollama-2024-02-02-c01f8d
date: '2024-02-02'
description: 'Ollama · 2024-02-02 · Model Support: 13 changes in v0.1.23 — The [LLaVA](https://ollama.ai/library/llava)
  model family on Ollama has been updated to [version…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 389
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 035690cf38e6d75fec9b0da5bdc1969296800b64b5358e6efc2ad3a86dde8823
product: ollama
product_name: Ollama
record:
  card_id: ollama-2024-02-02-c01f8d
  comparison: ''
  date: '2024-02-02'
  description: 'Ollama — v0.1.23: 13 Model Support changes'
  evidence:
  - quote: 'The [LLaVA](https://ollama.ai/library/llava) model family on Ollama has
      been updated to [version 1.6](https://llava-vl.github.io/blog/2024-01-30-llava-1-6/),
      and now includes a new `34b` version:'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.1.23
  - quote: '`ollama run llava` A new 7B LLaVA model based on mistral.'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.1.23
  - quote: '`ollama run llava:13b` 13B LLaVA model'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.1.23
  - quote: '`ollama run llava:34b` 34B LLaVA model – one of the most powerful open-source
      vision models available'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.1.23
  - quote: 'These new models share new improvements:'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.1.23
  - quote: '**More permissive licenses:** LLaVA 1.6 models are distributed via the
      Apache 2.0 license or the LLaMA 2 Community License.'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.1.23
  - quote: '**Higher image resolution:** support for up to 4x more pixels, allowing
      the model to grasp more details.'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.1.23
  - quote: '**Improved text recognition and reasoning capabilities:** these models
      are trained on additional document, chart and diagram data sets.'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.1.23
  - quote: If set to a positive duration (e.g. `20m`, `1hr` or `30`), the model will
      stay loaded for the provided duration
    source_release: https://github.com/ollama/ollama/releases/tag/v0.1.23
  - quote: If set to a negative duration (e.g. `-1`), the model will stay loaded indefinitely
    source_release: https://github.com/ollama/ollama/releases/tag/v0.1.23
  - quote: If set to `0`, the model will be unloaded immediately once finished
    source_release: https://github.com/ollama/ollama/releases/tag/v0.1.23
  - quote: If not set, the model will stay loaded for 5 minutes by default
    source_release: https://github.com/ollama/ollama/releases/tag/v0.1.23
  - quote: New `keep_alive` API parameter to control how long models stay loaded
    source_release: https://github.com/ollama/ollama/releases/tag/v0.1.23
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: ollama
  product_name: Ollama
  slug: 13-model-support-changes-in-v0-1-23
  source_release: ollama-2024-02-02-v0-1-23-github-139618642-fffe661f
  source_type: github_releases
  theme: model-support
  title: 13 Model Support changes in v0.1.23
  type: change
related_changes:
- '[[Changes/Ollama/2024-01-26-stable-lm-2-https-ollama-ai-library-stablelm2-a-state-of-the-art-1-6b-small-lang|Stable
  LM 2((source link)]]'
- '[[Changes/Dify/2024-02-01-4-model-support-changes-in-0-5-3|4 Model Support changes
  in 0.5.3]]'
- '[[Changes/Gemini/2024-02-01-bard-with-gemini-pro-is-coming-to-more-languages|Bard
  with Gemini Pro is coming to more languages]]'
source_release: '[[Releases/Ollama/ollama-2024-02-02-v0-1-23-github-139618642-fffe661f|ollama-2024-02-02-v0-1-23-github-139618642-fffe661f]]'
source_type: github_releases
theme: model-support
title: 13 Model Support changes in v0.1.23
type: change
---

<!-- chronolog:begin region="header" -->
# 13 Model Support changes in v0.1.23

**Ollama** · 2024-02-02 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/ollama/ollama/releases/tag/v0.1.23) · from [[Releases/Ollama/ollama-2024-02-02-v0-1-23-github-139618642-fffe661f|v0.1.23]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> The [LLaVA](https://ollama.ai/library/llava) model family on Ollama has been updated to [version 1.6](https://llava-vl.github.io/blog/2024-01-30-llava-1-6/), and now includes a new `34b` version:

> `ollama run llava` A new 7B LLaVA model based on mistral.

> `ollama run llava:13b` 13B LLaVA model

> `ollama run llava:34b` 34B LLaVA model – one of the most powerful open-source vision models available

> These new models share new improvements:

> **More permissive licenses:** LLaVA 1.6 models are distributed via the Apache 2.0 license or the LLaMA 2 Community License.

> **Higher image resolution:** support for up to 4x more pixels, allowing the model to grasp more details.

> **Improved text recognition and reasoning capabilities:** these models are trained on additional document, chart and diagram data sets.

> If set to a positive duration (e.g. `20m`, `1hr` or `30`), the model will stay loaded for the provided duration

> If set to a negative duration (e.g. `-1`), the model will stay loaded indefinitely

> If set to `0`, the model will be unloaded immediately once finished

> If not set, the model will stay loaded for 5 minutes by default

> New `keep_alive` API parameter to control how long models stay loaded

Source: https://github.com/ollama/ollama/releases/tag/v0.1.23
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Ollama/2024-02-02-ollama-serve-will-now-print-prompt-when-ollama-debug-1-is-set|ollama serve will now print prompt when OLLAMA_DEBUG=1 is set]] · Developer Workflow
- [[Changes/Ollama/2024-02-02-3-multimodal-input-changes-in-v0-1-23|3 Multimodal Input changes in v0.1.23]] · Multimodal Input
- [[Changes/Ollama/2024-02-02-when-making-api-requests-the-new-keep-alive-parameter-can-be-used-to-control-how|When making API requests, the new keep_alive parameter can be used to control how…]] · Reliability and Performance
- [[Changes/Ollama/2024-02-02-6-other-changes-in-v0-1-23|6 other changes in v0.1.23]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2024-02-01 · Gemini · [[Changes/Gemini/2024-02-01-bard-with-gemini-pro-is-coming-to-more-languages|Bard with Gemini Pro is coming to more languages]]
- Later: 2024-02-03 · Aider · [[Changes/Aider/2024-02-03-added-support-for-model-gpt-4-0125-preview-and-openai-s-alias-model-gpt-4-turbo|Added support for --model gpt-4-0125-preview and OpenAI's alias…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20ollama-2024-02-02-c01f8d&body=Card%3A%20Changes%2FOllama%2F2024-02-02-13-model-support-changes-in-v0-1-23.md%0ACard%20ID%3A%20ollama-2024-02-02-c01f8d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Follama%2Follama%2Freleases%2Ftag%2Fv0.1.23%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->