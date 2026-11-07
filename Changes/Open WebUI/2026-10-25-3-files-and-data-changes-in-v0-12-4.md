---
card_id: open-webui-2026-10-25-d463c4
date: '2026-10-25'
description: "Open WebUI · 2026-10-25 · Files and Data: 3 changes in v0.12.4 — \U0001F441️
  **PDF image OCR stays light.** With PDF Extract Images (OCR) on, reading text from
  images…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-in-document-export-there-s-a-field-where-the-user-can-add-the-number-of-seconds|Timecode
    offset]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2594
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: file-data
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9f9a9419362af09e4696efe6ceec7c0de1ac61e0bdca14ffa66e3c7701b09aaf
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-10-25-d463c4
  comparison: ''
  date: '2026-10-25'
  description: 'Open WebUI — v0.12.4: 3 Files and Data changes'
  evidence:
  - quote: "\U0001F441️ **PDF image OCR stays light.** With PDF Extract Images (OCR)
      on, reading text from images in PDFs now uses one processor thread per upload
      by default, so uploads no longer start a thread pool the size of the server's
      cores that could slow the whole server down, and administrators can pass their
      own RapidOCR settings with \"RAPIDOCR_PARAMS\". [Commit](https://github.com/open-webui/open-webui/commit/56c570afc36e6dae528563059e30b1e030628734),
      [#32844](https://github.com/open-webui/open-webui/issues/32844)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F4CE **Attachments in the chat input.** An attached webpage now
      stays when file upload is not allowed, and a file's Entire Document switch shows
      that file's own setting after another attachment is removed. [#32701](https://github.com/open-webui/open-webui/pull/32701),
      [Commit](https://github.com/open-webui/open-webui/commit/bb8d49ff31d3503f91dff2d6e60b4376e021d2f7),
      [#32700](https://github.com/open-webui/open-webui/issues/32700), [#32699](https://github.com/open-webui/open-webui/pull/32699),
      [Commit](https://github.com/open-webui/open-webui/commit/a944564c20a3c207c6987e49d10cc01658e50b67),
      [#32698](https://github.com/open-webui/open-webui/issues/32698)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F4D1 **MinerU key in local mode.** Document extraction with MinerU
      in local mode now sends the configured API key to MinerU 4.x servers that require
      one, where every document failed. [#32838](https://github.com/open-webui/open-webui/pull/32838),
      [Commit](https://github.com/open-webui/open-webui/commit/3e0564d11a06052d8042fffc95b138dcbde5df6b),
      [#32836](https://github.com/open-webui/open-webui/issues/32836)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 3-files-and-data-changes-in-v0-12-4
  source_release: open-webui-2026-10-25-v0-12-4-github-423239437-ffa84a79
  source_type: github_releases
  theme: file-data
  title: 3 Files and Data changes in v0.12.4
  type: change
related_changes:
- '[[Changes/v0/2026-10-16-polished-the-design-mode-canvas-toolbar-and-panel-with-crisper-selection-real-fo|Polished
  the Design Mode canvas, toolbar, and panel, with crisper selection, real…]]'
- '[[Changes/Dify/2026-10-23-8-files-and-data-changes-in-1-18-0|8 Files and Data changes
  in 1.18.0]]'
- '[[Changes/OpenHands/2026-10-23-feat-canvas-quiet-backend-logs-by-default-by-neubig-in-https-github-com-openhand|feat(canvas):
  quiet backend logs by default]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-10-25-v0-12-4-github-423239437-ffa84a79|open-webui-2026-10-25-v0-12-4-github-423239437-ffa84a79]]'
source_type: github_releases
theme: file-data
title: 3 Files and Data changes in v0.12.4
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Files and Data changes in v0.12.4

**Open WebUI** · 2026-10-25 · [[Themes/file-data|Files and Data]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.4) · from [[Releases/Open WebUI/open-webui-2026-10-25-v0-12-4-github-423239437-ffa84a79|v0.12.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 👁️ **PDF image OCR stays light.** With PDF Extract Images (OCR) on, reading text from images in PDFs now uses one processor thread per upload by default, so uploads no longer start a thread pool the size of the server's cores that could slow the whole server down, and administrators can pass their own RapidOCR settings with "RAPIDOCR_PARAMS". [Commit](https://github.com/open-webui/open-webui/commit/56c570afc36e6dae528563059e30b1e030628734), [#32844](https://github.com/open-webui/open-webui/issues/32844)

> 📎 **Attachments in the chat input.** An attached webpage now stays when file upload is not allowed, and a file's Entire Document switch shows that file's own setting after another attachment is removed. [#32701](https://github.com/open-webui/open-webui/pull/32701), [Commit](https://github.com/open-webui/open-webui/commit/bb8d49ff31d3503f91dff2d6e60b4376e021d2f7), [#32700](https://github.com/open-webui/open-webui/issues/32700), [#32699](https://github.com/open-webui/open-webui/pull/32699), [Commit](https://github.com/open-webui/open-webui/commit/a944564c20a3c207c6987e49d10cc01658e50b67), [#32698](https://github.com/open-webui/open-webui/issues/32698)

> 📑 **MinerU key in local mode.** Document extraction with MinerU in local mode now sends the configured API key to MinerU 4.x servers that require one, where every document failed. [#32838](https://github.com/open-webui/open-webui/pull/32838), [Commit](https://github.com/open-webui/open-webui/commit/3e0564d11a06052d8042fffc95b138dcbde5df6b), [#32836](https://github.com/open-webui/open-webui/issues/32836)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-10-25-16-model-support-changes-in-v0-12-4|16 Model Support changes in v0.12.4]] · Model Support
- [[Changes/Open WebUI/2026-10-25-10-safety-and-privacy-changes-in-v0-12-4|10 Safety and Privacy changes in v0.12.4]] · Safety and Privacy
- [[Changes/Open WebUI/2026-10-25-13-interface-experience-changes-in-v0-12-4|13 Interface Experience changes in v0.12.4]] · Interface Experience
- [[Changes/Open WebUI/2026-10-25-images-settings-save-admins-can-now-save-images-settings-while-image-generation|🖌️ Images settings save. Admins can now save Images settings while Image…]] · Image Generation
- [[Changes/Open WebUI/2026-10-25-4-voice-and-audio-changes-in-v0-12-4|4 Voice and Audio changes in v0.12.4]] · Voice and Audio
- [[Changes/Open WebUI/2026-10-25-4-context-window-changes-in-v0-12-4|4 Context Window changes in v0.12.4]] · Context Window
- [[Changes/Open WebUI/2026-10-25-5-apps-and-integrations-changes-in-v0-12-4|5 Apps and Integrations changes in v0.12.4]] · Apps and Integrations
- [[Changes/Open WebUI/2026-10-25-49-developer-workflow-changes-in-v0-12-4|49 Developer Workflow changes in v0.12.4]] · Developer Workflow
- [[Changes/Open WebUI/2026-10-25-4-editor-experience-changes-in-v0-12-4|4 Editor Experience changes in v0.12.4]] · Editor Experience
- [[Changes/Open WebUI/2026-10-25-3-reliability-and-performance-changes-in-v0-12-4|3 Reliability and Performance changes in v0.12.4]] · Reliability and Performance
- [[Changes/Open WebUI/2026-10-25-5-account-and-access-changes-in-v0-12-4|5 Account and Access changes in v0.12.4]] · Account and Access
- [[Changes/Open WebUI/2026-10-25-shared-chat-pages-load-once-chats-opened-under-s-through-a-share-link-or-by-an-a|🔗 Shared chat pages load once. Chats opened under /s/, through a share link…]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-10-25-web-search-settings-save-admins-can-now-save-web-search-settings-such-as-the-web|🌍 Web Search settings save. Admins can now save Web Search settings such…]] · Search and Browsing
- [[Changes/Open WebUI/2026-10-25-translation-updates-translations-for-korean-cebuano-thai-german-japanese-vietnam|🌐 Translation updates. Translations for Korean, Cebuano, Thai, German, Japanese…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Files and Data

- Earlier: 2026-10-23 · OpenHands · [[Changes/OpenHands/2026-10-23-feat-canvas-quiet-backend-logs-by-default-by-neubig-in-https-github-com-openhand|feat(canvas): quiet backend logs by default]]
- Later: 2026-10-26 · AnythingLLM · [[Changes/AnythingLLM/2026-10-26-2-files-and-data-changes-in-v1-19-0|2 Files and Data changes in v1.19.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-in-document-export-there-s-a-field-where-the-user-can-add-the-number-of-seconds|Timecode offset]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-25-d463c4&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-25-3-files-and-data-changes-in-v0-12-4.md%0ACard%20ID%3A%20open-webui-2026-10-25-d463c4%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.4%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->