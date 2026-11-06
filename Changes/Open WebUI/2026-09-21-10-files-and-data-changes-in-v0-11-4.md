---
card_id: open-webui-2026-09-21-680e08
date: '2026-09-21'
description: "Open WebUI · 2026-09-21 · Files and Data: 10 changes in v0.11.4 — \U0001F9D7
  **Tagged blocks while streaming.** A reply using reasoning, solution or code interpreter…"
diffusion:
  first_in_tracked: '[[Changes/Dify/2023-05-25-2-files-and-data-changes-in-0-2-2|2
    Files and Data changes in 0.2.2]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1215
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: file-data
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f27e621862990b2694690b613edd463047e063de1530e10777903489f081a2a8
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-09-21-680e08
  comparison: ''
  date: '2026-09-21'
  description: 'Open WebUI — v0.11.4: 10 Files and Data changes'
  evidence:
  - quote: "\U0001F9D7 **Tagged blocks while streaming.** A reply using reasoning,
      solution or code interpreter tags briefly showed the raw tag text in the message
      as it arrived, because the chunk carrying it reached the browser before the
      cleaned output did; the cleaned output is now sent the moment a tag is taken
      out, and the code an interpreter block writes fills that block rather than the
      message body. [Commit](https://github.com/open-webui/open-webui/commit/58b36765a7c20f5943a3180bd289de48876d0878)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F4D7 **Excel in the code interpreter.** Reading or writing a spreadsheet
      in code the browser runs failed outright because the library that handles them
      never reached the browser, and it is now shipped alongside the rest. [#30140](https://github.com/open-webui/open-webui/pull/30140),
      [#30130](https://github.com/open-webui/open-webui/issues/30130)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F5DE **MinerU key in local mode.** The document settings save again
      in local mode with the MinerU key left empty, where the form demanded a key
      it did not need. [#30299](https://github.com/open-webui/open-webui/pull/30299),
      [#30298](https://github.com/open-webui/open-webui/issues/30298)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001FAE7 **Empty document ids.** A save arriving for a document with
      no id at all was filed against that empty id and never cleared, so anyone signed
      in could pile them up; nothing is filed for it now. [#29980](https://github.com/open-webui/open-webui/pull/29980)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F4CE **Safer Word document previews.** Previewing a Word document
      no longer renders an HTML sub-document embedded inside it, and a link in one
      opens only where it points at a web address, a mail address or a telephone number.
      [#29699](https://github.com/open-webui/open-webui/pull/29699)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F527 **Arduino sketches upload to knowledge.** A sketch file now
      reaches the plain text reader like the C++ and header files beside it, rather
      than being handed to a document extraction server that could make nothing of
      it and failing the upload. [#29673](https://github.com/open-webui/open-webui/pull/29673),
      [#29670](https://github.com/open-webui/open-webui/issues/29670)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: ✂️ **Slim document splitting.** Splitting a document along a downloaded
      tokenizer is unavailable on the slim image, which leaves splitting by character
      or by token count. [Commit](https://github.com/open-webui/open-webui/commit/cb942bb94c8dc7941336088fb3392e2398ff56c1)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F4C3 **Slim document readers.** The slim image reads text, Markdown,
      CSV, HTML and XML files as they are; uploading a PDF, a Word file or a presentation
      fails unless one of the external document extractors is configured. [Commit](https://github.com/open-webui/open-webui/commit/cb942bb94c8dc7941336088fb3392e2398ff56c1)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F4E5 **Slim code interpreter packages.** The slim image leaves out
      the code interpreter's packages, so the browser fetches numpy, pandas, matplotlib,
      scikit-learn and the rest from \"cdn.jsdelivr.net\" and the interpreter stops
      working where that is blocked. [Commit](https://github.com/open-webui/open-webui/commit/98fcb844e1b19f7dd6289af26273cdec5447dc52)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F9FA **LangChain community removal.** The readers for text, HTML,
      Word, CSV, PDF and Azure Document Intelligence are now written here rather than
      taken from \"langchain-community\", which is no longer installed; a tool or
      function importing it has to name it in its own requirements from now on. [Commit](https://github.com/open-webui/open-webui/commit/05484aa055a868a49842e1ddff169c19c98b755b)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 10-files-and-data-changes-in-v0-11-4
  source_release: open-webui-2026-09-21-v0-11-4-github-393232555-90de9130
  source_type: github_releases
  theme: file-data
  title: 10 Files and Data changes in v0.11.4
  type: change
related_changes:
- '[[Changes/Claude/2026-09-16-create-designs-decks-and-docs-in-any-conversation|Create
  designs, decks, and docs in any conversation]]'
- '[[Changes/OpenHands/2026-09-16-feat-track-authenticated-canvas-arrivals-by-neubig-in-https-github-com-openhands|feat:
  track authenticated Canvas arrivals]]'
- '[[Changes/Claude Code/2026-09-17-claude-tag-removed-the-repeated-guest-attribution-note-claude-appended-to-a-slac|Claude
  Tag Removed the repeated guest-attribution note Claude appended to a Slack…]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-09-21-v0-11-4-github-393232555-90de9130|open-webui-2026-09-21-v0-11-4-github-393232555-90de9130]]'
source_type: github_releases
theme: file-data
title: 10 Files and Data changes in v0.11.4
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Files and Data changes in v0.11.4

**Open WebUI** · 2026-09-21 · [[Themes/file-data|Files and Data]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.4) · from [[Releases/Open WebUI/open-webui-2026-09-21-v0-11-4-github-393232555-90de9130|v0.11.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🧗 **Tagged blocks while streaming.** A reply using reasoning, solution or code interpreter tags briefly showed the raw tag text in the message as it arrived, because the chunk carrying it reached the browser before the cleaned output did; the cleaned output is now sent the moment a tag is taken out, and the code an interpreter block writes fills that block rather than the message body. [Commit](https://github.com/open-webui/open-webui/commit/58b36765a7c20f5943a3180bd289de48876d0878)

> 📗 **Excel in the code interpreter.** Reading or writing a spreadsheet in code the browser runs failed outright because the library that handles them never reached the browser, and it is now shipped alongside the rest. [#30140](https://github.com/open-webui/open-webui/pull/30140), [#30130](https://github.com/open-webui/open-webui/issues/30130)

> 🗞 **MinerU key in local mode.** The document settings save again in local mode with the MinerU key left empty, where the form demanded a key it did not need. [#30299](https://github.com/open-webui/open-webui/pull/30299), [#30298](https://github.com/open-webui/open-webui/issues/30298)

> 🫧 **Empty document ids.** A save arriving for a document with no id at all was filed against that empty id and never cleared, so anyone signed in could pile them up; nothing is filed for it now. [#29980](https://github.com/open-webui/open-webui/pull/29980)

> 📎 **Safer Word document previews.** Previewing a Word document no longer renders an HTML sub-document embedded inside it, and a link in one opens only where it points at a web address, a mail address or a telephone number. [#29699](https://github.com/open-webui/open-webui/pull/29699)

> 🔧 **Arduino sketches upload to knowledge.** A sketch file now reaches the plain text reader like the C++ and header files beside it, rather than being handed to a document extraction server that could make nothing of it and failing the upload. [#29673](https://github.com/open-webui/open-webui/pull/29673), [#29670](https://github.com/open-webui/open-webui/issues/29670)

> ✂️ **Slim document splitting.** Splitting a document along a downloaded tokenizer is unavailable on the slim image, which leaves splitting by character or by token count. [Commit](https://github.com/open-webui/open-webui/commit/cb942bb94c8dc7941336088fb3392e2398ff56c1)

> 📃 **Slim document readers.** The slim image reads text, Markdown, CSV, HTML and XML files as they are; uploading a PDF, a Word file or a presentation fails unless one of the external document extractors is configured. [Commit](https://github.com/open-webui/open-webui/commit/cb942bb94c8dc7941336088fb3392e2398ff56c1)

> 📥 **Slim code interpreter packages.** The slim image leaves out the code interpreter's packages, so the browser fetches numpy, pandas, matplotlib, scikit-learn and the rest from "cdn.jsdelivr.net" and the interpreter stops working where that is blocked. [Commit](https://github.com/open-webui/open-webui/commit/98fcb844e1b19f7dd6289af26273cdec5447dc52)

> 🧺 **LangChain community removal.** The readers for text, HTML, Word, CSV, PDF and Azure Document Intelligence are now written here rather than taken from "langchain-community", which is no longer installed; a tool or function importing it has to name it in its own requirements from now on. [Commit](https://github.com/open-webui/open-webui/commit/05484aa055a868a49842e1ddff169c19c98b755b)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-09-21-4-safety-and-privacy-changes-in-v0-11-4|4 Safety and Privacy changes in v0.11.4]] · Safety and Privacy
- [[Changes/Open WebUI/2026-09-21-3-context-window-changes-in-v0-11-4|3 Context Window changes in v0.11.4]] · Context Window
- [[Changes/Open WebUI/2026-09-21-general-improvements-various-improvements-were-implemented-across-the-applicatio|🔄 General improvements. Various improvements were implemented across…]] · Reliability and Performance
- [[Changes/Open WebUI/2026-09-21-6-account-and-access-changes-in-v0-11-4|6 Account and Access changes in v0.11.4]] · Account and Access
- [[Changes/Open WebUI/2026-09-21-39-developer-workflow-changes-in-v0-11-4|39 Developer Workflow changes in v0.11.4]] · Developer Workflow
- [[Changes/Open WebUI/2026-09-21-2-image-generation-changes-in-v0-11-4|2 Image Generation changes in v0.11.4]] · Image Generation
- [[Changes/Open WebUI/2026-09-21-4-collaboration-changes-in-v0-11-4|4 Collaboration changes in v0.11.4]] · Collaboration
- [[Changes/Open WebUI/2026-09-21-5-voice-and-audio-changes-in-v0-11-4|5 Voice and Audio changes in v0.11.4]] · Voice and Audio
- [[Changes/Open WebUI/2026-09-21-21-editor-experience-changes-in-v0-11-4|21 Editor Experience changes in v0.11.4]] · Editor Experience
- [[Changes/Open WebUI/2026-09-21-6-memory-and-personalization-changes-in-v0-11-4|6 Memory and Personalization changes in v0.11.4]] · Memory and Personalization
- [[Changes/Open WebUI/2026-09-21-apple-device-replies-an-assistant-reply-no-longer-comes-up-blank-in-a-home-scree|📱 Apple device replies. An assistant reply no longer comes up blank in a home…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-09-21-3-apps-and-integrations-changes-in-v0-11-4|3 Apps and Integrations changes in v0.11.4]] · Apps and Integrations
- [[Changes/Open WebUI/2026-09-21-6-search-and-browsing-changes-in-v0-11-4|6 Search and Browsing changes in v0.11.4]] · Search and Browsing
- [[Changes/Open WebUI/2026-09-21-13-interface-experience-changes-in-v0-11-4|13 Interface Experience changes in v0.11.4]] · Interface Experience
- [[Changes/Open WebUI/2026-09-21-4-automation-and-scheduling-changes-in-v0-11-4|4 Automation and Scheduling changes in v0.11.4]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-09-21-41-model-support-changes-in-v0-11-4|41 Model Support changes in v0.11.4]] · Model Support
- [[Changes/Open WebUI/2026-09-21-5-enterprise-and-administration-changes-in-v0-11-4|5 Enterprise and Administration changes in v0.11.4]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-09-21-61-other-changes-in-v0-11-4|61 other changes in v0.11.4]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Files and Data

- Earlier: 2026-09-17 · Claude Code · [[Changes/Claude Code/2026-09-17-claude-tag-removed-the-repeated-guest-attribution-note-claude-appended-to-a-slac|Claude Tag Removed the repeated guest-attribution note Claude appended to a Slack…]]
- Later: 2026-09-22 · Codex CLI · [[Changes/Codex CLI/2026-09-22-46027-document-and-test-wildcards-in-network-proxy-domain-patterns-viyatb-oai|♯46027 Document and test ? wildcards in network proxy domain patterns @viyatb-oai]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-25 · Dify · [[Changes/Dify/2023-05-25-2-files-and-data-changes-in-0-2-2|2 Files and Data changes in 0.2.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-09-21-680e08&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-09-21-10-files-and-data-changes-in-v0-11-4.md%0ACard%20ID%3A%20open-webui-2026-09-21-680e08%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.4%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->