---
card_id: open-webui-2026-03-09-b258b6
date: '2026-03-09'
description: "Open WebUI · 2026-03-09 · Search and Browsing: 2 changes in v0.8.10
  — \U0001F4DA **Knowledge file embedding updates.** Fixed a bug where updating knowledge
  files left…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-browsing-an-experimental-model-that-knows-when-and-how-to-browse-the-internet|Browsing:
    An experimental model that knows when and how to browse the internet]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1082
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: search-browsing
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 85175a5de14085ba64759c4c7c25b0c47dc25f37b844d1fdef69576082f07539
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-03-09-b258b6
  comparison: ''
  date: '2026-03-09'
  description: 'Open WebUI — v0.8.10: 2 Search and Browsing changes'
  evidence:
  - quote: "\U0001F4DA **Knowledge file embedding updates.** Fixed a bug where updating
      knowledge files left old embeddings in the database, causing search results
      to include duplicate and stale data. [#20558](https://github.com/open-webui/open-webui/issues/20558)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.10
  - quote: "\U0001F50D **Web search favicon fallback.** Fixed web search sources showing
      broken image icons when favicons couldn't be loaded from external sources; now
      falls back to the default Open WebUI favicon. [#21897](https://github.com/open-webui/open-webui/pull/21897)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.10
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 2-search-and-browsing-changes-in-v0-8-10
  source_release: open-webui-2026-03-09-v0-8-10-github-294485945-5852a771
  source_type: github_releases
  theme: search-browsing
  title: 2 Search and Browsing changes in v0.8.10
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-03-05-13538-chore-add-web-search-tool-type-for-image-support-sayan-oai|♯13538
  chore: add web_search_tool_type for image support @sayan-oai]]'
- '[[Changes/GitHub Copilot CLI/2026-03-06-elicitation-enum-and-boolean-fields-now-require-enter-to-confirm-a-selection-wit|Elicitation
  enum and boolean fields now require Enter to confirm a selection…]]'
- '[[Changes/Open WebUI/2026-03-08-2-search-and-browsing-changes-in-v0-8-9|2 Search
  and Browsing changes in v0.8.9]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-03-09-v0-8-10-github-294485945-5852a771|open-webui-2026-03-09-v0-8-10-github-294485945-5852a771]]'
source_type: github_releases
theme: search-browsing
title: 2 Search and Browsing changes in v0.8.10
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Search and Browsing changes in v0.8.10

**Open WebUI** · 2026-03-09 · [[Themes/search-browsing|Search and Browsing]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.10) · from [[Releases/Open WebUI/open-webui-2026-03-09-v0-8-10-github-294485945-5852a771|v0.8.10]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📚 **Knowledge file embedding updates.** Fixed a bug where updating knowledge files left old embeddings in the database, causing search results to include duplicate and stale data. [#20558](https://github.com/open-webui/open-webui/issues/20558)

> 🔍 **Web search favicon fallback.** Fixed web search sources showing broken image icons when favicons couldn't be loaded from external sources; now falls back to the default Open WebUI favicon. [#21897](https://github.com/open-webui/open-webui/pull/21897)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.8.10
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-03-09-teams-webhook-crash-fixed-a-typeerror-crash-in-the-teams-webhook-handler-when-us|📨 Teams webhook crash. Fixed a TypeError crash in the Teams webhook handler…]] · Collaboration
- [[Changes/Open WebUI/2026-03-09-2-developer-workflow-changes-in-v0-8-10|2 Developer Workflow changes in v0.8.10]] · Developer Workflow
- [[Changes/Open WebUI/2026-03-09-2-account-and-access-changes-in-v0-8-10|2 Account and Access changes in v0.8.10]] · Account and Access
- [[Changes/Open WebUI/2026-03-09-azure-speech-transcription-errors-improved-azure-ai-speech-error-handling-to-dis|🎤 Azure speech transcription errors. Improved Azure AI Speech error handling…]] · Voice and Audio
- [[Changes/Open WebUI/2026-03-09-3-model-support-changes-in-v0-8-10|3 Model Support changes in v0.8.10]] · Model Support
- [[Changes/Open WebUI/2026-03-09-2-reliability-and-performance-changes-in-v0-8-10|2 Reliability and Performance changes in v0.8.10]] · Reliability and Performance
- [[Changes/Open WebUI/2026-03-09-12-other-changes-in-v0-8-10|12 other changes in v0.8.10]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Search and Browsing

- Earlier: 2026-03-08 · Open WebUI · [[Changes/Open WebUI/2026-03-08-2-search-and-browsing-changes-in-v0-8-9|2 Search and Browsing changes in v0.8.9]]
- Later: 2026-03-10 · Codex CLI · [[Changes/Codex CLI/2026-03-10-2-search-and-browsing-changes-in-rust-v0-113-0|2 Search and Browsing changes in rust-v0.113.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-browsing-an-experimental-model-that-knows-when-and-how-to-browse-the-internet|Browsing: An experimental model that knows when and how to browse the internet]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-03-09-b258b6&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-03-09-2-search-and-browsing-changes-in-v0-8-10.md%0ACard%20ID%3A%20open-webui-2026-03-09-b258b6%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.10%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->