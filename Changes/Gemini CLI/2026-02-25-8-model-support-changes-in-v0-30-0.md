---
card_id: gemini-cli-2026-02-25-17c466
date: '2026-02-25'
description: 'Gemini CLI · 2026-02-25 · Model Support: 8 changes in Release v0.30.0
  — feat(core): update internal utility models to Gemini 3 by @SandyTao520 in…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1143
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d5da6cfa6c4259e7e91f904b9b8bb89be1f8be94e6cc9e8a7859a5079a74ba5f
product: gemini-cli
product_name: Gemini CLI
record:
  card_id: gemini-cli-2026-02-25-17c466
  comparison: ''
  date: '2026-02-25'
  description: 'Gemini CLI — Release v0.30.0: 8 Model Support changes'
  evidence:
  - quote: 'feat(core): update internal utility models to Gemini 3 by @SandyTao520
      in https://github.com/google-gemini/gemini-cli/pull/18773'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.30.0
  - quote: 'feat(core): fallback to chat-base when using unrecognized models for chat
      by @SandyTao520 in https://github.com/google-gemini/gemini-cli/pull/19016'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.30.0
  - quote: 'refactor: use `CoreToolCallStatus` in the the history data model by @jerop
      in https://github.com/google-gemini/gemini-cli/pull/19033'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.30.0
  - quote: 'feat(cli): handle invalid model names in useQuotaAndFallback by @sehoon38
      in https://github.com/google-gemini/gemini-cli/pull/19222'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.30.0
  - quote: 'feat(cli): refactor model command to support set and manage subcommands
      by @sehoon38 in https://github.com/google-gemini/gemini-cli/pull/19221'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.30.0
  - quote: 'chore(ui): remove outdated tip about model routing by @sehoon38 in https://github.com/google-gemini/gemini-cli/pull/19226'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.30.0
  - quote: 'feat(core): support custom reasoning models by default by @NTaylorMullen
      in https://github.com/google-gemini/gemini-cli/pull/19227'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.30.0
  - quote: 'refactor(core): modularize tool definitions by model family by @aishaneeshah
      in https://github.com/google-gemini/gemini-cli/pull/19269'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.30.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: gemini-cli
  product_name: Gemini CLI
  slug: 8-model-support-changes-in-v0-30-0
  source_release: gemini-cli-2026-02-25-v0-30-0-github-290144121-620926b3
  source_type: github_releases
  theme: model-support
  title: 8 Model Support changes in v0.30.0
  type: change
related_changes:
- '[[Changes/Microsoft 365 Copilot/2026-02-24-declarative-agents-upgraded-to-gpt-5-1-microsoft-365-copilot-extensibility|Declarative
  agents upgraded to GPT-5.1 (Microsoft 365 Copilot extensibility)]]'
- '[[Changes/Ollama/2026-02-24-2-model-support-changes-in-v0-17-1|2 Model Support
  changes in v0.17.1]]'
- '[[Changes/Codex CLI/2026-02-25-6-model-support-changes-in-rust-v0-105-0|6 Model
  Support changes in rust-v0.105.0]]'
source_release: '[[Releases/Gemini CLI/gemini-cli-2026-02-25-v0-30-0-github-290144121-620926b3|gemini-cli-2026-02-25-v0-30-0-github-290144121-620926b3]]'
source_type: github_releases
theme: model-support
title: 8 Model Support changes in v0.30.0
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Model Support changes in v0.30.0

**Gemini CLI** · 2026-02-25 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/google-gemini/gemini-cli/releases/tag/v0.30.0) · from [[Releases/Gemini CLI/gemini-cli-2026-02-25-v0-30-0-github-290144121-620926b3|Release v0.30.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> feat(core): update internal utility models to Gemini 3 by @SandyTao520 in https://github.com/google-gemini/gemini-cli/pull/18773

> feat(core): fallback to chat-base when using unrecognized models for chat by @SandyTao520 in https://github.com/google-gemini/gemini-cli/pull/19016

> refactor: use `CoreToolCallStatus` in the the history data model by @jerop in https://github.com/google-gemini/gemini-cli/pull/19033

> feat(cli): handle invalid model names in useQuotaAndFallback by @sehoon38 in https://github.com/google-gemini/gemini-cli/pull/19222

> feat(cli): refactor model command to support set and manage subcommands by @sehoon38 in https://github.com/google-gemini/gemini-cli/pull/19221

> chore(ui): remove outdated tip about model routing by @sehoon38 in https://github.com/google-gemini/gemini-cli/pull/19226

> feat(core): support custom reasoning models by default by @NTaylorMullen in https://github.com/google-gemini/gemini-cli/pull/19227

> refactor(core): modularize tool definitions by model family by @aishaneeshah in https://github.com/google-gemini/gemini-cli/pull/19269

Source: https://github.com/google-gemini/gemini-cli/releases/tag/v0.30.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Gemini CLI/2026-02-25-feat-plan-document-and-validate-plan-mode-policy-overrides-by-jerop-in-https-git|feat(plan): document and validate Plan Mode policy overrides]] · Files and Data
- [[Changes/Gemini CLI/2026-02-25-2-context-window-changes-in-v0-30-0|2 Context Window changes in v0.30.0]] · Context Window
- [[Changes/Gemini CLI/2026-02-25-enable-in-cli-extension-management-commands-for-team-by-chrstnb-in-https-github|Enable in-CLI extension management commands for team]] · Collaboration
- [[Changes/Gemini CLI/2026-02-25-test-evals-mark-all-save-memory-evals-as-usually-passes-due-to-unreliability-by|test(evals): mark all save_memory evals as USUALLY_PASSES due to unreliability]] · Memory and Personalization
- [[Changes/Gemini CLI/2026-02-25-8-apps-and-integrations-changes-in-v0-30-0|8 Apps and Integrations changes in v0.30.0]] · Apps and Integrations
- [[Changes/Gemini CLI/2026-02-25-refactor-core-adopt-coretoolcallstatus-enum-for-type-safety-by-jerop-in-https-gi|refactor(core): adopt CoreToolCallStatus enum for type safety]] · Safety and Privacy
- [[Changes/Gemini CLI/2026-02-25-perf-ui-optimize-table-rendering-by-memoizing-styled-characters-by-devr0306-in-h|perf(ui): optimize table rendering by memoizing styled characters]] · Interface Experience
- [[Changes/Gemini CLI/2026-02-25-3-developer-workflow-changes-in-v0-30-0|3 Developer Workflow changes in v0.30.0]] · Developer Workflow
- [[Changes/Gemini CLI/2026-02-25-4-agent-mode-changes-in-v0-30-0|4 Agent Mode changes in v0.30.0]] · Agent Mode
- [[Changes/Gemini CLI/2026-02-25-feat-plan-hide-plan-write-and-edit-operations-on-plans-in-plan-mode-by-jerop-in|feat(plan): hide plan write and edit operations on plans in Plan Mode]] · Editor Experience
- [[Changes/Gemini CLI/2026-02-25-feat-admin-add-admin-controls-documentation-by-skeshive-in-https-github-com-goog|feat(admin): Add admin controls documentation]] · Enterprise and Administration
- [[Changes/Gemini CLI/2026-02-25-2-reliability-and-performance-changes-in-v0-30-0|2 Reliability and Performance changes in v0.30.0]] · Reliability and Performance
- [[Changes/Gemini CLI/2026-02-25-introduce-limits-for-search-results-by-gundermanc-in-https-github-com-google-gem|Introduce limits for search results]] · Search and Browsing
- [[Changes/Gemini CLI/2026-02-25-53-other-changes-in-v0-30-0|53 other changes in v0.30.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-02-25 · Codex CLI · [[Changes/Codex CLI/2026-02-25-6-model-support-changes-in-rust-v0-105-0|6 Model Support changes in rust-v0.105.0]]
- Later: 2026-02-25 · Windsurf · [[Changes/Windsurf/2026-02-25-new-model-picker|New Model Picker]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20gemini-cli-2026-02-25-17c466&body=Card%3A%20Changes%2FGemini%20CLI%2F2026-02-25-8-model-support-changes-in-v0-30-0.md%0ACard%20ID%3A%20gemini-cli-2026-02-25-17c466%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgoogle-gemini%2Fgemini-cli%2Freleases%2Ftag%2Fv0.30.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->