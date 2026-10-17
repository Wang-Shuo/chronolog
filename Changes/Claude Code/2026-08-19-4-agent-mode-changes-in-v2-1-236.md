---
card_id: claude-code-2026-08-19-d177f9
date: '2026-08-19'
description: 'Claude Code · 2026-08-19 · Agent Mode: 4 changes in v2.1.236 — Improved
  auto mode: `Monitor` allow rules are now set aside while auto mode is active, so…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1140
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 3c78ee6a2093bdb08f22176f1bd3be4d267af81e99b0efab2c5ed506311748a6
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-08-19-d177f9
  comparison: ''
  date: '2026-08-19'
  description: 'Claude Code — v2.1.236: 4 Agent Mode changes'
  evidence:
  - quote: 'Improved auto mode: `Monitor` allow rules are now set aside while auto
      mode is active, so Monitor commands are reviewed the same way Bash commands
      are'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.236
  - quote: 'Improved auto mode on Bedrock, Vertex AI, and Foundry, and when telemetry
      is disabled: the classifier now uses the same defaults as on the Claude API,
      including severity-scored classification'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.236
  - quote: 'Improved auto mode: the git status check can no longer be fooled by a
      repo''s `status.showUntrackedFiles=no` setting into reporting a clean tree'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.236
  - quote: Right-aligned footer items (goal indicator, session state, background agent
      status) and truncated notices now share a consistent right margin with the rest
      of the prompt area
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.236
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 4-agent-mode-changes-in-v2-1-236
  source_release: claude-code-2026-08-19-v2-1-236-github-373272539-bbbacf79
  source_type: github_releases
  theme: agent-mode
  title: 4 Agent Mode changes in v2.1.236
  type: change
related_changes:
- '[[Changes/Claude Code/2026-08-14-improved-claude-self-hosted-runner-session-start-time-the-session-branch-is-now|Improved
  claude self-hosted-runner session start time]]'
- '[[Changes/Claude Code/2026-08-17-removed-the-redundant-allowed-by-auto-mode-classifier-line-that-auto-mode-showed|Removed
  the redundant "Allowed by auto mode classifier" line that auto mode showed…]]'
- '[[Changes/Cursor/2026-08-17-agents-in-every-repo|Agents in every repo]]'
source_release: '[[Releases/Claude Code/claude-code-2026-08-19-v2-1-236-github-373272539-bbbacf79|claude-code-2026-08-19-v2-1-236-github-373272539-bbbacf79]]'
source_type: github_releases
theme: agent-mode
title: 4 Agent Mode changes in v2.1.236
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Agent Mode changes in v2.1.236

**Claude Code** · 2026-08-19 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.236) · from [[Releases/Claude Code/claude-code-2026-08-19-v2-1-236-github-373272539-bbbacf79|v2.1.236]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Improved auto mode: `Monitor` allow rules are now set aside while auto mode is active, so Monitor commands are reviewed the same way Bash commands are

> Improved auto mode on Bedrock, Vertex AI, and Foundry, and when telemetry is disabled: the classifier now uses the same defaults as on the Claude API, including severity-scored classification

> Improved auto mode: the git status check can no longer be fooled by a repo's `status.showUntrackedFiles=no` setting into reporting a clean tree

> Right-aligned footer items (goal indicator, session state, background agent status) and truncated notices now share a consistent right margin with the rest of the prompt area

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.236
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-08-19-improved-startup-performance-the-session-counter-is-now-written-in-the-backgroun|Improved startup performance: the session counter is now written in the background]] · Reliability and Performance
- [[Changes/Claude Code/2026-08-19-added-anthropic-default-model-environment-variable-sets-the-model-new-sessions-s|Added ANTHROPIC_DEFAULT_MODEL environment variable]] · Model Support
- [[Changes/Claude Code/2026-08-19-added-notify-when-idle-to-cross-session-sendmessage-ask-another-claude-code-sess|Added notify_when_idle to cross-session SendMessage]] · Mobile and Desktop
- [[Changes/Claude Code/2026-08-19-2-safety-and-privacy-changes-in-v2-1-236|2 Safety and Privacy changes in v2.1.236]] · Safety and Privacy
- [[Changes/Claude Code/2026-08-19-2-developer-workflow-changes-in-v2-1-236|2 Developer Workflow changes in v2.1.236]] · Developer Workflow
- [[Changes/Claude Code/2026-08-19-changed-the-model-picker-to-highlight-only-the-newest-model-s-name-so-the-highli|Changed the /model picker to highlight only the newest model's name…]] · Interface Experience
- [[Changes/Claude Code/2026-08-19-sigterm-in-print-sdk-mode-no-longer-records-an-interrupted-turn-or-synthetic-too|SIGTERM in print/SDK mode no longer records an interrupted turn or synthetic tool…]] · Apps and Integrations
- [[Changes/Claude Code/2026-08-19-usage-now-shows-the-usage-credits-spend-row-for-team-and-enterprise-members-and|/usage now shows the usage-credits spend row for Team and Enterprise members…]] · Pricing Model
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-08-17 · Cursor · [[Changes/Cursor/2026-08-17-agents-in-every-repo|Agents in every repo]]
- Later: 2026-08-19 · Cursor · [[Changes/Cursor/2026-08-19-custom-modes|Custom modes]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-08-19-d177f9&body=Card%3A%20Changes%2FClaude%20Code%2F2026-08-19-4-agent-mode-changes-in-v2-1-236.md%0ACard%20ID%3A%20claude-code-2026-08-19-d177f9%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.236%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->