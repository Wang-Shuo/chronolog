---
card_id: codex-cli-2025-11-19-5cd2ac
date: '2025-11-19'
description: 'Codex CLI · 2025-11-19 · Account and Access: :bug: fix(rmcp-client):
  refresh OAuth tokens using expires_at (#6574) — @LaelLuo'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 965
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: 2c5f3e5e95c77523b854aa23473c758586b3f84044ffda4fd5b683eeb4f85076
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2025-11-19-5cd2ac
  comparison: ''
  date: '2025-11-19'
  description: 'Codex CLI — 0.59.0: :bug: fix(rmcp-client): refresh OAuth tokens using
    expires_at (#6574) — @LaelLuo'
  evidence:
  - quote: ':bug: fix(rmcp-client): refresh OAuth tokens using expires_at (#6574)
      — @LaelLuo'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.59.0
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: codex-cli
  product_name: Codex CLI
  slug: bug-fix-rmcp-client-refresh-oauth-tokens-using-expires-at-6574-laelluo
  source_release: codex-cli-2025-11-19-rust-v0-59-0-github-263735550-757042e7
  source_type: github_releases
  theme: account-access
  theme_matches:
  - matched_terms:
    - oauth
    score: 50
    theme: account-access
  - matched_terms:
    - tokens
    score: 50
    theme: context-window
  theme_resolution: manual-semantic-rule-v1
  title: ':bug: fix(rmcp-client): refresh OAuth tokens using expires_at (#6574) —
    @LaelLuo'
  type: change
related_changes:
- '[[Changes/Cline/2025-11-13-feat-add-oauth-2-1-authentication-support-for-remote-mcp-servers-by-saoudrizwan|feat:
  Add OAuth 2.1 authentication support for remote MCP servers]]'
- '[[Changes/Codex CLI/2025-11-13-6419-support-exiting-from-the-login-menu-b46012e48|♯6419
  — Support exiting from the login menu (b46012e48)]]'
- '[[Changes/Cline/2025-11-18-retire-firebase-authentication-by-tseglevskiy-in-https-github-com-cline-cline-pu|Retire
  firebase authentication]]'
source_release: '[[Releases/Codex CLI/codex-cli-2025-11-19-rust-v0-59-0-github-263735550-757042e7|codex-cli-2025-11-19-rust-v0-59-0-github-263735550-757042e7]]'
source_type: github_releases
theme: account-access
title: ':bug: fix(rmcp-client): refresh OAuth tokens using expires_at (♯6574) — @LaelLuo'
type: change
---

<!-- chronolog:begin region="header" -->
# :bug: fix(rmcp-client): refresh OAuth tokens using expires_at (#6574) — @LaelLuo

**Codex CLI** · 2025-11-19 · [[Themes/account-access|Account and Access]] · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.59.0) · from [[Releases/Codex CLI/codex-cli-2025-11-19-rust-v0-59-0-github-263735550-757042e7|0.59.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> :bug: fix(rmcp-client): refresh OAuth tokens using expires_at (#6574) — @LaelLuo
>
> Source: https://github.com/openai/codex/releases/tag/rust-v0.59.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2025-11-19-handle-don-t-trust-directory-selection-in-onboarding-4941-viniciusmotta8|Handle "Don't Trust" directory selection in onboarding (♯4941) — @viniciusmotta8]] · Interface Experience
- [[Changes/Codex CLI/2025-11-19-2-agent-mode-changes-in-rust-v0-59-0|2 Agent Mode changes in rust-v0.59.0]] · Agent Mode
- [[Changes/Codex CLI/2025-11-19-native-compaction-support-added-first-class-support-for-compaction-improving-per|Native Compaction Support]] · Reliability and Performance
- [[Changes/Codex CLI/2025-11-19-promote-shared-helpers-for-suite-tests-6460-aibrahim|Promote shared helpers for suite tests (♯6460) — @aibrahim]] · Collaboration
- [[Changes/Codex CLI/2025-11-19-15-developer-workflow-changes-in-rust-v0-59-0|15 Developer Workflow changes in rust-v0.59.0]] · Developer Workflow
- [[Changes/Codex CLI/2025-11-19-6-context-window-changes-in-rust-v0-59-0|6 Context Window changes in rust-v0.59.0]] · Context Window
- [[Changes/Codex CLI/2025-11-19-3-mobile-and-desktop-changes-in-rust-v0-59-0|3 Mobile and Desktop changes in rust-v0.59.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2025-11-19-use-shared-network-gating-helper-in-chat-completion-tests-6461-aibrahim|Use shared network gating helper in chat completion tests (♯6461) — @aibrahim]] · Editor Experience
- [[Changes/Codex CLI/2025-11-19-5-model-support-changes-in-rust-v0-59-0|5 Model Support changes in rust-v0.59.0]] · Model Support
- [[Changes/Codex CLI/2025-11-19-5-apps-and-integrations-changes-in-rust-v0-59-0|5 Apps and Integrations changes in rust-v0.59.0]] · Apps and Integrations
- [[Changes/Codex CLI/2025-11-19-7-safety-and-privacy-changes-in-rust-v0-59-0|7 Safety and Privacy changes in rust-v0.59.0]] · Safety and Privacy
- [[Changes/Codex CLI/2025-11-19-credits-are-now-visible-in-status|Credits are now visible in /status]] · Pricing Model
- [[Changes/Codex CLI/2025-11-19-53-other-changes-in-rust-v0-59-0|53 other changes in rust-v0.59.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2025-11-18 · Cline · [[Changes/Cline/2025-11-18-retire-firebase-authentication-by-tseglevskiy-in-https-github-com-cline-cline-pu|Retire firebase authentication]]
- Later: 2025-11-24 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2025-11-24-add-support-for-github-askpass-environment-variable-for-authentication|Add support for GITHUB_ASKPASS environment variable for authentication]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2025-11-19-5cd2ac&body=Card%3A%20Changes%2FCodex%20CLI%2F2025-11-19-bug-fix-rmcp-client-refresh-oauth-tokens-using-expires-at-6574-laelluo.md%0ACard%20ID%3A%20codex-cli-2025-11-19-5cd2ac%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.59.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->