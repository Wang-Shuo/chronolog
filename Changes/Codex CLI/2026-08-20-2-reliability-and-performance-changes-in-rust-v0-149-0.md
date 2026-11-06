---
card_id: codex-cli-2026-08-20-043310
date: '2026-08-20'
description: 'Codex CLI · 2026-08-20 · Reliability and Performance: 2 changes in 0.149.0
  — #39025 Speed up the large diff highlighting test @copyberry'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General
    performance: Among other improvements, users will notice that ChatGPT is now…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1344
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 38145bcb80be4d4e3e9da2def52b99c809f01507f9e9eea23c70a6f3f06e48e5
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-08-20-043310
  comparison: ''
  date: '2026-08-20'
  description: 'Codex CLI — 0.149.0: 2 Reliability and Performance changes'
  evidence:
  - quote: '#39025 Speed up the large diff highlighting test @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39030 Speed up the in-app resume cwd test @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 2-reliability-and-performance-changes-in-rust-v0-149-0
  source_release: codex-cli-2026-08-20-rust-v0-149-0-github-374028976-829da944
  source_type: github_releases
  theme: reliability-performance
  title: 2 Reliability and Performance changes in rust-v0.149.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-08-19-improved-startup-performance-the-session-counter-is-now-written-in-the-backgroun|Improved
  startup performance: the session counter is now written in the background]]'
- '[[Changes/Lovable/2026-08-19-faster-preview-loading|Faster preview loading]]'
- '[[Changes/Claude Code/2026-08-20-improved-startup-responsiveness-the-automatic-update-check-now-runs-about-10-sec|Improved
  startup responsiveness]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-08-20-rust-v0-149-0-github-374028976-829da944|codex-cli-2026-08-20-rust-v0-149-0-github-374028976-829da944]]'
source_type: github_releases
theme: reliability-performance
title: 2 Reliability and Performance changes in rust-v0.149.0
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Reliability and Performance changes in rust-v0.149.0

**Codex CLI** · 2026-08-20 · [[Themes/reliability-performance|Reliability and Performance]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.149.0) · from [[Releases/Codex CLI/codex-cli-2026-08-20-rust-v0-149-0-github-374028976-829da944|0.149.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> #39025 Speed up the large diff highlighting test @copyberry

> #39030 Speed up the in-app resume cwd test @copyberry

Source: https://github.com/openai/codex/releases/tag/rust-v0.149.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-08-20-6-model-support-changes-in-rust-v0-149-0|6 Model Support changes in rust-v0.149.0]] · Model Support
- [[Changes/Codex CLI/2026-08-20-18-developer-workflow-changes-in-rust-v0-149-0|18 Developer Workflow changes in rust-v0.149.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-08-20-2-memory-and-personalization-changes-in-rust-v0-149-0|2 Memory and Personalization changes in rust-v0.149.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-08-20-39045-add-managed-gates-for-in-app-chat-and-dictation-copyberry|♯39045 Add managed gates for in-app chat and dictation @copyberry]] · Voice and Audio
- [[Changes/Codex CLI/2026-08-20-18-safety-and-privacy-changes-in-rust-v0-149-0|18 Safety and Privacy changes in rust-v0.149.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-08-20-9-context-window-changes-in-rust-v0-149-0|9 Context Window changes in rust-v0.149.0]] · Context Window
- [[Changes/Codex CLI/2026-08-20-2-collaboration-changes-in-rust-v0-149-0|2 Collaboration changes in rust-v0.149.0]] · Collaboration
- [[Changes/Codex CLI/2026-08-20-5-editor-experience-changes-in-rust-v0-149-0|5 Editor Experience changes in rust-v0.149.0]] · Editor Experience
- [[Changes/Codex CLI/2026-08-20-7-mobile-and-desktop-changes-in-rust-v0-149-0|7 Mobile and Desktop changes in rust-v0.149.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-08-20-3-interface-experience-changes-in-rust-v0-149-0|3 Interface Experience changes in rust-v0.149.0]] · Interface Experience
- [[Changes/Codex CLI/2026-08-20-33-apps-and-integrations-changes-in-rust-v0-149-0|33 Apps and Integrations changes in rust-v0.149.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-08-20-8-account-and-access-changes-in-rust-v0-149-0|8 Account and Access changes in rust-v0.149.0]] · Account and Access
- [[Changes/Codex CLI/2026-08-20-39072-persist-generated-images-through-turn-executors-copyberry|♯39072 Persist generated images through turn executors @copyberry]] · Image Generation
- [[Changes/Codex CLI/2026-08-20-12-agent-mode-changes-in-rust-v0-149-0|12 Agent Mode changes in rust-v0.149.0]] · Agent Mode
- [[Changes/Codex CLI/2026-08-20-39283-document-secure-devcontainer-dns-exfiltration-risk-copyberry|♯39283 Document secure devcontainer DNS exfiltration risk @copyberry]] · Files and Data
- [[Changes/Codex CLI/2026-08-20-39006-emit-api-key-turn-cost-telemetry-from-app-server-copyberry|♯39006 Emit API-key turn cost telemetry from app-server @copyberry]] · Pricing Model
- [[Changes/Codex CLI/2026-08-20-125-other-changes-in-rust-v0-149-0|125 other changes in rust-v0.149.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2026-08-20 · Claude Code · [[Changes/Claude Code/2026-08-20-improved-startup-responsiveness-the-automatic-update-check-now-runs-about-10-sec|Improved startup responsiveness]]
- Later: 2026-08-21 · ChatGPT · [[Changes/ChatGPT/2026-08-21-attach-recent-photos-faster-press-and-hold-the-button-to-open-your-recent-photos|Attach recent photos faster]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General performance: Among other improvements, users will notice that ChatGPT is now…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-08-20-043310&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-08-20-2-reliability-and-performance-changes-in-rust-v0-149-0.md%0ACard%20ID%3A%20codex-cli-2026-08-20-043310%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.149.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->