---
draft: true
machine_hash: ad005434c66e803ca8bf0ce4d7446df38525d398271523c77564219b3125a129
product: elevenlabs
record:
  card_id: elevenlabs-2026-05-04-3c2fe9
  comparison: ''
  date: '2026-05-04'
  description: 'ElevenLabs — ElevenLabs updates — 2026-05-04: **Conversation tags**:
    Added first-class conversation tags for organizing and filtering conversations.
    You can now create, update, list and delete tags, assign tags to conversations,
    and filter [conversation history](https://elevenlabs.io/docs/api-reference/conversations/list)
    by `tag_ids`.'
  evidence:
  - quote: '**Conversation tags**: Added first-class conversation tags for organizing
      and filtering conversations. You can now create, update, list and delete tags,
      assign tags to conversations, and filter [conversation history](https://elevenlabs.io/docs/api-reference/conversations/list)
      by `tag_ids`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/5/4
  - quote: '**Conversation list filters**: Added `exclude_statuses` to [list conversations](https://elevenlabs.io/docs/api-reference/conversations/list),
      allowing clients to hide conversations with statuses such as `initiated`, `in-progress`,
      `processing`, `done`, or `failed`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/5/4
  - quote: '**Model options**: Added `claude-opus-4-7`, `gpt-5.4`, `gpt-5.5`, `gpt-5.4-2026-03-05`,
      `gpt-5.5-2026-04-23`, and `qwen36-35b-a3b` to the `LLM` enum.'
    source_release: https://elevenlabs.io/docs/changelog/2026/5/4
  - quote: '**Contextual update metadata**: Added `contextual_update_info` to conversation
      transcript response items. The field references `ContextualUpdateInfo`, which
      includes `context_id` and `is_superseded`, so clients can identify contextual
      updates and whether they have been replaced by later context.'
    source_release: https://elevenlabs.io/docs/changelog/2026/5/4
  - quote: '**Batch calling filter**: Added an optional `agent_id` query parameter
      to [list workspace batch calling jobs](https://elevenlabs.io/docs/api-reference/batch-calling/list),
      allowing clients to return jobs for a single agent.'
    source_release: https://elevenlabs.io/docs/changelog/2026/5/4
  - quote: '**Test invocation listing**: Made the `agent_id` query parameter optional
      and nullable on [list test invocations](https://elevenlabs.io/docs/api-reference/tests/test-invocations/list),
      allowing clients to list test invocations without filtering by one agent.'
    source_release: https://elevenlabs.io/docs/changelog/2026/5/4
  - quote: '**MCP response timeout**: Increased the maximum `response_timeout_secs`
      value from `120` to `300` seconds on MCP server configuration and MCP tool configuration
      overrides.'
    source_release: https://elevenlabs.io/docs/changelog/2026/5/4
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-05-04-2026-05-04-9c04c503
  source_type: elevenlabs_changelog
  theme: __candidate__
  theme_matches: []
  theme_review_reason: no_match
  theme_suggestion: elevenagents-conversation-tags
  title: ElevenAgents
  type: change
---

Pending theme review. Resolve via the theme vocabulary or review decisions.