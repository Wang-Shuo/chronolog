---
card_id: dify-2026-09-10-d0a790
date: '2026-09-10'
description: 'Dify · 2026-09-10 · Multimodal Input: 3 changes in v1.17.1 - Bug Fixes
  and Improvements — **Partial segment updates wiped attachments.** A segment update
  that…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-11-16-descript-now-supports-video|Video
    Playback]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2855
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: multimodal
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: cd0dada9d3ff944e9d983f38457525100b9a46bad7d5c4f7408673b9e5733ac7
product: dify
product_name: Dify
record:
  card_id: dify-2026-09-10-d0a790
  comparison: ''
  date: '2026-09-10'
  description: 'Dify — v1.17.1 - Bug Fixes and Improvements: 3 Multimodal Input changes'
  evidence:
  - quote: '**Partial segment updates wiped attachments.** A segment update that omitted
      `attachment_ids` was treated as "replace with nothing", deleting the segment''s
      attachment bindings and multimodal vectors. Attachments are now left alone unless
      `attachment_ids` is explicitly provided; passing `[]` still clears them. (#41777)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: '**Deleting content left orphaned files in object storage.** Segment deletion,
      multimodal re-indexing, and batch document deletion each removed the database
      rows but left the physical attachment objects behind. All three paths now delete
      the underlying objects after the database commit, with an orphan check so attachments
      shared by other segments survive. (#41400, #41999, #41256)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: '**Images uploaded to an Agent App were turned into shell download instructions**
      rather than being shown to the model. Vision-capable models now receive them
      as native multimodal content, detected from the selected credential-bound model
      schema. The download fallback is preserved for non-image files and for models
      without vision support, and image URLs and Base64 payloads are redacted from
      agent backend logs. (#41685)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 3-multimodal-input-changes-in-1-17-1
  source_release: dify-2026-09-10-1-17-1-github-386157159-e472b6fe
  source_type: github_releases
  theme: multimodal
  title: 3 Multimodal Input changes in 1.17.1
  type: change
related_changes:
- '[[Changes/Krea/2026-09-07-realtime-director|Realtime Director]]'
- '[[Changes/OpenClaw/2026-09-08-provider-adapters-preserve-initial-anthropic-text-and-thinking-keep-images-with|Provider
  adapters preserve initial Anthropic text and thinking, keep images…]]'
- '[[Changes/DeepSeek API/2026-09-10-deepseek-v4-1-flash-release|DeepSeek-V4.1-Flash
  Release]]'
source_release: '[[Releases/Dify/dify-2026-09-10-1-17-1-github-386157159-e472b6fe|dify-2026-09-10-1-17-1-github-386157159-e472b6fe]]'
source_type: github_releases
theme: multimodal
title: 3 Multimodal Input changes in 1.17.1
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Multimodal Input changes in 1.17.1

**Dify** · 2026-09-10 · [[Themes/multimodal|Multimodal Input]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.17.1) · from [[Releases/Dify/dify-2026-09-10-1-17-1-github-386157159-e472b6fe|v1.17.1 - Bug Fixes and Improvements]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **Partial segment updates wiped attachments.** A segment update that omitted `attachment_ids` was treated as "replace with nothing", deleting the segment's attachment bindings and multimodal vectors. Attachments are now left alone unless `attachment_ids` is explicitly provided; passing `[]` still clears them. (#41777)

> **Deleting content left orphaned files in object storage.** Segment deletion, multimodal re-indexing, and batch document deletion each removed the database rows but left the physical attachment objects behind. All three paths now delete the underlying objects after the database commit, with an orphan check so attachments shared by other segments survive. (#41400, #41999, #41256)

> **Images uploaded to an Agent App were turned into shell download instructions** rather than being shown to the model. Vision-capable models now receive them as native multimodal content, detected from the selected credential-bound model schema. The download fallback is preserved for non-image files and for models without vision support, and image URLs and Base64 payloads are redacted from agent backend logs. (#41685)

Source: https://github.com/langgenius/dify/releases/tag/1.17.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-09-10-4-pricing-model-changes-in-1-17-1|4 Pricing Model changes in 1.17.1]] · Pricing Model
- [[Changes/Dify/2026-09-10-3-automation-and-scheduling-changes-in-1-17-1|3 Automation and Scheduling changes in 1.17.1]] · Automation and Scheduling
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
- [[Changes/Dify/2026-09-10-6-editor-experience-changes-in-1-17-1|6 Editor Experience changes in 1.17.1]] · Editor Experience
- [[Changes/Dify/2026-09-10-3-accessibility-and-localization-changes-in-1-17-1|3 Accessibility and Localization changes in 1.17.1]] · Accessibility and Localization
- [[Changes/Dify/2026-09-10-a-plugin-could-exhaust-worker-memory-with-one-declared-number-the-blob-chunk-mer|A plugin could exhaust worker memory with one declared number. The blob chunk…]] · Reliability and Performance
- [[Changes/Dify/2026-09-10-6-context-window-changes-in-1-17-1|6 Context Window changes in 1.17.1]] · Context Window
- [[Changes/Dify/2026-09-10-205-other-changes-in-1-17-1|205 other changes in 1.17.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Multimodal Input

- Earlier: 2026-09-10 · DeepSeek API · [[Changes/DeepSeek API/2026-09-10-deepseek-v4-1-flash-release|DeepSeek-V4.1-Flash Release]]
- Later: 2026-09-11 · OpenClaw · [[Changes/OpenClaw/2026-09-11-the-bundled-video-frames-skill-and-its-helper-script-have-been-removed-if-you-us|The bundled video-frames skill and its helper script have been removed]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-11-16 · Descript · [[Changes/Descript/2018-11-16-descript-now-supports-video|Video Playback]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-09-10-d0a790&body=Card%3A%20Changes%2FDify%2F2026-09-10-3-multimodal-input-changes-in-1-17-1.md%0ACard%20ID%3A%20dify-2026-09-10-d0a790%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.17.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->