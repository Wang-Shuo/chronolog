---
card_id: anythingllm-2026-10-26-32803a
date: '2026-10-26'
description: 'AnythingLLM · 2026-10-26 · Model Support: 6 changes in AnythingLLM v1.19.0
  — <img width="3680" height="2212" alt="AnythingLLM Docker built-in LLM powered by…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1386
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 26b839c8e9957f83025ec07affa0b5052304e6fad65538bce2eba1a8b6b35e1f
product: anythingllm
product_name: AnythingLLM
record:
  card_id: anythingllm-2026-10-26-32803a
  comparison: ''
  date: '2026-10-26'
  description: 'AnythingLLM — AnythingLLM v1.19.0: 6 Model Support changes'
  evidence:
  - quote: <img width="3680" height="2212" alt="AnythingLLM Docker built-in LLM powered
      by Lemonade and llama.cpp" src="https://github.com/user-attachments/assets/410b5784-ca15-4027-a1c4-056d9d5c748e"
      />
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.19.0
  - quote: 'AnythingLLM Docker now has a default local LLM experience right out of
      the box. The same kind of built-in engine that ships with [AnythingLLM Desktop](https://docs.anythingllm.com/setup/llm-configuration/local/built-in)
      can now run **inside the container**: [Lemonade](https://lemonade-server.ai),
      the fully [open-source](https://github.com/lemonade-sdk/lemonade) local inference
      server from AMD, running your models with [llama.cpp](https://github.com/ggml-org/llama.cpp).
      You no longer need to run Ollama, LM Studio or any other inference server next
      to AnythingLLM.'
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.19.0
  - quote: 'When it''s turned on, **Built-in** becomes the default LLM provider during
      onboarding, with three models recommended for your hardware. You can download
      any model from the model table or pull any GGUF model from Hugging Face. It
      works everywhere a provider can be used: the system LLM, workspace and agent
      LLMs, the chat window model picker, and [Model Router](https://docs.anythingllm.com/model-router/setup).'
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.19.0
  - quote: '> **The built-in LLM is off by default.** Turn it on by starting the container
      with `-e ENABLE_BUILT_IN_LLM=true`, and add `--gpus all` (or pass in your AMD
      or Intel GPU devices) for GPU acceleration. See [Built-in LLM for Docker](https://docs.anythingllm.com/installation-docker/built-in-llm)
      for the full setup for each kind of hardware.'
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.19.0
  - quote: Stop sending deprecated sampling and thinking params to Gemini by @shatfield4
      in https://github.com/Mintplex-Labs/anything-llm/pull/6733
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.19.0
  - quote: Built-in LLM for Docker (embedded_lemonade) by @timothycarambat in https://github.com/Mintplex-Labs/anything-llm/pull/6719
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.19.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: anythingllm
  product_name: AnythingLLM
  slug: 6-model-support-changes-in-v1-19-0
  source_release: anythingllm-2026-10-26-v1-19-0-github-422387962-7ad9a2a3
  source_type: github_releases
  theme: model-support
  title: 6 Model Support changes in v1.19.0
  type: change
related_changes:
- '[[Changes/Ollama/2026-10-24-d3-https-ollama-com-library-d3-brings-vllm-semantic-router-s-decision-models-to|d3((source
  link) brings vLLM Semantic Router''s decision models…]]'
- '[[Changes/OpenClaw/2026-10-24-2-model-support-changes-in-v2026-10-7|2 Model Support
  changes in v2026.10.7]]'
- '[[Changes/Open WebUI/2026-10-25-16-model-support-changes-in-v0-12-4|16 Model Support
  changes in v0.12.4]]'
source_release: '[[Releases/AnythingLLM/anythingllm-2026-10-26-v1-19-0-github-422387962-7ad9a2a3|anythingllm-2026-10-26-v1-19-0-github-422387962-7ad9a2a3]]'
source_type: github_releases
theme: model-support
title: 6 Model Support changes in v1.19.0
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Model Support changes in v1.19.0

**AnythingLLM** · 2026-10-26 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.19.0) · from [[Releases/AnythingLLM/anythingllm-2026-10-26-v1-19-0-github-422387962-7ad9a2a3|AnythingLLM v1.19.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> \<img width="3680" height="2212" alt="AnythingLLM Docker built-in LLM powered by Lemonade and llama.cpp" src="https://github.com/user-attachments/assets/410b5784-ca15-4027-a1c4-056d9d5c748e" />

> AnythingLLM Docker now has a default local LLM experience right out of the box. The same kind of built-in engine that ships with [AnythingLLM Desktop](https://docs.anythingllm.com/setup/llm-configuration/local/built-in) can now run **inside the container**: [Lemonade](https://lemonade-server.ai), the fully [open-source](https://github.com/lemonade-sdk/lemonade) local inference server from AMD, running your models with [llama.cpp](https://github.com/ggml-org/llama.cpp). You no longer need to run Ollama, LM Studio or any other inference server next to AnythingLLM.

> When it's turned on, **Built-in** becomes the default LLM provider during onboarding, with three models recommended for your hardware. You can download any model from the model table or pull any GGUF model from Hugging Face. It works everywhere a provider can be used: the system LLM, workspace and agent LLMs, the chat window model picker, and [Model Router](https://docs.anythingllm.com/model-router/setup).

> > **The built-in LLM is off by default.** Turn it on by starting the container with `-e ENABLE_BUILT_IN_LLM=true`, and add `--gpus all` (or pass in your AMD or Intel GPU devices) for GPU acceleration. See [Built-in LLM for Docker](https://docs.anythingllm.com/installation-docker/built-in-llm) for the full setup for each kind of hardware.

> Stop sending deprecated sampling and thinking params to Gemini by @shatfield4 in https://github.com/Mintplex-Labs/anything-llm/pull/6733

> Built-in LLM for Docker (embedded_lemonade) by @timothycarambat in https://github.com/Mintplex-Labs/anything-llm/pull/6719

Source: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.19.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/AnythingLLM/2026-10-26-2-context-window-changes-in-v1-19-0|2 Context Window changes in v1.19.0]] · Context Window
- [[Changes/AnythingLLM/2026-10-26-chore-drop-api-key-fragments-from-web-search-error-messages-by-u00dxk2-in-https|chore: drop API key fragments from web search error messages]] · Search and Browsing
- [[Changes/AnythingLLM/2026-10-26-apply-workspace-model-changes-to-agent-sessions-mid-thread-by-shatfield4-in-http|Apply workspace model changes to agent sessions mid-thread]] · Agent Mode
- [[Changes/AnythingLLM/2026-10-26-support-mov-files-for-transcription-by-shatfield4-in-https-github-com-mintplex-l|Support .mov files for transcription]] · Voice and Audio
- [[Changes/AnythingLLM/2026-10-26-2-files-and-data-changes-in-v1-19-0|2 Files and Data changes in v1.19.0]] · Files and Data
- [[Changes/AnythingLLM/2026-10-26-15-other-changes-in-v1-19-0|15 other changes in v1.19.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-10-25 · Open WebUI · [[Changes/Open WebUI/2026-10-25-16-model-support-changes-in-v0-12-4|16 Model Support changes in v0.12.4]]
- Later: 2026-10-26 · ChatGPT · [[Changes/ChatGPT/2026-10-26-gpt-6-1-terra-is-rolling-out-in-chatgpt-work-and-codex-it-supports-a-range-of-ta|GPT-6.1 Terra]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20anythingllm-2026-10-26-32803a&body=Card%3A%20Changes%2FAnythingLLM%2F2026-10-26-6-model-support-changes-in-v1-19-0.md%0ACard%20ID%3A%20anythingllm-2026-10-26-32803a%0ASource%3A%20https%3A%2F%2Fgithub.com%2FMintplex-Labs%2Fanything-llm%2Freleases%2Ftag%2Fv1.19.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->