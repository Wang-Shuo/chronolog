---
card_id: codex-cli-2026-02-04-df219d
date: '2026-02-04'
description: 'Codex CLI · 2026-02-04 · Apps and Integrations: 5 changes in 0.95.0
  — Completed migration off the deprecated `mcp-types` crate to `rmcp`-based protocol…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1049
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 49ff7e695ff8e4f6eb717e23a11afc6029153446e01a5ab875eed20d3585778c
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-02-04-df219d
  comparison: ''
  date: '2026-02-04'
  description: 'Codex CLI — 0.95.0: 5 Apps and Integrations changes'
  evidence:
  - quote: 'Completed migration off the deprecated `mcp-types` crate to `rmcp`-based
      protocol types/adapters, then removed the legacy crate. (#10356, #10349, #10357)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10356 feat: add MCP protocol types and rmcp adapters @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10349 feat: replace custom mcp-types crate with equivalents from rmcp
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10357 chore: remove deprecated mcp-types crate @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10289 [apps] Gateway MCP should be blocking. @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 5-apps-and-integrations-changes-in-rust-v0-95-0
  source_release: codex-cli-2026-02-04-rust-v0-95-0-github-282823276-932b0b6b
  source_type: github_releases
  theme: apps-integrations
  title: 5 Apps and Integrations changes in rust-v0.95.0
  type: change
related_changes:
- '[[Changes/Dify/2026-02-03-14-apps-and-integrations-changes-in-1-12-0|14 Apps and
  Integrations changes in 1.12.0]]'
- '[[Changes/GitHub Copilot CLI/2026-02-03-3-apps-and-integrations-changes-in-v0-0-401|3
  Apps and Integrations changes in v0.0.401]]'
- '[[Changes/GitHub Copilot CLI/2026-02-03-4-apps-and-integrations-changes-in-v0-0-402|4
  Apps and Integrations changes in v0.0.402]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-02-04-rust-v0-95-0-github-282823276-932b0b6b|codex-cli-2026-02-04-rust-v0-95-0-github-282823276-932b0b6b]]'
source_type: github_releases
theme: apps-integrations
title: 5 Apps and Integrations changes in rust-v0.95.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Apps and Integrations changes in rust-v0.95.0

**Codex CLI** · 2026-02-04 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.95.0) · from [[Releases/Codex CLI/codex-cli-2026-02-04-rust-v0-95-0-github-282823276-932b0b6b|0.95.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Completed migration off the deprecated `mcp-types` crate to `rmcp`-based protocol types/adapters, then removed the legacy crate. (#10356, #10349, #10357)

> #10356 feat: add MCP protocol types and rmcp adapters @bolinfest

> #10349 feat: replace custom mcp-types crate with equivalents from rmcp @bolinfest

> #10357 chore: remove deprecated mcp-types crate @bolinfest

> #10289 [apps] Gateway MCP should be blocking. @mzeng-openai

Source: https://github.com/openai/codex/releases/tag/rust-v0.95.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-02-04-10-developer-workflow-changes-in-rust-v0-95-0|10 Developer Workflow changes in rust-v0.95.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-02-04-10340-session-picker-shows-thread-name-if-set-pap-openai|♯10340 Session picker shows thread_name if set @pap-openai]] · Interface Experience
- [[Changes/Codex CLI/2026-02-04-2-context-window-changes-in-rust-v0-95-0|2 Context Window changes in rust-v0.95.0]] · Context Window
- [[Changes/Codex CLI/2026-02-04-10404-cleanup-collaboration-mode-variants-charley-oai|♯10404 Cleanup collaboration mode variants @charley-oai]] · Collaboration
- [[Changes/Codex CLI/2026-02-04-2-mobile-and-desktop-changes-in-rust-v0-95-0|2 Mobile and Desktop changes in rust-v0.95.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-02-04-2-model-support-changes-in-rust-v0-95-0|2 Model Support changes in rust-v0.95.0]] · Model Support
- [[Changes/Codex CLI/2026-02-04-4-agent-mode-changes-in-rust-v0-95-0|4 Agent Mode changes in rust-v0.95.0]] · Agent Mode
- [[Changes/Codex CLI/2026-02-04-10274-add-credits-tooltip-pakrym-oai|♯10274 Add credits tooltip @pakrym-oai]] · Pricing Model
- [[Changes/Codex CLI/2026-02-04-6-safety-and-privacy-changes-in-rust-v0-95-0|6 Safety and Privacy changes in rust-v0.95.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-02-04-2-search-and-browsing-changes-in-rust-v0-95-0|2 Search and Browsing changes in rust-v0.95.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-02-04-42-other-changes-in-rust-v0-95-0|42 other changes in rust-v0.95.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-02-03 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-02-03-4-apps-and-integrations-changes-in-v0-0-402|4 Apps and Integrations changes in v0.0.402]]
- Later: 2026-02-04 · Gemini CLI · [[Changes/Gemini CLI/2026-02-04-14-apps-and-integrations-changes-in-v0-27-0|14 Apps and Integrations changes in v0.27.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-02-04-df219d&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-02-04-5-apps-and-integrations-changes-in-rust-v0-95-0.md%0ACard%20ID%3A%20codex-cli-2026-02-04-df219d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.95.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->