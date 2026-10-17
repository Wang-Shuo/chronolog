---
draft: true
machine_hash: 50157e7bf6d15f0fc1c131affa03b4010a649ab11fa154e452482fe4323c5c73
product: claude-code
record:
  card_id: claude-code-2026-09-03-c41f0a
  comparison: ''
  date: '2026-09-03'
  description: 'Claude Code — v2.1.260: Improved the Claude apps gateway on Amazon
    Bedrock: input tokens for an aborted request are now counted with AWS''s free
    CountTokens API (grant `bedrock:CountTokens`) instead of a one-token request'
  evidence:
  - quote: 'Improved the Claude apps gateway on Amazon Bedrock: input tokens for an
      aborted request are now counted with AWS''s free CountTokens API (grant `bedrock:CountTokens`)
      instead of a one-token request'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.260
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: claude-code
  product_name: Claude Code
  slug: improved-the-claude-apps-gateway-on-amazon-bedrock-input-tokens-for-an-aborted-r
  source_release: claude-code-2026-09-03-v2-1-260-github-382367470-ac2ba1fc
  source_type: github_releases
  theme: __candidate__
  theme_matches:
  - matched_terms:
    - apps
    score: 50
    theme: apps-integrations
  - matched_terms:
    - tokens
    score: 50
    theme: context-window
  theme_review_reason: ambiguous_match
  theme_suggestion: apps-integrations-or-context-window
  title: Improved the Claude apps gateway on Amazon Bedrock
  type: change
---

Pending theme review. Resolve via the theme vocabulary or review decisions.