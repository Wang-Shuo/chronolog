---
card_id: open-webui-2026-06-01-200e80
date: '2026-06-01'
description: "Open WebUI · 2026-06-01 · Memory and Personalization: 2 changes in v0.9.6
  — \U0001F6AB **Unscoped retrieval collections denied by default.** Retrieval requests
  for…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1047
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 20c2bb6b2a7158aea16db94d876b76b2ffbf8a67ca1b70a67ec8f025d2808361
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-06-01-200e80
  comparison: ''
  date: '2026-06-01'
  description: 'Open WebUI — v0.9.6: 2 Memory and Personalization changes'
  evidence:
  - quote: "\U0001F6AB **Unscoped retrieval collections denied by default.** Retrieval
      requests for collection names that don't correspond to a known file, memory,
      web-search, or knowledge base are now denied for non-admins by default, with
      a new \"ENABLE_RETRIEVAL_UNSCOPED_COLLECTIONS\" setting to restore the previous
      behavior if needed. [Commit](https://github.com/open-webui/open-webui/commit/c93f071700520a60833b7f9616c292b11f210880)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F9F2 **Memory search quality.** Memory searches now apply the configured
      embedding query prefix, so retrieval works correctly with embedding models that
      require one for queries. [#24921](https://github.com/open-webui/open-webui/pull/24921),
      [Commit](https://github.com/open-webui/open-webui/commit/ce4dca47cb19a6582fd8a550806c89ab297c038d)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 2-memory-and-personalization-changes-in-v0-9-6
  source_release: open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e
  source_type: github_releases
  theme: memory
  title: 2 Memory and Personalization changes in v0.9.6
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-05-28-8-memory-and-personalization-changes-in-rust-v0-135-0|8
  Memory and Personalization changes in rust-v0.135.0]]'
- '[[Changes/GitHub Copilot CLI/2026-05-28-vote-memory-tool-calls-are-throttled-per-response-and-per-interaction-to-prevent|vote_memory
  tool calls are throttled per response and per interaction to prevent…]]'
- '[[Changes/Codex CLI/2026-06-01-2-memory-and-personalization-changes-in-rust-v0-136-0|2
  Memory and Personalization changes in rust-v0.136.0]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e|open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e]]'
source_type: github_releases
theme: memory
title: 2 Memory and Personalization changes in v0.9.6
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Memory and Personalization changes in v0.9.6

**Open WebUI** · 2026-06-01 · [[Themes/memory|Memory and Personalization]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.6) · from [[Releases/Open WebUI/open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e|v0.9.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🚫 **Unscoped retrieval collections denied by default.** Retrieval requests for collection names that don't correspond to a known file, memory, web-search, or knowledge base are now denied for non-admins by default, with a new "ENABLE_RETRIEVAL_UNSCOPED_COLLECTIONS" setting to restore the previous behavior if needed. [Commit](https://github.com/open-webui/open-webui/commit/c93f071700520a60833b7f9616c292b11f210880)

> 🧲 **Memory search quality.** Memory searches now apply the configured embedding query prefix, so retrieval works correctly with embedding models that require one for queries. [#24921](https://github.com/open-webui/open-webui/pull/24921), [Commit](https://github.com/open-webui/open-webui/commit/ce4dca47cb19a6582fd8a550806c89ab297c038d)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-06-01-bulk-enable-or-disable-automations-automations-can-now-be-enabled-or-disabled-in|🔘 Bulk enable or disable automations. Automations can now be enabled or disabled…]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-06-01-4-context-window-changes-in-v0-9-6|4 Context Window changes in v0.9.6]] · Context Window
- [[Changes/Open WebUI/2026-06-01-keyboard-and-screen-reader-access-to-menus-the-integrations-more-options-and-use|♿ Keyboard and screen reader access to menus. The integrations, more-options…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-06-01-27-developer-workflow-changes-in-v0-9-6|27 Developer Workflow changes in v0.9.6]] · Developer Workflow
- [[Changes/Open WebUI/2026-06-01-4-interface-experience-changes-in-v0-9-6|4 Interface Experience changes in v0.9.6]] · Interface Experience
- [[Changes/Open WebUI/2026-06-01-4-editor-experience-changes-in-v0-9-6|4 Editor Experience changes in v0.9.6]] · Editor Experience
- [[Changes/Open WebUI/2026-06-01-5-files-and-data-changes-in-v0-9-6|5 Files and Data changes in v0.9.6]] · Files and Data
- [[Changes/Open WebUI/2026-06-01-7-safety-and-privacy-changes-in-v0-9-6|7 Safety and Privacy changes in v0.9.6]] · Safety and Privacy
- [[Changes/Open WebUI/2026-06-01-startup-on-non-unicode-consoles-open-webui-no-longer-crashes-at-startup-when-the|🥾 Startup on non-Unicode consoles. Open WebUI no longer crashes at startup…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-06-01-youtube-short-link-transcripts-pasting-a-youtu-be-short-link-into-a-chat-now-loa|📺 YouTube short link transcripts. Pasting a "youtu.be" short link into a chat…]] · Multimodal Input
- [[Changes/Open WebUI/2026-06-01-9-search-and-browsing-changes-in-v0-9-6|9 Search and Browsing changes in v0.9.6]] · Search and Browsing
- [[Changes/Open WebUI/2026-06-01-shared-chat-file-write-protection-access-to-a-file-through-a-shared-chat-now-onl|🔐 Shared-chat file write protection. Access to a file through a shared chat now…]] · Collaboration
- [[Changes/Open WebUI/2026-06-01-2-enterprise-and-administration-changes-in-v0-9-6|2 Enterprise and Administration changes in v0.9.6]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-06-01-image-generation-with-non-standard-response-headers-image-generation-now-works-w|🖌️ Image generation with non-standard response headers. Image generation now…]] · Image Generation
- [[Changes/Open WebUI/2026-06-01-6-account-and-access-changes-in-v0-9-6|6 Account and Access changes in v0.9.6]] · Account and Access
- [[Changes/Open WebUI/2026-06-01-12-model-support-changes-in-v0-9-6|12 Model Support changes in v0.9.6]] · Model Support
- [[Changes/Open WebUI/2026-06-01-4-apps-and-integrations-changes-in-v0-9-6|4 Apps and Integrations changes in v0.9.6]] · Apps and Integrations
- [[Changes/Open WebUI/2026-06-01-5-reliability-and-performance-changes-in-v0-9-6|5 Reliability and Performance changes in v0.9.6]] · Reliability and Performance
- [[Changes/Open WebUI/2026-06-01-4-voice-and-audio-changes-in-v0-9-6|4 Voice and Audio changes in v0.9.6]] · Voice and Audio
- [[Changes/Open WebUI/2026-06-01-20-other-changes-in-v0-9-6|20 other changes in v0.9.6]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Memory and Personalization

- Earlier: 2026-06-01 · Codex CLI · [[Changes/Codex CLI/2026-06-01-2-memory-and-personalization-changes-in-rust-v0-136-0|2 Memory and Personalization changes in rust-v0.136.0]]
- Later: 2026-06-02 · HeyGen · [[Changes/HeyGen/2026-06-02-personal-settings-contains-settings-that-apply-only-to-the-individual-user-inclu|Personal Settings contains settings that apply only to the individual user…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-06-01-200e80&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-06-01-2-memory-and-personalization-changes-in-v0-9-6.md%0ACard%20ID%3A%20open-webui-2026-06-01-200e80%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.6%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->