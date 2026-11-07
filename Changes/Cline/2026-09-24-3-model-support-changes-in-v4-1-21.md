---
card_id: cline-2026-09-24-3b3449
date: '2026-09-24'
description: 'Cline · 2026-09-24 · Model Support: 3 changes in v4.1.21 — New provider:
  ai&, an OpenAI-compatible endpoint serving open-weight models from Japan.'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1354
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2e5e31bf77ba784f246cb4ef25e280535d642f06c8cca815fcbf2dff43dca836
product: cline
product_name: Cline
record:
  card_id: cline-2026-09-24-3b3449
  comparison: ''
  date: '2026-09-24'
  description: 'Cline — v4.1.21: 3 Model Support changes'
  evidence:
  - quote: 'New provider: ai&, an OpenAI-compatible endpoint serving open-weight models
      from Japan.'
    source_release: https://github.com/cline/cline/releases/tag/v4.1.21
  - quote: Refreshed the model catalog to 6,386 models across 209 providers. The resolved
      default model changes for 19 providers that do not pin one, 11 of them to Claude
      Opus 5.5 (including GitHub Copilot and Vertex). If you use one of those providers
      without pinning a model, expect a different default.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.21
  - quote: Canceling a request while it waits to retry an empty model response now
      takes effect right away, instead of after the backoff finishes.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.21
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: cline
  product_name: Cline
  slug: 3-model-support-changes-in-v4-1-21
  source_release: cline-2026-09-24-v4-1-21-github-395862160-2e42664e
  source_type: github_releases
  theme: model-support
  title: 3 Model Support changes in v4.1.21
  type: change
related_changes:
- '[[Changes/Recraft/2026-09-23-finally-zero-lag-in-your-workflow-recraft-v4-1-flash-generates-images-in-1-3-sec|V4.1
  Flash: The Fastest Model on the Market]]'
- '[[Changes/Superwhisper/2026-09-23-bring-your-own-key-byok-setups-now-respect-your-organization-s-cloud-model-setti|Bring-your-own-key
  (BYOK) setups now respect your organization''s cloud model settings]]'
- '[[Changes/Claude Code/2026-09-24-2-model-support-changes-in-v2-1-282|2 Model Support
  changes in v2.1.282]]'
source_release: '[[Releases/Cline/cline-2026-09-24-v4-1-21-github-395862160-2e42664e|cline-2026-09-24-v4-1-21-github-395862160-2e42664e]]'
source_type: github_releases
theme: model-support
title: 3 Model Support changes in v4.1.21
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Model Support changes in v4.1.21

**Cline** · 2026-09-24 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/cline/cline/releases/tag/v4.1.21) · from [[Releases/Cline/cline-2026-09-24-v4-1-21-github-395862160-2e42664e|v4.1.21]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> New provider: ai&, an OpenAI-compatible endpoint serving open-weight models from Japan.

> Refreshed the model catalog to 6,386 models across 209 providers. The resolved default model changes for 19 providers that do not pin one, 11 of them to Claude Opus 5.5 (including GitHub Copilot and Vertex). If you use one of those providers without pinning a model, expect a different default.

> Canceling a request while it waits to retry an empty model response now takes effect right away, instead of after the backoff finishes.

Source: https://github.com/cline/cline/releases/tag/v4.1.21
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Cline/2026-09-24-a-command-that-prints-nothing-no-longer-shows-a-raw-json-blob-like-query-git-add|A command that prints nothing no longer shows a raw JSON blob like…]] · Developer Workflow
- [[Changes/Cline/2026-09-24-on-windows-mention-search-results-now-show-the-right-file-names-nested-files-suc|On Windows, @-mention search results now show the right file names]] · Search and Browsing
- [[Changes/Cline/2026-09-24-raised-the-minimum-js-yaml-version-to-4-3-2-to-pick-up-a-security-fix-in-the-par|Raised the minimum js-yaml version to 4.3.2 to pick up a security fix in the parser…]] · Safety and Privacy
- [[Changes/Cline/2026-09-24-long-replies-on-local-models-llama-cpp-ollama-lm-studio-that-hit-the-output-toke|Long replies on local models (llama.cpp, Ollama, LM Studio) that hit…]] · Context Window
- [[Changes/Cline/2026-09-24-reopening-a-task-that-failed-now-shows-the-error-with-the-retry-option-instead-o|Reopening a task that failed now shows the error with the retry option, instead…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-09-24 · Claude Code · [[Changes/Claude Code/2026-09-24-2-model-support-changes-in-v2-1-282|2 Model Support changes in v2.1.282]]
- Later: 2026-09-25 · Claude Code · [[Changes/Claude Code/2026-09-25-3-model-support-changes-in-v2-1-283|3 Model Support changes in v2.1.283]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20cline-2026-09-24-3b3449&body=Card%3A%20Changes%2FCline%2F2026-09-24-3-model-support-changes-in-v4-1-21.md%0ACard%20ID%3A%20cline-2026-09-24-3b3449%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fcline%2Fcline%2Freleases%2Ftag%2Fv4.1.21%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->