---
card_id: codex-cli-2026-06-15-ba8cba
date: '2026-06-15'
description: 'Codex CLI · 2026-06-15 · Account and Access: 5 changes in 0.140.0 —
  Added managed Amazon Bedrock API-key authentication and encrypted local storage
  for CLI and…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1173
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a57f46bb00ea662bee81f9a4b1de51191f325f7afec6aa845f3df89c8b891a8e
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-06-15-ba8cba
  comparison: ''
  date: '2026-06-15'
  description: 'Codex CLI — 0.140.0: 5 Account and Access changes'
  evidence:
  - quote: 'Added managed Amazon Bedrock API-key authentication and encrypted local
      storage for CLI and MCP OAuth credentials. (#27443, #27689, #27504, #27535,
      #27539, #27541)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: 'Improved MCP reliability by retrying transient startup failures, reporting
      unusable OAuth credentials as logged out, and preserving explicitly disabled
      servers. (#25147, #26713, #27414)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#26713 [codex] Report unusable MCP OAuth credentials as logged out @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27674 [login] revoke existing auth before starting login @cooper-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27541 feat: use encrypted local secrets for MCP OAuth @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 5-account-and-access-changes-in-rust-v0-140-0
  source_release: codex-cli-2026-06-15-rust-v0-140-0-github-339797498-eb64f8cb
  source_type: github_releases
  theme: account-access
  title: 5 Account and Access changes in rust-v0.140.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-06-08-2-account-and-access-changes-in-rust-v0-138-0|2
  Account and Access changes in rust-v0.138.0]]'
- '[[Changes/GitHub Copilot CLI/2026-06-09-mcp-oauth-re-authentication-correctly-uses-the-saved-oauth-client-id-for-remote|MCP
  OAuth re-authentication correctly uses the saved OAuth client ID for remote servers]]'
- '[[Changes/GitHub Copilot CLI/2026-06-13-remote-mcp-oauth-servers-start-only-once-per-matching-config-instead-of-restarti|Remote
  MCP OAuth servers start only once per matching config instead of restarting…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-06-15-rust-v0-140-0-github-339797498-eb64f8cb|codex-cli-2026-06-15-rust-v0-140-0-github-339797498-eb64f8cb]]'
source_type: github_releases
theme: account-access
title: 5 Account and Access changes in rust-v0.140.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Account and Access changes in rust-v0.140.0

**Codex CLI** · 2026-06-15 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.140.0) · from [[Releases/Codex CLI/codex-cli-2026-06-15-rust-v0-140-0-github-339797498-eb64f8cb|0.140.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added managed Amazon Bedrock API-key authentication and encrypted local storage for CLI and MCP OAuth credentials. (#27443, #27689, #27504, #27535, #27539, #27541)

> Improved MCP reliability by retrying transient startup failures, reporting unusable OAuth credentials as logged out, and preserving explicitly disabled servers. (#25147, #26713, #27414)

> #26713 [codex] Report unusable MCP OAuth credentials as logged out @anp-oai

> #27674 [login] revoke existing auth before starting login @cooper-oai

> #27541 feat: use encrypted local secrets for MCP OAuth @celia-oai

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
- [[Changes/Codex CLI/2026-06-15-11-agent-mode-changes-in-rust-v0-140-0|11 Agent Mode changes in rust-v0.140.0]] · Agent Mode
- [[Changes/Codex CLI/2026-06-15-3-interface-experience-changes-in-rust-v0-140-0|3 Interface Experience changes in rust-v0.140.0]] · Interface Experience
- [[Changes/Codex CLI/2026-06-15-35-apps-and-integrations-changes-in-rust-v0-140-0|35 Apps and Integrations changes in rust-v0.140.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-06-15-4-model-support-changes-in-rust-v0-140-0|4 Model Support changes in rust-v0.140.0]] · Model Support
- [[Changes/Codex CLI/2026-06-15-clarified-contributor-guidance-around-keeping-crate-apis-narrow-and-supporting-l|Clarified contributor guidance around keeping crate APIs narrow and supporting…]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-06-15-27490-remove-tui-legacy-windows-sandbox-dependency-etraut-openai|♯27490 Remove TUI legacy Windows sandbox dependency @etraut-openai]] · Safety and Privacy
- [[Changes/Codex CLI/2026-06-15-6-developer-workflow-changes-in-rust-v0-140-0|6 Developer Workflow changes in rust-v0.140.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-06-15-2-voice-and-audio-changes-in-rust-v0-140-0|2 Voice and Audio changes in rust-v0.140.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-06-15-121-other-changes-in-rust-v0-140-0|121 other changes in rust-v0.140.0]] · Other changes
- [[Changes/Codex CLI/2026-06-15-added-usage-views-for-daily-weekly-and-cumulative-account-token-activity-27925|Added /usage views for daily, weekly, and cumulative account token activity]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-06-13 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-06-13-remote-mcp-oauth-servers-start-only-once-per-matching-config-instead-of-restarti|Remote MCP OAuth servers start only once per matching config instead of restarting…]]
- Later: 2026-06-16 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-06-16-2-account-and-access-changes-in-v1-0-63|2 Account and Access changes in v1.0.63]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-06-15-ba8cba&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-06-15-5-account-and-access-changes-in-rust-v0-140-0.md%0ACard%20ID%3A%20codex-cli-2026-06-15-ba8cba%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.140.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->