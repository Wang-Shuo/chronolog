---
card_id: open-webui-2025-08-21-096d78
date: '2025-08-21'
description: "Open WebUI · 2025-08-21 · Interface Experience: 8 changes in v0.6.23
  — \U0001F4BE **Save Temporary Chats Button**: Introduced a new 'Save Chat' button
  for conversations…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-04-14-descript-s-sidebar-now-has-an-economical-collapsed-state|Collapsed
    Sidebar]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2321
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 3076408b3b7472ff3d731157bcd7cf75dd4461cdea77840b954fbb088831ff27
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-08-21-096d78
  comparison: ''
  date: '2025-08-21'
  description: 'Open WebUI — v0.6.23: 8 Interface Experience changes'
  evidence:
  - quote: "\U0001F4BE **Save Temporary Chats Button**: Introduced a new 'Save Chat'
      button for conversations initiated in temporary mode. This allows users to permanently
      save valuable temporary conversations to their chat history, providing greater
      flexibility and ensuring important discussions are not lost."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  - quote: "\U0001F4C2 **Chat Movement Options in Menu**: Added the ability to move
      chats directly to folders from the chat menu. This enhances chat organization
      and allows users to manage their conversations more efficiently by relocating
      them between folders with ease."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  - quote: "\U0001F465 **Direct Navigation to User Groups from User Edit**: Enhanced
      the user edit modal to include a direct link to the associated user group. This
      allows administrators to quickly navigate from a user's profile to their group
      settings, streamlining user and group management workflows."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  - quote: '⚡ **Prevented UI Blocking by Unreachable Webhooks**: Resolved a critical
      performance and user experience issue where synchronous webhook calls to unreachable
      or slow endpoints would block the entire user interface for all users. Webhook
      requests are now processed asynchronously using "aiohttp", ensuring that the
      UI remains responsive and functional even if webhook delivery encounters delays
      or failures.'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  - quote: "\U0001F512 **Password Change Option Hidden for Externally Authenticated
      Users**: Resolved an issue where the password change dialog was visible to users
      authenticated via external methods (e.g., LDAP, OIDC, Trusted Header). The option
      to change a password in user settings is now correctly hidden for these users,
      as their passwords are managed externally, streamlining the user interface and
      preventing confusion."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  - quote: "\U0001F4DD **Restored Custom Pending User Overlay Visibility**: Fixed
      an issue where the custom title and description configured for pending users
      were not visible. The application now correctly exposes these UI configuration
      settings to pending users, ensuring that the custom onboarding messages are
      displayed as intended."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  - quote: "\U0001F6E0️ **Improved Tool List Synchronization in Multi-Replica Deployments**:
      Resolved an issue where tool updates were not consistently reflected across
      all instances in multi-replica environments, leading to stale tool lists for
      users on other replicas. The tool list in the message input menu is now automatically
      refreshed each time it is accessed, ensuring all users always see the most current
      set of available tools."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  - quote: "\U0001F310 **Corrected 'Releases' Link**: Fixed an issue where the 'Releases'
      button in the user menu directed to an incorrect URL, now correctly linking
      to the Open WebUI GitHub releases page."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 8-interface-experience-changes-in-v0-6-23
  source_release: open-webui-2025-08-21-v0-6-23-github-241603918-5e4a7f46
  source_type: github_releases
  theme: interface-experience
  title: 8 Interface Experience changes in v0.6.23
  type: change
related_changes:
- '[[Changes/Gemini CLI/2025-08-14-3-interface-experience-changes-in-v0-1-21|3 Interface
  Experience changes in v0.1.21]]'
- '[[Changes/Codex CLI/2025-08-20-2-interface-experience-changes-in-rust-v0-23-0|2
  Interface Experience changes in rust-v0.23.0]]'
- '[[Changes/Gemini/2025-08-21-revisit-your-conversations-you-can-now-search-your-gemini-chat-history|Revisit
  your conversations: You can now search your Gemini chat history]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-08-21-v0-6-23-github-241603918-5e4a7f46|open-webui-2025-08-21-v0-6-23-github-241603918-5e4a7f46]]'
source_type: github_releases
theme: interface-experience
title: 8 Interface Experience changes in v0.6.23
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Interface Experience changes in v0.6.23

**Open WebUI** · 2025-08-21 · [[Themes/interface-experience|Interface Experience]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.23) · from [[Releases/Open WebUI/open-webui-2025-08-21-v0-6-23-github-241603918-5e4a7f46|v0.6.23]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 💾 **Save Temporary Chats Button**: Introduced a new 'Save Chat' button for conversations initiated in temporary mode. This allows users to permanently save valuable temporary conversations to their chat history, providing greater flexibility and ensuring important discussions are not lost.

> 📂 **Chat Movement Options in Menu**: Added the ability to move chats directly to folders from the chat menu. This enhances chat organization and allows users to manage their conversations more efficiently by relocating them between folders with ease.

> 👥 **Direct Navigation to User Groups from User Edit**: Enhanced the user edit modal to include a direct link to the associated user group. This allows administrators to quickly navigate from a user's profile to their group settings, streamlining user and group management workflows.

> ⚡ **Prevented UI Blocking by Unreachable Webhooks**: Resolved a critical performance and user experience issue where synchronous webhook calls to unreachable or slow endpoints would block the entire user interface for all users. Webhook requests are now processed asynchronously using "aiohttp", ensuring that the UI remains responsive and functional even if webhook delivery encounters delays or failures.

> 🔒 **Password Change Option Hidden for Externally Authenticated Users**: Resolved an issue where the password change dialog was visible to users authenticated via external methods (e.g., LDAP, OIDC, Trusted Header). The option to change a password in user settings is now correctly hidden for these users, as their passwords are managed externally, streamlining the user interface and preventing confusion.

> 📝 **Restored Custom Pending User Overlay Visibility**: Fixed an issue where the custom title and description configured for pending users were not visible. The application now correctly exposes these UI configuration settings to pending users, ensuring that the custom onboarding messages are displayed as intended.

> 🛠️ **Improved Tool List Synchronization in Multi-Replica Deployments**: Resolved an issue where tool updates were not consistently reflected across all instances in multi-replica environments, leading to stale tool lists for users on other replicas. The tool list in the message input menu is now automatically refreshed each time it is accessed, ensuring all users always see the most current set of available tools.

> 🌐 **Corrected 'Releases' Link**: Fixed an issue where the 'Releases' button in the user menu directed to an incorrect URL, now correctly linking to the Open WebUI GitHub releases page.

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

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
- [[Changes/Open WebUI/2025-08-21-3-account-and-access-changes-in-v0-6-23|3 Account and Access changes in v0.6.23]] · Account and Access
- [[Changes/Open WebUI/2025-08-21-23-other-changes-in-v0-6-23|23 other changes in v0.6.23]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Interface Experience

- Earlier: 2025-08-21 · Gemini · [[Changes/Gemini/2025-08-21-revisit-your-conversations-you-can-now-search-your-gemini-chat-history|Revisit your conversations: You can now search your Gemini chat history]]
- Later: 2025-08-22 · Devin · [[Changes/Devin/2025-08-22-settings-navigation-enhancement|Settings Navigation Enhancement]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-04-14 · Descript · [[Changes/Descript/2019-04-14-descript-s-sidebar-now-has-an-economical-collapsed-state|Collapsed Sidebar]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-08-21-096d78&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-08-21-8-interface-experience-changes-in-v0-6-23.md%0ACard%20ID%3A%20open-webui-2025-08-21-096d78%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.23%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->