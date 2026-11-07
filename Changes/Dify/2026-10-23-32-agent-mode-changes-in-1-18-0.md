---
card_id: dify-2026-10-23-88b16c
date: '2026-10-23'
description: 'Dify · 2026-10-23 · Agent Mode: 32 changes in v1.18.0 — Smarter Agent
  Routing, Portable Apps, Deeper Workflow Visibility — Dify 1.18.0 brings **Agents
  that…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1205
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ad8622e98ffcb0bbe34530df38c8a95fc3b21d29009e07415e4b740adb160c6a
product: dify
product_name: Dify
record:
  card_id: dify-2026-10-23-88b16c
  comparison: ''
  date: '2026-10-23'
  description: 'Dify — v1.18.0 — Smarter Agent Routing, Portable Apps, Deeper Workflow
    Visibility: 32 Agent Mode changes'
  evidence:
  - quote: Dify 1.18.0 brings **Agents that route workflows**, **portable app packages**,
      **deeper visibility into nested workflow runs**, and the opt-in **Agent Knowledge
      Base** experience. OpenAPI and the new difyctl expand how you build and manage
      apps from the command line.
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: Let an Agent decide which workflow branch to take. Enable **Output Routes**,
      give each route a selection condition, and connect it to the next step—such
      as resolving a request directly or handing it to a specialist. The read-only
      `switch` output exposes the chosen route. (#42599)
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: '![Agent Output Routes with Resolve directly and Escalate to team branches](https://github.com/user-attachments/assets/30480ac3-d53e-4522-b1c5-95eb1d9ac9f2)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: Plain Agent v2 nodes also stream text as it is generated. Structured results,
      routed results, and nodes using default-value error handling remain buffered.
      (#43986)
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: 'Move an app with its supported resources in a single **`.ifpkg` package**.
      Workflow and Chatflow packages carry inline Agents, Skills, and their files;
      imports recreate those resources in the destination workspace and remap references.
      File and URL imports support both packages and YAML, and explicit YAML export
      remains available. (#42066, #42579, #42626, #42863)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: 'Install the bundled skill for agents building Dify apps:'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: '**Back up first.** Retain the database, vector-store data, uploaded files,
      Agent snapshot/workspace storage, and all deployment secrets and env files.
      Use a maintenance window for a single-stack upgrade.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: 'Update scripts to the current server-discovered command surface. The old
      mode-agnostic `/openapi/v1/apps/{app_id}:run` route is replaced by per-mode
      operations; use the catalog instead of hard-coded v1 routes. Refresh installed
      agent skills with `difyctl install skills <dir>`. (#42487, #42608, #43819)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: '**Agent Knowledge Base and KnowledgeFS**'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: Add the Beta knowledge-space experience with local upload preview, connected-source
      management, document availability and metadata, retrieval history/research,
      and quality evaluation. Settings control app, Agent, and Service API access.
      Classic Knowledge remains supported alongside it. (#44165)
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: Knowledge Retrieval v2 and Agent knowledge bindings use scoped capabilities;
      published Explore runs reuse published bindings without requiring ordinary viewers
      to reconfigure access. (#44165)
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: 'Agent exports can target a published version. Agent version menus now
      offer Restore, and pending draft saves finish before restoration so autosave
      cannot overwrite the restored configuration. Skill duplication and export use
      the latest saved draft content. (#42485, #42567, #42424, #42502)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: 'Nested Agent logs and usage records retain their source workflow identity
      and their relationship to the outer run. **Nested usage and step totals can
      still be approximate, particularly after pauses or stops.** (#42824, #42820)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: '**Agent Output Routes and Streaming**'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: Agent v2 nodes can select a workflow branch as part of completing their
      task. Enable Output Routes, define at least two branches and their selection
      conditions, and use the read-only `switch` output to inspect the chosen route.
      With routing disabled, the normal success outlet remains available. Routed nodes
      support stopping on error or taking a failure branch; node-level default-value
      handling is unavailable with routes enabled. (#42599)
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: Plain Agent v2 nodes stream text as it is generated. Structured or routed
      results remain buffered, and nodes using default-value error handling stay buffered
      so the configured fallback can still replace a failed result. (#43986)
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: '`dify-agent config prompt pull [--to PATH]` and `push [PATH|-]` read or
      replace the raw system prompt, preserving UTF-8, whitespace, and mention markers.
      Empty text clears it. Only the current account’s writable build draft can be
      changed; later requests use the saved prompt. (#44561)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: '**Agent Execution Tracing**'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: 'Agent apps and Workflow Agent v2 nodes can export their Agent, model,
      and tool execution trees through the existing tracing providers. Monitoring
      adds shared tracing configuration, delivery status, retry controls, and links
      to the trace belonging to the selected execution. Agents referenced by a Workflow
      inherit the caller’s tracing policy. (#44144, #44186)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: 'Application tracing is opt-in on both the API and Agent Backend. A separate
      deployment-wide OTLP trajectory exporter is also available, independently of
      system tracing. (#42651, #44144)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: 'Called Workflow Tools’ internal nodes are excluded from external exports
      because those exports have no viewer identity for source-app access checks.
      Agents inside those called tools are also excluded from the new execution-tree
      export for now; authorized Console drilldown remains available. (#42823, #44144)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: Optional E2B usage collection records provider execution duration and resource
      sizes through Celery Beat and the `ops_trace` queue. Collection starts from
      a configured activation time and does not backfill earlier executions. Both
      the API and Agent Backend metering flags default to off. (#42554)
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: 'Cloud users can preview and try published Agent templates before importing
      them. Agent “Create from Template” is hidden in Community and Enterprise editions
      because its template data source is Cloud-only. (#42837, #44035)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: 'In Cloud Workflow Log Archives, workspace owners can permanently delete
      a selected month, with confirmation, progress, and retry. The action removes
      archived objects and prepared ZIP downloads; live workflow-run records are outside
      its scope. Failed deletion jobs now enter the retry policy instead of reporting
      success. (#44052, #44061, #44203)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: The standalone Agent certifi bundle is updated to `2026.10.19`; rebuild
      Agent images to consume the updated trust bundle. (#44462)
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: <summary><strong>Bug fixes · workflows, Agents, Knowledge, APIs, and the
      web app</strong></summary>
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: '**Agents and Skills**'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: '| `DIFY_AGENT_LOCAL_SANDBOX_AUTH_TOKEN` | Required and nonblank for an
      enabled Local runtime. For Compose, set it in `docker/.env`, the invoking shell,
      or `--env-file` so Agent Backend and shellctl receive the same secret. Setting
      it only in a service env file is insufficient. |'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: '| Application Agent tracing | API: `OPS_AGENT_TRACE_ENABLED=false`. Agent
      Backend: `DIFY_AGENT_APPLICATION_TRACING_ENABLED=false`. Application policy
      and provider configuration are also required. `ENABLE_APPLICATION_TRACE_RECONCILE_TASK=true`
      controls scheduled reconciliation. |'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: '| E2B usage | API: `AGENT_SANDBOX_METERING_ENABLED=false`, `AGENT_SANDBOX_METERING_PROJECT_ID`,
      `AGENT_SANDBOX_METERING_START_AT`, `AGENT_SANDBOX_METERING_INTERVAL_SECONDS=60`.
      Backend: `DIFY_AGENT_SANDBOX_METERING_ENABLED=false`, `DIFY_AGENT_E2B_PROJECT_ID`,
      plus overlap/full-scan/page limits. |'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: '| OpenShell | Select `DIFY_AGENT_RUNTIME_BACKEND=openshell`; configure
      the `DIFY_AGENT_OPENSHELL_*` gateway, credentials, image, driver/shared-volume,
      shell token, and optional egress settings in the Agent service env file. |'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: '| Package bounds | `SKILL_PACKAGE_MAX_UNCOMPRESSED_BYTES=209715200`, `SKILL_PACKAGE_MAX_ENTRIES=5000`,
      `SKILL_PACKAGE_MAX_SKILL_MD_BYTES=1048576`; `AGENT_PACKAGE_MAX_BYTES=536870912`,
      `AGENT_PACKAGE_MAX_MANIFEST_BYTES=5242880`, `AGENT_PACKAGE_MAX_ENTRIES=5000`.
      Ordinary app packages retain the 10 MiB DSL limit. |'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 32-agent-mode-changes-in-1-18-0
  source_release: dify-2026-10-23-1-18-0-github-421489030-879b0613
  source_type: github_releases
  theme: agent-mode
  title: 32 Agent Mode changes in 1.18.0
  type: change
related_changes:
- '[[Changes/OpenHands/2026-10-22-chore-bump-agent-server-to-1-57-0-by-all-hands-bot-in-https-github-com-openhands|chore:
  bump agent-server to 1.57.0]]'
- '[[Changes/Claude Code/2026-10-23-2-agent-mode-changes-in-v2-1-310|2 Agent Mode
  changes in v2.1.310]]'
- '[[Changes/Codex CLI/2026-10-23-13-agent-mode-changes-in-rust-v0-164-0|13 Agent
  Mode changes in rust-v0.164.0]]'
source_release: '[[Releases/Dify/dify-2026-10-23-1-18-0-github-421489030-879b0613|dify-2026-10-23-1-18-0-github-421489030-879b0613]]'
source_type: github_releases
theme: agent-mode
title: 32 Agent Mode changes in 1.18.0
type: change
---

<!-- chronolog:begin region="header" -->
# 32 Agent Mode changes in 1.18.0

**Dify** · 2026-10-23 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.18.0) · from [[Releases/Dify/dify-2026-10-23-1-18-0-github-421489030-879b0613|v1.18.0 — Smarter Agent Routing, Portable Apps, Deeper Workflow Visibility]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Dify 1.18.0 brings **Agents that route workflows**, **portable app packages**, **deeper visibility into nested workflow runs**, and the opt-in **Agent Knowledge Base** experience. OpenAPI and the new difyctl expand how you build and manage apps from the command line.

> Let an Agent decide which workflow branch to take. Enable **Output Routes**, give each route a selection condition, and connect it to the next step—such as resolving a request directly or handing it to a specialist. The read-only `switch` output exposes the chosen route. (#42599)

> ![Agent Output Routes with Resolve directly and Escalate to team branches](https://github.com/user-attachments/assets/30480ac3-d53e-4522-b1c5-95eb1d9ac9f2)

> Plain Agent v2 nodes also stream text as it is generated. Structured results, routed results, and nodes using default-value error handling remain buffered. (#43986)

> Move an app with its supported resources in a single **`.ifpkg` package**. Workflow and Chatflow packages carry inline Agents, Skills, and their files; imports recreate those resources in the destination workspace and remap references. File and URL imports support both packages and YAML, and explicit YAML export remains available. (#42066, #42579, #42626, #42863)

> Install the bundled skill for agents building Dify apps:

> **Back up first.** Retain the database, vector-store data, uploaded files, Agent snapshot/workspace storage, and all deployment secrets and env files. Use a maintenance window for a single-stack upgrade.

> Update scripts to the current server-discovered command surface. The old mode-agnostic `/openapi/v1/apps/{app_id}:run` route is replaced by per-mode operations; use the catalog instead of hard-coded v1 routes. Refresh installed agent skills with `difyctl install skills <dir>`. (#42487, #42608, #43819)

> **Agent Knowledge Base and KnowledgeFS**

> Add the Beta knowledge-space experience with local upload preview, connected-source management, document availability and metadata, retrieval history/research, and quality evaluation. Settings control app, Agent, and Service API access. Classic Knowledge remains supported alongside it. (#44165)

> Knowledge Retrieval v2 and Agent knowledge bindings use scoped capabilities; published Explore runs reuse published bindings without requiring ordinary viewers to reconfigure access. (#44165)

> Agent exports can target a published version. Agent version menus now offer Restore, and pending draft saves finish before restoration so autosave cannot overwrite the restored configuration. Skill duplication and export use the latest saved draft content. (#42485, #42567, #42424, #42502)

> Nested Agent logs and usage records retain their source workflow identity and their relationship to the outer run. **Nested usage and step totals can still be approximate, particularly after pauses or stops.** (#42824, #42820)

> **Agent Output Routes and Streaming**

> Agent v2 nodes can select a workflow branch as part of completing their task. Enable Output Routes, define at least two branches and their selection conditions, and use the read-only `switch` output to inspect the chosen route. With routing disabled, the normal success outlet remains available. Routed nodes support stopping on error or taking a failure branch; node-level default-value handling is unavailable with routes enabled. (#42599)

> Plain Agent v2 nodes stream text as it is generated. Structured or routed results remain buffered, and nodes using default-value error handling stay buffered so the configured fallback can still replace a failed result. (#43986)

> `dify-agent config prompt pull [--to PATH]` and `push [PATH|-]` read or replace the raw system prompt, preserving UTF-8, whitespace, and mention markers. Empty text clears it. Only the current account’s writable build draft can be changed; later requests use the saved prompt. (#44561)

> **Agent Execution Tracing**

> Agent apps and Workflow Agent v2 nodes can export their Agent, model, and tool execution trees through the existing tracing providers. Monitoring adds shared tracing configuration, delivery status, retry controls, and links to the trace belonging to the selected execution. Agents referenced by a Workflow inherit the caller’s tracing policy. (#44144, #44186)

> Application tracing is opt-in on both the API and Agent Backend. A separate deployment-wide OTLP trajectory exporter is also available, independently of system tracing. (#42651, #44144)

> Called Workflow Tools’ internal nodes are excluded from external exports because those exports have no viewer identity for source-app access checks. Agents inside those called tools are also excluded from the new execution-tree export for now; authorized Console drilldown remains available. (#42823, #44144)

> Optional E2B usage collection records provider execution duration and resource sizes through Celery Beat and the `ops_trace` queue. Collection starts from a configured activation time and does not backfill earlier executions. Both the API and Agent Backend metering flags default to off. (#42554)

> Cloud users can preview and try published Agent templates before importing them. Agent “Create from Template” is hidden in Community and Enterprise editions because its template data source is Cloud-only. (#42837, #44035)

> In Cloud Workflow Log Archives, workspace owners can permanently delete a selected month, with confirmation, progress, and retry. The action removes archived objects and prepared ZIP downloads; live workflow-run records are outside its scope. Failed deletion jobs now enter the retry policy instead of reporting success. (#44052, #44061, #44203)

> The standalone Agent certifi bundle is updated to `2026.10.19`; rebuild Agent images to consume the updated trust bundle. (#44462)

> \<summary>\<strong>Bug fixes · workflows, Agents, Knowledge, APIs, and the web app\</strong>\</summary>

> **Agents and Skills**

> | `DIFY_AGENT_LOCAL_SANDBOX_AUTH_TOKEN` | Required and nonblank for an enabled Local runtime. For Compose, set it in `docker/.env`, the invoking shell, or `--env-file` so Agent Backend and shellctl receive the same secret. Setting it only in a service env file is insufficient. |

> | Application Agent tracing | API: `OPS_AGENT_TRACE_ENABLED=false`. Agent Backend: `DIFY_AGENT_APPLICATION_TRACING_ENABLED=false`. Application policy and provider configuration are also required. `ENABLE_APPLICATION_TRACE_RECONCILE_TASK=true` controls scheduled reconciliation. |

> | E2B usage | API: `AGENT_SANDBOX_METERING_ENABLED=false`, `AGENT_SANDBOX_METERING_PROJECT_ID`, `AGENT_SANDBOX_METERING_START_AT`, `AGENT_SANDBOX_METERING_INTERVAL_SECONDS=60`. Backend: `DIFY_AGENT_SANDBOX_METERING_ENABLED=false`, `DIFY_AGENT_E2B_PROJECT_ID`, plus overlap/full-scan/page limits. |

> | OpenShell | Select `DIFY_AGENT_RUNTIME_BACKEND=openshell`; configure the `DIFY_AGENT_OPENSHELL_*` gateway, credentials, image, driver/shared-volume, shell token, and optional egress settings in the Agent service env file. |

> | Package bounds | `SKILL_PACKAGE_MAX_UNCOMPRESSED_BYTES=209715200`, `SKILL_PACKAGE_MAX_ENTRIES=5000`, `SKILL_PACKAGE_MAX_SKILL_MD_BYTES=1048576`; `AGENT_PACKAGE_MAX_BYTES=536870912`, `AGENT_PACKAGE_MAX_MANIFEST_BYTES=5242880`, `AGENT_PACKAGE_MAX_ENTRIES=5000`. Ordinary app packages retain the 10 MiB DSL limit. |

Source: https://github.com/langgenius/dify/releases/tag/1.18.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-10-23-respect-xforward-headers-enabled-standalone-api-default-remains-false-bundled-co| /  RESPECT_XFORWARD_HEADERS_ENABLED  /  Standalone API default remains false]] · Developer Workflow
- [[Changes/Dify/2026-10-23-3-memory-and-personalization-changes-in-1-18-0|3 Memory and Personalization changes in 1.18.0]] · Memory and Personalization
- [[Changes/Dify/2026-10-23-3-accessibility-and-localization-changes-in-1-18-0|3 Accessibility and Localization changes in 1.18.0]] · Accessibility and Localization
- [[Changes/Dify/2026-10-23-3-context-window-changes-in-1-18-0|3 Context Window changes in 1.18.0]] · Context Window
- [[Changes/Dify/2026-10-23-operations-archive-storage-supports-configurable-s3-addressing-style-the-api-ima|Operations: archive storage supports configurable S3 addressing style]] · Model Support
- [[Changes/Dify/2026-10-23-2-interface-experience-changes-in-1-18-0|2 Interface Experience changes in 1.18.0]] · Interface Experience
- [[Changes/Dify/2026-10-23-3-editor-experience-changes-in-1-18-0|3 Editor Experience changes in 1.18.0]] · Editor Experience
- [[Changes/Dify/2026-10-23-11-safety-and-privacy-changes-in-1-18-0|11 Safety and Privacy changes in 1.18.0]] · Safety and Privacy
- [[Changes/Dify/2026-10-23-14-apps-and-integrations-changes-in-1-18-0|14 Apps and Integrations changes in 1.18.0]] · Apps and Integrations
- [[Changes/Dify/2026-10-23-6-account-and-access-changes-in-1-18-0|6 Account and Access changes in 1.18.0]] · Account and Access
- [[Changes/Dify/2026-10-23-2-reliability-and-performance-changes-in-1-18-0|2 Reliability and Performance changes in 1.18.0]] · Reliability and Performance
- [[Changes/Dify/2026-10-23-5-collaboration-changes-in-1-18-0|5 Collaboration changes in 1.18.0]] · Collaboration
- [[Changes/Dify/2026-10-23-8-files-and-data-changes-in-1-18-0|8 Files and Data changes in 1.18.0]] · Files and Data
- [[Changes/Dify/2026-10-23-2-automation-and-scheduling-changes-in-1-18-0|2 Automation and Scheduling changes in 1.18.0]] · Automation and Scheduling
- [[Changes/Dify/2026-10-23-81-other-changes-in-1-18-0|81 other changes in 1.18.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-10-23 · Codex CLI · [[Changes/Codex CLI/2026-10-23-13-agent-mode-changes-in-rust-v0-164-0|13 Agent Mode changes in rust-v0.164.0]]
- Later: 2026-10-23 · Replit · [[Changes/Replit/2026-10-23-stripe-atlas-on-replit|Stripe Atlas on Replit]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-10-23-88b16c&body=Card%3A%20Changes%2FDify%2F2026-10-23-32-agent-mode-changes-in-1-18-0.md%0ACard%20ID%3A%20dify-2026-10-23-88b16c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.18.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->