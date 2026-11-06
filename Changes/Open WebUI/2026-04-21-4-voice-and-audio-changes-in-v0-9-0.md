---
card_id: open-webui-2026-04-21-e00c38
date: '2026-04-21'
description: "Open WebUI · 2026-04-21 · Voice and Audio: 4 changes in v0.9.0 — \U0001F4F1
  **Screen-awake voice recording.** Voice recording now keeps the screen awake during
  active…"
diffusion:
  first_in_tracked: '[[Changes/Dify/2023-07-10-2-voice-and-audio-changes-in-0-3-7|2
    Voice and Audio changes in 0.3.7]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1016
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: voice
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2bce9f9ab832fb9e84f1d94b5ded12368955266c508ea25a7cab44b1cf2d3c9c
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-04-21-e00c38
  comparison: ''
  date: '2026-04-21'
  description: 'Open WebUI — v0.9.0: 4 Voice and Audio changes'
  evidence:
  - quote: "\U0001F4F1 **Screen-awake voice recording.** Voice recording now keeps
      the screen awake during active dictation and safely re-acquires wake lock after
      visibility changes, helping prevent long transcriptions from being cut off on
      mobile devices. [#23145](https://github.com/open-webui/open-webui/issues/23145)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F510 **Consistent outbound SSL handling.** External requests for
      tools, functions, terminals, webhooks, retrieval loaders, audio provider discovery,
      and OpenAI-compatible embedding calls now consistently apply the configured
      SSL client setting, improving reliability for deployments that require custom
      certificate or verification behavior. [Commit](https://github.com/open-webui/open-webui/commit/fd25152076ea7c310e42c9bacc5cd2b544eeae48),
      [Commit](https://github.com/open-webui/open-webui/commit/56c5bc1d3487020ab886d3332aacc1644c1d6123)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F399️ **Mistral speech input format.** Mistral speech-to-text requests
      now use the correct chat-completions audio input format for better compatibility.
      [Commit](https://github.com/open-webui/open-webui/commit/34d569d564a8ef2702c647dbad83eac840b76b2e),
      [#23822](https://github.com/open-webui/open-webui/issues/23822)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F9F1 **Safer file path handling.** File upload, transcription cache,
      and model download paths now use safer path construction helpers to reduce path
      parsing risks and improve cross-platform path safety. [Commit](https://github.com/open-webui/open-webui/commit/15f9a8f3f13f112c96cb1b16f88859f65de58346)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 4-voice-and-audio-changes-in-v0-9-0
  source_release: open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a
  source_type: github_releases
  theme: voice
  title: 4 Voice and Audio changes in v0.9.0
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-04-20-speech-to-text|Speech to Text]]'
- '[[Changes/ElevenLabs/2026-04-20-speech-to-text-c85018|Speech to Text]]'
- '[[Changes/ElevenLabs/2026-04-20-other|Other]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a|open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a]]'
source_type: github_releases
theme: voice
title: 4 Voice and Audio changes in v0.9.0
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Voice and Audio changes in v0.9.0

**Open WebUI** · 2026-04-21 · [[Themes/voice|Voice and Audio]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.0) · from [[Releases/Open WebUI/open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a|v0.9.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📱 **Screen-awake voice recording.** Voice recording now keeps the screen awake during active dictation and safely re-acquires wake lock after visibility changes, helping prevent long transcriptions from being cut off on mobile devices. [#23145](https://github.com/open-webui/open-webui/issues/23145)

> 🔐 **Consistent outbound SSL handling.** External requests for tools, functions, terminals, webhooks, retrieval loaders, audio provider discovery, and OpenAI-compatible embedding calls now consistently apply the configured SSL client setting, improving reliability for deployments that require custom certificate or verification behavior. [Commit](https://github.com/open-webui/open-webui/commit/fd25152076ea7c310e42c9bacc5cd2b544eeae48), [Commit](https://github.com/open-webui/open-webui/commit/56c5bc1d3487020ab886d3332aacc1644c1d6123)

> 🎙️ **Mistral speech input format.** Mistral speech-to-text requests now use the correct chat-completions audio input format for better compatibility. [Commit](https://github.com/open-webui/open-webui/commit/34d569d564a8ef2702c647dbad83eac840b76b2e), [#23822](https://github.com/open-webui/open-webui/issues/23822)

> 🧱 **Safer file path handling.** File upload, transcription cache, and model download paths now use safer path construction helpers to reduce path parsing risks and improve cross-platform path safety. [Commit](https://github.com/open-webui/open-webui/commit/15f9a8f3f13f112c96cb1b16f88859f65de58346)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-04-21-3-files-and-data-changes-in-v0-9-0|3 Files and Data changes in v0.9.0]] · Files and Data
- [[Changes/Open WebUI/2026-04-21-4-image-generation-changes-in-v0-9-0|4 Image Generation changes in v0.9.0]] · Image Generation
- [[Changes/Open WebUI/2026-04-21-28-model-support-changes-in-v0-9-0|28 Model Support changes in v0.9.0]] · Model Support
- [[Changes/Open WebUI/2026-04-21-5-editor-experience-changes-in-v0-9-0|5 Editor Experience changes in v0.9.0]] · Editor Experience
- [[Changes/Open WebUI/2026-04-21-persistent-chat-payload-efficiency-persisted-chats-now-use-server-side-history-l|🚀 Persistent chat payload efficiency. Persisted chats now use server-side…]] · Multimodal Input
- [[Changes/Open WebUI/2026-04-21-8-context-window-changes-in-v0-9-0|8 Context Window changes in v0.9.0]] · Context Window
- [[Changes/Open WebUI/2026-04-21-24-reliability-and-performance-changes-in-v0-9-0|24 Reliability and Performance changes in v0.9.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-04-21-4-apps-and-integrations-changes-in-v0-9-0|4 Apps and Integrations changes in v0.9.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-04-21-46-developer-workflow-changes-in-v0-9-0|46 Developer Workflow changes in v0.9.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-04-21-8-automation-and-scheduling-changes-in-v0-9-0|8 Automation and Scheduling changes in v0.9.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-04-21-7-memory-and-personalization-changes-in-v0-9-0|7 Memory and Personalization changes in v0.9.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-04-21-2-mobile-and-desktop-changes-in-v0-9-0|2 Mobile and Desktop changes in v0.9.0]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-04-21-17-interface-experience-changes-in-v0-9-0|17 Interface Experience changes in v0.9.0]] · Interface Experience
- [[Changes/Open WebUI/2026-04-21-11-safety-and-privacy-changes-in-v0-9-0|11 Safety and Privacy changes in v0.9.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-04-21-4-search-and-browsing-changes-in-v0-9-0|4 Search and Browsing changes in v0.9.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-04-21-shared-chat-access-controls-you-can-now-control-who-has-access-to-a-shared-chat|🔗 Shared chat access controls. You can now control who has access to a shared…]] · Collaboration
- [[Changes/Open WebUI/2026-04-21-17-account-and-access-changes-in-v0-9-0|17 Account and Access changes in v0.9.0]] · Account and Access
- [[Changes/Open WebUI/2026-04-21-21-other-changes-in-v0-9-0|21 other changes in v0.9.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Voice and Audio

- Earlier: 2026-04-20 · ElevenLabs · [[Changes/ElevenLabs/2026-04-20-other|Other]]
- Later: 2026-04-27 · ElevenLabs · [[Changes/ElevenLabs/2026-04-27-python-sdk|Python SDK]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-10 · Dify · [[Changes/Dify/2023-07-10-2-voice-and-audio-changes-in-0-3-7|2 Voice and Audio changes in 0.3.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-04-21-e00c38&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-04-21-4-voice-and-audio-changes-in-v0-9-0.md%0ACard%20ID%3A%20open-webui-2026-04-21-e00c38%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->