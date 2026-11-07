---
card_id: open-webui-2026-01-09-529d7d
date: '2026-01-09'
description: "Open WebUI · 2026-01-09 · Context Window: 3 changes in v0.7.0 — \U0001F9E0
  Users can now ask the model to find relevant context from their notes, past chats,
  and…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2
    Context Window changes in 0.2.9]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 981
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f40f1f8d94e3516c96f614dd2c89f985d63fefe982d718fc6191a00f883f3927
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-01-09-529d7d
  comparison: ''
  date: '2026-01-09'
  description: 'Open WebUI — v0.7.0: 3 Context Window changes'
  evidence:
  - quote: "\U0001F9E0 Users can now ask the model to find relevant context from their
      notes, past chats, and channel messages—for example, \"what did I discuss about
      project X last week?\" or \"find the conversation where I brainstormed ideas
      for Y.\" [Commit](https://github.com/open-webui/open-webui/commit/646835d76744ad9b2e67ede0407a61d62e969aab)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F4A8 Administrators can now enable KV prefix caching optimization
      by setting \"RAG_SYSTEM_CONTEXT\" to true, which injects RAG context into the
      system message instead of user messages, enabling models to reuse cached tokens
      for follow-up questions instead of reprocessing the entire context on each turn,
      significantly improving response times and reducing costs for cloud-based models.
      [#20301](https://github.com/open-webui/open-webui/discussions/20301), [#20317](https://github.com/open-webui/open-webui/pull/20317)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F4C4 In the model editor users can now disable the \"File Context\"
      capability to skip automatic file content extraction and injection, forwarding
      raw messages with file attachment metadata instead for use with custom tools
      or future built-in file access tools. [Commit](https://github.com/open-webui/open-webui/commit/daccf0713e3ecd6d24f003a87b5f8b3c61852958),
      [Docs:Commit](https://github.com/open-webui/docs/commit/18ec6eaefc071a278ec57d4d1b8d66d686af0870)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 3-context-window-changes-in-v0-7-0
  source_release: open-webui-2026-01-09-v0-7-0-github-275585328-a4da522c
  source_type: github_releases
  theme: context-window
  title: 3 Context Window changes in v0.7.0
  type: change
related_changes:
- '[[Changes/OpenCode/2026-01-04-2-context-window-changes-in-v1-1-1|2 Context Window
  changes in v1.1.1]]'
- '[[Changes/Codex CLI/2026-01-06-2-context-window-changes-in-rust-v0-78-0|2 Context
  Window changes in rust-v0.78.0]]'
- '[[Changes/Gemini CLI/2026-01-07-add-core-tool-that-adds-all-context-from-the-core-package-by-jacob314-in-https-g|Add
  core tool that adds all context from the core package]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-01-09-v0-7-0-github-275585328-a4da522c|open-webui-2026-01-09-v0-7-0-github-275585328-a4da522c]]'
source_type: github_releases
theme: context-window
title: 3 Context Window changes in v0.7.0
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Context Window changes in v0.7.0

**Open WebUI** · 2026-01-09 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.7.0) · from [[Releases/Open WebUI/open-webui-2026-01-09-v0-7-0-github-275585328-a4da522c|v0.7.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🧠 Users can now ask the model to find relevant context from their notes, past chats, and channel messages—for example, "what did I discuss about project X last week?" or "find the conversation where I brainstormed ideas for Y." [Commit](https://github.com/open-webui/open-webui/commit/646835d76744ad9b2e67ede0407a61d62e969aab)

> 💨 Administrators can now enable KV prefix caching optimization by setting "RAG_SYSTEM_CONTEXT" to true, which injects RAG context into the system message instead of user messages, enabling models to reuse cached tokens for follow-up questions instead of reprocessing the entire context on each turn, significantly improving response times and reducing costs for cloud-based models. [#20301](https://github.com/open-webui/open-webui/discussions/20301), [#20317](https://github.com/open-webui/open-webui/pull/20317)

> 📄 In the model editor users can now disable the "File Context" capability to skip automatic file content extraction and injection, forwarding raw messages with file attachment metadata instead for use with custom tools or future built-in file access tools. [Commit](https://github.com/open-webui/open-webui/commit/daccf0713e3ecd6d24f003a87b5f8b3c61852958), [Docs:Commit](https://github.com/open-webui/docs/commit/18ec6eaefc071a278ec57d4d1b8d66d686af0870)

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
- [[Changes/Open WebUI/2026-01-09-9-reliability-and-performance-changes-in-v0-7-0|9 Reliability and Performance changes in v0.7.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-01-09-6-safety-and-privacy-changes-in-v0-7-0|6 Safety and Privacy changes in v0.7.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-01-09-3-account-and-access-changes-in-v0-7-0|3 Account and Access changes in v0.7.0]] · Account and Access
- [[Changes/Open WebUI/2026-01-09-4-image-generation-changes-in-v0-7-0|4 Image Generation changes in v0.7.0]] · Image Generation
- [[Changes/Open WebUI/2026-01-09-5-interface-experience-changes-in-v0-7-0|5 Interface Experience changes in v0.7.0]] · Interface Experience
- [[Changes/Open WebUI/2026-01-09-11-model-support-changes-in-v0-7-0|11 Model Support changes in v0.7.0]] · Model Support
- [[Changes/Open WebUI/2026-01-09-24-developer-workflow-changes-in-v0-7-0|24 Developer Workflow changes in v0.7.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-01-09-3-voice-and-audio-changes-in-v0-7-0|3 Voice and Audio changes in v0.7.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-01-09-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-01-09-26-other-changes-in-v0-7-0|26 other changes in v0.7.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-01-07 · Gemini CLI · [[Changes/Gemini CLI/2026-01-07-add-core-tool-that-adds-all-context-from-the-core-package-by-jacob314-in-https-g|Add core tool that adds all context from the core package]]
- Later: 2026-01-09 · OpenCode · [[Changes/OpenCode/2026-01-09-desktop-cache-session-scoped-stores-and-add-optional-context-gating|Desktop Cache session-scoped stores and add optional context gating]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-04 · Cursor · [[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2 Context Window changes in 0.2.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-01-09-529d7d&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-01-09-3-context-window-changes-in-v0-7-0.md%0ACard%20ID%3A%20open-webui-2026-01-09-529d7d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.7.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->