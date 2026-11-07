---
card_id: github-copilot-cli-2026-08-27-25343a
date: '2026-08-27'
description: 'GitHub Copilot CLI · 2026-08-27 · Enterprise and Administration: 2 changes
  in 1.0.81 — Signing out of an account now clears its cached enterprise managed…'
diffusion:
  first_in_tracked: '[[Changes/Notion/2020-01-14-export-members-as-csv-for-enterprise-plans-quickly-download-a-list-of-the-people|Export
    members as CSV (for Enterprise Plans) Quickly download a list of the people…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2417
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: enterprise-admin
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2033258b7672f1a161ed408fe7973986c0bab8a53303cecf0587d07decf29529
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-08-27-25343a
  comparison: ''
  date: '2026-08-27'
  description: 'GitHub Copilot CLI — 1.0.81: 2 Enterprise and Administration changes'
  evidence:
  - quote: Signing out of an account now clears its cached enterprise managed settings,
      so signing back in generally re-fetches the policy rather than re-applying the
      one cached before sign-out
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.81
  - quote: An enterprise managed-settings policy is no longer rejected when `permissions.disableBypassPermissionsMode`
      carries an unrecognized value; it is now logged and enforced as `disable`.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.81
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 2-enterprise-and-administration-changes-in-v1-0-81
  source_release: github-copilot-cli-2026-08-27-v1-0-81-github-377993714-523d567a
  source_type: github_releases
  theme: enterprise-admin
  title: 2 Enterprise and Administration changes in v1.0.81
  type: change
related_changes:
- '[[Changes/Open WebUI/2026-08-25-4-enterprise-and-administration-changes-in-v0-11-1|4
  Enterprise and Administration changes in v0.11.1]]'
- '[[Changes/Lovable/2026-08-26-record-who-is-behind-each-commit-lovable-pushes|Record
  who is behind each commit Lovable pushes]]'
- '[[Changes/Lovable/2026-08-26-workspace-build-secrets-appear-in-your-project-s-secrets-list|Workspace
  build secrets appear in your project''s secrets list]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-08-27-v1-0-81-github-377993714-523d567a|github-copilot-cli-2026-08-27-v1-0-81-github-377993714-523d567a]]'
source_type: github_releases
theme: enterprise-admin
title: 2 Enterprise and Administration changes in v1.0.81
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Enterprise and Administration changes in v1.0.81

**GitHub Copilot CLI** · 2026-08-27 · [[Themes/enterprise-admin|Enterprise and Administration]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.81) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-08-27-v1-0-81-github-377993714-523d567a|1.0.81]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Signing out of an account now clears its cached enterprise managed settings, so signing back in generally re-fetches the policy rather than re-applying the one cached before sign-out

> An enterprise managed-settings policy is no longer rejected when `permissions.disableBypassPermissionsMode` carries an unrecognized value; it is now logged and enforced as `disable`.

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.81
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-08-27-resume-large-sessions-faster-by-showing-recent-history-first-while-older-message|Resume large sessions faster by showing recent history first while older messages load]] · Reliability and Performance
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
- [[Changes/GitHub Copilot CLI/2026-08-27-5-safety-and-privacy-changes-in-v1-0-81|5 Safety and Privacy changes in v1.0.81]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-08-27-use-ctrl-space-to-toggle-voice-dictation|Use Ctrl+Space to toggle voice dictation]] · Voice and Audio
- [[Changes/GitHub Copilot CLI/2026-08-27-6-other-changes-in-v1-0-81|6 other changes in v1.0.81]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Enterprise and Administration

- Earlier: 2026-08-26 · Lovable · [[Changes/Lovable/2026-08-26-workspace-build-secrets-appear-in-your-project-s-secrets-list|Workspace build secrets appear in your project's secrets list]]
- Later: 2026-09-01 · Lovable · [[Changes/Lovable/2026-09-01-find-buy-and-connect-a-domain-from-chat|Find, buy, and connect a domain from chat]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-01-14 · Notion · [[Changes/Notion/2020-01-14-export-members-as-csv-for-enterprise-plans-quickly-download-a-list-of-the-people|Export members as CSV (for Enterprise Plans) Quickly download a list of the people…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-08-27-25343a&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-08-27-2-enterprise-and-administration-changes-in-v1-0-81.md%0ACard%20ID%3A%20github-copilot-cli-2026-08-27-25343a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.81%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->