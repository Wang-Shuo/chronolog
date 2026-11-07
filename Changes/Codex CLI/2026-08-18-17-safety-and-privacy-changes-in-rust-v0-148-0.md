---
card_id: codex-cli-2026-08-18-95d16c
date: '2026-08-18'
description: 'Codex CLI · 2026-08-18 · Safety and Privacy: 17 changes in 0.148.0 —
  Sandbox restrictions now fail closed for denied or unreadable paths across Linux
  and…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2212
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 755aba1bd3877e969e636524dd84b08903e4b947b939138d2782a1a2a128fe5a
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-08-18-95d16c
  comparison: ''
  date: '2026-08-18'
  description: 'Codex CLI — 0.148.0: 17 Safety and Privacy changes'
  evidence:
  - quote: 'Sandbox restrictions now fail closed for denied or unreadable paths across
      Linux and Windows. (#37875, #38026, #38416, #38660)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37507 Include sandbox mode in response metadata @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37875 Honor the configured Windows sandbox level for managed networking
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37882 Read safety buffering from response metadata @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38043 Sandbox remote apply_patch operations @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38061 Preserve proxy settings for Windows sandbox debug sessions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38064 Grant Windows sandbox access to the Codex app root @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38080 Allow nested Git repositories in the Windows sandbox @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38306 Protect inline visualization viewers from sandbox writes @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38363 Persist security risk scores in rollout history @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38450 Embed the Windows sandbox setup manifest in Bazel builds @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38561 Restrict filesystem helper sandbox access @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38567 Store security risk scores as a snapshot @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38651 Move permission profile snapshots into the protocol @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38660 Enforce managed deny-read rules in the Windows sandbox @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38673 Honor per-environment permission profiles @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38701 Route permission requests through shared Guardian approvals @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 17-safety-and-privacy-changes-in-rust-v0-148-0
  source_release: codex-cli-2026-08-18-rust-v0-148-0-github-372686337-4265c0ae
  source_type: github_releases
  theme: safety-privacy
  title: 17 Safety and Privacy changes in rust-v0.148.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-08-17-8-safety-and-privacy-changes-in-v2-1-234|8 Safety
  and Privacy changes in v2.1.234]]'
- '[[Changes/Lovable/2026-08-17-workspace-insights-is-now-security-insights|Workspace
  insights is now Security insights]]'
- '[[Changes/Claude Code/2026-08-18-2-safety-and-privacy-changes-in-v2-1-235|2 Safety
  and Privacy changes in v2.1.235]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-08-18-rust-v0-148-0-github-372686337-4265c0ae|codex-cli-2026-08-18-rust-v0-148-0-github-372686337-4265c0ae]]'
source_type: github_releases
theme: safety-privacy
title: 17 Safety and Privacy changes in rust-v0.148.0
type: change
---

<!-- chronolog:begin region="header" -->
# 17 Safety and Privacy changes in rust-v0.148.0

**Codex CLI** · 2026-08-18 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.148.0) · from [[Releases/Codex CLI/codex-cli-2026-08-18-rust-v0-148-0-github-372686337-4265c0ae|0.148.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Sandbox restrictions now fail closed for denied or unreadable paths across Linux and Windows. (#37875, #38026, #38416, #38660)

> #37507 Include sandbox mode in response metadata @copyberry

> #37875 Honor the configured Windows sandbox level for managed networking @copyberry

> #37882 Read safety buffering from response metadata @copyberry

> #38043 Sandbox remote apply_patch operations @copyberry

> #38061 Preserve proxy settings for Windows sandbox debug sessions @copyberry

> #38064 Grant Windows sandbox access to the Codex app root @copyberry

> #38080 Allow nested Git repositories in the Windows sandbox @copyberry

> #38306 Protect inline visualization viewers from sandbox writes @copyberry

> #38363 Persist security risk scores in rollout history @copyberry

> #38450 Embed the Windows sandbox setup manifest in Bazel builds @copyberry

> #38561 Restrict filesystem helper sandbox access @copyberry

> #38567 Store security risk scores as a snapshot @copyberry

> #38651 Move permission profile snapshots into the protocol @copyberry

> #38660 Enforce managed deny-read rules in the Windows sandbox @copyberry

> #38673 Honor per-environment permission profiles @copyberry

> #38701 Route permission requests through shared Guardian approvals @copyberry

Source: https://github.com/openai/codex/releases/tag/rust-v0.148.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-08-18-57-apps-and-integrations-changes-in-rust-v0-148-0|57 Apps and Integrations changes in rust-v0.148.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-08-18-13-interface-experience-changes-in-rust-v0-148-0|13 Interface Experience changes in rust-v0.148.0]] · Interface Experience
- [[Changes/Codex CLI/2026-08-18-18-model-support-changes-in-rust-v0-148-0|18 Model Support changes in rust-v0.148.0]] · Model Support
- [[Changes/Codex CLI/2026-08-18-3-mobile-and-desktop-changes-in-rust-v0-148-0|3 Mobile and Desktop changes in rust-v0.148.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-08-18-5-developer-workflow-changes-in-rust-v0-148-0|5 Developer Workflow changes in rust-v0.148.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-08-18-38650-canonicalize-default-namespaces-in-grpc-subscription-filters-copyberry|♯38650 Canonicalize default namespaces in gRPC subscription filters @copyberry]] · Pricing Model
- [[Changes/Codex CLI/2026-08-18-37828-track-running-unified-exec-processes-at-turn-completion-copyberry|♯37828 Track running unified exec processes at turn completion @copyberry]] · Editor Experience
- [[Changes/Codex CLI/2026-08-18-16-account-and-access-changes-in-rust-v0-148-0|16 Account and Access changes in rust-v0.148.0]] · Account and Access
- [[Changes/Codex CLI/2026-08-18-13-context-window-changes-in-rust-v0-148-0|13 Context Window changes in rust-v0.148.0]] · Context Window
- [[Changes/Codex CLI/2026-08-18-12-agent-mode-changes-in-rust-v0-148-0|12 Agent Mode changes in rust-v0.148.0]] · Agent Mode
- [[Changes/Codex CLI/2026-08-18-38024-expose-image-generation-usage-limit-failures-copyberry|♯38024 Expose image generation usage-limit failures @copyberry]] · Image Generation
- [[Changes/Codex CLI/2026-08-18-5-collaboration-changes-in-rust-v0-148-0|5 Collaboration changes in rust-v0.148.0]] · Collaboration
- [[Changes/Codex CLI/2026-08-18-231-other-changes-in-rust-v0-148-0|231 other changes in rust-v0.148.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-08-18 · Claude Code · [[Changes/Claude Code/2026-08-18-2-safety-and-privacy-changes-in-v2-1-235|2 Safety and Privacy changes in v2.1.235]]
- Later: 2026-08-18 · Z.ai API · [[Changes/Z.ai API/2026-08-18-emergent-cybersecurity-capabilities-glm-5-3-matches-mythos-5-in-white-box-code-r|Emergent Cybersecurity Capabilities]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-08-18-95d16c&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-08-18-17-safety-and-privacy-changes-in-rust-v0-148-0.md%0ACard%20ID%3A%20codex-cli-2026-08-18-95d16c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.148.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->