---
card_id: codex-cli-2025-10-23-e8a3b5
date: '2025-10-23'
description: 'Codex CLI · 2025-10-23 · Apps and Integrations: 11 changes in 0.48.0
  — Many MCP improvements:'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 945
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ad9f49da4116d6d4715602fe0f42a8514a81c6159975eb50460e5e5a684a1e22
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2025-10-23-e8a3b5
  comparison: ''
  date: '2025-10-23'
  description: 'Codex CLI — 0.48.0: 11 Apps and Integrations changes'
  evidence:
  - quote: 'Many MCP improvements:'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: stdio servers now use a new client backed by the official [rust MCP sdk](https://github.com/modelcontextprotocol/rust-sdk)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: '[MCP] Render full MCP errors to the model by @gpeal in https://github.com/openai/codex/pull/5298'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: '[MCP] When MCP auth expires, prompt the user to log in again. by @gpeal
      in https://github.com/openai/codex/pull/5300'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: '[MCP] Prefix MCP tools names with `mcp__` by @gpeal in https://github.com/openai/codex/pull/5309'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: Expand approvals integration coverage by @pakrym-oai in https://github.com/openai/codex/pull/5358
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: 'feat: add images support to the Codex Typescript SDK by @needs in https://github.com/openai/codex/pull/5281'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: '[MCP] Add configuration options to enable or disable specific tools by
      @gpeal in https://github.com/openai/codex/pull/5367'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: '[MCP] Dedicated error message for GitHub MCPs missing a personal access
      token by @gpeal in https://github.com/openai/codex/pull/5393'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: '[MCP] Bump rmcp to 0.8.2 by @gpeal in https://github.com/openai/codex/pull/5423'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: '[MCP] Remove the legacy stdio client in favor of rmcp by @gpeal in https://github.com/openai/codex/pull/5529'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 11-apps-and-integrations-changes-in-rust-v0-48-0
  source_release: codex-cli-2025-10-23-rust-v0-48-0-github-256860123-ffacccba
  source_type: github_releases
  theme: apps-integrations
  title: 11 Apps and Integrations changes in rust-v0.48.0
  type: change
related_changes:
- '[[Changes/Dify/2025-10-22-12-apps-and-integrations-changes-in-1-9-2|12 Apps and
  Integrations changes in 1.9.2]]'
- '[[Changes/Gemini CLI/2025-10-22-7-apps-and-integrations-changes-in-v0-10-0|7 Apps
  and Integrations changes in v0.10.0]]'
- '[[Changes/Cline/2025-10-23-3-apps-and-integrations-changes-in-v3-34-0|3 Apps and
  Integrations changes in v3.34.0]]'
source_release: '[[Releases/Codex CLI/codex-cli-2025-10-23-rust-v0-48-0-github-256860123-ffacccba|codex-cli-2025-10-23-rust-v0-48-0-github-256860123-ffacccba]]'
source_type: github_releases
theme: apps-integrations
title: 11 Apps and Integrations changes in rust-v0.48.0
type: change
---

<!-- chronolog:begin region="header" -->
# 11 Apps and Integrations changes in rust-v0.48.0

**Codex CLI** · 2025-10-23 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.48.0) · from [[Releases/Codex CLI/codex-cli-2025-10-23-rust-v0-48-0-github-256860123-ffacccba|0.48.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Many MCP improvements:

> stdio servers now use a new client backed by the official [rust MCP sdk](https://github.com/modelcontextprotocol/rust-sdk)

> [MCP] Render full MCP errors to the model by @gpeal in https://github.com/openai/codex/pull/5298

> [MCP] When MCP auth expires, prompt the user to log in again. by @gpeal in https://github.com/openai/codex/pull/5300

> [MCP] Prefix MCP tools names with `mcp__` by @gpeal in https://github.com/openai/codex/pull/5309

> Expand approvals integration coverage by @pakrym-oai in https://github.com/openai/codex/pull/5358

> feat: add images support to the Codex Typescript SDK by @needs in https://github.com/openai/codex/pull/5281

> [MCP] Add configuration options to enable or disable specific tools by @gpeal in https://github.com/openai/codex/pull/5367

> [MCP] Dedicated error message for GitHub MCPs missing a personal access token by @gpeal in https://github.com/openai/codex/pull/5393

> [MCP] Bump rmcp to 0.8.2 by @gpeal in https://github.com/openai/codex/pull/5423

> [MCP] Remove the legacy stdio client in favor of rmcp by @gpeal in https://github.com/openai/codex/pull/5529

Source: https://github.com/openai/codex/releases/tag/rust-v0.48.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2025-10-23-tui-drop-citation-rendering-by-nornagon-openai-in-https-github-com-openai-codex|tui: drop citation rendering]] · Interface Experience
- [[Changes/Codex CLI/2025-10-23-3-account-and-access-changes-in-rust-v0-48-0|3 Account and Access changes in rust-v0.48.0]] · Account and Access
- [[Changes/Codex CLI/2025-10-23-2-agent-mode-changes-in-rust-v0-48-0|2 Agent Mode changes in rust-v0.48.0]] · Agent Mode
- [[Changes/Codex CLI/2025-10-23-chore-ci-speed-up-macos-builds-by-using-larger-runner-by-javisoto-in-https-githu|chore(ci): Speed up macOS builds by using larger runner]] · Reliability and Performance
- [[Changes/Codex CLI/2025-10-23-auto-compact-at-90-by-aibrahim-oai-in-https-github-com-openai-codex-pull-5292|Auto compact at ~90%]] · Context Window
- [[Changes/Codex CLI/2025-10-23-docs-document-exec-json-events-by-tibo-openai-in-https-github-com-openai-codex-p|docs: document exec json events]] · Files and Data
- [[Changes/Codex CLI/2025-10-23-2-safety-and-privacy-changes-in-rust-v0-48-0|2 Safety and Privacy changes in rust-v0.48.0]] · Safety and Privacy
- [[Changes/Codex CLI/2025-10-23-3-model-support-changes-in-rust-v0-48-0|3 Model Support changes in rust-v0.48.0]] · Model Support
- [[Changes/Codex CLI/2025-10-23-4-developer-workflow-changes-in-rust-v0-48-0|4 Developer Workflow changes in rust-v0.48.0]] · Developer Workflow
- [[Changes/Codex CLI/2025-10-23-45-other-changes-in-rust-v0-48-0|45 other changes in rust-v0.48.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2025-10-23 · Cline · [[Changes/Cline/2025-10-23-3-apps-and-integrations-changes-in-v3-34-0|3 Apps and Integrations changes in v3.34.0]]
- Later: 2025-10-25 · Codex CLI · [[Changes/Codex CLI/2025-10-25-3-apps-and-integrations-changes-in-rust-v0-50-0|3 Apps and Integrations changes in rust-v0.50.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2025-10-23-e8a3b5&body=Card%3A%20Changes%2FCodex%20CLI%2F2025-10-23-11-apps-and-integrations-changes-in-rust-v0-48-0.md%0ACard%20ID%3A%20codex-cli-2025-10-23-e8a3b5%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.48.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->