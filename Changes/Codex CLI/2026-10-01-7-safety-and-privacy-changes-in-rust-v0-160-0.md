---
card_id: codex-cli-2026-10-01-b4f5df
date: '2026-10-01'
description: 'Codex CLI · 2026-10-01 · Safety and Privacy: 7 changes in 0.160.0 —
  Fixed Windows sandbox PowerShell fallbacks and long-path permission repairs, and
  suppressed…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2256
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: daf521ea1084cd5d916286af21a5e677d51f44f3200d3896b4d78ad80cecec3c
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-10-01-b4f5df
  comparison: ''
  date: '2026-10-01'
  description: 'Codex CLI — 0.160.0: 7 Safety and Privacy changes'
  evidence:
  - quote: 'Fixed Windows sandbox PowerShell fallbacks and long-path permission repairs,
      and suppressed unwanted console windows from background helpers. (#49019, #49058,
      #49098, #49164, #49386)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.160.0
  - quote: '#49019 Use a compatible PowerShell fallback for the Windows MXC sandbox
      @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.160.0
  - quote: '#49028 Use the numeric ioctl value in the macOS sandbox policy @aionescu-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.160.0
  - quote: '#49058 Fix Windows sandbox ACL repair for long runtime paths @darius-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.160.0
  - quote: '#49067 Keep configuration values out of Windows sandbox policy events
      @zm-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.160.0
  - quote: '#49098 Resolve Windows sandbox PowerShell fallbacks on the exec server
      @zm-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.160.0
  - quote: '#49763 [0.160] Backport maintenance-line catalog and security reminder
      updates @andrewgu-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.160.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 7-safety-and-privacy-changes-in-rust-v0-160-0
  source_release: codex-cli-2026-10-01-rust-v0-160-0-github-401312540-620e0269
  source_type: github_releases
  theme: safety-privacy
  title: 7 Safety and Privacy changes in rust-v0.160.0
  type: change
related_changes:
- '[[Changes/Lovable/2026-09-30-rotate-your-cloud-database-password-from-chat|Rotate
  your Cloud database password from chat]]'
- '[[Changes/OpenClaw/2026-09-30-21-safety-and-privacy-changes-in-v2026-9-7|21 Safety
  and Privacy changes in v2026.9.7]]'
- '[[Changes/Claude Code/2026-10-01-6-safety-and-privacy-changes-in-v2-1-287|6 Safety
  and Privacy changes in v2.1.287]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-10-01-rust-v0-160-0-github-401312540-620e0269|codex-cli-2026-10-01-rust-v0-160-0-github-401312540-620e0269]]'
source_type: github_releases
theme: safety-privacy
title: 7 Safety and Privacy changes in rust-v0.160.0
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Safety and Privacy changes in rust-v0.160.0

**Codex CLI** · 2026-10-01 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.160.0) · from [[Releases/Codex CLI/codex-cli-2026-10-01-rust-v0-160-0-github-401312540-620e0269|0.160.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Fixed Windows sandbox PowerShell fallbacks and long-path permission repairs, and suppressed unwanted console windows from background helpers. (#49019, #49058, #49098, #49164, #49386)

> #49019 Use a compatible PowerShell fallback for the Windows MXC sandbox @iceweasel-oai

> #49028 Use the numeric ioctl value in the macOS sandbox policy @aionescu-oai

> #49058 Fix Windows sandbox ACL repair for long runtime paths @darius-oai

> #49067 Keep configuration values out of Windows sandbox policy events @zm-oai

> #49098 Resolve Windows sandbox PowerShell fallbacks on the exec server @zm-oai

> #49763 [0.160] Backport maintenance-line catalog and security reminder updates @andrewgu-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.160.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-10-01-2-interface-experience-changes-in-rust-v0-160-0|2 Interface Experience changes in rust-v0.160.0]] · Interface Experience
- [[Changes/Codex CLI/2026-10-01-browse-older-tasks-in-the-agent-command-center-with-a-keyboard-accessible-show-m|Browse older tasks in the agent command center with a keyboard-accessible…]] · Search and Browsing
- [[Changes/Codex CLI/2026-10-01-49130-move-content-filter-guidance-into-the-shared-responses-retry-handler-won-o|♯49130 Move content-filter guidance into the shared Responses retry handler @won-openai]] · Collaboration
- [[Changes/Codex CLI/2026-10-01-49079-update-and-centralize-tui-subscription-labels-etraut-openai|♯49079 Update and centralize TUI subscription labels @etraut-openai]] · Pricing Model
- [[Changes/Codex CLI/2026-10-01-4-apps-and-integrations-changes-in-rust-v0-160-0|4 Apps and Integrations changes in rust-v0.160.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-10-01-5-model-support-changes-in-rust-v0-160-0|5 Model Support changes in rust-v0.160.0]] · Model Support
- [[Changes/Codex CLI/2026-10-01-49000-isolate-the-memory-startup-metadata-test-from-git-enrichment-jif-oai|♯49000 Isolate the memory startup metadata test from Git enrichment @jif-oai]] · Memory and Personalization
- [[Changes/Codex CLI/2026-10-01-6-agent-mode-changes-in-rust-v0-160-0|6 Agent Mode changes in rust-v0.160.0]] · Agent Mode
- [[Changes/Codex CLI/2026-10-01-2-account-and-access-changes-in-rust-v0-160-0|2 Account and Access changes in rust-v0.160.0]] · Account and Access
- [[Changes/Codex CLI/2026-10-01-49082-skip-remote-git-discovery-for-guardian-diff-paths-jif-oai|♯49082 Skip remote Git discovery for Guardian diff paths @jif-oai]] · Editor Experience
- [[Changes/Codex CLI/2026-10-01-49093-simplify-startup-promotions-to-platform-specific-desktop-app-tips-etraut-o|♯49093 Simplify startup promotions to platform-specific desktop app tips @etraut-openai]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-10-01-3-context-window-changes-in-rust-v0-160-0|3 Context Window changes in rust-v0.160.0]] · Context Window
- [[Changes/Codex CLI/2026-10-01-49073-surface-realtime-voice-catalog-failures-in-the-tui-etraut-openai|♯49073 Surface realtime voice catalog failures in the TUI @etraut-openai]] · Voice and Audio
- [[Changes/Codex CLI/2026-10-01-2-developer-workflow-changes-in-rust-v0-160-0|2 Developer Workflow changes in rust-v0.160.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-10-01-29-other-changes-in-rust-v0-160-0|29 other changes in rust-v0.160.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-10-01 · Claude Code · [[Changes/Claude Code/2026-10-01-6-safety-and-privacy-changes-in-v2-1-287|6 Safety and Privacy changes in v2.1.287]]
- Later: 2026-10-01 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-10-01-2-safety-and-privacy-changes-in-v1-0-91|2 Safety and Privacy changes in v1.0.91]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-10-01-b4f5df&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-10-01-7-safety-and-privacy-changes-in-rust-v0-160-0.md%0ACard%20ID%3A%20codex-cli-2026-10-01-b4f5df%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.160.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->