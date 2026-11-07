---
card_id: github-copilot-cli-2026-03-16-b43280
date: '2026-03-16'
description: 'GitHub Copilot CLI · 2026-03-16 · Agent Mode: 5 changes in 1.0.6 — Resolve
  session crashes caused by HTTP/2 connection pool race conditions when sub-agents
  are…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 984
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 04b7562318b58cd777a65658c81c3af460b720a88df602ef45dae58518578933
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-03-16-b43280
  comparison: ''
  date: '2026-03-16'
  description: 'GitHub Copilot CLI — 1.0.6: 5 Agent Mode changes'
  evidence:
  - quote: Resolve session crashes caused by HTTP/2 connection pool race conditions
      when sub-agents are active
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.6
  - quote: Subagent elapsed time in /tasks view freezes when idle and resumes when
      active again
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.6
  - quote: Agent creation wizard shows the correct user agents directory path
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.6
  - quote: Sub-agents launched by the task tool are assigned human-readable IDs based
      on their name (e.g., `math-helper-0`) instead of generic `agent-0` identifiers
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.6
  - quote: read_agent output includes inbound messages that triggered each turn in
      multi-turn agents
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.6
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 5-agent-mode-changes-in-v1-0-6
  source_release: github-copilot-cli-2026-03-16-v1-0-6-github-297705118-b80b4107
  source_type: github_releases
  theme: agent-mode
  title: 5 Agent Mode changes in v1.0.6
  type: change
related_changes:
- '[[Changes/Claude Code/2026-03-14-improved-background-agent-behavior-killing-a-background-agent-now-preserves-its|Improved
  background agent behavior]]'
- '[[Changes/Codex CLI/2026-03-16-16-agent-mode-changes-in-rust-v0-115-0|16 Agent
  Mode changes in rust-v0.115.0]]'
- '[[Changes/ElevenLabs/2026-03-16-elevenagents|ElevenAgents]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-03-16-v1-0-6-github-297705118-b80b4107|github-copilot-cli-2026-03-16-v1-0-6-github-297705118-b80b4107]]'
source_type: github_releases
theme: agent-mode
title: 5 Agent Mode changes in v1.0.6
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Agent Mode changes in v1.0.6

**GitHub Copilot CLI** · 2026-03-16 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.6) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-03-16-v1-0-6-github-297705118-b80b4107|1.0.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Resolve session crashes caused by HTTP/2 connection pool race conditions when sub-agents are active

> Subagent elapsed time in /tasks view freezes when idle and resumes when active again

> Agent creation wizard shows the correct user agents directory path

> Sub-agents launched by the task tool are assigned human-readable IDs based on their name (e.g., `math-helper-0`) instead of generic `agent-0` identifiers

> read_agent output includes inbound messages that triggered each turn in multi-turn agents

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.6
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-03-16-remaining-requests-widget-no-longer-shows-inaccurate-quota-data-for-copilot-free|Remaining requests widget no longer shows inaccurate quota data for Copilot Free users]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-03-16-model-can-discover-and-use-tools-dynamically-with-tool-search-for-claude-models|Model can discover and use tools dynamically with tool search for Claude models]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-03-16-extension-tools-now-work-with-the-permissions-system-use-skippermission-per-tool|Extension tools now work with the permissions system, use skipPermission per-tool…]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-03-16-custom-instruction-file-paths-load-correctly-when-using-copilot-custom-instructi|Custom instruction file paths load correctly when using COPILOT_CUSTOM_INSTRUCTIONS_DIRS]] · Memory and Personalization
- [[Changes/GitHub Copilot CLI/2026-03-16-4-developer-workflow-changes-in-v1-0-6|4 Developer Workflow changes in v1.0.6]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-03-16-show-friendlier-error-messages-and-provide-keyboard-shortcut-to-open-event-links|Show friendlier error messages and provide keyboard shortcut to open event links…]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-03-16-6-apps-and-integrations-changes-in-v1-0-6|6 Apps and Integrations changes in v1.0.6]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-03-16-3-mobile-and-desktop-changes-in-v1-0-6|3 Mobile and Desktop changes in v1.0.6]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-03-16-3-reliability-and-performance-changes-in-v1-0-6|3 Reliability and Performance changes in v1.0.6]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-03-16-8-other-changes-in-v1-0-6|8 other changes in v1.0.6]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-03-16 · ElevenLabs · [[Changes/ElevenLabs/2026-03-16-elevenagents|ElevenAgents]]
- Later: 2026-03-16 · OpenCode · [[Changes/OpenCode/2026-03-16-core-ensure-that-compaction-message-is-tracked-as-agent-initiated|Core Ensure that compaction message is tracked as agent initiated]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-03-16-b43280&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-03-16-5-agent-mode-changes-in-v1-0-6.md%0ACard%20ID%3A%20github-copilot-cli-2026-03-16-b43280%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.6%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->