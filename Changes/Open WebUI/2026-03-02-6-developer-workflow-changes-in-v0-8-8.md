---
card_id: open-webui-2026-03-02-fb21ff
date: '2026-03-02'
description: "Open WebUI · 2026-03-02 · Developer Workflow: 6 changes in v0.8.8 —
  \U0001F4C1 **Open Terminal file moving.** Users can now move files and folders between
  directories…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2729
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9936f6ba29c5a0a160a44a4f85e0199a381d340e749abbcdeafcbaf86531788c
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-03-02-fb21ff
  comparison: ''
  date: '2026-03-02'
  description: 'Open WebUI — v0.8.8: 6 Developer Workflow changes'
  evidence:
  - quote: "\U0001F4C1 **Open Terminal file moving.** Users can now move files and
      folders between directories in the Open Terminal file browser by dragging and
      dropping them. [Commit](https://github.com/open-webui/open-webui/commit/0c42cd2c012f9f49816adac897e2b46573b3cb6c),
      [Commit](https://github.com/open-webui/open-webui/commit/72951324dfeef64e09f4776898d675bc1c44f040),
      [Commit](https://github.com/open-webui/open-webui/commit/395098c6f1b7499d37ad55145a5931431d3e72e9),
      [Commit](https://github.com/open-webui/open-webui/commit/11487d66fc1a2dfafbdaa2b7ef939a86caaf3872)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.8
  - quote: "\U0001F4C4 **Open Terminal HTML file preview.** Users can now preview
      HTML files directly in the Open Terminal file browser, with a rendered iframe
      view and source toggle, enabling iterative AI editing of HTML files. [Commit](https://github.com/open-webui/open-webui/commit/3909b62ffcf49839fa57346ed8487ae759811503),
      [Commit](https://github.com/open-webui/open-webui/commit/933a3bbbd3f4fc3eeb0ec52c7965e9ac1c4cea39)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.8
  - quote: "\U0001F310 **Open Terminal WebSocket proxy.** Added a new WebSocket proxy
      endpoint for interactive terminal sessions, enabling real-time bidirectional
      terminal communication with the terminal server. [Commit](https://github.com/open-webui/open-webui/commit/4f6cb771f1afded09aad6199cdb244dd8a6c77a6)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.8
  - quote: ⚙️ **Open Terminal feature toggle.** Administrators can now enable or disable
      the Interactive Terminal feature for Open Terminal via configuration on the
      terminal server, controlling access to terminal routes. [Commit](https://github.com/open-webui/open-webui/commit/b5c3395f79bcc7ff5bc1d82bb86a60583bb3b5bd)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.8
  - quote: "\U0001F50C **Open Terminal tools for direct connections.** Fixed an issue
      where Open Terminal tools were not available to the model when the terminal
      was configured via direct connection settings, ensuring users can now interact
      with terminal files and operations through the AI. [#22137](https://github.com/open-webui/open-webui/issues/22137)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.8
  - quote: "\U0001F527 **Terminal tool null parameter handling.** Fixed a bug where
      null parameters in terminal tool calls were sent as the string \"None\" instead
      of being omitted, causing 422 validation errors from the open-terminal server.
      [#22124](https://github.com/open-webui/open-webui/issues/22124), [#22144](https://github.com/open-webui/open-webui/pull/22144)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.8
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 6-developer-workflow-changes-in-v0-8-8
  source_release: open-webui-2026-03-02-v0-8-8-github-292312215-9d692419
  source_type: github_releases
  theme: developer-workflow
  title: 6 Developer Workflow changes in v0.8.8
  type: change
related_changes:
- '[[Changes/Open WebUI/2026-03-01-9-developer-workflow-changes-in-v0-8-6|9 Developer
  Workflow changes in v0.8.6]]'
- '[[Changes/Codex CLI/2026-03-02-3-developer-workflow-changes-in-rust-v0-107-0|3
  Developer Workflow changes in rust-v0.107.0]]'
- '[[Changes/Open WebUI/2026-03-02-faster-artifact-content-updates-artifact-content-extraction-during-streaming-is|⚡
  Faster artifact content updates. Artifact content extraction during streaming…]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-03-02-v0-8-8-github-292312215-9d692419|open-webui-2026-03-02-v0-8-8-github-292312215-9d692419]]'
source_type: github_releases
theme: developer-workflow
title: 6 Developer Workflow changes in v0.8.8
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Developer Workflow changes in v0.8.8

**Open WebUI** · 2026-03-02 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.8) · from [[Releases/Open WebUI/open-webui-2026-03-02-v0-8-8-github-292312215-9d692419|v0.8.8]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📁 **Open Terminal file moving.** Users can now move files and folders between directories in the Open Terminal file browser by dragging and dropping them. [Commit](https://github.com/open-webui/open-webui/commit/0c42cd2c012f9f49816adac897e2b46573b3cb6c), [Commit](https://github.com/open-webui/open-webui/commit/72951324dfeef64e09f4776898d675bc1c44f040), [Commit](https://github.com/open-webui/open-webui/commit/395098c6f1b7499d37ad55145a5931431d3e72e9), [Commit](https://github.com/open-webui/open-webui/commit/11487d66fc1a2dfafbdaa2b7ef939a86caaf3872)

> 📄 **Open Terminal HTML file preview.** Users can now preview HTML files directly in the Open Terminal file browser, with a rendered iframe view and source toggle, enabling iterative AI editing of HTML files. [Commit](https://github.com/open-webui/open-webui/commit/3909b62ffcf49839fa57346ed8487ae759811503), [Commit](https://github.com/open-webui/open-webui/commit/933a3bbbd3f4fc3eeb0ec52c7965e9ac1c4cea39)

> 🌐 **Open Terminal WebSocket proxy.** Added a new WebSocket proxy endpoint for interactive terminal sessions, enabling real-time bidirectional terminal communication with the terminal server. [Commit](https://github.com/open-webui/open-webui/commit/4f6cb771f1afded09aad6199cdb244dd8a6c77a6)

> ⚙️ **Open Terminal feature toggle.** Administrators can now enable or disable the Interactive Terminal feature for Open Terminal via configuration on the terminal server, controlling access to terminal routes. [Commit](https://github.com/open-webui/open-webui/commit/b5c3395f79bcc7ff5bc1d82bb86a60583bb3b5bd)

> 🔌 **Open Terminal tools for direct connections.** Fixed an issue where Open Terminal tools were not available to the model when the terminal was configured via direct connection settings, ensuring users can now interact with terminal files and operations through the AI. [#22137](https://github.com/open-webui/open-webui/issues/22137)

> 🔧 **Terminal tool null parameter handling.** Fixed a bug where null parameters in terminal tool calls were sent as the string "None" instead of being omitted, causing 422 validation errors from the open-terminal server. [#22124](https://github.com/open-webui/open-webui/issues/22124), [#22144](https://github.com/open-webui/open-webui/pull/22144)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.8.8
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-03-02-chatcontrols-reactivity-fix-fixed-a-svelte-reactivity-issue-where-the-active-tab|⚡ ChatControls reactivity fix. Fixed a Svelte reactivity issue where the active…]] · Editor Experience
- [[Changes/Open WebUI/2026-03-02-general-improvements-various-improvements-were-implemented-across-the-applicatio|🔄 General improvements. Various improvements were implemented across…]] · Reliability and Performance
- [[Changes/Open WebUI/2026-03-02-chat-history-pagination-fixed-an-issue-where-older-messages-in-long-chats-were-n|📜 Chat history pagination. Fixed an issue where older messages in long chats…]] · Interface Experience
- [[Changes/Open WebUI/2026-03-02-3-other-changes-in-v0-8-8|3 other changes in v0.8.8]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-03-02 · Open WebUI · [[Changes/Open WebUI/2026-03-02-faster-artifact-content-updates-artifact-content-extraction-during-streaming-is|⚡ Faster artifact content updates. Artifact content extraction during streaming…]]
- Later: 2026-03-03 · Cline · [[Changes/Cline/2026-03-03-retry-nested-git-restore-and-prevent-silent-git-disabled-leftovers-in-checkpoint|Retry nested git restore and prevent silent .git_disabled leftovers in checkpoints]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-03-02-fb21ff&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-03-02-6-developer-workflow-changes-in-v0-8-8.md%0ACard%20ID%3A%20open-webui-2026-03-02-fb21ff%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.8%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->