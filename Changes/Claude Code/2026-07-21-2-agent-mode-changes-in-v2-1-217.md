---
card_id: claude-code-2026-07-21-e00ee5
date: '2026-07-21'
description: 'Claude Code · 2026-07-21 · Agent Mode: 2 changes in v2.1.217 — Added
  a cap on concurrently-running subagents (default 20, override with…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1111
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 23e756e274f9595fb9df82f08a98f4fac320a6473edf97686e2b6d2da92417ac
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-07-21-e00ee5
  comparison: ''
  date: '2026-07-21'
  description: 'Claude Code — v2.1.217: 2 Agent Mode changes'
  evidence:
  - quote: Added a cap on concurrently-running subagents (default 20, override with
      `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`) so one message can't fan out unbounded
      background agents
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.217
  - quote: Changed subagents to no longer spawn nested subagents by default; set `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`
      to allow deeper nesting
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.217
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-agent-mode-changes-in-v2-1-217
  source_release: claude-code-2026-07-21-v2-1-217-github-357601516-b5c19f5d
  source_type: github_releases
  theme: agent-mode
  title: 2 Agent Mode changes in v2.1.217
  type: change
related_changes:
- '[[Changes/Claude Code/2026-07-15-2-agent-mode-changes-in-v2-1-211|2 Agent Mode
  changes in v2.1.211]]'
- '[[Changes/Claude Code/2026-07-17-7-agent-mode-changes-in-v2-1-212|7 Agent Mode
  changes in v2.1.212]]'
- '[[Changes/Claude Code/2026-07-18-added-reasoning-effort-to-the-subagentstatusline-payload-so-custom-agent-rows-ca|Added
  reasoning effort to the subagentStatusLine payload, so custom agent rows can…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-21-v2-1-217-github-357601516-b5c19f5d|claude-code-2026-07-21-v2-1-217-github-357601516-b5c19f5d]]'
source_type: github_releases
theme: agent-mode
title: 2 Agent Mode changes in v2.1.217
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Agent Mode changes in v2.1.217

**Claude Code** · 2026-07-21 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.217) · from [[Releases/Claude Code/claude-code-2026-07-21-v2-1-217-github-357601516-b5c19f5d|v2.1.217]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added a cap on concurrently-running subagents (default 20, override with `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`) so one message can't fan out unbounded background agents

> Changed subagents to no longer spawn nested subagents by default; set `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` to allow deeper nesting

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.217
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-07-21-capped-the-frontend-design-plugin-suggestion-tip-at-3-lifetime-impressions-inste|Capped the frontend-design plugin suggestion tip at 3 lifetime impressions instead…]] · Apps and Integrations
- [[Changes/Claude Code/2026-07-21-changed-the-login-expiry-warning-to-appear-3-days-before-expiry-instead-of-5|Changed the login-expiry warning to appear 3 days before expiry instead of 5]] · Account and Access
- [[Changes/Claude Code/2026-07-21-added-warnings-when-transcript-writes-are-failing-e-g-disk-full-or-when-session|Added warnings when transcript writes are failing (e.g. disk full) or when session…]] · Reliability and Performance
- [[Changes/Claude Code/2026-07-21-fixed-remote-control-sessions-not-showing-a-pending-permission-prompt-or-dialog|Fixed Remote Control sessions not showing a pending permission prompt or dialog…]] · Safety and Privacy
- [[Changes/Claude Code/2026-07-21-improved-footer-pr-badge-links-to-be-clickable-hyperlinks-even-when-terminal-sup|Improved footer PR badge links to be clickable hyperlinks even when terminal support…]] · Developer Workflow
- [[Changes/Claude Code/2026-07-21-added-emoji-shortcode-autocomplete-in-the-prompt-input-type-heart-to-insert-or-h|Added emoji shortcode autocomplete in the prompt input]] · Editor Experience
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-07-18 · Claude Code · [[Changes/Claude Code/2026-07-18-added-reasoning-effort-to-the-subagentstatusline-payload-so-custom-agent-rows-ca|Added reasoning effort to the subagentStatusLine payload, so custom agent rows can…]]
- Later: 2026-07-22 · Claude Code · [[Changes/Claude Code/2026-07-22-changed-plan-mode-with-auto-to-no-longer-prompt-for-bash-commands-the-static-ana|Changed plan mode with auto to no longer prompt for Bash commands the static…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-07-21-e00ee5&body=Card%3A%20Changes%2FClaude%20Code%2F2026-07-21-2-agent-mode-changes-in-v2-1-217.md%0ACard%20ID%3A%20claude-code-2026-07-21-e00ee5%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.217%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->