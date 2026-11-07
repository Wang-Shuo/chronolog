---
card_id: open-webui-2026-07-27-3c3ea6
date: '2026-07-27'
description: "Open WebUI · 2026-07-27 · Memory and Personalization: 7 changes in v0.11.0
  — \U0001F9E0 **Memory as a per-model capability.** Whether a model receives your
  stored…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1103
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 302a91f9c9fec2e7666a21e0a6dd147b794e8bed2251125e4abb4b96d7b7bd87
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-07-27-3c3ea6
  comparison: ''
  date: '2026-07-27'
  description: 'Open WebUI — v0.11.0: 7 Memory and Personalization changes'
  evidence:
  - quote: "\U0001F9E0 **Memory as a per-model capability.** Whether a model receives
      your stored memories is now a switch on the model itself, so it can be left
      on for everyday assistants and off for ones that should start from nothing.
      [Commit](https://github.com/open-webui/open-webui/commit/6732852ce6c1a2a445bc001b122c60cf12e0278b),
      [#26861](https://github.com/open-webui/open-webui/pull/26861), [#18610](https://github.com/open-webui/open-webui/discussions/18610)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F9E0 **Memories in settings.** Your memories are now listed directly
      in personalization settings where you can search, add, edit, and remove them,
      instead of being tucked behind a separate manage dialog. [Commit](https://github.com/open-webui/open-webui/commit/db934a3b4ff16532b48670d7cc75e7048a6db993)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F4E4 **Streamed file transfers.** Uploading a model, pipeline or
      audio file now sends it in chunks instead of holding the whole thing in memory,
      and reading and writing files no longer blocks other requests, so large transfers
      no longer spike memory or stall the server. [Commit](https://github.com/open-webui/open-webui/commit/429f2df50cd2f0ec8d0a1bb4136a46e2f94a4bf5),
      [#27351](https://github.com/open-webui/open-webui/pull/27351), [#27349](https://github.com/open-webui/open-webui/issues/27349)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: ⚡ **Faster memory lookups.** Stored memories are now indexed so retrieving
      them stays quick as the number you have grows. [Commit](https://github.com/open-webui/open-webui/commit/28bdcb063b8d5d6a0b10943b1b2f87b16ff63621),
      [#26957](https://github.com/open-webui/open-webui/pull/26957)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F9F5 **Lighter chat listings and search.** Building a page of chat
      search results or a folder listing no longer copies each full conversation to
      read its title and dates, so those pages come together faster and use far less
      memory while they are built. [#27388](https://github.com/open-webui/open-webui/pull/27388)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F4D0 **System prompt lost during tool calls.** A model's system
      prompt now stays in place through every round of tool calls, instead of being
      dropped after the first one and, with memories enabled, replaced by the memory
      block alone. [#26857](https://github.com/open-webui/open-webui/pull/26857),
      [#26836](https://github.com/open-webui/open-webui/issues/26836)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001FAB6 **Memories from structured replies.** A reply delivered as
      structured output is now read when memories are reviewed after a turn, so nothing
      worth remembering is skipped just because of how the answer arrived. [Commit](https://github.com/open-webui/open-webui/commit/3fe03583a3b240da3cc42364088f22bc3a059487),
      [#26705](https://github.com/open-webui/open-webui/pull/26705), [#26651](https://github.com/open-webui/open-webui/issues/26651)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 7-memory-and-personalization-changes-in-v0-11-0
  source_release: open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f
  source_type: github_releases
  theme: memory
  title: 7 Memory and Personalization changes in v0.11.0
  type: change
related_changes:
- '[[Changes/Midjourney/2026-07-24-personalization-will-understand-your-personal-taste-much-better-especially-if-yo|Personalization
  will "understand" your personal taste much better]]'
- '[[Changes/Midjourney/2026-07-24-creating-personalization-profiles-for-v8-2-now-has-a-much-larger-and-improved-po|Creating
  personalization profiles for V8.2 now has a much larger and improved pool…]]'
- '[[Changes/Midjourney/2026-07-24-we-are-launching-our-v8-2-image-model-today-this-update-focuses-on-aesthetics-an|Midjourney
  launches our V8.2 image model today]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f|open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f]]'
source_type: github_releases
theme: memory
title: 7 Memory and Personalization changes in v0.11.0
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Memory and Personalization changes in v0.11.0

**Open WebUI** · 2026-07-27 · [[Themes/memory|Memory and Personalization]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.0) · from [[Releases/Open WebUI/open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f|v0.11.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🧠 **Memory as a per-model capability.** Whether a model receives your stored memories is now a switch on the model itself, so it can be left on for everyday assistants and off for ones that should start from nothing. [Commit](https://github.com/open-webui/open-webui/commit/6732852ce6c1a2a445bc001b122c60cf12e0278b), [#26861](https://github.com/open-webui/open-webui/pull/26861), [#18610](https://github.com/open-webui/open-webui/discussions/18610)

> 🧠 **Memories in settings.** Your memories are now listed directly in personalization settings where you can search, add, edit, and remove them, instead of being tucked behind a separate manage dialog. [Commit](https://github.com/open-webui/open-webui/commit/db934a3b4ff16532b48670d7cc75e7048a6db993)

> 📤 **Streamed file transfers.** Uploading a model, pipeline or audio file now sends it in chunks instead of holding the whole thing in memory, and reading and writing files no longer blocks other requests, so large transfers no longer spike memory or stall the server. [Commit](https://github.com/open-webui/open-webui/commit/429f2df50cd2f0ec8d0a1bb4136a46e2f94a4bf5), [#27351](https://github.com/open-webui/open-webui/pull/27351), [#27349](https://github.com/open-webui/open-webui/issues/27349)

> ⚡ **Faster memory lookups.** Stored memories are now indexed so retrieving them stays quick as the number you have grows. [Commit](https://github.com/open-webui/open-webui/commit/28bdcb063b8d5d6a0b10943b1b2f87b16ff63621), [#26957](https://github.com/open-webui/open-webui/pull/26957)

> 🧵 **Lighter chat listings and search.** Building a page of chat search results or a folder listing no longer copies each full conversation to read its title and dates, so those pages come together faster and use far less memory while they are built. [#27388](https://github.com/open-webui/open-webui/pull/27388)

> 📐 **System prompt lost during tool calls.** A model's system prompt now stays in place through every round of tool calls, instead of being dropped after the first one and, with memories enabled, replaced by the memory block alone. [#26857](https://github.com/open-webui/open-webui/pull/26857), [#26836](https://github.com/open-webui/open-webui/issues/26836)

> 🪶 **Memories from structured replies.** A reply delivered as structured output is now read when memories are reviewed after a turn, so nothing worth remembering is skipped just because of how the answer arrived. [Commit](https://github.com/open-webui/open-webui/commit/3fe03583a3b240da3cc42364088f22bc3a059487), [#26705](https://github.com/open-webui/open-webui/pull/26705), [#26651](https://github.com/open-webui/open-webui/issues/26651)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-07-27-9-automation-and-scheduling-changes-in-v0-11-0|9 Automation and Scheduling changes in v0.11.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-07-27-13-safety-and-privacy-changes-in-v0-11-0|13 Safety and Privacy changes in v0.11.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-07-27-4-voice-and-audio-changes-in-v0-11-0|4 Voice and Audio changes in v0.11.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-07-27-62-developer-workflow-changes-in-v0-11-0|62 Developer Workflow changes in v0.11.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-07-27-19-interface-experience-changes-in-v0-11-0|19 Interface Experience changes in v0.11.0]] · Interface Experience
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
## Nearby in Memory and Personalization

- Earlier: 2026-07-24 · Midjourney · [[Changes/Midjourney/2026-07-24-we-are-launching-our-v8-2-image-model-today-this-update-focuses-on-aesthetics-an|Midjourney launches our V8.2 image model today]]
- Later: 2026-07-28 · Dify · [[Changes/Dify/2026-07-28-test-use-sqlite-sessions-in-core-memory-by-asukaminato0721-in-https-github-com-l|test: use SQLite sessions in core memory]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-07-27-3c3ea6&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-07-27-7-memory-and-personalization-changes-in-v0-11-0.md%0ACard%20ID%3A%20open-webui-2026-07-27-3c3ea6%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->