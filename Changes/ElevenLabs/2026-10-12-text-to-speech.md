---
card_id: elevenlabs-2026-10-12-3e94ad
date: '2026-10-12'
description: 'ElevenLabs · 2026-10-12 · Voice and Audio: **Audio effects**: [Text
  to Speech](https://elevenlabs.io/docs/api-reference/text-to-speech/convert) and
  [Text to…'
diffusion:
  first_in_tracked: '[[Changes/Dify/2023-07-10-2-voice-and-audio-changes-in-0-3-7|2
    Voice and Audio changes in 0.3.7]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1190
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: voice
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: launch
machine_hash: 5491c1d06b7968358437479a9b372c8cddfd8e890e1ab91f7e2eb5233a4bc446
product: elevenlabs
product_name: ElevenLabs
record:
  card_id: elevenlabs-2026-10-12-3e94ad
  comparison: ''
  date: '2026-10-12'
  description: 'ElevenLabs — ElevenLabs updates — 2026-10-12: **Audio effects**: [Text
    to Speech](https://elevenlabs.io/docs/api-reference/text-to-speech/convert) and
    [Text to Dialogue](https://elevenlabs.io/docs/api-reference/text-to-dialogue/convert)
    requests accept an optional `audio_effects` object. It applies a filter preset,
    perceived distance, a reverb environment, a looped background noise bed and stereo
    panning to the generated audio. List valid preset, environment and background
    noise IDs with `GET /v1/audio-effects/catalog`. Reverb and non-zero panning produce
    stereo audio and are rejected for `ulaw_*`, `alaw_*` and `pcm_*` output formats.
    Effects do not change the cost of a request.'
  evidence:
  - quote: '**Audio effects**: [Text to Speech](https://elevenlabs.io/docs/api-reference/text-to-speech/convert)
      and [Text to Dialogue](https://elevenlabs.io/docs/api-reference/text-to-dialogue/convert)
      requests accept an optional `audio_effects` object. It applies a filter preset,
      perceived distance, a reverb environment, a looped background noise bed and
      stereo panning to the generated audio. List valid preset, environment and background
      noise IDs with `GET /v1/audio-effects/catalog`. Reverb and non-zero panning
      produce stereo audio and are rejected for `ulaw_*`, `alaw_*` and `pcm_*` output
      formats. Effects do not change the cost of a request.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/12
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: text-to-speech
  source_release: elevenlabs-2026-10-12-2026-10-12-16e5a6a0
  source_type: elevenlabs_changelog
  theme: voice
  title: Text to Speech
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-10-08-2-voice-and-audio-changes-in-rust-v0-162-0|2 Voice
  and Audio changes in rust-v0.162.0]]'
- '[[Changes/Open WebUI/2026-10-10-12-voice-and-audio-changes-in-v0-12-0|12 Voice
  and Audio changes in v0.12.0]]'
- '[[Changes/ElevenLabs/2026-10-12-javascript-sdk|JavaScript SDK]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-10-12-2026-10-12-16e5a6a0|elevenlabs-2026-10-12-2026-10-12-16e5a6a0]]'
source_type: elevenlabs_changelog
theme: voice
title: Text to Speech
type: change
---

<!-- chronolog:begin region="header" -->
# Text to Speech

**ElevenLabs** · 2026-10-12 · [[Themes/voice|Voice and Audio]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/10/12) · from [[Releases/ElevenLabs/elevenlabs-2026-10-12-2026-10-12-16e5a6a0|ElevenLabs updates — 2026-10-12]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **Audio effects**: [Text to Speech](https://elevenlabs.io/docs/api-reference/text-to-speech/convert) and [Text to Dialogue](https://elevenlabs.io/docs/api-reference/text-to-dialogue/convert) requests accept an optional `audio_effects` object. It applies a filter preset, perceived distance, a reverb environment, a looped background noise bed and stereo panning to the generated audio. List valid preset, environment and background noise IDs with `GET /v1/audio-effects/catalog`. Reverb and non-zero panning produce stereo audio and are rejected for `ulaw_*`, `alaw_*` and `pcm_*` output formats. Effects do not change the cost of a request.
>
> Source: https://elevenlabs.io/docs/changelog/2026/10/12
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-10-12-elevenagents|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-10-12-javascript-sdk|JavaScript SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-12-sdk-releases|SDK releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-10-12-elevenagents-545be2|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-10-12-speech-to-text|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-12-packages|Packages]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-12-music|Music]] · Multimodal Input
- [[Changes/ElevenLabs/2026-10-12-text-to-dialogue|Text to Dialogue]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-12-elevenlabs-cli|ElevenLabs CLI]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-12-voices|Voices]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-12-python-sdk|Python SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-12-audio-effects|Audio effects]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-12-voices-e71bd5|Voices]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-12-speech-to-text-f7d11e|Speech to Text]] · Voice and Audio
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Voice and Audio

- Earlier: 2026-10-10 · Open WebUI · [[Changes/Open WebUI/2026-10-10-12-voice-and-audio-changes-in-v0-12-0|12 Voice and Audio changes in v0.12.0]]
- Later: 2026-10-14 · Claude Code · [[Changes/Claude Code/2026-10-14-claude-tag-added-support-for-slack-voice-clips-in-claude-in-slack-claude-reads-s|Claude Tag Added support for Slack voice clips in Claude in Slack]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-10 · Dify · [[Changes/Dify/2023-07-10-2-voice-and-audio-changes-in-0-3-7|2 Voice and Audio changes in 0.3.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-10-12-3e94ad&body=Card%3A%20Changes%2FElevenLabs%2F2026-10-12-text-to-speech.md%0ACard%20ID%3A%20elevenlabs-2026-10-12-3e94ad%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F10%2F12%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->