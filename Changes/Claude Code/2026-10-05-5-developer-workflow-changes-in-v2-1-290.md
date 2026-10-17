---
card_id: claude-code-2026-10-05-f639e9
date: '2026-10-05'
description: 'Claude Code · 2026-10-05 · Developer Workflow: 5 changes in v2.1.290
  — Improved the Bash changed-files view: when a chained command includes git merge,
  pull or…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1297
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 152506f7c03cb78e5308a62568a3b12d0c6f2fe4586db94a6a2932f1a71784f0
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-05-f639e9
  comparison: ''
  date: '2026-10-05'
  description: 'Claude Code — v2.1.290: 5 Developer Workflow changes'
  evidence:
  - quote: 'Improved the Bash changed-files view: when a chained command includes
      git merge, pull or checkout, it lists the files without full diffs'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
  - quote: 'Improved the error shown when a git config file stops the `/ultrareview`
      upload: it is about half as long and says what kind of file is the problem'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
  - quote: Changed skills and custom commands to refuse a `!` shell command that contains
      raw control characters other than tab and newline, with a message that shows
      where they are
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
  - quote: 'Changed the errors shown when the `/ultrareview` upload fails at a git
      step: they name the step and what to try, and no longer repeat git''s own error
      text'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
  - quote: Changed `CLAUDE_CODE_DISABLE_ATTACHMENTS` so a repository's `.claude/settings.json`
      or `.claude/settings.local.json` can no longer set it; shell, user and managed
      settings still can
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 5-developer-workflow-changes-in-v2-1-290
  source_release: claude-code-2026-10-05-v2-1-290-github-403993621-ae06f2b6
  source_type: github_releases
  theme: developer-workflow
  title: 5 Developer Workflow changes in v2.1.290
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-30-3-developer-workflow-changes-in-v2-1-286|3 Developer
  Workflow changes in v2.1.286]]'
- '[[Changes/Claude Code/2026-10-01-3-developer-workflow-changes-in-v2-1-287|3 Developer
  Workflow changes in v2.1.287]]'
- '[[Changes/Claude Code/2026-10-02-3-developer-workflow-changes-in-v2-1-288|3 Developer
  Workflow changes in v2.1.288]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-05-v2-1-290-github-403993621-ae06f2b6|claude-code-2026-10-05-v2-1-290-github-403993621-ae06f2b6]]'
source_type: github_releases
theme: developer-workflow
title: 5 Developer Workflow changes in v2.1.290
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Developer Workflow changes in v2.1.290

**Claude Code** · 2026-10-05 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.290) · from [[Releases/Claude Code/claude-code-2026-10-05-v2-1-290-github-403993621-ae06f2b6|v2.1.290]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Improved the Bash changed-files view: when a chained command includes git merge, pull or checkout, it lists the files without full diffs

> Improved the error shown when a git config file stops the `/ultrareview` upload: it is about half as long and says what kind of file is the problem

> Changed skills and custom commands to refuse a `!` shell command that contains raw control characters other than tab and newline, with a message that shows where they are

> Changed the errors shown when the `/ultrareview` upload fails at a git step: they name the step and what to try, and no longer repeat git's own error text

> Changed `CLAUDE_CODE_DISABLE_ATTACHMENTS` so a repository's `.claude/settings.json` or `.claude/settings.local.json` can no longer set it; shell, user and managed settings still can

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-05-changed-background-sessions-waiting-on-a-scheduled-wakeup-loop-they-are-now-left|Changed background sessions waiting on a scheduled wakeup (/loop)]] · Memory and Personalization
- [[Changes/Claude Code/2026-10-05-added-claude-api-managed-agents-onboard-url-to-set-up-the-managed-agents-pattern|Added /claude-api managed-agents-onboard url to set up the Managed Agents…]] · Agent Mode
- [[Changes/Claude Code/2026-10-05-19-safety-and-privacy-changes-in-v2-1-290|19 Safety and Privacy changes in v2.1.290]] · Safety and Privacy
- [[Changes/Claude Code/2026-10-05-added-claude-api-managed-agents-onboard-quickstart-name-to-build-a-console-quick|Added /claude-api managed-agents-onboard quickstart-name to build a Console…]] · Agent Mode
- [[Changes/Claude Code/2026-10-05-3-account-and-access-changes-in-v2-1-290|3 Account and Access changes in v2.1.290]] · Account and Access
- [[Changes/Claude Code/2026-10-05-vscode-added-a-screen-reader-announcement-message-queued-when-you-send-a-message|VSCode Added a screen reader announcement, "Message queued.", when you send…]] · Accessibility and Localization
- [[Changes/Claude Code/2026-10-05-changed-the-interactive-session-s-websearch-budget-to-refill-over-time-100-calls|Changed the interactive session's WebSearch budget to refill over time (100 calls/hour]] · Search and Browsing
- [[Changes/Claude Code/2026-10-05-14-apps-and-integrations-changes-in-v2-1-290|14 Apps and Integrations changes in v2.1.290]] · Apps and Integrations
- [[Changes/Claude Code/2026-10-05-4-agent-mode-changes-in-v2-1-290|4 Agent Mode changes in v2.1.290]] · Agent Mode
- [[Changes/Claude Code/2026-10-05-2-model-support-changes-in-v2-1-290|2 Model Support changes in v2.1.290]] · Model Support
- [[Changes/Claude Code/2026-10-05-changed-background-sessions-whose-scheduled-task-is-gone-they-now-move-to-comple|Changed background sessions whose scheduled task is gone]] · Automation and Scheduling
- [[Changes/Claude Code/2026-10-05-improved-responsiveness-while-resuming-large-sessions-timers-input-and-rendering|Improved responsiveness while resuming large sessions]] · Reliability and Performance
- [[Changes/Claude Code/2026-10-05-18-other-changes-in-v2-1-290|18 other changes in v2.1.290]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-10-02 · Claude Code · [[Changes/Claude Code/2026-10-02-3-developer-workflow-changes-in-v2-1-288|3 Developer Workflow changes in v2.1.288]]
- Later: 2026-10-06 · Claude Code · [[Changes/Claude Code/2026-10-06-2-developer-workflow-changes-in-v2-1-292|2 Developer Workflow changes in v2.1.292]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-05-f639e9&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-05-5-developer-workflow-changes-in-v2-1-290.md%0ACard%20ID%3A%20claude-code-2026-10-05-f639e9%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.290%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->