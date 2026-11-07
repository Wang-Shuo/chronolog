---
card_id: dify-2026-02-11-043124
date: '2026-02-11'
description: 'Dify · 2026-02-11 · Reliability and Performance: 3 changes in 1.13.0
  - Human-in-the-Loop and Workflow Execution Upgrades — high-stakes scenarios where
  AI speed…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General
    performance: Among other improvements, users will notice that ChatGPT is now…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1154
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 1c4e9e20c856630224a1778fe3696efca57cf74ae659ad85093710e1e11a6939
product: dify
product_name: Dify
record:
  card_id: dify-2026-02-11-043124
  comparison: ''
  date: '2026-02-11'
  description: 'Dify — 1.13.0 - Human-in-the-Loop and Workflow Execution Upgrades:
    3 Reliability and Performance changes'
  evidence:
  - quote: high-stakes scenarios where AI speed is needed but human judgment is essential.
      With HITL, we are making h
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.0
  - quote: 'We have introduced a new Celery queue named `workflow_based_app_execution`.
      While standard setups will work out of the box, high-throughput environments
      should consider the following optimizations to ensure stability and performance:'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.0
  - quote: Improved large-data task stability with split DB sessions, batched cleanup
      execution, index tuning, and configurable inter-batch throttling for retention
      cleanup jobs.
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 3-reliability-and-performance-changes-in-1-13-0
  source_release: dify-2026-02-11-1-13-0-github-285073967-47691626
  source_type: github_releases
  theme: reliability-performance
  title: 3 Reliability and Performance changes in 1.13.0
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-02-09-text-to-speech|Text to Speech]]'
- '[[Changes/OpenCode/2026-02-10-core-memory-leak-fixed-in-platform-fetch-for-events|Core
  Memory leak fixed in platform fetch for events]]'
- '[[Changes/OpenCode/2026-02-10-2-reliability-and-performance-changes-in-v1-1-54|2
  Reliability and Performance changes in v1.1.54]]'
source_release: '[[Releases/Dify/dify-2026-02-11-1-13-0-github-285073967-47691626|dify-2026-02-11-1-13-0-github-285073967-47691626]]'
source_type: github_releases
theme: reliability-performance
title: 3 Reliability and Performance changes in 1.13.0
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Reliability and Performance changes in 1.13.0

**Dify** · 2026-02-11 · [[Themes/reliability-performance|Reliability and Performance]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.13.0) · from [[Releases/Dify/dify-2026-02-11-1-13-0-github-285073967-47691626|1.13.0 - Human-in-the-Loop and Workflow Execution Upgrades]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> high-stakes scenarios where AI speed is needed but human judgment is essential. With HITL, we are making h

> We have introduced a new Celery queue named `workflow_based_app_execution`. While standard setups will work out of the box, high-throughput environments should consider the following optimizations to ensure stability and performance:

> Improved large-data task stability with split DB sessions, batched cleanup execution, index tuning, and configurable inter-batch throttling for retention cleanup jobs.

Source: https://github.com/langgenius/dify/releases/tag/1.13.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-02-11-10-apps-and-integrations-changes-in-1-13-0|10 Apps and Integrations changes in 1.13.0]] · Apps and Integrations
- [[Changes/Dify/2026-02-11-flexible-delivery-methods-human-input-forms-can-be-delivered-via-webapp-or-email|Flexible Delivery Methods: Human input forms can be delivered…]] · Agent Mode
- [[Changes/Dify/2026-02-11-to-support-the-stateful-pause-resume-mechanism-required-by-hitl-and-provide-even|To support the stateful pause/resume mechanism required by HITL and provide…]] · Pricing Model
- [[Changes/Dify/2026-02-11-review-edit-the-node-generates-a-ui-where-humans-can-review-ai-outputs-and-modif|Review & Edit: The node generates a UI where humans can review AI outputs…]] · Editor Experience
- [[Changes/Dify/2026-02-11-please-use-the-following-command-instead-for-details-please-read-this-https-gith| Please use the following command instead]] · Developer Workflow
- [[Changes/Dify/2026-02-11-2-model-support-changes-in-1-13-0|2 Model Support changes in 1.13.0]] · Model Support
- [[Changes/Dify/2026-02-11-2-files-and-data-changes-in-1-13-0|2 Files and Data changes in 1.13.0]] · Files and Data
- [[Changes/Dify/2026-02-11-added-dutch-nl-nl-language-support-across-backend-language-mapping-and-web-local|Added Dutch (nl-NL) language support across backend language mapping and web…]] · Accessibility and Localization
- [[Changes/Dify/2026-02-11-2-safety-and-privacy-changes-in-1-13-0|2 Safety and Privacy changes in 1.13.0]] · Safety and Privacy
- [[Changes/Dify/2026-02-11-97-other-changes-in-1-13-0|97 other changes in 1.13.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2026-02-10 · OpenCode · [[Changes/OpenCode/2026-02-10-2-reliability-and-performance-changes-in-v1-1-54|2 Reliability and Performance changes in v1.1.54]]
- Later: 2026-02-12 · Codex CLI · [[Changes/Codex CLI/2026-02-12-improved-websocket-session-stability-by-continuing-ping-handling-when-idle-and-s|Improved websocket session stability by continuing ping handling when idle…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General performance: Among other improvements, users will notice that ChatGPT is now…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-02-11-043124&body=Card%3A%20Changes%2FDify%2F2026-02-11-3-reliability-and-performance-changes-in-1-13-0.md%0ACard%20ID%3A%20dify-2026-02-11-043124%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.13.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->