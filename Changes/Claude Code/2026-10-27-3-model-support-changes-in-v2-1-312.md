---
card_id: claude-code-2026-10-27-c903dd
date: '2026-10-27'
description: 'Claude Code · 2026-10-27 · Model Support: 3 changes in v2.1.312 — Changed
  Bedrock, Vertex, Foundry and Mantle to use the shorter system prompt for model names…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1387
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 46383c1a61b42f55a9216cc9a429b317d953f59c7a11831eea6ed8f4b2b08ab9
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-27-c903dd
  comparison: ''
  date: '2026-10-27'
  description: 'Claude Code — v2.1.312: 3 Model Support changes'
  evidence:
  - quote: Changed Bedrock, Vertex, Foundry and Mantle to use the shorter system prompt
      for model names Claude Code doesn't recognize, such as custom deployment names
      and inference profile ARNs, even when they front Sonnet or Haiku; set `CLAUDE_CODE_SIMPLE_SYSTEM_PROMPT=0`
      to keep the full prompt
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.312
  - quote: Changed automatic model switches after a flagged message to also cover
      model names Claude Code doesn't recognize, such as custom deployment names;
      set `CLAUDE_CODE_DISABLE_REFUSAL_FALLBACK=1` to turn them off
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.312
  - quote: '[Claude Tag] Improved Claude Tag''s retry notice in Slack to name the
      model in use, or say rate limits were hit, instead of a generic API error'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.312
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-model-support-changes-in-v2-1-312
  source_release: claude-code-2026-10-27-v2-1-312-github-425846009-439d063a
  source_type: github_releases
  theme: model-support
  title: 3 Model Support changes in v2.1.312
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-19-2-model-support-changes-in-v2-1-304|2 Model Support
  changes in v2.1.304]]'
- '[[Changes/ChatGPT/2026-10-26-gpt-6-1-terra-is-rolling-out-in-chatgpt-work-and-codex-it-supports-a-range-of-ta|GPT-6.1
  Terra]]'
- '[[Changes/Claude Code/2026-10-26-5-model-support-changes-in-v2-1-311|5 Model Support
  changes in v2.1.311]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-27-v2-1-312-github-425846009-439d063a|claude-code-2026-10-27-v2-1-312-github-425846009-439d063a]]'
source_type: github_releases
theme: model-support
title: 3 Model Support changes in v2.1.312
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Model Support changes in v2.1.312

**Claude Code** · 2026-10-27 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.312) · from [[Releases/Claude Code/claude-code-2026-10-27-v2-1-312-github-425846009-439d063a|v2.1.312]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Changed Bedrock, Vertex, Foundry and Mantle to use the shorter system prompt for model names Claude Code doesn't recognize, such as custom deployment names and inference profile ARNs, even when they front Sonnet or Haiku; set `CLAUDE_CODE_SIMPLE_SYSTEM_PROMPT=0` to keep the full prompt

> Changed automatic model switches after a flagged message to also cover model names Claude Code doesn't recognize, such as custom deployment names; set `CLAUDE_CODE_DISABLE_REFUSAL_FALLBACK=1` to turn them off

> [Claude Tag] Improved Claude Tag's retry notice in Slack to name the model in use, or say rate limits were hit, instead of a generic API error

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.312
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-27-2-agent-mode-changes-in-v2-1-312|2 Agent Mode changes in v2.1.312]] · Agent Mode
- [[Changes/Claude Code/2026-10-27-2-apps-and-integrations-changes-in-v2-1-312|2 Apps and Integrations changes in v2.1.312]] · Apps and Integrations
- [[Changes/Claude Code/2026-10-27-cloud-sessions-added-a-bash-editor-with-colors-line-numbers-and-a-copy-button-to|Cloud sessions Added a Bash editor with colors, line numbers and a Copy button…]] · Editor Experience
- [[Changes/Claude Code/2026-10-27-2-interface-experience-changes-in-v2-1-312|2 Interface Experience changes in v2.1.312]] · Interface Experience
- [[Changes/Claude Code/2026-10-27-changed-claude-code-to-stop-sending-the-claude-code-safety-event-opentelemetry-e|Changed Claude Code to stop sending the claude_code.safety_event OpenTelemetry event]] · Safety and Privacy
- [[Changes/Claude Code/2026-10-27-changed-a-subagent-s-autocompactwindow-to-lower-the-window-set-by-claude-code-au|Changed a subagent's autoCompactWindow to lower the window set…]] · Context Window
- [[Changes/Claude Code/2026-10-27-5-other-changes-in-v2-1-312|5 other changes in v2.1.312]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-10-26 · Claude Code · [[Changes/Claude Code/2026-10-26-5-model-support-changes-in-v2-1-311|5 Model Support changes in v2.1.311]]
- Later: 2026-10-30 · Claude Code · [[Changes/Claude Code/2026-10-30-2-model-support-changes-in-v2-1-314|2 Model Support changes in v2.1.314]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-27-c903dd&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-27-3-model-support-changes-in-v2-1-312.md%0ACard%20ID%3A%20claude-code-2026-10-27-c903dd%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.312%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->