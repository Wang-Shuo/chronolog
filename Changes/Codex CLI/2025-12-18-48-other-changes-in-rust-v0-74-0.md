---
card_id: codex-cli-2025-12-18-76291a
date: '2025-12-18'
description: 'Codex CLI · 2025-12-18 · Other changes: 48 changes in 0.74.0 — Ghost
  snapshot warning disable toggle (#8178)'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 5a6afdad2b953a0bc8aea17bf576084c93a957d70581ee072abcf28c96b671bb
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2025-12-18-76291a
  comparison: ''
  date: '2025-12-18'
  description: 'Codex CLI — 0.74.0: 48 other changes'
  evidence:
  - quote: Ghost snapshot warning disable toggle (#8178)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.74.0
  - quote: '#8266 feat: add name to beta features'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.74.0
  - quote: '#8264 docs: clarify codex resume --all (CWD column & filtering)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.74.0
  - quote: '#8255 nit: ui background terminals'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.74.0
  - quote: '#8249 chore: prefer AsRef<Path> to &Path'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.74.0
  - quote: '#8248 chore: simplify loading of Mac-specific logic in config_loader'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.74.0
  - quote: '#8244 Reintroduce feature flags for skills.'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.74.0
  - quote: '#8243 Make loading malformed skills fail-open'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.74.0
  - quote: '#8235 fix: introduce ConfigBuilder'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.74.0
  - quote: '#8228 Show migration link'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.74.0
  - quote: '#8226 chore: cleanup Config instantiation codepaths'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.74.0
  - quote: '#8220 Support SYSTEM skills.'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.74.0
  - quote: '#8205 fix: PathBuf -> AbsolutePathBuf in ConfigToml struct'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.74.0
  - quote: '#8203 download new windows binaries when staging npm package'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.74.0
  - quote: '#8201 chore: add beta features'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.74.0
  - quote: '#8199 chore: move back stuff out of beta program'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.74.0
  - quote: '#8196 fix: session downgrade'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.74.0
  - quote: '#8194 fix: proper skills dir cleanup'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.74.0
  - quote: '#8186 nit: doc'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.74.0
  - quote: '#8182 nit: drop dead branch with unified_exec tool'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.74.0
  - quote: '#8178 feat: add config to disable warnings around ghost snapshot'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.74.0
  - quote: '#8175 fix: flaky test 6'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.74.0
  - quote: '#8152 [app-server] add new RawResponseItem v2 event'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.74.0
  - quote: '#8151 chore: update listMcpServerStatus to be non-blocking'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.74.0
  - quote: '#8141 chore(apply-patch) unicode scenario'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.74.0
  - quote: '#8140 include new windows binaries in npm package.'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.74.0
  - quote: '#8127 Revert “chore: review in read-only (#7593)”'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.74.0
  - quote: '#8124 fix tui2 compile error'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.74.0
  - quote: '#8122 docs: refine tui2 viewport roadmap'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.74.0
  - quote: '#8117 feat: unified exec footer'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.74.0
  - quote: '#8114 chore: update listMcpServers to listMcpServerStatus'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.74.0
  - quote: '#8111 chore(apply-patch) move invocation tests'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.74.0
  - quote: '#8109 Revert “feat: unified exec footer”'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.74.0
  - quote: '#8102 Upgrade GitHub Actions for Node 24 compatibility'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.74.0
  - quote: '#8098 Add public skills + improve repo skill discovery and error UX'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.74.0
  - quote: '#8095 feat: change ConfigLayerName into a disjoint union rather than a
      simple enum'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.74.0
  - quote: '#8089 refactor(tui2): make transcript line metadata explicit'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.74.0
  - quote: '#8086 chore(app-server): remove stubbed thread/compact API'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.74.0
  - quote: '#8085 chore: mac codesign refactor'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.74.0
  - quote: '#8067 feat: unified exec footer'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.74.0
  - quote: '#8060 feat: do not compact on last user turn'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.74.0
  - quote: '#8057 chore: dedup review result duplication'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.74.0
  - quote: '#8053 nit: trace span for regular task'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.74.0
  - quote: '#8052 feat: close unified_exec at end of turn'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.74.0
  - quote: '#8004 Fix: Detect Bun global install via path check'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.74.0
  - quote: '#7969 Fix: Skip Option<()> schema generation to avoid invalid Windows
      filenames (#7479)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.74.0
  - quote: '#7956 fix parallel tool calls'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.74.0
  - quote: '#7778 feat: Constrain values for approval_policy'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.74.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 48-other-changes-in-rust-v0-74-0
  source_release: codex-cli-2025-12-18-rust-v0-74-0-github-271533952-972d825a
  source_type: github_releases
  theme: uncategorized
  title: 48 other changes in rust-v0.74.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2025-12-18-rust-v0-74-0-github-271533952-972d825a|codex-cli-2025-12-18-rust-v0-74-0-github-271533952-972d825a]]'
source_type: github_releases
theme: uncategorized
title: 48 other changes in rust-v0.74.0
type: change
---

<!-- chronolog:begin region="header" -->
# 48 other changes in rust-v0.74.0

**Codex CLI** · 2025-12-18 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.74.0) · from [[Releases/Codex CLI/codex-cli-2025-12-18-rust-v0-74-0-github-271533952-972d825a|0.74.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Ghost snapshot warning disable toggle (#8178)

> #8266 feat: add name to beta features

> #8264 docs: clarify codex resume --all (CWD column & filtering)

> #8255 nit: ui background terminals

> #8249 chore: prefer AsRef\<Path> to &Path

> #8248 chore: simplify loading of Mac-specific logic in config_loader

> #8244 Reintroduce feature flags for skills.

> #8243 Make loading malformed skills fail-open

> #8235 fix: introduce ConfigBuilder

> #8228 Show migration link

> #8226 chore: cleanup Config instantiation codepaths

> #8220 Support SYSTEM skills.

> #8205 fix: PathBuf -> AbsolutePathBuf in ConfigToml struct

> #8203 download new windows binaries when staging npm package

> #8201 chore: add beta features

> #8199 chore: move back stuff out of beta program

> #8196 fix: session downgrade

> #8194 fix: proper skills dir cleanup

> #8186 nit: doc

> #8182 nit: drop dead branch with unified_exec tool

> #8178 feat: add config to disable warnings around ghost snapshot

> #8175 fix: flaky test 6

> #8152 [app-server] add new RawResponseItem v2 event

> #8151 chore: update listMcpServerStatus to be non-blocking

> #8141 chore(apply-patch) unicode scenario

> #8140 include new windows binaries in npm package.

> #8127 Revert “chore: review in read-only (#7593)”

> #8124 fix tui2 compile error

> #8122 docs: refine tui2 viewport roadmap

> #8117 feat: unified exec footer

> #8114 chore: update listMcpServers to listMcpServerStatus

> #8111 chore(apply-patch) move invocation tests

> #8109 Revert “feat: unified exec footer”

> #8102 Upgrade GitHub Actions for Node 24 compatibility

> #8098 Add public skills + improve repo skill discovery and error UX

> #8095 feat: change ConfigLayerName into a disjoint union rather than a simple enum

> #8089 refactor(tui2): make transcript line metadata explicit

> #8086 chore(app-server): remove stubbed thread/compact API

> #8085 chore: mac codesign refactor

> #8067 feat: unified exec footer

> #8060 feat: do not compact on last user turn

> #8057 chore: dedup review result duplication

> #8053 nit: trace span for regular task

> #8052 feat: close unified_exec at end of turn

> #8004 Fix: Detect Bun global install via path check

> #7969 Fix: Skip Option<()> schema generation to avoid invalid Windows filenames (#7479)

> #7956 fix parallel tool calls

> #7778 feat: Constrain values for approval_policy

Source: https://github.com/openai/codex/releases/tag/rust-v0.74.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2025-12-18-8084-chore-ci-drop-homebrew-origin-main-workaround-for-macos-runners|♯8084 chore(ci): drop Homebrew origin/main workaround for macOS runners]] · Mobile and Desktop
- [[Changes/Codex CLI/2025-12-18-7961-refactor-tui-event-loop-to-enable-dropping-recreating-crossterm-event-strea|♯7961 refactor TUI event loop to enable dropping + recreating crossterm event stream]] · Automation and Scheduling
- [[Changes/Codex CLI/2025-12-18-2-apps-and-integrations-changes-in-rust-v0-74-0|2 Apps and Integrations changes in rust-v0.74.0]] · Apps and Integrations
- [[Changes/Codex CLI/2025-12-18-6-model-support-changes-in-rust-v0-74-0|6 Model Support changes in rust-v0.74.0]] · Model Support
- [[Changes/Codex CLI/2025-12-18-3-agent-mode-changes-in-rust-v0-74-0|3 Agent Mode changes in rust-v0.74.0]] · Agent Mode
- [[Changes/Codex CLI/2025-12-18-6-interface-experience-changes-in-rust-v0-74-0|6 Interface Experience changes in rust-v0.74.0]] · Interface Experience
- [[Changes/Codex CLI/2025-12-18-7931-chore-persist-comments-in-edit|♯7931 chore: persist comments in edit]] · Editor Experience
- [[Changes/Codex CLI/2025-12-18-8216-speed-and-reliability-improvements-for-setting-reads-acls|♯8216 speed and reliability improvements for setting reads ACLs]] · Reliability and Performance
- [[Changes/Codex CLI/2025-12-18-8221-change-team-to-buisness-and-add-education|♯8221 Change “Team” to “Buisness” and add Education]] · Collaboration
- [[Changes/Codex CLI/2025-12-18-7935-exec-server-additional-context-for-errors|♯7935 exec-server: additional context for errors]] · Context Window
- [[Changes/Codex CLI/2025-12-18-2-developer-workflow-changes-in-rust-v0-74-0|2 Developer Workflow changes in rust-v0.74.0]] · Developer Workflow
- [[Changes/Codex CLI/2025-12-18-introducing-gpt-5-2-codex-our-latest-frontier-model-with-improvements-across-kno|Introducing gpt-5.2-codex our latest frontier model with improvements across…]] · Model Support
- [[Changes/Codex CLI/2025-12-18-3-safety-and-privacy-changes-in-rust-v0-74-0|3 Safety and Privacy changes in rust-v0.74.0]] · Safety and Privacy
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2025-12-18-76291a&body=Card%3A%20Changes%2FCodex%20CLI%2F2025-12-18-48-other-changes-in-rust-v0-74-0.md%0ACard%20ID%3A%20codex-cli-2025-12-18-76291a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.74.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->