---
card_id: codex-cli-2026-06-18-14582d
date: '2026-06-18'
description: 'Codex CLI · 2026-06-18 · Other changes: 42 changes in 0.141.0 — Remote
  executors now use authenticated, end-to-end encrypted Noise relay channels. (#26242…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 4300fe797a012d89018410f596a5644b3f60f13a3beca6de9cc464ddf5237c45
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-06-18-14582d
  comparison: ''
  date: '2026-06-18'
  description: 'Codex CLI — 0.141.0: 42 other changes'
  evidence:
  - quote: 'Remote executors now use authenticated, end-to-end encrypted Noise relay
      channels. (#26242, #26245)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: TUI input prompts can auto-resolve after inactivity, with a countdown that
      pauses on interaction. (#28235)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: Bundled SQLite is pinned to a version containing the WAL-reset corruption
      fix. (#27992)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: 'Bounded prompt-image caching to 64 MiB and feedback uploads to eight related
      threads. (#28294, #28332)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#28001 [codex] package Windows ARM64 on x64 @tamird'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#28032 [codex] Carry exec-server cwd as PathUri @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#27992 [codex] Pin bundled SQLite to fixed WAL-reset version @gpeal'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#28125 build: run buildifier from just fmt @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#28120 bazel: add PowerShell to Wine test harness @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#27819 path-uri: render native paths across platforms @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#26662 feat(app-server): filter threads by parent @btraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#28332 [codex] Cap feedback upload subtrees @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#27365 Represent dynamic tools with explicit namespaces internally @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#28333 skills: hide orchestrator skills with a local executor @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#28286 chore: restore exec-server relay keepalives @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#27371 Expose explicit dynamic tool namespaces in thread start @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#28309 linearize history output normalization @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#28306 avoid cloning sampling request input @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#28323 serialize websocket requests directly @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#28313 avoid cloning websocket request history @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#28344 [codex] remove stale PathExt import @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#27059 [codex] Cover OTLP HTTP log and trace event export @richardopenai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#28327 reuse encoded Responses request bodies @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#27995 [codex] preserve explicit environment cwd @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#28294 bound prompt image cache retention @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#28336 skills: cache orchestrator resources per thread @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#27706 Use aws-lc-rs for rustls crypto provider @malsamiri-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#28347 [codex] add path-types skill @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#28235 Add request user input auto-resolution timer @shijie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#27086 Add Windows unified exec yield floor @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#27258 core: cache the tool search handler per session @mchen-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#28355 feat(core): add metadata field to ResponseItem @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#28300 Deflake realtime handoff steering test @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#27955 [codex] retain resolved environments across turns @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#27917 Add realtime speech append control @guinness-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#26242 exec-server: add Noise relay transport @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#28415 [codex] Fix missing response item metadata in tests @adaley-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#27058 [codex] Add second-based OTEL duration histograms @richardopenai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#26434 Preserve hook trust bypass in codex exec threads @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#26245 exec-server: default remote transport to Noise @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#28383 [codex] Load API curated marketplace by auth @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#28429 [codex] Add interruptible sleep tool @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 42-other-changes-in-rust-v0-141-0
  source_release: codex-cli-2026-06-18-rust-v0-141-0-github-341160952-94bdbd75
  source_type: github_releases
  theme: uncategorized
  title: 42 other changes in rust-v0.141.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-06-18-rust-v0-141-0-github-341160952-94bdbd75|codex-cli-2026-06-18-rust-v0-141-0-github-341160952-94bdbd75]]'
source_type: github_releases
theme: uncategorized
title: 42 other changes in rust-v0.141.0
type: change
---

<!-- chronolog:begin region="header" -->
# 42 other changes in rust-v0.141.0

**Codex CLI** · 2026-06-18 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.141.0) · from [[Releases/Codex CLI/codex-cli-2026-06-18-rust-v0-141-0-github-341160952-94bdbd75|0.141.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Remote executors now use authenticated, end-to-end encrypted Noise relay channels. (#26242, #26245)

> TUI input prompts can auto-resolve after inactivity, with a countdown that pauses on interaction. (#28235)

> Bundled SQLite is pinned to a version containing the WAL-reset corruption fix. (#27992)

> Bounded prompt-image caching to 64 MiB and feedback uploads to eight related threads. (#28294, #28332)

> #28001 [codex] package Windows ARM64 on x64 @tamird

> #28032 [codex] Carry exec-server cwd as PathUri @anp-oai

> #27992 [codex] Pin bundled SQLite to fixed WAL-reset version @gpeal

> #28125 build: run buildifier from just fmt @anp-oai

> #28120 bazel: add PowerShell to Wine test harness @anp-oai

> #27819 path-uri: render native paths across platforms @anp-oai

> #26662 feat(app-server): filter threads by parent @btraut-openai

> #28332 [codex] Cap feedback upload subtrees @jif-oai

> #27365 Represent dynamic tools with explicit namespaces internally @sayan-oai

> #28333 skills: hide orchestrator skills with a local executor @jif-oai

> #28286 chore: restore exec-server relay keepalives @jif-oai

> #27371 Expose explicit dynamic tool namespaces in thread start @sayan-oai

> #28309 linearize history output normalization @jif-oai

> #28306 avoid cloning sampling request input @jif-oai

> #28323 serialize websocket requests directly @jif-oai

> #28313 avoid cloning websocket request history @jif-oai

> #28344 [codex] remove stale PathExt import @pakrym-oai

> #27059 [codex] Cover OTLP HTTP log and trace event export @richardopenai

> #28327 reuse encoded Responses request bodies @jif-oai

> #27995 [codex] preserve explicit environment cwd @pakrym-oai

> #28294 bound prompt image cache retention @jif-oai

> #28336 skills: cache orchestrator resources per thread @jif-oai

> #27706 Use aws-lc-rs for rustls crypto provider @malsamiri-oai

> #28347 [codex] add path-types skill @anp-oai

> #28235 Add request user input auto-resolution timer @shijie-oai

> #27086 Add Windows unified exec yield floor @iceweasel-oai

> #27258 core: cache the tool search handler per session @mchen-oai

> #28355 feat(core): add metadata field to ResponseItem @owenlin0

> #28300 Deflake realtime handoff steering test @felixxia-oai

> #27955 [codex] retain resolved environments across turns @pakrym-oai

> #27917 Add realtime speech append control @guinness-oai

> #26242 exec-server: add Noise relay transport @viyatb-oai

> #28415 [codex] Fix missing response item metadata in tests @adaley-openai

> #27058 [codex] Add second-based OTEL duration histograms @richardopenai

> #26434 Preserve hook trust bypass in codex exec threads @abhinav-oai

> #26245 exec-server: default remote transport to Noise @viyatb-oai

> #28383 [codex] Load API curated marketplace by auth @felixxia-oai

> #28429 [codex] Add interruptible sleep tool @pakrym-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.141.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-06-18-7-safety-and-privacy-changes-in-rust-v0-141-0|7 Safety and Privacy changes in rust-v0.141.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-06-18-5-agent-mode-changes-in-rust-v0-141-0|5 Agent Mode changes in rust-v0.141.0]] · Agent Mode
- [[Changes/Codex CLI/2026-06-18-7-developer-workflow-changes-in-rust-v0-141-0|7 Developer Workflow changes in rust-v0.141.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-06-18-tls-connections-now-support-p-521-certificate-signatures-commonly-used-by-enterp|TLS connections now support P-521 certificate signatures commonly used by enterprise…]] · Enterprise and Administration
- [[Changes/Codex CLI/2026-06-18-28257-support-staging-oauth-client-id-overrides-apanasenko-oai|♯28257 Support staging OAuth client ID overrides @apanasenko-oai]] · Account and Access
- [[Changes/Codex CLI/2026-06-18-2-context-window-changes-in-rust-v0-141-0|2 Context Window changes in rust-v0.141.0]] · Context Window
- [[Changes/Codex CLI/2026-06-18-17-apps-and-integrations-changes-in-rust-v0-141-0|17 Apps and Integrations changes in rust-v0.141.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-06-18-3-memory-and-personalization-changes-in-rust-v0-141-0|3 Memory and Personalization changes in rust-v0.141.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-06-18-28143-feat-app-server-expose-rate-limit-reset-credits-jayp-oai|♯28143 feat(app-server): expose rate-limit reset credits @jayp-oai]] · Pricing Model
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-06-18-14582d&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-06-18-42-other-changes-in-rust-v0-141-0.md%0ACard%20ID%3A%20codex-cli-2026-06-18-14582d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.141.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->