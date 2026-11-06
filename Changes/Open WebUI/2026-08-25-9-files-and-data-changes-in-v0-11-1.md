---
card_id: open-webui-2026-08-25-01c5a8
date: '2026-08-25'
description: "Open WebUI · 2026-08-25 · Files and Data: 9 changes in v0.11.1 — \U0001F40D
  **Much faster code interpreter output.** Printed output and generated images from
  code run…"
diffusion:
  first_in_tracked: '[[Changes/Dify/2023-05-25-2-files-and-data-changes-in-0-2-2|2
    Files and Data changes in 0.2.2]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1188
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: file-data
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 6670d56e864af24b724ae7954c40dd3ba0eff3911c37584e00855d0b4229c1f1
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-08-25-01c5a8
  comparison: ''
  date: '2026-08-25'
  description: 'Open WebUI — v0.11.1: 9 Files and Data changes'
  evidence:
  - quote: "\U0001F40D **Much faster code interpreter output.** Printed output and
      generated images from code run in chat appear much faster when the \"ENABLE_ORJSON\"
      option is turned on. [#27812](https://github.com/open-webui/open-webui/pull/27812)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F4D6 **Opening a document at the right page.** A model showing you
      a PDF, Word document, or slide deck from a terminal can now open it at a particular
      page or slide, so a reply that cites something on page 76 can put that page
      in front of you. [Commit](https://github.com/open-webui/open-webui/commit/fd8cc2ba4a226ccbf51e114c71f156676eabb2d9),
      [Commit](https://github.com/open-webui/open-webui/commit/cf4ac9c8db67031627f196fae894764367fba5b4),
      [Commit](https://github.com/open-webui/open-webui/commit/6cb2449ab70ed6aa5124fcd2b1291b48527af4cd)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F517 **Attaching any link.** Pasting a link into a chat or a knowledge
      base now works out what is behind it, downloading a document or image as a real
      attachment rather than treating everything as a web page to be read as text.
      [Commit](https://github.com/open-webui/open-webui/commit/8fbfd14a8b3fe7236883594fd18760076e4de0d5)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F4C4 **Faithful Word document previews.** Word documents now open
      as proper pages with headers, footers, footnotes, and embedded images intact,
      and can be zoomed, rather than being flattened into plain formatted text. [Commit](https://github.com/open-webui/open-webui/commit/ff7467b4c593f1e775311c088c63340d0cc1e4a2),
      [Commit](https://github.com/open-webui/open-webui/commit/060648f939447e2a9de390d05221ca896c50eeed)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F4D1 **Apache Tika 4 support.** Administrators extracting document
      text with Tika can now choose which server version they run, from Admin Settings
      under Documents or through \"TIKA_SERVER_VERSION\", where only Tika 3 was understood
      before. [Commit](https://github.com/open-webui/open-webui/commit/170ad0595d9440113721eb06375a2fc99aefaad1),
      [#28939](https://github.com/open-webui/open-webui/issues/28939)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F5A8️ **File and image detail parts on API requests.** A request
      sent to the OpenAI-compatible endpoint carrying an image detail level or a file
      part in its message content now forwards both to providers that use the Responses
      API, where they were dropped, while documents attached inside Open WebUI are
      unaffected because those still go through knowledge retrieval. [Commit](https://github.com/open-webui/open-webui/commit/ca4e07a40b4ff11989a25d84b517d3d0049f93ae)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F4C3 **Word and PowerPoint previews overflowing.** Previewing one
      of these files now keeps the document inside its frame, with the zoom and slide
      controls staying put rather than scrolling away, and a presentation opens on
      its current slide instead of below the visible area. [#28878](https://github.com/open-webui/open-webui/pull/28878),
      [#28877](https://github.com/open-webui/open-webui/issues/28877)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: ⛳ **Embedding servers behind a password.** An embedding server protected
      by a username and password rather than a key now works, where an empty key still
      sent an authorisation header, which such a server rejected and which made document
      uploads fail. [#28684](https://github.com/open-webui/open-webui/pull/28684),
      [#28683](https://github.com/open-webui/open-webui/issues/28683), [Commit](https://github.com/open-webui/open-webui/commit/97466deea105d6fdde60bf4d9401703fd32e03e9)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F4D3 **Notes opening blank.** A note whose shared editing session
      has not been started yet now opens with its stored content even when several
      people open it at once, where previously anyone but a lone first viewer got
      an empty document. [Commit](https://github.com/open-webui/open-webui/commit/5078d987f83943671f1d23ebe66bcc8d2af902c3)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 9-files-and-data-changes-in-v0-11-1
  source_release: open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c
  source_type: github_releases
  theme: file-data
  title: 9 Files and Data changes in v0.11.1
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-08-20-39283-document-secure-devcontainer-dns-exfiltration-risk-copyberry|♯39283
  Document secure devcontainer DNS exfiltration risk @copyberry]]'
- '[[Changes/OpenHands/2026-08-21-ci-bump-agent-canvas-chart-image-tag-on-release-by-aivong-openhands-in-https-git|ci:
  bump agent-canvas chart image tag on release]]'
- '[[Changes/Dify/2026-08-25-5-files-and-data-changes-in-1-17-0|5 Files and Data changes
  in 1.17.0]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c|open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c]]'
source_type: github_releases
theme: file-data
title: 9 Files and Data changes in v0.11.1
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Files and Data changes in v0.11.1

**Open WebUI** · 2026-08-25 · [[Themes/file-data|Files and Data]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.1) · from [[Releases/Open WebUI/open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c|v0.11.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🐍 **Much faster code interpreter output.** Printed output and generated images from code run in chat appear much faster when the "ENABLE_ORJSON" option is turned on. [#27812](https://github.com/open-webui/open-webui/pull/27812)

> 📖 **Opening a document at the right page.** A model showing you a PDF, Word document, or slide deck from a terminal can now open it at a particular page or slide, so a reply that cites something on page 76 can put that page in front of you. [Commit](https://github.com/open-webui/open-webui/commit/fd8cc2ba4a226ccbf51e114c71f156676eabb2d9), [Commit](https://github.com/open-webui/open-webui/commit/cf4ac9c8db67031627f196fae894764367fba5b4), [Commit](https://github.com/open-webui/open-webui/commit/6cb2449ab70ed6aa5124fcd2b1291b48527af4cd)

> 🔗 **Attaching any link.** Pasting a link into a chat or a knowledge base now works out what is behind it, downloading a document or image as a real attachment rather than treating everything as a web page to be read as text. [Commit](https://github.com/open-webui/open-webui/commit/8fbfd14a8b3fe7236883594fd18760076e4de0d5)

> 📄 **Faithful Word document previews.** Word documents now open as proper pages with headers, footers, footnotes, and embedded images intact, and can be zoomed, rather than being flattened into plain formatted text. [Commit](https://github.com/open-webui/open-webui/commit/ff7467b4c593f1e775311c088c63340d0cc1e4a2), [Commit](https://github.com/open-webui/open-webui/commit/060648f939447e2a9de390d05221ca896c50eeed)

> 📑 **Apache Tika 4 support.** Administrators extracting document text with Tika can now choose which server version they run, from Admin Settings under Documents or through "TIKA_SERVER_VERSION", where only Tika 3 was understood before. [Commit](https://github.com/open-webui/open-webui/commit/170ad0595d9440113721eb06375a2fc99aefaad1), [#28939](https://github.com/open-webui/open-webui/issues/28939)

> 🖨️ **File and image detail parts on API requests.** A request sent to the OpenAI-compatible endpoint carrying an image detail level or a file part in its message content now forwards both to providers that use the Responses API, where they were dropped, while documents attached inside Open WebUI are unaffected because those still go through knowledge retrieval. [Commit](https://github.com/open-webui/open-webui/commit/ca4e07a40b4ff11989a25d84b517d3d0049f93ae)

> 📃 **Word and PowerPoint previews overflowing.** Previewing one of these files now keeps the document inside its frame, with the zoom and slide controls staying put rather than scrolling away, and a presentation opens on its current slide instead of below the visible area. [#28878](https://github.com/open-webui/open-webui/pull/28878), [#28877](https://github.com/open-webui/open-webui/issues/28877)

> ⛳ **Embedding servers behind a password.** An embedding server protected by a username and password rather than a key now works, where an empty key still sent an authorisation header, which such a server rejected and which made document uploads fail. [#28684](https://github.com/open-webui/open-webui/pull/28684), [#28683](https://github.com/open-webui/open-webui/issues/28683), [Commit](https://github.com/open-webui/open-webui/commit/97466deea105d6fdde60bf4d9401703fd32e03e9)

> 📓 **Notes opening blank.** A note whose shared editing session has not been started yet now opens with its stored content even when several people open it at once, where previously anyone but a lone first viewer got an empty document. [Commit](https://github.com/open-webui/open-webui/commit/5078d987f83943671f1d23ebe66bcc8d2af902c3)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

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
- [[Changes/Open WebUI/2026-08-25-5-search-and-browsing-changes-in-v0-11-1|5 Search and Browsing changes in v0.11.1]] · Search and Browsing
- [[Changes/Open WebUI/2026-08-25-4-voice-and-audio-changes-in-v0-11-1|4 Voice and Audio changes in v0.11.1]] · Voice and Audio
- [[Changes/Open WebUI/2026-08-25-56-model-support-changes-in-v0-11-1|56 Model Support changes in v0.11.1]] · Model Support
- [[Changes/Open WebUI/2026-08-25-39-other-changes-in-v0-11-1|39 other changes in v0.11.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Files and Data

- Earlier: 2026-08-25 · Dify · [[Changes/Dify/2026-08-25-5-files-and-data-changes-in-1-17-0|5 Files and Data changes in 1.17.0]]
- Later: 2026-08-27 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-08-27-canvas-windows-open-and-refresh-in-the-background-instead-of-stealing-focus-from|Canvas windows open and refresh in the background instead of stealing focus…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-25 · Dify · [[Changes/Dify/2023-05-25-2-files-and-data-changes-in-0-2-2|2 Files and Data changes in 0.2.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-08-25-01c5a8&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-08-25-9-files-and-data-changes-in-v0-11-1.md%0ACard%20ID%3A%20open-webui-2026-08-25-01c5a8%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->