---
card_id: open-webui-2026-05-09-65c3d6
date: '2026-05-09'
description: "Open WebUI · 2026-05-09 · Apps and Integrations: 3 changes in v0.9.3
  — \U0001F6A6 **MCP cleanup response reliability.** Successful native MCP tool calls
  no longer get…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1143
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 5026ddd7446e5491599a3e1848843953f85ea8ded75945d67d21c691d8e23eff
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-05-09-65c3d6
  comparison: ''
  date: '2026-05-09'
  description: 'Open WebUI — v0.9.3: 3 Apps and Integrations changes'
  evidence:
  - quote: "\U0001F6A6 **MCP cleanup response reliability.** Successful native MCP
      tool calls no longer get replaced by a 500 \"No response returned\" error during
      cleanup, so valid chat responses are now returned consistently. [#24105](https://github.com/open-webui/open-webui/pull/24105)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F6E0️ **OpenAPI tool spec compatibility.** OpenAPI tool integrations
      now handle null or non-operation path entries more safely and parse path-level
      parameters consistently, preventing crashes and improving tool execution reliability
      across imperfect OpenAPI specs. [Commit](https://github.com/open-webui/open-webui/commit/2ba6b423aa0c9c800bd96cb638c6ade867cac0f6),
      [Commit](https://github.com/open-webui/open-webui/commit/5b80932e5951786bb348b91589e8d87753f18905),
      [#24376](https://github.com/open-webui/open-webui/pull/24376)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F6AA **Signout request method.** The signout endpoint now requires
      POST instead of GET, so custom clients and integrations must update logout calls
      accordingly. [#24420](https://github.com/open-webui/open-webui/pull/24420)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 3-apps-and-integrations-changes-in-v0-9-3
  source_release: open-webui-2026-05-09-v0-9-3-github-319872270-bb8aabca
  source_type: github_releases
  theme: apps-integrations
  title: 3 Apps and Integrations changes in v0.9.3
  type: change
related_changes:
- '[[Changes/Claude Code/2026-05-08-changed-plugin-marketplace-removal-key-to-d-matching-delete-elsewhere-instead-of|Changed
  plugin marketplace removal key to d (matching delete elsewhere) instead…]]'
- '[[Changes/Codex CLI/2026-05-08-8-apps-and-integrations-changes-in-rust-v0-130-0|8
  Apps and Integrations changes in rust-v0.130.0]]'
- '[[Changes/Replit/2026-05-08-speaker-notes-and-presenter-view-in-slide-decks|Speaker
  notes and Presenter view in Slide Decks]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-05-09-v0-9-3-github-319872270-bb8aabca|open-webui-2026-05-09-v0-9-3-github-319872270-bb8aabca]]'
source_type: github_releases
theme: apps-integrations
title: 3 Apps and Integrations changes in v0.9.3
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Apps and Integrations changes in v0.9.3

**Open WebUI** · 2026-05-09 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.3) · from [[Releases/Open WebUI/open-webui-2026-05-09-v0-9-3-github-319872270-bb8aabca|v0.9.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🚦 **MCP cleanup response reliability.** Successful native MCP tool calls no longer get replaced by a 500 "No response returned" error during cleanup, so valid chat responses are now returned consistently. [#24105](https://github.com/open-webui/open-webui/pull/24105)

> 🛠️ **OpenAPI tool spec compatibility.** OpenAPI tool integrations now handle null or non-operation path entries more safely and parse path-level parameters consistently, preventing crashes and improving tool execution reliability across imperfect OpenAPI specs. [Commit](https://github.com/open-webui/open-webui/commit/2ba6b423aa0c9c800bd96cb638c6ade867cac0f6), [Commit](https://github.com/open-webui/open-webui/commit/5b80932e5951786bb348b91589e8d87753f18905), [#24376](https://github.com/open-webui/open-webui/pull/24376)

> 🚪 **Signout request method.** The signout endpoint now requires POST instead of GET, so custom clients and integrations must update logout calls accordingly. [#24420](https://github.com/open-webui/open-webui/pull/24420)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-05-09-5-search-and-browsing-changes-in-v0-9-3|5 Search and Browsing changes in v0.9.3]] · Search and Browsing
- [[Changes/Open WebUI/2026-05-09-10-voice-and-audio-changes-in-v0-9-3|10 Voice and Audio changes in v0.9.3]] · Voice and Audio
- [[Changes/Open WebUI/2026-05-09-5-editor-experience-changes-in-v0-9-3|5 Editor Experience changes in v0.9.3]] · Editor Experience
- [[Changes/Open WebUI/2026-05-09-8-interface-experience-changes-in-v0-9-3|8 Interface Experience changes in v0.9.3]] · Interface Experience
- [[Changes/Open WebUI/2026-05-09-4-context-window-changes-in-v0-9-3|4 Context Window changes in v0.9.3]] · Context Window
- [[Changes/Open WebUI/2026-05-09-2-automation-and-scheduling-changes-in-v0-9-3|2 Automation and Scheduling changes in v0.9.3]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-05-09-22-developer-workflow-changes-in-v0-9-3|22 Developer Workflow changes in v0.9.3]] · Developer Workflow
- [[Changes/Open WebUI/2026-05-09-4-reliability-and-performance-changes-in-v0-9-3|4 Reliability and Performance changes in v0.9.3]] · Reliability and Performance
- [[Changes/Open WebUI/2026-05-09-4-account-and-access-changes-in-v0-9-3|4 Account and Access changes in v0.9.3]] · Account and Access
- [[Changes/Open WebUI/2026-05-09-sanitized-spreadsheet-html-previews-spreadsheet-previews-now-sanitize-generated|🛡️ Sanitized spreadsheet HTML previews. Spreadsheet previews now sanitize…]] · Files and Data
- [[Changes/Open WebUI/2026-05-09-9-model-support-changes-in-v0-9-3|9 Model Support changes in v0.9.3]] · Model Support
- [[Changes/Open WebUI/2026-05-09-3-safety-and-privacy-changes-in-v0-9-3|3 Safety and Privacy changes in v0.9.3]] · Safety and Privacy
- [[Changes/Open WebUI/2026-05-09-faster-memory-query-performance-per-user-memory-lookups-and-deletions-now-run-mu|⚡ Faster memory query performance. Per-user memory lookups and deletions now run…]] · Memory and Personalization
- [[Changes/Open WebUI/2026-05-09-5-other-changes-in-v0-9-3|5 other changes in v0.9.3]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-05-08 · Replit · [[Changes/Replit/2026-05-08-speaker-notes-and-presenter-view-in-slide-decks|Speaker notes and Presenter view in Slide Decks]]
- Later: 2026-05-11 · Claude Code · [[Changes/Claude Code/2026-05-11-added-goal-command-set-a-completion-condition-and-claude-keeps-working-across-tu|Added /goal command]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-05-09-65c3d6&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-05-09-3-apps-and-integrations-changes-in-v0-9-3.md%0ACard%20ID%3A%20open-webui-2026-05-09-65c3d6%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.3%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->