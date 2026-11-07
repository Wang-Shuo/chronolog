---
card_id: elevenlabs-2026-01-19-97d485
date: '2026-01-19'
description: 'ElevenLabs · 2026-01-19 · Agent Mode: [Get signed URL](https://elevenlabs.io/docs/api-reference/conversations/get-signed-url),
  [Get conversation…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 928
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: launch
machine_hash: 39b17b3ad43319696d12a4b62510a7e7341c7cbae2d674a12da118fd03514dda
product: elevenlabs
product_name: ElevenLabs
record:
  card_id: elevenlabs-2026-01-19-97d485
  comparison: ''
  date: '2026-01-19'
  description: 'ElevenLabs — ElevenLabs updates — 2026-01-19: [Get signed URL](https://elevenlabs.io/docs/api-reference/conversations/get-signed-url),
    [Get conversation token](https://elevenlabs.io/docs/api-reference/conversations/get-webrtc-token),
    [Get conversations](https://elevenlabs.io/docs/api-reference/conversations/get-conversations)'
  evidence:
  - quote: '[Get signed URL](https://elevenlabs.io/docs/api-reference/conversations/get-signed-url),
      [Get conversation token](https://elevenlabs.io/docs/api-reference/conversations/get-webrtc-token),
      [Get conversations](https://elevenlabs.io/docs/api-reference/conversations/get-conversations)'
    source_release: https://elevenlabs.io/docs/changelog/2026/1/19
  - quote: Added `branch_id` (string, optional) query parameter for filtering by agent
      version branch
    source_release: https://elevenlabs.io/docs/changelog/2026/1/19
  - quote: '[Create agent](https://elevenlabs.io/docs/api-reference/agents/create),
      [Update agent](https://elevenlabs.io/docs/api-reference/agents/update), [Get
      agent](https://elevenlabs.io/docs/api-reference/agents/get)'
    source_release: https://elevenlabs.io/docs/changelog/2026/1/19
  - quote: 'Added `spelling_patience` (enum: `auto`, `low`, `medium`, `high`) to turn
      configuration'
    source_release: https://elevenlabs.io/docs/changelog/2026/1/19
  - quote: Added `whatsapp_accounts` (array) to agent response model
    source_release: https://elevenlabs.io/docs/changelog/2026/1/19
  - quote: '[Simulate conversation](https://elevenlabs.io/docs/api-reference/agents/simulate-conversation),
      [Simulate conversation stream](https://elevenlabs.io/docs/api-reference/agents/simulate-conversation-stream)'
    source_release: https://elevenlabs.io/docs/changelog/2026/1/19
  - quote: Request schema updated (breaking change)
    source_release: https://elevenlabs.io/docs/changelog/2026/1/19
  - quote: '[Get conversation](https://elevenlabs.io/docs/api-reference/conversations/get)'
    source_release: https://elevenlabs.io/docs/changelog/2026/1/19
  - quote: Removed `initiation_trigger` from metadata (breaking change)
    source_release: https://elevenlabs.io/docs/changelog/2026/1/19
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: agents-platform
  source_release: elevenlabs-2026-01-19-2026-01-19-0e264fd7
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: Agents Platform
  type: change
related_changes:
- '[[Changes/Replit/2026-01-16-redesigned-tool-calls-ui-in-agent-chat|Redesigned tool
  calls UI in Agent chat]]'
- '[[Changes/ElevenLabs/2026-01-19-agents-platform|Agents Platform]]'
- '[[Changes/ElevenLabs/2026-01-19-new-endpoints|New Endpoints]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-01-19-2026-01-19-0e264fd7|elevenlabs-2026-01-19-2026-01-19-0e264fd7]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: Agents Platform
type: change
---

<!-- chronolog:begin region="header" -->
# Agents Platform

**ElevenLabs** · 2026-01-19 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/1/19) · from [[Releases/ElevenLabs/elevenlabs-2026-01-19-2026-01-19-0e264fd7|ElevenLabs updates — 2026-01-19]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> [Get signed URL](https://elevenlabs.io/docs/api-reference/conversations/get-signed-url), [Get conversation token](https://elevenlabs.io/docs/api-reference/conversations/get-webrtc-token), [Get conversations](https://elevenlabs.io/docs/api-reference/conversations/get-conversations)
>
> Added `branch_id` (string, optional) query parameter for filtering by agent version branch
>
> [Create agent](https://elevenlabs.io/docs/api-reference/agents/create), [Update agent](https://elevenlabs.io/docs/api-reference/agents/update), [Get agent](https://elevenlabs.io/docs/api-reference/agents/get)
>
> Added `spelling_patience` (enum: `auto`, `low`, `medium`, `high`) to turn configuration
>
> Added `whatsapp_accounts` (array) to agent response model
>
> [Simulate conversation](https://elevenlabs.io/docs/api-reference/agents/simulate-conversation), [Simulate conversation stream](https://elevenlabs.io/docs/api-reference/agents/simulate-conversation-stream)
>
> Request schema updated (breaking change)
>
> [Get conversation](https://elevenlabs.io/docs/api-reference/conversations/get)
>
> Removed `initiation_trigger` from metadata (breaking change)
>
> Source: https://elevenlabs.io/docs/changelog/2026/1/19
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-01-19-modified-schemas|Modified Schemas]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-01-19-knowledge-base|Knowledge Base]] · Files and Data
- [[Changes/ElevenLabs/2026-01-19-agents-platform|Agents Platform]] · Agent Mode
- [[Changes/ElevenLabs/2026-01-19-python-sdk|Python SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-01-19-react-and-client-sdks|React and Client SDKs]] · Voice and Audio
- [[Changes/ElevenLabs/2026-01-19-new-endpoints|New Endpoints]] · Agent Mode
- [[Changes/ElevenLabs/2026-01-19-voice-management|Voice Management]] · Voice and Audio
- [[Changes/ElevenLabs/2026-01-19-audio-output-formats|Audio Output Formats]] · Voice and Audio
- [[Changes/ElevenLabs/2026-01-19-speech-to-text|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-01-19-audio-generation|Audio Generation]] · Voice and Audio
- [[Changes/ElevenLabs/2026-01-19-javascript-sdk|JavaScript SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-01-19-sdk-releases|SDK Releases]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-01-16 · Replit · [[Changes/Replit/2026-01-16-redesigned-tool-calls-ui-in-agent-chat|Redesigned tool calls UI in Agent chat]]
- Later: 2026-01-19 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-01-19-mcp-server-management-when-swapping-between-custom-agents-with-agent|MCP server management when swapping between custom agents with /agent]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-01-19-97d485&body=Card%3A%20Changes%2FElevenLabs%2F2026-01-19-agents-platform-97d485.md%0ACard%20ID%3A%20elevenlabs-2026-01-19-97d485%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F1%2F19%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->