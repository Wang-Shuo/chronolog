---
card_id: codex-cli-2026-06-09-babd75
date: '2026-06-09'
description: 'Codex CLI · 2026-06-09 · Apps and Integrations: 8 changes in 0.139.0
  — Tool and connector input schemas now preserve `oneOf` and `allOf`, and large schemas…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1174
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: bdfa886f411ea735016332611e7d4500036df3ffb2458360b5d10a6010d8a7f4
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-06-09-babd75
  comparison: ''
  date: '2026-06-09'
  description: 'Codex CLI — 0.139.0: 8 Apps and Integrations changes'
  evidence:
  - quote: 'Tool and connector input schemas now preserve `oneOf` and `allOf`, and
      large schemas keep more shallow structure when compacted, improving compatibility
      with richer MCP tools. (#24118, #27084)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.139.0
  - quote: MCP startup warnings from subagents now stay in the thread that owns them,
      avoiding duplicate parent-thread alerts and stuck startup spinners in the TUI.
      (#26639)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.139.0
  - quote: '#26741 fix(remote-control): preserve enrollment on generic websocket 404s
      @apanasenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.139.0
  - quote: '#26804 fix(core-plugins): send Codex product SKU to plugin-service @ericning-o'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.139.0
  - quote: '#26639 fix(tui): scope MCP startup status by thread @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.139.0
  - quote: '#27009 [plugins] Expose marketplace source in marketplace list JSON @mpc-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.139.0
  - quote: '#26934 [codex] Prune stale curated plugin caches @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.139.0
  - quote: '#26932 Use cached remote plugin catalog for plugin list @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.139.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 8-apps-and-integrations-changes-in-rust-v0-139-0
  source_release: codex-cli-2026-06-09-rust-v0-139-0-github-336847772-eda0ee6f
  source_type: github_releases
  theme: apps-integrations
  title: 8 Apps and Integrations changes in rust-v0.139.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-06-08-19-apps-and-integrations-changes-in-rust-v0-138-0|19
  Apps and Integrations changes in rust-v0.138.0]]'
- '[[Changes/ElevenLabs/2026-06-08-sdk-releases|SDK Releases]]'
- '[[Changes/v0/2026-06-08-4-apps-and-integrations-changes-in-changelog-update|4 Apps
  and Integrations changes in Changelog update]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-06-09-rust-v0-139-0-github-336847772-eda0ee6f|codex-cli-2026-06-09-rust-v0-139-0-github-336847772-eda0ee6f]]'
source_type: github_releases
theme: apps-integrations
title: 8 Apps and Integrations changes in rust-v0.139.0
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Apps and Integrations changes in rust-v0.139.0

**Codex CLI** · 2026-06-09 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.139.0) · from [[Releases/Codex CLI/codex-cli-2026-06-09-rust-v0-139-0-github-336847772-eda0ee6f|0.139.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Tool and connector input schemas now preserve `oneOf` and `allOf`, and large schemas keep more shallow structure when compacted, improving compatibility with richer MCP tools. (#24118, #27084)

> MCP startup warnings from subagents now stay in the thread that owns them, avoiding duplicate parent-thread alerts and stuck startup spinners in the TUI. (#26639)

> #26741 fix(remote-control): preserve enrollment on generic websocket 404s @apanasenko-oai

> #26804 fix(core-plugins): send Codex product SKU to plugin-service @ericning-o

> #26639 fix(tui): scope MCP startup status by thread @fcoury-oai

> #27009 [plugins] Expose marketplace source in marketplace list JSON @mpc-oai

> #26934 [codex] Prune stale curated plugin caches @xl-openai

> #26932 Use cached remote plugin catalog for plugin list @xl-openai

Source: https://github.com/openai/codex/releases/tag/rust-v0.139.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-06-09-3-context-window-changes-in-rust-v0-139-0|3 Context Window changes in rust-v0.139.0]] · Context Window
- [[Changes/Codex CLI/2026-06-09-3-search-and-browsing-changes-in-rust-v0-139-0|3 Search and Browsing changes in rust-v0.139.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-06-09-plugin-marketplace-automation-is-more-informative-and-responsive-codex-plugin-ma|Plugin marketplace automation is more informative and responsive]] · Automation and Scheduling
- [[Changes/Codex CLI/2026-06-09-26637-codex-speed-up-external-agent-session-imports-stefanstokic-oai|♯26637 codex Speed up external agent session imports @stefanstokic-oai]] · Reliability and Performance
- [[Changes/Codex CLI/2026-06-09-26821-codex-exclude-external-tool-output-from-memories-rka-oai|♯26821 codex Exclude external tool output from memories @rka-oai]] · Memory and Personalization
- [[Changes/Codex CLI/2026-06-09-5-agent-mode-changes-in-rust-v0-139-0|5 Agent Mode changes in rust-v0.139.0]] · Agent Mode
- [[Changes/Codex CLI/2026-06-09-release-builds-once-again-publish-separate-symbol-archives-with-line-tables-impr|Release builds once again publish separate symbol archives with line tables…]] · Developer Workflow
- [[Changes/Codex CLI/2026-06-09-4-editor-experience-changes-in-rust-v0-139-0|4 Editor Experience changes in rust-v0.139.0]] · Editor Experience
- [[Changes/Codex CLI/2026-06-09-5-safety-and-privacy-changes-in-rust-v0-139-0|5 Safety and Privacy changes in rust-v0.139.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-06-09-24-other-changes-in-rust-v0-139-0|24 other changes in rust-v0.139.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-06-08 · v0 · [[Changes/v0/2026-06-08-4-apps-and-integrations-changes-in-changelog-update|4 Apps and Integrations changes in Changelog update]]
- Later: 2026-06-09 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-06-09-4-apps-and-integrations-changes-in-v1-0-61|4 Apps and Integrations changes in v1.0.61]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-06-09-babd75&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-06-09-8-apps-and-integrations-changes-in-rust-v0-139-0.md%0ACard%20ID%3A%20codex-cli-2026-06-09-babd75%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.139.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->