---
card_id: elevenlabs-2026-09-14-d9e798
date: '2026-09-14'
description: 'ElevenLabs · 2026-09-14 · Agent Mode: [Upload agent hold audio](https://elevenlabs.io/docs/api-reference/agents/hold-audio/create)
  - `POST…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1166
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: 3ab51a769704f2f3769ed8b860533a3aa37ff4f6a86531d3e92b59c458ff468e
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-09-14-d9e798
  comparison: ''
  confidence: low
  date: '2026-09-14'
  description: 'ElevenLabs — ElevenLabs updates — 2026-09-14: [Upload agent hold audio](https://elevenlabs.io/docs/api-reference/agents/hold-audio/create)
    - `POST /v1/convai/agents/{agent_id}/hold-audio`'
  evidence:
  - quote: '[Upload agent hold audio](https://elevenlabs.io/docs/api-reference/agents/hold-audio/create)
      - `POST /v1/convai/agents/{agent_id}/hold-audio`'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/14
  - quote: Accepts required `hold_audio_file` (binary) as multipart form data. The
      file must be MP3 or WAV, up to 40 MB and 180 seconds.
    source_release: https://elevenlabs.io/docs/changelog/2026/9/14
  - quote: Returns required `agent_id` (string) and `hold_audio` (`AgentHoldAudioConfig`).
      The hold-audio object requires `audio_path`, `audio_url`, `original_filename`
      (strings), `duration_secs` (number) and `size_bytes` (integer).
    source_release: https://elevenlabs.io/docs/changelog/2026/9/14
  - quote: '[Delete agent hold audio](https://elevenlabs.io/docs/api-reference/agents/hold-audio/delete)
      - `DELETE /v1/convai/agents/{agent_id}/hold-audio`'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/14
  - quote: Removes the custom clip so queued callers hear the default hold tone.
    source_release: https://elevenlabs.io/docs/changelog/2026/9/14
  - quote: Returns required `agent_id` (string).
    source_release: https://elevenlabs.io/docs/changelog/2026/9/14
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-09-14-2026-09-14-583c2a71
  source_type: elevenlabs_changelog
  theme: agent-mode
  theme_matches:
  - matched_terms:
    - agent
    - agents
    score: 100
    theme: agent-mode
  - matched_terms:
    - audio
    score: 50
    theme: voice
  title: ElevenAgents
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-09-11-25-agent-mode-changes-in-v2026-9-4|25 Agent Mode
  changes in v2026.9.4]]'
- '[[Changes/Claude Code/2026-09-14-7-agent-mode-changes-in-v2-1-271|7 Agent Mode
  changes in v2.1.271]]'
- '[[Changes/ElevenLabs/2026-09-14-elevenagents|ElevenAgents]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-09-14-2026-09-14-583c2a71|elevenlabs-2026-09-14-2026-09-14-583c2a71]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: ElevenAgents
type: change
---

<!-- chronolog:begin region="header" -->
# ElevenAgents

**ElevenLabs** · 2026-09-14 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/9/14) · from [[Releases/ElevenLabs/elevenlabs-2026-09-14-2026-09-14-583c2a71|ElevenLabs updates — 2026-09-14]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> [Upload agent hold audio](https://elevenlabs.io/docs/api-reference/agents/hold-audio/create) - `POST /v1/convai/agents/{agent_id}/hold-audio`
>
> Accepts required `hold_audio_file` (binary) as multipart form data. The file must be MP3 or WAV, up to 40 MB and 180 seconds.
>
> Returns required `agent_id` (string) and `hold_audio` (`AgentHoldAudioConfig`). The hold-audio object requires `audio_path`, `audio_url`, `original_filename` (strings), `duration_secs` (number) and `size_bytes` (integer).
>
> [Delete agent hold audio](https://elevenlabs.io/docs/api-reference/agents/hold-audio/delete) - `DELETE /v1/convai/agents/{agent_id}/hold-audio`
>
> Removes the custom clip so queued callers hear the default hold tone.
>
> Returns required `agent_id` (string).
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
- [[Changes/ElevenLabs/2026-09-14-elevenagents-bdb11f|ElevenAgents]] · Voice and Audio
- [[Changes/ElevenLabs/2026-09-14-music|Music]] · Multimodal Input
- [[Changes/ElevenLabs/2026-09-14-elevenagents-dab1d0|ElevenAgents]] · Voice and Audio
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-09-14 · Claude Code · [[Changes/Claude Code/2026-09-14-7-agent-mode-changes-in-v2-1-271|7 Agent Mode changes in v2.1.271]]
- Later: 2026-09-15 · Claude Code · [[Changes/Claude Code/2026-09-15-changed-auto-mode-on-bedrock-vertex-and-foundry-to-use-the-local-classifier-by-d|Changed auto mode on Bedrock, Vertex and Foundry to use the local classifier…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-09-14-d9e798&body=Card%3A%20Changes%2FElevenLabs%2F2026-09-14-elevenagents-d9e798.md%0ACard%20ID%3A%20elevenlabs-2026-09-14-d9e798%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F9%2F14%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->