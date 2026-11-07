---
card_id: dify-2026-03-17-8cc572
date: '2026-03-17'
description: 'Dify · 2026-03-17 · Model Support: 18 changes in v1.13.1 — Removed GPT-4-specific
  hardcoded behavior from default model selection logic.'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1163
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 134e8fefcb7cd5b244026511adecd2a438b1c948f7c0c7d3c9a8ba8e02216b2a
product: dify
product_name: Dify
record:
  card_id: dify-2026-03-17-8cc572
  comparison: ''
  date: '2026-03-17'
  description: 'Dify — v1.13.1: 18 Model Support changes'
  evidence:
  - quote: Removed GPT-4-specific hardcoded behavior from default model selection
      logic.
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  - quote: 'Added a dedicated Celery queue: `dataset_summary` for LLM-heavy summary
      generation tasks.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  - quote: 'test(web): Added test for model-auth files in header folder by @akashseth-ifp
      in https://github.com/langgenius/dify/pull/32358'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  - quote: 'test(web): add tests for model-provider-page files in header account-…
      by @akashseth-ifp in https://github.com/langgenius/dify/pull/32360'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  - quote: 'test(web): increase test coverage for model-provider-page folder by @akashseth-ifp
      in https://github.com/langgenius/dify/pull/32374'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  - quote: 'refactor(workflow): inject credential/model access ports into LLM nodes
      by @laipz8200 in https://github.com/langgenius/dify/pull/32569'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  - quote: 'refactor: consolidate LLM runtime model state on ModelInstance by @laipz8200
      in https://github.com/langgenius/dify/pull/32746'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  - quote: 'refactor(api): move llm quota deduction to app graph layer by @laipz8200
      in https://github.com/langgenius/dify/pull/32786'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  - quote: 'refactor(api): move model_runtime into dify_graph by @laipz8200 in https://github.com/langgenius/dify/pull/32858'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  - quote: 'refactor(api): add TypedDict definitions to models/model.py by @statxc
      in https://github.com/langgenius/dify/pull/32925'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  - quote: 'chore(deps): bump the llm group in /api with 6 updates by @dependabot[bot]
      in https://github.com/langgenius/dify/pull/33305'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  - quote: 'chore(deps): bump mlflow-skinny from 3.6.0 to 3.10.1 in /api in the llm
      group across 1 directory by @dependabot[bot] in https://github.com/langgenius/dify/pull/33317'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  - quote: 'test: add test for core extension, external_data_tool and llm generator
      by @mahammadasim in https://github.com/langgenius/dify/pull/32468'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  - quote: 'feat: Remove GPT-4 special-casing from default model selection by @laipz8200
      in https://github.com/langgenius/dify/pull/33458'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  - quote: 'refactor: llm decouple code executor module by @fatelei in https://github.com/langgenius/dify/pull/33400'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  - quote: 'chore(deps): bump litellm from 1.82.1 to 1.82.2 in /api in the llm group
      by @dependabot[bot] in https://github.com/langgenius/dify/pull/33480'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  - quote: 'chore(deps): bump the llm group across 1 directory with 2 updates by @dependabot[bot]
      in https://github.com/langgenius/dify/pull/33491'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  - quote: 'refactor(api): replace dict/Mapping with TypedDict in dataset models by
      @statxc in https://github.com/langgenius/dify/pull/33550'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 18-model-support-changes-in-1-13-1
  source_release: dify-2026-03-17-1-13-1-github-297876307-84187197
  source_type: github_releases
  theme: model-support
  title: 18 Model Support changes in 1.13.1
  type: change
related_changes:
- '[[Changes/Descript/2026-03-17-improved-regenerate-model|Improved Regenerate model]]'
- '[[Changes/Descript/2026-03-17-heads-up-for-existing-projects|Heads up for existing
  projects]]'
- '[[Changes/Descript/2026-03-17-updated-the-underlying-model-powering-regenerate-to-improve-how-natural-the-outp|Updated
  the underlying model powering Regenerate to improve how natural the output sounds]]'
source_release: '[[Releases/Dify/dify-2026-03-17-1-13-1-github-297876307-84187197|dify-2026-03-17-1-13-1-github-297876307-84187197]]'
source_type: github_releases
theme: model-support
title: 18 Model Support changes in 1.13.1
type: change
---

<!-- chronolog:begin region="header" -->
# 18 Model Support changes in 1.13.1

**Dify** · 2026-03-17 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.13.1) · from [[Releases/Dify/dify-2026-03-17-1-13-1-github-297876307-84187197|v1.13.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Removed GPT-4-specific hardcoded behavior from default model selection logic.

> Added a dedicated Celery queue: `dataset_summary` for LLM-heavy summary generation tasks.

> test(web): Added test for model-auth files in header folder by @akashseth-ifp in https://github.com/langgenius/dify/pull/32358

> test(web): add tests for model-provider-page files in header account-… by @akashseth-ifp in https://github.com/langgenius/dify/pull/32360

> test(web): increase test coverage for model-provider-page folder by @akashseth-ifp in https://github.com/langgenius/dify/pull/32374

> refactor(workflow): inject credential/model access ports into LLM nodes by @laipz8200 in https://github.com/langgenius/dify/pull/32569

> refactor: consolidate LLM runtime model state on ModelInstance by @laipz8200 in https://github.com/langgenius/dify/pull/32746

> refactor(api): move llm quota deduction to app graph layer by @laipz8200 in https://github.com/langgenius/dify/pull/32786

> refactor(api): move model_runtime into dify_graph by @laipz8200 in https://github.com/langgenius/dify/pull/32858

> refactor(api): add TypedDict definitions to models/model.py by @statxc in https://github.com/langgenius/dify/pull/32925

> chore(deps): bump the llm group in /api with 6 updates by @dependabot[bot] in https://github.com/langgenius/dify/pull/33305

> chore(deps): bump mlflow-skinny from 3.6.0 to 3.10.1 in /api in the llm group across 1 directory by @dependabot[bot] in https://github.com/langgenius/dify/pull/33317

> test: add test for core extension, external_data_tool and llm generator by @mahammadasim in https://github.com/langgenius/dify/pull/32468

> feat: Remove GPT-4 special-casing from default model selection by @laipz8200 in https://github.com/langgenius/dify/pull/33458

> refactor: llm decouple code executor module by @fatelei in https://github.com/langgenius/dify/pull/33400

> chore(deps): bump litellm from 1.82.1 to 1.82.2 in /api in the llm group by @dependabot[bot] in https://github.com/langgenius/dify/pull/33480

> chore(deps): bump the llm group across 1 directory with 2 updates by @dependabot[bot] in https://github.com/langgenius/dify/pull/33491

> refactor(api): replace dict/Mapping with TypedDict in dataset models by @statxc in https://github.com/langgenius/dify/pull/33550

Source: https://github.com/langgenius/dify/releases/tag/1.13.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-03-17-test-add-comprehensive-unit-and-integration-tests-for-billing-components-by-codi|test: add comprehensive unit and integration tests for billing components]] · Pricing Model
- [[Changes/Dify/2026-03-17-refactor-web-split-share-text-generation-and-add-high-coverage-tests-by-codingon|refactor(web): split share text-generation and add high-coverage tests]] · Collaboration
- [[Changes/Dify/2026-03-17-16-files-and-data-changes-in-1-13-1|16 Files and Data changes in 1.13.1]] · Files and Data
- [[Changes/Dify/2026-03-17-3-safety-and-privacy-changes-in-1-13-1|3 Safety and Privacy changes in 1.13.1]] · Safety and Privacy
- [[Changes/Dify/2026-03-17-5-agent-mode-changes-in-1-13-1|5 Agent Mode changes in 1.13.1]] · Agent Mode
- [[Changes/Dify/2026-03-17-2-reliability-and-performance-changes-in-1-13-1|2 Reliability and Performance changes in 1.13.1]] · Reliability and Performance
- [[Changes/Dify/2026-03-17-ci-add-weekly-schedule-for-pip-and-uv-ecosystems-by-asukaminato0721-in-https-git|ci: Add weekly schedule for pip and uv ecosystems]] · Automation and Scheduling
- [[Changes/Dify/2026-03-17-9-context-window-changes-in-1-13-1|9 Context Window changes in 1.13.1]] · Context Window
- [[Changes/Dify/2026-03-17-27-apps-and-integrations-changes-in-1-13-1|27 Apps and Integrations changes in 1.13.1]] · Apps and Integrations
- [[Changes/Dify/2026-03-17-7-interface-experience-changes-in-1-13-1|7 Interface Experience changes in 1.13.1]] · Interface Experience
- [[Changes/Dify/2026-03-17-8-editor-experience-changes-in-1-13-1|8 Editor Experience changes in 1.13.1]] · Editor Experience
- [[Changes/Dify/2026-03-17-4-memory-and-personalization-changes-in-1-13-1|4 Memory and Personalization changes in 1.13.1]] · Memory and Personalization
- [[Changes/Dify/2026-03-17-test-add-integration-tests-for-app-card-operations-list-browsing-and-create-app|test: add integration tests for app card operations, list browsing, and create app flows]] · Search and Browsing
- [[Changes/Dify/2026-03-17-8-developer-workflow-changes-in-1-13-1|8 Developer Workflow changes in 1.13.1]] · Developer Workflow
- [[Changes/Dify/2026-03-17-2-enterprise-and-administration-changes-in-1-13-1|2 Enterprise and Administration changes in 1.13.1]] · Enterprise and Administration
- [[Changes/Dify/2026-03-17-295-other-changes-in-1-13-1|295 other changes in 1.13.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-03-17 · Descript · [[Changes/Descript/2026-03-17-updated-the-underlying-model-powering-regenerate-to-improve-how-natural-the-outp|Updated the underlying model powering Regenerate to improve how natural the output sounds]]
- Later: 2026-03-17 · Gemini CLI · [[Changes/Gemini CLI/2026-03-17-5-model-support-changes-in-v0-34-0|5 Model Support changes in v0.34.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-03-17-8cc572&body=Card%3A%20Changes%2FDify%2F2026-03-17-18-model-support-changes-in-1-13-1.md%0ACard%20ID%3A%20dify-2026-03-17-8cc572%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.13.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->