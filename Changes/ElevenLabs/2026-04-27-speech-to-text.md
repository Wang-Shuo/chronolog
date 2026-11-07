---
card_id: elevenlabs-2026-04-27-a00b08
date: '2026-04-27'
description: 'ElevenLabs · 2026-04-27 · Voice and Audio: **Realtime keyterms and verbatim
  mode**: The [Scribe realtime…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-07-09-type-in-parentheses-to-add-notes-to-your-script-that-don-t-affect-the-audio-text|Support
    for Inline Notes]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2849
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: voice
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: launch
machine_hash: d86a3aee130909f979a66180dc35a691986b2314335a36d2bcb2dd17fbaeb919
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-04-27-a00b08
  comparison: ''
  confidence: low
  date: '2026-04-27'
  description: 'ElevenLabs — ElevenLabs updates — 2026-04-27: **Realtime keyterms
    and verbatim mode**: The [Scribe realtime WebSocket](https://elevenlabs.io/docs/api-reference/speech-to-text/v-1-speech-to-text-realtime)
    now accepts a `keyterms` parameter (array of strings, max 50 entries of up to
    20 characters each) to bias the model toward specific terms, and a `no_verbatim`
    boolean to remove filler words, false starts, and disfluencies from transcripts.
    Both parameters are echoed back in the `session_started` event. Available across
    the [JavaScript SDK](https://github.com/elevenlabs/elevenlabs-js/releases/tag/v2.45.0),
    [Python SDK](https://github.com/elevenlabs/elevenlabs-python), and the [`@elevenlabs/client`](https://github.com/elevenlabs/packages/tree/main/packages/client)
    browser/Node client SDK.'
  evidence:
  - quote: '**Realtime keyterms and verbatim mode**: The [Scribe realtime WebSocket](https://elevenlabs.io/docs/api-reference/speech-to-text/v-1-speech-to-text-realtime)
      now accepts a `keyterms` parameter (array of strings, max 50 entries of up to
      20 characters each) to bias the model toward specific terms, and a `no_verbatim`
      boolean to remove filler words, false starts, and disfluencies from transcripts.
      Both parameters are echoed back in the `session_started` event. Available across
      the [JavaScript SDK](https://github.com/elevenlabs/elevenlabs-js/releases/tag/v2.45.0),
      [Python SDK](https://github.com/elevenlabs/elevenlabs-python), and the [`@elevenlabs/client`](https://github.com/elevenlabs/packages/tree/main/packages/client)
      browser/Node client SDK.'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/27
  extractor_version: fallback-v5
  impact: significant
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: speech-to-text
  source_release: elevenlabs-2026-04-27-2026-04-27-7b6333fc
  source_type: elevenlabs_changelog
  theme: voice
  title: Speech to Text
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-04-27-audio-isolation|Audio Isolation]]'
- '[[Changes/ElevenLabs/2026-04-27-new-endpoints|New Endpoints]]'
- '[[Changes/ElevenLabs/2026-04-27-elevenagents|ElevenAgents]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-04-27-2026-04-27-7b6333fc|elevenlabs-2026-04-27-2026-04-27-7b6333fc]]'
source_type: elevenlabs_changelog
theme: voice
title: Speech to Text
type: change
---

<!-- chronolog:begin region="header" -->
# Speech to Text

**ElevenLabs** · 2026-04-27 · [[Themes/voice|Voice and Audio]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/4/27) · from [[Releases/ElevenLabs/elevenlabs-2026-04-27-2026-04-27-7b6333fc|ElevenLabs updates — 2026-04-27]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **Realtime keyterms and verbatim mode**: The [Scribe realtime WebSocket](https://elevenlabs.io/docs/api-reference/speech-to-text/v-1-speech-to-text-realtime) now accepts a `keyterms` parameter (array of strings, max 50 entries of up to 20 characters each) to bias the model toward specific terms, and a `no_verbatim` boolean to remove filler words, false starts, and disfluencies from transcripts. Both parameters are echoed back in the `session_started` event. Available across the [JavaScript SDK](https://github.com/elevenlabs/elevenlabs-js/releases/tag/v2.45.0), [Python SDK](https://github.com/elevenlabs/elevenlabs-python), and the [`@elevenlabs/client`](https://github.com/elevenlabs/packages/tree/main/packages/client) browser/Node client SDK.
>
> Source: https://elevenlabs.io/docs/changelog/2026/4/27
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-04-27-python-sdk|Python SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-04-27-sdk-releases|SDK Releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-04-27-audio-isolation|Audio Isolation]] · Voice and Audio
- [[Changes/ElevenLabs/2026-04-27-other|Other]] · Collaboration
- [[Changes/ElevenLabs/2026-04-27-swift-sdk|Swift SDK]] · Agent Mode
- [[Changes/ElevenLabs/2026-04-27-new-endpoints|New Endpoints]] · Voice and Audio
- [[Changes/ElevenLabs/2026-04-27-packages|Packages]] · Agent Mode
- [[Changes/ElevenLabs/2026-04-27-elevenagents|ElevenAgents]] · Voice and Audio
- [[Changes/ElevenLabs/2026-04-27-elevenagents-e7cc6e|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-04-27-javascript-sdk|JavaScript SDK]] · Voice and Audio
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Voice and Audio

- Earlier: 2026-04-24 · Wispr Flow · [[Changes/Wispr Flow/2026-04-24-copy-button-after-dictation-android|Copy button after dictation (Android)]]
- Later: 2026-04-28 · Claude Code · [[Changes/Claude Code/2026-04-28-vscode-voice-dictation-now-respects-the-accessibility-voice-speechlanguage-setti|VSCode Voice dictation now respects the accessibility.voice.speechLanguage…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-07-09 · Descript · [[Changes/Descript/2018-07-09-type-in-parentheses-to-add-notes-to-your-script-that-don-t-affect-the-audio-text|Support for Inline Notes]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-04-27-a00b08&body=Card%3A%20Changes%2FElevenLabs%2F2026-04-27-speech-to-text.md%0ACard%20ID%3A%20elevenlabs-2026-04-27-a00b08%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F4%2F27%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->