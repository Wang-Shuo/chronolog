---
card_id: dify-2024-09-30-a24956
date: '2024-09-30'
description: 'Dify · 2024-09-30 · Model Support: 36 changes in v0.9.0 — **Website
  Crawling**: Now supports **Jina Reader** as additional alternative for website crawling…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 630
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 75b1eb7e6da1f12d703a39a719d4fc18e8f8275a90e6c183f929c0a516c7b592
product: dify
product_name: Dify
record:
  card_id: dify-2024-09-30-a24956
  comparison: ''
  date: '2024-09-30'
  description: 'Dify — v0.9.0: 36 Model Support changes'
  evidence:
  - quote: '**Website Crawling**: Now supports **Jina Reader** as additional alternative
      for website crawling, converting web page URL to LLM-friendly input format.
      Read [Sync Data from Website](https://docs.dify.ai/guides/knowledge-base/sync-from-website#jina-reader)
      for details. (@mapleeit in [#8761](https://github.com/langgenius/dify/pull/8761)).'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: '**Voyage AI**: A new model provider added (thanks to @hwzhuhao in #8747).'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: '**Jamba**: Another new model to expand our capabilities (@longzhihun in
      #8878).'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'New **Nomic embedding model provider** introduced (@yaoice in #8640).'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: '**Support for o1 series models** for OpenRouter (@sinomoe in [#8358](https://github.com/langgenius/dify/pull/8358)).'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: '**DeepSeek-v2.5** added as a model provider for SiliconFlow (@hwzhuhao
      in [#8639](https://github.com/langgenius/dify/pull/8639)).'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: '**Vertex AI Gemini 1.5 002** and experimental models are now supported
      (@hellof20 in [#8767](https://github.com/langgenius/dify/pull/8767)).'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'Corrected **Spark''s LLM token calculation** error for accurate token
      usage (@cherryhuahua in #8755).'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: Update the PerfXCloud provider model list，Update PerfXCloudProvider validate_provider_credentials
      method. by @BingGeX in https://github.com/langgenius/dify/pull/8587
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: add MixtralAI Model by @AAEE86 in https://github.com/langgenius/dify/pull/8517
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: add Qwen custom add model interface by @AAEE86 in https://github.com/langgenius/dify/pull/8565
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: Add Fireworks AI as new model provider by @yaoice in https://github.com/langgenius/dify/pull/8428
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: Add model parameter translation by @AAEE86 in https://github.com/langgenius/dify/pull/8509
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'feat: support o1 series models for openrouter by @sinomoe in https://github.com/langgenius/dify/pull/8358'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'chore: add Gemini newest experimental models (close #7121) by @CXwudi
      in https://github.com/langgenius/dify/pull/8621'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'feat: add qwen2.5 for model provider siliconflow by @hwzhuhao in https://github.com/langgenius/dify/pull/8630'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'feat: add deepseek-v2.5 for model provider siliconflow by @hwzhuhao in
      https://github.com/langgenius/dify/pull/8639'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: add Qwen model translate by @AAEE86 in https://github.com/langgenius/dify/pull/8674
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: Add nomic embedding model provider by @yaoice in https://github.com/langgenius/dify/pull/8640
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'feat: add mixedbread as a new model provider by @hwzhuhao in https://github.com/langgenius/dify/pull/8523'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: Add embedding models in fireworks provider by @yaoice in https://github.com/langgenius/dify/pull/8728
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'feat: add support for Vertex AI Gemini 1.5 002 and experimental models
      by @hellof20 in https://github.com/langgenius/dify/pull/8767'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: Add more models for SiliconFlow by @jackalcooper in https://github.com/langgenius/dify/pull/8779
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'feat: add qwen to add custom model parameters by @AAEE86 in https://github.com/langgenius/dify/pull/8759'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'feat: add stream for Gemini by @AAEE86 in https://github.com/langgenius/dify/pull/8678'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: Add llama3.2 model in fireworks provider by @yaoice in https://github.com/langgenius/dify/pull/8809
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: add more detailed doc for models of qwen series by @wenmengzhou in https://github.com/langgenius/dify/pull/8799
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'chore: massive update of the Gemini models based on latest documentation
      by @CXwudi in https://github.com/langgenius/dify/pull/8822'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'feat: deprecate mistral model for siliconflow by @hwzhuhao in https://github.com/langgenius/dify/pull/8828'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: Add Llama3.2 models in Groq provider by @Howe829 in https://github.com/langgenius/dify/pull/8831
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'feat: add internlm2.5-20b and qwen2.5-coder-7b model by @hwzhuhao in https://github.com/langgenius/dify/pull/8862'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'feat: deprecate gte-Qwen2-7B-instruct embedding model by @hwzhuhao in
      https://github.com/langgenius/dify/pull/8866'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: Add Jamba and Llama3.2 model support by @longzhihun in https://github.com/langgenius/dify/pull/8878
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'docs: add english versions for the files customizable_model_scale_out
      and predefined_model_scale_out by @hwzhuhao in https://github.com/langgenius/dify/pull/8871'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'feat: add voyage ai as a new model provider by @hwzhuhao in https://github.com/langgenius/dify/pull/8747'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'refactor: optimize the calculation of rerank threshold and the logic for
      forbidden characters in model_uid by @hwzhuhao in https://github.com/langgenius/dify/pull/8879'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 36-model-support-changes-in-0-9-0
  source_release: dify-2024-09-30-0-9-0-github-177564351-208577ea
  source_type: github_releases
  theme: model-support
  title: 36 Model Support changes in 0.9.0
  type: change
related_changes:
- "[[Changes/Open WebUI/2024-09-26-o1-max-completion-tokens-issue-resolved-compatibility-issues-with-openai-s-o1-mo|\U0001F527
  O1 Max Completion Tokens Issue]]"
- '[[Changes/OpenHands/2024-09-26-display-full-model-name-in-settings-ui-3900-by-iaavas-in-https-github-com-all-ha|Display
  full model name in Settings UI (♯3900)]]'
- '[[Changes/Aider/2024-09-29-6-model-support-changes-in-v0-58-0|6 Model Support changes
  in v0.58.0]]'
source_release: '[[Releases/Dify/dify-2024-09-30-0-9-0-github-177564351-208577ea|dify-2024-09-30-0-9-0-github-177564351-208577ea]]'
source_type: github_releases
theme: model-support
title: 36 Model Support changes in 0.9.0
type: change
---

<!-- chronolog:begin region="header" -->
# 36 Model Support changes in 0.9.0

**Dify** · 2024-09-30 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/0.9.0) · from [[Releases/Dify/dify-2024-09-30-0-9-0-github-177564351-208577ea|v0.9.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **Website Crawling**: Now supports **Jina Reader** as additional alternative for website crawling, converting web page URL to LLM-friendly input format. Read [Sync Data from Website](https://docs.dify.ai/guides/knowledge-base/sync-from-website#jina-reader) for details. (@mapleeit in [#8761](https://github.com/langgenius/dify/pull/8761)).

> **Voyage AI**: A new model provider added (thanks to @hwzhuhao in #8747).

> **Jamba**: Another new model to expand our capabilities (@longzhihun in #8878).

> New **Nomic embedding model provider** introduced (@yaoice in #8640).

> **Support for o1 series models** for OpenRouter (@sinomoe in [#8358](https://github.com/langgenius/dify/pull/8358)).

> **DeepSeek-v2.5** added as a model provider for SiliconFlow (@hwzhuhao in [#8639](https://github.com/langgenius/dify/pull/8639)).

> **Vertex AI Gemini 1.5 002** and experimental models are now supported (@hellof20 in [#8767](https://github.com/langgenius/dify/pull/8767)).

> Corrected **Spark's LLM token calculation** error for accurate token usage (@cherryhuahua in #8755).

> Update the PerfXCloud provider model list，Update PerfXCloudProvider validate_provider_credentials method. by @BingGeX in https://github.com/langgenius/dify/pull/8587

> add MixtralAI Model by @AAEE86 in https://github.com/langgenius/dify/pull/8517

> add Qwen custom add model interface by @AAEE86 in https://github.com/langgenius/dify/pull/8565

> Add Fireworks AI as new model provider by @yaoice in https://github.com/langgenius/dify/pull/8428

> Add model parameter translation by @AAEE86 in https://github.com/langgenius/dify/pull/8509

> feat: support o1 series models for openrouter by @sinomoe in https://github.com/langgenius/dify/pull/8358

> chore: add Gemini newest experimental models (close #7121) by @CXwudi in https://github.com/langgenius/dify/pull/8621

> feat: add qwen2.5 for model provider siliconflow by @hwzhuhao in https://github.com/langgenius/dify/pull/8630

> feat: add deepseek-v2.5 for model provider siliconflow by @hwzhuhao in https://github.com/langgenius/dify/pull/8639

> add Qwen model translate by @AAEE86 in https://github.com/langgenius/dify/pull/8674

> Add nomic embedding model provider by @yaoice in https://github.com/langgenius/dify/pull/8640

> feat: add mixedbread as a new model provider by @hwzhuhao in https://github.com/langgenius/dify/pull/8523

> Add embedding models in fireworks provider by @yaoice in https://github.com/langgenius/dify/pull/8728

> feat: add support for Vertex AI Gemini 1.5 002 and experimental models by @hellof20 in https://github.com/langgenius/dify/pull/8767

> Add more models for SiliconFlow by @jackalcooper in https://github.com/langgenius/dify/pull/8779

> feat: add qwen to add custom model parameters by @AAEE86 in https://github.com/langgenius/dify/pull/8759

> feat: add stream for Gemini by @AAEE86 in https://github.com/langgenius/dify/pull/8678

> Add llama3.2 model in fireworks provider by @yaoice in https://github.com/langgenius/dify/pull/8809

> add more detailed doc for models of qwen series by @wenmengzhou in https://github.com/langgenius/dify/pull/8799

> chore: massive update of the Gemini models based on latest documentation by @CXwudi in https://github.com/langgenius/dify/pull/8822

> feat: deprecate mistral model for siliconflow by @hwzhuhao in https://github.com/langgenius/dify/pull/8828

> Add Llama3.2 models in Groq provider by @Howe829 in https://github.com/langgenius/dify/pull/8831

> feat: add internlm2.5-20b and qwen2.5-coder-7b model by @hwzhuhao in https://github.com/langgenius/dify/pull/8862

> feat: deprecate gte-Qwen2-7B-instruct embedding model by @hwzhuhao in https://github.com/langgenius/dify/pull/8866

> Add Jamba and Llama3.2 model support by @longzhihun in https://github.com/langgenius/dify/pull/8878

> docs: add english versions for the files customizable_model_scale_out and predefined_model_scale_out by @hwzhuhao in https://github.com/langgenius/dify/pull/8871

> feat: add voyage ai as a new model provider by @hwzhuhao in https://github.com/langgenius/dify/pull/8747

> refactor: optimize the calculation of rerank threshold and the logic for forbidden characters in model_uid by @hwzhuhao in https://github.com/langgenius/dify/pull/8879

Source: https://github.com/langgenius/dify/releases/tag/0.9.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2024-09-30-2-mobile-and-desktop-changes-in-0-9-0|2 Mobile and Desktop changes in 0.9.0]] · Mobile and Desktop
- [[Changes/Dify/2024-09-30-added-english-versions-for-customizable-model-scale-documentation-to-broaden-acc|Added English versions for customizable model scale documentation to broaden…]] · Accessibility and Localization
- [[Changes/Dify/2024-09-30-2-agent-mode-changes-in-0-9-0|2 Agent Mode changes in 0.9.0]] · Agent Mode
- [[Changes/Dify/2024-09-30-2-developer-workflow-changes-in-0-9-0|2 Developer Workflow changes in 0.9.0]] · Developer Workflow
- [[Changes/Dify/2024-09-30-corrected-a-linking-error-in-help-documents-hjlarry-in-8508|Corrected a linking error in help documents (@hjlarry in ♯8508)]] · Files and Data
- [[Changes/Dify/2024-09-30-4-reliability-and-performance-changes-in-0-9-0|4 Reliability and Performance changes in 0.9.0]] · Reliability and Performance
- [[Changes/Dify/2024-09-30-3-apps-and-integrations-changes-in-0-9-0|3 Apps and Integrations changes in 0.9.0]] · Apps and Integrations
- [[Changes/Dify/2024-09-30-stream-for-gemini-now-available-aaee86-in-8678-https-github-com-langgenius-dify|Stream for Gemini now available…]] · Model Support
- [[Changes/Dify/2024-09-30-add-zhipuai-web-search-by-aaee86-in-https-github-com-langgenius-dify-pull-8668|add zhipuai web search]] · Search and Browsing
- [[Changes/Dify/2024-09-30-with-this-release-we-re-truly-showcasing-the-power-of-dify-we-appreciate-your-co|With this release, we’re truly showcasing the power of Dify!]] · Collaboration
- [[Changes/Dify/2024-09-30-58-other-changes-in-0-9-0|58 other changes in 0.9.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2024-09-29 · Aider · [[Changes/Aider/2024-09-29-6-model-support-changes-in-v0-58-0|6 Model Support changes in v0.58.0]]
- Later: 2024-10-02 · Gemini · [[Changes/Gemini/2024-10-02-gemini-1-5-pro-in-gemini-advanced-just-became-more-capable|Gemini 1.5 Pro in Gemini Advanced just became more capable]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2024-09-30-a24956&body=Card%3A%20Changes%2FDify%2F2024-09-30-36-model-support-changes-in-0-9-0.md%0ACard%20ID%3A%20dify-2024-09-30-a24956%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F0.9.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->