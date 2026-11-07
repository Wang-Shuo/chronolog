---
card_id: open-webui-2026-05-09-7a5713
date: '2026-05-09'
description: "Open WebUI · 2026-05-09 · Developer Workflow: 22 changes in v0.9.3 —
  \U0001F5D1️ **Delete from conversation menu.** You can now delete the current conversation
  directly…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2797
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8694f9f7db4657e3174600c44bc7dfa9acfdc6a8692c522f70dfc6069b6bcf73
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-05-09-7a5713
  comparison: ''
  date: '2026-05-09'
  description: 'Open WebUI — v0.9.3: 22 Developer Workflow changes'
  evidence:
  - quote: "\U0001F5D1️ **Delete from conversation menu.** You can now delete the
      current conversation directly from the chat menu with a confirmation step, so
      cleanup is faster without searching through the full chat list. [Commit](https://github.com/open-webui/open-webui/commit/ef6d4f2d6c4b79c7e12e864a4fcb6a57ee84e5d4),
      [#24329](https://github.com/open-webui/open-webui/issues/24329)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: ⬆️ **Scroll to Top shortcut.** Long conversations now include a Scroll
      to Top action in the chat menu when you are away from the top, making it much
      faster to jump back to the beginning of a chat. [Commit](https://github.com/open-webui/open-webui/commit/cdfcbc4af6e9aec835b88dc1806a2a46711e6947),
      [#24133](https://github.com/open-webui/open-webui/issues/24133)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F680 **Smarter function dependency installs.** Function dependencies
      are now skipped when they were already preinstalled and unchanged, reducing
      first-load delays and repeated package installation churn after startup. [Commit](https://github.com/open-webui/open-webui/commit/ae43562b869b24699408e5ab107261a0a8bdb4bc),
      [#24166](https://github.com/open-webui/open-webui/pull/24166)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F9F5 **Background code execution reliability.** Code execution no
      longer hangs indefinitely when you switch conversations or browser tabs during
      a run, and disconnected or inactive sessions now fail with a clear timeout error
      instead of endless processing. [Commit](https://github.com/open-webui/open-webui/commit/552bbcecfae5ae273ab98e2ce3e540d0771aa964),
      [#24089](https://github.com/open-webui/open-webui/issues/24089)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F9F5 **Active task state recovery.** Chat input no longer stays
      blocked by unrelated background tasks after a response is already complete,
      and interrupted assistant replies are now marked done more reliably. [Commit](https://github.com/open-webui/open-webui/commit/04bd0425ead28185bcd124e77892e31209a6e15b),
      [#23264](https://github.com/open-webui/open-webui/pull/23264)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F4CC **Per-user note pinning behavior.** Pinned notes are now tracked
      per user instead of with a shared note-level flag, so one person’s pin changes
      no longer affect everyone else. [Commit](https://github.com/open-webui/open-webui/commit/33e588cf09b294f0abe08b9566efa8545a7dbf92)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F9F1 **Custom header value coercion.** Custom header values are
      now converted to text before requests are sent, preventing request failures
      when non-text values are configured. [Commit](https://github.com/open-webui/open-webui/commit/9907c0a25ae830d134af70022238715f834d20c6),
      [#24164](https://github.com/open-webui/open-webui/pull/24164)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F4F8 **Complete chat image capture.** Downloaded chat snapshots
      now include all messages more reliably through visibility overrides and layout
      timing improvements during capture. [Commit](https://github.com/open-webui/open-webui/commit/34146ab60f5dc1a2f8bdda8e61ce02797233a25d),
      [Commit](https://github.com/open-webui/open-webui/commit/1baf73bdd56f4e5ded12a4bd3c168f4d2a70b840),
      [#24088](https://github.com/open-webui/open-webui/issues/24088)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F5D3️ **Calendar deletion lock handling.** Calendar deletion now
      avoids SQLite write-lock contention by revoking calendar access grants in a
      separate transaction after calendar and event removal. [Commit](https://github.com/open-webui/open-webui/commit/1d892ce2c513c4d933c902de5e5d76c317a06dd2)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F9E9 **Filter and internal tool coexistence.** Internal tools now
      remain available when filters add provider-native tools, so filter-added tools
      no longer replace the built-in tool set during request processing. [Commit](https://github.com/open-webui/open-webui/commit/02f9fe78907c2ecf6f1d93646cbfa2173409bbe8),
      [#24237](https://github.com/open-webui/open-webui/issues/24237)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F9F0 **OpenAPI tool schema parsing.** OpenAPI tool imports now ignore
      non-method path item fields and correctly resolve nested composition schemas,
      preventing invalid tool parsing for compatible specs. [Commit](https://github.com/open-webui/open-webui/commit/85c7373f68ac3e39a9cd37e63b6926b13fb8b8cc),
      [#23254](https://github.com/open-webui/open-webui/pull/23254)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F9FE **Final markdown render flush.** Streaming markdown now forces
      an immediate final parse when generation completes, preventing stale or partially
      rendered final output. [Commit](https://github.com/open-webui/open-webui/commit/29f6c72e879d67f23021938e24a21914cc9fb120),
      [#24088](https://github.com/open-webui/open-webui/issues/24088)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F50E **Knowledge content search matching.** Knowledge file search
      now matches both file titles and file content, so relevant files are easier
      to find even when the keyword is not in the filename. [Commit](https://github.com/open-webui/open-webui/commit/11e076817ae5db34621ce03136353248f7377d97),
      [#24297](https://github.com/open-webui/open-webui/pull/24297)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F9FE **Citation overflow badge readability.** Citation overflow
      badges now keep multi-digit counts readable in a single compact bubble, preventing
      wrapped or cramped display when many sources are attached. [Commit](https://github.com/open-webui/open-webui/commit/23ff9943a9fc8c314100fa074157853fbece1a55),
      [#24391](https://github.com/open-webui/open-webui/pull/24391)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F9F9 **Embedding model name trimming.** Embedding model names entered
      in Documents settings now automatically trim surrounding whitespace, preventing
      silent embedding failures caused by accidental trailing spaces. [Commit](https://github.com/open-webui/open-webui/commit/6082e1adaebc8aa3e7f55265c8dc2dbe130c0446),
      [#24090](https://github.com/open-webui/open-webui/issues/24090)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F310 **SearXNG language parameter handling.** Web searches now send
      clean multi-language values without trailing separators, so SearXNG requests
      no longer fail when multiple languages are selected. [Commit](https://github.com/open-webui/open-webui/commit/6dff85b9d205cfc4bc2845dac40909b8d859910c),
      [#24198](https://github.com/open-webui/open-webui/issues/24198)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F4CE **Chat attachment display recovery.** Files attached by chat
      tools now appear reliably in assistant responses, including non-image file attachments
      that were previously hidden. [Commit](https://github.com/open-webui/open-webui/commit/7eeff2fdf945024585a01b72071a61971afc844d),
      [#24332](https://github.com/open-webui/open-webui/pull/24332)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F504 **Config import and Redis consistency.** Imported settings
      now remain effective after import because configuration values are immediately
      synchronized to Redis, preventing stale cached values from overriding imported
      permissions and settings. [Commit](https://github.com/open-webui/open-webui/commit/55a572cd398c9b4e6118728f8f129941437aa225),
      [Commit](https://github.com/open-webui/open-webui/commit/1c1c8b18e5cc90ca3c6961a4c193a4363febbc83),
      [#24346](https://github.com/open-webui/open-webui/issues/24346)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F517 **Admin shared chat links.** Admin users can now open and clone
      shared chat links reliably without 401 errors because shared links are now resolved
      by share ID first, with safe fallback behavior for direct chat ID access. [Commit](https://github.com/open-webui/open-webui/commit/cde21b9f6dc11575a668484f42440824ec5a4fae),
      [#24311](https://github.com/open-webui/open-webui/issues/24311), [#24096](https://github.com/open-webui/open-webui/issues/24096)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F4BE **Chat settings persistence.** System prompts and other chat-level
      settings now persist correctly after creating a new chat and reloading, preventing
      prompt loss in affected conversations. [Commit](https://github.com/open-webui/open-webui/commit/86df8bf27e1b84abbe2eeedcc8650df59c7d23d6),
      [#24193](https://github.com/open-webui/open-webui/issues/24193), [#24270](https://github.com/open-webui/open-webui/issues/24270)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: ☁️ **OneDrive option visibility.** OneDrive personal and business upload
      options now appear only when their respective client IDs are configured, preventing
      unavailable options from showing in attachment menus. [Commit](https://github.com/open-webui/open-webui/commit/b72019db393a658ca0ceecdcc59b70f6cc5dcd40),
      [#24411](https://github.com/open-webui/open-webui/issues/24411)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F501 **Single-confirmation connection deletion.** Deleting OpenAI,
      Ollama, tool server, and terminal server connections now shows exactly one confirmation
      dialog instead of two, because redundant outer confirmation wrappers were removed
      from all connection components."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 22-developer-workflow-changes-in-v0-9-3
  source_release: open-webui-2026-05-09-v0-9-3-github-319872270-bb8aabca
  source_type: github_releases
  theme: developer-workflow
  title: 22 Developer Workflow changes in v0.9.3
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-05-08-2-developer-workflow-changes-in-v1-0-44|2
  Developer Workflow changes in v1.0.44]]'
- '[[Changes/Raycast/2026-05-08-ai-commands-improved-summarize-webpage-command-giving-responses-that-were-too-sh|AI
  Commands : Improved summarize webpage command giving responses that were too short]]'
- '[[Changes/Raycast/2026-05-08-2-developer-workflow-changes-in-raycast-windows-0-56|2
  Developer Workflow changes in Raycast windows 0.56]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-05-09-v0-9-3-github-319872270-bb8aabca|open-webui-2026-05-09-v0-9-3-github-319872270-bb8aabca]]'
source_type: github_releases
theme: developer-workflow
title: 22 Developer Workflow changes in v0.9.3
type: change
---

<!-- chronolog:begin region="header" -->
# 22 Developer Workflow changes in v0.9.3

**Open WebUI** · 2026-05-09 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.3) · from [[Releases/Open WebUI/open-webui-2026-05-09-v0-9-3-github-319872270-bb8aabca|v0.9.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🗑️ **Delete from conversation menu.** You can now delete the current conversation directly from the chat menu with a confirmation step, so cleanup is faster without searching through the full chat list. [Commit](https://github.com/open-webui/open-webui/commit/ef6d4f2d6c4b79c7e12e864a4fcb6a57ee84e5d4), [#24329](https://github.com/open-webui/open-webui/issues/24329)

> ⬆️ **Scroll to Top shortcut.** Long conversations now include a Scroll to Top action in the chat menu when you are away from the top, making it much faster to jump back to the beginning of a chat. [Commit](https://github.com/open-webui/open-webui/commit/cdfcbc4af6e9aec835b88dc1806a2a46711e6947), [#24133](https://github.com/open-webui/open-webui/issues/24133)

> 🚀 **Smarter function dependency installs.** Function dependencies are now skipped when they were already preinstalled and unchanged, reducing first-load delays and repeated package installation churn after startup. [Commit](https://github.com/open-webui/open-webui/commit/ae43562b869b24699408e5ab107261a0a8bdb4bc), [#24166](https://github.com/open-webui/open-webui/pull/24166)

> 🧵 **Background code execution reliability.** Code execution no longer hangs indefinitely when you switch conversations or browser tabs during a run, and disconnected or inactive sessions now fail with a clear timeout error instead of endless processing. [Commit](https://github.com/open-webui/open-webui/commit/552bbcecfae5ae273ab98e2ce3e540d0771aa964), [#24089](https://github.com/open-webui/open-webui/issues/24089)

> 🧵 **Active task state recovery.** Chat input no longer stays blocked by unrelated background tasks after a response is already complete, and interrupted assistant replies are now marked done more reliably. [Commit](https://github.com/open-webui/open-webui/commit/04bd0425ead28185bcd124e77892e31209a6e15b), [#23264](https://github.com/open-webui/open-webui/pull/23264)

> 📌 **Per-user note pinning behavior.** Pinned notes are now tracked per user instead of with a shared note-level flag, so one person’s pin changes no longer affect everyone else. [Commit](https://github.com/open-webui/open-webui/commit/33e588cf09b294f0abe08b9566efa8545a7dbf92)

> 🧱 **Custom header value coercion.** Custom header values are now converted to text before requests are sent, preventing request failures when non-text values are configured. [Commit](https://github.com/open-webui/open-webui/commit/9907c0a25ae830d134af70022238715f834d20c6), [#24164](https://github.com/open-webui/open-webui/pull/24164)

> 📸 **Complete chat image capture.** Downloaded chat snapshots now include all messages more reliably through visibility overrides and layout timing improvements during capture. [Commit](https://github.com/open-webui/open-webui/commit/34146ab60f5dc1a2f8bdda8e61ce02797233a25d), [Commit](https://github.com/open-webui/open-webui/commit/1baf73bdd56f4e5ded12a4bd3c168f4d2a70b840), [#24088](https://github.com/open-webui/open-webui/issues/24088)

> 🗓️ **Calendar deletion lock handling.** Calendar deletion now avoids SQLite write-lock contention by revoking calendar access grants in a separate transaction after calendar and event removal. [Commit](https://github.com/open-webui/open-webui/commit/1d892ce2c513c4d933c902de5e5d76c317a06dd2)

> 🧩 **Filter and internal tool coexistence.** Internal tools now remain available when filters add provider-native tools, so filter-added tools no longer replace the built-in tool set during request processing. [Commit](https://github.com/open-webui/open-webui/commit/02f9fe78907c2ecf6f1d93646cbfa2173409bbe8), [#24237](https://github.com/open-webui/open-webui/issues/24237)

> 🧰 **OpenAPI tool schema parsing.** OpenAPI tool imports now ignore non-method path item fields and correctly resolve nested composition schemas, preventing invalid tool parsing for compatible specs. [Commit](https://github.com/open-webui/open-webui/commit/85c7373f68ac3e39a9cd37e63b6926b13fb8b8cc), [#23254](https://github.com/open-webui/open-webui/pull/23254)

> 🧾 **Final markdown render flush.** Streaming markdown now forces an immediate final parse when generation completes, preventing stale or partially rendered final output. [Commit](https://github.com/open-webui/open-webui/commit/29f6c72e879d67f23021938e24a21914cc9fb120), [#24088](https://github.com/open-webui/open-webui/issues/24088)

> 🔎 **Knowledge content search matching.** Knowledge file search now matches both file titles and file content, so relevant files are easier to find even when the keyword is not in the filename. [Commit](https://github.com/open-webui/open-webui/commit/11e076817ae5db34621ce03136353248f7377d97), [#24297](https://github.com/open-webui/open-webui/pull/24297)

> 🧾 **Citation overflow badge readability.** Citation overflow badges now keep multi-digit counts readable in a single compact bubble, preventing wrapped or cramped display when many sources are attached. [Commit](https://github.com/open-webui/open-webui/commit/23ff9943a9fc8c314100fa074157853fbece1a55), [#24391](https://github.com/open-webui/open-webui/pull/24391)

> 🧹 **Embedding model name trimming.** Embedding model names entered in Documents settings now automatically trim surrounding whitespace, preventing silent embedding failures caused by accidental trailing spaces. [Commit](https://github.com/open-webui/open-webui/commit/6082e1adaebc8aa3e7f55265c8dc2dbe130c0446), [#24090](https://github.com/open-webui/open-webui/issues/24090)

> 🌐 **SearXNG language parameter handling.** Web searches now send clean multi-language values without trailing separators, so SearXNG requests no longer fail when multiple languages are selected. [Commit](https://github.com/open-webui/open-webui/commit/6dff85b9d205cfc4bc2845dac40909b8d859910c), [#24198](https://github.com/open-webui/open-webui/issues/24198)

> 📎 **Chat attachment display recovery.** Files attached by chat tools now appear reliably in assistant responses, including non-image file attachments that were previously hidden. [Commit](https://github.com/open-webui/open-webui/commit/7eeff2fdf945024585a01b72071a61971afc844d), [#24332](https://github.com/open-webui/open-webui/pull/24332)

> 🔄 **Config import and Redis consistency.** Imported settings now remain effective after import because configuration values are immediately synchronized to Redis, preventing stale cached values from overriding imported permissions and settings. [Commit](https://github.com/open-webui/open-webui/commit/55a572cd398c9b4e6118728f8f129941437aa225), [Commit](https://github.com/open-webui/open-webui/commit/1c1c8b18e5cc90ca3c6961a4c193a4363febbc83), [#24346](https://github.com/open-webui/open-webui/issues/24346)

> 🔗 **Admin shared chat links.** Admin users can now open and clone shared chat links reliably without 401 errors because shared links are now resolved by share ID first, with safe fallback behavior for direct chat ID access. [Commit](https://github.com/open-webui/open-webui/commit/cde21b9f6dc11575a668484f42440824ec5a4fae), [#24311](https://github.com/open-webui/open-webui/issues/24311), [#24096](https://github.com/open-webui/open-webui/issues/24096)

> 💾 **Chat settings persistence.** System prompts and other chat-level settings now persist correctly after creating a new chat and reloading, preventing prompt loss in affected conversations. [Commit](https://github.com/open-webui/open-webui/commit/86df8bf27e1b84abbe2eeedcc8650df59c7d23d6), [#24193](https://github.com/open-webui/open-webui/issues/24193), [#24270](https://github.com/open-webui/open-webui/issues/24270)

> ☁️ **OneDrive option visibility.** OneDrive personal and business upload options now appear only when their respective client IDs are configured, preventing unavailable options from showing in attachment menus. [Commit](https://github.com/open-webui/open-webui/commit/b72019db393a658ca0ceecdcc59b70f6cc5dcd40), [#24411](https://github.com/open-webui/open-webui/issues/24411)

> 🔁 **Single-confirmation connection deletion.** Deleting OpenAI, Ollama, tool server, and terminal server connections now shows exactly one confirmation dialog instead of two, because redundant outer confirmation wrappers were removed from all connection components.

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-05-09-5-search-and-browsing-changes-in-v0-9-3|5 Search and Browsing changes in v0.9.3]] · Search and Browsing
- [[Changes/Open WebUI/2026-05-09-10-voice-and-audio-changes-in-v0-9-3|10 Voice and Audio changes in v0.9.3]] · Voice and Audio
- [[Changes/Open WebUI/2026-05-09-5-editor-experience-changes-in-v0-9-3|5 Editor Experience changes in v0.9.3]] · Editor Experience
- [[Changes/Open WebUI/2026-05-09-8-interface-experience-changes-in-v0-9-3|8 Interface Experience changes in v0.9.3]] · Interface Experience
- [[Changes/Open WebUI/2026-05-09-4-context-window-changes-in-v0-9-3|4 Context Window changes in v0.9.3]] · Context Window
- [[Changes/Open WebUI/2026-05-09-3-apps-and-integrations-changes-in-v0-9-3|3 Apps and Integrations changes in v0.9.3]] · Apps and Integrations
- [[Changes/Open WebUI/2026-05-09-2-automation-and-scheduling-changes-in-v0-9-3|2 Automation and Scheduling changes in v0.9.3]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-05-09-4-reliability-and-performance-changes-in-v0-9-3|4 Reliability and Performance changes in v0.9.3]] · Reliability and Performance
- [[Changes/Open WebUI/2026-05-09-4-account-and-access-changes-in-v0-9-3|4 Account and Access changes in v0.9.3]] · Account and Access
- [[Changes/Open WebUI/2026-05-09-sanitized-spreadsheet-html-previews-spreadsheet-previews-now-sanitize-generated|🛡️ Sanitized spreadsheet HTML previews. Spreadsheet previews now sanitize…]] · Files and Data
- [[Changes/Open WebUI/2026-05-09-9-model-support-changes-in-v0-9-3|9 Model Support changes in v0.9.3]] · Model Support
- [[Changes/Open WebUI/2026-05-09-3-safety-and-privacy-changes-in-v0-9-3|3 Safety and Privacy changes in v0.9.3]] · Safety and Privacy
- [[Changes/Open WebUI/2026-05-09-faster-memory-query-performance-per-user-memory-lookups-and-deletions-now-run-mu|⚡ Faster memory query performance. Per-user memory lookups and deletions now run…]] · Memory and Personalization
- [[Changes/Open WebUI/2026-05-09-5-other-changes-in-v0-9-3|5 other changes in v0.9.3]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-05-08 · Raycast · [[Changes/Raycast/2026-05-08-2-developer-workflow-changes-in-raycast-windows-0-56|2 Developer Workflow changes in Raycast windows 0.56]]
- Later: 2026-05-09 · OpenCode · [[Changes/OpenCode/2026-05-09-3-developer-workflow-changes-in-v1-14-44-2|3 Developer Workflow changes in v1.14.44 + 2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-05-09-7a5713&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-05-09-22-developer-workflow-changes-in-v0-9-3.md%0ACard%20ID%3A%20open-webui-2026-05-09-7a5713%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.3%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->