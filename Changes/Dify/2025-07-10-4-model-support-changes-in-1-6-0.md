---
card_id: dify-2025-07-10-e44714
date: '2025-07-10'
description: 'Dify · 2025-07-10 · Model Support: 4 changes in v1.6.0 — We’re thrilled
  to introduce **support for [Anthropic’s Model Context Protocol…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 913
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: cbd13502c5973be5bb2e9df34320b92684ff4c4df298809f4354ac14f7791412
product: dify
product_name: Dify
record:
  card_id: dify-2025-07-10-e44714
  comparison: ''
  date: '2025-07-10'
  description: 'Dify — v1.6.0: 4 Model Support changes'
  evidence:
  - quote: We’re thrilled to introduce **support for [Anthropic’s Model Context Protocol
      (MCP)](https://docs.anthropic.com/claude/docs/model-context-protocol)** — a
      new industry standard for structuring model inputs and outputs. MCP makes it
      easier than ever to integrate with cutting-edge language models using a unified,
      reliable format.
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: 'feat(tests): add structured output parser tests for LLM responses by @Yeuoly
      in https://github.com/langgenius/dify/pull/21838'
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: moving the `MessageStatus` class from the `models.model` module to `models.enums`
      module by @NeatGuyCoding in https://github.com/langgenius/dify/pull/21867
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: Expose LLM usage in workflows by @DavideDelbianco in https://github.com/langgenius/dify/pull/21766
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 4-model-support-changes-in-1-6-0
  source_release: dify-2025-07-10-1-6-0-github-231400193-9181f945
  source_type: github_releases
  theme: model-support
  title: 4 Model Support changes in 1.6.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2025-07-09-2-model-support-changes-in-rust-v0-4-0|2 Model Support
  changes in rust-v0.4.0]]'
- '[[Changes/Cline/2025-07-10-adding-thinking-token-config-to-gemini-2-5-pro-model-and-adding-gemini-2-5-flash|Adding
  Thinking Token Config to Gemini 2.5 pro model and adding gemini 2.5 flash preview]]'
- '[[Changes/Codex CLI/2025-07-10-added-new-config-option-model-supports-reasoning-summaries-https-github-com-open|Added
  new config option]]'
source_release: '[[Releases/Dify/dify-2025-07-10-1-6-0-github-231400193-9181f945|dify-2025-07-10-1-6-0-github-231400193-9181f945]]'
source_type: github_releases
theme: model-support
title: 4 Model Support changes in 1.6.0
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Model Support changes in 1.6.0

**Dify** · 2025-07-10 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.6.0) · from [[Releases/Dify/dify-2025-07-10-1-6-0-github-231400193-9181f945|v1.6.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> We’re thrilled to introduce **support for [Anthropic’s Model Context Protocol (MCP)](https://docs.anthropic.com/claude/docs/model-context-protocol)** — a new industry standard for structuring model inputs and outputs. MCP makes it easier than ever to integrate with cutting-edge language models using a unified, reliable format.

> feat(tests): add structured output parser tests for LLM responses by @Yeuoly in https://github.com/langgenius/dify/pull/21838

> moving the `MessageStatus` class from the `models.model` module to `models.enums` module by @NeatGuyCoding in https://github.com/langgenius/dify/pull/21867

> Expose LLM usage in workflows by @DavideDelbianco in https://github.com/langgenius/dify/pull/21766

Source: https://github.com/langgenius/dify/releases/tag/1.6.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2025-07-10-2-editor-experience-changes-in-1-6-0|2 Editor Experience changes in 1.6.0]] · Editor Experience
- [[Changes/Dify/2025-07-10-optimize-the-memory-usage-of-tencent-vector-database-by-wlleiiwang-in-https-gith|Optimize the memory usage of Tencent Vector Database]] · Reliability and Performance
- [[Changes/Dify/2025-07-10-feat-retain-llm-setting-for-agent-node-by-fdb02983rhy-in-https-github-com-langge|feat: Retain llm setting for agent node]] · Agent Mode
- [[Changes/Dify/2025-07-10-10-apps-and-integrations-changes-in-1-6-0|10 Apps and Integrations changes in 1.6.0]] · Apps and Integrations
- [[Changes/Dify/2025-07-10-2-interface-experience-changes-in-1-6-0|2 Interface Experience changes in 1.6.0]] · Interface Experience
- [[Changes/Dify/2025-07-10-style-config-var-update-styling-classes-to-use-design-system-tokens-by-minamiyam|style(config-var): update styling classes to use design system tokens]] · Context Window
- [[Changes/Dify/2025-07-10-3-files-and-data-changes-in-1-6-0|3 Files and Data changes in 1.6.0]] · Files and Data
- [[Changes/Dify/2025-07-10-54-other-changes-in-1-6-0|54 other changes in 1.6.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2025-07-10 · Codex CLI · [[Changes/Codex CLI/2025-07-10-added-new-config-option-model-supports-reasoning-summaries-https-github-com-open|Added new config option]]
- Later: 2025-07-11 · Gemini CLI · [[Changes/Gemini CLI/2025-07-11-5-model-support-changes-in-v0-1-10|5 Model Support changes in v0.1.10]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2025-07-10-e44714&body=Card%3A%20Changes%2FDify%2F2025-07-10-4-model-support-changes-in-1-6-0.md%0ACard%20ID%3A%20dify-2025-07-10-e44714%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.6.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->