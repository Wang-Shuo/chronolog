---
card_id: open-webui-2026-10-10-68cd1b
date: '2026-10-10'
description: "Open WebUI · 2026-10-10 · Files and Data: 6 changes in v0.12.0 — \U0001F4D1
  **Word and PowerPoint files from code.** The code interpreter can now create Word
  documents…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-in-document-export-there-s-a-field-where-the-user-can-add-the-number-of-seconds|Timecode
    offset]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2579
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: file-data
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 515d7ea2537d0193d1cf8150532775c2d4a11fee8db968d2a2e356285fb2e37b
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-10-10-68cd1b
  comparison: ''
  date: '2026-10-10'
  description: 'Open WebUI — v0.12.0: 6 Files and Data changes'
  evidence:
  - quote: "\U0001F4D1 **Word and PowerPoint files from code.** The code interpreter
      can now create Word documents and PowerPoint decks that open in Office, using
      libraries bundled with Open WebUI so it also works without internet access.
      [#30382](https://github.com/open-webui/open-webui/pull/30382), [#30361](https://github.com/open-webui/open-webui/issues/30361)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F5A8️ **Images in note PDFs.** Downloading a note as a PDF now includes
      the images pasted into it, where the PDF held only the title and text. [#30975](https://github.com/open-webui/open-webui/pull/30975),
      [#30974](https://github.com/open-webui/open-webui/issues/30974)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4C4 **Docling file names.** A document sent to a Docling server
      for extraction now carries only its file name, where it previously revealed
      the full path the file is stored under on the server. [#30357](https://github.com/open-webui/open-webui/pull/30357),
      [#30352](https://github.com/open-webui/open-webui/issues/30352)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F5C3️ **Live document saves limited to notes.** Live collaborative
      edits are now only saved for note documents, the only documents that have a
      save handler. [#30395](https://github.com/open-webui/open-webui/pull/30395)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001FAA3 **Limits for collaborative note editing.** Live collaborative
      editing now keeps a size budget per document and a limit on open documents per
      connection and stores only well-formed updates, so a client can no longer make
      the server hold unbounded editing data. [#31603](https://github.com/open-webui/open-webui/pull/31603)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F9FE **Document loader headers checked on save.** Invalid headers
      for the external document loader now show an error on save whichever extraction
      engine is selected, where they silently kept the documents settings from saving.
      [#30434](https://github.com/open-webui/open-webui/pull/30434), [#30294](https://github.com/open-webui/open-webui/issues/30294)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 6-files-and-data-changes-in-v0-12-0
  source_release: open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b
  source_type: github_releases
  theme: file-data
  title: 6 Files and Data changes in v0.12.0
  type: change
related_changes:
- '[[Changes/OpenHands/2026-10-06-6-files-and-data-changes-in-v1-25-0|6 Files and
  Data changes in v1.25.0]]'
- '[[Changes/Devin/2026-10-07-slack|Slack]]'
- '[[Changes/OpenHands/2026-10-08-2-files-and-data-changes-in-v1-26-0|2 Files and
  Data changes in v1.26.0]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b|open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b]]'
source_type: github_releases
theme: file-data
title: 6 Files and Data changes in v0.12.0
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Files and Data changes in v0.12.0

**Open WebUI** · 2026-10-10 · [[Themes/file-data|Files and Data]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.0) · from [[Releases/Open WebUI/open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b|v0.12.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📑 **Word and PowerPoint files from code.** The code interpreter can now create Word documents and PowerPoint decks that open in Office, using libraries bundled with Open WebUI so it also works without internet access. [#30382](https://github.com/open-webui/open-webui/pull/30382), [#30361](https://github.com/open-webui/open-webui/issues/30361)

> 🖨️ **Images in note PDFs.** Downloading a note as a PDF now includes the images pasted into it, where the PDF held only the title and text. [#30975](https://github.com/open-webui/open-webui/pull/30975), [#30974](https://github.com/open-webui/open-webui/issues/30974)

> 📄 **Docling file names.** A document sent to a Docling server for extraction now carries only its file name, where it previously revealed the full path the file is stored under on the server. [#30357](https://github.com/open-webui/open-webui/pull/30357), [#30352](https://github.com/open-webui/open-webui/issues/30352)

> 🗃️ **Live document saves limited to notes.** Live collaborative edits are now only saved for note documents, the only documents that have a save handler. [#30395](https://github.com/open-webui/open-webui/pull/30395)

> 🪣 **Limits for collaborative note editing.** Live collaborative editing now keeps a size budget per document and a limit on open documents per connection and stores only well-formed updates, so a client can no longer make the server hold unbounded editing data. [#31603](https://github.com/open-webui/open-webui/pull/31603)

> 🧾 **Document loader headers checked on save.** Invalid headers for the external document loader now show an error on save whichever extraction engine is selected, where they silently kept the documents settings from saving. [#30434](https://github.com/open-webui/open-webui/pull/30434), [#30294](https://github.com/open-webui/open-webui/issues/30294)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-10-10-5-reliability-and-performance-changes-in-v0-12-0|5 Reliability and Performance changes in v0.12.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-10-10-5-enterprise-and-administration-changes-in-v0-12-0|5 Enterprise and Administration changes in v0.12.0]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-10-10-7-apps-and-integrations-changes-in-v0-12-0|7 Apps and Integrations changes in v0.12.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-10-10-12-voice-and-audio-changes-in-v0-12-0|12 Voice and Audio changes in v0.12.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-10-10-27-developer-workflow-changes-in-v0-12-0|27 Developer Workflow changes in v0.12.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-10-10-5-image-generation-changes-in-v0-12-0|5 Image Generation changes in v0.12.0]] · Image Generation
- [[Changes/Open WebUI/2026-10-10-49-model-support-changes-in-v0-12-0|49 Model Support changes in v0.12.0]] · Model Support
- [[Changes/Open WebUI/2026-10-10-19-account-and-access-changes-in-v0-12-0|19 Account and Access changes in v0.12.0]] · Account and Access
- [[Changes/Open WebUI/2026-10-10-10-automation-and-scheduling-changes-in-v0-12-0|10 Automation and Scheduling changes in v0.12.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-10-10-3-mobile-and-desktop-changes-in-v0-12-0|3 Mobile and Desktop changes in v0.12.0]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-10-10-13-collaboration-changes-in-v0-12-0|13 Collaboration changes in v0.12.0]] · Collaboration
- [[Changes/Open WebUI/2026-10-10-2-memory-and-personalization-changes-in-v0-12-0|2 Memory and Personalization changes in v0.12.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-10-10-5-context-window-changes-in-v0-12-0|5 Context Window changes in v0.12.0]] · Context Window
- [[Changes/Open WebUI/2026-10-10-18-interface-experience-changes-in-v0-12-0|18 Interface Experience changes in v0.12.0]] · Interface Experience
- [[Changes/Open WebUI/2026-10-10-7-agent-mode-changes-in-v0-12-0|7 Agent Mode changes in v0.12.0]] · Agent Mode
- [[Changes/Open WebUI/2026-10-10-6-safety-and-privacy-changes-in-v0-12-0|6 Safety and Privacy changes in v0.12.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-10-10-21-editor-experience-changes-in-v0-12-0|21 Editor Experience changes in v0.12.0]] · Editor Experience
- [[Changes/Open WebUI/2026-10-10-4-search-and-browsing-changes-in-v0-12-0|4 Search and Browsing changes in v0.12.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-10-10-68-other-changes-in-v0-12-0|68 other changes in v0.12.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Files and Data

- Earlier: 2026-10-08 · OpenHands · [[Changes/OpenHands/2026-10-08-2-files-and-data-changes-in-v1-26-0|2 Files and Data changes in v1.26.0]]
- Later: 2026-10-10 · OpenClaw · [[Changes/OpenClaw/2026-10-10-2-files-and-data-changes-in-v2026-10-1|2 Files and Data changes in v2026.10.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-in-document-export-there-s-a-field-where-the-user-can-add-the-number-of-seconds|Timecode offset]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-10-68cd1b&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-10-6-files-and-data-changes-in-v0-12-0.md%0ACard%20ID%3A%20open-webui-2026-10-10-68cd1b%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->