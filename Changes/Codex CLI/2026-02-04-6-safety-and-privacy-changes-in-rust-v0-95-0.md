---
card_id: codex-cli-2026-02-04-d07ff8
date: '2026-02-04'
description: 'Codex CLI · 2026-02-04 · Safety and Privacy: 6 changes in 0.95.0 — Added
  vendored Bubblewrap + FFI wiring in the Linux sandbox as groundwork for upcoming…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1025
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 372073c5e302b4e11d1d715e10f659fb06da4475578808bf28c463fa280ff461
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-02-04-d07ff8
  comparison: ''
  date: '2026-02-04'
  description: 'Codex CLI — 0.95.0: 6 Safety and Privacy changes'
  evidence:
  - quote: Added vendored Bubblewrap + FFI wiring in the Linux sandbox as groundwork
      for upcoming runtime integration. (#10413)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: Hardened Git command safety so destructive or write-capable invocations
      no longer bypass approval checks. (#10258)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: Updated the `bytes` dependency for a security advisory and cleaned up resolved
      advisory configuration. (#10525)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10415 Fixed sandbox mode inconsistency if untrusted is selected @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10413 feat(linux-sandbox): vendor bubblewrap and wire it with FFI @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10525 chore: update bytes crate in response to security advisory @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 6-safety-and-privacy-changes-in-rust-v0-95-0
  source_release: codex-cli-2026-02-04-rust-v0-95-0-github-282823276-932b0b6b
  source_type: github_releases
  theme: safety-privacy
  title: 6 Safety and Privacy changes in rust-v0.95.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-01-31-4-safety-and-privacy-changes-in-rust-v0-93-0|4 Safety
  and Privacy changes in rust-v0.93.0]]'
- '[[Changes/OpenHands/2026-02-02-2-safety-and-privacy-changes-in-1-3-0|2 Safety and
  Privacy changes in 1.3.0]]'
- '[[Changes/Claude Code/2026-02-03-fixed-permission-dialogs-stealing-focus-while-actively-typing|Fixed
  permission dialogs stealing focus while actively typing]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-02-04-rust-v0-95-0-github-282823276-932b0b6b|codex-cli-2026-02-04-rust-v0-95-0-github-282823276-932b0b6b]]'
source_type: github_releases
theme: safety-privacy
title: 6 Safety and Privacy changes in rust-v0.95.0
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Safety and Privacy changes in rust-v0.95.0

**Codex CLI** · 2026-02-04 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.95.0) · from [[Releases/Codex CLI/codex-cli-2026-02-04-rust-v0-95-0-github-282823276-932b0b6b|0.95.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added vendored Bubblewrap + FFI wiring in the Linux sandbox as groundwork for upcoming runtime integration. (#10413)

> Hardened Git command safety so destructive or write-capable invocations no longer bypass approval checks. (#10258)

> Updated the `bytes` dependency for a security advisory and cleaned up resolved advisory configuration. (#10525)

> #10415 Fixed sandbox mode inconsistency if untrusted is selected @etraut-openai

> #10413 feat(linux-sandbox): vendor bubblewrap and wire it with FFI @viyatb-oai

> #10525 chore: update bytes crate in response to security advisory @bolinfest

Source: https://github.com/openai/codex/releases/tag/rust-v0.95.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-02-04-10-developer-workflow-changes-in-rust-v0-95-0|10 Developer Workflow changes in rust-v0.95.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-02-04-10340-session-picker-shows-thread-name-if-set-pap-openai|♯10340 Session picker shows thread_name if set @pap-openai]] · Interface Experience
- [[Changes/Codex CLI/2026-02-04-2-context-window-changes-in-rust-v0-95-0|2 Context Window changes in rust-v0.95.0]] · Context Window
- [[Changes/Codex CLI/2026-02-04-10404-cleanup-collaboration-mode-variants-charley-oai|♯10404 Cleanup collaboration mode variants @charley-oai]] · Collaboration
- [[Changes/Codex CLI/2026-02-04-2-mobile-and-desktop-changes-in-rust-v0-95-0|2 Mobile and Desktop changes in rust-v0.95.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-02-04-2-model-support-changes-in-rust-v0-95-0|2 Model Support changes in rust-v0.95.0]] · Model Support
- [[Changes/Codex CLI/2026-02-04-4-agent-mode-changes-in-rust-v0-95-0|4 Agent Mode changes in rust-v0.95.0]] · Agent Mode
- [[Changes/Codex CLI/2026-02-04-10274-add-credits-tooltip-pakrym-oai|♯10274 Add credits tooltip @pakrym-oai]] · Pricing Model
- [[Changes/Codex CLI/2026-02-04-5-apps-and-integrations-changes-in-rust-v0-95-0|5 Apps and Integrations changes in rust-v0.95.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-02-04-2-search-and-browsing-changes-in-rust-v0-95-0|2 Search and Browsing changes in rust-v0.95.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-02-04-42-other-changes-in-rust-v0-95-0|42 other changes in rust-v0.95.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-02-03 · Claude Code · [[Changes/Claude Code/2026-02-03-fixed-permission-dialogs-stealing-focus-while-actively-typing|Fixed permission dialogs stealing focus while actively typing]]
- Later: 2026-02-04 · Gemini CLI · [[Changes/Gemini CLI/2026-02-04-security-hooks-wrap-hook-injected-context-in-distinct-xml-tags-by-yunaseoul-in-h|security(hooks): Wrap hook-injected context in distinct XML tags]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-02-04-d07ff8&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-02-04-6-safety-and-privacy-changes-in-rust-v0-95-0.md%0ACard%20ID%3A%20codex-cli-2026-02-04-d07ff8%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.95.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->