---
card_id: codex-cli-2026-08-07-133439
date: '2026-08-07'
description: 'Codex CLI · 2026-08-07 · Account and Access: 8 changes in 0.147.0 —
  Require explicit trust for unfamiliar local projects and enforce managed authentication…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1226
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 0d566e1c61f6f74a09802a7a4b9be8ceea2ab141285ce08ac546b932c4c69b88
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-08-07-133439
  comparison: ''
  date: '2026-08-07'
  description: 'Codex CLI — 0.147.0: 8 Account and Access changes'
  evidence:
  - quote: 'Require explicit trust for unfamiliar local projects and enforce managed
      authentication restrictions before credentials are used. (#36960, #37132)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35671 Route curated plugins by authentication mode @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35806 Route MCP OAuth through configured HTTP clients @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35814 Use configured HTTP clients for all MCP OAuth requests @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36045 Distinguish unknown MCP authentication status @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36310 Isolate MCP OAuth credentials by environment @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36635 Expose onboarding hints in login completion notifications @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#37132 Enforce managed authentication requirements locally @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 8-account-and-access-changes-in-rust-v0-147-0
  source_release: codex-cli-2026-08-07-rust-v0-147-0-github-366471016-f6cfdee2
  source_type: github_releases
  theme: account-access
  title: 8 Account and Access changes in rust-v0.147.0
  type: change
related_changes:
- '[[Changes/Windsurf/2026-08-01-devin-desktop-for-windows-loads-root-and-intermediate-certificates-from-the-wind|Devin
  Desktop for Windows loads root and intermediate certificates from the Windows…]]'
- '[[Changes/GitHub Copilot CLI/2026-08-03-2-account-and-access-changes-in-v1-0-78|2
  Account and Access changes in v1.0.78]]'
- '[[Changes/Claude Code/2026-08-07-changed-managed-settings-the-approval-prompt-no-longer-re-appears-after-re-login|Changed
  managed settings]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-08-07-rust-v0-147-0-github-366471016-f6cfdee2|codex-cli-2026-08-07-rust-v0-147-0-github-366471016-f6cfdee2]]'
source_type: github_releases
theme: account-access
title: 8 Account and Access changes in rust-v0.147.0
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Account and Access changes in rust-v0.147.0

**Codex CLI** · 2026-08-07 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.147.0) · from [[Releases/Codex CLI/codex-cli-2026-08-07-rust-v0-147-0-github-366471016-f6cfdee2|0.147.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Require explicit trust for unfamiliar local projects and enforce managed authentication restrictions before credentials are used. (#36960, #37132)

> #35671 Route curated plugins by authentication mode @copyberry

> #35806 Route MCP OAuth through configured HTTP clients @copyberry

> #35814 Use configured HTTP clients for all MCP OAuth requests @copyberry

> #36045 Distinguish unknown MCP authentication status @copyberry

> #36310 Isolate MCP OAuth credentials by environment @copyberry

> #36635 Expose onboarding hints in login completion notifications @copyberry

> #37132 Enforce managed authentication requirements locally @copyberry

Source: https://github.com/openai/codex/releases/tag/rust-v0.147.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-08-07-10-collaboration-changes-in-rust-v0-147-0|10 Collaboration changes in rust-v0.147.0]] · Collaboration
- [[Changes/Codex CLI/2026-08-07-36140-wait-for-memory-consolidation-shutdown-before-finishing-jobs-copyberry|♯36140 Wait for memory consolidation shutdown before finishing jobs @copyberry]] · Memory and Personalization
- [[Changes/Codex CLI/2026-08-07-65-apps-and-integrations-changes-in-rust-v0-147-0|65 Apps and Integrations changes in rust-v0.147.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-08-07-15-developer-workflow-changes-in-rust-v0-147-0|15 Developer Workflow changes in rust-v0.147.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-08-07-36043-document-the-responses-api-proxy-reqwest-exception-copyberry|♯36043 Document the Responses API proxy reqwest exception @copyberry]] · Files and Data
- [[Changes/Codex CLI/2026-08-07-36228-support-enterprise-automation-account-plans-copyberry|♯36228 Support Enterprise automation account plans @copyberry]] · Automation and Scheduling
- [[Changes/Codex CLI/2026-08-07-3-search-and-browsing-changes-in-rust-v0-147-0|3 Search and Browsing changes in rust-v0.147.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-08-07-17-agent-mode-changes-in-rust-v0-147-0|17 Agent Mode changes in rust-v0.147.0]] · Agent Mode
- [[Changes/Codex CLI/2026-08-07-13-model-support-changes-in-rust-v0-147-0|13 Model Support changes in rust-v0.147.0]] · Model Support
- [[Changes/Codex CLI/2026-08-07-36807-extract-audio-preparation-into-a-utility-crate-copyberry|♯36807 Extract audio preparation into a utility crate @copyberry]] · Voice and Audio
- [[Changes/Codex CLI/2026-08-07-4-mobile-and-desktop-changes-in-rust-v0-147-0|4 Mobile and Desktop changes in rust-v0.147.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-08-07-9-safety-and-privacy-changes-in-rust-v0-147-0|9 Safety and Privacy changes in rust-v0.147.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-08-07-10-context-window-changes-in-rust-v0-147-0|10 Context Window changes in rust-v0.147.0]] · Context Window
- [[Changes/Codex CLI/2026-08-07-6-interface-experience-changes-in-rust-v0-147-0|6 Interface Experience changes in rust-v0.147.0]] · Interface Experience
- [[Changes/Codex CLI/2026-08-07-196-other-changes-in-rust-v0-147-0|196 other changes in rust-v0.147.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-08-07 · Claude Code · [[Changes/Claude Code/2026-08-07-changed-managed-settings-the-approval-prompt-no-longer-re-appears-after-re-login|Changed managed settings]]
- Later: 2026-08-09 · Cline · [[Changes/Cline/2026-08-09-2-account-and-access-changes-in-v4-1-7|2 Account and Access changes in v4.1.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-08-07-133439&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-08-07-8-account-and-access-changes-in-rust-v0-147-0.md%0ACard%20ID%3A%20codex-cli-2026-08-07-133439%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.147.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->