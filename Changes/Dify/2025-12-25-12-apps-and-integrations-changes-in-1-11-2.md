---
card_id: dify-2025-12-25-42a6c0
date: '2025-12-25'
description: 'Dify · 2025-12-25 · Apps and Integrations: 12 changes in v1.11.2 — Welcome
  to version 1.11.2! This release sees a significant number of improvements…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2568
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2a3948d74a6d470a87fd4a8c4c74f26d9a7c074414236e0a173566644f4f1de8
product: dify
product_name: Dify
record:
  card_id: dify-2025-12-25-42a6c0
  comparison: ''
  date: '2025-12-25'
  description: 'Dify — v1.11.2: 12 Apps and Integrations changes'
  evidence:
  - quote: 'Welcome to version 1.11.2! This release sees a significant number of improvements,
      especially around testing, fixes, and new integrations to enhance the robustness
      and flexibility of the platform. Here''s the lowdown:'
    source_release: https://github.com/langgenius/dify/releases/tag/1.11.2
  - quote: '**Aliyun SLS Integration**: Workflow execution logging can now leverage
      Aliyun''s Simple Log Service, courtesy of @adongfan. (#28986)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.11.2
  - quote: '> [error] failed to initialize database, got error failed to connect to
      `host=db_postgres user=postgres database=dify_plugin`: hostname resolving error
      (lookup db_postgres on 127.0.0.11:53: server misbehaving)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.11.2
  - quote: '> 2025/11/26 11:37:57 init.go:99: [PANIC]failed to init dify plugin db:
      failed to connect to `host=db_postgres user=postgres database=postgres`: hostname
      resolving error (lookup db_postgres on 127.0.0.11:53: server misbehaving)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.11.2
  - quote: '> panic: [PANIC]failed to init dify plugin db: failed to connect to `host=db_postgres
      user=postgres database=postgres`: hostname resolving error (lookup db_postgres
      on 127.0.0.11:53: server misbehaving)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.11.2
  - quote: 'test: try to use Anthropic Skills to add tests for web/app/components/apps/
      by @lyzno1 in https://github.com/langgenius/dify/pull/29607'
    source_release: https://github.com/langgenius/dify/releases/tag/1.11.2
  - quote: 'feat: add GraphEngine layer node execution hooks by @hieheihei in https://github.com/langgenius/dify/pull/28583'
    source_release: https://github.com/langgenius/dify/releases/tag/1.11.2
  - quote: 'feat: Add Aliyun SLS (Simple Log Service) integration for workflow execution
      logging by @adongfan in https://github.com/langgenius/dify/pull/28986'
    source_release: https://github.com/langgenius/dify/releases/tag/1.11.2
  - quote: 'feat: update RAG recommended plugins hook to accept type parameter by
      @WTW0313 in https://github.com/langgenius/dify/pull/29735'
    source_release: https://github.com/langgenius/dify/releases/tag/1.11.2
  - quote: 'refactor: split changes for api/tests/test_containers_integration_tes…
      by @asukaminato0721 in https://github.com/langgenius/dify/pull/29897'
    source_release: https://github.com/langgenius/dify/releases/tag/1.11.2
  - quote: 'chore: bump plugin daemon image tag to 0.5.2-local by @laipz8200 in https://github.com/langgenius/dify/pull/29993'
    source_release: https://github.com/langgenius/dify/releases/tag/1.11.2
  - quote: 'refactor: nodejs sdk by @lyzno1 in https://github.com/langgenius/dify/pull/30036'
    source_release: https://github.com/langgenius/dify/releases/tag/1.11.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 12-apps-and-integrations-changes-in-1-11-2
  source_release: dify-2025-12-25-1-11-2-github-272776889-1d40e2fa
  source_type: github_releases
  theme: apps-integrations
  title: 12 Apps and Integrations changes in 1.11.2
  type: change
related_changes:
- '[[Changes/Gemini CLI/2025-12-22-3-apps-and-integrations-changes-in-v0-22-0|3 Apps
  and Integrations changes in v0.22.0]]'
- '[[Changes/Lovable/2025-12-23-lovable-chatgpt-app|Lovable ChatGPT app]]'
- '[[Changes/Lovable/2025-12-23-connectors-elevenlabs-perplexity-and-firecrawl|Connectors:
  ElevenLabs, Perplexity, and Firecrawl]]'
source_release: '[[Releases/Dify/dify-2025-12-25-1-11-2-github-272776889-1d40e2fa|dify-2025-12-25-1-11-2-github-272776889-1d40e2fa]]'
source_type: github_releases
theme: apps-integrations
title: 12 Apps and Integrations changes in 1.11.2
type: change
---

<!-- chronolog:begin region="header" -->
# 12 Apps and Integrations changes in 1.11.2

**Dify** · 2025-12-25 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.11.2) · from [[Releases/Dify/dify-2025-12-25-1-11-2-github-272776889-1d40e2fa|v1.11.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Welcome to version 1.11.2! This release sees a significant number of improvements, especially around testing, fixes, and new integrations to enhance the robustness and flexibility of the platform. Here's the lowdown:

> **Aliyun SLS Integration**: Workflow execution logging can now leverage Aliyun's Simple Log Service, courtesy of @adongfan. (#28986)

> > [error] failed to initialize database, got error failed to connect to `host=db_postgres user=postgres database=dify_plugin`: hostname resolving error (lookup db_postgres on 127.0.0.11:53: server misbehaving)

> > 2025/11/26 11:37:57 init.go:99: [PANIC]failed to init dify plugin db: failed to connect to `host=db_postgres user=postgres database=postgres`: hostname resolving error (lookup db_postgres on 127.0.0.11:53: server misbehaving)

> > panic: [PANIC]failed to init dify plugin db: failed to connect to `host=db_postgres user=postgres database=postgres`: hostname resolving error (lookup db_postgres on 127.0.0.11:53: server misbehaving)

> test: try to use Anthropic Skills to add tests for web/app/components/apps/ by @lyzno1 in https://github.com/langgenius/dify/pull/29607

> feat: add GraphEngine layer node execution hooks by @hieheihei in https://github.com/langgenius/dify/pull/28583

> feat: Add Aliyun SLS (Simple Log Service) integration for workflow execution logging by @adongfan in https://github.com/langgenius/dify/pull/28986

> feat: update RAG recommended plugins hook to accept type parameter by @WTW0313 in https://github.com/langgenius/dify/pull/29735

> refactor: split changes for api/tests/test_containers_integration_tes… by @asukaminato0721 in https://github.com/langgenius/dify/pull/29897

> chore: bump plugin daemon image tag to 0.5.2-local by @laipz8200 in https://github.com/langgenius/dify/pull/29993

> refactor: nodejs sdk by @lyzno1 in https://github.com/langgenius/dify/pull/30036

Source: https://github.com/langgenius/dify/releases/tag/1.11.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2025-12-25-feat-show-generate-speed-in-chatbot-by-leslie2046-in-https-github-com-langgenius|feat: show generate speed in chatbot]] · Reliability and Performance
- [[Changes/Dify/2025-12-25-test-add-unit-tests-for-datasetconfig-component-with-comprehensive-coverage-of-r|test: add unit tests for DatasetConfig component with comprehensive coverage…]] · Context Window
- [[Changes/Dify/2025-12-25-2-agent-mode-changes-in-1-11-2|2 Agent Mode changes in 1.11.2]] · Agent Mode
- [[Changes/Dify/2025-12-25-chore-add-apptypeselector-tests-and-improve-clear-button-accessibility-by-lyzno1|chore: add AppTypeSelector tests and improve clear button accessibility]] · Accessibility and Localization
- [[Changes/Dify/2025-12-25-3-pricing-model-changes-in-1-11-2|3 Pricing Model changes in 1.11.2]] · Pricing Model
- [[Changes/Dify/2025-12-25-refactor-create-shared-react-i18next-mock-to-reduce-duplication-by-lyzno1-in-htt|refactor: create shared react-i18next mock to reduce duplication]] · Collaboration
- [[Changes/Dify/2025-12-25-2-developer-workflow-changes-in-1-11-2|2 Developer Workflow changes in 1.11.2]] · Developer Workflow
- [[Changes/Dify/2025-12-25-refactor-split-changes-for-api-controllers-web-audio-py-by-asukaminato0721-in-ht|refactor: split changes for api/controllers/web/audio.py]] · Voice and Audio
- [[Changes/Dify/2025-12-25-2-editor-experience-changes-in-1-11-2|2 Editor Experience changes in 1.11.2]] · Editor Experience
- [[Changes/Dify/2025-12-25-add-file-upload-enabled-check-and-new-i18n-message-by-halogen22-in-https-github|Add file upload enabled check and new i18n message]] · Files and Data
- [[Changes/Dify/2025-12-25-feat-add-type-field-to-pipelinerecommendedplugin-model-add-query-param-type-to-r|feat: Add "type" field to PipelineRecommendedPlugin model]] · Model Support
- [[Changes/Dify/2025-12-25-chore-remove-unused-login-call-from-activation-flow-by-hjlarry-in-https-github-c|chore: remove unused login call from activation flow]] · Account and Access
- [[Changes/Dify/2025-12-25-3-safety-and-privacy-changes-in-1-11-2|3 Safety and Privacy changes in 1.11.2]] · Safety and Privacy
- [[Changes/Dify/2025-12-25-137-other-changes-in-1-11-2|137 other changes in 1.11.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2025-12-23 · Lovable · [[Changes/Lovable/2025-12-23-connectors-elevenlabs-perplexity-and-firecrawl|Connectors: ElevenLabs, Perplexity, and Firecrawl]]
- Later: 2025-12-26 · Replit · [[Changes/Replit/2025-12-26-replit-rewind-2025|Replit Rewind 2025]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2025-12-25-42a6c0&body=Card%3A%20Changes%2FDify%2F2025-12-25-12-apps-and-integrations-changes-in-1-11-2.md%0ACard%20ID%3A%20dify-2025-12-25-42a6c0%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.11.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->