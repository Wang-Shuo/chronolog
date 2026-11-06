---
draft: true
machine_hash: 418bd87deb58cc5be690a0396d9b2892c47b1a2383e5c2955cd9089d01b2c74d
product: elevenlabs
record:
  card_id: elevenlabs-2026-08-24-cc2b45
  comparison: ''
  date: '2026-08-24'
  description: 'ElevenLabs — ElevenLabs updates — 2026-08-24: Added nine conversation
    triage ticket endpoints:'
  evidence:
  - quote: 'Added nine conversation triage ticket endpoints:'
    source_release: https://elevenlabs.io/docs/changelog/2026/8/24
  - quote: '[Create conversation ticket](https://elevenlabs.io/docs/api-reference/triage-tickets/create-agent-conversation-ticket-route)
      - `POST /v1/convai/triage-tickets`. The request requires `conversation_id` (string)
      and accepts `qa_comment` (nullable string, 1–10,000 characters) and up to 200
      turn comments.'
    source_release: https://elevenlabs.io/docs/changelog/2026/8/24
  - quote: '[List tickets](https://elevenlabs.io/docs/api-reference/triage-tickets/list-agent-conversation-tickets-route)
      - `GET /v1/convai/agents/{agent_id}/triage-tickets`, with cursor pagination.'
    source_release: https://elevenlabs.io/docs/changelog/2026/8/24
  - quote: '[Create manual ticket](https://elevenlabs.io/docs/api-reference/triage-tickets/create-manual-agent-ticket-route)
      - `POST /v1/convai/agents/{agent_id}/triage-tickets`. The request requires `qa_comment`
      (string, 1–10,000 characters).'
    source_release: https://elevenlabs.io/docs/changelog/2026/8/24
  - quote: '[List assignable users](https://elevenlabs.io/docs/api-reference/triage-tickets/get-assignable-users-route)
      - `GET /v1/convai/agents/{agent_id}/triage-tickets/assignable-users`. The response
      lists non-service-account workspace members and whether each member has access
      to the agent.'
    source_release: https://elevenlabs.io/docs/changelog/2026/8/24
  - quote: '[Get ticket](https://elevenlabs.io/docs/api-reference/triage-tickets/get-agent-conversation-ticket-route)
      - `GET /v1/convai/triage-tickets/{agentqa_ticket_id}`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/8/24
  - quote: '[Update ticket](https://elevenlabs.io/docs/api-reference/triage-tickets/update-agent-conversation-ticket-route)
      - `PATCH /v1/convai/triage-tickets/{agentqa_ticket_id}`. The request accepts
      optional `status` and nullable `assignee_user_id`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/8/24
  - quote: '[Delete ticket](https://elevenlabs.io/docs/api-reference/triage-tickets/delete-agent-conversation-ticket-route)
      - `DELETE /v1/convai/triage-tickets/{agentqa_ticket_id}`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/8/24
  - quote: '[Add comment](https://elevenlabs.io/docs/api-reference/triage-tickets/add-ticket-comment-route)
      - `POST /v1/convai/triage-tickets/{agentqa_ticket_id}/comments`. The request
      requires `comment` (string, 1–10,000 characters).'
    source_release: https://elevenlabs.io/docs/changelog/2026/8/24
  - quote: '[Add turn comment](https://elevenlabs.io/docs/api-reference/triage-tickets/add-turn-comment-route)
      - `POST /v1/convai/triage-tickets/{agentqa_ticket_id}/turn-comments`. The request
      requires zero-based `turn_index` (integer) and `comment` (string, 1–10,000 characters).'
    source_release: https://elevenlabs.io/docs/changelog/2026/8/24
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-08-24-2026-08-24-b7c01132
  source_type: elevenlabs_changelog
  theme: __candidate__
  theme_matches: []
  theme_review_reason: no_match
  theme_suggestion: elevenagents-added-nine
  title: ElevenAgents
  type: change
---

Pending theme review. Resolve via the theme vocabulary or review decisions.