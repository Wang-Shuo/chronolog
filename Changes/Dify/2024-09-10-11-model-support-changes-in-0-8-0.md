---
card_id: dify-2024-09-10-673a73
date: '2024-09-10'
description: 'Dify · 2024-09-10 · Model Support: 11 changes in v0.8.0 — **Support
  `gpt-4o-2024-08-06` and `json_schema` for Azure OpenAI Service**: Support for the
  latest…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 610
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b45e33faf7060ed4c9f77f7ecf6911febf500ed9ccf1e52d03eae929a5d8e390
product: dify
product_name: Dify
record:
  card_id: dify-2024-09-10-673a73
  comparison: ''
  date: '2024-09-10'
  description: 'Dify — v0.8.0: 11 Model Support changes'
  evidence:
  - quote: '**Support `gpt-4o-2024-08-06` and `json_schema` for Azure OpenAI Service**:
      Support for the latest GPT-4o model and JSON schema for Azure OpenAI by @hjlarry
      in #7648'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: '**Support Oracle Cloud Infrastructure Generative AI Service**: Oracle
      Cloud Infrastructure is now a supported model provider by @tmuife in #7775'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: 'feat: ops trace add llm model by @ZhouhaoJiang in https://github.com/langgenius/dify/pull/7306'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: 'chore: refactor the beichuan model by @hjlarry in https://github.com/langgenius/dify/pull/7953'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: Concurrent calls to the Wenxin model, and the exception problem when obtaining
      the token is fixed by @wochuideng in https://github.com/langgenius/dify/pull/7976
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: 'feat: add gpt-4o-2024-08-06 and json_schema for azure openAI service by
      @hjlarry in https://github.com/langgenius/dify/pull/7648'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: Add OCI(Oracle Cloud Infrastructure) Generative AI Service as a Model Provider
      by @tmuife in https://github.com/langgenius/dify/pull/7775
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: 'feat: support more model types and builtin tools on aws/sagemaker by @ybalbert001
      in https://github.com/langgenius/dify/pull/8061'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: Modify model parameters in Spark LLMs and zhipuai LLMs by @AAEE86 in https://github.com/langgenius/dify/pull/8078
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: 'feat(api/core/model_runtime/entities/defaults.py): Add TOP_K in default
      parameters. by @laipz8200 in https://github.com/langgenius/dify/pull/8167'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: 'chore(api/models): apply ruff reformatting by @bowenliang123 in https://github.com/langgenius/dify/pull/7600'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 11-model-support-changes-in-0-8-0
  source_release: dify-2024-09-10-0-8-0-github-174308904-2a45a31c
  source_type: github_releases
  theme: model-support
  title: 11 Model Support changes in 0.8.0
  type: change
related_changes:
- '[[Changes/OpenHands/2024-09-04-2-model-support-changes-in-0-9-2|2 Model Support
  changes in 0.9.2]]'
- '[[Changes/DeepSeek API/2024-09-05-deepseek-coder-deepseek-chat-upgraded-to-deepseek-v2-5-model|deepseek-coder
  & deepseek-chat Upgraded to DeepSeek V2.5 Model]]'
- '[[Changes/Aider/2024-09-09-3-model-support-changes-in-v0-56-0|3 Model Support changes
  in v0.56.0]]'
source_release: '[[Releases/Dify/dify-2024-09-10-0-8-0-github-174308904-2a45a31c|dify-2024-09-10-0-8-0-github-174308904-2a45a31c]]'
source_type: github_releases
theme: model-support
title: 11 Model Support changes in 0.8.0
type: change
---

<!-- chronolog:begin region="header" -->
# 11 Model Support changes in 0.8.0

**Dify** · 2024-09-10 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/0.8.0) · from [[Releases/Dify/dify-2024-09-10-0-8-0-github-174308904-2a45a31c|v0.8.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **Support `gpt-4o-2024-08-06` and `json_schema` for Azure OpenAI Service**: Support for the latest GPT-4o model and JSON schema for Azure OpenAI by @hjlarry in #7648

> **Support Oracle Cloud Infrastructure Generative AI Service**: Oracle Cloud Infrastructure is now a supported model provider by @tmuife in #7775

> feat: ops trace add llm model by @ZhouhaoJiang in https://github.com/langgenius/dify/pull/7306

> chore: refactor the beichuan model by @hjlarry in https://github.com/langgenius/dify/pull/7953

> Concurrent calls to the Wenxin model, and the exception problem when obtaining the token is fixed by @wochuideng in https://github.com/langgenius/dify/pull/7976

> feat: add gpt-4o-2024-08-06 and json_schema for azure openAI service by @hjlarry in https://github.com/langgenius/dify/pull/7648

> Add OCI(Oracle Cloud Infrastructure) Generative AI Service as a Model Provider by @tmuife in https://github.com/langgenius/dify/pull/7775

> feat: support more model types and builtin tools on aws/sagemaker by @ybalbert001 in https://github.com/langgenius/dify/pull/8061

> Modify model parameters in Spark LLMs and zhipuai LLMs by @AAEE86 in https://github.com/langgenius/dify/pull/8078

> feat(api/core/model_runtime/entities/defaults.py): Add TOP_K in default parameters. by @laipz8200 in https://github.com/langgenius/dify/pull/8167

> chore(api/models): apply ruff reformatting by @bowenliang123 in https://github.com/langgenius/dify/pull/7600

Source: https://github.com/langgenius/dify/releases/tag/0.8.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2024-09-10-refactor-api-core-improve-type-hints-and-apply-ruff-formatter-in-agent-runner-an|refactor(api/core): Improve type hints and apply ruff formatter in agent runner…]] · Agent Mode
- [[Changes/Dify/2024-09-10-2-pricing-model-changes-in-0-8-0|2 Pricing Model changes in 0.8.0]] · Pricing Model
- [[Changes/Dify/2024-09-10-3-voice-and-audio-changes-in-0-8-0|3 Voice and Audio changes in 0.8.0]] · Voice and Audio
- [[Changes/Dify/2024-09-10-nodes-can-now-be-executed-in-parallel-within-a-workflow-greatly-increasing-the-e|Nodes can now be executed in parallel within a workflow, greatly increasing…]] · Reliability and Performance
- [[Changes/Dify/2024-09-10-add-dify-sandbox-health-check-in-docker-compose-yaml-8121-by-hwzhuhao-in-https-g|add dify-sandbox health check in docker-compose.yaml (♯8121)]] · Safety and Privacy
- [[Changes/Dify/2024-09-10-2-developer-workflow-changes-in-0-8-0|2 Developer Workflow changes in 0.8.0]] · Developer Workflow
- [[Changes/Dify/2024-09-10-feat-return-page-number-of-pdf-documents-upon-retrieval-by-jasonkang14-in-https|feat: return page number of pdf documents upon retrieval]] · Files and Data
- [[Changes/Dify/2024-09-10-53-other-changes-in-0-8-0|53 other changes in 0.8.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2024-09-09 · Aider · [[Changes/Aider/2024-09-09-3-model-support-changes-in-v0-56-0|3 Model Support changes in v0.56.0]]
- Later: 2024-09-12 · Cline · [[Changes/Cline/2024-09-12-adds-support-for-azure-openai-and-google-gemini-free-for-up-to-15-requests-per-m|Adds support for Azure OpenAI and Google Gemini (free for up to 15 requests per minute!)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2024-09-10-673a73&body=Card%3A%20Changes%2FDify%2F2024-09-10-11-model-support-changes-in-0-8-0.md%0ACard%20ID%3A%20dify-2024-09-10-673a73%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F0.8.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->