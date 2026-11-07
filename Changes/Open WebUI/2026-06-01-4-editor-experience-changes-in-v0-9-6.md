---
card_id: open-webui-2026-06-01-3ec1c6
date: '2026-06-01'
description: "Open WebUI · 2026-06-01 · Editor Experience: 4 changes in v0.9.6 — \U0001F4DD
  **Frontmatter auto-fill for tools, functions, and skills.** Opening a tool, function,
  or…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3
    Editor Experience changes in 0.0.37]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1175
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: editor-experience
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 1e7d2a0db7cb264ead76c908fabf81282754bec058aeb4ad134ae99a251f58ce
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-06-01-3ec1c6
  comparison: ''
  date: '2026-06-01'
  description: 'Open WebUI — v0.9.6: 4 Editor Experience changes'
  evidence:
  - quote: "\U0001F4DD **Frontmatter auto-fill for tools, functions, and skills.**
      Opening a tool, function, or skill editor now auto-fills the name, id, and description
      fields from the file's frontmatter, saving you from re-entering metadata already
      declared in the source. [#24649](https://github.com/open-webui/open-webui/pull/24649),
      [Commit](https://github.com/open-webui/open-webui/commit/ef975649b26d3e7cd589c49be2fc77cee80fad8f)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F9FE **Model knowledge file ownership checks.** Creating or updating
      a model now verifies that any knowledge files attached to it are files the editor
      can access, preventing another user's files from being attached to a model.
      [#25055](https://github.com/open-webui/open-webui/pull/25055), [Commit](https://github.com/open-webui/open-webui/commit/27fb20c13a4bf8501f7a485abe0654eb5880980d)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F3AF **All skills selectable in the model editor.** The model editor's
      skills selector now lists every skill you have access to, with a search box
      for large lists, instead of showing only the first 30 with no way to reach the
      rest. [#24873](https://github.com/open-webui/open-webui/issues/24873), [Commit](https://github.com/open-webui/open-webui/commit/936d5f2676dfbd2ba763b30af33a8557dcda9b05)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F4F6 **Quieter reconnection notifications.** Brief connection interruptions,
      such as backgrounding a mobile tab, no longer flash a \"connection lost\" warning,
      and the \"reconnected\" message only appears if a disconnect was actually shown.
      [Commit](https://github.com/open-webui/open-webui/commit/77c8c54b1ea07189e21313f9cd401f3b956bb93a)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 4-editor-experience-changes-in-v0-9-6
  source_release: open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e
  source_type: github_releases
  theme: editor-experience
  title: 4 Editor Experience changes in v0.9.6
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-05-29-2-editor-experience-changes-in-v1-0-56|2
  Editor Experience changes in v1.0.56]]'
- '[[Changes/Codex CLI/2026-06-01-2-editor-experience-changes-in-rust-v0-136-0|2 Editor
  Experience changes in rust-v0.136.0]]'
- '[[Changes/GitHub Copilot CLI/2026-06-01-9-editor-experience-changes-in-v1-0-57|9
  Editor Experience changes in v1.0.57]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e|open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e]]'
source_type: github_releases
theme: editor-experience
title: 4 Editor Experience changes in v0.9.6
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Editor Experience changes in v0.9.6

**Open WebUI** · 2026-06-01 · [[Themes/editor-experience|Editor Experience]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.6) · from [[Releases/Open WebUI/open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e|v0.9.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📝 **Frontmatter auto-fill for tools, functions, and skills.** Opening a tool, function, or skill editor now auto-fills the name, id, and description fields from the file's frontmatter, saving you from re-entering metadata already declared in the source. [#24649](https://github.com/open-webui/open-webui/pull/24649), [Commit](https://github.com/open-webui/open-webui/commit/ef975649b26d3e7cd589c49be2fc77cee80fad8f)

> 🧾 **Model knowledge file ownership checks.** Creating or updating a model now verifies that any knowledge files attached to it are files the editor can access, preventing another user's files from being attached to a model. [#25055](https://github.com/open-webui/open-webui/pull/25055), [Commit](https://github.com/open-webui/open-webui/commit/27fb20c13a4bf8501f7a485abe0654eb5880980d)

> 🎯 **All skills selectable in the model editor.** The model editor's skills selector now lists every skill you have access to, with a search box for large lists, instead of showing only the first 30 with no way to reach the rest. [#24873](https://github.com/open-webui/open-webui/issues/24873), [Commit](https://github.com/open-webui/open-webui/commit/936d5f2676dfbd2ba763b30af33a8557dcda9b05)

> 📶 **Quieter reconnection notifications.** Brief connection interruptions, such as backgrounding a mobile tab, no longer flash a "connection lost" warning, and the "reconnected" message only appears if a disconnect was actually shown. [Commit](https://github.com/open-webui/open-webui/commit/77c8c54b1ea07189e21313f9cd401f3b956bb93a)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-06-01-bulk-enable-or-disable-automations-automations-can-now-be-enabled-or-disabled-in|🔘 Bulk enable or disable automations. Automations can now be enabled or disabled…]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-06-01-4-context-window-changes-in-v0-9-6|4 Context Window changes in v0.9.6]] · Context Window
- [[Changes/Open WebUI/2026-06-01-2-memory-and-personalization-changes-in-v0-9-6|2 Memory and Personalization changes in v0.9.6]] · Memory and Personalization
- [[Changes/Open WebUI/2026-06-01-keyboard-and-screen-reader-access-to-menus-the-integrations-more-options-and-use|♿ Keyboard and screen reader access to menus. The integrations, more-options…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-06-01-27-developer-workflow-changes-in-v0-9-6|27 Developer Workflow changes in v0.9.6]] · Developer Workflow
- [[Changes/Open WebUI/2026-06-01-4-interface-experience-changes-in-v0-9-6|4 Interface Experience changes in v0.9.6]] · Interface Experience
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
## Nearby in Editor Experience

- Earlier: 2026-06-01 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-06-01-9-editor-experience-changes-in-v1-0-57|9 Editor Experience changes in v1.0.57]]
- Later: 2026-06-02 · Claude Code · [[Changes/Claude Code/2026-06-02-edit-no-longer-requires-a-separate-read-after-viewing-a-file-with-grep-single-fi|Edit no longer requires a separate Read after viewing a file with grep]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-14 · Cursor · [[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3 Editor Experience changes in 0.0.37]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-06-01-3ec1c6&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-06-01-4-editor-experience-changes-in-v0-9-6.md%0ACard%20ID%3A%20open-webui-2026-06-01-3ec1c6%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.6%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->