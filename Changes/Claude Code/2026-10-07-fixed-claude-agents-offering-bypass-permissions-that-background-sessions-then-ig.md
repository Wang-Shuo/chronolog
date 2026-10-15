---
card_id: claude-code-2026-10-07-a06fc1
date: '2026-10-07'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
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
machine_hash: 18d9fbda6bae068eeaca7e6e212eecc86bbc79905de311f147cec1723e1f5b4e
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
- '[[Changes/Claude Code/2026-10-05-added-agentid-to-the-tool-check-event-of-plugin-hooks-so-a-hook-can-tell-a-subag|claude-code-2026-10-05-fd658b]]'
- '[[Changes/Claude Code/2026-10-06-fixed-a-regression-in-2-1-290-where-cloud-sessions-could-drop-answers-to-permiss|claude-code-2026-10-06-3ab833]]'
- '[[Changes/Claude Code/2026-10-07-fixed-claude-being-told-to-continue-or-message-subagents-with-sendmessage-in-ses|claude-code-2026-10-07-30e918]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-07-v2-1-293-github-405988533-66d1bb8d|claude-code-2026-10-07-v2-1-293-github-405988533-66d1bb8d]]'
source_type: github_releases
theme: safety-privacy
title: Fixed claude agents offering bypass permissions that background sessions then…
type: change
---

# Fixed `claude agents` offering bypass permissions that background sessions then…

<!-- chronolog:begin region="description" -->
Claude Code — v2.1.293: Fixed `claude agents` offering bypass permissions that background sessions then ignored when consent was saved only in `.claude/settings.local.json` or a `--settings` file; it now asks for consent first, and a session that ignores bypass shows a short notice that stays
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Fixed `claude agents` offering bypass permissions that background sessions then ignored when consent was saved only in `.claude/settings.local.json` or a `--settings` file; it now asks for consent first, and a session that ignores bypass shows a short notice that stays
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.293
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
No evidence-backed evolution relationship assigned.
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: safety-privacy
- Relation: same-theme-chronology
- Inference: No adoption, equivalence, or causation claim.
- Scope: tracked-products-only
- Role: later-observed
- First In Tracked: [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]
- Lag Days: 1270
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes