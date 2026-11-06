---
card_id: open-webui-2026-10-16-2afbdc
date: '2026-10-16'
description: "Open WebUI · 2026-10-16 · Account and Access: 2 changes in v0.12.3 —
  \U0001F511 **OAuth token refresh with client_secret_basic.** When…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1296
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2e0887e344a9d5c3b7135bfc545077979b9278239f10c54c7f6239b2203ddff9
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-10-16-2afbdc
  comparison: ''
  date: '2026-10-16'
  description: 'Open WebUI — v0.12.3: 2 Account and Access changes'
  evidence:
  - quote: "\U0001F511 **OAuth token refresh with client_secret_basic.** When \"OAUTH_TOKEN_ENDPOINT_AUTH_METHOD\"
      is client_secret_basic, token refresh now sends the client credentials in the
      Basic header like sign-in does, where providers that accept only Basic rejected
      the refresh and Open WebUI deleted the user's OAuth tokens, breaking model connections
      and tool servers that use them until the next sign-in. [#32507](https://github.com/open-webui/open-webui/pull/32507),
      [Commit](https://github.com/open-webui/open-webui/commit/ae6793dd4f209455387bcc418a5c775eec0b16c3),
      [#32506](https://github.com/open-webui/open-webui/issues/32506)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.3
  - quote: "\U0001F6E0️ **OAuth tools after sign-in.** An OAuth MCP tool now stays
      turned on after its sign-in redirect when the model has default tools, and links
      with ?tools= turn the listed tools on. [#32488](https://github.com/open-webui/open-webui/pull/32488),
      [Commit](https://github.com/open-webui/open-webui/commit/81722918384cb56608a2ab26ca03059b3a811758),
      [#32476](https://github.com/open-webui/open-webui/issues/32476)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.3
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 2-account-and-access-changes-in-v0-12-3
  source_release: open-webui-2026-10-16-v0-12-3-github-414903453-58a8a82d
  source_type: github_releases
  theme: account-access
  title: 2 Account and Access changes in v0.12.3
  type: change
related_changes:
- '[[Changes/Lovable/2026-10-15-login-pages-include-sign-in-with-lovable-by-default|Login
  pages include Sign in with Lovable by default]]'
- '[[Changes/Claude Code/2026-10-16-added-a-notice-to-design-sync-and-design-login-that-standalone-claude-design-cla|Added
  a notice to /design-sync and /design-login that standalone Claude Design…]]'
- '[[Changes/Lovable/2026-10-16-add-oidc-sign-in-to-your-app|Add OIDC sign-in to your
  app]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-10-16-v0-12-3-github-414903453-58a8a82d|open-webui-2026-10-16-v0-12-3-github-414903453-58a8a82d]]'
source_type: github_releases
theme: account-access
title: 2 Account and Access changes in v0.12.3
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Account and Access changes in v0.12.3

**Open WebUI** · 2026-10-16 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.3) · from [[Releases/Open WebUI/open-webui-2026-10-16-v0-12-3-github-414903453-58a8a82d|v0.12.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔑 **OAuth token refresh with client_secret_basic.** When "OAUTH_TOKEN_ENDPOINT_AUTH_METHOD" is client_secret_basic, token refresh now sends the client credentials in the Basic header like sign-in does, where providers that accept only Basic rejected the refresh and Open WebUI deleted the user's OAuth tokens, breaking model connections and tool servers that use them until the next sign-in. [#32507](https://github.com/open-webui/open-webui/pull/32507), [Commit](https://github.com/open-webui/open-webui/commit/ae6793dd4f209455387bcc418a5c775eec0b16c3), [#32506](https://github.com/open-webui/open-webui/issues/32506)

> 🛠️ **OAuth tools after sign-in.** An OAuth MCP tool now stays turned on after its sign-in redirect when the model has default tools, and links with ?tools= turn the listed tools on. [#32488](https://github.com/open-webui/open-webui/pull/32488), [Commit](https://github.com/open-webui/open-webui/commit/81722918384cb56608a2ab26ca03059b3a811758), [#32476](https://github.com/open-webui/open-webui/issues/32476)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.12.3
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-10-16-built-in-tools-turned-back-on-stay-on-a-built-in-tool-such-as-memory-that-is-off|🧰 Built-in tools turned back on stay on. A built-in tool such as Memory…]] · Memory and Personalization
- [[Changes/Open WebUI/2026-10-16-20-developer-workflow-changes-in-v0-12-3|20 Developer Workflow changes in v0.12.3]] · Developer Workflow
- [[Changes/Open WebUI/2026-10-16-4-files-and-data-changes-in-v0-12-3|4 Files and Data changes in v0.12.3]] · Files and Data
- [[Changes/Open WebUI/2026-10-16-general-improvements-various-improvements-were-implemented-across-the-applicatio|🔄 General improvements. Various improvements were implemented across…]] · Reliability and Performance
- [[Changes/Open WebUI/2026-10-16-3-model-support-changes-in-v0-12-3|3 Model Support changes in v0.12.3]] · Model Support
- [[Changes/Open WebUI/2026-10-16-2-enterprise-and-administration-changes-in-v0-12-3|2 Enterprise and Administration changes in v0.12.3]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-10-16-2-context-window-changes-in-v0-12-3|2 Context Window changes in v0.12.3]] · Context Window
- [[Changes/Open WebUI/2026-10-16-clear-input-selections-shortcut-clearing-the-model-override-selected-tools-and-f|🧹 Clear Input Selections shortcut. Clearing the model override, selected tools…]] · Image Generation
- [[Changes/Open WebUI/2026-10-16-built-in-tools-with-a-custom-tools-parameter-a-model-with-a-custom-parameter-nam|🧩 Built-in tools with a custom tools parameter. A model with a custom parameter…]] · Search and Browsing
- [[Changes/Open WebUI/2026-10-16-4-interface-experience-changes-in-v0-12-3|4 Interface Experience changes in v0.12.3]] · Interface Experience
- [[Changes/Open WebUI/2026-10-16-2-editor-experience-changes-in-v0-12-3|2 Editor Experience changes in v0.12.3]] · Editor Experience
- [[Changes/Open WebUI/2026-10-16-2-safety-and-privacy-changes-in-v0-12-3|2 Safety and Privacy changes in v0.12.3]] · Safety and Privacy
- [[Changes/Open WebUI/2026-10-16-2-collaboration-changes-in-v0-12-3|2 Collaboration changes in v0.12.3]] · Collaboration
- [[Changes/Open WebUI/2026-10-16-translation-updates-translations-for-portuguese-brazil-chinese-traditional-arabi|🌐 Translation updates. Translations for Portuguese (Brazil), Chinese…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-10-16 · Lovable · [[Changes/Lovable/2026-10-16-add-oidc-sign-in-to-your-app|Add OIDC sign-in to your app]]
- Later: 2026-10-19 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-10-19-3-account-and-access-changes-in-v1-0-100|3 Account and Access changes in v1.0.100]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-16-2afbdc&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-16-2-account-and-access-changes-in-v0-12-3.md%0ACard%20ID%3A%20open-webui-2026-10-16-2afbdc%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.3%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->