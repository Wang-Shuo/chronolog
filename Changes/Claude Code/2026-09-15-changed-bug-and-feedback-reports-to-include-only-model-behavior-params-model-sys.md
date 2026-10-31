---
card_id: claude-code-2026-09-15-6c3c0b
date: '2026-09-15'
description: 'Claude Code · 2026-09-15 · Model Support: Changed `/bug` and `/feedback`
  reports to include only model-behavior params (model, system prompt, tools) from
  the…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1345
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: change
machine_hash: 2e37c066d16992f293019730fab94b47b372b1f836eea62ff22e95048e97e0bc
product: claude-code
product_name: Claude Code
record:
  ai_generated: true
  card_id: claude-code-2026-09-15-6c3c0b
  comparison: ''
  confidence: low
  date: '2026-09-15'
  description: 'Claude Code — v2.1.273: Changed `/bug` and `/feedback` reports to
    include only model-behavior params (model, system prompt, tools) from the last
    API request, omitting request metadata and `CLAUDE_CODE_EXTRA_BODY` fields'
  evidence:
  - quote: Changed `/bug` and `/feedback` reports to include only model-behavior params
      (model, system prompt, tools) from the last API request, omitting request metadata
      and `CLAUDE_CODE_EXTRA_BODY` fields
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.273
  extractor_version: fallback-v5
  impact: significant
  kind: change
  product: claude-code
  product_name: Claude Code
  slug: changed-bug-and-feedback-reports-to-include-only-model-behavior-params-model-sys
  source_release: claude-code-2026-09-15-v2-1-273-github-389362239-6ea37826
  source_type: github_releases
  theme: model-support
  title: Changed `/bug` and `/feedback` reports to include only model-behavior params…
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-11-added-claude-code-gateway-model-discovery-timeout-ms-to-extend-the-llm-gateway-v|Added
  CLAUDE_CODE_GATEWAY_MODEL_DISCOVERY_TIMEOUT_MS to extend the LLM gateway…]]'
- '[[Changes/ChatGPT/2026-09-14-we-re-retiring-automatic-switching-from-instant-to-thinking-reasoning-for-chatgp|Changes
  to automatic switching to thinking in ChatGPT (Plus and Pro)]]'
- '[[Changes/Claude Code/2026-09-14-2-model-support-changes-in-v2-1-271|2 Model Support
  changes in v2.1.271]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-15-v2-1-273-github-389362239-6ea37826|claude-code-2026-09-15-v2-1-273-github-389362239-6ea37826]]'
source_type: github_releases
theme: model-support
title: Changed /bug and /feedback reports to include only model-behavior params…
type: change
---

<!-- chronolog:begin region="header" -->
# Changed `/bug` and `/feedback` reports to include only model-behavior params…

**Claude Code** · 2026-09-15 · [[Themes/model-support|Model Support]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.273) · from [[Releases/Claude Code/claude-code-2026-09-15-v2-1-273-github-389362239-6ea37826|v2.1.273]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Changed `/bug` and `/feedback` reports to include only model-behavior params (model, system prompt, tools) from the last API request, omitting request metadata and `CLAUDE_CODE_EXTRA_BODY` fields
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.273
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-15-claude-code-on-the-web-improved-the-routine-detail-page-menu-and-rename-in-the-b|Claude Code on the web Improved the routine detail page]] · Interface Experience
- [[Changes/Claude Code/2026-09-15-improved-artifact-database-writes-an-update-can-now-remove-a-single-field-instea|Improved artifact database writes]] · Files and Data
- [[Changes/Claude Code/2026-09-15-5-safety-and-privacy-changes-in-v2-1-273|5 Safety and Privacy changes in v2.1.273]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-15-3-apps-and-integrations-changes-in-v2-1-273|3 Apps and Integrations changes in v2.1.273]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-15-changed-auto-mode-on-bedrock-vertex-and-foundry-to-use-the-local-classifier-by-d|Changed auto mode on Bedrock, Vertex and Foundry to use the local classifier…]] · Agent Mode
- [[Changes/Claude Code/2026-09-15-claude-code-on-the-web-added-a-discard-unsaved-changes-confirmation-before-the-n|Claude Code on the web Added a "Discard unsaved changes?" confirmation before…]] · Editor Experience
- [[Changes/Claude Code/2026-09-15-4-account-and-access-changes-in-v2-1-273|4 Account and Access changes in v2.1.273]] · Account and Access
- [[Changes/Claude Code/2026-09-15-improved-responsiveness-in-long-sessions-hook-progress-and-sub-agent-activity-no|Improved responsiveness in long sessions]] · Reliability and Performance
- [[Changes/Claude Code/2026-09-15-added-x-claude-code-request-class-x-claude-code-agent-type-x-claude-code-prev-to|Added x-claude-code-request-class, x-claude-code-agent-type…]] · Context Window
- [[Changes/Claude Code/2026-09-15-claude-code-on-the-web-removed-the-full-page-desktop-app-download-screen-that-ne|Claude Code on the web Removed the full-page desktop-app download screen that new…]] · Mobile and Desktop
- [[Changes/Claude Code/2026-09-15-3-developer-workflow-changes-in-v2-1-273|3 Developer Workflow changes in v2.1.273]] · Developer Workflow
- [[Changes/Claude Code/2026-09-15-8-other-changes-in-v2-1-273|8 other changes in v2.1.273]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-09-14 · Claude Code · [[Changes/Claude Code/2026-09-14-2-model-support-changes-in-v2-1-271|2 Model Support changes in v2.1.271]]
- Later: 2026-09-17 · Claude Code · [[Changes/Claude Code/2026-09-17-2-model-support-changes-in-v2-1-274|2 Model Support changes in v2.1.274]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-15-6c3c0b&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-15-changed-bug-and-feedback-reports-to-include-only-model-behavior-params-model-sys.md%0ACard%20ID%3A%20claude-code-2026-09-15-6c3c0b%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.273%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->