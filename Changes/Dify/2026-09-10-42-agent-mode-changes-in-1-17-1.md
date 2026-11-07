---
card_id: dify-2026-09-10-46f802
date: '2026-09-10'
description: 'Dify · 2026-09-10 · Agent Mode: 42 changes in v1.17.1 - Bug Fixes and
  Improvements — **Agent & Chat**'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1162
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2b67fe0d5b34adfcd15d906bf57ed7419c4b15a462701128b9b1647fad9a6432
product: dify
product_name: Dify
record:
  card_id: dify-2026-09-10-46f802
  comparison: ''
  date: '2026-09-10'
  description: 'Dify — v1.17.1 - Bug Fixes and Improvements: 42 Agent Mode changes'
  evidence:
  - quote: '**Agent & Chat**'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: '**E2B-backed agent runs failed with `502 binding_create_failed`.** A stale
      HTTP/2 connection in the pinned E2B SDK surfaced as an inline chat failure.
      The SDK is upgraded past the affected transport path, connect/pause/kill/delete-snapshot
      are retried once on bounded transport failures, and provider capacity exhaustion
      now returns a `429` instead of being reported as a create failure. Binding and
      snapshot creation stay one-shot, so ambiguous results are never silently adopted.
      (#41623)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: '**Agent Preview reused a session that no longer matched the configuration.**
      Because Preview edits the draft in place, a conversation could keep a session
      snapshot whose composition layers had since been added, removed, or reordered,
      and the agent backend rejected it with an internal mismatch error. This now
      returns `409 agent_session_configuration_changed` with an instruction to start
      a new conversation; changing configuration *values* without changing the layer
      topology still reuses the session. (#41447)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: '**Agent skills bypassed the SSRF private-network policy.** Agent traffic
      goes through a separate proxy that ignored `SSRF_PROXY_ALLOW_PRIVATE_IPS` and
      `SSRF_PROXY_ALLOW_PRIVATE_DOMAINS`, so the allowlist you configured for workflows
      did not constrain the agent runtime. Both proxies now honor the same allowlist.
      (#41870)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: '`h2` bumped from `4.3.0` to `4.4.1` in both `api` and `dify-agent` (#40120,
      #40119)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: '**Agent runs no longer fill up Redis.** Per-run event streams were appended
      without any cap: production held 3.89 GB across 3,457 streams — 81% of the affected
      Redis node — with individual streams reaching 30 MB and 78,000 entries, because
      every stream event including token-scale text deltas was written unbounded and
      every write refreshed a three-day TTL. Streams are now capped, consecutive text
      deltas from the same part are coalesced within a 100 ms / 4,096-character window,
      the cancellation-intent stream holds one entry, and default retention drops
      from 3 days to 2 hours. The public Agent event schema and SSE cursor contract
      are unchanged. (#41566)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: '**Agent build-draft checks waited on an unrelated request.** Two surfaces
      returned their loading UI before the component owning the build-draft query
      mounted, so the browser could not start that request — which needs only the
      agent ID — until the composer request had finished. Both waterfalls are flattened.
      (#41816)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: A compact command map makes agents discoverable from Go to Anything (#41226),
      and app and agent card interactions were reworked (#41449)
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: '| `NEXT_PUBLIC_ENABLE_AGENT_V2_IN_CHATFLOW` | `false` | Feature gate for
      the Agent V2 node in Chatflow apps. Off by default. |'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: '| `DIFY_AGENT_RUN_EVENT_STREAM_MAX_LENGTH` | `5000` | Maximum entries
      retained per Agent run event stream. |'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: '| `DIFY_AGENT_STREAM_TEXT_DELTA_COALESCING_ENABLED` | `true` | Merge consecutive
      Agent text deltas before writing them to Redis. |'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: '| `DIFY_AGENT_STREAM_TEXT_DELTA_FLUSH_INTERVAL_MS` | `100` | Coalescing
      flush window. |'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: '| `DIFY_AGENT_STREAM_TEXT_DELTA_MAX_CHARS` | `4096` | Coalescing size
      cap. |'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: '`DIFY_AGENT_RUN_RETENTION_SECONDS`: `259200` (3 days) → `7200` (2 hours)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: '> Agent run records and event streams now expire after **2 hours** instead
      of 3 days. This is part of the fix for unbounded Redis growth (#41566). If you
      rely on inspecting Agent run events for longer than that, set `DIFY_AGENT_RUN_RETENTION_SECONDS`
      explicitly in your env file before upgrading.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: '**`docker-compose.middleware.yaml`**: adds the `local_sandbox` service
      (present in the main Compose file since 1.16.1) with the `dify_agent_local_sandbox_home`
      and `dify_agent_local_sandbox_workspace` volumes, and publishes Weaviate''s
      gRPC port `50051`.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: '> Review the env changes above and re-apply your local customizations
      before bringing the stack up — in particular the reduced `DIFY_AGENT_RUN_RETENTION_SECONDS`
      default (3 days → 2 hours).'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'feat(cli): add a compact command map for agent discovery by @samzong in
      https://github.com/langgenius/dify/pull/41226'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'test(e2e): stabilize Agent access toggles by @lyzno1 in https://github.com/langgenius/dify/pull/41282'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'test: migrate agent observability sessions and ORM models to SQLite by
      @asukaminato0721 in https://github.com/langgenius/dify/pull/40588'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'feat: track inline agent and preview mode events by @iamjoel in https://github.com/langgenius/dify/pull/41373'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'test: migrate agent service sessions and ORM models to SQLite by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40598'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'ci: run the dify-agent test suite by @alanhuangyoo in https://github.com/langgenius/dify/pull/41327'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'feat(web): enhance app and agent card interactions by @lyzno1 in https://github.com/langgenius/dify/pull/41449'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'test: migrate model and agent sessions to SQLite by @asukaminato0721 in
      https://github.com/langgenius/dify/pull/40087'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'chore(dify-agent): make local dev work with defaults out of the box by
      @wylswz in https://github.com/langgenius/dify/pull/41533'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'test: migrate agent-v2 workflow sessions and ORM models to SQLite by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40514'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'chore(deps): bump pypdf from 6.14.2 to 6.16.1 in /dify-agent by @dependabot[bot]
      in https://github.com/langgenius/dify/pull/41604'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'chore(deps): bump transformers from 5.6.2 to 5.10.1 in /dify-agent by
      @dependabot[bot] in https://github.com/langgenius/dify/pull/41608'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'chore: run dify-agent typecheck in python-style by @wylswz in https://github.com/langgenius/dify/pull/41701'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'chore(deps-dev): bump mkdocs-material from 9.7.6 to 9.7.7 in /dify-agent
      by @dependabot[bot] in https://github.com/langgenius/dify/pull/41767'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'perf(agent-v2): flatten build draft request waterfalls by @lyzno1 in https://github.com/langgenius/dify/pull/41816'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'test: migrate core agent runner sessions and ORM models to SQLite by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40508'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'feat(rbac): agent RBAC/ACL scenes and resource-locator check bundles by
      @GareArc in https://github.com/langgenius/dify/pull/41768'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(models): remove the App.bound_agent_id and App.is_agent wrappers
      by @ShousenZHANG in https://github.com/langgenius/dify/pull/41998'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'chore(deps): bump transformers from 5.6.2 to 5.16.1 in /dify-agent by
      @wylswz in https://github.com/langgenius/dify/pull/42054'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'feat: add agent resource permissions by @WTW0313 in https://github.com/langgenius/dify/pull/41940'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'chore(deps): bump h2 from 4.3.0 to 4.4.1 in /dify-agent by @dependabot[bot]
      in https://github.com/langgenius/dify/pull/40119'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'chore(deps): bump httpx2 from 2.5.0 to 2.12.0 in /dify-agent by @dependabot[bot]
      in https://github.com/langgenius/dify/pull/42011'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'chore(deps): bump unstructured from 0.21.5 to 0.24.0 in /dify-agent by
      @dependabot[bot] in https://github.com/langgenius/dify/pull/41765'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'chore(codeowners): assign dify-agent to Yanli by @laipz8200 in https://github.com/langgenius/dify/pull/42091'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'test: migrate agent workspace and publishing sessions and ORM models to
      SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40506'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 42-agent-mode-changes-in-1-17-1
  source_release: dify-2026-09-10-1-17-1-github-386157159-e472b6fe
  source_type: github_releases
  theme: agent-mode
  title: 42 Agent Mode changes in 1.17.1
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-10-improved-auto-mode-denials-the-message-claude-receives-now-names-the-rule-that-b|Improved
  auto mode denials]]'
- '[[Changes/Cursor/2026-09-10-a-project-runs-on-its-own-computer-in-the-cloud-so-closing-your-laptop-doesn-t-s|Powered
  by Cloud Agents]]'
- '[[Changes/Cursor/2026-09-10-subscriptions|Subscriptions]]'
source_release: '[[Releases/Dify/dify-2026-09-10-1-17-1-github-386157159-e472b6fe|dify-2026-09-10-1-17-1-github-386157159-e472b6fe]]'
source_type: github_releases
theme: agent-mode
title: 42 Agent Mode changes in 1.17.1
type: change
---

<!-- chronolog:begin region="header" -->
# 42 Agent Mode changes in 1.17.1

**Dify** · 2026-09-10 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.17.1) · from [[Releases/Dify/dify-2026-09-10-1-17-1-github-386157159-e472b6fe|v1.17.1 - Bug Fixes and Improvements]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **Agent & Chat**

> **E2B-backed agent runs failed with `502 binding_create_failed`.** A stale HTTP/2 connection in the pinned E2B SDK surfaced as an inline chat failure. The SDK is upgraded past the affected transport path, connect/pause/kill/delete-snapshot are retried once on bounded transport failures, and provider capacity exhaustion now returns a `429` instead of being reported as a create failure. Binding and snapshot creation stay one-shot, so ambiguous results are never silently adopted. (#41623)

> **Agent Preview reused a session that no longer matched the configuration.** Because Preview edits the draft in place, a conversation could keep a session snapshot whose composition layers had since been added, removed, or reordered, and the agent backend rejected it with an internal mismatch error. This now returns `409 agent_session_configuration_changed` with an instruction to start a new conversation; changing configuration *values* without changing the layer topology still reuses the session. (#41447)

> **Agent skills bypassed the SSRF private-network policy.** Agent traffic goes through a separate proxy that ignored `SSRF_PROXY_ALLOW_PRIVATE_IPS` and `SSRF_PROXY_ALLOW_PRIVATE_DOMAINS`, so the allowlist you configured for workflows did not constrain the agent runtime. Both proxies now honor the same allowlist. (#41870)

> `h2` bumped from `4.3.0` to `4.4.1` in both `api` and `dify-agent` (#40120, #40119)

> **Agent runs no longer fill up Redis.** Per-run event streams were appended without any cap: production held 3.89 GB across 3,457 streams — 81% of the affected Redis node — with individual streams reaching 30 MB and 78,000 entries, because every stream event including token-scale text deltas was written unbounded and every write refreshed a three-day TTL. Streams are now capped, consecutive text deltas from the same part are coalesced within a 100 ms / 4,096-character window, the cancellation-intent stream holds one entry, and default retention drops from 3 days to 2 hours. The public Agent event schema and SSE cursor contract are unchanged. (#41566)

> **Agent build-draft checks waited on an unrelated request.** Two surfaces returned their loading UI before the component owning the build-draft query mounted, so the browser could not start that request — which needs only the agent ID — until the composer request had finished. Both waterfalls are flattened. (#41816)

> A compact command map makes agents discoverable from Go to Anything (#41226), and app and agent card interactions were reworked (#41449)

> | `NEXT_PUBLIC_ENABLE_AGENT_V2_IN_CHATFLOW` | `false` | Feature gate for the Agent V2 node in Chatflow apps. Off by default. |

> | `DIFY_AGENT_RUN_EVENT_STREAM_MAX_LENGTH` | `5000` | Maximum entries retained per Agent run event stream. |

> | `DIFY_AGENT_STREAM_TEXT_DELTA_COALESCING_ENABLED` | `true` | Merge consecutive Agent text deltas before writing them to Redis. |

> | `DIFY_AGENT_STREAM_TEXT_DELTA_FLUSH_INTERVAL_MS` | `100` | Coalescing flush window. |

> | `DIFY_AGENT_STREAM_TEXT_DELTA_MAX_CHARS` | `4096` | Coalescing size cap. |

> `DIFY_AGENT_RUN_RETENTION_SECONDS`: `259200` (3 days) → `7200` (2 hours)

> > Agent run records and event streams now expire after **2 hours** instead of 3 days. This is part of the fix for unbounded Redis growth (#41566). If you rely on inspecting Agent run events for longer than that, set `DIFY_AGENT_RUN_RETENTION_SECONDS` explicitly in your env file before upgrading.

> **`docker-compose.middleware.yaml`**: adds the `local_sandbox` service (present in the main Compose file since 1.16.1) with the `dify_agent_local_sandbox_home` and `dify_agent_local_sandbox_workspace` volumes, and publishes Weaviate's gRPC port `50051`.

> > Review the env changes above and re-apply your local customizations before bringing the stack up — in particular the reduced `DIFY_AGENT_RUN_RETENTION_SECONDS` default (3 days → 2 hours).

> feat(cli): add a compact command map for agent discovery by @samzong in https://github.com/langgenius/dify/pull/41226

> test(e2e): stabilize Agent access toggles by @lyzno1 in https://github.com/langgenius/dify/pull/41282

> test: migrate agent observability sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40588

> feat: track inline agent and preview mode events by @iamjoel in https://github.com/langgenius/dify/pull/41373

> test: migrate agent service sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40598

> ci: run the dify-agent test suite by @alanhuangyoo in https://github.com/langgenius/dify/pull/41327

> feat(web): enhance app and agent card interactions by @lyzno1 in https://github.com/langgenius/dify/pull/41449

> test: migrate model and agent sessions to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40087

> chore(dify-agent): make local dev work with defaults out of the box by @wylswz in https://github.com/langgenius/dify/pull/41533

> test: migrate agent-v2 workflow sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40514

> chore(deps): bump pypdf from 6.14.2 to 6.16.1 in /dify-agent by @dependabot[bot] in https://github.com/langgenius/dify/pull/41604

> chore(deps): bump transformers from 5.6.2 to 5.10.1 in /dify-agent by @dependabot[bot] in https://github.com/langgenius/dify/pull/41608

> chore: run dify-agent typecheck in python-style by @wylswz in https://github.com/langgenius/dify/pull/41701

> chore(deps-dev): bump mkdocs-material from 9.7.6 to 9.7.7 in /dify-agent by @dependabot[bot] in https://github.com/langgenius/dify/pull/41767

> perf(agent-v2): flatten build draft request waterfalls by @lyzno1 in https://github.com/langgenius/dify/pull/41816

> test: migrate core agent runner sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40508

> feat(rbac): agent RBAC/ACL scenes and resource-locator check bundles by @GareArc in https://github.com/langgenius/dify/pull/41768

> refactor(models): remove the App.bound_agent_id and App.is_agent wrappers by @ShousenZHANG in https://github.com/langgenius/dify/pull/41998

> chore(deps): bump transformers from 5.6.2 to 5.16.1 in /dify-agent by @wylswz in https://github.com/langgenius/dify/pull/42054

> feat: add agent resource permissions by @WTW0313 in https://github.com/langgenius/dify/pull/41940

> chore(deps): bump h2 from 4.3.0 to 4.4.1 in /dify-agent by @dependabot[bot] in https://github.com/langgenius/dify/pull/40119

> chore(deps): bump httpx2 from 2.5.0 to 2.12.0 in /dify-agent by @dependabot[bot] in https://github.com/langgenius/dify/pull/42011

> chore(deps): bump unstructured from 0.21.5 to 0.24.0 in /dify-agent by @dependabot[bot] in https://github.com/langgenius/dify/pull/41765

> chore(codeowners): assign dify-agent to Yanli by @laipz8200 in https://github.com/langgenius/dify/pull/42091

> test: migrate agent workspace and publishing sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40506

Source: https://github.com/langgenius/dify/releases/tag/1.17.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-09-10-4-pricing-model-changes-in-1-17-1|4 Pricing Model changes in 1.17.1]] · Pricing Model
- [[Changes/Dify/2026-09-10-3-automation-and-scheduling-changes-in-1-17-1|3 Automation and Scheduling changes in 1.17.1]] · Automation and Scheduling
- [[Changes/Dify/2026-09-10-8-interface-experience-changes-in-1-17-1|8 Interface Experience changes in 1.17.1]] · Interface Experience
- [[Changes/Dify/2026-09-10-76-model-support-changes-in-1-17-1|76 Model Support changes in 1.17.1]] · Model Support
- [[Changes/Dify/2026-09-10-4-developer-workflow-changes-in-1-17-1|4 Developer Workflow changes in 1.17.1]] · Developer Workflow
- [[Changes/Dify/2026-09-10-3-collaboration-changes-in-1-17-1|3 Collaboration changes in 1.17.1]] · Collaboration
- [[Changes/Dify/2026-09-10-2-memory-and-personalization-changes-in-1-17-1|2 Memory and Personalization changes in 1.17.1]] · Memory and Personalization
- [[Changes/Dify/2026-09-10-16-safety-and-privacy-changes-in-1-17-1|16 Safety and Privacy changes in 1.17.1]] · Safety and Privacy
- [[Changes/Dify/2026-09-10-13-files-and-data-changes-in-1-17-1|13 Files and Data changes in 1.17.1]] · Files and Data
- [[Changes/Dify/2026-09-10-skill-packages-built-on-windows-failed-with-a-misleading-error-a-skill-md-using|Skill packages built on Windows failed with a misleading error. A SKILL.md…]] · Mobile and Desktop
- [[Changes/Dify/2026-09-10-12-apps-and-integrations-changes-in-1-17-1|12 Apps and Integrations changes in 1.17.1]] · Apps and Integrations
- [[Changes/Dify/2026-09-10-6-account-and-access-changes-in-1-17-1|6 Account and Access changes in 1.17.1]] · Account and Access
- [[Changes/Dify/2026-09-10-3-multimodal-input-changes-in-1-17-1|3 Multimodal Input changes in 1.17.1]] · Multimodal Input
- [[Changes/Dify/2026-09-10-6-editor-experience-changes-in-1-17-1|6 Editor Experience changes in 1.17.1]] · Editor Experience
- [[Changes/Dify/2026-09-10-3-accessibility-and-localization-changes-in-1-17-1|3 Accessibility and Localization changes in 1.17.1]] · Accessibility and Localization
- [[Changes/Dify/2026-09-10-a-plugin-could-exhaust-worker-memory-with-one-declared-number-the-blob-chunk-mer|A plugin could exhaust worker memory with one declared number. The blob chunk…]] · Reliability and Performance
- [[Changes/Dify/2026-09-10-6-context-window-changes-in-1-17-1|6 Context Window changes in 1.17.1]] · Context Window
- [[Changes/Dify/2026-09-10-205-other-changes-in-1-17-1|205 other changes in 1.17.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-09-10 · Cursor · [[Changes/Cursor/2026-09-10-subscriptions|Subscriptions]]
- Later: 2026-09-10 · Krea · [[Changes/Krea/2026-09-10-krea-agent-is-open-on-every-plan|Krea Agent is open on every plan]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-09-10-46f802&body=Card%3A%20Changes%2FDify%2F2026-09-10-42-agent-mode-changes-in-1-17-1.md%0ACard%20ID%3A%20dify-2026-09-10-46f802%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.17.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->