---
card_id: open-webui-2025-11-25-74b2b4
date: '2025-11-25'
description: 'Open WebUI · 2025-11-25 · Other changes: 5 changes in v0.6.39 — ⚡ A
  toggle to disable parallel embedding processing was added via "ENABLE_ASYNC_EMBEDDING"…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d784877011b64cdc11c070355a4b564633e858c022d118447cb96081631cc571
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-11-25-74b2b4
  comparison: ''
  date: '2025-11-25'
  description: 'Open WebUI — v0.6.39: 5 other changes'
  evidence:
  - quote: ⚡ A toggle to disable parallel embedding processing was added via "ENABLE_ASYNC_EMBEDDING",
      allowing sequential processing for rate-limited or resource-constrained local
      embedding setups. [#19444](https://github.com/open-webui/open-webui/pull/19444)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.39
  - quote: "\U0001F4DD Inline citations now render correctly within markdown lists
      and nested elements instead of displaying as \"undefined\" values. [#19452](https://github.com/open-webui/open-webui/issues/19452)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.39
  - quote: "\U0001F465 Admin panel user list now displays the correct total user count
      and properly paginates 30 items per page after fixing database query issues
      with group member joins. [#19429](https://github.com/open-webui/open-webui/issues/19429)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.39
  - quote: "\U0001F50D Knowledge base reindexing now works correctly after resolving
      async execution chain issues by implementing threadpool workers for embedding
      operations. [#19434](https://github.com/open-webui/open-webui/pull/19434)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.39
  - quote: "\U0001F527 The environment variable \"REPLACE_IMAGE_URLS_IN_CHAT_RESPONSE\"
      has been renamed to \"ENABLE_CHAT_RESPONSE_BASE64_IMAGE_URL_CONVERSION\" for
      naming consistency."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.39
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 5-other-changes-in-v0-6-39
  source_release: open-webui-2025-11-25-v0-6-39-github-265081468-eef9ff80
  source_type: github_releases
  theme: uncategorized
  title: 5 other changes in v0.6.39
  type: change
source_release: '[[Releases/Open WebUI/open-webui-2025-11-25-v0-6-39-github-265081468-eef9ff80|open-webui-2025-11-25-v0-6-39-github-265081468-eef9ff80]]'
source_type: github_releases
theme: uncategorized
title: 5 other changes in v0.6.39
type: change
---

<!-- chronolog:begin region="header" -->
# 5 other changes in v0.6.39

**Open WebUI** · 2025-11-25 · Other changes · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.39) · from [[Releases/Open WebUI/open-webui-2025-11-25-v0-6-39-github-265081468-eef9ff80|v0.6.39]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> ⚡ A toggle to disable parallel embedding processing was added via "ENABLE_ASYNC_EMBEDDING", allowing sequential processing for rate-limited or resource-constrained local embedding setups. [#19444](https://github.com/open-webui/open-webui/pull/19444)

> 📝 Inline citations now render correctly within markdown lists and nested elements instead of displaying as "undefined" values. [#19452](https://github.com/open-webui/open-webui/issues/19452)

> 👥 Admin panel user list now displays the correct total user count and properly paginates 30 items per page after fixing database query issues with group member joins. [#19429](https://github.com/open-webui/open-webui/issues/19429)

> 🔍 Knowledge base reindexing now works correctly after resolving async execution chain issues by implementing threadpool workers for embedding operations. [#19434](https://github.com/open-webui/open-webui/pull/19434)

> 🔧 The environment variable "REPLACE_IMAGE_URLS_IN_CHAT_RESPONSE" has been renamed to "ENABLE_CHAT_RESPONSE_BASE64_IMAGE_URL_CONVERSION" for naming consistency.

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.39
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-11-25-openai-image-generation-now-works-correctly-after-fixing-a-connection-adapter-er|🖼️ OpenAI image generation now works correctly after fixing a connection adapter…]] · Image Generation
- [[Changes/Open WebUI/2025-11-25-breaking-docling-configuration-has-been-consolidated-from-individual-environment|🔧 BREAKING: Docling configuration has been consolidated from individual environment…]] · Account and Access
- [[Changes/Open WebUI/2025-11-25-localization-improvements-were-made-for-german-de-de-and-portuguese-brazil-trans|🌐 Localization improvements were made for German (de-DE) and Portuguese (Brazil)…]] · Accessibility and Localization
- [[Changes/Open WebUI/2025-11-25-a-user-list-modal-was-added-to-channels-displaying-all-users-with-access-and-fea|💬 A user list modal was added to channels, displaying all users with access…]] · Developer Workflow
- [[Changes/Open WebUI/2025-11-25-various-improvements-were-implemented-across-the-frontend-and-backend-to-enhance|🔄 Various improvements were implemented across the frontend and backend to enhance…]] · Reliability and Performance
- [[Changes/Open WebUI/2025-11-25-2-interface-experience-changes-in-v0-6-39|2 Interface Experience changes in v0.6.39]] · Interface Experience
- [[Changes/Open WebUI/2025-11-25-tool-servers-and-mcp-connections-now-support-function-name-filtering-allowing-ad|🔌 Tool servers and MCP connections now support function name filtering, allowing…]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-11-25-74b2b4&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-11-25-5-other-changes-in-v0-6-39.md%0ACard%20ID%3A%20open-webui-2025-11-25-74b2b4%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.39%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->