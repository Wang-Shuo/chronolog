---
card_id: dify-2025-10-22-eb8fea
date: '2025-10-22'
description: 'Dify · 2025-10-22 · Model Support: 8 changes in v1.9.2 - Sharper, Faster,
  and More Reliable — Structured output now supported during LLM node streaming *(by…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1017
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f99e7d4d894d681d3ab3d221c2a6ed2363f22fdfd043a1fa449f65ff9ebf7801
product: dify
product_name: Dify
record:
  card_id: dify-2025-10-22-eb8fea
  comparison: ''
  date: '2025-10-22'
  description: 'Dify — v1.9.2 - Sharper, Faster, and More Reliable: 8 Model Support
    changes'
  evidence:
  - quote: Structured output now supported during LLM node streaming *(by [@white‑loub](https://github.com/white-loub)
      in [#27089](https://github.com/langgenius/dify/pull/27089))*
    source_release: https://github.com/langgenius/dify/releases/tag/1.9.2
  - quote: App models now track `updated_by` and `updated_at` fields *(by [@liugddx](https://github.com/liugddx)
      in [#26736](https://github.com/langgenius/dify/pull/26736))*
    source_release: https://github.com/langgenius/dify/releases/tag/1.9.2
  - quote: Corrected missing LLM output var descriptions, variable truncation logic,
      and EndUser relationship loading *(by [@hjlarry](https://github.com/hjlarry)
      in [#26648](https://github.com/langgenius/dify/pull/26648), [@hj24](https://github.com/hj24)
      in [#27129](https://github.com/langgenius/dify/pull/27129), [@liugddx](https://github.com/liugddx)
      in [#27162](https://github.com/langgenius/dify/pull/27162))*
    source_release: https://github.com/langgenius/dify/releases/tag/1.9.2
  - quote: support returning structured output when using LLM API non streaming invocation
      by @goofy-z in https://github.com/langgenius/dify/pull/26451
    source_release: https://github.com/langgenius/dify/releases/tag/1.9.2
  - quote: Refactor account models to use SQLAlchemy 2.0 dataclass mapping by @asukaminato0721
      in https://github.com/langgenius/dify/pull/26415
    source_release: https://github.com/langgenius/dify/releases/tag/1.9.2
  - quote: use model_validate by @asukaminato0721 in https://github.com/langgenius/dify/pull/26182
    source_release: https://github.com/langgenius/dify/releases/tag/1.9.2
  - quote: 'feat: add tracking for updated_by and updated_at fields in app models
      by @liugddx in https://github.com/langgenius/dify/pull/26736'
    source_release: https://github.com/langgenius/dify/releases/tag/1.9.2
  - quote: 'feat: Enhance knowledge base node validation by adding checks for embedding
      and reranking models by @WTW0313 in https://github.com/langgenius/dify/pull/27241'
    source_release: https://github.com/langgenius/dify/releases/tag/1.9.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 8-model-support-changes-in-1-9-2
  source_release: dify-2025-10-22-1-9-2-github-255984243-4bd350a7
  source_type: github_releases
  theme: model-support
  title: 8 Model Support changes in 1.9.2
  type: change
related_changes:
- '[[Changes/Open WebUI/2025-10-16-2-model-support-changes-in-v0-6-34|2 Model Support
  changes in v0.6.34]]'
- '[[Changes/GitHub Copilot CLI/2025-10-18-added-list-of-supported-models-as-part-of-copilot-help-config-text|Added
  list of supported models as part of copilot help config text]]'
- '[[Changes/ChatGPT/2025-10-22-we-re-updating-the-model-for-signed-out-users-to-gpt-5-instant-giving-more-peopl|We’re
  updating the model for signed-out users to GPT-5 Instant, giving more people…]]'
source_release: '[[Releases/Dify/dify-2025-10-22-1-9-2-github-255984243-4bd350a7|dify-2025-10-22-1-9-2-github-255984243-4bd350a7]]'
source_type: github_releases
theme: model-support
title: 8 Model Support changes in 1.9.2
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Model Support changes in 1.9.2

**Dify** · 2025-10-22 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.9.2) · from [[Releases/Dify/dify-2025-10-22-1-9-2-github-255984243-4bd350a7|v1.9.2 - Sharper, Faster, and More Reliable]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Structured output now supported during LLM node streaming *(by [@white‑loub](https://github.com/white-loub) in [#27089](https://github.com/langgenius/dify/pull/27089))*

> App models now track `updated_by` and `updated_at` fields *(by [@liugddx](https://github.com/liugddx) in [#26736](https://github.com/langgenius/dify/pull/26736))*

> Corrected missing LLM output var descriptions, variable truncation logic, and EndUser relationship loading *(by [@hjlarry](https://github.com/hjlarry) in [#26648](https://github.com/langgenius/dify/pull/26648), [@hj24](https://github.com/hj24) in [#27129](https://github.com/langgenius/dify/pull/27129), [@liugddx](https://github.com/liugddx) in [#27162](https://github.com/langgenius/dify/pull/27162))*

> support returning structured output when using LLM API non streaming invocation by @goofy-z in https://github.com/langgenius/dify/pull/26451

> Refactor account models to use SQLAlchemy 2.0 dataclass mapping by @asukaminato0721 in https://github.com/langgenius/dify/pull/26415

> use model_validate by @asukaminato0721 in https://github.com/langgenius/dify/pull/26182

> feat: add tracking for updated_by and updated_at fields in app models by @liugddx in https://github.com/langgenius/dify/pull/26736

> feat: Enhance knowledge base node validation by adding checks for embedding and reranking models by @WTW0313 in https://github.com/langgenius/dify/pull/27241

Source: https://github.com/langgenius/dify/releases/tag/1.9.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2025-10-22-4-agent-mode-changes-in-1-9-2|4 Agent Mode changes in 1.9.2]] · Agent Mode
- [[Changes/Dify/2025-10-22-fix-web-app-permission-check-by-douxc-in-https-github-com-langgenius-dify-pull-2|Fix/web app permission check]] · Safety and Privacy
- [[Changes/Dify/2025-10-22-knowledge-pipeline-for-enterprise-by-garfielddai-in-https-github-com-langgenius|knowledge-pipeline-for-enterprise]] · Enterprise and Administration
- [[Changes/Dify/2025-10-22-improve-explicitly-delete-task-redis-key-on-completion-in-appqueuemanager-by-bla|improve: Explicitly delete task Redis key on completion in AppQueueManager]] · Editor Experience
- [[Changes/Dify/2025-10-22-chore-remove-pnpm-build-from-dev-setup-command-by-laipz8200-in-https-github-com|chore: remove pnpm build from dev-setup command]] · Developer Workflow
- [[Changes/Dify/2025-10-22-3-context-window-changes-in-1-9-2|3 Context Window changes in 1.9.2]] · Context Window
- [[Changes/Dify/2025-10-22-3-interface-experience-changes-in-1-9-2|3 Interface Experience changes in 1.9.2]] · Interface Experience
- [[Changes/Dify/2025-10-22-4-account-and-access-changes-in-1-9-2|4 Account and Access changes in 1.9.2]] · Account and Access
- [[Changes/Dify/2025-10-22-3-pricing-model-changes-in-1-9-2|3 Pricing Model changes in 1.9.2]] · Pricing Model
- [[Changes/Dify/2025-10-22-5-reliability-and-performance-changes-in-1-9-2|5 Reliability and Performance changes in 1.9.2]] · Reliability and Performance
- [[Changes/Dify/2025-10-22-12-apps-and-integrations-changes-in-1-9-2|12 Apps and Integrations changes in 1.9.2]] · Apps and Integrations
- [[Changes/Dify/2025-10-22-139-other-changes-in-1-9-2|139 other changes in 1.9.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2025-10-22 · ChatGPT · [[Changes/ChatGPT/2025-10-22-we-re-updating-the-model-for-signed-out-users-to-gpt-5-instant-giving-more-peopl|We’re updating the model for signed-out users to GPT-5 Instant, giving more people…]]
- Later: 2025-10-22 · Gemini CLI · [[Changes/Gemini CLI/2025-10-22-3-model-support-changes-in-v0-10-0|3 Model Support changes in v0.10.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2025-10-22-eb8fea&body=Card%3A%20Changes%2FDify%2F2025-10-22-8-model-support-changes-in-1-9-2.md%0ACard%20ID%3A%20dify-2025-10-22-eb8fea%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.9.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->