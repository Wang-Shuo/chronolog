---
card_id: claude-code-2026-09-01-a7bdf3
date: '2026-09-01'
description: 'Claude Code · 2026-09-01 · Safety and Privacy: 10 changes in v2.1.257
  — Added a `/doctor` warning for stale sandbox mask files left by a killed session'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1234
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a7d151e2a778c1929fe1d0a49e5a2202672b2477fdc756755cdc607e151aa45a
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-01-a7bdf3
  comparison: ''
  date: '2026-09-01'
  description: 'Claude Code — v2.1.257: 10 Safety and Privacy changes'
  evidence:
  - quote: Added a `/doctor` warning for stale sandbox mask files left by a killed
      session
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.257
  - quote: Fixed sessions dispatched from an agent view opened with `←` always starting
      in the original session's permission mode, overriding the target directory's
      `defaultMode` and the agent's `permissionMode`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.257
  - quote: Fixed a teammate permission request being answered twice when the leader's
      mailbox write was briefly locked
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.257
  - quote: Fixed dismissing the Remote Control consent prompt (Esc, or `n` at `claude
      remote-control`) counting as consent, so the next request connected without
      asking
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.257
  - quote: Fixed the Edit permission prompt's diff view rendering emoji and multi-code-point
      characters with incorrect widths
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.257
  - quote: Fixed Bash permission checks auto-approving certain `[[ ]]` conditionals
      that zsh parses differently from bash; these commands now prompt for approval
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.257
  - quote: 'Improved notifications: an MCP elicitation or permission ask queued under
      another dialog now sends its idle desktop notification at the same delay as
      a visible ask'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.257
  - quote: 'Changed `managedSourcesBehavior: "merge"` to take `sandbox.credentials.awsPairs`
      and `sandbox.ripgrep` whole from the highest managed source that sets them instead
      of combining the sources'' values'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.257
  - quote: 'Changed `defaultMode: "bypassPermissions"` in `.claude/settings.json`
      or `.claude/settings.local.json` to be ignored, like `"auto"`; set it in user
      or managed settings, or pass `--permission-mode`'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.257
  - quote: Removed the Ctrl+E command explanation on Bash and PowerShell permission
      prompts
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.257
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 10-safety-and-privacy-changes-in-v2-1-257
  source_release: claude-code-2026-09-01-v2-1-257-github-380686035-b86855a6
  source_type: github_releases
  theme: safety-privacy
  title: 10 Safety and Privacy changes in v2.1.257
  type: change
related_changes:
- '[[Changes/Claude Code/2026-08-27-4-safety-and-privacy-changes-in-v2-1-248|4 Safety
  and Privacy changes in v2.1.248]]'
- '[[Changes/Claude Code/2026-08-28-6-safety-and-privacy-changes-in-v2-1-251|6 Safety
  and Privacy changes in v2.1.251]]'
- '[[Changes/Claude Code/2026-09-01-fixed-remote-and-scheduled-sessions-failing-with-user-messages-must-have-non-emp|Fixed
  remote and scheduled sessions failing…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-01-v2-1-257-github-380686035-b86855a6|claude-code-2026-09-01-v2-1-257-github-380686035-b86855a6]]'
source_type: github_releases
theme: safety-privacy
title: 10 Safety and Privacy changes in v2.1.257
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Safety and Privacy changes in v2.1.257

**Claude Code** · 2026-09-01 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.257) · from [[Releases/Claude Code/claude-code-2026-09-01-v2-1-257-github-380686035-b86855a6|v2.1.257]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added a `/doctor` warning for stale sandbox mask files left by a killed session

> Fixed sessions dispatched from an agent view opened with `←` always starting in the original session's permission mode, overriding the target directory's `defaultMode` and the agent's `permissionMode`

> Fixed a teammate permission request being answered twice when the leader's mailbox write was briefly locked

> Fixed dismissing the Remote Control consent prompt (Esc, or `n` at `claude remote-control`) counting as consent, so the next request connected without asking

> Fixed the Edit permission prompt's diff view rendering emoji and multi-code-point characters with incorrect widths

> Fixed Bash permission checks auto-approving certain `[[ ]]` conditionals that zsh parses differently from bash; these commands now prompt for approval

> Improved notifications: an MCP elicitation or permission ask queued under another dialog now sends its idle desktop notification at the same delay as a visible ask

> Changed `managedSourcesBehavior: "merge"` to take `sandbox.credentials.awsPairs` and `sandbox.ripgrep` whole from the highest managed source that sets them instead of combining the sources' values

> Changed `defaultMode: "bypassPermissions"` in `.claude/settings.json` or `.claude/settings.local.json` to be ignored, like `"auto"`; set it in user or managed settings, or pass `--permission-mode`

> Removed the Ctrl+E command explanation on Bash and PowerShell permission prompts

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.257
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-01-2-editor-experience-changes-in-v2-1-257|2 Editor Experience changes in v2.1.257]] · Editor Experience
- [[Changes/Claude Code/2026-09-01-3-developer-workflow-changes-in-v2-1-257|3 Developer Workflow changes in v2.1.257]] · Developer Workflow
- [[Changes/Claude Code/2026-09-01-improved-prompt-input-responsiveness-by-reducing-per-keystroke-rendering-work|Improved prompt input responsiveness by reducing per-keystroke rendering work]] · Reliability and Performance
- [[Changes/Claude Code/2026-09-01-5-agent-mode-changes-in-v2-1-257|5 Agent Mode changes in v2.1.257]] · Agent Mode
- [[Changes/Claude Code/2026-09-01-changed-btw-history-browsing-from-to-shift-shift-or-stepping-through-your-recent|Changed /btw history browsing from ←/→ to Shift+←/Shift+→ (or /)…]] · Search and Browsing
- [[Changes/Claude Code/2026-09-01-changed-add-dir-add-dir-and-additionaldirectories-to-refuse-network-paths-unc-sh|Changed --add-dir, /add-dir, and additionalDirectories to refuse network paths…]] · Mobile and Desktop
- [[Changes/Claude Code/2026-09-01-2-apps-and-integrations-changes-in-v2-1-257|2 Apps and Integrations changes in v2.1.257]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-01-2-account-and-access-changes-in-v2-1-257|2 Account and Access changes in v2.1.257]] · Account and Access
- [[Changes/Claude Code/2026-09-01-2-interface-experience-changes-in-v2-1-257|2 Interface Experience changes in v2.1.257]] · Interface Experience
- [[Changes/Claude Code/2026-09-01-6-model-support-changes-in-v2-1-257|6 Model Support changes in v2.1.257]] · Model Support
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-09-01 · Claude Code · [[Changes/Claude Code/2026-09-01-fixed-remote-and-scheduled-sessions-failing-with-user-messages-must-have-non-emp|Fixed remote and scheduled sessions failing…]]
- Later: 2026-09-02 · Claude Code · [[Changes/Claude Code/2026-09-02-4-safety-and-privacy-changes-in-v2-1-259|4 Safety and Privacy changes in v2.1.259]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-01-a7bdf3&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-01-10-safety-and-privacy-changes-in-v2-1-257.md%0ACard%20ID%3A%20claude-code-2026-09-01-a7bdf3%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.257%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->