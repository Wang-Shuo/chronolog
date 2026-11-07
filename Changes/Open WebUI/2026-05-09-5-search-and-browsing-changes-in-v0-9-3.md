---
card_id: open-webui-2026-05-09-00c796
date: '2026-05-09'
description: "Open WebUI · 2026-05-09 · Search and Browsing: 5 changes in v0.9.3 —
  \U0001F50E **Brave LLM Context web search.** Administrators can now choose Brave
  LLM Context as a…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-browsing-an-experimental-model-that-knows-when-and-how-to-browse-the-internet|Browsing:
    An experimental model that knows when and how to browse the internet]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1143
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: search-browsing
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f378b1ce7ca8bf8329432f2298143748420c4924a16e8e58761df6d49eff8a89
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-05-09-00c796
  comparison: ''
  date: '2026-05-09'
  description: 'Open WebUI — v0.9.3: 5 Search and Browsing changes'
  evidence:
  - quote: "\U0001F50E **Brave LLM Context web search.** Administrators can now choose
      Brave LLM Context as a web search provider to retrieve richer grounded passages
      with a configurable context token budget. [Commit](https://github.com/open-webui/open-webui/commit/6700f7bb72d14a3f8dbb72dfa064cae3b3dc29ac),
      [#24120](https://github.com/open-webui/open-webui/issues/24120)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F5C2️ **Open Terminal date sorting.** Open Terminal now includes
      sort controls for name and date, with directory-first ordering and modified-time
      visibility to make file browsing faster. [Commit](https://github.com/open-webui/open-webui/commit/6bdc2ffa79d72daf78981209c9c5292c697cbfe5),
      [#24425](https://github.com/open-webui/open-webui/issues/24425)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F30D **Web search proxy compatibility.** DuckDuckGo search now respects
      configured proxy environments more reliably, and trust-env behavior defaults
      to enabled so proxied web loading does not fail unexpectedly. [Commit](https://github.com/open-webui/open-webui/commit/bb0e6cb1085aa3c3da66a5f5ea1cecff7e9b5297),
      [#23810](https://github.com/open-webui/open-webui/pull/23810)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F310 **Yandex result parsing guard.** Yandex web search no longer
      fails when some XML fields are missing in individual results, so valid search
      responses continue to return usable sources instead of dropping to no results.
      [Commit](https://github.com/open-webui/open-webui/commit/9386fc83a3eff3e55cc157ac8c15c337e3d822c1),
      [#24243](https://github.com/open-webui/open-webui/issues/24243)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F986 **DDGS auto-backend compatibility.** Web search now handles
      DDGS automatic backend selection correctly and safely falls back on empty or
      rate-limited responses, preventing search failures in newer DDGS versions. [Commit](https://github.com/open-webui/open-webui/commit/9adc0c442a57eaa88a5f30c2b2cb393623154e20),
      [#24188](https://github.com/open-webui/open-webui/issues/24188)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 5-search-and-browsing-changes-in-v0-9-3
  source_release: open-webui-2026-05-09-v0-9-3-github-319872270-bb8aabca
  source_type: github_releases
  theme: search-browsing
  title: 5 Search and Browsing changes in v0.9.3
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-05-01-research-uses-an-orchestrator-subagent-model-for-more-thorough-and-reliable-deep|/research
  uses an orchestrator/subagent model for more thorough and reliable deep…]]'
- '[[Changes/Ollama/2026-05-03-web-search-coming-soon|Web Search (coming soon)]]'
- '[[Changes/Codex CLI/2026-05-07-21054-rollout-store-web-search-and-mcp-tool-calls-owenlin0|♯21054
  rollout: store web search and mcp tool calls @owenlin0]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-05-09-v0-9-3-github-319872270-bb8aabca|open-webui-2026-05-09-v0-9-3-github-319872270-bb8aabca]]'
source_type: github_releases
theme: search-browsing
title: 5 Search and Browsing changes in v0.9.3
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Search and Browsing changes in v0.9.3

**Open WebUI** · 2026-05-09 · [[Themes/search-browsing|Search and Browsing]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.3) · from [[Releases/Open WebUI/open-webui-2026-05-09-v0-9-3-github-319872270-bb8aabca|v0.9.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔎 **Brave LLM Context web search.** Administrators can now choose Brave LLM Context as a web search provider to retrieve richer grounded passages with a configurable context token budget. [Commit](https://github.com/open-webui/open-webui/commit/6700f7bb72d14a3f8dbb72dfa064cae3b3dc29ac), [#24120](https://github.com/open-webui/open-webui/issues/24120)

> 🗂️ **Open Terminal date sorting.** Open Terminal now includes sort controls for name and date, with directory-first ordering and modified-time visibility to make file browsing faster. [Commit](https://github.com/open-webui/open-webui/commit/6bdc2ffa79d72daf78981209c9c5292c697cbfe5), [#24425](https://github.com/open-webui/open-webui/issues/24425)

> 🌍 **Web search proxy compatibility.** DuckDuckGo search now respects configured proxy environments more reliably, and trust-env behavior defaults to enabled so proxied web loading does not fail unexpectedly. [Commit](https://github.com/open-webui/open-webui/commit/bb0e6cb1085aa3c3da66a5f5ea1cecff7e9b5297), [#23810](https://github.com/open-webui/open-webui/pull/23810)

> 🌐 **Yandex result parsing guard.** Yandex web search no longer fails when some XML fields are missing in individual results, so valid search responses continue to return usable sources instead of dropping to no results. [Commit](https://github.com/open-webui/open-webui/commit/9386fc83a3eff3e55cc157ac8c15c337e3d822c1), [#24243](https://github.com/open-webui/open-webui/issues/24243)

> 🦆 **DDGS auto-backend compatibility.** Web search now handles DDGS automatic backend selection correctly and safely falls back on empty or rate-limited responses, preventing search failures in newer DDGS versions. [Commit](https://github.com/open-webui/open-webui/commit/9adc0c442a57eaa88a5f30c2b2cb393623154e20), [#24188](https://github.com/open-webui/open-webui/issues/24188)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-05-09-10-voice-and-audio-changes-in-v0-9-3|10 Voice and Audio changes in v0.9.3]] · Voice and Audio
- [[Changes/Open WebUI/2026-05-09-5-editor-experience-changes-in-v0-9-3|5 Editor Experience changes in v0.9.3]] · Editor Experience
- [[Changes/Open WebUI/2026-05-09-8-interface-experience-changes-in-v0-9-3|8 Interface Experience changes in v0.9.3]] · Interface Experience
- [[Changes/Open WebUI/2026-05-09-4-context-window-changes-in-v0-9-3|4 Context Window changes in v0.9.3]] · Context Window
- [[Changes/Open WebUI/2026-05-09-3-apps-and-integrations-changes-in-v0-9-3|3 Apps and Integrations changes in v0.9.3]] · Apps and Integrations
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
## Nearby in Search and Browsing

- Earlier: 2026-05-07 · Codex CLI · [[Changes/Codex CLI/2026-05-07-21054-rollout-store-web-search-and-mcp-tool-calls-owenlin0|♯21054 rollout: store web search and mcp tool calls @owenlin0]]
- Later: 2026-05-09 · OpenCode · [[Changes/OpenCode/2026-05-09-core-limited-openai-deep-research-models-to-the-reasoning-level-they-actually-su|Core Limited OpenAI deep research models to the reasoning level they actually support]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-browsing-an-experimental-model-that-knows-when-and-how-to-browse-the-internet|Browsing: An experimental model that knows when and how to browse the internet]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-05-09-00c796&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-05-09-5-search-and-browsing-changes-in-v0-9-3.md%0ACard%20ID%3A%20open-webui-2026-05-09-00c796%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.3%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->