---
card_id: codex-cli-2025-10-30-6bf4d7
date: '2025-10-30'
description: 'Codex CLI · 2025-10-30 · Apps and Integrations: 11 changes in 0.52.0
  — Images: client-side image resizing; prevent crashes with MIME verification; SDK
  image…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 952
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 272111a0d1b3333dffe7b54f6ec0bc4adfe740c8028b287ab74f84a595a6d4c3
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2025-10-30-6bf4d7
  comparison: ''
  date: '2025-10-30'
  description: 'Codex CLI — 0.52.0: 11 Apps and Integrations changes'
  evidence:
  - quote: 'Images: client-side image resizing; prevent crashes with MIME verification;
      SDK image forwarding tests re-enabled.'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: '[MCP] Remove the legacy stdio client in favor of rmcp in https://github.com/openai/codex/pull/5529'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: '[MCP] Update rmcp to 0.8.3 in https://github.com/openai/codex/pull/5542'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: '[MCP] Improve startup errors for timeouts and github in https://github.com/openai/codex/pull/5595'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: '[MCP] Redact environment variable values in /mcp and mcp get in https://github.com/openai/codex/pull/5648'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: '[MCP] Minor docs clarifications around stdio tokens in https://github.com/openai/codex/pull/5676'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: '[MCP] Render MCP tool call result images to the model in https://github.com/openai/codex/pull/5600'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: Truncate the content-item for mcp tools in https://github.com/openai/codex/pull/5835
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: 'chore: use anyhow::Result for all app-server integration tests in https://github.com/openai/codex/pull/5836'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: '[exec] Add MCP tool arguments and results in https://github.com/openai/codex/pull/5899'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: Re-enable SDK image forwarding test in https://github.com/openai/codex/pull/5934
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 11-apps-and-integrations-changes-in-rust-v0-52-0
  source_release: codex-cli-2025-10-30-rust-v0-52-0-github-258584762-83f2b559
  source_type: github_releases
  theme: apps-integrations
  title: 11 Apps and Integrations changes in rust-v0.52.0
  type: change
related_changes:
- '[[Changes/ElevenLabs/2025-10-27-javascript-sdk|JavaScript SDK]]'
- '[[Changes/GitHub Copilot CLI/2025-10-27-improve-handling-of-mcp-tools-containing-slashes|Improve
  handling of MCP tools containing slashes]]'
- '[[Changes/Gemini CLI/2025-10-29-7-apps-and-integrations-changes-in-v0-11-0|7 Apps
  and Integrations changes in v0.11.0]]'
source_release: '[[Releases/Codex CLI/codex-cli-2025-10-30-rust-v0-52-0-github-258584762-83f2b559|codex-cli-2025-10-30-rust-v0-52-0-github-258584762-83f2b559]]'
source_type: github_releases
theme: apps-integrations
title: 11 Apps and Integrations changes in rust-v0.52.0
type: change
---

<!-- chronolog:begin region="header" -->
# 11 Apps and Integrations changes in rust-v0.52.0

**Codex CLI** · 2025-10-30 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.52.0) · from [[Releases/Codex CLI/codex-cli-2025-10-30-rust-v0-52-0-github-258584762-83f2b559|0.52.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Images: client-side image resizing; prevent crashes with MIME verification; SDK image forwarding tests re-enabled.

> [MCP] Remove the legacy stdio client in favor of rmcp in https://github.com/openai/codex/pull/5529

> [MCP] Update rmcp to 0.8.3 in https://github.com/openai/codex/pull/5542

> [MCP] Improve startup errors for timeouts and github in https://github.com/openai/codex/pull/5595

> [MCP] Redact environment variable values in /mcp and mcp get in https://github.com/openai/codex/pull/5648

> [MCP] Minor docs clarifications around stdio tokens in https://github.com/openai/codex/pull/5676

> [MCP] Render MCP tool call result images to the model in https://github.com/openai/codex/pull/5600

> Truncate the content-item for mcp tools in https://github.com/openai/codex/pull/5835

> chore: use anyhow::Result for all app-server integration tests in https://github.com/openai/codex/pull/5836

> [exec] Add MCP tool arguments and results in https://github.com/openai/codex/pull/5899

> Re-enable SDK image forwarding test in https://github.com/openai/codex/pull/5934

Source: https://github.com/openai/codex/releases/tag/rust-v0.52.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2025-10-30-chore-speed-up-pipeline-in-https-github-com-openai-codex-pull-5812|chore: speed-up pipeline in (source link)]] · Reliability and Performance
- [[Changes/Codex CLI/2025-10-30-ability-to-buy-credits-for-more-usage-more-information-https-help-openai-com-en|Ability to buy credits for more usage]] · Pricing Model
- [[Changes/Codex CLI/2025-10-30-5-model-support-changes-in-rust-v0-52-0|5 Model Support changes in rust-v0.52.0]] · Model Support
- [[Changes/Codex CLI/2025-10-30-chore-decompose-submission-loop-in-https-github-com-openai-codex-pull-5854|chore: decompose submission loop in (source link)]] · Automation and Scheduling
- [[Changes/Codex CLI/2025-10-30-3-agent-mode-changes-in-rust-v0-52-0|3 Agent Mode changes in rust-v0.52.0]] · Agent Mode
- [[Changes/Codex CLI/2025-10-30-2-context-window-changes-in-rust-v0-52-0|2 Context Window changes in rust-v0.52.0]] · Context Window
- [[Changes/Codex CLI/2025-10-30-2-account-and-access-changes-in-rust-v0-52-0|2 Account and Access changes in rust-v0.52.0]] · Account and Access
- [[Changes/Codex CLI/2025-10-30-chore-config-editor-in-https-github-com-openai-codex-pull-5878|chore: config editor in (source link)]] · Editor Experience
- [[Changes/Codex CLI/2025-10-30-5-developer-workflow-changes-in-rust-v0-52-0|5 Developer Workflow changes in rust-v0.52.0]] · Developer Workflow
- [[Changes/Codex CLI/2025-10-30-3-safety-and-privacy-changes-in-rust-v0-52-0|3 Safety and Privacy changes in rust-v0.52.0]] · Safety and Privacy
- [[Changes/Codex CLI/2025-10-30-59-other-changes-in-rust-v0-52-0|59 other changes in rust-v0.52.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2025-10-29 · Gemini CLI · [[Changes/Gemini CLI/2025-10-29-7-apps-and-integrations-changes-in-v0-11-0|7 Apps and Integrations changes in v0.11.0]]
- Later: 2025-10-31 · Cline · [[Changes/Cline/2025-10-31-5-apps-and-integrations-changes-in-v3-35-0|5 Apps and Integrations changes in v3.35.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2025-10-30-6bf4d7&body=Card%3A%20Changes%2FCodex%20CLI%2F2025-10-30-11-apps-and-integrations-changes-in-rust-v0-52-0.md%0ACard%20ID%3A%20codex-cli-2025-10-30-6bf4d7%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.52.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->