---
card_id: claude-code-2026-06-25-82838a
date: '2026-06-25'
description: 'Claude Code · 2026-06-25 · Model Support: Added `claude_code.assistant_response`
  OpenTelemetry log event containing the model''s response text. Redacted unless…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1263
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: change
machine_hash: 2beaa20e4d450e1c0e0185b241b1aa11801a8d2c772a4367cd2e9cbb76f7896f
product: claude-code
product_name: Claude Code
record:
  ai_generated: true
  card_id: claude-code-2026-06-25-82838a
  comparison: ''
  confidence: low
  date: '2026-06-25'
  description: 'Claude Code — v2.1.193: Added `claude_code.assistant_response` OpenTelemetry
    log event containing the model''s response text. Redacted unless `OTEL_LOG_ASSISTANT_RESPONSES=1`;
    when that var is unset it follows `OTEL_LOG_USER_PROMPTS`, so deployments that
    already log prompt content will start receiving response content on upgrade —
    set `OTEL_LOG_ASSISTANT_RESPONSES=0` to keep prompts-only.'
  evidence:
  - quote: Added `claude_code.assistant_response` OpenTelemetry log event containing
      the model's response text. Redacted unless `OTEL_LOG_ASSISTANT_RESPONSES=1`;
      when that var is unset it follows `OTEL_LOG_USER_PROMPTS`, so deployments that
      already log prompt content will start receiving response content on upgrade
      — set `OTEL_LOG_ASSISTANT_RESPONSES=0` to keep prompts-only.
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.193
  extractor_version: fallback-v5
  impact: significant
  kind: change
  product: claude-code
  product_name: Claude Code
  slug: added-claude-code-assistant-response-opentelemetry-log-event-containing-the-mode
  source_release: claude-code-2026-06-25-v2-1-193-github-344922230-0655000d
  source_type: github_releases
  theme: model-support
  title: Added `claude_code.assistant_response` OpenTelemetry log event containing…
  type: change
related_changes:
- '[[Changes/Claude Code/2026-06-15-bug-now-requires-a-description-before-submitting-and-no-longer-uses-model-refusa|/bug
  now requires a description before submitting, and no longer uses…]]'
- '[[Changes/Claude Code/2026-06-19-added-a-warning-when-the-requested-model-is-deprecated-or-automatically-updated|Added
  a warning when the requested model is deprecated or automatically updated…]]'
- '[[Changes/ChatGPT/2026-06-24-we-re-updating-gpt-5-5-instant-our-most-used-model-in-chatgpt-to-improve-convers|GPT-5.5
  Instant Update]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-25-v2-1-193-github-344922230-0655000d|claude-code-2026-06-25-v2-1-193-github-344922230-0655000d]]'
source_type: github_releases
theme: model-support
title: Added claude_code.assistant_response OpenTelemetry log event containing…
type: change
---

<!-- chronolog:begin region="header" -->
# Added `claude_code.assistant_response` OpenTelemetry log event containing…

**Claude Code** · 2026-06-25 · [[Themes/model-support|Model Support]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.193) · from [[Releases/Claude Code/claude-code-2026-06-25-v2-1-193-github-344922230-0655000d|v2.1.193]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `claude_code.assistant_response` OpenTelemetry log event containing the model's response text. Redacted unless `OTEL_LOG_ASSISTANT_RESPONSES=1`; when that var is unset it follows `OTEL_LOG_USER_PROMPTS`, so deployments that already log prompt content will start receiving response content on upgrade — set `OTEL_LOG_ASSISTANT_RESPONSES=0` to keep prompts-only.
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.193
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-06-25-2-apps-and-integrations-changes-in-v2-1-193|2 Apps and Integrations changes in v2.1.193]] · Apps and Integrations
- [[Changes/Claude Code/2026-06-25-added-live-file-path-autocomplete-to-bash-mode|Added live file path autocomplete to bash mode (!)]] · Editor Experience
- [[Changes/Claude Code/2026-06-25-added-a-startup-notice-when-mcp-servers-need-authentication-pointing-at-mcp|Added a startup notice when MCP servers need authentication, pointing at /mcp]] · Account and Access
- [[Changes/Claude Code/2026-06-25-added-automatic-memory-pressure-reaping-for-idle-background-shell-commands-disab|Added automatic memory-pressure reaping for idle background shell commands…]] · Reliability and Performance
- [[Changes/Claude Code/2026-06-25-3-agent-mode-changes-in-v2-1-193|3 Agent Mode changes in v2.1.193]] · Agent Mode
- [[Changes/Claude Code/2026-06-25-improved-add-dir-message-when-the-directory-is-already-a-working-directory|Improved /add-dir message when the directory is already a working directory]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-06-24 · ChatGPT · [[Changes/ChatGPT/2026-06-24-we-re-updating-gpt-5-5-instant-our-most-used-model-in-chatgpt-to-improve-convers|GPT-5.5 Instant Update]]
- Later: 2026-06-26 · ChatGPT · [[Changes/ChatGPT/2026-06-26-as-of-june-26-2026-gpt-4-5-is-no-longer-available-in-chatgpt-including-for-custo|Retiring GPT-4.5]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-06-25-82838a&body=Card%3A%20Changes%2FClaude%20Code%2F2026-06-25-added-claude-code-assistant-response-opentelemetry-log-event-containing-the-mode.md%0ACard%20ID%3A%20claude-code-2026-06-25-82838a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.193%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->