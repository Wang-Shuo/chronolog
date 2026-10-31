---
card_id: claude-code-2026-05-13-add191
date: '2026-05-13'
description: 'Claude Code · 2026-05-13 · Account and Access: Bedrock: `awsCredentialExport`
  now always runs when configured instead of being skipped when ambient AWS…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1140
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: 20f0afe0ead37baf6e25e595960d1706a2949af9a83a01b5d801657570978e7b
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-05-13-add191
  comparison: ''
  date: '2026-05-13'
  description: 'Claude Code — v2.1.141: Bedrock: `awsCredentialExport` now always
    runs when configured instead of being skipped when ambient AWS credentials resolve,
    fixing auth for cross-account access'
  evidence:
  - quote: 'Bedrock: `awsCredentialExport` now always runs when configured instead
      of being skipped when ambient AWS credentials resolve, fixing auth for cross-account
      access'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.141
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: claude-code
  product_name: Claude Code
  slug: bedrock-awscredentialexport-now-always-runs-when-configured-instead-of-being-ski
  source_release: claude-code-2026-05-13-v2-1-141-github-322186176-9f8e2e22
  source_type: github_releases
  theme: account-access
  title: 'Bedrock: `awsCredentialExport` now always runs when configured instead of
    being…'
  type: change
related_changes:
- '[[Changes/Claude Code/2026-05-04-channels-now-works-with-console-api-key-authentication-console-orgs-with-managed|--channels
  now works with console (API key) authentication]]'
- '[[Changes/ChatGPT/2026-05-05-chatgpt-for-excel-and-google-sheets-is-now-available-globally-bringing-chatgpt-i|ChatGPT
  for Excel and Google Sheets]]'
- '[[Changes/Claude Code/2026-05-06-improved-visual-consistency-in-slash-command-dialogs-and-login-upgrade-extra-usa|Improved
  visual consistency in slash command dialogs and /login, /upgrade…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-13-v2-1-141-github-322186176-9f8e2e22|claude-code-2026-05-13-v2-1-141-github-322186176-9f8e2e22]]'
source_type: github_releases
theme: account-access
title: 'Bedrock: awsCredentialExport now always runs when configured instead of being…'
type: change
---

<!-- chronolog:begin region="header" -->
# Bedrock: `awsCredentialExport` now always runs when configured instead of being…

**Claude Code** · 2026-05-13 · [[Themes/account-access|Account and Access]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.141) · from [[Releases/Claude Code/claude-code-2026-05-13-v2-1-141-github-322186176-9f8e2e22|v2.1.141]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Bedrock: `awsCredentialExport` now always runs when configured instead of being skipped when ambient AWS credentials resolve, fixing auth for cross-account access
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.141
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-05-13-5-safety-and-privacy-changes-in-v2-1-141|5 Safety and Privacy changes in v2.1.141]] · Safety and Privacy
- [[Changes/Claude Code/2026-05-13-2-interface-experience-changes-in-v2-1-141|2 Interface Experience changes in v2.1.141]] · Interface Experience
- [[Changes/Claude Code/2026-05-13-vscode-voice-mode-the-wsl-error-now-suggests-installing-sox-libsox-fmt-pulse-for|VSCode Voice mode]] · Voice and Audio
- [[Changes/Claude Code/2026-05-13-rewind-menu-added-summarize-up-to-here-to-compress-earlier-context-while-keeping|Rewind menu: added "Summarize up to here" to compress earlier context while keeping…]] · Context Window
- [[Changes/Claude Code/2026-05-13-feedback-can-now-include-recent-sessions-last-24-hours-or-7-days-for-issues-span|/feedback can now include recent sessions (last 24 hours or 7 days) for issues…]] · Projects and Workspaces
- [[Changes/Claude Code/2026-05-13-added-terminalsequence-field-to-hook-json-output-so-hooks-can-emit-desktop-notif|Added terminalSequence field to hook JSON output so hooks can emit desktop…]] · Developer Workflow
- [[Changes/Claude Code/2026-05-13-added-claude-code-plugin-prefer-https-to-clone-github-plugin-sources-over-https|Added CLAUDE_CODE_PLUGIN_PREFER_HTTPS to clone GitHub plugin sources over HTTPS…]] · Apps and Integrations
- [[Changes/Claude Code/2026-05-13-4-agent-mode-changes-in-v2-1-141|4 Agent Mode changes in v2.1.141]] · Agent Mode
- [[Changes/Claude Code/2026-05-13-added-anthropic-workspace-id-environment-variable-for-workload-identity-federati|Added ANTHROPIC_WORKSPACE_ID environment variable for workload identity federation]] · Enterprise and Administration
- [[Changes/Claude Code/2026-05-13-empty-idle-background-sessions-left-over-from-are-now-automatically-retired-by-t|Empty idle background sessions left over from ← are now automatically retired…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-05-06 · Claude Code · [[Changes/Claude Code/2026-05-06-improved-visual-consistency-in-slash-command-dialogs-and-login-upgrade-extra-usa|Improved visual consistency in slash command dialogs and /login, /upgrade…]]
- Later: 2026-06-02 · ChatGPT · [[Changes/ChatGPT/2026-06-02-active-sessions-shows-sessions-known-through-session-management-including-chatgp|Active sessions shows sessions known through session management, including ChatGPT…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-05-13-add191&body=Card%3A%20Changes%2FClaude%20Code%2F2026-05-13-bedrock-awscredentialexport-now-always-runs-when-configured-instead-of-being-ski.md%0ACard%20ID%3A%20claude-code-2026-05-13-add191%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.141%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->