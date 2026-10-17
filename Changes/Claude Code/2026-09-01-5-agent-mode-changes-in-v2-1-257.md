---
card_id: claude-code-2026-09-01-765f93
date: '2026-09-01'
description: 'Claude Code · 2026-09-01 · Agent Mode: 5 changes in v2.1.257 — Added
  a Containment Escape rule to auto mode so cloud metadata-credential fetches, egress…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1153
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 53e7746ce10a2cb5cb90cbb44dbc28e78347ba305923e8c8e5f5b550a29ee967
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-01-765f93
  comparison: ''
  date: '2026-09-01'
  description: 'Claude Code — v2.1.257: 5 Agent Mode changes'
  evidence:
  - quote: Added a Containment Escape rule to auto mode so cloud metadata-credential
      fetches, egress evasion, and cross-tenant reach are no longer auto-approved
      unless your environment marks them expected
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.257
  - quote: Added `CLAUDE_CODE_SUBAGENT_MODEL_FORCE` to apply `CLAUDE_CODE_SUBAGENT_MODEL`
      (or the main model) to every subagent, ignoring per-spawn and agent-definition
      model overrides
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.257
  - quote: Added a one-time prompt in auto mode before the first file read outside
      the working directories, with the option to block such reads (`permissions.blockReadsOutsideWorkingDirectories`)
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.257
  - quote: 'Improved rendering performance: less re-render work per turn in long conversations,
      streaming no longer slows down as the reply grows, and background-agent updates
      no longer re-render the whole screen'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.257
  - quote: 'Changed Cowork and claude.ai cloud sessions: reading an artifact that
      isn''t yours now always asks you first, even in auto mode'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.257
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 5-agent-mode-changes-in-v2-1-257
  source_release: claude-code-2026-09-01-v2-1-257-github-380686035-b86855a6
  source_type: github_releases
  theme: agent-mode
  title: 5 Agent Mode changes in v2.1.257
  type: change
related_changes:
- '[[Changes/Cursor/2026-08-27-cloud-agents-no-longer-require-a-connected-github-or-other-third-party-scm-provi|Cloud
  Agents no longer require a connected GitHub or other third-party SCM provider…]]'
- '[[Changes/Cursor/2026-08-27-cursor-now-port-forwards-your-cloud-agent-s-live-environment-straight-to-your-br|A
  live preview, right in the browser]]'
- '[[Changes/Claude Code/2026-08-28-4-agent-mode-changes-in-v2-1-251|4 Agent Mode
  changes in v2.1.251]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-01-v2-1-257-github-380686035-b86855a6|claude-code-2026-09-01-v2-1-257-github-380686035-b86855a6]]'
source_type: github_releases
theme: agent-mode
title: 5 Agent Mode changes in v2.1.257
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Agent Mode changes in v2.1.257

**Claude Code** · 2026-09-01 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.257) · from [[Releases/Claude Code/claude-code-2026-09-01-v2-1-257-github-380686035-b86855a6|v2.1.257]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added a Containment Escape rule to auto mode so cloud metadata-credential fetches, egress evasion, and cross-tenant reach are no longer auto-approved unless your environment marks them expected

> Added `CLAUDE_CODE_SUBAGENT_MODEL_FORCE` to apply `CLAUDE_CODE_SUBAGENT_MODEL` (or the main model) to every subagent, ignoring per-spawn and agent-definition model overrides

> Added a one-time prompt in auto mode before the first file read outside the working directories, with the option to block such reads (`permissions.blockReadsOutsideWorkingDirectories`)

> Improved rendering performance: less re-render work per turn in long conversations, streaming no longer slows down as the reply grows, and background-agent updates no longer re-render the whole screen

> Changed Cowork and claude.ai cloud sessions: reading an artifact that isn't yours now always asks you first, even in auto mode

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.257
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-01-2-editor-experience-changes-in-v2-1-257|2 Editor Experience changes in v2.1.257]] · Editor Experience
- [[Changes/Claude Code/2026-09-01-3-developer-workflow-changes-in-v2-1-257|3 Developer Workflow changes in v2.1.257]] · Developer Workflow
- [[Changes/Claude Code/2026-09-01-improved-prompt-input-responsiveness-by-reducing-per-keystroke-rendering-work|Improved prompt input responsiveness by reducing per-keystroke rendering work]] · Reliability and Performance
- [[Changes/Claude Code/2026-09-01-changed-btw-history-browsing-from-to-shift-shift-or-stepping-through-your-recent|Changed /btw history browsing from ←/→ to Shift+←/Shift+→ (or /)…]] · Search and Browsing
- [[Changes/Claude Code/2026-09-01-10-safety-and-privacy-changes-in-v2-1-257|10 Safety and Privacy changes in v2.1.257]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-01-changed-add-dir-add-dir-and-additionaldirectories-to-refuse-network-paths-unc-sh|Changed --add-dir, /add-dir, and additionalDirectories to refuse network paths…]] · Mobile and Desktop
- [[Changes/Claude Code/2026-09-01-2-apps-and-integrations-changes-in-v2-1-257|2 Apps and Integrations changes in v2.1.257]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-01-2-account-and-access-changes-in-v2-1-257|2 Account and Access changes in v2.1.257]] · Account and Access
- [[Changes/Claude Code/2026-09-01-2-interface-experience-changes-in-v2-1-257|2 Interface Experience changes in v2.1.257]] · Interface Experience
- [[Changes/Claude Code/2026-09-01-6-model-support-changes-in-v2-1-257|6 Model Support changes in v2.1.257]] · Model Support
- [[Changes/Claude Code/2026-09-01-7-other-changes-in-v2-1-257|7 other changes in v2.1.257]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-08-28 · Claude Code · [[Changes/Claude Code/2026-08-28-4-agent-mode-changes-in-v2-1-251|4 Agent Mode changes in v2.1.251]]
- Later: 2026-09-02 · Claude Code · [[Changes/Claude Code/2026-09-02-2-agent-mode-changes-in-v2-1-259|2 Agent Mode changes in v2.1.259]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-01-765f93&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-01-5-agent-mode-changes-in-v2-1-257.md%0ACard%20ID%3A%20claude-code-2026-09-01-765f93%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.257%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->