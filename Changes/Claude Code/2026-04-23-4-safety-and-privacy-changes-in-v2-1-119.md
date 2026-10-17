---
card_id: claude-code-2026-04-23-d0e7d2
date: '2026-04-23'
description: 'Claude Code · 2026-04-23 · Safety and Privacy: 4 changes in v2.1.119
  — PowerShell tool commands can now be auto-approved in permission mode, matching
  Bash…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1103
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ec3a9cbbc179d21a7cc450f5ee0982faf6ed6d5fe9f2e9d76ad5a5329f82f580
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-04-23-d0e7d2
  comparison: ''
  date: '2026-04-23'
  description: 'Claude Code — v2.1.119: 4 Safety and Privacy changes'
  evidence:
  - quote: PowerShell tool commands can now be auto-approved in permission mode, matching
      Bash behavior
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.119
  - quote: 'Hooks: `PostToolUse` and `PostToolUseFailure` hook inputs now include
      `duration_ms` (tool execution time, excluding permission prompts and PreToolUse
      hooks)'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.119
  - quote: 'Security: `blockedMarketplaces` now correctly enforces `hostPattern` and
      `pathPattern` entries'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.119
  - quote: '[VSCode] Fixed voice dictation''s first recording producing nothing on
      macOS while the microphone permission prompt is showing'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.119
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 4-safety-and-privacy-changes-in-v2-1-119
  source_release: claude-code-2026-04-23-v2-1-119-github-312949780-573724e7
  source_type: github_releases
  theme: safety-privacy
  title: 4 Safety and Privacy changes in v2.1.119
  type: change
related_changes:
- '[[Changes/Claude Code/2026-04-18-fixed-a-crash-in-the-permission-dialog-when-an-agent-teams-teammate-requested-to|Fixed
  a crash in the permission dialog when an agent teams teammate requested tool…]]'
- '[[Changes/Claude Code/2026-04-20-security-sandbox-auto-allow-no-longer-bypasses-the-dangerous-path-safety-check-f|Security:
  sandbox auto-allow no longer bypasses the dangerous-path safety check…]]'
- '[[Changes/Claude Code/2026-04-23-fixed-mcp-step-up-authorization-silently-refreshing-instead-of-prompting-for-re|Fixed
  MCP step-up authorization silently refreshing instead of prompting…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-23-v2-1-119-github-312949780-573724e7|claude-code-2026-04-23-v2-1-119-github-312949780-573724e7]]'
source_type: github_releases
theme: safety-privacy
title: 4 Safety and Privacy changes in v2.1.119
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Safety and Privacy changes in v2.1.119

**Claude Code** · 2026-04-23 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.119) · from [[Releases/Claude Code/claude-code-2026-04-23-v2-1-119-github-312949780-573724e7|v2.1.119]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> PowerShell tool commands can now be auto-approved in permission mode, matching Bash behavior

> Hooks: `PostToolUse` and `PostToolUseFailure` hook inputs now include `duration_ms` (tool execution time, excluding permission prompts and PreToolUse hooks)

> Security: `blockedMarketplaces` now correctly enforces `hostPattern` and `pathPattern` entries

> [VSCode] Fixed voice dictation's first recording producing nothing on macOS while the microphone permission prompt is showing

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.119
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-04-23-3-interface-experience-changes-in-v2-1-119|3 Interface Experience changes in v2.1.119]] · Interface Experience
- [[Changes/Claude Code/2026-04-23-from-pr-now-accepts-gitlab-merge-request-bitbucket-pull-request-and-github-enter|--from-pr now accepts GitLab merge-request, Bitbucket pull-request, and GitHub…]] · Enterprise and Administration
- [[Changes/Claude Code/2026-04-23-3-apps-and-integrations-changes-in-v2-1-119|3 Apps and Integrations changes in v2.1.119]] · Apps and Integrations
- [[Changes/Claude Code/2026-04-23-config-settings-theme-editor-mode-verbose-etc-now-persist-to-claude-settings-jso|/config settings (theme, editor mode, verbose, etc.) now persist…]] · Editor Experience
- [[Changes/Claude Code/2026-04-23-3-developer-workflow-changes-in-v2-1-119|3 Developer Workflow changes in v2.1.119]] · Developer Workflow
- [[Changes/Claude Code/2026-04-23-2-agent-mode-changes-in-v2-1-119|2 Agent Mode changes in v2.1.119]] · Agent Mode
- [[Changes/Claude Code/2026-04-23-3-other-changes-in-v2-1-119|3 other changes in v2.1.119]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-04-23 · Claude Code · [[Changes/Claude Code/2026-04-23-fixed-mcp-step-up-authorization-silently-refreshing-instead-of-prompting-for-re|Fixed MCP step-up authorization silently refreshing instead of prompting…]]
- Later: 2026-04-30 · Cursor · [[Changes/Cursor/2026-04-30-cursor-security-review-is-now-in-beta-on-teams-and-enterprise-plans-you-can-run|Cursor Security Review is now in beta on Teams and Enterprise plans]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-04-23-d0e7d2&body=Card%3A%20Changes%2FClaude%20Code%2F2026-04-23-4-safety-and-privacy-changes-in-v2-1-119.md%0ACard%20ID%3A%20claude-code-2026-04-23-d0e7d2%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.119%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->