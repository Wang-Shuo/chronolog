---
card_id: open-webui-2026-02-23-b98526
date: '2026-02-23'
description: "Open WebUI · 2026-02-23 · Account and Access: 3 changes in v0.8.4 —
  \U0001F465 **Multi-device OAuth sessions.** Users can now stay logged in on multiple
  devices…"
diffusion:
  first_in_tracked: "[[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign
    into Notion with your Apple ID \U0001F5DD️ The perfect combination of speedy and
    secure]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2036
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 13a746246fb3e33cc7c7fe5c2c7374018c4a91c0e82d017b9ed50d29facadc33
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-02-23-b98526
  comparison: ''
  date: '2026-02-23'
  description: 'Open WebUI — v0.8.4: 3 Account and Access changes'
  evidence:
  - quote: "\U0001F465 **Multi-device OAuth sessions.** Users can now stay logged
      in on multiple devices simultaneously with OAuth, as re-logging in no longer
      terminates existing sessions. The oldest sessions are automatically pruned when
      the session limit is exceeded. [#21647](https://github.com/open-webui/open-webui/issues/21647),
      [Commit](https://github.com/open-webui/open-webui/commit/ae05586fdabf318d551b53ede41575355d3b9e2b)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  - quote: "\U0001F510 **OAuth group default share setting.** Administrators can now
      configure the default sharing setting for OAuth-created groups using the OAUTH_GROUP_DEFAULT_SHARE
      environment variable, allowing control over whether new groups default to private
      or shared with members. [#21679](https://github.com/open-webui/open-webui/pull/21679),
      [Commit](https://github.com/open-webui/open-webui/commit/4b9f821b58007d4efa4aa16a4995b23126e08a88)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  - quote: "\U0001F510 **LDAP optional fields fix.** LDAP configuration now properly
      accepts empty Application DN and password values, allowing LDAP authentication
      to work without these optional fields. Previously, empty values caused authentication
      failures. [Commit](https://github.com/open-webui/open-webui/commit/e1fa42d48a15c8b496a887ecfa32fc01cfd74b36)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 3-account-and-access-changes-in-v0-8-4
  source_release: open-webui-2026-02-23-v0-8-4-github-289302856-177fc54c
  source_type: github_releases
  theme: account-access
  title: 3 Account and Access changes in v0.8.4
  type: change
related_changes:
- '[[Changes/Claude Code/2026-02-19-improved-performance-by-caching-authentication-failures-for-http-and-sse-mcp-ser|Improved
  performance by caching authentication failures for HTTP and SSE MCP…]]'
- '[[Changes/OpenCode/2026-02-19-3-account-and-access-changes-in-v1-2-7|3 Account
  and Access changes in v1.2.7]]'
- '[[Changes/ElevenLabs/2026-02-23-elevenagents-f6efef|ElevenAgents]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-02-23-v0-8-4-github-289302856-177fc54c|open-webui-2026-02-23-v0-8-4-github-289302856-177fc54c]]'
source_type: github_releases
theme: account-access
title: 3 Account and Access changes in v0.8.4
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Account and Access changes in v0.8.4

**Open WebUI** · 2026-02-23 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.4) · from [[Releases/Open WebUI/open-webui-2026-02-23-v0-8-4-github-289302856-177fc54c|v0.8.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 👥 **Multi-device OAuth sessions.** Users can now stay logged in on multiple devices simultaneously with OAuth, as re-logging in no longer terminates existing sessions. The oldest sessions are automatically pruned when the session limit is exceeded. [#21647](https://github.com/open-webui/open-webui/issues/21647), [Commit](https://github.com/open-webui/open-webui/commit/ae05586fdabf318d551b53ede41575355d3b9e2b)

> 🔐 **OAuth group default share setting.** Administrators can now configure the default sharing setting for OAuth-created groups using the OAUTH_GROUP_DEFAULT_SHARE environment variable, allowing control over whether new groups default to private or shared with members. [#21679](https://github.com/open-webui/open-webui/pull/21679), [Commit](https://github.com/open-webui/open-webui/commit/4b9f821b58007d4efa4aa16a4995b23126e08a88)

> 🔐 **LDAP optional fields fix.** LDAP configuration now properly accepts empty Application DN and password values, allowing LDAP authentication to work without these optional fields. Previously, empty values caused authentication failures. [Commit](https://github.com/open-webui/open-webui/commit/e1fa42d48a15c8b496a887ecfa32fc01cfd74b36)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-02-23-12-developer-workflow-changes-in-v0-8-4|12 Developer Workflow changes in v0.8.4]] · Developer Workflow
- [[Changes/Open WebUI/2026-02-23-10-reliability-and-performance-changes-in-v0-8-4|10 Reliability and Performance changes in v0.8.4]] · Reliability and Performance
- [[Changes/Open WebUI/2026-02-23-text-file-type-detection-fix-typescript-and-other-text-files-that-were-mis-detec|📄 Text file type detection fix. TypeScript and other text files…]] · Multimodal Input
- [[Changes/Open WebUI/2026-02-23-2-memory-and-personalization-changes-in-v0-8-4|2 Memory and Personalization changes in v0.8.4]] · Memory and Personalization
- [[Changes/Open WebUI/2026-02-23-ui-accessibility-improvements-screen-reader-users-can-now-navigate-the-interface|♿ UI accessibility improvements. Screen reader users can now navigate…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-02-23-8-interface-experience-changes-in-v0-8-4|8 Interface Experience changes in v0.8.4]] · Interface Experience
- [[Changes/Open WebUI/2026-02-23-2-editor-experience-changes-in-v0-8-4|2 Editor Experience changes in v0.8.4]] · Editor Experience
- [[Changes/Open WebUI/2026-02-23-4-search-and-browsing-changes-in-v0-8-4|4 Search and Browsing changes in v0.8.4]] · Search and Browsing
- [[Changes/Open WebUI/2026-02-23-mcp-ssl-verification-fix-mcp-tool-connections-now-properly-respect-the-aiohttp-c|🔓 MCP SSL verification fix. MCP tool connections now properly respect…]] · Apps and Integrations
- [[Changes/Open WebUI/2026-02-23-file-access-control-respect-the-files-list-and-search-endpoints-now-properly-res|🗄️ File access control respect. The files list and search endpoints now properly…]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-02-23-3-safety-and-privacy-changes-in-v0-8-4|3 Safety and Privacy changes in v0.8.4]] · Safety and Privacy
- [[Changes/Open WebUI/2026-02-23-16-model-support-changes-in-v0-8-4|16 Model Support changes in v0.8.4]] · Model Support
- [[Changes/Open WebUI/2026-02-23-api-tools-fix-the-api-v1-chat-completions-endpoint-now-properly-respects-caller|🛠️ API tools fix. The /api/v1/chat/completions endpoint now properly respects…]] · Agent Mode
- [[Changes/Open WebUI/2026-02-23-15-other-changes-in-v0-8-4|15 other changes in v0.8.4]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-02-23 · ElevenLabs · [[Changes/ElevenLabs/2026-02-23-elevenagents-f6efef|ElevenAgents]]
- Later: 2026-02-25 · Codex CLI · [[Changes/Codex CLI/2026-02-25-3-account-and-access-changes-in-rust-v0-105-0|3 Account and Access changes in rust-v0.105.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Notion · [[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign into Notion with your Apple ID 🗝️ The perfect combination of speedy and secure]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-02-23-b98526&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-02-23-3-account-and-access-changes-in-v0-8-4.md%0ACard%20ID%3A%20open-webui-2026-02-23-b98526%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.4%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->