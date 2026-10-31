---
card_id: claude-code-2026-04-22-9e3d36
date: '2026-04-22'
description: 'Claude Code · 2026-04-22 · Pricing Model: OpenTelemetry: `user_prompt`
  events now include `command_name` and `command_source` for slash commands; `cost.usage`…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-daily-limit-to-ensure-a-high-quality-experience-for-all-chatgpt-users-we-are-exp|Daily
    limit: To ensure a high-quality experience for all ChatGPT users, we…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1224
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: pricing-model
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: pricing
machine_hash: 0059a32670269438c60b5ebbf52df65e5721030dfd0c4e0ad08435bfe602ea6b
product: claude-code
product_name: Claude Code
record:
  ai_generated: true
  card_id: claude-code-2026-04-22-9e3d36
  comparison: ''
  confidence: low
  date: '2026-04-22'
  description: 'Claude Code — v2.1.117: OpenTelemetry: `user_prompt` events now include
    `command_name` and `command_source` for slash commands; `cost.usage`, `token.usage`,
    `api_request`, and `api_error` now include an `effort` attribute when the model
    supports effort levels. Custom/MCP command names are redacted unless `OTEL_LOG_TOOL_DETAILS=1`
    is set'
  evidence:
  - quote: 'OpenTelemetry: `user_prompt` events now include `command_name` and `command_source`
      for slash commands; `cost.usage`, `token.usage`, `api_request`, and `api_error`
      now include an `effort` attribute when the model supports effort levels. Custom/MCP
      command names are redacted unless `OTEL_LOG_TOOL_DETAILS=1` is set'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.117
  extractor_version: fallback-v5
  impact: significant
  kind: pricing
  product: claude-code
  product_name: Claude Code
  slug: opentelemetry-user-prompt-events-now-include-command-name-and-command-source-for
  source_release: claude-code-2026-04-22-v2-1-117-github-311984967-1d917373
  source_type: github_releases
  theme: pricing-model
  theme_matches:
  - matched_terms:
    - mcp
    score: 50
    theme: apps-integrations
  - matched_terms:
    - model
    score: 50
    theme: model-support
  theme_resolution: manual-semantic-rule-v1
  title: 'OpenTelemetry: `user_prompt` events now include `command_name` and `command_source`…'
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-04-09-plus-20-month-plus-remains-best-for-steady-day-to-day-use-as-the-temporary-codex|Plus
  ($20/month): Plus remains best for steady, day-to-day use]]'
- '[[Changes/ChatGPT/2026-04-09-pro-200-month-our-highest-usage-option-remains-available-and-continues-on-its-cu|Pro
  ($200/month): Our highest-usage option remains available and continues…]]'
- '[[Changes/ChatGPT/2026-04-09-you-can-upgrade-switch-or-cancel-your-plan-from-settings-my-plan-or-from-the-pri|You
  can upgrade, switch, or cancel your plan from Settings  My Plan or…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-22-v2-1-117-github-311984967-1d917373|claude-code-2026-04-22-v2-1-117-github-311984967-1d917373]]'
source_type: github_releases
theme: pricing-model
title: 'OpenTelemetry: user_prompt events now include command_name and command_source…'
type: change
---

<!-- chronolog:begin region="header" -->
# OpenTelemetry: `user_prompt` events now include `command_name` and `command_source`…

**Claude Code** · 2026-04-22 · [[Themes/pricing-model|Pricing Model]] · Pricing · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.117) · from [[Releases/Claude Code/claude-code-2026-04-22-v2-1-117-github-311984967-1d917373|v2.1.117]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> OpenTelemetry: `user_prompt` events now include `command_name` and `command_source` for slash commands; `cost.usage`, `token.usage`, `api_request`, and `api_error` now include an `effort` attribute when the model supports effort levels. Custom/MCP command names are redacted unless `OTEL_LOG_TOOL_DETAILS=1` is set
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.117
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-04-22-2-developer-workflow-changes-in-v2-1-117|2 Developer Workflow changes in v2.1.117]] · Developer Workflow
- [[Changes/Claude Code/2026-04-22-4-apps-and-integrations-changes-in-v2-1-117|4 Apps and Integrations changes in v2.1.117]] · Apps and Integrations
- [[Changes/Claude Code/2026-04-22-2-model-support-changes-in-v2-1-117|2 Model Support changes in v2.1.117]] · Model Support
- [[Changes/Claude Code/2026-04-22-2-reliability-and-performance-changes-in-v2-1-117|2 Reliability and Performance changes in v2.1.117]] · Reliability and Performance
- [[Changes/Claude Code/2026-04-22-2-agent-mode-changes-in-v2-1-117|2 Agent Mode changes in v2.1.117]] · Agent Mode
- [[Changes/Claude Code/2026-04-22-advisor-tool-experimental-dialog-now-carries-an-experimental-label-learn-more-li|Advisor Tool (experimental)]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Pricing Model

- Earlier: 2026-04-09 · ChatGPT · [[Changes/ChatGPT/2026-04-09-you-can-upgrade-switch-or-cancel-your-plan-from-settings-my-plan-or-from-the-pri|You can upgrade, switch, or cancel your plan from Settings  My Plan or…]]
- Later: 2026-05-11 · Cursor · [[Changes/Cursor/2026-05-11-customers-must-be-on-usage-based-billing-for-bugbot-to-customize-effort-levels-l|Customers must be on usage-based billing for Bugbot to customize effort levels]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-daily-limit-to-ensure-a-high-quality-experience-for-all-chatgpt-users-we-are-exp|Daily limit: To ensure a high-quality experience for all ChatGPT users, we…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-04-22-9e3d36&body=Card%3A%20Changes%2FClaude%20Code%2F2026-04-22-opentelemetry-user-prompt-events-now-include-command-name-and-command-source-for.md%0ACard%20ID%3A%20claude-code-2026-04-22-9e3d36%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.117%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->