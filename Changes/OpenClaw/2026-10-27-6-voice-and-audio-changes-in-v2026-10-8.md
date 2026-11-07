---
card_id: openclaw-2026-10-27-102348
date: '2026-10-27'
description: 'OpenClaw · 2026-10-27 · Voice and Audio: 6 changes in v2026.10.8 — Discord
  realtime voice consultations can reach the agent and return an answer in a fresh…'
diffusion:
  first_in_tracked: '[[Changes/Dify/2023-07-10-2-voice-and-audio-changes-in-0-3-7|2
    Voice and Audio changes in 0.3.7]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1205
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: voice
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: c797407d094f2e9769011fd94790d23496895d8919ec949ef7e297206c6d0c27
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-10-27-102348
  comparison: ''
  date: '2026-10-27'
  description: 'OpenClaw — v2026.10.8: 6 Voice and Audio changes'
  evidence:
  - quote: Discord realtime voice consultations can reach the agent and return an
      answer in a fresh session.
    source_release: https://docs.openclaw.ai/releases/2026.10.8
  - quote: Talk calls using the Gateway relay on iOS and macOS can stay open through
      brief recoverable stalls. Audio may be dropped during the stall; iOS asks you
      to repeat it, while macOS has no matching notice.
    source_release: https://docs.openclaw.ai/releases/2026.10.8
  - quote: iOS Talk recovery guidance is localized in 21 non-English locales when
      microphone input recovers or realtime audio falls behind.
    source_release: https://docs.openclaw.ai/releases/2026.10.8
  - quote: Long meeting talk-back replies can play in order when a provider sends
      audio faster than playback consumes it.
    source_release: https://docs.openclaw.ai/releases/2026.10.8
  - quote: Voice-call consultations and classic responses now use the call agent model
      when responseModel is unset. An explicit override still takes precedence.
    source_release: https://docs.openclaw.ai/releases/2026.10.8
  - quote: Silent maintenance turns now suppress attachments and other rich content
      as well as text, while still delivering errors, voice messages and notices marked
      for delivery.
    source_release: https://docs.openclaw.ai/releases/2026.10.8
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 6-voice-and-audio-changes-in-v2026-10-8
  source_release: openclaw-2026-10-27-v2026-10-8-9d674f40
  source_type: openclaw_changelog
  theme: voice
  title: 6 Voice and Audio changes in v2026.10.8
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-10-26-14-voice-and-audio-changes-in-elevenlabs-updates-2026-10-26|14
  Voice and Audio changes in ElevenLabs updates — 2026-10-26]]'
- '[[Changes/ElevenLabs/2026-10-26-javascript-sdk|JavaScript SDK]]'
- '[[Changes/Ollama/2026-10-27-3-voice-and-audio-changes-in-v0-40-12|3 Voice and Audio
  changes in v0.40.12]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-10-27-v2026-10-8-9d674f40|openclaw-2026-10-27-v2026-10-8-9d674f40]]'
source_type: openclaw_changelog
theme: voice
title: 6 Voice and Audio changes in v2026.10.8
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Voice and Audio changes in v2026.10.8

**OpenClaw** · 2026-10-27 · [[Themes/voice|Voice and Audio]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.10.8) · from [[Releases/OpenClaw/openclaw-2026-10-27-v2026-10-8-9d674f40|v2026.10.8]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Discord realtime voice consultations can reach the agent and return an answer in a fresh session.

> Talk calls using the Gateway relay on iOS and macOS can stay open through brief recoverable stalls. Audio may be dropped during the stall; iOS asks you to repeat it, while macOS has no matching notice.

> iOS Talk recovery guidance is localized in 21 non-English locales when microphone input recovers or realtime audio falls behind.

> Long meeting talk-back replies can play in order when a provider sends audio faster than playback consumes it.

> Voice-call consultations and classic responses now use the call agent model when responseModel is unset. An explicit override still takes precedence.

> Silent maintenance turns now suppress attachments and other rich content as well as text, while still delivering errors, voice messages and notices marked for delivery.

Source: https://docs.openclaw.ai/releases/2026.10.8
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-10-27-6-model-support-changes-in-v2026-10-8|6 Model Support changes in v2026.10.8]] · Model Support
- [[Changes/OpenClaw/2026-10-27-2-developer-workflow-changes-in-v2026-10-8|2 Developer Workflow changes in v2026.10.8]] · Developer Workflow
- [[Changes/OpenClaw/2026-10-27-on-linux-doctor-can-repair-a-managed-gateway-that-is-using-an-unsupported-node-v|On Linux, Doctor can repair a managed Gateway that is using an unsupported Node…]] · Interface Experience
- [[Changes/OpenClaw/2026-10-27-4-automation-and-scheduling-changes-in-v2026-10-8|4 Automation and Scheduling changes in v2026.10.8]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-10-27-oversized-macos-camera-clips-and-screen-recordings-now-return-an-error-instead-o|Oversized macOS camera clips and screen recordings now return an error instead…]] · Multimodal Input
- [[Changes/OpenClaw/2026-10-27-future-macos-updates-wait-for-the-serving-gateway-to-exit-and-release-its-databa|Future macOS updates wait for the serving Gateway to exit and release its databases…]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-10-27-4-memory-and-personalization-changes-in-v2026-10-8|4 Memory and Personalization changes in v2026.10.8]] · Memory and Personalization
- [[Changes/OpenClaw/2026-10-27-5-account-and-access-changes-in-v2026-10-8|5 Account and Access changes in v2026.10.8]] · Account and Access
- [[Changes/OpenClaw/2026-10-27-2-safety-and-privacy-changes-in-v2026-10-8|2 Safety and Privacy changes in v2026.10.8]] · Safety and Privacy
- [[Changes/OpenClaw/2026-10-27-the-control-ui-now-reconnects-when-a-visible-tab-has-lost-contact-but-still-show|The Control UI now reconnects when a visible tab has lost contact but still shows…]] · Editor Experience
- [[Changes/OpenClaw/2026-10-27-7-agent-mode-changes-in-v2026-10-8|7 Agent Mode changes in v2026.10.8]] · Agent Mode
- [[Changes/OpenClaw/2026-10-27-9-apps-and-integrations-changes-in-v2026-10-8|9 Apps and Integrations changes in v2026.10.8]] · Apps and Integrations
- [[Changes/OpenClaw/2026-10-27-malformed-microsoft-teams-message-html-no-longer-causes-the-parsing-stalls-that|Malformed Microsoft Teams message HTML no longer causes the parsing stalls…]] · Collaboration
- [[Changes/OpenClaw/2026-10-27-32-other-changes-in-v2026-10-8|32 other changes in v2026.10.8]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Voice and Audio

- Earlier: 2026-10-27 · Ollama · [[Changes/Ollama/2026-10-27-3-voice-and-audio-changes-in-v0-40-12|3 Voice and Audio changes in v0.40.12]]
- Later: 2026-10-27 · OpenCode · [[Changes/OpenCode/2026-10-27-2-voice-and-audio-changes-in-v2-2-0|2 Voice and Audio changes in v2.2.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-10 · Dify · [[Changes/Dify/2023-07-10-2-voice-and-audio-changes-in-0-3-7|2 Voice and Audio changes in 0.3.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-10-27-102348&body=Card%3A%20Changes%2FOpenClaw%2F2026-10-27-6-voice-and-audio-changes-in-v2026-10-8.md%0ACard%20ID%3A%20openclaw-2026-10-27-102348%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.10.8%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->