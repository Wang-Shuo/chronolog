---
card_id: claude-code-2026-10-05-1d1a15
date: '2026-10-05'
description: 'Claude Code · 2026-10-05 · Safety and Privacy: 19 changes in v2.1.290
  — Added `agentId` to the `tool.check` event of plugin hooks, so a hook can tell
  a…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1268
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2d0d08bbdfe046e65b3dbe9644fedf539596ef93bef744b825d6f1bd0ab9de3a
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-05-1d1a15
  comparison: ''
  date: '2026-10-05'
  description: 'Claude Code — v2.1.290: 19 Safety and Privacy changes'
  evidence:
  - quote: Added `agentId` to the `tool.check` event of plugin hooks, so a hook can
      tell a subagent's permission check from the main session's
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
  - quote: Added a /status and doctor warning when managed settings ignore user-configured
      sandbox allowRead paths or allowed domains
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
  - quote: Fixed `claude agents` sessions in manual permission mode asking for approval
      to read an image pasted into a reply or a new agent's prompt
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
  - quote: Fixed auto mode denials suggesting a permission rule that would skip the
      classifier for a whole tool or that Claude Code would ignore
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
  - quote: 'Fixed `--channels` permission relay: a reply ID that repeats within a
      session is now ignored instead of approving a different prompt'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
  - quote: Fixed Bash permission checks auto-approving some read-only commands (such
      as `rg` or `git grep`) whose arguments the shell would still expand as wildcards;
      these now prompt for approval
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
  - quote: Fixed Bash permission checks auto-approving certain commands whose variable
      names zsh reads differently from bash; these now prompt for approval
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
  - quote: Fixed sandboxed Monitor tool commands skipping the permission prompt under
      sandbox auto-allow; they now follow your permission rules
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
  - quote: Fixed a freeze when the secret scan or a permission prompt met long token-like
      text
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
  - quote: Fixed Bash permission checks not applying Read deny rules or the outside-directory
      read block to a wildcard in some option values of read-only commands
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
  - quote: Fixed some permission rules and safety checks not being applied to a tool
      call after a PreToolUse hook rewrote its input
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
  - quote: Fixed file names containing line breaks being displayed incorrectly in
      file tool errors and permission prompts
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
  - quote: Fixed edits to the file a symlinked settings file points at running without
      the settings-file permission question
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
  - quote: Improved permission prompts from background agents to show the Ctrl+X Ctrl+K
      shortcut that stops all background agents
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
  - quote: Changed the Bash tool to ask for permission before running `pyright`, which
      is no longer treated as a read-only command
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
  - quote: Changed Bash permission checks so that more forms of the `ps` command ask
      for approval instead of running without asking
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
  - quote: Changed the `claude-api` skill's Managed Agents examples to turn off the
      web tools unless the agent needs them and to use the `auto` permission policy
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
  - quote: '[VSCode] Fixed a permission prompt that arrived behind an open dialog
      taking keyboard focus, so a key pressed in the dialog could answer it'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
  - quote: '[Claude Tag] Fixed members with the Claude Tag Admin permission getting
      "Couldn''t load memory files" on the Activity page''s Memory tab; they can now
      read workspace and channel memory'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 19-safety-and-privacy-changes-in-v2-1-290
  source_release: claude-code-2026-10-05-v2-1-290-github-403993621-ae06f2b6
  source_type: github_releases
  theme: safety-privacy
  title: 19 Safety and Privacy changes in v2.1.290
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-30-4-safety-and-privacy-changes-in-v2-1-286|4 Safety
  and Privacy changes in v2.1.286]]'
- '[[Changes/Claude Code/2026-10-01-6-safety-and-privacy-changes-in-v2-1-287|6 Safety
  and Privacy changes in v2.1.287]]'
- '[[Changes/Claude Code/2026-10-02-6-safety-and-privacy-changes-in-v2-1-288|6 Safety
  and Privacy changes in v2.1.288]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-05-v2-1-290-github-403993621-ae06f2b6|claude-code-2026-10-05-v2-1-290-github-403993621-ae06f2b6]]'
source_type: github_releases
theme: safety-privacy
title: 19 Safety and Privacy changes in v2.1.290
type: change
---

<!-- chronolog:begin region="header" -->
# 19 Safety and Privacy changes in v2.1.290

**Claude Code** · 2026-10-05 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.290) · from [[Releases/Claude Code/claude-code-2026-10-05-v2-1-290-github-403993621-ae06f2b6|v2.1.290]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `agentId` to the `tool.check` event of plugin hooks, so a hook can tell a subagent's permission check from the main session's

> Added a /status and doctor warning when managed settings ignore user-configured sandbox allowRead paths or allowed domains

> Fixed `claude agents` sessions in manual permission mode asking for approval to read an image pasted into a reply or a new agent's prompt

> Fixed auto mode denials suggesting a permission rule that would skip the classifier for a whole tool or that Claude Code would ignore

> Fixed `--channels` permission relay: a reply ID that repeats within a session is now ignored instead of approving a different prompt

> Fixed Bash permission checks auto-approving some read-only commands (such as `rg` or `git grep`) whose arguments the shell would still expand as wildcards; these now prompt for approval

> Fixed Bash permission checks auto-approving certain commands whose variable names zsh reads differently from bash; these now prompt for approval

> Fixed sandboxed Monitor tool commands skipping the permission prompt under sandbox auto-allow; they now follow your permission rules

> Fixed a freeze when the secret scan or a permission prompt met long token-like text

> Fixed Bash permission checks not applying Read deny rules or the outside-directory read block to a wildcard in some option values of read-only commands

> Fixed some permission rules and safety checks not being applied to a tool call after a PreToolUse hook rewrote its input

> Fixed file names containing line breaks being displayed incorrectly in file tool errors and permission prompts

> Fixed edits to the file a symlinked settings file points at running without the settings-file permission question

> Improved permission prompts from background agents to show the Ctrl+X Ctrl+K shortcut that stops all background agents

> Changed the Bash tool to ask for permission before running `pyright`, which is no longer treated as a read-only command

> Changed Bash permission checks so that more forms of the `ps` command ask for approval instead of running without asking

> Changed the `claude-api` skill's Managed Agents examples to turn off the web tools unless the agent needs them and to use the `auto` permission policy

> [VSCode] Fixed a permission prompt that arrived behind an open dialog taking keyboard focus, so a key pressed in the dialog could answer it

> [Claude Tag] Fixed members with the Claude Tag Admin permission getting "Couldn't load memory files" on the Activity page's Memory tab; they can now read workspace and channel memory

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-05-changed-background-sessions-waiting-on-a-scheduled-wakeup-loop-they-are-now-left|Changed background sessions waiting on a scheduled wakeup (/loop)]] · Memory and Personalization
- [[Changes/Claude Code/2026-10-05-added-claude-api-managed-agents-onboard-url-to-set-up-the-managed-agents-pattern|Added /claude-api managed-agents-onboard url to set up the Managed Agents…]] · Agent Mode
- [[Changes/Claude Code/2026-10-05-added-claude-api-managed-agents-onboard-quickstart-name-to-build-a-console-quick|Added /claude-api managed-agents-onboard quickstart-name to build a Console…]] · Agent Mode
- [[Changes/Claude Code/2026-10-05-3-account-and-access-changes-in-v2-1-290|3 Account and Access changes in v2.1.290]] · Account and Access
- [[Changes/Claude Code/2026-10-05-vscode-added-a-screen-reader-announcement-message-queued-when-you-send-a-message|VSCode Added a screen reader announcement, "Message queued.", when you send…]] · Accessibility and Localization
- [[Changes/Claude Code/2026-10-05-changed-the-interactive-session-s-websearch-budget-to-refill-over-time-100-calls|Changed the interactive session's WebSearch budget to refill over time (100 calls/hour]] · Search and Browsing
- [[Changes/Claude Code/2026-10-05-14-apps-and-integrations-changes-in-v2-1-290|14 Apps and Integrations changes in v2.1.290]] · Apps and Integrations
- [[Changes/Claude Code/2026-10-05-4-agent-mode-changes-in-v2-1-290|4 Agent Mode changes in v2.1.290]] · Agent Mode
- [[Changes/Claude Code/2026-10-05-2-model-support-changes-in-v2-1-290|2 Model Support changes in v2.1.290]] · Model Support
- [[Changes/Claude Code/2026-10-05-5-developer-workflow-changes-in-v2-1-290|5 Developer Workflow changes in v2.1.290]] · Developer Workflow
- [[Changes/Claude Code/2026-10-05-changed-background-sessions-whose-scheduled-task-is-gone-they-now-move-to-comple|Changed background sessions whose scheduled task is gone]] · Automation and Scheduling
- [[Changes/Claude Code/2026-10-05-improved-responsiveness-while-resuming-large-sessions-timers-input-and-rendering|Improved responsiveness while resuming large sessions]] · Reliability and Performance
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-10-02 · Claude Code · [[Changes/Claude Code/2026-10-02-6-safety-and-privacy-changes-in-v2-1-288|6 Safety and Privacy changes in v2.1.288]]
- Later: 2026-10-06 · Claude Code · [[Changes/Claude Code/2026-10-06-6-safety-and-privacy-changes-in-v2-1-292|6 Safety and Privacy changes in v2.1.292]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-05-1d1a15&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-05-19-safety-and-privacy-changes-in-v2-1-290.md%0ACard%20ID%3A%20claude-code-2026-10-05-1d1a15%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.290%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->