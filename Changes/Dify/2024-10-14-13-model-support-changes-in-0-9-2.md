---
card_id: dify-2024-10-14-613ad2
date: '2024-10-14'
description: 'Dify · 2024-10-14 · Model Support: 13 changes in v0.9.2 — **Model Additions
  and Enhancements:** Added models `qwen2.5-72b` and `llama3.2` for OpenRouter by…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 644
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: fd251a5eadfca1f462acc911c60397428e5d498e76aeeaaea88f85e3e16dc35c
product: dify
product_name: Dify
record:
  card_id: dify-2024-10-14-613ad2
  comparison: ''
  date: '2024-10-14'
  description: 'Dify — v0.9.2: 13 Model Support changes'
  evidence:
  - quote: '**Model Additions and Enhancements:** Added models `qwen2.5-72b` and `llama3.2`
      for OpenRouter by @hwzhuhao in #8956. Also, `O1-mini`, `O1-preview`, and `LlamaGuard`
      models have joined the lineup thanks to contributions from @charli117 and @crazywoola.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: '**Responsive Front-end Updates:** With rerank model verification and error
      logs only in debug mode, your interface just became more practical and informative.
      Thanks, @YIXIAO0 and @hwzhuhao.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: '**API and Logs:** Chat API now reliably retrieves conversation history
      (thanks @xuzuodong), and fixes have been applied to API proxy updates and missing
      model information in LLM spans.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: 'chore: add missing models from Voyage by @CXwudi in https://github.com/langgenius/dify/pull/8950'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: 'chore: sort Gemini models by @CXwudi in https://github.com/langgenius/dify/pull/8951'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: Correct max_tokens for OpenRouter Sonnet 3.5 by @infinitnet in https://github.com/langgenius/dify/pull/9068
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: azure add o1-mini、o1-preview models by @charli117 in https://github.com/langgenius/dify/pull/9088
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: Corrected type annotation to "Any" from "any" all files in "model_providers"
      folder by @ronaksingh27 in https://github.com/langgenius/dify/pull/9135
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: 'improve: Refresh updated_at field of DataSourceOauthBinding model by @sunxiaoguang
      in https://github.com/langgenius/dify/pull/9173'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: 'feat: add allow_llm_to_see_data flag for vanna by @hwzhuhao in https://github.com/langgenius/dify/pull/9156'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: 'feat: add siliconflow custom add model interface by @AAEE86 in https://github.com/langgenius/dify/pull/8745'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: Chore/model icon url by @zxhlyh in https://github.com/langgenius/dify/pull/9218
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: 'Feat: rerank model verification in front end by @YIXIAO0 in https://github.com/langgenius/dify/pull/9271'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 13-model-support-changes-in-0-9-2
  source_release: dify-2024-10-14-0-9-2-github-179747449-3e58ccc7
  source_type: github_releases
  theme: model-support
  title: 13 Model Support changes in 0.9.2
  type: change
related_changes:
- '[[Changes/Gemini/2024-10-09-introducing-imagen-3|Introducing Imagen 3]]'
- '[[Changes/Ollama/2024-10-11-4-model-support-changes-in-v0-3-13|4 Model Support
  changes in v0.3.13]]'
- '[[Changes/ElevenLabs/2024-10-13-model|Model]]'
source_release: '[[Releases/Dify/dify-2024-10-14-0-9-2-github-179747449-3e58ccc7|dify-2024-10-14-0-9-2-github-179747449-3e58ccc7]]'
source_type: github_releases
theme: model-support
title: 13 Model Support changes in 0.9.2
type: change
---

<!-- chronolog:begin region="header" -->
# 13 Model Support changes in 0.9.2

**Dify** · 2024-10-14 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/0.9.2) · from [[Releases/Dify/dify-2024-10-14-0-9-2-github-179747449-3e58ccc7|v0.9.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **Model Additions and Enhancements:** Added models `qwen2.5-72b` and `llama3.2` for OpenRouter by @hwzhuhao in #8956. Also, `O1-mini`, `O1-preview`, and `LlamaGuard` models have joined the lineup thanks to contributions from @charli117 and @crazywoola.

> **Responsive Front-end Updates:** With rerank model verification and error logs only in debug mode, your interface just became more practical and informative. Thanks, @YIXIAO0 and @hwzhuhao.

> **API and Logs:** Chat API now reliably retrieves conversation history (thanks @xuzuodong), and fixes have been applied to API proxy updates and missing model information in LLM spans.

> chore: add missing models from Voyage by @CXwudi in https://github.com/langgenius/dify/pull/8950

> chore: sort Gemini models by @CXwudi in https://github.com/langgenius/dify/pull/8951

> Correct max_tokens for OpenRouter Sonnet 3.5 by @infinitnet in https://github.com/langgenius/dify/pull/9068

> azure add o1-mini、o1-preview models by @charli117 in https://github.com/langgenius/dify/pull/9088

> Corrected type annotation to "Any" from "any" all files in "model_providers" folder by @ronaksingh27 in https://github.com/langgenius/dify/pull/9135

> improve: Refresh updated_at field of DataSourceOauthBinding model by @sunxiaoguang in https://github.com/langgenius/dify/pull/9173

> feat: add allow_llm_to_see_data flag for vanna by @hwzhuhao in https://github.com/langgenius/dify/pull/9156

> feat: add siliconflow custom add model interface by @AAEE86 in https://github.com/langgenius/dify/pull/8745

> Chore/model icon url by @zxhlyh in https://github.com/langgenius/dify/pull/9218

> Feat: rerank model verification in front end by @YIXIAO0 in https://github.com/langgenius/dify/pull/9271

Source: https://github.com/langgenius/dify/releases/tag/0.9.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2024-10-14-miscellaneous-fixes-including-max-token-adjustments-in-openrouter-by-infinitnet|Miscellaneous Fixes: Including max-token adjustments in OpenRouter…]] · Projects and Workspaces
- [[Changes/Dify/2024-10-14-feat-implement-refresh-tokens-by-laipz8200-in-https-github-com-langgenius-dify-p|Feat/implement-refresh-tokens]] · Context Window
- [[Changes/Dify/2024-10-14-2-image-generation-changes-in-0-9-2|2 Image Generation changes in 0.9.2]] · Image Generation
- [[Changes/Dify/2024-10-14-2-reliability-and-performance-changes-in-0-9-2|2 Reliability and Performance changes in 0.9.2]] · Reliability and Performance
- [[Changes/Dify/2024-10-14-prompt-editor-optimization-clearer-and-more-efficient-prompt-editing-with-reset|Prompt Editor Optimization: Clearer and more efficient prompt editing with reset…]] · Editor Experience
- [[Changes/Dify/2024-10-14-2-safety-and-privacy-changes-in-0-9-2|2 Safety and Privacy changes in 0.9.2]] · Safety and Privacy
- [[Changes/Dify/2024-10-14-external-knowledge-and-retrievals-addressing-issues-in-agent-retrieval-and-entry|External Knowledge and Retrievals: Addressing issues in agent retrieval…]] · Agent Mode
- [[Changes/Dify/2024-10-14-2-developer-workflow-changes-in-0-9-2|2 Developer Workflow changes in 0.9.2]] · Developer Workflow
- [[Changes/Dify/2024-10-14-4-apps-and-integrations-changes-in-0-9-2|4 Apps and Integrations changes in 0.9.2]] · Apps and Integrations
- [[Changes/Dify/2024-10-14-66-other-changes-in-0-9-2|66 other changes in 0.9.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2024-10-13 · ElevenLabs · [[Changes/ElevenLabs/2024-10-13-model|Model]]
- Later: 2024-10-17 · Ollama · [[Changes/Ollama/2024-10-17-2-model-support-changes-in-v0-3-14|2 Model Support changes in v0.3.14]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2024-10-14-613ad2&body=Card%3A%20Changes%2FDify%2F2024-10-14-13-model-support-changes-in-0-9-2.md%0ACard%20ID%3A%20dify-2024-10-14-613ad2%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F0.9.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->