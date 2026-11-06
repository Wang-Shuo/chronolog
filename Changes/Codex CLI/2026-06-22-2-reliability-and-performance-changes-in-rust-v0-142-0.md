---
card_id: codex-cli-2026-06-22-9227a0
date: '2026-06-22'
description: 'Codex CLI · 2026-06-22 · Reliability and Performance: 2 changes in 0.142.0
  — #28782 [codex] trace tools build latency @owenlin0'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General
    performance: Among other improvements, users will notice that ChatGPT is now…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1285
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a8537190cc403862ce1fa9f336fee4d3b48e3d2f9925bb65a16dabf82a37ad47
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-06-22-9227a0
  comparison: ''
  date: '2026-06-22'
  description: 'Codex CLI — 0.142.0: 2 Reliability and Performance changes'
  evidence:
  - quote: '#28782 [codex] trace tools build latency @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#29042 [codex] trace pre-sampling skill and persistence latency @rphilizaire-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 2-reliability-and-performance-changes-in-rust-v0-142-0
  source_release: codex-cli-2026-06-22-rust-v0-142-0-github-343189954-a218ab4e
  source_type: github_releases
  theme: reliability-performance
  title: 2 Reliability and Performance changes in rust-v0.142.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-06-17-improved-auto-retry-api-connection-drops-mid-thinking-now-automatically-retry-in|Improved
  auto-retry: API connection drops mid-thinking now automatically retry…]]'
- '[[Changes/ChatGPT/2026-06-18-easier-conversation-sharing-sharing-a-conversation-is-now-faster-with-a-one-clic|Easier
  conversation sharing]]'
- '[[Changes/Claude Code/2026-06-20-the-stream-stall-hint-now-reads-waiting-for-api-response-will-retry-in-instead-o|The
  stream-stall hint now reads "Waiting for API response · will retry in …" instead…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-06-22-rust-v0-142-0-github-343189954-a218ab4e|codex-cli-2026-06-22-rust-v0-142-0-github-343189954-a218ab4e]]'
source_type: github_releases
theme: reliability-performance
title: 2 Reliability and Performance changes in rust-v0.142.0
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Reliability and Performance changes in rust-v0.142.0

**Codex CLI** · 2026-06-22 · [[Themes/reliability-performance|Reliability and Performance]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.142.0) · from [[Releases/Codex CLI/codex-cli-2026-06-22-rust-v0-142-0-github-343189954-a218ab4e|0.142.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> #28782 [codex] trace tools build latency @owenlin0

> #29042 [codex] trace pre-sampling skill and persistence latency @rphilizaire-openai

Source: https://github.com/openai/codex/releases/tag/rust-v0.142.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-06-22-12-safety-and-privacy-changes-in-rust-v0-142-0|12 Safety and Privacy changes in rust-v0.142.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-06-22-4-interface-experience-changes-in-rust-v0-142-0|4 Interface Experience changes in rust-v0.142.0]] · Interface Experience
- [[Changes/Codex CLI/2026-06-22-26496-make-auto-review-on-request-prompt-more-proactive-maja-openai|♯26496 Make auto-review on-request prompt more proactive @maja-openai]] · Automation and Scheduling
- [[Changes/Codex CLI/2026-06-22-usage-can-now-show-and-redeem-earned-usage-limit-reset-credits-with-confirmation|/usage can now show and redeem earned usage-limit reset credits…]] · Pricing Model
- [[Changes/Codex CLI/2026-06-22-28791-bazel-refresh-expired-macos-sdk-pin-anp-oai|♯28791 bazel: refresh expired macOS SDK pin @anp-oai]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-06-22-14-agent-mode-changes-in-rust-v0-142-0|14 Agent Mode changes in rust-v0.142.0]] · Agent Mode
- [[Changes/Codex CLI/2026-06-22-26707-pac-2-add-shared-auth-system-proxy-contract-canvrno-oai|♯26707 PAC 2 - Add shared auth system proxy contract @canvrno-oai]] · Collaboration
- [[Changes/Codex CLI/2026-06-22-4-developer-workflow-changes-in-rust-v0-142-0|4 Developer Workflow changes in rust-v0.142.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-06-22-10-context-window-changes-in-rust-v0-142-0|10 Context Window changes in rust-v0.142.0]] · Context Window
- [[Changes/Codex CLI/2026-06-22-29289-code-mode-preserve-initial-yield-at-completion-cconger|♯29289 code-mode: preserve initial yield at completion @cconger]] · Editor Experience
- [[Changes/Codex CLI/2026-06-22-37-apps-and-integrations-changes-in-rust-v0-142-0|37 Apps and Integrations changes in rust-v0.142.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-06-22-29022-codex-support-protected-resource-oauth-discovery-xl-openai|♯29022 codex Support protected resource OAuth discovery @xl-openai]] · Account and Access
- [[Changes/Codex CLI/2026-06-22-28770-connectors-ignore-synthetic-links-for-app-accessibility-adaley-openai|♯28770 connectors Ignore synthetic links for app accessibility @adaley-openai]] · Accessibility and Localization
- [[Changes/Codex CLI/2026-06-22-29086-document-raw-response-item-compatibility-jif-oai|♯29086 Document raw response item compatibility @jif-oai]] · Files and Data
- [[Changes/Codex CLI/2026-06-22-3-model-support-changes-in-rust-v0-142-0|3 Model Support changes in rust-v0.142.0]] · Model Support
- [[Changes/Codex CLI/2026-06-22-2-search-and-browsing-changes-in-rust-v0-142-0|2 Search and Browsing changes in rust-v0.142.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-06-22-98-other-changes-in-rust-v0-142-0|98 other changes in rust-v0.142.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2026-06-20 · Claude Code · [[Changes/Claude Code/2026-06-20-the-stream-stall-hint-now-reads-waiting-for-api-response-will-retry-in-instead-o|The stream-stall hint now reads "Waiting for API response · will retry in …" instead…]]
- Later: 2026-06-23 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-06-23-show-per-model-token-totals-in-usage-and-speed-up-large-history-scans|Show per-model token totals in /usage and speed up large history scans]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General performance: Among other improvements, users will notice that ChatGPT is now…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-06-22-9227a0&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-06-22-2-reliability-and-performance-changes-in-rust-v0-142-0.md%0ACard%20ID%3A%20codex-cli-2026-06-22-9227a0%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.142.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->