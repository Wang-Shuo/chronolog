---
card_id: aider-2025-03-21-181c1c
date: '2025-03-21'
description: 'Aider · 2025-03-21 · Model Support: 6 changes in Aider v0.78.0 — Added
  support for thinking tokens for OpenRouter Sonnet 3.7.'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 802
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 94eddba0accb1cf24a790db3b03b6a54ec84e719afca662d1f1bb756a90d388f
product: aider
product_name: Aider
record:
  card_id: aider-2025-03-21-181c1c
  comparison: ''
  date: '2025-03-21'
  description: 'Aider — Aider v0.78.0: 6 Model Support changes'
  evidence:
  - quote: Added support for thinking tokens for OpenRouter Sonnet 3.7.
    source_release: https://github.com/Aider-AI/aider/releases/tag/v0.78.0
  - quote: Added model setting validation to ignore `--reasoning-effort` and `--thinking-tokens`
      if the model doesn't support them.
    source_release: https://github.com/Aider-AI/aider/releases/tag/v0.78.0
  - quote: 'Added `--check-model-accepts-settings` flag (default: true) to force unsupported
      model settings.'
    source_release: https://github.com/Aider-AI/aider/releases/tag/v0.78.0
  - quote: Annotated which models support reasoning_effort and thinking_tokens settings
      in the model settings data.
    source_release: https://github.com/Aider-AI/aider/releases/tag/v0.78.0
  - quote: Added AWS_PROFILE support for Bedrock models, allowing use of AWS profiles
      instead of explicit credentials, by lentil32.
    source_release: https://github.com/Aider-AI/aider/releases/tag/v0.78.0
  - quote: Added support for `openrouter/google/gemma-3-27b-it` model.
    source_release: https://github.com/Aider-AI/aider/releases/tag/v0.78.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: aider
  product_name: Aider
  slug: 6-model-support-changes-in-v0-78-0
  source_release: aider-2025-03-21-v0-78-0-github-207521806-fc6d03b9
  source_type: github_releases
  theme: model-support
  title: 6 Model Support changes in v0.78.0
  type: change
related_changes:
- '[[Changes/Aider/2025-03-13-added-reasoning-effort-command-to-control-model-reasoning-level|Added
  /reasoning-effort command to control model reasoning level]]'
- '[[Changes/ChatGPT/2025-03-18-o1-and-o3-mini-now-offer-python-powered-data-analysis-in-chatgpt-you-can-now-ask-bfa530|o1
  and o3-mini now offer Python-powered data analysis in ChatGPT]]'
- '[[Changes/OpenHands/2025-03-18-make-microagents-available-in-the-event-stream-as-recall-observations-accessible|Make
  microagents available in the event stream as recall observations…]]'
source_release: '[[Releases/Aider/aider-2025-03-21-v0-78-0-github-207521806-fc6d03b9|aider-2025-03-21-v0-78-0-github-207521806-fc6d03b9]]'
source_type: github_releases
theme: model-support
title: 6 Model Support changes in v0.78.0
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Model Support changes in v0.78.0

**Aider** · 2025-03-21 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/Aider-AI/aider/releases/tag/v0.78.0) · from [[Releases/Aider/aider-2025-03-21-v0-78-0-github-207521806-fc6d03b9|Aider v0.78.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added support for thinking tokens for OpenRouter Sonnet 3.7.

> Added model setting validation to ignore `--reasoning-effort` and `--thinking-tokens` if the model doesn't support them.

> Added `--check-model-accepts-settings` flag (default: true) to force unsupported model settings.

> Annotated which models support reasoning_effort and thinking_tokens settings in the model settings data.

> Added AWS_PROFILE support for Bedrock models, allowing use of AWS profiles instead of explicit credentials, by lentil32.

> Added support for `openrouter/google/gemma-3-27b-it` model.

Source: https://github.com/Aider-AI/aider/releases/tag/v0.78.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Aider/2025-03-21-added-git-commit-verify-flag-default-false-to-control-whether-git-commit-hooks-a|Added --git-commit-verify flag (default]] · Apps and Integrations
- [[Changes/Aider/2025-03-21-added-commands-to-switch-between-model-types-editor-model-for-editor-model-and-w|Added commands to switch between model types]] · Editor Experience
- [[Changes/Aider/2025-03-21-3-interface-experience-changes-in-v0-78-0|3 Interface Experience changes in v0.78.0]] · Interface Experience
- [[Changes/Aider/2025-03-21-6-other-changes-in-v0-78-0|6 other changes in v0.78.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2025-03-18 · OpenHands · [[Changes/OpenHands/2025-03-18-make-microagents-available-in-the-event-stream-as-recall-observations-accessible|Make microagents available in the event stream as recall observations…]]
- Later: 2025-03-23 · Cursor · [[Changes/Cursor/2025-03-23-2-model-support-changes-in-0-48-x|2 Model Support changes in 0.48.x]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20aider-2025-03-21-181c1c&body=Card%3A%20Changes%2FAider%2F2025-03-21-6-model-support-changes-in-v0-78-0.md%0ACard%20ID%3A%20aider-2025-03-21-181c1c%0ASource%3A%20https%3A%2F%2Fgithub.com%2FAider-AI%2Faider%2Freleases%2Ftag%2Fv0.78.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->