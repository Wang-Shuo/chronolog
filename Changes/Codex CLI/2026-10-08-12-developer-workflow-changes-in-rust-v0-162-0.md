---
card_id: codex-cli-2026-10-08-7ea867
date: '2026-10-08'
description: 'Codex CLI · 2026-10-08 · Developer Workflow: 12 changes in 0.162.0 —
  Add tools for creating and listing managed Git worktrees from trusted local projects
  when…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2949
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 5fb51bb2c0600bdcc78f801dbc8db2e883152a61d518390d1156ea89a8c67479
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-10-08-7ea867
  comparison: ''
  date: '2026-10-08'
  description: 'Codex CLI — 0.162.0: 12 Developer Workflow changes'
  evidence:
  - quote: Add tools for creating and listing managed Git worktrees from trusted local
      projects when the worktrees feature is enabled. (#50148)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50148 Add managed worktree tools to the TUI @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50375 Use printable ASCII terminal titles under GNU Screen @imac-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50402 Consolidate command execution output into `aggregated_output` @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50416 Clarify Git worktree choices for new and forked conversations @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50427 Cap persisted command output in paginated history at 64 KiB @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50431 Preserve terminal hyperlinks in agents overview previews @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50555 Skip daemon auto-start for Windows-mounted WSL homes @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50720 Decode Windows Terminal''s mapped Shift+Enter sequence @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50786 Remember Command Center grouping across launches @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51347 Measure shell snapshot use and wait time per command @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51350 Allow larger shell snapshots when replaying from a file @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 12-developer-workflow-changes-in-rust-v0-162-0
  source_release: codex-cli-2026-10-08-rust-v0-162-0-github-407151970-b80d60db
  source_type: github_releases
  theme: developer-workflow
  title: 12 Developer Workflow changes in rust-v0.162.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-10-07-10-developer-workflow-changes-in-rust-v0-161-0|10
  Developer Workflow changes in rust-v0.161.0]]'
- '[[Changes/GitHub Copilot CLI/2026-10-07-warmed-language-servers-stay-running-across-lsp-requests-when-sandboxing-is-disa|Warmed
  language servers stay running across LSP requests when sandboxing is disabled]]'
- '[[Changes/Claude Code/2026-10-08-added-a-line-on-stderr-when-it-is-a-terminal-that-says-what-a-claude-p-run-is-wa|Added
  a line on stderr, when it is a terminal, that says what a claude -p run…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-10-08-rust-v0-162-0-github-407151970-b80d60db|codex-cli-2026-10-08-rust-v0-162-0-github-407151970-b80d60db]]'
source_type: github_releases
theme: developer-workflow
title: 12 Developer Workflow changes in rust-v0.162.0
type: change
---

<!-- chronolog:begin region="header" -->
# 12 Developer Workflow changes in rust-v0.162.0

**Codex CLI** · 2026-10-08 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.162.0) · from [[Releases/Codex CLI/codex-cli-2026-10-08-rust-v0-162-0-github-407151970-b80d60db|0.162.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Add tools for creating and listing managed Git worktrees from trusted local projects when the worktrees feature is enabled. (#50148)

> #50148 Add managed worktree tools to the TUI @bc-openai

> #50375 Use printable ASCII terminal titles under GNU Screen @imac-oai

> #50402 Consolidate command execution output into `aggregated_output` @owenlin0

> #50416 Clarify Git worktree choices for new and forked conversations @bc-openai

> #50427 Cap persisted command output in paginated history at 64 KiB @owenlin0

> #50431 Preserve terminal hyperlinks in agents overview previews @bc-openai

> #50555 Skip daemon auto-start for Windows-mounted WSL homes @etraut-openai

> #50720 Decode Windows Terminal's mapped Shift+Enter sequence @bc-openai

> #50786 Remember Command Center grouping across launches @bc-openai

> #51347 Measure shell snapshot use and wait time per command @jif-oai

> #51350 Allow larger shell snapshots when replaying from a file @jif-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.162.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-10-08-51223-remove-legacy-personality-template-metadata-rhan-oai|♯51223 Remove legacy personality template metadata @rhan-oai]] · Memory and Personalization
- [[Changes/Codex CLI/2026-10-08-3-reliability-and-performance-changes-in-rust-v0-162-0|3 Reliability and Performance changes in rust-v0.162.0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-10-08-2-voice-and-audio-changes-in-rust-v0-162-0|2 Voice and Audio changes in rust-v0.162.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-10-08-10-context-window-changes-in-rust-v0-162-0|10 Context Window changes in rust-v0.162.0]] · Context Window
- [[Changes/Codex CLI/2026-10-08-50216-use-the-shared-text-editor-for-command-center-task-renaming-bc-openai|♯50216 Use the shared text editor for command-center task renaming @bc-openai]] · Editor Experience
- [[Changes/Codex CLI/2026-10-08-13-safety-and-privacy-changes-in-rust-v0-162-0|13 Safety and Privacy changes in rust-v0.162.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-10-08-20-apps-and-integrations-changes-in-rust-v0-162-0|20 Apps and Integrations changes in rust-v0.162.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-10-08-50384-allow-opting-into-16-kib-arm64-code-pages-for-macos-signing-chess-oai|♯50384 Allow opting into 16 KiB ARM64 code pages for macOS signing @chess-oai]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-10-08-8-interface-experience-changes-in-rust-v0-162-0|8 Interface Experience changes in rust-v0.162.0]] · Interface Experience
- [[Changes/Codex CLI/2026-10-08-14-agent-mode-changes-in-rust-v0-162-0|14 Agent Mode changes in rust-v0.162.0]] · Agent Mode
- [[Changes/Codex CLI/2026-10-08-11-model-support-changes-in-rust-v0-162-0|11 Model Support changes in rust-v0.162.0]] · Model Support
- [[Changes/Codex CLI/2026-10-08-2-account-and-access-changes-in-rust-v0-162-0|2 Account and Access changes in rust-v0.162.0]] · Account and Access
- [[Changes/Codex CLI/2026-10-08-2-collaboration-changes-in-rust-v0-162-0|2 Collaboration changes in rust-v0.162.0]] · Collaboration
- [[Changes/Codex CLI/2026-10-08-137-other-changes-in-rust-v0-162-0|137 other changes in rust-v0.162.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-10-08 · Claude Code · [[Changes/Claude Code/2026-10-08-added-a-line-on-stderr-when-it-is-a-terminal-that-says-what-a-claude-p-run-is-wa|Added a line on stderr, when it is a terminal, that says what a claude -p run…]]
- Later: 2026-10-08 · OpenClaw · [[Changes/OpenClaw/2026-10-08-3-developer-workflow-changes-in-v2026-9-9|3 Developer Workflow changes in v2026.9.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-10-08-7ea867&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-10-08-12-developer-workflow-changes-in-rust-v0-162-0.md%0ACard%20ID%3A%20codex-cli-2026-10-08-7ea867%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.162.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->