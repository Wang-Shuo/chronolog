---
card_id: github-copilot-cli-2026-07-07-0d1959
date: '2026-07-07'
description: 'GitHub Copilot CLI · 2026-07-07 · Safety and Privacy: 8 changes in 1.0.69
  — Label built-in file edits with a (sandbox policy) badge instead of (sandboxed)…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2170
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8dcd1e38cfea3320e73ec513f0fa10ea599fe8bca5fe9ff2609902163f57d163
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-07-07-0d1959
  comparison: ''
  date: '2026-07-07'
  description: 'GitHub Copilot CLI — 1.0.69: 8 Safety and Privacy changes'
  evidence:
  - quote: Label built-in file edits with a (sandbox policy) badge instead of (sandboxed),
      since they follow the sandbox policy on a best-effort basis rather than running
      in the OS-level sandbox
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.69
  - quote: Let built-in file edits bypass the sandbox when you approve it
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.69
  - quote: web_fetch now follows the active sandbox network policy (denying outbound
      or local targets the policy blocks) and, when the host opts in via sandbox.allowBypass,
      lets you approve a one-time bypass from the fetch prompt
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.69
  - quote: Show descriptions for sandbox userPolicy settings in /settings
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.69
  - quote: Improve /sandbox add-path suggestions so they open only when you ask for
      them
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.69
  - quote: Skip the autopilot permission prompt when bypass mode is disabled by policy
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.69
  - quote: Remove inert sandbox host lists and the Clear policy on exit toggle
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.69
  - quote: Add file and folder completion to /sandbox path entries
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.69
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 8-safety-and-privacy-changes-in-v1-0-69
  source_release: github-copilot-cli-2026-07-07-v1-0-69-github-350582031-19558357
  source_type: github_releases
  theme: safety-privacy
  title: 8 Safety and Privacy changes in v1.0.69
  type: change
related_changes:
- '[[Changes/Claude Code/2026-07-06-fixed-remote-control-sessions-showing-the-wrong-permission-mode-in-the-mobile-an|Fixed
  /remote-control sessions showing the wrong permission mode in the mobile…]]'
- '[[Changes/OpenHands/2026-07-06-4-safety-and-privacy-changes-in-1-9-0|4 Safety and
  Privacy changes in 1.9.0]]'
- '[[Changes/Claude Code/2026-07-07-added-a-grey-badge-to-the-footer-when-in-manual-permission-mode-making-the-activ|Added
  a grey ⏸ badge to the footer when in manual permission mode, making the active…]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-07-07-v1-0-69-github-350582031-19558357|github-copilot-cli-2026-07-07-v1-0-69-github-350582031-19558357]]'
source_type: github_releases
theme: safety-privacy
title: 8 Safety and Privacy changes in v1.0.69
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Safety and Privacy changes in v1.0.69

**GitHub Copilot CLI** · 2026-07-07 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.69) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-07-07-v1-0-69-github-350582031-19558357|1.0.69]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Label built-in file edits with a (sandbox policy) badge instead of (sandboxed), since they follow the sandbox policy on a best-effort basis rather than running in the OS-level sandbox

> Let built-in file edits bypass the sandbox when you approve it

> web_fetch now follows the active sandbox network policy (denying outbound or local targets the policy blocks) and, when the host opts in via sandbox.allowBypass, lets you approve a one-time bypass from the fetch prompt

> Show descriptions for sandbox userPolicy settings in /settings

> Improve /sandbox add-path suggestions so they open only when you ask for them

> Skip the autopilot permission prompt when bypass mode is disabled by policy

> Remove inert sandbox host lists and the Clear policy on exit toggle

> Add file and folder completion to /sandbox path entries

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.69
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-07-07-7-developer-workflow-changes-in-v1-0-69|7 Developer Workflow changes in v1.0.69]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-07-07-6-model-support-changes-in-v1-0-69|6 Model Support changes in v1.0.69]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-07-07-warn-when-static-context-uses-most-of-the-prompt-budget-and-block-requests-when|Warn when static context uses most of the prompt budget and block requests…]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-07-07-6-account-and-access-changes-in-v1-0-69|6 Account and Access changes in v1.0.69]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-07-07-5-reliability-and-performance-changes-in-v1-0-69|5 Reliability and Performance changes in v1.0.69]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-07-07-3-mobile-and-desktop-changes-in-v1-0-69|3 Mobile and Desktop changes in v1.0.69]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-07-07-2-editor-experience-changes-in-v1-0-69|2 Editor Experience changes in v1.0.69]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-07-07-keep-session-resume-working-when-token-timing-includes-fractional-milliseconds|Keep session resume working when token timing includes fractional milliseconds]] · Projects and Workspaces
- [[Changes/GitHub Copilot CLI/2026-07-07-improve-chronicle-cost-tips-with-more-precise-evidence-backed-recommendations|Improve /chronicle cost-tips with more precise evidence-backed recommendations]] · Pricing Model
- [[Changes/GitHub Copilot CLI/2026-07-07-double-press-esc-now-interrupts-the-running-main-turn-flushing-queued-messages-o|Double-press Esc now interrupts the running main turn (flushing queued messages)…]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-07-07-5-interface-experience-changes-in-v1-0-69|5 Interface Experience changes in v1.0.69]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-07-07-7-apps-and-integrations-changes-in-v1-0-69|7 Apps and Integrations changes in v1.0.69]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-07-07-24-other-changes-in-v1-0-69|24 other changes in v1.0.69]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-07-07 · Claude Code · [[Changes/Claude Code/2026-07-07-added-a-grey-badge-to-the-footer-when-in-manual-permission-mode-making-the-activ|Added a grey ⏸ badge to the footer when in manual permission mode, making the active…]]
- Later: 2026-07-07 · Kimi Code · [[Changes/Kimi Code/2026-07-07-2-safety-and-privacy-changes-in-kimi-code-0-23-1|2 Safety and Privacy changes in Kimi Code 0.23.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-07-07-0d1959&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-07-07-8-safety-and-privacy-changes-in-v1-0-69.md%0ACard%20ID%3A%20github-copilot-cli-2026-07-07-0d1959%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.69%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->