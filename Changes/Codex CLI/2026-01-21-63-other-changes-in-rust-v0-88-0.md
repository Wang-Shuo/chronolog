---
card_id: codex-cli-2026-01-21-63213a
date: '2026-01-21'
description: 'Codex CLI · 2026-01-21 · Other changes: 63 changes in 0.88.0 — Added
  device-code auth as a standalone fallback in headless environments. (#9333)'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 22e9f778d5789f5731cc1dac4002d134f47edac5879c2c8421bea909d25bf927
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-01-21-63213a
  comparison: ''
  date: '2026-01-21'
  description: 'Codex CLI — 0.88.0: 63 other changes'
  evidence:
  - quote: Added device-code auth as a standalone fallback in headless environments.
      (#9333)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: 'Load configs from trusted folders only and fix symlinked `config.toml`
      resolution. (#9533, #9445)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: Prevented interrupted turns from repeating. (#9043)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: 'Upgraded to Rust 1.92 and refreshed core Rust dependencies. (#8860, #9465,
      #9466, #9467, #9468, #9469)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9373 fix: flaky tests @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9333 [device-auth] Add device code auth as a standalone option when headless
      environment is detected. @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9352 Made `codex exec resume --last` consistent with `codex resume --last`
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9324 add codex cloud list @nornagon-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9332 Turn-state sticky routing per turn @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9364 feat: tool call duration metric @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#8860 chore: upgrade to Rust 1.92.0 @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9247 feat(app-server, core): return threads by created_at or updated_at
      @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9330 feat: show forked from session id in /status @apanasenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9328 Support enable/disable skill via config/api. @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9400 fix(codex-api): treat invalid_prompt as non-retryable @fouad-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9401 Defer backtrack trim until rollback confirms @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9414 fix unified_exec::tests::unified_exec_timeouts to use a more unique
      match value @ahornby'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9422 chore(core) Create instructions module @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9423 chore(instructions) Remove unread SessionMeta.instructions field
      @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9445 Fixed symlink support for config.toml @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9466 chore(deps): bump log from 0.4.28 to 0.4.29 in /codex-rs @dependabot'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9467 chore(deps): bump tokio from 1.48.0 to 1.49.0 in /codex-rs @dependabot'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9468 chore(deps): bump arc-swap from 1.7.1 to 1.8.0 in /codex-rs @dependabot'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9469 chore(deps): bump ctor from 0.5.0 to 0.6.3 in /codex-rs @dependabot'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9465 chore(deps): bump chrono from 0.4.42 to 0.4.43 in /codex-rs @dependabot'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9382 feat: timer total turn metrics @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9478 feat: close all threads in `/new` @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9477 feat: detach non-tty childs @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9479 prompt 3 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9387 Fix invalid input error on Azure endpoint @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9487 chore: warning metric @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9472 Feat: request user input tool @shijie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9496 chore: fix beta VS experimental @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9495 Feat: plan mode prompt update @shijie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9451 tui: avoid Esc interrupt when skill popup active @prateek-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9497 Migrate tui to use UserTurn @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9427 fix(core) Preserve base_instructions in SessionMeta @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9393 Persist text elements through TUI input and history @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9407 fix(tui) fix user message light mode background @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9525 chore: collab in experimental @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9529 feat: record timer with additional tags @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9533 Only load config from trusted folders @gt-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9409 feat: support proxy for ws connection @apanasenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9193 fix: `writable_roots` doesn''t recognize home directory symbol in
      non-windows OS @tiffanycitra'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9509 Fixed config merging issue with profiles @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9043 fix: prevent repeating interrupted turns @swordfish444'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9553 fix(core): don''t update the file''s mtime on resume @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9552 lookup system SIDs instead of hardcoding English strings. @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9545 Add total (non-partial) TextElement placeholder accessors @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9162 Improve UI spacing for queued messages @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9558 queue only when task is working @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9568 Show session header before configuration @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9518 Prompt Expansion: Preserve Text Elements @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9560 Reject ask user question tool in Execute and Custom @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9575 feat: add skill injected counter metric @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9578 Feature to auto-enable websockets transport @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9587 fix CI by running pnpm @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9586 don''t ask for approval for `just fix` @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9585 Add request-user-input overlay @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9596 fix going up and down on questions after writing notes @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9483 feat: max threads config @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9594 Added "codex." prefix to "conversation.turn.count" metric name @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9551 nit: better collab tui @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 63-other-changes-in-rust-v0-88-0
  source_release: codex-cli-2026-01-21-rust-v0-88-0-github-278754265-4d0aa1b4
  source_type: github_releases
  theme: uncategorized
  title: 63 other changes in rust-v0.88.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-01-21-rust-v0-88-0-github-278754265-4d0aa1b4|codex-cli-2026-01-21-rust-v0-88-0-github-278754265-4d0aa1b4]]'
source_type: github_releases
theme: uncategorized
title: 63 other changes in rust-v0.88.0
type: change
---

<!-- chronolog:begin region="header" -->
# 63 other changes in rust-v0.88.0

**Codex CLI** · 2026-01-21 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.88.0) · from [[Releases/Codex CLI/codex-cli-2026-01-21-rust-v0-88-0-github-278754265-4d0aa1b4|0.88.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added device-code auth as a standalone fallback in headless environments. (#9333)

> Load configs from trusted folders only and fix symlinked `config.toml` resolution. (#9533, #9445)

> Prevented interrupted turns from repeating. (#9043)

> Upgraded to Rust 1.92 and refreshed core Rust dependencies. (#8860, #9465, #9466, #9467, #9468, #9469)

> #9373 fix: flaky tests @jif-oai

> #9333 [device-auth] Add device code auth as a standalone option when headless environment is detected. @mzeng-openai

> #9352 Made `codex exec resume --last` consistent with `codex resume --last` @etraut-openai

> #9324 add codex cloud list @nornagon-openai

> #9332 Turn-state sticky routing per turn @aibrahim-oai

> #9364 feat: tool call duration metric @jif-oai

> #8860 chore: upgrade to Rust 1.92.0 @viyatb-oai

> #9247 feat(app-server, core): return threads by created_at or updated_at @owenlin0

> #9330 feat: show forked from session id in /status @apanasenko-oai

> #9328 Support enable/disable skill via config/api. @xl-openai

> #9400 fix(codex-api): treat invalid_prompt as non-retryable @fouad-openai

> #9401 Defer backtrack trim until rollback confirms @aibrahim-oai

> #9414 fix unified_exec::tests::unified_exec_timeouts to use a more unique match value @ahornby

> #9422 chore(core) Create instructions module @dylan-hurd-oai

> #9423 chore(instructions) Remove unread SessionMeta.instructions field @dylan-hurd-oai

> #9445 Fixed symlink support for config.toml @etraut-openai

> #9466 chore(deps): bump log from 0.4.28 to 0.4.29 in /codex-rs @dependabot

> #9467 chore(deps): bump tokio from 1.48.0 to 1.49.0 in /codex-rs @dependabot

> #9468 chore(deps): bump arc-swap from 1.7.1 to 1.8.0 in /codex-rs @dependabot

> #9469 chore(deps): bump ctor from 0.5.0 to 0.6.3 in /codex-rs @dependabot

> #9465 chore(deps): bump chrono from 0.4.42 to 0.4.43 in /codex-rs @dependabot

> #9382 feat: timer total turn metrics @jif-oai

> #9478 feat: close all threads in `/new` @jif-oai

> #9477 feat: detach non-tty childs @jif-oai

> #9479 prompt 3 @jif-oai

> #9387 Fix invalid input error on Azure endpoint @etraut-openai

> #9487 chore: warning metric @jif-oai

> #9472 Feat: request user input tool @shijie-oai

> #9496 chore: fix beta VS experimental @jif-oai

> #9495 Feat: plan mode prompt update @shijie-oai

> #9451 tui: avoid Esc interrupt when skill popup active @prateek-oai

> #9497 Migrate tui to use UserTurn @aibrahim-oai

> #9427 fix(core) Preserve base_instructions in SessionMeta @dylan-hurd-oai

> #9393 Persist text elements through TUI input and history @charley-oai

> #9407 fix(tui) fix user message light mode background @dylan-hurd-oai

> #9525 chore: collab in experimental @jif-oai

> #9529 feat: record timer with additional tags @jif-oai

> #9533 Only load config from trusted folders @gt-oai

> #9409 feat: support proxy for ws connection @apanasenko-oai

> #9193 fix: `writable_roots` doesn't recognize home directory symbol in non-windows OS @tiffanycitra

> #9509 Fixed config merging issue with profiles @etraut-openai

> #9043 fix: prevent repeating interrupted turns @swordfish444

> #9553 fix(core): don't update the file's mtime on resume @owenlin0

> #9552 lookup system SIDs instead of hardcoding English strings. @iceweasel-oai

> #9545 Add total (non-partial) TextElement placeholder accessors @charley-oai

> #9162 Improve UI spacing for queued messages @charley-oai

> #9558 queue only when task is working @aibrahim-oai

> #9568 Show session header before configuration @aibrahim-oai

> #9518 Prompt Expansion: Preserve Text Elements @charley-oai

> #9560 Reject ask user question tool in Execute and Custom @charley-oai

> #9575 feat: add skill injected counter metric @alexsong-oai

> #9578 Feature to auto-enable websockets transport @pakrym-oai

> #9587 fix CI by running pnpm @aibrahim-oai

> #9586 don't ask for approval for `just fix` @aibrahim-oai

> #9585 Add request-user-input overlay @aibrahim-oai

> #9596 fix going up and down on questions after writing notes @aibrahim-oai

> #9483 feat: max threads config @jif-oai

> #9594 Added "codex." prefix to "conversation.turn.count" metric name @etraut-openai

> #9551 nit: better collab tui @jif-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.88.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-01-21-3-apps-and-integrations-changes-in-rust-v0-88-0|3 Apps and Integrations changes in rust-v0.88.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-01-21-8590-fix-core-require-approval-for-force-delete-on-windows-hdcodedev|♯8590 fix(core): require approval for force delete on Windows @hdcodedev]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-01-21-3-safety-and-privacy-changes-in-rust-v0-88-0|3 Safety and Privacy changes in rust-v0.88.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-01-21-9459-feat-personality-introduce-model-personality-config-dylan-hurd-oai|♯9459 feat(personality) introduce model_personality config @dylan-hurd-oai]] · Memory and Personalization
- [[Changes/Codex CLI/2026-01-21-9543-fix-memory-leak-issue-jif-oai|♯9543 fix: memory leak issue @jif-oai]] · Reliability and Performance
- [[Changes/Codex CLI/2026-01-21-9-collaboration-changes-in-rust-v0-88-0|9 Collaboration changes in rust-v0.88.0]] · Collaboration
- [[Changes/Codex CLI/2026-01-21-2-agent-mode-changes-in-rust-v0-88-0|2 Agent Mode changes in rust-v0.88.0]] · Agent Mode
- [[Changes/Codex CLI/2026-01-21-5-model-support-changes-in-rust-v0-88-0|5 Model Support changes in rust-v0.88.0]] · Model Support
- [[Changes/Codex CLI/2026-01-21-3-interface-experience-changes-in-rust-v0-88-0|3 Interface Experience changes in rust-v0.88.0]] · Interface Experience
- [[Changes/Codex CLI/2026-01-21-9-developer-workflow-changes-in-rust-v0-88-0|9 Developer Workflow changes in rust-v0.88.0]] · Developer Workflow
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-01-21-63213a&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-01-21-63-other-changes-in-rust-v0-88-0.md%0ACard%20ID%3A%20codex-cli-2026-01-21-63213a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.88.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->