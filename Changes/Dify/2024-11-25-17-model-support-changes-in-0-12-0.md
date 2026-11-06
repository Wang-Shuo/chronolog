---
card_id: dify-2024-11-25-78128d
date: '2024-11-25'
description: 'Dify · 2024-11-25 · Model Support: 17 changes in v0.12.0 — LLM Node
  now supports directly referencing File and Array File variables in Prompts, unlocking…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 686
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: bbf56b52fe6fe8a2665d9799459f04207ce7355b18da7a6d9d944f32ab49e3c1
product: dify
product_name: Dify
record:
  card_id: dify-2024-11-25-78128d
  comparison: ''
  date: '2024-11-25'
  description: 'Dify — v0.12.0: 17 Model Support changes'
  evidence:
  - quote: LLM Node now supports directly referencing File and Array File variables
      in Prompts, unlocking greater possibilities for developers.
    source_release: https://github.com/langgenius/dify/releases/tag/0.12.0
  - quote: For example, you can upload multiple file variables (such as PDFs and images)
      and have the model collaboratively handle complex tasks, like summarizing report
      content or extracting key data. Multi-file support makes workflow design more
      efficient and seamless!
    source_release: https://github.com/langgenius/dify/releases/tag/0.12.0
  - quote: '> 1. **File Support Scope**: The file types supported by the model may
      be more limited than the types allowed for upload. Be sure to read your model
      provider''s official documentation to ensure that uploaded files can be processed
      correctly.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.12.0
  - quote: '> 2. **Document Handling in Unsupported Models**: If the model does not
      natively support processing document files, you will still need to use the *Document
      Extractor* for extracting content.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.12.0
  - quote: '> 4. **Relation to Vision Features**: File support operates independently
      of the Vision toggle. As long as the model supports Vision capabilities, you
      can use files as input.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.12.0
  - quote: '**OpenAI o1 Streaming Support:** We now support streaming output for OpenAI
      o1-preview and o1-mini, thanks to @laipz8200 in #10890.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.12.0
  - quote: '**JSON Schema for Gemini Models:** Added support for JSON schema integration,
      ensuring smoother alignment with Gemini models, thanks to @hjlarry in #10835.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.12.0
  - quote: 'feat: support json schema for gemini models by @hjlarry in https://github.com/langgenius/dify/pull/10835'
    source_release: https://github.com/langgenius/dify/releases/tag/0.12.0
  - quote: Support streaming output for OpenAI o1-preview and o1-mini by @laipz8200
      in https://github.com/langgenius/dify/pull/10890
    source_release: https://github.com/langgenius/dify/releases/tag/0.12.0
  - quote: Resolve 8475 support rerank model from infinity by @LastHopeOfGPNU in https://github.com/langgenius/dify/pull/10939
    source_release: https://github.com/langgenius/dify/releases/tag/0.12.0
  - quote: 'feat: add gpt-4o-2024-11-20 by @agungbesti in https://github.com/langgenius/dify/pull/10951'
    source_release: https://github.com/langgenius/dify/releases/tag/0.12.0
  - quote: 'chore: Added the new gemini exp-1121 and learnlm-1.5 models by @CXwudi
      in https://github.com/langgenius/dify/pull/10963'
    source_release: https://github.com/langgenius/dify/releases/tag/0.12.0
  - quote: 'feat: Allow using file variables directly in the LLM node and support
      more file types. by @laipz8200 in https://github.com/langgenius/dify/pull/10679'
    source_release: https://github.com/langgenius/dify/releases/tag/0.12.0
  - quote: 'feat: support LLM process document file by @hjlarry in https://github.com/langgenius/dify/pull/10966'
    source_release: https://github.com/langgenius/dify/releases/tag/0.12.0
  - quote: 'Fixing #11005: Incorrect max_tokens in yaml file for AWS Bedrock US Cross
      Region Inference version of 3.5 Sonnet v2 and 3.5 Haiku by @kazuhisa-wada in
      https://github.com/langgenius/dify/pull/11013'
    source_release: https://github.com/langgenius/dify/releases/tag/0.12.0
  - quote: make tool parameters parsing compatible with the response of glm4 model
      in xinference provider when function tool call integerated by @cyflhn in https://github.com/langgenius/dify/pull/11049
    source_release: https://github.com/langgenius/dify/releases/tag/0.12.0
  - quote: 'ISSUE=11042: add tts model in siliconflow by @senseb in https://github.com/langgenius/dify/pull/11043'
    source_release: https://github.com/langgenius/dify/releases/tag/0.12.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 17-model-support-changes-in-0-12-0
  source_release: dify-2024-11-25-0-12-0-github-187239779-b9caba2f
  source_type: github_releases
  theme: model-support
  title: 17 Model Support changes in 0.12.0
  type: change
related_changes:
- '[[Changes/Open WebUI/2024-11-20-3-model-support-changes-in-v0-4-1|3 Model Support
  changes in v0.4.1]]'
- '[[Changes/Aider/2024-11-21-7-model-support-changes-in-v0-64-0|7 Model Support changes
  in v0.64.0]]'
- '[[Changes/Ollama/2024-11-23-marco-o1-https-ollama-com-library-marco-o1-an-open-large-reasoning-model-for-rea|Marco-o1((source
  link) An open large reasoning model…]]'
source_release: '[[Releases/Dify/dify-2024-11-25-0-12-0-github-187239779-b9caba2f|dify-2024-11-25-0-12-0-github-187239779-b9caba2f]]'
source_type: github_releases
theme: model-support
title: 17 Model Support changes in 0.12.0
type: change
---

<!-- chronolog:begin region="header" -->
# 17 Model Support changes in 0.12.0

**Dify** · 2024-11-25 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/0.12.0) · from [[Releases/Dify/dify-2024-11-25-0-12-0-github-187239779-b9caba2f|v0.12.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> LLM Node now supports directly referencing File and Array File variables in Prompts, unlocking greater possibilities for developers.

> For example, you can upload multiple file variables (such as PDFs and images) and have the model collaboratively handle complex tasks, like summarizing report content or extracting key data. Multi-file support makes workflow design more efficient and seamless!

> > 1. **File Support Scope**: The file types supported by the model may be more limited than the types allowed for upload. Be sure to read your model provider's official documentation to ensure that uploaded files can be processed correctly.

> > 2. **Document Handling in Unsupported Models**: If the model does not natively support processing document files, you will still need to use the *Document Extractor* for extracting content.

> > 4. **Relation to Vision Features**: File support operates independently of the Vision toggle. As long as the model supports Vision capabilities, you can use files as input.

> **OpenAI o1 Streaming Support:** We now support streaming output for OpenAI o1-preview and o1-mini, thanks to @laipz8200 in #10890.

> **JSON Schema for Gemini Models:** Added support for JSON schema integration, ensuring smoother alignment with Gemini models, thanks to @hjlarry in #10835.

> feat: support json schema for gemini models by @hjlarry in https://github.com/langgenius/dify/pull/10835

> Support streaming output for OpenAI o1-preview and o1-mini by @laipz8200 in https://github.com/langgenius/dify/pull/10890

> Resolve 8475 support rerank model from infinity by @LastHopeOfGPNU in https://github.com/langgenius/dify/pull/10939

> feat: add gpt-4o-2024-11-20 by @agungbesti in https://github.com/langgenius/dify/pull/10951

> chore: Added the new gemini exp-1121 and learnlm-1.5 models by @CXwudi in https://github.com/langgenius/dify/pull/10963

> feat: Allow using file variables directly in the LLM node and support more file types. by @laipz8200 in https://github.com/langgenius/dify/pull/10679

> feat: support LLM process document file by @hjlarry in https://github.com/langgenius/dify/pull/10966

> Fixing #11005: Incorrect max_tokens in yaml file for AWS Bedrock US Cross Region Inference version of 3.5 Sonnet v2 and 3.5 Haiku by @kazuhisa-wada in https://github.com/langgenius/dify/pull/11013

> make tool parameters parsing compatible with the response of glm4 model in xinference provider when function tool call integerated by @cyflhn in https://github.com/langgenius/dify/pull/11049

> ISSUE=11042: add tts model in siliconflow by @senseb in https://github.com/langgenius/dify/pull/11043

Source: https://github.com/langgenius/dify/releases/tag/0.12.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2024-11-25-feat-add-a-minimal-separator-between-pinned-apps-and-unpinned-apps-in-the-explor|feat: add a minimal separator between pinned apps and unpinned apps in the explore page]] · Apps and Integrations
- [[Changes/Dify/2024-11-25-support-video-proxy-and-ted-embedding-by-taowang1993-in-https-github-com-langgen|Support Video Proxy and TED Embedding]] · Multimodal Input
- [[Changes/Dify/2024-11-25-3-files-and-data-changes-in-0-12-0|3 Files and Data changes in 0.12.0]] · Files and Data
- [[Changes/Dify/2024-11-25-2-account-and-access-changes-in-0-12-0|2 Account and Access changes in 0.12.0]] · Account and Access
- [[Changes/Dify/2024-11-25-performance-optimization-the-weightrerankrunner-logic-has-been-optimized-to-achi|Performance Optimization: The WeightRerankRunner logic has been optimized…]] · Reliability and Performance
- [[Changes/Dify/2024-11-25-style-refactor-fetch-and-context-by-akarachen-in-https-github-com-langgenius-dif|style: refactor fetch and context]] · Context Window
- [[Changes/Dify/2024-11-25-the-new-version-extends-support-for-multi-modal-tasks-for-example-you-can-upload|The new version extends support for multi-modal tasks]] · Voice and Audio
- [[Changes/Dify/2024-11-25-stop-the-service-command-please-execute-in-the-docker-directory|Stop the service，Command, please execute in the docker directory]] · Developer Workflow
- [[Changes/Dify/2024-11-25-feat-add-japanese-translations-for-api-documentation-chat-advanced-chat-completi|feat : Add Japanese translations for API documentation: chat, advanced-chat…]] · Editor Experience
- [[Changes/Dify/2024-11-25-for-instance-you-can-upload-a-pdf-report-and-let-the-agent-automatically-analyze|For instance, you can upload a PDF report and let the Agent automatically analyze…]] · Agent Mode
- [[Changes/Dify/2024-11-25-57-other-changes-in-0-12-0|57 other changes in 0.12.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2024-11-23 · Ollama · [[Changes/Ollama/2024-11-23-marco-o1-https-ollama-com-library-marco-o1-an-open-large-reasoning-model-for-rea|Marco-o1((source link) An open large reasoning model…]]
- Later: 2024-11-26 · Aider · [[Changes/Aider/2024-11-26-added-alias-config-to-define-custom-model-aliases-https-aider-chat-docs-config-m|Added --alias config to define custom model…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2024-11-25-78128d&body=Card%3A%20Changes%2FDify%2F2024-11-25-17-model-support-changes-in-0-12-0.md%0ACard%20ID%3A%20dify-2024-11-25-78128d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F0.12.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->