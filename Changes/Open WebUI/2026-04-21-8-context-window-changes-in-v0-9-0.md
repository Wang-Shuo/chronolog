---
card_id: open-webui-2026-04-21-65e89b
date: '2026-04-21'
description: "Open WebUI · 2026-04-21 · Context Window: 8 changes in v0.9.0 — \U0001F3F7️
  **Source context metadata.** Retrieval source context now includes each source’s
  resource…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2
    Context Window changes in 0.2.9]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1083
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9c8e0710c437456f743880242d8dda0abd98fe63c2400651cc443c3882dbc1c4
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-04-21-65e89b
  comparison: ''
  date: '2026-04-21'
  description: 'Open WebUI — v0.9.0: 8 Context Window changes'
  evidence:
  - quote: "\U0001F3F7️ **Source context metadata.** Retrieval source context now
      includes each source’s resource type and resource ID metadata, helping downstream
      model workflows preserve richer source identity during processing. [Commit](https://github.com/open-webui/open-webui/commit/c3c8c605d76a3b0ee067307f9cef6d081658e287)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F9E9 **Richer Anthropic tool results.** Anthropic-compatible tool
      calls now preserve more tool result content types, including images and structured
      search or document outputs, so models can use fuller tool context instead of
      receiving only plain text fragments. [#23188](https://github.com/open-webui/open-webui/issues/23188),
      [Commit](https://github.com/open-webui/open-webui/commit/40f5b3d135190dc9a2d8e94dbb1b2cbcbd829132)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F4DA **Channel document context retention.** Channel conversations
      now preserve and load the correct stored message history so model responses
      can use uploaded and retrieved document context more reliably. [#23686](https://github.com/open-webui/open-webui/issues/23686),
      [Commit](https://github.com/open-webui/open-webui/commit/cf4218e688def6f11d195aeda6665ae5b5376b67),
      [Commit](https://github.com/open-webui/open-webui/commit/18fe17127a7175579506e7456d3e5aba201371e6)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F6A8 **Provider SSE error visibility.** Provider failures returned
      with streaming content types are now surfaced as proper API errors and logged
      clearly, so issues like context-window limits no longer fail silently during
      chat generation. [#23379](https://github.com/open-webui/open-webui/pull/23379)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F511 **User invite token expiry.** New user invite logins now respect
      the configured \"JWT_EXPIRES_IN\" setting, so signup tokens expire as expected
      instead of using the default lifetime. [#23576](https://github.com/open-webui/open-webui/pull/23576)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F4DA **Batch file processing database handling.** Batch knowledge
      file processing now consistently uses the active database session, preventing
      failures caused by missing database context during file ownership checks and
      update writes. [#23137](https://github.com/open-webui/open-webui/issues/23137)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: ✉️ **Context-aware input action button.** The input now shows the send
      action when text or files are present during generation, while keeping stop
      controls for truly empty input states to avoid action confusion. [Commit](https://github.com/open-webui/open-webui/commit/86472bb4453af7ea4e5ddc8d127b14d8e67733bc),
      [#23306](https://github.com/open-webui/open-webui/issues/23306)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F4C9 **Pyodide prompt cache stability.** Pyodide code interpreter
      context is now appended to the system prompt instead of user messages, preserving
      stable prefix caching across turns and reducing repeated token costs in long
      native tool-calling chats. [#23269](https://github.com/open-webui/open-webui/issues/23269)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 8-context-window-changes-in-v0-9-0
  source_release: open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a
  source_type: github_releases
  theme: context-window
  title: 8 Context Window changes in v0.9.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-04-16-add-statusline-command-with-footer-alias-to-customize-which-items-appear-in-the|Add
  /statusline command (with /footer alias) to customize which items appear…]]'
- '[[Changes/GitHub Copilot CLI/2026-04-17-3-context-window-changes-in-v1-0-32|3 Context
  Window changes in v1.0.32]]'
- '[[Changes/Codex CLI/2026-04-20-10-context-window-changes-in-rust-v0-122-0|10 Context
  Window changes in rust-v0.122.0]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a|open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a]]'
source_type: github_releases
theme: context-window
title: 8 Context Window changes in v0.9.0
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Context Window changes in v0.9.0

**Open WebUI** · 2026-04-21 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.0) · from [[Releases/Open WebUI/open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a|v0.9.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🏷️ **Source context metadata.** Retrieval source context now includes each source’s resource type and resource ID metadata, helping downstream model workflows preserve richer source identity during processing. [Commit](https://github.com/open-webui/open-webui/commit/c3c8c605d76a3b0ee067307f9cef6d081658e287)

> 🧩 **Richer Anthropic tool results.** Anthropic-compatible tool calls now preserve more tool result content types, including images and structured search or document outputs, so models can use fuller tool context instead of receiving only plain text fragments. [#23188](https://github.com/open-webui/open-webui/issues/23188), [Commit](https://github.com/open-webui/open-webui/commit/40f5b3d135190dc9a2d8e94dbb1b2cbcbd829132)

> 📚 **Channel document context retention.** Channel conversations now preserve and load the correct stored message history so model responses can use uploaded and retrieved document context more reliably. [#23686](https://github.com/open-webui/open-webui/issues/23686), [Commit](https://github.com/open-webui/open-webui/commit/cf4218e688def6f11d195aeda6665ae5b5376b67), [Commit](https://github.com/open-webui/open-webui/commit/18fe17127a7175579506e7456d3e5aba201371e6)

> 🚨 **Provider SSE error visibility.** Provider failures returned with streaming content types are now surfaced as proper API errors and logged clearly, so issues like context-window limits no longer fail silently during chat generation. [#23379](https://github.com/open-webui/open-webui/pull/23379)

> 🔑 **User invite token expiry.** New user invite logins now respect the configured "JWT_EXPIRES_IN" setting, so signup tokens expire as expected instead of using the default lifetime. [#23576](https://github.com/open-webui/open-webui/pull/23576)

> 📚 **Batch file processing database handling.** Batch knowledge file processing now consistently uses the active database session, preventing failures caused by missing database context during file ownership checks and update writes. [#23137](https://github.com/open-webui/open-webui/issues/23137)

> ✉️ **Context-aware input action button.** The input now shows the send action when text or files are present during generation, while keeping stop controls for truly empty input states to avoid action confusion. [Commit](https://github.com/open-webui/open-webui/commit/86472bb4453af7ea4e5ddc8d127b14d8e67733bc), [#23306](https://github.com/open-webui/open-webui/issues/23306)

> 📉 **Pyodide prompt cache stability.** Pyodide code interpreter context is now appended to the system prompt instead of user messages, preserving stable prefix caching across turns and reducing repeated token costs in long native tool-calling chats. [#23269](https://github.com/open-webui/open-webui/issues/23269)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-04-21-3-files-and-data-changes-in-v0-9-0|3 Files and Data changes in v0.9.0]] · Files and Data
- [[Changes/Open WebUI/2026-04-21-4-image-generation-changes-in-v0-9-0|4 Image Generation changes in v0.9.0]] · Image Generation
- [[Changes/Open WebUI/2026-04-21-28-model-support-changes-in-v0-9-0|28 Model Support changes in v0.9.0]] · Model Support
- [[Changes/Open WebUI/2026-04-21-5-editor-experience-changes-in-v0-9-0|5 Editor Experience changes in v0.9.0]] · Editor Experience
- [[Changes/Open WebUI/2026-04-21-persistent-chat-payload-efficiency-persisted-chats-now-use-server-side-history-l|🚀 Persistent chat payload efficiency. Persisted chats now use server-side…]] · Multimodal Input
- [[Changes/Open WebUI/2026-04-21-24-reliability-and-performance-changes-in-v0-9-0|24 Reliability and Performance changes in v0.9.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-04-21-4-apps-and-integrations-changes-in-v0-9-0|4 Apps and Integrations changes in v0.9.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-04-21-46-developer-workflow-changes-in-v0-9-0|46 Developer Workflow changes in v0.9.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-04-21-8-automation-and-scheduling-changes-in-v0-9-0|8 Automation and Scheduling changes in v0.9.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-04-21-7-memory-and-personalization-changes-in-v0-9-0|7 Memory and Personalization changes in v0.9.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-04-21-2-mobile-and-desktop-changes-in-v0-9-0|2 Mobile and Desktop changes in v0.9.0]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-04-21-17-interface-experience-changes-in-v0-9-0|17 Interface Experience changes in v0.9.0]] · Interface Experience
- [[Changes/Open WebUI/2026-04-21-11-safety-and-privacy-changes-in-v0-9-0|11 Safety and Privacy changes in v0.9.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-04-21-4-search-and-browsing-changes-in-v0-9-0|4 Search and Browsing changes in v0.9.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-04-21-shared-chat-access-controls-you-can-now-control-who-has-access-to-a-shared-chat|🔗 Shared chat access controls. You can now control who has access to a shared…]] · Collaboration
- [[Changes/Open WebUI/2026-04-21-4-voice-and-audio-changes-in-v0-9-0|4 Voice and Audio changes in v0.9.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-04-21-17-account-and-access-changes-in-v0-9-0|17 Account and Access changes in v0.9.0]] · Account and Access
- [[Changes/Open WebUI/2026-04-21-21-other-changes-in-v0-9-0|21 other changes in v0.9.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-04-20 · Codex CLI · [[Changes/Codex CLI/2026-04-20-10-context-window-changes-in-rust-v0-122-0|10 Context Window changes in rust-v0.122.0]]
- Later: 2026-04-23 · Codex CLI · [[Changes/Codex CLI/2026-04-23-18794-organize-context-fragments-pakrym-oai|♯18794 Organize context fragments @pakrym-oai]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-04 · Cursor · [[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2 Context Window changes in 0.2.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-04-21-65e89b&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-04-21-8-context-window-changes-in-v0-9-0.md%0ACard%20ID%3A%20open-webui-2026-04-21-65e89b%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->