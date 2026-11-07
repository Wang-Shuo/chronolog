---
card_id: codex-cli-2026-03-10-876d59
date: '2026-03-10'
description: 'Codex CLI · 2026-03-10 · Developer Workflow: 8 changes in 0.113.0 —
  Upgraded app-server command execution with streaming stdin/stdout/stderr plus TTY/PTY…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2737
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: c21e5e2697b644cc7d47a0e3b9eebaef4f949726627951640602fba00e79ceb8
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-03-10-876d59
  comparison: ''
  date: '2026-03-10'
  description: 'Codex CLI — 0.113.0: 8 Developer Workflow changes'
  evidence:
  - quote: 'Upgraded app-server command execution with streaming stdin/stdout/stderr
      plus TTY/PTY support, and wired `exec` to the new in-process app server path.
      (#13640, #14005)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13770 fix(app-server): fix turn_start_shell_zsh_fork_executes_command_v2
      flake @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13695 utils/pty: add streaming spawn and terminal sizing primitives @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13640 app-server: Add streaming and tty/pty capabilities to `command/exec`
      @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13804 fix: avoid invoking git before project trust is established @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13877 Stabilize shell serialization tests @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13878 Serialize shell snapshot stdin test @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#14114 fix(ci) Faster shell_command::unicode_output test @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 8-developer-workflow-changes-in-rust-v0-113-0
  source_release: codex-cli-2026-03-10-rust-v0-113-0-github-294999501-e594ccb6
  source_type: github_releases
  theme: developer-workflow
  title: 8 Developer Workflow changes in rust-v0.113.0
  type: change
related_changes:
- '[[Changes/OpenCode/2026-03-09-terminal-pass-missing-auth-headers-in-run-attach|Terminal
  Pass missing auth headers in run --attach]]'
- '[[Changes/Windsurf/2026-03-09-cascade|Cascade]]'
- '[[Changes/Claude Code/2026-03-10-3-developer-workflow-changes-in-v2-1-72|3 Developer
  Workflow changes in v2.1.72]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-03-10-rust-v0-113-0-github-294999501-e594ccb6|codex-cli-2026-03-10-rust-v0-113-0-github-294999501-e594ccb6]]'
source_type: github_releases
theme: developer-workflow
title: 8 Developer Workflow changes in rust-v0.113.0
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Developer Workflow changes in rust-v0.113.0

**Codex CLI** · 2026-03-10 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.113.0) · from [[Releases/Codex CLI/codex-cli-2026-03-10-rust-v0-113-0-github-294999501-e594ccb6|0.113.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Upgraded app-server command execution with streaming stdin/stdout/stderr plus TTY/PTY support, and wired `exec` to the new in-process app server path. (#13640, #14005)

> #13770 fix(app-server): fix turn_start_shell_zsh_fork_executes_command_v2 flake @owenlin0

> #13695 utils/pty: add streaming spawn and terminal sizing primitives @euroelessar

> #13640 app-server: Add streaming and tty/pty capabilities to `command/exec` @euroelessar

> #13804 fix: avoid invoking git before project trust is established @viyatb-oai

> #13877 Stabilize shell serialization tests @aibrahim-oai

> #13878 Serialize shell snapshot stdin test @aibrahim-oai

> #14114 fix(ci) Faster shell_command::unicode_output test @dylan-hurd-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.113.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-03-10-10-safety-and-privacy-changes-in-rust-v0-113-0|10 Safety and Privacy changes in rust-v0.113.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-03-10-2-automation-and-scheduling-changes-in-rust-v0-113-0|2 Automation and Scheduling changes in rust-v0.113.0]] · Automation and Scheduling
- [[Changes/Codex CLI/2026-03-10-13734-feat-prune-old-memories-in-db-jif-oai|♯13734 feat: prune old memories in DB @jif-oai]] · Memory and Personalization
- [[Changes/Codex CLI/2026-03-10-4-interface-experience-changes-in-rust-v0-113-0|4 Interface Experience changes in rust-v0.113.0]] · Interface Experience
- [[Changes/Codex CLI/2026-03-10-11-apps-and-integrations-changes-in-rust-v0-113-0|11 Apps and Integrations changes in rust-v0.113.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-03-10-14117-feat-otel-centralize-otel-metric-names-and-shared-tag-builders-owenlin0|♯14117 feat(otel): Centralize OTEL metric names and shared tag builders @owenlin0]] · Collaboration
- [[Changes/Codex CLI/2026-03-10-image-generation-now-saves-output-files-into-the-current-working-directory-13607|Image generation now saves output files into the current working directory]] · Image Generation
- [[Changes/Codex CLI/2026-03-10-14123-pass-on-save-info-to-model-ui-tweaks-won-openai|♯14123 pass on save info to model + ui tweaks @won-openai]] · Model Support
- [[Changes/Codex CLI/2026-03-10-2-search-and-browsing-changes-in-rust-v0-113-0|2 Search and Browsing changes in rust-v0.113.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-03-10-2-account-and-access-changes-in-rust-v0-113-0|2 Account and Access changes in rust-v0.113.0]] · Account and Access
- [[Changes/Codex CLI/2026-03-10-4-context-window-changes-in-rust-v0-113-0|4 Context Window changes in rust-v0.113.0]] · Context Window
- [[Changes/Codex CLI/2026-03-10-70-other-changes-in-rust-v0-113-0|70 other changes in rust-v0.113.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-03-10 · Claude Code · [[Changes/Claude Code/2026-03-10-3-developer-workflow-changes-in-v2-1-72|3 Developer Workflow changes in v2.1.72]]
- Later: 2026-03-11 · Claude Code · [[Changes/Claude Code/2026-03-11-deprecated-output-style-command-use-config-instead-output-style-is-now-fixed-at|Deprecated /output-style command — use /config instead]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-03-10-876d59&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-03-10-8-developer-workflow-changes-in-rust-v0-113-0.md%0ACard%20ID%3A%20codex-cli-2026-03-10-876d59%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.113.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->