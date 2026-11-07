---
card_id: codex-cli-2026-06-08-96009e
date: '2026-06-08'
description: 'Codex CLI · 2026-06-08 · Apps and Integrations: 19 changes in 0.138.0
  — Plugin automation got richer structured output: add/remove and marketplace commands…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2733
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 05af26bc9bc9f595fd70bee1d4b5ccb8b4a431171136f0a4ffbaffd8f060b25d
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-06-08-96009e
  comparison: ''
  date: '2026-06-08'
  description: 'Codex CLI — 0.138.0: 19 Apps and Integrations changes'
  evidence:
  - quote: 'Plugin automation got richer structured output: add/remove and marketplace
      commands support `--json`, plugin list JSON includes marketplace source, and
      plugin detail data now exposes default prompts, remote MCP servers, and unavailable
      app templates. (#26631, #26417, #25887, #26453, #26317)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: 'TUI startup does less repeated plugin work by reusing discovery results
      and loading only hook metadata on the critical path. (#26469, #26272)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: Large MCP/Ollama streams and long message histories process much faster
      thanks to optimized byte scanning. (#26265)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26216 [codex] Pin Python SDK to runtime 0.137.0a4 @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#25887 Preserve remote plugin default prompts @ericning-o'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26002 log plugin MCP server names @chrisdong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26396 Reduce SQLite contention from OpenTelemetry SDK debug logs @zanie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26272 Load plugin hooks without other plugin capabilities @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26417 Expose configured marketplace source in plugin list JSON @mpc-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26435 external-agent-migration: avoid mixed MCP transport configs @stefanstokic-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26453 fix(app-server): expose remote MCP servers in plugin read @ericning-o'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26317 [codex] Expose unavailable app templates in plugin detail @charlesgong-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26431 Pull plugin service less frequently @beggers-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26215 feat(remote-control): allow pairing while disabled @apanasenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26449 feat(remote-control): add pairing status transport @hefuc-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26450 feat(app-server): add remote control pairing status RPC @hefuc-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26469 Speed up TUI startup by reusing plugin discovery @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26631 Add JSON output for plugin subcommands @mpc-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#25936 [codex] Remove legacy remote plugin startup sync @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 19-apps-and-integrations-changes-in-rust-v0-138-0
  source_release: codex-cli-2026-06-08-rust-v0-138-0-github-336275797-115d015a
  source_type: github_releases
  theme: apps-integrations
  title: 19 Apps and Integrations changes in rust-v0.138.0
  type: change
related_changes:
- '[[Changes/Replit/2026-06-05-integrations|Integrations]]'
- '[[Changes/Claude Code/2026-06-06-added-glob-pattern-support-in-deny-rule-tool-name-position-denies-all-tools-allo|Added
  glob pattern support in deny rule tool-name position ("" denies all tools)]]'
- '[[Changes/Ollama/2026-06-07-ollama-launch-now-supports-hermes-desktop-a-native-desktop-interface-for-the-her|Ollama
  Launch now supports Hermes Desktop, a native desktop interface for the Hermes agent]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-06-08-rust-v0-138-0-github-336275797-115d015a|codex-cli-2026-06-08-rust-v0-138-0-github-336275797-115d015a]]'
source_type: github_releases
theme: apps-integrations
title: 19 Apps and Integrations changes in rust-v0.138.0
type: change
---

<!-- chronolog:begin region="header" -->
# 19 Apps and Integrations changes in rust-v0.138.0

**Codex CLI** · 2026-06-08 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.138.0) · from [[Releases/Codex CLI/codex-cli-2026-06-08-rust-v0-138-0-github-336275797-115d015a|0.138.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Plugin automation got richer structured output: add/remove and marketplace commands support `--json`, plugin list JSON includes marketplace source, and plugin detail data now exposes default prompts, remote MCP servers, and unavailable app templates. (#26631, #26417, #25887, #26453, #26317)

> TUI startup does less repeated plugin work by reusing discovery results and loading only hook metadata on the critical path. (#26469, #26272)

> Large MCP/Ollama streams and long message histories process much faster thanks to optimized byte scanning. (#26265)

> #26216 [codex] Pin Python SDK to runtime 0.137.0a4 @aibrahim-oai

> #25887 Preserve remote plugin default prompts @ericning-o

> #26002 log plugin MCP server names @chrisdong-oai

> #26396 Reduce SQLite contention from OpenTelemetry SDK debug logs @zanie-oai

> #26272 Load plugin hooks without other plugin capabilities @charliemarsh-oai

> #26417 Expose configured marketplace source in plugin list JSON @mpc-oai

> #26435 external-agent-migration: avoid mixed MCP transport configs @stefanstokic-oai

> #26453 fix(app-server): expose remote MCP servers in plugin read @ericning-o

> #26317 [codex] Expose unavailable app templates in plugin detail @charlesgong-openai

> #26431 Pull plugin service less frequently @beggers-openai

> #26215 feat(remote-control): allow pairing while disabled @apanasenko-oai

> #26449 feat(remote-control): add pairing status transport @hefuc-oai

> #26450 feat(app-server): add remote control pairing status RPC @hefuc-oai

> #26469 Speed up TUI startup by reusing plugin discovery @charliemarsh-oai

> #26631 Add JSON output for plugin subcommands @mpc-oai

> #25936 [codex] Remove legacy remote plugin startup sync @xl-openai

Source: https://github.com/openai/codex/releases/tag/rust-v0.138.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-06-08-6-safety-and-privacy-changes-in-rust-v0-138-0|6 Safety and Privacy changes in rust-v0.138.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-06-08-2-image-generation-changes-in-rust-v0-138-0|2 Image Generation changes in rust-v0.138.0]] · Image Generation
- [[Changes/Codex CLI/2026-06-08-4-mobile-and-desktop-changes-in-rust-v0-138-0|4 Mobile and Desktop changes in rust-v0.138.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-06-08-2-account-and-access-changes-in-rust-v0-138-0|2 Account and Access changes in rust-v0.138.0]] · Account and Access
- [[Changes/Codex CLI/2026-06-08-7-developer-workflow-changes-in-rust-v0-138-0|7 Developer Workflow changes in rust-v0.138.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-06-08-6-model-support-changes-in-rust-v0-138-0|6 Model Support changes in rust-v0.138.0]] · Model Support
- [[Changes/Codex CLI/2026-06-08-4-context-window-changes-in-rust-v0-138-0|4 Context Window changes in rust-v0.138.0]] · Context Window
- [[Changes/Codex CLI/2026-06-08-8-agent-mode-changes-in-rust-v0-138-0|8 Agent Mode changes in rust-v0.138.0]] · Agent Mode
- [[Changes/Codex CLI/2026-06-08-3-editor-experience-changes-in-rust-v0-138-0|3 Editor Experience changes in rust-v0.138.0]] · Editor Experience
- [[Changes/Codex CLI/2026-06-08-54-other-changes-in-rust-v0-138-0|54 other changes in rust-v0.138.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-06-07 · Ollama · [[Changes/Ollama/2026-06-07-ollama-launch-now-supports-hermes-desktop-a-native-desktop-interface-for-the-her|Ollama Launch now supports Hermes Desktop, a native desktop interface for the Hermes agent]]
- Later: 2026-06-08 · ElevenLabs · [[Changes/ElevenLabs/2026-06-08-sdk-releases|SDK Releases]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-06-08-96009e&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-06-08-19-apps-and-integrations-changes-in-rust-v0-138-0.md%0ACard%20ID%3A%20codex-cli-2026-06-08-96009e%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.138.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->