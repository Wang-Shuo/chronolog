---
card_id: aider-2025-05-09-f81bfe
date: '2025-05-09'
description: 'Aider · 2025-05-09 · Model Support: 12 changes in Aider v0.83.0 — Added
  support for `gemini-2.5-pro-preview-05-06` models.'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 851
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 4ecc4700c1edf15bb5485457d82cb8b3dee85257de4a6bdfc452b8263c08392f
product: aider
product_name: Aider
record:
  card_id: aider-2025-05-09-f81bfe
  comparison: ''
  date: '2025-05-09'
  description: 'Aider — Aider v0.83.0: 12 Model Support changes'
  evidence:
  - quote: Added support for `gemini-2.5-pro-preview-05-06` models.
    source_release: https://github.com/Aider-AI/aider/releases/tag/v0.83.0
  - quote: Added support for `qwen3-235b` models.
    source_release: https://github.com/Aider-AI/aider/releases/tag/v0.83.0
  - quote: Added a spinner animation while waiting for the LLM to start streaming
      its response.
    source_release: https://github.com/Aider-AI/aider/releases/tag/v0.83.0
  - quote: Updated Gemini model aliases (e.g., `gemini`, `gemini-2.5-pro`) to point
      to the `05-06` preview versions.
    source_release: https://github.com/Aider-AI/aider/releases/tag/v0.83.0
  - quote: Marked Gemini 2.5 Pro preview models as `overeager` by default.
    source_release: https://github.com/Aider-AI/aider/releases/tag/v0.83.0
  - quote: Updated the default weak model for Gemini 2.5 Pro models to `gemini/gemini-2.5-flash-preview-04-17`.
    source_release: https://github.com/Aider-AI/aider/releases/tag/v0.83.0
  - quote: Corrected `gemini-2.5-pro-exp-03-25` model settings to reflect its lack
      of support for `thinking_budget`.
    source_release: https://github.com/Aider-AI/aider/releases/tag/v0.83.0
  - quote: Ensured model-specific system prompt prefixes are placed on a new line
      before the main system prompt.
    source_release: https://github.com/Aider-AI/aider/releases/tag/v0.83.0
  - quote: Enabled support for `thinking_tokens` and `reasoning_effort` parameters
      for OpenRouter models.
    source_release: https://github.com/Aider-AI/aider/releases/tag/v0.83.0
  - quote: Added model settings for `openrouter/google/gemini-2.5-pro-preview-03-25`.
    source_release: https://github.com/Aider-AI/aider/releases/tag/v0.83.0
  - quote: Improved `/ask` mode to instruct the LLM to elide unchanging code in its
      responses.
    source_release: https://github.com/Aider-AI/aider/releases/tag/v0.83.0
  - quote: Enabled `reasoning_effort` for Gemini 2.5 Flash models.
    source_release: https://github.com/Aider-AI/aider/releases/tag/v0.83.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: aider
  product_name: Aider
  slug: 12-model-support-changes-in-v0-83-0
  source_release: aider-2025-05-09-v0-83-0-github-217725361-c9b2b84c
  source_type: github_releases
  theme: model-support
  title: 12 Model Support changes in v0.83.0
  type: change
related_changes:
- '[[Changes/Gemini/2025-05-06-2-5-pro-experimental-got-a-major-upgrade-for-coding|2.5
  Pro (experimental) got a major upgrade for coding]]'
- "[[Changes/Open WebUI/2025-05-06-automatic1111-image-model-setting-applied-properly-fixed-an-issue-where-switchin|\U0001F3A8
  Automatic1111 Image Model Setting Applied Properly]]"
- '[[Changes/Windsurf/2025-05-07-cascade-ux-improvements|Cascade UX Improvements]]'
source_release: '[[Releases/Aider/aider-2025-05-09-v0-83-0-github-217725361-c9b2b84c|aider-2025-05-09-v0-83-0-github-217725361-c9b2b84c]]'
source_type: github_releases
theme: model-support
title: 12 Model Support changes in v0.83.0
type: change
---

<!-- chronolog:begin region="header" -->
# 12 Model Support changes in v0.83.0

**Aider** · 2025-05-09 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/Aider-AI/aider/releases/tag/v0.83.0) · from [[Releases/Aider/aider-2025-05-09-v0-83-0-github-217725361-c9b2b84c|Aider v0.83.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added support for `gemini-2.5-pro-preview-05-06` models.

> Added support for `qwen3-235b` models.

> Added a spinner animation while waiting for the LLM to start streaming its response.

> Updated Gemini model aliases (e.g., `gemini`, `gemini-2.5-pro`) to point to the `05-06` preview versions.

> Marked Gemini 2.5 Pro preview models as `overeager` by default.

> Updated the default weak model for Gemini 2.5 Pro models to `gemini/gemini-2.5-flash-preview-04-17`.

> Corrected `gemini-2.5-pro-exp-03-25` model settings to reflect its lack of support for `thinking_budget`.

> Ensured model-specific system prompt prefixes are placed on a new line before the main system prompt.

> Enabled support for `thinking_tokens` and `reasoning_effort` parameters for OpenRouter models.

> Added model settings for `openrouter/google/gemini-2.5-pro-preview-03-25`.

> Improved `/ask` mode to instruct the LLM to elide unchanging code in its responses.

> Enabled `reasoning_effort` for Gemini 2.5 Flash models.

Source: https://github.com/Aider-AI/aider/releases/tag/v0.83.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Aider/2025-05-09-2-editor-experience-changes-in-v0-83-0|2 Editor Experience changes in v0.83.0]] · Editor Experience
- [[Changes/Aider/2025-05-09-5-developer-workflow-changes-in-v0-83-0|5 Developer Workflow changes in v0.83.0]] · Developer Workflow
- [[Changes/Aider/2025-05-09-2-context-window-changes-in-v0-83-0|2 Context Window changes in v0.83.0]] · Context Window
- [[Changes/Aider/2025-05-09-3-interface-experience-changes-in-v0-83-0|3 Interface Experience changes in v0.83.0]] · Interface Experience
- [[Changes/Aider/2025-05-09-9-other-changes-in-v0-83-0|9 other changes in v0.83.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2025-05-07 · Windsurf · [[Changes/Windsurf/2025-05-07-cascade-ux-improvements|Cascade UX Improvements]]
- Later: 2025-05-10 · Cline · [[Changes/Cline/2025-05-10-7-model-support-changes-in-v3-15-0|7 Model Support changes in v3.15.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20aider-2025-05-09-f81bfe&body=Card%3A%20Changes%2FAider%2F2025-05-09-12-model-support-changes-in-v0-83-0.md%0ACard%20ID%3A%20aider-2025-05-09-f81bfe%0ASource%3A%20https%3A%2F%2Fgithub.com%2FAider-AI%2Faider%2Freleases%2Ftag%2Fv0.83.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->