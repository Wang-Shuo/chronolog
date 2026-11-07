---
card_id: dify-2026-08-25-e78748
date: '2026-08-25'
description: 'Dify · 2026-08-25 · Context Window: 8 changes in v1.17.0 — **Context-aware
  history compaction**: long agent conversations no longer blow past the model''s…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click
    to select a range]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2533
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 040e31d894dd9ad8b019a46b302f876c9a1270236eb17c78c042375c40499974
product: dify
product_name: Dify
record:
  card_id: dify-2026-08-25-e78748
  comparison: ''
  date: '2026-08-25'
  description: 'Dify — v1.17.0: 8 Context Window changes'
  evidence:
  - quote: '**Context-aware history compaction**: long agent conversations no longer
      blow past the model''s context window — Dify resolves each model''s effective
      window and tiers compaction (clear old tool results first, then summarize older
      history) so runs stay within budget without losing recent context (#40872).'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: '`OPS_TRACE_UNIFIED_ENABLED`, `OPS_TRACE_PARENT_CONTEXT_TTL_SECONDS`'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'refactor(web): remove app log drawer context by @lyzno1 in https://github.com/langgenius/dify/pull/39792'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'refactor(web): remove configuration mitt context by @lyzno1 in https://github.com/langgenius/dify/pull/39796'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'refactor(web): remove dead dataset operator context state by @lyzno1 in
      https://github.com/langgenius/dify/pull/39800'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'refactor(web): narrow app list context by @lyzno1 in https://github.com/langgenius/dify/pull/39802'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'chore: Remove redundant dataset context string conversions by @medisean
      in https://github.com/langgenius/dify/pull/40189'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'feat(dify-agent): add context-aware history compaction by @BeautyyuYanli
      in https://github.com/langgenius/dify/pull/40872'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 8-context-window-changes-in-1-17-0
  source_release: dify-2026-08-25-1-17-0-github-376348099-66c16161
  source_type: github_releases
  theme: context-window
  title: 8 Context Window changes in 1.17.0
  type: change
related_changes:
- '[[Changes/Cline/2026-08-21-only-treat-an-anthropic-invalid-request-error-as-a-context-overflow-when-its-mes|Only
  treat an Anthropic invalid_request_error as a context-overflow…]]'
- '[[Changes/Ollama/2026-08-21-disabled-claude-code-s-tokens-left-token-countdown-system-message-which-ollama-m|Disabled
  Claude Code''s "tokens left" token-countdown system message, which Ollama…]]'
- '[[Changes/Replit/2026-08-21-start-with-conversations|Start with Conversations]]'
source_release: '[[Releases/Dify/dify-2026-08-25-1-17-0-github-376348099-66c16161|dify-2026-08-25-1-17-0-github-376348099-66c16161]]'
source_type: github_releases
theme: context-window
title: 8 Context Window changes in 1.17.0
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Context Window changes in 1.17.0

**Dify** · 2026-08-25 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.17.0) · from [[Releases/Dify/dify-2026-08-25-1-17-0-github-376348099-66c16161|v1.17.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **Context-aware history compaction**: long agent conversations no longer blow past the model's context window — Dify resolves each model's effective window and tiers compaction (clear old tool results first, then summarize older history) so runs stay within budget without losing recent context (#40872).

> `OPS_TRACE_UNIFIED_ENABLED`, `OPS_TRACE_PARENT_CONTEXT_TTL_SECONDS`

> refactor(web): remove app log drawer context by @lyzno1 in https://github.com/langgenius/dify/pull/39792

> refactor(web): remove configuration mitt context by @lyzno1 in https://github.com/langgenius/dify/pull/39796

> refactor(web): remove dead dataset operator context state by @lyzno1 in https://github.com/langgenius/dify/pull/39800

> refactor(web): narrow app list context by @lyzno1 in https://github.com/langgenius/dify/pull/39802

> chore: Remove redundant dataset context string conversions by @medisean in https://github.com/langgenius/dify/pull/40189

> feat(dify-agent): add context-aware history compaction by @BeautyyuYanli in https://github.com/langgenius/dify/pull/40872

Source: https://github.com/langgenius/dify/releases/tag/1.17.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-08-25-2-enterprise-and-administration-changes-in-1-17-0|2 Enterprise and Administration changes in 1.17.0]] · Enterprise and Administration
- [[Changes/Dify/2026-08-25-audio-asr-now-accepts-audio-x-m4a-and-audio-mime-types-are-validated-more-accura|Audio ASR now accepts audio/x-m4a, and audio MIME types are validated more…]] · Voice and Audio
- [[Changes/Dify/2026-08-25-5-collaboration-changes-in-1-17-0|5 Collaboration changes in 1.17.0]] · Collaboration
- [[Changes/Dify/2026-08-25-16-safety-and-privacy-changes-in-1-17-0|16 Safety and Privacy changes in 1.17.0]] · Safety and Privacy
- [[Changes/Dify/2026-08-25-feat-workflow-support-human-input-in-loop-and-iteration-by-laipz8200-in-https-gi|feat(workflow): support human input in loop and iteration]] · Automation and Scheduling
- [[Changes/Dify/2026-08-25-4-editor-experience-changes-in-1-17-0|4 Editor Experience changes in 1.17.0]] · Editor Experience
- [[Changes/Dify/2026-08-25-3-multimodal-input-changes-in-1-17-0|3 Multimodal Input changes in 1.17.0]] · Multimodal Input
- [[Changes/Dify/2026-08-25-53-agent-mode-changes-in-1-17-0|53 Agent Mode changes in 1.17.0]] · Agent Mode
- [[Changes/Dify/2026-08-25-4-developer-workflow-changes-in-1-17-0|4 Developer Workflow changes in 1.17.0]] · Developer Workflow
- [[Changes/Dify/2026-08-25-93-model-support-changes-in-1-17-0|93 Model Support changes in 1.17.0]] · Model Support
- [[Changes/Dify/2026-08-25-13-account-and-access-changes-in-1-17-0|13 Account and Access changes in 1.17.0]] · Account and Access
- [[Changes/Dify/2026-08-25-28-apps-and-integrations-changes-in-1-17-0|28 Apps and Integrations changes in 1.17.0]] · Apps and Integrations
- [[Changes/Dify/2026-08-25-7-pricing-model-changes-in-1-17-0|7 Pricing Model changes in 1.17.0]] · Pricing Model
- [[Changes/Dify/2026-08-25-5-files-and-data-changes-in-1-17-0|5 Files and Data changes in 1.17.0]] · Files and Data
- [[Changes/Dify/2026-08-25-workflow-runtime-stability|Workflow & Runtime Stability]] · Reliability and Performance
- [[Changes/Dify/2026-08-25-9-interface-experience-changes-in-1-17-0|9 Interface Experience changes in 1.17.0]] · Interface Experience
- [[Changes/Dify/2026-08-25-3-accessibility-and-localization-changes-in-1-17-0|3 Accessibility and Localization changes in 1.17.0]] · Accessibility and Localization
- [[Changes/Dify/2026-08-25-351-other-changes-in-1-17-0|351 other changes in 1.17.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-08-21 · Replit · [[Changes/Replit/2026-08-21-start-with-conversations|Start with Conversations]]
- Later: 2026-08-25 · Gemini CLI · [[Changes/Gemini CLI/2026-08-25-ssr-agent-issue-fix-19239-update-clear-command-docs-to-include-context-reset-by|SSR Agent Issue Fix (19239): Update /clear command docs to include context reset]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click to select a range]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-08-25-e78748&body=Card%3A%20Changes%2FDify%2F2026-08-25-8-context-window-changes-in-1-17-0.md%0ACard%20ID%3A%20dify-2026-08-25-e78748%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.17.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->