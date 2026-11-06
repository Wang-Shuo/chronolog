---
draft: true
machine_hash: ffff335029cc60e04b85f04d907df1ac734d2212531eebc75b15db8ebe2bb0a9
product: elevenlabs
record:
  card_id: elevenlabs-2026-09-07-e4a3c3
  comparison: ''
  date: '2026-09-07'
  description: 'ElevenLabs — ElevenLabs updates — 2026-09-07: [List workspace tickets](https://elevenlabs.io/docs/api-reference/triage-tickets/list-for-workspace)
    - `GET /v1/convai/triage-tickets`'
  evidence:
  - quote: '[List workspace tickets](https://elevenlabs.io/docs/api-reference/triage-tickets/list-for-workspace)
      - `GET /v1/convai/triage-tickets`'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/7
  - quote: Lists conversation triage tickets across every agent the caller can access,
      ordered by most recently created first.
    source_release: https://elevenlabs.io/docs/changelog/2026/9/7
  - quote: Added optional `page_size` (integer, 1–100, default `100`), `status` (`AgentConversationTicketStatus`),
      `assignee_user_id` (string or `unassigned`) and `cursor` (string) query parameters.
    source_release: https://elevenlabs.io/docs/changelog/2026/9/7
  - quote: Returns `GetAgentConversationTicketsPageResponseModel`.
    source_release: https://elevenlabs.io/docs/changelog/2026/9/7
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-09-07-2026-09-07-cf030a1d
  source_type: elevenlabs_changelog
  theme: __candidate__
  theme_matches: []
  theme_review_reason: no_match
  theme_suggestion: elevenagents-list-workspace
  title: ElevenAgents
  type: change
---

Pending theme review. Resolve via the theme vocabulary or review decisions.