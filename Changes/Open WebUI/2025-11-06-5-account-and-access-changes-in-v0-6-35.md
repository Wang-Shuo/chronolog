---
card_id: open-webui-2025-11-06-fae69a
date: '2025-11-06'
description: "Open WebUI · 2025-11-06 · Account and Access: 5 changes in v0.6.35 —
  \U0001F510 OAUTH_ROLES_SEPARATOR environment variable now allows custom role separators
  for OAuth…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 952
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 341d2942df880de232a173f2d7cf76fdda6202e1d2643cb12bb8b7744aba0259
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-11-06-fae69a
  comparison: ''
  date: '2025-11-06'
  description: 'Open WebUI — v0.6.35: 5 Account and Access changes'
  evidence:
  - quote: "\U0001F510 OAUTH_ROLES_SEPARATOR environment variable now allows custom
      role separators for OAuth roles that contain commas, useful for roles specified
      in LDAP syntax. [#18572](https://github.com/open-webui/open-webui/pull/18572)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  - quote: "\U0001F510 Login failures with passwords longer than 72 bytes are resolved
      by safely truncating oversized passwords for bcrypt compatibility. [#18157](https://github.com/open-webui/open-webui/issues/18157)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  - quote: "\U0001F510 OAuth 2.1 MCP tool connections now automatically re-register
      clients when stored client IDs become stale, preventing unauthorized_client
      errors after editing tool endpoints and providing detailed error messages for
      callback failures. [#18415](https://github.com/open-webui/open-webui/pull/18415),
      [#18309](https://github.com/open-webui/open-webui/issues/18309)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  - quote: "\U0001F513 OAuth 2.1 discovery, metadata fetching, and dynamic client
      registration now correctly use HTTP proxy environment variables when trust_env
      is enabled. [Commit](https://github.com/open-webui/open-webui/commit/bafeb76c411483bd6b135f0edbcdce048120f264)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  - quote: "\U0001F512 Incorrect await call in the OAuth 2.1 flow is removed, eliminating
      a logged exception during authentication. [#18236](https://github.com/open-webui/open-webui/pull/18236)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 5-account-and-access-changes-in-v0-6-35
  source_release: open-webui-2025-11-06-v0-6-35-github-260376122-7fa65234
  source_type: github_releases
  theme: account-access
  title: 5 Account and Access changes in v0.6.35
  type: change
related_changes:
- '[[Changes/Gemini CLI/2025-11-04-disable-model-routing-for-oauth-users-by-mrcabbage972-in-https-github-com-google|Disable
  model routing for oauth users]]'
- '[[Changes/Ollama/2025-11-05-ollama-will-now-show-login-instructions-when-switching-to-a-cloud-model-in-inter|Ollama
  will now show login instructions when switching to a cloud model…]]'
- "[[Changes/Open WebUI/2025-11-06-oauth-group-parsing-now-supports-configurable-separators-via-the-oauth-groups-se|\U0001F510
  OAuth group parsing now supports configurable separators…]]"
source_release: '[[Releases/Open WebUI/open-webui-2025-11-06-v0-6-35-github-260376122-7fa65234|open-webui-2025-11-06-v0-6-35-github-260376122-7fa65234]]'
source_type: github_releases
theme: account-access
title: 5 Account and Access changes in v0.6.35
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Account and Access changes in v0.6.35

**Open WebUI** · 2025-11-06 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.35) · from [[Releases/Open WebUI/open-webui-2025-11-06-v0-6-35-github-260376122-7fa65234|v0.6.35]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔐 OAUTH_ROLES_SEPARATOR environment variable now allows custom role separators for OAuth roles that contain commas, useful for roles specified in LDAP syntax. [#18572](https://github.com/open-webui/open-webui/pull/18572)

> 🔐 Login failures with passwords longer than 72 bytes are resolved by safely truncating oversized passwords for bcrypt compatibility. [#18157](https://github.com/open-webui/open-webui/issues/18157)

> 🔐 OAuth 2.1 MCP tool connections now automatically re-register clients when stored client IDs become stale, preventing unauthorized_client errors after editing tool endpoints and providing detailed error messages for callback failures. [#18415](https://github.com/open-webui/open-webui/pull/18415), [#18309](https://github.com/open-webui/open-webui/issues/18309)

> 🔓 OAuth 2.1 discovery, metadata fetching, and dynamic client registration now correctly use HTTP proxy environment variables when trust_env is enabled. [Commit](https://github.com/open-webui/open-webui/commit/bafeb76c411483bd6b135f0edbcdce048120f264)

> 🔒 Incorrect await call in the OAuth 2.1 flow is removed, eliminating a logged exception during authentication. [#18236](https://github.com/open-webui/open-webui/pull/18236)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-11-06-chat-controls-button-is-now-properly-hidden-on-mobile-for-users-without-admin-or|📱 Chat controls button is now properly hidden on mobile for users without admin…]] · Mobile and Desktop
- [[Changes/Open WebUI/2025-11-06-3-voice-and-audio-changes-in-v0-6-35|3 Voice and Audio changes in v0.6.35]] · Voice and Audio
- [[Changes/Open WebUI/2025-11-06-10-model-support-changes-in-v0-6-35|10 Model Support changes in v0.6.35]] · Model Support
- [[Changes/Open WebUI/2025-11-06-2-multimodal-input-changes-in-v0-6-35|2 Multimodal Input changes in v0.6.35]] · Multimodal Input
- [[Changes/Open WebUI/2025-11-06-4-safety-and-privacy-changes-in-v0-6-35|4 Safety and Privacy changes in v0.6.35]] · Safety and Privacy
- [[Changes/Open WebUI/2025-11-06-3-developer-workflow-changes-in-v0-6-35|3 Developer Workflow changes in v0.6.35]] · Developer Workflow
- [[Changes/Open WebUI/2025-11-06-10-interface-experience-changes-in-v0-6-35|10 Interface Experience changes in v0.6.35]] · Interface Experience
- [[Changes/Open WebUI/2025-11-06-3-editor-experience-changes-in-v0-6-35|3 Editor Experience changes in v0.6.35]] · Editor Experience
- [[Changes/Open WebUI/2025-11-06-4-search-and-browsing-changes-in-v0-6-35|4 Search and Browsing changes in v0.6.35]] · Search and Browsing
- [[Changes/Open WebUI/2025-11-06-3-reliability-and-performance-changes-in-v0-6-35|3 Reliability and Performance changes in v0.6.35]] · Reliability and Performance
- [[Changes/Open WebUI/2025-11-06-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-11-06-3-context-window-changes-in-v0-6-35|3 Context Window changes in v0.6.35]] · Context Window
- [[Changes/Open WebUI/2025-11-06-edit-button-is-now-available-in-the-three-dot-menu-of-models-in-the-workspace-se|✏️ Edit button is now available in the three-dot menu of models in the workspace…]] · Model Support
- [[Changes/Open WebUI/2025-11-06-screen-reader-support-was-enhanced-by-wrapping-messages-in-semantic-elements-wit|♿ Screen reader support was enhanced by wrapping messages in semantic elements…]] · Accessibility and Localization
- [[Changes/Open WebUI/2025-11-06-external-document-loaders-can-now-optionally-forward-user-information-headers-wh|📄 External document loaders can now optionally forward user information headers…]] · Pricing Model
- [[Changes/Open WebUI/2025-11-06-3-files-and-data-changes-in-v0-6-35|3 Files and Data changes in v0.6.35]] · Files and Data
- [[Changes/Open WebUI/2025-11-06-2-apps-and-integrations-changes-in-v0-6-35|2 Apps and Integrations changes in v0.6.35]] · Apps and Integrations
- [[Changes/Open WebUI/2025-11-06-22-other-changes-in-v0-6-35|22 other changes in v0.6.35]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2025-11-06 · Open WebUI · [[Changes/Open WebUI/2025-11-06-oauth-group-parsing-now-supports-configurable-separators-via-the-oauth-groups-se|🔐 OAuth group parsing now supports configurable separators…]]
- Later: 2025-11-07 · Codex CLI · [[Changes/Codex CLI/2025-11-07-3-account-and-access-changes-in-rust-v0-56-0|3 Account and Access changes in rust-v0.56.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-11-06-fae69a&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-11-06-5-account-and-access-changes-in-v0-6-35.md%0ACard%20ID%3A%20open-webui-2025-11-06-fae69a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.35%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->