---
card_id: codex-cli-2025-09-08-265688
date: '2025-09-08'
description: 'Codex CLI · 2025-09-08 · Apps and Integrations: 4 changes in 0.31.0
  — https://github.com/openai/codex/pull/3182 added support for a `startup_timeout_ms`
  option…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 900
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 40af3c0f24ed4ce54111be957da542755d9a4554cdef89dd0689eafbff6a097c
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2025-09-08-265688
  comparison: ''
  date: '2025-09-08'
  description: 'Codex CLI — 0.31.0: 4 Apps and Integrations changes'
  evidence:
  - quote: 'https://github.com/openai/codex/pull/3182 added support for a `startup_timeout_ms`
      option when declaring an MCP server [(docs)](https://github.com/openai/codex/blob/main/docs/config.md#mcp_servers),
      which has been a highly requested feature, particularly for Windows users:'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.31.0
  - quote: 'Thanks to @Bit-urd for adding more fault tolerance to MCP startup: https://github.com/openai/codex/pull/3243'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.31.0
  - quote: '[#3182] feat(mcp): per-server startup timeout'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.31.0
  - quote: '[#3320] Add a getUserAgent MCP method'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.31.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 4-apps-and-integrations-changes-in-rust-v0-31-0
  source_release: codex-cli-2025-09-08-rust-v0-31-0-github-245666045-ad57a22f
  source_type: github_releases
  theme: apps-integrations
  title: 4 Apps and Integrations changes in rust-v0.31.0
  type: change
related_changes:
- '[[Changes/Gemini CLI/2025-09-04-17-apps-and-integrations-changes-in-v0-3-0|17 Apps
  and Integrations changes in v0.3.0]]'
- '[[Changes/Codex CLI/2025-09-05-4-apps-and-integrations-changes-in-rust-v0-30-0|4
  Apps and Integrations changes in rust-v0.30.0]]'
- '[[Changes/Replit/2025-09-05-gcp-marketplace-integration|GCP Marketplace integration]]'
source_release: '[[Releases/Codex CLI/codex-cli-2025-09-08-rust-v0-31-0-github-245666045-ad57a22f|codex-cli-2025-09-08-rust-v0-31-0-github-245666045-ad57a22f]]'
source_type: github_releases
theme: apps-integrations
title: 4 Apps and Integrations changes in rust-v0.31.0
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Apps and Integrations changes in rust-v0.31.0

**Codex CLI** · 2025-09-08 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.31.0) · from [[Releases/Codex CLI/codex-cli-2025-09-08-rust-v0-31-0-github-245666045-ad57a22f|0.31.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> https://github.com/openai/codex/pull/3182 added support for a `startup_timeout_ms` option when declaring an MCP server [(docs)](https://github.com/openai/codex/blob/main/docs/config.md#mcp_servers), which has been a highly requested feature, particularly for Windows users:

> Thanks to @Bit-urd for adding more fault tolerance to MCP startup: https://github.com/openai/codex/pull/3243

> [#3182] feat(mcp): per-server startup timeout

> [#3320] Add a getUserAgent MCP method

Source: https://github.com/openai/codex/releases/tag/rust-v0.31.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2025-09-08-3217-added-logic-to-cancel-pending-oauth-login-to-free-up-localhost-port|♯3217 Added logic to cancel pending oauth login to free up localhost port]] · Account and Access
- [[Changes/Codex CLI/2025-09-08-3176-codex-respect-overrides-for-model-family-configuration-from-toml-file|♯3176 codex respect overrides for model family configuration from toml file]] · Model Support
- [[Changes/Codex CLI/2025-09-08-3211-fixes-image-pasting-from-finder-with-ctrl-v-on-macos|♯3211 fixes image pasting from Finder with ctrl+v on macOS]] · Mobile and Desktop
- [[Changes/Codex CLI/2025-09-08-2-developer-workflow-changes-in-rust-v0-31-0|2 Developer Workflow changes in rust-v0.31.0]] · Developer Workflow
- [[Changes/Codex CLI/2025-09-08-3221-move-token-usage-context-information-to-session-level|♯3221 Move token usage/context information to session level]] · Context Window
- [[Changes/Codex CLI/2025-09-08-18-other-changes-in-rust-v0-31-0|18 other changes in rust-v0.31.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2025-09-05 · Replit · [[Changes/Replit/2025-09-05-gcp-marketplace-integration|GCP Marketplace integration]]
- Later: 2025-09-08 · ElevenLabs · [[Changes/ElevenLabs/2025-09-08-mcp-server|MCP Server]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2025-09-08-265688&body=Card%3A%20Changes%2FCodex%20CLI%2F2025-09-08-4-apps-and-integrations-changes-in-rust-v0-31-0.md%0ACard%20ID%3A%20codex-cli-2025-09-08-265688%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.31.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->