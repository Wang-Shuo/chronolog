---
card_id: claude-code-2026-05-13-f0c29e
date: '2026-05-13'
description: 'Claude Code · 2026-05-13 · Agent Mode: 4 changes in v2.1.141 — Added
  `claude agents --cwd <path>` to scope the session list to a directory'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1042
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2da2d7d8d128ee5912928793c8e93743ae5d94d42697192511b30b9a9bcae180
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-05-13-f0c29e
  comparison: ''
  date: '2026-05-13'
  description: 'Claude Code — v2.1.141: 4 Agent Mode changes'
  evidence:
  - quote: Added `claude agents --cwd <path>` to scope the session list to a directory
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.141
  - quote: '`claude agents`: agents that finish work but leave a background shell
      running now move to Completed instead of staying under Working'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.141
  - quote: '`claude agents`: launching a session no longer fails when the pre-warmed
      background worker is unhealthy — now falls back to a fresh launch'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.141
  - quote: '`claude agents` no longer shows empty placeholder sessions left over from
      backgrounding a fresh REPL, and shows onboarding text when entered via ← with
      no other agents'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.141
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 4-agent-mode-changes-in-v2-1-141
  source_release: claude-code-2026-05-13-v2-1-141-github-322186176-9f8e2e22
  source_type: github_releases
  theme: agent-mode
  title: 4 Agent Mode changes in v2.1.141
  type: change
related_changes:
- '[[Changes/Cursor/2026-05-07-added-the-ability-to-control-explore-subagent-behavior-from-settings-choose-a-sp|Added
  the ability to control Explore subagent behavior from settings]]'
- '[[Changes/Claude Code/2026-05-11-2-agent-mode-changes-in-v2-1-139|2 Agent Mode
  changes in v2.1.139]]'
- '[[Changes/Claude Code/2026-05-12-2-agent-mode-changes-in-v2-1-140|2 Agent Mode
  changes in v2.1.140]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-13-v2-1-141-github-322186176-9f8e2e22|claude-code-2026-05-13-v2-1-141-github-322186176-9f8e2e22]]'
source_type: github_releases
theme: agent-mode
title: 4 Agent Mode changes in v2.1.141
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Agent Mode changes in v2.1.141

**Claude Code** · 2026-05-13 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.141) · from [[Releases/Claude Code/claude-code-2026-05-13-v2-1-141-github-322186176-9f8e2e22|v2.1.141]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `claude agents --cwd <path>` to scope the session list to a directory

> `claude agents`: agents that finish work but leave a background shell running now move to Completed instead of staying under Working

> `claude agents`: launching a session no longer fails when the pre-warmed background worker is unhealthy — now falls back to a fresh launch

> `claude agents` no longer shows empty placeholder sessions left over from backgrounding a fresh REPL, and shows onboarding text when entered via ← with no other agents

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.141
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-05-13-5-safety-and-privacy-changes-in-v2-1-141|5 Safety and Privacy changes in v2.1.141]] · Safety and Privacy
- [[Changes/Claude Code/2026-05-13-2-interface-experience-changes-in-v2-1-141|2 Interface Experience changes in v2.1.141]] · Interface Experience
- [[Changes/Claude Code/2026-05-13-vscode-voice-mode-the-wsl-error-now-suggests-installing-sox-libsox-fmt-pulse-for|VSCode Voice mode]] · Voice and Audio
- [[Changes/Claude Code/2026-05-13-rewind-menu-added-summarize-up-to-here-to-compress-earlier-context-while-keeping|Rewind menu: added "Summarize up to here" to compress earlier context while keeping…]] · Context Window
- [[Changes/Claude Code/2026-05-13-feedback-can-now-include-recent-sessions-last-24-hours-or-7-days-for-issues-span|/feedback can now include recent sessions (last 24 hours or 7 days) for issues…]] · Projects and Workspaces
- [[Changes/Claude Code/2026-05-13-bedrock-awscredentialexport-now-always-runs-when-configured-instead-of-being-ski|Bedrock: awsCredentialExport now always runs when configured instead of being…]] · Account and Access
- [[Changes/Claude Code/2026-05-13-2-apps-and-integrations-changes-in-v2-1-141|2 Apps and Integrations changes in v2.1.141]] · Apps and Integrations
- [[Changes/Claude Code/2026-05-13-added-anthropic-workspace-id-environment-variable-for-workload-identity-federati|Added ANTHROPIC_WORKSPACE_ID environment variable for workload identity federation]] · Enterprise and Administration
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-05-12 · Claude Code · [[Changes/Claude Code/2026-05-12-2-agent-mode-changes-in-v2-1-140|2 Agent Mode changes in v2.1.140]]
- Later: 2026-05-13 · Cursor · [[Changes/Cursor/2026-05-13-improved-agent-led-environment-setup|Improved agent-led environment setup]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-05-13-f0c29e&body=Card%3A%20Changes%2FClaude%20Code%2F2026-05-13-4-agent-mode-changes-in-v2-1-141.md%0ACard%20ID%3A%20claude-code-2026-05-13-f0c29e%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.141%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->