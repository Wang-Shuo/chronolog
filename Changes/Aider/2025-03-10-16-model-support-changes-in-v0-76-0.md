---
card_id: aider-2025-03-10-d02527
date: '2025-03-10'
description: 'Aider · 2025-03-10 · Model Support: 16 changes in Aider v0.76.0 — Improved
  support for [thinking/reasoning…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 791
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 1dc20c7be7bfad1ff51d2409183a8209ff05263be79c03fee2423035af861246
product: aider
product_name: Aider
record:
  card_id: aider-2025-03-10-d02527
  comparison: ''
  date: '2025-03-10'
  description: 'Aider — Aider v0.76.0: 16 Model Support changes'
  evidence:
  - quote: 'Improved support for [thinking/reasoning models](https://aider.chat/docs/config/reasoning.html):'
    source_release: https://github.com/Aider-AI/aider/releases/tag/v0.76.0
  - quote: Display thinking/reasoning content from LLMs which return it.
    source_release: https://github.com/Aider-AI/aider/releases/tag/v0.76.0
  - quote: Enhanced handling of reasoning tags to better clean up model responses.
    source_release: https://github.com/Aider-AI/aider/releases/tag/v0.76.0
  - quote: Added deprecation warning for `remove_reasoning` setting, now replaced
      by `reasoning_tag`.
    source_release: https://github.com/Aider-AI/aider/releases/tag/v0.76.0
  - quote: Added [notifications when LLM responses are ready](https://aider.chat/docs/usage/notifications.html)
      with `--notifications` flag.
    source_release: https://github.com/Aider-AI/aider/releases/tag/v0.76.0
  - quote: 'Added/improved support for many models/providers:'
    source_release: https://github.com/Aider-AI/aider/releases/tag/v0.76.0
  - quote: 'Support for DeepSeek V3 free on OpenRouter: `--model openrouter/deepseek/deepseek-chat:free`.'
    source_release: https://github.com/Aider-AI/aider/releases/tag/v0.76.0
  - quote: Added support for Claude 3.7 Sonnet models on OpenRouter, Bedrock and Vertex
      AI.
    source_release: https://github.com/Aider-AI/aider/releases/tag/v0.76.0
  - quote: Updated default model to Claude 3.7 Sonnet on OpenRouter.
    source_release: https://github.com/Aider-AI/aider/releases/tag/v0.76.0
  - quote: Added support for GPT-4.5-preview model.
    source_release: https://github.com/Aider-AI/aider/releases/tag/v0.76.0
  - quote: Added support for Claude 3.7 Sonnet:beta on OpenRouter.
    source_release: https://github.com/Aider-AI/aider/releases/tag/v0.76.0
  - quote: Added support for `openrouter/anthropic/claude-3.7-sonnet`
    source_release: https://github.com/Aider-AI/aider/releases/tag/v0.76.0
  - quote: Improved SSL verification control for model information requests.
    source_release: https://github.com/Aider-AI/aider/releases/tag/v0.76.0
  - quote: Improved empty LLM response handling with clearer warning messages.
    source_release: https://github.com/Aider-AI/aider/releases/tag/v0.76.0
  - quote: Offer to install dependencies for Bedrock and Vertex AI models.
    source_release: https://github.com/Aider-AI/aider/releases/tag/v0.76.0
  - quote: Deprecated model shortcut args (like --4o, --opus) in favor of the --model
      flag.
    source_release: https://github.com/Aider-AI/aider/releases/tag/v0.76.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: aider
  product_name: Aider
  slug: 16-model-support-changes-in-v0-76-0
  source_release: aider-2025-03-10-v0-76-0-github-204781393-e828f532
  source_type: github_releases
  theme: model-support
  title: 16 Model Support changes in v0.76.0
  type: change
related_changes:
- '[[Changes/Cline/2025-03-06-add-new-gemini-models-to-gcp-vertex-thanks-shohei-ihaya-and-claude-models-asksag|Add
  new Gemini models to GCP Vertex (thanks @shohei-ihaya!) and Claude models…]]'
- '[[Changes/Lovable/2025-03-07-addressed-main-regressions-introduced-with-sonnet-3-7-https-lovable-dev-blog-ant|Addressed
  main regressions introduced with Sonnet…]]'
- '[[Changes/OpenHands/2025-03-07-default-version-of-claude-is-now-claude-3-7-sonnet-20250219-by-tofarr-in-https-g|Default
  version of Claude is now claude-3-7-sonnet-20250219]]'
source_release: '[[Releases/Aider/aider-2025-03-10-v0-76-0-github-204781393-e828f532|aider-2025-03-10-v0-76-0-github-204781393-e828f532]]'
source_type: github_releases
theme: model-support
title: 16 Model Support changes in v0.76.0
type: change
---

<!-- chronolog:begin region="header" -->
# 16 Model Support changes in v0.76.0

**Aider** · 2025-03-10 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/Aider-AI/aider/releases/tag/v0.76.0) · from [[Releases/Aider/aider-2025-03-10-v0-76-0-github-204781393-e828f532|Aider v0.76.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Improved support for [thinking/reasoning models](https://aider.chat/docs/config/reasoning.html):

> Display thinking/reasoning content from LLMs which return it.

> Enhanced handling of reasoning tags to better clean up model responses.

> Added deprecation warning for `remove_reasoning` setting, now replaced by `reasoning_tag`.

> Added [notifications when LLM responses are ready](https://aider.chat/docs/usage/notifications.html) with `--notifications` flag.

> Added/improved support for many models/providers:

> Support for DeepSeek V3 free on OpenRouter: `--model openrouter/deepseek/deepseek-chat:free`.

> Added support for Claude 3.7 Sonnet models on OpenRouter, Bedrock and Vertex AI.

> Updated default model to Claude 3.7 Sonnet on OpenRouter.

> Added support for GPT-4.5-preview model.

> Added support for Claude 3.7 Sonnet:beta on OpenRouter.

> Added support for `openrouter/anthropic/claude-3.7-sonnet`

> Improved SSL verification control for model information requests.

> Improved empty LLM response handling with clearer warning messages.

> Offer to install dependencies for Bedrock and Vertex AI models.

> Deprecated model shortcut args (like --4o, --opus) in favor of the --model flag.

Source: https://github.com/Aider-AI/aider/releases/tag/v0.76.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Aider/2025-03-10-https-aider-chat-history-html|(source link)]] · Interface Experience
- [[Changes/Aider/2025-03-10-switch-to-tree-sitter-language-pack-for-tree-sitter-support|Switch to tree-sitter-language-pack for tree sitter support]] · Accessibility and Localization
- [[Changes/Aider/2025-03-10-specify-desktop-notification-command-with-notifications-command|Specify desktop notification command with --notifications-command]] · Mobile and Desktop
- [[Changes/Aider/2025-03-10-7-other-changes-in-v0-76-0|7 other changes in v0.76.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2025-03-07 · OpenHands · [[Changes/OpenHands/2025-03-07-default-version-of-claude-is-now-claude-3-7-sonnet-20250219-by-tofarr-in-https-g|Default version of Claude is now claude-3-7-sonnet-20250219]]
- Later: 2025-03-10 · Cline · [[Changes/Cline/2025-03-10-2-model-support-changes-in-v3-6-9|2 Model Support changes in v3.6.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20aider-2025-03-10-d02527&body=Card%3A%20Changes%2FAider%2F2025-03-10-16-model-support-changes-in-v0-76-0.md%0ACard%20ID%3A%20aider-2025-03-10-d02527%0ASource%3A%20https%3A%2F%2Fgithub.com%2FAider-AI%2Faider%2Freleases%2Ftag%2Fv0.76.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->