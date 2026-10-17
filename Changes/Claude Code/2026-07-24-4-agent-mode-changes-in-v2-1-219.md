---
card_id: claude-code-2026-07-24-b7af5c
date: '2026-07-24'
description: 'Claude Code · 2026-07-24 · Agent Mode: 4 changes in v2.1.219 — Added
  the `workflowSizeGuideline` settings key so the advisory Dynamic workflow size guideline…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1114
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8811c32e98d05ed76f7d2588fffd3254f7f66dcf18cbd9f2cda2e244c209266e
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-07-24-b7af5c
  comparison: ''
  date: '2026-07-24'
  description: 'Claude Code — v2.1.219: 4 Agent Mode changes'
  evidence:
  - quote: Added the `workflowSizeGuideline` settings key so the advisory Dynamic
      workflow size guideline can be set from any settings file; the `/config` row
      is hidden while one does
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.219
  - quote: 'Added nested subagent forwarding in stream-json: subagents spawned at
      depth-2+ now appear when `--forward-subagent-text` is set, keyed by their spawning
      Agent `tool_use` id'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.219
  - quote: Changed dynamic workflows to default to a medium size guideline (aim for
      fewer than 15 agents); pick another size or unrestricted with Dynamic workflow
      size in `/config`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.219
  - quote: Subagents can now spawn nested subagents up to depth 3 by default (was
      1); set CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH=1 to disable nesting
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.219
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 4-agent-mode-changes-in-v2-1-219
  source_release: claude-code-2026-07-24-v2-1-219-github-359412713-6c14d233
  source_type: github_releases
  theme: agent-mode
  title: 4 Agent Mode changes in v2.1.219
  type: change
related_changes:
- '[[Changes/Claude Code/2026-07-21-2-agent-mode-changes-in-v2-1-217|2 Agent Mode
  changes in v2.1.217]]'
- '[[Changes/Claude Code/2026-07-22-changed-plan-mode-with-auto-to-no-longer-prompt-for-bash-commands-the-static-ana|Changed
  plan mode with auto to no longer prompt for Bash commands the static…]]'
- '[[Changes/Cursor/2026-07-22-auto-mode-is-now-powered-by-cursor-router|Auto mode
  is now powered by Cursor Router]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-24-v2-1-219-github-359412713-6c14d233|claude-code-2026-07-24-v2-1-219-github-359412713-6c14d233]]'
source_type: github_releases
theme: agent-mode
title: 4 Agent Mode changes in v2.1.219
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Agent Mode changes in v2.1.219

**Claude Code** · 2026-07-24 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.219) · from [[Releases/Claude Code/claude-code-2026-07-24-v2-1-219-github-359412713-6c14d233|v2.1.219]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added the `workflowSizeGuideline` settings key so the advisory Dynamic workflow size guideline can be set from any settings file; the `/config` row is hidden while one does

> Added nested subagent forwarding in stream-json: subagents spawned at depth-2+ now appear when `--forward-subagent-text` is set, keyed by their spawning Agent `tool_use` id

> Changed dynamic workflows to default to a medium size guideline (aim for fewer than 15 agents); pick another size or unrestricted with Dynamic workflow size in `/config`

> Subagents can now spawn nested subagents up to depth 3 by default (was 1); set CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH=1 to disable nesting

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.219
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-07-24-5-apps-and-integrations-changes-in-v2-1-219|5 Apps and Integrations changes in v2.1.219]] · Apps and Integrations
- [[Changes/Claude Code/2026-07-24-2-interface-experience-changes-in-v2-1-219|2 Interface Experience changes in v2.1.219]] · Interface Experience
- [[Changes/Claude Code/2026-07-24-3-model-support-changes-in-v2-1-219|3 Model Support changes in v2.1.219]] · Model Support
- [[Changes/Claude Code/2026-07-24-2-safety-and-privacy-changes-in-v2-1-219|2 Safety and Privacy changes in v2.1.219]] · Safety and Privacy
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-07-22 · Cursor · [[Changes/Cursor/2026-07-22-auto-mode-is-now-powered-by-cursor-router|Auto mode is now powered by Cursor Router]]
- Later: 2026-07-28 · Cursor · [[Changes/Cursor/2026-07-28-always-on-cloud-agents-that-build-test-and-ship-code-while-you-keep-working-725c7c|Always-on cloud agents that build, test, and ship code while you keep working]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-07-24-b7af5c&body=Card%3A%20Changes%2FClaude%20Code%2F2026-07-24-4-agent-mode-changes-in-v2-1-219.md%0ACard%20ID%3A%20claude-code-2026-07-24-b7af5c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.219%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->