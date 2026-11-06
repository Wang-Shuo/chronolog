---
draft: true
machine_hash: ecf24b02b425a94e8ccdc42047e19eaf58ec460bf3649369633758e90d2a9b0f
product: elevenlabs
record:
  card_id: elevenlabs-2026-09-07-c6fc47
  comparison: ''
  date: '2026-09-07'
  description: 'ElevenLabs — ElevenLabs updates — 2026-09-07: `WebhookEventType` adds
    `answering_machine_detection`.'
  evidence:
  - quote: '`WebhookEventType` adds `answering_machine_detection`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/7
  - quote: '`AgentBranchSummary` adds optional nullable `draft_created_at` (integer)
      and optional `draft_is_behind_tip` (boolean, default `false`).'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/7
  - quote: '`AgentKnowledgeBaseRagChunkResponseModel` adds required nullable `source_url`
      (string).'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/7
  - quote: '`AgentSummaryResponseModel` and `SpeechEngineSummaryResponse` add required
      `voice_id` (string).'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/7
  - quote: '`AnalysisProperty` adds optional nullable `name` (string) and `allowed_values`
      (`AllowedValues`). `LiteralJsonSchemaProperty` also adds `allowed_values`. Both
      deprecate `allowed_values_dynamic_variable`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/7
  - quote: '`DataCollectionResultCommonModel` adds optional nullable `name` (string).'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/7
  - quote: '`WorkspaceApiKeyResponseModel` adds optional nullable `platform_limits`
      (`PlatformLimits`).'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/7
  - quote: MCP tool `Icon` adds optional nullable `theme` (`light` or `dark`).
    source_release: https://elevenlabs.io/docs/changelog/2026/9/7
  - quote: '`SMBToolConfig` adds `send_custom_email`, `create_service_quote_request`
      and `create_product_quote_request` parameter variants.'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/7
  - quote: Webhook query parameter schemas and telephony call configuration now use
      separate input and output models.
    source_release: https://elevenlabs.io/docs/changelog/2026/9/7
  - quote: '`agent_response` WebSocket events add optional `attachments` (array).
      Each item requires `url` and `name` (strings) and accepts optional `mime_type`
      (string).'
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
  theme_suggestion: elevenagents-webhookeventtype-adds
  title: ElevenAgents
  type: change
---

Pending theme review. Resolve via the theme vocabulary or review decisions.