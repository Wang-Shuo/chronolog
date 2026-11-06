---
card_id: open-webui-2025-08-21-dd6362
date: '2025-08-21'
description: "Open WebUI · 2025-08-21 · Account and Access: 3 changes in v0.6.23 —
  \U0001F510 **Enhanced OAuth Role Claim Handling**: Improved compatibility with diverse
  OAuth…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 875
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: cc2a1a37814c461dcf7ec194ce4a162fbf695c0b1f3419016459df16feb57abc
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-08-21-dd6362
  comparison: ''
  date: '2025-08-21'
  description: 'Open WebUI — v0.6.23: 3 Account and Access changes'
  evidence:
  - quote: "\U0001F510 **Enhanced OAuth Role Claim Handling**: Improved compatibility
      with diverse OAuth providers by allowing role claims to be supplied as single
      strings or integers, in addition to arrays. The system now automatically normalizes
      these single-value claims into arrays for consistent processing, streamlining
      integration with identity providers that format role data differently."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  - quote: "\U0001F6E1️ **Resolved Critical OIDC SSO Login Failure**: Fixed a critical
      issue where OIDC Single Sign-On (SSO) logins failed due to an error in setting
      the authentication token as a cookie during the redirect process. This ensures
      reliable and seamless authentication for users utilizing OIDC providers, restoring
      full login functionality that was impacted by previous security hardening."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  - quote: "\U0001F510 **Resolved OAUTH_GROUPS_CLAIM Configuration Issue**: Fixed
      a bug where the \"OAUTH_GROUPS_CLAIM\" environment variable was not correctly
      parsed due to a typo in the configuration file. This ensures that OAuth group
      management features, including automatic group creation, now correctly utilize
      the specified claim from the identity provider, allowing for seamless integration
      with external user directories like Keycloak."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 3-account-and-access-changes-in-v0-6-23
  source_release: open-webui-2025-08-21-v0-6-23-github-241603918-5e4a7f46
  source_type: github_releases
  theme: account-access
  title: 3 Account and Access changes in v0.6.23
  type: change
related_changes:
- '[[Changes/Codex CLI/2025-08-15-https-github-com-openai-codex-pull-2294-moves-the-login-server-from-python-to-ru|(source
  link) moves the login server from Python…]]'
- '[[Changes/Gemini CLI/2025-08-18-feat-oauth-make-oauth-client-a-singleton-to-survive-cache-failures-by-mboshernit|feat(oauth):
  Make oauth client a singleton to survive cache failures]]'
- '[[Changes/Codex CLI/2025-08-20-9-account-and-access-changes-in-rust-v0-23-0|9 Account
  and Access changes in rust-v0.23.0]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-08-21-v0-6-23-github-241603918-5e4a7f46|open-webui-2025-08-21-v0-6-23-github-241603918-5e4a7f46]]'
source_type: github_releases
theme: account-access
title: 3 Account and Access changes in v0.6.23
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Account and Access changes in v0.6.23

**Open WebUI** · 2025-08-21 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.23) · from [[Releases/Open WebUI/open-webui-2025-08-21-v0-6-23-github-241603918-5e4a7f46|v0.6.23]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔐 **Enhanced OAuth Role Claim Handling**: Improved compatibility with diverse OAuth providers by allowing role claims to be supplied as single strings or integers, in addition to arrays. The system now automatically normalizes these single-value claims into arrays for consistent processing, streamlining integration with identity providers that format role data differently.

> 🛡️ **Resolved Critical OIDC SSO Login Failure**: Fixed a critical issue where OIDC Single Sign-On (SSO) logins failed due to an error in setting the authentication token as a cookie during the redirect process. This ensures reliable and seamless authentication for users utilizing OIDC providers, restoring full login functionality that was impacted by previous security hardening.

> 🔐 **Resolved OAUTH_GROUPS_CLAIM Configuration Issue**: Fixed a bug where the "OAUTH_GROUPS_CLAIM" environment variable was not correctly parsed due to a typo in the configuration file. This ensures that OAuth group management features, including automatic group creation, now correctly utilize the specified claim from the identity provider, allowing for seamless integration with external user directories like Keycloak.

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-08-21-8-interface-experience-changes-in-v0-6-23|8 Interface Experience changes in v0.6.23]] · Interface Experience
- [[Changes/Open WebUI/2025-08-21-restored-message-toolbar-icons-for-empty-messages-with-files-fixed-an-issue-wher|🐛 Restored Message Toolbar Icons for Empty Messages with Files]] · Editor Experience
- [[Changes/Open WebUI/2025-08-21-3-search-and-browsing-changes-in-v0-6-23|3 Search and Browsing changes in v0.6.23]] · Search and Browsing
- [[Changes/Open WebUI/2025-08-21-resolved-silently-dropped-streaming-response-chunks-fixed-an-issue-where-the-fin|💬 Resolved Silently Dropped Streaming Response Chunks]] · Files and Data
- [[Changes/Open WebUI/2025-08-21-3-mobile-and-desktop-changes-in-v0-6-23|3 Mobile and Desktop changes in v0.6.23]] · Mobile and Desktop
- [[Changes/Open WebUI/2025-08-21-6-reliability-and-performance-changes-in-v0-6-23|6 Reliability and Performance changes in v0.6.23]] · Reliability and Performance
- [[Changes/Open WebUI/2025-08-21-6-safety-and-privacy-changes-in-v0-6-23|6 Safety and Privacy changes in v0.6.23]] · Safety and Privacy
- [[Changes/Open WebUI/2025-08-21-2-voice-and-audio-changes-in-v0-6-23|2 Voice and Audio changes in v0.6.23]] · Voice and Audio
- [[Changes/Open WebUI/2025-08-21-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-08-21-2-accessibility-and-localization-changes-in-v0-6-23|2 Accessibility and Localization changes in v0.6.23]] · Accessibility and Localization
- [[Changes/Open WebUI/2025-08-21-7-model-support-changes-in-v0-6-23|7 Model Support changes in v0.6.23]] · Model Support
- [[Changes/Open WebUI/2025-08-21-resolved-image-generation-api-size-parameter-issue-fixed-a-bug-where-the-api-v1|🖼️ Resolved Image Generation API Size Parameter Issue]] · Image Generation
- [[Changes/Open WebUI/2025-08-21-resolved-code-block-input-issue-with-shift-enter-fixed-a-bug-where-typing-three|📝 Resolved Code Block Input Issue with Shift+Enter]] · Developer Workflow
- [[Changes/Open WebUI/2025-08-21-5-apps-and-integrations-changes-in-v0-6-23|5 Apps and Integrations changes in v0.6.23]] · Apps and Integrations
- [[Changes/Open WebUI/2025-08-21-23-other-changes-in-v0-6-23|23 other changes in v0.6.23]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2025-08-20 · Codex CLI · [[Changes/Codex CLI/2025-08-20-9-account-and-access-changes-in-rust-v0-23-0|9 Account and Access changes in rust-v0.23.0]]
- Later: 2025-08-22 · Open WebUI · [[Changes/Open WebUI/2025-08-22-redis-user-session-reliability-fixed-a-problem-affecting-the-saving-of-user-sess|🛡️ Redis User Session Reliability]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-08-21-dd6362&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-08-21-3-account-and-access-changes-in-v0-6-23.md%0ACard%20ID%3A%20open-webui-2025-08-21-dd6362%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.23%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->