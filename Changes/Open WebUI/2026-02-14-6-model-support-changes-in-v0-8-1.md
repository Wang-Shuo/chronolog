---
card_id: open-webui-2026-02-14-aaeef7
date: '2026-02-14'
description: "Open WebUI · 2026-02-14 · Model Support: 6 changes in v0.8.1 — \U0001F517
  **Responses API endpoint with model routing.** The OpenAI API proxy now supports
  a /responses…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1132
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 64e284b20b6979ba4629983b9d65b43df0852cec3db02830d542e16a41d18098
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-02-14-aaeef7
  comparison: ''
  date: '2026-02-14'
  description: 'Open WebUI — v0.8.1: 6 Model Support changes'
  evidence:
  - quote: "\U0001F517 **Responses API endpoint with model routing.** The OpenAI API
      proxy now supports a /responses endpoint that routes requests to the correct
      backend based on the model field in the request, instead of always using the
      first configured endpoint. This enables support for backends like vLLM that
      provide /skills and /v1/responses endpoints. [Commit](https://github.com/open-webui/open-webui/commit/abc9b63093d65f4d74342db85b7d5df1809aa0f0),
      [Commit](https://github.com/open-webui/open-webui/commit/79ecbfc757f0642740d0e44fab98263d84295490)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.1
  - quote: ⚡ **Model and prompt list optimization.** Improved performance when loading
      models and prompts by pre-fetching user group IDs once instead of making multiple
      database queries. [Commit](https://github.com/open-webui/open-webui/commit/20de5a87da0c12e4052b50887a42ddd7228c5ef5)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.1
  - quote: "\U0001F512 **Direct model access control fix.** Model access control changes
      now persist correctly for direct Ollama and OpenAI models that don't have database
      entries, and error messages display properly instead of showing \"[object Object]\".
      [Commit](https://github.com/open-webui/open-webui/commit/f027a01ab2ff3b6175af3dd13a4478c265c0544a),
      [#21377](https://github.com/open-webui/open-webui/issues/21377)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.1
  - quote: "\U0001F5C4️ **PostgreSQL analytics query fix.** Fixed an issue where retrieving
      chat IDs by model ID would fail on PostgreSQL due to incompatible DISTINCT ordering,
      while SQLite worked correctly. [#21347](https://github.com/open-webui/open-webui/issues/21347),
      [Commit](https://github.com/open-webui/open-webui/commit/7bda6bf767d5d5c4dc1111465096a88e10b5030e)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.1
  - quote: ☁️ **Ollama Cloud model naming fix.** Fixed an issue where using Ollama
      Cloud models would fail with "Model not found" errors because ":latest" was
      incorrectly appended to model names. [#21386](https://github.com/open-webui/open-webui/issues/21386)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.1
  - quote: "\U0001F3AF **Model selector scroll position.** The model selector dropdown
      now correctly scrolls to and centers the currently selected model when opened,
      and resets scroll position when reopened. [Commit](https://github.com/open-webui/open-webui/commit/0b05b2fc7ed4c38af158707438ff404d1beb7c91)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 6-model-support-changes-in-v0-8-1
  source_release: open-webui-2026-02-14-v0-8-1-github-286288526-aa333d77
  source_type: github_releases
  theme: model-support
  title: 6 Model Support changes in v0.8.1
  type: change
related_changes:
- '[[Changes/Replit/2026-02-13-claude-opus-4-5-support|Claude Opus 4.5 support]]'
- '[[Changes/Midjourney/2026-02-14-please-note|Please Note]]'
- '[[Changes/Ollama/2026-02-14-2-model-support-changes-in-v0-16-2|2 Model Support
  changes in v0.16.2]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-02-14-v0-8-1-github-286288526-aa333d77|open-webui-2026-02-14-v0-8-1-github-286288526-aa333d77]]'
source_type: github_releases
theme: model-support
title: 6 Model Support changes in v0.8.1
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Model Support changes in v0.8.1

**Open WebUI** · 2026-02-14 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.1) · from [[Releases/Open WebUI/open-webui-2026-02-14-v0-8-1-github-286288526-aa333d77|v0.8.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔗 **Responses API endpoint with model routing.** The OpenAI API proxy now supports a /responses endpoint that routes requests to the correct backend based on the model field in the request, instead of always using the first configured endpoint. This enables support for backends like vLLM that provide /skills and /v1/responses endpoints. [Commit](https://github.com/open-webui/open-webui/commit/abc9b63093d65f4d74342db85b7d5df1809aa0f0), [Commit](https://github.com/open-webui/open-webui/commit/79ecbfc757f0642740d0e44fab98263d84295490)

> ⚡ **Model and prompt list optimization.** Improved performance when loading models and prompts by pre-fetching user group IDs once instead of making multiple database queries. [Commit](https://github.com/open-webui/open-webui/commit/20de5a87da0c12e4052b50887a42ddd7228c5ef5)

> 🔒 **Direct model access control fix.** Model access control changes now persist correctly for direct Ollama and OpenAI models that don't have database entries, and error messages display properly instead of showing "[object Object]". [Commit](https://github.com/open-webui/open-webui/commit/f027a01ab2ff3b6175af3dd13a4478c265c0544a), [#21377](https://github.com/open-webui/open-webui/issues/21377)

> 🗄️ **PostgreSQL analytics query fix.** Fixed an issue where retrieving chat IDs by model ID would fail on PostgreSQL due to incompatible DISTINCT ordering, while SQLite worked correctly. [#21347](https://github.com/open-webui/open-webui/issues/21347), [Commit](https://github.com/open-webui/open-webui/commit/7bda6bf767d5d5c4dc1111465096a88e10b5030e)

> ☁️ **Ollama Cloud model naming fix.** Fixed an issue where using Ollama Cloud models would fail with "Model not found" errors because ":latest" was incorrectly appended to model names. [#21386](https://github.com/open-webui/open-webui/issues/21386)

> 🎯 **Model selector scroll position.** The model selector dropdown now correctly scrolls to and centers the currently selected model when opened, and resets scroll position when reopened. [Commit](https://github.com/open-webui/open-webui/commit/0b05b2fc7ed4c38af158707438ff404d1beb7c91)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.8.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-02-14-2-apps-and-integrations-changes-in-v0-8-1|2 Apps and Integrations changes in v0.8.1]] · Apps and Integrations
- [[Changes/Open WebUI/2026-02-14-2-developer-workflow-changes-in-v0-8-1|2 Developer Workflow changes in v0.8.1]] · Developer Workflow
- [[Changes/Open WebUI/2026-02-14-public-sharing-security-fix-fixed-a-security-issue-where-users-with-write-access|🛡️ Public sharing security fix. Fixed a security issue where users with write…]] · Safety and Privacy
- [[Changes/Open WebUI/2026-02-14-2-reliability-and-performance-changes-in-v0-8-1|2 Reliability and Performance changes in v0.8.1]] · Reliability and Performance
- [[Changes/Open WebUI/2026-02-14-web-search-result-count-the-built-in-search-web-tool-now-respects-the-admin-conf|🔍 Web search result count. The built-in search_web tool now respects…]] · Search and Browsing
- [[Changes/Open WebUI/2026-02-14-metadata-processing-crash-fix-fixed-a-latent-bug-where-processing-document-metad|📝 Metadata processing crash fix. Fixed a latent bug where processing document…]] · Files and Data
- [[Changes/Open WebUI/2026-02-14-sync-modal-unexpected-appearance-fixed-an-issue-where-the-sync-modal-would-appea|🐛 Sync modal unexpected appearance. Fixed an issue where the Sync Modal would…]] · Collaboration
- [[Changes/Open WebUI/2026-02-14-2-interface-experience-changes-in-v0-8-1|2 Interface Experience changes in v0.8.1]] · Interface Experience
- [[Changes/Open WebUI/2026-02-14-6-other-changes-in-v0-8-1|6 other changes in v0.8.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-02-14 · Ollama · [[Changes/Ollama/2026-02-14-2-model-support-changes-in-v0-16-2|2 Model Support changes in v0.16.2]]
- Later: 2026-02-14 · OpenCode · [[Changes/OpenCode/2026-02-14-core-update-ai-sdk-packages-and-use-adaptive-reasoning-for-claude-opus-4-6-on-ve|Core Update AI SDK packages and use adaptive reasoning for Claude Opus 4.6…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-02-14-aaeef7&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-02-14-6-model-support-changes-in-v0-8-1.md%0ACard%20ID%3A%20open-webui-2026-02-14-aaeef7%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->