---
card_id: open-webui-2026-09-21-616362
date: '2026-09-21'
description: "Open WebUI · 2026-09-21 · Voice and Audio: 5 changes in v0.11.4 — \U0001F39A️
  **Partial settings permissions.** An account barred from changing the interface
  settings…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-07-09-type-in-parentheses-to-add-notes-to-your-script-that-don-t-affect-the-audio-text|Support
    for Inline Notes]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2996
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: voice
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ea75ed84a7dd5b734ce33608d2b1dd2c689dae00bd3a06723c81575d71aaf188
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-09-21-616362
  comparison: ''
  date: '2026-09-21'
  description: 'Open WebUI — v0.11.4: 5 Voice and Audio changes'
  evidence:
  - quote: "\U0001F39A️ **Partial settings permissions.** An account barred from changing
      the interface settings can now save its system prompt, notifications, audio,
      keyboard shortcuts and pinned models, which were refused along with them. [Commit](https://github.com/open-webui/open-webui/commit/98a920168e2eea435ac15e1ad3d679946631e41d)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F3A7 **Speech file types kept.** Saving the audio settings emptied
      the list of file types accepted for speech recognition, so transcription then
      turned away the recordings it had taken before. [#30208](https://github.com/open-webui/open-webui/pull/30208)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F4E2 **Speech engine defaults.** Switching the text to speech engine
      now applies that engine's own default voice and model, where the change kept
      the previous engine's settings in place. [#30289](https://github.com/open-webui/open-webui/pull/30289),
      [#30288](https://github.com/open-webui/open-webui/issues/30288)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F3CE️ **Faster media page reads.** The browser-driven loader pulled
      every image, video and font a page referenced down through the server before
      any text was extracted, so a page carrying a few dozen audio players took ten
      seconds or timed out. Those requests are now dropped before they are made, and
      the same page comes back in under three seconds, having pulled 4 MB where it
      used to pull 55. [#29742](https://github.com/open-webui/open-webui/pull/29742),
      [#29741](https://github.com/open-webui/open-webui/issues/29741)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F399️ **Slim speech requirements.** The slim image carries neither
      local Whisper nor local voices, so speech to text and text to speech need an
      external engine before they will work. [Commit](https://github.com/open-webui/open-webui/commit/cb942bb94c8dc7941336088fb3392e2398ff56c1)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 5-voice-and-audio-changes-in-v0-11-4
  source_release: open-webui-2026-09-21-v0-11-4-github-393232555-90de9130
  source_type: github_releases
  theme: voice
  title: 5 Voice and Audio changes in v0.11.4
  type: change
related_changes:
- '[[Changes/Qoder/2026-09-18-voice-input-press-and-hold-the-mouse-button-in-the-chat-input-box-to-dictate-rel|Voice
  input: Press and hold the mouse button in the chat input box to dictate]]'
- '[[Changes/OpenClaw/2026-09-19-15-voice-and-audio-changes-in-v2026-9-5|15 Voice
  and Audio changes in v2026.9.5]]'
- '[[Changes/ElevenLabs/2026-09-21-text-to-speech|Text to Speech]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-09-21-v0-11-4-github-393232555-90de9130|open-webui-2026-09-21-v0-11-4-github-393232555-90de9130]]'
source_type: github_releases
theme: voice
title: 5 Voice and Audio changes in v0.11.4
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Voice and Audio changes in v0.11.4

**Open WebUI** · 2026-09-21 · [[Themes/voice|Voice and Audio]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.4) · from [[Releases/Open WebUI/open-webui-2026-09-21-v0-11-4-github-393232555-90de9130|v0.11.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🎚️ **Partial settings permissions.** An account barred from changing the interface settings can now save its system prompt, notifications, audio, keyboard shortcuts and pinned models, which were refused along with them. [Commit](https://github.com/open-webui/open-webui/commit/98a920168e2eea435ac15e1ad3d679946631e41d)

> 🎧 **Speech file types kept.** Saving the audio settings emptied the list of file types accepted for speech recognition, so transcription then turned away the recordings it had taken before. [#30208](https://github.com/open-webui/open-webui/pull/30208)

> 📢 **Speech engine defaults.** Switching the text to speech engine now applies that engine's own default voice and model, where the change kept the previous engine's settings in place. [#30289](https://github.com/open-webui/open-webui/pull/30289), [#30288](https://github.com/open-webui/open-webui/issues/30288)

> 🏎️ **Faster media page reads.** The browser-driven loader pulled every image, video and font a page referenced down through the server before any text was extracted, so a page carrying a few dozen audio players took ten seconds or timed out. Those requests are now dropped before they are made, and the same page comes back in under three seconds, having pulled 4 MB where it used to pull 55. [#29742](https://github.com/open-webui/open-webui/pull/29742), [#29741](https://github.com/open-webui/open-webui/issues/29741)

> 🎙️ **Slim speech requirements.** The slim image carries neither local Whisper nor local voices, so speech to text and text to speech need an external engine before they will work. [Commit](https://github.com/open-webui/open-webui/commit/cb942bb94c8dc7941336088fb3392e2398ff56c1)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-09-21-4-safety-and-privacy-changes-in-v0-11-4|4 Safety and Privacy changes in v0.11.4]] · Safety and Privacy
- [[Changes/Open WebUI/2026-09-21-3-context-window-changes-in-v0-11-4|3 Context Window changes in v0.11.4]] · Context Window
- [[Changes/Open WebUI/2026-09-21-general-improvements-various-improvements-were-implemented-across-the-applicatio|🔄 General improvements. Various improvements were implemented across…]] · Reliability and Performance
- [[Changes/Open WebUI/2026-09-21-6-account-and-access-changes-in-v0-11-4|6 Account and Access changes in v0.11.4]] · Account and Access
- [[Changes/Open WebUI/2026-09-21-39-developer-workflow-changes-in-v0-11-4|39 Developer Workflow changes in v0.11.4]] · Developer Workflow
- [[Changes/Open WebUI/2026-09-21-2-image-generation-changes-in-v0-11-4|2 Image Generation changes in v0.11.4]] · Image Generation
- [[Changes/Open WebUI/2026-09-21-4-collaboration-changes-in-v0-11-4|4 Collaboration changes in v0.11.4]] · Collaboration
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
## Nearby in Voice and Audio

- Earlier: 2026-09-21 · ElevenLabs · [[Changes/ElevenLabs/2026-09-21-text-to-speech|Text to Speech]]
- Later: 2026-09-22 · Codex CLI · [[Changes/Codex CLI/2026-09-22-17-voice-and-audio-changes-in-rust-v0-156-0|17 Voice and Audio changes in rust-v0.156.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-07-09 · Descript · [[Changes/Descript/2018-07-09-type-in-parentheses-to-add-notes-to-your-script-that-don-t-affect-the-audio-text|Support for Inline Notes]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-09-21-616362&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-09-21-5-voice-and-audio-changes-in-v0-11-4.md%0ACard%20ID%3A%20open-webui-2026-09-21-616362%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.4%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->