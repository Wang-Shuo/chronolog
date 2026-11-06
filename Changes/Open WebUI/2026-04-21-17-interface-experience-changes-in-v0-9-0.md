---
card_id: open-webui-2026-04-21-99efc2
date: '2026-04-21'
description: "Open WebUI · 2026-04-21 · Interface Experience: 17 changes in v0.9.0
  — \U0001F9E9 **Responses tool output rendering.** Built-in tool outputs in Responses
  API flows now…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop
    generating: Based on your feedback, we''ve added the ability to stop generating…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1198
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 3c0e5ea7a98785fbdde27c283eb5cdfb8154bb733250821e4e225eccca27044e
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-04-21-99efc2
  comparison: ''
  date: '2026-04-21'
  description: 'Open WebUI — v0.9.0: 17 Interface Experience changes'
  evidence:
  - quote: "\U0001F9E9 **Responses tool output rendering.** Built-in tool outputs
      in Responses API flows now render more consistently so downstream chat output
      is easier to interpret. [Commit](https://github.com/open-webui/open-webui/commit/e695d854f2d11fada84d5fbec8d3edea4e468e19),
      [#23482](https://github.com/open-webui/open-webui/pull/23482)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F9F7 **Default model terminal selection.** Workspace model editors
      can now preselect an Open Terminal connection, so new chats automatically start
      with the model’s configured terminal ready to use. [Commit](https://github.com/open-webui/open-webui/commit/47d413ce7b2a006a8126f4a9055b13e5fcb33a1d),
      [#23605](https://github.com/open-webui/open-webui/issues/23605)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F3A8 **Emoji shortcode support.** Typing a colon in the chat input
      now opens an emoji suggestion menu, making it easier to insert emojis using
      shortcodes like :wave:. [Commit](https://github.com/open-webui/open-webui/commit/2040095050056d01c61aa597c5010445449a42c7)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F4CC **Recently used emojis.** The emoji picker now shows your most
      recently used emojis at the top, making it faster to find emojis you use often.
      [Commit](https://github.com/open-webui/open-webui/commit/64da99a32218171d41b3af5acc14783de8dbdf49)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F514 **Unread chat indicators.** Sidebar chats now show unread status
      and are marked as read when opened, making it easier to spot conversations with
      new activity. [Commit](https://github.com/open-webui/open-webui/commit/0638b9f56ce1ba8a496d0e84da2e7fa178b01a3f)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F4CD **Pinned notes in sidebar.** Notes can now be pinned to the
      sidebar for quick access, and you can also create a new note directly from the
      pinned notes section. [Commit](https://github.com/open-webui/open-webui/commit/ecd74f220c7dd671d5705189a3f4493a3868c8bf),
      [Commit](https://github.com/open-webui/open-webui/commit/f1be85d997439b49fc143d2bcd2dc710f44446c8)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F5C2️ **Model selector layout.** The model selector now behaves
      more predictably as a custom popup, and the completions playground uses a simpler
      model picker for easier selection. [Commit](https://github.com/open-webui/open-webui/commit/c40ea7f29d34fa9535cdf9ffe599f4429ff3f455)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F680 **Inline code rendering performance.** Inline code tokens in
      streaming responses now fade in with a lightweight CSS animation, making chat
      output feel smoother while reducing interface overhead during rapid token updates.
      [#23258](https://github.com/open-webui/open-webui/pull/23258)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F6E1️ **Safer placeholder rendering.** Chat placeholder descriptions
      and the pending account notice now sanitize rendered markdown more consistently,
      reducing the risk of unsafe content being shown in these views. [Commit](https://github.com/open-webui/open-webui/commit/ae0316a30e01a2e5ff3f9d2f9f759c1cd6410f34)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F9ED **Safer in-flight chat navigation.** Sending a message no longer
      overwrites your active chat or causes duplicate background notifications when
      you switch conversations before a response finishes. [Commit](https://github.com/open-webui/open-webui/commit/dc6df52a917b49fa1264ac81a8cc74603f6155b3)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F9F0 **Large tool result rendering.** Tool call details now display
      large result payloads reliably in chat instead of intermittently showing empty
      output for bigger tool responses. [#18743](https://github.com/open-webui/open-webui/issues/18743),
      [Commit](https://github.com/open-webui/open-webui/commit/45e49d33e51f7720c00b564215484aff9b48b20c)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F4C2 **Channel input menu dismissal.** In Workspace Channels, the
      message input dropdown now closes immediately after selecting \"Upload Files\"
      or \"Capture\", matching normal chat input behavior and preventing the menu
      from staying open unnecessarily. [#23684](https://github.com/open-webui/open-webui/pull/23684)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F4D0 **Display math rendering.** Chat markdown now correctly recognizes
      and renders \"$$...$$\" expressions as display math, improving reliability for
      multiline and escaped KaTeX content while keeping malformed delimiters from
      disrupting message rendering. [#23526](https://github.com/open-webui/open-webui/issues/23526),
      [Commit](https://github.com/open-webui/open-webui/commit/15b89b9218b7d2c7239c579aa3d23c2892227ac6)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F9FE **Tool call JSON rendering.** Tool call arguments and structured
      results now render as plain formatted JSON blocks instead of markdown code fences,
      preventing formatting quirks and making tool output easier to read consistently.
      [Commit](https://github.com/open-webui/open-webui/commit/a7d4c53f3adb80768b67e4a410b486b04a581521)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F5C2️ **Archived chats menu visibility.** The 'Archived Chats' option
      in the user menu is now shown reliably for all users, so non-admin accounts
      can consistently access archived conversations. [Commit](https://github.com/open-webui/open-webui/commit/07262fa62c2323fc7948389e5b5b8a5d1b72fade)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F4DD **Writing block parsing reliability.** \":::writing\" blocks
      now parse more reliably when headers or extra inline text are present, preventing
      malformed rendering and duplicate output artifacts. [#23174](https://github.com/open-webui/open-webui/issues/23174)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F5B1️ **Rapid sidebar action protection.** Archive and delete actions
      in the chat sidebar now ignore repeated clicks while a request is in progress,
      preventing duplicate requests and stacked error toasts. [#23172](https://github.com/open-webui/open-webui/issues/23172)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 17-interface-experience-changes-in-v0-9-0
  source_release: open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a
  source_type: github_releases
  theme: interface-experience
  title: 17 Interface Experience changes in v0.9.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-04-20-3-interface-experience-changes-in-v2-1-116|3 Interface
  Experience changes in v2.1.116]]'
- '[[Changes/Codex CLI/2026-04-20-2-interface-experience-changes-in-rust-v0-122-0|2
  Interface Experience changes in rust-v0.122.0]]'
- '[[Changes/GitHub Copilot CLI/2026-04-20-4-interface-experience-changes-in-v1-0-33|4
  Interface Experience changes in v1.0.33]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a|open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a]]'
source_type: github_releases
theme: interface-experience
title: 17 Interface Experience changes in v0.9.0
type: change
---

<!-- chronolog:begin region="header" -->
# 17 Interface Experience changes in v0.9.0

**Open WebUI** · 2026-04-21 · [[Themes/interface-experience|Interface Experience]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.0) · from [[Releases/Open WebUI/open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a|v0.9.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🧩 **Responses tool output rendering.** Built-in tool outputs in Responses API flows now render more consistently so downstream chat output is easier to interpret. [Commit](https://github.com/open-webui/open-webui/commit/e695d854f2d11fada84d5fbec8d3edea4e468e19), [#23482](https://github.com/open-webui/open-webui/pull/23482)

> 🧷 **Default model terminal selection.** Workspace model editors can now preselect an Open Terminal connection, so new chats automatically start with the model’s configured terminal ready to use. [Commit](https://github.com/open-webui/open-webui/commit/47d413ce7b2a006a8126f4a9055b13e5fcb33a1d), [#23605](https://github.com/open-webui/open-webui/issues/23605)

> 🎨 **Emoji shortcode support.** Typing a colon in the chat input now opens an emoji suggestion menu, making it easier to insert emojis using shortcodes like :wave:. [Commit](https://github.com/open-webui/open-webui/commit/2040095050056d01c61aa597c5010445449a42c7)

> 📌 **Recently used emojis.** The emoji picker now shows your most recently used emojis at the top, making it faster to find emojis you use often. [Commit](https://github.com/open-webui/open-webui/commit/64da99a32218171d41b3af5acc14783de8dbdf49)

> 🔔 **Unread chat indicators.** Sidebar chats now show unread status and are marked as read when opened, making it easier to spot conversations with new activity. [Commit](https://github.com/open-webui/open-webui/commit/0638b9f56ce1ba8a496d0e84da2e7fa178b01a3f)

> 📍 **Pinned notes in sidebar.** Notes can now be pinned to the sidebar for quick access, and you can also create a new note directly from the pinned notes section. [Commit](https://github.com/open-webui/open-webui/commit/ecd74f220c7dd671d5705189a3f4493a3868c8bf), [Commit](https://github.com/open-webui/open-webui/commit/f1be85d997439b49fc143d2bcd2dc710f44446c8)

> 🗂️ **Model selector layout.** The model selector now behaves more predictably as a custom popup, and the completions playground uses a simpler model picker for easier selection. [Commit](https://github.com/open-webui/open-webui/commit/c40ea7f29d34fa9535cdf9ffe599f4429ff3f455)

> 🚀 **Inline code rendering performance.** Inline code tokens in streaming responses now fade in with a lightweight CSS animation, making chat output feel smoother while reducing interface overhead during rapid token updates. [#23258](https://github.com/open-webui/open-webui/pull/23258)

> 🛡️ **Safer placeholder rendering.** Chat placeholder descriptions and the pending account notice now sanitize rendered markdown more consistently, reducing the risk of unsafe content being shown in these views. [Commit](https://github.com/open-webui/open-webui/commit/ae0316a30e01a2e5ff3f9d2f9f759c1cd6410f34)

> 🧭 **Safer in-flight chat navigation.** Sending a message no longer overwrites your active chat or causes duplicate background notifications when you switch conversations before a response finishes. [Commit](https://github.com/open-webui/open-webui/commit/dc6df52a917b49fa1264ac81a8cc74603f6155b3)

> 🧰 **Large tool result rendering.** Tool call details now display large result payloads reliably in chat instead of intermittently showing empty output for bigger tool responses. [#18743](https://github.com/open-webui/open-webui/issues/18743), [Commit](https://github.com/open-webui/open-webui/commit/45e49d33e51f7720c00b564215484aff9b48b20c)

> 📂 **Channel input menu dismissal.** In Workspace Channels, the message input dropdown now closes immediately after selecting "Upload Files" or "Capture", matching normal chat input behavior and preventing the menu from staying open unnecessarily. [#23684](https://github.com/open-webui/open-webui/pull/23684)

> 📐 **Display math rendering.** Chat markdown now correctly recognizes and renders "$$...$$" expressions as display math, improving reliability for multiline and escaped KaTeX content while keeping malformed delimiters from disrupting message rendering. [#23526](https://github.com/open-webui/open-webui/issues/23526), [Commit](https://github.com/open-webui/open-webui/commit/15b89b9218b7d2c7239c579aa3d23c2892227ac6)

> 🧾 **Tool call JSON rendering.** Tool call arguments and structured results now render as plain formatted JSON blocks instead of markdown code fences, preventing formatting quirks and making tool output easier to read consistently. [Commit](https://github.com/open-webui/open-webui/commit/a7d4c53f3adb80768b67e4a410b486b04a581521)

> 🗂️ **Archived chats menu visibility.** The 'Archived Chats' option in the user menu is now shown reliably for all users, so non-admin accounts can consistently access archived conversations. [Commit](https://github.com/open-webui/open-webui/commit/07262fa62c2323fc7948389e5b5b8a5d1b72fade)

> 📝 **Writing block parsing reliability.** ":::writing" blocks now parse more reliably when headers or extra inline text are present, preventing malformed rendering and duplicate output artifacts. [#23174](https://github.com/open-webui/open-webui/issues/23174)

> 🖱️ **Rapid sidebar action protection.** Archive and delete actions in the chat sidebar now ignore repeated clicks while a request is in progress, preventing duplicate requests and stacked error toasts. [#23172](https://github.com/open-webui/open-webui/issues/23172)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-04-21-3-files-and-data-changes-in-v0-9-0|3 Files and Data changes in v0.9.0]] · Files and Data
- [[Changes/Open WebUI/2026-04-21-4-image-generation-changes-in-v0-9-0|4 Image Generation changes in v0.9.0]] · Image Generation
- [[Changes/Open WebUI/2026-04-21-28-model-support-changes-in-v0-9-0|28 Model Support changes in v0.9.0]] · Model Support
- [[Changes/Open WebUI/2026-04-21-5-editor-experience-changes-in-v0-9-0|5 Editor Experience changes in v0.9.0]] · Editor Experience
- [[Changes/Open WebUI/2026-04-21-persistent-chat-payload-efficiency-persisted-chats-now-use-server-side-history-l|🚀 Persistent chat payload efficiency. Persisted chats now use server-side…]] · Multimodal Input
- [[Changes/Open WebUI/2026-04-21-8-context-window-changes-in-v0-9-0|8 Context Window changes in v0.9.0]] · Context Window
- [[Changes/Open WebUI/2026-04-21-24-reliability-and-performance-changes-in-v0-9-0|24 Reliability and Performance changes in v0.9.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-04-21-4-apps-and-integrations-changes-in-v0-9-0|4 Apps and Integrations changes in v0.9.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-04-21-46-developer-workflow-changes-in-v0-9-0|46 Developer Workflow changes in v0.9.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-04-21-8-automation-and-scheduling-changes-in-v0-9-0|8 Automation and Scheduling changes in v0.9.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-04-21-7-memory-and-personalization-changes-in-v0-9-0|7 Memory and Personalization changes in v0.9.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-04-21-2-mobile-and-desktop-changes-in-v0-9-0|2 Mobile and Desktop changes in v0.9.0]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-04-21-11-safety-and-privacy-changes-in-v0-9-0|11 Safety and Privacy changes in v0.9.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-04-21-4-search-and-browsing-changes-in-v0-9-0|4 Search and Browsing changes in v0.9.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-04-21-shared-chat-access-controls-you-can-now-control-who-has-access-to-a-shared-chat|🔗 Shared chat access controls. You can now control who has access to a shared…]] · Collaboration
- [[Changes/Open WebUI/2026-04-21-4-voice-and-audio-changes-in-v0-9-0|4 Voice and Audio changes in v0.9.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-04-21-17-account-and-access-changes-in-v0-9-0|17 Account and Access changes in v0.9.0]] · Account and Access
- [[Changes/Open WebUI/2026-04-21-21-other-changes-in-v0-9-0|21 other changes in v0.9.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Interface Experience

- Earlier: 2026-04-20 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-04-20-4-interface-experience-changes-in-v1-0-33|4 Interface Experience changes in v1.0.33]]
- Later: 2026-04-23 · Claude Code · [[Changes/Claude Code/2026-04-23-3-interface-experience-changes-in-v2-1-119|3 Interface Experience changes in v2.1.119]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop generating: Based on your feedback, we've added the ability to stop generating…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-04-21-99efc2&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-04-21-17-interface-experience-changes-in-v0-9-0.md%0ACard%20ID%3A%20open-webui-2026-04-21-99efc2%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->