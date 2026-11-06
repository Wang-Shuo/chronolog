---
card_id: codex-cli-2026-09-01-d5112f
date: '2026-09-01'
description: 'Codex CLI · 2026-09-01 · Other changes: 50 changes in 0.152.0 — App-server
  clients can configure `thread/shellCommand` timeouts, including deadlines longer…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b0bdd43945282beb08496551dd553863d533b07506ec99d5960ad2958ba03739
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-09-01-d5112f
  comparison: ''
  date: '2026-09-01'
  description: 'Codex CLI — 0.152.0: 50 other changes'
  evidence:
  - quote: App-server clients can configure `thread/shellCommand` timeouts, including
      deadlines longer than one hour. (#41384)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: Vim-enabled composers now start fresh drafts in Insert mode, including
      after submitting messages or dispatching slash commands. (#41921)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: Automatic approval reviews can retain longer messages and a larger conversation
      transcript. (#41931)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: 'Resumed threads restore their saved working directory when none is supplied,
      and client metadata updates preserve filesystem permissions. (#41567, #41464)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: Cloud task requests reject untrusted backend URLs and disable redirects
      to protect saved credentials. (#41403)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: The planning tool is disabled by default; enable it with `tools.update_plan.enabled
      = true`. (#41744)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41219 Retry confirmed remote registration conflicts @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41221 Honor turn token budgets in Guardian review rollover @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41223 Add recency sorting to `project/list` @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41226 Move Guardian review session tests to a separate file @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41235 Sanitize history notes backend errors @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41243 Add configurable gating for the sleep tool @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41250 Include thread source in realtime connection metadata @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41260 Let the history backend enforce tool output budgets @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41285 Drive keymap conflict checks from the action registry @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41309 Honor required reviews when reusing Guardian scores @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41331 Classify clock tools as built-in control tools @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41349 Assign stable IDs to generated Responses input items @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41360 Measure Codex home usage at app-server startup @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41365 Restrict async user messages to questions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41385 Give Guardian classifications distinct turn identities @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41393 Preserve one-shot exec when unified exec is disabled @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41403 Restrict cloud task credentials to trusted origins @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41413 Optimize history item lookups @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41416 Add app-server notification media filtering @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41427 Filter media from function call output notifications @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41447 Support `openai/elicitation` form requests @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41449 Rename the read-only Seatbelt platform defaults policy @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41452 Report code mode host request durations @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41454 Block goals after repeated execution host failures @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41464 Preserve permissions when updating session metadata @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41476 Use rules_rs platforms for release binaries @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41477 Organize bundled Rust resources under asset directories @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41562 Preserve turn lineage across goal continuations @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41567 Restore thread cwd from owned settings snapshots @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41569 Harden diagnostic report uploads @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41586 Add Vim search motions to the composer @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41613 Move Vim history tests into the history search module @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41630 Update tests for default-enabled update_plan @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41666 Approve the first Node REPL execution without a Guardian wait @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41742 Show actionable rate-limit banners in the TUI @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41743 Mark history ingestion requests in turn metadata @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41744 Make the update_plan tool opt-in @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41840 Use the async stack budget for approval reviews @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41853 Box the session startup future at its API boundary @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41857 Preserve Guardian user answers from current history @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41858 Preserve user text when Guardian history drops oversized images
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41861 Keep history extension tools out of Guardian reviews @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41921 Start fresh Vim drafts in Insert mode'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41931 Increase Guardian message transcript limits'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 50-other-changes-in-rust-v0-152-0
  source_release: codex-cli-2026-09-01-rust-v0-152-0-github-380164108-cd339544
  source_type: github_releases
  theme: uncategorized
  title: 50 other changes in rust-v0.152.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-09-01-rust-v0-152-0-github-380164108-cd339544|codex-cli-2026-09-01-rust-v0-152-0-github-380164108-cd339544]]'
source_type: github_releases
theme: uncategorized
title: 50 other changes in rust-v0.152.0
type: change
---

<!-- chronolog:begin region="header" -->
# 50 other changes in rust-v0.152.0

**Codex CLI** · 2026-09-01 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.152.0) · from [[Releases/Codex CLI/codex-cli-2026-09-01-rust-v0-152-0-github-380164108-cd339544|0.152.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> App-server clients can configure `thread/shellCommand` timeouts, including deadlines longer than one hour. (#41384)

> Vim-enabled composers now start fresh drafts in Insert mode, including after submitting messages or dispatching slash commands. (#41921)

> Automatic approval reviews can retain longer messages and a larger conversation transcript. (#41931)

> Resumed threads restore their saved working directory when none is supplied, and client metadata updates preserve filesystem permissions. (#41567, #41464)

> Cloud task requests reject untrusted backend URLs and disable redirects to protect saved credentials. (#41403)

> The planning tool is disabled by default; enable it with `tools.update_plan.enabled = true`. (#41744)

> #41219 Retry confirmed remote registration conflicts @copyberry

> #41221 Honor turn token budgets in Guardian review rollover @copyberry

> #41223 Add recency sorting to `project/list` @copyberry

> #41226 Move Guardian review session tests to a separate file @copyberry

> #41235 Sanitize history notes backend errors @copyberry

> #41243 Add configurable gating for the sleep tool @copyberry

> #41250 Include thread source in realtime connection metadata @copyberry

> #41260 Let the history backend enforce tool output budgets @copyberry

> #41285 Drive keymap conflict checks from the action registry @copyberry

> #41309 Honor required reviews when reusing Guardian scores @copyberry

> #41331 Classify clock tools as built-in control tools @copyberry

> #41349 Assign stable IDs to generated Responses input items @copyberry

> #41360 Measure Codex home usage at app-server startup @copyberry

> #41365 Restrict async user messages to questions @copyberry

> #41385 Give Guardian classifications distinct turn identities @copyberry

> #41393 Preserve one-shot exec when unified exec is disabled @copyberry

> #41403 Restrict cloud task credentials to trusted origins @copyberry

> #41413 Optimize history item lookups @copyberry

> #41416 Add app-server notification media filtering @copyberry

> #41427 Filter media from function call output notifications @copyberry

> #41447 Support `openai/elicitation` form requests @copyberry

> #41449 Rename the read-only Seatbelt platform defaults policy @copyberry

> #41452 Report code mode host request durations @copyberry

> #41454 Block goals after repeated execution host failures @copyberry

> #41464 Preserve permissions when updating session metadata @copyberry

> #41476 Use rules_rs platforms for release binaries @copyberry

> #41477 Organize bundled Rust resources under asset directories @copyberry

> #41562 Preserve turn lineage across goal continuations @copyberry

> #41567 Restore thread cwd from owned settings snapshots @copyberry

> #41569 Harden diagnostic report uploads @copyberry

> #41586 Add Vim search motions to the composer @copyberry

> #41613 Move Vim history tests into the history search module @copyberry

> #41630 Update tests for default-enabled update_plan @copyberry

> #41666 Approve the first Node REPL execution without a Guardian wait @copyberry

> #41742 Show actionable rate-limit banners in the TUI @copyberry

> #41743 Mark history ingestion requests in turn metadata @copyberry

> #41744 Make the update_plan tool opt-in @copyberry

> #41840 Use the async stack budget for approval reviews @copyberry

> #41853 Box the session startup future at its API boundary @copyberry

> #41857 Preserve Guardian user answers from current history @copyberry

> #41858 Preserve user text when Guardian history drops oversized images @copyberry

> #41861 Keep history extension tools out of Guardian reviews @copyberry

> #41921 Start fresh Vim drafts in Insert mode

> #41931 Increase Guardian message transcript limits

Source: https://github.com/openai/codex/releases/tag/rust-v0.152.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-09-01-5-collaboration-changes-in-rust-v0-152-0|5 Collaboration changes in rust-v0.152.0]] · Collaboration
- [[Changes/Codex CLI/2026-09-01-4-agent-mode-changes-in-rust-v0-152-0|4 Agent Mode changes in rust-v0.152.0]] · Agent Mode
- [[Changes/Codex CLI/2026-09-01-41457-source-proactive-multi-agent-instructions-from-the-model-catalog-copyberry|♯41457 Source proactive multi-agent instructions from the model catalog @copyberry]] · Automation and Scheduling
- [[Changes/Codex CLI/2026-09-01-6-model-support-changes-in-rust-v0-152-0|6 Model Support changes in rust-v0.152.0]] · Model Support
- [[Changes/Codex CLI/2026-09-01-rate-limit-banners-offer-actions-for-checking-usage-managing-credits-resetting-l|Rate-limit banners offer actions for checking usage, managing credits, resetting…]] · Pricing Model
- [[Changes/Codex CLI/2026-09-01-6-developer-workflow-changes-in-rust-v0-152-0|6 Developer Workflow changes in rust-v0.152.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-09-01-9-context-window-changes-in-rust-v0-152-0|9 Context Window changes in rust-v0.152.0]] · Context Window
- [[Changes/Codex CLI/2026-09-01-41227-use-compatible-powershell-for-elevated-windows-sandbox-commands-copyberry|♯41227 Use compatible PowerShell for elevated Windows sandbox commands @copyberry]] · Safety and Privacy
- [[Changes/Codex CLI/2026-09-01-2-account-and-access-changes-in-rust-v0-152-0|2 Account and Access changes in rust-v0.152.0]] · Account and Access
- [[Changes/Codex CLI/2026-09-01-3-interface-experience-changes-in-rust-v0-152-0|3 Interface Experience changes in rust-v0.152.0]] · Interface Experience
- [[Changes/Codex CLI/2026-09-01-16-apps-and-integrations-changes-in-rust-v0-152-0|16 Apps and Integrations changes in rust-v0.152.0]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-09-01-d5112f&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-09-01-50-other-changes-in-rust-v0-152-0.md%0ACard%20ID%3A%20codex-cli-2026-09-01-d5112f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.152.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->