---
card_id: codex-cli-2026-08-07-a7ed55
date: '2026-08-07'
description: 'Codex CLI · 2026-08-07 · Safety and Privacy: 9 changes in 0.147.0 —
  Remove the deprecated `codex exec --full-auto` flag; use `--sandbox workspace-write`…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2201
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 941ee08a578fd780907c7094e8a017d90c70f9ff7870a6195eecca5252f90fbd
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-08-07-a7ed55
  comparison: ''
  date: '2026-08-07'
  description: 'Codex CLI — 0.147.0: 9 Safety and Privacy changes'
  evidence:
  - quote: Remove the deprecated `codex exec --full-auto` flag; use `--sandbox workspace-write`
      instead. (#36054)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35661 Place host skills before permission instructions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35685 Load cloud-managed profiles for `codex sandbox` @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36121 Sandbox executor skill resource reads @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36138 Isolate apply-patch permission test variants @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36183 Use permission profiles throughout sandbox execution @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36207 Record normalized sandbox violation events @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36350 Require explicit sandbox permissions with shell justifications
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#37031 Apply permission profile updates to future turn environments @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 9-safety-and-privacy-changes-in-rust-v0-147-0
  source_release: codex-cli-2026-08-07-rust-v0-147-0-github-366471016-f6cfdee2
  source_type: github_releases
  theme: safety-privacy
  title: 9 Safety and Privacy changes in rust-v0.147.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-08-05-apply-safer-automatic-review-defaults-for-cyber-capable-models-and-explain-permi|Apply
  safer automatic-review defaults for cyber-capable models and explain…]]'
- '[[Changes/Claude Code/2026-08-06-3-safety-and-privacy-changes-in-v2-1-223|3 Safety
  and Privacy changes in v2.1.223]]'
- '[[Changes/Claude Code/2026-08-07-2-safety-and-privacy-changes-in-v2-1-224|2 Safety
  and Privacy changes in v2.1.224]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-08-07-rust-v0-147-0-github-366471016-f6cfdee2|codex-cli-2026-08-07-rust-v0-147-0-github-366471016-f6cfdee2]]'
source_type: github_releases
theme: safety-privacy
title: 9 Safety and Privacy changes in rust-v0.147.0
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Safety and Privacy changes in rust-v0.147.0

**Codex CLI** · 2026-08-07 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.147.0) · from [[Releases/Codex CLI/codex-cli-2026-08-07-rust-v0-147-0-github-366471016-f6cfdee2|0.147.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Remove the deprecated `codex exec --full-auto` flag; use `--sandbox workspace-write` instead. (#36054)

> #35661 Place host skills before permission instructions @copyberry

> #35685 Load cloud-managed profiles for `codex sandbox` @copyberry

> #36121 Sandbox executor skill resource reads @copyberry

> #36138 Isolate apply-patch permission test variants @copyberry

> #36183 Use permission profiles throughout sandbox execution @copyberry

> #36207 Record normalized sandbox violation events @copyberry

> #36350 Require explicit sandbox permissions with shell justifications @copyberry

> #37031 Apply permission profile updates to future turn environments @copyberry

Source: https://github.com/openai/codex/releases/tag/rust-v0.147.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-08-07-10-collaboration-changes-in-rust-v0-147-0|10 Collaboration changes in rust-v0.147.0]] · Collaboration
- [[Changes/Codex CLI/2026-08-07-8-account-and-access-changes-in-rust-v0-147-0|8 Account and Access changes in rust-v0.147.0]] · Account and Access
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
- [[Changes/Codex CLI/2026-08-07-10-context-window-changes-in-rust-v0-147-0|10 Context Window changes in rust-v0.147.0]] · Context Window
- [[Changes/Codex CLI/2026-08-07-6-interface-experience-changes-in-rust-v0-147-0|6 Interface Experience changes in rust-v0.147.0]] · Interface Experience
- [[Changes/Codex CLI/2026-08-07-196-other-changes-in-rust-v0-147-0|196 other changes in rust-v0.147.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-08-07 · Claude Code · [[Changes/Claude Code/2026-08-07-2-safety-and-privacy-changes-in-v2-1-224|2 Safety and Privacy changes in v2.1.224]]
- Later: 2026-08-07 · Google Antigravity · [[Changes/Google Antigravity/2026-08-07-steps-waiting-on-your-input-now-show-the-icon-for-the-tool-involved-including-in|Steps waiting on your input now show the icon for the tool involved, including…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-08-07-a7ed55&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-08-07-9-safety-and-privacy-changes-in-rust-v0-147-0.md%0ACard%20ID%3A%20codex-cli-2026-08-07-a7ed55%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.147.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->