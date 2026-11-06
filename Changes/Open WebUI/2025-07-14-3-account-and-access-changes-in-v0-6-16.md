---
card_id: open-webui-2025-07-14-a2efc5
date: '2025-07-14'
description: "Open WebUI · 2025-07-14 · Account and Access: 3 changes in v0.6.16 —
  \U0001F570️ **Configurable OAuth Timeout**: Enhance login reliability by setting
  a custom timeout…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 837
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: e5e9abc3ce4c945cf4179b4efd846d691f152157cdebbdeb564d0e3b131e08ba
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-07-14-a2efc5
  comparison: ''
  date: '2025-07-14'
  description: 'Open WebUI — v0.6.16: 3 Account and Access changes'
  evidence:
  - quote: "\U0001F570️ **Configurable OAuth Timeout**: Enhance login reliability
      by setting a custom timeout (OAUTH_TIMEOUT) for all OAuth providers (Google,
      Microsoft, GitHub, OIDC), preventing authentication failures on slow or restricted
      networks."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.16
  - quote: "\U0001F510 **OAuth Login Stability**: Resolved a critical OAuth bug that
      caused login failures on subsequent attempts after logging out. The user session
      is now completely cleared on logout, ensuring reliable and secure authentication
      across all supported providers (Google, Microsoft, GitHub, OIDC)."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.16
  - quote: "\U0001F6AA **OAuth Logout and Redirect Reliability**: The OAuth logout
      process has been made more robust. Logout requests now correctly use proxy environment
      variables, ensuring they succeed in corporate networks. Additionally, the custom
      WEBUI_AUTH_SIGNOUT_REDIRECT_URL is now properly respected for all OAuth/OIDC
      configurations, ensuring a seamless sign-out experience."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.16
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 3-account-and-access-changes-in-v0-6-16
  source_release: open-webui-2025-07-14-v0-6-16-github-232298341-b0885edf
  source_type: github_releases
  theme: account-access
  title: 3 Account and Access changes in v0.6.16
  type: change
related_changes:
- '[[Changes/Dify/2025-06-25-3-account-and-access-changes-in-1-5-0|3 Account and Access
  changes in 1.5.0]]'
- '[[Changes/Gemini CLI/2025-07-01-rename-authtype-login-with-google-personal-login-with-google-by-scidomino-in-htt|Rename
  AuthType LOGIN_WITH_GOOGLE_PERSONAL - LOGIN_WITH_GOOGLE]]'
- '[[Changes/Gemini CLI/2025-07-11-add-no-browser-environment-variable-to-trigger-offline-oauth-flow-by-sethtroisi|Add
  NO_BROWSER environment variable to trigger offline oauth flow]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-07-14-v0-6-16-github-232298341-b0885edf|open-webui-2025-07-14-v0-6-16-github-232298341-b0885edf]]'
source_type: github_releases
theme: account-access
title: 3 Account and Access changes in v0.6.16
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Account and Access changes in v0.6.16

**Open WebUI** · 2025-07-14 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.16) · from [[Releases/Open WebUI/open-webui-2025-07-14-v0-6-16-github-232298341-b0885edf|v0.6.16]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🕰️ **Configurable OAuth Timeout**: Enhance login reliability by setting a custom timeout (OAUTH_TIMEOUT) for all OAuth providers (Google, Microsoft, GitHub, OIDC), preventing authentication failures on slow or restricted networks.

> 🔐 **OAuth Login Stability**: Resolved a critical OAuth bug that caused login failures on subsequent attempts after logging out. The user session is now completely cleared on logout, ensuring reliable and secure authentication across all supported providers (Google, Microsoft, GitHub, OIDC).

> 🚪 **OAuth Logout and Redirect Reliability**: The OAuth logout process has been made more robust. Logout requests now correctly use proxy environment variables, ensuring they succeed in corporate networks. Additionally, the custom WEBUI_AUTH_SIGNOUT_REDIRECT_URL is now properly respected for all OAuth/OIDC configurations, ensuring a seamless sign-out experience.

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.16
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-07-14-2-automation-and-scheduling-changes-in-v0-6-16|2 Automation and Scheduling changes in v0.6.16]] · Automation and Scheduling
- [[Changes/Open WebUI/2025-07-14-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-07-14-4-context-window-changes-in-v0-6-16|4 Context Window changes in v0.6.16]] · Context Window
- [[Changes/Open WebUI/2025-07-14-instant-folder-based-chat-creation-start-a-new-chat-directly-from-any-folder-jus|📁 Instant Folder-Based Chat Creation]] · Projects and Workspaces
- [[Changes/Open WebUI/2025-07-14-4-reliability-and-performance-changes-in-v0-6-16|4 Reliability and Performance changes in v0.6.16]] · Reliability and Performance
- [[Changes/Open WebUI/2025-07-14-4-interface-experience-changes-in-v0-6-16|4 Interface Experience changes in v0.6.16]] · Interface Experience
- [[Changes/Open WebUI/2025-07-14-accessibility-high-contrast-theme-enhancements-major-accessibility-overhaul-with|🎨 Accessibility & High-Contrast Theme Enhancements]] · Accessibility and Localization
- [[Changes/Open WebUI/2025-07-14-6-model-support-changes-in-v0-6-16|6 Model Support changes in v0.6.16]] · Model Support
- [[Changes/Open WebUI/2025-07-14-3-safety-and-privacy-changes-in-v0-6-16|3 Safety and Privacy changes in v0.6.16]] · Safety and Privacy
- [[Changes/Open WebUI/2025-07-14-3-files-and-data-changes-in-v0-6-16|3 Files and Data changes in v0.6.16]] · Files and Data
- [[Changes/Open WebUI/2025-07-14-audio-mime-type-registration-issues-with-audio-file-content-types-have-been-reso|🔄 Audio MIME Type Registration]] · Voice and Audio
- [[Changes/Open WebUI/2025-07-14-seamless-iphone-image-uploads-effortlessly-upload-photos-from-iphones-and-other|📷 Seamless iPhone Image Uploads]] · Mobile and Desktop
- [[Changes/Open WebUI/2025-07-14-4-collaboration-changes-in-v0-6-16|4 Collaboration changes in v0.6.16]] · Collaboration
- [[Changes/Open WebUI/2025-07-14-3-editor-experience-changes-in-v0-6-16|3 Editor Experience changes in v0.6.16]] · Editor Experience
- [[Changes/Open WebUI/2025-07-14-20-other-changes-in-v0-6-16|20 other changes in v0.6.16]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2025-07-11 · Gemini CLI · [[Changes/Gemini CLI/2025-07-11-add-no-browser-environment-variable-to-trigger-offline-oauth-flow-by-sethtroisi|Add NO_BROWSER environment variable to trigger offline oauth flow]]
- Later: 2025-07-17 · Windsurf · [[Changes/Windsurf/2025-07-17-support-for-more-mcp-servers-with-easier-and-more-secure-authentication-by-integ|Support for more MCP servers with easier and more secure authentication…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-07-14-a2efc5&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-07-14-3-account-and-access-changes-in-v0-6-16.md%0ACard%20ID%3A%20open-webui-2025-07-14-a2efc5%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.16%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->