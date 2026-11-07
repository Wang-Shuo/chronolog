---
card_id: elevenlabs-2026-07-20-78d341
date: '2026-07-20'
description: 'ElevenLabs · 2026-07-20 · Agent Mode: **Resolve external conversation
  references**: Added `GET /v1/convai/conversations/resolve` to resolve a Slack message
  URL…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1110
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: a011e43d3b8e0d90cb84a4bad2f0f171b6e8a006e49dcb3ec6e044e3418ff0df
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-07-20-78d341
  comparison: ''
  confidence: low
  date: '2026-07-20'
  description: 'ElevenLabs — ElevenLabs updates — 2026-07-20: **Resolve external conversation
    references**: Added `GET /v1/convai/conversations/resolve` to resolve a Slack
    message URL or Zendesk ticket URL to a conversation. Requests require `agent_id`
    and `reference` query parameters (strings).'
  evidence:
  - quote: '**Resolve external conversation references**: Added `GET /v1/convai/conversations/resolve`
      to resolve a Slack message URL or Zendesk ticket URL to a conversation. Requests
      require `agent_id` and `reference` query parameters (strings).'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/20
  - quote: '**Query agent knowledge bases**: Added `POST /v1/convai/agents/{agent_id}/knowledge-base/rag-query`
      for read-only RAG queries against an agent''s knowledge base. The request requires
      `query` (string), accepts optional `branch_id` (string), and returns ranked
      chunks with document, chunk, text and vector-distance metadata. This endpoint
      is excluded from generated SDKs.'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/20
  - quote: '**Knowledge base content formats**: Knowledge base file, text and URL
      responses add optional `content_format` (`html` | `markdown`, default `html`).'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/20
  - quote: '**Agent voice configuration**: TTS override schemas add optional client-overridable
      `model_id` (`TTSConversationalModel`). The default for `enable_phoneme_tags`
      changes from `false` to `true`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/20
  - quote: '**Faster backup LLM cascade**: The default `cascade_timeout_seconds` changes
      from 8 to 4 seconds. The allowed range remains 2–15 seconds.'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/20
  - quote: '**Tool parameter value sources**: Object tool parameters can now use `dynamic_variable`,
      `constant_value` or `is_omitted`, matching existing scalar and array controls.
      Constant schema overrides now accept arbitrary arrays and objects.'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/20
  - quote: '**Full-response guardrails**: Custom guardrails add optional `evaluate_full_response_only`
      (boolean, default `false`) to evaluate the complete non-TTS response once. This
      option requires blocking mode.'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/20
  - quote: '**Twilio call recording**: Telephony call configuration adds optional
      `twilio_call_recording_enabled` (boolean, default `false`). Recordings are stored
      in the connected Twilio account and the setting is ignored by other providers.'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/20
  - quote: '**Widget file-upload text**: Widget text configuration adds optional labels
      and error messages for attaching and removing files, upload failures, unsupported
      types, oversized files, file-count limits and the typing indicator.'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/20
  - quote: '**Knowledge base sync status**: Knowledge base file responses add optional
      `auto_sync_info` and `refresh_status` (`FileRefreshStatus`). Folder responses
      add required `document_count` (integer), a recursive count of non-folder documents
      capped at 1000.'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/20
  - quote: '**Conversation text search filters**: [Text search conversation messages](https://elevenlabs.io/docs/api-reference/conversations/messages/text-search)
      adds optional `exclude_statuses` and `termination_reasons` array query parameters.'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/20
  - quote: '**LLM options**: Agent LLM configuration adds `gpt-5.6-sol`, `gpt-5.6-terra`
      and `gpt-5.6-luna`. `LLMReasoningEffort` adds `max`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/20
  - quote: '**WhatsApp typing indicators**: WhatsApp account request and response
      schemas add optional `enable_typing_indicator` (boolean).'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/20
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-07-20-2026-07-20-b16c37ed
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: ElevenAgents
  type: change
related_changes:
- '[[Changes/Dify/2026-07-17-64-agent-mode-changes-in-1-16-0|64 Agent Mode changes
  in 1.16.0]]'
- '[[Changes/Claude Code/2026-07-18-added-reasoning-effort-to-the-subagentstatusline-payload-so-custom-agent-rows-ca|Added
  reasoning effort to the subagentStatusLine payload, so custom agent rows can…]]'
- '[[Changes/ElevenLabs/2026-07-20-cli|CLI]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-07-20-2026-07-20-b16c37ed|elevenlabs-2026-07-20-2026-07-20-b16c37ed]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: ElevenAgents
type: change
---

<!-- chronolog:begin region="header" -->
# ElevenAgents

**ElevenLabs** · 2026-07-20 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/7/20) · from [[Releases/ElevenLabs/elevenlabs-2026-07-20-2026-07-20-b16c37ed|ElevenLabs updates — 2026-07-20]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **Resolve external conversation references**: Added `GET /v1/convai/conversations/resolve` to resolve a Slack message URL or Zendesk ticket URL to a conversation. Requests require `agent_id` and `reference` query parameters (strings).
>
> **Query agent knowledge bases**: Added `POST /v1/convai/agents/{agent_id}/knowledge-base/rag-query` for read-only RAG queries against an agent's knowledge base. The request requires `query` (string), accepts optional `branch_id` (string), and returns ranked chunks with document, chunk, text and vector-distance metadata. This endpoint is excluded from generated SDKs.
>
> **Knowledge base content formats**: Knowledge base file, text and URL responses add optional `content_format` (`html` | `markdown`, default `html`).
>
> **Agent voice configuration**: TTS override schemas add optional client-overridable `model_id` (`TTSConversationalModel`). The default for `enable_phoneme_tags` changes from `false` to `true`.
>
> **Faster backup LLM cascade**: The default `cascade_timeout_seconds` changes from 8 to 4 seconds. The allowed range remains 2–15 seconds.
>
> **Tool parameter value sources**: Object tool parameters can now use `dynamic_variable`, `constant_value` or `is_omitted`, matching existing scalar and array controls. Constant schema overrides now accept arbitrary arrays and objects.
>
> **Full-response guardrails**: Custom guardrails add optional `evaluate_full_response_only` (boolean, default `false`) to evaluate the complete non-TTS response once. This option requires blocking mode.
>
> **Twilio call recording**: Telephony call configuration adds optional `twilio_call_recording_enabled` (boolean, default `false`). Recordings are stored in the connected Twilio account and the setting is ignored by other providers.
>
> **Widget file-upload text**: Widget text configuration adds optional labels and error messages for attaching and removing files, upload failures, unsupported types, oversized files, file-count limits and the typing indicator.
>
> **Knowledge base sync status**: Knowledge base file responses add optional `auto_sync_info` and `refresh_status` (`FileRefreshStatus`). Folder responses add required `document_count` (integer), a recursive count of non-folder documents capped at 1000.
>
> **Conversation text search filters**: [Text search conversation messages](https://elevenlabs.io/docs/api-reference/conversations/messages/text-search) adds optional `exclude_statuses` and `termination_reasons` array query parameters.
>
> **LLM options**: Agent LLM configuration adds `gpt-5.6-sol`, `gpt-5.6-terra` and `gpt-5.6-luna`. `LLMReasoningEffort` adds `max`.
>
> **WhatsApp typing indicators**: WhatsApp account request and response schemas add optional `enable_typing_indicator` (boolean).
>
> Source: https://elevenlabs.io/docs/changelog/2026/7/20
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-07-20-android-sdk|Android SDK]] · Mobile and Desktop
- [[Changes/ElevenLabs/2026-07-20-speech-to-text|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-07-20-speech-to-text-2aefae|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-07-20-music|Music]] · Voice and Audio
- [[Changes/ElevenLabs/2026-07-20-python-sdk|Python SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-07-20-cli|CLI]] · Agent Mode
- [[Changes/ElevenLabs/2026-07-20-workspaces|Workspaces]] · Voice and Audio
- [[Changes/ElevenLabs/2026-07-20-packages|Packages]] · Voice and Audio
- [[Changes/ElevenLabs/2026-07-20-javascript-sdk|JavaScript SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-07-20-sdk-releases|SDK Releases]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-07-18 · Claude Code · [[Changes/Claude Code/2026-07-18-added-reasoning-effort-to-the-subagentstatusline-payload-so-custom-agent-rows-ca|Added reasoning effort to the subagentStatusLine payload, so custom agent rows can…]]
- Later: 2026-07-20 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-07-20-3-agent-mode-changes-in-v1-0-72|3 Agent Mode changes in v1.0.72]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-07-20-78d341&body=Card%3A%20Changes%2FElevenLabs%2F2026-07-20-elevenagents.md%0ACard%20ID%3A%20elevenlabs-2026-07-20-78d341%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F7%2F20%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->