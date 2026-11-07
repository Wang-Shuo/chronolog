---
card_id: openclaw-2026-11-05-17ee2a
date: '2026-11-05'
description: 'OpenClaw · 2026-11-05 · Voice and Audio: 7 changes in v2026.11.1 — Buffers
  up to three seconds of microphone audio in Gateway-routed iOS and Mac Talk when
  the…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-07-09-type-in-parentheses-to-add-notes-to-your-script-that-don-t-affect-the-audio-text|Support
    for Inline Notes]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 3041
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: voice
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b2416eba62e1ea44860d34ccd03499aa2e8e5f07ed6cd1d62d438647ac2e3f6a
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-11-05-17ee2a
  comparison: ''
  date: '2026-11-05'
  description: 'OpenClaw — v2026.11.1: 7 Voice and Audio changes'
  evidence:
  - quote: Buffers up to three seconds of microphone audio in Gateway-routed iOS and
      Mac Talk when the connection is slow to confirm it, though excess audio can
      still be dropped.
    source_release: https://docs.openclaw.ai/releases/2026.11.1
  - quote: Allows long spoken replies in meetings to queue for playback, with checks
      for audio that remains stalled.
    source_release: https://docs.openclaw.ai/releases/2026.11.1
  - quote: Helps continuous voice conversations routed through the Gateway continue
      by starting a new spoken reply when provider audio arrives.
    source_release: https://docs.openclaw.ai/releases/2026.11.1
  - quote: Translates Talk input recovery messages into 21 non-English native app
      locales, including guidance to repeat the last part when audio falls behind
      or microphone input recovers.
    source_release: https://docs.openclaw.ai/releases/2026.11.1
  - quote: Routes OpenAI realtime connections through your managed proxy, including
      audio, without falling back to a direct connection if the proxy fails.
    source_release: https://docs.openclaw.ai/releases/2026.11.1
  - quote: Uses the call agent’s configured model for voice calls when no response
      model is set.
    source_release: https://docs.openclaw.ai/releases/2026.11.1
  - quote: Redacts Fish Audio and Gradium credentials from provider errors.
    source_release: https://docs.openclaw.ai/releases/2026.11.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 7-voice-and-audio-changes-in-v2026-11-1
  source_release: openclaw-2026-11-05-v2026-11-1-7d3de823
  source_type: openclaw_changelog
  theme: voice
  title: 7 Voice and Audio changes in v2026.11.1
  type: change
related_changes:
- '[[Changes/Dify/2026-11-04-2-voice-and-audio-changes-in-1-19-0|2 Voice and Audio
  changes in 1.19.0]]'
- '[[Changes/Raycast/2026-11-04-3-voice-and-audio-changes-in-raycast-macos-2-11|3
  Voice and Audio changes in Raycast macos 2.11]]'
- '[[Changes/Raycast/2026-11-04-3-voice-and-audio-changes-in-raycast-windows-2-11|3
  Voice and Audio changes in Raycast windows 2.11]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-11-05-v2026-11-1-7d3de823|openclaw-2026-11-05-v2026-11-1-7d3de823]]'
source_type: openclaw_changelog
theme: voice
title: 7 Voice and Audio changes in v2026.11.1
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Voice and Audio changes in v2026.11.1

**OpenClaw** · 2026-11-05 · [[Themes/voice|Voice and Audio]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.11.1) · from [[Releases/OpenClaw/openclaw-2026-11-05-v2026-11-1-7d3de823|v2026.11.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Buffers up to three seconds of microphone audio in Gateway-routed iOS and Mac Talk when the connection is slow to confirm it, though excess audio can still be dropped.

> Allows long spoken replies in meetings to queue for playback, with checks for audio that remains stalled.

> Helps continuous voice conversations routed through the Gateway continue by starting a new spoken reply when provider audio arrives.

> Translates Talk input recovery messages into 21 non-English native app locales, including guidance to repeat the last part when audio falls behind or microphone input recovers.

> Routes OpenAI realtime connections through your managed proxy, including audio, without falling back to a direct connection if the proxy fails.

> Uses the call agent’s configured model for voice calls when no response model is set.

> Redacts Fish Audio and Gradium credentials from provider errors.

Source: https://docs.openclaw.ai/releases/2026.11.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-11-05-reduces-prompt-cache-misses-across-completion-heartbeat-and-background-turns-by|Reduces prompt-cache misses across completion, heartbeat and background turns…]] · Editor Experience
- [[Changes/OpenClaw/2026-11-05-keeps-accepted-talk-work-running-when-you-end-talk-on-an-android-phone-connected|Keeps accepted Talk work running when you end Talk on an Android phone connected…]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-11-05-5-apps-and-integrations-changes-in-v2026-11-1|5 Apps and Integrations changes in v2026.11.1]] · Apps and Integrations
- [[Changes/OpenClaw/2026-11-05-3-context-window-changes-in-v2026-11-1|3 Context Window changes in v2026.11.1]] · Context Window
- [[Changes/OpenClaw/2026-11-05-5-memory-and-personalization-changes-in-v2026-11-1|5 Memory and Personalization changes in v2026.11.1]] · Memory and Personalization
- [[Changes/OpenClaw/2026-11-05-2-safety-and-privacy-changes-in-v2026-11-1|2 Safety and Privacy changes in v2026.11.1]] · Safety and Privacy
- [[Changes/OpenClaw/2026-11-05-prevents-oversized-mac-camera-clips-and-screen-recordings-from-disconnecting-the|Prevents oversized Mac camera clips and screen recordings from disconnecting…]] · Multimodal Input
- [[Changes/OpenClaw/2026-11-05-4-model-support-changes-in-v2026-11-1|4 Model Support changes in v2026.11.1]] · Model Support
- [[Changes/OpenClaw/2026-11-05-4-agent-mode-changes-in-v2026-11-1|4 Agent Mode changes in v2026.11.1]] · Agent Mode
- [[Changes/OpenClaw/2026-11-05-4-account-and-access-changes-in-v2026-11-1|4 Account and Access changes in v2026.11.1]] · Account and Access
- [[Changes/OpenClaw/2026-11-05-avoids-restoring-cold-archived-conversations-just-to-refresh-usage-and-cost-repo|Avoids restoring cold archived conversations just to refresh usage and cost reports…]] · Pricing Model
- [[Changes/OpenClaw/2026-11-05-allows-authorized-native-commands-to-restore-archived-source-sessions-and-report|Allows authorized native commands to restore archived source sessions, and reports…]] · Collaboration
- [[Changes/OpenClaw/2026-11-05-3-developer-workflow-changes-in-v2026-11-1|3 Developer Workflow changes in v2026.11.1]] · Developer Workflow
- [[Changes/OpenClaw/2026-11-05-keeps-the-windows-scheduled-task-available-during-update-recovery-until-the-gate|Keeps the Windows scheduled task available during update recovery until the Gateway…]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-11-05-40-other-changes-in-v2026-11-1|40 other changes in v2026.11.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Voice and Audio

- Earlier: 2026-11-04 · Raycast · [[Changes/Raycast/2026-11-04-3-voice-and-audio-changes-in-raycast-windows-2-11|3 Voice and Audio changes in Raycast windows 2.11]]
- Later: 2026-11-05 · Superwhisper · [[Changes/Superwhisper/2026-11-05-import-vocabulary-and-dictation-history-from-wispr-flow-aqua-voice-typeless-and|Import vocabulary and dictation history from Wispr Flow, Aqua Voice, Typeless…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-07-09 · Descript · [[Changes/Descript/2018-07-09-type-in-parentheses-to-add-notes-to-your-script-that-don-t-affect-the-audio-text|Support for Inline Notes]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-11-05-17ee2a&body=Card%3A%20Changes%2FOpenClaw%2F2026-11-05-7-voice-and-audio-changes-in-v2026-11-1.md%0ACard%20ID%3A%20openclaw-2026-11-05-17ee2a%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.11.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->