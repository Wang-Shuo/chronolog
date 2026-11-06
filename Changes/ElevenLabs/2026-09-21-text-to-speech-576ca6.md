---
card_id: elevenlabs-2026-09-21-576ca6
date: '2026-09-21'
description: 'ElevenLabs · 2026-09-21 · Model Support: **Multi-context turn boundaries**:
  The `is_final_audio_for_turn` marker is now emitted after every buffered byte for…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1351
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: launch
machine_hash: fbf04f6a2181cb1587f176eb5c8e2f007467649f93d4f249a2121c85d6a57796
product: elevenlabs
product_name: ElevenLabs
record:
  card_id: elevenlabs-2026-09-21-576ca6
  comparison: ''
  date: '2026-09-21'
  description: 'ElevenLabs — ElevenLabs updates — 2026-09-21: **Multi-context turn
    boundaries**: The `is_final_audio_for_turn` marker is now emitted after every
    buffered byte for that turn, including MP3 and Opus output. Clients can use the
    marker as an exact turn boundary without switching to PCM.'
  evidence:
  - quote: '**Multi-context turn boundaries**: The `is_final_audio_for_turn` marker
      is now emitted after every buffered byte for that turn, including MP3 and Opus
      output. Clients can use the marker as an exact turn boundary without switching
      to PCM.'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/21
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: text-to-speech
  source_release: elevenlabs-2026-09-21-2026-09-21-6d2d4d80
  source_type: elevenlabs_changelog
  theme: model-support
  theme_matches:
  - matched_terms:
    - context
    score: 50
    theme: context-window
  - matched_terms:
    - opus
    score: 50
    theme: model-support
  - matched_terms:
    - audio
    score: 50
    theme: voice
  theme_resolution: manual-semantic-rule-v2
  title: Text to Speech
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-18-changed-fable-to-always-appear-in-model-on-the-anthropic-api-it-is-greyed-out-on|Changed
  Fable to always appear in /model on the Anthropic API]]'
- '[[Changes/Codex CLI/2026-09-18-2-model-support-changes-in-rust-v0-155-1|2 Model
  Support changes in rust-v0.155.1]]'
- '[[Changes/Ollama/2026-09-19-2-model-support-changes-in-v0-34-3|2 Model Support
  changes in v0.34.3]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-09-21-2026-09-21-6d2d4d80|elevenlabs-2026-09-21-2026-09-21-6d2d4d80]]'
source_type: elevenlabs_changelog
theme: model-support
title: Text to Speech
type: change
---

<!-- chronolog:begin region="header" -->
# Text to Speech

**ElevenLabs** · 2026-09-21 · [[Themes/model-support|Model Support]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/9/21) · from [[Releases/ElevenLabs/elevenlabs-2026-09-21-2026-09-21-6d2d4d80|ElevenLabs updates — 2026-09-21]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **Multi-context turn boundaries**: The `is_final_audio_for_turn` marker is now emitted after every buffered byte for that turn, including MP3 and Opus output. Clients can use the marker as an exact turn boundary without switching to PCM.
>
> Source: https://elevenlabs.io/docs/changelog/2026/9/21
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-09-21-image-and-video|Image and video]] · Image Generation
- [[Changes/ElevenLabs/2026-09-21-text-to-speech|Text to Speech]] · Voice and Audio
- [[Changes/ElevenLabs/2026-09-21-sdk-releases|SDK releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-09-21-javascript-sdk|JavaScript SDK]] · Model Support
- [[Changes/ElevenLabs/2026-09-21-elevenagents|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-09-21-python-sdk|Python SDK]] · Model Support
- [[Changes/ElevenLabs/2026-09-21-user|User]] · Pricing Model
- [[Changes/ElevenLabs/2026-09-21-image-and-video-915070|Image and video]] · Image Generation
- [[Changes/ElevenLabs/2026-09-21-elevenagents-d15bdd|ElevenAgents]] · Agent Mode
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-09-19 · Ollama · [[Changes/Ollama/2026-09-19-2-model-support-changes-in-v0-34-3|2 Model Support changes in v0.34.3]]
- Later: 2026-09-21 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-09-21-enable-the-rubber-duck-agent-for-every-model-family-and-for-low-cost-tier-sessio|Enable the rubber-duck agent for every model family and for low-cost-tier session models]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-09-21-576ca6&body=Card%3A%20Changes%2FElevenLabs%2F2026-09-21-text-to-speech-576ca6.md%0ACard%20ID%3A%20elevenlabs-2026-09-21-576ca6%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F9%2F21%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->