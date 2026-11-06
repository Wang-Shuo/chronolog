---
card_id: dify-2025-11-13-0c83ad
date: '2025-11-13'
description: 'Dify · 2025-11-13 · Model Support: 5 changes in v1.10.0 - Event-Driven
  Workflows — feat: add draft trigger detection to app model and UI by @zhsama in…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1039
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2291d2504ff394013adfc76718614e1ab886e43f674a2cb6f36927856d4a9534
product: dify
product_name: Dify
record:
  card_id: dify-2025-11-13-0c83ad
  comparison: ''
  date: '2025-11-13'
  description: 'Dify — v1.10.0 - Event-Driven Workflows: 5 Model Support changes'
  evidence:
  - quote: 'feat: add draft trigger detection to app model and UI by @zhsama in https://github.com/langgenius/dify/pull/28163'
    source_release: https://github.com/langgenius/dify/releases/tag/1.10.0
  - quote: refactor:Decouple Domain Models from Direct Database Access by @hieheihei
      in https://github.com/langgenius/dify/pull/27316
    source_release: https://github.com/langgenius/dify/releases/tag/1.10.0
  - quote: 'refactor(api): add SQLAlchemy 2.x Mapped type hints to Message model by
      @laipz8200 in https://github.com/langgenius/dify/pull/27709'
    source_release: https://github.com/langgenius/dify/releases/tag/1.10.0
  - quote: 'refactor: Use Repository Pattern for Model Layer by @hieheihei in https://github.com/langgenius/dify/pull/27663'
    source_release: https://github.com/langgenius/dify/releases/tag/1.10.0
  - quote: 'chore: warning messages too long in model config caused ui issue by @iamjoel
      in https://github.com/langgenius/dify/pull/27542'
    source_release: https://github.com/langgenius/dify/releases/tag/1.10.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 5-model-support-changes-in-1-10-0
  source_release: dify-2025-11-13-1-10-0-github-262130588-ef271481
  source_type: github_releases
  theme: model-support
  title: 5 Model Support changes in 1.10.0
  type: change
related_changes:
- '[[Changes/Ollama/2025-11-12-ollama-will-now-prefer-dedicated-gpus-over-igpus-when-scheduling-models|Ollama
  will now prefer dedicated GPUs over iGPUs when scheduling models]]'
- '[[Changes/Cline/2025-11-13-8-model-support-changes-in-v3-37-0|8 Model Support changes
  in v3.37.0]]'
- '[[Changes/Codex CLI/2025-11-13-11-model-support-changes-in-rust-v0-58-0|11 Model
  Support changes in rust-v0.58.0]]'
source_release: '[[Releases/Dify/dify-2025-11-13-1-10-0-github-262130588-ef271481|dify-2025-11-13-1-10-0-github-262130588-ef271481]]'
source_type: github_releases
theme: model-support
title: 5 Model Support changes in 1.10.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Model Support changes in 1.10.0

**Dify** · 2025-11-13 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.10.0) · from [[Releases/Dify/dify-2025-11-13-1-10-0-github-262130588-ef271481|v1.10.0 - Event-Driven Workflows]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> feat: add draft trigger detection to app model and UI by @zhsama in https://github.com/langgenius/dify/pull/28163

> refactor:Decouple Domain Models from Direct Database Access by @hieheihei in https://github.com/langgenius/dify/pull/27316

> refactor(api): add SQLAlchemy 2.x Mapped type hints to Message model by @laipz8200 in https://github.com/langgenius/dify/pull/27709

> refactor: Use Repository Pattern for Model Layer by @hieheihei in https://github.com/langgenius/dify/pull/27663

> chore: warning messages too long in model config caused ui issue by @iamjoel in https://github.com/langgenius/dify/pull/27542

Source: https://github.com/langgenius/dify/releases/tag/1.10.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2025-11-13-chore-improve-the-user-experience-of-not-login-into-apps-by-iamjoel-in-https-git|chore: improve the user experience of not login into apps]] · Account and Access
- [[Changes/Dify/2025-11-13-7-apps-and-integrations-changes-in-1-10-0|7 Apps and Integrations changes in 1.10.0]] · Apps and Integrations
- [[Changes/Dify/2025-11-13-feat-add-audio-content-support-for-mcp-tools-by-ithacadream-in-https-github-com|feat: Add Audio Content Support for MCP Tools]] · Voice and Audio
- [[Changes/Dify/2025-11-13-refactor-web-reuse-the-same-edit-custom-collection-modal-component-and-fix-the-p|refactor(web): reuse the same edit-custom-collection-modal component, and fix…]] · Editor Experience
- [[Changes/Dify/2025-11-13-chore-add-type-check-to-pre-commit-by-lyzno1-in-https-github-com-langgenius-dify|chore: add type-check to pre-commit]] · Developer Workflow
- [[Changes/Dify/2025-11-13-feat-localization-for-hi-in-by-smartdever02-in-https-github-com-langgenius-dify|feat: localization for hi-IN]] · Accessibility and Localization
- [[Changes/Dify/2025-11-13-2-safety-and-privacy-changes-in-1-10-0|2 Safety and Privacy changes in 1.10.0]] · Safety and Privacy
- [[Changes/Dify/2025-11-13-these-trigger-features-are-only-available-for-workflows-chatflow-agent-and-basic|These trigger features are only available for Workflows]] · Agent Mode
- [[Changes/Dify/2025-11-13-chore-remove-unused-enterprise-bot-from-the-readme-by-crazywoola-in-https-github|chore: remove unused enterprise bot from the readme]] · Enterprise and Administration
- [[Changes/Dify/2025-11-13-2-automation-and-scheduling-changes-in-1-10-0|2 Automation and Scheduling changes in 1.10.0]] · Automation and Scheduling
- [[Changes/Dify/2025-11-13-46-other-changes-in-1-10-0|46 other changes in 1.10.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2025-11-13 · Codex CLI · [[Changes/Codex CLI/2025-11-13-11-model-support-changes-in-rust-v0-58-0|11 Model Support changes in rust-v0.58.0]]
- Later: 2025-11-13 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2025-11-13-gpt-5-1-gpt-5-1-codex-and-gpt-5-1-codex-mini-are-now-available-in-github-copilot|GPT-5.1, GPT-5.1-Codex, and GPT-5.1-Codex-Mini are now available in GitHub Copilot CLI]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2025-11-13-0c83ad&body=Card%3A%20Changes%2FDify%2F2025-11-13-5-model-support-changes-in-1-10-0.md%0ACard%20ID%3A%20dify-2025-11-13-0c83ad%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.10.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->