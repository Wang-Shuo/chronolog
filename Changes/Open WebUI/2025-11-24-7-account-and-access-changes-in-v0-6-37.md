---
card_id: open-webui-2025-11-24-702f0c
date: '2025-11-24'
description: "Open WebUI · 2025-11-24 · Account and Access: 7 changes in v0.6.37 —
  \U0001F512 Password-based authentication can now be fully disabled via \"ENABLE_PASSWORD_AUTH\"…"
diffusion:
  first_in_tracked: "[[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign
    into Notion with your Apple ID \U0001F5DD️ The perfect combination of speedy and
    secure]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1945
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 0e9a136ab3d552c9b092f73cf0b6c82a53a199d0d098c0bac5298b80682f3c27
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-11-24-702f0c
  comparison: ''
  date: '2025-11-24'
  description: 'Open WebUI — v0.6.37: 7 Account and Access changes'
  evidence:
  - quote: "\U0001F512 Password-based authentication can now be fully disabled via
      \"ENABLE_PASSWORD_AUTH\" environment variable, enforcing SSO-only authentication
      and preventing password login fallback when SSO is configured. [#19113](https://github.com/open-webui/open-webui/pull/19113)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: "\U0001F527 MCP OAuth dynamic client registration now automatically detects
      and uses the appropriate token endpoint authentication method from server-supported
      options, enabling compatibility with OAuth servers that only support \"client_secret_basic\"
      instead of \"client_secret_post\". [#19193](https://github.com/open-webui/open-webui/issues/19193)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: "\U0001F527 MCP OAuth server metadata discovery now follows the correct
      specification order, ensuring proper authentication flow compliance. [#19244](https://github.com/open-webui/open-webui/pull/19244)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: "\U0001F513 OAuth role claim parsing now supports both flat and nested
      claim structures, enabling compatibility with OAuth providers that deliver claims
      as direct properties on the user object rather than nested structures. [#19286](https://github.com/open-webui/open-webui/pull/19286)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: "\U0001F511 OAuth MCP server verification now correctly extracts the access
      token value for authorization headers instead of sending the entire token dictionary.
      [#19149](https://github.com/open-webui/open-webui/pull/19149), [#19148](https://github.com/open-webui/open-webui/issues/19148)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: "\U0001F510 OIDC authentication now correctly passes client credentials
      in access token requests, ensuring compatibility with providers that require
      these parameters per RFC 6749. [#19132](https://github.com/open-webui/open-webui/pull/19132),
      [#19131](https://github.com/open-webui/open-webui/issues/19131)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: "\U0001F517 OAuth client creation now respects configured token endpoint
      authentication methods instead of defaulting to basic authentication, preventing
      failures with servers that don't support basic auth. [#19165](https://github.com/open-webui/open-webui/pull/19165)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 7-account-and-access-changes-in-v0-6-37
  source_release: open-webui-2025-11-24-v0-6-37-github-264669867-8b715894
  source_type: github_releases
  theme: account-access
  title: 7 Account and Access changes in v0.6.37
  type: change
related_changes:
- '[[Changes/Codex CLI/2025-11-19-bug-fix-rmcp-client-refresh-oauth-tokens-using-expires-at-6574-laelluo|:bug:
  fix(rmcp-client): refresh OAuth tokens using expires_at (♯6574) — @LaelLuo]]'
- '[[Changes/Replit/2025-11-21-replit-auth-ui-improvements|Replit Auth UI improvements]]'
- '[[Changes/GitHub Copilot CLI/2025-11-24-add-support-for-github-askpass-environment-variable-for-authentication|Add
  support for GITHUB_ASKPASS environment variable for authentication]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-11-24-v0-6-37-github-264669867-8b715894|open-webui-2025-11-24-v0-6-37-github-264669867-8b715894]]'
source_type: github_releases
theme: account-access
title: 7 Account and Access changes in v0.6.37
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Account and Access changes in v0.6.37

**Open WebUI** · 2025-11-24 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.37) · from [[Releases/Open WebUI/open-webui-2025-11-24-v0-6-37-github-264669867-8b715894|v0.6.37]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔒 Password-based authentication can now be fully disabled via "ENABLE_PASSWORD_AUTH" environment variable, enforcing SSO-only authentication and preventing password login fallback when SSO is configured. [#19113](https://github.com/open-webui/open-webui/pull/19113)

> 🔧 MCP OAuth dynamic client registration now automatically detects and uses the appropriate token endpoint authentication method from server-supported options, enabling compatibility with OAuth servers that only support "client_secret_basic" instead of "client_secret_post". [#19193](https://github.com/open-webui/open-webui/issues/19193)

> 🔧 MCP OAuth server metadata discovery now follows the correct specification order, ensuring proper authentication flow compliance. [#19244](https://github.com/open-webui/open-webui/pull/19244)

> 🔓 OAuth role claim parsing now supports both flat and nested claim structures, enabling compatibility with OAuth providers that deliver claims as direct properties on the user object rather than nested structures. [#19286](https://github.com/open-webui/open-webui/pull/19286)

> 🔑 OAuth MCP server verification now correctly extracts the access token value for authorization headers instead of sending the entire token dictionary. [#19149](https://github.com/open-webui/open-webui/pull/19149), [#19148](https://github.com/open-webui/open-webui/issues/19148)

> 🔐 OIDC authentication now correctly passes client credentials in access token requests, ensuring compatibility with providers that require these parameters per RFC 6749. [#19132](https://github.com/open-webui/open-webui/pull/19132), [#19131](https://github.com/open-webui/open-webui/issues/19131)

> 🔗 OAuth client creation now respects configured token endpoint authentication methods instead of defaulting to basic authentication, preventing failures with servers that don't support basic auth. [#19165](https://github.com/open-webui/open-webui/pull/19165)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-11-24-3-search-and-browsing-changes-in-v0-6-37|3 Search and Browsing changes in v0.6.37]] · Search and Browsing
- [[Changes/Open WebUI/2025-11-24-model-cloning-is-now-available-in-admin-settings-allowing-administrators-to-quic|🤖 Model cloning is now available in admin settings, allowing administrators…]] · Model Support
- [[Changes/Open WebUI/2025-11-24-granular-sharing-permissions-are-now-available-with-two-tiered-control-separatin|🔐 Granular sharing permissions are now available with two-tiered control separating…]] · Safety and Privacy
- [[Changes/Open WebUI/2025-11-24-5-interface-experience-changes-in-v0-6-37|5 Interface Experience changes in v0.6.37]] · Interface Experience
- [[Changes/Open WebUI/2025-11-24-granular-import-and-export-permissions-are-now-available-for-workspace-items-int|🔐 Granular import and export permissions are now available for workspace items…]] · Safety and Privacy
- [[Changes/Open WebUI/2025-11-24-prompt-autocompletion-is-now-available-independently-of-the-rich-text-input-sett|✍️ Prompt autocompletion is now available independently of the rich text input…]] · Accessibility and Localization
- [[Changes/Open WebUI/2025-11-24-rag-template-query-placeholder-escaping-logic-was-corrected-to-prevent-unintende|📝 RAG template query placeholder escaping logic was corrected to prevent unintended…]] · Context Window
- [[Changes/Open WebUI/2025-11-24-default-group-assignment-is-now-available-for-new-users-allowing-administrators|👥 Default group assignment is now available for new users, allowing administrators…]] · Model Support
- [[Changes/Open WebUI/2025-11-24-2-voice-and-audio-changes-in-v0-6-37|2 Voice and Audio changes in v0.6.37]] · Voice and Audio
- [[Changes/Open WebUI/2025-11-24-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-11-24-ui-scale-adjustment-is-now-available-in-interface-settings-allowing-users-to-inc|🎨 UI scale adjustment is now available in interface settings, allowing users…]] · Accessibility and Localization
- [[Changes/Open WebUI/2025-11-24-2-files-and-data-changes-in-v0-6-37|2 Files and Data changes in v0.6.37]] · Files and Data
- [[Changes/Open WebUI/2025-11-24-api-key-creation-is-now-controlled-by-granular-user-and-group-permissions-with-t|🔐 API key creation is now controlled by granular user and group permissions…]] · Safety and Privacy
- [[Changes/Open WebUI/2025-11-24-4-image-generation-changes-in-v0-6-37|4 Image Generation changes in v0.6.37]] · Image Generation
- [[Changes/Open WebUI/2025-11-24-websocket-and-redis-configuration-options-are-now-available-including-debug-logg|🔧 WebSocket and Redis configuration options are now available including debug…]] · Developer Workflow
- [[Changes/Open WebUI/2025-11-24-pwa-installations-on-ios-now-properly-refresh-after-server-container-restarts-re|📱 PWA installations on iOS now properly refresh after server container restarts…]] · Mobile and Desktop
- [[Changes/Open WebUI/2025-11-24-11-model-support-changes-in-v0-6-37|11 Model Support changes in v0.6.37]] · Model Support
- [[Changes/Open WebUI/2025-11-24-9-reliability-and-performance-changes-in-v0-6-37|9 Reliability and Performance changes in v0.6.37]] · Reliability and Performance
- [[Changes/Open WebUI/2025-11-24-4-apps-and-integrations-changes-in-v0-6-37|4 Apps and Integrations changes in v0.6.37]] · Apps and Integrations
- [[Changes/Open WebUI/2025-11-24-password-policy-enforcement-is-now-available-with-configurable-validation-rules|🔐 Password policy enforcement is now available with configurable validation rules…]] · Other changes
- [[Changes/Open WebUI/2025-11-24-24-other-changes-in-v0-6-37|24 other changes in v0.6.37]] · Other changes
- [[Changes/Open WebUI/2025-11-24-daily-active-user-metric-is-now-available-for-monitoring-tracking-unique-users-a|📊 Daily active user metric is now available for monitoring, tracking unique users…]] · Other changes
- [[Changes/Open WebUI/2025-11-24-base64-image-conversion-is-now-available-for-markdown-content-in-chat-responses|💨 Base64 image conversion is now available for markdown content in chat responses…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2025-11-24 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2025-11-24-add-support-for-github-askpass-environment-variable-for-authentication|Add support for GITHUB_ASKPASS environment variable for authentication]]
- Later: 2025-11-24 · Open WebUI · [[Changes/Open WebUI/2025-11-24-sso-oidc-code-fixed-to-improve-login-reliability-and-better-handle-edge-cases|🔐 SSO/OIDC code fixed to improve login reliability and better handle edge cases]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Notion · [[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign into Notion with your Apple ID 🗝️ The perfect combination of speedy and secure]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-11-24-702f0c&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-11-24-7-account-and-access-changes-in-v0-6-37.md%0ACard%20ID%3A%20open-webui-2025-11-24-702f0c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.37%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->