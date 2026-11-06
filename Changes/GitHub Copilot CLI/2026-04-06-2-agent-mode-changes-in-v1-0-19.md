---
card_id: github-copilot-cli-2026-04-06-e42644
date: '2026-04-06'
description: 'GitHub Copilot CLI · 2026-04-06 · Agent Mode: 2 changes in 1.0.19 —
  OpenTelemetry monitoring: subagent spans now use INTERNAL span kind, and chat spans
  include…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1005
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ab84b697f7f41d4af165793abd53822ce6e3e207b1580dc333572ba24af12e91
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-04-06-e42644
  comparison: ''
  date: '2026-04-06'
  description: 'GitHub Copilot CLI — 1.0.19: 2 Agent Mode changes'
  evidence:
  - quote: 'OpenTelemetry monitoring: subagent spans now use INTERNAL span kind, and
      chat spans include a `github.copilot.time_to_first_chunk` attribute (streaming
      only)'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.19
  - quote: Custom agent is properly restored when resuming a session where the agent
      display name differs from its filename
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.19
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 2-agent-mode-changes-in-v1-0-19
  source_release: github-copilot-cli-2026-04-06-v1-0-19-github-305837484-a9d8ae9e
  source_type: github_releases
  theme: agent-mode
  title: 2 Agent Mode changes in v1.0.19
  type: change
related_changes:
- '[[Changes/Cursor/2026-04-02-design-mode|Design Mode]]'
- '[[Changes/Cursor/2026-04-02-agents-window-da5689|Agents Window]]'
- '[[Changes/GitHub Copilot CLI/2026-04-03-built-in-skills-are-now-included-with-the-cli-starting-with-a-guide-for-customiz|Built-in
  skills are now included with the CLI, starting with a guide for customizing…]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-04-06-v1-0-19-github-305837484-a9d8ae9e|github-copilot-cli-2026-04-06-v1-0-19-github-305837484-a9d8ae9e]]'
source_type: github_releases
theme: agent-mode
title: 2 Agent Mode changes in v1.0.19
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Agent Mode changes in v1.0.19

**GitHub Copilot CLI** · 2026-04-06 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.19) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-04-06-v1-0-19-github-305837484-a9d8ae9e|1.0.19]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> OpenTelemetry monitoring: subagent spans now use INTERNAL span kind, and chat spans include a `github.copilot.time_to_first_chunk` attribute (streaming only)

> Custom agent is properly restored when resuming a session where the agent display name differs from its filename

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.19
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-04-06-skip-ide-auto-connect-when-session-is-already-in-use-by-another-client|Skip IDE auto-connect when session is already in use by another client]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-04-06-2-apps-and-integrations-changes-in-v1-0-19|2 Apps and Integrations changes in v1.0.19]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-04-06-slash-command-timeline-entries-now-include-the-command-name-e-g-review-plan-for|Slash command timeline entries now include the command name (e.g., "Review", "Plan")…]] · Context Window
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-04-03 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-04-03-built-in-skills-are-now-included-with-the-cli-starting-with-a-guide-for-customiz|Built-in skills are now included with the CLI, starting with a guide for customizing…]]
- Later: 2026-04-07 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-04-07-spinner-no-longer-appears-stuck-when-a-long-running-async-shell-command-is-activ|Spinner no longer appears stuck when a long-running async shell command is active]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-04-06-e42644&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-04-06-2-agent-mode-changes-in-v1-0-19.md%0ACard%20ID%3A%20github-copilot-cli-2026-04-06-e42644%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.19%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->