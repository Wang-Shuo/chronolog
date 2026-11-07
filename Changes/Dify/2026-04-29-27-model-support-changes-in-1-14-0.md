---
card_id: dify-2026-04-29-2896e3
date: '2026-04-29'
description: 'Dify · 2026-04-29 · Model Support: 27 changes in v1.14.0 — refactor:
  use EnumText for model_type and WorkflowNodeExecution.status by @tmimmanuel in…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1206
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: bba0fdcfeb3665064c5aa1bf7e582a130eac32ed8e48a04b6ac983ffcecec59f
product: dify
product_name: Dify
record:
  card_id: dify-2026-04-29-2896e3
  comparison: ''
  date: '2026-04-29'
  description: 'Dify — v1.14.0: 27 Model Support changes'
  evidence:
  - quote: 'refactor: use EnumText for model_type and WorkflowNodeExecution.status
      by @tmimmanuel in https://github.com/langgenius/dify/pull/34093'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'chore(deps): bump opik from 1.10.45 to 1.10.54 in /api in the llm group
      by @dependabot[bot] in https://github.com/langgenius/dify/pull/34254'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor: use EnumText for model_type in provider models by @tmimmanuel
      in https://github.com/langgenius/dify/pull/34300'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor: model_load_balancing_service and api_tools_manage_service by
      @RenzoMXD in https://github.com/langgenius/dify/pull/34434'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'chore(deps): bump the llm group in /api with 3 updates by @dependabot[bot]
      in https://github.com/langgenius/dify/pull/34583'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor(api): type LLM generator results with TypedDict by @statxc in
      https://github.com/langgenius/dify/pull/34621'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor(api): enforce strict typing on retrieval_model to resolve FIXME
      by @iamPulakesh in https://github.com/langgenius/dify/pull/34614'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor: use sessionmaker in controllers, events, models, and tasks 1
      by @carlos4s in https://github.com/langgenius/dify/pull/34693'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor(api): deduplicate Pydantic models across fields and controllers
      by @corevibe555 in https://github.com/langgenius/dify/pull/34718'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor(api): deduplicate json serialization in AppModelConfig.from_model_config_dict
      by @jonathanchang31 in https://github.com/langgenius/dify/pull/34795'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor(models): replace Any with precise types in Tenant and MCPToo…
      by @corevibe555 in https://github.com/langgenius/dify/pull/34880'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor: replace inline api.model with Pydantic BaseModel in model_config
      by @ai-hpc in https://github.com/langgenius/dify/pull/34930'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor: replace inline api.model with register_schema_models in billing
      by @ai-hpc in https://github.com/langgenius/dify/pull/34928'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor: migrate _model_to_insertion_dict return type to TypedDict by
      @thegdsks in https://github.com/langgenius/dify/pull/34988'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'chore(deps): bump the llm group in /api with 4 updates by @dependabot[bot]
      in https://github.com/langgenius/dify/pull/35019'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'chore(deps): bump weave from 0.52.17 to 0.52.36 in /api in the llm group
      by @dependabot[bot] in https://github.com/langgenius/dify/pull/35038'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor: remove marshal_with and inline api.model from app_import by
      @ai-hpc in https://github.com/langgenius/dify/pull/34934'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor: migrate app site from marshal_with/api.model to Pydantic BaseModel
      by @ai-hpc in https://github.com/langgenius/dify/pull/34933'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor: migrate apikey from marshal_with/api.model to Pydantic BaseModel
      by @ai-hpc in https://github.com/langgenius/dify/pull/34932'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor: replace inline api.model response schemas with register_schema_models
      in activate by @ai-hpc in https://github.com/langgenius/dify/pull/34929'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor: replace bare dict with dict[str, Any] in model_manager and …
      by @wdeveloper16 in https://github.com/langgenius/dify/pull/35083'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor: replace bare dict with typed annotations in llm_generator and
      prompt by @dataCenter430 in https://github.com/langgenius/dify/pull/35100'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor: replace bare dict with dict[str, Any] in model provider service
      and core modules by @wdeveloper16 in https://github.com/langgenius/dify/pull/35122'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor: replace bare dict with dict[str, Any] in models, providers,
      extensions, libs, and test utilities by @wdeveloper16 in https://github.com/langgenius/dify/pull/35186'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor(api): migrate console extension endpoint from api.model to BaseModel
      by @ai-hpc in https://github.com/langgenius/dify/pull/35189'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor(api): migrate dataset hit-testing response model to BaseModel
      by @ai-hpc in https://github.com/langgenius/dify/pull/35192'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor(api): migrate console conversation variables response model to
      BaseModel by @ai-hpc in https://github.com/langgenius/dify/pull/35193'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 27-model-support-changes-in-1-14-0
  source_release: dify-2026-04-29-1-14-0-github-314986233-63073e86
  source_type: github_releases
  theme: model-support
  title: 27 Model Support changes in 1.14.0
  type: change
related_changes:
- '[[Changes/Ollama/2026-04-28-model-recommendations-are-now-updated-without-updating-ollama|Model
  recommendations are now updated without updating Ollama]]'
- '[[Changes/Ollama/2026-04-28-poolside-s-first-open-weight-coding-model-laguna-xs-2-https-ollama-com-library-l|Poolside''s
  first open-weight coding model - Laguna…]]'
- '[[Changes/OpenCode/2026-04-28-2-model-support-changes-in-v1-14-29|2 Model Support
  changes in v1.14.29]]'
source_release: '[[Releases/Dify/dify-2026-04-29-1-14-0-github-314986233-63073e86|dify-2026-04-29-1-14-0-github-314986233-63073e86]]'
source_type: github_releases
theme: model-support
title: 27 Model Support changes in 1.14.0
type: change
---

<!-- chronolog:begin region="header" -->
# 27 Model Support changes in 1.14.0

**Dify** · 2026-04-29 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.14.0) · from [[Releases/Dify/dify-2026-04-29-1-14-0-github-314986233-63073e86|v1.14.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> refactor: use EnumText for model_type and WorkflowNodeExecution.status by @tmimmanuel in https://github.com/langgenius/dify/pull/34093

> chore(deps): bump opik from 1.10.45 to 1.10.54 in /api in the llm group by @dependabot[bot] in https://github.com/langgenius/dify/pull/34254

> refactor: use EnumText for model_type in provider models by @tmimmanuel in https://github.com/langgenius/dify/pull/34300

> refactor: model_load_balancing_service and api_tools_manage_service by @RenzoMXD in https://github.com/langgenius/dify/pull/34434

> chore(deps): bump the llm group in /api with 3 updates by @dependabot[bot] in https://github.com/langgenius/dify/pull/34583

> refactor(api): type LLM generator results with TypedDict by @statxc in https://github.com/langgenius/dify/pull/34621

> refactor(api): enforce strict typing on retrieval_model to resolve FIXME by @iamPulakesh in https://github.com/langgenius/dify/pull/34614

> refactor: use sessionmaker in controllers, events, models, and tasks 1 by @carlos4s in https://github.com/langgenius/dify/pull/34693

> refactor(api): deduplicate Pydantic models across fields and controllers by @corevibe555 in https://github.com/langgenius/dify/pull/34718

> refactor(api): deduplicate json serialization in AppModelConfig.from_model_config_dict by @jonathanchang31 in https://github.com/langgenius/dify/pull/34795

> refactor(models): replace Any with precise types in Tenant and MCPToo… by @corevibe555 in https://github.com/langgenius/dify/pull/34880

> refactor: replace inline api.model with Pydantic BaseModel in model_config by @ai-hpc in https://github.com/langgenius/dify/pull/34930

> refactor: replace inline api.model with register_schema_models in billing by @ai-hpc in https://github.com/langgenius/dify/pull/34928

> refactor: migrate _model_to_insertion_dict return type to TypedDict by @thegdsks in https://github.com/langgenius/dify/pull/34988

> chore(deps): bump the llm group in /api with 4 updates by @dependabot[bot] in https://github.com/langgenius/dify/pull/35019

> chore(deps): bump weave from 0.52.17 to 0.52.36 in /api in the llm group by @dependabot[bot] in https://github.com/langgenius/dify/pull/35038

> refactor: remove marshal_with and inline api.model from app_import by @ai-hpc in https://github.com/langgenius/dify/pull/34934

> refactor: migrate app site from marshal_with/api.model to Pydantic BaseModel by @ai-hpc in https://github.com/langgenius/dify/pull/34933

> refactor: migrate apikey from marshal_with/api.model to Pydantic BaseModel by @ai-hpc in https://github.com/langgenius/dify/pull/34932

> refactor: replace inline api.model response schemas with register_schema_models in activate by @ai-hpc in https://github.com/langgenius/dify/pull/34929

> refactor: replace bare dict with dict[str, Any] in model_manager and … by @wdeveloper16 in https://github.com/langgenius/dify/pull/35083

> refactor: replace bare dict with typed annotations in llm_generator and prompt by @dataCenter430 in https://github.com/langgenius/dify/pull/35100

> refactor: replace bare dict with dict[str, Any] in model provider service and core modules by @wdeveloper16 in https://github.com/langgenius/dify/pull/35122

> refactor: replace bare dict with dict[str, Any] in models, providers, extensions, libs, and test utilities by @wdeveloper16 in https://github.com/langgenius/dify/pull/35186

> refactor(api): migrate console extension endpoint from api.model to BaseModel by @ai-hpc in https://github.com/langgenius/dify/pull/35189

> refactor(api): migrate dataset hit-testing response model to BaseModel by @ai-hpc in https://github.com/langgenius/dify/pull/35192

> refactor(api): migrate console conversation variables response model to BaseModel by @ai-hpc in https://github.com/langgenius/dify/pull/35193

Source: https://github.com/langgenius/dify/releases/tag/1.14.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-04-29-13-files-and-data-changes-in-1-14-0|13 Files and Data changes in 1.14.0]] · Files and Data
- [[Changes/Dify/2026-04-29-2-developer-workflow-changes-in-1-14-0|2 Developer Workflow changes in 1.14.0]] · Developer Workflow
- [[Changes/Dify/2026-04-29-10-interface-experience-changes-in-1-14-0|10 Interface Experience changes in 1.14.0]] · Interface Experience
- [[Changes/Dify/2026-04-29-2-accessibility-and-localization-changes-in-1-14-0|2 Accessibility and Localization changes in 1.14.0]] · Accessibility and Localization
- [[Changes/Dify/2026-04-29-6-editor-experience-changes-in-1-14-0|6 Editor Experience changes in 1.14.0]] · Editor Experience
- [[Changes/Dify/2026-04-29-7-pricing-model-changes-in-1-14-0|7 Pricing Model changes in 1.14.0]] · Pricing Model
- [[Changes/Dify/2026-04-29-48-apps-and-integrations-changes-in-1-14-0|48 Apps and Integrations changes in 1.14.0]] · Apps and Integrations
- [[Changes/Dify/2026-04-29-13-collaboration-changes-in-1-14-0|13 Collaboration changes in 1.14.0]] · Collaboration
- [[Changes/Dify/2026-04-29-7-safety-and-privacy-changes-in-1-14-0|7 Safety and Privacy changes in 1.14.0]] · Safety and Privacy
- [[Changes/Dify/2026-04-29-8-account-and-access-changes-in-1-14-0|8 Account and Access changes in 1.14.0]] · Account and Access
- [[Changes/Dify/2026-04-29-2-agent-mode-changes-in-1-14-0|2 Agent Mode changes in 1.14.0]] · Agent Mode
- [[Changes/Dify/2026-04-29-3-automation-and-scheduling-changes-in-1-14-0|3 Automation and Scheduling changes in 1.14.0]] · Automation and Scheduling
- [[Changes/Dify/2026-04-29-2-enterprise-and-administration-changes-in-1-14-0|2 Enterprise and Administration changes in 1.14.0]] · Enterprise and Administration
- [[Changes/Dify/2026-04-29-3-context-window-changes-in-1-14-0|3 Context Window changes in 1.14.0]] · Context Window
- [[Changes/Dify/2026-04-29-3-reliability-and-performance-changes-in-1-14-0|3 Reliability and Performance changes in 1.14.0]] · Reliability and Performance
- [[Changes/Dify/2026-04-29-520-other-changes-in-1-14-0|520 other changes in 1.14.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-04-28 · OpenCode · [[Changes/OpenCode/2026-04-28-2-model-support-changes-in-v1-14-29|2 Model Support changes in v1.14.29]]
- Later: 2026-04-29 · OpenCode · [[Changes/OpenCode/2026-04-29-4-model-support-changes-in-v1-14-30|4 Model Support changes in v1.14.30]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-04-29-2896e3&body=Card%3A%20Changes%2FDify%2F2026-04-29-27-model-support-changes-in-1-14-0.md%0ACard%20ID%3A%20dify-2026-04-29-2896e3%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.14.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->