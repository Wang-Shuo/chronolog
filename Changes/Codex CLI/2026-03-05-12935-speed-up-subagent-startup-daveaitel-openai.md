---
card_id: codex-cli-2026-03-05-07ca36
date: '2026-03-05'
description: 'Codex CLI · 2026-03-05 · Reliability and Performance: #12935 Speed up
  subagent startup @daveaitel-openai'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General
    performance: Among other improvements, users will notice that ChatGPT is now…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1176
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: f0cc549602a7bf8e132f140195eac8d5626e8ffee23d8d7be61a8dc92aa57314
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-03-05-07ca36
  comparison: ''
  date: '2026-03-05'
  description: 'Codex CLI — 0.110.0: #12935 Speed up subagent startup @daveaitel-openai'
  evidence:
  - quote: '#12935 Speed up subagent startup @daveaitel-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: codex-cli
  product_name: Codex CLI
  slug: 12935-speed-up-subagent-startup-daveaitel-openai
  source_release: codex-cli-2026-03-05-rust-v0-110-0-github-293239637-d5d06302
  source_type: github_releases
  theme: reliability-performance
  theme_matches:
  - matched_terms:
    - subagent
    score: 50
    theme: agent-mode
  - matched_terms:
    - speed
    score: 50
    theme: reliability-performance
  theme_resolution: manual-semantic-rule-v1
  title: '#12935 Speed up subagent startup @daveaitel-openai'
  type: change
related_changes:
- "[[Changes/Open WebUI/2026-03-02-general-improvements-various-improvements-were-implemented-across-the-applicatio|\U0001F504
  General improvements. Various improvements were implemented across…]]"
- '[[Changes/Cursor/2026-03-03-modals-load-faster|Modals load faster]]'
- '[[Changes/Claude Code/2026-03-05-9-reliability-and-performance-changes-in-v2-1-69|9
  Reliability and Performance changes in v2.1.69]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-03-05-rust-v0-110-0-github-293239637-d5d06302|codex-cli-2026-03-05-rust-v0-110-0-github-293239637-d5d06302]]'
source_type: github_releases
theme: reliability-performance
title: ♯12935 Speed up subagent startup @daveaitel-openai
type: change
---

<!-- chronolog:begin region="header" -->
# #12935 Speed up subagent startup @daveaitel-openai

**Codex CLI** · 2026-03-05 · [[Themes/reliability-performance|Reliability and Performance]] · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.110.0) · from [[Releases/Codex CLI/codex-cli-2026-03-05-rust-v0-110-0-github-293239637-d5d06302|0.110.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> #12935 Speed up subagent startup @daveaitel-openai
>
> Source: https://github.com/openai/codex/releases/tag/rust-v0.110.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-03-05-2-model-support-changes-in-rust-v0-110-0|2 Model Support changes in rust-v0.110.0]] · Model Support
- [[Changes/Codex CLI/2026-03-05-13127-nit-disable-on-windows-jif-oai|♯13127 nit: disable on windows @jif-oai]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-03-05-13-agent-mode-changes-in-rust-v0-110-0|13 Agent Mode changes in rust-v0.110.0]] · Agent Mode
- [[Changes/Codex CLI/2026-03-05-13313-renaming-team-to-business-plan-during-tui-onboarding-bwanner-oai|♯13313 Renaming Team to Business plan during TUI onboarding @bwanner-oai]] · Interface Experience
- [[Changes/Codex CLI/2026-03-05-12383-add-new-scopes-to-login-adaley-openai|♯12383 add new scopes to login @adaley-openai]] · Account and Access
- [[Changes/Codex CLI/2026-03-05-4-files-and-data-changes-in-rust-v0-110-0|4 Files and Data changes in rust-v0.110.0]] · Files and Data
- [[Changes/Codex CLI/2026-03-05-13388-config-enforce-enterprise-feature-requirements-bolinfest|♯13388 config: enforce enterprise feature requirements @bolinfest]] · Enterprise and Administration
- [[Changes/Codex CLI/2026-03-05-7-apps-and-integrations-changes-in-rust-v0-110-0|7 Apps and Integrations changes in rust-v0.110.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-03-05-7-developer-workflow-changes-in-rust-v0-110-0|7 Developer Workflow changes in rust-v0.110.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-03-05-5-memory-and-personalization-changes-in-rust-v0-110-0|5 Memory and Personalization changes in rust-v0.110.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-03-05-4-safety-and-privacy-changes-in-rust-v0-110-0|4 Safety and Privacy changes in rust-v0.110.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-03-05-3-context-window-changes-in-rust-v0-110-0|3 Context Window changes in rust-v0.110.0]] · Context Window
- [[Changes/Codex CLI/2026-03-05-71-other-changes-in-rust-v0-110-0|71 other changes in rust-v0.110.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2026-03-05 · Claude Code · [[Changes/Claude Code/2026-03-05-9-reliability-and-performance-changes-in-v2-1-69|9 Reliability and Performance changes in v2.1.69]]
- Later: 2026-03-05 · Codex CLI · [[Changes/Codex CLI/2026-03-05-13446-tui-show-speed-in-session-header-pash-openai|♯13446 tui Show speed in session header @pash-openai]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General performance: Among other improvements, users will notice that ChatGPT is now…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-03-05-07ca36&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-03-05-12935-speed-up-subagent-startup-daveaitel-openai.md%0ACard%20ID%3A%20codex-cli-2026-03-05-07ca36%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.110.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->