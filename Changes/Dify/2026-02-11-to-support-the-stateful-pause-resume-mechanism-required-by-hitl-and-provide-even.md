---
card_id: dify-2026-02-11-623a89
date: '2026-02-11'
description: 'Dify · 2026-02-11 · Pricing Model: To support the stateful pause/resume
  mechanism required by HITL and provide event‑subscription APIs, we refactored the…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-daily-limit-to-ensure-a-high-quality-experience-for-all-chatgpt-users-we-are-exp|Daily
    limit: To ensure a high-quality experience for all ChatGPT users, we…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1154
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: pricing-model
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: pricing
machine_hash: fbfb9c3632351ab458227f0c7f1ed0560d2e907092847be05ffe9b12293b7145
product: dify
product_name: Dify
record:
  ai_generated: true
  card_id: dify-2026-02-11-623a89
  comparison: ''
  confidence: low
  date: '2026-02-11'
  description: 'Dify — 1.13.0 - Human-in-the-Loop and Workflow Execution Upgrades:
    To support the stateful pause/resume mechanism required by HITL and provide event‑subscription
    APIs, we refactored the execution engine: **Workflow‑based streaming executions
    and Advanced Chat executions now run in Celery workers**, while non‑streaming
    **WORKFLOW** runs still execute in the API process.'
  evidence:
  - quote: 'To support the stateful pause/resume mechanism required by HITL and provide
      event‑subscription APIs, we refactored the execution engine: **Workflow‑based
      streaming executions and Advanced Chat executions now run in Celery workers**,
      while non‑streaming **WORKFLOW** runs still execute in the API process.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.0
  extractor_version: fallback-v5
  impact: significant
  kind: pricing
  product: dify
  product_name: Dify
  slug: to-support-the-stateful-pause-resume-mechanism-required-by-hitl-and-provide-even
  source_release: dify-2026-02-11-1-13-0-github-285073967-47691626
  source_type: github_releases
  theme: pricing-model
  title: To support the stateful pause/resume mechanism required by HITL and provide…
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-02-04-10274-add-credits-tooltip-pakrym-oai|♯10274 Add
  credits tooltip @pakrym-oai]]'
- '[[Changes/Cline/2026-02-05-codex-5-3-through-chatgpt-subscription|Codex-5.3 through
  ChatGPT subscription]]'
- '[[Changes/GitHub Copilot CLI/2026-02-07-display-warning-when-user-has-no-copilot-subscription|Display
  warning when user has no Copilot subscription]]'
source_release: '[[Releases/Dify/dify-2026-02-11-1-13-0-github-285073967-47691626|dify-2026-02-11-1-13-0-github-285073967-47691626]]'
source_type: github_releases
theme: pricing-model
title: To support the stateful pause/resume mechanism required by HITL and provide…
type: change
---

<!-- chronolog:begin region="header" -->
# To support the stateful pause/resume mechanism required by HITL and provide…

**Dify** · 2026-02-11 · [[Themes/pricing-model|Pricing Model]] · Pricing · [Official source](https://github.com/langgenius/dify/releases/tag/1.13.0) · from [[Releases/Dify/dify-2026-02-11-1-13-0-github-285073967-47691626|1.13.0 - Human-in-the-Loop and Workflow Execution Upgrades]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> To support the stateful pause/resume mechanism required by HITL and provide event‑subscription APIs, we refactored the execution engine: **Workflow‑based streaming executions and Advanced Chat executions now run in Celery workers**, while non‑streaming **WORKFLOW** runs still execute in the API process.
>
> Source: https://github.com/langgenius/dify/releases/tag/1.13.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-02-11-3-reliability-and-performance-changes-in-1-13-0|3 Reliability and Performance changes in 1.13.0]] · Reliability and Performance
- [[Changes/Dify/2026-02-11-10-apps-and-integrations-changes-in-1-13-0|10 Apps and Integrations changes in 1.13.0]] · Apps and Integrations
- [[Changes/Dify/2026-02-11-flexible-delivery-methods-human-input-forms-can-be-delivered-via-webapp-or-email|Flexible Delivery Methods: Human input forms can be delivered…]] · Agent Mode
- [[Changes/Dify/2026-02-11-review-edit-the-node-generates-a-ui-where-humans-can-review-ai-outputs-and-modif|Review & Edit: The node generates a UI where humans can review AI outputs…]] · Editor Experience
- [[Changes/Dify/2026-02-11-please-use-the-following-command-instead-for-details-please-read-this-https-gith| Please use the following command instead]] · Developer Workflow
- [[Changes/Dify/2026-02-11-2-model-support-changes-in-1-13-0|2 Model Support changes in 1.13.0]] · Model Support
- [[Changes/Dify/2026-02-11-2-files-and-data-changes-in-1-13-0|2 Files and Data changes in 1.13.0]] · Files and Data
- [[Changes/Dify/2026-02-11-added-dutch-nl-nl-language-support-across-backend-language-mapping-and-web-local|Added Dutch (nl-NL) language support across backend language mapping and web…]] · Accessibility and Localization
- [[Changes/Dify/2026-02-11-2-safety-and-privacy-changes-in-1-13-0|2 Safety and Privacy changes in 1.13.0]] · Safety and Privacy
- [[Changes/Dify/2026-02-11-97-other-changes-in-1-13-0|97 other changes in 1.13.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Pricing Model

- Earlier: 2026-02-07 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-02-07-display-warning-when-user-has-no-copilot-subscription|Display warning when user has no Copilot subscription]]
- Later: 2026-03-03 · Gemini CLI · [[Changes/Gemini CLI/2026-03-03-feat-billing-implement-g1-ai-credits-overage-flow-with-billing-telemetry-by-gsqu|feat(billing): implement G1 AI credits overage flow with billing telemetry]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-daily-limit-to-ensure-a-high-quality-experience-for-all-chatgpt-users-we-are-exp|Daily limit: To ensure a high-quality experience for all ChatGPT users, we…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-02-11-623a89&body=Card%3A%20Changes%2FDify%2F2026-02-11-to-support-the-stateful-pause-resume-mechanism-required-by-hitl-and-provide-even.md%0ACard%20ID%3A%20dify-2026-02-11-623a89%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.13.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->