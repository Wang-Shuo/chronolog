---
card_id: open-webui-2026-06-29-051a84
date: '2026-06-29'
description: "Open WebUI · 2026-06-29 · Files and Data: 5 changes in v0.10.0 — \U0001F4C4
  **File details forwarded to external document extractors.** External custom…"
diffusion:
  first_in_tracked: '[[Changes/Dify/2023-05-25-2-files-and-data-changes-in-0-2-2|2
    Files and Data changes in 0.2.2]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1131
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: file-data
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 0843c477cf3bc0ddd590f472f090859d0be3ac30aed1e712b8e09f899afd92ff
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-06-29-051a84
  comparison: ''
  date: '2026-06-29'
  description: 'Open WebUI — v0.10.0: 5 Files and Data changes'
  evidence:
  - quote: "\U0001F4C4 **File details forwarded to external document extractors.**
      External custom document-extraction servers now receive the file's ID, name,
      and content type, and these are also available as custom header variables, so
      extraction can be tailored per file. [Commit](https://github.com/open-webui/open-webui/commit/b1c2536ed2f8639efade04618018e6de9b332df2),
      [#26259](https://github.com/open-webui/open-webui/issues/26259)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F4D1 **More robust MinerU document processing.** Document processing
      through MinerU now handles its ZIP results more safely, including very large
      outputs. [Commit](https://github.com/open-webui/open-webui/commit/23d03d6aaebcced6c1e39e98dfff76ab73df8804),
      [#26263](https://github.com/open-webui/open-webui/pull/26263)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F590️ **Sidebar drags don't trigger uploads.** Dragging a chat item
      in the sidebar no longer shows the file-upload overlay. [#25675](https://github.com/open-webui/open-webui/pull/25675)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F5C2️ **Empty metadata no longer breaks Chroma indexing.** Document
      metadata with empty values is now filtered out before indexing, fixing a case
      that could fail on Chroma. [Commit](https://github.com/open-webui/open-webui/commit/118549caf3),
      [#26342](https://github.com/open-webui/open-webui/pull/26342), [#26339](https://github.com/open-webui/open-webui/issues/26339)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F524 **Documents with special tokens index correctly.** Measuring
      chunk sizes no longer fails when a document contains text that looks like a
      special token. [#26210](https://github.com/open-webui/open-webui/pull/26210)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 5-files-and-data-changes-in-v0-10-0
  source_release: open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01
  source_type: github_releases
  theme: file-data
  title: 5 Files and Data changes in v0.10.0
  type: change
related_changes:
- '[[Changes/Ollama/2026-06-25-docs-document-max-think-level-by-parthsareen-in-https-github-com-ollama-ollama-p|docs:
  document max think level]]'
- '[[Changes/ChatGPT/2026-06-26-the-personal-finance-experience-in-chatgpt-is-rolling-out-to-plus-users-in-the-u|Personal
  finance in ChatGPT expands to Plus users and Android]]'
- '[[Changes/Claude Code/2026-06-29-added-clickable-file-attachments-in-chat-cmd-ctrl-click-reveals-the-file-in-find|Added
  clickable file attachments in chat]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01|open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01]]'
source_type: github_releases
theme: file-data
title: 5 Files and Data changes in v0.10.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Files and Data changes in v0.10.0

**Open WebUI** · 2026-06-29 · [[Themes/file-data|Files and Data]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.10.0) · from [[Releases/Open WebUI/open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01|v0.10.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📄 **File details forwarded to external document extractors.** External custom document-extraction servers now receive the file's ID, name, and content type, and these are also available as custom header variables, so extraction can be tailored per file. [Commit](https://github.com/open-webui/open-webui/commit/b1c2536ed2f8639efade04618018e6de9b332df2), [#26259](https://github.com/open-webui/open-webui/issues/26259)

> 📑 **More robust MinerU document processing.** Document processing through MinerU now handles its ZIP results more safely, including very large outputs. [Commit](https://github.com/open-webui/open-webui/commit/23d03d6aaebcced6c1e39e98dfff76ab73df8804), [#26263](https://github.com/open-webui/open-webui/pull/26263)

> 🖐️ **Sidebar drags don't trigger uploads.** Dragging a chat item in the sidebar no longer shows the file-upload overlay. [#25675](https://github.com/open-webui/open-webui/pull/25675)

> 🗂️ **Empty metadata no longer breaks Chroma indexing.** Document metadata with empty values is now filtered out before indexing, fixing a case that could fail on Chroma. [Commit](https://github.com/open-webui/open-webui/commit/118549caf3), [#26342](https://github.com/open-webui/open-webui/pull/26342), [#26339](https://github.com/open-webui/open-webui/issues/26339)

> 🔤 **Documents with special tokens index correctly.** Measuring chunk sizes no longer fails when a document contains text that looks like a special token. [#26210](https://github.com/open-webui/open-webui/pull/26210)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-06-29-5-memory-and-personalization-changes-in-v0-10-0|5 Memory and Personalization changes in v0.10.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-06-29-3-voice-and-audio-changes-in-v0-10-0|3 Voice and Audio changes in v0.10.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-06-29-14-interface-experience-changes-in-v0-10-0|14 Interface Experience changes in v0.10.0]] · Interface Experience
- [[Changes/Open WebUI/2026-06-29-4-collaboration-changes-in-v0-10-0|4 Collaboration changes in v0.10.0]] · Collaboration
- [[Changes/Open WebUI/2026-06-29-client-user-agent-forwarded-to-model-backends-the-browser-s-user-agent-is-now-pa|🪪 Client User-Agent forwarded to model backends. The browser's User-Agent is now…]] · Agent Mode
- [[Changes/Open WebUI/2026-06-29-scim-sync-can-t-demote-an-admin-a-scim-provisioning-sync-that-marks-a-user-inact|🛟 SCIM sync can't demote an admin. A SCIM provisioning sync that marks a user…]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-06-29-8-search-and-browsing-changes-in-v0-10-0|8 Search and Browsing changes in v0.10.0]] · Search and Browsing
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
## Nearby in Files and Data

- Earlier: 2026-06-29 · Claude Code · [[Changes/Claude Code/2026-06-29-added-clickable-file-attachments-in-chat-cmd-ctrl-click-reveals-the-file-in-find|Added clickable file attachments in chat]]
- Later: 2026-06-30 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-06-30-match-the-terminal-text-color-to-the-github-theme-canvas|Match the terminal text color to the GitHub theme canvas]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-25 · Dify · [[Changes/Dify/2023-05-25-2-files-and-data-changes-in-0-2-2|2 Files and Data changes in 0.2.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-06-29-051a84&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-06-29-5-files-and-data-changes-in-v0-10-0.md%0ACard%20ID%3A%20open-webui-2026-06-29-051a84%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.10.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->