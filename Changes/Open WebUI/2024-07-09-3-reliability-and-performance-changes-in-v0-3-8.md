---
card_id: open-webui-2024-07-09-96cf06
date: '2024-07-09'
description: 'Open WebUI · 2024-07-09 · Reliability and Performance: 3 changes in
  v0.3.8 — **⏰ OpenAI Streaming Timeout**: Resolved issues with OpenAI streaming response…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General
    performance: Among other improvements, users will notice that ChatGPT is now…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 572
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 78b3820935eea229a730b494f6a51003182649316120bad33bf99bfe58552141
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2024-07-09-96cf06
  comparison: ''
  date: '2024-07-09'
  description: 'Open WebUI — v0.3.8: 3 Reliability and Performance changes'
  evidence:
  - quote: '**⏰ OpenAI Streaming Timeout**: Resolved issues with OpenAI streaming
      response using the ''AIOHTTP_CLIENT_TIMEOUT'' setting, ensuring reliable performance.'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.3.8
  - quote: "**\U0001F5C3️ Database Backend**: Switched from Peewee to SQLAlchemy for
      improved concurrency support, enhancing database performance."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.3.8
  - quote: "**\U0001F680 Lazy Loading**: Implemented lazy loading for 'faster_whisper'
      and 'sentence_transformers' to reduce startup memory usage."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.3.8
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 3-reliability-and-performance-changes-in-v0-3-8
  source_release: open-webui-2024-07-09-v0-3-8-github-164686549-1ca2b2b5
  source_type: github_releases
  theme: reliability-performance
  title: 3 Reliability and Performance changes in v0.3.8
  type: change
related_changes:
- '[[Changes/Ollama/2024-06-22-3-reliability-and-performance-changes-in-v0-1-46|3
  Reliability and Performance changes in v0.1.46]]'
- '[[Changes/Ollama/2024-07-02-5-reliability-and-performance-changes-in-v0-2-0|5 Reliability
  and Performance changes in v0.2.0]]'
- '[[Changes/Aider/2024-07-04-3-reliability-and-performance-changes-in-v0-42-0|3 Reliability
  and Performance changes in v0.42.0]]'
source_release: '[[Releases/Open WebUI/open-webui-2024-07-09-v0-3-8-github-164686549-1ca2b2b5|open-webui-2024-07-09-v0-3-8-github-164686549-1ca2b2b5]]'
source_type: github_releases
theme: reliability-performance
title: 3 Reliability and Performance changes in v0.3.8
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Reliability and Performance changes in v0.3.8

**Open WebUI** · 2024-07-09 · [[Themes/reliability-performance|Reliability and Performance]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.3.8) · from [[Releases/Open WebUI/open-webui-2024-07-09-v0-3-8-github-164686549-1ca2b2b5|v0.3.8]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **⏰ OpenAI Streaming Timeout**: Resolved issues with OpenAI streaming response using the 'AIOHTTP_CLIENT_TIMEOUT' setting, ensuring reliable performance.

> **🗃️ Database Backend**: Switched from Peewee to SQLAlchemy for improved concurrency support, enhancing database performance.

> **🚀 Lazy Loading**: Implemented lazy loading for 'faster_whisper' and 'sentence_transformers' to reduce startup memory usage.

Source: https://github.com/open-webui/open-webui/releases/tag/v0.3.8
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2024-07-09-language-updates-updated-translations-for-indonesian-german-french-and-catalan-l|🌐 Language Updates]] · Accessibility and Localization
- [[Changes/Open WebUI/2024-07-09-custom-environment-for-openid-claims-allows-setting-custom-claims-for-openid-pro|🛠️ Custom Environment for OpenID Claims]] · Account and Access
- [[Changes/Open WebUI/2024-07-09-apache-tika-integration-added-support-for-using-apache-tika-as-a-document-loader|📄 Apache Tika Integration]] · Apps and Integrations
- [[Changes/Open WebUI/2024-07-09-sideways-scrolling-in-settings-settings-tabs-container-now-supports-horizontal-s|↔️ Sideways Scrolling in Settings]] · Interface Experience
- [[Changes/Open WebUI/2024-07-09-font-change-for-windows-replaced-arimo-with-inter-font-for-windows-users-improvi|🔄 Font Change for Windows]] · Mobile and Desktop
- [[Changes/Open WebUI/2024-07-09-11-other-changes-in-v0-3-8|11 other changes in v0.3.8]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2024-07-04 · Aider · [[Changes/Aider/2024-07-04-3-reliability-and-performance-changes-in-v0-42-0|3 Reliability and Performance changes in v0.42.0]]
- Later: 2024-07-11 · Ollama · [[Changes/Ollama/2024-07-11-glm4-models-will-no-longer-fail-to-load-from-out-of-memory-errors|glm4 models will no longer fail to load from out of memory errors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General performance: Among other improvements, users will notice that ChatGPT is now…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2024-07-09-96cf06&body=Card%3A%20Changes%2FOpen%20WebUI%2F2024-07-09-3-reliability-and-performance-changes-in-v0-3-8.md%0ACard%20ID%3A%20open-webui-2024-07-09-96cf06%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.3.8%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->