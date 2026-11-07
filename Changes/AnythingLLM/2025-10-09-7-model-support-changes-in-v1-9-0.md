---
card_id: anythingllm-2025-10-09-fa8563
date: '2025-10-09'
description: 'AnythingLLM · 2025-10-09 · Model Support: 7 changes in AnythingLLM v1.9.0
  — Streams tool calls and responses in real time (all providers, all models)'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1004
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b2fb9e0fc5884853b2e3b1140269870f4f8c3085093900968efc56162a0f0838
product: anythingllm
product_name: AnythingLLM
record:
  card_id: anythingllm-2025-10-09-fa8563
  comparison: ''
  date: '2025-10-09'
  description: 'AnythingLLM — AnythingLLM v1.9.0: 7 Model Support changes'
  evidence:
  - quote: Streams tool calls and responses in real time (all providers, all models)
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.9.0
  - quote: Migrate OpenAI LLM provider to use Responses API by @shatfield4 in https://github.com/Mintplex-Labs/anything-llm/pull/4404
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.9.0
  - quote: Add stream options to Gemini LLM for usage tracking by @angelplusultra
      in https://github.com/Mintplex-Labs/anything-llm/pull/4466
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.9.0
  - quote: Model context limit auto-detection for LM Studio and Ollama LLM Providers
      by @shatfield4 in https://github.com/Mintplex-Labs/anything-llm/pull/4468
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.9.0
  - quote: Sync models from remote for FireworksAI by @timothycarambat in https://github.com/Mintplex-Labs/anything-llm/pull/4475
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.9.0
  - quote: Reimplement Cohere models for basic chat by @timothycarambat in https://github.com/Mintplex-Labs/anything-llm/pull/4489
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.9.0
  - quote: Migrate gemini agents away from `Untooled` by @timothycarambat in https://github.com/Mintplex-Labs/anything-llm/pull/4505
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.9.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: anythingllm
  product_name: AnythingLLM
  slug: 7-model-support-changes-in-v1-9-0
  source_release: anythingllm-2025-10-09-v1-9-0-github-253490461-30425365
  source_type: github_releases
  theme: model-support
  title: 7 Model Support changes in v1.9.0
  type: change
related_changes:
- '[[Changes/Open WebUI/2025-10-07-8-model-support-changes-in-v0-6-33|8 Model Support
  changes in v0.6.33]]'
- '[[Changes/Cline/2025-10-08-update-local-models-docs-remove-emojis-from-docs-by-nickbaumann98-in-https-githu|Update
  local models docs & remove emojis from Docs]]'
- '[[Changes/Gemini CLI/2025-10-08-revert-get-around-the-initial-empty-response-from-gemini-2-5-flash-by-sandytao52|Revert
  "Get around the initial empty response from gemini-2.5-flash]]'
source_release: '[[Releases/AnythingLLM/anythingllm-2025-10-09-v1-9-0-github-253490461-30425365|anythingllm-2025-10-09-v1-9-0-github-253490461-30425365]]'
source_type: github_releases
theme: model-support
title: 7 Model Support changes in v1.9.0
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Model Support changes in v1.9.0

**AnythingLLM** · 2025-10-09 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.9.0) · from [[Releases/AnythingLLM/anythingllm-2025-10-09-v1-9-0-github-253490461-30425365|AnythingLLM v1.9.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Streams tool calls and responses in real time (all providers, all models)

> Migrate OpenAI LLM provider to use Responses API by @shatfield4 in https://github.com/Mintplex-Labs/anything-llm/pull/4404

> Add stream options to Gemini LLM for usage tracking by @angelplusultra in https://github.com/Mintplex-Labs/anything-llm/pull/4466

> Model context limit auto-detection for LM Studio and Ollama LLM Providers by @shatfield4 in https://github.com/Mintplex-Labs/anything-llm/pull/4468

> Sync models from remote for FireworksAI by @timothycarambat in https://github.com/Mintplex-Labs/anything-llm/pull/4475

> Reimplement Cohere models for basic chat by @timothycarambat in https://github.com/Mintplex-Labs/anything-llm/pull/4489

> Migrate gemini agents away from `Untooled` by @timothycarambat in https://github.com/Mintplex-Labs/anything-llm/pull/4505

Source: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.9.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/AnythingLLM/2025-10-09-2-files-and-data-changes-in-v1-9-0|2 Files and Data changes in v1.9.0]] · Files and Data
- [[Changes/AnythingLLM/2025-10-09-video-src-https-github-com-user-attachments-assets-fbbfab37-e1b0-442b-b7d4-277aa|video…]] · Multimodal Input
- [[Changes/AnythingLLM/2025-10-09-agent-system-prompt-passthrough-user-context-awareness|Agent system prompt passthrough + user context awareness]] · Context Window
- [[Changes/AnythingLLM/2025-10-09-10-agent-mode-changes-in-v1-9-0|10 Agent Mode changes in v1.9.0]] · Agent Mode
- [[Changes/AnythingLLM/2025-10-09-2-apps-and-integrations-changes-in-v1-9-0|2 Apps and Integrations changes in v1.9.0]] · Apps and Integrations
- [[Changes/AnythingLLM/2025-10-09-add-support-for-simple-sso-no-login-redirect-config-setting-by-timothycarambat-i|Add support for SIMPLE_SSO_NO_LOGIN_REDIRECT config setting]] · Account and Access
- [[Changes/AnythingLLM/2025-10-09-28-other-changes-in-v1-9-0|28 other changes in v1.9.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2025-10-08 · Gemini CLI · [[Changes/Gemini CLI/2025-10-08-revert-get-around-the-initial-empty-response-from-gemini-2-5-flash-by-sandytao52|Revert "Get around the initial empty response from gemini-2.5-flash]]
- Later: 2025-10-10 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2025-10-10-improved-the-error-handling-in-the-model-picker-when-no-models-are-available-fix|Improved the error handling in the /model picker when no models are available…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20anythingllm-2025-10-09-fa8563&body=Card%3A%20Changes%2FAnythingLLM%2F2025-10-09-7-model-support-changes-in-v1-9-0.md%0ACard%20ID%3A%20anythingllm-2025-10-09-fa8563%0ASource%3A%20https%3A%2F%2Fgithub.com%2FMintplex-Labs%2Fanything-llm%2Freleases%2Ftag%2Fv1.9.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->