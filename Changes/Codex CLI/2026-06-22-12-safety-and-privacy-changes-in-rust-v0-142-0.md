---
card_id: codex-cli-2026-06-22-0b9efa
date: '2026-06-22'
description: 'Codex CLI · 2026-06-22 · Safety and Privacy: 12 changes in 0.142.0 —
  Remote environments now preserve executor-native paths, shells, `AGENTS.md` discovery,
  and…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1163
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f821a2e9a8a39b8f723cea1d8d97ed36897e045c31af60d1b53f90707e30b24b
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-06-22-0b9efa
  comparison: ''
  date: '2026-06-22'
  description: 'Codex CLI — 0.142.0: 12 Safety and Privacy changes'
  evidence:
  - quote: 'Remote environments now preserve executor-native paths, shells, `AGENTS.md`
      discovery, and sandbox behavior across operating systems. (#28146, #28152, #28958,
      #28983, #29099, #29108, #29113, #29424)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28542 perf(config): defer remote sandbox hostname lookup @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28359 Run fs helper through Windows sandbox wrapper @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28915 Avoid sandbox helper in apply_patch approval tests @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28914 Scope MCP sandbox metadata to server environment @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28943 [codex] Fix Windows sandbox runtime ACL refresh @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#29108 Carry sandbox intent to remote exec servers @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#29371 Propagate safety buffering events to app-server clients @fc-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#29113 Apply sandbox intent inside remote exec servers @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#29424 Report remote sandbox denials semantically @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#26678 permission profiles: expose availability to clients @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#29479 fix(config): address permission profile review follow-ups @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 12-safety-and-privacy-changes-in-rust-v0-142-0
  source_release: codex-cli-2026-06-22-rust-v0-142-0-github-343189954-a218ab4e
  source_type: github_releases
  theme: safety-privacy
  title: 12 Safety and Privacy changes in rust-v0.142.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-06-18-7-safety-and-privacy-changes-in-rust-v0-141-0|7
  Safety and Privacy changes in rust-v0.141.0]]'
- '[[Changes/v0/2026-06-19-responding-to-an-agent-prompt-for-an-environment-variable-permission-question-or|Responding
  to an agent prompt for an environment variable, permission, question…]]'
- '[[Changes/Claude Code/2026-06-22-2-safety-and-privacy-changes-in-v2-1-186|2 Safety
  and Privacy changes in v2.1.186]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-06-22-rust-v0-142-0-github-343189954-a218ab4e|codex-cli-2026-06-22-rust-v0-142-0-github-343189954-a218ab4e]]'
source_type: github_releases
theme: safety-privacy
title: 12 Safety and Privacy changes in rust-v0.142.0
type: change
---

<!-- chronolog:begin region="header" -->
# 12 Safety and Privacy changes in rust-v0.142.0

**Codex CLI** · 2026-06-22 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.142.0) · from [[Releases/Codex CLI/codex-cli-2026-06-22-rust-v0-142-0-github-343189954-a218ab4e|0.142.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Remote environments now preserve executor-native paths, shells, `AGENTS.md` discovery, and sandbox behavior across operating systems. (#28146, #28152, #28958, #28983, #29099, #29108, #29113, #29424)

> #28542 perf(config): defer remote sandbox hostname lookup @fcoury-oai

> #28359 Run fs helper through Windows sandbox wrapper @iceweasel-oai

> #28915 Avoid sandbox helper in apply_patch approval tests @jif-oai

> #28914 Scope MCP sandbox metadata to server environment @jif-oai

> #28943 [codex] Fix Windows sandbox runtime ACL refresh @iceweasel-oai

> #29108 Carry sandbox intent to remote exec servers @jif-oai

> #29371 Propagate safety buffering events to app-server clients @fc-oai

> #29113 Apply sandbox intent inside remote exec servers @jif-oai

> #29424 Report remote sandbox denials semantically @jif-oai

> #26678 permission profiles: expose availability to clients @viyatb-oai

> #29479 fix(config): address permission profile review follow-ups @viyatb-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.142.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-06-22-4-interface-experience-changes-in-rust-v0-142-0|4 Interface Experience changes in rust-v0.142.0]] · Interface Experience
- [[Changes/Codex CLI/2026-06-22-26496-make-auto-review-on-request-prompt-more-proactive-maja-openai|♯26496 Make auto-review on-request prompt more proactive @maja-openai]] · Automation and Scheduling
- [[Changes/Codex CLI/2026-06-22-usage-can-now-show-and-redeem-earned-usage-limit-reset-credits-with-confirmation|/usage can now show and redeem earned usage-limit reset credits…]] · Pricing Model
- [[Changes/Codex CLI/2026-06-22-28791-bazel-refresh-expired-macos-sdk-pin-anp-oai|♯28791 bazel: refresh expired macOS SDK pin @anp-oai]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-06-22-14-agent-mode-changes-in-rust-v0-142-0|14 Agent Mode changes in rust-v0.142.0]] · Agent Mode
- [[Changes/Codex CLI/2026-06-22-26707-pac-2-add-shared-auth-system-proxy-contract-canvrno-oai|♯26707 PAC 2 - Add shared auth system proxy contract @canvrno-oai]] · Collaboration
- [[Changes/Codex CLI/2026-06-22-4-developer-workflow-changes-in-rust-v0-142-0|4 Developer Workflow changes in rust-v0.142.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-06-22-10-context-window-changes-in-rust-v0-142-0|10 Context Window changes in rust-v0.142.0]] · Context Window
- [[Changes/Codex CLI/2026-06-22-29289-code-mode-preserve-initial-yield-at-completion-cconger|♯29289 code-mode: preserve initial yield at completion @cconger]] · Editor Experience
- [[Changes/Codex CLI/2026-06-22-2-reliability-and-performance-changes-in-rust-v0-142-0|2 Reliability and Performance changes in rust-v0.142.0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-06-22-37-apps-and-integrations-changes-in-rust-v0-142-0|37 Apps and Integrations changes in rust-v0.142.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-06-22-29022-codex-support-protected-resource-oauth-discovery-xl-openai|♯29022 codex Support protected resource OAuth discovery @xl-openai]] · Account and Access
- [[Changes/Codex CLI/2026-06-22-28770-connectors-ignore-synthetic-links-for-app-accessibility-adaley-openai|♯28770 connectors Ignore synthetic links for app accessibility @adaley-openai]] · Accessibility and Localization
- [[Changes/Codex CLI/2026-06-22-29086-document-raw-response-item-compatibility-jif-oai|♯29086 Document raw response item compatibility @jif-oai]] · Files and Data
- [[Changes/Codex CLI/2026-06-22-3-model-support-changes-in-rust-v0-142-0|3 Model Support changes in rust-v0.142.0]] · Model Support
- [[Changes/Codex CLI/2026-06-22-2-search-and-browsing-changes-in-rust-v0-142-0|2 Search and Browsing changes in rust-v0.142.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-06-22-98-other-changes-in-rust-v0-142-0|98 other changes in rust-v0.142.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-06-22 · Claude Code · [[Changes/Claude Code/2026-06-22-2-safety-and-privacy-changes-in-v2-1-186|2 Safety and Privacy changes in v2.1.186]]
- Later: 2026-06-22 · Google Antigravity · [[Changes/Google Antigravity/2026-06-22-fixed-agent-permission-issue-fixed-the-bug-where-changes-to-the-agent-security-m|Fixed Agent Permission Issue]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-06-22-0b9efa&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-06-22-12-safety-and-privacy-changes-in-rust-v0-142-0.md%0ACard%20ID%3A%20codex-cli-2026-06-22-0b9efa%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.142.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->