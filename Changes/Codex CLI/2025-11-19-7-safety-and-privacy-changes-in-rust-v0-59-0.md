---
card_id: codex-cli-2025-11-19-de8149
date: '2025-11-19'
description: 'Codex CLI · 2025-11-19 · Safety and Privacy: 7 changes in 0.59.0 — Windows
  Agent mode: Introduced Agent mode for native Windows. Codex can read files, write…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 948
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8a4baeb7cbec02a2a387748644e240bd3d0460ca842e6aabf94b93a0d769c030
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2025-11-19-de8149
  comparison: ''
  date: '2025-11-19'
  description: 'Codex CLI — 0.59.0: 7 Safety and Privacy changes'
  evidence:
  - quote: 'Windows Agent mode: Introduced Agent mode for native Windows. Codex can
      read files, write files, and run commands in your working folder with fewer
      approvals. Agent mode uses a new experimental Windows sandbox to limit filesystem
      and network access. Learn more at https://developers.openai.com/codex/windows'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.59.0
  - quote: 'feat: tweak windows sandbox strings (#6875) — @ae'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.59.0
  - quote: 'chore: update windows sandbox docs (#6872) — @ae'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.59.0
  - quote: smoketest for browser vuln, rough draft of Windows security doc (#6822)
      — @iceweasel
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.59.0
  - quote: 'windows sandbox: support multiple workspace roots (#6854) — @iceweasel'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.59.0
  - quote: Prompt to turn on windows sandbox when auto mode selected. (#6618) — @iceweasel
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.59.0
  - quote: move cap_sid file into ~/.codex so the sandbox cannot overwrite it (#6798)
      — @iceweasel
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.59.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 7-safety-and-privacy-changes-in-rust-v0-59-0
  source_release: codex-cli-2025-11-19-rust-v0-59-0-github-263735550-757042e7
  source_type: github_releases
  theme: safety-privacy
  title: 7 Safety and Privacy changes in rust-v0.59.0
  type: change
related_changes:
- '[[Changes/Dify/2025-11-13-2-safety-and-privacy-changes-in-1-10-0|2 Safety and Privacy
  changes in 1.10.0]]'
- '[[Changes/GitHub Copilot CLI/2025-11-17-2-safety-and-privacy-changes-in-v0-0-359|2
  Safety and Privacy changes in v0.0.359]]'
- '[[Changes/GitHub Copilot CLI/2025-11-18-fix-file-operations-timing-out-while-waiting-for-user-permission|Fix
  file operations timing out while waiting for user permission]]'
source_release: '[[Releases/Codex CLI/codex-cli-2025-11-19-rust-v0-59-0-github-263735550-757042e7|codex-cli-2025-11-19-rust-v0-59-0-github-263735550-757042e7]]'
source_type: github_releases
theme: safety-privacy
title: 7 Safety and Privacy changes in rust-v0.59.0
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Safety and Privacy changes in rust-v0.59.0

**Codex CLI** · 2025-11-19 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.59.0) · from [[Releases/Codex CLI/codex-cli-2025-11-19-rust-v0-59-0-github-263735550-757042e7|0.59.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Windows Agent mode: Introduced Agent mode for native Windows. Codex can read files, write files, and run commands in your working folder with fewer approvals. Agent mode uses a new experimental Windows sandbox to limit filesystem and network access. Learn more at https://developers.openai.com/codex/windows

> feat: tweak windows sandbox strings (#6875) — @ae

> chore: update windows sandbox docs (#6872) — @ae

> smoketest for browser vuln, rough draft of Windows security doc (#6822) — @iceweasel

> windows sandbox: support multiple workspace roots (#6854) — @iceweasel

> Prompt to turn on windows sandbox when auto mode selected. (#6618) — @iceweasel

> move cap_sid file into ~/.codex so the sandbox cannot overwrite it (#6798) — @iceweasel

Source: https://github.com/openai/codex/releases/tag/rust-v0.59.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2025-11-19-handle-don-t-trust-directory-selection-in-onboarding-4941-viniciusmotta8|Handle "Don't Trust" directory selection in onboarding (♯4941) — @viniciusmotta8]] · Interface Experience
- [[Changes/Codex CLI/2025-11-19-2-agent-mode-changes-in-rust-v0-59-0|2 Agent Mode changes in rust-v0.59.0]] · Agent Mode
- [[Changes/Codex CLI/2025-11-19-native-compaction-support-added-first-class-support-for-compaction-improving-per|Native Compaction Support]] · Reliability and Performance
- [[Changes/Codex CLI/2025-11-19-bug-fix-rmcp-client-refresh-oauth-tokens-using-expires-at-6574-laelluo|:bug: fix(rmcp-client): refresh OAuth tokens using expires_at (♯6574) — @LaelLuo]] · Account and Access
- [[Changes/Codex CLI/2025-11-19-promote-shared-helpers-for-suite-tests-6460-aibrahim|Promote shared helpers for suite tests (♯6460) — @aibrahim]] · Collaboration
- [[Changes/Codex CLI/2025-11-19-15-developer-workflow-changes-in-rust-v0-59-0|15 Developer Workflow changes in rust-v0.59.0]] · Developer Workflow
- [[Changes/Codex CLI/2025-11-19-6-context-window-changes-in-rust-v0-59-0|6 Context Window changes in rust-v0.59.0]] · Context Window
- [[Changes/Codex CLI/2025-11-19-3-mobile-and-desktop-changes-in-rust-v0-59-0|3 Mobile and Desktop changes in rust-v0.59.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2025-11-19-use-shared-network-gating-helper-in-chat-completion-tests-6461-aibrahim|Use shared network gating helper in chat completion tests (♯6461) — @aibrahim]] · Editor Experience
- [[Changes/Codex CLI/2025-11-19-5-model-support-changes-in-rust-v0-59-0|5 Model Support changes in rust-v0.59.0]] · Model Support
- [[Changes/Codex CLI/2025-11-19-5-apps-and-integrations-changes-in-rust-v0-59-0|5 Apps and Integrations changes in rust-v0.59.0]] · Apps and Integrations
- [[Changes/Codex CLI/2025-11-19-credits-are-now-visible-in-status|Credits are now visible in /status]] · Pricing Model
- [[Changes/Codex CLI/2025-11-19-53-other-changes-in-rust-v0-59-0|53 other changes in rust-v0.59.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2025-11-18 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2025-11-18-fix-file-operations-timing-out-while-waiting-for-user-permission|Fix file operations timing out while waiting for user permission]]
- Later: 2025-11-20 · Codex CLI · [[Changes/Codex CLI/2025-11-20-shell-reliability-and-sandbox-warnings-fallback-shell-selection-is-hardened-and|Shell reliability and sandbox warnings]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2025-11-19-de8149&body=Card%3A%20Changes%2FCodex%20CLI%2F2025-11-19-7-safety-and-privacy-changes-in-rust-v0-59-0.md%0ACard%20ID%3A%20codex-cli-2025-11-19-de8149%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.59.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->