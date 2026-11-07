---
card_id: open-webui-2026-06-01-cd2962
date: '2026-06-01'
description: "Open WebUI · 2026-06-01 · Account and Access: 6 changes in v0.9.6 —
  \U0001F3AB **Wildcard OAuth role mapping.** Administrators can now set \"\\*\" in
  the allowed OAuth…"
diffusion:
  first_in_tracked: "[[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign
    into Notion with your Apple ID \U0001F5DD️ The perfect combination of speedy and
    secure]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2134
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 1cb6210e6ce780b8da93e4b3a7662db78bb8c4eb14d8710c5250faf940b3666c
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-06-01-cd2962
  comparison: ''
  date: '2026-06-01'
  description: 'Open WebUI — v0.9.6: 6 Account and Access changes'
  evidence:
  - quote: "\U0001F3AB **Wildcard OAuth role mapping.** Administrators can now set
      \"\\*\" in the allowed OAuth roles to grant the user role to any authenticated
      OAuth user, instead of having to enumerate every accepted role. [#25062](https://github.com/open-webui/open-webui/pull/25062),
      [Commit](https://github.com/open-webui/open-webui/commit/07cbc91a8eba3a9a3b39588b2ae5de916930af70)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: ➡️ **Optional auto-redirect to single sign-on.** Administrators can now
      enable "OAUTH_AUTO_REDIRECT" so that, on deployments with a single sign-on provider
      and no other login methods, users are sent straight to the provider instead
      of seeing a login page first. [#25067](https://github.com/open-webui/open-webui/pull/25067),
      [Commit](https://github.com/open-webui/open-webui/commit/d64ef1803d2f5cedb7b3a308151d08ff2cd2b8e1)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: ☁️ **Azure AI Foundry v1 with Entra ID.** Open WebUI now supports Azure
      AI Foundry's OpenAI v1 endpoint together with Microsoft Entra ID authentication,
      so these connections work without manual workarounds. [#24761](https://github.com/open-webui/open-webui/issues/24761),
      [#24985](https://github.com/open-webui/open-webui/pull/24985), [Commit](https://github.com/open-webui/open-webui/commit/eb4eebc3ce1042cb0d393bf890c1895db6e08b19)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001FA9E **OAuth profile picture redirect handling.** The OAuth profile
      picture fetch now follows redirects only when administrators have explicitly
      allowed it, closing a window where a redirect from an externally validated URL
      could be used to reach internal addresses. [#24809](https://github.com/open-webui/open-webui/pull/24809)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F39F️ **MCP tool server sessions stay connected.** OAuth-authenticated
      MCP tool server sessions are no longer mistakenly refreshed and deleted by the
      single sign-on session handler, so those connections stay active. [#24618](https://github.com/open-webui/open-webui/issues/24618),
      [Commit](https://github.com/open-webui/open-webui/commit/c8eb8edca4174ec68fabd071d6b08c0bc07f8117)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F91D **MCP OAuth scope discovery.** The OAuth flow for MCP tool
      servers now reads the scopes a server advertises through its Protected Resource
      Metadata, so connecting to servers that declare their own scopes succeeds. [#24730](https://github.com/open-webui/open-webui/issues/24730),
      [#24690](https://github.com/open-webui/open-webui/pull/24690)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 6-account-and-access-changes-in-v0-9-6
  source_release: open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e
  source_type: github_releases
  theme: account-access
  title: 6 Account and Access changes in v0.9.6
  type: change
related_changes:
- '[[Changes/Kimi Code/2026-05-26-4-account-and-access-changes-in-kimi-code-0-2-0|4
  Account and Access changes in Kimi Code 0.2.0]]'
- '[[Changes/OpenCode/2026-05-27-core-digitalocean-inference-now-uses-your-oauth-token-directly-instead-of-creati|Core
  DigitalOcean inference now uses your OAuth token directly instead of creating a
  MAK]]'
- '[[Changes/GitHub Copilot CLI/2026-06-01-surface-the-underlying-reason-e-g-github-api-rate-limit-when-sdk-auth-token-vali|Surface
  the underlying reason (e.g. GitHub API rate limit) when SDK auth-token…]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e|open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e]]'
source_type: github_releases
theme: account-access
title: 6 Account and Access changes in v0.9.6
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Account and Access changes in v0.9.6

**Open WebUI** · 2026-06-01 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.6) · from [[Releases/Open WebUI/open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e|v0.9.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🎫 **Wildcard OAuth role mapping.** Administrators can now set "\*" in the allowed OAuth roles to grant the user role to any authenticated OAuth user, instead of having to enumerate every accepted role. [#25062](https://github.com/open-webui/open-webui/pull/25062), [Commit](https://github.com/open-webui/open-webui/commit/07cbc91a8eba3a9a3b39588b2ae5de916930af70)

> ➡️ **Optional auto-redirect to single sign-on.** Administrators can now enable "OAUTH_AUTO_REDIRECT" so that, on deployments with a single sign-on provider and no other login methods, users are sent straight to the provider instead of seeing a login page first. [#25067](https://github.com/open-webui/open-webui/pull/25067), [Commit](https://github.com/open-webui/open-webui/commit/d64ef1803d2f5cedb7b3a308151d08ff2cd2b8e1)

> ☁️ **Azure AI Foundry v1 with Entra ID.** Open WebUI now supports Azure AI Foundry's OpenAI v1 endpoint together with Microsoft Entra ID authentication, so these connections work without manual workarounds. [#24761](https://github.com/open-webui/open-webui/issues/24761), [#24985](https://github.com/open-webui/open-webui/pull/24985), [Commit](https://github.com/open-webui/open-webui/commit/eb4eebc3ce1042cb0d393bf890c1895db6e08b19)

> 🪞 **OAuth profile picture redirect handling.** The OAuth profile picture fetch now follows redirects only when administrators have explicitly allowed it, closing a window where a redirect from an externally validated URL could be used to reach internal addresses. [#24809](https://github.com/open-webui/open-webui/pull/24809)

> 🎟️ **MCP tool server sessions stay connected.** OAuth-authenticated MCP tool server sessions are no longer mistakenly refreshed and deleted by the single sign-on session handler, so those connections stay active. [#24618](https://github.com/open-webui/open-webui/issues/24618), [Commit](https://github.com/open-webui/open-webui/commit/c8eb8edca4174ec68fabd071d6b08c0bc07f8117)

> 🤝 **MCP OAuth scope discovery.** The OAuth flow for MCP tool servers now reads the scopes a server advertises through its Protected Resource Metadata, so connecting to servers that declare their own scopes succeeds. [#24730](https://github.com/open-webui/open-webui/issues/24730), [#24690](https://github.com/open-webui/open-webui/pull/24690)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-06-01-bulk-enable-or-disable-automations-automations-can-now-be-enabled-or-disabled-in|🔘 Bulk enable or disable automations. Automations can now be enabled or disabled…]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-06-01-4-context-window-changes-in-v0-9-6|4 Context Window changes in v0.9.6]] · Context Window
- [[Changes/Open WebUI/2026-06-01-2-memory-and-personalization-changes-in-v0-9-6|2 Memory and Personalization changes in v0.9.6]] · Memory and Personalization
- [[Changes/Open WebUI/2026-06-01-keyboard-and-screen-reader-access-to-menus-the-integrations-more-options-and-use|♿ Keyboard and screen reader access to menus. The integrations, more-options…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-06-01-27-developer-workflow-changes-in-v0-9-6|27 Developer Workflow changes in v0.9.6]] · Developer Workflow
- [[Changes/Open WebUI/2026-06-01-4-interface-experience-changes-in-v0-9-6|4 Interface Experience changes in v0.9.6]] · Interface Experience
- [[Changes/Open WebUI/2026-06-01-4-editor-experience-changes-in-v0-9-6|4 Editor Experience changes in v0.9.6]] · Editor Experience
- [[Changes/Open WebUI/2026-06-01-5-files-and-data-changes-in-v0-9-6|5 Files and Data changes in v0.9.6]] · Files and Data
- [[Changes/Open WebUI/2026-06-01-7-safety-and-privacy-changes-in-v0-9-6|7 Safety and Privacy changes in v0.9.6]] · Safety and Privacy
- [[Changes/Open WebUI/2026-06-01-startup-on-non-unicode-consoles-open-webui-no-longer-crashes-at-startup-when-the|🥾 Startup on non-Unicode consoles. Open WebUI no longer crashes at startup…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-06-01-youtube-short-link-transcripts-pasting-a-youtu-be-short-link-into-a-chat-now-loa|📺 YouTube short link transcripts. Pasting a "youtu.be" short link into a chat…]] · Multimodal Input
- [[Changes/Open WebUI/2026-06-01-9-search-and-browsing-changes-in-v0-9-6|9 Search and Browsing changes in v0.9.6]] · Search and Browsing
- [[Changes/Open WebUI/2026-06-01-shared-chat-file-write-protection-access-to-a-file-through-a-shared-chat-now-onl|🔐 Shared-chat file write protection. Access to a file through a shared chat now…]] · Collaboration
- [[Changes/Open WebUI/2026-06-01-2-enterprise-and-administration-changes-in-v0-9-6|2 Enterprise and Administration changes in v0.9.6]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-06-01-image-generation-with-non-standard-response-headers-image-generation-now-works-w|🖌️ Image generation with non-standard response headers. Image generation now…]] · Image Generation
- [[Changes/Open WebUI/2026-06-01-12-model-support-changes-in-v0-9-6|12 Model Support changes in v0.9.6]] · Model Support
- [[Changes/Open WebUI/2026-06-01-4-apps-and-integrations-changes-in-v0-9-6|4 Apps and Integrations changes in v0.9.6]] · Apps and Integrations
- [[Changes/Open WebUI/2026-06-01-5-reliability-and-performance-changes-in-v0-9-6|5 Reliability and Performance changes in v0.9.6]] · Reliability and Performance
- [[Changes/Open WebUI/2026-06-01-4-voice-and-audio-changes-in-v0-9-6|4 Voice and Audio changes in v0.9.6]] · Voice and Audio
- [[Changes/Open WebUI/2026-06-01-20-other-changes-in-v0-9-6|20 other changes in v0.9.6]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-06-01 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-06-01-surface-the-underlying-reason-e-g-github-api-rate-limit-when-sdk-auth-token-vali|Surface the underlying reason (e.g. GitHub API rate limit) when SDK auth-token…]]
- Later: 2026-06-02 · ChatGPT · [[Changes/ChatGPT/2026-06-02-active-sessions-shows-sessions-known-through-session-management-including-chatgp|Active sessions shows sessions known through session management, including ChatGPT…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Notion · [[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign into Notion with your Apple ID 🗝️ The perfect combination of speedy and secure]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-06-01-cd2962&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-06-01-6-account-and-access-changes-in-v0-9-6.md%0ACard%20ID%3A%20open-webui-2026-06-01-cd2962%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.6%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->