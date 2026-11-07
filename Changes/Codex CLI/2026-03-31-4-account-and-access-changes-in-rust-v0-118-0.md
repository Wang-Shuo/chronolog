---
card_id: codex-cli-2026-03-31-78e7f5
date: '2026-03-31'
description: 'Codex CLI · 2026-03-31 · Account and Access: 4 changes in 0.118.0 —
  App-server clients can now start ChatGPT sign-in with a device code flow, which
  helps when…'
diffusion:
  first_in_tracked: "[[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign
    into Notion with your Apple ID \U0001F5DD️ The perfect combination of speedy and
    secure]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2072
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: c6dc2665da503d42e00e3129a4e591b795df0a390e95352d07e09a272f06a0ee
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-03-31-78e7f5
  comparison: ''
  date: '2026-03-31'
  description: 'Codex CLI — 0.118.0: 4 Account and Access changes'
  evidence:
  - quote: App-server clients can now start ChatGPT sign-in with a device code flow,
      which helps when browser callback login is unreliable or unavailable. (#15525)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#15903 [codex] import token_data from codex-login directly @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#15525 Add ChatGPT device-code login to app server @daniel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#16000 Use codex-utils-template for login error page @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 4-account-and-access-changes-in-rust-v0-118-0
  source_release: codex-cli-2026-03-31-rust-v0-118-0-github-303805427-02df59b6
  source_type: github_releases
  theme: account-access
  title: 4 Account and Access changes in rust-v0.118.0
  type: change
related_changes:
- '[[Changes/OpenCode/2026-03-26-2-account-and-access-changes-in-v1-3-3|2 Account
  and Access changes in v1.3.3]]'
- '[[Changes/Dify/2026-03-27-2-account-and-access-changes-in-1-13-3|2 Account and
  Access changes in 1.13.3]]'
- '[[Changes/GitHub Copilot CLI/2026-03-30-mcp-server-oauth-authentication-works-when-the-cli-runs-in-acp-mode|MCP
  server OAuth authentication works when the CLI runs in ACP mode]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-03-31-rust-v0-118-0-github-303805427-02df59b6|codex-cli-2026-03-31-rust-v0-118-0-github-303805427-02df59b6]]'
source_type: github_releases
theme: account-access
title: 4 Account and Access changes in rust-v0.118.0
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Account and Access changes in rust-v0.118.0

**Codex CLI** · 2026-03-31 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.118.0) · from [[Releases/Codex CLI/codex-cli-2026-03-31-rust-v0-118-0-github-303805427-02df59b6|0.118.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> App-server clients can now start ChatGPT sign-in with a device code flow, which helps when browser callback login is unreliable or unavailable. (#15525)

> #15903 [codex] import token_data from codex-login directly @bolinfest

> #15525 Add ChatGPT device-code login to app server @daniel-oai

> #16000 Use codex-utils-template for login error page @jif-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.118.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-03-31-16286-auth-generalize-external-auth-tokens-for-bearer-only-sources-bolinfest|♯16286 auth: generalize external auth tokens for bearer-only sources @bolinfest]] · Context Window
- [[Changes/Codex CLI/2026-03-31-16021-fix-copy-regression-in-tui-app-server-turn-completion-etraut-openai|♯16021 Fix /copy regression in tui_app_server turn completion @etraut-openai]] · Editor Experience
- [[Changes/Codex CLI/2026-03-31-12-apps-and-integrations-changes-in-rust-v0-118-0|12 Apps and Integrations changes in rust-v0.118.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-03-31-16114-remove-tui-voice-transcription-feature-etraut-openai|♯16114 Remove TUI voice transcription feature @etraut-openai]] · Voice and Audio
- [[Changes/Codex CLI/2026-03-31-3-interface-experience-changes-in-rust-v0-118-0|3 Interface Experience changes in rust-v0.118.0]] · Interface Experience
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
## Nearby in Account and Access

- Earlier: 2026-03-30 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-03-30-mcp-server-oauth-authentication-works-when-the-cli-runs-in-acp-mode|MCP server OAuth authentication works when the CLI runs in ACP mode]]
- Later: 2026-03-31 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-03-31-mcp-server-oauth-authentication-works-when-the-cli-runs-in-acp-mode|MCP server OAuth authentication works when the CLI runs in ACP mode]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Notion · [[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign into Notion with your Apple ID 🗝️ The perfect combination of speedy and secure]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-03-31-78e7f5&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-03-31-4-account-and-access-changes-in-rust-v0-118-0.md%0ACard%20ID%3A%20codex-cli-2026-03-31-78e7f5%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.118.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->