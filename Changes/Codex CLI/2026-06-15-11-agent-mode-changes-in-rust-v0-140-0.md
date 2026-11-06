---
card_id: codex-cli-2026-06-15-8a2c15
date: '2026-06-15'
description: 'Codex CLI · 2026-06-15 · Agent Mode: 11 changes in 0.140.0 — Added permanent
  session deletion through `codex delete`, `/delete`, and app-server…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1075
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 123c7ad912dd047126616b647fc9d6a5afc697378ad496ecd2d5a5d1770c04c1
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-06-15-8a2c15
  comparison: ''
  date: '2026-06-15'
  description: 'Codex CLI — 0.140.0: 11 Agent Mode changes'
  evidence:
  - quote: 'Added permanent session deletion through `codex delete`, `/delete`, and
      app-server `thread/delete`, with confirmation safeguards and subagent cleanup.
      (#25018, #27476)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27007 multi-agent: add path-based v2 activity tracking @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27166 app-server: clear stale thread watches after v2 agent interruption
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27173 app-server: reject direct input to multi-agent v2 sub-agents @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27375 [codex] Tag multi-agent spawn metrics with version @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27064 [codex] remove blocking external agent migration flow @stefanstokic-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27071 [codex] add /import for external agents @stefanstokic-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27569 multi-agent: move concurrency guidance into v2 usage hints @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27696 [codex] Load AGENTS.md from all bound environments @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27830 Support plaintext agent messages @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27966 Specify platform support in AGENTS.md @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 11-agent-mode-changes-in-rust-v0-140-0
  source_release: codex-cli-2026-06-15-rust-v0-140-0-github-339797498-eb64f8cb
  source_type: github_releases
  theme: agent-mode
  title: 11 Agent Mode changes in rust-v0.140.0
  type: change
related_changes:
- '[[Changes/Replit/2026-06-12-agent|Agent]]'
- '[[Changes/GitHub Copilot CLI/2026-06-13-4-agent-mode-changes-in-v1-0-62|4 Agent
  Mode changes in v1.0.62]]'
- '[[Changes/Claude Code/2026-06-15-2-agent-mode-changes-in-v2-1-178|2 Agent Mode
  changes in v2.1.178]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-06-15-rust-v0-140-0-github-339797498-eb64f8cb|codex-cli-2026-06-15-rust-v0-140-0-github-339797498-eb64f8cb]]'
source_type: github_releases
theme: agent-mode
title: 11 Agent Mode changes in rust-v0.140.0
type: change
---

<!-- chronolog:begin region="header" -->
# 11 Agent Mode changes in rust-v0.140.0

**Codex CLI** · 2026-06-15 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.140.0) · from [[Releases/Codex CLI/codex-cli-2026-06-15-rust-v0-140-0-github-339797498-eb64f8cb|0.140.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added permanent session deletion through `codex delete`, `/delete`, and app-server `thread/delete`, with confirmation safeguards and subagent cleanup. (#25018, #27476)

> #27007 multi-agent: add path-based v2 activity tracking @jif-oai

> #27166 app-server: clear stale thread watches after v2 agent interruption @jif-oai

> #27173 app-server: reject direct input to multi-agent v2 sub-agents @jif-oai

> #27375 [codex] Tag multi-agent spawn metrics with version @jif-oai

> #27064 [codex] remove blocking external agent migration flow @stefanstokic-oai

> #27071 [codex] add /import for external agents @stefanstokic-oai

> #27569 multi-agent: move concurrency guidance into v2 usage hints @jif-oai

> #27696 [codex] Load AGENTS.md from all bound environments @anp-oai

> #27830 Support plaintext agent messages @jif-oai

> #27966 Specify platform support in AGENTS.md @anp-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.140.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-06-15-27245-image-add-shared-data-url-preparation-utilities-fjord-oai|♯27245 image: add shared data URL preparation utilities @fjord-oai]] · Collaboration
- [[Changes/Codex CLI/2026-06-15-27501-codex-expand-hosted-web-search-citation-guidance-yuning-oai|♯27501 codex Expand hosted web search citation guidance @yuning-oai]] · Search and Browsing
- [[Changes/Codex CLI/2026-06-15-3-reliability-and-performance-changes-in-rust-v0-140-0|3 Reliability and Performance changes in rust-v0.140.0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-06-15-2-editor-experience-changes-in-rust-v0-140-0|2 Editor Experience changes in rust-v0.140.0]] · Editor Experience
- [[Changes/Codex CLI/2026-06-15-7-context-window-changes-in-rust-v0-140-0|7 Context Window changes in rust-v0.140.0]] · Context Window
- [[Changes/Codex CLI/2026-06-15-added-import-for-selectively-importing-setup-project-configuration-and-recent-ch|Added /import for selectively importing setup, project configuration, and recent…]] · Interface Experience
- [[Changes/Codex CLI/2026-06-15-27920-handle-standalone-image-generation-failures-as-terminal-items-won-openai|♯27920 Handle standalone image generation failures as terminal items @won-openai]] · Image Generation
- [[Changes/Codex CLI/2026-06-15-27129-feat-use-provider-defaults-for-memory-models-celia-oai|♯27129 feat: use provider defaults for memory models @celia-oai]] · Memory and Personalization
- [[Changes/Codex CLI/2026-06-15-3-interface-experience-changes-in-rust-v0-140-0|3 Interface Experience changes in rust-v0.140.0]] · Interface Experience
- [[Changes/Codex CLI/2026-06-15-35-apps-and-integrations-changes-in-rust-v0-140-0|35 Apps and Integrations changes in rust-v0.140.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-06-15-5-account-and-access-changes-in-rust-v0-140-0|5 Account and Access changes in rust-v0.140.0]] · Account and Access
- [[Changes/Codex CLI/2026-06-15-4-model-support-changes-in-rust-v0-140-0|4 Model Support changes in rust-v0.140.0]] · Model Support
- [[Changes/Codex CLI/2026-06-15-clarified-contributor-guidance-around-keeping-crate-apis-narrow-and-supporting-l|Clarified contributor guidance around keeping crate APIs narrow and supporting…]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-06-15-27490-remove-tui-legacy-windows-sandbox-dependency-etraut-openai|♯27490 Remove TUI legacy Windows sandbox dependency @etraut-openai]] · Safety and Privacy
- [[Changes/Codex CLI/2026-06-15-6-developer-workflow-changes-in-rust-v0-140-0|6 Developer Workflow changes in rust-v0.140.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-06-15-2-voice-and-audio-changes-in-rust-v0-140-0|2 Voice and Audio changes in rust-v0.140.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-06-15-121-other-changes-in-rust-v0-140-0|121 other changes in rust-v0.140.0]] · Other changes
- [[Changes/Codex CLI/2026-06-15-added-usage-views-for-daily-weekly-and-cumulative-account-token-activity-27925|Added /usage views for daily, weekly, and cumulative account token activity]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-06-15 · Claude Code · [[Changes/Claude Code/2026-06-15-2-agent-mode-changes-in-v2-1-178|2 Agent Mode changes in v2.1.178]]
- Later: 2026-06-15 · ElevenLabs · [[Changes/ElevenLabs/2026-06-15-elevenagents|ElevenAgents]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-06-15-8a2c15&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-06-15-11-agent-mode-changes-in-rust-v0-140-0.md%0ACard%20ID%3A%20codex-cli-2026-06-15-8a2c15%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.140.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->