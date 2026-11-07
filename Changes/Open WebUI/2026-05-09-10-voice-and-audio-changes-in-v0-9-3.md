---
card_id: open-webui-2026-05-09-200623
date: '2026-05-09'
description: "Open WebUI · 2026-05-09 · Voice and Audio: 10 changes in v0.9.3 — \U0001F507
  **Voice Mode mute control.** Voice Mode now includes a dedicated mute toggle with
  an \"M\"…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-07-09-type-in-parentheses-to-add-notes-to-your-script-that-don-t-affect-the-audio-text|Support
    for Inline Notes]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2861
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: voice
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9c0e421d5f3fd86cdeb4c52b9940a3a8d89e1353b3017d415802ca58cb7af156
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-05-09-200623
  comparison: ''
  date: '2026-05-09'
  description: 'Open WebUI — v0.9.3: 10 Voice and Audio changes'
  evidence:
  - quote: "\U0001F507 **Voice Mode mute control.** Voice Mode now includes a dedicated
      mute toggle with an \"M\" shortcut and auto-unmute after assistant playback,
      so you can prevent accidental interruptions from background noise without leaving
      the call overlay. [Commit](https://github.com/open-webui/open-webui/commit/072d2000f35a9f7b96342fa9bb28f925a92e7b4c),
      [#23832](https://github.com/open-webui/open-webui/issues/23832)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F399️ **STT file extension controls.** Administrators can now configure
      which audio file extensions are accepted for speech-to-text uploads, helping
      enforce safer and more predictable upload policies. [Commit](https://github.com/open-webui/open-webui/commit/4754ece4a2de5bba85a1d53af2dc8d24fdfb58be)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F4F7 **Remembered call camera selection.** Voice call overlay now
      remembers your last selected camera and restores it automatically when available,
      so you do not need to reselect it every time you start voice mode. [Commit](https://github.com/open-webui/open-webui/commit/5c3edc2539ac4d92c4cc2d37079549995203238a),
      [#24416](https://github.com/open-webui/open-webui/issues/24416)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F3A4 **Voice mode prompt toggle.** Administrators can now explicitly
      enable or disable the Voice Mode custom prompt behavior from Interface settings,
      giving finer control over how voice replies are guided. [Commit](https://github.com/open-webui/open-webui/commit/17893038869e3a763a8b34457f723b9666804e27)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F399️ **Voice recording MIME fallback support.** Voice recording
      now tries a broader set of browser-supported audio formats and resets halted
      audio playback cleanly, improving microphone capture reliability in browsers
      where recording previously failed to start. [Commit](https://github.com/open-webui/open-webui/commit/8ffc3d746f20007e9eb4e3ae4f152f383bc371e1),
      [#24162](https://github.com/open-webui/open-webui/issues/24162)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F3A7 **Safer voice transcription uploads.** Empty or failed voice
      conversions are now rejected with a clear error instead of continuing as malformed
      audio, reducing failed transcription attempts from corrupted or near-empty recordings.
      [Commit](https://github.com/open-webui/open-webui/commit/072d2000f35a9f7b96342fa9bb28f925a92e7b4c)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F39A️ **Safer chunked STT processing.** Chunked transcription now
      limits worker concurrency when no external STT engine is configured, reducing
      failed transcription behavior caused by overly parallel local processing. [Commit](https://github.com/open-webui/open-webui/commit/55e7c7854bba5182803239c903a0ac2d14426a4c)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F50A **PCM TTS playback compatibility.** Text-to-speech audio returned
      as PCM is now converted to MP3 before delivery, so speech playback works correctly
      with providers that return raw PCM audio. [Commit](https://github.com/open-webui/open-webui/commit/ff791b4814fc1453df2235ea78016d7015aa6806),
      [#24143](https://github.com/open-webui/open-webui/issues/24143)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F3A4 **Non-blocking STT processing.** Speech-to-text transcription
      no longer blocks the server event loop during both live transcription and uploaded
      audio file processing, so other users can continue using chats and live connections
      under concurrent load. [#24338](https://github.com/open-webui/open-webui/pull/24338),
      [#24379](https://github.com/open-webui/open-webui/pull/24379), [#24169](https://github.com/open-webui/open-webui/issues/24169)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F6E1️ **Safer cached file delivery.** Cached files that are not
      recognized as image, audio, or video now download as attachments instead of
      rendering inline, reducing the risk of unsafe browser content handling. [Commit](https://github.com/open-webui/open-webui/commit/4754ece4a2de5bba85a1d53af2dc8d24fdfb58be)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 10-voice-and-audio-changes-in-v0-9-3
  source_release: open-webui-2026-05-09-v0-9-3-github-319872270-bb8aabca
  source_type: github_releases
  theme: voice
  title: 10 Voice and Audio changes in v0.9.3
  type: change
related_changes:
- '[[Changes/Gemini CLI/2026-05-05-feat-voice-implement-real-time-voice-mode-with-cloud-and-local-backends-by-abhij|feat(voice):
  implement real-time voice mode with cloud and local backends]]'
- '[[Changes/Raycast/2026-05-08-dictation-brings-fast-accurate-voice-to-text-to-raycast-on-mac-press-your-hotkey|Dictation
  brings fast, accurate voice-to-text to Raycast on Mac]]'
- '[[Changes/Raycast/2026-05-08-2-voice-and-audio-changes-in-raycast-macos-0-57|2
  Voice and Audio changes in Raycast macos 0.57]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-05-09-v0-9-3-github-319872270-bb8aabca|open-webui-2026-05-09-v0-9-3-github-319872270-bb8aabca]]'
source_type: github_releases
theme: voice
title: 10 Voice and Audio changes in v0.9.3
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Voice and Audio changes in v0.9.3

**Open WebUI** · 2026-05-09 · [[Themes/voice|Voice and Audio]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.3) · from [[Releases/Open WebUI/open-webui-2026-05-09-v0-9-3-github-319872270-bb8aabca|v0.9.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔇 **Voice Mode mute control.** Voice Mode now includes a dedicated mute toggle with an "M" shortcut and auto-unmute after assistant playback, so you can prevent accidental interruptions from background noise without leaving the call overlay. [Commit](https://github.com/open-webui/open-webui/commit/072d2000f35a9f7b96342fa9bb28f925a92e7b4c), [#23832](https://github.com/open-webui/open-webui/issues/23832)

> 🎙️ **STT file extension controls.** Administrators can now configure which audio file extensions are accepted for speech-to-text uploads, helping enforce safer and more predictable upload policies. [Commit](https://github.com/open-webui/open-webui/commit/4754ece4a2de5bba85a1d53af2dc8d24fdfb58be)

> 📷 **Remembered call camera selection.** Voice call overlay now remembers your last selected camera and restores it automatically when available, so you do not need to reselect it every time you start voice mode. [Commit](https://github.com/open-webui/open-webui/commit/5c3edc2539ac4d92c4cc2d37079549995203238a), [#24416](https://github.com/open-webui/open-webui/issues/24416)

> 🎤 **Voice mode prompt toggle.** Administrators can now explicitly enable or disable the Voice Mode custom prompt behavior from Interface settings, giving finer control over how voice replies are guided. [Commit](https://github.com/open-webui/open-webui/commit/17893038869e3a763a8b34457f723b9666804e27)

> 🎙️ **Voice recording MIME fallback support.** Voice recording now tries a broader set of browser-supported audio formats and resets halted audio playback cleanly, improving microphone capture reliability in browsers where recording previously failed to start. [Commit](https://github.com/open-webui/open-webui/commit/8ffc3d746f20007e9eb4e3ae4f152f383bc371e1), [#24162](https://github.com/open-webui/open-webui/issues/24162)

> 🎧 **Safer voice transcription uploads.** Empty or failed voice conversions are now rejected with a clear error instead of continuing as malformed audio, reducing failed transcription attempts from corrupted or near-empty recordings. [Commit](https://github.com/open-webui/open-webui/commit/072d2000f35a9f7b96342fa9bb28f925a92e7b4c)

> 🎚️ **Safer chunked STT processing.** Chunked transcription now limits worker concurrency when no external STT engine is configured, reducing failed transcription behavior caused by overly parallel local processing. [Commit](https://github.com/open-webui/open-webui/commit/55e7c7854bba5182803239c903a0ac2d14426a4c)

> 🔊 **PCM TTS playback compatibility.** Text-to-speech audio returned as PCM is now converted to MP3 before delivery, so speech playback works correctly with providers that return raw PCM audio. [Commit](https://github.com/open-webui/open-webui/commit/ff791b4814fc1453df2235ea78016d7015aa6806), [#24143](https://github.com/open-webui/open-webui/issues/24143)

> 🎤 **Non-blocking STT processing.** Speech-to-text transcription no longer blocks the server event loop during both live transcription and uploaded audio file processing, so other users can continue using chats and live connections under concurrent load. [#24338](https://github.com/open-webui/open-webui/pull/24338), [#24379](https://github.com/open-webui/open-webui/pull/24379), [#24169](https://github.com/open-webui/open-webui/issues/24169)

> 🛡️ **Safer cached file delivery.** Cached files that are not recognized as image, audio, or video now download as attachments instead of rendering inline, reducing the risk of unsafe browser content handling. [Commit](https://github.com/open-webui/open-webui/commit/4754ece4a2de5bba85a1d53af2dc8d24fdfb58be)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-05-09-5-search-and-browsing-changes-in-v0-9-3|5 Search and Browsing changes in v0.9.3]] · Search and Browsing
- [[Changes/Open WebUI/2026-05-09-5-editor-experience-changes-in-v0-9-3|5 Editor Experience changes in v0.9.3]] · Editor Experience
- [[Changes/Open WebUI/2026-05-09-8-interface-experience-changes-in-v0-9-3|8 Interface Experience changes in v0.9.3]] · Interface Experience
- [[Changes/Open WebUI/2026-05-09-4-context-window-changes-in-v0-9-3|4 Context Window changes in v0.9.3]] · Context Window
- [[Changes/Open WebUI/2026-05-09-3-apps-and-integrations-changes-in-v0-9-3|3 Apps and Integrations changes in v0.9.3]] · Apps and Integrations
- [[Changes/Open WebUI/2026-05-09-2-automation-and-scheduling-changes-in-v0-9-3|2 Automation and Scheduling changes in v0.9.3]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-05-09-22-developer-workflow-changes-in-v0-9-3|22 Developer Workflow changes in v0.9.3]] · Developer Workflow
- [[Changes/Open WebUI/2026-05-09-4-reliability-and-performance-changes-in-v0-9-3|4 Reliability and Performance changes in v0.9.3]] · Reliability and Performance
- [[Changes/Open WebUI/2026-05-09-4-account-and-access-changes-in-v0-9-3|4 Account and Access changes in v0.9.3]] · Account and Access
- [[Changes/Open WebUI/2026-05-09-sanitized-spreadsheet-html-previews-spreadsheet-previews-now-sanitize-generated|🛡️ Sanitized spreadsheet HTML previews. Spreadsheet previews now sanitize…]] · Files and Data
- [[Changes/Open WebUI/2026-05-09-9-model-support-changes-in-v0-9-3|9 Model Support changes in v0.9.3]] · Model Support
- [[Changes/Open WebUI/2026-05-09-3-safety-and-privacy-changes-in-v0-9-3|3 Safety and Privacy changes in v0.9.3]] · Safety and Privacy
- [[Changes/Open WebUI/2026-05-09-faster-memory-query-performance-per-user-memory-lookups-and-deletions-now-run-mu|⚡ Faster memory query performance. Per-user memory lookups and deletions now run…]] · Memory and Personalization
- [[Changes/Open WebUI/2026-05-09-5-other-changes-in-v0-9-3|5 other changes in v0.9.3]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Voice and Audio

- Earlier: 2026-05-08 · Raycast · [[Changes/Raycast/2026-05-08-2-voice-and-audio-changes-in-raycast-macos-0-57|2 Voice and Audio changes in Raycast macos 0.57]]
- Later: 2026-05-12 · Dify · [[Changes/Dify/2026-05-12-audio-and-transcript-behavior-explicitly-resume-audiocontext-and-play-audio-on-f|Audio and transcript behavior]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-07-09 · Descript · [[Changes/Descript/2018-07-09-type-in-parentheses-to-add-notes-to-your-script-that-don-t-affect-the-audio-text|Support for Inline Notes]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-05-09-200623&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-05-09-10-voice-and-audio-changes-in-v0-9-3.md%0ACard%20ID%3A%20open-webui-2026-05-09-200623%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.3%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->