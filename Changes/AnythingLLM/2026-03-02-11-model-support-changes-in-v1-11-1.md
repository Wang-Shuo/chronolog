---
card_id: anythingllm-2026-03-02-112a7d
date: '2026-03-02'
description: 'AnythingLLM · 2026-03-02 · Model Support: 11 changes in AnythingLLM
  v1.11.1 — Native tool calling is the best performance and experience for tool calling
  with…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1148
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: cd04c8d2ca2be78bd38ddf802300abb392f15febf092776447de45e7b3cf4c0e
product: anythingllm
product_name: AnythingLLM
record:
  card_id: anythingllm-2026-03-02-112a7d
  comparison: ''
  date: '2026-03-02'
  description: 'AnythingLLM — AnythingLLM v1.11.1: 11 Model Support changes'
  evidence:
  - quote: Native tool calling is the best performance and experience for tool calling
      with your LLM provider and model. If you can enable it, you should.
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.11.1
  - quote: _this only applies to local LLM providers. It has no impact on cloud LLMs
      like OpenAI, Anthropic, or Azure._
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.11.1
  - quote: We have completely overhauled how `@agent` tool calling works. Now, we
      will leverage the new native tool calling abilities of your LLM provider and
      model.
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.11.1
  - quote: Your model will now continue to work until your final response is generated
      or determined to be complete.
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.11.1
  - quote: You will get 100x better responses from even small tool-calling models
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.11.1
  - quote: Most providers do not allow us to probe for if a model supports native
      tool calling.
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.11.1
  - quote: 'The following local LLM providers will automatically support native tool
      calling if your model supports it:'
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.11.1
  - quote: Default Built in LLM Provider (AnythingLLM Default)
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.11.1
  - quote: This can be set via the [`PROVIDER_SUPPORTS_NATIVE_TOOL_CALLING`](/configuration#native-tool-calling-for-llm-providers)
      environment variable.
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.11.1
  - quote: '[Lemonade](https://lemonade-server.ai) by AMD is an [open-source](https://github.com/lemonade-sdk/lemonade)
      local model runtime that optimizes performance and efficiency for local models
      (LLM, ASR, TTS, Image Generation, etc.) for all types of hardware including
      AMD GPUs and NPUs.'
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.11.1
  - quote: We have added first class support so you can use your local models running
      via Lemonade within AnythingLLM for the best application experience on top of
      your local hardware.
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.11.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: anythingllm
  product_name: AnythingLLM
  slug: 11-model-support-changes-in-v1-11-1
  source_release: anythingllm-2026-03-02-v1-11-1-github-292168930-c640f35f
  source_type: github_releases
  theme: model-support
  title: 11 Model Support changes in v1.11.1
  type: change
related_changes:
- '[[Changes/LM Studio/2026-02-27-connect-to-remote-instances-of-lm-studio-load-your-models-and-use-them-as-if-the|Connect
  to remote instances of LM Studio, load your models, and use them as if they…]]'
- '[[Changes/Ollama/2026-02-27-lfm-2-https-ollama-com-library-lfm2-lfm2-is-a-family-of-hybrid-models-designed-f|LFM
  2((source link) LFM2 is a family of hybrid models designed…]]'
- '[[Changes/Open WebUI/2026-03-01-8-model-support-changes-in-v0-8-6|8 Model Support
  changes in v0.8.6]]'
source_release: '[[Releases/AnythingLLM/anythingllm-2026-03-02-v1-11-1-github-292168930-c640f35f|anythingllm-2026-03-02-v1-11-1-github-292168930-c640f35f]]'
source_type: github_releases
theme: model-support
title: 11 Model Support changes in v1.11.1
type: change
---

<!-- chronolog:begin region="header" -->
# 11 Model Support changes in v1.11.1

**AnythingLLM** · 2026-03-02 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.11.1) · from [[Releases/AnythingLLM/anythingllm-2026-03-02-v1-11-1-github-292168930-c640f35f|AnythingLLM v1.11.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Native tool calling is the best performance and experience for tool calling with your LLM provider and model. If you can enable it, you should.

> _this only applies to local LLM providers. It has no impact on cloud LLMs like OpenAI, Anthropic, or Azure._

> We have completely overhauled how `@agent` tool calling works. Now, we will leverage the new native tool calling abilities of your LLM provider and model.

> Your model will now continue to work until your final response is generated or determined to be complete.

> You will get 100x better responses from even small tool-calling models

> Most providers do not allow us to probe for if a model supports native tool calling.

> The following local LLM providers will automatically support native tool calling if your model supports it:

> Default Built in LLM Provider (AnythingLLM Default)

> This can be set via the [`PROVIDER_SUPPORTS_NATIVE_TOOL_CALLING`](https://github.com/Mintplex-Labs/anything-llm/blob/v1.11.1/configuration#native-tool-calling-for-llm-providers) environment variable.

> [Lemonade](https://lemonade-server.ai) by AMD is an [open-source](https://github.com/lemonade-sdk/lemonade) local model runtime that optimizes performance and efficiency for local models (LLM, ASR, TTS, Image Generation, etc.) for all types of hardware including AMD GPUs and NPUs.

> We have added first class support so you can use your local models running via Lemonade within AnythingLLM for the best application experience on top of your local hardware.

Source: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.11.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/AnythingLLM/2026-03-02-lemonade-integration-by-timothycarambat-in-https-github-com-mintplex-labs-anythi|Lemonade integration]] · Apps and Integrations
- [[Changes/AnythingLLM/2026-03-02-2-interface-experience-changes-in-v1-11-1|2 Interface Experience changes in v1.11.1]] · Interface Experience
- [[Changes/AnythingLLM/2026-03-02-you-can-now-run-complex-multi-step-tool-calls-with-your-llm-provider-and-model|Run complex, multi-step tool calls with your LLM provider and model]] · Model Support
- [[Changes/AnythingLLM/2026-03-02-12-other-changes-in-v1-11-1|12 other changes in v1.11.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-03-01 · Open WebUI · [[Changes/Open WebUI/2026-03-01-8-model-support-changes-in-v0-8-6|8 Model Support changes in v0.8.6]]
- Later: 2026-03-02 · Codex CLI · [[Changes/Codex CLI/2026-03-02-4-model-support-changes-in-rust-v0-107-0|4 Model Support changes in rust-v0.107.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20anythingllm-2026-03-02-112a7d&body=Card%3A%20Changes%2FAnythingLLM%2F2026-03-02-11-model-support-changes-in-v1-11-1.md%0ACard%20ID%3A%20anythingllm-2026-03-02-112a7d%0ASource%3A%20https%3A%2F%2Fgithub.com%2FMintplex-Labs%2Fanything-llm%2Freleases%2Ftag%2Fv1.11.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->