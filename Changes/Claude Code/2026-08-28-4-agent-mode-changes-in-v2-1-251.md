---
card_id: claude-code-2026-08-28-c58bda
date: '2026-08-28'
description: 'Claude Code · 2026-08-28 · Agent Mode: 4 changes in v2.1.251 — Added
  live streaming of a foreground subagent''s tool calls and results to Remote Control
  clients…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1149
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8e848d18a730f92d5eb87915cec22bf281d1a98aa2d00c11e9442b7b441ec091
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-08-28-c58bda
  comparison: ''
  date: '2026-08-28'
  description: 'Claude Code — v2.1.251: 4 Agent Mode changes'
  evidence:
  - quote: Added live streaming of a foreground subagent's tool calls and results
      to Remote Control clients (background subagents, the default, still show status
      only)
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.251
  - quote: 'Improved framing of messages from your own subagents: Claude is told the
      sender is a worker inside this session, not an unrelated Claude session'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.251
  - quote: Improved the prompt placeholder to read "Message @name…" while viewing
      a background subagent or fork transcript opened from the subagent panel or `/tasks`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.251
  - quote: 'Changed `CLAUDE_CODE_SUBAGENT_MODEL` to set the default subagent model
      rather than override everything: an agent definition''s `model:` and an explicit
      per-spawn model now take precedence over it'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.251
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 4-agent-mode-changes-in-v2-1-251
  source_release: claude-code-2026-08-28-v2-1-251-github-378586104-42ac2f96
  source_type: github_releases
  theme: agent-mode
  title: 4 Agent Mode changes in v2.1.251
  type: change
related_changes:
- '[[Changes/Claude Code/2026-08-27-3-agent-mode-changes-in-v2-1-248|3 Agent Mode
  changes in v2.1.248]]'
- '[[Changes/Cursor/2026-08-27-cloud-agents-no-longer-require-a-connected-github-or-other-third-party-scm-provi|Cloud
  Agents no longer require a connected GitHub or other third-party SCM provider…]]'
- '[[Changes/Cursor/2026-08-27-cursor-now-port-forwards-your-cloud-agent-s-live-environment-straight-to-your-br|A
  live preview, right in the browser]]'
source_release: '[[Releases/Claude Code/claude-code-2026-08-28-v2-1-251-github-378586104-42ac2f96|claude-code-2026-08-28-v2-1-251-github-378586104-42ac2f96]]'
source_type: github_releases
theme: agent-mode
title: 4 Agent Mode changes in v2.1.251
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Agent Mode changes in v2.1.251

**Claude Code** · 2026-08-28 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.251) · from [[Releases/Claude Code/claude-code-2026-08-28-v2-1-251-github-378586104-42ac2f96|v2.1.251]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added live streaming of a foreground subagent's tool calls and results to Remote Control clients (background subagents, the default, still show status only)

> Improved framing of messages from your own subagents: Claude is told the sender is a worker inside this session, not an unrelated Claude session

> Improved the prompt placeholder to read "Message @name…" while viewing a background subagent or fork transcript opened from the subagent panel or `/tasks`

> Changed `CLAUDE_CODE_SUBAGENT_MODEL` to set the default subagent model rather than override everything: an agent definition's `model:` and an explicit per-spawn model now take precedence over it

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.251
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-08-28-changed-analytics-to-no-longer-turn-off-before-sign-in-solely-because-managed-se|Changed analytics to no longer turn off before sign-in solely because managed…]] · Account and Access
- [[Changes/Claude Code/2026-08-28-4-model-support-changes-in-v2-1-251|4 Model Support changes in v2.1.251]] · Model Support
- [[Changes/Claude Code/2026-08-28-added-a-per-session-prompt-cache-line-to-cost-hit-ratio-misses-tokens-re-cached|Added a per-session prompt-cache line to /cost…]] · Pricing Model
- [[Changes/Claude Code/2026-08-28-4-apps-and-integrations-changes-in-v2-1-251|4 Apps and Integrations changes in v2.1.251]] · Apps and Integrations
- [[Changes/Claude Code/2026-08-28-3-developer-workflow-changes-in-v2-1-251|3 Developer Workflow changes in v2.1.251]] · Developer Workflow
- [[Changes/Claude Code/2026-08-28-improved-retry-when-the-model-s-tool-call-is-malformed-the-broken-output-is-now|Improved retry when the model's tool call is malformed]] · Context Window
- [[Changes/Claude Code/2026-08-28-improved-amazon-bedrock-session-start-under-claude-code-provider-managed-by-host|Improved Amazon Bedrock session start under CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST…]] · Mobile and Desktop
- [[Changes/Claude Code/2026-08-28-6-safety-and-privacy-changes-in-v2-1-251|6 Safety and Privacy changes in v2.1.251]] · Safety and Privacy
- [[Changes/Claude Code/2026-08-28-8-other-changes-in-v2-1-251|8 other changes in v2.1.251]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-08-27 · Cursor · [[Changes/Cursor/2026-08-27-cursor-now-port-forwards-your-cloud-agent-s-live-environment-straight-to-your-br|A live preview, right in the browser]]
- Later: 2026-09-01 · Claude Code · [[Changes/Claude Code/2026-09-01-5-agent-mode-changes-in-v2-1-257|5 Agent Mode changes in v2.1.257]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-08-28-c58bda&body=Card%3A%20Changes%2FClaude%20Code%2F2026-08-28-4-agent-mode-changes-in-v2-1-251.md%0ACard%20ID%3A%20claude-code-2026-08-28-c58bda%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.251%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->