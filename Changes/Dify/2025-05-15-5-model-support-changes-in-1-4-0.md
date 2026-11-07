---
card_id: dify-2025-05-15-d3dbb8
date: '2025-05-15'
description: 'Dify · 2025-05-15 · Model Support: 5 changes in v1.4.0 — Our platform
  now supports multimodal outputs, allowing LLMs to handle both text and images within
  the…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 857
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 83f0213e298a49499d3d4500b226b86f33f6d9d1ac14378d6e62334a9964762f
product: dify
product_name: Dify
record:
  card_id: dify-2025-05-15-d3dbb8
  comparison: ''
  date: '2025-05-15'
  description: 'Dify — v1.4.0: 5 Model Support changes'
  evidence:
  - quote: 'Our platform now supports multimodal outputs, allowing LLMs to handle
      both text and images within the LLMNode. This feature enhances the richness
      of data interaction and boosts your model''s capabilities, courtesy of @QuantumGhost''s
      efforts in PR #17372. You can now try these new features using the Gemini 2.0
      Flash Exp model! This integration ensures that your AI can process and respond
      with both text and visual data seamlessly.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.4.0
  - quote: 'refactor(models): Use the SQLAlchemy base model. by @laipz8200 in https://github.com/langgenius/dify/pull/19435'
    source_release: https://github.com/langgenius/dify/releases/tag/1.4.0
  - quote: 'chore: all model.query replace to db.session.query by @hjlarry in https://github.com/langgenius/dify/pull/19521'
    source_release: https://github.com/langgenius/dify/releases/tag/1.4.0
  - quote: correct key to 'embedding_model_provider' in docs by @osaimi in https://github.com/langgenius/dify/pull/19541
    source_release: https://github.com/langgenius/dify/releases/tag/1.4.0
  - quote: 'chore: model.query change to db.session.query by @hjlarry in https://github.com/langgenius/dify/pull/19551'
    source_release: https://github.com/langgenius/dify/releases/tag/1.4.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 5-model-support-changes-in-1-4-0
  source_release: dify-2025-05-15-1-4-0-github-218877198-a895b1ee
  source_type: github_releases
  theme: model-support
  title: 5 Model Support changes in 1.4.0
  type: change
related_changes:
- '[[Changes/ChatGPT/2025-05-14-gpt-4-1-mini-is-a-fast-capable-and-efficient-small-model-delivering-significant-722b7d|Introducing
  GPT-4.1 mini, replacing GPT-4o mini, in ChatGPT for all users]]'
- '[[Changes/Cline/2025-05-14-2-model-support-changes-in-v3-15-4|2 Model Support changes
  in v3.15.4]]'
- '[[Changes/Cursor/2025-05-15-max-mode-for-all-top-models|Max Mode for all top models]]'
source_release: '[[Releases/Dify/dify-2025-05-15-1-4-0-github-218877198-a895b1ee|dify-2025-05-15-1-4-0-github-218877198-a895b1ee]]'
source_type: github_releases
theme: model-support
title: 5 Model Support changes in 1.4.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Model Support changes in 1.4.0

**Dify** · 2025-05-15 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.4.0) · from [[Releases/Dify/dify-2025-05-15-1-4-0-github-218877198-a895b1ee|v1.4.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Our platform now supports multimodal outputs, allowing LLMs to handle both text and images within the LLMNode. This feature enhances the richness of data interaction and boosts your model's capabilities, courtesy of @QuantumGhost's efforts in PR #17372. You can now try these new features using the Gemini 2.0 Flash Exp model! This integration ensures that your AI can process and respond with both text and visual data seamlessly.

> refactor(models): Use the SQLAlchemy base model. by @laipz8200 in https://github.com/langgenius/dify/pull/19435

> chore: all model.query replace to db.session.query by @hjlarry in https://github.com/langgenius/dify/pull/19521

> correct key to 'embedding_model_provider' in docs by @osaimi in https://github.com/langgenius/dify/pull/19541

> chore: model.query change to db.session.query by @hjlarry in https://github.com/langgenius/dify/pull/19551

Source: https://github.com/langgenius/dify/releases/tag/1.4.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2025-05-15-2-interface-experience-changes-in-1-4-0|2 Interface Experience changes in 1.4.0]] · Interface Experience
- [[Changes/Dify/2025-05-15-add-accept-ranges-header-for-audio-video-files-by-sondin-in-https-github-com-lan|add Accept-Ranges header for audio/video files]] · Voice and Audio
- [[Changes/Dify/2025-05-15-chore-upgrade-package-version-to-fix-security-issue-by-iamjoel-in-https-github-c|chore: upgrade package version to fix security issue]] · Safety and Privacy
- [[Changes/Dify/2025-05-15-chore-avoid-repeated-type-ignore-noqa-by-adding-flask-restful-and-flask-login-in|chore: avoid repeated type ignore noqa by adding flask_restful and flask_login…]] · Account and Access
- [[Changes/Dify/2025-05-15-feat-api-add-image-multimodal-support-for-llmnode-by-quantumghost-in-https-githu|feat(api): Add image multimodal support for LLMNode]] · Multimodal Input
- [[Changes/Dify/2025-05-15-ci-add-diff-to-lint-ci-by-yihong0618-in-https-github-com-langgenius-dify-pull-17|ci: add diff to lint ci]] · Editor Experience
- [[Changes/Dify/2025-05-15-imagine-if-every-idea-could-become-an-ai-agent-with-dify-if-you-can-ask-it-you-c|Imagine if every idea could become an AI agent]] · Agent Mode
- [[Changes/Dify/2025-05-15-3-reliability-and-performance-changes-in-1-4-0|3 Reliability and Performance changes in 1.4.0]] · Reliability and Performance
- [[Changes/Dify/2025-05-15-5-apps-and-integrations-changes-in-1-4-0|5 Apps and Integrations changes in 1.4.0]] · Apps and Integrations
- [[Changes/Dify/2025-05-15-refactor-workflow-revamp-logging-module-for-loop-iteration-nodes-by-auxpd-in-htt|refactor(workflow): revamp logging module for loop & iteration nodes]] · Automation and Scheduling
- [[Changes/Dify/2025-05-15-72-other-changes-in-1-4-0|72 other changes in 1.4.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2025-05-15 · Cursor · [[Changes/Cursor/2025-05-15-max-mode-for-all-top-models|Max Mode for all top models]]
- Later: 2025-05-15 · Windsurf · [[Changes/Windsurf/2025-05-15-swe-1|SWE-1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2025-05-15-d3dbb8&body=Card%3A%20Changes%2FDify%2F2025-05-15-5-model-support-changes-in-1-4-0.md%0ACard%20ID%3A%20dify-2025-05-15-d3dbb8%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.4.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->