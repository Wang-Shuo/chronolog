---
card_id: github-copilot-cli-2026-06-05-55bf95
date: '2026-06-05'
description: 'GitHub Copilot CLI · 2026-06-05 · Editor Experience: 3 changes in 1.0.60
  — Tab completes `..` parent traversal in slash-command path arguments instead of…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3
    Editor Experience changes in 0.0.37]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1179
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: editor-experience
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 93d613bf52bbba3a010e5373372a2d6030c9572e8329b1992b6ad64e95f3e6d1
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-06-05-55bf95
  comparison: ''
  date: '2026-06-05'
  description: 'GitHub Copilot CLI — 1.0.60: 3 Editor Experience changes'
  evidence:
  - quote: Tab completes `..` parent traversal in slash-command path arguments instead
      of switching tabs
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.60
  - quote: IDE picker now hides entries whose editor connection has gone away, so
      selecting one no longer fails with a connection error, and appends a process
      id to entries that share the same editor and folder so git worktrees of the
      same repo can be told apart
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.60
  - quote: Prompt for approval before running commands that set dynamic-loader or
      git-config env vars (e.g. LD_PRELOAD, GIT_EXTERNAL_DIFF)
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.60
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 3-editor-experience-changes-in-v1-0-60
  source_release: github-copilot-cli-2026-06-05-v1-0-60-github-335046279-6a5628d4
  source_type: github_releases
  theme: editor-experience
  title: 3 Editor Experience changes in v1.0.60
  type: change
related_changes:
- '[[Changes/Claude Code/2026-06-02-edit-no-longer-requires-a-separate-read-after-viewing-a-file-with-grep-single-fi|Edit
  no longer requires a separate Read after viewing a file with grep]]'
- '[[Changes/Claude Code/2026-06-03-renamed-windsurf-to-devin-desktop-in-the-ide-menu-terminal-setup-and-scroll-spee|Renamed
  Windsurf to Devin Desktop in the /ide menu, /terminal-setup…]]'
- '[[Changes/Google Antigravity/2026-06-03-antivirus-and-open-ide-fixes|Antivirus
  and Open IDE fixes]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-05-v1-0-60-github-335046279-6a5628d4|github-copilot-cli-2026-06-05-v1-0-60-github-335046279-6a5628d4]]'
source_type: github_releases
theme: editor-experience
title: 3 Editor Experience changes in v1.0.60
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Editor Experience changes in v1.0.60

**GitHub Copilot CLI** · 2026-06-05 · [[Themes/editor-experience|Editor Experience]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.60) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-05-v1-0-60-github-335046279-6a5628d4|1.0.60]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Tab completes `..` parent traversal in slash-command path arguments instead of switching tabs

> IDE picker now hides entries whose editor connection has gone away, so selecting one no longer fails with a connection error, and appends a process id to entries that share the same editor and folder so git worktrees of the same repo can be told apart

> Prompt for approval before running commands that set dynamic-loader or git-config env vars (e.g. LD_PRELOAD, GIT_EXTERNAL_DIFF)

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.60
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-06-05-add-billing-help-topic-with-an-overview-of-ai-credit-usage-features|Add billing help topic with an overview of AI credit usage features]] · Pricing Model
- [[Changes/GitHub Copilot CLI/2026-06-05-show-the-mission-control-sharing-status-of-synced-sessions-in-the-session-info-v|Show the Mission Control sharing status of synced sessions in the /session info view]] · Collaboration
- [[Changes/GitHub Copilot CLI/2026-06-05-6-interface-experience-changes-in-v1-0-60|6 Interface Experience changes in v1.0.60]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-06-05-11-developer-workflow-changes-in-v1-0-60|11 Developer Workflow changes in v1.0.60]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-06-05-mcp-tools-added-or-removed-by-a-server-mid-turn-are-now-available-immediately-in|MCP tools added or removed by a server mid-turn are now available immediately…]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-06-05-mcp-oauth-re-authentication-no-longer-fails-with-an-address-in-use-error-when-a|MCP OAuth re-authentication no longer fails with an address-in-use error…]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-06-05-2-agent-mode-changes-in-v1-0-60|2 Agent Mode changes in v1.0.60]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-06-05-2-model-support-changes-in-v1-0-60|2 Model Support changes in v1.0.60]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-06-05-2-safety-and-privacy-changes-in-v1-0-60|2 Safety and Privacy changes in v1.0.60]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-06-05-10-apps-and-integrations-changes-in-v1-0-60|10 Apps and Integrations changes in v1.0.60]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-06-05-2-context-window-changes-in-v1-0-60|2 Context Window changes in v1.0.60]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-06-05-2-mobile-and-desktop-changes-in-v1-0-60|2 Mobile and Desktop changes in v1.0.60]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-06-05-15-other-changes-in-v1-0-60|15 other changes in v1.0.60]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Editor Experience

- Earlier: 2026-06-03 · Google Antigravity · [[Changes/Google Antigravity/2026-06-03-antivirus-and-open-ide-fixes|Antivirus and Open IDE fixes]]
- Later: 2026-06-05 · OpenCode · [[Changes/OpenCode/2026-06-05-3-editor-experience-changes-in-v1-16-2|3 Editor Experience changes in v1.16.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-14 · Cursor · [[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3 Editor Experience changes in 0.0.37]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-06-05-55bf95&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-06-05-3-editor-experience-changes-in-v1-0-60.md%0ACard%20ID%3A%20github-copilot-cli-2026-06-05-55bf95%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.60%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->