---
draft: true
machine_hash: 523d1cada55231f9d9a42985797ff061e7eb5ea73c857f0f1af8eeaa1c614625
product: elevenlabs
record:
  card_id: elevenlabs-2026-11-02-2eb7ff
  comparison: ''
  date: '2026-11-02'
  description: 'ElevenLabs — ElevenLabs updates — 2026-11-02: Analysis items'
  evidence:
  - quote: Analysis items
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '`GET /v1/convai/analysis-items` - List analysis items, with optional `search`,
      `kind` (`evaluation` or `data_collection`), `analysis_item_ids`, `created_by_user_id`,
      `sort_direction`, `page_size` and `cursor`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '`POST /v1/convai/analysis-items` - Create an analysis item.'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '`GET /v1/convai/analysis-items/{analysis_item_id}` - Get an analysis item.'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '`PATCH /v1/convai/analysis-items/{analysis_item_id}` - Update an analysis
      item.'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '`DELETE /v1/convai/analysis-items/{analysis_item_id}` - Delete an analysis
      item. Pass `force=true` to delete it even when agents use it, removing it from
      the dependent agents and branches.'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '`POST /v1/convai/analysis-items/{analysis_item_id}/copy` - Copy an analysis
      item.'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '`GET /v1/convai/analysis-items/{analysis_item_id}/versions` - List an
      analysis item''s versions.'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '`GET /v1/convai/analysis-items/{analysis_item_id}/dependent-agents` -
      List the agents that use an analysis item.'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '`PATCH /v1/convai/analysis-items/{analysis_item_id}/attachments` - Attach
      or detach an analysis item across agents and branches.'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: Realtime conversation groups
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '`GET /v1/convai/realtime/conversation-groups` and `POST /v1/convai/realtime/conversation-groups`
      - List and create conversation groups. Create requires `title` (string, unique
      per workspace, up to 64 characters) and accepts optional `description` (string,
      up to 500 characters).'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '`GET`, `PATCH` and `DELETE /v1/convai/realtime/conversation-groups/{conversation_group_id}`
      - Get, update and delete a conversation group.'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '`PUT /v1/convai/realtime/conversations/{conversation_id}/conversation-group`
      - Place a conversation in a group, with required `conversation_group_id`. A
      conversation belongs to at most one group.'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '`DELETE /v1/convai/realtime/conversations/{conversation_id}/conversation-group`
      - Remove a conversation from its group.'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-11-02-2026-11-02-7efe9660
  source_type: elevenlabs_changelog
  theme: __candidate__
  theme_matches: []
  theme_review_reason: no_match
  theme_suggestion: elevenagents-analysis-items
  title: ElevenAgents
  type: change
---

Pending theme review. Resolve via the theme vocabulary or review decisions.