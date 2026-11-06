---
card_id: dify-2026-08-25-577543
date: '2026-08-25'
description: 'Dify · 2026-08-25 · Safety and Privacy: 16 changes in v1.17.0 — **Agent:
  E2B Sandbox, Home Snapshots, and Skill Management**'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1227
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d99627bc14c40dca5765d9212f0dad952aec2db27dce09efb20bf9385133dfd5
product: dify
product_name: Dify
record:
  card_id: dify-2026-08-25-577543
  comparison: ''
  date: '2026-08-25'
  description: 'Dify — v1.17.0: 16 Safety and Privacy changes'
  evidence:
  - quote: '**Agent: E2B Sandbox, Home Snapshots, and Skill Management**'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: '**E2B sandbox backend**: agent shell/code execution can now run on [E2B](https://e2b.dev)
      cloud sandboxes in addition to the local sandbox. Select the backend with `DIFY_AGENT_RUNTIME_BACKEND`;
      a new `docker-compose.e2b.yaml` ships the E2B stack, E2B traffic is authenticated,
      and the E2B template is synced on release (#39480, #39705, #39873, #39996, #40858,
      #40871, #40891, #40892).'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: '**Build-time Home Snapshots**: when an agent build is applied (published),
      the agent''s sandbox home directory — installed packages, prepared files, working
      state — is captured and subsequent runs of the published agent restore their
      home directory from that snapshot, so the agent starts from the exact filesystem
      state it had at build time. (#39702, #40876, #40996).'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: '**Agent runtime / sandbox** (`docker/envs/core-services/dify-agent.env.example`)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'Local sandbox: `DIFY_AGENT_LOCAL_SANDBOX_ENDPOINT`, `DIFY_AGENT_LOCAL_SANDBOX_AUTH_TOKEN`'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: '**Auth / security**'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: '`docker/docker-compose.e2b.yaml` — **new** (E2B agent sandbox stack)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'fix(web): gate plugin auth permission hint by @hjlarry in https://github.com/langgenius/dify/pull/39721'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'fix(web): clarify member permission exception copy by @WTW0313 in https://github.com/langgenius/dify/pull/39917'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'fix: get role and list role need filter billing permission key by @fatelei
      in https://github.com/langgenius/dify/pull/38218'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'chore: dep inject for model in agent app sandbox upload by @likalikali
      in https://github.com/langgenius/dify/pull/40153'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'fix: restrict app deploy to explicit enterprise permission by @zhangx1n
      in https://github.com/langgenius/dify/pull/40564'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate agent app sandbox sessions and ORM models to SQLite by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40568'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate annotation security sessions and ORM models to SQLite by
      @asukaminato0721 in https://github.com/langgenius/dify/pull/40604'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'fix(api): add missing admin and RBAC permission decorators to model credentials
      GET endpoints by @FasihUrRahman in https://github.com/langgenius/dify/pull/40962'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'fix(api): enforce APP_EDIT RBAC permission on MCP server refresh endpoint
      by @loulanyue in https://github.com/langgenius/dify/pull/41235'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 16-safety-and-privacy-changes-in-1-17-0
  source_release: dify-2026-08-25-1-17-0-github-376348099-66c16161
  source_type: github_releases
  theme: safety-privacy
  title: 16 Safety and Privacy changes in 1.17.0
  type: change
related_changes:
- '[[Changes/Replit/2026-08-21-run-black-box-pen-tests|Run black-box pen tests]]'
- '[[Changes/ElevenLabs/2026-08-24-packages|Packages]]'
- '[[Changes/Claude Code/2026-08-25-6-safety-and-privacy-changes-in-v2-1-246|6 Safety
  and Privacy changes in v2.1.246]]'
source_release: '[[Releases/Dify/dify-2026-08-25-1-17-0-github-376348099-66c16161|dify-2026-08-25-1-17-0-github-376348099-66c16161]]'
source_type: github_releases
theme: safety-privacy
title: 16 Safety and Privacy changes in 1.17.0
type: change
---

<!-- chronolog:begin region="header" -->
# 16 Safety and Privacy changes in 1.17.0

**Dify** · 2026-08-25 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.17.0) · from [[Releases/Dify/dify-2026-08-25-1-17-0-github-376348099-66c16161|v1.17.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **Agent: E2B Sandbox, Home Snapshots, and Skill Management**

> **E2B sandbox backend**: agent shell/code execution can now run on [E2B](https://e2b.dev) cloud sandboxes in addition to the local sandbox. Select the backend with `DIFY_AGENT_RUNTIME_BACKEND`; a new `docker-compose.e2b.yaml` ships the E2B stack, E2B traffic is authenticated, and the E2B template is synced on release (#39480, #39705, #39873, #39996, #40858, #40871, #40891, #40892).

> **Build-time Home Snapshots**: when an agent build is applied (published), the agent's sandbox home directory — installed packages, prepared files, working state — is captured and subsequent runs of the published agent restore their home directory from that snapshot, so the agent starts from the exact filesystem state it had at build time. (#39702, #40876, #40996).

> **Agent runtime / sandbox** (`docker/envs/core-services/dify-agent.env.example`)

> Local sandbox: `DIFY_AGENT_LOCAL_SANDBOX_ENDPOINT`, `DIFY_AGENT_LOCAL_SANDBOX_AUTH_TOKEN`

> **Auth / security**

> `docker/docker-compose.e2b.yaml` — **new** (E2B agent sandbox stack)

> fix(web): gate plugin auth permission hint by @hjlarry in https://github.com/langgenius/dify/pull/39721

> fix(web): clarify member permission exception copy by @WTW0313 in https://github.com/langgenius/dify/pull/39917

> fix: get role and list role need filter billing permission key by @fatelei in https://github.com/langgenius/dify/pull/38218

> chore: dep inject for model in agent app sandbox upload by @likalikali in https://github.com/langgenius/dify/pull/40153

> fix: restrict app deploy to explicit enterprise permission by @zhangx1n in https://github.com/langgenius/dify/pull/40564

> test: migrate agent app sandbox sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40568

> test: migrate annotation security sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40604

> fix(api): add missing admin and RBAC permission decorators to model credentials GET endpoints by @FasihUrRahman in https://github.com/langgenius/dify/pull/40962

> fix(api): enforce APP_EDIT RBAC permission on MCP server refresh endpoint by @loulanyue in https://github.com/langgenius/dify/pull/41235

Source: https://github.com/langgenius/dify/releases/tag/1.17.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-08-25-2-enterprise-and-administration-changes-in-1-17-0|2 Enterprise and Administration changes in 1.17.0]] · Enterprise and Administration
- [[Changes/Dify/2026-08-25-audio-asr-now-accepts-audio-x-m4a-and-audio-mime-types-are-validated-more-accura|Audio ASR now accepts audio/x-m4a, and audio MIME types are validated more…]] · Voice and Audio
- [[Changes/Dify/2026-08-25-5-collaboration-changes-in-1-17-0|5 Collaboration changes in 1.17.0]] · Collaboration
- [[Changes/Dify/2026-08-25-feat-workflow-support-human-input-in-loop-and-iteration-by-laipz8200-in-https-gi|feat(workflow): support human input in loop and iteration]] · Automation and Scheduling
- [[Changes/Dify/2026-08-25-4-editor-experience-changes-in-1-17-0|4 Editor Experience changes in 1.17.0]] · Editor Experience
- [[Changes/Dify/2026-08-25-3-multimodal-input-changes-in-1-17-0|3 Multimodal Input changes in 1.17.0]] · Multimodal Input
- [[Changes/Dify/2026-08-25-53-agent-mode-changes-in-1-17-0|53 Agent Mode changes in 1.17.0]] · Agent Mode
- [[Changes/Dify/2026-08-25-4-developer-workflow-changes-in-1-17-0|4 Developer Workflow changes in 1.17.0]] · Developer Workflow
- [[Changes/Dify/2026-08-25-93-model-support-changes-in-1-17-0|93 Model Support changes in 1.17.0]] · Model Support
- [[Changes/Dify/2026-08-25-13-account-and-access-changes-in-1-17-0|13 Account and Access changes in 1.17.0]] · Account and Access
- [[Changes/Dify/2026-08-25-28-apps-and-integrations-changes-in-1-17-0|28 Apps and Integrations changes in 1.17.0]] · Apps and Integrations
- [[Changes/Dify/2026-08-25-7-pricing-model-changes-in-1-17-0|7 Pricing Model changes in 1.17.0]] · Pricing Model
- [[Changes/Dify/2026-08-25-5-files-and-data-changes-in-1-17-0|5 Files and Data changes in 1.17.0]] · Files and Data
- [[Changes/Dify/2026-08-25-workflow-runtime-stability|Workflow & Runtime Stability]] · Reliability and Performance
- [[Changes/Dify/2026-08-25-8-context-window-changes-in-1-17-0|8 Context Window changes in 1.17.0]] · Context Window
- [[Changes/Dify/2026-08-25-9-interface-experience-changes-in-1-17-0|9 Interface Experience changes in 1.17.0]] · Interface Experience
- [[Changes/Dify/2026-08-25-3-accessibility-and-localization-changes-in-1-17-0|3 Accessibility and Localization changes in 1.17.0]] · Accessibility and Localization
- [[Changes/Dify/2026-08-25-351-other-changes-in-1-17-0|351 other changes in 1.17.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-08-25 · Claude Code · [[Changes/Claude Code/2026-08-25-6-safety-and-privacy-changes-in-v2-1-246|6 Safety and Privacy changes in v2.1.246]]
- Later: 2026-08-25 · Gemini CLI · [[Changes/Gemini CLI/2026-08-25-ssr-agent-issue-fix-26120-clarify-privacy-notice-wording-and-selection-options-b|SSR Agent Issue Fix (26120): Clarify privacy notice wording and selection options]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-08-25-577543&body=Card%3A%20Changes%2FDify%2F2026-08-25-16-safety-and-privacy-changes-in-1-17-0.md%0ACard%20ID%3A%20dify-2026-08-25-577543%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.17.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->