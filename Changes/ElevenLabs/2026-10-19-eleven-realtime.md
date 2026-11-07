---
card_id: elevenlabs-2026-10-19-5913f6
date: '2026-10-19'
description: 'ElevenLabs · 2026-10-19 · Voice and Audio: Eleven Realtime is a new
  family of models for ElevenAgents voice agents, rolling out gradually across workspaces…'
diffusion:
  first_in_tracked: '[[Changes/Dify/2023-07-10-2-voice-and-audio-changes-in-0-3-7|2
    Voice and Audio changes in 0.3.7]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1197
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: voice
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: cd877eb11b135a774df09eedf5b0a4cb8002d8305cfeb320e5119a5d39db3e76
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-10-19-5913f6
  comparison: ''
  confidence: low
  date: '2026-10-19'
  description: 'ElevenLabs — ElevenLabs updates — 2026-10-19: Eleven Realtime is a
    new family of models for ElevenAgents voice agents, rolling out gradually across
    workspaces. Each one is a complete voice agent configuration. You pick one model,
    and ElevenLabs handles the LLM, Speech to Text and Text to Speech settings behind
    it. Your agent''s system prompt, voice, tools and knowledge base work the same
    as before.'
  evidence:
  - quote: Eleven Realtime is a new family of models for ElevenAgents voice agents,
      rolling out gradually across workspaces. Each one is a complete voice agent
      configuration. You pick one model, and ElevenLabs handles the LLM, Speech to
      Text and Text to Speech settings behind it. Your agent's system prompt, voice,
      tools and knowledge base work the same as before.
    source_release: https://elevenlabs.io/docs/changelog/2026/10/19
  - quote: There are two to choose from. Eleven Realtime v1 Mini (`eleven_realtime_v1_mini`)
      is the default, and it's the fastest and cheapest. Eleven Realtime v1 Max (`eleven_realtime_v1_max`)
      reasons before it answers, so use it when your agent has complex instructions
      or multi-step tool calls.
    source_release: https://elevenlabs.io/docs/changelog/2026/10/19
  - quote: If you've already built on OpenAI's Realtime API, you don't need to rewrite
      your client. The events and the WebSocket transport are the same, so you change
      the endpoint and the session configuration. Your backend calls [Create realtime
      client secret](https://elevenlabs.io/docs/api-reference/conversations/create-client-secret)
      to get a short-lived secret, and the browser uses it to connect directly.
    source_release: https://elevenlabs.io/docs/changelog/2026/10/19
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: eleven-realtime
  source_release: elevenlabs-2026-10-19-2026-10-19-dd219c14
  source_type: elevenlabs_changelog
  theme: voice
  theme_matches:
  - matched_terms:
    - voice
    - speech to text
    score: 180
    theme: voice
  - matched_terms:
    - llm
    - model
    - models
    score: 150
    theme: model-support
  - matched_terms:
    - agent
    - agents
    score: 100
    theme: agent-mode
  title: Eleven Realtime
  type: change
related_changes:
- '[[Changes/Lovable/2026-10-16-gpt-transcribe-for-your-app-s-speech-to-text-features|GPT
  Transcribe for your app''s speech-to-text features]]'
- '[[Changes/OpenClaw/2026-10-16-discord-voice-changes-you-can-change-voices-and-continue-asking-for-agent-checks|Discord
  voice changes]]'
- '[[Changes/ElevenLabs/2026-10-19-speech-to-text|Speech to Text]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-10-19-2026-10-19-dd219c14|elevenlabs-2026-10-19-2026-10-19-dd219c14]]'
source_type: elevenlabs_changelog
theme: voice
title: Eleven Realtime
type: change
---

<!-- chronolog:begin region="header" -->
# Eleven Realtime

**ElevenLabs** · 2026-10-19 · [[Themes/voice|Voice and Audio]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/10/19) · from [[Releases/ElevenLabs/elevenlabs-2026-10-19-2026-10-19-dd219c14|ElevenLabs updates — 2026-10-19]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Eleven Realtime is a new family of models for ElevenAgents voice agents, rolling out gradually across workspaces. Each one is a complete voice agent configuration. You pick one model, and ElevenLabs handles the LLM, Speech to Text and Text to Speech settings behind it. Your agent's system prompt, voice, tools and knowledge base work the same as before.
>
> There are two to choose from. Eleven Realtime v1 Mini (`eleven_realtime_v1_mini`) is the default, and it's the fastest and cheapest. Eleven Realtime v1 Max (`eleven_realtime_v1_max`) reasons before it answers, so use it when your agent has complex instructions or multi-step tool calls.
>
> If you've already built on OpenAI's Realtime API, you don't need to rewrite your client. The events and the WebSocket transport are the same, so you change the endpoint and the session configuration. Your backend calls [Create realtime client secret](https://elevenlabs.io/docs/api-reference/conversations/create-client-secret) to get a short-lived secret, and the browser uses it to connect directly.
>
> Source: https://elevenlabs.io/docs/changelog/2026/10/19
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-10-19-speech-to-text|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-19-sdk-releases|SDK releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-10-19-music-and-sound-effects|Music and Sound Effects]] · Enterprise and Administration
- [[Changes/ElevenLabs/2026-10-19-elevenagents|ElevenAgents]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-19-video-to-music|Video to Music]] · Multimodal Input
- [[Changes/ElevenLabs/2026-10-19-realtime-translation|Realtime Translation]] · Enterprise and Administration
- [[Changes/ElevenLabs/2026-10-19-javascript-sdk|JavaScript SDK]] · Agent Mode
- [[Changes/ElevenLabs/2026-10-19-elevenagents-b18b24|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-10-19-music|Music]] · Multimodal Input
- [[Changes/ElevenLabs/2026-10-19-voices|Voices]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-19-python-sdk|Python SDK]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-10-19-elevenagents-ee74ab|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-10-19-voices-f9aa8c|Voices]] · Voice and Audio
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Voice and Audio

- Earlier: 2026-10-16 · OpenClaw · [[Changes/OpenClaw/2026-10-16-discord-voice-changes-you-can-change-voices-and-continue-asking-for-agent-checks|Discord voice changes]]
- Later: 2026-10-19 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-10-19-voice-dictation-no-longer-inserts-language-markers-like-en-us-into-transcript-te|Voice dictation no longer inserts language markers like en-US into transcript text]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-10 · Dify · [[Changes/Dify/2023-07-10-2-voice-and-audio-changes-in-0-3-7|2 Voice and Audio changes in 0.3.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-10-19-5913f6&body=Card%3A%20Changes%2FElevenLabs%2F2026-10-19-eleven-realtime.md%0ACard%20ID%3A%20elevenlabs-2026-10-19-5913f6%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F10%2F19%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->