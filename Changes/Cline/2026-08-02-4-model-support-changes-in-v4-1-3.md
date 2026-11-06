---
card_id: cline-2026-08-02-dbfb79
date: '2026-08-02'
description: 'Cline · 2026-08-02 · Model Support: 4 changes in v4.1.3 — Fall back
  to the default Cline model when migrating a setup that references a model id the
  new…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1301
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a74a5282128b4f7489144f2a897c63720c4d55d38ff1fe5b7d1870b7e3074faa
product: cline
product_name: Cline
record:
  card_id: cline-2026-08-02-dbfb79
  comparison: ''
  date: '2026-08-02'
  description: 'Cline — v4.1.3: 4 Model Support changes'
  evidence:
  - quote: Fall back to the default Cline model when migrating a setup that references
      a model id the new extension doesn't recognize, instead of leaving the provider
      unconfigured.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.3
  - quote: Retry empty Ollama responses at the model boundary, and raise the response-start
      timeout to 5 minutes so cold model loads no longer error out.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.3
  - quote: Show proper display names for Cline free models and recommended models
      in the model picker.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.3
  - quote: Preserve video input capability for models that support it.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.3
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: cline
  product_name: Cline
  slug: 4-model-support-changes-in-v4-1-3
  source_release: cline-2026-08-02-v4-1-3-github-363709138-84b1555e
  source_type: github_releases
  theme: model-support
  title: 4 Model Support changes in v4.1.3
  type: change
related_changes:
- '[[Changes/Lovable/2026-07-31-opt-out-of-ai-model-training|Opt out of AI model training]]'
- '[[Changes/Replit/2026-07-31-choose-agent-s-primary-model|Choose Agent''s primary
  model]]'
- '[[Changes/v0/2026-07-31-3-model-support-changes-in-claude-opus-5-direct-figma-inspection|3
  Model Support changes in Claude Opus 5, direct Figma inspection…]]'
source_release: '[[Releases/Cline/cline-2026-08-02-v4-1-3-github-363709138-84b1555e|cline-2026-08-02-v4-1-3-github-363709138-84b1555e]]'
source_type: github_releases
theme: model-support
title: 4 Model Support changes in v4.1.3
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Model Support changes in v4.1.3

**Cline** · 2026-08-02 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/cline/cline/releases/tag/v4.1.3) · from [[Releases/Cline/cline-2026-08-02-v4-1-3-github-363709138-84b1555e|v4.1.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Fall back to the default Cline model when migrating a setup that references a model id the new extension doesn't recognize, instead of leaving the provider unconfigured.

> Retry empty Ollama responses at the model boundary, and raise the response-start timeout to 5 minutes so cold model loads no longer error out.

> Show proper display names for Cline free models and recommended models in the model picker.

> Preserve video input capability for models that support it.

Source: https://github.com/cline/cline/releases/tag/v4.1.3
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Cline/2026-08-02-2-developer-workflow-changes-in-v4-1-3|2 Developer Workflow changes in v4.1.3]] · Developer Workflow
- [[Changes/Cline/2026-08-02-keep-settings-edits-that-are-made-before-the-provider-config-finishes-loading-ba|Keep settings edits that are made before the provider config finishes loading]] · Editor Experience
- [[Changes/Cline/2026-08-02-stop-the-two-bundles-of-the-combined-rollout-package-from-invalidating-each-othe|Stop the two bundles of the combined rollout package from invalidating each other's…]] · Collaboration
- [[Changes/Cline/2026-08-02-8-other-changes-in-v4-1-3|8 other changes in v4.1.3]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-07-31 · v0 · [[Changes/v0/2026-07-31-3-model-support-changes-in-claude-opus-5-direct-figma-inspection|3 Model Support changes in Claude Opus 5, direct Figma inspection…]]
- Later: 2026-08-03 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-08-03-the-allow-all-auto-safety-judge-model-is-no-longer-user-configurable-the-judge-m|The /allow-all auto safety-judge model is no longer user-configurable]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20cline-2026-08-02-dbfb79&body=Card%3A%20Changes%2FCline%2F2026-08-02-4-model-support-changes-in-v4-1-3.md%0ACard%20ID%3A%20cline-2026-08-02-dbfb79%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fcline%2Fcline%2Freleases%2Ftag%2Fv4.1.3%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->