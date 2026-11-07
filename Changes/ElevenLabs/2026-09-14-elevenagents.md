---
card_id: elevenlabs-2026-09-14-283419
date: '2026-09-14'
description: 'ElevenLabs · 2026-09-14 · Agent Mode: [Create agent](https://elevenlabs.io/docs/api-reference/agents/create),
  [Get…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1166
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: bb67e740cdf757f9f711795d4b2df90551a601aee8dab50d07f1f10ff55f2afe
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-09-14-283419
  comparison: ''
  confidence: low
  date: '2026-09-14'
  description: 'ElevenLabs — ElevenLabs updates — 2026-09-14: [Create agent](https://elevenlabs.io/docs/api-reference/agents/create),
    [Get agent](https://elevenlabs.io/docs/api-reference/agents/get) and [Update agent](https://elevenlabs.io/docs/api-reference/agents/update)'
  evidence:
  - quote: '[Create agent](https://elevenlabs.io/docs/api-reference/agents/create),
      [Get agent](https://elevenlabs.io/docs/api-reference/agents/get) and [Update
      agent](https://elevenlabs.io/docs/api-reference/agents/update)'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/14
  - quote: Added optional `platform_settings.queueing_config` (`AgentQueueingConfig`)
      with `enabled` (boolean, default `false`) and `wait_timeout_seconds` (integer,
      1–1,800, default `180`).
    source_release: https://elevenlabs.io/docs/changelog/2026/9/14
  - quote: Queue configuration responses include read-only nullable `hold_audio` (`AgentHoldAudioConfig`).
      Agent responses also include optional `default_hold_audio_url` (string).
    source_release: https://elevenlabs.io/docs/changelog/2026/9/14
  - quote: '[Get conversation](https://elevenlabs.io/docs/api-reference/conversations/get)
      - `GET /v1/convai/conversations/{conversation_id}`'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/14
  - quote: Metadata adds optional nullable `queue_wait_secs` (number). Queue time
      is excluded from `call_duration_secs` and billed time.
    source_release: https://elevenlabs.io/docs/changelog/2026/9/14
  - quote: '[Create agent branch](https://elevenlabs.io/docs/api-reference/agents/branches/create)
      - `POST /v1/convai/agents/{agent_id}/branches`'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/14
  - quote: Added optional `include_draft` (boolean, default `false`). When `true`,
      a branch created from the branch tip includes the caller's draft procedure set.
    source_release: https://elevenlabs.io/docs/changelog/2026/9/14
  - quote: '[List procedures](https://elevenlabs.io/docs/api-reference/agents/procedures/list)
      and procedure create, get and draft endpoints'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/14
  - quote: List items add optional `referenced_tool_ids`, `referenced_kb_ids`, `referenced_procedure_ids`
      and `referenced_dynamic_variables` (string arrays).
    source_release: https://elevenlabs.io/docs/changelog/2026/9/14
  - quote: Agent and merge-preview responses add optional `procedures`, a map keyed
      by procedure ID.
    source_release: https://elevenlabs.io/docs/changelog/2026/9/14
  - quote: '[List test invocations](https://elevenlabs.io/docs/api-reference/tests/test-invocations/list)
      - `GET /v1/convai/test-invocations`'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/14
  - quote: Added optional nullable `search` (string) to filter tests and folders by
      name.
    source_release: https://elevenlabs.io/docs/changelog/2026/9/14
  - quote: '[Run tests on agent](https://elevenlabs.io/docs/api-reference/tests/run-tests)
      and [Get test invocation](https://elevenlabs.io/docs/api-reference/tests/test-invocations/get)'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/14
  - quote: Test suite invocation and unit test run responses add optional nullable
      `version_id` (string) and optional `ran_against_draft` (boolean, default `false`).
    source_release: https://elevenlabs.io/docs/changelog/2026/9/14
  - quote: Invocation summaries also add optional `runs_diverged_from_version` (boolean,
      default `false`).
    source_release: https://elevenlabs.io/docs/changelog/2026/9/14
  - quote: '`POST /v1/convai/agents/{agent_id}/knowledge-base/rag-query`'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/14
  - quote: The request body adds optional nullable `max_documents_length` (integer,
      1–50,000) and `max_retrieved_rag_chunks_count` (integer, 1–20) query-specific
      overrides.
    source_release: https://elevenlabs.io/docs/changelog/2026/9/14
  - quote: '[Get WhatsApp account](https://elevenlabs.io/docs/api-reference/whats-app/accounts/get)
      - `GET /v1/convai/whatsapp-accounts/{phone_number_id}`'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/14
  - quote: Added optional `account_type` (`WhatsAppAccountType`, default `cloud_api`).
      Values are `cloud_api` and `coexistence`.
    source_release: https://elevenlabs.io/docs/changelog/2026/9/14
  - quote: '[Calculate expected LLM usage](https://elevenlabs.io/docs/api-reference/agents/calculate)
      - `POST /v1/convai/agent/{agent_id}/llm-usage/calculate`'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/14
  - quote: '`LLMUsageCalculatorLLMResponseModel` adds required `price_per_message`
      (number).'
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
  title: ElevenAgents
  type: change
related_changes:
- '[[Changes/Raycast/2026-09-11-ai-added-auto-review-rules-for-greater-control-over-how-auto-mode-behaves|AI
  : Added Auto-review rules for greater control over how Auto mode behaves]]'
- '[[Changes/Raycast/2026-09-11-2-agent-mode-changes-in-raycast-macos-2-3|2 Agent
  Mode changes in Raycast macos 2.3]]'
- '[[Changes/Claude Code/2026-09-14-7-agent-mode-changes-in-v2-1-271|7 Agent Mode
  changes in v2.1.271]]'
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
> [Create agent](https://elevenlabs.io/docs/api-reference/agents/create), [Get agent](https://elevenlabs.io/docs/api-reference/agents/get) and [Update agent](https://elevenlabs.io/docs/api-reference/agents/update)
>
> Added optional `platform_settings.queueing_config` (`AgentQueueingConfig`) with `enabled` (boolean, default `false`) and `wait_timeout_seconds` (integer, 1–1,800, default `180`).
>
> Queue configuration responses include read-only nullable `hold_audio` (`AgentHoldAudioConfig`). Agent responses also include optional `default_hold_audio_url` (string).
>
> [Get conversation](https://elevenlabs.io/docs/api-reference/conversations/get) - `GET /v1/convai/conversations/{conversation_id}`
>
> Metadata adds optional nullable `queue_wait_secs` (number). Queue time is excluded from `call_duration_secs` and billed time.
>
> [Create agent branch](https://elevenlabs.io/docs/api-reference/agents/branches/create) - `POST /v1/convai/agents/{agent_id}/branches`
>
> Added optional `include_draft` (boolean, default `false`). When `true`, a branch created from the branch tip includes the caller's draft procedure set.
>
> [List procedures](https://elevenlabs.io/docs/api-reference/agents/procedures/list) and procedure create, get and draft endpoints
>
> List items add optional `referenced_tool_ids`, `referenced_kb_ids`, `referenced_procedure_ids` and `referenced_dynamic_variables` (string arrays).
>
> Agent and merge-preview responses add optional `procedures`, a map keyed by procedure ID.
>
> [List test invocations](https://elevenlabs.io/docs/api-reference/tests/test-invocations/list) - `GET /v1/convai/test-invocations`
>
> Added optional nullable `search` (string) to filter tests and folders by name.
>
> [Run tests on agent](https://elevenlabs.io/docs/api-reference/tests/run-tests) and [Get test invocation](https://elevenlabs.io/docs/api-reference/tests/test-invocations/get)
>
> Test suite invocation and unit test run responses add optional nullable `version_id` (string) and optional `ran_against_draft` (boolean, default `false`).
>
> Invocation summaries also add optional `runs_diverged_from_version` (boolean, default `false`).
>
> `POST /v1/convai/agents/{agent_id}/knowledge-base/rag-query`
>
> The request body adds optional nullable `max_documents_length` (integer, 1–50,000) and `max_retrieved_rag_chunks_count` (integer, 1–20) query-specific overrides.
>
> [Get WhatsApp account](https://elevenlabs.io/docs/api-reference/whats-app/accounts/get) - `GET /v1/convai/whatsapp-accounts/{phone_number_id}`
>
> Added optional `account_type` (`WhatsAppAccountType`, default `cloud_api`). Values are `cloud_api` and `coexistence`.
>
> [Calculate expected LLM usage](https://elevenlabs.io/docs/api-reference/agents/calculate) - `POST /v1/convai/agent/{agent_id}/llm-usage/calculate`
>
> `LLMUsageCalculatorLLMResponseModel` adds required `price_per_message` (number).
>
> Source: https://elevenlabs.io/docs/changelog/2026/9/14
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-09-14-sdk-releases|SDK releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-09-14-packages|Packages]] · Voice and Audio
- [[Changes/ElevenLabs/2026-09-14-ios-sdk|iOS SDK]] · Mobile and Desktop
- [[Changes/ElevenLabs/2026-09-14-javascript-sdk|JavaScript SDK]] · Model Support
- [[Changes/ElevenLabs/2026-09-14-python-sdk|Python SDK]] · Model Support
- [[Changes/ElevenLabs/2026-09-14-elevenagents-bdb11f|ElevenAgents]] · Voice and Audio
- [[Changes/ElevenLabs/2026-09-14-music|Music]] · Multimodal Input
- [[Changes/ElevenLabs/2026-09-14-elevenagents-d9e798|ElevenAgents]] · Agent Mode
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
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-09-14-283419&body=Card%3A%20Changes%2FElevenLabs%2F2026-09-14-elevenagents.md%0ACard%20ID%3A%20elevenlabs-2026-09-14-283419%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F9%2F14%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->