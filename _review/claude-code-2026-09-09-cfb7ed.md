---
draft: true
machine_hash: 079a6df6c29800222fc4eaa3b627290f736648cac4be9d5f87480e9825d48f55
product: claude-code
record:
  card_id: claude-code-2026-09-09-cfb7ed
  comparison: ''
  date: '2026-09-09'
  description: 'Claude Code — v2.1.267: Gateway: Changed `forward_user_identity` upstreams
    to return a 429 as-is to a developer whose email was forwarded, instead of failing
    over to the next upstream, so the proxy''s per-user limits hold'
  evidence:
  - quote: 'Gateway: Changed `forward_user_identity` upstreams to return a 429 as-is
      to a developer whose email was forwarded, instead of failing over to the next
      upstream, so the proxy''s per-user limits hold'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.267
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: claude-code
  product_name: Claude Code
  slug: gateway-changed-forward-user-identity-upstreams-to-return-a-429-as-is-to-a-devel
  source_release: claude-code-2026-09-09-v2-1-267-github-385748811-6409148e
  source_type: github_releases
  theme: __candidate__
  theme_matches: []
  theme_review_reason: no_match
  theme_suggestion: gateway-changed-forward
  title: 'Gateway: Changed `forward_user_identity` upstreams to return a 429 as-is…'
  type: change
---

Pending theme review. Resolve via the theme vocabulary or review decisions.