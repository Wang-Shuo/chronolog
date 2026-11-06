---
card_id: codex-cli-2025-08-27-f240fa
date: '2025-08-27'
description: 'Codex CLI · 2025-08-27 · Other changes: 21 changes in 0.25.0 — Core:
  remove_conversation API for manual cleanup in long‑lived servers (#2613)'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 32f05323dc1adb8735025152a618153c4dab1495d176fd88e1b9e81c932d8120
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2025-08-27-f240fa
  comparison: ''
  date: '2025-08-27'
  description: 'Codex CLI — 0.25.0: 21 other changes'
  evidence:
  - quote: 'Core: remove_conversation API for manual cleanup in long‑lived servers
      (#2613)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.25.0
  - quote: 'TUI: Alt+Ctrl+H deletes the previous word (parity with Alt+Backspace)
      (#2717)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.25.0
  - quote: Cache transcript line wraps to keep long transcripts responsive (#2739)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.25.0
  - quote: ESC with queued messages returns them to the composer (#2687)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.25.0
  - quote: Prevent crash when backspacing placeholders near multibyte text (#2674)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.25.0
  - quote: Don’t send Exec deltas on apply_patch (#2742)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.25.0
  - quote: Reduce test load when running interactively (#2707)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.25.0
  - quote: Deduplicate assistant messages in history (#2758)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.25.0
  - quote: Remove the Codex GitHub Action for now (#2729)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.25.0
  - quote: '#2758 [fix] Deduplicate assistant messages'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.25.0
  - quote: '#2739 [perf] Cache transcript wraps'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.25.0
  - quote: '#2707 [feat] Decrease testing when running interactively'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.25.0
  - quote: '#2742 [fix] Don’t send Exec deltas on apply patch'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.25.0
  - quote: '#2674 [fix] Crash when backspacing placeholders adjacent to multibyte
      text'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.25.0
  - quote: '#2735 [fix] Emoji spacing'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.25.0
  - quote: '#2717 [feat] Alt+Ctrl+H deletes backward word'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.25.0
  - quote: '#2687 [feat] Esc with queued messages returns them to composer'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.25.0
  - quote: '#2728 [tui] Render keyboard icon with emoji variation selector (⌨️)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.25.0
  - quote: '#2613 [feat(core)] Add remove_conversation to ConversationManager'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.25.0
  - quote: '#2729 [chore] Remove GitHub Action that runs Codex'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.25.0
  - quote: '#2686 [feat] Enable alternate scroll in transcript mode'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.25.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 21-other-changes-in-rust-v0-25-0
  source_release: codex-cli-2025-08-27-rust-v0-25-0-github-242803749-ad836b6a
  source_type: github_releases
  theme: uncategorized
  title: 21 other changes in rust-v0.25.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2025-08-27-rust-v0-25-0-github-242803749-ad836b6a|codex-cli-2025-08-27-rust-v0-25-0-github-242803749-ad836b6a]]'
source_type: github_releases
theme: uncategorized
title: 21 other changes in rust-v0.25.0
type: change
---

<!-- chronolog:begin region="header" -->
# 21 other changes in rust-v0.25.0

**Codex CLI** · 2025-08-27 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.25.0) · from [[Releases/Codex CLI/codex-cli-2025-08-27-rust-v0-25-0-github-242803749-ad836b6a|0.25.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Core: remove_conversation API for manual cleanup in long‑lived servers (#2613)

> TUI: Alt+Ctrl+H deletes the previous word (parity with Alt+Backspace) (#2717)

> Cache transcript line wraps to keep long transcripts responsive (#2739)

> ESC with queued messages returns them to the composer (#2687)

> Prevent crash when backspacing placeholders near multibyte text (#2674)

> Don’t send Exec deltas on apply_patch (#2742)

> Reduce test load when running interactively (#2707)

> Deduplicate assistant messages in history (#2758)

> Remove the Codex GitHub Action for now (#2729)

> #2758 [fix] Deduplicate assistant messages

> #2739 [perf] Cache transcript wraps

> #2707 [feat] Decrease testing when running interactively

> #2742 [fix] Don’t send Exec deltas on apply patch

> #2674 [fix] Crash when backspacing placeholders adjacent to multibyte text

> #2735 [fix] Emoji spacing

> #2717 [feat] Alt+Ctrl+H deletes backward word

> #2687 [feat] Esc with queued messages returns them to composer

> #2728 [tui] Render keyboard icon with emoji variation selector (⌨️)

> #2613 [feat(core)] Add remove_conversation to ConversationManager

> #2729 [chore] Remove GitHub Action that runs Codex

> #2686 [feat] Enable alternate scroll in transcript mode

Source: https://github.com/openai/codex/releases/tag/rust-v0.25.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2025-08-27-4-editor-experience-changes-in-rust-v0-25-0|4 Editor Experience changes in rust-v0.25.0]] · Editor Experience
- [[Changes/Codex CLI/2025-08-27-2-context-window-changes-in-rust-v0-25-0|2 Context Window changes in rust-v0.25.0]] · Context Window
- [[Changes/Codex CLI/2025-08-27-improve-emoji-rendering-proper-spacing-and-emoji-variant-2735-2728|Improve emoji rendering: proper spacing and ⌨️ emoji variant (♯2735, ♯2728)]] · Interface Experience
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2025-08-27-f240fa&body=Card%3A%20Changes%2FCodex%20CLI%2F2025-08-27-21-other-changes-in-rust-v0-25-0.md%0ACard%20ID%3A%20codex-cli-2025-08-27-f240fa%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.25.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->