---
card_id: claude-code-2026-03-17-9ae10a
date: '2026-03-17'
description: 'Claude Code · 2026-03-17 · Safety and Privacy: 3 changes in v2.1.77
  — Added `allowRead` sandbox filesystem setting to re-allow read access within `denyRead`…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1066
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: bc131bc1f9ccc4e89317580e831658fa80dc93c216be1bfe47a640181dd188a9
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-03-17-9ae10a
  comparison: ''
  date: '2026-03-17'
  description: 'Claude Code — v2.1.77: 3 Safety and Privacy changes'
  evidence:
  - quote: Added `allowRead` sandbox filesystem setting to re-allow read access within
      `denyRead` regions
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.77
  - quote: Fixed "Always Allow" on compound bash commands (e.g. `cd src && npm test`)
      saving a single rule for the full string instead of per-subcommand, leading
      to dead rules and repeated permission prompts
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.77
  - quote: Fixed PreToolUse hooks returning `"allow"` bypassing `deny` permission
      rules, including enterprise managed settings
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.77
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-safety-and-privacy-changes-in-v2-1-77
  source_release: claude-code-2026-03-17-v2-1-77-github-297726061-caf6c30c
  source_type: github_releases
  theme: safety-privacy
  title: 3 Safety and Privacy changes in v2.1.77
  type: change
related_changes:
- '[[Changes/Claude Code/2026-03-12-fixed-voice-mode-silently-failing-on-the-macos-native-binary-for-users-whose-ter|Fixed
  voice mode silently failing on the macOS native binary for users whose…]]'
- '[[Changes/Claude Code/2026-03-14-3-safety-and-privacy-changes-in-v2-1-76|3 Safety
  and Privacy changes in v2.1.76]]'
- '[[Changes/Claude Code/2026-03-17-2-safety-and-privacy-changes-in-v2-1-78|2 Safety
  and Privacy changes in v2.1.78]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-17-v2-1-77-github-297726061-caf6c30c|claude-code-2026-03-17-v2-1-77-github-297726061-caf6c30c]]'
source_type: github_releases
theme: safety-privacy
title: 3 Safety and Privacy changes in v2.1.77
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Safety and Privacy changes in v2.1.77

**Claude Code** · 2026-03-17 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.77) · from [[Releases/Claude Code/claude-code-2026-03-17-v2-1-77-github-297726061-caf6c30c|v2.1.77]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `allowRead` sandbox filesystem setting to re-allow read access within `denyRead` regions

> Fixed "Always Allow" on compound bash commands (e.g. `cd src && npm test`) saving a single rule for the full string instead of per-subcommand, leading to dead rules and repeated permission prompts

> Fixed PreToolUse hooks returning `"allow"` bypassing `deny` permission rules, including enterprise managed settings

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.77
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-03-17-show-a-notice-when-apikeyhelper-takes-longer-than-10s-preventing-it-from-blockin|Show a notice when apiKeyHelper takes longer than 10s, preventing it from blocking…]] · Automation and Scheduling
- [[Changes/Claude Code/2026-03-17-vscode-when-option-click-doesn-t-trigger-native-selection-on-macos-the-footer-no|VSCode When option+click doesn't trigger native selection on macOS, the footer now…]] · Mobile and Desktop
- [[Changes/Claude Code/2026-03-17-vscode-improved-plan-preview-tab-titles-to-use-the-plan-s-heading-instead-of-cla|VSCode Improved plan preview tab titles to use the plan's heading instead…]] · Editor Experience
- [[Changes/Claude Code/2026-03-17-copy-now-accepts-an-optional-index-copy-n-copies-the-nth-latest-assistant-respon|/copy now accepts an optional index: /copy N copies the Nth-latest assistant response]] · Interface Experience
- [[Changes/Claude Code/2026-03-17-2-apps-and-integrations-changes-in-v2-1-77|2 Apps and Integrations changes in v2.1.77]] · Apps and Integrations
- [[Changes/Claude Code/2026-03-17-background-bash-tasks-are-now-killed-if-output-exceeds-5gb-preventing-runaway-pr|Background bash tasks are now killed if output exceeds 5GB, preventing runaway…]] · Developer Workflow
- [[Changes/Claude Code/2026-03-17-2-reliability-and-performance-changes-in-v2-1-77|2 Reliability and Performance changes in v2.1.77]] · Reliability and Performance
- [[Changes/Claude Code/2026-03-17-2-agent-mode-changes-in-v2-1-77|2 Agent Mode changes in v2.1.77]] · Agent Mode
- [[Changes/Claude Code/2026-03-17-increased-default-maximum-output-token-limits-for-claude-opus-4-6-to-64k-tokens|Increased default maximum output token limits for Claude Opus 4.6 to 64k tokens…]] · Model Support
- [[Changes/Claude Code/2026-03-17-3-other-changes-in-v2-1-77|3 other changes in v2.1.77]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-03-17 · Claude Code · [[Changes/Claude Code/2026-03-17-2-safety-and-privacy-changes-in-v2-1-78|2 Safety and Privacy changes in v2.1.78]]
- Later: 2026-03-18 · Claude Code · [[Changes/Claude Code/2026-03-18-fixed-custom-status-line-showing-nothing-when-workspace-trust-is-blocking-it|Fixed custom status line showing nothing when workspace trust is blocking it]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-03-17-9ae10a&body=Card%3A%20Changes%2FClaude%20Code%2F2026-03-17-3-safety-and-privacy-changes-in-v2-1-77.md%0ACard%20ID%3A%20claude-code-2026-03-17-9ae10a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.77%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->