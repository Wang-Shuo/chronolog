---
card_id: open-webui-2026-10-10-d8ba25
date: '2026-10-10'
description: "Open WebUI · 2026-10-10 · Search and Browsing: 4 changes in v0.12.0
  — \U0001F575️ **Tavily search depth.** Administrators can now choose how deep Tavily
  web searches…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-05-28-added-ability-to-batch-delete-ignore-search-results|Added
    ability to batch delete/ignore search results]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2326
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: search-browsing
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9f3169390492e881e6c5f1598494bc176136b1d9269d2c45bb26ec1d54ec6ed9
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-10-10-d8ba25
  comparison: ''
  date: '2026-10-10'
  description: 'Open WebUI — v0.12.0: 4 Search and Browsing changes'
  evidence:
  - quote: "\U0001F575️ **Tavily search depth.** Administrators can now choose how
      deep Tavily web searches go, from ultra-fast to advanced, in the Tavily settings
      of the web search page or through \"TAVILY_SEARCH_DEPTH\", separately from the
      existing extract depth. [#31308](https://github.com/open-webui/open-webui/pull/31308),
      [#29891](https://github.com/open-webui/open-webui/issues/29891)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F6F8 **Exa as the web loader.** Administrators can now pick Exa
      as the Web Loader Engine in Web Search settings, so pages from web search and
      attached links are fetched through Exa, reusing the Exa API key when Exa is
      also the search engine. [Commit](https://github.com/open-webui/open-webui/commit/09dcb6088720d6df8dbd35c0e40b5c7dbc8f6c1b)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F526 **Web searches where no page loads.** A web search where none
      of the result pages could be loaded now says so, where it reported an embedding
      configuration failure. [#31859](https://github.com/open-webui/open-webui/pull/31859),
      [#29327](https://github.com/open-webui/open-webui/issues/29327)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: ✌️ **Web search confirmation needing two clicks.** With web search confirmation
      on, turning on Web Search from the Integrations menu now closes the menu, so
      a single click on Cancel or Continue in the confirmation popup works. [#31976](https://github.com/open-webui/open-webui/pull/31976),
      [#31963](https://github.com/open-webui/open-webui/issues/31963)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 4-search-and-browsing-changes-in-v0-12-0
  source_release: open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b
  source_type: github_releases
  theme: search-browsing
  title: 4 Search and Browsing changes in v0.12.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-10-07-3-search-and-browsing-changes-in-rust-v0-161-0|3
  Search and Browsing changes in rust-v0.161.0]]'
- '[[Changes/Raycast/2026-10-09-custom-ai-providers-you-can-now-give-custom-provider-models-raycast-s-web-search|Custom
  AI Providers]]'
- '[[Changes/Raycast/2026-10-09-custom-ai-providers-you-can-now-give-custom-provider-models-raycast-s-web-search-a80f41|Custom
  AI Providers]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b|open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b]]'
source_type: github_releases
theme: search-browsing
title: 4 Search and Browsing changes in v0.12.0
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Search and Browsing changes in v0.12.0

**Open WebUI** · 2026-10-10 · [[Themes/search-browsing|Search and Browsing]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.0) · from [[Releases/Open WebUI/open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b|v0.12.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🕵️ **Tavily search depth.** Administrators can now choose how deep Tavily web searches go, from ultra-fast to advanced, in the Tavily settings of the web search page or through "TAVILY_SEARCH_DEPTH", separately from the existing extract depth. [#31308](https://github.com/open-webui/open-webui/pull/31308), [#29891](https://github.com/open-webui/open-webui/issues/29891)

> 🛸 **Exa as the web loader.** Administrators can now pick Exa as the Web Loader Engine in Web Search settings, so pages from web search and attached links are fetched through Exa, reusing the Exa API key when Exa is also the search engine. [Commit](https://github.com/open-webui/open-webui/commit/09dcb6088720d6df8dbd35c0e40b5c7dbc8f6c1b)

> 🔦 **Web searches where no page loads.** A web search where none of the result pages could be loaded now says so, where it reported an embedding configuration failure. [#31859](https://github.com/open-webui/open-webui/pull/31859), [#29327](https://github.com/open-webui/open-webui/issues/29327)

> ✌️ **Web search confirmation needing two clicks.** With web search confirmation on, turning on Web Search from the Integrations menu now closes the menu, so a single click on Cancel or Continue in the confirmation popup works. [#31976](https://github.com/open-webui/open-webui/pull/31976), [#31963](https://github.com/open-webui/open-webui/issues/31963)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-10-10-5-reliability-and-performance-changes-in-v0-12-0|5 Reliability and Performance changes in v0.12.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-10-10-5-enterprise-and-administration-changes-in-v0-12-0|5 Enterprise and Administration changes in v0.12.0]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-10-10-7-apps-and-integrations-changes-in-v0-12-0|7 Apps and Integrations changes in v0.12.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-10-10-12-voice-and-audio-changes-in-v0-12-0|12 Voice and Audio changes in v0.12.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-10-10-27-developer-workflow-changes-in-v0-12-0|27 Developer Workflow changes in v0.12.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-10-10-5-image-generation-changes-in-v0-12-0|5 Image Generation changes in v0.12.0]] · Image Generation
- [[Changes/Open WebUI/2026-10-10-49-model-support-changes-in-v0-12-0|49 Model Support changes in v0.12.0]] · Model Support
- [[Changes/Open WebUI/2026-10-10-19-account-and-access-changes-in-v0-12-0|19 Account and Access changes in v0.12.0]] · Account and Access
- [[Changes/Open WebUI/2026-10-10-10-automation-and-scheduling-changes-in-v0-12-0|10 Automation and Scheduling changes in v0.12.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-10-10-3-mobile-and-desktop-changes-in-v0-12-0|3 Mobile and Desktop changes in v0.12.0]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-10-10-6-files-and-data-changes-in-v0-12-0|6 Files and Data changes in v0.12.0]] · Files and Data
- [[Changes/Open WebUI/2026-10-10-13-collaboration-changes-in-v0-12-0|13 Collaboration changes in v0.12.0]] · Collaboration
- [[Changes/Open WebUI/2026-10-10-2-memory-and-personalization-changes-in-v0-12-0|2 Memory and Personalization changes in v0.12.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-10-10-5-context-window-changes-in-v0-12-0|5 Context Window changes in v0.12.0]] · Context Window
- [[Changes/Open WebUI/2026-10-10-18-interface-experience-changes-in-v0-12-0|18 Interface Experience changes in v0.12.0]] · Interface Experience
- [[Changes/Open WebUI/2026-10-10-7-agent-mode-changes-in-v0-12-0|7 Agent Mode changes in v0.12.0]] · Agent Mode
- [[Changes/Open WebUI/2026-10-10-6-safety-and-privacy-changes-in-v0-12-0|6 Safety and Privacy changes in v0.12.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-10-10-21-editor-experience-changes-in-v0-12-0|21 Editor Experience changes in v0.12.0]] · Editor Experience
- [[Changes/Open WebUI/2026-10-10-68-other-changes-in-v0-12-0|68 other changes in v0.12.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Search and Browsing

- Earlier: 2026-10-09 · Raycast · [[Changes/Raycast/2026-10-09-custom-ai-providers-you-can-now-give-custom-provider-models-raycast-s-web-search-a80f41|Custom AI Providers]]
- Later: 2026-10-10 · OpenClaw · [[Changes/OpenClaw/2026-10-10-3-search-and-browsing-changes-in-v2026-10-1|3 Search and Browsing changes in v2026.10.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-05-28 · Descript · [[Changes/Descript/2020-05-28-added-ability-to-batch-delete-ignore-search-results|Added ability to batch delete/ignore search results]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-10-d8ba25&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-10-4-search-and-browsing-changes-in-v0-12-0.md%0ACard%20ID%3A%20open-webui-2026-10-10-d8ba25%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->