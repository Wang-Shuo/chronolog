---
card_id: claude-code-2026-10-14-77cdf5
date: '2026-10-14'
description: 'Claude Code · 2026-10-14 · Agent Mode: 5 changes in v2.1.299 — Added
  a "safe mode" line to the agents view peek panel for background sessions started
  with…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1196
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d509a5e35d9334c6d92c52984ba64248c44f1f3bdf521655d1cfcd6cc41d789d
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-14-77cdf5
  comparison: ''
  date: '2026-10-14'
  description: 'Claude Code — v2.1.299: 5 Agent Mode changes'
  evidence:
  - quote: Added a "safe mode" line to the agents view peek panel for background sessions
      started with `--safe-mode`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.299
  - quote: 'Improved background agent notifications: they now say when an agent is
      only waiting on its own background work, got a message too late for its result,
      or was stopped by a usage limit'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.299
  - quote: 'Changed Claude in Chrome in Cowork cloud sessions outside auto mode: an
      approved-site action the safety classifier flags now asks you instead of being
      refused, unless managed settings apply'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.299
  - quote: 'Changed auto mode in Cowork cloud sessions: a `PermissionRequest` hook
      can no longer approve shell commands or subagents; those prompts wait or are
      denied'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.299
  - quote: Changed the `turn.start` mod hook to also hear subagents' and teammates'
      turns, not only the main loop's; tell them apart by `e.agentId` (absent on the
      main loop)
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.299
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 5-agent-mode-changes-in-v2-1-299
  source_release: claude-code-2026-10-14-v2-1-299-github-412217284-623d9162
  source_type: github_releases
  theme: agent-mode
  title: 5 Agent Mode changes in v2.1.299
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-07-2-agent-mode-changes-in-v2-1-293|2 Agent Mode
  changes in v2.1.293]]'
- '[[Changes/Claude Code/2026-10-08-3-agent-mode-changes-in-v2-1-295|3 Agent Mode
  changes in v2.1.295]]'
- '[[Changes/Claude Code/2026-10-09-3-agent-mode-changes-in-v2-1-296|3 Agent Mode
  changes in v2.1.296]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-14-v2-1-299-github-412217284-623d9162|claude-code-2026-10-14-v2-1-299-github-412217284-623d9162]]'
source_type: github_releases
theme: agent-mode
title: 5 Agent Mode changes in v2.1.299
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Agent Mode changes in v2.1.299

**Claude Code** · 2026-10-14 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.299) · from [[Releases/Claude Code/claude-code-2026-10-14-v2-1-299-github-412217284-623d9162|v2.1.299]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added a "safe mode" line to the agents view peek panel for background sessions started with `--safe-mode`

> Improved background agent notifications: they now say when an agent is only waiting on its own background work, got a message too late for its result, or was stopped by a usage limit

> Changed Claude in Chrome in Cowork cloud sessions outside auto mode: an approved-site action the safety classifier flags now asks you instead of being refused, unless managed settings apply

> Changed auto mode in Cowork cloud sessions: a `PermissionRequest` hook can no longer approve shell commands or subagents; those prompts wait or are denied

> Changed the `turn.start` mod hook to also hear subagents' and teammates' turns, not only the main loop's; tell them apart by `e.agentId` (absent on the main loop)

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.299
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-14-added-a-one-time-note-when-plan-mode-won-t-ask-before-most-edits-or-commands-bec|Added a one-time note when plan mode won't ask before most edits or commands because…]] · Editor Experience
- [[Changes/Claude Code/2026-10-14-19-apps-and-integrations-changes-in-v2-1-299|19 Apps and Integrations changes in v2.1.299]] · Apps and Integrations
- [[Changes/Claude Code/2026-10-14-2-context-window-changes-in-v2-1-299|2 Context Window changes in v2.1.299]] · Context Window
- [[Changes/Claude Code/2026-10-14-10-developer-workflow-changes-in-v2-1-299|10 Developer Workflow changes in v2.1.299]] · Developer Workflow
- [[Changes/Claude Code/2026-10-14-2-model-support-changes-in-v2-1-299|2 Model Support changes in v2.1.299]] · Model Support
- [[Changes/Claude Code/2026-10-14-2-files-and-data-changes-in-v2-1-299|2 Files and Data changes in v2.1.299]] · Files and Data
- [[Changes/Claude Code/2026-10-14-added-support-for-turning-off-the-attribution-block-in-claude-desktop-s-code-tab|Added support for turning off the attribution block in Claude Desktop's Code tab]] · Mobile and Desktop
- [[Changes/Claude Code/2026-10-14-added-effort-and-fast-in-agent-view-to-set-what-new-sessions-start-with-a-bare-m|Added /effort and /fast in agent view to set what new sessions start with]] · Interface Experience
- [[Changes/Claude Code/2026-10-14-improved-memory-and-disk-use-when-pdfs-are-mentioned-their-bytes-are-no-longer-k|Improved memory and disk use when PDFs are @-mentioned]] · Memory and Personalization
- [[Changes/Claude Code/2026-10-14-added-usage-warnings-for-max-effort-workflows-always-on-context-and-large-tool-r|Added /usage warnings for max effort, workflows, always-on context and large tool…]] · Context Window
- [[Changes/Claude Code/2026-10-14-improved-the-error-shown-when-a-cloud-session-is-refused-because-your-claude-ai|Improved the error shown when a cloud session is refused because your claude.ai…]] · Account and Access
- [[Changes/Claude Code/2026-10-14-vscode-improved-startup-the-model-picker-and-slash-command-menu-now-fill-in-righ|VSCode Improved startup]] · Interface Experience
- [[Changes/Claude Code/2026-10-14-6-safety-and-privacy-changes-in-v2-1-299|6 Safety and Privacy changes in v2.1.299]] · Safety and Privacy
- [[Changes/Claude Code/2026-10-14-11-other-changes-in-v2-1-299|11 other changes in v2.1.299]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-10-09 · Claude Code · [[Changes/Claude Code/2026-10-09-3-agent-mode-changes-in-v2-1-296|3 Agent Mode changes in v2.1.296]]
- Later: 2026-10-14 · Claude Code · [[Changes/Claude Code/2026-10-14-3-agent-mode-changes-in-v2-1-300|3 Agent Mode changes in v2.1.300]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-14-77cdf5&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-14-5-agent-mode-changes-in-v2-1-299.md%0ACard%20ID%3A%20claude-code-2026-10-14-77cdf5%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.299%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->