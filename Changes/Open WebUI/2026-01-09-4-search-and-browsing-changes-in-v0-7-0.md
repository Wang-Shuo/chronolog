---
card_id: open-webui-2026-01-09-2d2dbb
date: '2026-01-09'
description: "Open WebUI · 2026-01-09 · Search and Browsing: 4 changes in v0.7.0 —
  \U0001F50D When models invoke web search, search results appear as clickable citations
  in real-time…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-05-28-added-ability-to-batch-delete-ignore-search-results|Added
    ability to batch delete/ignore search results]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2052
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: search-browsing
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 3d1ec017223eea48ef0bdd22f720df0a2db489c11ca2f2593d7533bba1a0ad49
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-01-09-2d2dbb
  comparison: ''
  date: '2026-01-09'
  description: 'Open WebUI — v0.7.0: 4 Search and Browsing changes'
  evidence:
  - quote: "\U0001F50D When models invoke web search, search results appear as clickable
      citations in real-time for full source verification. [Commit](https://github.com/open-webui/open-webui/commit/2789f6a24d8405c30cd48ae460071f6a4f2c35f9)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F310 Users with OpenAI-compatible models that have web search capabilities
      now see URL citations displayed as sources in the interface. [#20172](https://github.com/open-webui/open-webui/pull/20172),
      [Commit](https://github.com/open-webui/open-webui/commit/fe84afd09a2bc8a89311f30186ec2608a4edda3a)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F9ED Administrators can now configure custom Jina Search API endpoints
      using the \"JINA_API_BASE_URL\" environment variable, enabling region-specific
      deployments such as EU data processing. [#19718](https://github.com/open-webui/open-webui/pull/19718),
      [Commit](https://github.com/open-webui/open-webui/commit/f7f8a263b92289df8d4f8dbc3bae09bd009a5699)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F6A6 Users with Brave Search now experience automatic retry with
      a 1-second delay when hitting rate limits, preventing failures when sequential
      requests exceed the 1 request per second limit, though this only works reliably
      when web search concurrency is set to a maximum of 1. [#15134](https://github.com/open-webui/open-webui/issues/15134),
      [#20255](https://github.com/open-webui/open-webui/pull/20255)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 4-search-and-browsing-changes-in-v0-7-0
  source_release: open-webui-2026-01-09-v0-7-0-github-275585328-a4da522c
  source_type: github_releases
  theme: search-browsing
  title: 4 Search and Browsing changes in v0.7.0
  type: change
related_changes:
- '[[Changes/Open WebUI/2025-12-21-3-search-and-browsing-changes-in-v0-6-42|3 Search
  and Browsing changes in v0.6.42]]'
- '[[Changes/Codex CLI/2026-01-07-4-search-and-browsing-changes-in-rust-v0-79-0|4
  Search and Browsing changes in rust-v0.79.0]]'
- '[[Changes/v0/2026-01-08-improved-the-speed-and-token-use-of-the-web-search-tool|Improved
  the speed and token use of the Web Search tool]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-01-09-v0-7-0-github-275585328-a4da522c|open-webui-2026-01-09-v0-7-0-github-275585328-a4da522c]]'
source_type: github_releases
theme: search-browsing
title: 4 Search and Browsing changes in v0.7.0
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Search and Browsing changes in v0.7.0

**Open WebUI** · 2026-01-09 · [[Themes/search-browsing|Search and Browsing]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.7.0) · from [[Releases/Open WebUI/open-webui-2026-01-09-v0-7-0-github-275585328-a4da522c|v0.7.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔍 When models invoke web search, search results appear as clickable citations in real-time for full source verification. [Commit](https://github.com/open-webui/open-webui/commit/2789f6a24d8405c30cd48ae460071f6a4f2c35f9)

> 🌐 Users with OpenAI-compatible models that have web search capabilities now see URL citations displayed as sources in the interface. [#20172](https://github.com/open-webui/open-webui/pull/20172), [Commit](https://github.com/open-webui/open-webui/commit/fe84afd09a2bc8a89311f30186ec2608a4edda3a)

> 🧭 Administrators can now configure custom Jina Search API endpoints using the "JINA_API_BASE_URL" environment variable, enabling region-specific deployments such as EU data processing. [#19718](https://github.com/open-webui/open-webui/pull/19718), [Commit](https://github.com/open-webui/open-webui/commit/f7f8a263b92289df8d4f8dbc3bae09bd009a5699)

> 🚦 Users with Brave Search now experience automatic retry with a 1-second delay when hitting rate limits, preventing failures when sequential requests exceed the 1 request per second limit, though this only works reliably when web search concurrency is set to a maximum of 1. [#15134](https://github.com/open-webui/open-webui/issues/15134), [#20255](https://github.com/open-webui/open-webui/pull/20255)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-01-09-3-editor-experience-changes-in-v0-7-0|3 Editor Experience changes in v0.7.0]] · Editor Experience
- [[Changes/Open WebUI/2026-01-09-users-on-windows-now-see-correctly-preserved-line-breaks-when-using-the-clipboar|📋 Users on Windows now see correctly preserved line breaks when using…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-01-09-2-memory-and-personalization-changes-in-v0-7-0|2 Memory and Personalization changes in v0.7.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-01-09-3-apps-and-integrations-changes-in-v0-7-0|3 Apps and Integrations changes in v0.7.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-01-09-5-files-and-data-changes-in-v0-7-0|5 Files and Data changes in v0.7.0]] · Files and Data
- [[Changes/Open WebUI/2026-01-09-3-context-window-changes-in-v0-7-0|3 Context Window changes in v0.7.0]] · Context Window
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
## Nearby in Search and Browsing

- Earlier: 2026-01-08 · v0 · [[Changes/v0/2026-01-08-improved-the-speed-and-token-use-of-the-web-search-tool|Improved the speed and token use of the Web Search tool]]
- Later: 2026-01-16 · Codex CLI · [[Changes/Codex CLI/2026-01-16-2-search-and-browsing-changes-in-rust-v0-86-0|2 Search and Browsing changes in rust-v0.86.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-05-28 · Descript · [[Changes/Descript/2020-05-28-added-ability-to-batch-delete-ignore-search-results|Added ability to batch delete/ignore search results]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-01-09-2d2dbb&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-01-09-4-search-and-browsing-changes-in-v0-7-0.md%0ACard%20ID%3A%20open-webui-2026-01-09-2d2dbb%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.7.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->