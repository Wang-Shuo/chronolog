---
card_id: codex-cli-2026-05-18-c53959
date: '2026-05-18'
description: 'Codex CLI · 2026-05-18 · Mobile and Desktop: 10 changes in 0.131.0 —
  Documented new app-server/API contracts for remote environments and the desktop-owned…'
diffusion:
  first_in_tracked: "[[Changes/Cursor/2023-03-14-windows-and-linux-support|Windows
    and Linux support \U0001F973]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1161
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: mobile-desktop
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: adf6eb481c1f69744746b6c0ac89cf98488ed73b4e3ebcbbacf7dd9836472c7f
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-05-18-c53959
  comparison: ''
  date: '2026-05-18'
  description: 'Codex CLI — 0.131.0: 10 Mobile and Desktop changes'
  evidence:
  - quote: 'Documented new app-server/API contracts for remote environments and the
      desktop-owned config namespace. (#21323, #22584)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: 'Improved CI and release reliability across Rust CI, exact PR-head checkout,
      Windows Bazel sharding, unsigned macOS artifacts, and signed macOS promotion.
      (#21604, #21628, #21835, #22408, #22559, #22649, #22737, #22788, #22900)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#20619 [codex] request desktop attestation from app @jiamingz42'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22443 Scope macOS signing secrets to release environment @shijie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22513 Revert "Scope macOS signing secrets to release environment" @shijie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22559 Add unsigned macOS release artifacts @shijie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22737 ci: support signed macOS release promotion @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22584 [codex] Add opaque desktop config namespace @guinness-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22788 Fix signed macOS release promotion follow-up jobs @shijie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22900 Disable DMG staging for signed macOS promotion @shijie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 10-mobile-and-desktop-changes-in-rust-v0-131-0
  source_release: codex-cli-2026-05-18-rust-v0-131-0-github-324452638-5f16ff1d
  source_type: github_releases
  theme: mobile-desktop
  title: 10 Mobile and Desktop changes in rust-v0.131.0
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-05-12-free-users-in-chatgpt-will-now-see-more-inline-images-from-the-web-to-help-make|More
  images in answers for Free users]]'
- '[[Changes/ChatGPT/2026-05-14-generated-images-will-continue-to-appear-in-the-images-tab-storage-management-is|Generated
  images will continue to appear in the Images tab]]'
- '[[Changes/Claude Code/2026-05-15-the-powershell-tool-is-now-enabled-by-default-on-windows-for-bedrock-vertex-and|The
  PowerShell tool is now enabled by default on Windows for Bedrock, Vertex…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-05-18-rust-v0-131-0-github-324452638-5f16ff1d|codex-cli-2026-05-18-rust-v0-131-0-github-324452638-5f16ff1d]]'
source_type: github_releases
theme: mobile-desktop
title: 10 Mobile and Desktop changes in rust-v0.131.0
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Mobile and Desktop changes in rust-v0.131.0

**Codex CLI** · 2026-05-18 · [[Themes/mobile-desktop|Mobile and Desktop]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.131.0) · from [[Releases/Codex CLI/codex-cli-2026-05-18-rust-v0-131-0-github-324452638-5f16ff1d|0.131.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Documented new app-server/API contracts for remote environments and the desktop-owned config namespace. (#21323, #22584)

> Improved CI and release reliability across Rust CI, exact PR-head checkout, Windows Bazel sharding, unsigned macOS artifacts, and signed macOS promotion. (#21604, #21628, #21835, #22408, #22559, #22649, #22737, #22788, #22900)

> #20619 [codex] request desktop attestation from app @jiamingz42

> #22443 Scope macOS signing secrets to release environment @shijie-oai

> #22513 Revert "Scope macOS signing secrets to release environment" @shijie-oai

> #22559 Add unsigned macOS release artifacts @shijie-oai

> #22737 ci: support signed macOS release promotion @bolinfest

> #22584 [codex] Add opaque desktop config namespace @guinness-oai

> #22788 Fix signed macOS release promotion follow-up jobs @shijie-oai

> #22900 Disable DMG staging for signed macOS promotion @shijie-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.131.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-05-18-5-account-and-access-changes-in-rust-v0-131-0|5 Account and Access changes in rust-v0.131.0]] · Account and Access
- [[Changes/Codex CLI/2026-05-18-17-safety-and-privacy-changes-in-rust-v0-131-0|17 Safety and Privacy changes in rust-v0.131.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-05-18-9-agent-mode-changes-in-rust-v0-131-0|9 Agent Mode changes in rust-v0.131.0]] · Agent Mode
- [[Changes/Codex CLI/2026-05-18-4-memory-and-personalization-changes-in-rust-v0-131-0|4 Memory and Personalization changes in rust-v0.131.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-05-18-5-interface-experience-changes-in-rust-v0-131-0|5 Interface Experience changes in rust-v0.131.0]] · Interface Experience
- [[Changes/Codex CLI/2026-05-18-12-developer-workflow-changes-in-rust-v0-131-0|12 Developer Workflow changes in rust-v0.131.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-05-18-56-apps-and-integrations-changes-in-rust-v0-131-0|56 Apps and Integrations changes in rust-v0.131.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-05-18-21954-fix-goal-update-and-add-goal-edit-command-in-tui-etraut-openai|♯21954 Fix goal update and add /goal edit command in TUI @etraut-openai]] · Editor Experience
- [[Changes/Codex CLI/2026-05-18-7-context-window-changes-in-rust-v0-131-0|7 Context Window changes in rust-v0.131.0]] · Context Window
- [[Changes/Codex CLI/2026-05-18-3-collaboration-changes-in-rust-v0-131-0|3 Collaboration changes in rust-v0.131.0]] · Collaboration
- [[Changes/Codex CLI/2026-05-18-4-model-support-changes-in-rust-v0-131-0|4 Model Support changes in rust-v0.131.0]] · Model Support
- [[Changes/Codex CLI/2026-05-18-155-other-changes-in-rust-v0-131-0|155 other changes in rust-v0.131.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Mobile and Desktop

- Earlier: 2026-05-15 · Claude Code · [[Changes/Claude Code/2026-05-15-the-powershell-tool-is-now-enabled-by-default-on-windows-for-bedrock-vertex-and|The PowerShell tool is now enabled by default on Windows for Bedrock, Vertex…]]
- Later: 2026-05-19 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-05-19-2-mobile-and-desktop-changes-in-v1-0-49|2 Mobile and Desktop changes in v1.0.49]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-14 · Cursor · [[Changes/Cursor/2023-03-14-windows-and-linux-support|Windows and Linux support 🥳]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-05-18-c53959&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-05-18-10-mobile-and-desktop-changes-in-rust-v0-131-0.md%0ACard%20ID%3A%20codex-cli-2026-05-18-c53959%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.131.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->