---
card_id: claude-code-2026-09-03-9edb67
date: '2026-09-03'
description: 'Claude Code · 2026-09-03 · Agent Mode: 2 changes in v2.1.260 — Improved
  structured output: Workflow `agent({schema})` rejects a JSON Schema that can never
  be…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1155
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2ac4243195159d13c79447321f7f8fea1fad9e039306a83cf0312b489e6c6040
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-03-9edb67
  comparison: ''
  date: '2026-09-03'
  description: 'Claude Code — v2.1.260: 2 Agent Mode changes'
  evidence:
  - quote: 'Improved structured output: Workflow `agent({schema})` rejects a JSON
      Schema that can never be satisfied up front, and retry-cap errors now include
      the last validation failure'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.260
  - quote: Removed the one-hour time limit on background commands started by subagents;
      they now run until they exit or are stopped, matching the main session
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.260
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-agent-mode-changes-in-v2-1-260
  source_release: claude-code-2026-09-03-v2-1-260-github-382367470-ac2ba1fc
  source_type: github_releases
  theme: agent-mode
  title: 2 Agent Mode changes in v2.1.260
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-02-2-agent-mode-changes-in-v2-1-259|2 Agent Mode
  changes in v2.1.259]]'
- '[[Changes/Cursor/2026-09-02-run-on-your-sandboxes|Run on your sandboxes]]'
- '[[Changes/Cursor/2026-09-02-cursor-supports-self-hosted-machines-which-let-you-keep-tool-execution-entirely|Cursor
  supports self-hosted machines, which let you keep tool execution entirely…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-03-v2-1-260-github-382367470-ac2ba1fc|claude-code-2026-09-03-v2-1-260-github-382367470-ac2ba1fc]]'
source_type: github_releases
theme: agent-mode
title: 2 Agent Mode changes in v2.1.260
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Agent Mode changes in v2.1.260

**Claude Code** · 2026-09-03 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.260) · from [[Releases/Claude Code/claude-code-2026-09-03-v2-1-260-github-382367470-ac2ba1fc|v2.1.260]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Improved structured output: Workflow `agent({schema})` rejects a JSON Schema that can never be satisfied up front, and retry-cap errors now include the last validation failure

> Removed the one-hour time limit on background commands started by subagents; they now run until they exit or are stopped, matching the main session

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.260
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-03-2-model-support-changes-in-v2-1-260|2 Model Support changes in v2.1.260]] · Model Support
- [[Changes/Claude Code/2026-09-03-2-context-window-changes-in-v2-1-260|2 Context Window changes in v2.1.260]] · Context Window
- [[Changes/Claude Code/2026-09-03-improved-the-settings-error-for-rules-such-as-edit-c-dir-name-where-is-read-as-a|Improved the settings error for rules such as Edit(C:\dir\(name)\), where…]] · Editor Experience
- [[Changes/Claude Code/2026-09-03-improved-deleting-a-background-session-whose-worktree-has-unpushed-commits-the-m|Improved deleting a background session whose worktree has unpushed commits]] · Developer Workflow
- [[Changes/Claude Code/2026-09-03-4-interface-experience-changes-in-v2-1-260|4 Interface Experience changes in v2.1.260]] · Interface Experience
- [[Changes/Claude Code/2026-09-03-3-mobile-and-desktop-changes-in-v2-1-260|3 Mobile and Desktop changes in v2.1.260]] · Mobile and Desktop
- [[Changes/Claude Code/2026-09-03-4-apps-and-integrations-changes-in-v2-1-260|4 Apps and Integrations changes in v2.1.260]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-03-7-safety-and-privacy-changes-in-v2-1-260|7 Safety and Privacy changes in v2.1.260]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-03-added-reload-plugins-to-headless-sessions-so-it-appears-in-the-claude-code-deskt|Added /reload-plugins to headless sessions, so it appears in the Claude Code…]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-03-4-other-changes-in-v2-1-260|4 other changes in v2.1.260]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-09-02 · Cursor · [[Changes/Cursor/2026-09-02-cursor-supports-self-hosted-machines-which-let-you-keep-tool-execution-entirely|Cursor supports self-hosted machines, which let you keep tool execution entirely…]]
- Later: 2026-09-04 · Claude Code · [[Changes/Claude Code/2026-09-04-2-agent-mode-changes-in-v2-1-261|2 Agent Mode changes in v2.1.261]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-03-9edb67&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-03-2-agent-mode-changes-in-v2-1-260.md%0ACard%20ID%3A%20claude-code-2026-09-03-9edb67%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.260%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->