---
card_id: claude-code-2026-05-11-f49f9d
date: '2026-05-11'
description: 'Claude Code · 2026-05-11 · Agent Mode: 2 changes in v2.1.139 — Added
  agent view (Research Preview): a single list of every Claude Code session — running…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1040
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 0045c5d39c004ab0e44d15abeed7d7b35169e1f5090d8dedbdb27ecc5ce0a74e
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-05-11-f49f9d
  comparison: ''
  date: '2026-05-11'
  description: 'Claude Code — v2.1.139: 2 Agent Mode changes'
  evidence:
  - quote: 'Added agent view (Research Preview): a single list of every Claude Code
      session — running, blocked on you, or done. Run `claude agents` to get started.
      See https://code.claude.com/docs/en/agent-view'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.139
  - quote: API requests from subagents now carry `x-claude-code-agent-id` / `x-claude-code-parent-agent-id`
      headers, and `claude_code.llm_request` OTEL spans include `agent_id` / `parent_agent_id`
      attributes
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.139
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-agent-mode-changes-in-v2-1-139
  source_release: claude-code-2026-05-11-v2-1-139-github-320692766-5e65de7d
  source_type: github_releases
  theme: agent-mode
  title: 2 Agent Mode changes in v2.1.139
  type: change
related_changes:
- '[[Changes/Cursor/2026-04-29-3-agent-mode-changes-in-build-programmatic-agents|3
  Agent Mode changes in Build programmatic agents…]]'
- '[[Changes/Claude Code/2026-05-04-auto-mode-when-the-classifier-can-t-evaluate-an-action-the-error-now-includes-a|Auto
  mode: when the classifier can''t evaluate an action, the error now includes…]]'
- '[[Changes/Cursor/2026-05-07-added-the-ability-to-control-explore-subagent-behavior-from-settings-choose-a-sp|Added
  the ability to control Explore subagent behavior from settings]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-11-v2-1-139-github-320692766-5e65de7d|claude-code-2026-05-11-v2-1-139-github-320692766-5e65de7d]]'
source_type: github_releases
theme: agent-mode
title: 2 Agent Mode changes in v2.1.139
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Agent Mode changes in v2.1.139

**Claude Code** · 2026-05-11 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.139) · from [[Releases/Claude Code/claude-code-2026-05-11-v2-1-139-github-320692766-5e65de7d|v2.1.139]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added agent view (Research Preview): a single list of every Claude Code session — running, blocked on you, or done. Run `claude agents` to get started. See https://code.claude.com/docs/en/agent-view

> API requests from subagents now carry `x-claude-code-agent-id` / `x-claude-code-parent-agent-id` headers, and `claude_code.llm_request` OTEL spans include `agent_id` / `parent_agent_id` attributes

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.139
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-05-11-fixed-skill-name-permission-rules-the-wildcard-form-now-works-as-a-prefix-match|Fixed Skill(name ) permission rules]] · Safety and Privacy
- [[Changes/Claude Code/2026-05-11-added-hook-args-string-field-exec-form-that-spawns-the-command-directly-without|Added hook args: string field (exec form) that spawns the command directly…]] · Developer Workflow
- [[Changes/Claude Code/2026-05-11-context-all-per-skill-token-estimates-now-account-for-the-model-s-tokenizer-and|/context all per-skill token estimates now account for the model's tokenizer…]] · Context Window
- [[Changes/Claude Code/2026-05-11-added-goal-command-set-a-completion-condition-and-claude-keeps-working-across-tu|Added /goal command]] · Apps and Integrations
- [[Changes/Claude Code/2026-05-11-8-apps-and-integrations-changes-in-v2-1-139|8 Apps and Integrations changes in v2.1.139]] · Apps and Integrations
- [[Changes/Claude Code/2026-05-11-compaction-prompt-now-asks-the-model-to-preserve-sensitive-user-instructions|Compaction prompt now asks the model to preserve sensitive user instructions]] · Model Support
- [[Changes/Claude Code/2026-05-11-vscode-press-cmd-ctrl-shift-t-to-reopen-the-most-recently-closed-session-tab-con|VSCode Press Cmd/Ctrl+Shift+T to reopen the most recently closed session tab…]] · Editor Experience
- [[Changes/Claude Code/2026-05-11-added-scroll-speed-command-to-tune-mouse-wheel-scroll-speed-with-a-live-preview|Added /scroll-speed command to tune mouse wheel scroll speed with a live preview]] · Reliability and Performance
- [[Changes/Claude Code/2026-05-11-added-transcript-view-navigation-for-keyboard-shortcuts-to-jump-between-user-pro|Added transcript view navigation]] · Interface Experience
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-05-07 · Cursor · [[Changes/Cursor/2026-05-07-added-the-ability-to-control-explore-subagent-behavior-from-settings-choose-a-sp|Added the ability to control Explore subagent behavior from settings]]
- Later: 2026-05-12 · Claude Code · [[Changes/Claude Code/2026-05-12-2-agent-mode-changes-in-v2-1-140|2 Agent Mode changes in v2.1.140]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-05-11-f49f9d&body=Card%3A%20Changes%2FClaude%20Code%2F2026-05-11-2-agent-mode-changes-in-v2-1-139.md%0ACard%20ID%3A%20claude-code-2026-05-11-f49f9d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.139%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->