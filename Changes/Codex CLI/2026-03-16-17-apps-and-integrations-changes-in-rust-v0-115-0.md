---
card_id: codex-cli-2026-03-16-0341af
date: '2026-03-16'
description: 'Codex CLI · 2026-03-16 · Apps and Integrations: 17 changes in 0.115.0
  — The v2 app-server now exposes filesystem RPCs for file reads, writes, copies,
  directory…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1089
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8c3e69c28a4bddf684ff6e44b5544d04419987f7be28c21334dd3c8385d41db8
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-03-16-0341af
  comparison: ''
  date: '2026-03-16'
  description: 'Codex CLI — 0.115.0: 17 Apps and Integrations changes'
  evidence:
  - quote: 'The v2 app-server now exposes filesystem RPCs for file reads, writes,
      copies, directory operations, and path watching, and there is a new Python SDK
      for integrating with that API. (#14245, #14435)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: 'MCP and elicitation flows are more robust, with safer tool-name normalization
      and preserved `tool_params` in approval prompts. (#14491, #14605, #14769)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14407 chore: use AVAILABLE and ON_INSTALL as default plugin install and
      auth policies @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14287 [apps] Add tool_suggest tool. @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14427 feat: refactor on openai-curated plugins. @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14435 Add Python app-server SDK @shaqayeq-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14491 Fix MCP tool calling @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14445 feat: add plugin/read. @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14531 Add plugin usage telemetry @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14541 chore: clarify plugin + app copy in model instructions @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14304 Override local apps settings with requirements.toml settings @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14605 Normalize MCP tool names to code-mode safe form @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14532 [hooks] stop continuation & stop_hook_active mechanics @eternal-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14609 move plugin/skill instructions into dev msg and reorder @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14646 Refresh Python SDK generated types @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14647 [apps] Add tool call meta. @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14732 [apps] Improve search tool fallback. @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 17-apps-and-integrations-changes-in-rust-v0-115-0
  source_release: codex-cli-2026-03-16-rust-v0-115-0-github-297641413-c704d9db
  source_type: github_releases
  theme: apps-integrations
  title: 17 Apps and Integrations changes in rust-v0.115.0
  type: change
related_changes:
- '[[Changes/Cline/2026-03-12-hooks-reintroduced-feature-toggle|Hooks: reintroduced
  feature toggle]]'
- '[[Changes/GitHub Copilot CLI/2026-03-13-4-apps-and-integrations-changes-in-v1-0-5|4
  Apps and Integrations changes in v1.0.5]]'
- '[[Changes/Claude Code/2026-03-14-4-apps-and-integrations-changes-in-v2-1-76|4 Apps
  and Integrations changes in v2.1.76]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-03-16-rust-v0-115-0-github-297641413-c704d9db|codex-cli-2026-03-16-rust-v0-115-0-github-297641413-c704d9db]]'
source_type: github_releases
theme: apps-integrations
title: 17 Apps and Integrations changes in rust-v0.115.0
type: change
---

<!-- chronolog:begin region="header" -->
# 17 Apps and Integrations changes in rust-v0.115.0

**Codex CLI** · 2026-03-16 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.115.0) · from [[Releases/Codex CLI/codex-cli-2026-03-16-rust-v0-115-0-github-297641413-c704d9db|0.115.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> The v2 app-server now exposes filesystem RPCs for file reads, writes, copies, directory operations, and path watching, and there is a new Python SDK for integrating with that API. (#14245, #14435)

> MCP and elicitation flows are more robust, with safer tool-name normalization and preserved `tool_params` in approval prompts. (#14491, #14605, #14769)

> #14407 chore: use AVAILABLE and ON_INSTALL as default plugin install and auth policies @sayan-oai

> #14287 [apps] Add tool_suggest tool. @mzeng-openai

> #14427 feat: refactor on openai-curated plugins. @xl-openai

> #14435 Add Python app-server SDK @shaqayeq-oai

> #14491 Fix MCP tool calling @pakrym-oai

> #14445 feat: add plugin/read. @xl-openai

> #14531 Add plugin usage telemetry @alexsong-oai

> #14541 chore: clarify plugin + app copy in model instructions @sayan-oai

> #14304 Override local apps settings with requirements.toml settings @canvrno-oai

> #14605 Normalize MCP tool names to code-mode safe form @pakrym-oai

> #14532 [hooks] stop continuation & stop_hook_active mechanics @eternal-openai

> #14609 move plugin/skill instructions into dev msg and reorder @sayan-oai

> #14646 Refresh Python SDK generated types @sayan-oai

> #14647 [apps] Add tool call meta. @mzeng-openai

> #14732 [apps] Improve search tool fallback. @mzeng-openai

Source: https://github.com/openai/codex/releases/tag/rust-v0.115.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-03-16-2-context-window-changes-in-rust-v0-115-0|2 Context Window changes in rust-v0.115.0]] · Context Window
- [[Changes/Codex CLI/2026-03-16-16-agent-mode-changes-in-rust-v0-115-0|16 Agent Mode changes in rust-v0.115.0]] · Agent Mode
- [[Changes/Codex CLI/2026-03-16-2-mobile-and-desktop-changes-in-rust-v0-115-0|2 Mobile and Desktop changes in rust-v0.115.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-03-16-4-voice-and-audio-changes-in-rust-v0-115-0|4 Voice and Audio changes in rust-v0.115.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-03-16-14493-memories-focus-write-prompts-on-user-preferences-andi-oai|♯14493 memories: focus write prompts on user preferences @andi-oai]] · Memory and Personalization
- [[Changes/Codex CLI/2026-03-16-9-safety-and-privacy-changes-in-rust-v0-115-0|9 Safety and Privacy changes in rust-v0.115.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-03-16-5-model-support-changes-in-rust-v0-115-0|5 Model Support changes in rust-v0.115.0]] · Model Support
- [[Changes/Codex CLI/2026-03-16-2-account-and-access-changes-in-rust-v0-115-0|2 Account and Access changes in rust-v0.115.0]] · Account and Access
- [[Changes/Codex CLI/2026-03-16-2-developer-workflow-changes-in-rust-v0-115-0|2 Developer Workflow changes in rust-v0.115.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-03-16-14410-make-collab-model-metadata-accurate-on-completion-aibrahim-oai|♯14410 Make collab model metadata accurate on completion @aibrahim-oai]] · Interface Experience
- [[Changes/Codex CLI/2026-03-16-70-other-changes-in-rust-v0-115-0|70 other changes in rust-v0.115.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-03-14 · Claude Code · [[Changes/Claude Code/2026-03-14-4-apps-and-integrations-changes-in-v2-1-76|4 Apps and Integrations changes in v2.1.76]]
- Later: 2026-03-16 · ElevenLabs · [[Changes/ElevenLabs/2026-03-16-javascript-sdk|JavaScript SDK]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-03-16-0341af&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-03-16-17-apps-and-integrations-changes-in-rust-v0-115-0.md%0ACard%20ID%3A%20codex-cli-2026-03-16-0341af%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.115.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->