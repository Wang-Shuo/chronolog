---
card_id: codex-cli-2026-03-31-2c3f4e
date: '2026-03-31'
description: 'Codex CLI · 2026-03-31 · Apps and Integrations: 12 changes in 0.118.0
  — MCP startup is more robust: local servers get a longer startup window, and failed…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2664
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 5d08d574f0334ab2ed52aea441aeba40eeb5548fef988d0051c1b41af2df2073
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-03-31-2c3f4e
  comparison: ''
  date: '2026-03-31'
  description: 'Codex CLI — 0.118.0: 12 Apps and Integrations changes'
  evidence:
  - quote: 'MCP startup is more robust: local servers get a longer startup window,
      and failed handshakes surface warnings in the TUI again instead of looking like
      clean startups. (#16080, #16041)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#15891 [plugins] Polish tool suggest prompts. @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#15928 codex-tools: extract MCP schema adapters @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#16036 fix: disable plugins in SDK integration tests @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#15946 Normalize /mcp tool grouping for hyphenated server names @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#16035 plugins: Clean up stale curated plugin sync temp dirs and add sync
      metrics @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#16044 [mcp] Bypass read-only tool checks. @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#16046 ci: run SDK tests with a Bazel-built codex @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#16126 core: fix stale curated plugin cache refresh races @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#16080 [mcp] Increase MCP startup timeout. @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#16041 Fix app-server TUI MCP startup warnings regression @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#16204 [codex] Normalize Windows path in MCP startup snapshot test @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 12-apps-and-integrations-changes-in-rust-v0-118-0
  source_release: codex-cli-2026-03-31-rust-v0-118-0-github-303805427-02df59b6
  source_type: github_releases
  theme: apps-integrations
  title: 12 Apps and Integrations changes in rust-v0.118.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-03-30-5-apps-and-integrations-changes-in-v1-0-13|5
  Apps and Integrations changes in v1.0.13]]'
- '[[Changes/OpenCode/2026-03-30-2-apps-and-integrations-changes-in-v1-3-9-1|2 Apps
  and Integrations changes in v1.3.9 + 1]]'
- '[[Changes/OpenHands/2026-03-30-added-support-for-hooks-by-xingyaoww-in-https-github-com-openhands-openhands-pul|Added
  support for hooks]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-03-31-rust-v0-118-0-github-303805427-02df59b6|codex-cli-2026-03-31-rust-v0-118-0-github-303805427-02df59b6]]'
source_type: github_releases
theme: apps-integrations
title: 12 Apps and Integrations changes in rust-v0.118.0
type: change
---

<!-- chronolog:begin region="header" -->
# 12 Apps and Integrations changes in rust-v0.118.0

**Codex CLI** · 2026-03-31 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.118.0) · from [[Releases/Codex CLI/codex-cli-2026-03-31-rust-v0-118-0-github-303805427-02df59b6|0.118.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> MCP startup is more robust: local servers get a longer startup window, and failed handshakes surface warnings in the TUI again instead of looking like clean startups. (#16080, #16041)

> #15891 [plugins] Polish tool suggest prompts. @mzeng-openai

> #15928 codex-tools: extract MCP schema adapters @bolinfest

> #16036 fix: disable plugins in SDK integration tests @bolinfest

> #15946 Normalize /mcp tool grouping for hyphenated server names @pakrym-oai

> #16035 plugins: Clean up stale curated plugin sync temp dirs and add sync metrics @xl-openai

> #16044 [mcp] Bypass read-only tool checks. @mzeng-openai

> #16046 ci: run SDK tests with a Bazel-built codex @bolinfest

> #16126 core: fix stale curated plugin cache refresh races @bolinfest

> #16080 [mcp] Increase MCP startup timeout. @mzeng-openai

> #16041 Fix app-server TUI MCP startup warnings regression @etraut-openai

> #16204 [codex] Normalize Windows path in MCP startup snapshot test @etraut-openai

Source: https://github.com/openai/codex/releases/tag/rust-v0.118.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-03-31-16286-auth-generalize-external-auth-tokens-for-bearer-only-sources-bolinfest|♯16286 auth: generalize external auth tokens for bearer-only sources @bolinfest]] · Context Window
- [[Changes/Codex CLI/2026-03-31-16021-fix-copy-regression-in-tui-app-server-turn-completion-etraut-openai|♯16021 Fix /copy regression in tui_app_server turn completion @etraut-openai]] · Editor Experience
- [[Changes/Codex CLI/2026-03-31-16114-remove-tui-voice-transcription-feature-etraut-openai|♯16114 Remove TUI voice transcription feature @etraut-openai]] · Voice and Audio
- [[Changes/Codex CLI/2026-03-31-3-interface-experience-changes-in-rust-v0-118-0|3 Interface Experience changes in rust-v0.118.0]] · Interface Experience
- [[Changes/Codex CLI/2026-03-31-4-account-and-access-changes-in-rust-v0-118-0|4 Account and Access changes in rust-v0.118.0]] · Account and Access
- [[Changes/Codex CLI/2026-03-31-3-developer-workflow-changes-in-rust-v0-118-0|3 Developer Workflow changes in rust-v0.118.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-03-31-15934-add-usage-based-business-plan-types-bwanner-oai|♯15934 Add usage-based business plan types @bwanner-oai]] · Pricing Model
- [[Changes/Codex CLI/2026-03-31-7-safety-and-privacy-changes-in-rust-v0-118-0|7 Safety and Privacy changes in rust-v0.118.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-03-31-4-agent-mode-changes-in-rust-v0-118-0|4 Agent Mode changes in rust-v0.118.0]] · Agent Mode
- [[Changes/Codex CLI/2026-03-31-7-mobile-and-desktop-changes-in-rust-v0-118-0|7 Mobile and Desktop changes in rust-v0.118.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-03-31-4-collaboration-changes-in-rust-v0-118-0|4 Collaboration changes in rust-v0.118.0]] · Collaboration
- [[Changes/Codex CLI/2026-03-31-5-model-support-changes-in-rust-v0-118-0|5 Model Support changes in rust-v0.118.0]] · Model Support
- [[Changes/Codex CLI/2026-03-31-51-other-changes-in-rust-v0-118-0|51 other changes in rust-v0.118.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-03-30 · OpenHands · [[Changes/OpenHands/2026-03-30-added-support-for-hooks-by-xingyaoww-in-https-github-com-openhands-openhands-pul|Added support for hooks]]
- Later: 2026-03-31 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-03-31-5-apps-and-integrations-changes-in-v1-0-14|5 Apps and Integrations changes in v1.0.14]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-03-31-2c3f4e&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-03-31-12-apps-and-integrations-changes-in-rust-v0-118-0.md%0ACard%20ID%3A%20codex-cli-2026-03-31-2c3f4e%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.118.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->