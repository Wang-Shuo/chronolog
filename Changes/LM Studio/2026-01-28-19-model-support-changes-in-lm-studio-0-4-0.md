---
card_id: lm-studio-2026-01-28-b74f7b
date: '2026-01-28'
description: 'LM Studio · 2026-01-28 · Model Support: 19 changes in LM Studio 0.4.0
  — New icons and placements for Discover, My Models buttons'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1115
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 95cfb2f0f64bbd474d7de58079c54213ddb2c5987fcd7d89f19abf402b65a771
product: lm-studio
product_name: LM Studio
record:
  card_id: lm-studio-2026-01-28-b74f7b
  comparison: ''
  date: '2026-01-28'
  description: 'LM Studio — LM Studio 0.4.0: 19 Model Support changes'
  evidence:
  - quote: New icons and placements for Discover, My Models buttons
    source_release: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.4.0
  - quote: When loading a model, you can now select n_parallel to allow multiple requests
      to be processed in parallel.
    source_release: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.4.0
  - quote: When enabled, instead of queuing requests one by one, the model will process
      up to N requests simultaneously.
    source_release: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.4.0
  - quote: "New \U0001F52D Model Search experience"
    source_release: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.4.0
  - quote: Model format filter preferences persist between app restarts
    source_release: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.4.0
  - quote: Bring back gear button to change load parameters for currently loaded model
    source_release: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.4.0
  - quote: 'New in My Models: Capabilities and Format columns'
    source_release: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.4.0
  - quote: 'Slash commands available: /model, /download, /system-prompt, /help and
      /exit'
    source_release: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.4.0
  - quote: 'New REST API endpoint: `api/v1/models/unload` to unload models'
    source_release: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.4.0
  - quote: 'Breaking change: in `api/v1/models/load` endpoint response, introduced
      in this beta, `model_instance_id` has been renamed to `instance_id`.'
    source_release: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.4.0
  - quote: Display live processing status for each loaded LLM on the Developer page
    source_release: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.4.0
  - quote: Minor fix to overlapping labels in model loader
    source_release: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.4.0
  - quote: Support for EssentialAI's rnj-1 model
    source_release: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.4.0
  - quote: Image validation checks in `v1/chat` and `v1/responses` REST API now run
      without model loading
    source_release: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.4.0
  - quote: Load models on CPU/GPU and serve them, use via `lms` CLI or our APIs
    source_release: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.4.0
  - quote: Support for MistralAI Ministral models (3B, 8B, 13B)
    source_release: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.4.0
  - quote: '`lms get` interactive mode now shows the latest model catalog options'
    source_release: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.4.0
  - quote: 'We''re trying something out: Model search now in its own tab'
    source_release: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.4.0
  - quote: Display model indexing errors as buttons rather than hints
    source_release: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.4.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: lm-studio
  product_name: LM Studio
  slug: 19-model-support-changes-in-lm-studio-0-4-0
  source_release: lm-studio-2026-01-28-0-4-0-75d802d3
  source_type: lmstudio_changelog
  theme: model-support
  title: 19 Model Support changes in LM Studio 0.4.0
  type: change
related_changes:
- '[[Changes/Ollama/2026-01-27-new-ollama-launch-clawdbot-command-for-launching-clawdbot-using-ollama-models|New
  ollama launch clawdbot command for launching Clawdbot using Ollama models]]'
- '[[Changes/Cline/2026-01-28-2-model-support-changes-in-v3-55-0|2 Model Support changes
  in v3.55.0]]'
- '[[Changes/Gemini CLI/2026-01-28-4-model-support-changes-in-v0-26-0|4 Model Support
  changes in v0.26.0]]'
source_release: '[[Releases/LM Studio/lm-studio-2026-01-28-0-4-0-75d802d3|lm-studio-2026-01-28-0-4-0-75d802d3]]'
source_type: lmstudio_changelog
theme: model-support
title: 19 Model Support changes in LM Studio 0.4.0
type: change
---

<!-- chronolog:begin region="header" -->
# 19 Model Support changes in LM Studio 0.4.0

**LM Studio** · 2026-01-28 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.4.0) · from [[Releases/LM Studio/lm-studio-2026-01-28-0-4-0-75d802d3|LM Studio 0.4.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> New icons and placements for Discover, My Models buttons

> When loading a model, you can now select n_parallel to allow multiple requests to be processed in parallel.

> When enabled, instead of queuing requests one by one, the model will process up to N requests simultaneously.

> New 🔭 Model Search experience

> Model format filter preferences persist between app restarts

> Bring back gear button to change load parameters for currently loaded model

> New in My Models: Capabilities and Format columns

> Slash commands available: /model, /download, /system-prompt, /help and /exit

> New REST API endpoint: `api/v1/models/unload` to unload models

> Breaking change: in `api/v1/models/load` endpoint response, introduced in this beta, `model_instance_id` has been renamed to `instance_id`.

> Display live processing status for each loaded LLM on the Developer page

> Minor fix to overlapping labels in model loader

> Support for EssentialAI's rnj-1 model

> Image validation checks in `v1/chat` and `v1/responses` REST API now run without model loading

> Load models on CPU/GPU and serve them, use via `lms` CLI or our APIs

> Support for MistralAI Ministral models (3B, 8B, 13B)

> `lms get` interactive mode now shows the latest model catalog options

> We're trying something out: Model search now in its own tab

> Display model indexing errors as buttons rather than hints

Source: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.4.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/LM Studio/2026-01-28-allow-creating-permission-tokens-without-allowed-mcp-permissions|Allow creating permission tokens without allowed MCP permissions]] · Safety and Privacy
- [[Changes/LM Studio/2026-01-28-bring-back-context-fullness-indicator-and-current-input-token-counter|Bring back context fullness indicator and current input token counter]] · Context Window
- [[Changes/LM Studio/2026-01-28-4-developer-workflow-changes-in-lm-studio-0-4-0|4 Developer Workflow changes in LM Studio 0.4.0]] · Developer Workflow
- [[Changes/LM Studio/2026-01-28-updated-style-for-integrations-panel-and-select|Updated style for Integrations panel and select]] · Apps and Integrations
- [[Changes/LM Studio/2026-01-28-show-release-notes-in-a-dedicated-tab-after-app-updates|Show release notes in a dedicated tab after app updates]] · Editor Experience
- [[Changes/LM Studio/2026-01-28-2-reliability-and-performance-changes-in-lm-studio-0-4-0|2 Reliability and Performance changes in LM Studio 0.4.0]] · Reliability and Performance
- [[Changes/LM Studio/2026-01-28-adds-download-copy-and-reveal-in-working-directory-buttons-to-generated-images-i|Adds download, copy, and reveal in working directory buttons to generated images in chat]] · Image Generation
- [[Changes/LM Studio/2026-01-28-7-interface-experience-changes-in-lm-studio-0-4-0|7 Interface Experience changes in LM Studio 0.4.0]] · Interface Experience
- [[Changes/LM Studio/2026-01-28-improved-pdf-rendering-quality-for-tool-requests-and-responses|Improved PDF rendering quality for tool requests and responses]] · Files and Data
- [[Changes/LM Studio/2026-01-28-41-other-changes-in-lm-studio-0-4-0|41 other changes in LM Studio 0.4.0]] · Other changes
- [[Changes/LM Studio/2026-01-28-introducing-split-view-in-chat-view-two-chats-side-by-side|Introducing Split View in Chat: view two chats side by side]] · Other changes
- [[Changes/LM Studio/2026-01-28-introducing-developer-mode-a-simplification-of-the-previous-developer-power-user|Introducing 🔧 Developer Mode]] · Other changes
- [[Changes/LM Studio/2026-01-28-introducing-llmster-the-lm-studio-daemon|Introducing 'llmster': the LM Studio Daemon!]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-01-28 · Gemini CLI · [[Changes/Gemini CLI/2026-01-28-4-model-support-changes-in-v0-26-0|4 Model Support changes in v0.26.0]]
- Later: 2026-01-28 · OpenCode · [[Changes/OpenCode/2026-01-28-8-model-support-changes-in-v1-1-37|8 Model Support changes in v1.1.37]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20lm-studio-2026-01-28-b74f7b&body=Card%3A%20Changes%2FLM%20Studio%2F2026-01-28-19-model-support-changes-in-lm-studio-0-4-0.md%0ACard%20ID%3A%20lm-studio-2026-01-28-b74f7b%0ASource%3A%20https%3A%2F%2Flmstudio.ai%2Fchangelog%2Flmstudio%2Flmstudio-v0.4.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->