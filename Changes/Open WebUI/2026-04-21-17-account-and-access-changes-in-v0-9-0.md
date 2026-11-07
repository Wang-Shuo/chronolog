---
card_id: open-webui-2026-04-21-f1237d
date: '2026-04-21'
description: "Open WebUI · 2026-04-21 · Account and Access: 17 changes in v0.9.0 —
  \U0001F3AB **Static OAuth tool authentication.** Tool server authentication now
  works reliably for…"
diffusion:
  first_in_tracked: "[[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign
    into Notion with your Apple ID \U0001F5DD️ The perfect combination of speedy and
    secure]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2093
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 44a25f8feaeaa792ee2aa9407de3434b17d63d1d1697e52e0d333875a93f5318
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-04-21-f1237d
  comparison: ''
  date: '2026-04-21'
  description: 'Open WebUI — v0.9.0: 17 Account and Access changes'
  evidence:
  - quote: "\U0001F3AB **Static OAuth tool authentication.** Tool server authentication
      now works reliably for both \"oauth_2.1\" and \"oauth_2.1_static\" connection
      types, so OAuth-backed tool access is correctly detected and forwarded during
      chat requests. [Commit](https://github.com/open-webui/open-webui/commit/60676bfdcfbce1a69b3e97f2013f0cfd63371737)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F6AA **Back-channel logout.** OpenID Connect providers can now trigger
      centralized logout through the \"ENABLE_OAUTH_BACKCHANNEL_LOGOUT\" setting,
      helping administrators invalidate user sessions more reliably across connected
      devices. [Commit](https://github.com/open-webui/open-webui/commit/0dd9f462ffb2f160bc4aebad182047f41874d250)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F510 **OAuth 2.1 PKCE enforcement.** OAuth 2.1 providers now default
      to S256 PKCE even when discovery metadata omits supported challenge methods,
      preventing login failures with providers that require PKCE by default. [#23667](https://github.com/open-webui/open-webui/issues/23667),
      [Commit](https://github.com/open-webui/open-webui/commit/050c4b97a95addc5eaeef86ba00631673a90dec4)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F510 **Static OAuth scope handling.** Static OAuth credential flows
      now prioritize administrator-defined scopes and handle OAuth 2.1 static flow
      behavior more reliably. [Commit](https://github.com/open-webui/open-webui/commit/349ea4ea9e577f2cbfb4917ef5f52e5ac53c5b70),
      [#23668](https://github.com/open-webui/open-webui/issues/23668), [#23696](https://github.com/open-webui/open-webui/pull/23696),
      [#23783](https://github.com/open-webui/open-webui/pull/23783)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F510 **Static OAuth tool registration reliability.** Static OAuth
      tool server registration now resolves and uses saved admin credentials more
      reliably, preventing registration failures when valid client credentials are
      provided. [#23670](https://github.com/open-webui/open-webui/issues/23670), [Commit](https://github.com/open-webui/open-webui/commit/2943955c529138c0e530fd07b6333a0052e3684e),
      [Commit](https://github.com/open-webui/open-webui/commit/c767bcaa739f76b1a4337dfd9d6be47adb504825)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: ⏳ **OAuth token expiry fallback.** OAuth sessions now always store a safe
      expiry value even when providers omit "expires_in" or "expires_at", so token
      refresh checks continue working and tool calls are less likely to fail later
      with unexpected authorization errors. [#23669](https://github.com/open-webui/open-webui/issues/23669),
      [Commit](https://github.com/open-webui/open-webui/commit/31406caa795173a59d5843d3601b891bf617cbaa)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F511 **Open Terminal MCP authentication.** Open Terminal MCP tool
      calls now include the configured API key when calling internal routes, preventing
      unauthorized errors for commands like file reads and command execution. [#106](https://github.com/open-webui/open-terminal/pull/106)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F511 **OIDC key-rotation recovery.** OIDC login now retries token
      authorization with refreshed provider signing keys after a bad-signature failure,
      so logins recover automatically after identity-provider key rotation without
      requiring a service restart. [#23582](https://github.com/open-webui/open-webui/issues/23582),
      [Commit](https://github.com/open-webui/open-webui/commit/facb194a07486e847f0725a0a839e99b5864d37b)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F6AB **LDAP empty-password rejection.** LDAP login now rejects empty
      or whitespace-only passwords before bind attempts, preventing unauthenticated
      simple-bind behavior from granting access on permissive LDAP server configurations.
      [#23633](https://github.com/open-webui/open-webui/pull/23633)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F465 **First-user admin race protection.** Concurrent first-time
      LDAP or OAuth registrations can no longer create multiple admin accounts, so
      only the true first account is promoted during initial setup. [#23626](https://github.com/open-webui/open-webui/pull/23626)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F512 **SCIM token checks.** SCIM authentication now compares tokens
      in a safer way, helping prevent timing-based token guessing attacks. [#23577](https://github.com/open-webui/open-webui/pull/23577)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F6AA **OAuth redirect URI reliability.** OAuth login redirects now
      use provider client metadata more consistently, preventing incorrect HTTP callback
      URLs behind reverse proxies and improving sign-in reliability for providers
      such as Feishu. [#23203](https://github.com/open-webui/open-webui/pull/23203),
      [#23128](https://github.com/open-webui/open-webui/issues/23128)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F310 **OAuth redirect handling.** OAuth provider token exchange
      now follows redirects automatically, improving sign-in reliability with identity
      providers that redirect token endpoint requests. [#23409](https://github.com/open-webui/open-webui/issues/23409),
      [Commit](https://github.com/open-webui/open-webui/commit/498ff8cdc3dd47000cdc60e5adcf36f4adfbe07d)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: ☁️ **OneDrive picker redirect handling.** OneDrive file picker authentication
      now uses the current app origin as the redirect URI, improving sign-in reliability
      when launching the picker from deployed environments. [#23450](https://github.com/open-webui/open-webui/issues/23450),
      [Commit](https://github.com/open-webui/open-webui/commit/21cc8281323d505d7d084cc496bd433063315c86)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F36A **OAuth session cookie persistence.** OIDC sign-in now correctly
      sets the \"oauth_session_id\" cookie, so \"system_oauth\" connections can forward
      user OAuth tokens to upstream providers as expected. [#23251](https://github.com/open-webui/open-webui/pull/23251),
      [#23250](https://github.com/open-webui/open-webui/issues/23250)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F511 **OAuth session cookie handling.** OAuth callback processing
      no longer fails on undefined cookie expiry data, so OAuth session cookies are
      stored correctly after sign-in. [#23207](https://github.com/open-webui/open-webui/pull/23207),
      [#23197](https://github.com/open-webui/open-webui/issues/23197)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F6E1️ **OAuth avatar URL validation.** OAuth sign-in now validates
      profile picture URLs before fetching them, preventing invalid image links from
      causing login-time errors. [#23356](https://github.com/open-webui/open-webui/pull/23356)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 17-account-and-access-changes-in-v0-9-0
  source_release: open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a
  source_type: github_releases
  theme: account-access
  title: 17 Account and Access changes in v0.9.0
  type: change
related_changes:
- '[[Changes/OpenCode/2026-04-15-2-account-and-access-changes-in-v1-4-4|2 Account
  and Access changes in v1.4.4]]'
- '[[Changes/OpenCode/2026-04-16-core-workspaces-now-receive-your-auth-context-so-provider-sign-in-carries-across|Core
  Workspaces now receive your auth context, so provider sign-in carries across…]]'
- '[[Changes/GitHub Copilot CLI/2026-04-17-copilot-login-host-now-correctly-authenticates-with-github-enterprise-cloud-ghe|copilot
  login --host now correctly authenticates with GitHub Enterprise Cloud (GHE)…]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a|open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a]]'
source_type: github_releases
theme: account-access
title: 17 Account and Access changes in v0.9.0
type: change
---

<!-- chronolog:begin region="header" -->
# 17 Account and Access changes in v0.9.0

**Open WebUI** · 2026-04-21 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.0) · from [[Releases/Open WebUI/open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a|v0.9.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🎫 **Static OAuth tool authentication.** Tool server authentication now works reliably for both "oauth_2.1" and "oauth_2.1_static" connection types, so OAuth-backed tool access is correctly detected and forwarded during chat requests. [Commit](https://github.com/open-webui/open-webui/commit/60676bfdcfbce1a69b3e97f2013f0cfd63371737)

> 🚪 **Back-channel logout.** OpenID Connect providers can now trigger centralized logout through the "ENABLE_OAUTH_BACKCHANNEL_LOGOUT" setting, helping administrators invalidate user sessions more reliably across connected devices. [Commit](https://github.com/open-webui/open-webui/commit/0dd9f462ffb2f160bc4aebad182047f41874d250)

> 🔐 **OAuth 2.1 PKCE enforcement.** OAuth 2.1 providers now default to S256 PKCE even when discovery metadata omits supported challenge methods, preventing login failures with providers that require PKCE by default. [#23667](https://github.com/open-webui/open-webui/issues/23667), [Commit](https://github.com/open-webui/open-webui/commit/050c4b97a95addc5eaeef86ba00631673a90dec4)

> 🔐 **Static OAuth scope handling.** Static OAuth credential flows now prioritize administrator-defined scopes and handle OAuth 2.1 static flow behavior more reliably. [Commit](https://github.com/open-webui/open-webui/commit/349ea4ea9e577f2cbfb4917ef5f52e5ac53c5b70), [#23668](https://github.com/open-webui/open-webui/issues/23668), [#23696](https://github.com/open-webui/open-webui/pull/23696), [#23783](https://github.com/open-webui/open-webui/pull/23783)

> 🔐 **Static OAuth tool registration reliability.** Static OAuth tool server registration now resolves and uses saved admin credentials more reliably, preventing registration failures when valid client credentials are provided. [#23670](https://github.com/open-webui/open-webui/issues/23670), [Commit](https://github.com/open-webui/open-webui/commit/2943955c529138c0e530fd07b6333a0052e3684e), [Commit](https://github.com/open-webui/open-webui/commit/c767bcaa739f76b1a4337dfd9d6be47adb504825)

> ⏳ **OAuth token expiry fallback.** OAuth sessions now always store a safe expiry value even when providers omit "expires_in" or "expires_at", so token refresh checks continue working and tool calls are less likely to fail later with unexpected authorization errors. [#23669](https://github.com/open-webui/open-webui/issues/23669), [Commit](https://github.com/open-webui/open-webui/commit/31406caa795173a59d5843d3601b891bf617cbaa)

> 🔑 **Open Terminal MCP authentication.** Open Terminal MCP tool calls now include the configured API key when calling internal routes, preventing unauthorized errors for commands like file reads and command execution. [#106](https://github.com/open-webui/open-terminal/pull/106)

> 🔑 **OIDC key-rotation recovery.** OIDC login now retries token authorization with refreshed provider signing keys after a bad-signature failure, so logins recover automatically after identity-provider key rotation without requiring a service restart. [#23582](https://github.com/open-webui/open-webui/issues/23582), [Commit](https://github.com/open-webui/open-webui/commit/facb194a07486e847f0725a0a839e99b5864d37b)

> 🚫 **LDAP empty-password rejection.** LDAP login now rejects empty or whitespace-only passwords before bind attempts, preventing unauthenticated simple-bind behavior from granting access on permissive LDAP server configurations. [#23633](https://github.com/open-webui/open-webui/pull/23633)

> 👥 **First-user admin race protection.** Concurrent first-time LDAP or OAuth registrations can no longer create multiple admin accounts, so only the true first account is promoted during initial setup. [#23626](https://github.com/open-webui/open-webui/pull/23626)

> 🔒 **SCIM token checks.** SCIM authentication now compares tokens in a safer way, helping prevent timing-based token guessing attacks. [#23577](https://github.com/open-webui/open-webui/pull/23577)

> 🚪 **OAuth redirect URI reliability.** OAuth login redirects now use provider client metadata more consistently, preventing incorrect HTTP callback URLs behind reverse proxies and improving sign-in reliability for providers such as Feishu. [#23203](https://github.com/open-webui/open-webui/pull/23203), [#23128](https://github.com/open-webui/open-webui/issues/23128)

> 🌐 **OAuth redirect handling.** OAuth provider token exchange now follows redirects automatically, improving sign-in reliability with identity providers that redirect token endpoint requests. [#23409](https://github.com/open-webui/open-webui/issues/23409), [Commit](https://github.com/open-webui/open-webui/commit/498ff8cdc3dd47000cdc60e5adcf36f4adfbe07d)

> ☁️ **OneDrive picker redirect handling.** OneDrive file picker authentication now uses the current app origin as the redirect URI, improving sign-in reliability when launching the picker from deployed environments. [#23450](https://github.com/open-webui/open-webui/issues/23450), [Commit](https://github.com/open-webui/open-webui/commit/21cc8281323d505d7d084cc496bd433063315c86)

> 🍪 **OAuth session cookie persistence.** OIDC sign-in now correctly sets the "oauth_session_id" cookie, so "system_oauth" connections can forward user OAuth tokens to upstream providers as expected. [#23251](https://github.com/open-webui/open-webui/pull/23251), [#23250](https://github.com/open-webui/open-webui/issues/23250)

> 🔑 **OAuth session cookie handling.** OAuth callback processing no longer fails on undefined cookie expiry data, so OAuth session cookies are stored correctly after sign-in. [#23207](https://github.com/open-webui/open-webui/pull/23207), [#23197](https://github.com/open-webui/open-webui/issues/23197)

> 🛡️ **OAuth avatar URL validation.** OAuth sign-in now validates profile picture URLs before fetching them, preventing invalid image links from causing login-time errors. [#23356](https://github.com/open-webui/open-webui/pull/23356)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-04-21-3-files-and-data-changes-in-v0-9-0|3 Files and Data changes in v0.9.0]] · Files and Data
- [[Changes/Open WebUI/2026-04-21-4-image-generation-changes-in-v0-9-0|4 Image Generation changes in v0.9.0]] · Image Generation
- [[Changes/Open WebUI/2026-04-21-28-model-support-changes-in-v0-9-0|28 Model Support changes in v0.9.0]] · Model Support
- [[Changes/Open WebUI/2026-04-21-5-editor-experience-changes-in-v0-9-0|5 Editor Experience changes in v0.9.0]] · Editor Experience
- [[Changes/Open WebUI/2026-04-21-persistent-chat-payload-efficiency-persisted-chats-now-use-server-side-history-l|🚀 Persistent chat payload efficiency. Persisted chats now use server-side…]] · Multimodal Input
- [[Changes/Open WebUI/2026-04-21-8-context-window-changes-in-v0-9-0|8 Context Window changes in v0.9.0]] · Context Window
- [[Changes/Open WebUI/2026-04-21-24-reliability-and-performance-changes-in-v0-9-0|24 Reliability and Performance changes in v0.9.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-04-21-4-apps-and-integrations-changes-in-v0-9-0|4 Apps and Integrations changes in v0.9.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-04-21-46-developer-workflow-changes-in-v0-9-0|46 Developer Workflow changes in v0.9.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-04-21-8-automation-and-scheduling-changes-in-v0-9-0|8 Automation and Scheduling changes in v0.9.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-04-21-7-memory-and-personalization-changes-in-v0-9-0|7 Memory and Personalization changes in v0.9.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-04-21-2-mobile-and-desktop-changes-in-v0-9-0|2 Mobile and Desktop changes in v0.9.0]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-04-21-17-interface-experience-changes-in-v0-9-0|17 Interface Experience changes in v0.9.0]] · Interface Experience
- [[Changes/Open WebUI/2026-04-21-11-safety-and-privacy-changes-in-v0-9-0|11 Safety and Privacy changes in v0.9.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-04-21-4-search-and-browsing-changes-in-v0-9-0|4 Search and Browsing changes in v0.9.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-04-21-shared-chat-access-controls-you-can-now-control-who-has-access-to-a-shared-chat|🔗 Shared chat access controls. You can now control who has access to a shared…]] · Collaboration
- [[Changes/Open WebUI/2026-04-21-4-voice-and-audio-changes-in-v0-9-0|4 Voice and Audio changes in v0.9.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-04-21-21-other-changes-in-v0-9-0|21 other changes in v0.9.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-04-17 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-04-17-copilot-login-host-now-correctly-authenticates-with-github-enterprise-cloud-ghe|copilot login --host now correctly authenticates with GitHub Enterprise Cloud (GHE)…]]
- Later: 2026-04-22 · ChatGPT · [[Changes/ChatGPT/2026-04-22-we-re-launching-chatgpt-for-clinicians-a-free-version-of-chatgpt-for-verified-cl|ChatGPT for Clinicians]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Notion · [[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign into Notion with your Apple ID 🗝️ The perfect combination of speedy and secure]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-04-21-f1237d&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-04-21-17-account-and-access-changes-in-v0-9-0.md%0ACard%20ID%3A%20open-webui-2026-04-21-f1237d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->