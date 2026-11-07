---
card_id: elevenlabs-2026-02-23-48c08c
date: '2026-02-23'
description: 'ElevenLabs · 2026-02-23 · Voice and Audio: [Create voice previews](https://elevenlabs.io/docs/api-reference/legacy/voices/create-previews),
  [Design…'
diffusion:
  first_in_tracked: '[[Changes/Dify/2023-07-10-2-voice-and-audio-changes-in-0-3-7|2
    Voice and Audio changes in 0.3.7]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 959
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: voice
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: launch
machine_hash: 92d258f53ee7f7acf06cbd003b4d1aaf147f634b725709cfb23f0490cbd6bb2c
product: elevenlabs
product_name: ElevenLabs
record:
  card_id: elevenlabs-2026-02-23-48c08c
  comparison: ''
  date: '2026-02-23'
  description: 'ElevenLabs — ElevenLabs updates — 2026-02-23: [Create voice previews](https://elevenlabs.io/docs/api-reference/legacy/voices/create-previews),
    [Design voice](https://elevenlabs.io/docs/api-reference/text-to-voice/design),
    [Remix voice](https://elevenlabs.io/docs/api-reference/text-to-voice/remix)'
  evidence:
  - quote: '[Create voice previews](https://elevenlabs.io/docs/api-reference/legacy/voices/create-previews),
      [Design voice](https://elevenlabs.io/docs/api-reference/text-to-voice/design),
      [Remix voice](https://elevenlabs.io/docs/api-reference/text-to-voice/remix)'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/23
  - quote: 'Updated `loudness` parameter description: Controls the volume level of
      the generated voice. -1 is quietest, 1 is loudest, 0 corresponds to roughly
      -24 LUFS'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/23
  - quote: 'Updated `guidance_scale` parameter description: Controls how closely the
      AI follows the prompt. Lower numbers give the AI more freedom to be creative,
      while higher numbers force it to stick more to the prompt. High numbers can
      cause voice to sound artificial or robotic. Longer, more detailed prompts work
      better at lower guidance scale.'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/23
  - quote: Updated `quality` parameter description for voice preview creation
    source_release: https://elevenlabs.io/docs/changelog/2026/2/23
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: text-to-voice
  source_release: elevenlabs-2026-02-23-2026-02-23-19067983
  source_type: elevenlabs_changelog
  theme: voice
  title: Text to Voice
  type: change
related_changes:
- "[[Changes/Open WebUI/2026-02-12-audio-service-timeout-handling-audio-transcription-and-text-to-speech-requests-n|\U0001F50C
  Audio service timeout handling. Audio transcription and text-to-speech…]]"
- '[[Changes/Open WebUI/2026-02-16-resource-handle-cleanup-file-handles-are-now-properly-closed-during-audio-transc|♻️
  Resource handle cleanup. File handles are now properly closed during audio…]]'
- '[[Changes/ElevenLabs/2026-02-23-javascript-sdk|JavaScript SDK]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-02-23-2026-02-23-19067983|elevenlabs-2026-02-23-2026-02-23-19067983]]'
source_type: elevenlabs_changelog
theme: voice
title: Text to Voice
type: change
---

<!-- chronolog:begin region="header" -->
# Text to Voice

**ElevenLabs** · 2026-02-23 · [[Themes/voice|Voice and Audio]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/2/23) · from [[Releases/ElevenLabs/elevenlabs-2026-02-23-2026-02-23-19067983|ElevenLabs updates — 2026-02-23]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> [Create voice previews](https://elevenlabs.io/docs/api-reference/legacy/voices/create-previews), [Design voice](https://elevenlabs.io/docs/api-reference/text-to-voice/design), [Remix voice](https://elevenlabs.io/docs/api-reference/text-to-voice/remix)
>
> Updated `loudness` parameter description: Controls the volume level of the generated voice. -1 is quietest, 1 is loudest, 0 corresponds to roughly -24 LUFS
>
> Updated `guidance_scale` parameter description: Controls how closely the AI follows the prompt. Lower numbers give the AI more freedom to be creative, while higher numbers force it to stick more to the prompt. High numbers can cause voice to sound artificial or robotic. Longer, more detailed prompts work better at lower guidance scale.
>
> Updated `quality` parameter description for voice preview creation
>
> Source: https://elevenlabs.io/docs/changelog/2026/2/23
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-02-23-javascript-sdk|JavaScript SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-02-23-sdk-releases|SDK Releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-02-23-workspaces|Workspaces]] · Safety and Privacy
- [[Changes/ElevenLabs/2026-02-23-python-sdk|Python SDK]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-02-23-elevenagents|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-02-23-music|Music]] · Collaboration
- [[Changes/ElevenLabs/2026-02-23-removed-endpoints|Removed Endpoints]] · Voice and Audio
- [[Changes/ElevenLabs/2026-02-23-voices|Voices]] · Voice and Audio
- [[Changes/ElevenLabs/2026-02-23-elevenagents-f6efef|ElevenAgents]] · Account and Access
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Voice and Audio

- Earlier: 2026-02-16 · Open WebUI · [[Changes/Open WebUI/2026-02-16-resource-handle-cleanup-file-handles-are-now-properly-closed-during-audio-transc|♻️ Resource handle cleanup. File handles are now properly closed during audio…]]
- Later: 2026-02-23 · Open WebUI · [[Changes/Open WebUI/2026-02-23-voice-dictation-shortcut-users-can-now-toggle-voice-dictation-using-cmd-shift-l|⌨️ Voice dictation shortcut. Users can now toggle voice dictation using…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-10 · Dify · [[Changes/Dify/2023-07-10-2-voice-and-audio-changes-in-0-3-7|2 Voice and Audio changes in 0.3.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-02-23-48c08c&body=Card%3A%20Changes%2FElevenLabs%2F2026-02-23-text-to-voice.md%0ACard%20ID%3A%20elevenlabs-2026-02-23-48c08c%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F2%2F23%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->