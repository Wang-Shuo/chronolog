---
card_id: codex-cli-2026-06-25-da0276
date: '2026-06-25'
description: 'Codex CLI · 2026-06-25 · Other changes: 13 changes in 0.142.2 — Expired
  Amazon Bedrock credentials now produce actionable recovery guidance instead of a…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f99d7ef89fec0d34b97a792329a5e17f5219b47a4b57260e95eb8895a0f18ee5
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-06-25-da0276
  comparison: ''
  date: '2026-06-25'
  description: 'Codex CLI — 0.142.2: 13 other changes'
  evidence:
  - quote: Expired Amazon Bedrock credentials now produce actionable recovery guidance
      instead of a generic authorization error. (#28992)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.2
  - quote: 'Updated bundled OpenSSL and esbuild dependencies to patched releases.
      (#29487, #29489)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.2
  - quote: Successful formatter runs are now quiet while failures still show diagnostics.
      (#29467)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.2
  - quote: '#28769 Register full CDP requirements feature @syuan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.2
  - quote: '#29487 Upgrade bundled OpenSSL to 3.6.3 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.2
  - quote: '#29489 [codex] Update esbuild to 0.28.1 @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.2
  - quote: '#28360 feat(core): store turn_id on ResponseItem metadata @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.2
  - quote: '#29501 path-uri: clarify host-native path conversion @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.2
  - quote: '#29504 fix: world state response item test @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.2
  - quote: '#29419 [codex] reject remote images at app-server ingress @rka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.2
  - quote: '#28992 chore: improve expired Bedrock credential errors @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.2
  - quote: '#29467 Make formatter output quiet on success @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.2
  - quote: '#24092 [codex] Reject unlowered PowerShell AST regions @bookholt-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 13-other-changes-in-rust-v0-142-2
  source_release: codex-cli-2026-06-25-rust-v0-142-2-github-344540546-8fdabe3c
  source_type: github_releases
  theme: uncategorized
  title: 13 other changes in rust-v0.142.2
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-06-25-rust-v0-142-2-github-344540546-8fdabe3c|codex-cli-2026-06-25-rust-v0-142-2-github-344540546-8fdabe3c]]'
source_type: github_releases
theme: uncategorized
title: 13 other changes in rust-v0.142.2
type: change
---

<!-- chronolog:begin region="header" -->
# 13 other changes in rust-v0.142.2

**Codex CLI** · 2026-06-25 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.142.2) · from [[Releases/Codex CLI/codex-cli-2026-06-25-rust-v0-142-2-github-344540546-8fdabe3c|0.142.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Expired Amazon Bedrock credentials now produce actionable recovery guidance instead of a generic authorization error. (#28992)

> Updated bundled OpenSSL and esbuild dependencies to patched releases. (#29487, #29489)

> Successful formatter runs are now quiet while failures still show diagnostics. (#29467)

> #28769 Register full CDP requirements feature @syuan-oai

> #29487 Upgrade bundled OpenSSL to 3.6.3 @jif-oai

> #29489 [codex] Update esbuild to 0.28.1 @pakrym-oai

> #28360 feat(core): store turn_id on ResponseItem metadata @owenlin0

> #29501 path-uri: clarify host-native path conversion @anp-oai

> #29504 fix: world state response item test @celia-oai

> #29419 [codex] reject remote images at app-server ingress @rka-oai

> #28992 chore: improve expired Bedrock credential errors @celia-oai

> #29467 Make formatter output quiet on success @anp-oai

> #24092 [codex] Reject unlowered PowerShell AST regions @bookholt-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.142.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-06-25-macos-authentication-clients-can-honor-system-proxy-pac-and-wpad-settings-when-r|macOS authentication clients can honor system proxy, PAC, and WPAD settings…]] · Account and Access
- [[Changes/Codex CLI/2026-06-25-26709-pac-4-add-macos-system-proxy-resolver-canvrno-oai|♯26709 PAC 4 - Add macOS system proxy resolver @canvrno-oai]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-06-25-2-context-window-changes-in-rust-v0-142-2|2 Context Window changes in rust-v0.142.2]] · Context Window
- [[Changes/Codex CLI/2026-06-25-4-model-support-changes-in-rust-v0-142-2|4 Model Support changes in rust-v0.142.2]] · Model Support
- [[Changes/Codex CLI/2026-06-25-9-apps-and-integrations-changes-in-rust-v0-142-2|9 Apps and Integrations changes in rust-v0.142.2]] · Apps and Integrations
- [[Changes/Codex CLI/2026-06-25-apps-can-display-richer-safety-buffering-ui-using-server-provided-visibility-and|Apps can display richer safety-buffering UI using server-provided visibility…]] · Reliability and Performance
- [[Changes/Codex CLI/2026-06-25-2-safety-and-privacy-changes-in-rust-v0-142-2|2 Safety and Privacy changes in rust-v0.142.2]] · Safety and Privacy
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-06-25-da0276&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-06-25-13-other-changes-in-rust-v0-142-2.md%0ACard%20ID%3A%20codex-cli-2026-06-25-da0276%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.142.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->