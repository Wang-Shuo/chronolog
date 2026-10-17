---
card_id: claude-code-2026-07-17-b03858
date: '2026-07-17'
description: 'Claude Code · 2026-07-17 · Model Support: 3 changes in v2.1.212 — Improved
  prompt caching: the mid-conversation system block now works behind LLM gateways
  and…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1285
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9462ca17fdc758d5ad23689aab0cb8e76efcb5f84329fcb00609bfb7d37868da
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-07-17-b03858
  comparison: ''
  date: '2026-07-17'
  description: 'Claude Code — v2.1.212: 3 Model Support changes'
  evidence:
  - quote: 'Improved prompt caching: the mid-conversation system block now works behind
      LLM gateways and custom base URLs (Bedrock, Vertex, 1P)'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.212
  - quote: Changed session transcripts to record the reasoning effort level on each
      assistant message
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.212
  - quote: Changed headless/SDK sessions to apply a `set_model` control request mid-turn;
      the next model round-trip uses the new model instead of waiting for the next
      turn
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.212
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-model-support-changes-in-v2-1-212
  source_release: claude-code-2026-07-17-v2-1-212-github-355310036-d94b4e11
  source_type: github_releases
  theme: model-support
  title: 3 Model Support changes in v2.1.212
  type: change
related_changes:
- '[[Changes/Claude Code/2026-07-10-improved-code-review-findings-quality-on-claude-opus-4-8-across-all-effort-level|Improved
  /code-review findings quality on claude-opus-4-8 across all effort levels]]'
- '[[Changes/Claude Code/2026-07-11-changed-bedrock-vertex-and-claude-platform-on-aws-to-default-to-claude-opus-4-8|Changed
  Bedrock, Vertex, and Claude Platform on AWS to default to Claude Opus 4.8]]'
- '[[Changes/Claude Code/2026-07-14-improved-the-bash-powershell-tool-message-when-a-command-hits-its-timeout-and-is|Improved
  the Bash/PowerShell tool message when a command hits its timeout…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-17-v2-1-212-github-355310036-d94b4e11|claude-code-2026-07-17-v2-1-212-github-355310036-d94b4e11]]'
source_type: github_releases
theme: model-support
title: 3 Model Support changes in v2.1.212
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Model Support changes in v2.1.212

**Claude Code** · 2026-07-17 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.212) · from [[Releases/Claude Code/claude-code-2026-07-17-v2-1-212-github-355310036-d94b4e11|v2.1.212]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Improved prompt caching: the mid-conversation system block now works behind LLM gateways and custom base URLs (Bedrock, Vertex, 1P)

> Changed session transcripts to record the reasoning effort level on each assistant message

> Changed headless/SDK sessions to apply a `set_model` control request mid-turn; the next model round-trip uses the new model instead of waiting for the next turn

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.212
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-07-17-7-agent-mode-changes-in-v2-1-212|7 Agent Mode changes in v2.1.212]] · Agent Mode
- [[Changes/Claude Code/2026-07-17-typing-resume-in-the-agent-view-now-opens-a-picker-of-past-sessions-including-se|Typing /resume in the agent view now opens a picker of past sessions]] · Interface Experience
- [[Changes/Claude Code/2026-07-17-updated-the-auth-status-panel-title-from-cloud-authentication-to-authentication|Updated the auth status panel title from "Cloud authentication" to "Authentication"]] · Account and Access
- [[Changes/Claude Code/2026-07-17-3-search-and-browsing-changes-in-v2-1-212|3 Search and Browsing changes in v2.1.212]] · Search and Browsing
- [[Changes/Claude Code/2026-07-17-2-apps-and-integrations-changes-in-v2-1-212|2 Apps and Integrations changes in v2.1.212]] · Apps and Integrations
- [[Changes/Claude Code/2026-07-17-3-safety-and-privacy-changes-in-v2-1-212|3 Safety and Privacy changes in v2.1.212]] · Safety and Privacy
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-07-14 · Claude Code · [[Changes/Claude Code/2026-07-14-improved-the-bash-powershell-tool-message-when-a-command-hits-its-timeout-and-is|Improved the Bash/PowerShell tool message when a command hits its timeout…]]
- Later: 2026-07-22 · Claude Code · [[Changes/Claude Code/2026-07-22-added-an-announcement-when-fast-mode-changes-as-a-result-of-switching-models-via|Added an announcement when fast mode changes as a result of switching models…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-07-17-b03858&body=Card%3A%20Changes%2FClaude%20Code%2F2026-07-17-3-model-support-changes-in-v2-1-212.md%0ACard%20ID%3A%20claude-code-2026-07-17-b03858%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.212%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->