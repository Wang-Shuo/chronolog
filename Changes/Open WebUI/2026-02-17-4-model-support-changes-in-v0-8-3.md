---
card_id: open-webui-2026-02-17-899ab0
date: '2026-02-17'
description: 'Open WebUI · 2026-02-17 · Model Support: 4 changes in v0.8.3 — ✏️ **Model
  edit shortcut.** Users can now edit models directly from the model selector dropdown…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1135
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 97d5525cc9161eb9736c3f027b8f3c15836b0bcb7e7e45375407aec7595df789
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-02-17-899ab0
  comparison: ''
  date: '2026-02-17'
  description: 'Open WebUI — v0.8.3: 4 Model Support changes'
  evidence:
  - quote: ✏️ **Model edit shortcut.** Users can now edit models directly from the
      model selector dropdown menu, making it faster to modify model settings without
      navigating to separate admin or workspace pages. [Commit](https://github.com/open-webui/open-webui/commit/519ff40cb69cdc1d215cee369e9db70ff7438153)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.3
  - quote: "\U0001F6E1️ **Missing function error handling.** Models that reference
      deleted functions no longer cause the entire /api/models endpoint to crash;
      instead, the missing functions are skipped and logged, allowing the rest of
      the models to load successfully. [#21476](https://github.com/open-webui/open-webui/pull/21476),
      [#21464](https://github.com/open-webui/open-webui/issues/21464)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.3
  - quote: "\U0001F680 **Startup model pre-fetch error handling.** If model pre-fetching
      fails during app startup, the application now logs a warning and continues instead
      of crashing entirely. [Commit](https://github.com/open-webui/open-webui/commit/337109e99ce390f55a9085d0a301853637923779)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.3
  - quote: ⚙️ **Function module loading error handling.** Function modules that fail
      to load during startup or model processing are now caught and logged, preventing
      crashes when models reference functions with loading errors. [Commit](https://github.com/open-webui/open-webui/commit/15b893e651de71b033408e1b713e0b51f6829ab8)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.3
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 4-model-support-changes-in-v0-8-3
  source_release: open-webui-2026-02-17-v0-8-3-github-287117379-ddae610a
  source_type: github_releases
  theme: model-support
  title: 4 Model Support changes in v0.8.3
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-02-17-11699-chore-rm-remote-models-fflag-sayan-oai|♯11699
  chore: rm remote models fflag @sayan-oai]]'
- '[[Changes/GitHub Copilot CLI/2026-02-17-2-model-support-changes-in-v0-0-411|2 Model
  Support changes in v0.0.411]]'
- '[[Changes/Midjourney/2026-02-17-please-note|Please Note]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-02-17-v0-8-3-github-287117379-ddae610a|open-webui-2026-02-17-v0-8-3-github-287117379-ddae610a]]'
source_type: github_releases
theme: model-support
title: 4 Model Support changes in v0.8.3
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Model Support changes in v0.8.3

**Open WebUI** · 2026-02-17 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.3) · from [[Releases/Open WebUI/open-webui-2026-02-17-v0-8-3-github-287117379-ddae610a|v0.8.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> ✏️ **Model edit shortcut.** Users can now edit models directly from the model selector dropdown menu, making it faster to modify model settings without navigating to separate admin or workspace pages. [Commit](https://github.com/open-webui/open-webui/commit/519ff40cb69cdc1d215cee369e9db70ff7438153)

> 🛡️ **Missing function error handling.** Models that reference deleted functions no longer cause the entire /api/models endpoint to crash; instead, the missing functions are skipped and logged, allowing the rest of the models to load successfully. [#21476](https://github.com/open-webui/open-webui/pull/21476), [#21464](https://github.com/open-webui/open-webui/issues/21464)

> 🚀 **Startup model pre-fetch error handling.** If model pre-fetching fails during app startup, the application now logs a warning and continues instead of crashing entirely. [Commit](https://github.com/open-webui/open-webui/commit/337109e99ce390f55a9085d0a301853637923779)

> ⚙️ **Function module loading error handling.** Function modules that fail to load during startup or model processing are now caught and logged, preventing crashes when models reference functions with loading errors. [Commit](https://github.com/open-webui/open-webui/commit/15b893e651de71b033408e1b713e0b51f6829ab8)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.8.3
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-02-17-general-improvements-various-improvements-were-implemented-across-the-applicatio|🔄 General improvements. Various improvements were implemented across…]] · Reliability and Performance
- [[Changes/Open WebUI/2026-02-17-image-edit-api-background-support-the-image-edit-api-now-supports-the-background|🎨 Image edit API background support. The image edit API now supports…]] · Editor Experience
- [[Changes/Open WebUI/2026-02-17-faster-model-filtering-model-access-control-filtering-no-longer-makes-a-redundan|⚡ Faster model filtering. Model access control filtering no longer makes…]] · Memory and Personalization
- [[Changes/Open WebUI/2026-02-17-tool-call-display-improvements-tool-call-results-now-display-arguments-in-a-clea|🔧 Tool call display improvements. Tool call results now display arguments…]] · Developer Workflow
- [[Changes/Open WebUI/2026-02-17-image-and-file-attachment-handling-fixes-uploaded-images-are-now-correctly-sent|🖼️ Image and file attachment handling fixes. Uploaded images are now correctly…]] · Context Window
- [[Changes/Open WebUI/2026-02-17-3-other-changes-in-v0-8-3|3 other changes in v0.8.3]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-02-17 · Midjourney · [[Changes/Midjourney/2026-02-17-please-note|Please Note]]
- Later: 2026-02-18 · AnythingLLM · [[Changes/AnythingLLM/2026-02-18-4-model-support-changes-in-v1-11-0|4 Model Support changes in v1.11.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-02-17-899ab0&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-02-17-4-model-support-changes-in-v0-8-3.md%0ACard%20ID%3A%20open-webui-2026-02-17-899ab0%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.3%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->