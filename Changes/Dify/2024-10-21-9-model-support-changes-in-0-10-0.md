---
card_id: dify-2024-10-21-389aa6
date: '2024-10-21'
description: 'Dify · 2024-10-21 · Model Support: 9 changes in v0.10.0 — **Advanced
  File Handling**: Nodes like **START**, **LLM**, **HTTP Request** and **IF-ELSE**
  now…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 651
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 78c62bbabad645755989054ccd8099f08027a47269a4ca5ef8a8c0b4d5dd8ae9
product: dify
product_name: Dify
record:
  card_id: dify-2024-10-21-389aa6
  comparison: ''
  date: '2024-10-21'
  description: 'Dify — v0.10.0: 9 Model Support changes'
  evidence:
  - quote: '**Advanced File Handling**: Nodes like **START**, **LLM**, **HTTP Request**
      and **IF-ELSE** now seamlessly manage "File" types, simplifying the processing
      of various file formats within your workflows.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.10.0
  - quote: '**Efficient Array Handling**: Directly use `array[string]` and `array[number]`
      in LLM prompts for more agile data interactions.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.10.0
  - quote: '**Fireworks Model Integration**: Access Qwen2.5 72B Instruct models for
      expanded AI capability, thanks to @yaoice in #9333 and #9340.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.10.0
  - quote: 'feat: Add fireworks custom llm intergration by @yaoice in https://github.com/langgenius/dify/pull/9333'
    source_release: https://github.com/langgenius/dify/releases/tag/0.10.0
  - quote: 'feat: Add qwen2.5 72B Instruct model in Fireworks AI by @yaoice in https://github.com/langgenius/dify/pull/9340'
    source_release: https://github.com/langgenius/dify/releases/tag/0.10.0
  - quote: Adapt input type parameter with MiniMax embedding model by @yaoice in https://github.com/langgenius/dify/pull/9342
    source_release: https://github.com/langgenius/dify/releases/tag/0.10.0
  - quote: 'feat: add yi-lightning llm model for yi by @hwzhuhao in https://github.com/langgenius/dify/pull/9458'
    source_release: https://github.com/langgenius/dify/releases/tag/0.10.0
  - quote: 'feat: add parameter top-k for the llm model provided by openrouter and
      siliconflow by @hwzhuhao in https://github.com/langgenius/dify/pull/9455'
    source_release: https://github.com/langgenius/dify/releases/tag/0.10.0
  - quote: 'feat: add yi custom llm intergration by @hwzhuhao in https://github.com/langgenius/dify/pull/9482'
    source_release: https://github.com/langgenius/dify/releases/tag/0.10.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 9-model-support-changes-in-0-10-0
  source_release: dify-2024-10-21-0-10-0-github-180976661-70c09171
  source_type: github_releases
  theme: model-support
  title: 9 Model Support changes in 0.10.0
  type: change
related_changes:
- '[[Changes/Dify/2024-10-14-13-model-support-changes-in-0-9-2|13 Model Support changes
  in 0.9.2]]'
- '[[Changes/Ollama/2024-10-17-2-model-support-changes-in-v0-3-14|2 Model Support
  changes in v0.3.14]]'
- '[[Changes/ElevenLabs/2024-10-20-api|API]]'
source_release: '[[Releases/Dify/dify-2024-10-21-0-10-0-github-180976661-70c09171|dify-2024-10-21-0-10-0-github-180976661-70c09171]]'
source_type: github_releases
theme: model-support
title: 9 Model Support changes in 0.10.0
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Model Support changes in 0.10.0

**Dify** · 2024-10-21 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/0.10.0) · from [[Releases/Dify/dify-2024-10-21-0-10-0-github-180976661-70c09171|v0.10.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **Advanced File Handling**: Nodes like **START**, **LLM**, **HTTP Request** and **IF-ELSE** now seamlessly manage "File" types, simplifying the processing of various file formats within your workflows.

> **Efficient Array Handling**: Directly use `array[string]` and `array[number]` in LLM prompts for more agile data interactions.

> **Fireworks Model Integration**: Access Qwen2.5 72B Instruct models for expanded AI capability, thanks to @yaoice in #9333 and #9340.

> feat: Add fireworks custom llm intergration by @yaoice in https://github.com/langgenius/dify/pull/9333

> feat: Add qwen2.5 72B Instruct model in Fireworks AI by @yaoice in https://github.com/langgenius/dify/pull/9340

> Adapt input type parameter with MiniMax embedding model by @yaoice in https://github.com/langgenius/dify/pull/9342

> feat: add yi-lightning llm model for yi by @hwzhuhao in https://github.com/langgenius/dify/pull/9458

> feat: add parameter top-k for the llm model provided by openrouter and siliconflow by @hwzhuhao in https://github.com/langgenius/dify/pull/9455

> feat: add yi custom llm intergration by @hwzhuhao in https://github.com/langgenius/dify/pull/9482

Source: https://github.com/langgenius/dify/releases/tag/0.10.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2024-10-21-if-you-have-a-basic-chatbot-or-text-generator-app-with-the-vision-feature-enable| If you have a Basic Chatbot or Text Generator App with the ‘Vision’ feature…]] · Multimodal Input
- [[Changes/Dify/2024-10-21-2-reliability-and-performance-changes-in-0-10-0|2 Reliability and Performance changes in 0.10.0]] · Reliability and Performance
- [[Changes/Dify/2024-10-21-2-files-and-data-changes-in-0-10-0|2 Files and Data changes in 0.10.0]] · Files and Data
- [[Changes/Dify/2024-10-21-update-dify-sandbox-version-to-0-2-10-by-hexian2001-in-https-github-com-langgeni|Update dify-sandbox version to 0.2.10]] · Safety and Privacy
- [[Changes/Dify/2024-10-21-2-account-and-access-changes-in-0-10-0|2 Account and Access changes in 0.10.0]] · Account and Access
- [[Changes/Dify/2024-10-21-stop-the-service-command-please-execute-in-the-docker-directory|Stop the service，Command, please execute in the docker directory]] · Developer Workflow
- [[Changes/Dify/2024-10-21-53-other-changes-in-0-10-0|53 other changes in 0.10.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2024-10-20 · ElevenLabs · [[Changes/ElevenLabs/2024-10-20-api|API]]
- Later: 2024-10-21 · Ollama · [[Changes/Ollama/2024-10-21-2-model-support-changes-in-v0-4-0|2 Model Support changes in v0.4.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2024-10-21-389aa6&body=Card%3A%20Changes%2FDify%2F2024-10-21-9-model-support-changes-in-0-10-0.md%0ACard%20ID%3A%20dify-2024-10-21-389aa6%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F0.10.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->