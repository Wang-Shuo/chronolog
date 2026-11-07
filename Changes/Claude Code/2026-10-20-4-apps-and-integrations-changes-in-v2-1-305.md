---
card_id: claude-code-2026-10-20-315de1
date: '2026-10-20'
description: 'Claude Code · 2026-10-20 · Apps and Integrations: 4 changes in v2.1.305
  — Remote Control: Improved the spawn-mode messages: pressing `w` now says the new
  mode…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2867
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 4c13e8e09c27c7f038b99e2201a767670c3343eb651c8e3ab93be232f63f7ac4
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-20-315de1
  comparison: ''
  date: '2026-10-20'
  description: 'Claude Code — v2.1.305: 4 Apps and Integrations changes'
  evidence:
  - quote: 'Remote Control: Improved the spawn-mode messages: pressing `w` now says
      the new mode is saved for the folder, and a later `claude remote-control` start
      that uses the saved mode says where it came from'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.305
  - quote: 'Changed `allowedMcpServers` to stop filtering `managed-mcp.json` stdio
      servers that use `${VAR}` only in `env`: one your allowlist left out now loads
      on upgrade; use `deniedMcpServers` to keep it off'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.305
  - quote: Changed plugins that Claude Desktop mounts by path to no longer keep their
      `allowed-tools` when your organization's managed settings set `allowManagedPermissionRulesOnly`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.305
  - quote: '[Claude Tag] Improved Claude Tag admin pages in large organizations so
      plugin, skill and bundle edits work while the channel list is still loading'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.305
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 4-apps-and-integrations-changes-in-v2-1-305
  source_release: claude-code-2026-10-20-v2-1-305-github-418781864-90995baa
  source_type: github_releases
  theme: apps-integrations
  title: 4 Apps and Integrations changes in v2.1.305
  type: change
related_changes:
- '[[Changes/Krea/2026-10-19-quote-a-generation-with-mcp-preflight|Quote a generation
  with MCP preflight]]'
- '[[Changes/Lovable/2026-10-19-connect-your-app-to-cube|Connect your app to Cube]]'
- '[[Changes/v0/2026-10-19-connect-your-slack-workspace-to-v0-to-bring-team-conversations-into-your-work-wi|Connect
  your Slack workspace to v0 to bring team conversations into your work]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-20-v2-1-305-github-418781864-90995baa|claude-code-2026-10-20-v2-1-305-github-418781864-90995baa]]'
source_type: github_releases
theme: apps-integrations
title: 4 Apps and Integrations changes in v2.1.305
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Apps and Integrations changes in v2.1.305

**Claude Code** · 2026-10-20 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.305) · from [[Releases/Claude Code/claude-code-2026-10-20-v2-1-305-github-418781864-90995baa|v2.1.305]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Remote Control: Improved the spawn-mode messages: pressing `w` now says the new mode is saved for the folder, and a later `claude remote-control` start that uses the saved mode says where it came from

> Changed `allowedMcpServers` to stop filtering `managed-mcp.json` stdio servers that use `${VAR}` only in `env`: one your allowlist left out now loads on upgrade; use `deniedMcpServers` to keep it off

> Changed plugins that Claude Desktop mounts by path to no longer keep their `allowed-tools` when your organization's managed settings set `allowManagedPermissionRulesOnly`

> [Claude Tag] Improved Claude Tag admin pages in large organizations so plugin, skill and bundle edits work while the channel list is still loading

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.305
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-20-2-developer-workflow-changes-in-v2-1-305|2 Developer Workflow changes in v2.1.305]] · Developer Workflow
- [[Changes/Claude Code/2026-10-20-vscode-changed-the-message-shown-when-a-session-does-not-start-in-time-and-no-ho|VSCode Changed the message shown when a session does not start in time and no hook…]] · Account and Access
- [[Changes/Claude Code/2026-10-20-3-safety-and-privacy-changes-in-v2-1-305|3 Safety and Privacy changes in v2.1.305]] · Safety and Privacy
- [[Changes/Claude Code/2026-10-20-claude-tag-added-public-slack-channels-claude-hasn-t-joined-to-the-claude-tag-ad|Claude Tag Added public Slack channels Claude hasn't joined to the Claude Tag…]] · Enterprise and Administration
- [[Changes/Claude Code/2026-10-20-improved-a-mod-s-image-to-draw-its-picture-in-iterm2-3-5-and-later-with-fullscre|Improved a mod's Image to draw its picture in iTerm2 3.5 and later with fullscreen…]] · Interface Experience
- [[Changes/Claude Code/2026-10-20-vscode-added-a-running-start-up-hooks-spinner-status-with-a-screen-reader-announ|VSCode Added a "Running start-up hooks" spinner status, with a screen reader…]] · Accessibility and Localization
- [[Changes/Claude Code/2026-10-20-4-other-changes-in-v2-1-305|4 other changes in v2.1.305]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-10-19 · v0 · [[Changes/v0/2026-10-19-connect-your-slack-workspace-to-v0-to-bring-team-conversations-into-your-work-wi|Connect your Slack workspace to v0 to bring team conversations into your work]]
- Later: 2026-10-20 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-10-20-4-apps-and-integrations-changes-in-v1-0-101|4 Apps and Integrations changes in v1.0.101]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-20-315de1&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-20-4-apps-and-integrations-changes-in-v2-1-305.md%0ACard%20ID%3A%20claude-code-2026-10-20-315de1%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.305%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->