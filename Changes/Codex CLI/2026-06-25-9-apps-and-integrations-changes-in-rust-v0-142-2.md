---
card_id: codex-cli-2026-06-25-c8cb0f
date: '2026-06-25'
description: 'Codex CLI · 2026-06-25 · Apps and Integrations: 9 changes in 0.142.2
  — MCP tools now use tool search by default when supported, improving tool discovery
  while…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2750
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 520cac96590a285c0c472834e5a104262a3159f6acb106669324cf4c42faf566
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-06-25-c8cb0f
  comparison: ''
  date: '2026-06-25'
  description: 'Codex CLI — 0.142.2: 9 Apps and Integrations changes'
  evidence:
  - quote: MCP tools now use tool search by default when supported, improving tool
      discovery while preserving compatibility with older models and providers. (#29486)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.2
  - quote: Plugins can provide dedicated dark-mode logos through local manifests and
      remote catalogs. (#29488)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.2
  - quote: Remote plugin catalogs now return curated featured-plugin rankings. (#29485)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.2
  - quote: Remote stdio MCP servers now accept absolute working directories written
      in the remote platform’s path format. (#29493)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.2
  - quote: '#29485 [codex] fetch featured IDs for remote plugins @ericning-o'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.2
  - quote: '#29488 [plugins] Add dark-mode logo metadata @drewschuster-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.2
  - quote: '#29486 [codex] Use tool search for MCP tools by default @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.2
  - quote: '#26704 TUI Plugin Sharing 4 - cover remote plugin catalog flows @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.2
  - quote: '#29493 mcp: accept foreign absolute cwd for remote stdio @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 9-apps-and-integrations-changes-in-rust-v0-142-2
  source_release: codex-cli-2026-06-25-rust-v0-142-2-github-344540546-8fdabe3c
  source_type: github_releases
  theme: apps-integrations
  title: 9 Apps and Integrations changes in rust-v0.142.2
  type: change
related_changes:
- '[[Changes/OpenCode/2026-06-24-added-mcp-server-instructions-to-session-context|Added
  MCP server instructions to session context]]'
- '[[Changes/OpenCode/2026-06-24-9-apps-and-integrations-changes-in-v1-17-10|9 Apps
  and Integrations changes in v1.17.10]]'
- '[[Changes/Claude Code/2026-06-25-2-apps-and-integrations-changes-in-v2-1-193|2
  Apps and Integrations changes in v2.1.193]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-06-25-rust-v0-142-2-github-344540546-8fdabe3c|codex-cli-2026-06-25-rust-v0-142-2-github-344540546-8fdabe3c]]'
source_type: github_releases
theme: apps-integrations
title: 9 Apps and Integrations changes in rust-v0.142.2
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Apps and Integrations changes in rust-v0.142.2

**Codex CLI** · 2026-06-25 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.142.2) · from [[Releases/Codex CLI/codex-cli-2026-06-25-rust-v0-142-2-github-344540546-8fdabe3c|0.142.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> MCP tools now use tool search by default when supported, improving tool discovery while preserving compatibility with older models and providers. (#29486)

> Plugins can provide dedicated dark-mode logos through local manifests and remote catalogs. (#29488)

> Remote plugin catalogs now return curated featured-plugin rankings. (#29485)

> Remote stdio MCP servers now accept absolute working directories written in the remote platform’s path format. (#29493)

> #29485 [codex] fetch featured IDs for remote plugins @ericning-o

> #29488 [plugins] Add dark-mode logo metadata @drewschuster-openai

> #29486 [codex] Use tool search for MCP tools by default @sayan-oai

> #26704 TUI Plugin Sharing 4 - cover remote plugin catalog flows @canvrno-oai

> #29493 mcp: accept foreign absolute cwd for remote stdio @anp-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.142.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-06-25-macos-authentication-clients-can-honor-system-proxy-pac-and-wpad-settings-when-r|macOS authentication clients can honor system proxy, PAC, and WPAD settings…]] · Account and Access
- [[Changes/Codex CLI/2026-06-25-26709-pac-4-add-macos-system-proxy-resolver-canvrno-oai|♯26709 PAC 4 - Add macOS system proxy resolver @canvrno-oai]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-06-25-2-context-window-changes-in-rust-v0-142-2|2 Context Window changes in rust-v0.142.2]] · Context Window
- [[Changes/Codex CLI/2026-06-25-4-model-support-changes-in-rust-v0-142-2|4 Model Support changes in rust-v0.142.2]] · Model Support
- [[Changes/Codex CLI/2026-06-25-apps-can-display-richer-safety-buffering-ui-using-server-provided-visibility-and|Apps can display richer safety-buffering UI using server-provided visibility…]] · Reliability and Performance
- [[Changes/Codex CLI/2026-06-25-2-safety-and-privacy-changes-in-rust-v0-142-2|2 Safety and Privacy changes in rust-v0.142.2]] · Safety and Privacy
- [[Changes/Codex CLI/2026-06-25-13-other-changes-in-rust-v0-142-2|13 other changes in rust-v0.142.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-06-25 · Claude Code · [[Changes/Claude Code/2026-06-25-2-apps-and-integrations-changes-in-v2-1-193|2 Apps and Integrations changes in v2.1.193]]
- Later: 2026-06-25 · Dify · [[Changes/Dify/2026-06-25-27-apps-and-integrations-changes-in-1-15-0|27 Apps and Integrations changes in 1.15.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-06-25-c8cb0f&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-06-25-9-apps-and-integrations-changes-in-rust-v0-142-2.md%0ACard%20ID%3A%20codex-cli-2026-06-25-c8cb0f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.142.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->