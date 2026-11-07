---
card_id: openclaw-2026-11-03-b66331
date: '2026-11-03'
description: 'OpenClaw · 2026-11-03 · Voice and Audio: 6 changes in v2026.10.10 —
  There is now an additional voice option that uses the same AI model that answers
  your typed…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-07-09-type-in-parentheses-to-add-notes-to-your-script-that-don-t-affect-the-audio-text|Support
    for Inline Notes]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 3039
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: voice
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 7526f92e45815fbdb15c61435316dd465b57b3e89e9183288ae1181fedad8935
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-11-03-b66331
  comparison: ''
  date: '2026-11-03'
  description: 'OpenClaw — v2026.10.10: 6 Voice and Audio changes'
  evidence:
  - quote: There is now an additional voice option that uses the same AI model that
      answers your typed messages, while using separately configured services for
      transcription and speech generation.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: Choose Fish Audio’s Drama 3 preview for speech and Talk if you want to
      try it; the existing voice default does not change.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: Talk voice and transcription choices now keep the settings you selected
      when providers refresh. Language hints reach automatically found Python Whisper,
      and supported GPT-Live subscription voice accepts a valid pasted ChatGPT access
      token with an account ID.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: Voice Call commands now keep their JSON results readable by other tools
      and reject unsupported call-brief files instead of waiting indefinitely.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: Telegram now keeps slow voice notes and messages waiting behind a busy
      reply eligible for retry instead of silently losing them. Saved ordinary final
      text can recover after eligible delivery failures, but if Telegram accepted
      the first send and its acknowledgment was lost, the reply may appear twice.
      On the first legacy-queue import, messages older than 24 hours are marked failed
      and will not run, including ones that were never processed.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: Discord voice consultations continue after a voice change during a call.
      Update and restart OpenClaw to apply that fix. If a call ends while an answer
      is still being prepared, the answer can continue in the same channel's text
      chat unless you cancelled it.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 6-voice-and-audio-changes-in-v2026-10-10
  source_release: openclaw-2026-11-03-v2026-10-10-c26ff355
  source_type: openclaw_changelog
  theme: voice
  title: 6 Voice and Audio changes in v2026.10.10
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-11-02-realtime-entity-redaction|Realtime entity redaction]]'
- '[[Changes/Google Antigravity/2026-11-03-voice-mode-remote-agents-redesigned-automations-and-jupyter-notebook-viewer|Voice
  mode, remote agents, redesigned Automations, and Jupyter notebook viewer]]'
- '[[Changes/Open WebUI/2026-11-03-4-voice-and-audio-changes-in-v0-13-0|4 Voice and
  Audio changes in v0.13.0]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-11-03-v2026-10-10-c26ff355|openclaw-2026-11-03-v2026-10-10-c26ff355]]'
source_type: openclaw_changelog
theme: voice
title: 6 Voice and Audio changes in v2026.10.10
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Voice and Audio changes in v2026.10.10

**OpenClaw** · 2026-11-03 · [[Themes/voice|Voice and Audio]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.10.10) · from [[Releases/OpenClaw/openclaw-2026-11-03-v2026-10-10-c26ff355|v2026.10.10]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> There is now an additional voice option that uses the same AI model that answers your typed messages, while using separately configured services for transcription and speech generation.

> Choose Fish Audio’s Drama 3 preview for speech and Talk if you want to try it; the existing voice default does not change.

> Talk voice and transcription choices now keep the settings you selected when providers refresh. Language hints reach automatically found Python Whisper, and supported GPT-Live subscription voice accepts a valid pasted ChatGPT access token with an account ID.

> Voice Call commands now keep their JSON results readable by other tools and reject unsupported call-brief files instead of waiting indefinitely.

> Telegram now keeps slow voice notes and messages waiting behind a busy reply eligible for retry instead of silently losing them. Saved ordinary final text can recover after eligible delivery failures, but if Telegram accepted the first send and its acknowledgment was lost, the reply may appear twice. On the first legacy-queue import, messages older than 24 hours are marked failed and will not run, including ones that were never processed.

> Discord voice consultations continue after a voice change during a call. Update and restart OpenClaw to apply that fix. If a call ends while an answer is still being prepared, the answer can continue in the same channel's text chat unless you cancelled it.

Source: https://docs.openclaw.ai/releases/2026.10.10
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-11-03-generated-images-music-and-video-can-wait-behind-a-busy-chat-without-reporting-f|Generated images, music and video can wait behind a busy chat without reporting…]] · Multimodal Input
- [[Changes/OpenClaw/2026-11-03-you-can-now-guide-the-same-running-conversation-from-the-control-ui-or-an-admini|Guide the same running conversation from the Control UI or an administrator-linked…]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-11-03-2-files-and-data-changes-in-v2026-10-10|2 Files and Data changes in v2026.10.10]] · Files and Data
- [[Changes/OpenClaw/2026-11-03-6-account-and-access-changes-in-v2026-10-10|6 Account and Access changes in v2026.10.10]] · Account and Access
- [[Changes/OpenClaw/2026-11-03-image-generation-and-editing-now-reject-invalid-size-and-shape-options-before-co|Image generation and editing now reject invalid size and shape options before…]] · Image Generation
- [[Changes/OpenClaw/2026-11-03-9-agent-mode-changes-in-v2026-10-10|9 Agent Mode changes in v2026.10.10]] · Agent Mode
- [[Changes/OpenClaw/2026-11-03-13-interface-experience-changes-in-v2026-10-10|13 Interface Experience changes in v2026.10.10]] · Interface Experience
- [[Changes/OpenClaw/2026-11-03-you-can-now-work-directly-in-a-folder-on-another-computer-connected-to-openclaw|Work directly in a folder on another computer connected to OpenClaw]] · Agent Mode
- [[Changes/OpenClaw/2026-11-03-5-context-window-changes-in-v2026-10-10|5 Context Window changes in v2026.10.10]] · Context Window
- [[Changes/OpenClaw/2026-11-03-15-memory-and-personalization-changes-in-v2026-10-10|15 Memory and Personalization changes in v2026.10.10]] · Memory and Personalization
- [[Changes/OpenClaw/2026-11-03-4-automation-and-scheduling-changes-in-v2026-10-10|4 Automation and Scheduling changes in v2026.10.10]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-11-03-3-editor-experience-changes-in-v2026-10-10|3 Editor Experience changes in v2026.10.10]] · Editor Experience
- [[Changes/OpenClaw/2026-11-03-web-search-now-honors-more-of-your-chosen-provider-settings-result-counts-and-ti|Web search now honors more of your chosen provider settings, result counts…]] · Search and Browsing
- [[Changes/OpenClaw/2026-11-03-6-collaboration-changes-in-v2026-10-10|6 Collaboration changes in v2026.10.10]] · Collaboration
- [[Changes/OpenClaw/2026-11-03-7-safety-and-privacy-changes-in-v2026-10-10|7 Safety and Privacy changes in v2026.10.10]] · Safety and Privacy
- [[Changes/OpenClaw/2026-11-03-4-mobile-and-desktop-changes-in-v2026-10-10|4 Mobile and Desktop changes in v2026.10.10]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-11-03-retrying-a-meeting-transcript-from-summary-or-transcript-now-restores-all-availa|Retrying a meeting transcript from Summary or Transcript now restores all available pages]] · Meeting Notes
- [[Changes/OpenClaw/2026-11-03-18-developer-workflow-changes-in-v2026-10-10|18 Developer Workflow changes in v2026.10.10]] · Developer Workflow
- [[Changes/OpenClaw/2026-11-03-21-apps-and-integrations-changes-in-v2026-10-10|21 Apps and Integrations changes in v2026.10.10]] · Apps and Integrations
- [[Changes/OpenClaw/2026-11-03-17-model-support-changes-in-v2026-10-10|17 Model Support changes in v2026.10.10]] · Model Support
- [[Changes/OpenClaw/2026-11-03-incognito-conversations-now-keep-openclaw-conversation-contents-in-memory-instea|Incognito conversations now keep OpenClaw conversation contents in memory instead…]] · Reliability and Performance
- [[Changes/OpenClaw/2026-11-03-83-other-changes-in-v2026-10-10|83 other changes in v2026.10.10]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Voice and Audio

- Earlier: 2026-11-03 · Open WebUI · [[Changes/Open WebUI/2026-11-03-4-voice-and-audio-changes-in-v0-13-0|4 Voice and Audio changes in v0.13.0]]
- Later: 2026-11-04 · Dify · [[Changes/Dify/2026-11-04-2-voice-and-audio-changes-in-1-19-0|2 Voice and Audio changes in 1.19.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-07-09 · Descript · [[Changes/Descript/2018-07-09-type-in-parentheses-to-add-notes-to-your-script-that-don-t-affect-the-audio-text|Support for Inline Notes]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-11-03-b66331&body=Card%3A%20Changes%2FOpenClaw%2F2026-11-03-6-voice-and-audio-changes-in-v2026-10-10.md%0ACard%20ID%3A%20openclaw-2026-11-03-b66331%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.10.10%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->