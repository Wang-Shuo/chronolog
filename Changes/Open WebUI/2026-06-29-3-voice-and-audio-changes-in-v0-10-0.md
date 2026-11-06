---
card_id: open-webui-2026-06-29-0a4042
date: '2026-06-29'
description: "Open WebUI · 2026-06-29 · Voice and Audio: 3 changes in v0.10.0 — \U0001F5E3️
  **Voice suggestions in the model editor.** The model editor now offers a dropdown
  of…"
diffusion:
  first_in_tracked: '[[Changes/Dify/2023-07-10-2-voice-and-audio-changes-in-0-3-7|2
    Voice and Audio changes in 0.3.7]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1085
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: voice
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 67c3ab2d3e33247ca4072566c7e630ea7f036d22305272586c52944b7e53b79a
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-06-29-0a4042
  comparison: ''
  date: '2026-06-29'
  description: 'Open WebUI — v0.10.0: 3 Voice and Audio changes'
  evidence:
  - quote: "\U0001F5E3️ **Voice suggestions in the model editor.** The model editor
      now offers a dropdown of available text-to-speech voices, making it easier to
      pick one. [Commit](https://github.com/open-webui/open-webui/commit/a5c945940134b957dbad47790b5baafeecdac6c4),
      [#25706](https://github.com/open-webui/open-webui/pull/25706)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F5E3️ **Azure speech input is escaped.** Voice and language values
      are now escaped when building Azure text-to-speech requests, preventing malformed
      or injected markup. [#25776](https://github.com/open-webui/open-webui/pull/25776)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F399️ **ElevenLabs speech keeps working when voices can't load.**
      Text-to-speech through ElevenLabs no longer fails when the available-voice list
      can't be fetched, instead of rejecting every voice. [Commit](https://github.com/open-webui/open-webui/commit/bb1419328b11b801b4c939dfc112700ba6f6fdab),
      [#26075](https://github.com/open-webui/open-webui/issues/26075)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 3-voice-and-audio-changes-in-v0-10-0
  source_release: open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01
  source_type: github_releases
  theme: voice
  title: 3 Voice and Audio changes in v0.10.0
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-06-29-javascript-sdk|JavaScript SDK]]'
- '[[Changes/ElevenLabs/2026-06-29-python-sdk|Python SDK]]'
- '[[Changes/ElevenLabs/2026-06-29-speech-to-text-b8f62a|Speech to Text]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01|open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01]]'
source_type: github_releases
theme: voice
title: 3 Voice and Audio changes in v0.10.0
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Voice and Audio changes in v0.10.0

**Open WebUI** · 2026-06-29 · [[Themes/voice|Voice and Audio]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.10.0) · from [[Releases/Open WebUI/open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01|v0.10.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🗣️ **Voice suggestions in the model editor.** The model editor now offers a dropdown of available text-to-speech voices, making it easier to pick one. [Commit](https://github.com/open-webui/open-webui/commit/a5c945940134b957dbad47790b5baafeecdac6c4), [#25706](https://github.com/open-webui/open-webui/pull/25706)

> 🗣️ **Azure speech input is escaped.** Voice and language values are now escaped when building Azure text-to-speech requests, preventing malformed or injected markup. [#25776](https://github.com/open-webui/open-webui/pull/25776)

> 🎙️ **ElevenLabs speech keeps working when voices can't load.** Text-to-speech through ElevenLabs no longer fails when the available-voice list can't be fetched, instead of rejecting every voice. [Commit](https://github.com/open-webui/open-webui/commit/bb1419328b11b801b4c939dfc112700ba6f6fdab), [#26075](https://github.com/open-webui/open-webui/issues/26075)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-06-29-5-files-and-data-changes-in-v0-10-0|5 Files and Data changes in v0.10.0]] · Files and Data
- [[Changes/Open WebUI/2026-06-29-5-memory-and-personalization-changes-in-v0-10-0|5 Memory and Personalization changes in v0.10.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-06-29-14-interface-experience-changes-in-v0-10-0|14 Interface Experience changes in v0.10.0]] · Interface Experience
- [[Changes/Open WebUI/2026-06-29-4-collaboration-changes-in-v0-10-0|4 Collaboration changes in v0.10.0]] · Collaboration
- [[Changes/Open WebUI/2026-06-29-client-user-agent-forwarded-to-model-backends-the-browser-s-user-agent-is-now-pa|🪪 Client User-Agent forwarded to model backends. The browser's User-Agent is now…]] · Agent Mode
- [[Changes/Open WebUI/2026-06-29-scim-sync-can-t-demote-an-admin-a-scim-provisioning-sync-that-marks-a-user-inact|🛟 SCIM sync can't demote an admin. A SCIM provisioning sync that marks a user…]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-06-29-8-search-and-browsing-changes-in-v0-10-0|8 Search and Browsing changes in v0.10.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-06-29-25-model-support-changes-in-v0-10-0|25 Model Support changes in v0.10.0]] · Model Support
- [[Changes/Open WebUI/2026-06-29-6-reliability-and-performance-changes-in-v0-10-0|6 Reliability and Performance changes in v0.10.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-06-29-4-mobile-and-desktop-changes-in-v0-10-0|4 Mobile and Desktop changes in v0.10.0]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-06-29-better-screen-reader-labels-on-toggles-integration-and-switch-toggles-now-expose|♿ Better screen-reader labels on toggles. Integration and switch toggles now…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-06-29-16-safety-and-privacy-changes-in-v0-10-0|16 Safety and Privacy changes in v0.10.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-06-29-2-pricing-model-changes-in-v0-10-0|2 Pricing Model changes in v0.10.0]] · Pricing Model
- [[Changes/Open WebUI/2026-06-29-7-apps-and-integrations-changes-in-v0-10-0|7 Apps and Integrations changes in v0.10.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-06-29-9-account-and-access-changes-in-v0-10-0|9 Account and Access changes in v0.10.0]] · Account and Access
- [[Changes/Open WebUI/2026-06-29-usable-chat-input-on-mobile-with-many-tools-when-skills-tools-terminal-web-searc|📱 Usable chat input on mobile with many tools. When skills, tools, terminal, web…]] · Image Generation
- [[Changes/Open WebUI/2026-06-29-6-automation-and-scheduling-changes-in-v0-10-0|6 Automation and Scheduling changes in v0.10.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-06-29-3-context-window-changes-in-v0-10-0|3 Context Window changes in v0.10.0]] · Context Window
- [[Changes/Open WebUI/2026-06-29-42-developer-workflow-changes-in-v0-10-0|42 Developer Workflow changes in v0.10.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-06-29-10-editor-experience-changes-in-v0-10-0|10 Editor Experience changes in v0.10.0]] · Editor Experience
- [[Changes/Open WebUI/2026-06-29-29-other-changes-in-v0-10-0|29 other changes in v0.10.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Voice and Audio

- Earlier: 2026-06-29 · ElevenLabs · [[Changes/ElevenLabs/2026-06-29-speech-to-text-b8f62a|Speech to Text]]
- Later: 2026-06-30 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-06-30-voice-mode-turns-itself-off-when-the-engine-fails-to-start-at-boot|Voice mode turns itself off when the engine fails to start at boot]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-10 · Dify · [[Changes/Dify/2023-07-10-2-voice-and-audio-changes-in-0-3-7|2 Voice and Audio changes in 0.3.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-06-29-0a4042&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-06-29-3-voice-and-audio-changes-in-v0-10-0.md%0ACard%20ID%3A%20open-webui-2026-06-29-0a4042%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.10.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->