---
card_id: claude-code-2026-06-25-f62c9e
date: '2026-06-25'
description: 'Claude Code · 2026-06-25 · Agent Mode: 3 changes in v2.1.193 — Added
  `autoMode.classifyAllShell` setting to route all Bash/PowerShell commands through
  the…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1085
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8f1f559d4cd396e6eae67682eb464f3745fa87df3faad49d5d931b205ee98bba
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-06-25-f62c9e
  comparison: ''
  date: '2026-06-25'
  description: 'Claude Code — v2.1.193: 3 Agent Mode changes'
  evidence:
  - quote: Added `autoMode.classifyAllShell` setting to route all Bash/PowerShell
      commands through the auto-mode classifier instead of only arbitrary-code-execution
      patterns
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.193
  - quote: Added auto-mode denial reasons to the transcript, the denial toast, and
      `/permissions` recent denials
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.193
  - quote: 'Improved background agents: the launch result no longer instructs Claude
      to "end your response" — it keeps working on other tasks while the agent runs'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.193
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-agent-mode-changes-in-v2-1-193
  source_release: claude-code-2026-06-25-v2-1-193-github-344922230-0655000d
  source_type: github_releases
  theme: agent-mode
  title: 3 Agent Mode changes in v2.1.193
  type: change
related_changes:
- '[[Changes/Cursor/2026-06-17-cloud-subagents-with-in-cloud-eb7958|Cloud subagents
  with /in-cloud]]'
- '[[Changes/Claude Code/2026-06-19-improved-auto-mode-safety-destructive-git-commands-git-reset-hard-git-checkout-g|Improved
  auto mode safety]]'
- '[[Changes/Claude Code/2026-06-22-2-agent-mode-changes-in-v2-1-186|2 Agent Mode
  changes in v2.1.186]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-25-v2-1-193-github-344922230-0655000d|claude-code-2026-06-25-v2-1-193-github-344922230-0655000d]]'
source_type: github_releases
theme: agent-mode
title: 3 Agent Mode changes in v2.1.193
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Agent Mode changes in v2.1.193

**Claude Code** · 2026-06-25 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.193) · from [[Releases/Claude Code/claude-code-2026-06-25-v2-1-193-github-344922230-0655000d|v2.1.193]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `autoMode.classifyAllShell` setting to route all Bash/PowerShell commands through the auto-mode classifier instead of only arbitrary-code-execution patterns

> Added auto-mode denial reasons to the transcript, the denial toast, and `/permissions` recent denials

> Improved background agents: the launch result no longer instructs Claude to "end your response" — it keeps working on other tasks while the agent runs

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.193
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-06-25-2-apps-and-integrations-changes-in-v2-1-193|2 Apps and Integrations changes in v2.1.193]] · Apps and Integrations
- [[Changes/Claude Code/2026-06-25-added-live-file-path-autocomplete-to-bash-mode|Added live file path autocomplete to bash mode (!)]] · Editor Experience
- [[Changes/Claude Code/2026-06-25-added-claude-code-assistant-response-opentelemetry-log-event-containing-the-mode|Added claude_code.assistant_response OpenTelemetry log event containing…]] · Model Support
- [[Changes/Claude Code/2026-06-25-added-a-startup-notice-when-mcp-servers-need-authentication-pointing-at-mcp|Added a startup notice when MCP servers need authentication, pointing at /mcp]] · Account and Access
- [[Changes/Claude Code/2026-06-25-added-automatic-memory-pressure-reaping-for-idle-background-shell-commands-disab|Added automatic memory-pressure reaping for idle background shell commands…]] · Reliability and Performance
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-06-22 · Claude Code · [[Changes/Claude Code/2026-06-22-2-agent-mode-changes-in-v2-1-186|2 Agent Mode changes in v2.1.186]]
- Later: 2026-06-26 · Claude Code · [[Changes/Claude Code/2026-06-26-improved-claude-agents-completed-list-to-fill-available-vertical-space-on-short|Improved claude agents completed list to fill available vertical space]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-06-25-f62c9e&body=Card%3A%20Changes%2FClaude%20Code%2F2026-06-25-3-agent-mode-changes-in-v2-1-193.md%0ACard%20ID%3A%20claude-code-2026-06-25-f62c9e%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.193%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->