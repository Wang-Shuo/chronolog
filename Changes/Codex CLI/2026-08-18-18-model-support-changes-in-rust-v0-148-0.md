---
card_id: codex-cli-2026-08-18-0ca906
date: '2026-08-18'
description: 'Codex CLI · 2026-08-18 · Model Support: 18 changes in 0.148.0 — Use
  Amazon Bedrock Runtime as a built-in provider with AWS profile, region, and GPT-5.6
  routing…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1317
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 663dc1b1137909493b01915116eb65edb0da20f9ad8f97e83ec1d0f5bd668442
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-08-18-0ca906
  comparison: ''
  date: '2026-08-18'
  description: 'Codex CLI — 0.148.0: 18 Model Support changes'
  evidence:
  - quote: Use Amazon Bedrock Runtime as a built-in provider with AWS profile, region,
      and GPT-5.6 routing support. (#38470)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: 'Model switches and settings updates no longer leave stale instructions
      behind or change an active turn midstream. (#37260, #38785)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37190 Interrupt cyber model turns after one Guardian denial @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37260 Fix first-turn model switching and rollback @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37345 Send model routing hints to the Codex backend @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37511 Enforce automatic review for managed models @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37516 Ignore reusable command approvals for cyber models @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37807 Share model-visible tool specs across prompts @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38045 Store model history in response item envelopes @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38251 Read model ETags from WebSocket metadata events @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38432 Gate Node REPL Guardian guidance on model metadata @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38439 Preserve approval policies for auto-reviewed models @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38449 Expose model upgrade retirement times @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38467 Parse model annotations from skill frontmatter @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38475 Add bounded skill model delegation instructions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38499 Enable parallel tool calls for all model prompts @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38617 Prioritize global models in the Bedrock Runtime catalog @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38785 Keep active-turn model settings stable across updates @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 18-model-support-changes-in-rust-v0-148-0
  source_release: codex-cli-2026-08-18-rust-v0-148-0-github-372686337-4265c0ae
  source_type: github_releases
  theme: model-support
  title: 18 Model Support changes in rust-v0.148.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-08-14-update-model-configurations|Update model
  configurations]]'
- '[[Changes/Claude Code/2026-08-17-2-model-support-changes-in-v2-1-234|2 Model Support
  changes in v2.1.234]]'
- '[[Changes/OpenHands/2026-08-17-feat-add-llm-pre-flight-validation-to-prevent-saving-misconfigured-profiles-by-n|feat:
  add LLM pre-flight validation to prevent saving misconfigured profiles]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-08-18-rust-v0-148-0-github-372686337-4265c0ae|codex-cli-2026-08-18-rust-v0-148-0-github-372686337-4265c0ae]]'
source_type: github_releases
theme: model-support
title: 18 Model Support changes in rust-v0.148.0
type: change
---

<!-- chronolog:begin region="header" -->
# 18 Model Support changes in rust-v0.148.0

**Codex CLI** · 2026-08-18 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.148.0) · from [[Releases/Codex CLI/codex-cli-2026-08-18-rust-v0-148-0-github-372686337-4265c0ae|0.148.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Use Amazon Bedrock Runtime as a built-in provider with AWS profile, region, and GPT-5.6 routing support. (#38470)

> Model switches and settings updates no longer leave stale instructions behind or change an active turn midstream. (#37260, #38785)

> #37190 Interrupt cyber model turns after one Guardian denial @copyberry

> #37260 Fix first-turn model switching and rollback @copyberry

> #37345 Send model routing hints to the Codex backend @copyberry

> #37511 Enforce automatic review for managed models @copyberry

> #37516 Ignore reusable command approvals for cyber models @copyberry

> #37807 Share model-visible tool specs across prompts @copyberry

> #38045 Store model history in response item envelopes @copyberry

> #38251 Read model ETags from WebSocket metadata events @copyberry

> #38432 Gate Node REPL Guardian guidance on model metadata @copyberry

> #38439 Preserve approval policies for auto-reviewed models @copyberry

> #38449 Expose model upgrade retirement times @copyberry

> #38467 Parse model annotations from skill frontmatter @copyberry

> #38475 Add bounded skill model delegation instructions @copyberry

> #38499 Enable parallel tool calls for all model prompts @copyberry

> #38617 Prioritize global models in the Bedrock Runtime catalog @copyberry

> #38785 Keep active-turn model settings stable across updates @copyberry

Source: https://github.com/openai/codex/releases/tag/rust-v0.148.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-08-18-57-apps-and-integrations-changes-in-rust-v0-148-0|57 Apps and Integrations changes in rust-v0.148.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-08-18-13-interface-experience-changes-in-rust-v0-148-0|13 Interface Experience changes in rust-v0.148.0]] · Interface Experience
- [[Changes/Codex CLI/2026-08-18-3-mobile-and-desktop-changes-in-rust-v0-148-0|3 Mobile and Desktop changes in rust-v0.148.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-08-18-5-developer-workflow-changes-in-rust-v0-148-0|5 Developer Workflow changes in rust-v0.148.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-08-18-38650-canonicalize-default-namespaces-in-grpc-subscription-filters-copyberry|♯38650 Canonicalize default namespaces in gRPC subscription filters @copyberry]] · Pricing Model
- [[Changes/Codex CLI/2026-08-18-37828-track-running-unified-exec-processes-at-turn-completion-copyberry|♯37828 Track running unified exec processes at turn completion @copyberry]] · Editor Experience
- [[Changes/Codex CLI/2026-08-18-17-safety-and-privacy-changes-in-rust-v0-148-0|17 Safety and Privacy changes in rust-v0.148.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-08-18-16-account-and-access-changes-in-rust-v0-148-0|16 Account and Access changes in rust-v0.148.0]] · Account and Access
- [[Changes/Codex CLI/2026-08-18-13-context-window-changes-in-rust-v0-148-0|13 Context Window changes in rust-v0.148.0]] · Context Window
- [[Changes/Codex CLI/2026-08-18-12-agent-mode-changes-in-rust-v0-148-0|12 Agent Mode changes in rust-v0.148.0]] · Agent Mode
- [[Changes/Codex CLI/2026-08-18-38024-expose-image-generation-usage-limit-failures-copyberry|♯38024 Expose image generation usage-limit failures @copyberry]] · Image Generation
- [[Changes/Codex CLI/2026-08-18-5-collaboration-changes-in-rust-v0-148-0|5 Collaboration changes in rust-v0.148.0]] · Collaboration
- [[Changes/Codex CLI/2026-08-18-231-other-changes-in-rust-v0-148-0|231 other changes in rust-v0.148.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-08-17 · OpenHands · [[Changes/OpenHands/2026-08-17-feat-add-llm-pre-flight-validation-to-prevent-saving-misconfigured-profiles-by-n|feat: add LLM pre-flight validation to prevent saving misconfigured profiles]]
- Later: 2026-08-19 · Claude Code · [[Changes/Claude Code/2026-08-19-added-anthropic-default-model-environment-variable-sets-the-model-new-sessions-s|Added ANTHROPIC_DEFAULT_MODEL environment variable]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-08-18-0ca906&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-08-18-18-model-support-changes-in-rust-v0-148-0.md%0ACard%20ID%3A%20codex-cli-2026-08-18-0ca906%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.148.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->