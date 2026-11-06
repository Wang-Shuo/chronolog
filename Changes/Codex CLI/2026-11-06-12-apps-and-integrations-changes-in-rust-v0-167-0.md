---
card_id: codex-cli-2026-11-06-ede021
date: '2026-11-06'
description: 'Codex CLI · 2026-11-06 · Apps and Integrations: 12 changes in 0.167.0
  — #57855 Load TUI plugin mentions from installed plugins @zamoshchin-openai'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1324
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d26871db474a57840b5346f1fb552d8ac347da617dd4d7ad23caff9160646365
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-11-06-ede021
  comparison: ''
  date: '2026-11-06'
  description: 'Codex CLI — 0.167.0: 12 Apps and Integrations changes'
  evidence:
  - quote: '#57855 Load TUI plugin mentions from installed plugins @zamoshchin-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#57861 Skip resource template discovery for hosted Apps @khong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#57974 Apply session plugin overrides during MCP config refresh @TAFOYA-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#57978 Add per-chat leases for shared MCP connections @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58161 Include tool names and annotation hints in MCP approval metadata
      @brisebois-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58165 Keep remote plugin bundle URLs out of diagnostics @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58341 Add an MCP adapter for message-board tools @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58352 Allow Apps catalog discovery before the initial tool inventory
      completes @bkotsopoulos'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58368 Apply PreToolUse hooks before direct Guardian review policy checks
      @swastik-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58378 Scope agent MCP metadata to a host-selected plugin registration
      @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58395 Add scoped host metadata hooks for MCP tool requests @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58428 Support app settings in plugin configuration @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 12-apps-and-integrations-changes-in-rust-v0-167-0
  source_release: codex-cli-2026-11-06-rust-v0-167-0-github-435979892-a2e140bc
  source_type: github_releases
  theme: apps-integrations
  title: 12 Apps and Integrations changes in rust-v0.167.0
  type: change
related_changes:
- '[[Changes/OpenHands/2026-11-03-3-apps-and-integrations-changes-in-v1-35-0|3 Apps
  and Integrations changes in v1.35.0]]'
- '[[Changes/Dify/2026-11-04-15-apps-and-integrations-changes-in-1-19-0|15 Apps and
  Integrations changes in 1.19.0]]'
- '[[Changes/OpenHands/2026-11-05-3-apps-and-integrations-changes-in-v1-36-0|3 Apps
  and Integrations changes in v1.36.0]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-11-06-rust-v0-167-0-github-435979892-a2e140bc|codex-cli-2026-11-06-rust-v0-167-0-github-435979892-a2e140bc]]'
source_type: github_releases
theme: apps-integrations
title: 12 Apps and Integrations changes in rust-v0.167.0
type: change
---

<!-- chronolog:begin region="header" -->
# 12 Apps and Integrations changes in rust-v0.167.0

**Codex CLI** · 2026-11-06 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.167.0) · from [[Releases/Codex CLI/codex-cli-2026-11-06-rust-v0-167-0-github-435979892-a2e140bc|0.167.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> #57855 Load TUI plugin mentions from installed plugins @zamoshchin-openai

> #57861 Skip resource template discovery for hosted Apps @khong-oai

> #57974 Apply session plugin overrides during MCP config refresh @TAFOYA-OAI

> #57978 Add per-chat leases for shared MCP connections @charliemarsh-oai

> #58161 Include tool names and annotation hints in MCP approval metadata @brisebois-oai

> #58165 Keep remote plugin bundle URLs out of diagnostics @mzeng-openai

> #58341 Add an MCP adapter for message-board tools @jif-oai

> #58352 Allow Apps catalog discovery before the initial tool inventory completes @bkotsopoulos

> #58368 Apply PreToolUse hooks before direct Guardian review policy checks @swastik-oai

> #58378 Scope agent MCP metadata to a host-selected plugin registration @rhan-oai

> #58395 Add scoped host metadata hooks for MCP tool requests @rhan-oai

> #58428 Support app settings in plugin configuration @mzeng-openai

Source: https://github.com/openai/codex/releases/tag/rust-v0.167.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-11-06-2-memory-and-personalization-changes-in-rust-v0-167-0|2 Memory and Personalization changes in rust-v0.167.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-11-06-2-editor-experience-changes-in-rust-v0-167-0|2 Editor Experience changes in rust-v0.167.0]] · Editor Experience
- [[Changes/Codex CLI/2026-11-06-3-search-and-browsing-changes-in-rust-v0-167-0|3 Search and Browsing changes in rust-v0.167.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-11-06-7-model-support-changes-in-rust-v0-167-0|7 Model Support changes in rust-v0.167.0]] · Model Support
- [[Changes/Codex CLI/2026-11-06-8-context-window-changes-in-rust-v0-167-0|8 Context Window changes in rust-v0.167.0]] · Context Window
- [[Changes/Codex CLI/2026-11-06-6-developer-workflow-changes-in-rust-v0-167-0|6 Developer Workflow changes in rust-v0.167.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-11-06-4-voice-and-audio-changes-in-rust-v0-167-0|4 Voice and Audio changes in rust-v0.167.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-11-06-2-mobile-and-desktop-changes-in-rust-v0-167-0|2 Mobile and Desktop changes in rust-v0.167.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-11-06-5-account-and-access-changes-in-rust-v0-167-0|5 Account and Access changes in rust-v0.167.0]] · Account and Access
- [[Changes/Codex CLI/2026-11-06-6-agent-mode-changes-in-rust-v0-167-0|6 Agent Mode changes in rust-v0.167.0]] · Agent Mode
- [[Changes/Codex CLI/2026-11-06-13-interface-experience-changes-in-rust-v0-167-0|13 Interface Experience changes in rust-v0.167.0]] · Interface Experience
- [[Changes/Codex CLI/2026-11-06-57985-skip-read-only-volume-root-expansion-in-the-mxc-sandbox-iceweasel-oai|♯57985 Skip read-only volume-root expansion in the MXC sandbox @iceweasel-oai]] · Safety and Privacy
- [[Changes/Codex CLI/2026-11-06-65-other-changes-in-rust-v0-167-0|65 other changes in rust-v0.167.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-11-05 · OpenHands · [[Changes/OpenHands/2026-11-05-3-apps-and-integrations-changes-in-v1-36-0|3 Apps and Integrations changes in v1.36.0]]
- Later: 2026-11-06 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-11-06-89-apps-and-integrations-changes-in-v1-0-106|89 Apps and Integrations changes in v1.0.106]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-11-06-ede021&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-11-06-12-apps-and-integrations-changes-in-rust-v0-167-0.md%0ACard%20ID%3A%20codex-cli-2026-11-06-ede021%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.167.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->