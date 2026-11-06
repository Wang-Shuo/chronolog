---
card_id: codex-cli-2026-05-28-9af73b
date: '2026-05-28'
description: 'Codex CLI · 2026-05-28 · Other changes: 63 changes in 0.135.0 — `/status`
  shows remote connection details and server version when the TUI is connected over
  a…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 96035be4612fb4892f91e0c796298662cdaea9e5497767d3708093c2f3ca70c8
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-05-28-9af73b
  comparison: ''
  date: '2026-05-28'
  description: 'Codex CLI — 0.135.0: 63 other changes'
  evidence:
  - quote: '`/status` shows remote connection details and server version when the
      TUI is connected over a remote transport. (#24420)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: 'Vim mode gained text-object editing, improved word/line-end behavior,
      and a configurable interrupt-turn binding. (#24382, #24380, #24766)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '`install.sh`/`install.ps1` supports a non-interactive installation mode
      when `CODEX_NON_INTERACTIVE=1` is set. (#21567)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: 'Markdown tables and multiline lists render more readably in the TUI, with
      better column sizing and app-style table formatting. (#24489, #24346, #24351)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: Older tmux/iTerm control-mode sessions no longer lose normal `Ctrl-C` handling
      from unsupported keyboard enhancement setup. (#24371)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: 'Resume flows now include non-interactive exec sessions when requested
      and honor cwd overrides for idle cached threads. (#24503, #24528)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: 'Clarified image-viewing tool detail behavior and removed stale TUI composer
      documentation references. (#23949, #24641)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: 'Updated Rust toolchain pins and SQLx/SQLite dependencies. (#24684, #24728)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#23756 package: include zsh fork in Codex package @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24159 code-mode: merge stored values by key @cconger'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24261 feat(doctor): add environment diagnostics @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24311 Report app-server version in codex doctor @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24314 tui: label compact rate-limit percentages @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24420 Show remote connection details in /status @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24317 Respect hook trust bypass during TUI startup @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24254 TUI config cleanup: oss_provider @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24255 TUI config cleanup: trusted projects @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24305 Add doctor thread inventory audit @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24346 fix(tui): improve markdown table column allocation @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24351 fix(tui): improve multiline markdown list readability @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24474 Log rollout writer OS errors @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24076 chore: stop consuming legacy config profiles @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24131 centralize Responses retry policy @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#23858 [wip] goal shift @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24588 fix: drop flake @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24586 Wire app-server extension event sink @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24105 [codex] Make active turn task singular @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24503 tui: include exec sessions in resume list @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24611 test: clean up apply_patch allow-session artifact @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24609 Remove reserved namespaces dedup @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#23964 Move slash input logic out of chat composer @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24615 Add goal extension telemetry parity @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24371 fix(tui): avoid modifyOtherKeys for unknown tmux formats @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24626 fix: restore goal accounting after thread resume @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#23823 standalone websearch extension @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24593 fix(tui): keep raw output above composer in zellij @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24528 Respect resume cwd overrides for idle cached threads @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24160 Add forked_from_thread_id turn metadata @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24646 make direct only allowed caller for standalone websearch @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#23949 Clarify view_image tool description @fjord-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24320 Avoid repeated marketplace upgrades for alternate layouts @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24652 [codex] remove plain image wrapper spans @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24644 Restore legacy image detail values @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24655 [codex-analytics] add grouped session id to runtime events @marksteinbrick-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24658 [codex] Remove obsolete goal continuation turn marker @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24660 fix: dont compact standalone websearch schema @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24667 fix(core): instrument stalled tool-listing handoff @apanasenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24684 Uprev Rust toolchain pins to 1.95.0 @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#21567 fix: add noninteractive install script mode @efrazer-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24690 Revert "Add Bedrock Mantle GovCloud region (#23860)" @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24628 feat: handle goal usage limits in goal extension @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24746 Fix guardian review test user input @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24744 feat: add thread idle lifecycle hook @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24380 fix(tui): complete vim word-end and line-end behavior @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24728 Bump SQLx to pick up newer bundled SQLite @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24637 fix: run standalone updates noninteractively @efrazer-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24778 make vercel webhook url an env secret @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#23950 fix: Preserve draft text when completing argument-taking slash
      commands @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24641 [codex] Remove stale composer narrative doc references @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24382 feat(tui): add vim text object bindings @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24766 feat(tui): make turn interruption keybind configurable @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24489 feat(tui): render markdown tables in app style [1 of 2] @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24713 chore: enable namespace tools for Bedrock @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 63-other-changes-in-rust-v0-135-0
  source_release: codex-cli-2026-05-28-rust-v0-135-0-github-331012967-2f52956b
  source_type: github_releases
  theme: uncategorized
  title: 63 other changes in rust-v0.135.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-05-28-rust-v0-135-0-github-331012967-2f52956b|codex-cli-2026-05-28-rust-v0-135-0-github-331012967-2f52956b]]'
source_type: github_releases
theme: uncategorized
title: 63 other changes in rust-v0.135.0
type: change
---

<!-- chronolog:begin region="header" -->
# 63 other changes in rust-v0.135.0

**Codex CLI** · 2026-05-28 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.135.0) · from [[Releases/Codex CLI/codex-cli-2026-05-28-rust-v0-135-0-github-331012967-2f52956b|0.135.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> `/status` shows remote connection details and server version when the TUI is connected over a remote transport. (#24420)

> Vim mode gained text-object editing, improved word/line-end behavior, and a configurable interrupt-turn binding. (#24382, #24380, #24766)

> `install.sh`/`install.ps1` supports a non-interactive installation mode when `CODEX_NON_INTERACTIVE=1` is set. (#21567)

> Markdown tables and multiline lists render more readably in the TUI, with better column sizing and app-style table formatting. (#24489, #24346, #24351)

> Older tmux/iTerm control-mode sessions no longer lose normal `Ctrl-C` handling from unsupported keyboard enhancement setup. (#24371)

> Resume flows now include non-interactive exec sessions when requested and honor cwd overrides for idle cached threads. (#24503, #24528)

> Clarified image-viewing tool detail behavior and removed stale TUI composer documentation references. (#23949, #24641)

> Updated Rust toolchain pins and SQLx/SQLite dependencies. (#24684, #24728)

> #23756 package: include zsh fork in Codex package @bolinfest

> #24159 code-mode: merge stored values by key @cconger

> #24261 feat(doctor): add environment diagnostics @fcoury-oai

> #24311 Report app-server version in codex doctor @etraut-openai

> #24314 tui: label compact rate-limit percentages @etraut-openai

> #24420 Show remote connection details in /status @etraut-openai

> #24317 Respect hook trust bypass during TUI startup @etraut-openai

> #24254 TUI config cleanup: oss_provider @etraut-openai

> #24255 TUI config cleanup: trusted projects @etraut-openai

> #24305 Add doctor thread inventory audit @etraut-openai

> #24346 fix(tui): improve markdown table column allocation @fcoury-oai

> #24351 fix(tui): improve multiline markdown list readability @fcoury-oai

> #24474 Log rollout writer OS errors @etraut-openai

> #24076 chore: stop consuming legacy config profiles @jif-oai

> #24131 centralize Responses retry policy @rhan-oai

> #23858 [wip] goal shift @jif-oai

> #24588 fix: drop flake @jif-oai

> #24586 Wire app-server extension event sink @jif-oai

> #24105 [codex] Make active turn task singular @pakrym-oai

> #24503 tui: include exec sessions in resume list @etraut-openai

> #24611 test: clean up apply_patch allow-session artifact @jif-oai

> #24609 Remove reserved namespaces dedup @pakrym-oai

> #23964 Move slash input logic out of chat composer @canvrno-oai

> #24615 Add goal extension telemetry parity @jif-oai

> #24371 fix(tui): avoid modifyOtherKeys for unknown tmux formats @fcoury-oai

> #24626 fix: restore goal accounting after thread resume @jif-oai

> #23823 standalone websearch extension @sayan-oai

> #24593 fix(tui): keep raw output above composer in zellij @fcoury-oai

> #24528 Respect resume cwd overrides for idle cached threads @etraut-openai

> #24160 Add forked_from_thread_id turn metadata @owenlin0

> #24646 make direct only allowed caller for standalone websearch @sayan-oai

> #23949 Clarify view_image tool description @fjord-oai

> #24320 Avoid repeated marketplace upgrades for alternate layouts @etraut-openai

> #24652 [codex] remove plain image wrapper spans @pakrym-oai

> #24644 Restore legacy image detail values @rhan-oai

> #24655 [codex-analytics] add grouped session id to runtime events @marksteinbrick-oai

> #24658 [codex] Remove obsolete goal continuation turn marker @pakrym-oai

> #24660 fix: dont compact standalone websearch schema @sayan-oai

> #24667 fix(core): instrument stalled tool-listing handoff @apanasenko-oai

> #24684 Uprev Rust toolchain pins to 1.95.0 @anp-oai

> #21567 fix: add noninteractive install script mode @efrazer-oai

> #24690 Revert "Add Bedrock Mantle GovCloud region (#23860)" @celia-oai

> #24628 feat: handle goal usage limits in goal extension @jif-oai

> #24746 Fix guardian review test user input @jif-oai

> #24744 feat: add thread idle lifecycle hook @jif-oai

> #24380 fix(tui): complete vim word-end and line-end behavior @fcoury-oai

> #24728 Bump SQLx to pick up newer bundled SQLite @jif-oai

> #24637 fix: run standalone updates noninteractively @efrazer-oai

> #24778 make vercel webhook url an env secret @sayan-oai

> #23950 fix: Preserve draft text when completing argument-taking slash commands @canvrno-oai

> #24641 [codex] Remove stale composer narrative doc references @canvrno-oai

> #24382 feat(tui): add vim text object bindings @fcoury-oai

> #24766 feat(tui): make turn interruption keybind configurable @fcoury-oai

> #24489 feat(tui): render markdown tables in app style [1 of 2] @fcoury-oai

> #24713 chore: enable namespace tools for Bedrock @celia-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.135.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-05-28-4-context-window-changes-in-rust-v0-135-0|4 Context Window changes in rust-v0.135.0]] · Context Window
- [[Changes/Codex CLI/2026-05-28-14-apps-and-integrations-changes-in-rust-v0-135-0|14 Apps and Integrations changes in rust-v0.135.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-05-28-24714-fix-auto-review-skip-legacy-notify-for-auto-review-threads-dylan-hurd-oai|♯24714 fix(auto-review) skip legacy notify for auto review threads @dylan-hurd-oai]] · Agent Mode
- [[Changes/Codex CLI/2026-05-28-8-memory-and-personalization-changes-in-rust-v0-135-0|8 Memory and Personalization changes in rust-v0.135.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-05-28-5-mobile-and-desktop-changes-in-rust-v0-135-0|5 Mobile and Desktop changes in rust-v0.135.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-05-28-slash-command-completion-now-preserves-existing-draft-text-for-commands-that-acc|Slash-command completion now preserves existing draft text for commands that accept…]] · Editor Experience
- [[Changes/Codex CLI/2026-05-28-7-safety-and-privacy-changes-in-rust-v0-135-0|7 Safety and Privacy changes in rust-v0.135.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-05-28-codex-doctor-now-reports-richer-environment-git-terminal-app-server-and-thread-i|codex doctor now reports richer environment, Git, terminal, app-server, and thread…]] · Developer Workflow
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-05-28-9af73b&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-05-28-63-other-changes-in-rust-v0-135-0.md%0ACard%20ID%3A%20codex-cli-2026-05-28-9af73b%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.135.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->