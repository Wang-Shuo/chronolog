---
card_id: open-webui-2026-06-29-b0062f
date: '2026-06-29'
description: "Open WebUI · 2026-06-29 · Account and Access: 9 changes in v0.10.0 —
  \U0001F510 **Configure authentication from the admin panel.** LDAP and OAuth/OIDC
  settings now have…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1187
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8b3b569613196acc6bd090eeb0a8d87d53f25a8f1f26d3868a9094c1997ecbd2
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-06-29-b0062f
  comparison: ''
  date: '2026-06-29'
  description: 'Open WebUI — v0.10.0: 9 Account and Access changes'
  evidence:
  - quote: "\U0001F510 **Configure authentication from the admin panel.** LDAP and
      OAuth/OIDC settings now have a dedicated Authentication settings page, so providers
      can be configured from the admin interface. [Commit](https://github.com/open-webui/open-webui/commit/5cdcdbaeec9fc8156721c38c33ec37956962871c),
      [#12945](https://github.com/open-webui/open-webui/pull/12945)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F5C4️ **AWS RDS IAM database authentication.** The database connection
      can now authenticate using AWS RDS IAM tokens through a new opt-in setting,
      instead of only a static password. [Commit](https://github.com/open-webui/open-webui/commit/c0c6c2181a8dc57b62e8a5eabd550bf89db7ffed),
      [#23580](https://github.com/open-webui/open-webui/pull/23580)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F512 **Restrict OAuth scopes requested from MCP servers.** A new
      setting lets administrators limit which OAuth scopes Open WebUI requests when
      connecting to MCP servers. [Commit](https://github.com/open-webui/open-webui/commit/7be009649a0a94008484335c492ab0af18fde41f),
      [#25981](https://github.com/open-webui/open-webui/pull/25981), [#25978](https://github.com/open-webui/open-webui/issues/25978)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: ⏱️ **Login timing no longer reveals which accounts exist.** Sign-in now
      takes the same amount of time whether or not an account exists, removing a timing
      difference that could be used to discover valid accounts. [Commit](https://github.com/open-webui/open-webui/commit/993e74912199c66c522f08ec81abe31d76985e39),
      [Commit](https://github.com/open-webui/open-webui/commit/7b29834d4216e5db70b68f3598fa1ad654d3512b)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F5BC️ **OAuth profile pictures are validated.** Profile picture
      URLs from OAuth providers are now validated and their type checked when stored,
      preventing unsafe image sources. [Commit](https://github.com/open-webui/open-webui/commit/eb53281c9acb3660e09554a8dbde0a0b42646b70),
      [#24548](https://github.com/open-webui/open-webui/pull/24548)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F511 **Expired sessions return you to sign-in.** When a request
      fails because your session has expired, Open WebUI now redirects you to the
      sign-in page instead of leaving you on a broken view. [Commit](https://github.com/open-webui/open-webui/commit/5922727402593900758d84004f950071c701f6de),
      [#26237](https://github.com/open-webui/open-webui/pull/26237)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F517 **Broader MCP server compatibility for OAuth.** Open WebUI
      now discovers an MCP server's protected resource metadata even when the server
      doesn't advertise it, and recognizes more OAuth preflight variations, so more
      MCP servers connect. [#25980](https://github.com/open-webui/open-webui/pull/25980),
      [#25954](https://github.com/open-webui/open-webui/issues/25954), [Commit](https://github.com/open-webui/open-webui/commit/45fea34bd0c8ce54b0822499c40e3e6964220354),
      [#26068](https://github.com/open-webui/open-webui/pull/26068)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F4D0 **Long default group names don't overflow.** A long default
      group name no longer overflows its row in the admin authentication settings.
      [#25685](https://github.com/open-webui/open-webui/pull/25685)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F5C2️ **Authentication settings moved to their own page.** LDAP,
      OAuth, and related authentication settings have moved out of the General settings
      page into a dedicated Authentication page in the admin panel. [Commit](https://github.com/open-webui/open-webui/commit/5cdcdbaeec9fc8156721c38c33ec37956962871c)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 9-account-and-access-changes-in-v0-10-0
  source_release: open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01
  source_type: github_releases
  theme: account-access
  title: 9 Account and Access changes in v0.10.0
  type: change
related_changes:
- '[[Changes/Dify/2026-06-25-5-account-and-access-changes-in-1-15-0|5 Account and
  Access changes in 1.15.0]]'
- '[[Changes/v0/2026-06-26-3-account-and-access-changes-in-platform-api-v2-mcp-chat-tools|3
  Account and Access changes in Platform API v2, MCP chat tools…]]'
- "[[Changes/Open WebUI/2026-06-29-shared-folder-read-only-chats-no-longer-sign-users-out-opening-or-reading-chats|\U0001F91D
  Shared folder read-only chats no longer sign users out. Opening or reading…]]"
source_release: '[[Releases/Open WebUI/open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01|open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01]]'
source_type: github_releases
theme: account-access
title: 9 Account and Access changes in v0.10.0
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Account and Access changes in v0.10.0

**Open WebUI** · 2026-06-29 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.10.0) · from [[Releases/Open WebUI/open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01|v0.10.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔐 **Configure authentication from the admin panel.** LDAP and OAuth/OIDC settings now have a dedicated Authentication settings page, so providers can be configured from the admin interface. [Commit](https://github.com/open-webui/open-webui/commit/5cdcdbaeec9fc8156721c38c33ec37956962871c), [#12945](https://github.com/open-webui/open-webui/pull/12945)

> 🗄️ **AWS RDS IAM database authentication.** The database connection can now authenticate using AWS RDS IAM tokens through a new opt-in setting, instead of only a static password. [Commit](https://github.com/open-webui/open-webui/commit/c0c6c2181a8dc57b62e8a5eabd550bf89db7ffed), [#23580](https://github.com/open-webui/open-webui/pull/23580)

> 🔒 **Restrict OAuth scopes requested from MCP servers.** A new setting lets administrators limit which OAuth scopes Open WebUI requests when connecting to MCP servers. [Commit](https://github.com/open-webui/open-webui/commit/7be009649a0a94008484335c492ab0af18fde41f), [#25981](https://github.com/open-webui/open-webui/pull/25981), [#25978](https://github.com/open-webui/open-webui/issues/25978)

> ⏱️ **Login timing no longer reveals which accounts exist.** Sign-in now takes the same amount of time whether or not an account exists, removing a timing difference that could be used to discover valid accounts. [Commit](https://github.com/open-webui/open-webui/commit/993e74912199c66c522f08ec81abe31d76985e39), [Commit](https://github.com/open-webui/open-webui/commit/7b29834d4216e5db70b68f3598fa1ad654d3512b)

> 🖼️ **OAuth profile pictures are validated.** Profile picture URLs from OAuth providers are now validated and their type checked when stored, preventing unsafe image sources. [Commit](https://github.com/open-webui/open-webui/commit/eb53281c9acb3660e09554a8dbde0a0b42646b70), [#24548](https://github.com/open-webui/open-webui/pull/24548)

> 🔑 **Expired sessions return you to sign-in.** When a request fails because your session has expired, Open WebUI now redirects you to the sign-in page instead of leaving you on a broken view. [Commit](https://github.com/open-webui/open-webui/commit/5922727402593900758d84004f950071c701f6de), [#26237](https://github.com/open-webui/open-webui/pull/26237)

> 🔗 **Broader MCP server compatibility for OAuth.** Open WebUI now discovers an MCP server's protected resource metadata even when the server doesn't advertise it, and recognizes more OAuth preflight variations, so more MCP servers connect. [#25980](https://github.com/open-webui/open-webui/pull/25980), [#25954](https://github.com/open-webui/open-webui/issues/25954), [Commit](https://github.com/open-webui/open-webui/commit/45fea34bd0c8ce54b0822499c40e3e6964220354), [#26068](https://github.com/open-webui/open-webui/pull/26068)

> 📐 **Long default group names don't overflow.** A long default group name no longer overflows its row in the admin authentication settings. [#25685](https://github.com/open-webui/open-webui/pull/25685)

> 🗂️ **Authentication settings moved to their own page.** LDAP, OAuth, and related authentication settings have moved out of the General settings page into a dedicated Authentication page in the admin panel. [Commit](https://github.com/open-webui/open-webui/commit/5cdcdbaeec9fc8156721c38c33ec37956962871c)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-06-29-5-files-and-data-changes-in-v0-10-0|5 Files and Data changes in v0.10.0]] · Files and Data
- [[Changes/Open WebUI/2026-06-29-5-memory-and-personalization-changes-in-v0-10-0|5 Memory and Personalization changes in v0.10.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-06-29-3-voice-and-audio-changes-in-v0-10-0|3 Voice and Audio changes in v0.10.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-06-29-14-interface-experience-changes-in-v0-10-0|14 Interface Experience changes in v0.10.0]] · Interface Experience
- [[Changes/Open WebUI/2026-06-29-4-collaboration-changes-in-v0-10-0|4 Collaboration changes in v0.10.0]] · Collaboration
- [[Changes/Open WebUI/2026-06-29-client-user-agent-forwarded-to-model-backends-the-browser-s-user-agent-is-now-pa|🪪 Client User-Agent forwarded to model backends. The browser's User-Agent is now…]] · Agent Mode
- [[Changes/Open WebUI/2026-06-29-scim-sync-can-t-demote-an-admin-a-scim-provisioning-sync-that-marks-a-user-inact|🛟 SCIM sync can't demote an admin. A SCIM provisioning sync that marks a user…]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-06-29-8-search-and-browsing-changes-in-v0-10-0|8 Search and Browsing changes in v0.10.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-06-29-25-model-support-changes-in-v0-10-0|25 Model Support changes in v0.10.0]] · Model Support
- [[Changes/Open WebUI/2026-06-29-6-reliability-and-performance-changes-in-v0-10-0|6 Reliability and Performance changes in v0.10.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-06-29-4-mobile-and-desktop-changes-in-v0-10-0|4 Mobile and Desktop changes in v0.10.0]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-06-29-better-screen-reader-labels-on-toggles-integration-and-switch-toggles-now-expose|♿ Better screen-reader labels on toggles. Integration and switch toggles now…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-06-29-16-safety-and-privacy-changes-in-v0-10-0|16 Safety and Privacy changes in v0.10.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-06-29-2-pricing-model-changes-in-v0-10-0|2 Pricing Model changes in v0.10.0]] · Pricing Model
- [[Changes/Open WebUI/2026-06-29-7-apps-and-integrations-changes-in-v0-10-0|7 Apps and Integrations changes in v0.10.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-06-29-usable-chat-input-on-mobile-with-many-tools-when-skills-tools-terminal-web-searc|📱 Usable chat input on mobile with many tools. When skills, tools, terminal, web…]] · Image Generation
- [[Changes/Open WebUI/2026-06-29-6-automation-and-scheduling-changes-in-v0-10-0|6 Automation and Scheduling changes in v0.10.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-06-29-3-context-window-changes-in-v0-10-0|3 Context Window changes in v0.10.0]] · Context Window
- [[Changes/Open WebUI/2026-06-29-42-developer-workflow-changes-in-v0-10-0|42 Developer Workflow changes in v0.10.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-06-29-10-editor-experience-changes-in-v0-10-0|10 Editor Experience changes in v0.10.0]] · Editor Experience
- [[Changes/Open WebUI/2026-06-29-29-other-changes-in-v0-10-0|29 other changes in v0.10.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-06-29 · Open WebUI · [[Changes/Open WebUI/2026-06-29-shared-folder-read-only-chats-no-longer-sign-users-out-opening-or-reading-chats|🤝 Shared folder read-only chats no longer sign users out. Opening or reading…]]
- Later: 2026-06-30 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-06-30-mcp-oauth-against-microsoft-entra-servers-behind-a-tenant-vanity-domain-e-g-copi|MCP OAuth against Microsoft Entra servers behind a tenant vanity domain…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-06-29-b0062f&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-06-29-9-account-and-access-changes-in-v0-10-0.md%0ACard%20ID%3A%20open-webui-2026-06-29-b0062f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.10.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->