---
card_id: open-webui-2026-02-17-6e8a08
date: '2026-02-17'
description: 'Open WebUI · 2026-02-17 · Memory and Personalization: ⚡ **Faster model
  filtering.** Model access control filtering no longer makes a redundant database
  query…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 943
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: change
machine_hash: ac8068a8e92a790b7319ca06888da83cf2907614724abefbb17af2314c0b9f9d
product: open-webui
product_name: Open WebUI
record:
  ai_generated: true
  card_id: open-webui-2026-02-17-6e8a08
  comparison: ''
  confidence: low
  date: '2026-02-17'
  description: 'Open WebUI — v0.8.3: ⚡ **Faster model filtering.** Model access control
    filtering no longer makes a redundant database query to re-fetch model info that
    is already available in memory, reducing latency when loading model lists for
    non-admin users. [Commit](https://github.com/open-webui/open-webui/commit/34cd3d79e8688f589e3dd2f03415f8a8f9a13115)'
  evidence:
  - quote: ⚡ **Faster model filtering.** Model access control filtering no longer
      makes a redundant database query to re-fetch model info that is already available
      in memory, reducing latency when loading model lists for non-admin users. [Commit](https://github.com/open-webui/open-webui/commit/34cd3d79e8688f589e3dd2f03415f8a8f9a13115)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.3
  extractor_version: fallback-v5
  impact: significant
  kind: change
  product: open-webui
  product_name: Open WebUI
  slug: faster-model-filtering-model-access-control-filtering-no-longer-makes-a-redundan
  source_release: open-webui-2026-02-17-v0-8-3-github-287117379-ddae610a
  source_type: github_releases
  theme: memory
  theme_matches:
  - matched_terms:
    - memory
    score: 110
    theme: memory
  - matched_terms:
    - faster
    - latency
    score: 100
    theme: reliability-performance
  - matched_terms:
    - model
    score: 50
    theme: model-support
  theme_resolution: manual-semantic-rule-v1
  title: ⚡ **Faster model filtering.** Model access control filtering no longer makes…
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-02-14-reduced-memory-growth-in-long-sessions-by-evicting-transient-events-after-compac|Reduced
  memory growth in long sessions by evicting transient events after compaction]]'
- '[[Changes/Codex CLI/2026-02-17-4-memory-and-personalization-changes-in-rust-v0-102-0|4
  Memory and Personalization changes in rust-v0.102.0]]'
- '[[Changes/GitHub Copilot CLI/2026-02-17-2-memory-and-personalization-changes-in-v0-0-411|2
  Memory and Personalization changes in v0.0.411]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-02-17-v0-8-3-github-287117379-ddae610a|open-webui-2026-02-17-v0-8-3-github-287117379-ddae610a]]'
source_type: github_releases
theme: memory
title: ⚡ Faster model filtering. Model access control filtering no longer makes…
type: change
---

<!-- chronolog:begin region="header" -->
# ⚡ **Faster model filtering.** Model access control filtering no longer makes…

**Open WebUI** · 2026-02-17 · [[Themes/memory|Memory and Personalization]] · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.3) · from [[Releases/Open WebUI/open-webui-2026-02-17-v0-8-3-github-287117379-ddae610a|v0.8.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> ⚡ **Faster model filtering.** Model access control filtering no longer makes a redundant database query to re-fetch model info that is already available in memory, reducing latency when loading model lists for non-admin users. [Commit](https://github.com/open-webui/open-webui/commit/34cd3d79e8688f589e3dd2f03415f8a8f9a13115)
>
> Source: https://github.com/open-webui/open-webui/releases/tag/v0.8.3
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-02-17-general-improvements-various-improvements-were-implemented-across-the-applicatio|🔄 General improvements. Various improvements were implemented across…]] · Reliability and Performance
- [[Changes/Open WebUI/2026-02-17-image-edit-api-background-support-the-image-edit-api-now-supports-the-background|🎨 Image edit API background support. The image edit API now supports…]] · Editor Experience
- [[Changes/Open WebUI/2026-02-17-4-model-support-changes-in-v0-8-3|4 Model Support changes in v0.8.3]] · Model Support
- [[Changes/Open WebUI/2026-02-17-tool-call-display-improvements-tool-call-results-now-display-arguments-in-a-clea|🔧 Tool call display improvements. Tool call results now display arguments…]] · Developer Workflow
- [[Changes/Open WebUI/2026-02-17-image-and-file-attachment-handling-fixes-uploaded-images-are-now-correctly-sent|🖼️ Image and file attachment handling fixes. Uploaded images are now correctly…]] · Context Window
- [[Changes/Open WebUI/2026-02-17-3-other-changes-in-v0-8-3|3 other changes in v0.8.3]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Memory and Personalization

- Earlier: 2026-02-17 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-02-17-2-memory-and-personalization-changes-in-v0-0-411|2 Memory and Personalization changes in v0.0.411]]
- Later: 2026-02-18 · Gemini CLI · [[Changes/Gemini CLI/2026-02-18-2-memory-and-personalization-changes-in-v0-29-0|2 Memory and Personalization changes in v0.29.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-02-17-6e8a08&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-02-17-faster-model-filtering-model-access-control-filtering-no-longer-makes-a-redundan.md%0ACard%20ID%3A%20open-webui-2026-02-17-6e8a08%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.3%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->