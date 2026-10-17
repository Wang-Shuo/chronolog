---
card_id: claude-code-2026-05-19-673e7e
date: '2026-05-19'
description: 'Claude Code · 2026-05-19 · Agent Mode: 3 changes in v2.1.145 — Added
  `claude agents --json` to list live Claude sessions as JSON for scripting (tmux-resurrect…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1048
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a84d03934b1af24a09f1cefdbe23f152886f5b7ee80bf67a86c0d2d6b2f2366b
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-05-19-673e7e
  comparison: ''
  date: '2026-05-19'
  description: 'Claude Code — v2.1.145: 3 Agent Mode changes'
  evidence:
  - quote: Added `claude agents --json` to list live Claude sessions as JSON for scripting
      (tmux-resurrect, status bars, session pickers)
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.145
  - quote: Added `agent_id` and `parent_agent_id` attributes to `claude_code.tool`
      OTEL spans, and fixed trace parenting so background subagent spans nest under
      the dispatching Agent tool span
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.145
  - quote: '`claude agents` terminal tab title now shows the awaiting-input count
      so an alt-tabbed window tells you when an agent needs attention'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.145
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-agent-mode-changes-in-v2-1-145
  source_release: claude-code-2026-05-19-v2-1-145-github-325388499-227a5ce4
  source_type: github_releases
  theme: agent-mode
  title: 3 Agent Mode changes in v2.1.145
  type: change
related_changes:
- '[[Changes/Cursor/2026-05-18-composer-2-5-is-now-available-in-cursor|Composer 2.5
  is now available in Cursor]]'
- '[[Changes/Claude Code/2026-05-19-added-resume-support-for-background-sessions-sessions-started-via-claude-bg-or-a|Added
  /resume support for background sessions]]'
- '[[Changes/Claude Code/2026-05-19-3-agent-mode-changes-in-v2-1-144|3 Agent Mode
  changes in v2.1.144]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-19-v2-1-145-github-325388499-227a5ce4|claude-code-2026-05-19-v2-1-145-github-325388499-227a5ce4]]'
source_type: github_releases
theme: agent-mode
title: 3 Agent Mode changes in v2.1.145
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Agent Mode changes in v2.1.145

**Claude Code** · 2026-05-19 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.145) · from [[Releases/Claude Code/claude-code-2026-05-19-v2-1-145-github-325388499-227a5ce4|v2.1.145]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `claude agents --json` to list live Claude sessions as JSON for scripting (tmux-resurrect, status bars, session pickers)

> Added `agent_id` and `parent_agent_id` attributes to `claude_code.tool` OTEL spans, and fixed trace parenting so background subagent spans nest under the dispatching Agent tool span

> `claude agents` terminal tab title now shows the awaiting-input count so an alt-tabbed window tells you when an agent needs attention

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.145
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-05-19-plugin-discover-and-browse-screens-now-show-a-plugin-s-commands-agents-skills-ho|/plugin Discover and Browse screens now show a plugin's commands, agents, skills…]] · Apps and Integrations
- [[Changes/Claude Code/2026-05-19-fixed-a-permission-prompt-bypass-where-bare-variable-assignments-to-non-allowlis|Fixed a permission-prompt bypass where bare variable assignments to non-allowlisted…]] · Safety and Privacy
- [[Changes/Claude Code/2026-05-19-2-interface-experience-changes-in-v2-1-145|2 Interface Experience changes in v2.1.145]] · Interface Experience
- [[Changes/Claude Code/2026-05-19-improved-the-read-tool-to-return-a-truncated-first-page-with-a-partial-view-noti|Improved the Read tool to return a truncated first page with a "PARTIAL view" notice…]] · Context Window
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-05-19 · Claude Code · [[Changes/Claude Code/2026-05-19-3-agent-mode-changes-in-v2-1-144|3 Agent Mode changes in v2.1.144]]
- Later: 2026-05-19 · Cursor · [[Changes/Cursor/2026-05-19-assign-work-items-to-cursor-or-mention-cursor-in-a-comment-to-kick-off-a-cloud-a-1c05f0|Assign work items to Cursor, or mention @Cursor in a comment to kick off a cloud agent]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-05-19-673e7e&body=Card%3A%20Changes%2FClaude%20Code%2F2026-05-19-3-agent-mode-changes-in-v2-1-145.md%0ACard%20ID%3A%20claude-code-2026-05-19-673e7e%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.145%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->