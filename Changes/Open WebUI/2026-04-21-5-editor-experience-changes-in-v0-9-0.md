---
card_id: open-webui-2026-04-21-40a161
date: '2026-04-21'
description: "Open WebUI · 2026-04-21 · Editor Experience: 5 changes in v0.9.0 — \U0001F50C
  **Backend outlet filters for local and persisted chats.** Pipeline and function
  outlet…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3
    Editor Experience changes in 0.0.37]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1134
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: editor-experience
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9a25735916e6ec2bbdf6acd9b6e98d88bc052d824542758d00ce34f2e5bff16b
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-04-21-40a161
  comparison: ''
  date: '2026-04-21'
  description: 'Open WebUI — v0.9.0: 5 Editor Experience changes'
  evidence:
  - quote: "\U0001F50C **Backend outlet filters for local and persisted chats.** Pipeline
      and function outlet filters now run reliably in backend completion flows for
      persisted chats and temporary local chats. [#3237](https://github.com/open-webui/open-webui/issues/3237),
      [Commit](https://github.com/open-webui/open-webui/commit/cf4218e688def6f11d195aeda6665ae5b5376b67)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F4DD **Knowledge text editor stability.** The Knowledge \"Add Text
      Content\" modal now uses a plain text editor, avoiding current rich text editor
      issues and keeping drafting behavior consistent with existing knowledge editing
      flows. [Commit](https://github.com/open-webui/open-webui/commit/cd55c3e21237e000c13c6f396bb95b261f3bda82)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F9FE **Prompt save error feedback.** Saving prompt edits now shows
      a clear error toast if the save fails, so failed updates are visible instead
      of silently failing in the editor flow. [Commit](https://github.com/open-webui/open-webui/commit/36a81ad43b7c0d450079f818a7546eaa517e3d95)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F6AB **Missing message completion guard.** Chat completion finalization
      now skips invalid requests without a message identifier, preventing unnecessary
      error toasts caused by rare frontend concurrency timing. [#23184](https://github.com/open-webui/open-webui/pull/23184)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F9E0 **Active message completion accuracy.** Switching chats or
      refreshing during generation no longer marks the currently streaming assistant
      message as finished too early, so thinking blocks and action buttons appear
      at the correct time. [#23171](https://github.com/open-webui/open-webui/issues/23171)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 5-editor-experience-changes-in-v0-9-0
  source_release: open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a
  source_type: github_releases
  theme: editor-experience
  title: 5 Editor Experience changes in v0.9.0
  type: change
related_changes:
- '[[Changes/Ollama/2026-04-16-hermes-and-github-copilot-cli-in-ollama-launch-added-both-integrations-which-can|Hermes
  and GitHub Copilot CLI in ollama launch. Added both integrations…]]'
- '[[Changes/Claude Code/2026-04-17-remote-control-clients-can-now-query-file-autocomplete-suggestions|Remote
  Control clients can now query @-file autocomplete suggestions]]'
- '[[Changes/Claude Code/2026-04-20-2-editor-experience-changes-in-v2-1-116|2 Editor
  Experience changes in v2.1.116]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a|open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a]]'
source_type: github_releases
theme: editor-experience
title: 5 Editor Experience changes in v0.9.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Editor Experience changes in v0.9.0

**Open WebUI** · 2026-04-21 · [[Themes/editor-experience|Editor Experience]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.0) · from [[Releases/Open WebUI/open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a|v0.9.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔌 **Backend outlet filters for local and persisted chats.** Pipeline and function outlet filters now run reliably in backend completion flows for persisted chats and temporary local chats. [#3237](https://github.com/open-webui/open-webui/issues/3237), [Commit](https://github.com/open-webui/open-webui/commit/cf4218e688def6f11d195aeda6665ae5b5376b67)

> 📝 **Knowledge text editor stability.** The Knowledge "Add Text Content" modal now uses a plain text editor, avoiding current rich text editor issues and keeping drafting behavior consistent with existing knowledge editing flows. [Commit](https://github.com/open-webui/open-webui/commit/cd55c3e21237e000c13c6f396bb95b261f3bda82)

> 🧾 **Prompt save error feedback.** Saving prompt edits now shows a clear error toast if the save fails, so failed updates are visible instead of silently failing in the editor flow. [Commit](https://github.com/open-webui/open-webui/commit/36a81ad43b7c0d450079f818a7546eaa517e3d95)

> 🚫 **Missing message completion guard.** Chat completion finalization now skips invalid requests without a message identifier, preventing unnecessary error toasts caused by rare frontend concurrency timing. [#23184](https://github.com/open-webui/open-webui/pull/23184)

> 🧠 **Active message completion accuracy.** Switching chats or refreshing during generation no longer marks the currently streaming assistant message as finished too early, so thinking blocks and action buttons appear at the correct time. [#23171](https://github.com/open-webui/open-webui/issues/23171)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-04-21-3-files-and-data-changes-in-v0-9-0|3 Files and Data changes in v0.9.0]] · Files and Data
- [[Changes/Open WebUI/2026-04-21-4-image-generation-changes-in-v0-9-0|4 Image Generation changes in v0.9.0]] · Image Generation
- [[Changes/Open WebUI/2026-04-21-28-model-support-changes-in-v0-9-0|28 Model Support changes in v0.9.0]] · Model Support
- [[Changes/Open WebUI/2026-04-21-persistent-chat-payload-efficiency-persisted-chats-now-use-server-side-history-l|🚀 Persistent chat payload efficiency. Persisted chats now use server-side…]] · Multimodal Input
- [[Changes/Open WebUI/2026-04-21-8-context-window-changes-in-v0-9-0|8 Context Window changes in v0.9.0]] · Context Window
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
## Nearby in Editor Experience

- Earlier: 2026-04-20 · Claude Code · [[Changes/Claude Code/2026-04-20-2-editor-experience-changes-in-v2-1-116|2 Editor Experience changes in v2.1.116]]
- Later: 2026-04-23 · Claude Code · [[Changes/Claude Code/2026-04-23-config-settings-theme-editor-mode-verbose-etc-now-persist-to-claude-settings-jso|/config settings (theme, editor mode, verbose, etc.) now persist…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-14 · Cursor · [[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3 Editor Experience changes in 0.0.37]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-04-21-40a161&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-04-21-5-editor-experience-changes-in-v0-9-0.md%0ACard%20ID%3A%20open-webui-2026-04-21-40a161%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->