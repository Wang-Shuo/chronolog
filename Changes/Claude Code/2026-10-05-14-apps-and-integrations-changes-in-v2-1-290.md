---
card_id: claude-code-2026-10-05-d0014b
date: '2026-10-05'
description: 'Claude Code · 2026-10-05 · Apps and Integrations: 14 changes in v2.1.290
  — Added `ThemeKey` and `Color` types to the plugin hooks typings, so an editor lists…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1292
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 258fd1199b61bee2bf09e13b015e77d0f776895ffec2731a81c7b01ad6a08963
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-05-d0014b
  comparison: ''
  date: '2026-10-05'
  description: 'Claude Code — v2.1.290: 14 Apps and Integrations changes'
  evidence:
  - quote: Added `ThemeKey` and `Color` types to the plugin hooks typings, so an editor
      lists the theme colors a mod's drawing can name
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
  - quote: 'Added to `claude plugin validate`: each hook a mod registers at a gating
      site is listed with whether it has a `.catch` (`gatingHooks` under `--json`)'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
  - quote: 'Improved MCP startup behind a network proxy: a server the proxy blocks
      (HTTP 403) is no longer retried three times'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
  - quote: 'Improved the built-in `plugin-authoring` skill: Claude now gives the one
      command another person runs to install a mod you made, and writes it in a README''s
      install section'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
  - quote: 'Improved the reply to `/plugin` in the desktop app''s Code tab: it now
      says where to install and manage plugins there'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
  - quote: 'Improved the Claude apps gateway''s log when an upstream''s cloud credentials
      or connection fail: the warning now ends with the underlying cause'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
  - quote: Improved the Claude apps gateway to log a warning during the last 30 days
      before the certificate it presents to the identity provider expires
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
  - quote: 'Changed what a mod''s `$.process.spawn` rejects with when another mod
      denies it after the child ran: it now says the call ran and a plugin withheld
      its result'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
  - quote: Changed plugin hooks so long text is clipped and logged instead of being
      refused or dropped silently
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
  - quote: Changed the Claude apps gateway's minimum supported PostgreSQL version
      from 14 to 11
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
  - quote: Changed `claude plugin update` on a plugin loaded from a directory to print
      just its reason, without the "Failed to update plugin" prefix, as for built-in
      plugins
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
  - quote: '[VSCode] Added a way to review and run a plugin marketplace''s install
      or update command from the Manage plugins dialog'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
  - quote: '[VSCode] Improved Continue After Reload: tabs reopened after VS Code restarts
      its extensions now also finish a step the restart interrupted'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
  - quote: '[Claude Tag] Improved the earlier Claude in Slack app''s reply when it
      can''t start a session: it now says what failed and who can fix it, in full
      only once per thread'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 14-apps-and-integrations-changes-in-v2-1-290
  source_release: claude-code-2026-10-05-v2-1-290-github-403993621-ae06f2b6
  source_type: github_releases
  theme: apps-integrations
  title: 14 Apps and Integrations changes in v2.1.290
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-01-11-apps-and-integrations-changes-in-v2-1-287|11
  Apps and Integrations changes in v2.1.287]]'
- '[[Changes/Claude Code/2026-10-02-5-apps-and-integrations-changes-in-v2-1-288|5
  Apps and Integrations changes in v2.1.288]]'
- '[[Changes/Claude Code/2026-10-03-2-apps-and-integrations-changes-in-v2-1-289|2
  Apps and Integrations changes in v2.1.289]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-05-v2-1-290-github-403993621-ae06f2b6|claude-code-2026-10-05-v2-1-290-github-403993621-ae06f2b6]]'
source_type: github_releases
theme: apps-integrations
title: 14 Apps and Integrations changes in v2.1.290
type: change
---

<!-- chronolog:begin region="header" -->
# 14 Apps and Integrations changes in v2.1.290

**Claude Code** · 2026-10-05 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.290) · from [[Releases/Claude Code/claude-code-2026-10-05-v2-1-290-github-403993621-ae06f2b6|v2.1.290]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `ThemeKey` and `Color` types to the plugin hooks typings, so an editor lists the theme colors a mod's drawing can name

> Added to `claude plugin validate`: each hook a mod registers at a gating site is listed with whether it has a `.catch` (`gatingHooks` under `--json`)

> Improved MCP startup behind a network proxy: a server the proxy blocks (HTTP 403) is no longer retried three times

> Improved the built-in `plugin-authoring` skill: Claude now gives the one command another person runs to install a mod you made, and writes it in a README's install section

> Improved the reply to `/plugin` in the desktop app's Code tab: it now says where to install and manage plugins there

> Improved the Claude apps gateway's log when an upstream's cloud credentials or connection fail: the warning now ends with the underlying cause

> Improved the Claude apps gateway to log a warning during the last 30 days before the certificate it presents to the identity provider expires

> Changed what a mod's `$.process.spawn` rejects with when another mod denies it after the child ran: it now says the call ran and a plugin withheld its result

> Changed plugin hooks so long text is clipped and logged instead of being refused or dropped silently

> Changed the Claude apps gateway's minimum supported PostgreSQL version from 14 to 11

> Changed `claude plugin update` on a plugin loaded from a directory to print just its reason, without the "Failed to update plugin" prefix, as for built-in plugins

> [VSCode] Added a way to review and run a plugin marketplace's install or update command from the Manage plugins dialog

> [VSCode] Improved Continue After Reload: tabs reopened after VS Code restarts its extensions now also finish a step the restart interrupted

> [Claude Tag] Improved the earlier Claude in Slack app's reply when it can't start a session: it now says what failed and who can fix it, in full only once per thread

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
- [[Changes/Claude Code/2026-10-05-4-agent-mode-changes-in-v2-1-290|4 Agent Mode changes in v2.1.290]] · Agent Mode
- [[Changes/Claude Code/2026-10-05-2-model-support-changes-in-v2-1-290|2 Model Support changes in v2.1.290]] · Model Support
- [[Changes/Claude Code/2026-10-05-5-developer-workflow-changes-in-v2-1-290|5 Developer Workflow changes in v2.1.290]] · Developer Workflow
- [[Changes/Claude Code/2026-10-05-changed-background-sessions-whose-scheduled-task-is-gone-they-now-move-to-comple|Changed background sessions whose scheduled task is gone]] · Automation and Scheduling
- [[Changes/Claude Code/2026-10-05-improved-responsiveness-while-resuming-large-sessions-timers-input-and-rendering|Improved responsiveness while resuming large sessions]] · Reliability and Performance
- [[Changes/Claude Code/2026-10-05-18-other-changes-in-v2-1-290|18 other changes in v2.1.290]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-10-03 · Claude Code · [[Changes/Claude Code/2026-10-03-2-apps-and-integrations-changes-in-v2-1-289|2 Apps and Integrations changes in v2.1.289]]
- Later: 2026-10-06 · Claude Code · [[Changes/Claude Code/2026-10-06-9-apps-and-integrations-changes-in-v2-1-292|9 Apps and Integrations changes in v2.1.292]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-05-d0014b&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-05-14-apps-and-integrations-changes-in-v2-1-290.md%0ACard%20ID%3A%20claude-code-2026-10-05-d0014b%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.290%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->