---
card_id: open-webui-2025-10-07-2b1bb9
date: '2025-10-07'
description: "Open WebUI · 2025-10-07 · Account and Access: 10 changes in v0.6.33
  — \U0001F517 OpenAI connections now support custom HTTP headers, enabling users
  to configure…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 922
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: cca661ca9138b33e7a5e6007acdaca8934b9076ff8daef29940fd1748c24599d
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-10-07-2b1bb9
  comparison: ''
  date: '2025-10-07'
  description: 'Open WebUI — v0.6.33: 10 Account and Access changes'
  evidence:
  - quote: "\U0001F517 OpenAI connections now support custom HTTP headers, enabling
      users to configure authentication and routing headers for specific deployment
      requirements. [#18021](https://github.com/open-webui/open-webui/pull/18021),
      [#9732](https://github.com/open-webui/open-webui/discussions/9732)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.33
  - quote: "\U0001F510 OpenID Connect authentication now supports OIDC providers without
      email scope via the ENABLE_OAUTH_WITHOUT_EMAIL environment variable, enabling
      compatibility with identity providers that don't expose email addresses. [#18047](https://github.com/open-webui/open-webui/pull/18047),
      [#18045](https://github.com/open-webui/open-webui/issues/18045)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.33
  - quote: "\U0001F510 MCP OAuth 2.1 authentication now complies with the standard
      by implementing PKCE with S256 code challenge method and explicitly passing
      client credentials during token authorization, resolving \"code_challenge: Field
      required\" and \"client_id: Field required\" errors when connecting to OAuth-secured
      MCP servers. [Commit](https://github.com/open-webui/open-webui/commit/911a114ad459f5deebd97543c13c2b90196efb54),
      [#18010](https://github.com/open-webui/open-webui/issues/18010), [#18087](https://github.com/open-webui/open-webui/pull/18087)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.33
  - quote: "\U0001F510 OAuth signup flow now handles password hashing correctly by
      migrating from passlib to native bcrypt, preventing failures when passwords
      exceed 72 bytes. [#17917](https://github.com/open-webui/open-webui/issues/17917)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.33
  - quote: "\U0001F510 OAuth token refresh errors are resolved by properly registering
      and storing OAuth clients, fixing \"Constructor parameter should be str\" exceptions
      for Google, Microsoft, and OIDC providers. [#17829](https://github.com/open-webui/open-webui/issues/17829)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.33
  - quote: "\U0001F510 OAuth server metadata URL is now correctly accessed via the
      proper attribute, fixing automatic token refresh and logout functionality for
      Microsoft OAuth provider when OPENID_PROVIDER_URL is not set. [#18065](https://github.com/open-webui/open-webui/pull/18065)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.33
  - quote: "\U0001F510 OAuth credential decryption failures now allow the application
      to start gracefully with clear error messages instead of crashing, preventing
      complete service outages when WEBUI_SECRET_KEY mismatches occur during database
      migrations or environment changes. [#18094](https://github.com/open-webui/open-webui/pull/18094),
      [#18092](https://github.com/open-webui/open-webui/issues/18092)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.33
  - quote: "\U0001F510 OAuth 2.1 server discovery now correctly attempts all configured
      discovery URLs in sequence instead of only trying the first URL. [#17906](https://github.com/open-webui/open-webui/pull/17906),
      [#17904](https://github.com/open-webui/open-webui/issues/17904), [#18026](https://github.com/open-webui/open-webui/pull/18026)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.33
  - quote: "\U0001F510 Login redirect now correctly honors the redirect query parameter
      after authentication, ensuring users are returned to their intended destination
      with query parameters intact instead of defaulting to the homepage. [#18071](https://github.com/open-webui/open-webui/issues/18071)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.33
  - quote: ☁️ OneDrive Business integration authentication regression is resolved,
      ensuring the popup now properly triggers when connecting to OneDrive accounts.
      [#17902](https://github.com/open-webui/open-webui/pull/17902), [#17825](https://github.com/open-webui/open-webui/discussions/17825),
      [#17816](https://github.com/open-webui/open-webui/issues/17816)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.33
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 10-account-and-access-changes-in-v0-6-33
  source_release: open-webui-2025-10-07-v0-6-33-github-252853067-e907999d
  source_type: github_releases
  theme: account-access
  title: 10 Account and Access changes in v0.6.33
  type: change
related_changes:
- '[[Changes/Codex CLI/2025-10-06-3-account-and-access-changes-in-rust-v0-45-0|3 Account
  and Access changes in rust-v0.45.0]]'
- '[[Changes/Lovable/2025-10-06-lovable-cloud|Lovable Cloud]]'
- '[[Changes/Gemini CLI/2025-10-07-for-dynamic-client-registration-use-registration-endpoint-in-config-if-available|For
  dynamic client registration - use registration endpoint in config if available…]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-10-07-v0-6-33-github-252853067-e907999d|open-webui-2025-10-07-v0-6-33-github-252853067-e907999d]]'
source_type: github_releases
theme: account-access
title: 10 Account and Access changes in v0.6.33
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Account and Access changes in v0.6.33

**Open WebUI** · 2025-10-07 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.33) · from [[Releases/Open WebUI/open-webui-2025-10-07-v0-6-33-github-252853067-e907999d|v0.6.33]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔗 OpenAI connections now support custom HTTP headers, enabling users to configure authentication and routing headers for specific deployment requirements. [#18021](https://github.com/open-webui/open-webui/pull/18021), [#9732](https://github.com/open-webui/open-webui/discussions/9732)

> 🔐 OpenID Connect authentication now supports OIDC providers without email scope via the ENABLE_OAUTH_WITHOUT_EMAIL environment variable, enabling compatibility with identity providers that don't expose email addresses. [#18047](https://github.com/open-webui/open-webui/pull/18047), [#18045](https://github.com/open-webui/open-webui/issues/18045)

> 🔐 MCP OAuth 2.1 authentication now complies with the standard by implementing PKCE with S256 code challenge method and explicitly passing client credentials during token authorization, resolving "code_challenge: Field required" and "client_id: Field required" errors when connecting to OAuth-secured MCP servers. [Commit](https://github.com/open-webui/open-webui/commit/911a114ad459f5deebd97543c13c2b90196efb54), [#18010](https://github.com/open-webui/open-webui/issues/18010), [#18087](https://github.com/open-webui/open-webui/pull/18087)

> 🔐 OAuth signup flow now handles password hashing correctly by migrating from passlib to native bcrypt, preventing failures when passwords exceed 72 bytes. [#17917](https://github.com/open-webui/open-webui/issues/17917)

> 🔐 OAuth token refresh errors are resolved by properly registering and storing OAuth clients, fixing "Constructor parameter should be str" exceptions for Google, Microsoft, and OIDC providers. [#17829](https://github.com/open-webui/open-webui/issues/17829)

> 🔐 OAuth server metadata URL is now correctly accessed via the proper attribute, fixing automatic token refresh and logout functionality for Microsoft OAuth provider when OPENID_PROVIDER_URL is not set. [#18065](https://github.com/open-webui/open-webui/pull/18065)

> 🔐 OAuth credential decryption failures now allow the application to start gracefully with clear error messages instead of crashing, preventing complete service outages when WEBUI_SECRET_KEY mismatches occur during database migrations or environment changes. [#18094](https://github.com/open-webui/open-webui/pull/18094), [#18092](https://github.com/open-webui/open-webui/issues/18092)

> 🔐 OAuth 2.1 server discovery now correctly attempts all configured discovery URLs in sequence instead of only trying the first URL. [#17906](https://github.com/open-webui/open-webui/pull/17906), [#17904](https://github.com/open-webui/open-webui/issues/17904), [#18026](https://github.com/open-webui/open-webui/pull/18026)

> 🔐 Login redirect now correctly honors the redirect query parameter after authentication, ensuring users are returned to their intended destination with query parameters intact instead of defaulting to the homepage. [#18071](https://github.com/open-webui/open-webui/issues/18071)

> ☁️ OneDrive Business integration authentication regression is resolved, ensuring the popup now properly triggers when connecting to OneDrive accounts. [#17902](https://github.com/open-webui/open-webui/pull/17902), [#17825](https://github.com/open-webui/open-webui/discussions/17825), [#17816](https://github.com/open-webui/open-webui/issues/17816)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.33
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-10-07-8-model-support-changes-in-v0-6-33|8 Model Support changes in v0.6.33]] · Model Support
- [[Changes/Open WebUI/2025-10-07-2-files-and-data-changes-in-v0-6-33|2 Files and Data changes in v0.6.33]] · Files and Data
- [[Changes/Open WebUI/2025-10-07-tab-characters-are-now-preserved-when-pasting-code-or-formatted-text-into-the-ch|⌨️ Tab characters are now preserved when pasting code or formatted text…]] · Editor Experience
- [[Changes/Open WebUI/2025-10-07-2-search-and-browsing-changes-in-v0-6-33|2 Search and Browsing changes in v0.6.33]] · Search and Browsing
- [[Changes/Open WebUI/2025-10-07-6-reliability-and-performance-changes-in-v0-6-33|6 Reliability and Performance changes in v0.6.33]] · Reliability and Performance
- [[Changes/Open WebUI/2025-10-07-redis-session-storage-is-now-available-as-an-experimental-option-for-oauth-authe|🗄️ Redis session storage is now available as an experimental option for OAuth…]] · Account and Access
- [[Changes/Open WebUI/2025-10-07-8-interface-experience-changes-in-v0-6-33|8 Interface Experience changes in v0.6.33]] · Interface Experience
- [[Changes/Open WebUI/2025-10-07-azure-text-to-speech-now-properly-escapes-special-characters-like-ampersands-in|🔊 Azure Text-to-Speech now properly escapes special characters like ampersands…]] · Voice and Audio
- [[Changes/Open WebUI/2025-10-07-3-developer-workflow-changes-in-v0-6-33|3 Developer Workflow changes in v0.6.33]] · Developer Workflow
- [[Changes/Open WebUI/2025-10-07-3-apps-and-integrations-changes-in-v0-6-33|3 Apps and Integrations changes in v0.6.33]] · Apps and Integrations
- [[Changes/Open WebUI/2025-10-07-13-other-changes-in-v0-6-33|13 other changes in v0.6.33]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2025-10-07 · Gemini CLI · [[Changes/Gemini CLI/2025-10-07-for-dynamic-client-registration-use-registration-endpoint-in-config-if-available|For dynamic client registration - use registration endpoint in config if available…]]
- Later: 2025-10-08 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2025-10-08-updated-the-oauth-login-ui-to-begin-polling-as-soon-as-the-device-code-is-genera|Updated the OAuth login UI to begin polling as soon as the device code is generated…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-10-07-2b1bb9&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-10-07-10-account-and-access-changes-in-v0-6-33.md%0ACard%20ID%3A%20open-webui-2025-10-07-2b1bb9%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.33%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->