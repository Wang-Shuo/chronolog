---
card_id: open-webui-2026-08-25-eae4a1
date: '2026-08-25'
description: "Open WebUI · 2026-08-25 · Search and Browsing: 5 changes in v0.11.1
  — \U0001F332 **Browsing files as a tree.** The terminal file browser now expands
  folders in place…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-browsing-an-experimental-model-that-knows-when-and-how-to-browse-the-internet|Browsing:
    An experimental model that knows when and how to browse the internet]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1251
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: search-browsing
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 46d6fc4325493f05624c44762dee9193015270c35ce203bbb8d19e646e2df3b5
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-08-25-eae4a1
  comparison: ''
  date: '2026-08-25'
  description: 'Open WebUI — v0.11.1: 5 Search and Browsing changes'
  evidence:
  - quote: "\U0001F332 **Browsing files as a tree.** The terminal file browser now
      expands folders in place rather than only navigating into them, remembers what
      you had open, offers a right-click menu, can show hidden files, sorts by size,
      expands a folder you hover over while dragging something onto it, and moves
      a whole selection in one go when you drop it. [Commit](https://github.com/open-webui/open-webui/commit/7dfbdd221ac0f7a839dd049e3e82b6a84c316860),
      [Commit](https://github.com/open-webui/open-webui/commit/516cf1a9a6154336182475b9df2d333b1579516d)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F52D **OpenSERP in the search settings.** OpenSERP can now be picked
      as the web search engine in the admin panel, with a field for its address, rather
      than only being configurable through the environment. [#27594](https://github.com/open-webui/open-webui/pull/27594),
      [#27592](https://github.com/open-webui/open-webui/issues/27592)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F5F3 **Web searches failing without saying why.** A web search that
      fails now explains itself instead of returning nothing at all, which most often
      happens when a search engine has been selected without its key being configured.
      [#28942](https://github.com/open-webui/open-webui/pull/28942)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F5C4 **Browsing outside the home directory in a terminal.** A terminal
      server set to allow browsing the whole filesystem can be browsed above the home
      directory again, where the file panel pinned itself there and opening a file
      elsewhere quietly did nothing. [#29006](https://github.com/open-webui/open-webui/pull/29006),
      [#29000](https://github.com/open-webui/open-webui/issues/29000)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F5FA️ **Browsing the web through Microsoft Web IQ.** Fetching a
      page with the web loader set to Microsoft Web IQ now works, where every attempt
      failed before a single request was made and had done so ever since that loader
      was added. [Commit](https://github.com/open-webui/open-webui/commit/6dcc2d52692c3fa1993ff1b3ae84c07d35fd9f6b),
      [Commit](https://github.com/open-webui/open-webui/commit/140d2cf4b59e71d2e9f4986d4d8649fccb47c83d),
      [#28688](https://github.com/open-webui/open-webui/issues/28688)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 5-search-and-browsing-changes-in-v0-11-1
  source_release: open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c
  source_type: github_releases
  theme: search-browsing
  title: 5 Search and Browsing changes in v0.11.1
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-08-13-if-you-have-the-google-drive-plugin-connected-you-can-now-see-and-browse-your-go-97f18f|If
  you have the Google Drive plugin connected, you can now see and browse…]]'
- '[[Changes/Ollama/2026-08-14-the-openai-compatible-responses-api-now-supports-web-search|The
  OpenAI-compatible Responses API now supports web search]]'
- '[[Changes/Cursor/2026-08-17-cursor-can-now-host-your-code|Cursor can now host your
  code]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c|open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c]]'
source_type: github_releases
theme: search-browsing
title: 5 Search and Browsing changes in v0.11.1
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Search and Browsing changes in v0.11.1

**Open WebUI** · 2026-08-25 · [[Themes/search-browsing|Search and Browsing]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.1) · from [[Releases/Open WebUI/open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c|v0.11.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🌲 **Browsing files as a tree.** The terminal file browser now expands folders in place rather than only navigating into them, remembers what you had open, offers a right-click menu, can show hidden files, sorts by size, expands a folder you hover over while dragging something onto it, and moves a whole selection in one go when you drop it. [Commit](https://github.com/open-webui/open-webui/commit/7dfbdd221ac0f7a839dd049e3e82b6a84c316860), [Commit](https://github.com/open-webui/open-webui/commit/516cf1a9a6154336182475b9df2d333b1579516d)

> 🔭 **OpenSERP in the search settings.** OpenSERP can now be picked as the web search engine in the admin panel, with a field for its address, rather than only being configurable through the environment. [#27594](https://github.com/open-webui/open-webui/pull/27594), [#27592](https://github.com/open-webui/open-webui/issues/27592)

> 🗳 **Web searches failing without saying why.** A web search that fails now explains itself instead of returning nothing at all, which most often happens when a search engine has been selected without its key being configured. [#28942](https://github.com/open-webui/open-webui/pull/28942)

> 🗄 **Browsing outside the home directory in a terminal.** A terminal server set to allow browsing the whole filesystem can be browsed above the home directory again, where the file panel pinned itself there and opening a file elsewhere quietly did nothing. [#29006](https://github.com/open-webui/open-webui/pull/29006), [#29000](https://github.com/open-webui/open-webui/issues/29000)

> 🗺️ **Browsing the web through Microsoft Web IQ.** Fetching a page with the web loader set to Microsoft Web IQ now works, where every attempt failed before a single request was made and had done so ever since that loader was added. [Commit](https://github.com/open-webui/open-webui/commit/6dcc2d52692c3fa1993ff1b3ae84c07d35fd9f6b), [Commit](https://github.com/open-webui/open-webui/commit/140d2cf4b59e71d2e9f4986d4d8649fccb47c83d), [#28688](https://github.com/open-webui/open-webui/issues/28688)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-08-25-9-files-and-data-changes-in-v0-11-1|9 Files and Data changes in v0.11.1]] · Files and Data
- [[Changes/Open WebUI/2026-08-25-image-generation-and-web-search-staying-switched-off-turning-either-off-now-take|🎨 Image generation and web search staying switched off. Turning either off now…]] · Image Generation
- [[Changes/Open WebUI/2026-08-25-7-safety-and-privacy-changes-in-v0-11-1|7 Safety and Privacy changes in v0.11.1]] · Safety and Privacy
- [[Changes/Open WebUI/2026-08-25-improved-ui-accessibility-a-closed-sidebar-is-no-longer-reachable-by-keyboard-or|♿ Improved UI accessibility. A closed sidebar is no longer reachable by keyboard…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-08-25-2-pricing-model-changes-in-v0-11-1|2 Pricing Model changes in v0.11.1]] · Pricing Model
- [[Changes/Open WebUI/2026-08-25-11-automation-and-scheduling-changes-in-v0-11-1|11 Automation and Scheduling changes in v0.11.1]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-08-25-10-reliability-and-performance-changes-in-v0-11-1|10 Reliability and Performance changes in v0.11.1]] · Reliability and Performance
- [[Changes/Open WebUI/2026-08-25-6-collaboration-changes-in-v0-11-1|6 Collaboration changes in v0.11.1]] · Collaboration
- [[Changes/Open WebUI/2026-08-25-4-context-window-changes-in-v0-11-1|4 Context Window changes in v0.11.1]] · Context Window
- [[Changes/Open WebUI/2026-08-25-13-account-and-access-changes-in-v0-11-1|13 Account and Access changes in v0.11.1]] · Account and Access
- [[Changes/Open WebUI/2026-08-25-starting-up-on-windows-the-windows-start-script-now-creates-the-secret-key-it-ne|🪟 Starting up on Windows. The Windows start script now creates the secret key…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-08-25-2-multimodal-input-changes-in-v0-11-1|2 Multimodal Input changes in v0.11.1]] · Multimodal Input
- [[Changes/Open WebUI/2026-08-25-12-editor-experience-changes-in-v0-11-1|12 Editor Experience changes in v0.11.1]] · Editor Experience
- [[Changes/Open WebUI/2026-08-25-4-apps-and-integrations-changes-in-v0-11-1|4 Apps and Integrations changes in v0.11.1]] · Apps and Integrations
- [[Changes/Open WebUI/2026-08-25-73-developer-workflow-changes-in-v0-11-1|73 Developer Workflow changes in v0.11.1]] · Developer Workflow
- [[Changes/Open WebUI/2026-08-25-8-memory-and-personalization-changes-in-v0-11-1|8 Memory and Personalization changes in v0.11.1]] · Memory and Personalization
- [[Changes/Open WebUI/2026-08-25-files-for-delegated-tasks-a-task-handed-to-a-sub-agent-can-now-carry-the-attachm|🤝 Files for delegated tasks. A task handed to a sub-agent can now carry…]] · Agent Mode
- [[Changes/Open WebUI/2026-08-25-4-enterprise-and-administration-changes-in-v0-11-1|4 Enterprise and Administration changes in v0.11.1]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-08-25-24-interface-experience-changes-in-v0-11-1|24 Interface Experience changes in v0.11.1]] · Interface Experience
- [[Changes/Open WebUI/2026-08-25-4-voice-and-audio-changes-in-v0-11-1|4 Voice and Audio changes in v0.11.1]] · Voice and Audio
- [[Changes/Open WebUI/2026-08-25-56-model-support-changes-in-v0-11-1|56 Model Support changes in v0.11.1]] · Model Support
- [[Changes/Open WebUI/2026-08-25-39-other-changes-in-v0-11-1|39 other changes in v0.11.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Search and Browsing

- Earlier: 2026-08-17 · Cursor · [[Changes/Cursor/2026-08-17-cursor-can-now-host-your-code|Cursor can now host your code]]
- Later: 2026-08-26 · Lovable · [[Changes/Lovable/2026-08-26-see-how-each-app-page-appears-in-search-results-and-link-previews|See how each app page appears in search results and link previews]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-browsing-an-experimental-model-that-knows-when-and-how-to-browse-the-internet|Browsing: An experimental model that knows when and how to browse the internet]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-08-25-eae4a1&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-08-25-5-search-and-browsing-changes-in-v0-11-1.md%0ACard%20ID%3A%20open-webui-2026-08-25-eae4a1%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->