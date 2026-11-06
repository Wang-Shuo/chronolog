---
card_id: codex-cli-2026-02-12-bcfc53
date: '2026-02-12'
description: 'Codex CLI · 2026-02-12 · Safety and Privacy: 5 changes in 0.100.0 —
  Promoted sandbox capabilities on both Linux and Windows, and introduced a new…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1033
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 4fe39593c8558e3cfb226a79550fabe62d60b6376066cd693385b1c55c3047a0
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-02-12-bcfc53
  comparison: ''
  date: '2026-02-12'
  description: 'Codex CLI — 0.100.0: 5 Safety and Privacy changes'
  evidence:
  - quote: 'Promoted sandbox capabilities on both Linux and Windows, and introduced
      a new `ReadOnlyAccess` policy shape for configurable read access. (#11381, #11341,
      #11387)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11381 feat(core): promote Linux bubblewrap sandbox to Experimental @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11341 Promote Windows Sandbox @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11387 feat: make sandbox read access configurable with `ReadOnlyAccess`
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11498 build(linux-sandbox): always compile vendored bubblewrap on Linux;
      remove CODEX_BWRAP_ENABLE_FFI @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 5-safety-and-privacy-changes-in-rust-v0-100-0
  source_release: codex-cli-2026-02-12-rust-v0-100-0-github-285810603-4852bda6
  source_type: github_releases
  theme: safety-privacy
  title: 5 Safety and Privacy changes in rust-v0.100.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-02-10-2-safety-and-privacy-changes-in-v2-1-38|2 Safety
  and Privacy changes in v2.1.38]]'
- '[[Changes/Gemini CLI/2026-02-10-3-safety-and-privacy-changes-in-v0-28-0|3 Safety
  and Privacy changes in v0.28.0]]'
- '[[Changes/Codex CLI/2026-02-11-8-safety-and-privacy-changes-in-rust-v0-99-0|8 Safety
  and Privacy changes in rust-v0.99.0]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-02-12-rust-v0-100-0-github-285810603-4852bda6|codex-cli-2026-02-12-rust-v0-100-0-github-285810603-4852bda6]]'
source_type: github_releases
theme: safety-privacy
title: 5 Safety and Privacy changes in rust-v0.100.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Safety and Privacy changes in rust-v0.100.0

**Codex CLI** · 2026-02-12 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.100.0) · from [[Releases/Codex CLI/codex-cli-2026-02-12-rust-v0-100-0-github-285810603-4852bda6|0.100.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Promoted sandbox capabilities on both Linux and Windows, and introduced a new `ReadOnlyAccess` policy shape for configurable read access. (#11381, #11341, #11387)

> #11381 feat(core): promote Linux bubblewrap sandbox to Experimental @viyatb-oai

> #11341 Promote Windows Sandbox @iceweasel-oai

> #11387 feat: make sandbox read access configurable with `ReadOnlyAccess` @bolinfest

> #11498 build(linux-sandbox): always compile vendored bubblewrap on Linux; remove CODEX_BWRAP_ENABLE_FFI @viyatb-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.100.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-02-12-11-memory-and-personalization-changes-in-rust-v0-100-0|11 Memory and Personalization changes in rust-v0.100.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-02-12-11412-tui-show-non-file-layer-content-in-debug-config-bolinfest|♯11412 tui: show non-file layer content in /debug-config @bolinfest]] · Developer Workflow
- [[Changes/Codex CLI/2026-02-12-11521-test-app-server-stabilize-app-list-thread-feature-flag-test-by-using-file|♯11521 test(app-server): stabilize app/list thread feature-flag test by using…]] · Account and Access
- [[Changes/Codex CLI/2026-02-12-3-context-window-changes-in-rust-v0-100-0|3 Context Window changes in rust-v0.100.0]] · Context Window
- [[Changes/Codex CLI/2026-02-12-improved-websocket-session-stability-by-continuing-ping-handling-when-idle-and-s|Improved websocket session stability by continuing ping handling when idle…]] · Reliability and Performance
- [[Changes/Codex CLI/2026-02-12-2-agent-mode-changes-in-rust-v0-100-0|2 Agent Mode changes in rust-v0.100.0]] · Agent Mode
- [[Changes/Codex CLI/2026-02-12-4-mobile-and-desktop-changes-in-rust-v0-100-0|4 Mobile and Desktop changes in rust-v0.100.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-02-12-4-model-support-changes-in-rust-v0-100-0|4 Model Support changes in rust-v0.100.0]] · Model Support
- [[Changes/Codex CLI/2026-02-12-reduced-repeated-skill-parse-error-spam-during-active-edits-by-increasing-file-w|Reduced repeated skill parse-error spam during active edits by increasing…]] · Editor Experience
- [[Changes/Codex CLI/2026-02-12-5-apps-and-integrations-changes-in-rust-v0-100-0|5 Apps and Integrations changes in rust-v0.100.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-02-12-59-other-changes-in-rust-v0-100-0|59 other changes in rust-v0.100.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-02-11 · Codex CLI · [[Changes/Codex CLI/2026-02-11-8-safety-and-privacy-changes-in-rust-v0-99-0|8 Safety and Privacy changes in rust-v0.99.0]]
- Later: 2026-02-12 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-02-12-permission-prompts-with-long-diffs-are-scrollable-in-alt-screen-mode|Permission prompts with long diffs are scrollable in alt-screen mode]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-02-12-bcfc53&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-02-12-5-safety-and-privacy-changes-in-rust-v0-100-0.md%0ACard%20ID%3A%20codex-cli-2026-02-12-bcfc53%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.100.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->