---
card_id: codex-cli-2025-10-23-4ebece
date: '2025-10-23'
description: 'Codex CLI · 2025-10-23 · Other changes: 45 changes in 0.48.0 — `--add-dir`
  to add an additional working directory.'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 696a7208ab445567c06b6610aa19d48412ada904bdc8433955bc8f9e1876e174
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2025-10-23-4ebece
  comparison: ''
  date: '2025-10-23'
  description: 'Codex CLI — 0.48.0: 45 other changes'
  evidence:
  - quote: '`--add-dir` to add an additional working directory.'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: stdio servers can specify a `cwd`
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: All servers can specify `enabled_tools` or `disabled_tools`
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: Improved startup error messages
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: Move rust analyzer target dir by @pakrym-oai in https://github.com/openai/codex/pull/5328
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: Create independent TurnContexts by @pakrym-oai in https://github.com/openai/codex/pull/5308
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: 'feat: add --add-dir flag for extra writable roots by @tibo-openai in https://github.com/openai/codex/pull/5335'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: 'docs: improve overall documentation by @tibo-openai in https://github.com/openai/codex/pull/5354'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: 'feat: experimental `codex stdio-to-uds` subcommand by @bolinfest in https://github.com/openai/codex/pull/5350'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: Update Homebrew install instructions to use cask by @shijie-oai in https://github.com/openai/codex/pull/5377
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: Always enable plan tool in exec by @pakrym-oai in https://github.com/openai/codex/pull/5380
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: Generate JSON schema for app-server protocol by @rasmusrygaard in https://github.com/openai/codex/pull/5063
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: Use int timestamps for rate limit reset_at by @owenlin0 in https://github.com/openai/codex/pull/5383
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: 'chore: rework tools execution workflow by @jif-oai in https://github.com/openai/codex/pull/5278'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: Add ItemStarted/ItemCompleted events for UserInputItem by @pakrym-oai in
      https://github.com/openai/codex/pull/5306
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: '[app-server] read rate limits API by @owenlin0 in https://github.com/openai/codex/pull/5302'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: Reduce symbol size for tests by @pakrym-oai in https://github.com/openai/codex/pull/5389
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: 'docs: update advanced guide details by @tibo-openai in https://github.com/openai/codex/pull/5395'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: 'docs: clarify responses proxy metadata by @tibo-openai in https://github.com/openai/codex/pull/5406'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: 'docs: clarify prompt metadata behavior by @tibo-openai in https://github.com/openai/codex/pull/5403'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: 'docs: remove stale contribution reference by @tibo-openai in https://github.com/openai/codex/pull/5400'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: 'docs: correct getting-started behaviors by @tibo-openai in https://github.com/openai/codex/pull/5407'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: 'feat: include cwd in notify payload by @tibo-openai in https://github.com/openai/codex/pull/5415'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: Pass TurnContext around instead of sub_id by @pakrym-oai in https://github.com/openai/codex/pull/5421
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: 'chore: drop env var flag by @jif-oai in https://github.com/openai/codex/pull/5462'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: Enable plan tool by default by @pakrym-oai in https://github.com/openai/codex/pull/5384
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: 'feat: emit events for unified_exec by @jif-oai in https://github.com/openai/codex/pull/5448'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: Add a baseline test for resume initial messages by @pakrym-oai in https://github.com/openai/codex/pull/5466
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: '[otel] init otel for app-server by @apanasenko-oai in https://github.com/openai/codex/pull/5469'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: Log HTTP Version by @pakrym-oai in https://github.com/openai/codex/pull/5475
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: 'feat: add text cleared with ctrl+c to the history so it can be recovered
      with up arrow by @JaviSoto in https://github.com/openai/codex/pull/5470'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: 'chore: align unified_exec by @jif-oai in https://github.com/openai/codex/pull/5442'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: 'feat: local tokenizer by @jif-oai in https://github.com/openai/codex/pull/5508'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: 'chore: drop approve all by @jif-oai in https://github.com/openai/codex/pull/5503'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: Add new thread items and rewire event parsing to use them by @pakrym-oai
      in https://github.com/openai/codex/pull/5418
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: 'chore: clean spec tests by @jif-oai in https://github.com/openai/codex/pull/5517'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: Move changing turn input functionalities to `ConversationHistory` by @aibrahim-oai
      in https://github.com/openai/codex/pull/5473
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: '[app-server] send account/rateLimits/updated notifications by @owenlin0
      in https://github.com/openai/codex/pull/5477'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: '[app-server] add new account method API stubs by @owenlin0 in https://github.com/openai/codex/pull/5527'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: 'chore: clean `handle_container_exec_with_params` by @jif-oai in https://github.com/openai/codex/pull/5516'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: 'tui: show aggregated output in display by @nornagon-openai in https://github.com/openai/codex/pull/5539'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: Handle cancelling/aborting while processing a turn by @aibrahim-oai in
      https://github.com/openai/codex/pull/5543
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: 'chore: testing on apply_path by @jif-oai in https://github.com/openai/codex/pull/5557'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: 'feat: use actual tokenizer for unified_exec truncation by @jif-oai in
      https://github.com/openai/codex/pull/5514'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: 'feat: end events on unified exec by @jif-oai in https://github.com/openai/codex/pull/5551'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 45-other-changes-in-rust-v0-48-0
  source_release: codex-cli-2025-10-23-rust-v0-48-0-github-256860123-ffacccba
  source_type: github_releases
  theme: uncategorized
  title: 45 other changes in rust-v0.48.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2025-10-23-rust-v0-48-0-github-256860123-ffacccba|codex-cli-2025-10-23-rust-v0-48-0-github-256860123-ffacccba]]'
source_type: github_releases
theme: uncategorized
title: 45 other changes in rust-v0.48.0
type: change
---

<!-- chronolog:begin region="header" -->
# 45 other changes in rust-v0.48.0

**Codex CLI** · 2025-10-23 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.48.0) · from [[Releases/Codex CLI/codex-cli-2025-10-23-rust-v0-48-0-github-256860123-ffacccba|0.48.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> `--add-dir` to add an additional working directory.

> stdio servers can specify a `cwd`

> All servers can specify `enabled_tools` or `disabled_tools`

> Improved startup error messages

> Move rust analyzer target dir by @pakrym-oai in https://github.com/openai/codex/pull/5328

> Create independent TurnContexts by @pakrym-oai in https://github.com/openai/codex/pull/5308

> feat: add --add-dir flag for extra writable roots by @tibo-openai in https://github.com/openai/codex/pull/5335

> docs: improve overall documentation by @tibo-openai in https://github.com/openai/codex/pull/5354

> feat: experimental `codex stdio-to-uds` subcommand by @bolinfest in https://github.com/openai/codex/pull/5350

> Update Homebrew install instructions to use cask by @shijie-oai in https://github.com/openai/codex/pull/5377

> Always enable plan tool in exec by @pakrym-oai in https://github.com/openai/codex/pull/5380

> Generate JSON schema for app-server protocol by @rasmusrygaard in https://github.com/openai/codex/pull/5063

> Use int timestamps for rate limit reset_at by @owenlin0 in https://github.com/openai/codex/pull/5383

> chore: rework tools execution workflow by @jif-oai in https://github.com/openai/codex/pull/5278

> Add ItemStarted/ItemCompleted events for UserInputItem by @pakrym-oai in https://github.com/openai/codex/pull/5306

> [app-server] read rate limits API by @owenlin0 in https://github.com/openai/codex/pull/5302

> Reduce symbol size for tests by @pakrym-oai in https://github.com/openai/codex/pull/5389

> docs: update advanced guide details by @tibo-openai in https://github.com/openai/codex/pull/5395

> docs: clarify responses proxy metadata by @tibo-openai in https://github.com/openai/codex/pull/5406

> docs: clarify prompt metadata behavior by @tibo-openai in https://github.com/openai/codex/pull/5403

> docs: remove stale contribution reference by @tibo-openai in https://github.com/openai/codex/pull/5400

> docs: correct getting-started behaviors by @tibo-openai in https://github.com/openai/codex/pull/5407

> feat: include cwd in notify payload by @tibo-openai in https://github.com/openai/codex/pull/5415

> Pass TurnContext around instead of sub_id by @pakrym-oai in https://github.com/openai/codex/pull/5421

> chore: drop env var flag by @jif-oai in https://github.com/openai/codex/pull/5462

> Enable plan tool by default by @pakrym-oai in https://github.com/openai/codex/pull/5384

> feat: emit events for unified_exec by @jif-oai in https://github.com/openai/codex/pull/5448

> Add a baseline test for resume initial messages by @pakrym-oai in https://github.com/openai/codex/pull/5466

> [otel] init otel for app-server by @apanasenko-oai in https://github.com/openai/codex/pull/5469

> Log HTTP Version by @pakrym-oai in https://github.com/openai/codex/pull/5475

> feat: add text cleared with ctrl+c to the history so it can be recovered with up arrow by @JaviSoto in https://github.com/openai/codex/pull/5470

> chore: align unified_exec by @jif-oai in https://github.com/openai/codex/pull/5442

> feat: local tokenizer by @jif-oai in https://github.com/openai/codex/pull/5508

> chore: drop approve all by @jif-oai in https://github.com/openai/codex/pull/5503

> Add new thread items and rewire event parsing to use them by @pakrym-oai in https://github.com/openai/codex/pull/5418

> chore: clean spec tests by @jif-oai in https://github.com/openai/codex/pull/5517

> Move changing turn input functionalities to `ConversationHistory` by @aibrahim-oai in https://github.com/openai/codex/pull/5473

> [app-server] send account/rateLimits/updated notifications by @owenlin0 in https://github.com/openai/codex/pull/5477

> [app-server] add new account method API stubs by @owenlin0 in https://github.com/openai/codex/pull/5527

> chore: clean `handle_container_exec_with_params` by @jif-oai in https://github.com/openai/codex/pull/5516

> tui: show aggregated output in display by @nornagon-openai in https://github.com/openai/codex/pull/5539

> Handle cancelling/aborting while processing a turn by @aibrahim-oai in https://github.com/openai/codex/pull/5543

> chore: testing on apply_path by @jif-oai in https://github.com/openai/codex/pull/5557

> feat: use actual tokenizer for unified_exec truncation by @jif-oai in https://github.com/openai/codex/pull/5514

> feat: end events on unified exec by @jif-oai in https://github.com/openai/codex/pull/5551

Source: https://github.com/openai/codex/releases/tag/rust-v0.48.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2025-10-23-tui-drop-citation-rendering-by-nornagon-openai-in-https-github-com-openai-codex|tui: drop citation rendering]] · Interface Experience
- [[Changes/Codex CLI/2025-10-23-3-account-and-access-changes-in-rust-v0-48-0|3 Account and Access changes in rust-v0.48.0]] · Account and Access
- [[Changes/Codex CLI/2025-10-23-2-agent-mode-changes-in-rust-v0-48-0|2 Agent Mode changes in rust-v0.48.0]] · Agent Mode
- [[Changes/Codex CLI/2025-10-23-chore-ci-speed-up-macos-builds-by-using-larger-runner-by-javisoto-in-https-githu|chore(ci): Speed up macOS builds by using larger runner]] · Reliability and Performance
- [[Changes/Codex CLI/2025-10-23-auto-compact-at-90-by-aibrahim-oai-in-https-github-com-openai-codex-pull-5292|Auto compact at ~90%]] · Context Window
- [[Changes/Codex CLI/2025-10-23-docs-document-exec-json-events-by-tibo-openai-in-https-github-com-openai-codex-p|docs: document exec json events]] · Files and Data
- [[Changes/Codex CLI/2025-10-23-2-safety-and-privacy-changes-in-rust-v0-48-0|2 Safety and Privacy changes in rust-v0.48.0]] · Safety and Privacy
- [[Changes/Codex CLI/2025-10-23-11-apps-and-integrations-changes-in-rust-v0-48-0|11 Apps and Integrations changes in rust-v0.48.0]] · Apps and Integrations
- [[Changes/Codex CLI/2025-10-23-3-model-support-changes-in-rust-v0-48-0|3 Model Support changes in rust-v0.48.0]] · Model Support
- [[Changes/Codex CLI/2025-10-23-4-developer-workflow-changes-in-rust-v0-48-0|4 Developer Workflow changes in rust-v0.48.0]] · Developer Workflow
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2025-10-23-4ebece&body=Card%3A%20Changes%2FCodex%20CLI%2F2025-10-23-45-other-changes-in-rust-v0-48-0.md%0ACard%20ID%3A%20codex-cli-2025-10-23-4ebece%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.48.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->