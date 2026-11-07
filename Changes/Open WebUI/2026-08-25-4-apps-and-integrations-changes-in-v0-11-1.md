---
card_id: open-webui-2026-08-25-c19990
date: '2026-08-25'
description: "Open WebUI · 2026-08-25 · Apps and Integrations: 4 changes in v0.11.1
  — \U0001F4FD️ **Truer PowerPoint previews.** Slide previews now render tables, charts,
  connectors…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2811
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 29374e265ee59f9588c1510baa92aa10ff891e40e1997862d1e5382c263cf9eb
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-08-25-c19990
  comparison: ''
  date: '2026-08-25'
  description: 'Open WebUI — v0.11.1: 4 Apps and Integrations changes'
  evidence:
  - quote: "\U0001F4FD️ **Truer PowerPoint previews.** Slide previews now render tables,
      charts, connectors, gradients, theme colours, bullets, fonts, and text alignment
      far closer to the original, and the viewer lets you move between slides with
      the arrow keys or the scroll wheel while the thumbnail strip follows along.
      [Commit](https://github.com/open-webui/open-webui/commit/8dd23f74c9a59fdfbdaefb4a403ef79bdd3dfed9),
      [Commit](https://github.com/open-webui/open-webui/commit/048c06399363baac4046717129f072172ee90805),
      [Commit](https://github.com/open-webui/open-webui/commit/c93c6d6fc48ee8870eec349cb4c5af88c9435cfb),
      [Commit](https://github.com/open-webui/open-webui/commit/76583749edb966c0239ce203a84c1ee8d8c7faee),
      [Commit](https://github.com/open-webui/open-webui/commit/b3a5fd3875dc3c29a11eb5435438e55685cad639),
      [Commit](https://github.com/open-webui/open-webui/commit/794671a9883d5e067c407067f324ffa25ed38e3f),
      [Commit](https://github.com/open-webui/open-webui/commit/f96b717566b2084bd5fe70fb622ab66b5a643c0d),
      [Commit](https://github.com/open-webui/open-webui/commit/b7292890ccea794750651abbcde01cda62551e1b),
      [Commit](https://github.com/open-webui/open-webui/commit/31d08d592c4ee46a7ce827d6ffdf8e3cf16bf2ac)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: ↔️ **Connectors in the side-by-side overview.** With the conversation overview
      laid out left to right, the lines between messages now join at the sides rather
      than the top and bottom, so they no longer cut across the boxes. [Commit](https://github.com/open-webui/open-webui/commit/6e468c5b9539d3b6057bab63d81e8d2974acff7b)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F507 **Filter failures that said nothing.** When a filter's outlet
      or stream hook raises, the failure is now reported with the filter's name and
      a traceback at the default log level, where it was swallowed and left plugin
      authors with nothing to go on. [Commit](https://github.com/open-webui/open-webui/commit/35fbde0a3fb303b7076b03465b1a2b0ba832df53)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F433 **Test-only packages removed from the image.** The container
      no longer ships pytest, pytest-docker, the Docker SDK, or netcat, none of which
      anything in Open WebUI used, so the image is smaller; anyone whose own tools
      or functions relied on those being present will need to install them themselves.
      [#28726](https://github.com/open-webui/open-webui/pull/28726)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 4-apps-and-integrations-changes-in-v0-11-1
  source_release: open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c
  source_type: github_releases
  theme: apps-integrations
  title: 4 Apps and Integrations changes in v0.11.1
  type: change
related_changes:
- '[[Changes/Claude Code/2026-08-25-3-apps-and-integrations-changes-in-v2-1-246|3
  Apps and Integrations changes in v2.1.246]]'
- '[[Changes/Dify/2026-08-25-28-apps-and-integrations-changes-in-1-17-0|28 Apps and
  Integrations changes in 1.17.0]]'
- '[[Changes/Gemini CLI/2026-08-25-ssr-agent-issue-fix-21919-fix-typescript-strict-null-errors-in-integration-tests|SSR
  Agent Issue Fix (21919): Fix TypeScript strict-null errors in integration tests]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c|open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c]]'
source_type: github_releases
theme: apps-integrations
title: 4 Apps and Integrations changes in v0.11.1
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Apps and Integrations changes in v0.11.1

**Open WebUI** · 2026-08-25 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.1) · from [[Releases/Open WebUI/open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c|v0.11.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📽️ **Truer PowerPoint previews.** Slide previews now render tables, charts, connectors, gradients, theme colours, bullets, fonts, and text alignment far closer to the original, and the viewer lets you move between slides with the arrow keys or the scroll wheel while the thumbnail strip follows along. [Commit](https://github.com/open-webui/open-webui/commit/8dd23f74c9a59fdfbdaefb4a403ef79bdd3dfed9), [Commit](https://github.com/open-webui/open-webui/commit/048c06399363baac4046717129f072172ee90805), [Commit](https://github.com/open-webui/open-webui/commit/c93c6d6fc48ee8870eec349cb4c5af88c9435cfb), [Commit](https://github.com/open-webui/open-webui/commit/76583749edb966c0239ce203a84c1ee8d8c7faee), [Commit](https://github.com/open-webui/open-webui/commit/b3a5fd3875dc3c29a11eb5435438e55685cad639), [Commit](https://github.com/open-webui/open-webui/commit/794671a9883d5e067c407067f324ffa25ed38e3f), [Commit](https://github.com/open-webui/open-webui/commit/f96b717566b2084bd5fe70fb622ab66b5a643c0d), [Commit](https://github.com/open-webui/open-webui/commit/b7292890ccea794750651abbcde01cda62551e1b), [Commit](https://github.com/open-webui/open-webui/commit/31d08d592c4ee46a7ce827d6ffdf8e3cf16bf2ac)

> ↔️ **Connectors in the side-by-side overview.** With the conversation overview laid out left to right, the lines between messages now join at the sides rather than the top and bottom, so they no longer cut across the boxes. [Commit](https://github.com/open-webui/open-webui/commit/6e468c5b9539d3b6057bab63d81e8d2974acff7b)

> 🔇 **Filter failures that said nothing.** When a filter's outlet or stream hook raises, the failure is now reported with the filter's name and a traceback at the default log level, where it was swallowed and left plugin authors with nothing to go on. [Commit](https://github.com/open-webui/open-webui/commit/35fbde0a3fb303b7076b03465b1a2b0ba832df53)

> 🐳 **Test-only packages removed from the image.** The container no longer ships pytest, pytest-docker, the Docker SDK, or netcat, none of which anything in Open WebUI used, so the image is smaller; anyone whose own tools or functions relied on those being present will need to install them themselves. [#28726](https://github.com/open-webui/open-webui/pull/28726)

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
- [[Changes/Open WebUI/2026-08-25-73-developer-workflow-changes-in-v0-11-1|73 Developer Workflow changes in v0.11.1]] · Developer Workflow
- [[Changes/Open WebUI/2026-08-25-8-memory-and-personalization-changes-in-v0-11-1|8 Memory and Personalization changes in v0.11.1]] · Memory and Personalization
- [[Changes/Open WebUI/2026-08-25-files-for-delegated-tasks-a-task-handed-to-a-sub-agent-can-now-carry-the-attachm|🤝 Files for delegated tasks. A task handed to a sub-agent can now carry…]] · Agent Mode
- [[Changes/Open WebUI/2026-08-25-4-enterprise-and-administration-changes-in-v0-11-1|4 Enterprise and Administration changes in v0.11.1]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-08-25-24-interface-experience-changes-in-v0-11-1|24 Interface Experience changes in v0.11.1]] · Interface Experience
- [[Changes/Open WebUI/2026-08-25-5-search-and-browsing-changes-in-v0-11-1|5 Search and Browsing changes in v0.11.1]] · Search and Browsing
- [[Changes/Open WebUI/2026-08-25-4-voice-and-audio-changes-in-v0-11-1|4 Voice and Audio changes in v0.11.1]] · Voice and Audio
- [[Changes/Open WebUI/2026-08-25-56-model-support-changes-in-v0-11-1|56 Model Support changes in v0.11.1]] · Model Support
- [[Changes/Open WebUI/2026-08-25-39-other-changes-in-v0-11-1|39 other changes in v0.11.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-08-25 · Gemini CLI · [[Changes/Gemini CLI/2026-08-25-ssr-agent-issue-fix-21919-fix-typescript-strict-null-errors-in-integration-tests|SSR Agent Issue Fix (21919): Fix TypeScript strict-null errors in integration tests]]
- Later: 2026-08-25 · Raycast · [[Changes/Raycast/2026-08-25-ai-added-support-for-mentioning-ai-extensions-when-replying-to-a-question-asked|AI : Added support for mentioning AI extensions when replying to a question asked…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-08-25-c19990&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-08-25-4-apps-and-integrations-changes-in-v0-11-1.md%0ACard%20ID%3A%20open-webui-2026-08-25-c19990%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->