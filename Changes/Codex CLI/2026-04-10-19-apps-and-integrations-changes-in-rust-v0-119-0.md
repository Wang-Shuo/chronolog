---
card_id: codex-cli-2026-04-10-b7b30b
date: '2026-04-10'
description: 'Codex CLI · 2026-04-10 · Apps and Integrations: 19 changes in 0.119.0
  — MCP Apps and custom MCP servers gained richer support, including resource reads…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1114
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: cdb4f1703b1e8832cc32d6e75a7b697f21fafa0075f6f4666801332f954f531d
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-04-10-b7b30b
  comparison: ''
  date: '2026-04-10'
  description: 'Codex CLI — 0.119.0: 19 Apps and Integrations changes'
  evidence:
  - quote: 'MCP Apps and custom MCP servers gained richer support, including resource
      reads, tool-call metadata, custom-server tool search, server-driven elicitations,
      file-parameter uploads, and more reliable plugin cache refreshes (#16082, #16465,
      #16944, #17043, #15197, #16191, #16947).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: 'MCP status and startup are less noisy and faster: hyphenated server names
      list tools correctly, `/mcp` avoids slow full inventory probes, disabled servers
      skip auth probing, and residency headers are honored by `codex mcp-server` (#16674,
      #16831, #17098, #16952).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '`codex-core` was slimmed down through major crate extractions for MCP,
      tools, config, model management, auth, feedback, protocol, and related ownership
      boundaries (#15919, #16379, #16508, #16523, #16962).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#15919 Extract MCP into codex-mcp crate @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16510 core: use codex-mcp APIs directly @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16674 Fix MCP tool listing for hyphenated server names @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16947 feat: fallback curated plugin download from backend endpint. @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16191 feat: refresh non-curated cache from plugin list. @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16952 Respect residency requirements in mcp-server @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16831 Speed up /mcp inventory listing @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16082 [mcp] Support MCP Apps part 1. @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16972 app-server: Fix compilation of a test in mcp_resource @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16465 [mcp] Support MCP Apps part 2 - Add meta to mcp tool call result.
      @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16973 app-server: Allow enabling remote control in runtime @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17098 Skip MCP auth probing for disabled servers @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17043 [mcp] Support server-driven elicitations @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17164 Auto-approve MCP server elicitations in Full Access mode @leoshimo-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#15197 Add Codex Apps sediment file remapping @caseychow-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16944 [mcp] Expand tool search to custom MCPs. @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 19-apps-and-integrations-changes-in-rust-v0-119-0
  source_release: codex-cli-2026-04-10-rust-v0-119-0-github-307754801-19f169d1
  source_type: github_releases
  theme: apps-integrations
  title: 19 Apps and Integrations changes in rust-v0.119.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-04-09-7-apps-and-integrations-changes-in-v1-0-22|7
  Apps and Integrations changes in v1.0.22]]'
- '[[Changes/OpenCode/2026-04-09-sdk-fix-the-generated-sdk-and-openapi-types-for-providers-and-session-shell-resp|SDK
  Fix the generated SDK and OpenAPI types for /providers and session shell responses]]'
- '[[Changes/Claude Code/2026-04-10-4-apps-and-integrations-changes-in-v2-1-101|4
  Apps and Integrations changes in v2.1.101]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-04-10-rust-v0-119-0-github-307754801-19f169d1|codex-cli-2026-04-10-rust-v0-119-0-github-307754801-19f169d1]]'
source_type: github_releases
theme: apps-integrations
title: 19 Apps and Integrations changes in rust-v0.119.0
type: change
---

<!-- chronolog:begin region="header" -->
# 19 Apps and Integrations changes in rust-v0.119.0

**Codex CLI** · 2026-04-10 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.119.0) · from [[Releases/Codex CLI/codex-cli-2026-04-10-rust-v0-119-0-github-307754801-19f169d1|0.119.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> MCP Apps and custom MCP servers gained richer support, including resource reads, tool-call metadata, custom-server tool search, server-driven elicitations, file-parameter uploads, and more reliable plugin cache refreshes (#16082, #16465, #16944, #17043, #15197, #16191, #16947).

> MCP status and startup are less noisy and faster: hyphenated server names list tools correctly, `/mcp` avoids slow full inventory probes, disabled servers skip auth probing, and residency headers are honored by `codex mcp-server` (#16674, #16831, #17098, #16952).

> `codex-core` was slimmed down through major crate extractions for MCP, tools, config, model management, auth, feedback, protocol, and related ownership boundaries (#15919, #16379, #16508, #16523, #16962).

> #15919 Extract MCP into codex-mcp crate @aibrahim-oai

> #16510 core: use codex-mcp APIs directly @bolinfest

> #16674 Fix MCP tool listing for hyphenated server names @etraut-openai

> #16947 feat: fallback curated plugin download from backend endpint. @xl-openai

> #16191 feat: refresh non-curated cache from plugin list. @xl-openai

> #16952 Respect residency requirements in mcp-server @etraut-openai

> #16831 Speed up /mcp inventory listing @etraut-openai

> #16082 [mcp] Support MCP Apps part 1. @mzeng-openai

> #16972 app-server: Fix compilation of a test in mcp_resource @euroelessar

> #16465 [mcp] Support MCP Apps part 2 - Add meta to mcp tool call result. @mzeng-openai

> #16973 app-server: Allow enabling remote control in runtime @euroelessar

> #17098 Skip MCP auth probing for disabled servers @etraut-openai

> #17043 [mcp] Support server-driven elicitations @mzeng-openai

> #17164 Auto-approve MCP server elicitations in Full Access mode @leoshimo-oai

> #15197 Add Codex Apps sediment file remapping @caseychow-oai

> #16944 [mcp] Expand tool search to custom MCPs. @mzeng-openai

Source: https://github.com/openai/codex/releases/tag/rust-v0.119.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-04-10-4-context-window-changes-in-rust-v0-119-0|4 Context Window changes in rust-v0.119.0]] · Context Window
- [[Changes/Codex CLI/2026-04-10-8-safety-and-privacy-changes-in-rust-v0-119-0|8 Safety and Privacy changes in rust-v0.119.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-04-10-28-developer-workflow-changes-in-rust-v0-119-0|28 Developer Workflow changes in rust-v0.119.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-04-10-13-agent-mode-changes-in-rust-v0-119-0|13 Agent Mode changes in rust-v0.119.0]] · Agent Mode
- [[Changes/Codex CLI/2026-04-10-2-memory-and-personalization-changes-in-rust-v0-119-0|2 Memory and Personalization changes in rust-v0.119.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-04-10-the-readme-now-uses-the-current-chatgpt-business-plan-name-16348|The README now uses the current ChatGPT Business plan name (♯16348)]] · Enterprise and Administration
- [[Changes/Codex CLI/2026-04-10-3-voice-and-audio-changes-in-rust-v0-119-0|3 Voice and Audio changes in rust-v0.119.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-04-10-2-account-and-access-changes-in-rust-v0-119-0|2 Account and Access changes in rust-v0.119.0]] · Account and Access
- [[Changes/Codex CLI/2026-04-10-17256-app-server-use-shared-receivers-for-app-server-message-processors-euroeles|♯17256 app-server: Use shared receivers for app-server message processors @euroelessar]] · Collaboration
- [[Changes/Codex CLI/2026-04-10-10-interface-experience-changes-in-rust-v0-119-0|10 Interface Experience changes in rust-v0.119.0]] · Interface Experience
- [[Changes/Codex CLI/2026-04-10-16202-fix-paste-driven-bottom-pane-completion-teardown-etraut-openai|♯16202 Fix paste-driven bottom pane completion teardown @etraut-openai]] · Editor Experience
- [[Changes/Codex CLI/2026-04-10-2-reliability-and-performance-changes-in-rust-v0-119-0|2 Reliability and Performance changes in rust-v0.119.0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-04-10-5-model-support-changes-in-rust-v0-119-0|5 Model Support changes in rust-v0.119.0]] · Model Support
- [[Changes/Codex CLI/2026-04-10-6-mobile-and-desktop-changes-in-rust-v0-119-0|6 Mobile and Desktop changes in rust-v0.119.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-04-10-187-other-changes-in-rust-v0-119-0|187 other changes in rust-v0.119.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-04-10 · Claude Code · [[Changes/Claude Code/2026-04-10-4-apps-and-integrations-changes-in-v2-1-101|4 Apps and Integrations changes in v2.1.101]]
- Later: 2026-04-10 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-04-10-pretooluse-hooks-now-respect-modifiedargs-updatedinput-and-additionalcontext-fie|preToolUse hooks now respect modifiedArgs/updatedInput, and additionalContext fields]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-04-10-b7b30b&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-04-10-19-apps-and-integrations-changes-in-rust-v0-119-0.md%0ACard%20ID%3A%20codex-cli-2026-04-10-b7b30b%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.119.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->