---
card_id: open-webui-2026-03-01-c2467f
date: '2026-03-01'
description: "Open WebUI · 2026-03-01 · Developer Workflow: 9 changes in v0.8.6 —
  \U0001F4C4 **Terminal file creation.** Users can now create new empty files directly
  in the Open…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2728
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 377ebdc13df3ef9047246c66612d5bf54cbc62c5e40c0e58cc135453584af8fa
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-03-01-c2467f
  comparison: ''
  date: '2026-03-01'
  description: 'Open WebUI — v0.8.6: 9 Developer Workflow changes'
  evidence:
  - quote: "\U0001F4C4 **Terminal file creation.** Users can now create new empty
      files directly in the Open Terminal file browser, in addition to the existing
      folder creation functionality. [Commit](https://github.com/open-webui/open-webui/commit/234306ff57c9e24314ff805a60de919632465319)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  - quote: ✏️ **Terminal file editing.** Users can now edit text files directly in
      the Open Terminal file browser, with the ability to save changes back to the
      terminal. [Commit](https://github.com/open-webui/open-webui/commit/3d535db304bfc6fa09e655f737de8a36c0482868)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  - quote: "\U0001F6E0️ **Terminal file preview toolbar.** The Open Terminal file
      browser now displays contextual toolbar buttons based on file type, including
      preview/source toggle for Markdown and CSV files, reset view for images, and
      improved editing controls for text files. [Commit](https://github.com/open-webui/open-webui/commit/d2b38127d0572006577b85c770607b04782de4f9)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  - quote: "\U0001F504 **Terminal file write refresh.** The file browser now automatically
      refreshes when files are written or modified via the write_file or replace_file_content
      tools, eliminating the need to manually refresh. [Commit](https://github.com/open-webui/open-webui/commit/18865a9fef1bb154603b7b8af0116a10560e03ac)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  - quote: "\U0001F6E0️ **Tool server advanced options toggle.** Advanced OpenAPI
      configuration options in the tool server modal are now hidden by default behind
      a toggle, simplifying the interface for basic setups. The admin settings tab
      was also renamed from \"Tools\" to \"Integrations\" for clearer organization.
      [Commit](https://github.com/open-webui/open-webui/commit/f0c71e5a6d971af7322d4245313e5e04620253f0),
      [Commit](https://github.com/open-webui/open-webui/commit/4731ccb73c4b4bab78fd86fec7b2c231af8cca8b)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  - quote: "\U0001F5C4️ **Database migration execution.** Database migrations now
      run correctly on startup, fixing a circular import issue that caused schema
      updates to fail silently. [#21848](https://github.com/open-webui/open-webui/pull/21848),
      [Commit](https://github.com/open-webui/open-webui/commit/87d33f6e18196876603eee7d1bf8e4977c7fa9c1)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  - quote: "\U0001F9E0 **Reasoning model KV cache preservation.** Reasoning model
      thinking tags are no longer stored as HTML in the database, preserving KV cache
      efficiency for backends like llama.cpp and ensuring faster subsequent conversation
      turns. [#21815](https://github.com/open-webui/open-webui/issues/21815), [Commit](https://github.com/open-webui/open-webui/commit/81781e6495dcc788c863bbf6b4aa4cf0ddd9fdcc)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  - quote: "\U0001F4C4 **Web content knowledge base append.** Processing web URLs
      with overwrite=false now correctly appends content to existing knowledge bases
      instead of silently doing nothing, fixing a regression where no content was
      being added. [#21786](https://github.com/open-webui/open-webui/pull/21786),
      [Commit](https://github.com/open-webui/open-webui/commit/5ee509325970f01524348b0f91081110340f2e7e)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  - quote: "\U0001F4BB **Code block UI.** Code block headers are now sticky and properly
      positioned, with language labels now showing tooltips for truncated text. [Commit](https://github.com/open-webui/open-webui/commit/6b462ff121d28cd2d335db7763052622d374e3a5)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 9-developer-workflow-changes-in-v0-8-6
  source_release: open-webui-2026-03-01-v0-8-6-github-291846033-263bca05
  source_type: github_releases
  theme: developer-workflow
  title: 9 Developer Workflow changes in v0.8.6
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-02-27-type-to-reference-github-issues-pull-requests-and-discussions|Type
  ♯ to reference GitHub issues, pull requests and discussions]]'
- '[[Changes/Claude Code/2026-02-28-improved-model-command-to-show-the-currently-active-model-in-the-slash-command-m|Improved
  /model command to show the currently active model in the slash command menu]]'
- '[[Changes/Claude Code/2026-02-28-added-simplify-and-batch-bundled-slash-commands|Added
  /simplify and /batch bundled slash commands]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-03-01-v0-8-6-github-291846033-263bca05|open-webui-2026-03-01-v0-8-6-github-291846033-263bca05]]'
source_type: github_releases
theme: developer-workflow
title: 9 Developer Workflow changes in v0.8.6
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Developer Workflow changes in v0.8.6

**Open WebUI** · 2026-03-01 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.6) · from [[Releases/Open WebUI/open-webui-2026-03-01-v0-8-6-github-291846033-263bca05|v0.8.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📄 **Terminal file creation.** Users can now create new empty files directly in the Open Terminal file browser, in addition to the existing folder creation functionality. [Commit](https://github.com/open-webui/open-webui/commit/234306ff57c9e24314ff805a60de919632465319)

> ✏️ **Terminal file editing.** Users can now edit text files directly in the Open Terminal file browser, with the ability to save changes back to the terminal. [Commit](https://github.com/open-webui/open-webui/commit/3d535db304bfc6fa09e655f737de8a36c0482868)

> 🛠️ **Terminal file preview toolbar.** The Open Terminal file browser now displays contextual toolbar buttons based on file type, including preview/source toggle for Markdown and CSV files, reset view for images, and improved editing controls for text files. [Commit](https://github.com/open-webui/open-webui/commit/d2b38127d0572006577b85c770607b04782de4f9)

> 🔄 **Terminal file write refresh.** The file browser now automatically refreshes when files are written or modified via the write_file or replace_file_content tools, eliminating the need to manually refresh. [Commit](https://github.com/open-webui/open-webui/commit/18865a9fef1bb154603b7b8af0116a10560e03ac)

> 🛠️ **Tool server advanced options toggle.** Advanced OpenAPI configuration options in the tool server modal are now hidden by default behind a toggle, simplifying the interface for basic setups. The admin settings tab was also renamed from "Tools" to "Integrations" for clearer organization. [Commit](https://github.com/open-webui/open-webui/commit/f0c71e5a6d971af7322d4245313e5e04620253f0), [Commit](https://github.com/open-webui/open-webui/commit/4731ccb73c4b4bab78fd86fec7b2c231af8cca8b)

> 🗄️ **Database migration execution.** Database migrations now run correctly on startup, fixing a circular import issue that caused schema updates to fail silently. [#21848](https://github.com/open-webui/open-webui/pull/21848), [Commit](https://github.com/open-webui/open-webui/commit/87d33f6e18196876603eee7d1bf8e4977c7fa9c1)

> 🧠 **Reasoning model KV cache preservation.** Reasoning model thinking tags are no longer stored as HTML in the database, preserving KV cache efficiency for backends like llama.cpp and ensuring faster subsequent conversation turns. [#21815](https://github.com/open-webui/open-webui/issues/21815), [Commit](https://github.com/open-webui/open-webui/commit/81781e6495dcc788c863bbf6b4aa4cf0ddd9fdcc)

> 📄 **Web content knowledge base append.** Processing web URLs with overwrite=false now correctly appends content to existing knowledge bases instead of silently doing nothing, fixing a regression where no content was being added. [#21786](https://github.com/open-webui/open-webui/pull/21786), [Commit](https://github.com/open-webui/open-webui/commit/5ee509325970f01524348b0f91081110340f2e7e)

> 💻 **Code block UI.** Code block headers are now sticky and properly positioned, with language labels now showing tooltips for truncated text. [Commit](https://github.com/open-webui/open-webui/commit/6b462ff121d28cd2d335db7763052622d374e3a5)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-03-01-21-reliability-and-performance-changes-in-v0-8-6|21 Reliability and Performance changes in v0.8.6]] · Reliability and Performance
- [[Changes/Open WebUI/2026-03-01-2-search-and-browsing-changes-in-v0-8-6|2 Search and Browsing changes in v0.8.6]] · Search and Browsing
- [[Changes/Open WebUI/2026-03-01-oauth-session-token-decryption-oauth-sessions-are-now-properly-detached-from-the|🔓 OAuth session token decryption. OAuth sessions are now properly detached…]] · Context Window
- [[Changes/Open WebUI/2026-03-01-individual-user-sharing-control-administrators-can-now-disable-individual-user-s|🔐 Individual user sharing control. Administrators can now disable individual…]] · Collaboration
- [[Changes/Open WebUI/2026-03-01-4-interface-experience-changes-in-v0-8-6|4 Interface Experience changes in v0.8.6]] · Interface Experience
- [[Changes/Open WebUI/2026-03-01-3-account-and-access-changes-in-v0-8-6|3 Account and Access changes in v0.8.6]] · Account and Access
- [[Changes/Open WebUI/2026-03-01-4-safety-and-privacy-changes-in-v0-8-6|4 Safety and Privacy changes in v0.8.6]] · Safety and Privacy
- [[Changes/Open WebUI/2026-03-01-8-model-support-changes-in-v0-8-6|8 Model Support changes in v0.8.6]] · Model Support
- [[Changes/Open WebUI/2026-03-01-6-other-changes-in-v0-8-6|6 other changes in v0.8.6]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-02-28 · Claude Code · [[Changes/Claude Code/2026-02-28-added-simplify-and-batch-bundled-slash-commands|Added /simplify and /batch bundled slash commands]]
- Later: 2026-03-02 · Codex CLI · [[Changes/Codex CLI/2026-03-02-3-developer-workflow-changes-in-rust-v0-107-0|3 Developer Workflow changes in rust-v0.107.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-03-01-c2467f&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-03-01-9-developer-workflow-changes-in-v0-8-6.md%0ACard%20ID%3A%20open-webui-2026-03-01-c2467f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.6%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->