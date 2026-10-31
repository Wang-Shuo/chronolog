---
card_id: claude-code-2026-05-13-fdd0e0
date: '2026-05-13'
description: 'Claude Code · 2026-05-13 · Enterprise and Administration: Added `ANTHROPIC_WORKSPACE_ID`
  environment variable for workload identity federation — scopes the…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2024-03-20-admin-improvements-team-admins-can-now-mark-themselves-as-unpaid-users-and-can-s|Admin
    improvements: Team admins can now mark themselves as unpaid users and can see…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 784
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: enterprise-admin
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: 113befa11ae7ff14d518ec6ac5f888a9277cb9d613899d4ecb803546386be655
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-05-13-fdd0e0
  comparison: ''
  date: '2026-05-13'
  description: 'Claude Code — v2.1.141: Added `ANTHROPIC_WORKSPACE_ID` environment
    variable for workload identity federation — scopes the minted token to a specific
    workspace when the federation rule covers more than one'
  evidence:
  - quote: Added `ANTHROPIC_WORKSPACE_ID` environment variable for workload identity
      federation — scopes the minted token to a specific workspace when the federation
      rule covers more than one
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.141
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: claude-code
  product_name: Claude Code
  slug: added-anthropic-workspace-id-environment-variable-for-workload-identity-federati
  source_release: claude-code-2026-05-13-v2-1-141-github-322186176-9f8e2e22
  source_type: github_releases
  theme: enterprise-admin
  theme_matches: []
  theme_resolution: manual-backfill-review-v1
  title: Added `ANTHROPIC_WORKSPACE_ID` environment variable for workload identity
    federation
  type: change
related_changes:
- '[[Changes/Claude Code/2026-05-07-added-parentsettingsbehavior-admin-tier-key-first-wins-merge-to-let-admins-opt-s|Added
  parentSettingsBehavior admin-tier key (''first-wins''  /  ''merge'') to let…]]'
- '[[Changes/Claude Code/2026-05-08-added-claude-code-enable-feedback-survey-for-otel-to-re-enable-the-session-quali|Added
  CLAUDE_CODE_ENABLE_FEEDBACK_SURVEY_FOR_OTEL to re-enable the session quality…]]'
- '[[Changes/Cursor/2026-05-11-teams-admins-and-individual-plan-users-can-now-customize-the-effort-level-bugbot|Teams
  admins and Individual plan users can now customize the effort level Bugbot…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-13-v2-1-141-github-322186176-9f8e2e22|claude-code-2026-05-13-v2-1-141-github-322186176-9f8e2e22]]'
source_type: github_releases
theme: enterprise-admin
title: Added ANTHROPIC_WORKSPACE_ID environment variable for workload identity federation
type: change
---

<!-- chronolog:begin region="header" -->
# Added `ANTHROPIC_WORKSPACE_ID` environment variable for workload identity federation

**Claude Code** · 2026-05-13 · [[Themes/enterprise-admin|Enterprise and Administration]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.141) · from [[Releases/Claude Code/claude-code-2026-05-13-v2-1-141-github-322186176-9f8e2e22|v2.1.141]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `ANTHROPIC_WORKSPACE_ID` environment variable for workload identity federation — scopes the minted token to a specific workspace when the federation rule covers more than one
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
- [[Changes/Claude Code/2026-05-13-bedrock-awscredentialexport-now-always-runs-when-configured-instead-of-being-ski|Bedrock: awsCredentialExport now always runs when configured instead of being…]] · Account and Access
- [[Changes/Claude Code/2026-05-13-added-terminalsequence-field-to-hook-json-output-so-hooks-can-emit-desktop-notif|Added terminalSequence field to hook JSON output so hooks can emit desktop…]] · Developer Workflow
- [[Changes/Claude Code/2026-05-13-added-claude-code-plugin-prefer-https-to-clone-github-plugin-sources-over-https|Added CLAUDE_CODE_PLUGIN_PREFER_HTTPS to clone GitHub plugin sources over HTTPS…]] · Apps and Integrations
- [[Changes/Claude Code/2026-05-13-4-agent-mode-changes-in-v2-1-141|4 Agent Mode changes in v2.1.141]] · Agent Mode
- [[Changes/Claude Code/2026-05-13-empty-idle-background-sessions-left-over-from-are-now-automatically-retired-by-t|Empty idle background sessions left over from ← are now automatically retired…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Enterprise and Administration

- Earlier: 2026-05-11 · Cursor · [[Changes/Cursor/2026-05-11-teams-admins-and-individual-plan-users-can-now-customize-the-effort-level-bugbot|Teams admins and Individual plan users can now customize the effort level Bugbot…]]
- Later: 2026-06-03 · Cursor · [[Changes/Cursor/2026-06-03-admins-can-move-users-between-teams-through-the-dashboard-api-or-csv|Admins can move users between teams through the dashboard, API, or CSV]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2024-03-20 · Cursor · [[Changes/Cursor/2024-03-20-admin-improvements-team-admins-can-now-mark-themselves-as-unpaid-users-and-can-s|Admin improvements: Team admins can now mark themselves as unpaid users and can see…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-05-13-fdd0e0&body=Card%3A%20Changes%2FClaude%20Code%2F2026-05-13-added-anthropic-workspace-id-environment-variable-for-workload-identity-federati.md%0ACard%20ID%3A%20claude-code-2026-05-13-fdd0e0%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.141%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->