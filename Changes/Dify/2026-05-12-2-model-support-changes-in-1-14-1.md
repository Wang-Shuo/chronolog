---
card_id: dify-2026-05-12-64cf21
date: '2026-05-12'
description: 'Dify · 2026-05-12 · Model Support: 2 changes in v1.14.1 - Security hardening,
  workflow stability, and cleaner self-hosted deployments — refactor: improve model…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1219
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 97c6d82e70e060d6d959efea957365cb49f37fac2e42b1c23faaae2b7f9ff503
product: dify
product_name: Dify
record:
  card_id: dify-2026-05-12-64cf21
  comparison: ''
  date: '2026-05-12'
  description: 'Dify — v1.14.1 - Security hardening, workflow stability, and cleaner
    self-hosted deployments: 2 Model Support changes'
  evidence:
  - quote: 'refactor: improve model selector search by @lyzno1 in https://github.com/langgenius/dify/pull/35875'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.1
  - quote: 'refactor: rewrite estimate_args_validate using Pydantic v2 models by @Deepam02
      in https://github.com/langgenius/dify/pull/36036'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 2-model-support-changes-in-1-14-1
  source_release: dify-2026-05-12-1-14-1-github-321018473-9e9e1d9e
  source_type: github_releases
  theme: model-support
  title: 2 Model Support changes in 1.14.1
  type: change
related_changes:
- '[[Changes/Cursor/2026-05-11-high-bugbot-spends-more-time-reasoning-reviews-are-more-expensive-and-take-longe|High:
  Bugbot spends more time reasoning]]'
- '[[Changes/Cursor/2026-05-11-custom-describe-in-natural-language-when-bugbot-should-use-default-or-high-effor|Custom:
  Describe in natural language when Bugbot should use default or high effort]]'
- '[[Changes/OpenCode/2026-05-11-2-model-support-changes-in-v1-14-48-1|2 Model Support
  changes in v1.14.48 + 1]]'
source_release: '[[Releases/Dify/dify-2026-05-12-1-14-1-github-321018473-9e9e1d9e|dify-2026-05-12-1-14-1-github-321018473-9e9e1d9e]]'
source_type: github_releases
theme: model-support
title: 2 Model Support changes in 1.14.1
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Model Support changes in 1.14.1

**Dify** · 2026-05-12 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.14.1) · from [[Releases/Dify/dify-2026-05-12-1-14-1-github-321018473-9e9e1d9e|v1.14.1 - Security hardening, workflow stability, and cleaner self-hosted deployments]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> refactor: improve model selector search by @lyzno1 in https://github.com/langgenius/dify/pull/35875

> refactor: rewrite estimate_args_validate using Pydantic v2 models by @Deepam02 in https://github.com/langgenius/dify/pull/36036

Source: https://github.com/langgenius/dify/releases/tag/1.14.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-05-12-2-editor-experience-changes-in-1-14-1|2 Editor Experience changes in 1.14.1]] · Editor Experience
- [[Changes/Dify/2026-05-12-2-enterprise-and-administration-changes-in-1-14-1|2 Enterprise and Administration changes in 1.14.1]] · Enterprise and Administration
- [[Changes/Dify/2026-05-12-document-indexing-skip-empty-documents-before-vector-embedding-and-validate-miss|Document indexing — skip empty documents before vector embedding and validate…]] · Files and Data
- [[Changes/Dify/2026-05-12-refactor-web-migrate-workflow-panel-context-menu-primitive-by-lyzno1-in-https-gi|refactor(web): migrate workflow panel context menu primitive]] · Context Window
- [[Changes/Dify/2026-05-12-accessibility-and-semantics-improved-web-accessibility-removed-unnecessary-data|Accessibility and semantics]] · Accessibility and Localization
- [[Changes/Dify/2026-05-12-audio-and-transcript-behavior-explicitly-resume-audiocontext-and-play-audio-on-f|Audio and transcript behavior]] · Voice and Audio
- [[Changes/Dify/2026-05-12-3-safety-and-privacy-changes-in-1-14-1|3 Safety and Privacy changes in 1.14.1]] · Safety and Privacy
- [[Changes/Dify/2026-05-12-refactor-web-migrate-subscription-create-modal-to-dialog-by-lyzno1-in-https-gith|refactor(web): migrate subscription create modal to dialog]] · Pricing Model
- [[Changes/Dify/2026-05-12-chore-web-refresh-agent-skills-by-hyoban-in-https-github-com-langgenius-dify-pul|chore(web): refresh agent skills]] · Agent Mode
- [[Changes/Dify/2026-05-12-4-apps-and-integrations-changes-in-1-14-1|4 Apps and Integrations changes in 1.14.1]] · Apps and Integrations
- [[Changes/Dify/2026-05-12-human-input-exposed-selected-action-values-for-human-in-the-loop-flows-thanks-bl|Human input — exposed selected action values for Human-in-the-loop flows]] · Automation and Scheduling
- [[Changes/Dify/2026-05-12-refactor-auth-update-oauth-button-and-settings-modal-for-improved-state-manageme|refactor(auth): update OAuth button and settings modal for improved state management…]] · Account and Access
- [[Changes/Dify/2026-05-12-workflow-stability-restored-workflow-version-loading-through-the-backend-api-fix|Workflow stability — restored workflow-version loading through the backend API…]] · Reliability and Performance
- [[Changes/Dify/2026-05-12-8-interface-experience-changes-in-1-14-1|8 Interface Experience changes in 1.14.1]] · Interface Experience
- [[Changes/Dify/2026-05-12-112-other-changes-in-1-14-1|112 other changes in 1.14.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-05-11 · OpenCode · [[Changes/OpenCode/2026-05-11-2-model-support-changes-in-v1-14-48-1|2 Model Support changes in v1.14.48 + 1]]
- Later: 2026-05-12 · Gemini CLI · [[Changes/Gemini CLI/2026-05-12-5-model-support-changes-in-v0-42-0|5 Model Support changes in v0.42.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-05-12-64cf21&body=Card%3A%20Changes%2FDify%2F2026-05-12-2-model-support-changes-in-1-14-1.md%0ACard%20ID%3A%20dify-2026-05-12-64cf21%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.14.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->