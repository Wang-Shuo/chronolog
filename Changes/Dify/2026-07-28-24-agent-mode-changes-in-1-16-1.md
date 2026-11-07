---
card_id: dify-2026-07-28-e88674
date: '2026-07-28'
description: 'Dify · 2026-07-28 · Agent Mode: 24 changes in v1.16.1 - Bug Fixes and
  Security Enhancements — Show workflow node runs in agent execution logs (#39471)'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1118
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9894c60212cecfd984772893878987b5ae7fb0863fa723d58fda9e36406990b9
product: dify
product_name: Dify
record:
  card_id: dify-2026-07-28-e88674
  comparison: ''
  date: '2026-07-28'
  description: 'Dify — v1.16.1 - Bug Fixes and Security Enhancements: 24 Agent Mode
    changes'
  evidence:
  - quote: Show workflow node runs in agent execution logs (#39471)
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: Include workflow runs in agent monitoring stats (#39354)
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: Block unpublished agents from being used in workflows (#39532)
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: Prevent agent preview actions from being clipped (#39510)
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: Made agent composer save and publish state consistent (#39637)
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: '| `AGENT_BACKEND_API_TOKEN` | `dify-agent-run-token-for-dev-only` | Same
      token on the agent backend side. Must match `DIFY_AGENT_API_TOKEN`. |'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: '> `DIFY_AGENT_API_TOKEN` is a **new required variable** for secure communication
      between the Dify API and agent backend. The default value (`dify-agent-run-token-for-dev-only`)
      is insecure and **must be replaced in production**. Generate one with:'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: '> Set the same value as `AGENT_BACKEND_API_TOKEN` on the agent backend
      side.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: '**Bearer auth**: `AGENT_BACKEND_API_TOKEN` / `DIFY_AGENT_API_TOKEN` are
      now passed to `api`, `worker`, and `agent_backend` services.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: '`2026_07_22_1500-d2825e7b9c10_scope_agent_debug_conversations.py` — Add
      `draft_type` column to `agent_debug_conversations` and update unique constraint'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: '> Review the new `DIFY_AGENT_API_TOKEN` variable in `.env`. The default
      value is insecure — generate a secure token for production:'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: 'feat(web): add webapp access control to agent access point by @GareArc
      in https://github.com/langgenius/dify/pull/39285'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: 'test: use sqlite3 session in test_agent_app_parameters by @asukaminato0721
      in https://github.com/langgenius/dify/pull/38759'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: 'chore: bump setuptools from 82.0.1 to 83.0.0 in /dify-agent by @dependabot[bot]
      in https://github.com/langgenius/dify/pull/39387'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: 'chore: bump google.golang.org/grpc from 1.82.0 to 1.82.1 in /dify-agent-runtime
      by @dependabot[bot] in https://github.com/langgenius/dify/pull/39386'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: 'chore: bump pyasn1 from 0.6.3 to 0.6.4 in /dify-agent by @dependabot[bot]
      in https://github.com/langgenius/dify/pull/39388'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: 'chore: bump pillow from 12.2.0 to 12.3.0 in /dify-agent by @dependabot[bot]
      in https://github.com/langgenius/dify/pull/39328'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: 'chore(agent): update && simplify readme by @wylswz in https://github.com/langgenius/dify/pull/39584'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: 'chore: bump pypdf from 6.10.2 to 6.14.2 in /dify-agent by @dependabot[bot]
      in https://github.com/langgenius/dify/pull/39502'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: 'feat: add amptitude to new agent by @iamjoel in https://github.com/langgenius/dify/pull/39608'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: 'feat: add bearer auth to agent backend by @wylswz in https://github.com/langgenius/dify/pull/39622'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: 'refactor: make agent composer save and publish state consistent by @iamjoel
      in https://github.com/langgenius/dify/pull/39637'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: 'chore(deps): bump golang.org/x/net from 0.53.0 to 0.55.0 in /dify-agent-runtime
      by @dependabot[bot] in https://github.com/langgenius/dify/pull/39025'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: 'chore: bump pymdown-extensions from 10.21.2 to 11.0 in /dify-agent by
      @dependabot[bot] in https://github.com/langgenius/dify/pull/39618'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 24-agent-mode-changes-in-1-16-1
  source_release: dify-2026-07-28-1-16-1-github-360820489-855a9365
  source_type: github_releases
  theme: agent-mode
  title: 24 Agent Mode changes in 1.16.1
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-07-27-elevenagents-9c1cea|ElevenAgents]]'
- "[[Changes/Open WebUI/2026-07-27-sub-agents-administrators-can-now-enable-sub-agents-which-let-a-model-hand-parts|\U0001F916
  Sub-agents. Administrators can now enable sub-agents, which let a model hand…]]"
- '[[Changes/Cursor/2026-07-28-always-on-cloud-agents-that-build-test-and-ship-code-while-you-keep-working-725c7c|Always-on
  cloud agents that build, test, and ship code while you keep working]]'
source_release: '[[Releases/Dify/dify-2026-07-28-1-16-1-github-360820489-855a9365|dify-2026-07-28-1-16-1-github-360820489-855a9365]]'
source_type: github_releases
theme: agent-mode
title: 24 Agent Mode changes in 1.16.1
type: change
---

<!-- chronolog:begin region="header" -->
# 24 Agent Mode changes in 1.16.1

**Dify** · 2026-07-28 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.16.1) · from [[Releases/Dify/dify-2026-07-28-1-16-1-github-360820489-855a9365|v1.16.1 - Bug Fixes and Security Enhancements]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Show workflow node runs in agent execution logs (#39471)

> Include workflow runs in agent monitoring stats (#39354)

> Block unpublished agents from being used in workflows (#39532)

> Prevent agent preview actions from being clipped (#39510)

> Made agent composer save and publish state consistent (#39637)

> | `AGENT_BACKEND_API_TOKEN` | `dify-agent-run-token-for-dev-only` | Same token on the agent backend side. Must match `DIFY_AGENT_API_TOKEN`. |

> > `DIFY_AGENT_API_TOKEN` is a **new required variable** for secure communication between the Dify API and agent backend. The default value (`dify-agent-run-token-for-dev-only`) is insecure and **must be replaced in production**. Generate one with:

> > Set the same value as `AGENT_BACKEND_API_TOKEN` on the agent backend side.

> **Bearer auth**: `AGENT_BACKEND_API_TOKEN` / `DIFY_AGENT_API_TOKEN` are now passed to `api`, `worker`, and `agent_backend` services.

> `2026_07_22_1500-d2825e7b9c10_scope_agent_debug_conversations.py` — Add `draft_type` column to `agent_debug_conversations` and update unique constraint

> > Review the new `DIFY_AGENT_API_TOKEN` variable in `.env`. The default value is insecure — generate a secure token for production:

> feat(web): add webapp access control to agent access point by @GareArc in https://github.com/langgenius/dify/pull/39285

> test: use sqlite3 session in test_agent_app_parameters by @asukaminato0721 in https://github.com/langgenius/dify/pull/38759

> chore: bump setuptools from 82.0.1 to 83.0.0 in /dify-agent by @dependabot[bot] in https://github.com/langgenius/dify/pull/39387

> chore: bump google.golang.org/grpc from 1.82.0 to 1.82.1 in /dify-agent-runtime by @dependabot[bot] in https://github.com/langgenius/dify/pull/39386

> chore: bump pyasn1 from 0.6.3 to 0.6.4 in /dify-agent by @dependabot[bot] in https://github.com/langgenius/dify/pull/39388

> chore: bump pillow from 12.2.0 to 12.3.0 in /dify-agent by @dependabot[bot] in https://github.com/langgenius/dify/pull/39328

> chore(agent): update && simplify readme by @wylswz in https://github.com/langgenius/dify/pull/39584

> chore: bump pypdf from 6.10.2 to 6.14.2 in /dify-agent by @dependabot[bot] in https://github.com/langgenius/dify/pull/39502

> feat: add amptitude to new agent by @iamjoel in https://github.com/langgenius/dify/pull/39608

> feat: add bearer auth to agent backend by @wylswz in https://github.com/langgenius/dify/pull/39622

> refactor: make agent composer save and publish state consistent by @iamjoel in https://github.com/langgenius/dify/pull/39637

> chore(deps): bump golang.org/x/net from 0.53.0 to 0.55.0 in /dify-agent-runtime by @dependabot[bot] in https://github.com/langgenius/dify/pull/39025

> chore: bump pymdown-extensions from 10.21.2 to 11.0 in /dify-agent by @dependabot[bot] in https://github.com/langgenius/dify/pull/39618

Source: https://github.com/langgenius/dify/releases/tag/1.16.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-07-28-11-safety-and-privacy-changes-in-1-16-1|11 Safety and Privacy changes in 1.16.1]] · Safety and Privacy
- [[Changes/Dify/2026-07-28-6-model-support-changes-in-1-16-1|6 Model Support changes in 1.16.1]] · Model Support
- [[Changes/Dify/2026-07-28-refactor-agents-simplify-repository-context-by-lyzno1-in-https-github-com-langge|refactor(agents): simplify repository context]] · Context Window
- [[Changes/Dify/2026-07-28-3-files-and-data-changes-in-1-16-1|3 Files and Data changes in 1.16.1]] · Files and Data
- [[Changes/Dify/2026-07-28-3-collaboration-changes-in-1-16-1|3 Collaboration changes in 1.16.1]] · Collaboration
- [[Changes/Dify/2026-07-28-2-accessibility-and-localization-changes-in-1-16-1|2 Accessibility and Localization changes in 1.16.1]] · Accessibility and Localization
- [[Changes/Dify/2026-07-28-10-interface-experience-changes-in-1-16-1|10 Interface Experience changes in 1.16.1]] · Interface Experience
- [[Changes/Dify/2026-07-28-4-developer-workflow-changes-in-1-16-1|4 Developer Workflow changes in 1.16.1]] · Developer Workflow
- [[Changes/Dify/2026-07-28-lightweight-recent-apps-endpoint-new-get-console-api-apps-recent-endpoint-reduce|Lightweight recent apps endpoint]] · Reliability and Performance
- [[Changes/Dify/2026-07-28-feat-web-locate-workflow-nodes-by-node-id-in-the-workflow-editor-by-ruanimal-in|feat(web): locate workflow nodes by node_id in the workflow editor]] · Editor Experience
- [[Changes/Dify/2026-07-28-6-account-and-access-changes-in-1-16-1|6 Account and Access changes in 1.16.1]] · Account and Access
- [[Changes/Dify/2026-07-28-test-use-sqlite-sessions-in-core-memory-by-asukaminato0721-in-https-github-com-l|test: use SQLite sessions in core memory]] · Memory and Personalization
- [[Changes/Dify/2026-07-28-you-can-now-click-a-node-id-in-workflow-run-logs-or-error-messages-to-locate-and|Click a node_id in workflow run logs or error messages to locate and highlight…]] · Files and Data
- [[Changes/Dify/2026-07-28-10-apps-and-integrations-changes-in-1-16-1|10 Apps and Integrations changes in 1.16.1]] · Apps and Integrations
- [[Changes/Dify/2026-07-28-returned-400-instead-of-500-when-file-field-is-missing-from-audio-to-text-endpoi|Returned 400 instead of 500 when file field is missing from audio-to-text…]] · Voice and Audio
- [[Changes/Dify/2026-07-28-2-pricing-model-changes-in-1-16-1|2 Pricing Model changes in 1.16.1]] · Pricing Model
- [[Changes/Dify/2026-07-28-2-enterprise-and-administration-changes-in-1-16-1|2 Enterprise and Administration changes in 1.16.1]] · Enterprise and Administration
- [[Changes/Dify/2026-07-28-167-other-changes-in-1-16-1|167 other changes in 1.16.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-07-28 · Cursor · [[Changes/Cursor/2026-07-28-always-on-cloud-agents-that-build-test-and-ship-code-while-you-keep-working-725c7c|Always-on cloud agents that build, test, and ship code while you keep working]]
- Later: 2026-07-28 · Google Antigravity · [[Changes/Google Antigravity/2026-07-28-2-agent-mode-changes-in-hub-v2-4-3-preview-tabs-mcp|2 Agent Mode changes in HUB v2.4.3 — Preview tabs, MCP…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-07-28-e88674&body=Card%3A%20Changes%2FDify%2F2026-07-28-24-agent-mode-changes-in-1-16-1.md%0ACard%20ID%3A%20dify-2026-07-28-e88674%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.16.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->