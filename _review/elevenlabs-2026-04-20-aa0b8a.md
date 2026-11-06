---
draft: true
machine_hash: 95abf67cba18338eebfc60f44ba1126d1290bd6d1b8221ba3e14f7f1cc76f07d
product: elevenlabs
record:
  card_id: elevenlabs-2026-04-20-aa0b8a
  comparison: ''
  date: '2026-04-20'
  description: 'ElevenLabs — ElevenLabs updates — 2026-04-20: `GET /v1/usage/character-stats`
    - Deprecated in favor of `POST /v1/workspace/analytics/query/usage-by-product-over-time`'
  evidence:
  - quote: '`GET /v1/usage/character-stats` - Deprecated in favor of `POST /v1/workspace/analytics/query/usage-by-product-over-time`'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/20
  - quote: All dubbing resource editing endpoints (`POST /v1/dubbing/resource/{dubbing_id}/language`,
      `POST /v1/dubbing/resource/{dubbing_id}/speaker/{speaker_id}/segment`, `PATCH
      /v1/dubbing/resource/{dubbing_id}/segment/{segment_id}/{language}`, and others)
      are now deprecated
    source_release: https://elevenlabs.io/docs/changelog/2026/4/20
  extractor_version: fallback-v5
  impact: incremental
  kind: policy
  product: elevenlabs
  product_name: ElevenLabs
  slug: deprecated-endpoints
  source_release: elevenlabs-2026-04-20-2026-04-20-9278926e
  source_type: elevenlabs_changelog
  theme: __candidate__
  theme_matches: []
  theme_review_reason: no_match
  theme_suggestion: deprecated-endpoints-get
  title: Deprecated Endpoints
  type: change
---

Pending theme review. Resolve via the theme vocabulary or review decisions.