---
card_id: codex-cli-2026-07-09-222591
date: '2026-07-09'
description: 'Codex CLI · 2026-07-09 · Reliability and Performance: Responses WebSockets
  continue using the low-latency transport while respecting system proxies and custom…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General
    performance: Among other improvements, users will notice that ChatGPT is now…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1302
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: cb06fd7bc3e5804d4537e46a0a81bebcdc56639ba427fdcd20353b78c2a54c6c
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-07-09-222591
  comparison: ''
  date: '2026-07-09'
  description: 'Codex CLI — 0.144.0: Responses WebSockets continue using the low-latency
    transport while respecting system proxies and custom certificate authorities.
    (#31441, #31622)'
  evidence:
  - quote: 'Responses WebSockets continue using the low-latency transport while respecting
      system proxies and custom certificate authorities. (#31441, #31622)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: codex-cli
  product_name: Codex CLI
  slug: responses-websockets-continue-using-the-low-latency-transport-while-respecting-s
  source_release: codex-cli-2026-07-09-rust-v0-144-0-github-351657410-407edb96
  source_type: github_releases
  theme: reliability-performance
  title: Responses WebSockets continue using the low-latency transport while respecting…
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-07-07-5-reliability-and-performance-changes-in-v1-0-69|5
  Reliability and Performance changes in v1.0.69]]'
- '[[Changes/v0/2026-07-07-faster-vm-preview-startup-and-vercel-deploys-trimming-several-seconds-of-setup|Faster
  VM preview startup and Vercel deploys, trimming several seconds of setup]]'
- '[[Changes/Claude Code/2026-07-08-auto-update-binary-downloads-now-stream-to-disk-instead-of-buffering-in-memory-c|Auto-update
  binary downloads now stream to disk instead of buffering in memory…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-07-09-rust-v0-144-0-github-351657410-407edb96|codex-cli-2026-07-09-rust-v0-144-0-github-351657410-407edb96]]'
source_type: github_releases
theme: reliability-performance
title: Responses WebSockets continue using the low-latency transport while respecting…
type: change
---

<!-- chronolog:begin region="header" -->
# Responses WebSockets continue using the low-latency transport while respecting…

**Codex CLI** · 2026-07-09 · [[Themes/reliability-performance|Reliability and Performance]] · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.144.0) · from [[Releases/Codex CLI/codex-cli-2026-07-09-rust-v0-144-0-github-351657410-407edb96|0.144.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Responses WebSockets continue using the low-latency transport while respecting system proxies and custom certificate authorities. (#31441, #31622)
>
> Source: https://github.com/openai/codex/releases/tag/rust-v0.144.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-07-09-31191-handle-completion-separators-and-popup-dismissal-charliemarsh-oai|♯31191 Handle completion separators and popup dismissal @charliemarsh-oai]] · Editor Experience
- [[Changes/Codex CLI/2026-07-09-31596-use-the-image-generation-extension-by-default-won-openai|♯31596 Use the image generation extension by default @won-openai]] · Image Generation
- [[Changes/Codex CLI/2026-07-09-31356-ci-run-v8-source-builds-on-windows-2025-anp-oai|♯31356 ci: run V8 source builds on Windows 2025 @anp-oai]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-07-09-11-apps-and-integrations-changes-in-rust-v0-144-0|11 Apps and Integrations changes in rust-v0.144.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-07-09-31587-stabilize-shared-rollout-budget-test-jif-oai|♯31587 Stabilize shared rollout budget test @jif-oai]] · Collaboration
- [[Changes/Codex CLI/2026-07-09-31525-core-migrate-standalone-web-search-to-extension-owned-turn-items-owenlin0|♯31525 core: migrate standalone web search to extension-owned turn items @owenlin0]] · Search and Browsing
- [[Changes/Codex CLI/2026-07-09-5-account-and-access-changes-in-rust-v0-144-0|5 Account and Access changes in rust-v0.144.0]] · Account and Access
- [[Changes/Codex CLI/2026-07-09-8-model-support-changes-in-rust-v0-144-0|8 Model Support changes in rust-v0.144.0]] · Model Support
- [[Changes/Codex CLI/2026-07-09-usage-limit-reset-credits-now-show-their-type-and-expiration-and-let-you-choose|Usage-limit reset credits now show their type and expiration, and let you choose…]] · Pricing Model
- [[Changes/Codex CLI/2026-07-09-3-context-window-changes-in-rust-v0-144-0|3 Context Window changes in rust-v0.144.0]] · Context Window
- [[Changes/Codex CLI/2026-07-09-3-interface-experience-changes-in-rust-v0-144-0|3 Interface Experience changes in rust-v0.144.0]] · Interface Experience
- [[Changes/Codex CLI/2026-07-09-6-developer-workflow-changes-in-rust-v0-144-0|6 Developer Workflow changes in rust-v0.144.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-07-09-4-safety-and-privacy-changes-in-rust-v0-144-0|4 Safety and Privacy changes in rust-v0.144.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-07-09-4-agent-mode-changes-in-rust-v0-144-0|4 Agent Mode changes in rust-v0.144.0]] · Agent Mode
- [[Changes/Codex CLI/2026-07-09-43-other-changes-in-rust-v0-144-0|43 other changes in rust-v0.144.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2026-07-08 · Claude Code · [[Changes/Claude Code/2026-07-08-auto-update-binary-downloads-now-stream-to-disk-instead-of-buffering-in-memory-c|Auto-update binary downloads now stream to disk instead of buffering in memory…]]
- Later: 2026-07-13 · ElevenLabs · [[Changes/ElevenLabs/2026-07-13-packages|Packages]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General performance: Among other improvements, users will notice that ChatGPT is now…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-07-09-222591&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-07-09-responses-websockets-continue-using-the-low-latency-transport-while-respecting-s.md%0ACard%20ID%3A%20codex-cli-2026-07-09-222591%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.144.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->