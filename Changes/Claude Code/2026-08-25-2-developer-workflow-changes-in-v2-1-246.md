---
card_id: claude-code-2026-08-25-9d49af
date: '2026-08-25'
description: 'Claude Code · 2026-08-25 · Developer Workflow: 2 changes in v2.1.246
  — Added a startup warning for Bash allow rules with a wildcard before the subcommand
  (e.g…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1256
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 1f0d1fcee4fcc2e75f6a032a43930fd61894d43cda8cbf647b261cd04aaa7c1d
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-08-25-9d49af
  comparison: ''
  date: '2026-08-25'
  description: 'Claude Code — v2.1.246: 2 Developer Workflow changes'
  evidence:
  - quote: Added a startup warning for Bash allow rules with a wildcard before the
      subcommand (e.g. `Bash(git * main)`), since they also match options inserted
      before the subcommand
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.246
  - quote: Changed `/code-review` so Claude can also start it on its own on Bedrock,
      Vertex AI, and Foundry, through the Claude apps gateway, and when telemetry
      or non-essential traffic is disabled
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.246
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-developer-workflow-changes-in-v2-1-246
  source_release: claude-code-2026-08-25-v2-1-246-github-376644211-dd9805a0
  source_type: github_releases
  theme: developer-workflow
  title: 2 Developer Workflow changes in v2.1.246
  type: change
related_changes:
- '[[Changes/Claude Code/2026-08-19-2-developer-workflow-changes-in-v2-1-236|2 Developer
  Workflow changes in v2.1.236]]'
- '[[Changes/Claude Code/2026-08-20-2-developer-workflow-changes-in-v2-1-238|2 Developer
  Workflow changes in v2.1.238]]'
- '[[Changes/Claude Code/2026-08-21-2-developer-workflow-changes-in-v2-1-239|2 Developer
  Workflow changes in v2.1.239]]'
source_release: '[[Releases/Claude Code/claude-code-2026-08-25-v2-1-246-github-376644211-dd9805a0|claude-code-2026-08-25-v2-1-246-github-376644211-dd9805a0]]'
source_type: github_releases
theme: developer-workflow
title: 2 Developer Workflow changes in v2.1.246
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Developer Workflow changes in v2.1.246

**Claude Code** · 2026-08-25 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.246) · from [[Releases/Claude Code/claude-code-2026-08-25-v2-1-246-github-376644211-dd9805a0|v2.1.246]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added a startup warning for Bash allow rules with a wildcard before the subcommand (e.g. `Bash(git * main)`), since they also match options inserted before the subcommand

> Changed `/code-review` so Claude can also start it on its own on Bedrock, Vertex AI, and Foundry, through the Claude apps gateway, and when telemetry or non-essential traffic is disabled

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.246
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-08-25-improved-subagent-results-a-subagent-that-stops-at-its-maxturns-limit-now-return|Improved subagent results]] · Agent Mode
- [[Changes/Claude Code/2026-08-25-improved-bash-tool-latency-on-bash-shells-by-replaying-snapshot-functions-withou|Improved Bash tool latency on bash shells by replaying snapshot functions without…]] · Reliability and Performance
- [[Changes/Claude Code/2026-08-25-6-safety-and-privacy-changes-in-v2-1-246|6 Safety and Privacy changes in v2.1.246]] · Safety and Privacy
- [[Changes/Claude Code/2026-08-25-windows-macos-fixed-headless-sessions-not-cleaning-up-stale-entries-in-claude-se|Windows/macOS: Fixed headless sessions not cleaning up stale entries…]] · Mobile and Desktop
- [[Changes/Claude Code/2026-08-25-added-the-turn-s-completion-time-to-the-end-of-turn-duration-line-e-g-saut-ed-fo|Added the turn's completion time to the end-of-turn duration line…]] · Editor Experience
- [[Changes/Claude Code/2026-08-25-3-apps-and-integrations-changes-in-v2-1-246|3 Apps and Integrations changes in v2.1.246]] · Apps and Integrations
- [[Changes/Claude Code/2026-08-25-improved-attribution-of-usage-telemetry-to-your-organization-for-workload-identi|Improved attribution of usage telemetry to your organization for workload identity…]] · Account and Access
- [[Changes/Claude Code/2026-08-25-goal-changed-idle-sessions-to-start-at-most-three-check-ins-on-long-running-back|/goal: Changed idle sessions to start at most three check-ins on long-running…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-08-21 · Claude Code · [[Changes/Claude Code/2026-08-21-2-developer-workflow-changes-in-v2-1-239|2 Developer Workflow changes in v2.1.239]]
- Later: 2026-08-26 · Claude Code · [[Changes/Claude Code/2026-08-26-changed-terminal-hyperlinks-in-rendered-markdown-link-targets-that-point-at-a-ne|Changed terminal hyperlinks in rendered markdown]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-08-25-9d49af&body=Card%3A%20Changes%2FClaude%20Code%2F2026-08-25-2-developer-workflow-changes-in-v2-1-246.md%0ACard%20ID%3A%20claude-code-2026-08-25-9d49af%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.246%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->