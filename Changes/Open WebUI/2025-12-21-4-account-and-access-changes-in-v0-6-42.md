---
card_id: open-webui-2025-12-21-ac0b9d
date: '2025-12-21'
description: "Open WebUI · 2025-12-21 · Account and Access: 4 changes in v0.6.42 —
  \U0001F510 LDAP authentication now supports user entries with multiple username
  attributes…"
diffusion:
  first_in_tracked: "[[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign
    into Notion with your Apple ID \U0001F5DD️ The perfect combination of speedy and
    secure]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1972
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9af5c7ec6fb6ba3e9b02c476b00ab1a3cd9665cbb939dc9c6670977624d1303d
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-12-21-ac0b9d
  comparison: ''
  date: '2025-12-21'
  description: 'Open WebUI — v0.6.42: 4 Account and Access changes'
  evidence:
  - quote: "\U0001F510 LDAP authentication now supports user entries with multiple
      username attributes, correctly handling cases where the username field contains
      a list of values. [Commit](https://github.com/open-webui/open-webui/commit/379f888c9dc6dce21c3ef7a1fc455258aff993dc),
      [#19878](https://github.com/open-webui/open-webui/issues/19878)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F511 The \"OAUTH_AUDIENCE\" environment variable now allows OAuth
      providers to specify audience parameters for JWT access token generation. [#19768](https://github.com/open-webui/open-webui/pull/19768)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F3AB MCP OAuth 2.1 token exchange failures are now fixed by removing
      duplicate credential passing that caused \"ID1,ID1\" concatenation and 401 errors
      from the token endpoint. [#20076](https://github.com/open-webui/open-webui/pull/20076),
      [#19823](https://github.com/open-webui/open-webui/issues/19823)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F511 MCP OAuth 2.1 tool servers now work correctly in multi-node
      deployments through lazy-loading of OAuth clients from Redis-synced configuration,
      eliminating 404 errors when load balancers route requests to nodes that didn't
      process the original config update. [#20076](https://github.com/open-webui/open-webui/pull/20076),
      [#19902](https://github.com/open-webui/open-webui/pull/19902), [#19901](https://github.com/open-webui/open-webui/issues/19901)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 4-account-and-access-changes-in-v0-6-42
  source_release: open-webui-2025-12-21-v0-6-42-github-272053915-b8e46ad9
  source_type: github_releases
  theme: account-access
  title: 4 Account and Access changes in v0.6.42
  type: change
related_changes:
- '[[Changes/Windsurf/2025-12-12-request-all-supported-scopes-if-no-scopes-are-provided-in-mcp-oauth-config|Request
  all supported scopes if no scopes are provided in MCP OAuth config]]'
- '[[Changes/Gemini CLI/2025-12-16-allow-telemetry-exporters-to-gcp-to-utilize-user-s-login-credentials-if-requeste|Allow
  telemetry exporters to GCP to utilize user''s login credentials, if requested]]'
- '[[Changes/Codex CLI/2025-12-21-2-account-and-access-changes-in-rust-v0-77-0|2 Account
  and Access changes in rust-v0.77.0]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-12-21-v0-6-42-github-272053915-b8e46ad9|open-webui-2025-12-21-v0-6-42-github-272053915-b8e46ad9]]'
source_type: github_releases
theme: account-access
title: 4 Account and Access changes in v0.6.42
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Account and Access changes in v0.6.42

**Open WebUI** · 2025-12-21 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.42) · from [[Releases/Open WebUI/open-webui-2025-12-21-v0-6-42-github-272053915-b8e46ad9|v0.6.42]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔐 LDAP authentication now supports user entries with multiple username attributes, correctly handling cases where the username field contains a list of values. [Commit](https://github.com/open-webui/open-webui/commit/379f888c9dc6dce21c3ef7a1fc455258aff993dc), [#19878](https://github.com/open-webui/open-webui/issues/19878)

> 🔑 The "OAUTH_AUDIENCE" environment variable now allows OAuth providers to specify audience parameters for JWT access token generation. [#19768](https://github.com/open-webui/open-webui/pull/19768)

> 🎫 MCP OAuth 2.1 token exchange failures are now fixed by removing duplicate credential passing that caused "ID1,ID1" concatenation and 401 errors from the token endpoint. [#20076](https://github.com/open-webui/open-webui/pull/20076), [#19823](https://github.com/open-webui/open-webui/issues/19823)

> 🔑 MCP OAuth 2.1 tool servers now work correctly in multi-node deployments through lazy-loading of OAuth clients from Redis-synced configuration, eliminating 404 errors when load balancers route requests to nodes that didn't process the original config update. [#20076](https://github.com/open-webui/open-webui/pull/20076), [#19902](https://github.com/open-webui/open-webui/pull/19902), [#19901](https://github.com/open-webui/open-webui/issues/19901)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-12-21-user-uploaded-images-are-now-automatically-converted-from-base64-to-actual-file|🖼️ User-uploaded images are now automatically converted from base64 to actual file…]] · Collaboration
- [[Changes/Open WebUI/2025-12-21-3-editor-experience-changes-in-v0-6-42|3 Editor Experience changes in v0.6.42]] · Editor Experience
- [[Changes/Open WebUI/2025-12-21-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-12-21-2-apps-and-integrations-changes-in-v0-6-42|2 Apps and Integrations changes in v0.6.42]] · Apps and Integrations
- [[Changes/Open WebUI/2025-12-21-6-files-and-data-changes-in-v0-6-42|6 Files and Data changes in v0.6.42]] · Files and Data
- [[Changes/Open WebUI/2025-12-21-7-reliability-and-performance-changes-in-v0-6-42|7 Reliability and Performance changes in v0.6.42]] · Reliability and Performance
- [[Changes/Open WebUI/2025-12-21-11-model-support-changes-in-v0-6-42|11 Model Support changes in v0.6.42]] · Model Support
- [[Changes/Open WebUI/2025-12-21-6-safety-and-privacy-changes-in-v0-6-42|6 Safety and Privacy changes in v0.6.42]] · Safety and Privacy
- [[Changes/Open WebUI/2025-12-21-8-interface-experience-changes-in-v0-6-42|8 Interface Experience changes in v0.6.42]] · Interface Experience
- [[Changes/Open WebUI/2025-12-21-external-reranker-operations-were-optimized-to-prevent-event-loop-blocking-by-of|⚡ External reranker operations were optimized to prevent event loop blocking…]] · Automation and Scheduling
- [[Changes/Open WebUI/2025-12-21-3-search-and-browsing-changes-in-v0-6-42|3 Search and Browsing changes in v0.6.42]] · Search and Browsing
- [[Changes/Open WebUI/2025-12-21-11-developer-workflow-changes-in-v0-6-42|11 Developer Workflow changes in v0.6.42]] · Developer Workflow
- [[Changes/Open WebUI/2025-12-21-2-multimodal-input-changes-in-v0-6-42|2 Multimodal Input changes in v0.6.42]] · Multimodal Input
- [[Changes/Open WebUI/2025-12-21-4-image-generation-changes-in-v0-6-42|4 Image Generation changes in v0.6.42]] · Image Generation
- [[Changes/Open WebUI/2025-12-21-2-voice-and-audio-changes-in-v0-6-42|2 Voice and Audio changes in v0.6.42]] · Voice and Audio
- [[Changes/Open WebUI/2025-12-21-channel-image-upload-handling-was-optimized-to-process-and-store-compressed-imag|🖼️ Channel image upload handling was optimized to process and store compressed…]] · Memory and Personalization
- [[Changes/Open WebUI/2025-12-21-28-other-changes-in-v0-6-42|28 other changes in v0.6.42]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2025-12-21 · Codex CLI · [[Changes/Codex CLI/2025-12-21-2-account-and-access-changes-in-rust-v0-77-0|2 Account and Access changes in rust-v0.77.0]]
- Later: 2025-12-22 · Cursor · [[Changes/Cursor/2025-12-22-2-account-and-access-changes-in-2-3|2 Account and Access changes in 2.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Notion · [[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign into Notion with your Apple ID 🗝️ The perfect combination of speedy and secure]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-12-21-ac0b9d&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-12-21-4-account-and-access-changes-in-v0-6-42.md%0ACard%20ID%3A%20open-webui-2025-12-21-ac0b9d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.42%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->