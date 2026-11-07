---
card_id: lm-studio-2025-01-30-48ecd3
date: '2025-01-30'
description: 'LM Studio · 2025-01-30 · Model Support: 5 changes in LM Studio 0.3.9
  — CUDA model load crash, "llm_engine_cuda.node. The file cannot be accessed by the
  system"'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 752
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 1087c0917733a1ad40af42481193c10cabf20f34d6549595f549ecdf0e84eb47
product: lm-studio
product_name: LM Studio
record:
  card_id: lm-studio-2025-01-30-48ecd3
  comparison: ''
  date: '2025-01-30'
  description: 'LM Studio — LM Studio 0.3.9: 5 Model Support changes'
  evidence:
  - quote: CUDA model load crash, "llm_engine_cuda.node. The file cannot be accessed
      by the system"
    source_release: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.3.9
  - quote: ROCm garbled model generation
    source_release: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.3.9
  - quote: Works for models that generate content within `` `` tags (like DeepSeek
      R1)
    source_release: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.3.9
  - quote: 'My Models tab refresh: neater model names, and sidebar categories for
      model types'
    source_release: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.3.9
  - quote: 'To see raw model metadata (previously: (i) button), right-click on the
      model name and choose "View Raw Metadata"'
    source_release: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.3.9
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: lm-studio
  product_name: LM Studio
  slug: 5-model-support-changes-in-lm-studio-0-3-9
  source_release: lm-studio-2025-01-30-0-3-9-82c1097f
  source_type: lmstudio_changelog
  theme: model-support
  title: 5 Model Support changes in LM Studio 0.3.9
  type: change
related_changes:
- '[[Changes/Cline/2025-01-30-save-last-used-api-model-when-switching-between-plan-and-act-for-users-that-like|Save
  last used API/model when switching between Plan and Act, for users that like…]]'
- '[[Changes/Gemini/2025-01-30-introducing-gemini-2-0-flash-to-gemini|Introducing
  Gemini 2.0 Flash to Gemini]]'
- '[[Changes/LM Studio/2025-01-30-new-auto-evict-optionally-auto-unload-previously-loaded-api-models-before-loadin|New:
  Auto-Evict - optionally auto-unload previously loaded API models before…]]'
source_release: '[[Releases/LM Studio/lm-studio-2025-01-30-0-3-9-82c1097f|lm-studio-2025-01-30-0-3-9-82c1097f]]'
source_type: lmstudio_changelog
theme: model-support
title: 5 Model Support changes in LM Studio 0.3.9
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Model Support changes in LM Studio 0.3.9

**LM Studio** · 2025-01-30 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.3.9) · from [[Releases/LM Studio/lm-studio-2025-01-30-0-3-9-82c1097f|LM Studio 0.3.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> CUDA model load crash, "llm_engine_cuda.node. The file cannot be accessed by the system"

> ROCm garbled model generation

> Works for models that generate content within `` `` tags (like DeepSeek R1)

> My Models tab refresh: neater model names, and sidebar categories for model types

> To see raw model metadata (previously: (i) button), right-click on the model name and choose "View Raw Metadata"

Source: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.3.9
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/LM Studio/2025-01-30-new-auto-evict-optionally-auto-unload-previously-loaded-api-models-before-loadin|New: Auto-Evict - optionally auto-unload previously loaded API models before…]] · Model Support
- [[Changes/LM Studio/2025-01-30-developer-moved-logging-options-to-the-developer-logs-panel-header-menu|Developer Moved logging options to the Developer Logs panel header (••• menu)]] · Interface Experience
- [[Changes/LM Studio/2025-01-30-for-command-line-use-lms-load-ttl|For command line use: lms load --ttl ]] · Developer Workflow
- [[Changes/LM Studio/2025-01-30-new-ttl-optionally-auto-unload-unused-api-models-after-a-certain-amount-of-time|New: TTL - optionally auto-unload unused API models after a certain amount…]] · Model Support
- [[Changes/LM Studio/2025-01-30-new-added-support-for-downloading-models-from-nested-folders-in-hugging-face-rep|New: Added support for downloading models from nested folders in Hugging Face repositories]] · Model Support
- [[Changes/LM Studio/2025-01-30-new-experimental-api-send-reasoning-content-in-a-separate-field-in-chat-completi|New Experimental API]] · Editor Experience
- [[Changes/LM Studio/2025-01-30-new-kv-cache-quantization-for-mlx-models-requires-mlx-engine-0-3-0|New: KV Cache Quantization for MLX models (requires mlx-engine/0.3.0)]] · Model Support
- [[Changes/LM Studio/2025-01-30-new-add-a-chat-appearance-option-to-auto-expand-newly-added-thinking-ui-blocks|New: Add a Chat Appearance option to auto-expand newly added Thinking UI blocks]] · Other changes
- [[Changes/LM Studio/2025-01-30-new-show-quick-access-to-guardrail-config-when-the-app-gives-an-insufficient-sys|New: Show quick access to guardrail config when the app gives an insufficient system…]] · Other changes
- [[Changes/LM Studio/2025-01-30-new-added-an-option-to-use-lm-studio-s-hugging-face-proxy-this-can-help-users-wh|New: Added an option to use LM Studio's Hugging Face proxy]] · Other changes
- [[Changes/LM Studio/2025-01-30-new-automatically-update-selected-runtime-extension-packs-you-can-turn-this-off|New: Automatically update selected Runtime Extension Packs…]] · Other changes
- [[Changes/LM Studio/2025-01-30-4-other-changes-in-lm-studio-0-3-9|4 other changes in LM Studio 0.3.9]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2025-01-30 · Gemini · [[Changes/Gemini/2025-01-30-introducing-gemini-2-0-flash-to-gemini|Introducing Gemini 2.0 Flash to Gemini]]
- Later: 2025-01-30 · Raycast · [[Changes/Raycast/2025-01-30-6-model-support-changes-in-raycast-macos-v1-1-90-0|6 Model Support changes in Raycast macos-v1 1.90.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20lm-studio-2025-01-30-48ecd3&body=Card%3A%20Changes%2FLM%20Studio%2F2025-01-30-5-model-support-changes-in-lm-studio-0-3-9.md%0ACard%20ID%3A%20lm-studio-2025-01-30-48ecd3%0ASource%3A%20https%3A%2F%2Flmstudio.ai%2Fchangelog%2Flmstudio%2Flmstudio-v0.3.9%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->