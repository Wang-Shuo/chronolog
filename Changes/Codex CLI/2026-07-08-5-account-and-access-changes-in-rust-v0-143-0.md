---
card_id: codex-cli-2026-07-08-0511cd
date: '2026-07-08'
description: 'Codex CLI · 2026-07-08 · Account and Access: 5 changes in 0.143.0 —
  Codex can route authentication and Responses API traffic through macOS and Windows
  system…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1196
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 3d366f56f02e738b6319937f204b38f964749e396aa30039822cf650cd82256d
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-07-08-0511cd
  comparison: ''
  date: '2026-07-08'
  description: 'Codex CLI — 0.143.0: 5 Account and Access changes'
  evidence:
  - quote: 'Codex can route authentication and Responses API traffic through macOS
      and Windows system proxies, including PAC and WPAD configurations. (#26708,
      #26709, #31335)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: 'MCP tools now use tool search by default, and ChatGPT-hosted MCP servers
      can explicitly use session authentication. (#29486, #29733)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29924 Represent MCP authentication with an enum @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29656 Test executor-routed MCP OAuth token exchange @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30257 [codex] Classify nested MCP authentication startup errors @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 5-account-and-access-changes-in-rust-v0-143-0
  source_release: codex-cli-2026-07-08-rust-v0-143-0-github-350650561-9eba805c
  source_type: github_releases
  theme: account-access
  title: 5 Account and Access changes in rust-v0.143.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-07-07-added-a-warning-when-your-login-is-about-to-expire-so-you-can-re-authenticate-be|Added
  a warning when your login is about to expire, so you can re-authenticate…]]'
- '[[Changes/GitHub Copilot CLI/2026-07-07-6-account-and-access-changes-in-v1-0-69|6
  Account and Access changes in v1.0.69]]'
- '[[Changes/Lovable/2026-07-07-sign-in-with-sso-using-your-company-domain-or-provider-id|Sign
  in with SSO using your company domain or provider ID]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-07-08-rust-v0-143-0-github-350650561-9eba805c|codex-cli-2026-07-08-rust-v0-143-0-github-350650561-9eba805c]]'
source_type: github_releases
theme: account-access
title: 5 Account and Access changes in rust-v0.143.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Account and Access changes in rust-v0.143.0

**Codex CLI** · 2026-07-08 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.143.0) · from [[Releases/Codex CLI/codex-cli-2026-07-08-rust-v0-143-0-github-350650561-9eba805c|0.143.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Codex can route authentication and Responses API traffic through macOS and Windows system proxies, including PAC and WPAD configurations. (#26708, #26709, #31335)

> MCP tools now use tool search by default, and ChatGPT-hosted MCP servers can explicitly use session authentication. (#29486, #29733)

> #29924 Represent MCP authentication with an enum @aibrahim-oai

> #29656 Test executor-routed MCP OAuth token exchange @jif-oai

> #30257 [codex] Classify nested MCP authentication startup errors @felixxia-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.143.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-07-08-5-collaboration-changes-in-rust-v0-143-0|5 Collaboration changes in rust-v0.143.0]] · Collaboration
- [[Changes/Codex CLI/2026-07-08-66-apps-and-integrations-changes-in-rust-v0-143-0|66 Apps and Integrations changes in rust-v0.143.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-07-08-14-model-support-changes-in-rust-v0-143-0|14 Model Support changes in rust-v0.143.0]] · Model Support
- [[Changes/Codex CLI/2026-07-08-10-agent-mode-changes-in-rust-v0-143-0|10 Agent Mode changes in rust-v0.143.0]] · Agent Mode
- [[Changes/Codex CLI/2026-07-08-27714-app-server-document-thread-and-turn-ids-are-uuid7-owenlin0|♯27714 app-server: document thread and turn IDs are UUID7 @owenlin0]] · Files and Data
- [[Changes/Codex CLI/2026-07-08-13-safety-and-privacy-changes-in-rust-v0-143-0|13 Safety and Privacy changes in rust-v0.143.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-07-08-28593-codex-suppress-low-usage-remaining-warnings-when-credits-are-available-bro|♯28593 codex suppress low usage remaining warnings when credits are available…]] · Pricing Model
- [[Changes/Codex CLI/2026-07-08-12-context-window-changes-in-rust-v0-143-0|12 Context Window changes in rust-v0.143.0]] · Context Window
- [[Changes/Codex CLI/2026-07-08-30508-revert-make-auto-review-on-request-prompt-more-proactive-dylan-hurd-oai|♯30508 Revert "Make auto-review on-request prompt more proactive" @dylan-hurd-oai]] · Automation and Scheduling
- [[Changes/Codex CLI/2026-07-08-2-mobile-and-desktop-changes-in-rust-v0-143-0|2 Mobile and Desktop changes in rust-v0.143.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-07-08-3-editor-experience-changes-in-rust-v0-143-0|3 Editor Experience changes in rust-v0.143.0]] · Editor Experience
- [[Changes/Codex CLI/2026-07-08-7-developer-workflow-changes-in-rust-v0-143-0|7 Developer Workflow changes in rust-v0.143.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-07-08-3-image-generation-changes-in-rust-v0-143-0|3 Image Generation changes in rust-v0.143.0]] · Image Generation
- [[Changes/Codex CLI/2026-07-08-2-memory-and-personalization-changes-in-rust-v0-143-0|2 Memory and Personalization changes in rust-v0.143.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-07-08-remote-plugins-are-now-enabled-by-default-with-richer-catalog-rows-npm-marketpla|Remote plugins are now enabled by default, with richer catalog rows, npm marketplace…]] · Apps and Integrations
- [[Changes/Codex CLI/2026-07-08-145-other-changes-in-rust-v0-143-0|145 other changes in rust-v0.143.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-07-07 · Lovable · [[Changes/Lovable/2026-07-07-sign-in-with-sso-using-your-company-domain-or-provider-id|Sign in with SSO using your company domain or provider ID]]
- Later: 2026-07-08 · Lovable · [[Changes/Lovable/2026-07-08-configure-sso-just-in-time-provisioning-from-settings|Configure SSO Just-in-Time provisioning from settings]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-07-08-0511cd&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-07-08-5-account-and-access-changes-in-rust-v0-143-0.md%0ACard%20ID%3A%20codex-cli-2026-07-08-0511cd%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.143.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->