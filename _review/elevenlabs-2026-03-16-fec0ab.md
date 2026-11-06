---
draft: true
machine_hash: e5c17bcd9f2f9c50434676aaf06aa9ea2a1e799050dde1d2c442e0712f9b0578
product: elevenlabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-03-16-fec0ab
  comparison: ''
  confidence: low
  date: '2026-03-16'
  description: 'ElevenLabs — ElevenLabs updates — 2026-03-16: **Get all workspace
    groups**: New [GET /v1/workspace/groups](https://elevenlabs.io/docs/api-reference/workspace/groups/list)
    endpoint returns all groups in the workspace, including each group''s name, ID,
    members, permissions, usage limit, and character count.'
  evidence:
  - quote: '**Get all workspace groups**: New [GET /v1/workspace/groups](https://elevenlabs.io/docs/api-reference/workspace/groups/list)
      endpoint returns all groups in the workspace, including each group''s name,
      ID, members, permissions, usage limit, and character count.'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/16
  - quote: '**Seat type in bulk workspace invites**: The [invite multiple users](https://elevenlabs.io/docs/api-reference/workspace/invites/create-batch)
      endpoint now accepts an optional `seat_type` field to specify the seat type
      (e.g., `workspace_member`, `workspace_admin`) for all invited users in a bulk
      operation.'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/16
  - quote: '**Mobile SSO reliability improvements**: Fixed a regression where SSO
      login on mobile would get stuck on "Authenticating..." after a user logged out
      and attempted to sign in again. Also fixed workspace switching for mobile SSO
      users who sign in via SAML or OIDC providers.'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/16
  extractor_version: fallback-v5
  impact: significant
  kind: policy
  product: elevenlabs
  product_name: ElevenLabs
  slug: workspaces
  source_release: elevenlabs-2026-03-16-2026-03-16-c52d3abb
  source_type: elevenlabs_changelog
  theme: __candidate__
  theme_matches: []
  theme_review_reason: no_match
  theme_suggestion: workspaces-get-all
  title: Workspaces
  type: change
---

Pending theme review. Resolve via the theme vocabulary or review decisions.