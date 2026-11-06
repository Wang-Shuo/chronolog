---
draft: true
machine_hash: 40d50e68fd21698ad64e45764928e0f2ef790dd9b571774a3366df7f27ada708
product: elevenlabs
record:
  card_id: elevenlabs-2025-02-04-6bc4b2
  comparison: ''
  date: '2025-02-04'
  description: 'ElevenLabs — ElevenLabs updates — 2025-02-04: Added POST `v1/workspace/invites/add-bulk`
    [endpoint](https://elevenlabs.io/docs/api-reference/workspace/invites/create-batch)
    to enable inviting multiple users simultaneously'
  evidence:
  - quote: Added POST `v1/workspace/invites/add-bulk` [endpoint](https://elevenlabs.io/docs/api-reference/workspace/invites/create-batch)
      to enable inviting multiple users simultaneously
    source_release: https://elevenlabs.io/docs/changelog/2025/2/4
  - quote: Added POST `v1/projects/podcast/create` [endpoint](https://elevenlabs.io/docs/api-reference/studio/create-podcast)
      for programmatic podcast generation through GenFM
    source_release: https://elevenlabs.io/docs/changelog/2025/2/4
  - quote: Added 'v1/convai/knowledge-base/:documentation_id' [endpoints](https://elevenlabs.io/docs/api-reference/knowledge-base/)
      with CRUD operations for Agents Platform
    source_release: https://elevenlabs.io/docs/changelog/2025/2/4
  - quote: Added PATCH `v1/projects/:project_id/chapters/:chapter_id` [endpoint](https://elevenlabs.io/docs/api-reference/studio/update-chapter)
      for updating project chapter content and metadata
    source_release: https://elevenlabs.io/docs/changelog/2025/2/4
  - quote: Added `group_ids` parameter to [Workspace Invite endpoint](https://elevenlabs.io/docs/api-reference/workspace/invites/create)
      for group-based access control
    source_release: https://elevenlabs.io/docs/changelog/2025/2/4
  - quote: Added structured `content` property to [Chapter response objects](https://elevenlabs.io/docs/api-reference/studio/get-chapter)
    source_release: https://elevenlabs.io/docs/changelog/2025/2/4
  - quote: Added `retention_days` and `delete_transcript_and_pii` data retention parameters
      to [Agent creation](https://elevenlabs.io/docs/api-reference/agents/create)
    source_release: https://elevenlabs.io/docs/changelog/2025/2/4
  - quote: Added structured response to [AudioNative content](https://elevenlabs.io/docs/api-reference/audio-native/create#response.body.project_id)
    source_release: https://elevenlabs.io/docs/changelog/2025/2/4
  - quote: Added `convai_chars_per_minute` usage metric to [User endpoint](https://elevenlabs.io/docs/api-reference/user/get)
    source_release: https://elevenlabs.io/docs/changelog/2025/2/4
  - quote: Added `media_metadata` field to [Dubbing response objects](https://elevenlabs.io/docs/api-reference/dubbing/get)
    source_release: https://elevenlabs.io/docs/changelog/2025/2/4
  - quote: Added GDPR-compliant `deletion_settings` to [Conversation responses](https://elevenlabs.io/docs/api-reference/conversations/get#response.body.metadata.deletion_settings)
    source_release: https://elevenlabs.io/docs/changelog/2025/2/4
  - quote: 'Deprecated Knowledge Base legacy endpoints:'
    source_release: https://elevenlabs.io/docs/changelog/2025/2/4
  - quote: POST `/v1/convai/agents/{agent_id}/add-to-knowledge-base`
    source_release: https://elevenlabs.io/docs/changelog/2025/2/4
  - quote: GET `/v1/convai/agents/{agent_id}/knowledge-base/{documentation_id}`
    source_release: https://elevenlabs.io/docs/changelog/2025/2/4
  - quote: Updated Agent endpoints with consolidated [privacy control parameters](https://elevenlabs.io/docs/api-reference/agents/create)
    source_release: https://elevenlabs.io/docs/changelog/2025/2/4
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: api
  source_release: elevenlabs-2025-02-04-2025-02-04-7d131b98
  source_type: elevenlabs_changelog
  theme: __candidate__
  theme_matches: []
  theme_review_reason: no_match
  theme_suggestion: api-added-post
  title: API
  type: change
---

Pending theme review. Resolve via the theme vocabulary or review decisions.