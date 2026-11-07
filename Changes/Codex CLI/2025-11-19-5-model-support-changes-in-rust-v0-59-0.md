---
card_id: codex-cli-2025-11-19-c2d461
date: '2025-11-19'
description: 'Codex CLI · 2025-11-19 · Model Support: 5 changes in 0.59.0 — GPT-5.1-Codex-Max:
  introducing our newest frontier agentic coding model. GPT-5.1-Codex-Max…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1045
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 5c3a05aad4f910859db9953ea06c9172afda36dd233a6f98afdf4b889fd472fa
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2025-11-19-c2d461
  comparison: ''
  date: '2025-11-19'
  description: 'Codex CLI — 0.59.0: 5 Model Support changes'
  evidence:
  - quote: 'GPT-5.1-Codex-Max: introducing our newest frontier agentic coding model.
      GPT-5.1-Codex-Max delivers higher reliability, faster iteration, and support
      for long-running, project-scale workflows. Learn more at https://www.openai.com/index/gpt-5-1-codex-max'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.59.0
  - quote: updating codex backend models (#6855) — @zhao
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.59.0
  - quote: Update faq.md section on supported models (#6832) — @adpena
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.59.0
  - quote: Update defaults to gpt-5.1 (#6652) — @aibrahim
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.59.0
  - quote: '[App-server] add new v2 events:`item/reasoning/delta`, `item/agentMessage/delta`
      & `item/reasoning/summaryPartAdded` (#6559) — @celia'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.59.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 5-model-support-changes-in-rust-v0-59-0
  source_release: codex-cli-2025-11-19-rust-v0-59-0-github-263735550-757042e7
  source_type: github_releases
  theme: model-support
  title: 5 Model Support changes in rust-v0.59.0
  type: change
related_changes:
- '[[Changes/Windsurf/2025-11-18-gemini-3-pro-preview|Gemini 3 Pro Preview]]'
- '[[Changes/ChatGPT/2025-11-19-today-we-re-updating-gpt-5-pro-to-gpt-5-1-pro-in-early-testing-users-consistentl-191826|GPT-5.1
  Pro: Clearer, more capable answers for complex work]]'
- '[[Changes/Codex CLI/2025-11-19-default-model-for-api-users-is-now-gpt-5-1-codex|Default
  model for API users is now gpt-5.1-codex]]'
source_release: '[[Releases/Codex CLI/codex-cli-2025-11-19-rust-v0-59-0-github-263735550-757042e7|codex-cli-2025-11-19-rust-v0-59-0-github-263735550-757042e7]]'
source_type: github_releases
theme: model-support
title: 5 Model Support changes in rust-v0.59.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Model Support changes in rust-v0.59.0

**Codex CLI** · 2025-11-19 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.59.0) · from [[Releases/Codex CLI/codex-cli-2025-11-19-rust-v0-59-0-github-263735550-757042e7|0.59.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> GPT-5.1-Codex-Max: introducing our newest frontier agentic coding model. GPT-5.1-Codex-Max delivers higher reliability, faster iteration, and support for long-running, project-scale workflows. Learn more at https://www.openai.com/index/gpt-5-1-codex-max

> updating codex backend models (#6855) — @zhao

> Update faq.md section on supported models (#6832) — @adpena

> Update defaults to gpt-5.1 (#6652) — @aibrahim

> [App-server] add new v2 events:`item/reasoning/delta`, `item/agentMessage/delta` & `item/reasoning/summaryPartAdded` (#6559) — @celia

Source: https://github.com/openai/codex/releases/tag/rust-v0.59.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2025-11-19-handle-don-t-trust-directory-selection-in-onboarding-4941-viniciusmotta8|Handle "Don't Trust" directory selection in onboarding (♯4941) — @viniciusmotta8]] · Interface Experience
- [[Changes/Codex CLI/2025-11-19-2-agent-mode-changes-in-rust-v0-59-0|2 Agent Mode changes in rust-v0.59.0]] · Agent Mode
- [[Changes/Codex CLI/2025-11-19-native-compaction-support-added-first-class-support-for-compaction-improving-per|Native Compaction Support]] · Reliability and Performance
- [[Changes/Codex CLI/2025-11-19-bug-fix-rmcp-client-refresh-oauth-tokens-using-expires-at-6574-laelluo|:bug: fix(rmcp-client): refresh OAuth tokens using expires_at (♯6574) — @LaelLuo]] · Account and Access
- [[Changes/Codex CLI/2025-11-19-promote-shared-helpers-for-suite-tests-6460-aibrahim|Promote shared helpers for suite tests (♯6460) — @aibrahim]] · Collaboration
- [[Changes/Codex CLI/2025-11-19-15-developer-workflow-changes-in-rust-v0-59-0|15 Developer Workflow changes in rust-v0.59.0]] · Developer Workflow
- [[Changes/Codex CLI/2025-11-19-6-context-window-changes-in-rust-v0-59-0|6 Context Window changes in rust-v0.59.0]] · Context Window
- [[Changes/Codex CLI/2025-11-19-3-mobile-and-desktop-changes-in-rust-v0-59-0|3 Mobile and Desktop changes in rust-v0.59.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2025-11-19-use-shared-network-gating-helper-in-chat-completion-tests-6461-aibrahim|Use shared network gating helper in chat completion tests (♯6461) — @aibrahim]] · Editor Experience
- [[Changes/Codex CLI/2025-11-19-5-apps-and-integrations-changes-in-rust-v0-59-0|5 Apps and Integrations changes in rust-v0.59.0]] · Apps and Integrations
- [[Changes/Codex CLI/2025-11-19-7-safety-and-privacy-changes-in-rust-v0-59-0|7 Safety and Privacy changes in rust-v0.59.0]] · Safety and Privacy
- [[Changes/Codex CLI/2025-11-19-credits-are-now-visible-in-status|Credits are now visible in /status]] · Pricing Model
- [[Changes/Codex CLI/2025-11-19-53-other-changes-in-rust-v0-59-0|53 other changes in rust-v0.59.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2025-11-19 · Codex CLI · [[Changes/Codex CLI/2025-11-19-default-model-for-api-users-is-now-gpt-5-1-codex|Default model for API users is now gpt-5.1-codex]]
- Later: 2025-11-19 · Notion · [[Changes/Notion/2025-11-19-gemini-3-pro-is-now-available-in-notion|Gemini 3 Pro is live]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2025-11-19-c2d461&body=Card%3A%20Changes%2FCodex%20CLI%2F2025-11-19-5-model-support-changes-in-rust-v0-59-0.md%0ACard%20ID%3A%20codex-cli-2025-11-19-c2d461%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.59.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->