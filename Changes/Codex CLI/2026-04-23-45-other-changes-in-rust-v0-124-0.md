---
card_id: codex-cli-2026-04-23-e4bad7
date: '2026-04-23'
description: 'Codex CLI · 2026-04-23 · Other changes: 45 changes in 0.124.0 — App-server
  sessions can now manage multiple environments and choose an environment and working…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2f5f30a0e10c3c24a229f937dad35ffe28ef567921f309a71281fff6fb9c7229
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-04-23-e4bad7
  comparison: ''
  date: '2026-04-23'
  description: 'Codex CLI — 0.124.0: 45 other changes'
  evidence:
  - quote: 'App-server sessions can now manage multiple environments and choose an
      environment and working directory per turn, which makes multi-workspace and
      remote setups easier to target precisely. (#18401, #18416)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: Added first-class Amazon Bedrock support for OpenAI-compatible providers,
      including AWS SigV4 signing and AWS credential-based auth. (#17820)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: Eligible ChatGPT plans now default to the Fast service tier unless you
      explicitly opt out. (#19053)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: Preserved Cloudflare cookies across approved ChatGPT hosts, reducing auth
      breakage in HTTP-backed ChatGPT flows. (#17783)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: 'Startup now fails less often on managed config edge cases: unknown feature
      requirements warn instead of aborting, and cloud-requirements errors are clearer
      about what failed. (#19038, #19078)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18870 Load app-server config through ConfigManager @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18430 app-server: implement device key v2 methods @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#17783 Preserve Cloudfare HTTP cookies in codex @shijie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18876 [rollout_trace] Add rollout trace crate @cassirer-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18401 Support multiple managed environments @starr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18797 Allow guardian bare allow output @maja-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18886 Normalize /statusline & /title items @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18768 [codex] Tighten external migration prompt tests @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18909 Update /statusline and /title snapshots @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18416 Add turn-scoped environment selections @starr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18913 bazel: run wrapped Rust unit test shards @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18936 Fix remote app-server shutdown race @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18926 ci: keep argument comment lint checks materialized @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18935 Keep TUI status surfaces in sync @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18943 tests: serialize process-heavy Windows CI suites @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18934 [codex] Clean guardian instructions @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18948 chore: remove unused Bedrock auth lazy loading @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18785 feat: add explicit AgentIdentity auth mode @efrazer-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#17693 [codex-analytics] guardian review analytics events emission @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#17695 [codex-analytics] guardian review truncation @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#17696 [codex-analytics] guardian review TTFT plumbing and emission @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18962 nit: expose lib @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18502 Support multiple cwd filters for thread list @acrognale-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18971 fix: cargo deny @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18852 [codex] Update imagegen system skill @vb-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18865 Stage publishable Python runtime wheels @sdcoffey'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18932 TUI: Keep remote app-server events draining @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18877 [rollout_trace] Record core session rollout traces @cassirer-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18999 arg0: keep dispatch aliases alive during async main @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18582 [2/4] Implement executor HTTP request runner @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18956 [Codex] Register browser requirements feature keys @khoi-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#19043 Update bundled OpenAI Docs skill freshness check @kkahadze-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18583 [3/4] Add executor-backed RMCP HTTP client @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#19050 feat(request-permissions) approve with strict review @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#19067 test: set Rust test thread stack size @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#19072 tui: fix approvals popup disabled shortcut test @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#19053 Default Fast service tier for eligible ChatGPT plans @shijie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#19071 Add computer_use feature requirement key @leoshimo-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#19038 feat: Warn and continue on unknown feature requirements @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#19078 Clarify cloud requirements error messages @gverma-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 45-other-changes-in-rust-v0-124-0
  source_release: codex-cli-2026-04-23-rust-v0-124-0-github-312880358-5864635b
  source_type: github_releases
  theme: uncategorized
  title: 45 other changes in rust-v0.124.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-04-23-rust-v0-124-0-github-312880358-5864635b|codex-cli-2026-04-23-rust-v0-124-0-github-312880358-5864635b]]'
source_type: github_releases
theme: uncategorized
title: 45 other changes in rust-v0.124.0
type: change
---

<!-- chronolog:begin region="header" -->
# 45 other changes in rust-v0.124.0

**Codex CLI** · 2026-04-23 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.124.0) · from [[Releases/Codex CLI/codex-cli-2026-04-23-rust-v0-124-0-github-312880358-5864635b|0.124.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> App-server sessions can now manage multiple environments and choose an environment and working directory per turn, which makes multi-workspace and remote setups easier to target precisely. (#18401, #18416)

> Added first-class Amazon Bedrock support for OpenAI-compatible providers, including AWS SigV4 signing and AWS credential-based auth. (#17820)

> Eligible ChatGPT plans now default to the Fast service tier unless you explicitly opt out. (#19053)

> Preserved Cloudflare cookies across approved ChatGPT hosts, reducing auth breakage in HTTP-backed ChatGPT flows. (#17783)

> Startup now fails less often on managed config edge cases: unknown feature requirements warn instead of aborting, and cloud-requirements errors are clearer about what failed. (#19038, #19078)

> #18870 Load app-server config through ConfigManager @pakrym-oai

> #18430 app-server: implement device key v2 methods @euroelessar

> #17783 Preserve Cloudfare HTTP cookies in codex @shijie-oai

> #18876 [rollout_trace] Add rollout trace crate @cassirer-openai

> #18401 Support multiple managed environments @starr-openai

> #18797 Allow guardian bare allow output @maja-openai

> #18886 Normalize /statusline & /title items @canvrno-oai

> #18768 [codex] Tighten external migration prompt tests @alexsong-oai

> #18909 Update /statusline and /title snapshots @canvrno-oai

> #18416 Add turn-scoped environment selections @starr-openai

> #18913 bazel: run wrapped Rust unit test shards @bolinfest

> #18936 Fix remote app-server shutdown race @bolinfest

> #18926 ci: keep argument comment lint checks materialized @bolinfest

> #18935 Keep TUI status surfaces in sync @etraut-openai

> #18943 tests: serialize process-heavy Windows CI suites @bolinfest

> #18934 [codex] Clean guardian instructions @dylan-hurd-oai

> #18948 chore: remove unused Bedrock auth lazy loading @celia-oai

> #18785 feat: add explicit AgentIdentity auth mode @efrazer-oai

> #17693 [codex-analytics] guardian review analytics events emission @rhan-oai

> #17695 [codex-analytics] guardian review truncation @rhan-oai

> #17696 [codex-analytics] guardian review TTFT plumbing and emission @rhan-oai

> #18962 nit: expose lib @jif-oai

> #18502 Support multiple cwd filters for thread list @acrognale-oai

> #18971 fix: cargo deny @jif-oai

> #18852 [codex] Update imagegen system skill @vb-openai

> #18865 Stage publishable Python runtime wheels @sdcoffey

> #18932 TUI: Keep remote app-server events draining @etraut-openai

> #18877 [rollout_trace] Record core session rollout traces @cassirer-openai

> #18999 arg0: keep dispatch aliases alive during async main @bolinfest

> #18582 [2/4] Implement executor HTTP request runner @aibrahim-oai

> #18956 [Codex] Register browser requirements feature keys @khoi-oai

> #19043 Update bundled OpenAI Docs skill freshness check @kkahadze-oai

> #18583 [3/4] Add executor-backed RMCP HTTP client @aibrahim-oai

> #19050 feat(request-permissions) approve with strict review @dylan-hurd-oai

> #19067 test: set Rust test thread stack size @bolinfest

> #19072 tui: fix approvals popup disabled shortcut test @bolinfest

> #19053 Default Fast service tier for eligible ChatGPT plans @shijie-oai

> #19071 Add computer_use feature requirement key @leoshimo-oai

> #19038 feat: Warn and continue on unknown feature requirements @xl-openai

> #19078 Clarify cloud requirements error messages @gverma-openai

Source: https://github.com/openai/codex/releases/tag/rust-v0.124.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-04-23-17-safety-and-privacy-changes-in-rust-v0-124-0|17 Safety and Privacy changes in rust-v0.124.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-04-23-12-apps-and-integrations-changes-in-rust-v0-124-0|12 Apps and Integrations changes in rust-v0.124.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-04-23-2-developer-workflow-changes-in-rust-v0-124-0|2 Developer Workflow changes in rust-v0.124.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-04-23-18973-chore-prep-memories-for-ab-jif-oai|♯18973 chore: prep memories for AB @jif-oai]] · Memory and Personalization
- [[Changes/Codex CLI/2026-04-23-11-agent-mode-changes-in-rust-v0-124-0|11 Agent Mode changes in rust-v0.124.0]] · Agent Mode
- [[Changes/Codex CLI/2026-04-23-2-context-window-changes-in-rust-v0-124-0|2 Context Window changes in rust-v0.124.0]] · Context Window
- [[Changes/Codex CLI/2026-04-23-4-model-support-changes-in-rust-v0-124-0|4 Model Support changes in rust-v0.124.0]] · Model Support
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-04-23-e4bad7&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-04-23-45-other-changes-in-rust-v0-124-0.md%0ACard%20ID%3A%20codex-cli-2026-04-23-e4bad7%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.124.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->