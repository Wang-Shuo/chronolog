---
card_id: elevenlabs-2026-11-02-f40dff
date: '2026-11-02'
description: 'ElevenLabs · 2026-11-02 · Voice and Audio: **Speech to Text** can now
  redact entities in realtime transcripts. Pass `entity_redaction` and…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-07-09-type-in-parentheses-to-add-notes-to-your-script-that-don-t-affect-the-audio-text|Support
    for Inline Notes]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 3038
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: voice
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: launch
machine_hash: e5dc486a06f82c8d4ba15e8bdaedf03dd3c478b99a49ea8c871db66ff7f94575
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-11-02-f40dff
  comparison: ''
  confidence: low
  date: '2026-11-02'
  description: 'ElevenLabs — ElevenLabs updates — 2026-11-02: **Speech to Text** can
    now redact entities in realtime transcripts. Pass `entity_redaction` and `entity_redaction_mode`
    as query parameters on the [realtime WebSocket](https://elevenlabs.io/docs/api-reference/speech-to-text/v-1-speech-to-text-realtime),
    in the same format as batch transcription, and each committed transcript is followed
    by a `redacted_transcript` event carrying the original `text` and the `redacted_text`.
    The Python and JavaScript SDKs from v2.76.0 and `@elevenlabs/client` from 1.34.0
    support these options. See [Entity detection](https://elevenlabs.io/docs/eleven-api/guides/how-to/speech-to-text/batch/entity-detection#entity-redaction).'
  evidence:
  - quote: '**Speech to Text** can now redact entities in realtime transcripts. Pass
      `entity_redaction` and `entity_redaction_mode` as query parameters on the [realtime
      WebSocket](https://elevenlabs.io/docs/api-reference/speech-to-text/v-1-speech-to-text-realtime),
      in the same format as batch transcription, and each committed transcript is
      followed by a `redacted_transcript` event carrying the original `text` and the
      `redacted_text`. The Python and JavaScript SDKs from v2.76.0 and `@elevenlabs/client`
      from 1.34.0 support these options. See [Entity detection](https://elevenlabs.io/docs/eleven-api/guides/how-to/speech-to-text/batch/entity-detection#entity-redaction).'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  extractor_version: fallback-v5
  impact: significant
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: realtime-entity-redaction
  source_release: elevenlabs-2026-11-02-2026-11-02-7efe9660
  source_type: elevenlabs_changelog
  theme: voice
  title: Realtime entity redaction
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-11-02-javascript-sdk|JavaScript SDK]]'
- '[[Changes/ElevenLabs/2026-11-02-16-voice-and-audio-changes-in-elevenlabs-updates-2026-11-02|16
  Voice and Audio changes in ElevenLabs updates — 2026-11-02]]'
- '[[Changes/ElevenLabs/2026-11-02-professional-voice-clones-on-eleven-v4|Professional
  Voice Clones on Eleven v4]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-11-02-2026-11-02-7efe9660|elevenlabs-2026-11-02-2026-11-02-7efe9660]]'
source_type: elevenlabs_changelog
theme: voice
title: Realtime entity redaction
type: change
---

<!-- chronolog:begin region="header" -->
# Realtime entity redaction

**ElevenLabs** · 2026-11-02 · [[Themes/voice|Voice and Audio]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/11/2) · from [[Releases/ElevenLabs/elevenlabs-2026-11-02-2026-11-02-7efe9660|ElevenLabs updates — 2026-11-02]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **Speech to Text** can now redact entities in realtime transcripts. Pass `entity_redaction` and `entity_redaction_mode` as query parameters on the [realtime WebSocket](https://elevenlabs.io/docs/api-reference/speech-to-text/v-1-speech-to-text-realtime), in the same format as batch transcription, and each committed transcript is followed by a `redacted_transcript` event carrying the original `text` and the `redacted_text`. The Python and JavaScript SDKs from v2.76.0 and `@elevenlabs/client` from 1.34.0 support these options. See [Entity detection](https://elevenlabs.io/docs/eleven-api/guides/how-to/speech-to-text/batch/entity-detection#entity-redaction).
>
> Source: https://elevenlabs.io/docs/changelog/2026/11/2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-11-02-elevenlabs-cli|ElevenLabs CLI]] · Agent Mode
- [[Changes/ElevenLabs/2026-11-02-4-safety-and-privacy-changes-in-elevenlabs-updates-2026-11-02|4 Safety and Privacy changes in ElevenLabs updates — 2026-11-02]] · Safety and Privacy
- [[Changes/ElevenLabs/2026-11-02-3-pricing-model-changes-in-elevenlabs-updates-2026-11-02|3 Pricing Model changes in ElevenLabs updates — 2026-11-02]] · Pricing Model
- [[Changes/ElevenLabs/2026-11-02-analysis-items-api|Analysis items API]] · Agent Mode
- [[Changes/ElevenLabs/2026-11-02-sfx-v3|SFX v3]] · Model Support
- [[Changes/ElevenLabs/2026-11-02-7-model-support-changes-in-elevenlabs-updates-2026-11-02|7 Model Support changes in ElevenLabs updates — 2026-11-02]] · Model Support
- [[Changes/ElevenLabs/2026-11-02-elevenagents|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-11-02-2-interface-experience-changes-in-elevenlabs-updates-2026-11-02|2 Interface Experience changes in ElevenLabs updates — 2026-11-02]] · Interface Experience
- [[Changes/ElevenLabs/2026-11-02-python-sdk|Python SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-speech-to-text|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-8-agent-mode-changes-in-elevenlabs-updates-2026-11-02|8 Agent Mode changes in ElevenLabs updates — 2026-11-02]] · Agent Mode
- [[Changes/ElevenLabs/2026-11-02-packages|Packages]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-workspaces|Workspaces]] · Agent Mode
- [[Changes/ElevenLabs/2026-11-02-2-files-and-data-changes-in-elevenlabs-updates-2026-11-02|2 Files and Data changes in ElevenLabs updates — 2026-11-02]] · Files and Data
- [[Changes/ElevenLabs/2026-11-02-android-sdk|Android SDK]] · Mobile and Desktop
- [[Changes/ElevenLabs/2026-11-02-eleven-realtime-for-every-workspace|Eleven Realtime for every workspace]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-noisy-environment-detection-in-the-api|Noisy environment detection in the API]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-unity-sdk|Unity SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-javascript-sdk|JavaScript SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-video-clip-background-removal-video-clips-have-a-remove-background-action-and-ri|Video clip background removal]] · Multimodal Input
- [[Changes/ElevenLabs/2026-11-02-svg-assets-svg-uploads-to-assets-stay-svg-and-render-as-vectors-including-in-the|SVG assets: SVG uploads to Assets stay SVG and render as vectors, including…]] · Editor Experience
- [[Changes/ElevenLabs/2026-11-02-channel-integrations-asynchronous-channels-such-as-slack-telegram-intercom-gmail|Channel integrations: Asynchronous channels such as Slack, Telegram, Intercom…]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-11-02-fixes-oauth-discovery-names-the-host-the-client-connected-to-so-mcp-clients-such|Fixes: OAuth discovery names the host the client connected to, so MCP clients…]] · Account and Access
- [[Changes/ElevenLabs/2026-11-02-16-voice-and-audio-changes-in-elevenlabs-updates-2026-11-02|16 Voice and Audio changes in ElevenLabs updates — 2026-11-02]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-fixes-history-items-for-v4-generations-keep-clone-strength-and-speed-in-their-sa|Fixes: History items for v4 generations keep clone_strength and speed…]] · Reliability and Performance
- [[Changes/ElevenLabs/2026-11-02-professional-voice-clones-on-eleven-v4|Professional Voice Clones on Eleven v4]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-7-other-changes-in-elevenlabs-updates-2026-11-02|7 other changes in ElevenLabs updates — 2026-11-02]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Voice and Audio

- Earlier: 2026-10-29 · Suno · [[Changes/Suno/2026-10-29-auto-stretch-for-added-audio|Auto-stretch for Added Audio]]
- Later: 2026-11-03 · Google Antigravity · [[Changes/Google Antigravity/2026-11-03-voice-mode-remote-agents-redesigned-automations-and-jupyter-notebook-viewer|Voice mode, remote agents, redesigned Automations, and Jupyter notebook viewer]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-07-09 · Descript · [[Changes/Descript/2018-07-09-type-in-parentheses-to-add-notes-to-your-script-that-don-t-affect-the-audio-text|Support for Inline Notes]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-11-02-f40dff&body=Card%3A%20Changes%2FElevenLabs%2F2026-11-02-realtime-entity-redaction.md%0ACard%20ID%3A%20elevenlabs-2026-11-02-f40dff%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F11%2F2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->