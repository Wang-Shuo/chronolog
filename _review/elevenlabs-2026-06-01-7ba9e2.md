---
draft: true
machine_hash: 4688f0b6c074ff50849829dadd5b9bf6e5cf5f085db08f9834b1a11c6c097588
product: elevenlabs
record:
  card_id: elevenlabs-2026-06-01-7ba9e2
  comparison: ''
  date: '2026-06-01'
  description: 'ElevenLabs — ElevenLabs updates — 2026-06-01: [List conversations](https://elevenlabs.io/docs/api-reference/conversations/list)
    - `GET /v1/convai/conversations`'
  evidence:
  - quote: '[List conversations](https://elevenlabs.io/docs/api-reference/conversations/list)
      - `GET /v1/convai/conversations`'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/1
  - quote: Added optional `workflow_node_entered_id` query parameter (string)
    source_release: https://elevenlabs.io/docs/changelog/2026/6/1
  - quote: '[Text search conversation messages](https://elevenlabs.io/docs/api-reference/conversations/messages/text-search)
      - `GET /v1/convai/conversations/messages/text-search`'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/1
  - quote: Added optional `topic_ids` query parameter (array of strings)
    source_release: https://elevenlabs.io/docs/changelog/2026/6/1
  - quote: '[Create agent](https://elevenlabs.io/docs/api-reference/agents/create)
      - `POST /v1/convai/agents/create`'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/1
  - quote: Deprecated optional `enable_versioning` query parameter (boolean, ignored)
    source_release: https://elevenlabs.io/docs/changelog/2026/6/1
  - quote: '[Update agent](https://elevenlabs.io/docs/api-reference/agents/update)
      - `PATCH /v1/convai/agents/{agent_id}`'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/1
  - quote: Deprecated optional `enable_versioning_if_not_enabled` query parameter
      (boolean, ignored)
    source_release: https://elevenlabs.io/docs/changelog/2026/6/1
  - quote: '[Run tests on the agent](https://elevenlabs.io/docs/api-reference/tests/run-tests)
      - `POST /v1/convai/agents/{agent_id}/run-tests`'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/1
  - quote: Added optional `repeat_count` (integer, 1–20, default `1`)
    source_release: https://elevenlabs.io/docs/changelog/2026/6/1
  - quote: Response adds `bucketing_status` and `result_groups` when repeat runs are
      grouped
    source_release: https://elevenlabs.io/docs/changelog/2026/6/1
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-06-01-2026-06-01-63e7e167
  source_type: elevenlabs_changelog
  theme: __candidate__
  theme_matches: []
  theme_review_reason: no_match
  theme_suggestion: elevenagents-list-conversations
  title: ElevenAgents
  type: change
---

Pending theme review. Resolve via the theme vocabulary or review decisions.