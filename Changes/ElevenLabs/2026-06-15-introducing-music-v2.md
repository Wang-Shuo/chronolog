---
card_id: elevenlabs-2026-06-15-fe410e
date: '2026-06-15'
description: 'ElevenLabs · 2026-06-15 · Model Support: Music v2 is now available via
  the ElevenLabs API. Set `model_id` to `music_v2` on [Generate…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1253
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: launch
machine_hash: 5f099105607bb79ccb9f5ba3ef8713dc34be400f534526cd253cc00b582dbeb0
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-06-15-fe410e
  comparison: ''
  confidence: low
  date: '2026-06-15'
  description: 'ElevenLabs — ElevenLabs updates — 2026-06-15: Music v2 is now available
    via the ElevenLabs API. Set `model_id` to `music_v2` on [Generate music](https://elevenlabs.io/docs/api-reference/music/compose),
    [Stream music](https://elevenlabs.io/docs/api-reference/music/stream), [Generate
    music detailed](https://elevenlabs.io/docs/api-reference/music/compose-detailed)
    and [Upload music](https://elevenlabs.io/docs/api-reference/music/upload) to use
    the new model. Music v2 introduces chunk-based composition plans built from `GenerationChunk`
    and `AudioRefChunk` segments, giving you finer control over structure, pacing
    and arrangement than the prompt-based `music_v1` flow.'
  evidence:
  - quote: Music v2 is now available via the ElevenLabs API. Set `model_id` to `music_v2`
      on [Generate music](https://elevenlabs.io/docs/api-reference/music/compose),
      [Stream music](https://elevenlabs.io/docs/api-reference/music/stream), [Generate
      music detailed](https://elevenlabs.io/docs/api-reference/music/compose-detailed)
      and [Upload music](https://elevenlabs.io/docs/api-reference/music/upload) to
      use the new model. Music v2 introduces chunk-based composition plans built from
      `GenerationChunk` and `AudioRefChunk` segments, giving you finer control over
      structure, pacing and arrangement than the prompt-based `music_v1` flow.
    source_release: https://elevenlabs.io/docs/changelog/2026/6/15
  - quote: Use `music_v2` composition plans on generation and upload requests, or
      generate a plan first via the composition-plan endpoint. Request and response
      bodies accept either v1 or v2 plan shapes, so you can migrate endpoint by endpoint.
      `MusicPrompt` remains available for `music_v1` only.
    source_release: https://elevenlabs.io/docs/changelog/2026/6/15
  - quote: '**Upload timestamps**: [Upload music](https://elevenlabs.io/docs/api-reference/music/upload)
      accepts optional `with_timestamps`; responses may include `words_timestamps`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/15
  extractor_version: fallback-v5
  impact: significant
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: introducing-music-v2
  source_release: elevenlabs-2026-06-15-2026-06-15-9835dce0
  source_type: elevenlabs_changelog
  theme: model-support
  title: Introducing Music v2
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-06-13-3-model-support-changes-in-v1-0-62|3 Model
  Support changes in v1.0.62]]'
- '[[Changes/Claude Code/2026-06-15-bug-now-requires-a-description-before-submitting-and-no-longer-uses-model-refusa|/bug
  now requires a description before submitting, and no longer uses…]]'
- '[[Changes/Codex CLI/2026-06-15-4-model-support-changes-in-rust-v0-140-0|4 Model
  Support changes in rust-v0.140.0]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-06-15-2026-06-15-9835dce0|elevenlabs-2026-06-15-2026-06-15-9835dce0]]'
source_type: elevenlabs_changelog
theme: model-support
title: Introducing Music v2
type: change
---

<!-- chronolog:begin region="header" -->
# Introducing Music v2

**ElevenLabs** · 2026-06-15 · [[Themes/model-support|Model Support]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/6/15) · from [[Releases/ElevenLabs/elevenlabs-2026-06-15-2026-06-15-9835dce0|ElevenLabs updates — 2026-06-15]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Music v2 is now available via the ElevenLabs API. Set `model_id` to `music_v2` on [Generate music](https://elevenlabs.io/docs/api-reference/music/compose), [Stream music](https://elevenlabs.io/docs/api-reference/music/stream), [Generate music detailed](https://elevenlabs.io/docs/api-reference/music/compose-detailed) and [Upload music](https://elevenlabs.io/docs/api-reference/music/upload) to use the new model. Music v2 introduces chunk-based composition plans built from `GenerationChunk` and `AudioRefChunk` segments, giving you finer control over structure, pacing and arrangement than the prompt-based `music_v1` flow.
>
> Use `music_v2` composition plans on generation and upload requests, or generate a plan first via the composition-plan endpoint. Request and response bodies accept either v1 or v2 plan shapes, so you can migrate endpoint by endpoint. `MusicPrompt` remains available for `music_v1` only.
>
> **Upload timestamps**: [Upload music](https://elevenlabs.io/docs/api-reference/music/upload) accepts optional `with_timestamps`; responses may include `words_timestamps`.
>
> Source: https://elevenlabs.io/docs/changelog/2026/6/15
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-06-15-voices|Voices]] · Voice and Audio
- [[Changes/ElevenLabs/2026-06-15-sdk-releases|SDK Releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-06-15-voices-364b13|Voices]] · Voice and Audio
- [[Changes/ElevenLabs/2026-06-15-javascript-sdk|JavaScript SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-06-15-elevenagents|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-06-15-packages|Packages]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-06-15-workspaces|Workspaces]] · Editor Experience
- [[Changes/ElevenLabs/2026-06-15-elevencreative-studio|ElevenCreative Studio]] · Voice and Audio
- [[Changes/ElevenLabs/2026-06-15-python-sdk|Python SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-06-15-speech-to-text|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-06-15-speech-to-text-d2421e|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-06-15-ios-sdk|iOS SDK]] · Mobile and Desktop
- [[Changes/ElevenLabs/2026-06-15-elevencreative-studio-f3d23d|ElevenCreative Studio]] · Voice and Audio
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-06-15 · Codex CLI · [[Changes/Codex CLI/2026-06-15-4-model-support-changes-in-rust-v0-140-0|4 Model Support changes in rust-v0.140.0]]
- Later: 2026-06-15 · Kimi Code · [[Changes/Kimi Code/2026-06-15-2-model-support-changes-in-kimi-code-0-15-0|2 Model Support changes in Kimi Code 0.15.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-06-15-fe410e&body=Card%3A%20Changes%2FElevenLabs%2F2026-06-15-introducing-music-v2.md%0ACard%20ID%3A%20elevenlabs-2026-06-15-fe410e%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F6%2F15%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->