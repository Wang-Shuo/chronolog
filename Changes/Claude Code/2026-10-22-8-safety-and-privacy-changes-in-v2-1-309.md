---
card_id: claude-code-2026-10-22-2b30d3
date: '2026-10-22'
description: 'Claude Code · 2026-10-22 · Safety and Privacy: 8 changes in v2.1.309
  — Fixed a disabled MCP server being reconnected by a later permission prompt in
  print and…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1285
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: dc41c940674e560c1866afc2a95925854409da44a377395bcd5e41c054ade1f9
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-22-2b30d3
  comparison: ''
  date: '2026-10-22'
  description: 'Claude Code — v2.1.309: 8 Safety and Privacy changes'
  evidence:
  - quote: Fixed a disabled MCP server being reconnected by a later permission prompt
      in print and SDK sessions
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.309
  - quote: Fixed the Bash permission check trusting a variable set by a command whose
      redirect can fail to open
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.309
  - quote: Fixed Bash permission checks not prompting for some compound commands that
      change directory before running git when the `cd` is wrapped or prefixed, as
      they do for a plain `cd`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.309
  - quote: Fixed Claude asking for permission on each artifact update for the rest
      of a turn after the conversation was compacted in that turn
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.309
  - quote: 'Windows: Fixed PowerShell permission checks auto-approving some `Set-Location`
      or `cd` commands that target the current directory and carry extra arguments;
      these now prompt for approval'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.309
  - quote: 'Changed `claude ultrareview` to require workspace trust: it asks on a
      terminal, else refuses; scripts pass `--trust-workspace`, which takes no value
      (put a PR number or base branch before it), or set `CLAUDE_CODE_DISABLE_ULTRAREVIEW_TRUST_CHECK=1`'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.309
  - quote: Changed commands the settings exclude from the sandbox to ask before writing
      to its write-list paths while the sandbox is enabled but cannot run; the unsandboxed
      fallback is refused there
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.309
  - quote: Changed worktree creation and reuse so git no longer fetches objects on
      demand, in ordinary clones and in partial clones with a Bash sandbox configured;
      such a partial clone fetches them first
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.309
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 8-safety-and-privacy-changes-in-v2-1-309
  source_release: claude-code-2026-10-22-v2-1-309-github-421170674-b2394d99
  source_type: github_releases
  theme: safety-privacy
  title: 8 Safety and Privacy changes in v2.1.309
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-19-added-decider-person-to-a-mod-s-tool-check-answer-only-the-permission-dialog-or|Added
  decider: "person" to a mod''s tool.check answer: only the permission dialog…]]'
- '[[Changes/Claude Code/2026-10-20-3-safety-and-privacy-changes-in-v2-1-305|3 Safety
  and Privacy changes in v2.1.305]]'
- '[[Changes/Claude Code/2026-10-21-added-the-claude-code-safety-event-opentelemetry-event-for-each-tool-call-a-perm|Added
  the claude_code.safety_event OpenTelemetry event for each tool call…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-22-v2-1-309-github-421170674-b2394d99|claude-code-2026-10-22-v2-1-309-github-421170674-b2394d99]]'
source_type: github_releases
theme: safety-privacy
title: 8 Safety and Privacy changes in v2.1.309
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Safety and Privacy changes in v2.1.309

**Claude Code** · 2026-10-22 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.309) · from [[Releases/Claude Code/claude-code-2026-10-22-v2-1-309-github-421170674-b2394d99|v2.1.309]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Fixed a disabled MCP server being reconnected by a later permission prompt in print and SDK sessions

> Fixed the Bash permission check trusting a variable set by a command whose redirect can fail to open

> Fixed Bash permission checks not prompting for some compound commands that change directory before running git when the `cd` is wrapped or prefixed, as they do for a plain `cd`

> Fixed Claude asking for permission on each artifact update for the rest of a turn after the conversation was compacted in that turn

> Windows: Fixed PowerShell permission checks auto-approving some `Set-Location` or `cd` commands that target the current directory and carry extra arguments; these now prompt for approval

> Changed `claude ultrareview` to require workspace trust: it asks on a terminal, else refuses; scripts pass `--trust-workspace`, which takes no value (put a PR number or base branch before it), or set `CLAUDE_CODE_DISABLE_ULTRAREVIEW_TRUST_CHECK=1`

> Changed commands the settings exclude from the sandbox to ask before writing to its write-list paths while the sandbox is enabled but cannot run; the unsandboxed fallback is refused there

> Changed worktree creation and reuse so git no longer fetches objects on demand, in ordinary clones and in partial clones with a Bash sandbox configured; such a partial clone fetches them first

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.309
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-22-2-reliability-and-performance-changes-in-v2-1-309|2 Reliability and Performance changes in v2.1.309]] · Reliability and Performance
- [[Changes/Claude Code/2026-10-22-2-apps-and-integrations-changes-in-v2-1-309|2 Apps and Integrations changes in v2.1.309]] · Apps and Integrations
- [[Changes/Claude Code/2026-10-22-improved-disk-full-handling-a-bash-command-cut-off-by-a-full-disk-now-says-so-an|Improved disk-full handling]] · Developer Workflow
- [[Changes/Claude Code/2026-10-22-changed-the-dangerous-rm-and-rmdir-prompt-in-bypass-permissions-mode-in-the-desk|Changed the dangerous rm and rmdir prompt in bypass permissions mode…]] · Mobile and Desktop
- [[Changes/Claude Code/2026-10-22-updated-the-claude-api-skill-service-account-keys-and-workload-identity-federati|Updated the /claude-api skill]] · Context Window
- [[Changes/Claude Code/2026-10-22-2-editor-experience-changes-in-v2-1-309|2 Editor Experience changes in v2.1.309]] · Editor Experience
- [[Changes/Claude Code/2026-10-22-vscode-added-a-log-warning-that-says-what-to-do-when-dictation-or-the-extension|VSCode Added a log warning that says what to do when dictation or the extension's…]] · Voice and Audio
- [[Changes/Claude Code/2026-10-22-changed-the-claude-api-skill-to-build-managed-agents-subagent-teams-on-multiagen|Changed the /claude-api skill to build Managed Agents subagent teams…]] · Agent Mode
- [[Changes/Claude Code/2026-10-22-3-other-changes-in-v2-1-309|3 other changes in v2.1.309]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-10-21 · Claude Code · [[Changes/Claude Code/2026-10-21-added-the-claude-code-safety-event-opentelemetry-event-for-each-tool-call-a-perm|Added the claude_code.safety_event OpenTelemetry event for each tool call…]]
- Later: 2026-10-23 · Claude Code · [[Changes/Claude Code/2026-10-23-4-safety-and-privacy-changes-in-v2-1-310|4 Safety and Privacy changes in v2.1.310]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-22-2b30d3&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-22-8-safety-and-privacy-changes-in-v2-1-309.md%0ACard%20ID%3A%20claude-code-2026-10-22-2b30d3%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.309%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->