---
card_id: open-webui-2026-07-27-2d640e
date: '2026-07-27'
description: 'Open WebUI · 2026-07-27 · Voice and Audio: 4 changes in v0.11.0 — ☑️
  **Searchable model pickers.** When editing a model, the Tools, Skills, Knowledge,
  Voice…'
diffusion:
  first_in_tracked: '[[Changes/Dify/2023-07-10-2-voice-and-audio-changes-in-0-3-7|2
    Voice and Audio changes in 0.3.7]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1113
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: voice
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: c363c857c93f4cac2fa62de4d09641d7dd8f3f790055916a239de8f0b7a3301a
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-07-27-2d640e
  comparison: ''
  date: '2026-07-27'
  description: 'Open WebUI — v0.11.0: 4 Voice and Audio changes'
  evidence:
  - quote: ☑️ **Searchable model pickers.** When editing a model, the Tools, Skills,
      Knowledge, Voice, Filters and Actions pickers now let you search and toggle
      items in place, select or clear them all at once, and see what is active at
      a glance. [Commit](https://github.com/open-webui/open-webui/commit/e355959e9156fd61a1105953d731d007fbb4bae3),
      [Commit](https://github.com/open-webui/open-webui/commit/e1f96aa20ef80c8b01e3a81039d2cca3001d0ef5),
      [Commit](https://github.com/open-webui/open-webui/commit/fa889837e9e90c7284def56fac2daed20a3ce699),
      [Commit](https://github.com/open-webui/open-webui/commit/5424ac58917d2a21f21256b62d1c42f1a8c51c51),
      [Commit](https://github.com/open-webui/open-webui/commit/ea2e3d0afc76fa99f2af665fd50425dd28d000d5),
      [Commit](https://github.com/open-webui/open-webui/commit/cda5bdb9d42886dfe74d05907179e3f96097030c),
      [#26758](https://github.com/open-webui/open-webui/issues/26758)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F4E8 **Fewer settings lookups when sending a message.** Sending
      a chat message now reads the settings behind tools, file retrieval, voice, skills
      and the code interpreter in fewer trips to the database, so replies start sooner.
      [#27223](https://github.com/open-webui/open-webui/pull/27223)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F399️ **Dictation repeating earlier speech.** Dictating into the
      message box no longer re-inserts everything you said in previous recordings,
      and cancelling a recording no longer inserts the text anyway. [#26793](https://github.com/open-webui/open-webui/pull/26793),
      [#26784](https://github.com/open-webui/open-webui/issues/26784)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F9E9 **Order of long transcriptions.** A long recording split into
      pieces for transcription is now reassembled in the order it was spoken, instead
      of sections sometimes appearing out of sequence in the transcript and everything
      read from it. [#27417](https://github.com/open-webui/open-webui/pull/27417),
      [#27143](https://github.com/open-webui/open-webui/issues/27143)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 4-voice-and-audio-changes-in-v0-11-0
  source_release: open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f
  source_type: github_releases
  theme: voice
  title: 4 Voice and Audio changes in v0.11.0
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-07-27-python-sdk|Python SDK]]'
- '[[Changes/ElevenLabs/2026-07-27-javascript-sdk|JavaScript SDK]]'
- '[[Changes/ElevenLabs/2026-07-27-voices|Voices]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f|open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f]]'
source_type: github_releases
theme: voice
title: 4 Voice and Audio changes in v0.11.0
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Voice and Audio changes in v0.11.0

**Open WebUI** · 2026-07-27 · [[Themes/voice|Voice and Audio]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.0) · from [[Releases/Open WebUI/open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f|v0.11.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> ☑️ **Searchable model pickers.** When editing a model, the Tools, Skills, Knowledge, Voice, Filters and Actions pickers now let you search and toggle items in place, select or clear them all at once, and see what is active at a glance. [Commit](https://github.com/open-webui/open-webui/commit/e355959e9156fd61a1105953d731d007fbb4bae3), [Commit](https://github.com/open-webui/open-webui/commit/e1f96aa20ef80c8b01e3a81039d2cca3001d0ef5), [Commit](https://github.com/open-webui/open-webui/commit/fa889837e9e90c7284def56fac2daed20a3ce699), [Commit](https://github.com/open-webui/open-webui/commit/5424ac58917d2a21f21256b62d1c42f1a8c51c51), [Commit](https://github.com/open-webui/open-webui/commit/ea2e3d0afc76fa99f2af665fd50425dd28d000d5), [Commit](https://github.com/open-webui/open-webui/commit/cda5bdb9d42886dfe74d05907179e3f96097030c), [#26758](https://github.com/open-webui/open-webui/issues/26758)

> 📨 **Fewer settings lookups when sending a message.** Sending a chat message now reads the settings behind tools, file retrieval, voice, skills and the code interpreter in fewer trips to the database, so replies start sooner. [#27223](https://github.com/open-webui/open-webui/pull/27223)

> 🎙️ **Dictation repeating earlier speech.** Dictating into the message box no longer re-inserts everything you said in previous recordings, and cancelling a recording no longer inserts the text anyway. [#26793](https://github.com/open-webui/open-webui/pull/26793), [#26784](https://github.com/open-webui/open-webui/issues/26784)

> 🧩 **Order of long transcriptions.** A long recording split into pieces for transcription is now reassembled in the order it was spoken, instead of sections sometimes appearing out of sequence in the transcript and everything read from it. [#27417](https://github.com/open-webui/open-webui/pull/27417), [#27143](https://github.com/open-webui/open-webui/issues/27143)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-07-27-9-automation-and-scheduling-changes-in-v0-11-0|9 Automation and Scheduling changes in v0.11.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-07-27-13-safety-and-privacy-changes-in-v0-11-0|13 Safety and Privacy changes in v0.11.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-07-27-62-developer-workflow-changes-in-v0-11-0|62 Developer Workflow changes in v0.11.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-07-27-19-interface-experience-changes-in-v0-11-0|19 Interface Experience changes in v0.11.0]] · Interface Experience
- [[Changes/Open WebUI/2026-07-27-7-memory-and-personalization-changes-in-v0-11-0|7 Memory and Personalization changes in v0.11.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-07-27-sub-agents-administrators-can-now-enable-sub-agents-which-let-a-model-hand-parts|🤖 Sub-agents. Administrators can now enable sub-agents, which let a model hand…]] · Agent Mode
- [[Changes/Open WebUI/2026-07-27-media-types-an-extraction-engine-may-handle-administrators-can-now-list-which-im|🖼️ Media types an extraction engine may handle. Administrators can now list…]] · Multimodal Input
- [[Changes/Open WebUI/2026-07-27-15-account-and-access-changes-in-v0-11-0|15 Account and Access changes in v0.11.0]] · Account and Access
- [[Changes/Open WebUI/2026-07-27-shared-image-checkpoint-changes-only-administrators-can-now-change-the-instance|🖌️ Shared image checkpoint changes. Only administrators can now change…]] · Image Generation
- [[Changes/Open WebUI/2026-07-27-7-search-and-browsing-changes-in-v0-11-0|7 Search and Browsing changes in v0.11.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-07-27-2-collaboration-changes-in-v0-11-0|2 Collaboration changes in v0.11.0]] · Collaboration
- [[Changes/Open WebUI/2026-07-27-6-apps-and-integrations-changes-in-v0-11-0|6 Apps and Integrations changes in v0.11.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-07-27-3-enterprise-and-administration-changes-in-v0-11-0|3 Enterprise and Administration changes in v0.11.0]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-07-27-9-context-window-changes-in-v0-11-0|9 Context Window changes in v0.11.0]] · Context Window
- [[Changes/Open WebUI/2026-07-27-12-reliability-and-performance-changes-in-v0-11-0|12 Reliability and Performance changes in v0.11.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-07-27-2-pricing-model-changes-in-v0-11-0|2 Pricing Model changes in v0.11.0]] · Pricing Model
- [[Changes/Open WebUI/2026-07-27-9-files-and-data-changes-in-v0-11-0|9 Files and Data changes in v0.11.0]] · Files and Data
- [[Changes/Open WebUI/2026-07-27-39-model-support-changes-in-v0-11-0|39 Model Support changes in v0.11.0]] · Model Support
- [[Changes/Open WebUI/2026-07-27-7-editor-experience-changes-in-v0-11-0|7 Editor Experience changes in v0.11.0]] · Editor Experience
- [[Changes/Open WebUI/2026-07-27-2-mobile-and-desktop-changes-in-v0-11-0|2 Mobile and Desktop changes in v0.11.0]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-07-27-42-other-changes-in-v0-11-0|42 other changes in v0.11.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Voice and Audio

- Earlier: 2026-07-27 · ElevenLabs · [[Changes/ElevenLabs/2026-07-27-voices|Voices]]
- Later: 2026-07-28 · Dify · [[Changes/Dify/2026-07-28-returned-400-instead-of-500-when-file-field-is-missing-from-audio-to-text-endpoi|Returned 400 instead of 500 when file field is missing from audio-to-text…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-10 · Dify · [[Changes/Dify/2023-07-10-2-voice-and-audio-changes-in-0-3-7|2 Voice and Audio changes in 0.3.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-07-27-2d640e&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-07-27-4-voice-and-audio-changes-in-v0-11-0.md%0ACard%20ID%3A%20open-webui-2026-07-27-2d640e%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->