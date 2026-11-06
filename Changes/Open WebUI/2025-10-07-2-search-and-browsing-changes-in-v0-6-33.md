---
card_id: open-webui-2025-10-07-5c3893
date: '2025-10-07'
description: "Open WebUI · 2025-10-07 · Search and Browsing: 2 changes in v0.6.33
  — \U0001F50D Web search now handles individual source failures gracefully, continuing
  to process…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-browsing-an-experimental-model-that-knows-when-and-how-to-browse-the-internet|Browsing:
    An experimental model that knows when and how to browse the internet]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 929
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: search-browsing
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 7651f4df92c78731d3089502e8b43883b4e37c1e3259c06eac357f1de82f3311
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-10-07-5c3893
  comparison: ''
  date: '2025-10-07'
  description: 'Open WebUI — v0.6.33: 2 Search and Browsing changes'
  evidence:
  - quote: "\U0001F50D Web search now handles individual source failures gracefully,
      continuing to process remaining sources instead of failing entirely when a single
      URL is unreachable or returns an error. [Commit](https://github.com/open-webui/open-webui/commit/e000494e488090c5f66989a2b3f89d3eaeb7946b),
      [Commit](https://github.com/open-webui/open-webui/commit/53e98620bff38ab9280aee5165af0a704bdd99b9)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.33
  - quote: "\U0001F50D Web search query logging now uses debug level instead of info
      level, preventing user search queries from appearing in production logs. [#17888](https://github.com/open-webui/open-webui/pull/17888)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.33
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 2-search-and-browsing-changes-in-v0-6-33
  source_release: open-webui-2025-10-07-v0-6-33-github-252853067-e907999d
  source_type: github_releases
  theme: search-browsing
  title: 2 Search and Browsing changes in v0.6.33
  type: change
related_changes:
- '[[Changes/Cursor/2025-09-29-1-7-20-web-search-auto-accept-setting|1.7.20: Web search
  auto-accept setting]]'
- '[[Changes/Codex CLI/2025-10-03-4511-wire-up-web-search-item|♯4511 Wire up web search
  item]]'
- '[[Changes/Replit/2025-10-03-app-themes-font-improvements|App Themes font improvements]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-10-07-v0-6-33-github-252853067-e907999d|open-webui-2025-10-07-v0-6-33-github-252853067-e907999d]]'
source_type: github_releases
theme: search-browsing
title: 2 Search and Browsing changes in v0.6.33
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Search and Browsing changes in v0.6.33

**Open WebUI** · 2025-10-07 · [[Themes/search-browsing|Search and Browsing]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.33) · from [[Releases/Open WebUI/open-webui-2025-10-07-v0-6-33-github-252853067-e907999d|v0.6.33]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔍 Web search now handles individual source failures gracefully, continuing to process remaining sources instead of failing entirely when a single URL is unreachable or returns an error. [Commit](https://github.com/open-webui/open-webui/commit/e000494e488090c5f66989a2b3f89d3eaeb7946b), [Commit](https://github.com/open-webui/open-webui/commit/53e98620bff38ab9280aee5165af0a704bdd99b9)

> 🔍 Web search query logging now uses debug level instead of info level, preventing user search queries from appearing in production logs. [#17888](https://github.com/open-webui/open-webui/pull/17888)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.33
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-10-07-8-model-support-changes-in-v0-6-33|8 Model Support changes in v0.6.33]] · Model Support
- [[Changes/Open WebUI/2025-10-07-10-account-and-access-changes-in-v0-6-33|10 Account and Access changes in v0.6.33]] · Account and Access
- [[Changes/Open WebUI/2025-10-07-2-files-and-data-changes-in-v0-6-33|2 Files and Data changes in v0.6.33]] · Files and Data
- [[Changes/Open WebUI/2025-10-07-tab-characters-are-now-preserved-when-pasting-code-or-formatted-text-into-the-ch|⌨️ Tab characters are now preserved when pasting code or formatted text…]] · Editor Experience
- [[Changes/Open WebUI/2025-10-07-6-reliability-and-performance-changes-in-v0-6-33|6 Reliability and Performance changes in v0.6.33]] · Reliability and Performance
- [[Changes/Open WebUI/2025-10-07-redis-session-storage-is-now-available-as-an-experimental-option-for-oauth-authe|🗄️ Redis session storage is now available as an experimental option for OAuth…]] · Account and Access
- [[Changes/Open WebUI/2025-10-07-8-interface-experience-changes-in-v0-6-33|8 Interface Experience changes in v0.6.33]] · Interface Experience
- [[Changes/Open WebUI/2025-10-07-azure-text-to-speech-now-properly-escapes-special-characters-like-ampersands-in|🔊 Azure Text-to-Speech now properly escapes special characters like ampersands…]] · Voice and Audio
- [[Changes/Open WebUI/2025-10-07-3-developer-workflow-changes-in-v0-6-33|3 Developer Workflow changes in v0.6.33]] · Developer Workflow
- [[Changes/Open WebUI/2025-10-07-3-apps-and-integrations-changes-in-v0-6-33|3 Apps and Integrations changes in v0.6.33]] · Apps and Integrations
- [[Changes/Open WebUI/2025-10-07-13-other-changes-in-v0-6-33|13 other changes in v0.6.33]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Search and Browsing

- Earlier: 2025-10-03 · Replit · [[Changes/Replit/2025-10-03-app-themes-font-improvements|App Themes font improvements]]
- Later: 2025-10-22 · Gemini CLI · [[Changes/Gemini CLI/2025-10-22-refactor-core-migrate-web-search-tool-to-tool-names-by-abhipatel12-in-https-gith|refactor(core): migrate web search tool to tool-names]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-browsing-an-experimental-model-that-knows-when-and-how-to-browse-the-internet|Browsing: An experimental model that knows when and how to browse the internet]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-10-07-5c3893&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-10-07-2-search-and-browsing-changes-in-v0-6-33.md%0ACard%20ID%3A%20open-webui-2025-10-07-5c3893%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.33%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->