---
card_id: claude-code-2026-09-23-7c3882
date: '2026-09-23'
description: 'Claude Code · 2026-09-23 · Agent Mode: 9 changes in v2.1.281 — Improved
  the auto mode denial message so Claude treats a denial as covering the outcome,
  not…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1175
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d8458d6b5a97e9d0005b45112ce98b4027f971e6e71e9315567b6861cad0b9bf
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-23-7c3882
  comparison: ''
  date: '2026-09-23'
  description: 'Claude Code — v2.1.281: 9 Agent Mode changes'
  evidence:
  - quote: Improved the auto mode denial message so Claude treats a denial as covering
      the outcome, not only the exact command
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
  - quote: Improved `--agents` to accept the path to a JSON file (with `-p`) as well
      as inline JSON, and to allow an empty `prompt`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
  - quote: Improved `/batch` to run where a WorktreeCreate hook provides the agent
      worktrees, not only inside a git repository
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
  - quote: 'Improved the background workflow row below the prompt: it now shows the
      name, a progress bar, the agent count on wide terminals, elapsed time, total
      tokens, and the large-workflow warning'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
  - quote: Changed auto mode so that, where its classifier review runs server-side,
      read-only and sandboxed shell commands also wait for that review and are blocked
      when it flags them
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
  - quote: 'Changed `CLAUDE_CODE_AUTO_MODE_SERVER` to also apply on a direct Anthropic
      API connection: `0` opts out of the server-side auto mode classifier (the local
      classifier then counts toward usage), `1` opts in'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
  - quote: Changed the dangerous `rm` prompt in `--dangerously-skip-permissions` and
      auto mode to wait 2 minutes for an answer, then deny the command with a rewrite
      hint so unattended sessions keep going (`CLAUDE_CODE_DISABLE_DANGEROUS_RM_TIMEOUT=1`
      turns this off)
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
  - quote: '[VSCode] Added a Continue/Stop prompt in the VS Code and JetBrains panels
      when auto mode falls back to billed classifier requests, replacing the unanswerable
      warning line'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
  - quote: '[Claude Code on the web] Added a Fast mode switch to the composer''s model
      menu in cloud sessions, shown when your plan includes fast mode and the selected
      model supports it'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 9-agent-mode-changes-in-v2-1-281
  source_release: claude-code-2026-09-23-v2-1-281-github-394877414-9173ae95
  source_type: github_releases
  theme: agent-mode
  title: 9 Agent Mode changes in v2.1.281
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-18-4-agent-mode-changes-in-v2-1-277|4 Agent Mode
  changes in v2.1.277]]'
- '[[Changes/Claude Code/2026-09-19-added-an-auto-mode-server-row-to-status-showing-whether-this-session-s-auto-mode|Added
  an Auto mode server row to /status showing whether this session''s auto…]]'
- '[[Changes/Claude Code/2026-09-22-2-agent-mode-changes-in-v2-1-280|2 Agent Mode
  changes in v2.1.280]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-23-v2-1-281-github-394877414-9173ae95|claude-code-2026-09-23-v2-1-281-github-394877414-9173ae95]]'
source_type: github_releases
theme: agent-mode
title: 9 Agent Mode changes in v2.1.281
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Agent Mode changes in v2.1.281

**Claude Code** · 2026-09-23 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.281) · from [[Releases/Claude Code/claude-code-2026-09-23-v2-1-281-github-394877414-9173ae95|v2.1.281]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Improved the auto mode denial message so Claude treats a denial as covering the outcome, not only the exact command

> Improved `--agents` to accept the path to a JSON file (with `-p`) as well as inline JSON, and to allow an empty `prompt`

> Improved `/batch` to run where a WorktreeCreate hook provides the agent worktrees, not only inside a git repository

> Improved the background workflow row below the prompt: it now shows the name, a progress bar, the agent count on wide terminals, elapsed time, total tokens, and the large-workflow warning

> Changed auto mode so that, where its classifier review runs server-side, read-only and sandboxed shell commands also wait for that review and are blocked when it flags them

> Changed `CLAUDE_CODE_AUTO_MODE_SERVER` to also apply on a direct Anthropic API connection: `0` opts out of the server-side auto mode classifier (the local classifier then counts toward usage), `1` opts in

> Changed the dangerous `rm` prompt in `--dangerously-skip-permissions` and auto mode to wait 2 minutes for an answer, then deny the command with a rewrite hint so unattended sessions keep going (`CLAUDE_CODE_DISABLE_DANGEROUS_RM_TIMEOUT=1` turns this off)

> [VSCode] Added a Continue/Stop prompt in the VS Code and JetBrains panels when auto mode falls back to billed classifier requests, replacing the unanswerable warning line

> [Claude Code on the web] Added a Fast mode switch to the composer's model menu in cloud sessions, shown when your plan includes fast mode and the selected model supports it

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-23-improved-interactive-startup-time-git-reads-startup-telemetry-and-the-bedrock-ve|Improved interactive startup time]] · Model Support
- [[Changes/Claude Code/2026-09-23-2-account-and-access-changes-in-v2-1-281|2 Account and Access changes in v2.1.281]] · Account and Access
- [[Changes/Claude Code/2026-09-23-claude-tag-changed-the-routine-list-claude-gives-when-asked-in-a-slack-thread-to|Claude Tag Changed the routine list Claude gives when asked in a Slack thread…]] · Automation and Scheduling
- [[Changes/Claude Code/2026-09-23-7-developer-workflow-changes-in-v2-1-281|7 Developer Workflow changes in v2.1.281]] · Developer Workflow
- [[Changes/Claude Code/2026-09-23-2-mobile-and-desktop-changes-in-v2-1-281|2 Mobile and Desktop changes in v2.1.281]] · Mobile and Desktop
- [[Changes/Claude Code/2026-09-23-4-interface-experience-changes-in-v2-1-281|4 Interface Experience changes in v2.1.281]] · Interface Experience
- [[Changes/Claude Code/2026-09-23-improved-deep-research-reliability-on-long-research-briefs-by-removing-unused-re|Improved /deep-research reliability on long research briefs by removing unused…]] · Search and Browsing
- [[Changes/Claude Code/2026-09-23-18-apps-and-integrations-changes-in-v2-1-281|18 Apps and Integrations changes in v2.1.281]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-23-12-safety-and-privacy-changes-in-v2-1-281|12 Safety and Privacy changes in v2.1.281]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-23-improved-screen-reader-output-in-mcp-a-disabled-server-is-read-as-off-instead-of|Improved screen-reader output in /mcp]] · Accessibility and Localization
- [[Changes/Claude Code/2026-09-23-13-other-changes-in-v2-1-281|13 other changes in v2.1.281]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-09-22 · Claude Code · [[Changes/Claude Code/2026-09-22-2-agent-mode-changes-in-v2-1-280|2 Agent Mode changes in v2.1.280]]
- Later: 2026-09-23 · Cursor · [[Changes/Cursor/2026-09-23-when-rollouts-detects-a-regression-it-names-the-change-it-suspects-and-notifies|When Rollouts detects a regression, it names the change it suspects and notifies…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-23-7c3882&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-23-9-agent-mode-changes-in-v2-1-281.md%0ACard%20ID%3A%20claude-code-2026-09-23-7c3882%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.281%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->