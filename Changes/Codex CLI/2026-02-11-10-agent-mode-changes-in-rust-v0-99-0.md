---
card_id: codex-cli-2026-02-11-aa4088
date: '2026-02-11'
description: 'Codex CLI · 2026-02-11 · Agent Mode: 10 changes in 0.99.0 — App-server
  clients now get dedicated APIs for steering active turns, listing experimental features…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 951
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d66a1c5be2f5352e07a66fe6579027b4ad9f9f33e6e947de1b698bc0f933a173
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-02-11-aa4088
  comparison: ''
  date: '2026-02-11'
  description: 'Codex CLI — 0.99.0: 10 Agent Mode changes'
  evidence:
  - quote: 'App-server clients now get dedicated APIs for steering active turns, listing
      experimental features, resuming agents, and opting out of specific notifications.
      (#10721, #10821, #10903, #11319)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: 'Expanded app-server docs and protocol references for `turn/steer`, experimental-feature
      discovery, `resume_agent`, notification opt-outs, and null `developer_instructions`
      normalization. (#10721, #10821, #10903, #10983, #11319)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10914 chore(app-server): update AGENTS.md for config + optional collection
      guidance @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10903 Add resume_agent collab tool @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11175 fix: do not show closed agents in `/agent` @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11173 chore: enable sub agents @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11230 Revert "chore: enable sub agents" @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11247 Adjust shell command timeouts for Windows @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11304 Fix spawn_agent input type @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11378 chore: rename codex-command to codex-shell-command @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 10-agent-mode-changes-in-rust-v0-99-0
  source_release: codex-cli-2026-02-11-rust-v0-99-0-github-285424682-f7f48016
  source_type: github_releases
  theme: agent-mode
  title: 10 Agent Mode changes in rust-v0.99.0
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-02-09-agents-platform|Agents Platform]]'
- '[[Changes/ElevenLabs/2026-02-09-agents-platform-7f0c0d|Agents Platform]]'
- '[[Changes/Gemini CLI/2026-02-10-4-agent-mode-changes-in-v0-28-0|4 Agent Mode changes
  in v0.28.0]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-02-11-rust-v0-99-0-github-285424682-f7f48016|codex-cli-2026-02-11-rust-v0-99-0-github-285424682-f7f48016]]'
source_type: github_releases
theme: agent-mode
title: 10 Agent Mode changes in rust-v0.99.0
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Agent Mode changes in rust-v0.99.0

**Codex CLI** · 2026-02-11 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.99.0) · from [[Releases/Codex CLI/codex-cli-2026-02-11-rust-v0-99-0-github-285424682-f7f48016|0.99.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> App-server clients now get dedicated APIs for steering active turns, listing experimental features, resuming agents, and opting out of specific notifications. (#10721, #10821, #10903, #11319)

> Expanded app-server docs and protocol references for `turn/steer`, experimental-feature discovery, `resume_agent`, notification opt-outs, and null `developer_instructions` normalization. (#10721, #10821, #10903, #10983, #11319)

> #10914 chore(app-server): update AGENTS.md for config + optional collection guidance @owenlin0

> #10903 Add resume_agent collab tool @jif-oai

> #11175 fix: do not show closed agents in `/agent` @jif-oai

> #11173 chore: enable sub agents @jif-oai

> #11230 Revert "chore: enable sub agents" @jif-oai

> #11247 Adjust shell command timeouts for Windows @dylan-hurd-oai

> #11304 Fix spawn_agent input type @jif-oai

> #11378 chore: rename codex-command to codex-shell-command @bolinfest

Source: https://github.com/openai/codex/releases/tag/rust-v0.99.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-02-11-3-search-and-browsing-changes-in-rust-v0-99-0|3 Search and Browsing changes in rust-v0.99.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-02-11-9-developer-workflow-changes-in-rust-v0-99-0|9 Developer Workflow changes in rust-v0.99.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-02-11-6-context-window-changes-in-rust-v0-99-0|6 Context Window changes in rust-v0.99.0]] · Context Window
- [[Changes/Codex CLI/2026-02-11-13-apps-and-integrations-changes-in-rust-v0-99-0|13 Apps and Integrations changes in rust-v0.99.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-02-11-8-safety-and-privacy-changes-in-rust-v0-99-0|8 Safety and Privacy changes in rust-v0.99.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-02-11-7-memory-and-personalization-changes-in-rust-v0-99-0|7 Memory and Personalization changes in rust-v0.99.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-02-11-enterprise-admin-requirements-can-now-restrict-web-search-modes-and-define-netwo|Enterprise/admin requirements can now restrict web search modes and define network…]] · Enterprise and Administration
- [[Changes/Codex CLI/2026-02-11-2-editor-experience-changes-in-rust-v0-99-0|2 Editor Experience changes in rust-v0.99.0]] · Editor Experience
- [[Changes/Codex CLI/2026-02-11-11294-chore-put-crypto-provider-logic-in-a-shared-crate-bolinfest|♯11294 chore: put crypto provider logic in a shared crate @bolinfest]] · Collaboration
- [[Changes/Codex CLI/2026-02-11-11336-always-expose-view-image-and-return-unsupported-image-input-error-aibrahim|♯11336 Always expose view_image and return unsupported image-input error @aibrahim-oai]] · Multimodal Input
- [[Changes/Codex CLI/2026-02-11-15-model-support-changes-in-rust-v0-99-0|15 Model Support changes in rust-v0.99.0]] · Model Support
- [[Changes/Codex CLI/2026-02-11-4-mobile-and-desktop-changes-in-rust-v0-99-0|4 Mobile and Desktop changes in rust-v0.99.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-02-11-8-interface-experience-changes-in-rust-v0-99-0|8 Interface Experience changes in rust-v0.99.0]] · Interface Experience
- [[Changes/Codex CLI/2026-02-11-added-statusline-to-configure-which-metadata-appears-in-the-tui-footer-interacti|Added /statusline to configure which metadata appears in the TUI footer interactively]] · Other changes
- [[Changes/Codex CLI/2026-02-11-116-other-changes-in-rust-v0-99-0|116 other changes in rust-v0.99.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-02-10 · Gemini CLI · [[Changes/Gemini CLI/2026-02-10-4-agent-mode-changes-in-v0-28-0|4 Agent Mode changes in v0.28.0]]
- Later: 2026-02-11 · Dify · [[Changes/Dify/2026-02-11-flexible-delivery-methods-human-input-forms-can-be-delivered-via-webapp-or-email|Flexible Delivery Methods: Human input forms can be delivered…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-02-11-aa4088&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-02-11-10-agent-mode-changes-in-rust-v0-99-0.md%0ACard%20ID%3A%20codex-cli-2026-02-11-aa4088%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.99.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->