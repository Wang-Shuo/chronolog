---
card_id: claude-code-2026-03-05-715bbe
date: '2026-03-05'
description: 'Claude Code · 2026-03-05 · Safety and Privacy: 5 changes in v2.1.69
  — Added `sandbox.enableWeakerNetworkIsolation` setting (macOS only) to allow Go
  programs…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1054
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 0d020f430a988af1187e3b39979eae9555c232bbe02ca49cd5109ea00b09f563
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-03-05-715bbe
  comparison: ''
  date: '2026-03-05'
  description: 'Claude Code — v2.1.69: 5 Safety and Privacy changes'
  evidence:
  - quote: Added `sandbox.enableWeakerNetworkIsolation` setting (macOS only) to allow
      Go programs like `gh`, `gcloud`, and `terraform` to verify TLS certificates
      when using a custom MITM proxy with `httpProxyPort`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.69
  - quote: Fixed a security issue where nested skill discovery could load skills from
      gitignored directories like `node_modules`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.69
  - quote: Fixed interactive tools (e.g., `AskUserQuestion`) being silently auto-allowed
      when listed in a skill's allowed-tools, bypassing the permission prompt and
      running with empty answers
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.69
  - quote: Fixed `cd <outside-dir> && <cmd>` permission prompt to surface the chained
      command instead of only showing "Yes, allow reading from <dir>/"
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.69
  - quote: '[VSCode] The permission mode picker now respects `permissions.disableBypassPermissionsMode`
      from your effective Claude Code settings (including managed/policy settings)
      — when set to `disable`, bypass permissions mode is hidden from the picker'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.69
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 5-safety-and-privacy-changes-in-v2-1-69
  source_release: claude-code-2026-03-05-v2-1-69-github-293216328-162b2e44
  source_type: github_releases
  theme: safety-privacy
  title: 5 Safety and Privacy changes in v2.1.69
  type: change
related_changes:
- '[[Changes/Claude Code/2026-02-24-3-safety-and-privacy-changes-in-v2-1-51|3 Safety
  and Privacy changes in v2.1.51]]'
- '[[Changes/Claude Code/2026-02-28-fixed-listener-leak-in-interactive-permission-handler-during-auto-approvals|Fixed
  listener leak in interactive permission handler during auto-approvals]]'
- '[[Changes/Cursor/2026-03-03-fixed-team-permission-and-access-control-inconsistencies-across-organization-set|Fixed
  team permission and access control inconsistencies across organization setups]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-05-v2-1-69-github-293216328-162b2e44|claude-code-2026-03-05-v2-1-69-github-293216328-162b2e44]]'
source_type: github_releases
theme: safety-privacy
title: 5 Safety and Privacy changes in v2.1.69
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Safety and Privacy changes in v2.1.69

**Claude Code** · 2026-03-05 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.69) · from [[Releases/Claude Code/claude-code-2026-03-05-v2-1-69-github-293216328-162b2e44|v2.1.69]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `sandbox.enableWeakerNetworkIsolation` setting (macOS only) to allow Go programs like `gh`, `gcloud`, and `terraform` to verify TLS certificates when using a custom MITM proxy with `httpProxyPort`

> Fixed a security issue where nested skill discovery could load skills from gitignored directories like `node_modules`

> Fixed interactive tools (e.g., `AskUserQuestion`) being silently auto-allowed when listed in a skill's allowed-tools, bypassing the permission prompt and running with empty answers

> Fixed `cd <outside-dir> && <cmd>` permission prompt to surface the chained command instead of only showing "Yes, allow reading from \<dir>/"

> [VSCode] The permission mode picker now respects `permissions.disableBypassPermissionsMode` from your effective Claude Code settings (including managed/policy settings) — when set to `disable`, bypass permissions mode is hidden from the picker

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.69
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-03-05-2-agent-mode-changes-in-v2-1-69|2 Agent Mode changes in v2.1.69]] · Agent Mode
- [[Changes/Claude Code/2026-03-05-changed-sonnet-4-5-users-on-pro-max-team-premium-to-be-automatically-migrated-to|Changed Sonnet 4.5 users on Pro/Max/Team Premium to be automatically migrated…]] · Model Support
- [[Changes/Claude Code/2026-03-05-9-reliability-and-performance-changes-in-v2-1-69|9 Reliability and Performance changes in v2.1.69]] · Reliability and Performance
- [[Changes/Claude Code/2026-03-05-added-reload-plugins-command-to-activate-pending-plugin-changes-without-restarti|Added /reload-plugins command to activate pending plugin changes without restarting]] · Apps and Integrations
- [[Changes/Claude Code/2026-03-05-3-interface-experience-changes-in-v2-1-69|3 Interface Experience changes in v2.1.69]] · Interface Experience
- [[Changes/Claude Code/2026-03-05-improved-macos-startup-for-claude-ai-enterprise-team-users-by-skipping-an-unnece|Improved macOS startup for Claude.ai enterprise/team users by skipping…]] · Enterprise and Administration
- [[Changes/Claude Code/2026-03-05-3-voice-and-audio-changes-in-v2-1-69|3 Voice and Audio changes in v2.1.69]] · Voice and Audio
- [[Changes/Claude Code/2026-03-05-7-apps-and-integrations-changes-in-v2-1-69|7 Apps and Integrations changes in v2.1.69]] · Apps and Integrations
- [[Changes/Claude Code/2026-03-05-2-mobile-and-desktop-changes-in-v2-1-69|2 Mobile and Desktop changes in v2.1.69]] · Mobile and Desktop
- [[Changes/Claude Code/2026-03-05-6-developer-workflow-changes-in-v2-1-69|6 Developer Workflow changes in v2.1.69]] · Developer Workflow
- [[Changes/Claude Code/2026-03-05-2-account-and-access-changes-in-v2-1-69|2 Account and Access changes in v2.1.69]] · Account and Access
- [[Changes/Claude Code/2026-03-05-3-context-window-changes-in-v2-1-69|3 Context Window changes in v2.1.69]] · Context Window
- [[Changes/Claude Code/2026-03-05-3-other-changes-in-v2-1-69|3 other changes in v2.1.69]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-03-03 · Cursor · [[Changes/Cursor/2026-03-03-fixed-team-permission-and-access-control-inconsistencies-across-organization-set|Fixed team permission and access control inconsistencies across organization setups]]
- Later: 2026-03-05 · Cursor · [[Changes/Cursor/2026-03-05-when-invoked-the-agent-spins-up-a-cloud-sandbox-and-follows-your-instructions-us|When invoked, the agent spins up a cloud sandbox and follows your instructions using…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-03-05-715bbe&body=Card%3A%20Changes%2FClaude%20Code%2F2026-03-05-5-safety-and-privacy-changes-in-v2-1-69.md%0ACard%20ID%3A%20claude-code-2026-03-05-715bbe%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.69%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->