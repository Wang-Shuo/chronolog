---
card_id: codex-cli-2026-08-18-05bfbf
date: '2026-08-18'
description: 'Codex CLI · 2026-08-18 · Interface Experience: 13 changes in 0.148.0
  — Fork sessions with `codex exec fork`, and archive or restore sessions from the
  TUI…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop
    generating: Based on your feedback, we''ve added the ability to stop generating…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1317
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2ef173853e828614f2635f7beae969c00956996baf07b5a0c3279cac3400ac80
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-08-18-05bfbf
  comparison: ''
  date: '2026-08-18'
  description: 'Codex CLI — 0.148.0: 13 Interface Experience changes'
  evidence:
  - quote: 'Fork sessions with `codex exec fork`, and archive or restore sessions
      from the TUI resume picker. (#37367, #37369, #37371)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: 'Composer and transcript rendering now handle CRLF pastes, wrapped whitespace,
      and long URLs correctly. (#37709, #38380, #38704)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37369 Add session archiving to the resume picker @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37371 Restore archived sessions from the resume picker @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37833 Encapsulate watchable skill root selection @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38197 Add an LRU baseline to skill shadow selection @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38204 Fuse recent and lexical skills in shadow selection @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38414 Add bounded transcript rendering for Guardian v2 @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38423 Centralize thread environment selection state @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38461 Centralize turn environment selection state @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38473 Stop generating accepted-line fingerprints @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38605 Fix resume transcript preview line selection @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38608 Fix the missing resume picker history mode import @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 13-interface-experience-changes-in-rust-v0-148-0
  source_release: codex-cli-2026-08-18-rust-v0-148-0-github-372686337-4265c0ae
  source_type: github_releases
  theme: interface-experience
  title: 13 Interface Experience changes in rust-v0.148.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-08-12-vscode-added-session-groups-in-the-sidebar-right-click-to-create-rename-or-delet|VSCode
  Added session groups in the sidebar]]'
- '[[Changes/Claude Code/2026-08-13-improved-fullscreen-streaming-long-sessions-stay-responsive-because-the-whole-co|Improved
  fullscreen streaming]]'
- '[[Changes/Claude Code/2026-08-17-3-interface-experience-changes-in-v2-1-234|3 Interface
  Experience changes in v2.1.234]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-08-18-rust-v0-148-0-github-372686337-4265c0ae|codex-cli-2026-08-18-rust-v0-148-0-github-372686337-4265c0ae]]'
source_type: github_releases
theme: interface-experience
title: 13 Interface Experience changes in rust-v0.148.0
type: change
---

<!-- chronolog:begin region="header" -->
# 13 Interface Experience changes in rust-v0.148.0

**Codex CLI** · 2026-08-18 · [[Themes/interface-experience|Interface Experience]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.148.0) · from [[Releases/Codex CLI/codex-cli-2026-08-18-rust-v0-148-0-github-372686337-4265c0ae|0.148.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Fork sessions with `codex exec fork`, and archive or restore sessions from the TUI resume picker. (#37367, #37369, #37371)

> Composer and transcript rendering now handle CRLF pastes, wrapped whitespace, and long URLs correctly. (#37709, #38380, #38704)

> #37369 Add session archiving to the resume picker @copyberry

> #37371 Restore archived sessions from the resume picker @copyberry

> #37833 Encapsulate watchable skill root selection @copyberry

> #38197 Add an LRU baseline to skill shadow selection @copyberry

> #38204 Fuse recent and lexical skills in shadow selection @copyberry

> #38414 Add bounded transcript rendering for Guardian v2 @copyberry

> #38423 Centralize thread environment selection state @copyberry

> #38461 Centralize turn environment selection state @copyberry

> #38473 Stop generating accepted-line fingerprints @copyberry

> #38605 Fix resume transcript preview line selection @copyberry

> #38608 Fix the missing resume picker history mode import @copyberry

Source: https://github.com/openai/codex/releases/tag/rust-v0.148.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-08-18-57-apps-and-integrations-changes-in-rust-v0-148-0|57 Apps and Integrations changes in rust-v0.148.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-08-18-18-model-support-changes-in-rust-v0-148-0|18 Model Support changes in rust-v0.148.0]] · Model Support
- [[Changes/Codex CLI/2026-08-18-3-mobile-and-desktop-changes-in-rust-v0-148-0|3 Mobile and Desktop changes in rust-v0.148.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-08-18-5-developer-workflow-changes-in-rust-v0-148-0|5 Developer Workflow changes in rust-v0.148.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-08-18-38650-canonicalize-default-namespaces-in-grpc-subscription-filters-copyberry|♯38650 Canonicalize default namespaces in gRPC subscription filters @copyberry]] · Pricing Model
- [[Changes/Codex CLI/2026-08-18-37828-track-running-unified-exec-processes-at-turn-completion-copyberry|♯37828 Track running unified exec processes at turn completion @copyberry]] · Editor Experience
- [[Changes/Codex CLI/2026-08-18-17-safety-and-privacy-changes-in-rust-v0-148-0|17 Safety and Privacy changes in rust-v0.148.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-08-18-16-account-and-access-changes-in-rust-v0-148-0|16 Account and Access changes in rust-v0.148.0]] · Account and Access
- [[Changes/Codex CLI/2026-08-18-13-context-window-changes-in-rust-v0-148-0|13 Context Window changes in rust-v0.148.0]] · Context Window
- [[Changes/Codex CLI/2026-08-18-12-agent-mode-changes-in-rust-v0-148-0|12 Agent Mode changes in rust-v0.148.0]] · Agent Mode
- [[Changes/Codex CLI/2026-08-18-38024-expose-image-generation-usage-limit-failures-copyberry|♯38024 Expose image generation usage-limit failures @copyberry]] · Image Generation
- [[Changes/Codex CLI/2026-08-18-5-collaboration-changes-in-rust-v0-148-0|5 Collaboration changes in rust-v0.148.0]] · Collaboration
- [[Changes/Codex CLI/2026-08-18-231-other-changes-in-rust-v0-148-0|231 other changes in rust-v0.148.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Interface Experience

- Earlier: 2026-08-17 · Claude Code · [[Changes/Claude Code/2026-08-17-3-interface-experience-changes-in-v2-1-234|3 Interface Experience changes in v2.1.234]]
- Later: 2026-08-19 · Claude Code · [[Changes/Claude Code/2026-08-19-changed-the-model-picker-to-highlight-only-the-newest-model-s-name-so-the-highli|Changed the /model picker to highlight only the newest model's name…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop generating: Based on your feedback, we've added the ability to stop generating…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-08-18-05bfbf&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-08-18-13-interface-experience-changes-in-rust-v0-148-0.md%0ACard%20ID%3A%20codex-cli-2026-08-18-05bfbf%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.148.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->