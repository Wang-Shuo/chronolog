---
draft: true
machine_hash: 1aae3157eddfdef77b1e10ccb4e96251756daec084a27f6835aa2310b9fe29c0
product: elevenlabs
record:
  card_id: elevenlabs-2026-08-10-cbd5b2
  comparison: ''
  date: '2026-08-10'
  description: 'ElevenLabs — ElevenLabs updates — 2026-08-10: **Conversation guardrail
    filters**: [List conversations](https://elevenlabs.io/docs/api-reference/conversations/list)
    adds optional `guardrail_types` (`GuardrailType[]`) and `custom_guardrail_names`
    (string array) query parameters. The existing conversation hierarchy can now be
    filtered with optional `parent_conversation_id` (string).'
  evidence:
  - quote: '**Conversation guardrail filters**: [List conversations](https://elevenlabs.io/docs/api-reference/conversations/list)
      adds optional `guardrail_types` (`GuardrailType[]`) and `custom_guardrail_names`
      (string array) query parameters. The existing conversation hierarchy can now
      be filtered with optional `parent_conversation_id` (string).'
    source_release: https://elevenlabs.io/docs/changelog/2026/8/10
  - quote: '**Branch divergence status**: [List agent branches](https://elevenlabs.io/docs/api-reference/agents/branches/list)
      adds optional `include_commit_status` (boolean, default `false`). When enabled,
      branch summaries include nullable `commits_ahead`, `commits_behind` and `merged_into_branch_id`
      fields.'
    source_release: https://elevenlabs.io/docs/changelog/2026/8/10
  - quote: '**Conversation and tool controls**: Client overrides now support `max_duration_seconds`
      and `pronunciation_dictionary_locators`. MCP server configuration adds `request_meta`
      for passing MCP `_meta` values to tool calls, and webhook tool timeouts now
      support up to 300 seconds.'
    source_release: https://elevenlabs.io/docs/changelog/2026/8/10
  - quote: '**Post-call analysis usage**: Conversation charging adds an `analysis`
      breakdown with per-feature running totals and run snapshots. Transcript messages
      add `triggered_guardrails`, and conversation turns add optional `producing_llm`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/8/10
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-08-10-2026-08-10-3c63678b
  source_type: elevenlabs_changelog
  theme: __candidate__
  theme_matches: []
  theme_review_reason: no_match
  theme_suggestion: elevenagents-conversation-guardrail
  title: ElevenAgents
  type: change
---

Pending theme review. Resolve via the theme vocabulary or review decisions.