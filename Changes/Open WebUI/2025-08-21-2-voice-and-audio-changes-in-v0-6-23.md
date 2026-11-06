---
card_id: open-webui-2025-08-21-4c4f8f
date: '2025-08-21'
description: "Open WebUI · 2025-08-21 · Voice and Audio: 2 changes in v0.6.23 — \U0001F4C1
  **Asynchronous File Upload with Polling**: Implemented an asynchronous file upload
  process…"
diffusion:
  first_in_tracked: '[[Changes/Dify/2023-07-10-2-voice-and-audio-changes-in-0-3-7|2
    Voice and Audio changes in 0.3.7]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 773
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: voice
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ad7d221ecdec793b5696c299eb3add3e4b19616991373c690fbe74f673641061
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-08-21-4c4f8f
  comparison: ''
  date: '2025-08-21'
  description: 'Open WebUI — v0.6.23: 2 Voice and Audio changes'
  evidence:
  - quote: "\U0001F4C1 **Asynchronous File Upload with Polling**: Implemented an asynchronous
      file upload process with frontend polling to resolve gateway timeouts and improve
      reliability when uploading large files. This ensures that even lengthy file
      processing, such as embedding or transcription, does not block the user interface
      or lead to connection timeouts, providing a smoother experience for all file
      operations."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  - quote: "\U0001F5E3️ **Enhanced Audio Transcription Language Fallback and Deepgram
      Support**: Implemented a robust language fallback mechanism for both OpenAI
      and Deepgram Speech-to-Text (STT) API calls. If a specified language parameter
      is not supported by the model or provider, the system will now intelligently
      retry the transcription without the language parameter or with a default, ensuring
      greater reliability and preventing failed API calls. This also specifically
      adds and refines support for the audio language parameter in Deepgram API integrations."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 2-voice-and-audio-changes-in-v0-6-23
  source_release: open-webui-2025-08-21-v0-6-23-github-241603918-5e4a7f46
  source_type: github_releases
  theme: voice
  title: 2 Voice and Audio changes in v0.6.23
  type: change
related_changes:
- "[[Changes/Open WebUI/2025-08-09-admin-first-whisper-language-priority-the-global-whisper-language-setting-now-ac|\U0001F5E3️
  Admin-First Whisper Language Priority]]"
- '[[Changes/ElevenLabs/2025-08-20-voice-management|Voice Management]]'
- '[[Changes/ElevenLabs/2025-08-20-speech-to-text|Speech to Text]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-08-21-v0-6-23-github-241603918-5e4a7f46|open-webui-2025-08-21-v0-6-23-github-241603918-5e4a7f46]]'
source_type: github_releases
theme: voice
title: 2 Voice and Audio changes in v0.6.23
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Voice and Audio changes in v0.6.23

**Open WebUI** · 2025-08-21 · [[Themes/voice|Voice and Audio]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.23) · from [[Releases/Open WebUI/open-webui-2025-08-21-v0-6-23-github-241603918-5e4a7f46|v0.6.23]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📁 **Asynchronous File Upload with Polling**: Implemented an asynchronous file upload process with frontend polling to resolve gateway timeouts and improve reliability when uploading large files. This ensures that even lengthy file processing, such as embedding or transcription, does not block the user interface or lead to connection timeouts, providing a smoother experience for all file operations.

> 🗣️ **Enhanced Audio Transcription Language Fallback and Deepgram Support**: Implemented a robust language fallback mechanism for both OpenAI and Deepgram Speech-to-Text (STT) API calls. If a specified language parameter is not supported by the model or provider, the system will now intelligently retry the transcription without the language parameter or with a default, ensuring greater reliability and preventing failed API calls. This also specifically adds and refines support for the audio language parameter in Deepgram API integrations.

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-08-21-8-interface-experience-changes-in-v0-6-23|8 Interface Experience changes in v0.6.23]] · Interface Experience
- [[Changes/Open WebUI/2025-08-21-restored-message-toolbar-icons-for-empty-messages-with-files-fixed-an-issue-wher|🐛 Restored Message Toolbar Icons for Empty Messages with Files]] · Editor Experience
- [[Changes/Open WebUI/2025-08-21-3-search-and-browsing-changes-in-v0-6-23|3 Search and Browsing changes in v0.6.23]] · Search and Browsing
- [[Changes/Open WebUI/2025-08-21-resolved-silently-dropped-streaming-response-chunks-fixed-an-issue-where-the-fin|💬 Resolved Silently Dropped Streaming Response Chunks]] · Files and Data
- [[Changes/Open WebUI/2025-08-21-3-mobile-and-desktop-changes-in-v0-6-23|3 Mobile and Desktop changes in v0.6.23]] · Mobile and Desktop
- [[Changes/Open WebUI/2025-08-21-6-reliability-and-performance-changes-in-v0-6-23|6 Reliability and Performance changes in v0.6.23]] · Reliability and Performance
- [[Changes/Open WebUI/2025-08-21-6-safety-and-privacy-changes-in-v0-6-23|6 Safety and Privacy changes in v0.6.23]] · Safety and Privacy
- [[Changes/Open WebUI/2025-08-21-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-08-21-2-accessibility-and-localization-changes-in-v0-6-23|2 Accessibility and Localization changes in v0.6.23]] · Accessibility and Localization
- [[Changes/Open WebUI/2025-08-21-7-model-support-changes-in-v0-6-23|7 Model Support changes in v0.6.23]] · Model Support
- [[Changes/Open WebUI/2025-08-21-resolved-image-generation-api-size-parameter-issue-fixed-a-bug-where-the-api-v1|🖼️ Resolved Image Generation API Size Parameter Issue]] · Image Generation
- [[Changes/Open WebUI/2025-08-21-resolved-code-block-input-issue-with-shift-enter-fixed-a-bug-where-typing-three|📝 Resolved Code Block Input Issue with Shift+Enter]] · Developer Workflow
- [[Changes/Open WebUI/2025-08-21-5-apps-and-integrations-changes-in-v0-6-23|5 Apps and Integrations changes in v0.6.23]] · Apps and Integrations
- [[Changes/Open WebUI/2025-08-21-3-account-and-access-changes-in-v0-6-23|3 Account and Access changes in v0.6.23]] · Account and Access
- [[Changes/Open WebUI/2025-08-21-23-other-changes-in-v0-6-23|23 other changes in v0.6.23]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Voice and Audio

- Earlier: 2025-08-20 · ElevenLabs · [[Changes/ElevenLabs/2025-08-20-speech-to-text|Speech to Text]]
- Later: 2025-09-01 · ElevenLabs · [[Changes/ElevenLabs/2025-09-01-convai-packages|ConvAI packages]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-10 · Dify · [[Changes/Dify/2023-07-10-2-voice-and-audio-changes-in-0-3-7|2 Voice and Audio changes in 0.3.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-08-21-4c4f8f&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-08-21-2-voice-and-audio-changes-in-v0-6-23.md%0ACard%20ID%3A%20open-webui-2025-08-21-4c4f8f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.23%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->