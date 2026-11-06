---
card_id: open-webui-2026-03-25-109a7b
date: '2026-03-25'
description: "Open WebUI · 2026-03-25 · Editor Experience: 4 changes in v0.8.11 —
  \U0001F4CC **Knowledge file previews.** Knowledge base files can now be opened in
  a new tab directly…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3
    Editor Experience changes in 0.0.37]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1107
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: editor-experience
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 86e9750cbac8a59a49d32bd9915e80849338dabdddead8f001389349c79830df
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-03-25-109a7b
  comparison: ''
  date: '2026-03-25'
  description: 'Open WebUI — v0.8.11: 4 Editor Experience changes'
  evidence:
  - quote: "\U0001F4CC **Knowledge file previews.** Knowledge base files can now be
      opened in a new tab directly from the file list, making it easier to view content
      without downloading. [#22629](https://github.com/open-webui/open-webui/pull/22629)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: ✏️ **Markdown file editing.** Users can now edit and save Markdown files
      directly in the file navigator, with empty files automatically switching to
      editor mode for immediate editing. [Commit](https://github.com/open-webui/open-webui/commit/47e47e42af682e7f75c8359999f7cdf969bf903e)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F5A5️ **Pyodide file list refresh.** Files created or modified during
      manual code execution now appear immediately in the pyodide files list without
      requiring a browser tab refresh. [Commit](https://github.com/open-webui/open-webui/commit/5c4062c64841974bf193ff321d92d10f28a09746)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: ✏️ **Rich text paste sanitization.** Copying and pasting text with HTML
      characters (like `<` or `>`) no longer corrupts the editor content, as the paste
      handler now properly escapes HTML entities before processing mentions and special
      syntax. [Commit](https://github.com/open-webui/open-webui/commit/94f877ff328d410339308ad2c566c9afcdf43014)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 4-editor-experience-changes-in-v0-8-11
  source_release: open-webui-2026-03-25-v0-8-11-github-301478856-55ceba69
  source_type: github_releases
  theme: editor-experience
  title: 4 Editor Experience changes in v0.8.11
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-03-20-elicitation-form-shows-shift-tab-hint-for-navigating-between-fields-in-reverse|Elicitation
  form shows Shift+Tab hint for navigating between fields in reverse]]'
- '[[Changes/Claude Code/2026-03-25-3-editor-experience-changes-in-v2-1-83|3 Editor
  Experience changes in v2.1.83]]'
- '[[Changes/Ollama/2026-03-25-microsoft-visual-studio-code-now-directly-integrates-with-ollama-via-github-copi|Microsoft
  Visual Studio Code now directly integrates with Ollama via GitHub Copilot]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-03-25-v0-8-11-github-301478856-55ceba69|open-webui-2026-03-25-v0-8-11-github-301478856-55ceba69]]'
source_type: github_releases
theme: editor-experience
title: 4 Editor Experience changes in v0.8.11
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Editor Experience changes in v0.8.11

**Open WebUI** · 2026-03-25 · [[Themes/editor-experience|Editor Experience]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.11) · from [[Releases/Open WebUI/open-webui-2026-03-25-v0-8-11-github-301478856-55ceba69|v0.8.11]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📌 **Knowledge file previews.** Knowledge base files can now be opened in a new tab directly from the file list, making it easier to view content without downloading. [#22629](https://github.com/open-webui/open-webui/pull/22629)

> ✏️ **Markdown file editing.** Users can now edit and save Markdown files directly in the file navigator, with empty files automatically switching to editor mode for immediate editing. [Commit](https://github.com/open-webui/open-webui/commit/47e47e42af682e7f75c8359999f7cdf969bf903e)

> 🖥️ **Pyodide file list refresh.** Files created or modified during manual code execution now appear immediately in the pyodide files list without requiring a browser tab refresh. [Commit](https://github.com/open-webui/open-webui/commit/5c4062c64841974bf193ff321d92d10f28a09746)

> ✏️ **Rich text paste sanitization.** Copying and pasting text with HTML characters (like `<` or `>`) no longer corrupts the editor content, as the paste handler now properly escapes HTML entities before processing mentions and special syntax. [Commit](https://github.com/open-webui/open-webui/commit/94f877ff328d410339308ad2c566c9afcdf43014)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-03-25-rag-query-generation-robustness-the-rag-query-generation-web-search-and-image-ge|🔍 RAG query generation robustness. The RAG query generation, web search…]] · Image Generation
- [[Changes/Open WebUI/2026-03-25-shared-chat-viewing-crash-shared-chats-can-now-be-viewed-by-unauthenticated-user|🐛 Shared chat viewing crash. Shared chats can now be viewed by unauthenticated…]] · Collaboration
- [[Changes/Open WebUI/2026-03-25-11-account-and-access-changes-in-v0-8-11|11 Account and Access changes in v0.8.11]] · Account and Access
- [[Changes/Open WebUI/2026-03-25-3-context-window-changes-in-v0-8-11|3 Context Window changes in v0.8.11]] · Context Window
- [[Changes/Open WebUI/2026-03-25-2-search-and-browsing-changes-in-v0-8-11|2 Search and Browsing changes in v0.8.11]] · Search and Browsing
- [[Changes/Open WebUI/2026-03-25-2-files-and-data-changes-in-v0-8-11|2 Files and Data changes in v0.8.11]] · Files and Data
- [[Changes/Open WebUI/2026-03-25-4-memory-and-personalization-changes-in-v0-8-11|4 Memory and Personalization changes in v0.8.11]] · Memory and Personalization
- [[Changes/Open WebUI/2026-03-25-3-apps-and-integrations-changes-in-v0-8-11|3 Apps and Integrations changes in v0.8.11]] · Apps and Integrations
- [[Changes/Open WebUI/2026-03-25-17-interface-experience-changes-in-v0-8-11|17 Interface Experience changes in v0.8.11]] · Interface Experience
- [[Changes/Open WebUI/2026-03-25-5-reliability-and-performance-changes-in-v0-8-11|5 Reliability and Performance changes in v0.8.11]] · Reliability and Performance
- [[Changes/Open WebUI/2026-03-25-tool-binary-response-handling-tool-servers-can-now-return-binary-data-such-as-im|🏮 Tool binary response handling. Tool servers can now return binary data such…]] · Multimodal Input
- [[Changes/Open WebUI/2026-03-25-23-model-support-changes-in-v0-8-11|23 Model Support changes in v0.8.11]] · Model Support
- [[Changes/Open WebUI/2026-03-25-4-safety-and-privacy-changes-in-v0-8-11|4 Safety and Privacy changes in v0.8.11]] · Safety and Privacy
- [[Changes/Open WebUI/2026-03-25-34-developer-workflow-changes-in-v0-8-11|34 Developer Workflow changes in v0.8.11]] · Developer Workflow
- [[Changes/Open WebUI/2026-03-25-metrics-export-interval-configuration-administrators-can-now-control-opentelemet|📊 Metrics export interval configuration. Administrators can now control…]] · Pricing Model
- [[Changes/Open WebUI/2026-03-25-19-other-changes-in-v0-8-11|19 other changes in v0.8.11]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Editor Experience

- Earlier: 2026-03-25 · Ollama · [[Changes/Ollama/2026-03-25-microsoft-visual-studio-code-now-directly-integrates-with-ollama-via-github-copi|Microsoft Visual Studio Code now directly integrates with Ollama via GitHub Copilot]]
- Later: 2026-03-26 · Codex CLI · [[Changes/Codex CLI/2026-03-26-15480-use-shift-left-to-edit-queued-messages-in-tmux-charley-oai|♯15480 Use Shift+Left to edit queued messages in tmux @charley-oai]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-14 · Cursor · [[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3 Editor Experience changes in 0.0.37]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-03-25-109a7b&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-03-25-4-editor-experience-changes-in-v0-8-11.md%0ACard%20ID%3A%20open-webui-2026-03-25-109a7b%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.11%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->