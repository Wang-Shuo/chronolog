---
card_id: open-webui-2026-10-10-5ca25d
date: '2026-10-10'
description: "Open WebUI · 2026-10-10 · Account and Access: 19 changes in v0.12.0
  — \U0001F50F **Two-factor sign-in.** Administrators can require an authenticator
  app for every user…"
diffusion:
  first_in_tracked: "[[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign
    into Notion with your Apple ID \U0001F5DD️ The perfect combination of speedy and
    secure]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2265
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 6b94333051d8399b947bf27b5805ae76d3eb52f643514961e8d827dcaf0afa5a
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-10-10-5ca25d
  comparison: ''
  date: '2026-10-10'
  description: 'Open WebUI — v0.12.0: 19 Account and Access changes'
  evidence:
  - quote: "\U0001F50F **Two-factor sign-in.** Administrators can require an authenticator
      app for every user under Admin Settings > Authentication, or with \"ENABLE_MFA\",
      so users set one up from a QR code on their next sign-in, get ten single-use
      recovery codes, and can later replace their authenticator or create new recovery
      codes in their account settings; OAuth and trusted-header sign-ins can be let
      through without it with \"MFA_ALLOW_OAUTH_BYPASS\" and \"MFA_ALLOW_TRUSTED_HEADER_BYPASS\",
      and the \"open-webui mfa reset\" command gives a user who lost their authenticator
      a one-time recovery token. [Commit](https://github.com/open-webui/open-webui/commit/24e30d1cbdaab624dfe20f479f805e6791cf0226)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F194 **MCP Connection ID filled in from the name.** When adding
      an MCP tool server, the ID field is now labeled Connection ID and filled in
      from the server name, so it no longer has to be typed before saving or registering
      an OAuth client, and importing a connection keeps its ID. [Commit](https://github.com/open-webui/open-webui/commit/079647f1425ef80be5a330bf1b2c4158d66c8340)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F529 **MCP tools listed in the chat tools dialog.** Expanding an
      MCP tool server in the tools dialog of the chat input now loads and lists its
      tools with their descriptions and a tool count, offers Reconnect when the server
      needs you to sign in again, and only shows the tool servers selected for the
      chat. [Commit](https://github.com/open-webui/open-webui/commit/fb741ebcd2daed626405f9458c192e5161bce4c0)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F3AB **Login check when loading the app settings.** Loading the
      app's settings now uses the same login check as every other request, so a session
      that is no longer valid only gets the logged-out settings. [#31621](https://github.com/open-webui/open-webui/pull/31621)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: ⛓️ **Live connections end with the session.** A browser's live connection
      is now checked every 30 seconds and closed once its sign-in has been revoked
      or has expired, where it kept receiving updates. [Commit](https://github.com/open-webui/open-webui/commit/24e30d1cbdaab624dfe20f479f805e6791cf0226)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F910 **Sign-in requests kept out of the audit log.** With request
      auditing on, the bodies of authentication and OAuth requests and their responses,
      such as sign-in, password changes and API key creation, are no longer written
      to the audit log. [Commit](https://github.com/open-webui/open-webui/commit/24e30d1cbdaab624dfe20f479f805e6791cf0226)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001FAAA **Token exchange group mapping.** With OAuth group mapping
      on, signing in through token exchange now assigns groups from the token's own
      groups claim when the provider's user info leaves it out, as it already did
      for roles. [Commit](https://github.com/open-webui/open-webui/commit/f412538756f745b531036840bc0a153e62b0f003)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F511 **OAuth sessions survive parallel requests.** Chatting through
      a connection that forwards your single sign-on token no longer logs your OAuth
      session out when two requests renew an expiring token at once against a provider
      that rotates refresh tokens, including requests handled by different workers
      or replicas sharing Redis, which previously cost every following request its
      token until you signed in again. [#30426](https://github.com/open-webui/open-webui/pull/30426),
      [#30450](https://github.com/open-webui/open-webui/pull/30450), [#30416](https://github.com/open-webui/open-webui/issues/30416)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F9F1 **Blocked OAuth groups not created.** With automatic group
      creation on, groups matching \"OAUTH_BLOCKED_GROUPS\" are no longer created
      at sign-in, where a provider sending a user's full directory membership could
      fill the groups list with thousands of empty groups. [#31316](https://github.com/open-webui/open-webui/pull/31316),
      [#29558](https://github.com/open-webui/open-webui/issues/29558)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F999 **Ollama connection headers and sign-in everywhere.** An Ollama
      connection's custom headers, authentication type and cookie forwarding now apply
      to every request, including checking the connection, loading, uploading, downloading
      and unloading models and the Manage Ollama dialog, so Ollama servers behind
      gateways such as Cloudflare Access work throughout and no key is sent when the
      authentication type is None, which also applies to unloading models from llama.cpp
      connections. [Commit](https://github.com/open-webui/open-webui/commit/bc2416c5db5f5268de0f97730c5a51f55018837a),
      [#29868](https://github.com/open-webui/open-webui/issues/29868), [#31489](https://github.com/open-webui/open-webui/pull/31489),
      [#31487](https://github.com/open-webui/open-webui/issues/31487), [#31490](https://github.com/open-webui/open-webui/pull/31490)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F510 **MCP OAuth scopes.** MCP tool servers using OAuth with dynamic
      client registration, such as Atlassian and Notion, now receive the scopes they
      need so tool calls work after connecting, and connections set up earlier recover
      them without registering again. [#30384](https://github.com/open-webui/open-webui/pull/30384),
      [#29967](https://github.com/open-webui/open-webui/issues/29967)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F6E0️ **Refused authentication settings.** When the server refuses
      a value on the admin authentication page, such as a JWT expiration without a
      time unit, the page now shows the value actually stored instead of the refused
      one. [#30433](https://github.com/open-webui/open-webui/pull/30433), [#30293](https://github.com/open-webui/open-webui/issues/30293)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001FAAA **Clear message for failed SSO sign-ins.** When signing in
      through an OAuth or OIDC provider fails, for example because access was denied,
      the account has no email or its email domain is not allowed, the login page
      now says the sign-in with the identity provider failed, where it claimed the
      email or password was wrong; the exact reason still goes to the server log.
      [#31629](https://github.com/open-webui/open-webui/pull/31629), [#31627](https://github.com/open-webui/open-webui/issues/31627)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F511 **Google MCP connections stay signed in.** MCP tool servers
      that sign in through Google, such as Google's Gmail, Drive and Calendar servers,
      now receive a refresh token, so the connection renews itself instead of being
      dropped about an hour after signing in; existing connections pick this up at
      the next sign-in. [#31395](https://github.com/open-webui/open-webui/pull/31395),
      [#28319](https://github.com/open-webui/open-webui/issues/28319)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F68F **Shared chat links while signed out.** Opening a shared chat
      link while signed out now leads to the login page and back to the shared chat
      after signing in, including with OAuth, where it showed a blank home page. [#31337](https://github.com/open-webui/open-webui/pull/31337),
      [#31334](https://github.com/open-webui/open-webui/issues/31334)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4B2 **Dollar signs in saved code blocks.** Saving an edited code
      block now keeps \"$$\" and other dollar sign patterns as written, where each
      pair turned into a single dollar sign in the chat and in later messages. [#31386](https://github.com/open-webui/open-webui/pull/31386),
      [#31385](https://github.com/open-webui/open-webui/issues/31385)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F36A **MCP OAuth sign-in with long scope lists.** Connecting an
      MCP tool server over OAuth 2.1 no longer fails with an \"invalid or expired
      state\" error after signing in when the server asks for many scopes, such as
      the Google Workspace MCP server, as the session cookie no longer grows past
      the browser's size limit. [#31894](https://github.com/open-webui/open-webui/pull/31894),
      [#26382](https://github.com/open-webui/open-webui/issues/26382)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F5FA️ **MCP servers without OAuth discovery.** Connecting to an
      MCP server over OAuth 2.1 now works when the server publishes no discovery documents,
      using the standard /authorize, /token and /register addresses on the server's
      own domain, where the connection was refused because no sign-in address could
      be found. [Commit](https://github.com/open-webui/open-webui/commit/a0e606bfaa48e64bfe8cfc905d96f1da5a0b1bc9),
      [#26647](https://github.com/open-webui/open-webui/issues/26647)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F39F️ **Tool servers using your sign-in token after it renews.**
      MCP and OpenAPI tool servers set to use the signed-in user's OAuth token now
      pick up the current token for every call and retry once when it was renewed
      in the meantime, where tool calls kept sending the old token after a refresh
      and failed, and MCP servers now also get the token in automations and API requests
      without a browser session. [Commit](https://github.com/open-webui/open-webui/commit/93fc3fcb726f81d9ccca45245e476c4944ff30ba),
      [#31863](https://github.com/open-webui/open-webui/issues/31863)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 19-account-and-access-changes-in-v0-12-0
  source_release: open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b
  source_type: github_releases
  theme: account-access
  title: 19 Account and Access changes in v0.12.0
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-10-08-2-account-and-access-changes-in-v2026-9-9|2 Account
  and Access changes in v2026.9.9]]'
- '[[Changes/Claude Code/2026-10-09-improved-the-errors-for-a-refused-cloud-session-they-now-say-why-your-organizati|Improved
  the errors for a refused cloud session]]'
- '[[Changes/GitHub Copilot CLI/2026-10-09-use-native-microsoft-entra-broker-authentication-on-macos-when-available-with-br|Use
  native Microsoft Entra broker authentication on macOS when available…]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b|open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b]]'
source_type: github_releases
theme: account-access
title: 19 Account and Access changes in v0.12.0
type: change
---

<!-- chronolog:begin region="header" -->
# 19 Account and Access changes in v0.12.0

**Open WebUI** · 2026-10-10 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.0) · from [[Releases/Open WebUI/open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b|v0.12.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔏 **Two-factor sign-in.** Administrators can require an authenticator app for every user under Admin Settings > Authentication, or with "ENABLE_MFA", so users set one up from a QR code on their next sign-in, get ten single-use recovery codes, and can later replace their authenticator or create new recovery codes in their account settings; OAuth and trusted-header sign-ins can be let through without it with "MFA_ALLOW_OAUTH_BYPASS" and "MFA_ALLOW_TRUSTED_HEADER_BYPASS", and the "open-webui mfa reset" command gives a user who lost their authenticator a one-time recovery token. [Commit](https://github.com/open-webui/open-webui/commit/24e30d1cbdaab624dfe20f479f805e6791cf0226)

> 🆔 **MCP Connection ID filled in from the name.** When adding an MCP tool server, the ID field is now labeled Connection ID and filled in from the server name, so it no longer has to be typed before saving or registering an OAuth client, and importing a connection keeps its ID. [Commit](https://github.com/open-webui/open-webui/commit/079647f1425ef80be5a330bf1b2c4158d66c8340)

> 🔩 **MCP tools listed in the chat tools dialog.** Expanding an MCP tool server in the tools dialog of the chat input now loads and lists its tools with their descriptions and a tool count, offers Reconnect when the server needs you to sign in again, and only shows the tool servers selected for the chat. [Commit](https://github.com/open-webui/open-webui/commit/fb741ebcd2daed626405f9458c192e5161bce4c0)

> 🎫 **Login check when loading the app settings.** Loading the app's settings now uses the same login check as every other request, so a session that is no longer valid only gets the logged-out settings. [#31621](https://github.com/open-webui/open-webui/pull/31621)

> ⛓️ **Live connections end with the session.** A browser's live connection is now checked every 30 seconds and closed once its sign-in has been revoked or has expired, where it kept receiving updates. [Commit](https://github.com/open-webui/open-webui/commit/24e30d1cbdaab624dfe20f479f805e6791cf0226)

> 🤐 **Sign-in requests kept out of the audit log.** With request auditing on, the bodies of authentication and OAuth requests and their responses, such as sign-in, password changes and API key creation, are no longer written to the audit log. [Commit](https://github.com/open-webui/open-webui/commit/24e30d1cbdaab624dfe20f479f805e6791cf0226)

> 🪪 **Token exchange group mapping.** With OAuth group mapping on, signing in through token exchange now assigns groups from the token's own groups claim when the provider's user info leaves it out, as it already did for roles. [Commit](https://github.com/open-webui/open-webui/commit/f412538756f745b531036840bc0a153e62b0f003)

> 🔑 **OAuth sessions survive parallel requests.** Chatting through a connection that forwards your single sign-on token no longer logs your OAuth session out when two requests renew an expiring token at once against a provider that rotates refresh tokens, including requests handled by different workers or replicas sharing Redis, which previously cost every following request its token until you signed in again. [#30426](https://github.com/open-webui/open-webui/pull/30426), [#30450](https://github.com/open-webui/open-webui/pull/30450), [#30416](https://github.com/open-webui/open-webui/issues/30416)

> 🧱 **Blocked OAuth groups not created.** With automatic group creation on, groups matching "OAUTH_BLOCKED_GROUPS" are no longer created at sign-in, where a provider sending a user's full directory membership could fill the groups list with thousands of empty groups. [#31316](https://github.com/open-webui/open-webui/pull/31316), [#29558](https://github.com/open-webui/open-webui/issues/29558)

> 🦙 **Ollama connection headers and sign-in everywhere.** An Ollama connection's custom headers, authentication type and cookie forwarding now apply to every request, including checking the connection, loading, uploading, downloading and unloading models and the Manage Ollama dialog, so Ollama servers behind gateways such as Cloudflare Access work throughout and no key is sent when the authentication type is None, which also applies to unloading models from llama.cpp connections. [Commit](https://github.com/open-webui/open-webui/commit/bc2416c5db5f5268de0f97730c5a51f55018837a), [#29868](https://github.com/open-webui/open-webui/issues/29868), [#31489](https://github.com/open-webui/open-webui/pull/31489), [#31487](https://github.com/open-webui/open-webui/issues/31487), [#31490](https://github.com/open-webui/open-webui/pull/31490)

> 🔐 **MCP OAuth scopes.** MCP tool servers using OAuth with dynamic client registration, such as Atlassian and Notion, now receive the scopes they need so tool calls work after connecting, and connections set up earlier recover them without registering again. [#30384](https://github.com/open-webui/open-webui/pull/30384), [#29967](https://github.com/open-webui/open-webui/issues/29967)

> 🛠️ **Refused authentication settings.** When the server refuses a value on the admin authentication page, such as a JWT expiration without a time unit, the page now shows the value actually stored instead of the refused one. [#30433](https://github.com/open-webui/open-webui/pull/30433), [#30293](https://github.com/open-webui/open-webui/issues/30293)

> 🪪 **Clear message for failed SSO sign-ins.** When signing in through an OAuth or OIDC provider fails, for example because access was denied, the account has no email or its email domain is not allowed, the login page now says the sign-in with the identity provider failed, where it claimed the email or password was wrong; the exact reason still goes to the server log. [#31629](https://github.com/open-webui/open-webui/pull/31629), [#31627](https://github.com/open-webui/open-webui/issues/31627)

> 🔑 **Google MCP connections stay signed in.** MCP tool servers that sign in through Google, such as Google's Gmail, Drive and Calendar servers, now receive a refresh token, so the connection renews itself instead of being dropped about an hour after signing in; existing connections pick this up at the next sign-in. [#31395](https://github.com/open-webui/open-webui/pull/31395), [#28319](https://github.com/open-webui/open-webui/issues/28319)

> 🚏 **Shared chat links while signed out.** Opening a shared chat link while signed out now leads to the login page and back to the shared chat after signing in, including with OAuth, where it showed a blank home page. [#31337](https://github.com/open-webui/open-webui/pull/31337), [#31334](https://github.com/open-webui/open-webui/issues/31334)

> 💲 **Dollar signs in saved code blocks.** Saving an edited code block now keeps "$$" and other dollar sign patterns as written, where each pair turned into a single dollar sign in the chat and in later messages. [#31386](https://github.com/open-webui/open-webui/pull/31386), [#31385](https://github.com/open-webui/open-webui/issues/31385)

> 🍪 **MCP OAuth sign-in with long scope lists.** Connecting an MCP tool server over OAuth 2.1 no longer fails with an "invalid or expired state" error after signing in when the server asks for many scopes, such as the Google Workspace MCP server, as the session cookie no longer grows past the browser's size limit. [#31894](https://github.com/open-webui/open-webui/pull/31894), [#26382](https://github.com/open-webui/open-webui/issues/26382)

> 🗺️ **MCP servers without OAuth discovery.** Connecting to an MCP server over OAuth 2.1 now works when the server publishes no discovery documents, using the standard /authorize, /token and /register addresses on the server's own domain, where the connection was refused because no sign-in address could be found. [Commit](https://github.com/open-webui/open-webui/commit/a0e606bfaa48e64bfe8cfc905d96f1da5a0b1bc9), [#26647](https://github.com/open-webui/open-webui/issues/26647)

> 🎟️ **Tool servers using your sign-in token after it renews.** MCP and OpenAPI tool servers set to use the signed-in user's OAuth token now pick up the current token for every call and retry once when it was renewed in the meantime, where tool calls kept sending the old token after a refresh and failed, and MCP servers now also get the token in automations and API requests without a browser session. [Commit](https://github.com/open-webui/open-webui/commit/93fc3fcb726f81d9ccca45245e476c4944ff30ba), [#31863](https://github.com/open-webui/open-webui/issues/31863)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-10-10-5-reliability-and-performance-changes-in-v0-12-0|5 Reliability and Performance changes in v0.12.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-10-10-5-enterprise-and-administration-changes-in-v0-12-0|5 Enterprise and Administration changes in v0.12.0]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-10-10-7-apps-and-integrations-changes-in-v0-12-0|7 Apps and Integrations changes in v0.12.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-10-10-12-voice-and-audio-changes-in-v0-12-0|12 Voice and Audio changes in v0.12.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-10-10-27-developer-workflow-changes-in-v0-12-0|27 Developer Workflow changes in v0.12.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-10-10-5-image-generation-changes-in-v0-12-0|5 Image Generation changes in v0.12.0]] · Image Generation
- [[Changes/Open WebUI/2026-10-10-49-model-support-changes-in-v0-12-0|49 Model Support changes in v0.12.0]] · Model Support
- [[Changes/Open WebUI/2026-10-10-10-automation-and-scheduling-changes-in-v0-12-0|10 Automation and Scheduling changes in v0.12.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-10-10-3-mobile-and-desktop-changes-in-v0-12-0|3 Mobile and Desktop changes in v0.12.0]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-10-10-6-files-and-data-changes-in-v0-12-0|6 Files and Data changes in v0.12.0]] · Files and Data
- [[Changes/Open WebUI/2026-10-10-13-collaboration-changes-in-v0-12-0|13 Collaboration changes in v0.12.0]] · Collaboration
- [[Changes/Open WebUI/2026-10-10-2-memory-and-personalization-changes-in-v0-12-0|2 Memory and Personalization changes in v0.12.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-10-10-5-context-window-changes-in-v0-12-0|5 Context Window changes in v0.12.0]] · Context Window
- [[Changes/Open WebUI/2026-10-10-18-interface-experience-changes-in-v0-12-0|18 Interface Experience changes in v0.12.0]] · Interface Experience
- [[Changes/Open WebUI/2026-10-10-7-agent-mode-changes-in-v0-12-0|7 Agent Mode changes in v0.12.0]] · Agent Mode
- [[Changes/Open WebUI/2026-10-10-6-safety-and-privacy-changes-in-v0-12-0|6 Safety and Privacy changes in v0.12.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-10-10-21-editor-experience-changes-in-v0-12-0|21 Editor Experience changes in v0.12.0]] · Editor Experience
- [[Changes/Open WebUI/2026-10-10-4-search-and-browsing-changes-in-v0-12-0|4 Search and Browsing changes in v0.12.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-10-10-68-other-changes-in-v0-12-0|68 other changes in v0.12.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-10-09 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-10-09-use-native-microsoft-entra-broker-authentication-on-macos-when-available-with-br|Use native Microsoft Entra broker authentication on macOS when available…]]
- Later: 2026-10-10 · OpenClaw · [[Changes/OpenClaw/2026-10-10-18-account-and-access-changes-in-v2026-10-1|18 Account and Access changes in v2026.10.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Notion · [[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign into Notion with your Apple ID 🗝️ The perfect combination of speedy and secure]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-10-5ca25d&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-10-19-account-and-access-changes-in-v0-12-0.md%0ACard%20ID%3A%20open-webui-2026-10-10-5ca25d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->