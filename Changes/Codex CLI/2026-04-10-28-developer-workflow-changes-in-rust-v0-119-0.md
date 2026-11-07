---
card_id: codex-cli-2026-04-10-1da7fd
date: '2026-04-10'
description: 'Codex CLI · 2026-04-10 · Developer Workflow: 28 changes in 0.119.0 —
  TUI notifications are more configurable, including Warp OSC 9 support and an opt-in
  mode…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2768
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: cd2c032cf63f5dbf1747734f6f1970e8ecbc00892c098af7ea56e07915f36457
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-04-10-1da7fd
  comparison: ''
  date: '2026-04-10'
  description: 'Codex CLI — 0.119.0: 28 Developer Workflow changes'
  evidence:
  - quote: 'TUI notifications are more configurable, including Warp OSC 9 support
      and an opt-in mode for notifications even while the terminal is focused (#17174,
      #17175).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16457 tui: remove debug/test-only crate features @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16498 fix: guard guardian_command_source_tool_name with cfg(unix) @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16590 Fix non-determinism in rules_rs/crate_git_repository.bzl @tyler-french'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16617 fix: add shell fallback paths for pwsh/powershell that work on
      GitHub Actions Windows runners @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16635 app-server: make thread/shellCommand tests shell-aware @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16665 fix: use COMSPEC in Windows unicode shell test @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16668 fix: use cmd.exe in Windows unicode shell test @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16707 fix: preserve platform-specific core shell env vars @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17002 chore: debug flag to hide some parameters @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17007 chore: hide nickname for debug flag @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17031 fix(core) revert Command line in unified exec output @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17117 codex debug 1 (guardian approved) @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17119 codex debug 3 (guardian approved) @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17121 codex debug 5 (guardian approved) @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17123 codex debug 7 (guardian approved) @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17125 codex debug 9 (guardian approved) @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17127 codex debug 11 (guardian approved) @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17129 codex debug 13 (guardian approved) @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17131 codex debug 15 (guardian approved) @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17118 codex debug 2 (guardian approved) @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17120 codex debug 4 (guardian approved) @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17122 codex debug 6 (guardian approved) @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17124 codex debug 8 (guardian approved) @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17126 codex debug 10 (guardian approved) @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17128 codex debug 12 (guardian approved) @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17130 codex debug 14 (guardian approved) @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17217 Skip local shell snapshots for remote unified exec @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 28-developer-workflow-changes-in-rust-v0-119-0
  source_release: codex-cli-2026-04-10-rust-v0-119-0-github-307754801-19f169d1
  source_type: github_releases
  theme: developer-workflow
  title: 28 Developer Workflow changes in rust-v0.119.0
  type: change
related_changes:
- '[[Changes/OpenCode/2026-04-08-terminal-added-pdf-drag-and-drop-for-attachments|Terminal
  Added PDF drag and drop for attachments]]'
- '[[Changes/Claude Code/2026-04-09-6-developer-workflow-changes-in-v2-1-98|6 Developer
  Workflow changes in v2.1.98]]'
- '[[Changes/OpenCode/2026-04-09-4-developer-workflow-changes-in-v1-4-2-1|4 Developer
  Workflow changes in v1.4.2 + 1]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-04-10-rust-v0-119-0-github-307754801-19f169d1|codex-cli-2026-04-10-rust-v0-119-0-github-307754801-19f169d1]]'
source_type: github_releases
theme: developer-workflow
title: 28 Developer Workflow changes in rust-v0.119.0
type: change
---

<!-- chronolog:begin region="header" -->
# 28 Developer Workflow changes in rust-v0.119.0

**Codex CLI** · 2026-04-10 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.119.0) · from [[Releases/Codex CLI/codex-cli-2026-04-10-rust-v0-119-0-github-307754801-19f169d1|0.119.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> TUI notifications are more configurable, including Warp OSC 9 support and an opt-in mode for notifications even while the terminal is focused (#17174, #17175).

> #16457 tui: remove debug/test-only crate features @bolinfest

> #16498 fix: guard guardian_command_source_tool_name with cfg(unix) @bolinfest

> #16590 Fix non-determinism in rules_rs/crate_git_repository.bzl @tyler-french

> #16617 fix: add shell fallback paths for pwsh/powershell that work on GitHub Actions Windows runners @bolinfest

> #16635 app-server: make thread/shellCommand tests shell-aware @bolinfest

> #16665 fix: use COMSPEC in Windows unicode shell test @bolinfest

> #16668 fix: use cmd.exe in Windows unicode shell test @bolinfest

> #16707 fix: preserve platform-specific core shell env vars @bolinfest

> #17002 chore: debug flag to hide some parameters @jif-oai

> #17007 chore: hide nickname for debug flag @jif-oai

> #17031 fix(core) revert Command line in unified exec output @dylan-hurd-oai

> #17117 codex debug 1 (guardian approved) @jif-oai

> #17119 codex debug 3 (guardian approved) @jif-oai

> #17121 codex debug 5 (guardian approved) @jif-oai

> #17123 codex debug 7 (guardian approved) @jif-oai

> #17125 codex debug 9 (guardian approved) @jif-oai

> #17127 codex debug 11 (guardian approved) @jif-oai

> #17129 codex debug 13 (guardian approved) @jif-oai

> #17131 codex debug 15 (guardian approved) @jif-oai

> #17118 codex debug 2 (guardian approved) @jif-oai

> #17120 codex debug 4 (guardian approved) @jif-oai

> #17122 codex debug 6 (guardian approved) @jif-oai

> #17124 codex debug 8 (guardian approved) @jif-oai

> #17126 codex debug 10 (guardian approved) @jif-oai

> #17128 codex debug 12 (guardian approved) @jif-oai

> #17130 codex debug 14 (guardian approved) @jif-oai

> #17217 Skip local shell snapshots for remote unified exec @jif-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.119.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-04-10-4-context-window-changes-in-rust-v0-119-0|4 Context Window changes in rust-v0.119.0]] · Context Window
- [[Changes/Codex CLI/2026-04-10-8-safety-and-privacy-changes-in-rust-v0-119-0|8 Safety and Privacy changes in rust-v0.119.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-04-10-13-agent-mode-changes-in-rust-v0-119-0|13 Agent Mode changes in rust-v0.119.0]] · Agent Mode
- [[Changes/Codex CLI/2026-04-10-2-memory-and-personalization-changes-in-rust-v0-119-0|2 Memory and Personalization changes in rust-v0.119.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-04-10-the-readme-now-uses-the-current-chatgpt-business-plan-name-16348|The README now uses the current ChatGPT Business plan name (♯16348)]] · Enterprise and Administration
- [[Changes/Codex CLI/2026-04-10-3-voice-and-audio-changes-in-rust-v0-119-0|3 Voice and Audio changes in rust-v0.119.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-04-10-19-apps-and-integrations-changes-in-rust-v0-119-0|19 Apps and Integrations changes in rust-v0.119.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-04-10-2-account-and-access-changes-in-rust-v0-119-0|2 Account and Access changes in rust-v0.119.0]] · Account and Access
- [[Changes/Codex CLI/2026-04-10-17256-app-server-use-shared-receivers-for-app-server-message-processors-euroeles|♯17256 app-server: Use shared receivers for app-server message processors @euroelessar]] · Collaboration
- [[Changes/Codex CLI/2026-04-10-10-interface-experience-changes-in-rust-v0-119-0|10 Interface Experience changes in rust-v0.119.0]] · Interface Experience
- [[Changes/Codex CLI/2026-04-10-16202-fix-paste-driven-bottom-pane-completion-teardown-etraut-openai|♯16202 Fix paste-driven bottom pane completion teardown @etraut-openai]] · Editor Experience
- [[Changes/Codex CLI/2026-04-10-2-reliability-and-performance-changes-in-rust-v0-119-0|2 Reliability and Performance changes in rust-v0.119.0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-04-10-5-model-support-changes-in-rust-v0-119-0|5 Model Support changes in rust-v0.119.0]] · Model Support
- [[Changes/Codex CLI/2026-04-10-6-mobile-and-desktop-changes-in-rust-v0-119-0|6 Mobile and Desktop changes in rust-v0.119.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-04-10-187-other-changes-in-rust-v0-119-0|187 other changes in rust-v0.119.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-04-09 · OpenCode · [[Changes/OpenCode/2026-04-09-4-developer-workflow-changes-in-v1-4-2-1|4 Developer Workflow changes in v1.4.2 + 1]]
- Later: 2026-04-10 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-04-10-terminal-state-alt-screen-cursor-raw-mode-is-restored-correctly-after-cli-crashe|Terminal state (alt screen, cursor, raw mode) is restored correctly after CLI…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-04-10-1da7fd&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-04-10-28-developer-workflow-changes-in-rust-v0-119-0.md%0ACard%20ID%3A%20codex-cli-2026-04-10-1da7fd%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.119.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->