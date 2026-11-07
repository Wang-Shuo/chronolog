---
card_id: open-webui-2025-12-21-c659f5
date: '2025-12-21'
description: "Open WebUI · 2025-12-21 · Search and Browsing: 3 changes in v0.6.42
  — \U0001F5C4️ PostgreSQL null byte insertion failures when attaching web pages or
  processing…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-05-28-added-ability-to-batch-delete-ignore-search-results|Added
    ability to batch delete/ignore search results]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2033
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: search-browsing
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 906a4cde3988d3815231a13e7030c7d87bdfb1dedca78d37fc610454bf285b80
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-12-21-c659f5
  comparison: ''
  date: '2025-12-21'
  description: 'Open WebUI — v0.6.42: 3 Search and Browsing changes'
  evidence:
  - quote: "\U0001F5C4️ PostgreSQL null byte insertion failures when attaching web
      pages or processing embedded content are now prevented by consolidating text
      sanitization logic across chat messages, web search results, and knowledge base
      documents, removing null bytes and invalid UTF-8 surrogates before database
      insertion. [#20072](https://github.com/open-webui/open-webui/pull/20072), [#19867](https://github.com/open-webui/open-webui/issues/19867),
      [#18201](https://github.com/open-webui/open-webui/issues/18201), [#15616](https://github.com/open-webui/open-webui/issues/15616)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F310 Ollama Cloud web search now correctly applies domain filtering
      to search results. [Commit](https://github.com/open-webui/open-webui/commit/d4bd938a77c22409a1643c058b937a06e07baca9)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F4E1 WEB_SEARCH_CONCURRENT_REQUESTS default changed from 10 to 0
      (unlimited) — This setting now applies to all search engines instead of only
      DuckDuckGo; previously users were implicitly limited to 10 concurrent queries,
      but now have unlimited parallel requests by default; set to 1 for sequential
      execution if using rate-limited APIs like Brave free tier. [#20070](https://github.com/open-webui/open-webui/pull/20070)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 3-search-and-browsing-changes-in-v0-6-42
  source_release: open-webui-2025-12-21-v0-6-42-github-272053915-b8e46ad9
  source_type: github_releases
  theme: search-browsing
  title: 3 Search and Browsing changes in v0.6.42
  type: change
related_changes:
- '[[Changes/AnythingLLM/2025-12-09-add-serpapi-web-search-by-alexbarron-in-https-github-com-mintplex-labs-anything|Add
  SerpApi web search]]'
- '[[Changes/Gamma/2025-12-17-want-your-site-to-show-up-in-search-results-now-you-can-enable-indexing-to-help|Want
  your site to show up in search results?]]'
- "[[Changes/HeyGen/2025-12-19-heygen-moves-fast-until-now-keeping-track-of-those-changes-could-be-a-challenge|We're
  Starting a Changelog \U0001F4E3]]"
source_release: '[[Releases/Open WebUI/open-webui-2025-12-21-v0-6-42-github-272053915-b8e46ad9|open-webui-2025-12-21-v0-6-42-github-272053915-b8e46ad9]]'
source_type: github_releases
theme: search-browsing
title: 3 Search and Browsing changes in v0.6.42
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Search and Browsing changes in v0.6.42

**Open WebUI** · 2025-12-21 · [[Themes/search-browsing|Search and Browsing]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.42) · from [[Releases/Open WebUI/open-webui-2025-12-21-v0-6-42-github-272053915-b8e46ad9|v0.6.42]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🗄️ PostgreSQL null byte insertion failures when attaching web pages or processing embedded content are now prevented by consolidating text sanitization logic across chat messages, web search results, and knowledge base documents, removing null bytes and invalid UTF-8 surrogates before database insertion. [#20072](https://github.com/open-webui/open-webui/pull/20072), [#19867](https://github.com/open-webui/open-webui/issues/19867), [#18201](https://github.com/open-webui/open-webui/issues/18201), [#15616](https://github.com/open-webui/open-webui/issues/15616)

> 🌐 Ollama Cloud web search now correctly applies domain filtering to search results. [Commit](https://github.com/open-webui/open-webui/commit/d4bd938a77c22409a1643c058b937a06e07baca9)

> 📡 WEB_SEARCH_CONCURRENT_REQUESTS default changed from 10 to 0 (unlimited) — This setting now applies to all search engines instead of only DuckDuckGo; previously users were implicitly limited to 10 concurrent queries, but now have unlimited parallel requests by default; set to 1 for sequential execution if using rate-limited APIs like Brave free tier. [#20070](https://github.com/open-webui/open-webui/pull/20070)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-12-21-user-uploaded-images-are-now-automatically-converted-from-base64-to-actual-file|🖼️ User-uploaded images are now automatically converted from base64 to actual file…]] · Collaboration
- [[Changes/Open WebUI/2025-12-21-3-editor-experience-changes-in-v0-6-42|3 Editor Experience changes in v0.6.42]] · Editor Experience
- [[Changes/Open WebUI/2025-12-21-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-12-21-2-apps-and-integrations-changes-in-v0-6-42|2 Apps and Integrations changes in v0.6.42]] · Apps and Integrations
- [[Changes/Open WebUI/2025-12-21-6-files-and-data-changes-in-v0-6-42|6 Files and Data changes in v0.6.42]] · Files and Data
- [[Changes/Open WebUI/2025-12-21-7-reliability-and-performance-changes-in-v0-6-42|7 Reliability and Performance changes in v0.6.42]] · Reliability and Performance
- [[Changes/Open WebUI/2025-12-21-11-model-support-changes-in-v0-6-42|11 Model Support changes in v0.6.42]] · Model Support
- [[Changes/Open WebUI/2025-12-21-6-safety-and-privacy-changes-in-v0-6-42|6 Safety and Privacy changes in v0.6.42]] · Safety and Privacy
- [[Changes/Open WebUI/2025-12-21-8-interface-experience-changes-in-v0-6-42|8 Interface Experience changes in v0.6.42]] · Interface Experience
- [[Changes/Open WebUI/2025-12-21-4-account-and-access-changes-in-v0-6-42|4 Account and Access changes in v0.6.42]] · Account and Access
- [[Changes/Open WebUI/2025-12-21-external-reranker-operations-were-optimized-to-prevent-event-loop-blocking-by-of|⚡ External reranker operations were optimized to prevent event loop blocking…]] · Automation and Scheduling
- [[Changes/Open WebUI/2025-12-21-11-developer-workflow-changes-in-v0-6-42|11 Developer Workflow changes in v0.6.42]] · Developer Workflow
- [[Changes/Open WebUI/2025-12-21-2-multimodal-input-changes-in-v0-6-42|2 Multimodal Input changes in v0.6.42]] · Multimodal Input
- [[Changes/Open WebUI/2025-12-21-4-image-generation-changes-in-v0-6-42|4 Image Generation changes in v0.6.42]] · Image Generation
- [[Changes/Open WebUI/2025-12-21-2-voice-and-audio-changes-in-v0-6-42|2 Voice and Audio changes in v0.6.42]] · Voice and Audio
- [[Changes/Open WebUI/2025-12-21-channel-image-upload-handling-was-optimized-to-process-and-store-compressed-imag|🖼️ Channel image upload handling was optimized to process and store compressed…]] · Memory and Personalization
- [[Changes/Open WebUI/2025-12-21-28-other-changes-in-v0-6-42|28 other changes in v0.6.42]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Search and Browsing

- Earlier: 2025-12-19 · HeyGen · [[Changes/HeyGen/2025-12-19-heygen-moves-fast-until-now-keeping-track-of-those-changes-could-be-a-challenge|We're Starting a Changelog 📣]]
- Later: 2026-01-07 · Codex CLI · [[Changes/Codex CLI/2026-01-07-4-search-and-browsing-changes-in-rust-v0-79-0|4 Search and Browsing changes in rust-v0.79.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-05-28 · Descript · [[Changes/Descript/2020-05-28-added-ability-to-batch-delete-ignore-search-results|Added ability to batch delete/ignore search results]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-12-21-c659f5&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-12-21-3-search-and-browsing-changes-in-v0-6-42.md%0ACard%20ID%3A%20open-webui-2025-12-21-c659f5%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.42%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->