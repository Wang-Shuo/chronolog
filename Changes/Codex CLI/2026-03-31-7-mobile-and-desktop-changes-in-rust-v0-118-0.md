---
card_id: codex-cli-2026-03-31-d79e37
date: '2026-03-31'
description: 'Codex CLI · 2026-03-31 · Mobile and Desktop: 7 changes in 0.118.0 —
  On Windows, `apply_patch` is less likely to fail because it no longer adds redundant…'
diffusion:
  first_in_tracked: "[[Changes/Cursor/2023-03-14-windows-and-linux-support|Windows
    and Linux support \U0001F973]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1113
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: mobile-desktop
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b317c24672185932b4f2696b88c09d51fb66c23247d48d10137d0be84c41f67c
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-03-31-d79e37
  comparison: ''
  date: '2026-03-31'
  description: 'Codex CLI — 0.118.0: 7 Mobile and Desktop changes'
  evidence:
  - quote: On Windows, `apply_patch` is less likely to fail because it no longer adds
      redundant writable roots that could trigger unnecessary ACL churn. (#16030)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#15067 Protect first-time project .codex creation across Linux and macOS
      sandboxes @rreichel3-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#15918 permissions: remove macOS seatbelt extension profiles @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#15931 fix: make MACOS_DEFAULT_PREFERENCES_POLICY part of MACOS_SEATBELT_BASE_POLICY
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#16054 chore: clean up argument-comment lint and roll out all-target CI
      on macOS @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#16067 ci: run Bazel clippy on Windows gnullvm @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#16128 bazel: refresh the expired macOS SDK pin @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 7-mobile-and-desktop-changes-in-rust-v0-118-0
  source_release: codex-cli-2026-03-31-rust-v0-118-0-github-303805427-02df59b6
  source_type: github_releases
  theme: mobile-desktop
  title: 7 Mobile and Desktop changes in rust-v0.118.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-03-26-added-powershell-tool-for-windows-as-an-opt-in-preview-learn-more-at-https-code|Added
  PowerShell tool for Windows as an opt-in preview]]'
- '[[Changes/Codex CLI/2026-03-26-3-mobile-and-desktop-changes-in-rust-v0-117-0|3
  Mobile and Desktop changes in rust-v0.117.0]]'
- '[[Changes/GitHub Copilot CLI/2026-03-26-2-mobile-and-desktop-changes-in-v1-0-12|2
  Mobile and Desktop changes in v1.0.12]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-03-31-rust-v0-118-0-github-303805427-02df59b6|codex-cli-2026-03-31-rust-v0-118-0-github-303805427-02df59b6]]'
source_type: github_releases
theme: mobile-desktop
title: 7 Mobile and Desktop changes in rust-v0.118.0
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Mobile and Desktop changes in rust-v0.118.0

**Codex CLI** · 2026-03-31 · [[Themes/mobile-desktop|Mobile and Desktop]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.118.0) · from [[Releases/Codex CLI/codex-cli-2026-03-31-rust-v0-118-0-github-303805427-02df59b6|0.118.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> On Windows, `apply_patch` is less likely to fail because it no longer adds redundant writable roots that could trigger unnecessary ACL churn. (#16030)

> #15067 Protect first-time project .codex creation across Linux and macOS sandboxes @rreichel3-oai

> #15918 permissions: remove macOS seatbelt extension profiles @bolinfest

> #15931 fix: make MACOS_DEFAULT_PREFERENCES_POLICY part of MACOS_SEATBELT_BASE_POLICY @bolinfest

> #16054 chore: clean up argument-comment lint and roll out all-target CI on macOS @bolinfest

> #16067 ci: run Bazel clippy on Windows gnullvm @bolinfest

> #16128 bazel: refresh the expired macOS SDK pin @bolinfest

Source: https://github.com/openai/codex/releases/tag/rust-v0.118.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-03-31-16286-auth-generalize-external-auth-tokens-for-bearer-only-sources-bolinfest|♯16286 auth: generalize external auth tokens for bearer-only sources @bolinfest]] · Context Window
- [[Changes/Codex CLI/2026-03-31-16021-fix-copy-regression-in-tui-app-server-turn-completion-etraut-openai|♯16021 Fix /copy regression in tui_app_server turn completion @etraut-openai]] · Editor Experience
- [[Changes/Codex CLI/2026-03-31-12-apps-and-integrations-changes-in-rust-v0-118-0|12 Apps and Integrations changes in rust-v0.118.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-03-31-16114-remove-tui-voice-transcription-feature-etraut-openai|♯16114 Remove TUI voice transcription feature @etraut-openai]] · Voice and Audio
- [[Changes/Codex CLI/2026-03-31-3-interface-experience-changes-in-rust-v0-118-0|3 Interface Experience changes in rust-v0.118.0]] · Interface Experience
- [[Changes/Codex CLI/2026-03-31-4-account-and-access-changes-in-rust-v0-118-0|4 Account and Access changes in rust-v0.118.0]] · Account and Access
- [[Changes/Codex CLI/2026-03-31-3-developer-workflow-changes-in-rust-v0-118-0|3 Developer Workflow changes in rust-v0.118.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-03-31-15934-add-usage-based-business-plan-types-bwanner-oai|♯15934 Add usage-based business plan types @bwanner-oai]] · Pricing Model
- [[Changes/Codex CLI/2026-03-31-7-safety-and-privacy-changes-in-rust-v0-118-0|7 Safety and Privacy changes in rust-v0.118.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-03-31-4-agent-mode-changes-in-rust-v0-118-0|4 Agent Mode changes in rust-v0.118.0]] · Agent Mode
- [[Changes/Codex CLI/2026-03-31-4-collaboration-changes-in-rust-v0-118-0|4 Collaboration changes in rust-v0.118.0]] · Collaboration
- [[Changes/Codex CLI/2026-03-31-5-model-support-changes-in-rust-v0-118-0|5 Model Support changes in rust-v0.118.0]] · Model Support
- [[Changes/Codex CLI/2026-03-31-51-other-changes-in-rust-v0-118-0|51 other changes in rust-v0.118.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Mobile and Desktop

- Earlier: 2026-03-26 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-03-26-2-mobile-and-desktop-changes-in-v1-0-12|2 Mobile and Desktop changes in v1.0.12]]
- Later: 2026-04-01 · Claude Code · [[Changes/Claude Code/2026-04-01-powershell-tool-on-windows-external-command-arguments-containing-both-a-double-q|PowerShell tool on Windows]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-14 · Cursor · [[Changes/Cursor/2023-03-14-windows-and-linux-support|Windows and Linux support 🥳]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-03-31-d79e37&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-03-31-7-mobile-and-desktop-changes-in-rust-v0-118-0.md%0ACard%20ID%3A%20codex-cli-2026-03-31-d79e37%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.118.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->