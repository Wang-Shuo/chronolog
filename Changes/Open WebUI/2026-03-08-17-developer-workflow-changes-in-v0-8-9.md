---
card_id: open-webui-2026-03-08-4f455c
date: '2026-03-08'
description: 'Open WebUI · 2026-03-08 · Developer Workflow: 17 changes in v0.8.9 —
  ▶️ **Open Terminal notebook cell execution.** Users can now run Jupyter Notebook
  code…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2735
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2d329ec281dced2ad0dbe1979b02c6a8cb9b937bc1791cfd8f265eb74a075203
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-03-08-4f455c
  comparison: ''
  date: '2026-03-08'
  description: 'Open WebUI — v0.8.9: 17 Developer Workflow changes'
  evidence:
  - quote: ▶️ **Open Terminal notebook cell execution.** Users can now run Jupyter
      Notebook code cells directly in the Open Terminal file navigator, execute entire
      notebooks with a single click, edit and modify cells before running, and control
      the kernel - bringing full interactive notebook execution to the browser. [Commit](https://github.com/open-webui/open-webui/commit/4b3ed3e802d6f2ec8ee7caf358af810b7d09f789)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.9
  - quote: "\U0001F4C9 **Open Terminal Mermaid diagram rendering.** Markdown files
      with Mermaid code blocks are now rendered as diagrams directly in the Open Terminal
      file navigator, making it easier to visualize flowcharts and other diagrams.
      [Commit](https://github.com/open-webui/open-webui/commit/aaa49bdd6d6e5c10e8be554039d3cac673008fc2)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.9
  - quote: "\U0001F4D3 **Open Terminal Jupyter Notebook previews.** Users can now
      preview Jupyter Notebook files directly in the Open Terminal file navigator,
      making it easier to view notebook content without downloading them first. [Commit](https://github.com/open-webui/open-webui/commit/b081e33c0a37585a1ee60b6e0e1ea03457f1e5f4)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.9
  - quote: "\U0001F503 **Open Terminal auto-refresh.** The Open Terminal file navigator
      now automatically refreshes when the model writes or modifies files, keeping
      the view in sync without manual refresh. [Commit](https://github.com/open-webui/open-webui/commit/828656b35f04bf486609183799cf8aa2e9850a76)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.9
  - quote: "\U0001F4CE **Open Terminal file copy button.** Users can now copy file
      contents directly to clipboard in the Open Terminal file navigator with a single
      click, making it easier to quickly grab file content without downloading. [Commit](https://github.com/open-webui/open-webui/commit/f5ea1ce250cb02fbc583c6cb3f52a923912d0178)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.9
  - quote: "\U0001F333 **Open Terminal JSON tree view.** JSON, JSONC, JSONL, and JSON5
      files now display as interactive collapsible tree views in the Open Terminal
      file navigator, and SVG files render as preview images with syntax highlighting
      support. [Commit](https://github.com/open-webui/open-webui/commit/f4c38e6001dd9d4853ed923e0bc5e790c4fd9941)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.9
  - quote: "\U0001F6DC **Open Terminal port viewing.** Users can now view listening
      ports in the Open Terminal file navigator and open proxy connections to them
      directly from the UI. [Commit](https://github.com/open-webui/open-webui/commit/e08341dab3bb10e26a64eb44cbebd2d507087b03)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.9
  - quote: "\U0001F4C4 **Open Terminal DOCX preview.** Word documents generated or
      modified by the AI can now be viewed directly in the file navigator with formatted
      text, tables, and images rendered inline — no need to download and open in a
      separate application. [Commit](https://github.com/open-webui/open-webui/commit/890949abe6b01d201355a86c50317e20da07dd34)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.9
  - quote: "\U0001F4CA **Open Terminal XLSX preview.** Excel spreadsheets in the file
      navigator now render as interactive tables with column headers and row numbers,
      making it easy to verify data the AI has generated or processed. [Commit](https://github.com/open-webui/open-webui/commit/890949abe6b01d201355a86c50317e20da07dd34)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.9
  - quote: "\U0001F4FD️ **Open Terminal PPTX preview.** PowerPoint presentations created
      by the AI can now be viewed slide-by-slide directly in the file navigator, enabling
      quick review and iteration without leaving the browser. [Commit](https://github.com/open-webui/open-webui/commit/890949abe6b01d201355a86c50317e20da07dd34)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.9
  - quote: "\U0001F501 **File refresh button visibility.** The refresh button in the
      chat file navigator now appears when viewing files as well as directories, allowing
      users to refresh the file view at any time. [Commit](https://github.com/open-webui/open-webui/commit/49a2e5bf573415dae6d4c7e5bd635e499c8de77a)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.9
  - quote: "\U0001F6D1 **Stop sequence error.** Fixed a bug where setting stop sequences
      on a model caused the chat to fail with a split error, preventing any responses
      from being returned. The fix handles both string and array formats for stop
      tokens. [#22251](https://github.com/open-webui/open-webui/issues/22251), [Commit](https://github.com/open-webui/open-webui/commit/c7d1d1e390a79c6c86d4bfe439fd7de6f5fb060f)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.9
  - quote: "\U0001F4F6 **Terminal keepalive.** Terminal connections now stay active
      without being closed by idle timeouts from proxies or load balancers, and spurious
      disconnection messages no longer appear. [Commit](https://github.com/open-webui/open-webui/commit/ca2aaf0321c219d041e92e2c0c842a4e424732ef)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.9
  - quote: ⌨️ **Inline code typing.** Fixed a bug where typing inline code with backticks
      incorrectly deleted the character immediately before the opening backtick, so
      text formatted as inline code now correctly produces the full word instead of
      missing the last character. [#20417](https://github.com/open-webui/open-webui/issues/20417),
      [Commit](https://github.com/open-webui/open-webui/commit/e303c3da3b174da9e92a79b174f85ba574ca06ef)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.9
  - quote: "\U0001F4DD **Variable input newlines.** Fixed a bug where variables containing
      newlines were not displayed correctly in chat messages, and input values from
      Windows systems are now properly normalized to use standard line endings. [#21447](https://github.com/open-webui/open-webui/issues/21447),
      [Commit](https://github.com/open-webui/open-webui/commit/7b2f597b30c77ef300d1966e1c6a3edfdb0c465d)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.9
  - quote: "\U0001FA9F **Open Terminal Windows path fix.** Fixed a bug where navigating
      back to parent directories on Windows added an incorrect leading slash, causing
      directory loads to fail. Paths are now properly normalized for Windows drive
      letters. [#22352](https://github.com/open-webui/open-webui/issues/22352), [Commit](https://github.com/open-webui/open-webui/commit/044fd1bd15cae06a5c56a321ca79d8362942f66a)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.9
  - quote: "\U0001F4C2 **Folder knowledge base native tool call fix.** Fixed a bug
      where folders with attached knowledge bases were querying the knowledge base
      twice when using native tool call mode. The fix now correctly separates knowledge
      files from regular attachments, letting the builtin query_knowledge_files tool
      handle knowledge searches instead of duplicating RAG queries. [#22236](https://github.com/open-webui/open-webui/issues/22236),
      [Commit](https://github.com/open-webui/open-webui/commit/967b1137dcb7a52615f17d086ee89095bb9b60f3),
      [Commit](https://github.com/open-webui/open-webui/commit/80b5896b70d07ea868e2010b187430d43c9808f0)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.9
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 17-developer-workflow-changes-in-v0-8-9
  source_release: open-webui-2026-03-08-v0-8-9-github-294335564-7bdc11cb
  source_type: github_releases
  theme: developer-workflow
  title: 17 Developer Workflow changes in v0.8.9
  type: change
related_changes:
- '[[Changes/OpenCode/2026-03-06-3-developer-workflow-changes-in-v1-2-20-1|3 Developer
  Workflow changes in v1.2.20 + 1]]'
- '[[Changes/Claude Code/2026-03-07-2-developer-workflow-changes-in-v2-1-71|2 Developer
  Workflow changes in v2.1.71]]'
- '[[Changes/OpenCode/2026-03-07-2-developer-workflow-changes-in-v1-2-21|2 Developer
  Workflow changes in v1.2.21]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-03-08-v0-8-9-github-294335564-7bdc11cb|open-webui-2026-03-08-v0-8-9-github-294335564-7bdc11cb]]'
source_type: github_releases
theme: developer-workflow
title: 17 Developer Workflow changes in v0.8.9
type: change
---

<!-- chronolog:begin region="header" -->
# 17 Developer Workflow changes in v0.8.9

**Open WebUI** · 2026-03-08 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.9) · from [[Releases/Open WebUI/open-webui-2026-03-08-v0-8-9-github-294335564-7bdc11cb|v0.8.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> ▶️ **Open Terminal notebook cell execution.** Users can now run Jupyter Notebook code cells directly in the Open Terminal file navigator, execute entire notebooks with a single click, edit and modify cells before running, and control the kernel - bringing full interactive notebook execution to the browser. [Commit](https://github.com/open-webui/open-webui/commit/4b3ed3e802d6f2ec8ee7caf358af810b7d09f789)

> 📉 **Open Terminal Mermaid diagram rendering.** Markdown files with Mermaid code blocks are now rendered as diagrams directly in the Open Terminal file navigator, making it easier to visualize flowcharts and other diagrams. [Commit](https://github.com/open-webui/open-webui/commit/aaa49bdd6d6e5c10e8be554039d3cac673008fc2)

> 📓 **Open Terminal Jupyter Notebook previews.** Users can now preview Jupyter Notebook files directly in the Open Terminal file navigator, making it easier to view notebook content without downloading them first. [Commit](https://github.com/open-webui/open-webui/commit/b081e33c0a37585a1ee60b6e0e1ea03457f1e5f4)

> 🔃 **Open Terminal auto-refresh.** The Open Terminal file navigator now automatically refreshes when the model writes or modifies files, keeping the view in sync without manual refresh. [Commit](https://github.com/open-webui/open-webui/commit/828656b35f04bf486609183799cf8aa2e9850a76)

> 📎 **Open Terminal file copy button.** Users can now copy file contents directly to clipboard in the Open Terminal file navigator with a single click, making it easier to quickly grab file content without downloading. [Commit](https://github.com/open-webui/open-webui/commit/f5ea1ce250cb02fbc583c6cb3f52a923912d0178)

> 🌳 **Open Terminal JSON tree view.** JSON, JSONC, JSONL, and JSON5 files now display as interactive collapsible tree views in the Open Terminal file navigator, and SVG files render as preview images with syntax highlighting support. [Commit](https://github.com/open-webui/open-webui/commit/f4c38e6001dd9d4853ed923e0bc5e790c4fd9941)

> 🛜 **Open Terminal port viewing.** Users can now view listening ports in the Open Terminal file navigator and open proxy connections to them directly from the UI. [Commit](https://github.com/open-webui/open-webui/commit/e08341dab3bb10e26a64eb44cbebd2d507087b03)

> 📄 **Open Terminal DOCX preview.** Word documents generated or modified by the AI can now be viewed directly in the file navigator with formatted text, tables, and images rendered inline — no need to download and open in a separate application. [Commit](https://github.com/open-webui/open-webui/commit/890949abe6b01d201355a86c50317e20da07dd34)

> 📊 **Open Terminal XLSX preview.** Excel spreadsheets in the file navigator now render as interactive tables with column headers and row numbers, making it easy to verify data the AI has generated or processed. [Commit](https://github.com/open-webui/open-webui/commit/890949abe6b01d201355a86c50317e20da07dd34)

> 📽️ **Open Terminal PPTX preview.** PowerPoint presentations created by the AI can now be viewed slide-by-slide directly in the file navigator, enabling quick review and iteration without leaving the browser. [Commit](https://github.com/open-webui/open-webui/commit/890949abe6b01d201355a86c50317e20da07dd34)

> 🔁 **File refresh button visibility.** The refresh button in the chat file navigator now appears when viewing files as well as directories, allowing users to refresh the file view at any time. [Commit](https://github.com/open-webui/open-webui/commit/49a2e5bf573415dae6d4c7e5bd635e499c8de77a)

> 🛑 **Stop sequence error.** Fixed a bug where setting stop sequences on a model caused the chat to fail with a split error, preventing any responses from being returned. The fix handles both string and array formats for stop tokens. [#22251](https://github.com/open-webui/open-webui/issues/22251), [Commit](https://github.com/open-webui/open-webui/commit/c7d1d1e390a79c6c86d4bfe439fd7de6f5fb060f)

> 📶 **Terminal keepalive.** Terminal connections now stay active without being closed by idle timeouts from proxies or load balancers, and spurious disconnection messages no longer appear. [Commit](https://github.com/open-webui/open-webui/commit/ca2aaf0321c219d041e92e2c0c842a4e424732ef)

> ⌨️ **Inline code typing.** Fixed a bug where typing inline code with backticks incorrectly deleted the character immediately before the opening backtick, so text formatted as inline code now correctly produces the full word instead of missing the last character. [#20417](https://github.com/open-webui/open-webui/issues/20417), [Commit](https://github.com/open-webui/open-webui/commit/e303c3da3b174da9e92a79b174f85ba574ca06ef)

> 📝 **Variable input newlines.** Fixed a bug where variables containing newlines were not displayed correctly in chat messages, and input values from Windows systems are now properly normalized to use standard line endings. [#21447](https://github.com/open-webui/open-webui/issues/21447), [Commit](https://github.com/open-webui/open-webui/commit/7b2f597b30c77ef300d1966e1c6a3edfdb0c465d)

> 🪟 **Open Terminal Windows path fix.** Fixed a bug where navigating back to parent directories on Windows added an incorrect leading slash, causing directory loads to fail. Paths are now properly normalized for Windows drive letters. [#22352](https://github.com/open-webui/open-webui/issues/22352), [Commit](https://github.com/open-webui/open-webui/commit/044fd1bd15cae06a5c56a321ca79d8362942f66a)

> 📂 **Folder knowledge base native tool call fix.** Fixed a bug where folders with attached knowledge bases were querying the knowledge base twice when using native tool call mode. The fix now correctly separates knowledge files from regular attachments, letting the builtin query_knowledge_files tool handle knowledge searches instead of duplicating RAG queries. [#22236](https://github.com/open-webui/open-webui/issues/22236), [Commit](https://github.com/open-webui/open-webui/commit/967b1137dcb7a52615f17d086ee89095bb9b60f3), [Commit](https://github.com/open-webui/open-webui/commit/80b5896b70d07ea868e2010b187430d43c9808f0)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.8.9
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-03-08-image-generation-in-temporary-chats-generated-images-now-display-correctly-in-te|🖌️ Image generation in temporary chats. Generated images now display correctly…]] · Image Generation
- [[Changes/Open WebUI/2026-03-08-2-context-window-changes-in-v0-8-9|2 Context Window changes in v0.8.9]] · Context Window
- [[Changes/Open WebUI/2026-03-08-microsoft-oauth-refresh-token-fix-fixed-a-bug-where-microsoft-oauth-refresh-toke|🔐 Microsoft OAuth refresh token fix. Fixed a bug where Microsoft OAuth refresh…]] · Account and Access
- [[Changes/Open WebUI/2026-03-08-5-interface-experience-changes-in-v0-8-9|5 Interface Experience changes in v0.8.9]] · Interface Experience
- [[Changes/Open WebUI/2026-03-08-2-voice-and-audio-changes-in-v0-8-9|2 Voice and Audio changes in v0.8.9]] · Voice and Audio
- [[Changes/Open WebUI/2026-03-08-android-photo-capture-fixed-an-issue-where-the-first-photo-taken-in-chat-appeare|📷 Android photo capture. Fixed an issue where the first photo taken in chat…]] · Files and Data
- [[Changes/Open WebUI/2026-03-08-2-search-and-browsing-changes-in-v0-8-9|2 Search and Browsing changes in v0.8.9]] · Search and Browsing
- [[Changes/Open WebUI/2026-03-08-open-terminal-html-editing-users-can-now-edit-html-source-files-in-open-terminal|✏️ Open Terminal HTML editing. Users can now edit HTML source files in Open…]] · Editor Experience
- [[Changes/Open WebUI/2026-03-08-system-metrics-via-opentelemetry-administrators-can-now-monitor-python-runtime-a|📡 System metrics via OpenTelemetry. Administrators can now monitor Python…]] · Memory and Personalization
- [[Changes/Open WebUI/2026-03-08-artifacts-reactive-loop-fix-fixed-an-infinite-reactive-loop-in-chat-when-artifac|♾️ Artifacts reactive loop fix. Fixed an infinite reactive loop in chat…]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-03-08-13-reliability-and-performance-changes-in-v0-8-9|13 Reliability and Performance changes in v0.8.9]] · Reliability and Performance
- [[Changes/Open WebUI/2026-03-08-9-model-support-changes-in-v0-8-9|9 Model Support changes in v0.8.9]] · Model Support
- [[Changes/Open WebUI/2026-03-08-open-terminal-permission-fix-open-terminal-is-now-visible-without-requiring-allo|🖥️ Open Terminal permission fix. Open Terminal is now visible without requiring…]] · Safety and Privacy
- [[Changes/Open WebUI/2026-03-08-14-other-changes-in-v0-8-9|14 other changes in v0.8.9]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-03-07 · OpenCode · [[Changes/OpenCode/2026-03-07-2-developer-workflow-changes-in-v1-2-21|2 Developer Workflow changes in v1.2.21]]
- Later: 2026-03-08 · OpenCode · [[Changes/OpenCode/2026-03-08-3-developer-workflow-changes-in-v1-2-22|3 Developer Workflow changes in v1.2.22]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-03-08-4f455c&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-03-08-17-developer-workflow-changes-in-v0-8-9.md%0ACard%20ID%3A%20open-webui-2026-03-08-4f455c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.9%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->