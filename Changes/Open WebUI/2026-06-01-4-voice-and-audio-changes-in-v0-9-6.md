---
card_id: open-webui-2026-06-01-fc2a0c
date: '2026-06-01'
description: "Open WebUI · 2026-06-01 · Voice and Audio: 4 changes in v0.9.6 — \U0001F50A
  **Non-blocking text-to-speech transcoding.** Converting text-to-speech audio to
  MP3 no…"
diffusion:
  first_in_tracked: '[[Changes/Dify/2023-07-10-2-voice-and-audio-changes-in-0-3-7|2
    Voice and Audio changes in 0.3.7]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1057
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: voice
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d48f7c0cc9fceb2c9e53c08b4bd675ed4029f016a272f92c30cce8f4da716bf4
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-06-01-fc2a0c
  comparison: ''
  date: '2026-06-01'
  description: 'Open WebUI — v0.9.6: 4 Voice and Audio changes'
  evidence:
  - quote: "\U0001F50A **Non-blocking text-to-speech transcoding.** Converting text-to-speech
      audio to MP3 no longer blocks the server's event loop, so other requests stay
      responsive even while a TTS response is being transcoded. [#24876](https://github.com/open-webui/open-webui/pull/24876)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F39A️ **Default text-to-speech voice.** Text-to-speech requests
      now honor the voice specified in the request and fall back to the configured
      default only when none is given, instead of always using the admin default or
      failing. [#15143](https://github.com/open-webui/open-webui/issues/15143), [#25035](https://github.com/open-webui/open-webui/issues/25035),
      [Commit](https://github.com/open-webui/open-webui/commit/f16b5c446027eae1bd767617bac2fdf54b24d6fc),
      [Commit](https://github.com/open-webui/open-webui/commit/750604a11d4adcb5ae568b9fc93010031ad394f9)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F399️ **Voice mode mute shortcut listing.** The keyboard shortcut
      for muting voice mode now appears in the keyboard shortcuts help modal. [#25193](https://github.com/open-webui/open-webui/pull/25193)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F50A **Speech-to-text SSL setting honored.** Speech-to-text requests
      now respect the \"AIOHTTP_CLIENT_SESSION_SSL\" setting, so administrators using
      self-signed certificates or custom SSL configurations can use STT engines that
      were previously failing TLS verification. [#24568](https://github.com/open-webui/open-webui/issues/24568),
      [#24857](https://github.com/open-webui/open-webui/pull/24857), [Commit](https://github.com/open-webui/open-webui/commit/2ca91ceeeca6a6a21e5a6ad68ea3ab8c9d9f6deb),
      [Commit](https://github.com/open-webui/open-webui/commit/94b66b17972e0ad77954df4b81a6bb86a7a6a04b)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 4-voice-and-audio-changes-in-v0-9-6
  source_release: open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e
  source_type: github_releases
  theme: voice
  title: 4 Voice and Audio changes in v0.9.6
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-06-01-speech-to-text|Speech to Text]]'
- '[[Changes/ElevenLabs/2026-06-01-speech-to-text-9a648b|Speech to Text]]'
- '[[Changes/ElevenLabs/2026-06-01-dubbing-fad5c5|Dubbing]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e|open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e]]'
source_type: github_releases
theme: voice
title: 4 Voice and Audio changes in v0.9.6
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Voice and Audio changes in v0.9.6

**Open WebUI** · 2026-06-01 · [[Themes/voice|Voice and Audio]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.6) · from [[Releases/Open WebUI/open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e|v0.9.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔊 **Non-blocking text-to-speech transcoding.** Converting text-to-speech audio to MP3 no longer blocks the server's event loop, so other requests stay responsive even while a TTS response is being transcoded. [#24876](https://github.com/open-webui/open-webui/pull/24876)

> 🎚️ **Default text-to-speech voice.** Text-to-speech requests now honor the voice specified in the request and fall back to the configured default only when none is given, instead of always using the admin default or failing. [#15143](https://github.com/open-webui/open-webui/issues/15143), [#25035](https://github.com/open-webui/open-webui/issues/25035), [Commit](https://github.com/open-webui/open-webui/commit/f16b5c446027eae1bd767617bac2fdf54b24d6fc), [Commit](https://github.com/open-webui/open-webui/commit/750604a11d4adcb5ae568b9fc93010031ad394f9)

> 🎙️ **Voice mode mute shortcut listing.** The keyboard shortcut for muting voice mode now appears in the keyboard shortcuts help modal. [#25193](https://github.com/open-webui/open-webui/pull/25193)

> 🔊 **Speech-to-text SSL setting honored.** Speech-to-text requests now respect the "AIOHTTP_CLIENT_SESSION_SSL" setting, so administrators using self-signed certificates or custom SSL configurations can use STT engines that were previously failing TLS verification. [#24568](https://github.com/open-webui/open-webui/issues/24568), [#24857](https://github.com/open-webui/open-webui/pull/24857), [Commit](https://github.com/open-webui/open-webui/commit/2ca91ceeeca6a6a21e5a6ad68ea3ab8c9d9f6deb), [Commit](https://github.com/open-webui/open-webui/commit/94b66b17972e0ad77954df4b81a6bb86a7a6a04b)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-06-01-bulk-enable-or-disable-automations-automations-can-now-be-enabled-or-disabled-in|🔘 Bulk enable or disable automations. Automations can now be enabled or disabled…]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-06-01-4-context-window-changes-in-v0-9-6|4 Context Window changes in v0.9.6]] · Context Window
- [[Changes/Open WebUI/2026-06-01-2-memory-and-personalization-changes-in-v0-9-6|2 Memory and Personalization changes in v0.9.6]] · Memory and Personalization
- [[Changes/Open WebUI/2026-06-01-keyboard-and-screen-reader-access-to-menus-the-integrations-more-options-and-use|♿ Keyboard and screen reader access to menus. The integrations, more-options…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-06-01-27-developer-workflow-changes-in-v0-9-6|27 Developer Workflow changes in v0.9.6]] · Developer Workflow
- [[Changes/Open WebUI/2026-06-01-4-interface-experience-changes-in-v0-9-6|4 Interface Experience changes in v0.9.6]] · Interface Experience
- [[Changes/Open WebUI/2026-06-01-4-editor-experience-changes-in-v0-9-6|4 Editor Experience changes in v0.9.6]] · Editor Experience
- [[Changes/Open WebUI/2026-06-01-5-files-and-data-changes-in-v0-9-6|5 Files and Data changes in v0.9.6]] · Files and Data
- [[Changes/Open WebUI/2026-06-01-7-safety-and-privacy-changes-in-v0-9-6|7 Safety and Privacy changes in v0.9.6]] · Safety and Privacy
- [[Changes/Open WebUI/2026-06-01-startup-on-non-unicode-consoles-open-webui-no-longer-crashes-at-startup-when-the|🥾 Startup on non-Unicode consoles. Open WebUI no longer crashes at startup…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-06-01-youtube-short-link-transcripts-pasting-a-youtu-be-short-link-into-a-chat-now-loa|📺 YouTube short link transcripts. Pasting a "youtu.be" short link into a chat…]] · Multimodal Input
- [[Changes/Open WebUI/2026-06-01-9-search-and-browsing-changes-in-v0-9-6|9 Search and Browsing changes in v0.9.6]] · Search and Browsing
- [[Changes/Open WebUI/2026-06-01-shared-chat-file-write-protection-access-to-a-file-through-a-shared-chat-now-onl|🔐 Shared-chat file write protection. Access to a file through a shared chat now…]] · Collaboration
- [[Changes/Open WebUI/2026-06-01-2-enterprise-and-administration-changes-in-v0-9-6|2 Enterprise and Administration changes in v0.9.6]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-06-01-image-generation-with-non-standard-response-headers-image-generation-now-works-w|🖌️ Image generation with non-standard response headers. Image generation now…]] · Image Generation
- [[Changes/Open WebUI/2026-06-01-6-account-and-access-changes-in-v0-9-6|6 Account and Access changes in v0.9.6]] · Account and Access
- [[Changes/Open WebUI/2026-06-01-12-model-support-changes-in-v0-9-6|12 Model Support changes in v0.9.6]] · Model Support
- [[Changes/Open WebUI/2026-06-01-4-apps-and-integrations-changes-in-v0-9-6|4 Apps and Integrations changes in v0.9.6]] · Apps and Integrations
- [[Changes/Open WebUI/2026-06-01-5-reliability-and-performance-changes-in-v0-9-6|5 Reliability and Performance changes in v0.9.6]] · Reliability and Performance
- [[Changes/Open WebUI/2026-06-01-20-other-changes-in-v0-9-6|20 other changes in v0.9.6]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Voice and Audio

- Earlier: 2026-06-01 · ElevenLabs · [[Changes/ElevenLabs/2026-06-01-dubbing-fad5c5|Dubbing]]
- Later: 2026-06-02 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-06-02-add-the-voice-command-to-dictate-prompts-using-local-speech-to-text-models|Add the /voice command to dictate prompts using local speech-to-text models]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-10 · Dify · [[Changes/Dify/2023-07-10-2-voice-and-audio-changes-in-0-3-7|2 Voice and Audio changes in 0.3.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-06-01-fc2a0c&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-06-01-4-voice-and-audio-changes-in-v0-9-6.md%0ACard%20ID%3A%20open-webui-2026-06-01-fc2a0c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.6%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->