---
card_id: open-webui-2026-03-01-b4d5f4
date: '2026-03-01'
description: "Open WebUI · 2026-03-01 · Model Support: 8 changes in v0.8.6 — \U0001F3F7️
  **Public/Private model filtering.** The Admin Settings Model listing now displays…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1147
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: be06e4d6cad6a5a99c8dc9aba9defe0b36d604180afb215cc1d7657be58fe7f2
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-03-01-b4d5f4
  comparison: ''
  date: '2026-03-01'
  description: 'Open WebUI — v0.8.6: 8 Model Support changes'
  evidence:
  - quote: "\U0001F3F7️ **Public/Private model filtering.** The Admin Settings Model
      listing now displays Public/Private badges and includes filter options to easily
      view public or private models. [#21732](https://github.com/open-webui/open-webui/issues/21732),
      [#21797](https://github.com/open-webui/open-webui/pull/21797)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  - quote: "\U0001F441️ **Show/Hide all models bulk action.** Administrators can now
      show or hide all models at once from the Admin Settings Models page Actions
      menu, making it faster to manage model visibility. Bulk actions now display
      a single toast notification on success for better user feedback. [#21838](https://github.com/open-webui/open-webui/pull/21838),
      [#21958](https://github.com/open-webui/open-webui/pull/21958)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  - quote: "\U0001F6E0️ **Tool call JSON error handling.** Chat no longer crashes
      when models generate malformed JSON in tool call arguments; instead, a descriptive
      error message is returned to the model for retry. [#21984](https://github.com/open-webui/open-webui/pull/21984),
      [Commit](https://github.com/open-webui/open-webui/commit/668bd44485bdf88e9083c6f09c3c47ab97a128a4)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  - quote: ⚡ **Duplicate model execution prevention.** Models are no longer called
      twice when no tools are configured, eliminating unnecessary API requests and
      reducing latency. [#21802](https://github.com/open-webui/open-webui/issues/21802),
      [Commit](https://github.com/open-webui/open-webui/commit/3c8d658160809f6d651837cf93d89dddc1d17caf)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  - quote: "\U0001F4DD **RAG template duplication.** RAG templates are no longer duplicated
      in chat messages when models make multiple tool calls, preventing hallucinations
      and incorrect tool usage. [#21780](https://github.com/open-webui/open-webui/issues/21780),
      [Commit](https://github.com/open-webui/open-webui/commit/8f49725aa5f2d9b87e559e7d3f02f037335b7914)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  - quote: "\U0001F4CA **Multi-model responses horizontal scroll.** The model list
      in multi-model responses tabs now has horizontal scroll support, making all
      models accessible on desktop screens. [#21800](https://github.com/open-webui/open-webui/issues/21800),
      [Commit](https://github.com/open-webui/open-webui/commit/a3de0bcc586ddd14dde6ae915067f082d628eaeb)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  - quote: "\U0001F35E **Model toast notification fix.** Hiding or showing a single
      model now displays only one toast notification instead of two, removing the
      redundant generic \"model updated\" message when a specific action toast is
      shown. [#22079](https://github.com/open-webui/open-webui/pull/22079)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  - quote: "\U0001F4E1 **Offline mode embedding model fix.** Open WebUI no longer
      attempts to download embedding models when in offline mode, fixing error logs
      that occurred when trying to fetch models that weren't cached locally. [#22106](https://github.com/open-webui/open-webui/pull/22106),
      [#21405](https://github.com/open-webui/open-webui/issues/21405)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 8-model-support-changes-in-v0-8-6
  source_release: open-webui-2026-03-01-v0-8-6-github-291846033-263bca05
  source_type: github_releases
  theme: model-support
  title: 8 Model Support changes in v0.8.6
  type: change
related_changes:
- '[[Changes/Cline/2026-02-27-4-model-support-changes-in-v3-68-0|4 Model Support changes
  in v3.68.0]]'
- '[[Changes/Gemini CLI/2026-02-27-11-model-support-changes-in-v0-31-0|11 Model Support
  changes in v0.31.0]]'
- '[[Changes/Ollama/2026-02-27-lfm-2-https-ollama-com-library-lfm2-lfm2-is-a-family-of-hybrid-models-designed-f|LFM
  2((source link) LFM2 is a family of hybrid models designed…]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-03-01-v0-8-6-github-291846033-263bca05|open-webui-2026-03-01-v0-8-6-github-291846033-263bca05]]'
source_type: github_releases
theme: model-support
title: 8 Model Support changes in v0.8.6
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Model Support changes in v0.8.6

**Open WebUI** · 2026-03-01 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.6) · from [[Releases/Open WebUI/open-webui-2026-03-01-v0-8-6-github-291846033-263bca05|v0.8.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🏷️ **Public/Private model filtering.** The Admin Settings Model listing now displays Public/Private badges and includes filter options to easily view public or private models. [#21732](https://github.com/open-webui/open-webui/issues/21732), [#21797](https://github.com/open-webui/open-webui/pull/21797)

> 👁️ **Show/Hide all models bulk action.** Administrators can now show or hide all models at once from the Admin Settings Models page Actions menu, making it faster to manage model visibility. Bulk actions now display a single toast notification on success for better user feedback. [#21838](https://github.com/open-webui/open-webui/pull/21838), [#21958](https://github.com/open-webui/open-webui/pull/21958)

> 🛠️ **Tool call JSON error handling.** Chat no longer crashes when models generate malformed JSON in tool call arguments; instead, a descriptive error message is returned to the model for retry. [#21984](https://github.com/open-webui/open-webui/pull/21984), [Commit](https://github.com/open-webui/open-webui/commit/668bd44485bdf88e9083c6f09c3c47ab97a128a4)

> ⚡ **Duplicate model execution prevention.** Models are no longer called twice when no tools are configured, eliminating unnecessary API requests and reducing latency. [#21802](https://github.com/open-webui/open-webui/issues/21802), [Commit](https://github.com/open-webui/open-webui/commit/3c8d658160809f6d651837cf93d89dddc1d17caf)

> 📝 **RAG template duplication.** RAG templates are no longer duplicated in chat messages when models make multiple tool calls, preventing hallucinations and incorrect tool usage. [#21780](https://github.com/open-webui/open-webui/issues/21780), [Commit](https://github.com/open-webui/open-webui/commit/8f49725aa5f2d9b87e559e7d3f02f037335b7914)

> 📊 **Multi-model responses horizontal scroll.** The model list in multi-model responses tabs now has horizontal scroll support, making all models accessible on desktop screens. [#21800](https://github.com/open-webui/open-webui/issues/21800), [Commit](https://github.com/open-webui/open-webui/commit/a3de0bcc586ddd14dde6ae915067f082d628eaeb)

> 🍞 **Model toast notification fix.** Hiding or showing a single model now displays only one toast notification instead of two, removing the redundant generic "model updated" message when a specific action toast is shown. [#22079](https://github.com/open-webui/open-webui/pull/22079)

> 📡 **Offline mode embedding model fix.** Open WebUI no longer attempts to download embedding models when in offline mode, fixing error logs that occurred when trying to fetch models that weren't cached locally. [#22106](https://github.com/open-webui/open-webui/pull/22106), [#21405](https://github.com/open-webui/open-webui/issues/21405)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-03-01-21-reliability-and-performance-changes-in-v0-8-6|21 Reliability and Performance changes in v0.8.6]] · Reliability and Performance
- [[Changes/Open WebUI/2026-03-01-2-search-and-browsing-changes-in-v0-8-6|2 Search and Browsing changes in v0.8.6]] · Search and Browsing
- [[Changes/Open WebUI/2026-03-01-oauth-session-token-decryption-oauth-sessions-are-now-properly-detached-from-the|🔓 OAuth session token decryption. OAuth sessions are now properly detached…]] · Context Window
- [[Changes/Open WebUI/2026-03-01-individual-user-sharing-control-administrators-can-now-disable-individual-user-s|🔐 Individual user sharing control. Administrators can now disable individual…]] · Collaboration
- [[Changes/Open WebUI/2026-03-01-4-interface-experience-changes-in-v0-8-6|4 Interface Experience changes in v0.8.6]] · Interface Experience
- [[Changes/Open WebUI/2026-03-01-3-account-and-access-changes-in-v0-8-6|3 Account and Access changes in v0.8.6]] · Account and Access
- [[Changes/Open WebUI/2026-03-01-4-safety-and-privacy-changes-in-v0-8-6|4 Safety and Privacy changes in v0.8.6]] · Safety and Privacy
- [[Changes/Open WebUI/2026-03-01-9-developer-workflow-changes-in-v0-8-6|9 Developer Workflow changes in v0.8.6]] · Developer Workflow
- [[Changes/Open WebUI/2026-03-01-6-other-changes-in-v0-8-6|6 other changes in v0.8.6]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-02-27 · Ollama · [[Changes/Ollama/2026-02-27-lfm-2-https-ollama-com-library-lfm2-lfm2-is-a-family-of-hybrid-models-designed-f|LFM 2((source link) LFM2 is a family of hybrid models designed…]]
- Later: 2026-03-02 · Codex CLI · [[Changes/Codex CLI/2026-03-02-4-model-support-changes-in-rust-v0-107-0|4 Model Support changes in rust-v0.107.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-03-01-b4d5f4&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-03-01-8-model-support-changes-in-v0-8-6.md%0ACard%20ID%3A%20open-webui-2026-03-01-b4d5f4%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.6%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->