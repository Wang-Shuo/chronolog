---
card_id: elevenlabs-2026-09-14-bdb11f
date: '2026-09-14'
description: 'ElevenLabs · 2026-09-14 · Voice and Audio: **Call queueing and hold
  audio**: Added [call…'
diffusion:
  first_in_tracked: '[[Changes/Dify/2023-07-10-2-voice-and-audio-changes-in-0-3-7|2
    Voice and Audio changes in 0.3.7]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1162
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: voice
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: launch
machine_hash: 1308c04b3a368123fa020a2f14020d5463a61907b13489e8d82f9a0d6e81f12a
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-09-14-bdb11f
  comparison: ''
  confidence: low
  date: '2026-09-14'
  description: 'ElevenLabs — ElevenLabs updates — 2026-09-14: **Call queueing and
    hold audio**: Added [call queueing](https://elevenlabs.io/docs/eleven-agents/guides/call-queueing)
    for agents at their concurrency limit. Queued callers hear hold audio and receive
    `queue_status` events until they are admitted or time out. New API methods upload
    or delete custom hold audio.'
  evidence:
  - quote: '**Call queueing and hold audio**: Added [call queueing](https://elevenlabs.io/docs/eleven-agents/guides/call-queueing)
      for agents at their concurrency limit. Queued callers hear hold audio and receive
      `queue_status` events until they are admitted or time out. New API methods upload
      or delete custom hold audio.'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/14
  - quote: '**Test version metadata**: Agent test results now identify the agent version
      they ran against and whether they included draft changes. Invocation summaries
      also indicate when partial resubmissions ran against different versions.'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/14
  - quote: '**Model and account metadata**: Agent LLM configuration now accepts `gemini-3.8-flash`.
      WhatsApp account responses identify whether the account uses the Cloud API or
      coexistence signup flow.'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/14
  extractor_version: fallback-v5
  impact: significant
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-09-14-2026-09-14-583c2a71
  source_type: elevenlabs_changelog
  theme: voice
  theme_matches:
  - matched_terms:
    - agents
    score: 50
    theme: agent-mode
  - matched_terms:
    - audio
    score: 50
    theme: voice
  theme_resolution: manual-semantic-rule-v1
  title: ElevenAgents
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-09-07-workspaces|Workspaces]]'
- '[[Changes/Codex CLI/2026-09-09-20-voice-and-audio-changes-in-rust-v0-154-0|20 Voice
  and Audio changes in rust-v0.154.0]]'
- '[[Changes/ElevenLabs/2026-09-14-packages|Packages]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-09-14-2026-09-14-583c2a71|elevenlabs-2026-09-14-2026-09-14-583c2a71]]'
source_type: elevenlabs_changelog
theme: voice
title: ElevenAgents
type: change
---

<!-- chronolog:begin region="header" -->
# ElevenAgents

**ElevenLabs** · 2026-09-14 · [[Themes/voice|Voice and Audio]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/9/14) · from [[Releases/ElevenLabs/elevenlabs-2026-09-14-2026-09-14-583c2a71|ElevenLabs updates — 2026-09-14]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **Call queueing and hold audio**: Added [call queueing](https://elevenlabs.io/docs/eleven-agents/guides/call-queueing) for agents at their concurrency limit. Queued callers hear hold audio and receive `queue_status` events until they are admitted or time out. New API methods upload or delete custom hold audio.
>
> **Test version metadata**: Agent test results now identify the agent version they ran against and whether they included draft changes. Invocation summaries also indicate when partial resubmissions ran against different versions.
>
> **Model and account metadata**: Agent LLM configuration now accepts `gemini-3.8-flash`. WhatsApp account responses identify whether the account uses the Cloud API or coexistence signup flow.
>
> Source: https://elevenlabs.io/docs/changelog/2026/9/14
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-09-14-sdk-releases|SDK releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-09-14-packages|Packages]] · Voice and Audio
- [[Changes/ElevenLabs/2026-09-14-elevenagents|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-09-14-ios-sdk|iOS SDK]] · Mobile and Desktop
- [[Changes/ElevenLabs/2026-09-14-javascript-sdk|JavaScript SDK]] · Model Support
- [[Changes/ElevenLabs/2026-09-14-python-sdk|Python SDK]] · Model Support
- [[Changes/ElevenLabs/2026-09-14-music|Music]] · Multimodal Input
- [[Changes/ElevenLabs/2026-09-14-elevenagents-d9e798|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-09-14-elevenagents-dab1d0|ElevenAgents]] · Voice and Audio
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Voice and Audio

- Earlier: 2026-09-09 · Codex CLI · [[Changes/Codex CLI/2026-09-09-20-voice-and-audio-changes-in-rust-v0-154-0|20 Voice and Audio changes in rust-v0.154.0]]
- Later: 2026-09-17 · Codex CLI · [[Changes/Codex CLI/2026-09-17-20-voice-and-audio-changes-in-rust-v0-155-0|20 Voice and Audio changes in rust-v0.155.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-10 · Dify · [[Changes/Dify/2023-07-10-2-voice-and-audio-changes-in-0-3-7|2 Voice and Audio changes in 0.3.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-09-14-bdb11f&body=Card%3A%20Changes%2FElevenLabs%2F2026-09-14-elevenagents-bdb11f.md%0ACard%20ID%3A%20elevenlabs-2026-09-14-bdb11f%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F9%2F14%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->