---
card_id: claude-code-2026-10-01-7e6515
date: '2026-10-01'
description: 'Claude Code · 2026-10-01 · Agent Mode: 4 changes in v2.1.287 — Added
  an `n:<text>` filter to the agents view that matches session names and tasks; a
  filter now…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1183
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 59d579ad4a7a6db1a7850210298e104ed754a09215d4e427a3776bc8dfbc2d04
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-01-7e6515
  comparison: ''
  date: '2026-10-01'
  description: 'Claude Code — v2.1.287: 4 Agent Mode changes'
  evidence:
  - quote: Added an `n:<text>` filter to the agents view that matches session names
      and tasks; a filter now shows matches in collapsed sections and Enter opens
      the first match
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.287
  - quote: Changed replies from `claude agents` to arrive as queued messages; slash
      commands other than `/stop` sent while a turn is running now run when it ends
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.287
  - quote: '[VSCode] Added "Run in background" to a running command or sub-agent,
      to move it to the background and keep working'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.287
  - quote: '[VSCode] Added the output of background shells and Monitors to their cards
      in the agent map'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.287
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 4-agent-mode-changes-in-v2-1-287
  source_release: claude-code-2026-10-01-v2-1-287-github-401174143-9cfdbb87
  source_type: github_releases
  theme: agent-mode
  title: 4 Agent Mode changes in v2.1.287
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-09-29-we-re-introducing-dots-always-on-agents-in-chatgpt-that-can-take-on-ongoing-work-24bef5|ChatGPT
  introduces dots]]'
- '[[Changes/Claude Code/2026-09-29-2-agent-mode-changes-in-v2-1-285|2 Agent Mode
  changes in v2.1.285]]'
- '[[Changes/Claude Code/2026-09-30-6-agent-mode-changes-in-v2-1-286|6 Agent Mode
  changes in v2.1.286]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-01-v2-1-287-github-401174143-9cfdbb87|claude-code-2026-10-01-v2-1-287-github-401174143-9cfdbb87]]'
source_type: github_releases
theme: agent-mode
title: 4 Agent Mode changes in v2.1.287
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Agent Mode changes in v2.1.287

**Claude Code** · 2026-10-01 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.287) · from [[Releases/Claude Code/claude-code-2026-10-01-v2-1-287-github-401174143-9cfdbb87|v2.1.287]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added an `n:<text>` filter to the agents view that matches session names and tasks; a filter now shows matches in collapsed sections and Enter opens the first match

> Changed replies from `claude agents` to arrive as queued messages; slash commands other than `/stop` sent while a turn is running now run when it ends

> [VSCode] Added "Run in background" to a running command or sub-agent, to move it to the background and keep working

> [VSCode] Added the output of background shells and Monitors to their cards in the agent map

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.287
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-01-4-model-support-changes-in-v2-1-287|4 Model Support changes in v2.1.287]] · Model Support
- [[Changes/Claude Code/2026-10-01-changed-opus-4-7-and-fable-to-use-a-1m-context-window-by-default-on-bedrock-vert|Changed Opus 4.7+ and Fable to use a 1M context window by default on Bedrock…]] · Context Window
- [[Changes/Claude Code/2026-10-01-2-mobile-and-desktop-changes-in-v2-1-287|2 Mobile and Desktop changes in v2.1.287]] · Mobile and Desktop
- [[Changes/Claude Code/2026-10-01-vscode-changed-the-claude-in-chrome-enabled-by-default-switch-to-also-connect-th|VSCode Changed the Claude in Chrome "Enabled by default" switch to also connect…]] · Editor Experience
- [[Changes/Claude Code/2026-10-01-6-safety-and-privacy-changes-in-v2-1-287|6 Safety and Privacy changes in v2.1.287]] · Safety and Privacy
- [[Changes/Claude Code/2026-10-01-3-developer-workflow-changes-in-v2-1-287|3 Developer Workflow changes in v2.1.287]] · Developer Workflow
- [[Changes/Claude Code/2026-10-01-11-apps-and-integrations-changes-in-v2-1-287|11 Apps and Integrations changes in v2.1.287]] · Apps and Integrations
- [[Changes/Claude Code/2026-10-01-changed-screen-reader-mode-to-write-new-or-changed-lines-without-first-pausing-w|Changed screen reader mode to write new or changed lines without first pausing…]] · Accessibility and Localization
- [[Changes/Claude Code/2026-10-01-3-reliability-and-performance-changes-in-v2-1-287|3 Reliability and Performance changes in v2.1.287]] · Reliability and Performance
- [[Changes/Claude Code/2026-10-01-improved-memory-the-left-and-right-arrow-keys-now-flip-its-on-off-settings-such|Improved /memory: the left and right arrow keys now flip its on/off settings, such…]] · Memory and Personalization
- [[Changes/Claude Code/2026-10-01-added-url-prompts-from-mcp-servers-on-the-2025-11-25-protocol-for-example-to-sig|Added URL prompts from MCP servers on the 2025-11-25 protocol, for example to sign in]] · Account and Access
- [[Changes/Claude Code/2026-10-01-improved-sdk-sessions-so-a-message-sent-with-priority-now-no-longer-cancels-a-ru|Improved SDK sessions so a message sent with priority "now" no longer cancels…]] · Search and Browsing
- [[Changes/Claude Code/2026-10-01-4-other-changes-in-v2-1-287|4 other changes in v2.1.287]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-09-30 · Claude Code · [[Changes/Claude Code/2026-09-30-6-agent-mode-changes-in-v2-1-286|6 Agent Mode changes in v2.1.286]]
- Later: 2026-10-02 · Claude Code · [[Changes/Claude Code/2026-10-02-4-agent-mode-changes-in-v2-1-288|4 Agent Mode changes in v2.1.288]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-01-7e6515&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-01-4-agent-mode-changes-in-v2-1-287.md%0ACard%20ID%3A%20claude-code-2026-10-01-7e6515%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.287%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->