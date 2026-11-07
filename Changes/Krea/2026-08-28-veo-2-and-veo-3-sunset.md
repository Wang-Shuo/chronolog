---
card_id: krea-2026-08-28-664157
date: '2026-08-28'
description: 'Krea · 2026-08-28 · Model Support: **Veo 2 and Veo 3 are sunset as of
  August 28, 2026.** Both models no longer appear in the Video tool''s model picker,
  and…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1327
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: policy
machine_hash: 8d2dbbdcea343750af3c94c8ea785dac73536a9a875c9537ebd99abd41e039d2
product: krea
product_name: Krea
record:
  ai_generated: true
  card_id: krea-2026-08-28-664157
  comparison: ''
  confidence: low
  date: '2026-08-28'
  description: 'Krea — Wan 3.0 in the Video tool, plus the Veo 2 and Veo 3 sunset:
    **Veo 2 and Veo 3 are sunset as of August 28, 2026.** Both models no longer appear
    in the Video tool''s model picker, and their API endpoints are deprecated.'
  evidence:
  - quote: '**Veo 2 and Veo 3 are sunset as of August 28, 2026.** Both models no longer
      appear in the Video tool''s model picker, and their API endpoints are deprecated.'
    source_release: https://www.krea.ai/docs/changelog
  - quote: Requests to a deprecated endpoint return `Deprecation` and `Sunset` headers
      before the sunset date. After it, they return `410 Gone`.
    source_release: https://www.krea.ai/docs/changelog
  - quote: Veo 3.1 and Veo 3.1 Lite remain available and are the closest replacements.
    source_release: https://www.krea.ai/docs/changelog
  extractor_version: fallback-v5
  impact: significant
  kind: policy
  product: krea
  product_name: Krea
  slug: veo-2-and-veo-3-sunset
  source_release: krea-2026-08-28-2026-08-28-wan-3-0-in-the-video-tool-plus-the-veo-2-and-veo-3-su-97dd9c72
  source_type: krea_changelog
  theme: model-support
  theme_matches:
  - matched_terms:
    - model
    - models
    score: 100
    theme: model-support
  - matched_terms:
    - picker
    score: 50
    theme: interface-experience
  title: Veo 2 and Veo 3 sunset
  type: change
related_changes:
- '[[Changes/Qoder/2026-08-27-added-original-and-discounted-usage-multipliers-to-the-model-menu|Added
  original and discounted usage multipliers to the model menu]]'
- '[[Changes/Qoder/2026-08-27-frontier-models-smart-routing-qoder-brings-together-leading-models-without-locki|Frontier
  models, smart routing]]'
- '[[Changes/Claude Code/2026-08-28-5-model-support-changes-in-v2-1-251|5 Model Support
  changes in v2.1.251]]'
source_release: '[[Releases/Krea/krea-2026-08-28-2026-08-28-wan-3-0-in-the-video-tool-plus-the-veo-2-and-veo-3-su-97dd9c72|krea-2026-08-28-2026-08-28-wan-3-0-in-the-video-tool-plus-the-veo-2-and-veo-3-su-97dd9c72]]'
source_type: krea_changelog
theme: model-support
title: Veo 2 and Veo 3 sunset
type: change
---

<!-- chronolog:begin region="header" -->
# Veo 2 and Veo 3 sunset

**Krea** · 2026-08-28 · [[Themes/model-support|Model Support]] · Policy · [Official source](https://www.krea.ai/docs/changelog) · from [[Releases/Krea/krea-2026-08-28-2026-08-28-wan-3-0-in-the-video-tool-plus-the-veo-2-and-veo-3-su-97dd9c72|Wan 3.0 in the Video tool, plus the Veo 2 and Veo 3 sunset]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **Veo 2 and Veo 3 are sunset as of August 28, 2026.** Both models no longer appear in the Video tool's model picker, and their API endpoints are deprecated.
>
> Requests to a deprecated endpoint return `Deprecation` and `Sunset` headers before the sunset date. After it, they return `410 Gone`.
>
> Veo 3.1 and Veo 3.1 Lite remain available and are the closest replacements.
>
> Source: https://www.krea.ai/docs/changelog
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Krea/2026-08-28-wan-3-0|Wan 3.0]] · Voice and Audio
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-08-28 · Claude Code · [[Changes/Claude Code/2026-08-28-5-model-support-changes-in-v2-1-251|5 Model Support changes in v2.1.251]]
- Later: 2026-08-28 · OpenCode · [[Changes/OpenCode/2026-08-28-core-bedrock-reasoning-responses-no-longer-get-cached-into-unreplayable-empty-me|Core Bedrock reasoning responses no longer get cached into unreplayable empty messages]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20krea-2026-08-28-664157&body=Card%3A%20Changes%2FKrea%2F2026-08-28-veo-2-and-veo-3-sunset.md%0ACard%20ID%3A%20krea-2026-08-28-664157%0ASource%3A%20https%3A%2F%2Fwww.krea.ai%2Fdocs%2Fchangelog%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->