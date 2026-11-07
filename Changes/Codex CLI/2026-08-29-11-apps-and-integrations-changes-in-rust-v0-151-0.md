---
card_id: codex-cli-2026-08-29-02e161
date: '2026-08-29'
description: 'Codex CLI · 2026-08-29 · Apps and Integrations: 11 changes in 0.151.0
  — Added a configurable grace period for discovering tools from optional MCP servers…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2815
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 35374167a5abfd5968657d2ae5ed66f25ce112583a7978452abfdce4c4f20f15
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-08-29-02e161
  comparison: ''
  date: '2026-08-29'
  description: 'Codex CLI — 0.151.0: 11 Apps and Integrations changes'
  evidence:
  - quote: Added a configurable grace period for discovering tools from optional MCP
      servers. (#41199)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.151.0
  - quote: Extensions can now inspect or replace MCP tool results before they reach
      the model. (#41202)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.151.0
  - quote: Plugin catalogs now combine per-repository configuration and report invalid
      project marketplaces without hiding valid plugins. (#41208)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.151.0
  - quote: Preserved structured MCP tool and resource errors in app-server responses.
      (#41196)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.151.0
  - quote: 'Added telemetry for escalated stdin reviews and remote executor MCP discovery.
      (#41189, #41205)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.151.0
  - quote: '#41193 Report affected capabilities from remote plugin syncs @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.151.0
  - quote: '#41196 Improve sandboxing, MCP errors, and cached approvals @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.151.0
  - quote: '#41199 Make the optional MCP startup grace configurable @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.151.0
  - quote: '#41202 Let extensions process MCP tool results @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.151.0
  - quote: '#41205 Track executor MCP discovery telemetry @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.151.0
  - quote: '#41208 Honor per-repository plugin configuration in catalog requests @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.151.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 11-apps-and-integrations-changes-in-rust-v0-151-0
  source_release: codex-cli-2026-08-29-rust-v0-151-0-github-378941035-5571827d
  source_type: github_releases
  theme: apps-integrations
  title: 11 Apps and Integrations changes in rust-v0.151.0
  type: change
related_changes:
- '[[Changes/Replit/2026-08-28-customize-connectors|Customize connectors]]'
- '[[Changes/Replit/2026-08-28-integrations|Integrations]]'
- '[[Changes/v0/2026-08-28-2-apps-and-integrations-changes-in-gpt-5-6-sol-sign-in-inside-previews|2
  Apps and Integrations changes in GPT-5.6 Sol, sign-in inside previews…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-08-29-rust-v0-151-0-github-378941035-5571827d|codex-cli-2026-08-29-rust-v0-151-0-github-378941035-5571827d]]'
source_type: github_releases
theme: apps-integrations
title: 11 Apps and Integrations changes in rust-v0.151.0
type: change
---

<!-- chronolog:begin region="header" -->
# 11 Apps and Integrations changes in rust-v0.151.0

**Codex CLI** · 2026-08-29 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.151.0) · from [[Releases/Codex CLI/codex-cli-2026-08-29-rust-v0-151-0-github-378941035-5571827d|0.151.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added a configurable grace period for discovering tools from optional MCP servers. (#41199)

> Extensions can now inspect or replace MCP tool results before they reach the model. (#41202)

> Plugin catalogs now combine per-repository configuration and report invalid project marketplaces without hiding valid plugins. (#41208)

> Preserved structured MCP tool and resource errors in app-server responses. (#41196)

> Added telemetry for escalated stdin reviews and remote executor MCP discovery. (#41189, #41205)

> #41193 Report affected capabilities from remote plugin syncs @copyberry

> #41196 Improve sandboxing, MCP errors, and cached approvals @copyberry

> #41199 Make the optional MCP startup grace configurable @copyberry

> #41202 Let extensions process MCP tool results @copyberry

> #41205 Track executor MCP discovery telemetry @copyberry

> #41208 Honor per-repository plugin configuration in catalog requests @copyberry

Source: https://github.com/openai/codex/releases/tag/rust-v0.151.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-08-29-5-safety-and-privacy-changes-in-rust-v0-151-0|5 Safety and Privacy changes in rust-v0.151.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-08-29-3-model-support-changes-in-rust-v0-151-0|3 Model Support changes in rust-v0.151.0]] · Model Support
- [[Changes/Codex CLI/2026-08-29-2-agent-mode-changes-in-rust-v0-151-0|2 Agent Mode changes in rust-v0.151.0]] · Agent Mode
- [[Changes/Codex CLI/2026-08-29-6-other-changes-in-rust-v0-151-0|6 other changes in rust-v0.151.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-08-28 · v0 · [[Changes/v0/2026-08-28-2-apps-and-integrations-changes-in-gpt-5-6-sol-sign-in-inside-previews|2 Apps and Integrations changes in GPT-5.6 Sol, sign-in inside previews…]]
- Later: 2026-08-31 · ElevenLabs · [[Changes/ElevenLabs/2026-08-31-sdk-releases|SDK releases]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-08-29-02e161&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-08-29-11-apps-and-integrations-changes-in-rust-v0-151-0.md%0ACard%20ID%3A%20codex-cli-2026-08-29-02e161%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.151.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->