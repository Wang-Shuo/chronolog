---
card_id: claude-code-2026-10-07-a06fc1
date: '2026-10-07'
description: 'Claude Code · 2026-10-07 · Safety and Privacy: Fixed `claude agents`
  offering bypass permissions that background sessions then ignored when consent was
  saved…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1270
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v4
impact: incremental
machine_hash: 86e33ac7eb697799ef0f43518066e7e62396fcec766e3db9433bb59c75dcf330
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-07-a06fc1
  comparison: ''
  date: '2026-10-07'
  description: 'Claude Code — v2.1.293: Fixed `claude agents` offering bypass permissions
    that background sessions then ignored when consent was saved only in `.claude/settings.local.json`
    or a `--settings` file; it now asks for consent first, and a session that ignores
    bypass shows a short notice that stays'
  evidence:
  - quote: Fixed `claude agents` offering bypass permissions that background sessions
      then ignored when consent was saved only in `.claude/settings.local.json` or
      a `--settings` file; it now asks for consent first, and a session that ignores
      bypass shows a short notice that stays
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.293
  extractor_version: fallback-v4
  impact: incremental
  product: claude-code
  product_name: Claude Code
  slug: fixed-claude-agents-offering-bypass-permissions-that-background-sessions-then-ig
  source_release: claude-code-2026-10-07-v2-1-293-github-405988533-66d1bb8d
  source_type: github_releases
  theme: safety-privacy
  theme_matches: []
  theme_resolution: manual-semantic-rule-v2
  title: Fixed `claude agents` offering bypass permissions that background sessions
    then…
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-05-added-agentid-to-the-tool-check-event-of-plugin-hooks-so-a-hook-can-tell-a-subag|Added
  agentId to the tool.check event of plugin hooks, so a hook can tell…]]'
- '[[Changes/Claude Code/2026-10-06-fixed-a-regression-in-2-1-290-where-cloud-sessions-could-drop-answers-to-permiss|Fixed
  a regression in 2.1.290 where cloud sessions could drop answers to permission…]]'
- '[[Changes/Claude Code/2026-10-07-fixed-claude-being-told-to-continue-or-message-subagents-with-sendmessage-in-ses|Fixed
  Claude being told to continue or message subagents with SendMessage…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-07-v2-1-293-github-405988533-66d1bb8d|claude-code-2026-10-07-v2-1-293-github-405988533-66d1bb8d]]'
source_type: github_releases
theme: safety-privacy
title: Fixed claude agents offering bypass permissions that background sessions then…
type: change
---

<!-- chronolog:begin region="header" -->
# Fixed `claude agents` offering bypass permissions that background sessions then…

**Claude Code** · 2026-10-07 · [[Themes/safety-privacy|Safety and Privacy]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.293) · from [[Releases/Claude Code/claude-code-2026-10-07-v2-1-293-github-405988533-66d1bb8d|v2.1.293]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Fixed `claude agents` offering bypass permissions that background sessions then ignored when consent was saved only in `.claude/settings.local.json` or a `--settings` file; it now asks for consent first, and a session that ignores bypass shows a short notice that stays
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.293
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-07-added-claude-haiku-5-5-claude-haiku-5-5-now-the-default-haiku-model-on-the-anthr|Added Claude Haiku 5.5 (claude-haiku-5-5), now the default Haiku model…]] · Model Support
- [[Changes/Claude Code/2026-10-07-fixed-claude-being-told-to-continue-or-message-subagents-with-sendmessage-in-ses|Fixed Claude being told to continue or message subagents with SendMessage…]] · Safety and Privacy
- [[Changes/Claude Code/2026-10-07-added-agenttype-to-the-subagentstatusline-payload-so-scripts-can-tell-custom-sub|Added agentType to the subagentStatusLine payload, so scripts can tell custom…]] · Agent Mode
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-10-06 · Claude Code · [[Changes/Claude Code/2026-10-06-fixed-a-regression-in-2-1-290-where-cloud-sessions-could-drop-answers-to-permiss|Fixed a regression in 2.1.290 where cloud sessions could drop answers to permission…]]
- Later: 2026-10-13 · Cursor · [[Changes/Cursor/2026-10-13-origin-now-integrates-with-over-20-apps-for-deployments-ci-code-review-security|Origin now integrates with over 20 apps for deployments, CI, code review, security…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-07-a06fc1&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-07-fixed-claude-agents-offering-bypass-permissions-that-background-sessions-then-ig.md%0ACard%20ID%3A%20claude-code-2026-10-07-a06fc1%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.293%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->