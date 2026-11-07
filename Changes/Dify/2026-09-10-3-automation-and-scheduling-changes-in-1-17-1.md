---
card_id: dify-2026-09-10-1bc57b
date: '2026-09-10'
description: 'Dify · 2026-09-10 · Automation and Scheduling: 3 changes in v1.17.1
  - Bug Fixes and Improvements — **Loop Boolean break conditions never matched.**
  New…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-change-gain-with-volume-automation|Change
    gain, with volume automation]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2549
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: automation-scheduling
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d37a314f0dff2d0c6b6eb0113b53199a95791968056f1eb66b0ec2d1559b270b
product: dify
product_name: Dify
record:
  card_id: dify-2026-09-10-1bc57b
  comparison: ''
  date: '2026-09-10'
  description: 'Dify — v1.17.1 - Bug Fixes and Improvements: 3 Automation and Scheduling
    changes'
  evidence:
  - quote: '**Loop Boolean break conditions never matched.** New conditions stored
      `"true"` / `"false"` as strings rather than booleans. Values are now stored
      and kept as real booleans, and legacy string values are normalized when rendered.
      (#41186)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(workflow): migrate schedule cron input by @lyzno1 in https://github.com/langgenius/dify/pull/41550'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(web): migrate loop variable constant inputs by @lyzno1 in https://github.com/langgenius/dify/pull/41901'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 3-automation-and-scheduling-changes-in-1-17-1
  source_release: dify-2026-09-10-1-17-1-github-386157159-e472b6fe
  source_type: github_releases
  theme: automation-scheduling
  title: 3 Automation and Scheduling changes in 1.17.1
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-09-05-8-automation-and-scheduling-changes-in-v2026-9-2|8
  Automation and Scheduling changes in v2026.9.2]]'
- '[[Changes/OpenClaw/2026-09-08-7-automation-and-scheduling-changes-in-v2026-9-3|7
  Automation and Scheduling changes in v2026.9.3]]'
- '[[Changes/OpenHands/2026-09-09-9-automation-and-scheduling-changes-in-v1-17-0|9
  Automation and Scheduling changes in v1.17.0]]'
source_release: '[[Releases/Dify/dify-2026-09-10-1-17-1-github-386157159-e472b6fe|dify-2026-09-10-1-17-1-github-386157159-e472b6fe]]'
source_type: github_releases
theme: automation-scheduling
title: 3 Automation and Scheduling changes in 1.17.1
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Automation and Scheduling changes in 1.17.1

**Dify** · 2026-09-10 · [[Themes/automation-scheduling|Automation and Scheduling]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.17.1) · from [[Releases/Dify/dify-2026-09-10-1-17-1-github-386157159-e472b6fe|v1.17.1 - Bug Fixes and Improvements]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **Loop Boolean break conditions never matched.** New conditions stored `"true"` / `"false"` as strings rather than booleans. Values are now stored and kept as real booleans, and legacy string values are normalized when rendered. (#41186)

> refactor(workflow): migrate schedule cron input by @lyzno1 in https://github.com/langgenius/dify/pull/41550

> refactor(web): migrate loop variable constant inputs by @lyzno1 in https://github.com/langgenius/dify/pull/41901

Source: https://github.com/langgenius/dify/releases/tag/1.17.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-09-10-4-pricing-model-changes-in-1-17-1|4 Pricing Model changes in 1.17.1]] · Pricing Model
- [[Changes/Dify/2026-09-10-8-interface-experience-changes-in-1-17-1|8 Interface Experience changes in 1.17.1]] · Interface Experience
- [[Changes/Dify/2026-09-10-76-model-support-changes-in-1-17-1|76 Model Support changes in 1.17.1]] · Model Support
- [[Changes/Dify/2026-09-10-42-agent-mode-changes-in-1-17-1|42 Agent Mode changes in 1.17.1]] · Agent Mode
- [[Changes/Dify/2026-09-10-4-developer-workflow-changes-in-1-17-1|4 Developer Workflow changes in 1.17.1]] · Developer Workflow
- [[Changes/Dify/2026-09-10-3-collaboration-changes-in-1-17-1|3 Collaboration changes in 1.17.1]] · Collaboration
- [[Changes/Dify/2026-09-10-2-memory-and-personalization-changes-in-1-17-1|2 Memory and Personalization changes in 1.17.1]] · Memory and Personalization
- [[Changes/Dify/2026-09-10-16-safety-and-privacy-changes-in-1-17-1|16 Safety and Privacy changes in 1.17.1]] · Safety and Privacy
- [[Changes/Dify/2026-09-10-13-files-and-data-changes-in-1-17-1|13 Files and Data changes in 1.17.1]] · Files and Data
- [[Changes/Dify/2026-09-10-skill-packages-built-on-windows-failed-with-a-misleading-error-a-skill-md-using|Skill packages built on Windows failed with a misleading error. A SKILL.md…]] · Mobile and Desktop
- [[Changes/Dify/2026-09-10-12-apps-and-integrations-changes-in-1-17-1|12 Apps and Integrations changes in 1.17.1]] · Apps and Integrations
- [[Changes/Dify/2026-09-10-6-account-and-access-changes-in-1-17-1|6 Account and Access changes in 1.17.1]] · Account and Access
- [[Changes/Dify/2026-09-10-3-multimodal-input-changes-in-1-17-1|3 Multimodal Input changes in 1.17.1]] · Multimodal Input
- [[Changes/Dify/2026-09-10-6-editor-experience-changes-in-1-17-1|6 Editor Experience changes in 1.17.1]] · Editor Experience
- [[Changes/Dify/2026-09-10-3-accessibility-and-localization-changes-in-1-17-1|3 Accessibility and Localization changes in 1.17.1]] · Accessibility and Localization
- [[Changes/Dify/2026-09-10-a-plugin-could-exhaust-worker-memory-with-one-declared-number-the-blob-chunk-mer|A plugin could exhaust worker memory with one declared number. The blob chunk…]] · Reliability and Performance
- [[Changes/Dify/2026-09-10-6-context-window-changes-in-1-17-1|6 Context Window changes in 1.17.1]] · Context Window
- [[Changes/Dify/2026-09-10-205-other-changes-in-1-17-1|205 other changes in 1.17.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Automation and Scheduling

- Earlier: 2026-09-09 · OpenHands · [[Changes/OpenHands/2026-09-09-9-automation-and-scheduling-changes-in-v1-17-0|9 Automation and Scheduling changes in v1.17.0]]
- Later: 2026-09-11 · OpenClaw · [[Changes/OpenClaw/2026-09-11-7-automation-and-scheduling-changes-in-v2026-9-4|7 Automation and Scheduling changes in v2026.9.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-change-gain-with-volume-automation|Change gain, with volume automation]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-09-10-1bc57b&body=Card%3A%20Changes%2FDify%2F2026-09-10-3-automation-and-scheduling-changes-in-1-17-1.md%0ACard%20ID%3A%20dify-2026-09-10-1bc57b%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.17.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->