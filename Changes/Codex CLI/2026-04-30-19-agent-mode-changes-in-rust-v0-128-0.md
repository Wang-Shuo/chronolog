---
card_id: codex-cli-2026-04-30-6a19e4
date: '2026-04-30'
description: 'Codex CLI · 2026-04-30 · Agent Mode: 19 changes in 0.128.0 — Added external
  agent session import, including background imports and imported-session title…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1029
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 3d6d13639f0dd05dae2f167dd16cb415270ac1976ca9fcae3e897cb72405d4f4
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-04-30-6a19e4
  comparison: ''
  date: '2026-04-30'
  description: 'Codex CLI — 0.128.0: 19 Agent Mode changes'
  evidence:
  - quote: 'Added external agent session import, including background imports and
      imported-session title handling. (#19895, #20284, #20261)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: 'Made MultiAgentV2 configuration more explicit with thread caps, wait-time
      controls, root/subagent hints, and v2-specific depth handling. (#19360, #19792,
      #19805, #20052, #20180)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19360 feat: surface multi-agent thread limit in spawn description @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19351 Add agents.interrupt_message for interruption markers @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19733 Allow agents.max_threads to work with multi_agent_v2 @andmis'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19058 Add /auto-review-denials retry approval flow @won-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19792 multi_agent_v2: move thread cap into feature config @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19763 refactor: load agent identity runtime eagerly @efrazer-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#17689 [codex-analytics] include user agent in default headers @marksteinbrick-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19764 feat: verify agent identity JWTs with JWKS @efrazer-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19907 Clarify network approval auto-review prompts @maja-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19895 External agent session support @stefanstokic-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19708 Load cloud requirements for agent identity @shijie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20139 Delete multi_agent_v2 followup_task interrupt parameter @andmis'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20180 Make multi-agent v2 ignore agents.max_depth @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20046 test protocol: lock inter-agent commentary phase @friel-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20064 Include auto-review rollout in feedback uploads @won-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19229 Add agent graph store interface @rasmusrygaard'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20284 Import external agent sessions in background @stefanstokic-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 19-agent-mode-changes-in-rust-v0-128-0
  source_release: codex-cli-2026-04-30-rust-v0-128-0-github-315916672-1708ab89
  source_type: github_releases
  theme: agent-mode
  title: 19 Agent Mode changes in rust-v0.128.0
  type: change
related_changes:
- '[[Changes/Cursor/2026-04-29-3-agent-mode-changes-in-build-programmatic-agents|3
  Agent Mode changes in Build programmatic agents…]]'
- '[[Changes/Dify/2026-04-29-2-agent-mode-changes-in-1-14-0|2 Agent Mode changes in
  1.14.0]]'
- '[[Changes/Windsurf/2026-04-29-devin-agent-in-windsurf|Devin Agent in Windsurf]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-04-30-rust-v0-128-0-github-315916672-1708ab89|codex-cli-2026-04-30-rust-v0-128-0-github-315916672-1708ab89]]'
source_type: github_releases
theme: agent-mode
title: 19 Agent Mode changes in rust-v0.128.0
type: change
---

<!-- chronolog:begin region="header" -->
# 19 Agent Mode changes in rust-v0.128.0

**Codex CLI** · 2026-04-30 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.128.0) · from [[Releases/Codex CLI/codex-cli-2026-04-30-rust-v0-128-0-github-315916672-1708ab89|0.128.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added external agent session import, including background imports and imported-session title handling. (#19895, #20284, #20261)

> Made MultiAgentV2 configuration more explicit with thread caps, wait-time controls, root/subagent hints, and v2-specific depth handling. (#19360, #19792, #19805, #20052, #20180)

> #19360 feat: surface multi-agent thread limit in spawn description @jif-oai

> #19351 Add agents.interrupt_message for interruption markers @jif-oai

> #19733 Allow agents.max_threads to work with multi_agent_v2 @andmis

> #19058 Add /auto-review-denials retry approval flow @won-openai

> #19792 multi_agent_v2: move thread cap into feature config @jif-oai

> #19763 refactor: load agent identity runtime eagerly @efrazer-oai

> #17689 [codex-analytics] include user agent in default headers @marksteinbrick-oai

> #19764 feat: verify agent identity JWTs with JWKS @efrazer-oai

> #19907 Clarify network approval auto-review prompts @maja-openai

> #19895 External agent session support @stefanstokic-oai

> #19708 Load cloud requirements for agent identity @shijie-oai

> #20139 Delete multi_agent_v2 followup_task interrupt parameter @andmis

> #20180 Make multi-agent v2 ignore agents.max_depth @jif-oai

> #20046 test protocol: lock inter-agent commentary phase @friel-openai

> #20064 Include auto-review rollout in feedback uploads @won-openai

> #19229 Add agent graph store interface @rasmusrygaard

> #20284 Import external agent sessions in background @stefanstokic-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.128.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-04-30-2-interface-experience-changes-in-rust-v0-128-0|2 Interface Experience changes in rust-v0.128.0]] · Interface Experience
- [[Changes/Codex CLI/2026-04-30-19805-add-multiagentv2-root-and-subagent-context-hints-jif-oai|♯19805 Add MultiAgentV2 root and subagent context hints @jif-oai]] · Context Window
- [[Changes/Codex CLI/2026-04-30-3-mobile-and-desktop-changes-in-rust-v0-128-0|3 Mobile and Desktop changes in rust-v0.128.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-04-30-12-memory-and-personalization-changes-in-rust-v0-128-0|12 Memory and Personalization changes in rust-v0.128.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-04-30-20149-reduce-the-surface-of-collaboration-modes-pakrym-oai|♯20149 Reduce the surface of collaboration modes @pakrym-oai]] · Collaboration
- [[Changes/Codex CLI/2026-04-30-14-developer-workflow-changes-in-rust-v0-128-0|14 Developer Workflow changes in rust-v0.128.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-04-30-37-apps-and-integrations-changes-in-rust-v0-128-0|37 Apps and Integrations changes in rust-v0.128.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-04-30-19443-add-gpt-image-2-to-bundled-openai-docs-skill-kkahadze-oai|♯19443 Add gpt-image-2 to bundled OpenAI Docs skill @kkahadze-oai]] · Image Generation
- [[Changes/Codex CLI/2026-04-30-3-account-and-access-changes-in-rust-v0-128-0|3 Account and Access changes in rust-v0.128.0]] · Account and Access
- [[Changes/Codex CLI/2026-04-30-20045-fix-plan-mode-nudge-test-after-task-completion-signature-change-canvrno-oa|♯20045 Fix plan mode nudge test after task completion signature change @canvrno-oai]] · Editor Experience
- [[Changes/Codex CLI/2026-04-30-21-safety-and-privacy-changes-in-rust-v0-128-0|21 Safety and Privacy changes in rust-v0.128.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-04-30-10-model-support-changes-in-rust-v0-128-0|10 Model Support changes in rust-v0.128.0]] · Model Support
- [[Changes/Codex CLI/2026-04-30-145-other-changes-in-rust-v0-128-0|145 other changes in rust-v0.128.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-04-29 · Windsurf · [[Changes/Windsurf/2026-04-29-devin-agent-in-windsurf|Devin Agent in Windsurf]]
- Later: 2026-05-01 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-05-01-3-agent-mode-changes-in-v1-0-40|3 Agent Mode changes in v1.0.40]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-04-30-6a19e4&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-04-30-19-agent-mode-changes-in-rust-v0-128-0.md%0ACard%20ID%3A%20codex-cli-2026-04-30-6a19e4%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.128.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->