---
card_id: github-copilot-cli-2026-08-27-c5c76c
date: '2026-08-27'
description: 'GitHub Copilot CLI · 2026-08-27 · Safety and Privacy: 5 changes in 1.0.81
  — Add Ctrl+E in /sandbox to open settings.json in your editor'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1229
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 98f9d78d0bdf091270b9e121aa4b71994800a88220b4a7dce3a1cc0e7f4761cc
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-08-27-c5c76c
  comparison: ''
  date: '2026-08-27'
  description: 'GitHub Copilot CLI — 1.0.81: 5 Safety and Privacy changes'
  evidence:
  - quote: Add Ctrl+E in /sandbox to open settings.json in your editor
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.81
  - quote: Turning allow-all off from an ACP client now reaches the permission engine
      whenever there is a runtime override or auto-approval to revoke, so the setting
      can no longer report success while permissions stay enabled (a baseline granted
      by --allow-all-\* launch flags is still deliberately left intact)
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.81
  - quote: '`x` is now the delete key everywhere: /sandbox config, /settings, /mcp,
      the sessions dialog and the diff comments summary move off `d`'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.81
  - quote: When --no-sandbox is ignored because enterprise policy could not be determined,
      the notice now says so, and no longer points at an administrator, instead of
      claiming a policy requires the sandbox. The unsupported-host warning says the
      same rather than contradicting it.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.81
  - quote: A session sandboxed by an enterprise managed policy now says so on the
      timeline, including when the policy arrives mid-session, instead of leaving
      the footer's sandbox chip as the only hint that commands are being restricted
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.81
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 5-safety-and-privacy-changes-in-v1-0-81
  source_release: github-copilot-cli-2026-08-27-v1-0-81-github-377993714-523d567a
  source_type: github_releases
  theme: safety-privacy
  title: 5 Safety and Privacy changes in v1.0.81
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-08-26-12-safety-and-privacy-changes-in-rust-v0-150-0|12
  Safety and Privacy changes in rust-v0.150.0]]'
- '[[Changes/Lovable/2026-08-26-log-out-everywhere|Log out everywhere]]'
- '[[Changes/Claude Code/2026-08-27-4-safety-and-privacy-changes-in-v2-1-248|4 Safety
  and Privacy changes in v2.1.248]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-08-27-v1-0-81-github-377993714-523d567a|github-copilot-cli-2026-08-27-v1-0-81-github-377993714-523d567a]]'
source_type: github_releases
theme: safety-privacy
title: 5 Safety and Privacy changes in v1.0.81
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Safety and Privacy changes in v1.0.81

**GitHub Copilot CLI** · 2026-08-27 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.81) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-08-27-v1-0-81-github-377993714-523d567a|1.0.81]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Add Ctrl+E in /sandbox to open settings.json in your editor

> Turning allow-all off from an ACP client now reaches the permission engine whenever there is a runtime override or auto-approval to revoke, so the setting can no longer report success while permissions stay enabled (a baseline granted by --allow-all-\* launch flags is still deliberately left intact)

> `x` is now the delete key everywhere: /sandbox config, /settings, /mcp, the sessions dialog and the diff comments summary move off `d`

> When --no-sandbox is ignored because enterprise policy could not be determined, the notice now says so, and no longer points at an administrator, instead of claiming a policy requires the sandbox. The unsupported-host warning says the same rather than contradicting it.

> A session sandboxed by an enterprise managed policy now says so on the timeline, including when the policy arrives mid-session, instead of leaving the footer's sandbox chip as the only hint that commands are being restricted

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.81
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-08-27-resume-large-sessions-faster-by-showing-recent-history-first-while-older-message|Resume large sessions faster by showing recent history first while older messages load]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-08-27-2-enterprise-and-administration-changes-in-v1-0-81|2 Enterprise and Administration changes in v1.0.81]] · Enterprise and Administration
- [[Changes/GitHub Copilot CLI/2026-08-27-sandboxed-builds-on-windows-create-their-scratch-caches-on-first-run-so-cargo-go|Sandboxed builds on Windows create their scratch caches on first run, so cargo, go…]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-08-27-5-developer-workflow-changes-in-v1-0-81|5 Developer Workflow changes in v1.0.81]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-08-27-3-interface-experience-changes-in-v1-0-81|3 Interface Experience changes in v1.0.81]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-08-27-12-apps-and-integrations-changes-in-v1-0-81|12 Apps and Integrations changes in v1.0.81]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-08-27-8-agent-mode-changes-in-v1-0-81|8 Agent Mode changes in v1.0.81]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-08-27-hooks-can-now-receive-the-current-opentelemetry-trace-context-and-emit-correlate|Hooks can now receive the current OpenTelemetry trace context and emit correlated spans]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-08-27-ship-mcp-2026-07-28-support-to-cli-sdk-ide-and-in-memory-clients|Ship MCP 2026-07-28 support to CLI, SDK, IDE, and in-memory clients]] · Memory and Personalization
- [[Changes/GitHub Copilot CLI/2026-08-27-add-copilot-app-to-open-the-github-copilot-app-in-the-current-directory|Add copilot app to open the GitHub Copilot app in the current directory]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-08-27-2-account-and-access-changes-in-v1-0-81|2 Account and Access changes in v1.0.81]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-08-27-use-x-to-remove-scheduled-every-and-after-prompts-in-schedule-manager|Use x to remove scheduled /every and /after prompts in Schedule Manager]] · Automation and Scheduling
- [[Changes/GitHub Copilot CLI/2026-08-27-canvas-windows-open-and-refresh-in-the-background-instead-of-stealing-focus-from|Canvas windows open and refresh in the background instead of stealing focus…]] · Files and Data
- [[Changes/GitHub Copilot CLI/2026-08-27-4-model-support-changes-in-v1-0-81|4 Model Support changes in v1.0.81]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-08-27-use-ctrl-space-to-toggle-voice-dictation|Use Ctrl+Space to toggle voice dictation]] · Voice and Audio
- [[Changes/GitHub Copilot CLI/2026-08-27-6-other-changes-in-v1-0-81|6 other changes in v1.0.81]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-08-27 · Claude Code · [[Changes/Claude Code/2026-08-27-4-safety-and-privacy-changes-in-v2-1-248|4 Safety and Privacy changes in v2.1.248]]
- Later: 2026-08-27 · Lovable · [[Changes/Lovable/2026-08-27-restrict-external-invites-to-verified-email-domains|Restrict external invites to verified email domains]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-08-27-c5c76c&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-08-27-5-safety-and-privacy-changes-in-v1-0-81.md%0ACard%20ID%3A%20github-copilot-cli-2026-08-27-c5c76c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.81%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->