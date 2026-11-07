---
card_id: elevenlabs-2026-10-19-a35702
date: '2026-10-19'
description: 'ElevenLabs · 2026-10-19 · Agent Mode: [v2.74.0](https://github.com/elevenlabs/elevenlabs-js/releases/tag/v2.74.0)
  - Added…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1201
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: 0bd5d4fd09d1e7a7576fb5dec3dd524e71090fe65d0185bf9a1eac4bd8dd5414
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-10-19-a35702
  comparison: ''
  confidence: low
  date: '2026-10-19'
  description: 'ElevenLabs — ElevenLabs updates — 2026-10-19: [v2.74.0](https://github.com/elevenlabs/elevenlabs-js/releases/tag/v2.74.0)
    - Added `client.conversationalAi.realtime.createClientSecret` for the Realtime
    API, with the `RealtimeModel` and OpenAI-compatible session configuration types,
    and an `environments` client with `list`, `create` and `delete`. Also adds `force`
    on agent deletion, `sourceBranchId` on branch rebase and rebase preview, `includeProcedureGeneratedWorkflowElements`
    on agent reads, `enableLogging` on Music and Sound Effects methods, WAV output
    formats for Sound Effects, service account API key `disable`, and Twilio answering
    machine detection `actions`.'
  evidence:
  - quote: '[v2.74.0](https://github.com/elevenlabs/elevenlabs-js/releases/tag/v2.74.0)
      - Added `client.conversationalAi.realtime.createClientSecret` for the Realtime
      API, with the `RealtimeModel` and OpenAI-compatible session configuration types,
      and an `environments` client with `list`, `create` and `delete`. Also adds `force`
      on agent deletion, `sourceBranchId` on branch rebase and rebase preview, `includeProcedureGeneratedWorkflowElements`
      on agent reads, `enableLogging` on Music and Sound Effects methods, WAV output
      formats for Sound Effects, service account API key `disable`, and Twilio answering
      machine detection `actions`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/19
  - quote: '[v2.73.0](https://github.com/elevenlabs/elevenlabs-js/releases/tag/v2.73.0)
      - Added `createAndWait` helpers for Flows image, video and Text to Speech generations
      and template runs (`client.flows.templates.runs.createAndWait`). They create
      the request and poll until it completes or fails, pacing requests with the server''s
      `Retry-After` header. A `failed` result is returned rather than thrown, and
      `waitTimeoutInSeconds` throws `FlowsWaitTimeoutError` if the work is not finished
      in time. The regenerated client adds the Video to music `add_sfx`, `separate_tracks`
      and `use_audio_as_reference` options.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/19
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: javascript-sdk
  source_release: elevenlabs-2026-10-19-2026-10-19-dd219c14
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: JavaScript SDK
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-10-18-2-agent-mode-changes-in-v2026-10-5|2 Agent Mode changes
  in v2026.10.5]]'
- '[[Changes/Claude Code/2026-10-19-2-agent-mode-changes-in-v2-1-304|2 Agent Mode
  changes in v2.1.304]]'
- '[[Changes/Claude Code/2026-10-19-added-claude-api-managed-agents-secure-which-compares-a-managed-agents-agent-s-s|Added
  /claude-api managed-agents-secure, which compares a Managed Agents agent''s…]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-10-19-2026-10-19-dd219c14|elevenlabs-2026-10-19-2026-10-19-dd219c14]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: JavaScript SDK
type: change
---

<!-- chronolog:begin region="header" -->
# JavaScript SDK

**ElevenLabs** · 2026-10-19 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/10/19) · from [[Releases/ElevenLabs/elevenlabs-2026-10-19-2026-10-19-dd219c14|ElevenLabs updates — 2026-10-19]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> [v2.74.0](https://github.com/elevenlabs/elevenlabs-js/releases/tag/v2.74.0) - Added `client.conversationalAi.realtime.createClientSecret` for the Realtime API, with the `RealtimeModel` and OpenAI-compatible session configuration types, and an `environments` client with `list`, `create` and `delete`. Also adds `force` on agent deletion, `sourceBranchId` on branch rebase and rebase preview, `includeProcedureGeneratedWorkflowElements` on agent reads, `enableLogging` on Music and Sound Effects methods, WAV output formats for Sound Effects, service account API key `disable`, and Twilio answering machine detection `actions`.
>
> [v2.73.0](https://github.com/elevenlabs/elevenlabs-js/releases/tag/v2.73.0) - Added `createAndWait` helpers for Flows image, video and Text to Speech generations and template runs (`client.flows.templates.runs.createAndWait`). They create the request and poll until it completes or fails, pacing requests with the server's `Retry-After` header. A `failed` result is returned rather than thrown, and `waitTimeoutInSeconds` throws `FlowsWaitTimeoutError` if the work is not finished in time. The regenerated client adds the Video to music `add_sfx`, `separate_tracks` and `use_audio_as_reference` options.
>
> Source: https://elevenlabs.io/docs/changelog/2026/10/19
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-10-19-speech-to-text|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-19-sdk-releases|SDK releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-10-19-music-and-sound-effects|Music and Sound Effects]] · Enterprise and Administration
- [[Changes/ElevenLabs/2026-10-19-eleven-realtime|Eleven Realtime]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-19-elevenagents|ElevenAgents]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-19-video-to-music|Video to Music]] · Multimodal Input
- [[Changes/ElevenLabs/2026-10-19-realtime-translation|Realtime Translation]] · Enterprise and Administration
- [[Changes/ElevenLabs/2026-10-19-elevenagents-b18b24|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-10-19-music|Music]] · Multimodal Input
- [[Changes/ElevenLabs/2026-10-19-voices|Voices]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-19-python-sdk|Python SDK]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-10-19-elevenagents-ee74ab|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-10-19-voices-f9aa8c|Voices]] · Voice and Audio
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-10-19 · Claude Code · [[Changes/Claude Code/2026-10-19-added-claude-api-managed-agents-secure-which-compares-a-managed-agents-agent-s-s|Added /claude-api managed-agents-secure, which compares a Managed Agents agent's…]]
- Later: 2026-10-19 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-10-19-2-agent-mode-changes-in-v1-0-100|2 Agent Mode changes in v1.0.100]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-10-19-a35702&body=Card%3A%20Changes%2FElevenLabs%2F2026-10-19-javascript-sdk.md%0ACard%20ID%3A%20elevenlabs-2026-10-19-a35702%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F10%2F19%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->