---
card_id: open-webui-2026-01-09-b7e12f
date: '2026-01-09'
description: "Open WebUI · 2026-01-09 · Interface Experience: 5 changes in v0.7.0
  — \U0001F4CC Users can now pin or hide models directly from the Workspace Models
  page and Admin…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop
    generating: Based on your feedback, we''ve added the ability to stop generating…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1096
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 13993dbd2b2898f964de981e7f1775185304eed16850715b507619b7c5311c78
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-01-09-b7e12f
  comparison: ''
  date: '2026-01-09'
  description: 'Open WebUI — v0.7.0: 5 Interface Experience changes'
  evidence:
  - quote: "\U0001F4CC Users can now pin or hide models directly from the Workspace
      Models page and Admin Settings Models page, making it easier to manage which
      models appear in the sidebar without switching to the chat interface. [#20176](https://github.com/open-webui/open-webui/pull/20176)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F986 Administrators can now select a specific search backend for
      DDGS instead of random selection, with options including Bing, Brave, DuckDuckGo,
      Google, Wikipedia, Yahoo, and others. [#20330](https://github.com/open-webui/open-webui/issues/20330),
      [#20366](https://github.com/open-webui/open-webui/pull/20366)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F4E1 Users with Channels no longer experience infinite recursion
      and connection pool exhaustion when fetching threaded replies, preventing RecursionError
      crashes during chat history loading. [#20299](https://github.com/open-webui/open-webui/pull/20299),
      [Commit](https://github.com/open-webui/open-webui/commit/c144122f608759c2b79472e1f6948a7c1600a3d1)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F195 Non-admin users with disabled temporary chat permissions can
      now successfully create new chats and use pinned models from the sidebar. [#20336](https://github.com/open-webui/open-webui/issues/20336),
      [#20367](https://github.com/open-webui/open-webui/pull/20367), [Commit](https://github.com/open-webui/open-webui/commit/e754940c031f9689fb4f6edb3625aa06aeb53377)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F501 Users can now regenerate messages without crashes when the
      parent message is missing or corrupted in the chat history. [#20264](https://github.com/open-webui/open-webui/pull/20264)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 5-interface-experience-changes-in-v0-7-0
  source_release: open-webui-2026-01-09-v0-7-0-github-275585328-a4da522c
  source_type: github_releases
  theme: interface-experience
  title: 5 Interface Experience changes in v0.7.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-01-09-2-interface-experience-changes-in-v2-1-3|2 Interface
  Experience changes in v2.1.3]]'
- '[[Changes/Claude Code/2026-01-09-added-shift-tab-keyboard-shortcut-in-plan-mode-to-quickly-select-auto-accept-edi|Added
  Shift+Tab keyboard shortcut in plan mode to quickly select…]]'
- '[[Changes/Codex CLI/2026-01-09-3-interface-experience-changes-in-rust-v0-80-0|3
  Interface Experience changes in rust-v0.80.0]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-01-09-v0-7-0-github-275585328-a4da522c|open-webui-2026-01-09-v0-7-0-github-275585328-a4da522c]]'
source_type: github_releases
theme: interface-experience
title: 5 Interface Experience changes in v0.7.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Interface Experience changes in v0.7.0

**Open WebUI** · 2026-01-09 · [[Themes/interface-experience|Interface Experience]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.7.0) · from [[Releases/Open WebUI/open-webui-2026-01-09-v0-7-0-github-275585328-a4da522c|v0.7.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📌 Users can now pin or hide models directly from the Workspace Models page and Admin Settings Models page, making it easier to manage which models appear in the sidebar without switching to the chat interface. [#20176](https://github.com/open-webui/open-webui/pull/20176)

> 🦆 Administrators can now select a specific search backend for DDGS instead of random selection, with options including Bing, Brave, DuckDuckGo, Google, Wikipedia, Yahoo, and others. [#20330](https://github.com/open-webui/open-webui/issues/20330), [#20366](https://github.com/open-webui/open-webui/pull/20366)

> 📡 Users with Channels no longer experience infinite recursion and connection pool exhaustion when fetching threaded replies, preventing RecursionError crashes during chat history loading. [#20299](https://github.com/open-webui/open-webui/pull/20299), [Commit](https://github.com/open-webui/open-webui/commit/c144122f608759c2b79472e1f6948a7c1600a3d1)

> 🆕 Non-admin users with disabled temporary chat permissions can now successfully create new chats and use pinned models from the sidebar. [#20336](https://github.com/open-webui/open-webui/issues/20336), [#20367](https://github.com/open-webui/open-webui/pull/20367), [Commit](https://github.com/open-webui/open-webui/commit/e754940c031f9689fb4f6edb3625aa06aeb53377)

> 🔁 Users can now regenerate messages without crashes when the parent message is missing or corrupted in the chat history. [#20264](https://github.com/open-webui/open-webui/pull/20264)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-01-09-3-editor-experience-changes-in-v0-7-0|3 Editor Experience changes in v0.7.0]] · Editor Experience
- [[Changes/Open WebUI/2026-01-09-users-on-windows-now-see-correctly-preserved-line-breaks-when-using-the-clipboar|📋 Users on Windows now see correctly preserved line breaks when using…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-01-09-2-memory-and-personalization-changes-in-v0-7-0|2 Memory and Personalization changes in v0.7.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-01-09-4-search-and-browsing-changes-in-v0-7-0|4 Search and Browsing changes in v0.7.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-01-09-3-apps-and-integrations-changes-in-v0-7-0|3 Apps and Integrations changes in v0.7.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-01-09-5-files-and-data-changes-in-v0-7-0|5 Files and Data changes in v0.7.0]] · Files and Data
- [[Changes/Open WebUI/2026-01-09-3-context-window-changes-in-v0-7-0|3 Context Window changes in v0.7.0]] · Context Window
- [[Changes/Open WebUI/2026-01-09-9-reliability-and-performance-changes-in-v0-7-0|9 Reliability and Performance changes in v0.7.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-01-09-6-safety-and-privacy-changes-in-v0-7-0|6 Safety and Privacy changes in v0.7.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-01-09-3-account-and-access-changes-in-v0-7-0|3 Account and Access changes in v0.7.0]] · Account and Access
- [[Changes/Open WebUI/2026-01-09-4-image-generation-changes-in-v0-7-0|4 Image Generation changes in v0.7.0]] · Image Generation
- [[Changes/Open WebUI/2026-01-09-11-model-support-changes-in-v0-7-0|11 Model Support changes in v0.7.0]] · Model Support
- [[Changes/Open WebUI/2026-01-09-24-developer-workflow-changes-in-v0-7-0|24 Developer Workflow changes in v0.7.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-01-09-3-voice-and-audio-changes-in-v0-7-0|3 Voice and Audio changes in v0.7.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-01-09-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-01-09-26-other-changes-in-v0-7-0|26 other changes in v0.7.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Interface Experience

- Earlier: 2026-01-09 · Codex CLI · [[Changes/Codex CLI/2026-01-09-3-interface-experience-changes-in-rust-v0-80-0|3 Interface Experience changes in rust-v0.80.0]]
- Later: 2026-01-09 · OpenCode · [[Changes/OpenCode/2026-01-09-2-interface-experience-changes-in-v1-1-8|2 Interface Experience changes in v1.1.8]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop generating: Based on your feedback, we've added the ability to stop generating…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-01-09-b7e12f&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-01-09-5-interface-experience-changes-in-v0-7-0.md%0ACard%20ID%3A%20open-webui-2026-01-09-b7e12f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.7.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->