---
card_id: claude-code-2026-10-02-731d9f
date: '2026-10-02'
description: 'Claude Code · 2026-10-02 · Model Support: Changed the client-side auto
  mode classifier to ignore an `ANTHROPIC_DEFAULT_SONNET_MODEL` pin that names Claude…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1362
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: change
machine_hash: 8bbec639c88fd6bee6133b0d9f294a1764519a0c99eed07fb8bd4da70c31c628
product: claude-code
product_name: Claude Code
record:
  ai_generated: true
  card_id: claude-code-2026-10-02-731d9f
  comparison: ''
  confidence: low
  date: '2026-10-02'
  description: 'Claude Code — v2.1.288: Changed the client-side auto mode classifier
    to ignore an `ANTHROPIC_DEFAULT_SONNET_MODEL` pin that names Claude Sonnet 5.5
    or Opus 5.5 and use Claude Sonnet 5 instead'
  evidence:
  - quote: Changed the client-side auto mode classifier to ignore an `ANTHROPIC_DEFAULT_SONNET_MODEL`
      pin that names Claude Sonnet 5.5 or Opus 5.5 and use Claude Sonnet 5 instead
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.288
  extractor_version: fallback-v5
  impact: significant
  kind: change
  product: claude-code
  product_name: Claude Code
  slug: changed-the-client-side-auto-mode-classifier-to-ignore-an-anthropic-default-sonn
  source_release: claude-code-2026-10-02-v2-1-288-github-402056988-39eb9ac6
  source_type: github_releases
  theme: model-support
  theme_matches:
  - matched_terms:
    - claude sonnet
    - model
    - opus
    - sonnet
    score: 210
    theme: model-support
  - matched_terms:
    - auto mode
    score: 60
    theme: agent-mode
  theme_resolution: manual-semantic-rule-v2
  title: Changed the client-side auto mode classifier to ignore…
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-29-3-model-support-changes-in-v2-1-285|3 Model Support
  changes in v2.1.285]]'
- '[[Changes/Claude Code/2026-09-30-changed-how-failed-api-requests-are-retried-one-limit-now-covers-a-whole-model-c|Changed
  how failed API requests are retried]]'
- '[[Changes/Claude Code/2026-10-01-4-model-support-changes-in-v2-1-287|4 Model Support
  changes in v2.1.287]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-02-v2-1-288-github-402056988-39eb9ac6|claude-code-2026-10-02-v2-1-288-github-402056988-39eb9ac6]]'
source_type: github_releases
theme: model-support
title: Changed the client-side auto mode classifier to ignore…
type: change
---

<!-- chronolog:begin region="header" -->
# Changed the client-side auto mode classifier to ignore…

**Claude Code** · 2026-10-02 · [[Themes/model-support|Model Support]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.288) · from [[Releases/Claude Code/claude-code-2026-10-02-v2-1-288-github-402056988-39eb9ac6|v2.1.288]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Changed the client-side auto mode classifier to ignore an `ANTHROPIC_DEFAULT_SONNET_MODEL` pin that names Claude Sonnet 5.5 or Opus 5.5 and use Claude Sonnet 5 instead
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.288
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-02-added-a-re-authenticate-prompt-when-an-mcp-server-asks-for-more-oauth-scope-duri|Added a re-authenticate prompt when an MCP server asks for more OAuth scope during…]] · Account and Access
- [[Changes/Claude Code/2026-10-02-3-developer-workflow-changes-in-v2-1-288|3 Developer Workflow changes in v2.1.288]] · Developer Workflow
- [[Changes/Claude Code/2026-10-02-changed-autocompact-to-save-the-auto-compact-window-per-model-so-each-model-keep|Changed /autocompact to save the auto-compact window per model, so each model…]] · Context Window
- [[Changes/Claude Code/2026-10-02-5-apps-and-integrations-changes-in-v2-1-288|5 Apps and Integrations changes in v2.1.288]] · Apps and Integrations
- [[Changes/Claude Code/2026-10-02-2-accessibility-and-localization-changes-in-v2-1-288|2 Accessibility and Localization changes in v2.1.288]] · Accessibility and Localization
- [[Changes/Claude Code/2026-10-02-4-agent-mode-changes-in-v2-1-288|4 Agent Mode changes in v2.1.288]] · Agent Mode
- [[Changes/Claude Code/2026-10-02-6-safety-and-privacy-changes-in-v2-1-288|6 Safety and Privacy changes in v2.1.288]] · Safety and Privacy
- [[Changes/Claude Code/2026-10-02-added-ui-selection-for-mods-returns-the-text-you-last-selected-in-fullscreen-mod|Added $.ui.selection() for mods]] · Interface Experience
- [[Changes/Claude Code/2026-10-02-improved-the-usage-credits-message-shown-to-team-and-enterprise-members-whose-or|Improved the /usage-credits message shown to Team and Enterprise members whose…]] · Pricing Model
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-10-01 · Claude Code · [[Changes/Claude Code/2026-10-01-4-model-support-changes-in-v2-1-287|4 Model Support changes in v2.1.287]]
- Later: 2026-10-05 · Claude Code · [[Changes/Claude Code/2026-10-05-2-model-support-changes-in-v2-1-290|2 Model Support changes in v2.1.290]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-02-731d9f&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-02-changed-the-client-side-auto-mode-classifier-to-ignore-an-anthropic-default-sonn.md%0ACard%20ID%3A%20claude-code-2026-10-02-731d9f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.288%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->