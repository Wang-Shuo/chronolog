---
card_id: anythingllm-2026-08-27-9ed2c2
date: '2026-08-27'
description: 'AnythingLLM · 2026-08-27 · Model Support: 10 changes in AnythingLLM
  v1.16.1 — This gives you more screen real estate for the actual response while still…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1326
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 0886c298a8e2ab64dda1f8fc1776dea90d3c7ea13fbce36916b2b17ebe7d1a05
product: anythingllm
product_name: AnythingLLM
record:
  card_id: anythingllm-2026-08-27-9ed2c2
  comparison: ''
  date: '2026-08-27'
  description: 'AnythingLLM — AnythingLLM v1.16.1: 10 Model Support changes'
  evidence:
  - quote: This gives you more screen real estate for the actual response while still
      keeping the important call stack and thoughts the model produces in an easy-to-read
      format.
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.16.1
  - quote: Recently, we added true abort signals across every supported LLM so that
      when you cancel inference or leave the page, we stop inference to save you on
      compute costs.
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.16.1
  - quote: This uses WinML to load models for your CPU, GPU, or NPU across any Windows
      hardware configuration. It's a great option for hardware configurations we don't
      have explicit support for. Keep in mind that model availability may be limited
      as FoundryLocal is still rolling out. Vision models are **not** available currently.
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.16.1
  - quote: '[GenieX](https://github.com/qualcomm/GenieX) is an open-source inference
      engine built by Qualcomm (previously [NexaAI](https://aihub.qualcomm.com/genai))
      that efficiently runs GGUFs and Qualcomm AI Hub models on NPU for X and X2 Elite
      devices.'
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.16.1
  - quote: AnythingLLM offers fully managed and built-in support by selecting the
      "AnythingLLM GenieX" provider in the dropdown. Both GGUFs and NPU-only models
      can leverage the NPU, giving you the power efficiency and intelligence of both.
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.16.1
  - quote: '[x] Native Foundry Local SDK on Windows (x64/ARM64) - the Foundry provider
      is now fully self-contained and no longer requires a separate Foundry Local
      install, with GPU/NPU-optimized model variants exposed in the catalog'
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.16.1
  - quote: '[x] AWS Bedrock cross-region inference profile support - geo-prefixed
      profile IDs (`us.`, `eu.`, `global.`) now appear in the model dropdown and route
      correctly, plus manual region entry for regions outside the preset list (GovCloud,
      specialized partitions)'
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.16.1
  - quote: '[x] Foundry Local no longer prompts for setup when using the built-in
      runtime, and auto-loads models by capability detection'
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.16.1
  - quote: '[x] Onboarding light mode styling and a redesigned LLM selection UI'
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.16.1
  - quote: '[x] Beacon now renders thinking blocks and markdown formatting correctly
      while streaming, with collapsible thinking and a fix for model detail text overflow'
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.16.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: anythingllm
  product_name: AnythingLLM
  slug: 10-model-support-changes-in-v1-16-1
  source_release: anythingllm-2026-08-27-v1-16-1-github-377971782-c1011544
  source_type: github_releases
  theme: model-support
  title: 10 Model Support changes in v1.16.1
  type: change
related_changes:
- '[[Changes/Ollama/2026-08-26-mlxrunner-avoid-metal-gpu-timeouts-when-loading-models-from-slow-storage|mlxrunner:
  avoid Metal GPU timeouts when loading models from slow storage]]'
- '[[Changes/Superwhisper/2026-08-26-whisper-models-are-now-free-for-everyone|Whisper
  Models are now free for everyone!]]'
- '[[Changes/Z.ai API/2026-08-26-native-visual-capabilities-enable-the-model-to-observe-interfaces-rendering-resu|Native
  visual capabilities enable the model to observe interfaces, rendering…]]'
source_release: '[[Releases/AnythingLLM/anythingllm-2026-08-27-v1-16-1-github-377971782-c1011544|anythingllm-2026-08-27-v1-16-1-github-377971782-c1011544]]'
source_type: github_releases
theme: model-support
title: 10 Model Support changes in v1.16.1
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Model Support changes in v1.16.1

**AnythingLLM** · 2026-08-27 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.16.1) · from [[Releases/AnythingLLM/anythingllm-2026-08-27-v1-16-1-github-377971782-c1011544|AnythingLLM v1.16.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> This gives you more screen real estate for the actual response while still keeping the important call stack and thoughts the model produces in an easy-to-read format.

> Recently, we added true abort signals across every supported LLM so that when you cancel inference or leave the page, we stop inference to save you on compute costs.

> This uses WinML to load models for your CPU, GPU, or NPU across any Windows hardware configuration. It's a great option for hardware configurations we don't have explicit support for. Keep in mind that model availability may be limited as FoundryLocal is still rolling out. Vision models are **not** available currently.

> [GenieX](https://github.com/qualcomm/GenieX) is an open-source inference engine built by Qualcomm (previously [NexaAI](https://aihub.qualcomm.com/genai)) that efficiently runs GGUFs and Qualcomm AI Hub models on NPU for X and X2 Elite devices.

> AnythingLLM offers fully managed and built-in support by selecting the "AnythingLLM GenieX" provider in the dropdown. Both GGUFs and NPU-only models can leverage the NPU, giving you the power efficiency and intelligence of both.

> [x] Native Foundry Local SDK on Windows (x64/ARM64) - the Foundry provider is now fully self-contained and no longer requires a separate Foundry Local install, with GPU/NPU-optimized model variants exposed in the catalog

> [x] AWS Bedrock cross-region inference profile support - geo-prefixed profile IDs (`us.`, `eu.`, `global.`) now appear in the model dropdown and route correctly, plus manual region entry for regions outside the preset list (GovCloud, specialized partitions)

> [x] Foundry Local no longer prompts for setup when using the built-in runtime, and auto-loads models by capability detection

> [x] Onboarding light mode styling and a redesigned LLM selection UI

> [x] Beacon now renders thinking blocks and markdown formatting correctly while streaming, with collapsible thinking and a fix for model detail text overflow

Source: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.16.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/AnythingLLM/2026-08-27-2-agent-mode-changes-in-v1-16-1|2 Agent Mode changes in v1.16.1]] · Agent Mode
- [[Changes/AnythingLLM/2026-08-27-2-image-generation-changes-in-v1-16-1|2 Image Generation changes in v1.16.1]] · Image Generation
- [[Changes/AnythingLLM/2026-08-27-3-context-window-changes-in-v1-16-1|3 Context Window changes in v1.16.1]] · Context Window
- [[Changes/AnythingLLM/2026-08-27-feat-cost-tracking-by-timothycarambat-in-https-github-com-mintplex-labs-anything|Feat/cost tracking]] · Pricing Model
- [[Changes/AnythingLLM/2026-08-27-this-replaces-our-previous-snapdragon-npu-engine-any-previous-models-from-the-ol| This replaces our previous Snapdragon NPU engine]] · Reliability and Performance
- [[Changes/AnythingLLM/2026-08-27-2-collaboration-changes-in-v1-16-1|2 Collaboration changes in v1.16.1]] · Collaboration
- [[Changes/AnythingLLM/2026-08-27-2-interface-experience-changes-in-v1-16-1|2 Interface Experience changes in v1.16.1]] · Interface Experience
- [[Changes/AnythingLLM/2026-08-27-however-this-had-the-unintended-side-effect-of-canceling-inference-when-navigati|However, this had the unintended side effect of canceling inference when navigating…]] · Editor Experience
- [[Changes/AnythingLLM/2026-08-27-3-mobile-and-desktop-changes-in-v1-16-1|3 Mobile and Desktop changes in v1.16.1]] · Mobile and Desktop
- [[Changes/AnythingLLM/2026-08-27-14-other-changes-in-v1-16-1|14 other changes in v1.16.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-08-26 · Z.ai API · [[Changes/Z.ai API/2026-08-26-native-visual-capabilities-enable-the-model-to-observe-interfaces-rendering-resu|Native visual capabilities enable the model to observe interfaces, rendering…]]
- Later: 2026-08-27 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-08-27-4-model-support-changes-in-v1-0-81|4 Model Support changes in v1.0.81]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20anythingllm-2026-08-27-9ed2c2&body=Card%3A%20Changes%2FAnythingLLM%2F2026-08-27-10-model-support-changes-in-v1-16-1.md%0ACard%20ID%3A%20anythingllm-2026-08-27-9ed2c2%0ASource%3A%20https%3A%2F%2Fgithub.com%2FMintplex-Labs%2Fanything-llm%2Freleases%2Ftag%2Fv1.16.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->