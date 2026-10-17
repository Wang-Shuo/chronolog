---
card_id: claude-code-2026-07-14-68214c
date: '2026-07-14'
description: 'Claude Code · 2026-07-14 · Agent Mode: 4 changes in v2.1.208 — Added
  `CLAUDE_CODE_PROCESS_WRAPPER`: agent view and the background service now honor a
  corporate…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1104
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 1feaf5b410f9a3ea725f2733529e3f69f7836cf011077198ebb3a91213db4c95
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-07-14-68214c
  comparison: ''
  date: '2026-07-14'
  description: 'Claude Code — v2.1.208: 4 Agent Mode changes'
  evidence:
  - quote: 'Added `CLAUDE_CODE_PROCESS_WRAPPER`: agent view and the background service
      now honor a corporate launcher by running every Claude Code self-spawn through
      a required wrapper executable'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.208
  - quote: Completed background agents now stay listed in `/tasks` until cleanup instead
      of vanishing the moment they finish
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.208
  - quote: Attaching to a stopped background agent now shows its transcript immediately
      while the session warms up, instead of a blank "Session is starting" screen
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.208
  - quote: Catastrophic removals (e.g. `rm -rf ~`) in commands containing `$(…)`/backticks/`<(…)`
      now prompt in `--dangerously-skip-permissions` and auto mode, matching the plain
      form
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.208
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 4-agent-mode-changes-in-v2-1-208
  source_release: claude-code-2026-07-14-v2-1-208-github-353442054-2756b984
  source_type: github_releases
  theme: agent-mode
  title: 4 Agent Mode changes in v2.1.208
  type: change
related_changes:
- '[[Changes/Cursor/2026-07-10-this-release-makes-it-easier-to-stay-in-flow-with-side-chats-that-run-alongside|Cursor
  makes it easier to stay in flow with side chats that run alongside your main…]]'
- '[[Changes/Claude Code/2026-07-11-2-agent-mode-changes-in-v2-1-207|2 Agent Mode
  changes in v2.1.207]]'
- '[[Changes/Claude Code/2026-07-11-auto-mode-is-now-available-without-claude-code-enable-auto-mode-opt-in-on-bedroc|Auto
  mode is now available without CLAUDE_CODE_ENABLE_AUTO_MODE opt-in on Bedrock…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-14-v2-1-208-github-353442054-2756b984|claude-code-2026-07-14-v2-1-208-github-353442054-2756b984]]'
source_type: github_releases
theme: agent-mode
title: 4 Agent Mode changes in v2.1.208
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Agent Mode changes in v2.1.208

**Claude Code** · 2026-07-14 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.208) · from [[Releases/Claude Code/claude-code-2026-07-14-v2-1-208-github-353442054-2756b984|v2.1.208]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `CLAUDE_CODE_PROCESS_WRAPPER`: agent view and the background service now honor a corporate launcher by running every Claude Code self-spawn through a required wrapper executable

> Completed background agents now stay listed in `/tasks` until cleanup instead of vanishing the moment they finish

> Attaching to a stopped background agent now shows its transcript immediately while the session warms up, instead of a blank "Session is starting" screen

> Catastrophic removals (e.g. `rm -rf ~`) in commands containing `$(…)`/backticks/`<(…)` now prompt in `--dangerously-skip-permissions` and auto mode, matching the plain form

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.208
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-07-14-3-apps-and-integrations-changes-in-v2-1-208|3 Apps and Integrations changes in v2.1.208]] · Apps and Integrations
- [[Changes/Claude Code/2026-07-14-agent-view-ctrl-x-now-deletes-renamed-branch-worktrees-never-destroys-unpushed-c|Agent view: Ctrl+X now deletes renamed-branch worktrees, never destroys unpushed…]] · Developer Workflow
- [[Changes/Claude Code/2026-07-14-added-mouse-click-support-for-multi-select-menus-and-other-input-rows-in-fullscr|Added mouse-click support for multi-select menus and "Other" input rows in fullscreen mode]] · Interface Experience
- [[Changes/Claude Code/2026-07-14-2-editor-experience-changes-in-v2-1-208|2 Editor Experience changes in v2.1.208]] · Editor Experience
- [[Changes/Claude Code/2026-07-14-3-reliability-and-performance-changes-in-v2-1-208|3 Reliability and Performance changes in v2.1.208]] · Reliability and Performance
- [[Changes/Claude Code/2026-07-14-fixed-multi-second-per-turn-slowdowns-in-sessions-with-many-permission-deny-ask|Fixed multi-second per-turn slowdowns in sessions with many permission deny/ask rules]] · Safety and Privacy
- [[Changes/Claude Code/2026-07-14-added-screen-reader-mode-opt-in-plain-text-rendering-for-screen-reader-users-run|Added screen reader mode: opt-in plain-text rendering for screen reader users]] · Accessibility and Localization
- [[Changes/Claude Code/2026-07-14-2-other-changes-in-v2-1-208|2 other changes in v2.1.208]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-07-11 · Claude Code · [[Changes/Claude Code/2026-07-11-auto-mode-is-now-available-without-claude-code-enable-auto-mode-opt-in-on-bedroc|Auto mode is now available without CLAUDE_CODE_ENABLE_AUTO_MODE opt-in on Bedrock…]]
- Later: 2026-07-14 · Claude Code · [[Changes/Claude Code/2026-07-14-3-agent-mode-changes-in-v2-1-210|3 Agent Mode changes in v2.1.210]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-07-14-68214c&body=Card%3A%20Changes%2FClaude%20Code%2F2026-07-14-4-agent-mode-changes-in-v2-1-208.md%0ACard%20ID%3A%20claude-code-2026-07-14-68214c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.208%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->