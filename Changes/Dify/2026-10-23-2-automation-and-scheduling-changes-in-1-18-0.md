---
card_id: dify-2026-10-23-f7a266
date: '2026-10-23'
description: 'Dify · 2026-10-23 · Automation and Scheduling: 2 changes in v1.18.0
  — Smarter Agent Routing, Portable Apps, Deeper Workflow Visibility — Rebuild the
  web…'
diffusion:
  first_in_tracked: '[[Changes/Dify/2024-01-02-add-data-clean-schedule-by-johnjyong-in-https-github-com-langgenius-dify-pull-18|Add
    data clean schedule]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1025
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: automation-scheduling
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d449f68e6d843ef3b3c46940353c133fabd625ac294b1579038b3524caa3b0cd
product: dify
product_name: Dify
record:
  card_id: dify-2026-10-23-f7a266
  comparison: ''
  date: '2026-10-23'
  description: 'Dify — v1.18.0 — Smarter Agent Routing, Portable Apps, Deeper Workflow
    Visibility: 2 Automation and Scheduling changes'
  evidence:
  - quote: Rebuild the web application and restart API, worker, scheduler, and Agent
      services from the same release. If deploying Agent Backend separately from source,
      refresh its locked `server` dependencies as well.
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: 'Save the timezone shown on new schedule nodes, handle daylight-saving
      transitions in next-run calculation and offset labels, and correct hourly previews
      at month boundaries. (#43532, #43357, #43627, #43925)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 2-automation-and-scheduling-changes-in-1-18-0
  source_release: dify-2026-10-23-1-18-0-github-421489030-879b0613
  source_type: github_releases
  theme: automation-scheduling
  title: 2 Automation and Scheduling changes in 1.18.0
  type: change
related_changes:
- '[[Changes/OpenHands/2026-10-22-refactor-automations-express-the-activity-track-height-in-css-by-enyst-in-https|refactor(automations):
  express the activity track height in CSS]]'
- '[[Changes/OpenHands/2026-10-22-feat-automations-hide-the-github-token-secret-field-on-self-hosted-instances-whe|feat(automations):
  hide the GitHub token secret field on self-hosted instances…]]'
- '[[Changes/OpenHands/2026-10-22-feat-automations-reflect-the-built-in-integration-s-connection-state-in-the-setu|feat(automations):
  reflect the built-in integration''s connection state in the setup…]]'
source_release: '[[Releases/Dify/dify-2026-10-23-1-18-0-github-421489030-879b0613|dify-2026-10-23-1-18-0-github-421489030-879b0613]]'
source_type: github_releases
theme: automation-scheduling
title: 2 Automation and Scheduling changes in 1.18.0
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Automation and Scheduling changes in 1.18.0

**Dify** · 2026-10-23 · [[Themes/automation-scheduling|Automation and Scheduling]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.18.0) · from [[Releases/Dify/dify-2026-10-23-1-18-0-github-421489030-879b0613|v1.18.0 — Smarter Agent Routing, Portable Apps, Deeper Workflow Visibility]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Rebuild the web application and restart API, worker, scheduler, and Agent services from the same release. If deploying Agent Backend separately from source, refresh its locked `server` dependencies as well.

> Save the timezone shown on new schedule nodes, handle daylight-saving transitions in next-run calculation and offset labels, and correct hourly previews at month boundaries. (#43532, #43357, #43627, #43925)

Source: https://github.com/langgenius/dify/releases/tag/1.18.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-10-23-respect-xforward-headers-enabled-standalone-api-default-remains-false-bundled-co| /  RESPECT_XFORWARD_HEADERS_ENABLED  /  Standalone API default remains false]] · Developer Workflow
- [[Changes/Dify/2026-10-23-3-memory-and-personalization-changes-in-1-18-0|3 Memory and Personalization changes in 1.18.0]] · Memory and Personalization
- [[Changes/Dify/2026-10-23-3-accessibility-and-localization-changes-in-1-18-0|3 Accessibility and Localization changes in 1.18.0]] · Accessibility and Localization
- [[Changes/Dify/2026-10-23-3-context-window-changes-in-1-18-0|3 Context Window changes in 1.18.0]] · Context Window
- [[Changes/Dify/2026-10-23-operations-archive-storage-supports-configurable-s3-addressing-style-the-api-ima|Operations: archive storage supports configurable S3 addressing style]] · Model Support
- [[Changes/Dify/2026-10-23-2-interface-experience-changes-in-1-18-0|2 Interface Experience changes in 1.18.0]] · Interface Experience
- [[Changes/Dify/2026-10-23-3-editor-experience-changes-in-1-18-0|3 Editor Experience changes in 1.18.0]] · Editor Experience
- [[Changes/Dify/2026-10-23-32-agent-mode-changes-in-1-18-0|32 Agent Mode changes in 1.18.0]] · Agent Mode
- [[Changes/Dify/2026-10-23-11-safety-and-privacy-changes-in-1-18-0|11 Safety and Privacy changes in 1.18.0]] · Safety and Privacy
- [[Changes/Dify/2026-10-23-14-apps-and-integrations-changes-in-1-18-0|14 Apps and Integrations changes in 1.18.0]] · Apps and Integrations
- [[Changes/Dify/2026-10-23-6-account-and-access-changes-in-1-18-0|6 Account and Access changes in 1.18.0]] · Account and Access
- [[Changes/Dify/2026-10-23-2-reliability-and-performance-changes-in-1-18-0|2 Reliability and Performance changes in 1.18.0]] · Reliability and Performance
- [[Changes/Dify/2026-10-23-5-collaboration-changes-in-1-18-0|5 Collaboration changes in 1.18.0]] · Collaboration
- [[Changes/Dify/2026-10-23-8-files-and-data-changes-in-1-18-0|8 Files and Data changes in 1.18.0]] · Files and Data
- [[Changes/Dify/2026-10-23-81-other-changes-in-1-18-0|81 other changes in 1.18.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Automation and Scheduling

- Earlier: 2026-10-22 · OpenHands · [[Changes/OpenHands/2026-10-22-feat-automations-reflect-the-built-in-integration-s-connection-state-in-the-setu|feat(automations): reflect the built-in integration's connection state in the setup…]]
- Later: 2026-10-23 · OpenHands · [[Changes/OpenHands/2026-10-23-3-automation-and-scheduling-changes-in-v1-32-0|3 Automation and Scheduling changes in v1.32.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2024-01-02 · Dify · [[Changes/Dify/2024-01-02-add-data-clean-schedule-by-johnjyong-in-https-github-com-langgenius-dify-pull-18|Add data clean schedule]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-10-23-f7a266&body=Card%3A%20Changes%2FDify%2F2026-10-23-2-automation-and-scheduling-changes-in-1-18-0.md%0ACard%20ID%3A%20dify-2026-10-23-f7a266%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.18.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->