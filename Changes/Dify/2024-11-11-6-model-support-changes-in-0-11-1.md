---
card_id: dify-2024-11-11-69b3d0
date: '2024-11-11'
description: 'Dify · 2024-11-11 · Model Support: 6 changes in v0.11.1 — **Anthropic
  Claude-3-5-Haiku Support via OpenRouter**: Get ready to leverage the capabilities
  of…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 672
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 711057d91d7fe5802d925b6fc81574fe957abcba310326314c770de5a81fe12f
product: dify
product_name: Dify
record:
  card_id: dify-2024-11-11-69b3d0
  comparison: ''
  date: '2024-11-11'
  description: 'Dify — v0.11.1: 6 Model Support changes'
  evidence:
  - quote: '**Anthropic Claude-3-5-Haiku Support via OpenRouter**: Get ready to leverage
      the capabilities of Anthropic’s Claude-3-5-Haiku by @infinitnet in #10331.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.11.1
  - quote: '**Video Understanding and CogVideo Tool Support**: Your LLM can now understand
      videos, and with the new CogVideo tool, process them too! Thanks to @hjlarry
      in #9828 and #10456.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.11.1
  - quote: 'feat: add support for anthropic/claude-3-5-haiku through OpenRouter by
      @infinitnet in https://github.com/langgenius/dify/pull/10331'
    source_release: https://github.com/langgenius/dify/releases/tag/0.11.1
  - quote: 'feat: support LLM understand video by @hjlarry in https://github.com/langgenius/dify/pull/9828'
    source_release: https://github.com/langgenius/dify/releases/tag/0.11.1
  - quote: embedding model check when init the knowledge by @JohnJyong in https://github.com/langgenius/dify/pull/10463
    source_release: https://github.com/langgenius/dify/releases/tag/0.11.1
  - quote: 'chore (vanna): update form parameter from ''form'' to ''llm'' in vanna.yaml
      by @BenjaminX in https://github.com/langgenius/dify/pull/10488'
    source_release: https://github.com/langgenius/dify/releases/tag/0.11.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 6-model-support-changes-in-0-11-1
  source_release: dify-2024-11-11-0-11-1-github-184645691-184d9522
  source_type: github_releases
  theme: model-support
  title: 6 Model Support changes in 0.11.1
  type: change
related_changes:
- '[[Changes/Aider/2024-11-01-2-model-support-changes-in-v0-61-0|2 Model Support changes
  in v0.61.0]]'
- '[[Changes/Aider/2024-11-04-4-model-support-changes-in-v0-62-0|4 Model Support changes
  in v0.62.0]]'
- '[[Changes/Dify/2024-11-05-17-model-support-changes-in-0-11-0|17 Model Support changes
  in 0.11.0]]'
source_release: '[[Releases/Dify/dify-2024-11-11-0-11-1-github-184645691-184d9522|dify-2024-11-11-0-11-1-github-184645691-184d9522]]'
source_type: github_releases
theme: model-support
title: 6 Model Support changes in 0.11.1
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Model Support changes in 0.11.1

**Dify** · 2024-11-11 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/0.11.1) · from [[Releases/Dify/dify-2024-11-11-0-11-1-github-184645691-184d9522|v0.11.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **Anthropic Claude-3-5-Haiku Support via OpenRouter**: Get ready to leverage the capabilities of Anthropic’s Claude-3-5-Haiku by @infinitnet in #10331.

> **Video Understanding and CogVideo Tool Support**: Your LLM can now understand videos, and with the new CogVideo tool, process them too! Thanks to @hjlarry in #9828 and #10456.

> feat: add support for anthropic/claude-3-5-haiku through OpenRouter by @infinitnet in https://github.com/langgenius/dify/pull/10331

> feat: support LLM understand video by @hjlarry in https://github.com/langgenius/dify/pull/9828

> embedding model check when init the knowledge by @JohnJyong in https://github.com/langgenius/dify/pull/10463

> chore (vanna): update form parameter from 'form' to 'llm' in vanna.yaml by @BenjaminX in https://github.com/langgenius/dify/pull/10488

Source: https://github.com/langgenius/dify/releases/tag/0.11.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2024-11-11-chore-add-multimodal-send-video-format-to-docker-s-env-by-hjlarry-in-https-githu|chore: add MULTIMODAL_SEND_VIDEO_FORMAT to docker's env]] · Multimodal Input
- [[Changes/Dify/2024-11-11-2-developer-workflow-changes-in-0-11-1|2 Developer Workflow changes in 0.11.1]] · Developer Workflow
- [[Changes/Dify/2024-11-11-chore-ci-bring-back-poetry-cache-to-speed-up-ci-jobs-by-bowenliang123-in-https-g|chore(ci): bring back poetry cache to speed up CI jobs]] · Reliability and Performance
- [[Changes/Dify/2024-11-11-2-safety-and-privacy-changes-in-0-11-1|2 Safety and Privacy changes in 0.11.1]] · Safety and Privacy
- [[Changes/Dify/2024-11-11-update-document-and-segment-word-count-by-johnjyong-in-https-github-com-langgeni|update document and segment word count]] · Files and Data
- [[Changes/Dify/2024-11-11-gitlab-tools-integration-amp-up-your-devops-with-the-integration-of-gitlab-tools|GitLab Tools Integration]] · Apps and Integrations
- [[Changes/Dify/2024-11-11-57-other-changes-in-0-11-1|57 other changes in 0.11.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2024-11-05 · Dify · [[Changes/Dify/2024-11-05-17-model-support-changes-in-0-11-0|17 Model Support changes in 0.11.0]]
- Later: 2024-11-13 · Aider · [[Changes/Aider/2024-11-13-web-command-just-adds-the-page-to-the-chat-without-triggering-an-llm-response|/web command just adds the page to the chat, without triggering an LLM response]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2024-11-11-69b3d0&body=Card%3A%20Changes%2FDify%2F2024-11-11-6-model-support-changes-in-0-11-1.md%0ACard%20ID%3A%20dify-2024-11-11-69b3d0%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F0.11.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->