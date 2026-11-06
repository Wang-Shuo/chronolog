---
draft: true
machine_hash: 12969ae70bcc74ed202b0a4a98f58911dac4d92a06830349927759de9b307660
product: elevenlabs
record:
  ai_generated: true
  card_id: elevenlabs-2025-07-07-37fedd
  comparison: ''
  confidence: low
  date: '2025-07-07'
  description: 'ElevenLabs — ElevenLabs updates — 2025-07-07: `POST /v1/convai/phone-numbers/create`
    has been deprecated in favor of [POST /v1/convai/phone-numbers](https://elevenlabs.io/docs/api-reference/phone-numbers/create).
    Please note that migrating to the new endpoint requires a few adjustments:'
  evidence:
  - quote: '`POST /v1/convai/phone-numbers/create` has been deprecated in favor of
      [POST /v1/convai/phone-numbers](https://elevenlabs.io/docs/api-reference/phone-numbers/create).
      Please note that migrating to the new endpoint requires a few adjustments:'
    source_release: https://elevenlabs.io/docs/changelog/2025/7/7
  - quote: Replace `provider_config` field with `inbound_trunk` and `outbound_trunk`
      for SIP trunk configurations
    source_release: https://elevenlabs.io/docs/changelog/2025/7/7
  - quote: Update response parsing to handle the new trunk configuration structure
    source_release: https://elevenlabs.io/docs/changelog/2025/7/7
  extractor_version: fallback-v5
  impact: significant
  kind: policy
  product: elevenlabs
  product_name: ElevenLabs
  slug: deprecations
  source_release: elevenlabs-2025-07-07-2025-07-07-2ce7bb7f
  source_type: elevenlabs_changelog
  theme: __candidate__
  theme_matches: []
  theme_review_reason: no_match
  theme_suggestion: deprecations-post-v1
  title: Deprecations
  type: change
---

Pending theme review. Resolve via the theme vocabulary or review decisions.