---
card_id: open-webui-2025-12-02-1fa562
date: '2025-12-02'
description: "Open WebUI · 2025-12-02 · Account and Access: 7 changes in v0.6.41 —
  \U0001F6A6 Sign-in rate limiting was implemented to protect against brute force
  attacks, limiting…"
diffusion:
  first_in_tracked: "[[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign
    into Notion with your Apple ID \U0001F5DD️ The perfect combination of speedy and
    secure]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1953
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f08292eca9082cf20e8fa04738ab04e8510d9f34ca9ec195d65e0258d6d2921e
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-12-02-1fa562
  comparison: ''
  date: '2025-12-02'
  description: 'Open WebUI — v0.6.41: 7 Account and Access changes'
  evidence:
  - quote: "\U0001F6A6 Sign-in rate limiting was implemented to protect against brute
      force attacks, limiting login attempts to 15 per 3-minute window per email address
      using Redis with automatic fallback to in-memory storage when Redis is unavailable.
      [Commit](https://github.com/open-webui/open-webui/commit/7b166370432414ce8f186747fb098e0c70fb2d6b)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: "\U0001F511 The admin user edit modal now displays OAuth identity information
      with a per-provider breakdown, showing each linked identity provider and its
      associated subject identifier separately. [#19573](https://github.com/open-webui/open-webui/pull/19573)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: "\U0001F9E9 OAuth role claim parsing now respects the \"OAUTH_ROLES_SEPARATOR\"
      configuration, enabling proper parsing of roles returned as comma-separated
      strings and providing consistent behavior with group claim handling. [#19514](https://github.com/open-webui/open-webui/pull/19514)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: "\U0001F465 Default group assignment now applies consistently across all
      user registration methods including OAuth/SSO, LDAP, and admin-created users,
      fixing an issue where the \"DEFAULT_GROUP_ID\" setting was only being applied
      to users who signed up via the email/password signup form. [#19685](https://github.com/open-webui/open-webui/pull/19685)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: "\U0001F3F7️ OAuth group assignment now updates correctly on first login
      when users transition from admin to user role, ensuring group memberships reflect
      immediately when group management is enabled. [#19475](https://github.com/open-webui/open-webui/issues/19475),
      [#19476](https://github.com/open-webui/open-webui/pull/19476)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: "\U0001F575️♂️ Audit logging was fixed by correctly awaiting the async
      user authentication call, resolving failures where coroutine objects were passed
      instead of user data. [#19658](https://github.com/open-webui/open-webui/pull/19658),
      [Commit](https://github.com/open-webui/open-webui/commit/dba86bc)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: "\U0001F5C2️ The user table was restructured with API keys migrated to
      a dedicated table supporting future multi-key functionality, OAuth data storage
      converted to a JSON structure enabling multiple identity providers per user
      account, and internal column types optimized from TEXT to JSON for the \"info\"
      and \"settings\" fields, with automatic migration preserving all existing data
      and associations. [#19573](https://github.com/open-webui/open-webui/pull/19573)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 7-account-and-access-changes-in-v0-6-41
  source_release: open-webui-2025-12-02-v0-6-41-github-266904152-3dfc9f25
  source_type: github_releases
  theme: account-access
  title: 7 Account and Access changes in v0.6.41
  type: change
related_changes:
- '[[Changes/Lovable/2025-11-26-temporary-education-logins|Temporary education logins]]'
- '[[Changes/Raycast/2025-11-27-authentication-removed-the-required-login-step-before-getting-started|Authentication
  : Removed the required login step before getting started]]'
- '[[Changes/Codex CLI/2025-12-02-feat-support-login-as-an-option-on-shell-tool-mcp-by-bolinfest-in-7120|feat:
  support login as an option on shell-tool-mcp by @bolinfest in ♯7120]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-12-02-v0-6-41-github-266904152-3dfc9f25|open-webui-2025-12-02-v0-6-41-github-266904152-3dfc9f25]]'
source_type: github_releases
theme: account-access
title: 7 Account and Access changes in v0.6.41
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Account and Access changes in v0.6.41

**Open WebUI** · 2025-12-02 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.41) · from [[Releases/Open WebUI/open-webui-2025-12-02-v0-6-41-github-266904152-3dfc9f25|v0.6.41]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🚦 Sign-in rate limiting was implemented to protect against brute force attacks, limiting login attempts to 15 per 3-minute window per email address using Redis with automatic fallback to in-memory storage when Redis is unavailable. [Commit](https://github.com/open-webui/open-webui/commit/7b166370432414ce8f186747fb098e0c70fb2d6b)

> 🔑 The admin user edit modal now displays OAuth identity information with a per-provider breakdown, showing each linked identity provider and its associated subject identifier separately. [#19573](https://github.com/open-webui/open-webui/pull/19573)

> 🧩 OAuth role claim parsing now respects the "OAUTH_ROLES_SEPARATOR" configuration, enabling proper parsing of roles returned as comma-separated strings and providing consistent behavior with group claim handling. [#19514](https://github.com/open-webui/open-webui/pull/19514)

> 👥 Default group assignment now applies consistently across all user registration methods including OAuth/SSO, LDAP, and admin-created users, fixing an issue where the "DEFAULT_GROUP_ID" setting was only being applied to users who signed up via the email/password signup form. [#19685](https://github.com/open-webui/open-webui/pull/19685)

> 🏷️ OAuth group assignment now updates correctly on first login when users transition from admin to user role, ensuring group memberships reflect immediately when group management is enabled. [#19475](https://github.com/open-webui/open-webui/issues/19475), [#19476](https://github.com/open-webui/open-webui/pull/19476)

> 🕵️♂️ Audit logging was fixed by correctly awaiting the async user authentication call, resolving failures where coroutine objects were passed instead of user data. [#19658](https://github.com/open-webui/open-webui/pull/19658), [Commit](https://github.com/open-webui/open-webui/commit/dba86bc)

> 🗂️ The user table was restructured with API keys migrated to a dedicated table supporting future multi-key functionality, OAuth data storage converted to a JSON structure enabling multiple identity providers per user account, and internal column types optimized from TEXT to JSON for the "info" and "settings" fields, with automatic migration preserving all existing data and associations. [#19573](https://github.com/open-webui/open-webui/pull/19573)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-12-02-group-channels-were-introduced-as-a-new-channel-type-enabling-membership-based-c|👥 Group channels were introduced as a new channel type enabling membership-based…]] · Collaboration
- [[Changes/Open WebUI/2025-12-02-web-search-domain-filtering-was-corrected-to-properly-block-results-when-any-res|🛡️ Web search domain filtering was corrected to properly block results when any…]] · Search and Browsing
- [[Changes/Open WebUI/2025-12-02-tool-call-response-token-duplication-was-fixed-by-removing-redundant-message-his|🔄 Tool call response token duplication was fixed by removing redundant message…]] · Context Window
- [[Changes/Open WebUI/2025-12-02-13-developer-workflow-changes-in-v0-6-41|13 Developer Workflow changes in v0.6.41]] · Developer Workflow
- [[Changes/Open WebUI/2025-12-02-4-reliability-and-performance-changes-in-v0-6-41|4 Reliability and Performance changes in v0.6.41]] · Reliability and Performance
- [[Changes/Open WebUI/2025-12-02-2-safety-and-privacy-changes-in-v0-6-41|2 Safety and Privacy changes in v0.6.41]] · Safety and Privacy
- [[Changes/Open WebUI/2025-12-02-the-model-editor-interface-was-refined-with-access-control-settings-moved-to-a-d|🎨 The model editor interface was refined with access control settings moved…]] · Editor Experience
- [[Changes/Open WebUI/2025-12-02-9-model-support-changes-in-v0-6-41|9 Model Support changes in v0.6.41]] · Model Support
- [[Changes/Open WebUI/2025-12-02-image-generation-in-temporary-chats-was-fixed-by-correctly-handling-local-chat-s|🎨 Image generation in temporary chats was fixed by correctly handling local chat…]] · Image Generation
- [[Changes/Open WebUI/2025-12-02-2-enterprise-and-administration-changes-in-v0-6-41|2 Enterprise and Administration changes in v0.6.41]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-12-02-sentencetransformers-embedding-initialization-was-fixed-by-updating-the-transfor|🐍 SentenceTransformers embedding initialization was fixed by updating…]] · Files and Data
- [[Changes/Open WebUI/2025-12-02-11-interface-experience-changes-in-v0-6-41|11 Interface Experience changes in v0.6.41]] · Interface Experience
- [[Changes/Open WebUI/2025-12-02-2-apps-and-integrations-changes-in-v0-6-41|2 Apps and Integrations changes in v0.6.41]] · Apps and Integrations
- [[Changes/Open WebUI/2025-12-02-13-other-changes-in-v0-6-41|13 other changes in v0.6.41]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2025-12-02 · Codex CLI · [[Changes/Codex CLI/2025-12-02-feat-support-login-as-an-option-on-shell-tool-mcp-by-bolinfest-in-7120|feat: support login as an option on shell-tool-mcp by @bolinfest in ♯7120]]
- Later: 2025-12-08 · ElevenLabs · [[Changes/ElevenLabs/2025-12-08-webhook-tools|Webhook Tools]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Notion · [[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign into Notion with your Apple ID 🗝️ The perfect combination of speedy and secure]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-12-02-1fa562&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-12-02-7-account-and-access-changes-in-v0-6-41.md%0ACard%20ID%3A%20open-webui-2025-12-02-1fa562%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.41%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->