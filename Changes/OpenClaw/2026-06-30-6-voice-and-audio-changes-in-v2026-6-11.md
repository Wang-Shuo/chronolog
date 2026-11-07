---
card_id: openclaw-2026-06-30-73eeed
date: '2026-06-30'
description: 'OpenClaw · 2026-06-30 · Voice and Audio: 6 changes in v2026.6.11 — Feishu
  voice replies from OpenClaw now show their duration in the chat bubble, so recipients…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-07-09-type-in-parentheses-to-add-notes-to-your-script-that-don-t-affect-the-audio-text|Support
    for Inline Notes]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2913
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: voice
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: fd403257d8523d5475d76107680b5c6ea41039f5088eeec168680e0357ff29d0
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-06-30-73eeed
  comparison: ''
  date: '2026-06-30'
  description: 'OpenClaw — v2026.6.11: 6 Voice and Audio changes'
  evidence:
  - quote: 'Feishu voice replies from OpenClaw now show their duration in the chat
      bubble, so recipients can see how long the audio is before playing it. #89172
      Related #53798 . Thanks @areslp, @fxz26284407, @kinrocw.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: Discord voice conversations now keep back-to-back assistant responses moving,
      so a queued reply plays after the previous audio stream closes instead of remaining
      stuck. 88b64e4 Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'MiniMax text-to-speech and voice notes are less likely to fail because
      OpenClaw now explicitly requests the audio format it can decode instead of relying
      on provider defaults. #73079 Thanks @efe-arv.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: Voice Wake upgrades now keep existing trigger phrases and routing rules
      working as OpenClaw moves them from retired settings files into the shared state
      database. bdf81a8
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Canvas, Discord, Slack, Voice Call, and WhatsApp users keep the same skill
      guidance with each installed or bundled plugin, while references to the former
      root skills/... paths need to move into the relevant plugin directory. #95664
      Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'iOS screens now use consistent OpenClaw accent and status colors across
      onboarding, settings, chat, approval prompts, voice permissions, widgets, and
      shared chat views. #94627 Thanks @zats.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 6-voice-and-audio-changes-in-v2026-6-11
  source_release: openclaw-2026-06-30-v2026-6-11-23cb95a9
  source_type: openclaw_changelog
  theme: voice
  title: 6 Voice and Audio changes in v2026.6.11
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-06-29-speech-to-text-b8f62a|Speech to Text]]'
- '[[Changes/Open WebUI/2026-06-29-3-voice-and-audio-changes-in-v0-10-0|3 Voice and
  Audio changes in v0.10.0]]'
- '[[Changes/GitHub Copilot CLI/2026-06-30-voice-mode-turns-itself-off-when-the-engine-fails-to-start-at-boot|Voice
  mode turns itself off when the engine fails to start at boot]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-06-30-v2026-6-11-23cb95a9|openclaw-2026-06-30-v2026-6-11-23cb95a9]]'
source_type: openclaw_changelog
theme: voice
title: 6 Voice and Audio changes in v2026.6.11
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Voice and Audio changes in v2026.6.11

**OpenClaw** · 2026-06-30 · [[Themes/voice|Voice and Audio]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.6.11) · from [[Releases/OpenClaw/openclaw-2026-06-30-v2026-6-11-23cb95a9|v2026.6.11]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Feishu voice replies from OpenClaw now show their duration in the chat bubble, so recipients can see how long the audio is before playing it. #89172 Related #53798 . Thanks @areslp, @fxz26284407, @kinrocw.

> Discord voice conversations now keep back-to-back assistant responses moving, so a queued reply plays after the previous audio stream closes instead of remaining stuck. 88b64e4 Thanks @vincentkoc.

> MiniMax text-to-speech and voice notes are less likely to fail because OpenClaw now explicitly requests the audio format it can decode instead of relying on provider defaults. #73079 Thanks @efe-arv.

> Voice Wake upgrades now keep existing trigger phrases and routing rules working as OpenClaw moves them from retired settings files into the shared state database. bdf81a8

> Canvas, Discord, Slack, Voice Call, and WhatsApp users keep the same skill guidance with each installed or bundled plugin, while references to the former root skills/... paths need to move into the relevant plugin directory. #95664 Thanks @vincentkoc.

> iOS screens now use consistent OpenClaw accent and status colors across onboarding, settings, chat, approval prompts, voice permissions, widgets, and shared chat views. #94627 Thanks @zats.

Source: https://docs.openclaw.ai/releases/2026.6.11
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-06-30-7-editor-experience-changes-in-v2026-6-11|7 Editor Experience changes in v2026.6.11]] · Editor Experience
- [[Changes/OpenClaw/2026-06-30-canvas-a2ui-now-serves-only-the-current-app-assets-after-each-build-so-outdated|Canvas A2UI now serves only the current app assets after each build, so outdated…]] · Files and Data
- [[Changes/OpenClaw/2026-06-30-word-powerpoint-and-excel-document-reads-and-writes-now-use-the-intended-docx-pp|Word, PowerPoint, and Excel document reads and writes now use the intended .docx…]] · Presentation Creation
- [[Changes/OpenClaw/2026-06-30-20-context-window-changes-in-v2026-6-11|20 Context Window changes in v2026.6.11]] · Context Window
- [[Changes/OpenClaw/2026-06-30-32-agent-mode-changes-in-v2026-6-11|32 Agent Mode changes in v2026.6.11]] · Agent Mode
- [[Changes/OpenClaw/2026-06-30-15-mobile-and-desktop-changes-in-v2026-6-11|15 Mobile and Desktop changes in v2026.6.11]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-06-30-5-collaboration-changes-in-v2026-6-11|5 Collaboration changes in v2026.6.11]] · Collaboration
- [[Changes/OpenClaw/2026-06-30-26-memory-and-personalization-changes-in-v2026-6-11|26 Memory and Personalization changes in v2026.6.11]] · Memory and Personalization
- [[Changes/OpenClaw/2026-06-30-34-apps-and-integrations-changes-in-v2026-6-11|34 Apps and Integrations changes in v2026.6.11]] · Apps and Integrations
- [[Changes/OpenClaw/2026-06-30-32-model-support-changes-in-v2026-6-11|32 Model Support changes in v2026.6.11]] · Model Support
- [[Changes/OpenClaw/2026-06-30-qqbot-group-admins-can-choose-how-broadly-slash-commands-are-available-and-priva|QQBot group admins can choose how broadly slash commands are available…]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-06-30-4-reliability-and-performance-changes-in-v2026-6-11|4 Reliability and Performance changes in v2026.6.11]] · Reliability and Performance
- [[Changes/OpenClaw/2026-06-30-3-interface-experience-changes-in-v2026-6-11|3 Interface Experience changes in v2026.6.11]] · Interface Experience
- [[Changes/OpenClaw/2026-06-30-15-automation-and-scheduling-changes-in-v2026-6-11|15 Automation and Scheduling changes in v2026.6.11]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-06-30-when-a-codex-subscription-reaches-its-usage-limit-openclaw-now-moves-to-configur|When a Codex subscription reaches its usage limit, OpenClaw now moves to configured…]] · Pricing Model
- [[Changes/OpenClaw/2026-06-30-9-developer-workflow-changes-in-v2026-6-11|9 Developer Workflow changes in v2026.6.11]] · Developer Workflow
- [[Changes/OpenClaw/2026-06-30-6-safety-and-privacy-changes-in-v2026-6-11|6 Safety and Privacy changes in v2026.6.11]] · Safety and Privacy
- [[Changes/OpenClaw/2026-06-30-more-official-channel-provider-and-web-search-plugins-can-now-be-installed-or-re|More official channel, provider, and web-search plugins can now be installed…]] · Search and Browsing
- [[Changes/OpenClaw/2026-06-30-generated-images-from-a-remote-codex-app-server-now-arrive-as-attachments-instea|Generated images from a remote Codex app-server now arrive as attachments instead…]] · Image Generation
- [[Changes/OpenClaw/2026-06-30-background-image-video-and-music-results-now-return-to-the-chat-that-requested-t|Background image, video, and music results now return to the chat that requested…]] · Music Generation
- [[Changes/OpenClaw/2026-06-30-2-account-and-access-changes-in-v2026-6-11|2 Account and Access changes in v2026.6.11]] · Account and Access
- [[Changes/OpenClaw/2026-06-30-96-other-changes-in-v2026-6-11|96 other changes in v2026.6.11]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Voice and Audio

- Earlier: 2026-06-30 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-06-30-voice-mode-turns-itself-off-when-the-engine-fails-to-start-at-boot|Voice mode turns itself off when the engine fails to start at boot]]
- Later: 2026-07-01 · Microsoft 365 Copilot · [[Changes/Microsoft 365 Copilot/2026-07-01-real-time-voice-interactions-with-audio-overview-web-word|Real-time voice interactions with Audio Overview Web (Word)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-07-09 · Descript · [[Changes/Descript/2018-07-09-type-in-parentheses-to-add-notes-to-your-script-that-don-t-affect-the-audio-text|Support for Inline Notes]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-06-30-73eeed&body=Card%3A%20Changes%2FOpenClaw%2F2026-06-30-6-voice-and-audio-changes-in-v2026-6-11.md%0ACard%20ID%3A%20openclaw-2026-06-30-73eeed%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.6.11%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->