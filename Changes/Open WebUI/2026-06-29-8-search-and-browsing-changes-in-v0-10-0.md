---
card_id: open-webui-2026-06-29-422a5a
date: '2026-06-29'
description: "Open WebUI · 2026-06-29 · Search and Browsing: 8 changes in v0.10.0
  — \U0001F50E **Snippets in chat search results.** Searching your chats now shows
  a snippet of the…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-05-28-added-ability-to-batch-delete-ignore-search-results|Added
    ability to batch delete/ignore search results]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2223
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: search-browsing
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8e0ae9132c671c846048796f4ad335d7373161d9b0294d1fb07eec01cc2de028
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-06-29-422a5a
  comparison: ''
  date: '2026-06-29'
  description: 'Open WebUI — v0.10.0: 8 Search and Browsing changes'
  evidence:
  - quote: "\U0001F50E **Snippets in chat search results.** Searching your chats now
      shows a snippet of the matching content in each result, so you can tell results
      apart at a glance. [Commit](https://github.com/open-webui/open-webui/commit/0eba3df1199f56e8ac77213772a41313a3237296),
      [Commit](https://github.com/open-webui/open-webui/commit/67a7b23b85d2e3ce6b094b682ba9f07dc453d355),
      [Commit](https://github.com/open-webui/open-webui/commit/8927c9bb3d4b04f4fc8e443f42089f2a551276bc),
      [#25178](https://github.com/open-webui/open-webui/pull/25178)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F50E **SERPHouse web search.** SERPHouse can now be used as a web
      search provider. [Commit](https://github.com/open-webui/open-webui/commit/3a232f5e9a4d31a6b74cb34d007b581feeb2f005),
      [Commit](https://github.com/open-webui/open-webui/commit/dd4f43bfdb793c4276e6468b65fc32d9b881578a),
      [#26254](https://github.com/open-webui/open-webui/pull/26254)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F50E **Microsoft Web IQ web search.** Microsoft Web IQ can now be
      used as a web search provider, with a matching page-browse loader. [#26178](https://github.com/open-webui/open-webui/pull/26178)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: ⚠️ **Optional web search confirmation.** Administrators can now require
      users to confirm before a web search runs, with a banner and message making
      it clear when search is about to be used. [Commit](https://github.com/open-webui/open-webui/commit/fa76764c3b7f99c5adacd34dabd51ead09542c13),
      [#24942](https://github.com/open-webui/open-webui/pull/24942)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F4C1 **Terminal file browser can stay within a root folder.** The
      terminal file navigator now anchors to a defined root and home directory, so
      users can be kept within their workspace instead of browsing into system folders
      by accident. [Commit](https://github.com/open-webui/open-webui/commit/a0c2ec3d2cf8d696ede479211330eec2da360d39)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F50E **Web search results reach the model with retrieval on.** Web
      search results are now passed to the model even when embedding and retrieval
      are enabled, instead of being left out. [#25600](https://github.com/open-webui/open-webui/pull/25600)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F522 **Group count follows search.** The groups count now reflects
      the filtered search results instead of the full list. [#25689](https://github.com/open-webui/open-webui/pull/25689)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F527 **You.com search key renamed.** You.com web search now prefers
      the \"YDC_API_KEY\" environment variable, with the previous \"YOUCOM_API_KEY\"
      still accepted as a fallback. [Commit](https://github.com/open-webui/open-webui/commit/df634bb64f5043b0292e43c69bd1d31676c89328),
      [#26316](https://github.com/open-webui/open-webui/pull/26316)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 8-search-and-browsing-changes-in-v0-10-0
  source_release: open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01
  source_type: github_releases
  theme: search-browsing
  title: 8 Search and Browsing changes in v0.10.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-06-22-2-search-and-browsing-changes-in-rust-v0-142-0|2
  Search and Browsing changes in rust-v0.142.0]]'
- '[[Changes/GitHub Copilot CLI/2026-06-23-add-mcp-registry-installation-for-browsing-and-installing-mcp-servers|Add
  /mcp registry installation for browsing and installing MCP servers]]'
- '[[Changes/Kimi Code/2026-06-29-remove-the-sessions-slash-command-from-the-web-ui-the-sidebar-already-covers-ses|Remove
  the /sessions slash command from the web UI]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01|open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01]]'
source_type: github_releases
theme: search-browsing
title: 8 Search and Browsing changes in v0.10.0
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Search and Browsing changes in v0.10.0

**Open WebUI** · 2026-06-29 · [[Themes/search-browsing|Search and Browsing]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.10.0) · from [[Releases/Open WebUI/open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01|v0.10.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔎 **Snippets in chat search results.** Searching your chats now shows a snippet of the matching content in each result, so you can tell results apart at a glance. [Commit](https://github.com/open-webui/open-webui/commit/0eba3df1199f56e8ac77213772a41313a3237296), [Commit](https://github.com/open-webui/open-webui/commit/67a7b23b85d2e3ce6b094b682ba9f07dc453d355), [Commit](https://github.com/open-webui/open-webui/commit/8927c9bb3d4b04f4fc8e443f42089f2a551276bc), [#25178](https://github.com/open-webui/open-webui/pull/25178)

> 🔎 **SERPHouse web search.** SERPHouse can now be used as a web search provider. [Commit](https://github.com/open-webui/open-webui/commit/3a232f5e9a4d31a6b74cb34d007b581feeb2f005), [Commit](https://github.com/open-webui/open-webui/commit/dd4f43bfdb793c4276e6468b65fc32d9b881578a), [#26254](https://github.com/open-webui/open-webui/pull/26254)

> 🔎 **Microsoft Web IQ web search.** Microsoft Web IQ can now be used as a web search provider, with a matching page-browse loader. [#26178](https://github.com/open-webui/open-webui/pull/26178)

> ⚠️ **Optional web search confirmation.** Administrators can now require users to confirm before a web search runs, with a banner and message making it clear when search is about to be used. [Commit](https://github.com/open-webui/open-webui/commit/fa76764c3b7f99c5adacd34dabd51ead09542c13), [#24942](https://github.com/open-webui/open-webui/pull/24942)

> 📁 **Terminal file browser can stay within a root folder.** The terminal file navigator now anchors to a defined root and home directory, so users can be kept within their workspace instead of browsing into system folders by accident. [Commit](https://github.com/open-webui/open-webui/commit/a0c2ec3d2cf8d696ede479211330eec2da360d39)

> 🔎 **Web search results reach the model with retrieval on.** Web search results are now passed to the model even when embedding and retrieval are enabled, instead of being left out. [#25600](https://github.com/open-webui/open-webui/pull/25600)

> 🔢 **Group count follows search.** The groups count now reflects the filtered search results instead of the full list. [#25689](https://github.com/open-webui/open-webui/pull/25689)

> 🔧 **You.com search key renamed.** You.com web search now prefers the "YDC_API_KEY" environment variable, with the previous "YOUCOM_API_KEY" still accepted as a fallback. [Commit](https://github.com/open-webui/open-webui/commit/df634bb64f5043b0292e43c69bd1d31676c89328), [#26316](https://github.com/open-webui/open-webui/pull/26316)

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
- [[Changes/Open WebUI/2026-06-29-25-model-support-changes-in-v0-10-0|25 Model Support changes in v0.10.0]] · Model Support
- [[Changes/Open WebUI/2026-06-29-6-reliability-and-performance-changes-in-v0-10-0|6 Reliability and Performance changes in v0.10.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-06-29-4-mobile-and-desktop-changes-in-v0-10-0|4 Mobile and Desktop changes in v0.10.0]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-06-29-better-screen-reader-labels-on-toggles-integration-and-switch-toggles-now-expose|♿ Better screen-reader labels on toggles. Integration and switch toggles now…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-06-29-16-safety-and-privacy-changes-in-v0-10-0|16 Safety and Privacy changes in v0.10.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-06-29-2-pricing-model-changes-in-v0-10-0|2 Pricing Model changes in v0.10.0]] · Pricing Model
- [[Changes/Open WebUI/2026-06-29-7-apps-and-integrations-changes-in-v0-10-0|7 Apps and Integrations changes in v0.10.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-06-29-9-account-and-access-changes-in-v0-10-0|9 Account and Access changes in v0.10.0]] · Account and Access
- [[Changes/Open WebUI/2026-06-29-usable-chat-input-on-mobile-with-many-tools-when-skills-tools-terminal-web-searc|📱 Usable chat input on mobile with many tools. When skills, tools, terminal, web…]] · Image Generation
- [[Changes/Open WebUI/2026-06-29-6-automation-and-scheduling-changes-in-v0-10-0|6 Automation and Scheduling changes in v0.10.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-06-29-3-context-window-changes-in-v0-10-0|3 Context Window changes in v0.10.0]] · Context Window
- [[Changes/Open WebUI/2026-06-29-42-developer-workflow-changes-in-v0-10-0|42 Developer Workflow changes in v0.10.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-06-29-10-editor-experience-changes-in-v0-10-0|10 Editor Experience changes in v0.10.0]] · Editor Experience
- [[Changes/Open WebUI/2026-06-29-29-other-changes-in-v0-10-0|29 other changes in v0.10.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Search and Browsing

- Earlier: 2026-06-29 · Kimi Code · [[Changes/Kimi Code/2026-06-29-remove-the-sessions-slash-command-from-the-web-ui-the-sidebar-already-covers-ses|Remove the /sessions slash command from the web UI]]
- Later: 2026-06-30 · OpenClaw · [[Changes/OpenClaw/2026-06-30-more-official-channel-provider-and-web-search-plugins-can-now-be-installed-or-re|More official channel, provider, and web-search plugins can now be installed…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-05-28 · Descript · [[Changes/Descript/2020-05-28-added-ability-to-batch-delete-ignore-search-results|Added ability to batch delete/ignore search results]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-06-29-422a5a&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-06-29-8-search-and-browsing-changes-in-v0-10-0.md%0ACard%20ID%3A%20open-webui-2026-06-29-422a5a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.10.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->