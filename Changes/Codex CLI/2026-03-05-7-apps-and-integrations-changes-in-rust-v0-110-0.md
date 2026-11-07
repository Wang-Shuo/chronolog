---
card_id: codex-cli-2026-03-05-943812
date: '2026-03-05'
description: 'Codex CLI · 2026-03-05 · Apps and Integrations: 7 changes in 0.110.0
  — Added a plugin system that can load skills, MCP entries, and app connectors from
  config…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2638
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: c9259b01ef83137d5175207dd9e033aaaf0a7fbfa1205ca271f3a3a0b92b309d
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-03-05-943812
  comparison: ''
  date: '2026-03-05'
  description: 'Codex CLI — 0.110.0: 7 Apps and Integrations changes'
  evidence:
  - quote: 'Added a plugin system that can load skills, MCP entries, and app connectors
      from config or a local marketplace, with an install endpoint for enabling plugins
      from the app server. (#12864, #13333, #13401, #13422)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: 'Expanded app-server docs around service tiers, plugin installation, renaming
      unloaded threads, and the new `skills/changed` notification. (#13282, #13391,
      #13414, #13422)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13083 Enable analytics in codex exec and codex mcp-server @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#12864 feat: load from plugins @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13333 Refactor plugin config and cache path @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13401 feat: load plugin apps @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13422 plugin: support local-based marketplace.json + install endpoint.
      @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 7-apps-and-integrations-changes-in-rust-v0-110-0
  source_release: codex-cli-2026-03-05-rust-v0-110-0-github-293239637-d5d06302
  source_type: github_releases
  theme: apps-integrations
  title: 7 Apps and Integrations changes in rust-v0.110.0
  type: change
related_changes:
- '[[Changes/OpenCode/2026-03-04-rework-workspace-integration-and-adaptor-interface|Rework
  workspace integration and adaptor interface]]'
- '[[Changes/Claude Code/2026-03-05-added-reload-plugins-command-to-activate-pending-plugin-changes-without-restarti|Added
  /reload-plugins command to activate pending plugin changes without restarting]]'
- '[[Changes/Claude Code/2026-03-05-7-apps-and-integrations-changes-in-v2-1-69|7 Apps
  and Integrations changes in v2.1.69]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-03-05-rust-v0-110-0-github-293239637-d5d06302|codex-cli-2026-03-05-rust-v0-110-0-github-293239637-d5d06302]]'
source_type: github_releases
theme: apps-integrations
title: 7 Apps and Integrations changes in rust-v0.110.0
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Apps and Integrations changes in rust-v0.110.0

**Codex CLI** · 2026-03-05 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.110.0) · from [[Releases/Codex CLI/codex-cli-2026-03-05-rust-v0-110-0-github-293239637-d5d06302|0.110.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added a plugin system that can load skills, MCP entries, and app connectors from config or a local marketplace, with an install endpoint for enabling plugins from the app server. (#12864, #13333, #13401, #13422)

> Expanded app-server docs around service tiers, plugin installation, renaming unloaded threads, and the new `skills/changed` notification. (#13282, #13391, #13414, #13422)

> #13083 Enable analytics in codex exec and codex mcp-server @etraut-openai

> #12864 feat: load from plugins @xl-openai

> #13333 Refactor plugin config and cache path @xl-openai

> #13401 feat: load plugin apps @sayan-oai

> #13422 plugin: support local-based marketplace.json + install endpoint. @xl-openai

Source: https://github.com/openai/codex/releases/tag/rust-v0.110.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-03-05-12935-speed-up-subagent-startup-daveaitel-openai|♯12935 Speed up subagent startup @daveaitel-openai]] · Reliability and Performance
- [[Changes/Codex CLI/2026-03-05-2-model-support-changes-in-rust-v0-110-0|2 Model Support changes in rust-v0.110.0]] · Model Support
- [[Changes/Codex CLI/2026-03-05-13127-nit-disable-on-windows-jif-oai|♯13127 nit: disable on windows @jif-oai]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-03-05-13-agent-mode-changes-in-rust-v0-110-0|13 Agent Mode changes in rust-v0.110.0]] · Agent Mode
- [[Changes/Codex CLI/2026-03-05-13313-renaming-team-to-business-plan-during-tui-onboarding-bwanner-oai|♯13313 Renaming Team to Business plan during TUI onboarding @bwanner-oai]] · Interface Experience
- [[Changes/Codex CLI/2026-03-05-12383-add-new-scopes-to-login-adaley-openai|♯12383 add new scopes to login @adaley-openai]] · Account and Access
- [[Changes/Codex CLI/2026-03-05-4-files-and-data-changes-in-rust-v0-110-0|4 Files and Data changes in rust-v0.110.0]] · Files and Data
- [[Changes/Codex CLI/2026-03-05-13388-config-enforce-enterprise-feature-requirements-bolinfest|♯13388 config: enforce enterprise feature requirements @bolinfest]] · Enterprise and Administration
- [[Changes/Codex CLI/2026-03-05-7-developer-workflow-changes-in-rust-v0-110-0|7 Developer Workflow changes in rust-v0.110.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-03-05-5-memory-and-personalization-changes-in-rust-v0-110-0|5 Memory and Personalization changes in rust-v0.110.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-03-05-4-safety-and-privacy-changes-in-rust-v0-110-0|4 Safety and Privacy changes in rust-v0.110.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-03-05-3-context-window-changes-in-rust-v0-110-0|3 Context Window changes in rust-v0.110.0]] · Context Window
- [[Changes/Codex CLI/2026-03-05-71-other-changes-in-rust-v0-110-0|71 other changes in rust-v0.110.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-03-05 · Claude Code · [[Changes/Claude Code/2026-03-05-7-apps-and-integrations-changes-in-v2-1-69|7 Apps and Integrations changes in v2.1.69]]
- Later: 2026-03-05 · Codex CLI · [[Changes/Codex CLI/2026-03-05-5-apps-and-integrations-changes-in-rust-v0-111-0|5 Apps and Integrations changes in rust-v0.111.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-03-05-943812&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-03-05-7-apps-and-integrations-changes-in-rust-v0-110-0.md%0ACard%20ID%3A%20codex-cli-2026-03-05-943812%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.110.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->