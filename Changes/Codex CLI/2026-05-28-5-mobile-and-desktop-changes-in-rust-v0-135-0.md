---
card_id: codex-cli-2026-05-28-99890c
date: '2026-05-28'
description: 'Codex CLI · 2026-05-28 · Mobile and Desktop: 5 changes in 0.135.0 —
  Packaged Codex builds can discover and use the bundled patched zsh helper across
  supported…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-11-11-command-r-to-insert-a-speaker-label-ctrl-r-on-windows|command
    + R to insert a speaker label (ctrl + R on Windows)]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2755
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: mobile-desktop
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2f11a2a3b7472f3932549ab3eb2ce72e6c0f6302bfb5980c03f8af177dee266c
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-05-28-99890c
  comparison: ''
  date: '2026-05-28'
  description: 'Codex CLI — 0.135.0: 5 Mobile and Desktop changes'
  evidence:
  - quote: 'Packaged Codex builds can discover and use the bundled patched zsh helper
      across supported macOS and Linux targets. (#23756, #24171)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: 'TUI output is more stable on macOS and Zellij, avoiding stderr/composer
      corruption and raw-output overlap. (#24459, #24479, #24593)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24171 package: add x64 macOS codex-zsh artifact @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24459 fix(tui): prevent macos stderr from corrupting composer @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24479 fix(process-hardening): preserve macos malloc diagnostics @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 5-mobile-and-desktop-changes-in-rust-v0-135-0
  source_release: codex-cli-2026-05-28-rust-v0-135-0-github-331012967-2f52956b
  source_type: github_releases
  theme: mobile-desktop
  title: 5 Mobile and Desktop changes in rust-v0.135.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-05-26-2-mobile-and-desktop-changes-in-rust-v0-134-0|2
  Mobile and Desktop changes in rust-v0.134.0]]'
- '[[Changes/Gemini CLI/2026-05-27-auto-detect-pnpm-global-installation-path-for-macos-and-windows-by-tisonkun-in-h|Auto
  detect pnpm global installation path for macOS and Windows]]'
- '[[Changes/OpenCode/2026-05-27-6-mobile-and-desktop-changes-in-v1-15-11|6 Mobile
  and Desktop changes in v1.15.11]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-05-28-rust-v0-135-0-github-331012967-2f52956b|codex-cli-2026-05-28-rust-v0-135-0-github-331012967-2f52956b]]'
source_type: github_releases
theme: mobile-desktop
title: 5 Mobile and Desktop changes in rust-v0.135.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Mobile and Desktop changes in rust-v0.135.0

**Codex CLI** · 2026-05-28 · [[Themes/mobile-desktop|Mobile and Desktop]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.135.0) · from [[Releases/Codex CLI/codex-cli-2026-05-28-rust-v0-135-0-github-331012967-2f52956b|0.135.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Packaged Codex builds can discover and use the bundled patched zsh helper across supported macOS and Linux targets. (#23756, #24171)

> TUI output is more stable on macOS and Zellij, avoiding stderr/composer corruption and raw-output overlap. (#24459, #24479, #24593)

> #24171 package: add x64 macOS codex-zsh artifact @bolinfest

> #24459 fix(tui): prevent macos stderr from corrupting composer @fcoury-oai

> #24479 fix(process-hardening): preserve macos malloc diagnostics @fcoury-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.135.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-05-28-4-context-window-changes-in-rust-v0-135-0|4 Context Window changes in rust-v0.135.0]] · Context Window
- [[Changes/Codex CLI/2026-05-28-14-apps-and-integrations-changes-in-rust-v0-135-0|14 Apps and Integrations changes in rust-v0.135.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-05-28-24714-fix-auto-review-skip-legacy-notify-for-auto-review-threads-dylan-hurd-oai|♯24714 fix(auto-review) skip legacy notify for auto review threads @dylan-hurd-oai]] · Agent Mode
- [[Changes/Codex CLI/2026-05-28-8-memory-and-personalization-changes-in-rust-v0-135-0|8 Memory and Personalization changes in rust-v0.135.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-05-28-slash-command-completion-now-preserves-existing-draft-text-for-commands-that-acc|Slash-command completion now preserves existing draft text for commands that accept…]] · Editor Experience
- [[Changes/Codex CLI/2026-05-28-7-safety-and-privacy-changes-in-rust-v0-135-0|7 Safety and Privacy changes in rust-v0.135.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-05-28-codex-doctor-now-reports-richer-environment-git-terminal-app-server-and-thread-i|codex doctor now reports richer environment, Git, terminal, app-server, and thread…]] · Developer Workflow
- [[Changes/Codex CLI/2026-05-28-63-other-changes-in-rust-v0-135-0|63 other changes in rust-v0.135.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Mobile and Desktop

- Earlier: 2026-05-27 · OpenCode · [[Changes/OpenCode/2026-05-27-6-mobile-and-desktop-changes-in-v1-15-11|6 Mobile and Desktop changes in v1.15.11]]
- Later: 2026-05-28 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-05-28-clipboard-correctly-copies-cjk-and-supplementary-plane-unicode-characters-on-win|Clipboard correctly copies CJK and supplementary-plane Unicode characters on Windows]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-11-11 · Descript · [[Changes/Descript/2018-11-11-command-r-to-insert-a-speaker-label-ctrl-r-on-windows|command + R to insert a speaker label (ctrl + R on Windows)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-05-28-99890c&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-05-28-5-mobile-and-desktop-changes-in-rust-v0-135-0.md%0ACard%20ID%3A%20codex-cli-2026-05-28-99890c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.135.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->