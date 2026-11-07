---
card_id: open-webui-2026-08-25-ee5914
date: '2026-08-25'
description: "Open WebUI · 2026-08-25 · Voice and Audio: 4 changes in v0.11.1 — \U0001F399️
  **Voice mode in the notes editor.** The voice mode button is no longer offered in
  the chat…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-07-09-type-in-parentheses-to-add-notes-to-your-script-that-don-t-affect-the-audio-text|Support
    for Inline Notes]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2969
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: voice
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9b2661321562e51c770522972de33fd6b35a5b9b76bc5ebad7775918227ff339
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-08-25-ee5914
  comparison: ''
  date: '2026-08-25'
  description: 'Open WebUI — v0.11.1: 4 Voice and Audio changes'
  evidence:
  - quote: "\U0001F399️ **Voice mode in the notes editor.** The voice mode button
      is no longer offered in the chat embedded in a note, where it does not apply.
      [Commit](https://github.com/open-webui/open-webui/commit/9122c24ea2d506aad50384ca8aba1616d1bed626),
      [Commit](https://github.com/open-webui/open-webui/commit/e963d36e393aead56b941e99d4167fb0dc9d2d7a)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F507 **Voice mode staying silent with reasoning models.** Voice
      mode now speaks when the emoji option is on and the model behind it reports
      its answer as thinking rather than text, where the whole reply went unspoken
      and nothing reached the speech service at all. [#28724](https://github.com/open-webui/open-webui/pull/28724)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F5E3 **Sentences skipped in voice mode.** Voice mode now speaks
      every sentence of a reply, where any sentence that completed in the same piece
      of the reply as another was silently never read out, which happened routinely
      with providers that send whole paragraphs at a time. [Commit](https://github.com/open-webui/open-webui/commit/495296346edfcd96a506a22fed4bb5b8faf3cd4d),
      [#28730](https://github.com/open-webui/open-webui/issues/28730), [#19861](https://github.com/open-webui/open-webui/issues/19861)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F4DE **Links that start a voice call.** Opening a link that starts
      a call now starts one, where it opened the controls pane and stopped there,
      leaving the only way to begin a call from outside the application broken. [#28721](https://github.com/open-webui/open-webui/pull/28721),
      [#28677](https://github.com/open-webui/open-webui/issues/28677), [Commit](https://github.com/open-webui/open-webui/commit/8c1f3d382470edb81fa1efdf6cf4fb6bb188c460)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 4-voice-and-audio-changes-in-v0-11-1
  source_release: open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c
  source_type: github_releases
  theme: voice
  title: 4 Voice and Audio changes in v0.11.1
  type: change
related_changes:
- '[[Changes/Google Antigravity/2026-08-24-embedded-terminals-git-version-control-and-audio-attachments|Embedded
  Terminals, Git Version Control, and Audio Attachments]]'
- '[[Changes/Dify/2026-08-25-audio-asr-now-accepts-audio-x-m4a-and-audio-mime-types-are-validated-more-accura|Audio
  ASR now accepts audio/x-m4a, and audio MIME types are validated more…]]'
- '[[Changes/Microsoft 365 Copilot/2026-08-25-use-voice-for-q-a-during-read-aloud-in-word-windows-word|Use
  voice for Q&A during Read Aloud in Word Windows (Word)]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c|open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c]]'
source_type: github_releases
theme: voice
title: 4 Voice and Audio changes in v0.11.1
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Voice and Audio changes in v0.11.1

**Open WebUI** · 2026-08-25 · [[Themes/voice|Voice and Audio]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.1) · from [[Releases/Open WebUI/open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c|v0.11.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🎙️ **Voice mode in the notes editor.** The voice mode button is no longer offered in the chat embedded in a note, where it does not apply. [Commit](https://github.com/open-webui/open-webui/commit/9122c24ea2d506aad50384ca8aba1616d1bed626), [Commit](https://github.com/open-webui/open-webui/commit/e963d36e393aead56b941e99d4167fb0dc9d2d7a)

> 🔇 **Voice mode staying silent with reasoning models.** Voice mode now speaks when the emoji option is on and the model behind it reports its answer as thinking rather than text, where the whole reply went unspoken and nothing reached the speech service at all. [#28724](https://github.com/open-webui/open-webui/pull/28724)

> 🗣 **Sentences skipped in voice mode.** Voice mode now speaks every sentence of a reply, where any sentence that completed in the same piece of the reply as another was silently never read out, which happened routinely with providers that send whole paragraphs at a time. [Commit](https://github.com/open-webui/open-webui/commit/495296346edfcd96a506a22fed4bb5b8faf3cd4d), [#28730](https://github.com/open-webui/open-webui/issues/28730), [#19861](https://github.com/open-webui/open-webui/issues/19861)

> 📞 **Links that start a voice call.** Opening a link that starts a call now starts one, where it opened the controls pane and stopped there, leaving the only way to begin a call from outside the application broken. [#28721](https://github.com/open-webui/open-webui/pull/28721), [#28677](https://github.com/open-webui/open-webui/issues/28677), [Commit](https://github.com/open-webui/open-webui/commit/8c1f3d382470edb81fa1efdf6cf4fb6bb188c460)

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
- [[Changes/Open WebUI/2026-08-25-5-search-and-browsing-changes-in-v0-11-1|5 Search and Browsing changes in v0.11.1]] · Search and Browsing
- [[Changes/Open WebUI/2026-08-25-56-model-support-changes-in-v0-11-1|56 Model Support changes in v0.11.1]] · Model Support
- [[Changes/Open WebUI/2026-08-25-39-other-changes-in-v0-11-1|39 other changes in v0.11.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Voice and Audio

- Earlier: 2026-08-25 · Microsoft 365 Copilot · [[Changes/Microsoft 365 Copilot/2026-08-25-use-voice-for-q-a-during-read-aloud-in-word-windows-word|Use voice for Q&A during Read Aloud in Word Windows (Word)]]
- Later: 2026-08-25 · Raycast · [[Changes/Raycast/2026-08-25-dictation-added-a-word-count-to-the-details-of-each-entry-in-dictation-history|Dictation : Added a word count to the details of each entry in dictation history]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-07-09 · Descript · [[Changes/Descript/2018-07-09-type-in-parentheses-to-add-notes-to-your-script-that-don-t-affect-the-audio-text|Support for Inline Notes]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-08-25-ee5914&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-08-25-4-voice-and-audio-changes-in-v0-11-1.md%0ACard%20ID%3A%20open-webui-2026-08-25-ee5914%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->