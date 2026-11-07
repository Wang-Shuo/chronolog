---
card_id: open-webui-2026-06-01-1e0ffc
date: '2026-06-01'
description: "Open WebUI · 2026-06-01 · Context Window: 4 changes in v0.9.6 — \U0001F5C4️
  **Cross-user access to retrieval collections.** Resolving the documents used for
  retrieval…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2
    Context Window changes in 0.2.9]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1124
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: eaa8eeb685b8497faee5731f678497c79f5cdb0485c67cdb7888a2a2944348f8
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-06-01-1e0ffc
  comparison: ''
  date: '2026-06-01'
  description: 'Open WebUI — v0.9.6: 4 Context Window changes'
  evidence:
  - quote: "\U0001F5C4️ **Cross-user access to retrieval collections.** Resolving
      the documents used for retrieval now verifies the caller's access to each referenced
      file and rejects client-supplied collection names, preventing a crafted request
      from pulling another user's files or vector collections into its context. [Commit](https://github.com/open-webui/open-webui/commit/ee47c9c833f8889f3abe99d2266c56e8f8d40230)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F4E3 **Channel chat access control.** Generating a response in a
      channel context now verifies the caller's access to that channel and scopes
      the included messages, preventing access to channels or messages the user isn't
      permitted to see. [#24725](https://github.com/open-webui/open-webui/pull/24725)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F4DA **Knowledge tool context overflow.** The built-in tool that
      lists a model's knowledge no longer dumps every file in every knowledge base
      into the model's context; it now returns summaries by default and paginates
      file listings only for a requested knowledge base. [#25105](https://github.com/open-webui/open-webui/pull/25105),
      [Commit](https://github.com/open-webui/open-webui/commit/0e73f7af099e1f9437c55a5c2d16741c97dbd57f)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F4CE **Document attachments in channel model replies.** Tagging
      a model in a channel thread now forwards uploaded non-image documents such as
      PDFs and DOCX files into the model's context, so document summarization and
      comparison workflows that already worked in direct chat now work in channels
      too. [#24896](https://github.com/open-webui/open-webui/issues/24896), [#24898](https://github.com/open-webui/open-webui/pull/24898),
      [Commit](https://github.com/open-webui/open-webui/commit/7e9d41d664d7065a92ac93606d18e88c45eb36b6)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 4-context-window-changes-in-v0-9-6
  source_release: open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e
  source_type: github_releases
  theme: context-window
  title: 4 Context Window changes in v0.9.6
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-05-28-2-context-window-changes-in-v1-0-55|2 Context
  Window changes in v1.0.55]]'
- '[[Changes/GitHub Copilot CLI/2026-05-29-2-context-window-changes-in-v1-0-56|2 Context
  Window changes in v1.0.56]]'
- '[[Changes/Codex CLI/2026-06-01-9-context-window-changes-in-rust-v0-136-0|9 Context
  Window changes in rust-v0.136.0]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e|open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e]]'
source_type: github_releases
theme: context-window
title: 4 Context Window changes in v0.9.6
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Context Window changes in v0.9.6

**Open WebUI** · 2026-06-01 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.6) · from [[Releases/Open WebUI/open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e|v0.9.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🗄️ **Cross-user access to retrieval collections.** Resolving the documents used for retrieval now verifies the caller's access to each referenced file and rejects client-supplied collection names, preventing a crafted request from pulling another user's files or vector collections into its context. [Commit](https://github.com/open-webui/open-webui/commit/ee47c9c833f8889f3abe99d2266c56e8f8d40230)

> 📣 **Channel chat access control.** Generating a response in a channel context now verifies the caller's access to that channel and scopes the included messages, preventing access to channels or messages the user isn't permitted to see. [#24725](https://github.com/open-webui/open-webui/pull/24725)

> 📚 **Knowledge tool context overflow.** The built-in tool that lists a model's knowledge no longer dumps every file in every knowledge base into the model's context; it now returns summaries by default and paginates file listings only for a requested knowledge base. [#25105](https://github.com/open-webui/open-webui/pull/25105), [Commit](https://github.com/open-webui/open-webui/commit/0e73f7af099e1f9437c55a5c2d16741c97dbd57f)

> 📎 **Document attachments in channel model replies.** Tagging a model in a channel thread now forwards uploaded non-image documents such as PDFs and DOCX files into the model's context, so document summarization and comparison workflows that already worked in direct chat now work in channels too. [#24896](https://github.com/open-webui/open-webui/issues/24896), [#24898](https://github.com/open-webui/open-webui/pull/24898), [Commit](https://github.com/open-webui/open-webui/commit/7e9d41d664d7065a92ac93606d18e88c45eb36b6)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-06-01-bulk-enable-or-disable-automations-automations-can-now-be-enabled-or-disabled-in|🔘 Bulk enable or disable automations. Automations can now be enabled or disabled…]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-06-01-2-memory-and-personalization-changes-in-v0-9-6|2 Memory and Personalization changes in v0.9.6]] · Memory and Personalization
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
## Nearby in Context Window

- Earlier: 2026-06-01 · Codex CLI · [[Changes/Codex CLI/2026-06-01-9-context-window-changes-in-rust-v0-136-0|9 Context Window changes in rust-v0.136.0]]
- Later: 2026-06-03 · Gemini CLI · [[Changes/Gemini CLI/2026-06-03-feat-context-complete-simplification-work-by-joshualitt-in-https-github-com-goog|feat(context): Complete simplification work]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-04 · Cursor · [[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2 Context Window changes in 0.2.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-06-01-1e0ffc&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-06-01-4-context-window-changes-in-v0-9-6.md%0ACard%20ID%3A%20open-webui-2026-06-01-1e0ffc%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.6%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->