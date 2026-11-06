---
card_id: codex-cli-2026-04-11-c32011
date: '2026-04-11'
description: 'Codex CLI · 2026-04-11 · Safety and Privacy: 4 changes in 0.120.0 —
  Fixed sandbox permission handling for symlinked writable roots and carveouts, preventing…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1091
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 5c60c1c9d0c50346199cfe2c73dbb2394db9c87fddb5807a01ef9ad618cc98a2
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-04-11-c32011
  comparison: ''
  date: '2026-04-11'
  description: 'Codex CLI — 0.120.0: 4 Safety and Privacy changes'
  evidence:
  - quote: Fixed sandbox permission handling for symlinked writable roots and carveouts,
      preventing failures in shell and `apply_patch` workflows (#15981)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.120.0
  - quote: Documented the elevated vs restricted-token Windows sandbox support split
      in the core README (#14568)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.120.0
  - quote: '#14568 fix: support split carveouts in windows elevated sandbox @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.120.0
  - quote: '#15981 fix(permissions): fix symlinked writable roots in sandbox permissions
      @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.120.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 4-safety-and-privacy-changes-in-rust-v0-120-0
  source_release: codex-cli-2026-04-11-rust-v0-120-0-github-307789275-437473b9
  source_type: github_releases
  theme: safety-privacy
  title: 4 Safety and Privacy changes in rust-v0.120.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-04-09-permission-checks-and-other-hooks-now-work-correctly-when-using-anthropic-models|Permission
  checks and other hooks now work correctly when using Anthropic models…]]'
- '[[Changes/Claude Code/2026-04-10-fixed-a-command-injection-vulnerability-in-the-posix-which-fallback-used-by-lsp|Fixed
  a command injection vulnerability in the POSIX which fallback used by LSP…]]'
- '[[Changes/Codex CLI/2026-04-10-8-safety-and-privacy-changes-in-rust-v0-119-0|8
  Safety and Privacy changes in rust-v0.119.0]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-04-11-rust-v0-120-0-github-307789275-437473b9|codex-cli-2026-04-11-rust-v0-120-0-github-307789275-437473b9]]'
source_type: github_releases
theme: safety-privacy
title: 4 Safety and Privacy changes in rust-v0.120.0
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Safety and Privacy changes in rust-v0.120.0

**Codex CLI** · 2026-04-11 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.120.0) · from [[Releases/Codex CLI/codex-cli-2026-04-11-rust-v0-120-0-github-307789275-437473b9|0.120.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Fixed sandbox permission handling for symlinked writable roots and carveouts, preventing failures in shell and `apply_patch` workflows (#15981)

> Documented the elevated vs restricted-token Windows sandbox support split in the core README (#14568)

> #14568 fix: support split carveouts in windows elevated sandbox @viyatb-oai

> #15981 fix(permissions): fix symlinked writable roots in sandbox permissions @viyatb-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.120.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-04-11-3-context-window-changes-in-rust-v0-120-0|3 Context Window changes in rust-v0.120.0]] · Context Window
- [[Changes/Codex CLI/2026-04-11-2-interface-experience-changes-in-rust-v0-120-0|2 Interface Experience changes in rust-v0.120.0]] · Interface Experience
- [[Changes/Codex CLI/2026-04-11-4-apps-and-integrations-changes-in-rust-v0-120-0|4 Apps and Integrations changes in rust-v0.120.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-04-11-4-agent-mode-changes-in-rust-v0-120-0|4 Agent Mode changes in rust-v0.120.0]] · Agent Mode
- [[Changes/Codex CLI/2026-04-11-sessionstart-hooks-can-distinguish-sessions-created-by-clear-from-fresh-startup|SessionStart hooks can distinguish sessions created by /clear from fresh startup…]] · Projects and Workspaces
- [[Changes/Codex CLI/2026-04-11-2-search-and-browsing-changes-in-rust-v0-120-0|2 Search and Browsing changes in rust-v0.120.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-04-11-23-other-changes-in-rust-v0-120-0|23 other changes in rust-v0.120.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-04-10 · Codex CLI · [[Changes/Codex CLI/2026-04-10-8-safety-and-privacy-changes-in-rust-v0-119-0|8 Safety and Privacy changes in rust-v0.119.0]]
- Later: 2026-04-13 · Claude Code · [[Changes/Claude Code/2026-04-13-fixed-bash-tool-suggesting-acceptedits-permission-mode-when-exiting-plan-mode-wo|Fixed Bash tool suggesting acceptEdits permission mode when exiting plan mode…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-04-11-c32011&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-04-11-4-safety-and-privacy-changes-in-rust-v0-120-0.md%0ACard%20ID%3A%20codex-cli-2026-04-11-c32011%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.120.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->