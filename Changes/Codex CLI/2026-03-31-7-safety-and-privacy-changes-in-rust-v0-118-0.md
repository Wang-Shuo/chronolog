---
card_id: codex-cli-2026-03-31-90fd40
date: '2026-03-31'
description: 'Codex CLI · 2026-03-31 · Safety and Privacy: 7 changes in 0.118.0 —
  Windows sandbox runs can now enforce proxy-only networking with OS-level egress
  rules…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1080
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a97b12e2da8e2b45f9f1e99330638a7122391240eda17241fe037e39cae32373
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-03-31-90fd40
  comparison: ''
  date: '2026-03-31'
  description: 'Codex CLI — 0.118.0: 7 Safety and Privacy changes'
  evidence:
  - quote: Windows sandbox runs can now enforce proxy-only networking with OS-level
      egress rules, instead of relying on environment variables alone. (#12220)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: 'Linux sandbox launches are more reliable because Codex once again finds
      a trusted system `bwrap` on normal multi-entry `PATH`s. (#15791, #15973)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#15900 skills: remove unused skill permission metadata @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#12220 feat(windows-sandbox): add network proxy support @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#15954 chore: move pty and windows sandbox to Rust 2024 @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#15998 Use codex-utils-template for sandbox mode prompts @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#15973 fix(sandbox): fix bwrap lookup for multi-entry PATH @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 7-safety-and-privacy-changes-in-rust-v0-118-0
  source_release: codex-cli-2026-03-31-rust-v0-118-0-github-303805427-02df59b6
  source_type: github_releases
  theme: safety-privacy
  title: 7 Safety and Privacy changes in rust-v0.118.0
  type: change
related_changes:
- "[[Changes/Open WebUI/2026-03-27-terminal-server-connection-security-terminal-server-verification-and-policy-savi|\U0001F512
  Terminal server connection security. Terminal server verification and policy…]]"
- '[[Changes/GitHub Copilot CLI/2026-03-30-mcp-servers-using-microsoft-entra-id-authentication-no-longer-show-the-consent-s|MCP
  servers using Microsoft Entra ID authentication no longer show the consent…]]'
- '[[Changes/OpenHands/2026-03-30-added-clear-command-for-v1-conversations-typing-clear-in-the-chat-creates-a-new|Added
  /clear command for V1 conversations]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-03-31-rust-v0-118-0-github-303805427-02df59b6|codex-cli-2026-03-31-rust-v0-118-0-github-303805427-02df59b6]]'
source_type: github_releases
theme: safety-privacy
title: 7 Safety and Privacy changes in rust-v0.118.0
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Safety and Privacy changes in rust-v0.118.0

**Codex CLI** · 2026-03-31 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.118.0) · from [[Releases/Codex CLI/codex-cli-2026-03-31-rust-v0-118-0-github-303805427-02df59b6|0.118.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Windows sandbox runs can now enforce proxy-only networking with OS-level egress rules, instead of relying on environment variables alone. (#12220)

> Linux sandbox launches are more reliable because Codex once again finds a trusted system `bwrap` on normal multi-entry `PATH`s. (#15791, #15973)

> #15900 skills: remove unused skill permission metadata @bolinfest

> #12220 feat(windows-sandbox): add network proxy support @viyatb-oai

> #15954 chore: move pty and windows sandbox to Rust 2024 @bolinfest

> #15998 Use codex-utils-template for sandbox mode prompts @jif-oai

> #15973 fix(sandbox): fix bwrap lookup for multi-entry PATH @viyatb-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.118.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-03-31-16286-auth-generalize-external-auth-tokens-for-bearer-only-sources-bolinfest|♯16286 auth: generalize external auth tokens for bearer-only sources @bolinfest]] · Context Window
- [[Changes/Codex CLI/2026-03-31-16021-fix-copy-regression-in-tui-app-server-turn-completion-etraut-openai|♯16021 Fix /copy regression in tui_app_server turn completion @etraut-openai]] · Editor Experience
- [[Changes/Codex CLI/2026-03-31-12-apps-and-integrations-changes-in-rust-v0-118-0|12 Apps and Integrations changes in rust-v0.118.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-03-31-16114-remove-tui-voice-transcription-feature-etraut-openai|♯16114 Remove TUI voice transcription feature @etraut-openai]] · Voice and Audio
- [[Changes/Codex CLI/2026-03-31-3-interface-experience-changes-in-rust-v0-118-0|3 Interface Experience changes in rust-v0.118.0]] · Interface Experience
- [[Changes/Codex CLI/2026-03-31-4-account-and-access-changes-in-rust-v0-118-0|4 Account and Access changes in rust-v0.118.0]] · Account and Access
- [[Changes/Codex CLI/2026-03-31-3-developer-workflow-changes-in-rust-v0-118-0|3 Developer Workflow changes in rust-v0.118.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-03-31-15934-add-usage-based-business-plan-types-bwanner-oai|♯15934 Add usage-based business plan types @bwanner-oai]] · Pricing Model
- [[Changes/Codex CLI/2026-03-31-4-agent-mode-changes-in-rust-v0-118-0|4 Agent Mode changes in rust-v0.118.0]] · Agent Mode
- [[Changes/Codex CLI/2026-03-31-7-mobile-and-desktop-changes-in-rust-v0-118-0|7 Mobile and Desktop changes in rust-v0.118.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-03-31-4-collaboration-changes-in-rust-v0-118-0|4 Collaboration changes in rust-v0.118.0]] · Collaboration
- [[Changes/Codex CLI/2026-03-31-5-model-support-changes-in-rust-v0-118-0|5 Model Support changes in rust-v0.118.0]] · Model Support
- [[Changes/Codex CLI/2026-03-31-51-other-changes-in-rust-v0-118-0|51 other changes in rust-v0.118.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-03-30 · OpenHands · [[Changes/OpenHands/2026-03-30-added-clear-command-for-v1-conversations-typing-clear-in-the-chat-creates-a-new|Added /clear command for V1 conversations]]
- Later: 2026-03-31 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-03-31-2-safety-and-privacy-changes-in-v1-0-14|2 Safety and Privacy changes in v1.0.14]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-03-31-90fd40&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-03-31-7-safety-and-privacy-changes-in-rust-v0-118-0.md%0ACard%20ID%3A%20codex-cli-2026-03-31-90fd40%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.118.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->