---
card_id: open-webui-2026-04-24-473d44
date: '2026-04-24'
description: 'Open WebUI · 2026-04-24 · Reliability and Performance: 3 changes in
  v0.9.2 — ⚡ **Model list performance.** Model list API responses now strip base64
  profile…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General
    performance: Among other improvements, users will notice that ChatGPT is now…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1226
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: c1a93a30020cfd8540028f3efd7c98a29b9b81aed436a542e2cd3adacac55880
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-04-24-473d44
  comparison: ''
  date: '2026-04-24'
  description: 'Open WebUI — v0.9.2: 3 Reliability and Performance changes'
  evidence:
  - quote: ⚡ **Model list performance.** Model list API responses now strip base64
      profile image data from paginated results, and model tags are fetched via a
      dedicated efficient query instead of loading all models. This significantly
      reduces payload sizes and improves workspace Models page responsiveness.
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.2
  - quote: "\U0001F680 **Faster splash image loading.** Splash screen images are now
      prioritized earlier during page load with preload links, improving first-load
      LCP behavior and reducing delayed image discovery. [#24011](https://github.com/open-webui/open-webui/pull/24011)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.2
  - quote: "\U0001F504 **General improvements.** Various improvements were implemented
      across the application to enhance performance, stability, and security."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 3-reliability-and-performance-changes-in-v0-9-2
  source_release: open-webui-2026-04-24-v0-9-2-github-313142735-f0842502
  source_type: github_releases
  theme: reliability-performance
  title: 3 Reliability and Performance changes in v0.9.2
  type: change
related_changes:
- '[[Changes/Gemini CLI/2026-04-23-2-reliability-and-performance-changes-in-v0-39-0|2
  Reliability and Performance changes in v0.39.0]]'
- '[[Changes/GitHub Copilot CLI/2026-04-23-improve-rendering-performance-when-displaying-large-amounts-of-text-in-the-timel|Improve
  rendering performance when displaying large amounts of text in the timeline]]'
- '[[Changes/Cline/2026-04-24-add-periodic-memory-usage-logging|add periodic memory
  usage logging]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-04-24-v0-9-2-github-313142735-f0842502|open-webui-2026-04-24-v0-9-2-github-313142735-f0842502]]'
source_type: github_releases
theme: reliability-performance
title: 3 Reliability and Performance changes in v0.9.2
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Reliability and Performance changes in v0.9.2

**Open WebUI** · 2026-04-24 · [[Themes/reliability-performance|Reliability and Performance]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.2) · from [[Releases/Open WebUI/open-webui-2026-04-24-v0-9-2-github-313142735-f0842502|v0.9.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> ⚡ **Model list performance.** Model list API responses now strip base64 profile image data from paginated results, and model tags are fetched via a dedicated efficient query instead of loading all models. This significantly reduces payload sizes and improves workspace Models page responsiveness.

> 🚀 **Faster splash image loading.** Splash screen images are now prioritized earlier during page load with preload links, improving first-load LCP behavior and reducing delayed image discovery. [#24011](https://github.com/open-webui/open-webui/pull/24011)

> 🔄 **General improvements.** Various improvements were implemented across the application to enhance performance, stability, and security.

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-04-24-2-memory-and-personalization-changes-in-v0-9-2|2 Memory and Personalization changes in v0.9.2]] · Memory and Personalization
- [[Changes/Open WebUI/2026-04-24-4-model-support-changes-in-v0-9-2|4 Model Support changes in v0.9.2]] · Model Support
- [[Changes/Open WebUI/2026-04-24-automation-model-detection-the-create-automation-tool-now-correctly-detects-the|🧩 Automation model detection. The create_automation tool now correctly detects…]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-04-24-3-context-window-changes-in-v0-9-2|3 Context Window changes in v0.9.2]] · Context Window
- [[Changes/Open WebUI/2026-04-24-2-apps-and-integrations-changes-in-v0-9-2|2 Apps and Integrations changes in v0.9.2]] · Apps and Integrations
- [[Changes/Open WebUI/2026-04-24-2-editor-experience-changes-in-v0-9-2|2 Editor Experience changes in v0.9.2]] · Editor Experience
- [[Changes/Open WebUI/2026-04-24-3-account-and-access-changes-in-v0-9-2|3 Account and Access changes in v0.9.2]] · Account and Access
- [[Changes/Open WebUI/2026-04-24-paddleocr-vl-document-extraction-administrators-can-now-use-paddleocr-vl-as-a-co|🧠 PaddleOCR-vl document extraction. Administrators can now use PaddleOCR-vl…]] · Files and Data
- [[Changes/Open WebUI/2026-04-24-13-other-changes-in-v0-9-2|13 other changes in v0.9.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2026-04-24 · Cline · [[Changes/Cline/2026-04-24-add-periodic-memory-usage-logging|add periodic memory usage logging]]
- Later: 2026-04-28 · Claude Code · [[Changes/Claude Code/2026-04-28-faster-startup-after-upgrading-removed-the-recent-activity-panel-from-the-releas|Faster startup after upgrading]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General performance: Among other improvements, users will notice that ChatGPT is now…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-04-24-473d44&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-04-24-3-reliability-and-performance-changes-in-v0-9-2.md%0ACard%20ID%3A%20open-webui-2026-04-24-473d44%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->