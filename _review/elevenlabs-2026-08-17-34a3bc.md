---
draft: true
machine_hash: 67de8380c024d4b3defb0b23e9c857a2aad83bfbc8d50ed77382b0b415e89007
product: elevenlabs
record:
  card_id: elevenlabs-2026-08-17-34a3bc
  comparison: ''
  date: '2026-08-17'
  description: 'ElevenLabs — ElevenLabs updates — 2026-08-17: [Get conversation summary](https://elevenlabs.io/docs/api-reference/conversations/get-summary)
    - `GET /v1/convai/conversations/{conversation_id}/summary`'
  evidence:
  - quote: '[Get conversation summary](https://elevenlabs.io/docs/api-reference/conversations/get-summary)
      - `GET /v1/convai/conversations/{conversation_id}/summary`'
    source_release: https://elevenlabs.io/docs/changelog/2026/8/17
  - quote: Accepts optional `max_messages` (integer, 1–200, default `40`)
    source_release: https://elevenlabs.io/docs/changelog/2026/8/17
  - quote: Returns `GetConversationSummaryResponseModel` with required `conversation_id`,
      `agent_id`, `status`, `message_count` and `note`
    source_release: https://elevenlabs.io/docs/changelog/2026/8/17
  - quote: 'Plain `messages` contain only `role` (`user` or `agent`) and `message`;
      conversations over the limit return `messages_omitted: true`'
    source_release: https://elevenlabs.io/docs/changelog/2026/8/17
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-08-17-2026-08-17-6196d42b
  source_type: elevenlabs_changelog
  theme: __candidate__
  theme_matches: []
  theme_review_reason: no_match
  theme_suggestion: elevenagents-get-conversation
  title: ElevenAgents
  type: change
---

Pending theme review. Resolve via the theme vocabulary or review decisions.