---
card_id: dify-2026-07-28-202889
date: '2026-07-28'
description: 'Dify · 2026-07-28 · Model Support: 6 changes in v1.16.1 - Bug Fixes
  and Security Enhancements — > **One-time legacy model type migration for self-hosted…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1296
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 4cbb736adb73423653ba448ac73945b54b49a74188b96728116d24d12d931307
product: dify
product_name: Dify
record:
  card_id: dify-2026-07-28-202889
  comparison: ''
  date: '2026-07-28'
  description: 'Dify — v1.16.1 - Bug Fixes and Security Enhancements: 6 Model Support
    changes'
  evidence:
  - quote: '> **One-time legacy model type migration for self-hosted upgrades**'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: '> This migration is **not included in `flask db upgrade`**. Without it,
      legacy model records can cause model-related API requests to fail with errors,
      preventing affected models from being loaded or used.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: After applying the migration, run the dry-run command again. If it reports
      no additional row updates or deletions, restart the relevant services and verify
      that existing models can be loaded and invoked successfully.
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: 'test: use sqlite3 session in test_model_config_api by @asukaminato0721
      in https://github.com/langgenius/dify/pull/38675'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: 'test: use sqlite3 session in test_llm_quota by @asukaminato0721 in https://github.com/langgenius/dify/pull/38720'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: 'test: use sqlite3 session in test_llm_generator_missing by @asukaminato0721
      in https://github.com/langgenius/dify/pull/38742'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 6-model-support-changes-in-1-16-1
  source_release: dify-2026-07-28-1-16-1-github-360820489-855a9365
  source_type: github_releases
  theme: model-support
  title: 6 Model Support changes in 1.16.1
  type: change
related_changes:
- '[[Changes/Ollama/2026-07-25-quantize-draft-model-output-heads-at-the-requested-type-when-creating-speculativ|Quantize
  draft-model output heads at the requested type when creating…]]'
- '[[Changes/Open WebUI/2026-07-27-39-model-support-changes-in-v0-11-0|39 Model Support
  changes in v0.11.0]]'
- '[[Changes/Cline/2026-07-28-add-support-for-free-cline-models-shown-as-free-in-the-model-picker-with-a-dedic|Add
  support for free Cline models, shown as "(free)" in the model picker…]]'
source_release: '[[Releases/Dify/dify-2026-07-28-1-16-1-github-360820489-855a9365|dify-2026-07-28-1-16-1-github-360820489-855a9365]]'
source_type: github_releases
theme: model-support
title: 6 Model Support changes in 1.16.1
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Model Support changes in 1.16.1

**Dify** · 2026-07-28 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.16.1) · from [[Releases/Dify/dify-2026-07-28-1-16-1-github-360820489-855a9365|v1.16.1 - Bug Fixes and Security Enhancements]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> > **One-time legacy model type migration for self-hosted upgrades**

> > This migration is **not included in `flask db upgrade`**. Without it, legacy model records can cause model-related API requests to fail with errors, preventing affected models from being loaded or used.

> After applying the migration, run the dry-run command again. If it reports no additional row updates or deletions, restart the relevant services and verify that existing models can be loaded and invoked successfully.

> test: use sqlite3 session in test_model_config_api by @asukaminato0721 in https://github.com/langgenius/dify/pull/38675

> test: use sqlite3 session in test_llm_quota by @asukaminato0721 in https://github.com/langgenius/dify/pull/38720

> test: use sqlite3 session in test_llm_generator_missing by @asukaminato0721 in https://github.com/langgenius/dify/pull/38742

Source: https://github.com/langgenius/dify/releases/tag/1.16.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-07-28-11-safety-and-privacy-changes-in-1-16-1|11 Safety and Privacy changes in 1.16.1]] · Safety and Privacy
- [[Changes/Dify/2026-07-28-refactor-agents-simplify-repository-context-by-lyzno1-in-https-github-com-langge|refactor(agents): simplify repository context]] · Context Window
- [[Changes/Dify/2026-07-28-3-files-and-data-changes-in-1-16-1|3 Files and Data changes in 1.16.1]] · Files and Data
- [[Changes/Dify/2026-07-28-3-collaboration-changes-in-1-16-1|3 Collaboration changes in 1.16.1]] · Collaboration
- [[Changes/Dify/2026-07-28-2-accessibility-and-localization-changes-in-1-16-1|2 Accessibility and Localization changes in 1.16.1]] · Accessibility and Localization
- [[Changes/Dify/2026-07-28-10-interface-experience-changes-in-1-16-1|10 Interface Experience changes in 1.16.1]] · Interface Experience
- [[Changes/Dify/2026-07-28-4-developer-workflow-changes-in-1-16-1|4 Developer Workflow changes in 1.16.1]] · Developer Workflow
- [[Changes/Dify/2026-07-28-lightweight-recent-apps-endpoint-new-get-console-api-apps-recent-endpoint-reduce|Lightweight recent apps endpoint]] · Reliability and Performance
- [[Changes/Dify/2026-07-28-feat-web-locate-workflow-nodes-by-node-id-in-the-workflow-editor-by-ruanimal-in|feat(web): locate workflow nodes by node_id in the workflow editor]] · Editor Experience
- [[Changes/Dify/2026-07-28-6-account-and-access-changes-in-1-16-1|6 Account and Access changes in 1.16.1]] · Account and Access
- [[Changes/Dify/2026-07-28-test-use-sqlite-sessions-in-core-memory-by-asukaminato0721-in-https-github-com-l|test: use SQLite sessions in core memory]] · Memory and Personalization
- [[Changes/Dify/2026-07-28-you-can-now-click-a-node-id-in-workflow-run-logs-or-error-messages-to-locate-and|Click a node_id in workflow run logs or error messages to locate and highlight…]] · Files and Data
- [[Changes/Dify/2026-07-28-10-apps-and-integrations-changes-in-1-16-1|10 Apps and Integrations changes in 1.16.1]] · Apps and Integrations
- [[Changes/Dify/2026-07-28-returned-400-instead-of-500-when-file-field-is-missing-from-audio-to-text-endpoi|Returned 400 instead of 500 when file field is missing from audio-to-text…]] · Voice and Audio
- [[Changes/Dify/2026-07-28-24-agent-mode-changes-in-1-16-1|24 Agent Mode changes in 1.16.1]] · Agent Mode
- [[Changes/Dify/2026-07-28-2-pricing-model-changes-in-1-16-1|2 Pricing Model changes in 1.16.1]] · Pricing Model
- [[Changes/Dify/2026-07-28-2-enterprise-and-administration-changes-in-1-16-1|2 Enterprise and Administration changes in 1.16.1]] · Enterprise and Administration
- [[Changes/Dify/2026-07-28-167-other-changes-in-1-16-1|167 other changes in 1.16.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-07-28 · Cline · [[Changes/Cline/2026-07-28-add-support-for-free-cline-models-shown-as-free-in-the-model-picker-with-a-dedic|Add support for free Cline models, shown as "(free)" in the model picker…]]
- Later: 2026-07-28 · Gemini CLI · [[Changes/Gemini CLI/2026-07-28-2-model-support-changes-in-v0-53-0|2 Model Support changes in v0.53.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-07-28-202889&body=Card%3A%20Changes%2FDify%2F2026-07-28-6-model-support-changes-in-1-16-1.md%0ACard%20ID%3A%20dify-2026-07-28-202889%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.16.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->