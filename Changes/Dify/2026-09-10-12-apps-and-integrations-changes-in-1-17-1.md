---
card_id: dify-2026-09-10-c3d844
date: '2026-09-10'
description: 'Dify · 2026-09-10 · Apps and Integrations: 12 changes in v1.17.1 - Bug
  Fixes and Improvements — Knowledge base service-API keys were scoped to the whole…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2827
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9287d67f64200ecaf07e925eab308f02a7f02fe5534c70da4e3c5c38e6228da0
product: dify
product_name: Dify
record:
  card_id: dify-2026-09-10-c3d844
  comparison: ''
  date: '2026-09-10'
  description: 'Dify — v1.17.1 - Bug Fixes and Improvements: 12 Apps and Integrations
    changes'
  evidence:
  - quote: 'Knowledge base service-API keys were scoped to the whole workspace: one
      key could read and write every knowledge base in the tenant, so giving an integration
      access to a single knowledge base meant giving it access to all of them. Keys
      can now be bound to specific knowledge bases from the knowledge base''s API
      access panel, with a workspace / this-knowledge-base scope selector at creation
      time. A bound key returns `403` for any other dataset — both documents and retrieval
      — and for endpoints that carry no dataset ID, such as list-all. Existing keys
      are unbound and keep their workspace-wide behavior, so nothing changes when
      you upgrade. (#37569)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: '**Trigger-entry workflows could still be invoked manually** from the Web
      App, Service API, OpenAPI, and MCP `tools/call` — creating workflow runs that
      could never work. These are now rejected before a run or log is created, with
      a shared business code across HTTP and MCP JSON-RPC. Real trigger execution,
      read-only endpoints, and running a historical Start version by ID are unaffected.
      (#41519)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: '**Suggested questions could take minutes, or hang.** With no dedicated
      suggested-question model configured, the endpoint fell back to the workspace
      default — inheriting expensive settings such as `reasoning_effort=high`, a 2,560-token
      output allowance, and the global 600-second plugin timeout, so the browser gave
      up after 100 seconds while the backend kept working. Output is now capped at
      256 tokens, thinking is disabled or set to the lowest supported effort, and
      a request-scoped 30-second timeout applies. One reported case went from 113–344
      seconds to under 3 seconds; an unavailable default model now returns an empty
      list immediately instead of failing. (#41705)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: '**Deleting an MCP provider returned `422`.** Request parsing had started
      reading only query arguments on `DELETE`, while the web client sends `provider_id`
      in the JSON body; custom-model and credential deletion shared the same contract.
      The JSON body is now used as a fallback when the query string is empty, so query-parameter
      deletes keep working too. (#41288)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: '**Skills, Plugins & Triggers**'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: '**Triggers worked in Test Run but never fired in production.** Plugin
      trigger relationships were synchronized from the draft workflow rather than
      the version being published, so published events found no subscriber and no
      workflow started. (#41756)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: The settings dialog is centered at all viewport sizes (#42120), invalid-input
      focus colors are preserved (#42108), Home and Studio route titles are stable
      (#41654), and the plugin detail drawer no longer traps interaction as a modal
      (#41473)
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: '**The Console loaded 0.63 MB of support-widget JavaScript on every startup.**
      The Zendesk SDK is now fetched on the first Contact Us action instead: Home
      and Apps load with zero Zendesk requests, and the 36 requests / 628 KB are deferred
      to users who actually open support. (#41653)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'Embedded recommend-banner templates and plugins open in the detail dialog
      rather than navigating away, and banner logos and template authors are preserved
      (#42063, #41828, #41980)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'test(e2e): wait for apps console readiness by @lyzno1 in https://github.com/langgenius/dify/pull/41357'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(plugins): migrate credential rename input by @lyzno1 in https://github.com/langgenius/dify/pull/41552'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(api): extract plugin file upload application service by @hjlarry
      in https://github.com/langgenius/dify/pull/41808'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 12-apps-and-integrations-changes-in-1-17-1
  source_release: dify-2026-09-10-1-17-1-github-386157159-e472b6fe
  source_type: github_releases
  theme: apps-integrations
  title: 12 Apps and Integrations changes in 1.17.1
  type: change
related_changes:
- '[[Changes/OpenHands/2026-09-09-docs-remove-duplicate-openhands-extensions-bullet-in-development-md-by-imitater|docs:
  remove duplicate OpenHands/extensions bullet in DEVELOPMENT.md]]'
- '[[Changes/ChatGPT/2026-09-10-the-data-plugin-helps-you-analyze-connected-business-data-in-chatgpt-work-and-co|Data
  plugin in ChatGPT Work and Codex]]'
- '[[Changes/Claude Code/2026-09-10-7-apps-and-integrations-changes-in-v2-1-268|7
  Apps and Integrations changes in v2.1.268]]'
source_release: '[[Releases/Dify/dify-2026-09-10-1-17-1-github-386157159-e472b6fe|dify-2026-09-10-1-17-1-github-386157159-e472b6fe]]'
source_type: github_releases
theme: apps-integrations
title: 12 Apps and Integrations changes in 1.17.1
type: change
---

<!-- chronolog:begin region="header" -->
# 12 Apps and Integrations changes in 1.17.1

**Dify** · 2026-09-10 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.17.1) · from [[Releases/Dify/dify-2026-09-10-1-17-1-github-386157159-e472b6fe|v1.17.1 - Bug Fixes and Improvements]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Knowledge base service-API keys were scoped to the whole workspace: one key could read and write every knowledge base in the tenant, so giving an integration access to a single knowledge base meant giving it access to all of them. Keys can now be bound to specific knowledge bases from the knowledge base's API access panel, with a workspace / this-knowledge-base scope selector at creation time. A bound key returns `403` for any other dataset — both documents and retrieval — and for endpoints that carry no dataset ID, such as list-all. Existing keys are unbound and keep their workspace-wide behavior, so nothing changes when you upgrade. (#37569)

> **Trigger-entry workflows could still be invoked manually** from the Web App, Service API, OpenAPI, and MCP `tools/call` — creating workflow runs that could never work. These are now rejected before a run or log is created, with a shared business code across HTTP and MCP JSON-RPC. Real trigger execution, read-only endpoints, and running a historical Start version by ID are unaffected. (#41519)

> **Suggested questions could take minutes, or hang.** With no dedicated suggested-question model configured, the endpoint fell back to the workspace default — inheriting expensive settings such as `reasoning_effort=high`, a 2,560-token output allowance, and the global 600-second plugin timeout, so the browser gave up after 100 seconds while the backend kept working. Output is now capped at 256 tokens, thinking is disabled or set to the lowest supported effort, and a request-scoped 30-second timeout applies. One reported case went from 113–344 seconds to under 3 seconds; an unavailable default model now returns an empty list immediately instead of failing. (#41705)

> **Deleting an MCP provider returned `422`.** Request parsing had started reading only query arguments on `DELETE`, while the web client sends `provider_id` in the JSON body; custom-model and credential deletion shared the same contract. The JSON body is now used as a fallback when the query string is empty, so query-parameter deletes keep working too. (#41288)

> **Skills, Plugins & Triggers**

> **Triggers worked in Test Run but never fired in production.** Plugin trigger relationships were synchronized from the draft workflow rather than the version being published, so published events found no subscriber and no workflow started. (#41756)

> The settings dialog is centered at all viewport sizes (#42120), invalid-input focus colors are preserved (#42108), Home and Studio route titles are stable (#41654), and the plugin detail drawer no longer traps interaction as a modal (#41473)

> **The Console loaded 0.63 MB of support-widget JavaScript on every startup.** The Zendesk SDK is now fetched on the first Contact Us action instead: Home and Apps load with zero Zendesk requests, and the 36 requests / 628 KB are deferred to users who actually open support. (#41653)

> Embedded recommend-banner templates and plugins open in the detail dialog rather than navigating away, and banner logos and template authors are preserved (#42063, #41828, #41980)

> test(e2e): wait for apps console readiness by @lyzno1 in https://github.com/langgenius/dify/pull/41357

> refactor(plugins): migrate credential rename input by @lyzno1 in https://github.com/langgenius/dify/pull/41552

> refactor(api): extract plugin file upload application service by @hjlarry in https://github.com/langgenius/dify/pull/41808

Source: https://github.com/langgenius/dify/releases/tag/1.17.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-09-10-4-pricing-model-changes-in-1-17-1|4 Pricing Model changes in 1.17.1]] · Pricing Model
- [[Changes/Dify/2026-09-10-3-automation-and-scheduling-changes-in-1-17-1|3 Automation and Scheduling changes in 1.17.1]] · Automation and Scheduling
- [[Changes/Dify/2026-09-10-8-interface-experience-changes-in-1-17-1|8 Interface Experience changes in 1.17.1]] · Interface Experience
- [[Changes/Dify/2026-09-10-76-model-support-changes-in-1-17-1|76 Model Support changes in 1.17.1]] · Model Support
- [[Changes/Dify/2026-09-10-42-agent-mode-changes-in-1-17-1|42 Agent Mode changes in 1.17.1]] · Agent Mode
- [[Changes/Dify/2026-09-10-4-developer-workflow-changes-in-1-17-1|4 Developer Workflow changes in 1.17.1]] · Developer Workflow
- [[Changes/Dify/2026-09-10-3-collaboration-changes-in-1-17-1|3 Collaboration changes in 1.17.1]] · Collaboration
- [[Changes/Dify/2026-09-10-2-memory-and-personalization-changes-in-1-17-1|2 Memory and Personalization changes in 1.17.1]] · Memory and Personalization
- [[Changes/Dify/2026-09-10-16-safety-and-privacy-changes-in-1-17-1|16 Safety and Privacy changes in 1.17.1]] · Safety and Privacy
- [[Changes/Dify/2026-09-10-13-files-and-data-changes-in-1-17-1|13 Files and Data changes in 1.17.1]] · Files and Data
- [[Changes/Dify/2026-09-10-skill-packages-built-on-windows-failed-with-a-misleading-error-a-skill-md-using|Skill packages built on Windows failed with a misleading error. A SKILL.md…]] · Mobile and Desktop
- [[Changes/Dify/2026-09-10-6-account-and-access-changes-in-1-17-1|6 Account and Access changes in 1.17.1]] · Account and Access
- [[Changes/Dify/2026-09-10-3-multimodal-input-changes-in-1-17-1|3 Multimodal Input changes in 1.17.1]] · Multimodal Input
- [[Changes/Dify/2026-09-10-6-editor-experience-changes-in-1-17-1|6 Editor Experience changes in 1.17.1]] · Editor Experience
- [[Changes/Dify/2026-09-10-3-accessibility-and-localization-changes-in-1-17-1|3 Accessibility and Localization changes in 1.17.1]] · Accessibility and Localization
- [[Changes/Dify/2026-09-10-a-plugin-could-exhaust-worker-memory-with-one-declared-number-the-blob-chunk-mer|A plugin could exhaust worker memory with one declared number. The blob chunk…]] · Reliability and Performance
- [[Changes/Dify/2026-09-10-6-context-window-changes-in-1-17-1|6 Context Window changes in 1.17.1]] · Context Window
- [[Changes/Dify/2026-09-10-205-other-changes-in-1-17-1|205 other changes in 1.17.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-09-10 · Claude Code · [[Changes/Claude Code/2026-09-10-7-apps-and-integrations-changes-in-v2-1-268|7 Apps and Integrations changes in v2.1.268]]
- Later: 2026-09-10 · Lovable · [[Changes/Lovable/2026-09-10-chat-connectors-canva-and-wispr-flow|Chat connectors: Canva and Wispr Flow]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-09-10-c3d844&body=Card%3A%20Changes%2FDify%2F2026-09-10-12-apps-and-integrations-changes-in-1-17-1.md%0ACard%20ID%3A%20dify-2026-09-10-c3d844%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.17.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->