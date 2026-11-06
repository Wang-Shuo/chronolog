---
draft: true
machine_hash: 8570d169446d1a2a391ea3cbf66a34ad6f1fa3fc8fdfbf46c8b0e503eed18260
product: elevenlabs
record:
  card_id: elevenlabs-2026-06-15-eed151
  comparison: ''
  date: '2026-06-15'
  description: 'ElevenLabs — ElevenLabs updates — 2026-06-15: **Run conversation evaluation**:
    Added [Run conversation evaluation](https://elevenlabs.io/docs/api-reference/conversations/analysis/run-evaluation)
    endpoint (`POST /v1/convai/conversations/{conversation_id}/analysis/evaluations/run`)
    to rerun a single evaluation criterion against a completed conversation using
    `RunConversationEvaluationsRequest`.'
  evidence:
  - quote: '**Run conversation evaluation**: Added [Run conversation evaluation](https://elevenlabs.io/docs/api-reference/conversations/analysis/run-evaluation)
      endpoint (`POST /v1/convai/conversations/{conversation_id}/analysis/evaluations/run`)
      to rerun a single evaluation criterion against a completed conversation using
      `RunConversationEvaluationsRequest`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/15
  - quote: '**Workflow entry behavior**: Workflow override-agent nodes add optional
      `entry_behavior` (`generate_immediately`, `wait_for_user`, `auto`) to control
      whether the sub-agent speaks first or waits for user input.'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/15
  - quote: '**End procedure system tool**: Added `end_procedure` system tool configuration
      with matching error statuses. The `start_procedure` tool adds `already_active`
      to its error statuses.'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/15
  - quote: '**Transfer TTS overrides**: `AgentTransfer`, workflow standalone agent
      nodes and successful `transfer_to_agent` tool results add optional `preserve_client_tts_overrides`
      (boolean) to keep client-side TTS overrides after a transfer.'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/15
  - quote: '**Interaction budget enum**: `InteractionBudget` removes `async` and adds
      `5_minutes`, `10_minutes` and `1_hour`. Update any configs or SDK enums that
      still reference `async`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/15
  - quote: '**Custom guardrail model selection**: Custom guardrail configuration adds
      optional `model` with Gemini, Claude and GPT variants. Guardrail config also
      adds optional `history_message_count` (integer).'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/15
  - quote: '**Phone number list filters**: [List phone numbers](https://elevenlabs.io/docs/api-reference/phone-numbers/list)
      adds optional `provider`, `agent_id` and `branch_id` query parameters to filter
      imported numbers.'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/15
  - quote: '**WhatsApp account filtering**: [List WhatsApp accounts](https://elevenlabs.io/docs/api-reference/whats-app/accounts/list)
      adds optional `agent_id` query parameter to filter accounts by assigned agent.'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/15
  - quote: '**Topic time range filters**: [Get agent conversation topics](https://elevenlabs.io/docs/api-reference/conversations/topics/get)
      adds optional `from_unix_secs` and `to_unix_secs` query parameters to bound
      topic discovery results.'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/15
  - quote: '**SIP codec configuration**: Outbound SIP trunk request and response models
      add optional `enabled_codecs` (`MediaCodec` enum).'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/15
  - quote: '**Memory tool types**: Added `LoadableMemoryEntry` and `LoadMemoryEntryToolErrorStatus`
      schemas for memory-tool error handling.'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/15
  - quote: '**Agent test batch limits**: Agent test attach, run and resubmit request
      schemas raise maximum attached tests from 1000 to 5000.'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/15
  - quote: '**Phoneme tag support**: Agent TTS settings add optional `enable_phoneme_tags`
      (boolean) for opt-in V3 SSML phoneme handling.'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/15
  - quote: '**Array schema omit overrides**: Array JSON schema properties add optional
      `is_omitted` (mutually exclusive with other value sources). `ConstantSchemaOverride`
      can use array constant values.'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/15
  - quote: '**Transfer error context**: Transfer-to-number error payloads can include
      optional `agent_message` (string).'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/15
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-06-15-2026-06-15-9835dce0
  source_type: elevenlabs_changelog
  theme: __candidate__
  theme_matches: []
  theme_review_reason: no_match
  theme_suggestion: elevenagents-run-conversation
  title: ElevenAgents
  type: change
---

Pending theme review. Resolve via the theme vocabulary or review decisions.