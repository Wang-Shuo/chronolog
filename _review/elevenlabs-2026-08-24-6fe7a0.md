---
draft: true
machine_hash: 0e0afccceeb41c520ecdedd976d9737a182ec650e06bee611fd5d0e2ab2c142c
product: elevenlabs
record:
  card_id: elevenlabs-2026-08-24-6fe7a0
  comparison: ''
  date: '2026-08-24'
  description: 'ElevenLabs — ElevenLabs updates — 2026-08-24: [Get signed URL](https://elevenlabs.io/docs/api-reference/conversations/get-signed-url)
    - `GET /v1/convai/conversation/get-signed-url`'
  evidence:
  - quote: '[Get signed URL](https://elevenlabs.io/docs/api-reference/conversations/get-signed-url)
      - `GET /v1/convai/conversation/get-signed-url`'
    source_release: https://elevenlabs.io/docs/changelog/2026/8/24
  - quote: Added optional `debug_events_request` (boolean, default `false`). Debug
      events require editor access to the agent.
    source_release: https://elevenlabs.io/docs/changelog/2026/8/24
  - quote: '[Get WebRTC token](https://elevenlabs.io/docs/api-reference/conversations/get-webrtc-token)
      - `GET /v1/convai/conversation/token`'
    source_release: https://elevenlabs.io/docs/changelog/2026/8/24
  - quote: Added optional `debug_events_request` (boolean, default `false`). The legacy
      `GET /v1/convai/conversation/get_signed_url` route accepts the same parameter.
    source_release: https://elevenlabs.io/docs/changelog/2026/8/24
  - quote: '[List conversations](https://elevenlabs.io/docs/api-reference/conversations/list)
      - `GET /v1/convai/conversations`'
    source_release: https://elevenlabs.io/docs/changelog/2026/8/24
  - quote: Added optional `triggered_procedure_ids` (nullable string array, maximum
      50) to match conversations where any specified procedure ran.
    source_release: https://elevenlabs.io/docs/changelog/2026/8/24
  - quote: Added optional `include_invalid_tool_calls` (boolean, default `false`)
      to include tool calls that did not run.
    source_release: https://elevenlabs.io/docs/changelog/2026/8/24
  - quote: Added optional `sort_direction` (`asc` or `desc`, default `desc`) for call
      start time.
    source_release: https://elevenlabs.io/docs/changelog/2026/8/24
  - quote: '[Text search conversation messages](https://elevenlabs.io/docs/api-reference/conversations/messages/text-search)
      - `GET /v1/convai/conversations/messages/text-search`'
    source_release: https://elevenlabs.io/docs/changelog/2026/8/24
  - quote: Added optional `triggered_procedure_ids` (nullable string array, maximum
      50).
    source_release: https://elevenlabs.io/docs/changelog/2026/8/24
  - quote: Added optional `include_invalid_tool_calls` (boolean, default `false`).
    source_release: https://elevenlabs.io/docs/changelog/2026/8/24
  - quote: '[Get agent conversation topics](https://elevenlabs.io/docs/api-reference/conversations/topics/get)
      - `GET /v1/convai/agents/{agent_id}/topics`'
    source_release: https://elevenlabs.io/docs/changelog/2026/8/24
  - quote: Added optional `include_evaluation_criteria` (boolean, default `true`).
    source_release: https://elevenlabs.io/docs/changelog/2026/8/24
  - quote: Added `frustration` to `sort_by`.
    source_release: https://elevenlabs.io/docs/changelog/2026/8/24
  - quote: Topic responses add nullable `success_rate` (number), while the overall
      response adds `aggregated_run_count` (integer, default `0`).
    source_release: https://elevenlabs.io/docs/changelog/2026/8/24
  - quote: '`from_unix_secs` is floored to the start of its UTC day. A bounded range
      aggregates completed daily discovery runs; omitting both bounds returns the
      latest run.'
    source_release: https://elevenlabs.io/docs/changelog/2026/8/24
  - quote: '[List procedures](https://elevenlabs.io/docs/api-reference/agents/procedures/list)
      (`GET /v1/convai/agents/{agent_id}/branches/{branch_id}/procedures`) and [Get
      procedure](https://elevenlabs.io/docs/api-reference/agents/procedures/get) (`GET
      /v1/convai/agents/{agent_id}/branches/{branch_id}/procedures/{procedure_id}`)'
    source_release: https://elevenlabs.io/docs/changelog/2026/8/24
  - quote: Added optional nullable `agent_version_id` (string) to retrieve procedures
      from a specific agent version.
    source_release: https://elevenlabs.io/docs/changelog/2026/8/24
  - quote: '[Create test](https://elevenlabs.io/docs/api-reference/tests/create) and
      [Update test](https://elevenlabs.io/docs/api-reference/tests/update)'
    source_release: https://elevenlabs.io/docs/changelog/2026/8/24
  - quote: Added optional nullable `environment` (string) to response, simulation
      and tool-call unit test schemas. The value selects environment-specific URLs,
      headers and auth connections; it defaults to `production`.
    source_release: https://elevenlabs.io/docs/changelog/2026/8/24
  - quote: '[Create URL document](https://elevenlabs.io/docs/api-reference/knowledge-base/create-from-url),
      [Create crawl job](https://elevenlabs.io/docs/api-reference/knowledge-base/create-crawl-job)
      and [Create folder](https://elevenlabs.io/docs/api-reference/knowledge-base/create-folder)'
    source_release: https://elevenlabs.io/docs/changelog/2026/8/24
  - quote: Added optional nullable `minimum_frequency_days` (integer, 1–180) for auto-sync.
      The default is `7`, and a stricter parent-folder frequency takes precedence.
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
  theme_suggestion: elevenagents-get-signed
  title: ElevenAgents
  type: change
---

Pending theme review. Resolve via the theme vocabulary or review decisions.