---
card_id: open-webui-2026-02-12-8b6204
date: '2026-02-12'
description: "Open WebUI · 2026-02-12 · Account and Access: 6 changes in v0.8.0 —
  \U0001F511 **OAuth token exchange.** Administrators can now enable OAuth token exchange
  via…"
diffusion:
  first_in_tracked: "[[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign
    into Notion with your Apple ID \U0001F5DD️ The perfect combination of speedy and
    secure]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2025
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 890bd0dcff549bfdcb538845153e7f4949837781bf6260d43c72609b4ed74805
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-02-12-8b6204
  comparison: ''
  date: '2026-02-12'
  description: 'Open WebUI — v0.8.0: 6 Account and Access changes'
  evidence:
  - quote: "\U0001F511 **OAuth token exchange.** Administrators can now enable OAuth
      token exchange via \"ENABLE_OAUTH_TOKEN_EXCHANGE\", allowing external applications
      to authenticate users by exchanging OAuth provider tokens for Open WebUI session
      tokens. [Commit](https://github.com/open-webui/open-webui/commit/655420fd25ed0ea872954baa485030079c00c10e)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F511 **Faster authentication.** User authentication is now 34% faster
      by combining database lookups into a single query. [#21010](https://github.com/open-webui/open-webui/pull/21010)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F6AB **LDAP authentication hang fix.** LDAP authentication no longer
      freezes the entire service when logging in with non-existent accounts, preventing
      application hangs. [Commit](https://github.com/open-webui/open-webui/commit/a4281f6a7fbc9764b57830e4ef81bb780aa34af9),
      [#21300](https://github.com/open-webui/open-webui/issues/21300)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: ✅ **Trusted Header auto-registration fix.** Trusted Header Authentication
      now properly auto-registers new users after the first login, assigning the configured
      default role instead of failing for users not yet in the database. [Commit](https://github.com/open-webui/open-webui/commit/9b30e8f6894c8c8bad0a9ce4693eab810962adc9)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F511 **Docling API key fix.** Docling API key authentication now
      works correctly by using the proper \"X-Api-Key\" header format instead of the
      incorrect \"Bearer\" authorization prefix. [#20652](https://github.com/open-webui/open-webui/pull/20652)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F50C **MCP OAuth 2.1 fix.** MCP OAuth 2.1 authentication now works
      correctly, resolving connection verification failures and 401 errors during
      the authorization callback. [#20808](https://github.com/open-webui/open-webui/issues/20808),
      [#20828](https://github.com/open-webui/open-webui/issues/20828), [Commit](https://github.com/open-webui/open-webui/commit/8eebc2aea63b7045e61c9689a65a2dfa9c797bcb)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 6-account-and-access-changes-in-v0-8-0
  source_release: open-webui-2026-02-12-v0-8-0-github-285910626-490914ba
  source_type: github_releases
  theme: account-access
  title: 6 Account and Access changes in v0.8.0
  type: change
related_changes:
- '[[Changes/v0/2026-02-11-added-sso-page-for-team-specific-authentication|Added SSO
  page for team-specific authentication]]'
- '[[Changes/Cline/2026-02-12-2-account-and-access-changes-in-v3-58-0|2 Account and
  Access changes in v3.58.0]]'
- '[[Changes/Codex CLI/2026-02-12-11521-test-app-server-stabilize-app-list-thread-feature-flag-test-by-using-file|♯11521
  test(app-server): stabilize app/list thread feature-flag test by using…]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-02-12-v0-8-0-github-285910626-490914ba|open-webui-2026-02-12-v0-8-0-github-285910626-490914ba]]'
source_type: github_releases
theme: account-access
title: 6 Account and Access changes in v0.8.0
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Account and Access changes in v0.8.0

**Open WebUI** · 2026-02-12 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.0) · from [[Releases/Open WebUI/open-webui-2026-02-12-v0-8-0-github-285910626-490914ba|v0.8.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔑 **OAuth token exchange.** Administrators can now enable OAuth token exchange via "ENABLE_OAUTH_TOKEN_EXCHANGE", allowing external applications to authenticate users by exchanging OAuth provider tokens for Open WebUI session tokens. [Commit](https://github.com/open-webui/open-webui/commit/655420fd25ed0ea872954baa485030079c00c10e)

> 🔑 **Faster authentication.** User authentication is now 34% faster by combining database lookups into a single query. [#21010](https://github.com/open-webui/open-webui/pull/21010)

> 🚫 **LDAP authentication hang fix.** LDAP authentication no longer freezes the entire service when logging in with non-existent accounts, preventing application hangs. [Commit](https://github.com/open-webui/open-webui/commit/a4281f6a7fbc9764b57830e4ef81bb780aa34af9), [#21300](https://github.com/open-webui/open-webui/issues/21300)

> ✅ **Trusted Header auto-registration fix.** Trusted Header Authentication now properly auto-registers new users after the first login, assigning the configured default role instead of failing for users not yet in the database. [Commit](https://github.com/open-webui/open-webui/commit/9b30e8f6894c8c8bad0a9ce4693eab810962adc9)

> 🔑 **Docling API key fix.** Docling API key authentication now works correctly by using the proper "X-Api-Key" header format instead of the incorrect "Bearer" authorization prefix. [#20652](https://github.com/open-webui/open-webui/pull/20652)

> 🔌 **MCP OAuth 2.1 fix.** MCP OAuth 2.1 authentication now works correctly, resolving connection verification failures and 401 errors during the authorization callback. [#20808](https://github.com/open-webui/open-webui/issues/20808), [#20828](https://github.com/open-webui/open-webui/issues/20828), [Commit](https://github.com/open-webui/open-webui/commit/8eebc2aea63b7045e61c9689a65a2dfa9c797bcb)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-02-12-16-reliability-and-performance-changes-in-v0-8-0|16 Reliability and Performance changes in v0.8.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-02-12-audio-service-timeout-handling-audio-transcription-and-text-to-speech-requests-n|🔌 Audio service timeout handling. Audio transcription and text-to-speech…]] · Voice and Audio
- [[Changes/Open WebUI/2026-02-12-2-editor-experience-changes-in-v0-8-0|2 Editor Experience changes in v0.8.0]] · Editor Experience
- [[Changes/Open WebUI/2026-02-12-5-safety-and-privacy-changes-in-v0-8-0|5 Safety and Privacy changes in v0.8.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-02-12-19-model-support-changes-in-v0-8-0|19 Model Support changes in v0.8.0]] · Model Support
- [[Changes/Open WebUI/2026-02-12-27-developer-workflow-changes-in-v0-8-0|27 Developer Workflow changes in v0.8.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-02-12-5-context-window-changes-in-v0-8-0|5 Context Window changes in v0.8.0]] · Context Window
- [[Changes/Open WebUI/2026-02-12-2-image-generation-changes-in-v0-8-0|2 Image Generation changes in v0.8.0]] · Image Generation
- [[Changes/Open WebUI/2026-02-12-2-memory-and-personalization-changes-in-v0-8-0|2 Memory and Personalization changes in v0.8.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-02-12-gboard-multi-line-paste-fix-multi-line-text-pasted-from-gboard-on-android-now-in|📱 Gboard multi-line paste fix. Multi-line text pasted from Gboard on Android now…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-02-12-2-collaboration-changes-in-v0-8-0|2 Collaboration changes in v0.8.0]] · Collaboration
- [[Changes/Open WebUI/2026-02-12-async-pipeline-operations-pipeline-operations-now-run-asynchronously-instead-of|🔧 Async pipeline operations. Pipeline operations now run asynchronously instead…]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-02-12-5-search-and-browsing-changes-in-v0-8-0|5 Search and Browsing changes in v0.8.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-02-12-8-interface-experience-changes-in-v0-8-0|8 Interface Experience changes in v0.8.0]] · Interface Experience
- [[Changes/Open WebUI/2026-02-12-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-02-12-screen-reader-accessibility-screen-reader-users-now-hear-the-password-field-labe|♿ Screen reader accessibility. Screen reader users now hear the password field…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-02-12-10-files-and-data-changes-in-v0-8-0|10 Files and Data changes in v0.8.0]] · Files and Data
- [[Changes/Open WebUI/2026-02-12-6-apps-and-integrations-changes-in-v0-8-0|6 Apps and Integrations changes in v0.8.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-02-12-29-other-changes-in-v0-8-0|29 other changes in v0.8.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-02-12 · Codex CLI · [[Changes/Codex CLI/2026-02-12-11521-test-app-server-stabilize-app-list-thread-feature-flag-test-by-using-file|♯11521 test(app-server): stabilize app/list thread feature-flag test by using…]]
- Later: 2026-02-12 · OpenCode · [[Changes/OpenCode/2026-02-12-desktop-normalize-oauth-error-messages|Desktop Normalize OAuth error messages]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Notion · [[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign into Notion with your Apple ID 🗝️ The perfect combination of speedy and secure]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-02-12-8b6204&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-02-12-6-account-and-access-changes-in-v0-8-0.md%0ACard%20ID%3A%20open-webui-2026-02-12-8b6204%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->