---
card_id: codex-cli-2026-09-03-f1c6e3
date: '2026-09-03'
description: 'Codex CLI · 2026-09-03 · Apps and Integrations: 18 changes in 0.153.0
  — The plugin CLI can list, install, and remove plugins from remote marketplaces…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1260
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 511d2f4e134f616a68649b9958356466d0c9e28fc8b1a5fa114cf63db936d3f8
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-09-03-f1c6e3
  comparison: ''
  date: '2026-09-03'
  description: 'Codex CLI — 0.153.0: 18 Apps and Integrations changes'
  evidence:
  - quote: The plugin CLI can list, install, and remove plugins from remote marketplaces.
      ([#42150](https://github.com/openai/codex/pull/42150))
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: Remembered MCP tool approvals are scoped to the selected app account, and
      relative MCP executable paths start more reliably on macOS. ([#42133](https://github.com/openai/codex/pull/42133),
      [#42117](https://github.com/openai/codex/pull/42117))
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#41892](https://github.com/openai/codex/pull/41892) Retain the MCP client
      for event streams'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#41899](https://github.com/openai/codex/pull/41899) Keep MCP event subscriptions
      alive after task unloading'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#41906](https://github.com/openai/codex/pull/41906) Add a manager for
      MCP event streams'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#41949](https://github.com/openai/codex/pull/41949) Add plugin reconciliation
      app-server API'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#41953](https://github.com/openai/codex/pull/41953) Enforce marketplace
      source policy for curated plugins'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#42047](https://github.com/openai/codex/pull/42047) Add per-account approval
      settings for apps'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#42054](https://github.com/openai/codex/pull/42054) Honor explicit account
      selectors for Apps tool calls'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#42056](https://github.com/openai/codex/pull/42056) Honor app link settings
      for MCP tool approvals'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#42100](https://github.com/openai/codex/pull/42100) Prefer remote Sites
      over the bundled plugin'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#42110](https://github.com/openai/codex/pull/42110) Treat bundled cleanup
      hooks as built-ins'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#42114](https://github.com/openai/codex/pull/42114) Centralize remote
      plugin mutations in `PluginsManager`'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#42117](https://github.com/openai/codex/pull/42117) Fix relative MCP
      server spawning on macOS'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#42126](https://github.com/openai/codex/pull/42126) Ignore non-JSON files
      in plugin catalog test helpers'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#42133](https://github.com/openai/codex/pull/42133) Scope session MCP
      approvals to app account links'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#42134](https://github.com/openai/codex/pull/42134) Include app link
      metadata in MCP approval elicitations'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#42150](https://github.com/openai/codex/pull/42150) Support remote marketplaces
      in the plugin CLI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 18-apps-and-integrations-changes-in-rust-v0-153-0
  source_release: codex-cli-2026-09-03-rust-v0-153-0-github-381669913-72d3437f
  source_type: github_releases
  theme: apps-integrations
  title: 18 Apps and Integrations changes in rust-v0.153.0
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-09-03-today-we-added-the-zendesk-and-onenote-plugins-in-the-plugin-directory-the-zende-012cbd|Zendesk
  & OneNote Plugins in ChatGPT and Codex Beta]]'
- '[[Changes/Claude Code/2026-09-03-4-apps-and-integrations-changes-in-v2-1-260|4
  Apps and Integrations changes in v2.1.260]]'
- '[[Changes/Claude Code/2026-09-03-added-reload-plugins-to-headless-sessions-so-it-appears-in-the-claude-code-deskt|Added
  /reload-plugins to headless sessions, so it appears in the Claude Code…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-09-03-rust-v0-153-0-github-381669913-72d3437f|codex-cli-2026-09-03-rust-v0-153-0-github-381669913-72d3437f]]'
source_type: github_releases
theme: apps-integrations
title: 18 Apps and Integrations changes in rust-v0.153.0
type: change
---

<!-- chronolog:begin region="header" -->
# 18 Apps and Integrations changes in rust-v0.153.0

**Codex CLI** · 2026-09-03 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.153.0) · from [[Releases/Codex CLI/codex-cli-2026-09-03-rust-v0-153-0-github-381669913-72d3437f|0.153.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> The plugin CLI can list, install, and remove plugins from remote marketplaces. ([#42150](https://github.com/openai/codex/pull/42150))

> Remembered MCP tool approvals are scoped to the selected app account, and relative MCP executable paths start more reliably on macOS. ([#42133](https://github.com/openai/codex/pull/42133), [#42117](https://github.com/openai/codex/pull/42117))

> [#41892](https://github.com/openai/codex/pull/41892) Retain the MCP client for event streams

> [#41899](https://github.com/openai/codex/pull/41899) Keep MCP event subscriptions alive after task unloading

> [#41906](https://github.com/openai/codex/pull/41906) Add a manager for MCP event streams

> [#41949](https://github.com/openai/codex/pull/41949) Add plugin reconciliation app-server API

> [#41953](https://github.com/openai/codex/pull/41953) Enforce marketplace source policy for curated plugins

> [#42047](https://github.com/openai/codex/pull/42047) Add per-account approval settings for apps

> [#42054](https://github.com/openai/codex/pull/42054) Honor explicit account selectors for Apps tool calls

> [#42056](https://github.com/openai/codex/pull/42056) Honor app link settings for MCP tool approvals

> [#42100](https://github.com/openai/codex/pull/42100) Prefer remote Sites over the bundled plugin

> [#42110](https://github.com/openai/codex/pull/42110) Treat bundled cleanup hooks as built-ins

> [#42114](https://github.com/openai/codex/pull/42114) Centralize remote plugin mutations in `PluginsManager`

> [#42117](https://github.com/openai/codex/pull/42117) Fix relative MCP server spawning on macOS

> [#42126](https://github.com/openai/codex/pull/42126) Ignore non-JSON files in plugin catalog test helpers

> [#42133](https://github.com/openai/codex/pull/42133) Scope session MCP approvals to app account links

> [#42134](https://github.com/openai/codex/pull/42134) Include app link metadata in MCP approval elicitations

> [#42150](https://github.com/openai/codex/pull/42150) Support remote marketplaces in the plugin CLI

Source: https://github.com/openai/codex/releases/tag/rust-v0.153.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-09-03-42140-https-github-com-openai-codex-pull-42140-add-redo-support-to-vim-composer|♯42140((source link) Add redo support to Vim…]] · Projects and Workspaces
- [[Changes/Codex CLI/2026-09-03-3-interface-experience-changes-in-rust-v0-153-0|3 Interface Experience changes in rust-v0.153.0]] · Interface Experience
- [[Changes/Codex CLI/2026-09-03-2-model-support-changes-in-rust-v0-153-0|2 Model Support changes in rust-v0.153.0]] · Model Support
- [[Changes/Codex CLI/2026-09-03-5-voice-and-audio-changes-in-rust-v0-153-0|5 Voice and Audio changes in rust-v0.153.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-09-03-42128-https-github-com-openai-codex-pull-42128-prepare-mcp-connections-for-coord|♯42128((source link) Prepare MCP connections…]] · Account and Access
- [[Changes/Codex CLI/2026-09-03-5-developer-workflow-changes-in-rust-v0-153-0|5 Developer Workflow changes in rust-v0.153.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-09-03-6-safety-and-privacy-changes-in-rust-v0-153-0|6 Safety and Privacy changes in rust-v0.153.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-09-03-41944-https-github-com-openai-codex-pull-41944-emit-turn-cost-telemetry-for-chat|♯41944((source link) Emit turn cost telemetry…]] · Pricing Model
- [[Changes/Codex CLI/2026-09-03-6-context-window-changes-in-rust-v0-153-0|6 Context Window changes in rust-v0.153.0]] · Context Window
- [[Changes/Codex CLI/2026-09-03-6-collaboration-changes-in-rust-v0-153-0|6 Collaboration changes in rust-v0.153.0]] · Collaboration
- [[Changes/Codex CLI/2026-09-03-4-agent-mode-changes-in-rust-v0-153-0|4 Agent Mode changes in rust-v0.153.0]] · Agent Mode
- [[Changes/Codex CLI/2026-09-03-42068-https-github-com-openai-codex-pull-42068-detect-standalone-installs-from-t|♯42068((source link) Detect standalone installs…]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-09-03-50-other-changes-in-rust-v0-153-0|50 other changes in rust-v0.153.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-09-03 · Claude Code · [[Changes/Claude Code/2026-09-03-added-reload-plugins-to-headless-sessions-so-it-appears-in-the-claude-code-deskt|Added /reload-plugins to headless sessions, so it appears in the Claude Code…]]
- Later: 2026-09-04 · Claude Code · [[Changes/Claude Code/2026-09-04-vscode-added-an-add-server-form-and-a-remove-action-to-the-mcp-servers-dialog-so|VSCode Added an Add server form and a Remove action to the MCP servers dialog…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-09-03-f1c6e3&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-09-03-18-apps-and-integrations-changes-in-rust-v0-153-0.md%0ACard%20ID%3A%20codex-cli-2026-09-03-f1c6e3%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.153.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->