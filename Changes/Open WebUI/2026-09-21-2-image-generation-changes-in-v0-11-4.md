---
card_id: open-webui-2026-09-21-325343
date: '2026-09-21'
description: "Open WebUI · 2026-09-21 · Image Generation: 2 changes in v0.11.4 — \U0001F3A3
  **Testing an image connection.** The Verify button beside an image generation connection…"
diffusion:
  first_in_tracked: "[[Changes/Open WebUI/2024-03-10-dall-e-integration-introduced-dall-e-integration-for-image-generation-alongside|\U0001F3A8
    DALL-E Integration]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 925
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: image-generation
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8dca39e31b0746532c0907d9f4e50c5b07d5a2b05b7aef75122f29d54d4d09f9
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-09-21-325343
  comparison: ''
  date: '2026-09-21'
  description: 'Open WebUI — v0.11.4: 2 Image Generation changes'
  evidence:
  - quote: "\U0001F3A3 **Testing an image connection.** The Verify button beside an
      image generation connection saved the whole image configuration first and then
      tested whichever engine was active rather than the connection beside it, and
      it now tests exactly that connection and changes nothing. [Commit](https://github.com/open-webui/open-webui/commit/64bbdf7a73724986fac8bcf6e880fe32ef9ac495)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F4E1 **Image connection check endpoint.** The endpoint that checks
      an image generation connection has moved and now takes the connection to test
      in the request itself, so anything calling the old address needs updating. [Commit](https://github.com/open-webui/open-webui/commit/64bbdf7a73724986fac8bcf6e880fe32ef9ac495)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 2-image-generation-changes-in-v0-11-4
  source_release: open-webui-2026-09-21-v0-11-4-github-393232555-90de9130
  source_type: github_releases
  theme: image-generation
  title: 2 Image Generation changes in v0.11.4
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-09-17-43953-preserve-per-image-generation-ids-in-image-generation-analytics-copyberry|♯43953
  Preserve per-image generation IDs in image generation analytics @copyberry]]'
- '[[Changes/ElevenLabs/2026-09-21-image-and-video|Image and video]]'
- '[[Changes/ElevenLabs/2026-09-21-image-and-video-915070|Image and video]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-09-21-v0-11-4-github-393232555-90de9130|open-webui-2026-09-21-v0-11-4-github-393232555-90de9130]]'
source_type: github_releases
theme: image-generation
title: 2 Image Generation changes in v0.11.4
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Image Generation changes in v0.11.4

**Open WebUI** · 2026-09-21 · [[Themes/image-generation|Image Generation]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.4) · from [[Releases/Open WebUI/open-webui-2026-09-21-v0-11-4-github-393232555-90de9130|v0.11.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🎣 **Testing an image connection.** The Verify button beside an image generation connection saved the whole image configuration first and then tested whichever engine was active rather than the connection beside it, and it now tests exactly that connection and changes nothing. [Commit](https://github.com/open-webui/open-webui/commit/64bbdf7a73724986fac8bcf6e880fe32ef9ac495)

> 📡 **Image connection check endpoint.** The endpoint that checks an image generation connection has moved and now takes the connection to test in the request itself, so anything calling the old address needs updating. [Commit](https://github.com/open-webui/open-webui/commit/64bbdf7a73724986fac8bcf6e880fe32ef9ac495)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-09-21-4-safety-and-privacy-changes-in-v0-11-4|4 Safety and Privacy changes in v0.11.4]] · Safety and Privacy
- [[Changes/Open WebUI/2026-09-21-3-context-window-changes-in-v0-11-4|3 Context Window changes in v0.11.4]] · Context Window
- [[Changes/Open WebUI/2026-09-21-general-improvements-various-improvements-were-implemented-across-the-applicatio|🔄 General improvements. Various improvements were implemented across…]] · Reliability and Performance
- [[Changes/Open WebUI/2026-09-21-6-account-and-access-changes-in-v0-11-4|6 Account and Access changes in v0.11.4]] · Account and Access
- [[Changes/Open WebUI/2026-09-21-39-developer-workflow-changes-in-v0-11-4|39 Developer Workflow changes in v0.11.4]] · Developer Workflow
- [[Changes/Open WebUI/2026-09-21-4-collaboration-changes-in-v0-11-4|4 Collaboration changes in v0.11.4]] · Collaboration
- [[Changes/Open WebUI/2026-09-21-5-voice-and-audio-changes-in-v0-11-4|5 Voice and Audio changes in v0.11.4]] · Voice and Audio
- [[Changes/Open WebUI/2026-09-21-10-files-and-data-changes-in-v0-11-4|10 Files and Data changes in v0.11.4]] · Files and Data
- [[Changes/Open WebUI/2026-09-21-21-editor-experience-changes-in-v0-11-4|21 Editor Experience changes in v0.11.4]] · Editor Experience
- [[Changes/Open WebUI/2026-09-21-6-memory-and-personalization-changes-in-v0-11-4|6 Memory and Personalization changes in v0.11.4]] · Memory and Personalization
- [[Changes/Open WebUI/2026-09-21-apple-device-replies-an-assistant-reply-no-longer-comes-up-blank-in-a-home-scree|📱 Apple device replies. An assistant reply no longer comes up blank in a home…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-09-21-3-apps-and-integrations-changes-in-v0-11-4|3 Apps and Integrations changes in v0.11.4]] · Apps and Integrations
- [[Changes/Open WebUI/2026-09-21-6-search-and-browsing-changes-in-v0-11-4|6 Search and Browsing changes in v0.11.4]] · Search and Browsing
- [[Changes/Open WebUI/2026-09-21-13-interface-experience-changes-in-v0-11-4|13 Interface Experience changes in v0.11.4]] · Interface Experience
- [[Changes/Open WebUI/2026-09-21-4-automation-and-scheduling-changes-in-v0-11-4|4 Automation and Scheduling changes in v0.11.4]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-09-21-41-model-support-changes-in-v0-11-4|41 Model Support changes in v0.11.4]] · Model Support
- [[Changes/Open WebUI/2026-09-21-5-enterprise-and-administration-changes-in-v0-11-4|5 Enterprise and Administration changes in v0.11.4]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-09-21-61-other-changes-in-v0-11-4|61 other changes in v0.11.4]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Image Generation

- Earlier: 2026-09-21 · ElevenLabs · [[Changes/ElevenLabs/2026-09-21-image-and-video-915070|Image and video]]
- Later: 2026-09-22 · Codex CLI · [[Changes/Codex CLI/2026-09-22-45544-discourage-logging-full-image-generation-results-gan-tu|♯45544 Discourage logging full image generation results @Gan-Tu]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2024-03-10 · Open WebUI · [[Changes/Open WebUI/2024-03-10-dall-e-integration-introduced-dall-e-integration-for-image-generation-alongside|🎨 DALL-E Integration]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-09-21-325343&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-09-21-2-image-generation-changes-in-v0-11-4.md%0ACard%20ID%3A%20open-webui-2026-09-21-325343%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.4%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->