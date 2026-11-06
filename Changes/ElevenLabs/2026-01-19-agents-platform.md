---
card_id: elevenlabs-2026-01-19-213578
date: '2026-01-19'
description: 'ElevenLabs · 2026-01-19 · Agent Mode: **Agent summaries endpoint**:
  Added `GET /v1/convai/agents/summaries` endpoint for retrieving lightweight summaries
  of…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 928
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: f3d72a80dced1a8a82488508b0966df29f6361bb8acbe90a2989a8f91c009501
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-01-19-213578
  comparison: ''
  confidence: low
  date: '2026-01-19'
  description: 'ElevenLabs — ElevenLabs updates — 2026-01-19: **Agent summaries endpoint**:
    Added `GET /v1/convai/agents/summaries` endpoint for retrieving lightweight summaries
    of all agents in your workspace. This is useful for building agent selection interfaces
    without fetching full agent configurations.'
  evidence:
  - quote: '**Agent summaries endpoint**: Added `GET /v1/convai/agents/summaries`
      endpoint for retrieving lightweight summaries of all agents in your workspace.
      This is useful for building agent selection interfaces without fetching full
      agent configurations.'
    source_release: https://elevenlabs.io/docs/changelog/2026/1/19
  - quote: '**Delete batch calls**: Added `DELETE /v1/convai/batch-calling/{batch_id}`
      endpoint for removing batch call jobs that are no longer needed.'
    source_release: https://elevenlabs.io/docs/changelog/2026/1/19
  - quote: '**Branch filtering for conversations**: Added optional `branch_id` query
      parameter to conversation endpoints including `GET /v1/convai/conversation/get-signed-url`,
      `GET /v1/convai/conversation/token`, and `GET /v1/convai/conversations` for
      filtering conversations by agent version branch.'
    source_release: https://elevenlabs.io/docs/changelog/2026/1/19
  - quote: '**Spelling patience configuration**: Added `spelling_patience` setting
      to turn configuration with values `auto`, `low`, `medium`, and `high`. Controls
      how long the agent waits before assuming the user has finished spelling something
      out character by character.'
    source_release: https://elevenlabs.io/docs/changelog/2026/1/19
  - quote: '**Custom SIP headers for transfers**: Added support for custom SIP headers
      when transferring calls via REFER. Configure `custom_sip_headers` arrays on
      phone number transfer configurations and workflow phone nodes for advanced telephony
      integrations.'
    source_release: https://elevenlabs.io/docs/changelog/2026/1/19
  - quote: '**WhatsApp accounts on agents**: Agent responses now include `whatsapp_accounts`
      array for viewing connected WhatsApp Business accounts.'
    source_release: https://elevenlabs.io/docs/changelog/2026/1/19
  - quote: '**Zendesk integration support**: Added `zendesk_integration` to the `ConversationInitiationSource`
      enum for conversations initiated through Zendesk.'
    source_release: https://elevenlabs.io/docs/changelog/2026/1/19
  extractor_version: fallback-v5
  impact: paradigm-shift
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
- '[[Changes/Lovable/2026-01-16-smarter-agent-capabilities|Smarter agent capabilities]]'
- '[[Changes/Lovable/2026-01-16-vitest-is-now-included-in-the-react-template-enabling-the-agent-to-write-and-run|Vitest
  is now included in the React template, enabling the agent to write…]]'
- '[[Changes/Replit/2026-01-16-redesigned-tool-calls-ui-in-agent-chat|Redesigned tool
  calls UI in Agent chat]]'
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
> **Agent summaries endpoint**: Added `GET /v1/convai/agents/summaries` endpoint for retrieving lightweight summaries of all agents in your workspace. This is useful for building agent selection interfaces without fetching full agent configurations.
>
> **Delete batch calls**: Added `DELETE /v1/convai/batch-calling/{batch_id}` endpoint for removing batch call jobs that are no longer needed.
>
> **Branch filtering for conversations**: Added optional `branch_id` query parameter to conversation endpoints including `GET /v1/convai/conversation/get-signed-url`, `GET /v1/convai/conversation/token`, and `GET /v1/convai/conversations` for filtering conversations by agent version branch.
>
> **Spelling patience configuration**: Added `spelling_patience` setting to turn configuration with values `auto`, `low`, `medium`, and `high`. Controls how long the agent waits before assuming the user has finished spelling something out character by character.
>
> **Custom SIP headers for transfers**: Added support for custom SIP headers when transferring calls via REFER. Configure `custom_sip_headers` arrays on phone number transfer configurations and workflow phone nodes for advanced telephony integrations.
>
> **WhatsApp accounts on agents**: Agent responses now include `whatsapp_accounts` array for viewing connected WhatsApp Business accounts.
>
> **Zendesk integration support**: Added `zendesk_integration` to the `ConversationInitiationSource` enum for conversations initiated through Zendesk.
>
> Source: https://elevenlabs.io/docs/changelog/2026/1/19
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-01-19-modified-schemas|Modified Schemas]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-01-19-knowledge-base|Knowledge Base]] · Files and Data
- [[Changes/ElevenLabs/2026-01-19-python-sdk|Python SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-01-19-react-and-client-sdks|React and Client SDKs]] · Voice and Audio
- [[Changes/ElevenLabs/2026-01-19-new-endpoints|New Endpoints]] · Agent Mode
- [[Changes/ElevenLabs/2026-01-19-voice-management|Voice Management]] · Voice and Audio
- [[Changes/ElevenLabs/2026-01-19-agents-platform-97d485|Agents Platform]] · Agent Mode
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
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-01-19-213578&body=Card%3A%20Changes%2FElevenLabs%2F2026-01-19-agents-platform.md%0ACard%20ID%3A%20elevenlabs-2026-01-19-213578%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F1%2F19%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->