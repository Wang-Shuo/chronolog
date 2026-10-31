---
card_id: claude-code-2026-08-28-062add
date: '2026-08-28'
description: 'Claude Code · 2026-08-28 · Model Support: 4 changes in v2.1.251 — Added
  `PreModelSwitch` and `PostModelSwitch` hook events (block, confirm, or annotate
  a model…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1327
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: bc9dc20db0126ed863457310c5b33cd35e58996ff1a8a27b4a0352670e1fb4b7
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-08-28-062add
  comparison: ''
  date: '2026-08-28'
  description: 'Claude Code — v2.1.251: 4 Model Support changes'
  evidence:
  - quote: Added `PreModelSwitch` and `PostModelSwitch` hook events (block, confirm,
      or annotate a model switch); `SessionStart` resume hooks now receive session
      staleness and the estimated re-cache cost
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.251
  - quote: 'Changed the default commit trailer to `Co-Authored-By: Claude Code` when
      the active model isn''t a recognized Claude model (e.g. third-party models behind
      a custom `ANTHROPIC_BASE_URL`)'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.251
  - quote: Changed the default model for seat-based Enterprise subscriptions to Opus
      5, matching other premium plans
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.251
  - quote: Changed `/effort` to save your default effort level per model, so each
      model keeps its own setting when you switch
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.251
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 4-model-support-changes-in-v2-1-251
  source_release: claude-code-2026-08-28-v2-1-251-github-378586104-42ac2f96
  source_type: github_releases
  theme: model-support
  title: 4 Model Support changes in v2.1.251
  type: change
related_changes:
- '[[Changes/Claude Code/2026-08-17-2-model-support-changes-in-v2-1-234|2 Model Support
  changes in v2.1.234]]'
- '[[Changes/Claude Code/2026-08-19-added-anthropic-default-model-environment-variable-sets-the-model-new-sessions-s|Added
  ANTHROPIC_DEFAULT_MODEL environment variable]]'
- '[[Changes/Claude Code/2026-08-26-added-claude-api-cost-optimize-to-profile-an-existing-project-s-claude-api-spend|Added
  /claude-api cost-optimize to profile an existing project''s Claude API spend…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-08-28-v2-1-251-github-378586104-42ac2f96|claude-code-2026-08-28-v2-1-251-github-378586104-42ac2f96]]'
source_type: github_releases
superseded: true
theme: model-support
title: 4 Model Support changes in v2.1.251
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Model Support changes in v2.1.251

**Claude Code** · 2026-08-28 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.251) · from [[Releases/Claude Code/claude-code-2026-08-28-v2-1-251-github-378586104-42ac2f96|v2.1.251]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `PreModelSwitch` and `PostModelSwitch` hook events (block, confirm, or annotate a model switch); `SessionStart` resume hooks now receive session staleness and the estimated re-cache cost

> Changed the default commit trailer to `Co-Authored-By: Claude Code` when the active model isn't a recognized Claude model (e.g. third-party models behind a custom `ANTHROPIC_BASE_URL`)

> Changed the default model for seat-based Enterprise subscriptions to Opus 5, matching other premium plans

> Changed `/effort` to save your default effort level per model, so each model keeps its own setting when you switch

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.251
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-08-28-changed-analytics-to-no-longer-turn-off-before-sign-in-solely-because-managed-se|Changed analytics to no longer turn off before sign-in solely because managed…]] · Account and Access
- [[Changes/Claude Code/2026-08-28-added-a-per-session-prompt-cache-line-to-cost-hit-ratio-misses-tokens-re-cached|Added a per-session prompt-cache line to /cost…]] · Pricing Model
- [[Changes/Claude Code/2026-08-28-4-apps-and-integrations-changes-in-v2-1-251|4 Apps and Integrations changes in v2.1.251]] · Apps and Integrations
- [[Changes/Claude Code/2026-08-28-3-developer-workflow-changes-in-v2-1-251|3 Developer Workflow changes in v2.1.251]] · Developer Workflow
- [[Changes/Claude Code/2026-08-28-improved-retry-when-the-model-s-tool-call-is-malformed-the-broken-output-is-now|Improved retry when the model's tool call is malformed]] · Context Window
- [[Changes/Claude Code/2026-08-28-4-agent-mode-changes-in-v2-1-251|4 Agent Mode changes in v2.1.251]] · Agent Mode
- [[Changes/Claude Code/2026-08-28-improved-amazon-bedrock-session-start-under-claude-code-provider-managed-by-host|Improved Amazon Bedrock session start under CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST…]] · Mobile and Desktop
- [[Changes/Claude Code/2026-08-28-6-safety-and-privacy-changes-in-v2-1-251|6 Safety and Privacy changes in v2.1.251]] · Safety and Privacy
- [[Changes/Claude Code/2026-08-28-8-other-changes-in-v2-1-251|8 other changes in v2.1.251]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-08-26 · Claude Code · [[Changes/Claude Code/2026-08-26-added-claude-api-cost-optimize-to-profile-an-existing-project-s-claude-api-spend|Added /claude-api cost-optimize to profile an existing project's Claude API spend…]]
- Later: 2026-09-01 · Claude Code · [[Changes/Claude Code/2026-09-01-6-model-support-changes-in-v2-1-257|6 Model Support changes in v2.1.257]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-08-28-062add&body=Card%3A%20Changes%2FClaude%20Code%2F2026-08-28-4-model-support-changes-in-v2-1-251.md%0ACard%20ID%3A%20claude-code-2026-08-28-062add%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.251%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->