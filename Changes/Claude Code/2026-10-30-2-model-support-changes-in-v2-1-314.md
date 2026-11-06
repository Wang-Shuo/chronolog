---
card_id: claude-code-2026-10-30-6a593a
date: '2026-10-30'
description: 'Claude Code · 2026-10-30 · Model Support: 2 changes in v2.1.314 — Changed
  flagged requests to retry on another model, not end in a refusal, when…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1390
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: cd9837b23a6544324d5468c1dc6fd2d56f72a58a16a8c6df4c7aa34be3884ead
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-30-6a593a
  comparison: ''
  date: '2026-10-30'
  description: 'Claude Code — v2.1.314: 2 Model Support changes'
  evidence:
  - quote: Changed flagged requests to retry on another model, not end in a refusal,
      when `ANTHROPIC_DEFAULT_OPUS_MODEL`, `availableModels` or `deniedModels` leaves
      only an older Opus model, or none
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.314
  - quote: Changed idle compaction to also run for subscribers with telemetry turned
      off, and on Bedrock, Vertex, Foundry and LLM gateways once the one-hour prompt
      cache is on
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.314
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-model-support-changes-in-v2-1-314
  source_release: claude-code-2026-10-30-v2-1-314-github-428518421-b7ac83d7
  source_type: github_releases
  theme: model-support
  title: 2 Model Support changes in v2.1.314
  type: change
related_changes:
- '[[Changes/OpenHands/2026-10-27-refactor-settings-use-existing-model-profile-theme-aliases-by-enyst-in-https-git|refactor(settings):
  use existing model-profile theme aliases]]'
- '[[Changes/Codex CLI/2026-10-29-10-model-support-changes-in-rust-v0-166-0|10 Model
  Support changes in rust-v0.166.0]]'
- '[[Changes/Open WebUI/2026-10-29-7-model-support-changes-in-v0-12-5|7 Model Support
  changes in v0.12.5]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-30-v2-1-314-github-428518421-b7ac83d7|claude-code-2026-10-30-v2-1-314-github-428518421-b7ac83d7]]'
source_type: github_releases
theme: model-support
title: 2 Model Support changes in v2.1.314
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Model Support changes in v2.1.314

**Claude Code** · 2026-10-30 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.314) · from [[Releases/Claude Code/claude-code-2026-10-30-v2-1-314-github-428518421-b7ac83d7|v2.1.314]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Changed flagged requests to retry on another model, not end in a refusal, when `ANTHROPIC_DEFAULT_OPUS_MODEL`, `availableModels` or `deniedModels` leaves only an older Opus model, or none

> Changed idle compaction to also run for subscribers with telemetry turned off, and on Bedrock, Vertex, Foundry and LLM gateways once the one-hour prompt cache is on

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.314
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-30-3-agent-mode-changes-in-v2-1-314|3 Agent Mode changes in v2.1.314]] · Agent Mode
- [[Changes/Claude Code/2026-10-30-3-reliability-and-performance-changes-in-v2-1-314|3 Reliability and Performance changes in v2.1.314]] · Reliability and Performance
- [[Changes/Claude Code/2026-10-30-3-enterprise-and-administration-changes-in-v2-1-314|3 Enterprise and Administration changes in v2.1.314]] · Enterprise and Administration
- [[Changes/Claude Code/2026-10-30-4-developer-workflow-changes-in-v2-1-314|4 Developer Workflow changes in v2.1.314]] · Developer Workflow
- [[Changes/Claude Code/2026-10-30-improved-the-cloud-session-error-shown-while-a-request-refused-for-your-claude-a|Improved the cloud session error shown while a request refused for your claude.ai…]] · Account and Access
- [[Changes/Claude Code/2026-10-30-3-apps-and-integrations-changes-in-v2-1-314|3 Apps and Integrations changes in v2.1.314]] · Apps and Integrations
- [[Changes/Claude Code/2026-10-30-10-safety-and-privacy-changes-in-v2-1-314|10 Safety and Privacy changes in v2.1.314]] · Safety and Privacy
- [[Changes/Claude Code/2026-10-30-2-mobile-and-desktop-changes-in-v2-1-314|2 Mobile and Desktop changes in v2.1.314]] · Mobile and Desktop
- [[Changes/Claude Code/2026-10-30-2-editor-experience-changes-in-v2-1-314|2 Editor Experience changes in v2.1.314]] · Editor Experience
- [[Changes/Claude Code/2026-10-30-10-other-changes-in-v2-1-314|10 other changes in v2.1.314]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-10-29 · Open WebUI · [[Changes/Open WebUI/2026-10-29-7-model-support-changes-in-v0-12-5|7 Model Support changes in v0.12.5]]
- Later: 2026-10-30 · Replit · [[Changes/Replit/2026-10-30-gpt-6-1-terra-in-the-model-selector|GPT-6.1 Terra in the model selector]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-30-6a593a&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-30-2-model-support-changes-in-v2-1-314.md%0ACard%20ID%3A%20claude-code-2026-10-30-6a593a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.314%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->