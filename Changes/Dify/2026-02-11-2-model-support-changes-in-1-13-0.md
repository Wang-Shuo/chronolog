---
card_id: dify-2026-02-11-c3c359
date: '2026-02-11'
description: 'Dify · 2026-02-11 · Model Support: 2 changes in 1.13.0 - Human-in-the-Loop
  and Workflow Execution Upgrades — Added migration-time deduplication and a unique…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1129
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b3f86991d6e9af2167781924517b6b2ee0d089968b3d2354c9b4f447f12142f9
product: dify
product_name: Dify
record:
  card_id: dify-2026-02-11-c3c359
  comparison: ''
  date: '2026-02-11'
  description: 'Dify — 1.13.0 - Human-in-the-Loop and Workflow Execution Upgrades:
    2 Model Support changes'
  evidence:
  - quote: Added migration-time deduplication and a unique constraint for tenant default
      models to prevent duplicate default model records.
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.0
  - quote: 'refactor(api): replace reqparse with Pydantic models in trial.py by @Sean-Kenneth-Doherty
      in https://github.com/langgenius/dify/pull/31789'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 2-model-support-changes-in-1-13-0
  source_release: dify-2026-02-11-1-13-0-github-285073967-47691626
  source_type: github_releases
  theme: model-support
  title: 2 Model Support changes in 1.13.0
  type: change
related_changes:
- '[[Changes/Gemini CLI/2026-02-10-docs-document-gemini-cli-home-environment-variable-by-adamfweidman-in-https-gith|docs:
  document GEMINI_CLI_HOME environment variable]]'
- '[[Changes/OpenCode/2026-02-10-6-model-support-changes-in-v1-1-54|6 Model Support
  changes in v1.1.54]]'
- '[[Changes/Codex CLI/2026-02-11-15-model-support-changes-in-rust-v0-99-0|15 Model
  Support changes in rust-v0.99.0]]'
source_release: '[[Releases/Dify/dify-2026-02-11-1-13-0-github-285073967-47691626|dify-2026-02-11-1-13-0-github-285073967-47691626]]'
source_type: github_releases
theme: model-support
title: 2 Model Support changes in 1.13.0
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Model Support changes in 1.13.0

**Dify** · 2026-02-11 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.13.0) · from [[Releases/Dify/dify-2026-02-11-1-13-0-github-285073967-47691626|1.13.0 - Human-in-the-Loop and Workflow Execution Upgrades]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added migration-time deduplication and a unique constraint for tenant default models to prevent duplicate default model records.

> refactor(api): replace reqparse with Pydantic models in trial.py by @Sean-Kenneth-Doherty in https://github.com/langgenius/dify/pull/31789

Source: https://github.com/langgenius/dify/releases/tag/1.13.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-02-11-3-reliability-and-performance-changes-in-1-13-0|3 Reliability and Performance changes in 1.13.0]] · Reliability and Performance
- [[Changes/Dify/2026-02-11-10-apps-and-integrations-changes-in-1-13-0|10 Apps and Integrations changes in 1.13.0]] · Apps and Integrations
- [[Changes/Dify/2026-02-11-flexible-delivery-methods-human-input-forms-can-be-delivered-via-webapp-or-email|Flexible Delivery Methods: Human input forms can be delivered…]] · Agent Mode
- [[Changes/Dify/2026-02-11-to-support-the-stateful-pause-resume-mechanism-required-by-hitl-and-provide-even|To support the stateful pause/resume mechanism required by HITL and provide…]] · Pricing Model
- [[Changes/Dify/2026-02-11-review-edit-the-node-generates-a-ui-where-humans-can-review-ai-outputs-and-modif|Review & Edit: The node generates a UI where humans can review AI outputs…]] · Editor Experience
- [[Changes/Dify/2026-02-11-please-use-the-following-command-instead-for-details-please-read-this-https-gith| Please use the following command instead]] · Developer Workflow
- [[Changes/Dify/2026-02-11-2-files-and-data-changes-in-1-13-0|2 Files and Data changes in 1.13.0]] · Files and Data
- [[Changes/Dify/2026-02-11-added-dutch-nl-nl-language-support-across-backend-language-mapping-and-web-local|Added Dutch (nl-NL) language support across backend language mapping and web…]] · Accessibility and Localization
- [[Changes/Dify/2026-02-11-2-safety-and-privacy-changes-in-1-13-0|2 Safety and Privacy changes in 1.13.0]] · Safety and Privacy
- [[Changes/Dify/2026-02-11-97-other-changes-in-1-13-0|97 other changes in 1.13.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-02-11 · Codex CLI · [[Changes/Codex CLI/2026-02-11-15-model-support-changes-in-rust-v0-99-0|15 Model Support changes in rust-v0.99.0]]
- Later: 2026-02-11 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-02-11-2-model-support-changes-in-v0-0-407|2 Model Support changes in v0.0.407]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-02-11-c3c359&body=Card%3A%20Changes%2FDify%2F2026-02-11-2-model-support-changes-in-1-13-0.md%0ACard%20ID%3A%20dify-2026-02-11-c3c359%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.13.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->