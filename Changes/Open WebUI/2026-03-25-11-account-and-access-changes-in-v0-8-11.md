---
card_id: open-webui-2026-03-25-64cc55
date: '2026-03-25'
description: "Open WebUI · 2026-03-25 · Account and Access: 11 changes in v0.8.11
  — \U0001F511 **OIDC authorization parameter injection.** Administrators can now
  inject extra…"
diffusion:
  first_in_tracked: "[[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign
    into Notion with your Apple ID \U0001F5DD️ The perfect combination of speedy and
    secure]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2066
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 3284cf98a982c6b4d12f9c24d3a979a68b6b7b5a4fdb202cc965009e9facdf86
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-03-25-64cc55
  comparison: ''
  date: '2026-03-25'
  description: 'Open WebUI — v0.8.11: 11 Account and Access changes'
  evidence:
  - quote: "\U0001F511 **OIDC authorization parameter injection.** Administrators
      can now inject extra parameters into the OIDC authorization redirect URL via
      the OAUTH_AUTHORIZE_PARAMS environment variable, enabling IdP pre-selection
      for brokers like CILogon and Keycloak. [#22863](https://github.com/open-webui/open-webui/issues/22863),
      [Commit](https://github.com/open-webui/open-webui/commit/69171a4c8bb7f995461b4a2feef194f112b32004)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F511 **Google OAuth session persistence.** Administrators can now
      configure Google OAuth to issue refresh tokens via the GOOGLE_OAUTH_AUTHORIZE_PARAMS
      environment variable, preventing OAuth sessions from expiring after one hour
      and ensuring tools and integrations that rely on OAuth tokens remain functional.
      [#22652](https://github.com/open-webui/open-webui/pull/22652)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F916 **Ollama Anthropic endpoint support.** The Ollama proxy now
      supports the Anthropic-compatible /v1/messages endpoint, allowing clients using
      the Anthropic API format to work through Open WebUI with proper authentication
      and model access controls. [Commit](https://github.com/open-webui/open-webui/commit/f23296b22d3304e5bfcd19151e5802eec55bd98f),
      [#22861](https://github.com/open-webui/open-webui/issues/22861)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F50F **OAuth session persistence.** Users logging in via OAuth or
      OIDC providers now stay logged in for the configured JWT expiry duration instead
      of being logged out when closing the browser. [#22809](https://github.com/open-webui/open-webui/pull/22809)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F6AA **OAuth sub claim configuration crash.** Using the OAUTH_SUB_CLAIM
      environment variable no longer causes crashes during token exchange requests,
      fixing a missing configuration registration. [#22865](https://github.com/open-webui/open-webui/pull/22865)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F50D **OAuth discovery header parsing.** The OAuth protected resource
      discovery now correctly handles both quoted and unquoted values in the WWW-Authenticate
      header, fixing compatibility with MCP servers that return unquoted metadata.
      [#22646](https://github.com/open-webui/open-webui/discussions/22646), [Commit](https://github.com/open-webui/open-webui/commit/fe7e002fea7283abcf901e22de5c8a7d86e336ea)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F464 **Admin OAuth group sync.** Admin user group memberships from
      OAuth and LDAP providers are now properly synced to Open WebUI, fixing a limitation
      where admin role excluded users from group updates. [#22537](https://github.com/open-webui/open-webui/pull/22537),
      [Commit](https://github.com/open-webui/open-webui/commit/a1aceb5f879abd130ef83085d98a0d51316a8fc3)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F50F **OAuth role enforcement.** OAuth role management now properly
      denies access when a user's roles don't match any configured OAUTH_ALLOWED_ROLES
      or OAUTH_ADMIN_ROLES, instead of silently bypassing the restriction. [#13676](https://github.com/open-webui/open-webui/issues/13676),
      [#15551](https://github.com/open-webui/open-webui/issues/15551), [Commit](https://github.com/open-webui/open-webui/commit/6d7744c21903ec5a9ad951770dea76e9ba19cbcc)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F511 **Microsoft Entra ID role claim preservation.** Role claims
      from Microsoft Entra ID tokens are now preserved during OAuth login, fixing
      ENABLE_OAUTH_ROLE_MANAGEMENT for Microsoft OAuth which was previously ignored
      because the userinfo endpoint stripped the roles claim. [#20518](https://github.com/open-webui/open-webui/issues/20518),
      [Commit](https://github.com/open-webui/open-webui/commit/aa2f7fbe5229c3985ce427602069cdeababda481)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F527 **Tool server connection persistence.** Fixed a bug where tool
      server connection updates were not being saved to persistent storage, ensuring
      OAuth client information is now properly preserved. [Commit](https://github.com/open-webui/open-webui/commit/b8ea267f8ec3931de55db7801156b9c07d3ad5f6)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F50C **MCP OAuth tool auto-selection.** MCP tools requiring OAuth
      authentication are now automatically re-selected after completing the auth flow,
      instead of leaving users to manually re-enable the tool on return to the chat.
      [#22994](https://github.com/open-webui/open-webui/issues/22994), [#22995](https://github.com/open-webui/open-webui/pull/22995),
      [Commit](https://github.com/open-webui/open-webui/commit/4d50001c4192c609b1010626ebb6496692823873)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 11-account-and-access-changes-in-v0-8-11
  source_release: open-webui-2026-03-25-v0-8-11-github-301478856-55ceba69
  source_type: github_releases
  theme: account-access
  title: 11 Account and Access changes in v0.8.11
  type: change
related_changes:
- '[[Changes/Microsoft 365 Copilot/2026-03-24-faster-connector-authentication-setup-for-gong-github-and-monday-web-microsoft-3|Faster
  connector authentication setup for Gong, GitHub, and Monday…]]'
- '[[Changes/OpenCode/2026-03-24-added-poe-as-a-built-in-authentication-provider-with-oauth-and-api-key-support|Added
  Poe as a built-in authentication provider with OAuth and API key support]]'
- '[[Changes/Google Antigravity/2026-03-25-improved-mcp-authentication|Improved MCP
  authentication]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-03-25-v0-8-11-github-301478856-55ceba69|open-webui-2026-03-25-v0-8-11-github-301478856-55ceba69]]'
source_type: github_releases
theme: account-access
title: 11 Account and Access changes in v0.8.11
type: change
---

<!-- chronolog:begin region="header" -->
# 11 Account and Access changes in v0.8.11

**Open WebUI** · 2026-03-25 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.11) · from [[Releases/Open WebUI/open-webui-2026-03-25-v0-8-11-github-301478856-55ceba69|v0.8.11]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔑 **OIDC authorization parameter injection.** Administrators can now inject extra parameters into the OIDC authorization redirect URL via the OAUTH_AUTHORIZE_PARAMS environment variable, enabling IdP pre-selection for brokers like CILogon and Keycloak. [#22863](https://github.com/open-webui/open-webui/issues/22863), [Commit](https://github.com/open-webui/open-webui/commit/69171a4c8bb7f995461b4a2feef194f112b32004)

> 🔑 **Google OAuth session persistence.** Administrators can now configure Google OAuth to issue refresh tokens via the GOOGLE_OAUTH_AUTHORIZE_PARAMS environment variable, preventing OAuth sessions from expiring after one hour and ensuring tools and integrations that rely on OAuth tokens remain functional. [#22652](https://github.com/open-webui/open-webui/pull/22652)

> 🤖 **Ollama Anthropic endpoint support.** The Ollama proxy now supports the Anthropic-compatible /v1/messages endpoint, allowing clients using the Anthropic API format to work through Open WebUI with proper authentication and model access controls. [Commit](https://github.com/open-webui/open-webui/commit/f23296b22d3304e5bfcd19151e5802eec55bd98f), [#22861](https://github.com/open-webui/open-webui/issues/22861)

> 🔏 **OAuth session persistence.** Users logging in via OAuth or OIDC providers now stay logged in for the configured JWT expiry duration instead of being logged out when closing the browser. [#22809](https://github.com/open-webui/open-webui/pull/22809)

> 🚪 **OAuth sub claim configuration crash.** Using the OAUTH_SUB_CLAIM environment variable no longer causes crashes during token exchange requests, fixing a missing configuration registration. [#22865](https://github.com/open-webui/open-webui/pull/22865)

> 🔍 **OAuth discovery header parsing.** The OAuth protected resource discovery now correctly handles both quoted and unquoted values in the WWW-Authenticate header, fixing compatibility with MCP servers that return unquoted metadata. [#22646](https://github.com/open-webui/open-webui/discussions/22646), [Commit](https://github.com/open-webui/open-webui/commit/fe7e002fea7283abcf901e22de5c8a7d86e336ea)

> 👤 **Admin OAuth group sync.** Admin user group memberships from OAuth and LDAP providers are now properly synced to Open WebUI, fixing a limitation where admin role excluded users from group updates. [#22537](https://github.com/open-webui/open-webui/pull/22537), [Commit](https://github.com/open-webui/open-webui/commit/a1aceb5f879abd130ef83085d98a0d51316a8fc3)

> 🔏 **OAuth role enforcement.** OAuth role management now properly denies access when a user's roles don't match any configured OAUTH_ALLOWED_ROLES or OAUTH_ADMIN_ROLES, instead of silently bypassing the restriction. [#13676](https://github.com/open-webui/open-webui/issues/13676), [#15551](https://github.com/open-webui/open-webui/issues/15551), [Commit](https://github.com/open-webui/open-webui/commit/6d7744c21903ec5a9ad951770dea76e9ba19cbcc)

> 🔑 **Microsoft Entra ID role claim preservation.** Role claims from Microsoft Entra ID tokens are now preserved during OAuth login, fixing ENABLE_OAUTH_ROLE_MANAGEMENT for Microsoft OAuth which was previously ignored because the userinfo endpoint stripped the roles claim. [#20518](https://github.com/open-webui/open-webui/issues/20518), [Commit](https://github.com/open-webui/open-webui/commit/aa2f7fbe5229c3985ce427602069cdeababda481)

> 🔧 **Tool server connection persistence.** Fixed a bug where tool server connection updates were not being saved to persistent storage, ensuring OAuth client information is now properly preserved. [Commit](https://github.com/open-webui/open-webui/commit/b8ea267f8ec3931de55db7801156b9c07d3ad5f6)

> 🔌 **MCP OAuth tool auto-selection.** MCP tools requiring OAuth authentication are now automatically re-selected after completing the auth flow, instead of leaving users to manually re-enable the tool on return to the chat. [#22994](https://github.com/open-webui/open-webui/issues/22994), [#22995](https://github.com/open-webui/open-webui/pull/22995), [Commit](https://github.com/open-webui/open-webui/commit/4d50001c4192c609b1010626ebb6496692823873)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-03-25-4-editor-experience-changes-in-v0-8-11|4 Editor Experience changes in v0.8.11]] · Editor Experience
- [[Changes/Open WebUI/2026-03-25-rag-query-generation-robustness-the-rag-query-generation-web-search-and-image-ge|🔍 RAG query generation robustness. The RAG query generation, web search…]] · Image Generation
- [[Changes/Open WebUI/2026-03-25-shared-chat-viewing-crash-shared-chats-can-now-be-viewed-by-unauthenticated-user|🐛 Shared chat viewing crash. Shared chats can now be viewed by unauthenticated…]] · Collaboration
- [[Changes/Open WebUI/2026-03-25-3-context-window-changes-in-v0-8-11|3 Context Window changes in v0.8.11]] · Context Window
- [[Changes/Open WebUI/2026-03-25-2-search-and-browsing-changes-in-v0-8-11|2 Search and Browsing changes in v0.8.11]] · Search and Browsing
- [[Changes/Open WebUI/2026-03-25-2-files-and-data-changes-in-v0-8-11|2 Files and Data changes in v0.8.11]] · Files and Data
- [[Changes/Open WebUI/2026-03-25-4-memory-and-personalization-changes-in-v0-8-11|4 Memory and Personalization changes in v0.8.11]] · Memory and Personalization
- [[Changes/Open WebUI/2026-03-25-3-apps-and-integrations-changes-in-v0-8-11|3 Apps and Integrations changes in v0.8.11]] · Apps and Integrations
- [[Changes/Open WebUI/2026-03-25-17-interface-experience-changes-in-v0-8-11|17 Interface Experience changes in v0.8.11]] · Interface Experience
- [[Changes/Open WebUI/2026-03-25-5-reliability-and-performance-changes-in-v0-8-11|5 Reliability and Performance changes in v0.8.11]] · Reliability and Performance
- [[Changes/Open WebUI/2026-03-25-tool-binary-response-handling-tool-servers-can-now-return-binary-data-such-as-im|🏮 Tool binary response handling. Tool servers can now return binary data such…]] · Multimodal Input
- [[Changes/Open WebUI/2026-03-25-23-model-support-changes-in-v0-8-11|23 Model Support changes in v0.8.11]] · Model Support
- [[Changes/Open WebUI/2026-03-25-4-safety-and-privacy-changes-in-v0-8-11|4 Safety and Privacy changes in v0.8.11]] · Safety and Privacy
- [[Changes/Open WebUI/2026-03-25-34-developer-workflow-changes-in-v0-8-11|34 Developer Workflow changes in v0.8.11]] · Developer Workflow
- [[Changes/Open WebUI/2026-03-25-metrics-export-interval-configuration-administrators-can-now-control-opentelemet|📊 Metrics export interval configuration. Administrators can now control…]] · Pricing Model
- [[Changes/Open WebUI/2026-03-25-19-other-changes-in-v0-8-11|19 other changes in v0.8.11]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-03-25 · Google Antigravity · [[Changes/Google Antigravity/2026-03-25-improved-mcp-authentication|Improved MCP authentication]]
- Later: 2026-03-26 · Claude Code · [[Changes/Claude Code/2026-03-26-mcp-oauth-now-follows-rfc-9728-protected-resource-metadata-discovery-to-find-the|MCP OAuth now follows RFC 9728 Protected Resource Metadata discovery to find…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Notion · [[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign into Notion with your Apple ID 🗝️ The perfect combination of speedy and secure]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-03-25-64cc55&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-03-25-11-account-and-access-changes-in-v0-8-11.md%0ACard%20ID%3A%20open-webui-2026-03-25-64cc55%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.11%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->