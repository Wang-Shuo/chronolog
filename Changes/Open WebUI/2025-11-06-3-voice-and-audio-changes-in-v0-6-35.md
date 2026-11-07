---
card_id: open-webui-2025-11-06-1d1551
date: '2025-11-06'
description: "Open WebUI · 2025-11-06 · Voice and Audio: 3 changes in v0.6.35 — \U0001F50A
  Text-to-speech now uses a global audio queue system to prevent overlapping playback…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-07-09-type-in-parentheses-to-add-notes-to-your-script-that-don-t-affect-the-audio-text|Support
    for Inline Notes]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2677
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: voice
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: e61b2c1c1aee0d41486a8c64df993d63f61d81616c42f4d8fe93c3f7791cf9da
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-11-06-1d1551
  comparison: ''
  date: '2025-11-06'
  description: 'Open WebUI — v0.6.35: 3 Voice and Audio changes'
  evidence:
  - quote: "\U0001F50A Text-to-speech now uses a global audio queue system to prevent
      overlapping playback, ensuring only one TTS instance plays at a time with proper
      stop/start controls and automatic cleanup when switching between messages. [#16152](https://github.com/open-webui/open-webui/pull/16152),
      [#18744](https://github.com/open-webui/open-webui/pull/18744), [#16150](https://github.com/open-webui/open-webui/issues/16150)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  - quote: "\U0001F399️ Speech-to-text transcription no longer deletes or replaces
      existing text in the prompt input field, properly preserving any previously
      entered content. [#18540](https://github.com/open-webui/open-webui/issues/18540)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  - quote: "\U0001F399️ The \"Instant Auto-Send After Voice Transcription\" setting
      now functions correctly and automatically sends transcribed text when enabled.
      [#18466](https://github.com/open-webui/open-webui/issues/18466)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 3-voice-and-audio-changes-in-v0-6-35
  source_release: open-webui-2025-11-06-v0-6-35-github-260376122-7fa65234
  source_type: github_releases
  theme: voice
  title: 3 Voice and Audio changes in v0.6.35
  type: change
related_changes:
- '[[Changes/ElevenLabs/2025-11-05-music-api-0953e5|Music API]]'
- '[[Changes/ElevenLabs/2025-11-05-text-to-dialogue|Text to Dialogue]]'
- '[[Changes/ElevenLabs/2025-11-05-text-to-dialogue-7d0842|Text to Dialogue]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-11-06-v0-6-35-github-260376122-7fa65234|open-webui-2025-11-06-v0-6-35-github-260376122-7fa65234]]'
source_type: github_releases
theme: voice
title: 3 Voice and Audio changes in v0.6.35
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Voice and Audio changes in v0.6.35

**Open WebUI** · 2025-11-06 · [[Themes/voice|Voice and Audio]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.35) · from [[Releases/Open WebUI/open-webui-2025-11-06-v0-6-35-github-260376122-7fa65234|v0.6.35]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔊 Text-to-speech now uses a global audio queue system to prevent overlapping playback, ensuring only one TTS instance plays at a time with proper stop/start controls and automatic cleanup when switching between messages. [#16152](https://github.com/open-webui/open-webui/pull/16152), [#18744](https://github.com/open-webui/open-webui/pull/18744), [#16150](https://github.com/open-webui/open-webui/issues/16150)

> 🎙️ Speech-to-text transcription no longer deletes or replaces existing text in the prompt input field, properly preserving any previously entered content. [#18540](https://github.com/open-webui/open-webui/issues/18540)

> 🎙️ The "Instant Auto-Send After Voice Transcription" setting now functions correctly and automatically sends transcribed text when enabled. [#18466](https://github.com/open-webui/open-webui/issues/18466)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-11-06-chat-controls-button-is-now-properly-hidden-on-mobile-for-users-without-admin-or|📱 Chat controls button is now properly hidden on mobile for users without admin…]] · Mobile and Desktop
- [[Changes/Open WebUI/2025-11-06-10-model-support-changes-in-v0-6-35|10 Model Support changes in v0.6.35]] · Model Support
- [[Changes/Open WebUI/2025-11-06-2-multimodal-input-changes-in-v0-6-35|2 Multimodal Input changes in v0.6.35]] · Multimodal Input
- [[Changes/Open WebUI/2025-11-06-4-safety-and-privacy-changes-in-v0-6-35|4 Safety and Privacy changes in v0.6.35]] · Safety and Privacy
- [[Changes/Open WebUI/2025-11-06-3-developer-workflow-changes-in-v0-6-35|3 Developer Workflow changes in v0.6.35]] · Developer Workflow
- [[Changes/Open WebUI/2025-11-06-10-interface-experience-changes-in-v0-6-35|10 Interface Experience changes in v0.6.35]] · Interface Experience
- [[Changes/Open WebUI/2025-11-06-3-editor-experience-changes-in-v0-6-35|3 Editor Experience changes in v0.6.35]] · Editor Experience
- [[Changes/Open WebUI/2025-11-06-4-search-and-browsing-changes-in-v0-6-35|4 Search and Browsing changes in v0.6.35]] · Search and Browsing
- [[Changes/Open WebUI/2025-11-06-3-reliability-and-performance-changes-in-v0-6-35|3 Reliability and Performance changes in v0.6.35]] · Reliability and Performance
- [[Changes/Open WebUI/2025-11-06-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-11-06-3-context-window-changes-in-v0-6-35|3 Context Window changes in v0.6.35]] · Context Window
- [[Changes/Open WebUI/2025-11-06-edit-button-is-now-available-in-the-three-dot-menu-of-models-in-the-workspace-se|✏️ Edit button is now available in the three-dot menu of models in the workspace…]] · Model Support
- [[Changes/Open WebUI/2025-11-06-screen-reader-support-was-enhanced-by-wrapping-messages-in-semantic-elements-wit|♿ Screen reader support was enhanced by wrapping messages in semantic elements…]] · Accessibility and Localization
- [[Changes/Open WebUI/2025-11-06-external-document-loaders-can-now-optionally-forward-user-information-headers-wh|📄 External document loaders can now optionally forward user information headers…]] · Pricing Model
- [[Changes/Open WebUI/2025-11-06-3-files-and-data-changes-in-v0-6-35|3 Files and Data changes in v0.6.35]] · Files and Data
- [[Changes/Open WebUI/2025-11-06-2-apps-and-integrations-changes-in-v0-6-35|2 Apps and Integrations changes in v0.6.35]] · Apps and Integrations
- [[Changes/Open WebUI/2025-11-06-5-account-and-access-changes-in-v0-6-35|5 Account and Access changes in v0.6.35]] · Account and Access
- [[Changes/Open WebUI/2025-11-06-22-other-changes-in-v0-6-35|22 other changes in v0.6.35]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Voice and Audio

- Earlier: 2025-11-05 · ElevenLabs · [[Changes/ElevenLabs/2025-11-05-text-to-dialogue-7d0842|Text to Dialogue]]
- Later: 2025-11-12 · ElevenLabs · [[Changes/ElevenLabs/2025-11-12-voice-management|Voice Management]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-07-09 · Descript · [[Changes/Descript/2018-07-09-type-in-parentheses-to-add-notes-to-your-script-that-don-t-affect-the-audio-text|Support for Inline Notes]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-11-06-1d1551&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-11-06-3-voice-and-audio-changes-in-v0-6-35.md%0ACard%20ID%3A%20open-webui-2025-11-06-1d1551%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.35%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->