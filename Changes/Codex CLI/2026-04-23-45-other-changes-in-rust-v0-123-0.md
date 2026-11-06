---
card_id: codex-cli-2026-04-23-3da346
date: '2026-04-23'
description: 'Codex CLI · 2026-04-23 · Other changes: 45 changes in 0.123.0 — Removed
  leaked review prompts from TUI transcripts (#18659).'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2aff015136a7565425483e11ad0bed884263677e21ce0b285195b8bb0c0697a5
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-04-23-3da346
  comparison: ''
  date: '2026-04-23'
  description: 'Codex CLI — 0.123.0: 45 other changes'
  evidence:
  - quote: Removed leaked review prompts from TUI transcripts (#18659).
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: 'Documented intentional await-across-lock cases and enabled Clippy linting
      for them (#18423, #18698).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18659 chore: drop review prompt from TUI UX @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18661 feat: log client use min log level @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18260 [codex] Use background task auth for additional backend calls @adrian-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18657 fix: auth.json leak in tests @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18591 Surface parent thread status in side conversations @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18361 codex: move thread/name/set and thread/memoryModeSet into ThreadStore
      @wiltzius-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18274 protocol: canonicalize file system permissions @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18403 refactor: use semaphores for async serialization gates @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18289 Wire the PatchUpdated events through app_server @akshaynathan'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18631 Remove simple TUI legacy_core reexports @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18167 [codex] Fix high severity dependency alerts @caseysilver-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#17692 [codex-analytics] guardian review analytics schema polishing @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18597 Update realtime handoff transcript handling @guinness-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18627 Surface TUI skills refresh failures @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18714 Add experimental remote thread store config @wiltzius-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18739 fix(tui): keep /copy aligned with rollback @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18632 Use app server metadata for fork parent titles @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18112 feat: cascade thread archive @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18716 Read conversation summaries through thread store @wiltzius-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18635 Add realtime silence tool @guinness-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18254 uds: add async Unix socket crate @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18208 Add session config loader interface @rasmusrygaard'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18753 Refactor TUI app module into submodules @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18027 [6/6] Fail exec client operations after disconnect @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18761 [codex] Send realtime transcript deltas on handoff @guinness-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18581 [1/4] Add executor HTTP request protocol @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18418 refactor: narrow async lock scopes @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18795 fix(guardian) Dont hard error on feature disable @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18786 Fallback display names for TUI skill mentions @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18807 chore(app-server) linguist-generated @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18698 chore: enable await-holding clippy lints @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18413 [tool search] support namespaced deferred dynamic tools @pash-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18844 build: reduce Rust dev debuginfo @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18848 feat: baseline lib @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18846 core: make test-log a dev dependency @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18428 app-server: define device key v2 protocol @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#17836 [codex] Add tmux-aware OSC 9 notifications @caseychow-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18799 Move TUI app tests to modules they cover @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18442 Refactor app-server config loading into ConfigManager @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18813 Split DeveloperInstructions into individual fragments. @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18429 app-server: add codex-device-key crate @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18872 app-server: fix Bazel clippy in tracing tests @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18885 skip busted tests while I fix them @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 45-other-changes-in-rust-v0-123-0
  source_release: codex-cli-2026-04-23-rust-v0-123-0-github-312509536-cebe4f18
  source_type: github_releases
  theme: uncategorized
  title: 45 other changes in rust-v0.123.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-04-23-rust-v0-123-0-github-312509536-cebe4f18|codex-cli-2026-04-23-rust-v0-123-0-github-312509536-cebe4f18]]'
source_type: github_releases
theme: uncategorized
title: 45 other changes in rust-v0.123.0
type: change
---

<!-- chronolog:begin region="header" -->
# 45 other changes in rust-v0.123.0

**Codex CLI** · 2026-04-23 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.123.0) · from [[Releases/Codex CLI/codex-cli-2026-04-23-rust-v0-123-0-github-312509536-cebe4f18|0.123.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Removed leaked review prompts from TUI transcripts (#18659).

> Documented intentional await-across-lock cases and enabled Clippy linting for them (#18423, #18698).

> #18659 chore: drop review prompt from TUI UX @jif-oai

> #18661 feat: log client use min log level @jif-oai

> #18260 [codex] Use background task auth for additional backend calls @adrian-openai

> #18657 fix: auth.json leak in tests @jif-oai

> #18591 Surface parent thread status in side conversations @etraut-openai

> #18361 codex: move thread/name/set and thread/memoryModeSet into ThreadStore @wiltzius-openai

> #18274 protocol: canonicalize file system permissions @bolinfest

> #18403 refactor: use semaphores for async serialization gates @bolinfest

> #18289 Wire the PatchUpdated events through app_server @akshaynathan

> #18631 Remove simple TUI legacy_core reexports @etraut-openai

> #18167 [codex] Fix high severity dependency alerts @caseysilver-oai

> #17692 [codex-analytics] guardian review analytics schema polishing @rhan-oai

> #18597 Update realtime handoff transcript handling @guinness-oai

> #18627 Surface TUI skills refresh failures @etraut-openai

> #18714 Add experimental remote thread store config @wiltzius-openai

> #18739 fix(tui): keep /copy aligned with rollback @fcoury-oai

> #18632 Use app server metadata for fork parent titles @etraut-openai

> #18112 feat: cascade thread archive @jif-oai

> #18716 Read conversation summaries through thread store @wiltzius-openai

> #18635 Add realtime silence tool @guinness-oai

> #18254 uds: add async Unix socket crate @euroelessar

> #18208 Add session config loader interface @rasmusrygaard

> #18753 Refactor TUI app module into submodules @etraut-openai

> #18027 [6/6] Fail exec client operations after disconnect @aibrahim-oai

> #18761 [codex] Send realtime transcript deltas on handoff @guinness-oai

> #18581 [1/4] Add executor HTTP request protocol @aibrahim-oai

> #18418 refactor: narrow async lock scopes @bolinfest

> #18795 fix(guardian) Dont hard error on feature disable @dylan-hurd-oai

> #18786 Fallback display names for TUI skill mentions @canvrno-oai

> #18807 chore(app-server) linguist-generated @dylan-hurd-oai

> #18698 chore: enable await-holding clippy lints @bolinfest

> #18413 [tool search] support namespaced deferred dynamic tools @pash-openai

> #18844 build: reduce Rust dev debuginfo @bolinfest

> #18848 feat: baseline lib @jif-oai

> #18846 core: make test-log a dev dependency @bolinfest

> #18428 app-server: define device key v2 protocol @euroelessar

> #17836 [codex] Add tmux-aware OSC 9 notifications @caseychow-oai

> #18799 Move TUI app tests to modules they cover @etraut-openai

> #18442 Refactor app-server config loading into ConfigManager @pakrym-oai

> #18813 Split DeveloperInstructions into individual fragments. @pakrym-oai

> #18429 app-server: add codex-device-key crate @euroelessar

> #18872 app-server: fix Bazel clippy in tracing tests @euroelessar

> #18885 skip busted tests while I fix them @iceweasel-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.123.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-04-23-18662-feat-add-metric-to-track-the-number-of-turns-with-memory-usage-jif-oai|♯18662 feat: add metric to track the number of turns with memory usage @jif-oai]] · Reliability and Performance
- [[Changes/Codex CLI/2026-04-23-18794-organize-context-fragments-pakrym-oai|♯18794 Organize context fragments @pakrym-oai]] · Context Window
- [[Changes/Codex CLI/2026-04-23-2-collaboration-changes-in-rust-v0-123-0|2 Collaboration changes in rust-v0.123.0]] · Collaboration
- [[Changes/Codex CLI/2026-04-23-8-agent-mode-changes-in-rust-v0-123-0|8 Agent Mode changes in rust-v0.123.0]] · Agent Mode
- [[Changes/Codex CLI/2026-04-23-6-model-support-changes-in-rust-v0-123-0|6 Model Support changes in rust-v0.123.0]] · Model Support
- [[Changes/Codex CLI/2026-04-23-6-safety-and-privacy-changes-in-rust-v0-123-0|6 Safety and Privacy changes in rust-v0.123.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-04-23-18633-use-app-server-thread-names-in-tui-picker-etraut-openai|♯18633 Use app server thread names in TUI picker @etraut-openai]] · Interface Experience
- [[Changes/Codex CLI/2026-04-23-added-mcp-verbose-for-full-mcp-server-diagnostics-resources-and-resource-templat|Added /mcp verbose for full MCP server diagnostics, resources, and resource…]] · Apps and Integrations
- [[Changes/Codex CLI/2026-04-23-9-apps-and-integrations-changes-in-rust-v0-123-0|9 Apps and Integrations changes in rust-v0.123.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-04-23-18858-stabilize-debug-clear-memories-integration-test-jif-oai|♯18858 Stabilize debug clear memories integration test @jif-oai]] · Memory and Personalization
- [[Changes/Codex CLI/2026-04-23-11-developer-workflow-changes-in-rust-v0-123-0|11 Developer Workflow changes in rust-v0.123.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-04-23-18423-chore-document-intentional-await-holding-cases-bolinfest|♯18423 chore: document intentional await-holding cases @bolinfest]] · Files and Data
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-04-23-3da346&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-04-23-45-other-changes-in-rust-v0-123-0.md%0ACard%20ID%3A%20codex-cli-2026-04-23-3da346%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.123.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->