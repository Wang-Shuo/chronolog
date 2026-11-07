---
card_id: codex-cli-2026-06-22-23ba70
date: '2026-06-22'
description: 'Codex CLI · 2026-06-22 · Agent Mode: 14 changes in 0.142.0 — Configurable
  rollout token budgets track usage across agent threads, provide remaining-budget…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1082
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2f2eb6b29d6e2f5800b3533f86e607890c7fdeb374f6c7214993c5caf89f4a55
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-06-22-23ba70
  comparison: ''
  date: '2026-06-22'
  description: 'Codex CLI — 0.142.0: 14 Agent Mode changes'
  evidence:
  - quote: 'Configurable rollout token budgets track usage across agent threads, provide
      remaining-budget reminders, and abort turns when exhausted. (#28746, #28494,
      #28707, #29423)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: 'App-server clients can configure multi-agent delegation as disabled, explicit-request-only,
      or proactive at the thread and turn level. (#28685, #28792, #29324)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: Parent agents now receive terminal subagent errors instead of seeing failed
      work as an empty successful completion. (#28375)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28396 [codex] Record external agent import results @charlesgong-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28368 feat: render typed envelopes for multi-agent v2 messages @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28375 core: surface terminal subagent errors to parent agents @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28561 Add join key for MAv2 inter-agent messages @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#19049 feat: opt ChatGPT auth into agent identity @adrian-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28958 core: load AGENTS.md from foreign environments @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28993 [codex] Remove child AGENTS.md prompt experiment @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28989 core: log AGENTS.md paths as URIs @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28685 Add per-turn multi-agent mode @shijie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28792 Expose thread-level multi-agent mode @shijie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#29324 Simplify multi-agent mode controls @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 14-agent-mode-changes-in-rust-v0-142-0
  source_release: codex-cli-2026-06-22-rust-v0-142-0-github-343189954-a218ab4e
  source_type: github_releases
  theme: agent-mode
  title: 14 Agent Mode changes in rust-v0.142.0
  type: change
related_changes:
- '[[Changes/v0/2026-06-19-annotations-mode-lets-you-click-elements-in-the-preview-to-drop-numbered-comment|Annotations
  mode lets you click elements in the preview to drop numbered comments…]]'
- '[[Changes/OpenCode/2026-06-21-core-honor-configured-agent-step-limits-by-forcing-a-final-text-response-instead|Core
  Honor configured agent step limits by forcing a final text response instead…]]'
- '[[Changes/Claude Code/2026-06-22-2-agent-mode-changes-in-v2-1-186|2 Agent Mode
  changes in v2.1.186]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-06-22-rust-v0-142-0-github-343189954-a218ab4e|codex-cli-2026-06-22-rust-v0-142-0-github-343189954-a218ab4e]]'
source_type: github_releases
theme: agent-mode
title: 14 Agent Mode changes in rust-v0.142.0
type: change
---

<!-- chronolog:begin region="header" -->
# 14 Agent Mode changes in rust-v0.142.0

**Codex CLI** · 2026-06-22 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.142.0) · from [[Releases/Codex CLI/codex-cli-2026-06-22-rust-v0-142-0-github-343189954-a218ab4e|0.142.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Configurable rollout token budgets track usage across agent threads, provide remaining-budget reminders, and abort turns when exhausted. (#28746, #28494, #28707, #29423)

> App-server clients can configure multi-agent delegation as disabled, explicit-request-only, or proactive at the thread and turn level. (#28685, #28792, #29324)

> Parent agents now receive terminal subagent errors instead of seeing failed work as an empty successful completion. (#28375)

> #28396 [codex] Record external agent import results @charlesgong-openai

> #28368 feat: render typed envelopes for multi-agent v2 messages @jif-oai

> #28375 core: surface terminal subagent errors to parent agents @jif-oai

> #28561 Add join key for MAv2 inter-agent messages @jif-oai

> #19049 feat: opt ChatGPT auth into agent identity @adrian-openai

> #28958 core: load AGENTS.md from foreign environments @anp-oai

> #28993 [codex] Remove child AGENTS.md prompt experiment @pakrym-oai

> #28989 core: log AGENTS.md paths as URIs @anp-oai

> #28685 Add per-turn multi-agent mode @shijie-oai

> #28792 Expose thread-level multi-agent mode @shijie-oai

> #29324 Simplify multi-agent mode controls @jif-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.142.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-06-22-12-safety-and-privacy-changes-in-rust-v0-142-0|12 Safety and Privacy changes in rust-v0.142.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-06-22-4-interface-experience-changes-in-rust-v0-142-0|4 Interface Experience changes in rust-v0.142.0]] · Interface Experience
- [[Changes/Codex CLI/2026-06-22-26496-make-auto-review-on-request-prompt-more-proactive-maja-openai|♯26496 Make auto-review on-request prompt more proactive @maja-openai]] · Automation and Scheduling
- [[Changes/Codex CLI/2026-06-22-usage-can-now-show-and-redeem-earned-usage-limit-reset-credits-with-confirmation|/usage can now show and redeem earned usage-limit reset credits…]] · Pricing Model
- [[Changes/Codex CLI/2026-06-22-28791-bazel-refresh-expired-macos-sdk-pin-anp-oai|♯28791 bazel: refresh expired macOS SDK pin @anp-oai]] · Mobile and Desktop
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
## Nearby in Agent Mode

- Earlier: 2026-06-22 · Claude Code · [[Changes/Claude Code/2026-06-22-2-agent-mode-changes-in-v2-1-186|2 Agent Mode changes in v2.1.186]]
- Later: 2026-06-22 · ElevenLabs · [[Changes/ElevenLabs/2026-06-22-elevenagents|ElevenAgents]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-06-22-23ba70&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-06-22-14-agent-mode-changes-in-rust-v0-142-0.md%0ACard%20ID%3A%20codex-cli-2026-06-22-23ba70%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.142.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->