---
card_id: claude-code-2026-07-17-083e30
date: '2026-07-17'
description: 'Claude Code · 2026-07-17 · Agent Mode: 7 changes in v2.1.212 — `/fork`
  now copies your conversation into a new background session (its own row in `claude…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1107
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2330fbc80b1de0233d2e504bd8d918e21d93fddff8f7bea374905b21bf904cac
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-07-17-083e30
  comparison: ''
  date: '2026-07-17'
  description: 'Claude Code — v2.1.212: 7 Agent Mode changes'
  evidence:
  - quote: '`/fork` now copies your conversation into a new background session (its
      own row in `claude agents`) while you keep working; the in-session subagent
      it used to launch is now `/subtask`'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.212
  - quote: Added `claude auto-mode reset` to restore the default auto-mode configuration,
      with a confirmation prompt (pass `--yes` to skip)
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.212
  - quote: Added a per-session cap on subagent spawns (default 200, override with
      `CLAUDE_CODE_MAX_SUBAGENTS_PER_SESSION`) to stop runaway delegation loops; `/clear`
      resets the budget
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.212
  - quote: 'Improved background agent attach: cold-attaching now instantly shows the
      formatted transcript while the session boots, instead of a blank wait'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.212
  - quote: 'Reduced token usage in inter-agent messaging: `SendMessage` bodies are
      no longer duplicated into replayed history and tool results'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.212
  - quote: Changed `/fork` to name the copy after your prompt when the session has
      no title, so the row is recognizable in the agent view
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.212
  - quote: Changed the `←` footer hint to pulse `N done` for a moment when a background
      agent finishes while nothing needs your input
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.212
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 7-agent-mode-changes-in-v2-1-212
  source_release: claude-code-2026-07-17-v2-1-212-github-355310036-d94b4e11
  source_type: github_releases
  theme: agent-mode
  title: 7 Agent Mode changes in v2.1.212
  type: change
related_changes:
- '[[Changes/Claude Code/2026-07-14-4-agent-mode-changes-in-v2-1-208|4 Agent Mode
  changes in v2.1.208]]'
- '[[Changes/Claude Code/2026-07-14-3-agent-mode-changes-in-v2-1-210|3 Agent Mode
  changes in v2.1.210]]'
- '[[Changes/Claude Code/2026-07-15-2-agent-mode-changes-in-v2-1-211|2 Agent Mode
  changes in v2.1.211]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-17-v2-1-212-github-355310036-d94b4e11|claude-code-2026-07-17-v2-1-212-github-355310036-d94b4e11]]'
source_type: github_releases
theme: agent-mode
title: 7 Agent Mode changes in v2.1.212
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Agent Mode changes in v2.1.212

**Claude Code** · 2026-07-17 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.212) · from [[Releases/Claude Code/claude-code-2026-07-17-v2-1-212-github-355310036-d94b4e11|v2.1.212]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> `/fork` now copies your conversation into a new background session (its own row in `claude agents`) while you keep working; the in-session subagent it used to launch is now `/subtask`

> Added `claude auto-mode reset` to restore the default auto-mode configuration, with a confirmation prompt (pass `--yes` to skip)

> Added a per-session cap on subagent spawns (default 200, override with `CLAUDE_CODE_MAX_SUBAGENTS_PER_SESSION`) to stop runaway delegation loops; `/clear` resets the budget

> Improved background agent attach: cold-attaching now instantly shows the formatted transcript while the session boots, instead of a blank wait

> Reduced token usage in inter-agent messaging: `SendMessage` bodies are no longer duplicated into replayed history and tool results

> Changed `/fork` to name the copy after your prompt when the session has no title, so the row is recognizable in the agent view

> Changed the `←` footer hint to pulse `N done` for a moment when a background agent finishes while nothing needs your input

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.212
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-07-17-typing-resume-in-the-agent-view-now-opens-a-picker-of-past-sessions-including-se|Typing /resume in the agent view now opens a picker of past sessions]] · Interface Experience
- [[Changes/Claude Code/2026-07-17-updated-the-auth-status-panel-title-from-cloud-authentication-to-authentication|Updated the auth status panel title from "Cloud authentication" to "Authentication"]] · Account and Access
- [[Changes/Claude Code/2026-07-17-3-search-and-browsing-changes-in-v2-1-212|3 Search and Browsing changes in v2.1.212]] · Search and Browsing
- [[Changes/Claude Code/2026-07-17-2-apps-and-integrations-changes-in-v2-1-212|2 Apps and Integrations changes in v2.1.212]] · Apps and Integrations
- [[Changes/Claude Code/2026-07-17-3-model-support-changes-in-v2-1-212|3 Model Support changes in v2.1.212]] · Model Support
- [[Changes/Claude Code/2026-07-17-3-safety-and-privacy-changes-in-v2-1-212|3 Safety and Privacy changes in v2.1.212]] · Safety and Privacy
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-07-15 · Claude Code · [[Changes/Claude Code/2026-07-15-2-agent-mode-changes-in-v2-1-211|2 Agent Mode changes in v2.1.211]]
- Later: 2026-07-18 · Claude Code · [[Changes/Claude Code/2026-07-18-added-reasoning-effort-to-the-subagentstatusline-payload-so-custom-agent-rows-ca|Added reasoning effort to the subagentStatusLine payload, so custom agent rows can…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-07-17-083e30&body=Card%3A%20Changes%2FClaude%20Code%2F2026-07-17-7-agent-mode-changes-in-v2-1-212.md%0ACard%20ID%3A%20claude-code-2026-07-17-083e30%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.212%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->