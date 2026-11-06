---
draft: true
machine_hash: a3eb5bf97ae5104156f4f4b66af4e6e5c868156a59451ff81b9b0346745e4aaf
product: elevenlabs
record:
  card_id: elevenlabs-2026-09-28-631cbf
  comparison: ''
  date: '2026-09-28'
  description: 'ElevenLabs — ElevenLabs updates — 2026-09-28: [Create service account
    API key](https://elevenlabs.io/docs/api-reference/service-accounts/api-keys/create)
    - `POST /v1/service-accounts/{service_account_user_id}/api-keys`'
  evidence:
  - quote: '[Create service account API key](https://elevenlabs.io/docs/api-reference/service-accounts/api-keys/create)
      - `POST /v1/service-accounts/{service_account_user_id}/api-keys`'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/28
  - quote: Added optional nullable `tts_concurrency_limit`, `music_concurrency_limit`
      and `dubbing_concurrency_limit` (integers) for enterprise service account API
      keys.
    source_release: https://elevenlabs.io/docs/changelog/2026/9/28
  - quote: '[Update service account API key](https://elevenlabs.io/docs/api-reference/service-accounts/api-keys/update)
      - `PATCH /v1/service-accounts/{service_account_user_id}/api-keys/{api_key_id}`'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/28
  - quote: Added optional `tts_concurrency_limit`, `music_concurrency_limit` and `dubbing_concurrency_limit`.
      Each field accepts an integer, `clear`, `no_update` or `null` and defaults to
      `no_update`.
    source_release: https://elevenlabs.io/docs/changelog/2026/9/28
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: workspaces
  source_release: elevenlabs-2026-09-28-2026-09-28-7fc35a6b
  source_type: elevenlabs_changelog
  theme: __candidate__
  theme_matches: []
  theme_review_reason: no_match
  theme_suggestion: workspaces-create-service
  title: Workspaces
  type: change
---

Pending theme review. Resolve via the theme vocabulary or review decisions.