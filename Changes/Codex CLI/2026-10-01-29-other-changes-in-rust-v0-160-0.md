---
card_id: codex-cli-2026-10-01-5b2f79
date: '2026-10-01'
description: 'Codex CLI · 2026-10-01 · Other changes: 29 changes in 0.160.0 — Start
  sessions outside a project with workspace defaults when policy permits, and restore
  saved…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d7c443d0362d66f9b3cca776003bb4761a2681ed0112ce08956ecb37ce29e320
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-10-01-5b2f79
  comparison: ''
  date: '2026-10-01'
  description: 'Codex CLI — 0.160.0: 29 other changes'
  evidence:
  - quote: Start sessions outside a project with workspace defaults when policy permits,
      and restore saved permissions when resuming. (#49160)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.160.0
  - quote: Unsent queued messages now resume after reconnection once uncertain submissions
      are resolved, avoiding duplicate sends. (#49105)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.160.0
  - quote: 'Prevented SQLite stalls during connection setup and logging, and surfaced
      initialization errors instead of masking them as timeouts. (#49032, #49102)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.160.0
  - quote: Clarified how provider credentials use the configured storage backend and
      how `env_key` identifies the API-key environment variable. (#49118)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.160.0
  - quote: Added background reclamation of unused log database space to reduce disk
      usage. (#49069)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.160.0
  - quote: '#48983 Avoid full metadata rewrites for thread timestamp updates @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.160.0
  - quote: '#49032 Avoid SQLite stalls from connection setup and stderr span logging
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.160.0
  - quote: '#49036 Add opt-in conversation history retrieval to Guardian reviews @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.160.0
  - quote: '#49041 Copy selections within inline code as plain text @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.160.0
  - quote: '#49043 Update Pro plan display names in the TUI @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.160.0
  - quote: '#49069 Reclaim unused SQLite log database pages in the background @dkovalenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.160.0
  - quote: '#49074 Propagate Cargo package versions to Bazel Rust targets @tamird'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.160.0
  - quote: '#49084 Track app-server running turns incrementally @tamird'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.160.0
  - quote: '#49089 Render follow-up directive labels in the TUI and copied responses
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.160.0
  - quote: '#49096 Update `h2` from 0.4.16 to 0.4.19 in Cargo and Bazel lockfiles
      @cassirer-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.160.0
  - quote: '#49102 Preserve SQLite vacuum modes and surface pool initialization errors
      @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.160.0
  - quote: '#49103 Balance Windows Bazel test shards using duration estimates @jgershen-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.160.0
  - quote: '#49105 Resume unsent TUI input after reconnecting @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.160.0
  - quote: '#49117 Attribute analytics requests to each thread''s product SKU @papayo-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.160.0
  - quote: '#49119 Add recovery guidance to content-filter retries @won-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.160.0
  - quote: '#49127 Deduplicate cloud and executor skill listings before budgeting
      @TAFOYA-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.160.0
  - quote: '#49136 Remove the plus separator after Option symbols in TUI key hints
      @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.160.0
  - quote: '#49138 Expose original error details to turn lifecycle contributors @bryanashley'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.160.0
  - quote: '#49147 Simplify cloud task base URL normalization @akira-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.160.0
  - quote: '#49153 Omit blockquote markers when copying quoted selections in the TUI
      @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.160.0
  - quote: '#49160 Support projectless TUI sessions with workspace defaults @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.160.0
  - quote: '#49161 Honor app-server provider defaults in the TUI @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.160.0
  - quote: '#49164 Suppress Windows console windows for background subprocesses @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.160.0
  - quote: '#49386 [0.160] Backport remaining Windows console fix to frozen alpha.6
      @andrewgu-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.160.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 29-other-changes-in-rust-v0-160-0
  source_release: codex-cli-2026-10-01-rust-v0-160-0-github-401312540-620e0269
  source_type: github_releases
  theme: uncategorized
  title: 29 other changes in rust-v0.160.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-10-01-rust-v0-160-0-github-401312540-620e0269|codex-cli-2026-10-01-rust-v0-160-0-github-401312540-620e0269]]'
source_type: github_releases
theme: uncategorized
title: 29 other changes in rust-v0.160.0
type: change
---

<!-- chronolog:begin region="header" -->
# 29 other changes in rust-v0.160.0

**Codex CLI** · 2026-10-01 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.160.0) · from [[Releases/Codex CLI/codex-cli-2026-10-01-rust-v0-160-0-github-401312540-620e0269|0.160.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Start sessions outside a project with workspace defaults when policy permits, and restore saved permissions when resuming. (#49160)

> Unsent queued messages now resume after reconnection once uncertain submissions are resolved, avoiding duplicate sends. (#49105)

> Prevented SQLite stalls during connection setup and logging, and surfaced initialization errors instead of masking them as timeouts. (#49032, #49102)

> Clarified how provider credentials use the configured storage backend and how `env_key` identifies the API-key environment variable. (#49118)

> Added background reclamation of unused log database space to reduce disk usage. (#49069)

> #48983 Avoid full metadata rewrites for thread timestamp updates @jif-oai

> #49032 Avoid SQLite stalls from connection setup and stderr span logging @jif-oai

> #49036 Add opt-in conversation history retrieval to Guardian reviews @felixxia-oai

> #49041 Copy selections within inline code as plain text @fcoury-oai

> #49043 Update Pro plan display names in the TUI @etraut-openai

> #49069 Reclaim unused SQLite log database pages in the background @dkovalenko-oai

> #49074 Propagate Cargo package versions to Bazel Rust targets @tamird

> #49084 Track app-server running turns incrementally @tamird

> #49089 Render follow-up directive labels in the TUI and copied responses @etraut-openai

> #49096 Update `h2` from 0.4.16 to 0.4.19 in Cargo and Bazel lockfiles @cassirer-openai

> #49102 Preserve SQLite vacuum modes and surface pool initialization errors @bc-openai

> #49103 Balance Windows Bazel test shards using duration estimates @jgershen-oai

> #49105 Resume unsent TUI input after reconnecting @etraut-openai

> #49117 Attribute analytics requests to each thread's product SKU @papayo-oai

> #49119 Add recovery guidance to content-filter retries @won-openai

> #49127 Deduplicate cloud and executor skill listings before budgeting @TAFOYA-OAI

> #49136 Remove the plus separator after Option symbols in TUI key hints @bc-openai

> #49138 Expose original error details to turn lifecycle contributors @bryanashley

> #49147 Simplify cloud task base URL normalization @akira-oai

> #49153 Omit blockquote markers when copying quoted selections in the TUI @bc-openai

> #49160 Support projectless TUI sessions with workspace defaults @etraut-openai

> #49161 Honor app-server provider defaults in the TUI @etraut-openai

> #49164 Suppress Windows console windows for background subprocesses @etraut-openai

> #49386 [0.160] Backport remaining Windows console fix to frozen alpha.6 @andrewgu-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.160.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-10-01-2-interface-experience-changes-in-rust-v0-160-0|2 Interface Experience changes in rust-v0.160.0]] · Interface Experience
- [[Changes/Codex CLI/2026-10-01-browse-older-tasks-in-the-agent-command-center-with-a-keyboard-accessible-show-m|Browse older tasks in the agent command center with a keyboard-accessible…]] · Search and Browsing
- [[Changes/Codex CLI/2026-10-01-49130-move-content-filter-guidance-into-the-shared-responses-retry-handler-won-o|♯49130 Move content-filter guidance into the shared Responses retry handler @won-openai]] · Collaboration
- [[Changes/Codex CLI/2026-10-01-49079-update-and-centralize-tui-subscription-labels-etraut-openai|♯49079 Update and centralize TUI subscription labels @etraut-openai]] · Pricing Model
- [[Changes/Codex CLI/2026-10-01-4-apps-and-integrations-changes-in-rust-v0-160-0|4 Apps and Integrations changes in rust-v0.160.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-10-01-5-model-support-changes-in-rust-v0-160-0|5 Model Support changes in rust-v0.160.0]] · Model Support
- [[Changes/Codex CLI/2026-10-01-49000-isolate-the-memory-startup-metadata-test-from-git-enrichment-jif-oai|♯49000 Isolate the memory startup metadata test from Git enrichment @jif-oai]] · Memory and Personalization
- [[Changes/Codex CLI/2026-10-01-6-agent-mode-changes-in-rust-v0-160-0|6 Agent Mode changes in rust-v0.160.0]] · Agent Mode
- [[Changes/Codex CLI/2026-10-01-2-account-and-access-changes-in-rust-v0-160-0|2 Account and Access changes in rust-v0.160.0]] · Account and Access
- [[Changes/Codex CLI/2026-10-01-7-safety-and-privacy-changes-in-rust-v0-160-0|7 Safety and Privacy changes in rust-v0.160.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-10-01-49082-skip-remote-git-discovery-for-guardian-diff-paths-jif-oai|♯49082 Skip remote Git discovery for Guardian diff paths @jif-oai]] · Editor Experience
- [[Changes/Codex CLI/2026-10-01-49093-simplify-startup-promotions-to-platform-specific-desktop-app-tips-etraut-o|♯49093 Simplify startup promotions to platform-specific desktop app tips @etraut-openai]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-10-01-3-context-window-changes-in-rust-v0-160-0|3 Context Window changes in rust-v0.160.0]] · Context Window
- [[Changes/Codex CLI/2026-10-01-49073-surface-realtime-voice-catalog-failures-in-the-tui-etraut-openai|♯49073 Surface realtime voice catalog failures in the TUI @etraut-openai]] · Voice and Audio
- [[Changes/Codex CLI/2026-10-01-2-developer-workflow-changes-in-rust-v0-160-0|2 Developer Workflow changes in rust-v0.160.0]] · Developer Workflow
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-10-01-5b2f79&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-10-01-29-other-changes-in-rust-v0-160-0.md%0ACard%20ID%3A%20codex-cli-2026-10-01-5b2f79%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.160.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->