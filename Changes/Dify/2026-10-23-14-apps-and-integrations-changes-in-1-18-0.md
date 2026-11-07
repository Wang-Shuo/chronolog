---
card_id: dify-2026-10-23-d53418
date: '2026-10-23'
description: 'Dify · 2026-10-23 · Apps and Integrations: 14 changes in v1.18.0 — Smarter
  Agent Routing, Portable Apps, Deeper Workflow Visibility — Create a knowledge space…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2870
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 6f3de554fd36be8c785d41785a20349876c69881f64f5b8d40a3d4c3c54d0ce2
product: dify
product_name: Dify
record:
  card_id: dify-2026-10-23-d53418
  comparison: ''
  date: '2026-10-23'
  description: 'Dify — v1.18.0 — Smarter Agent Routing, Portable Apps, Deeper Workflow
    Visibility: 14 Apps and Integrations changes'
  evidence:
  - quote: Create a knowledge space for your agents, add files or connect sources,
      and inspect document processing, metadata, retrieval traces, and quality evaluations
      in one place. The new Knowledge Retrieval node and Agent integrations share
      access-controlled KnowledgeFS spaces. Classic Knowledge remains available. This
      is an opt-in integration with a separate service and database; see the deployment
      requirements below. (#44165)
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: '**Build and manage apps with OpenAPI and difyctl.** The CLI discovers
      commands from the server''s operation catalog, with searchable help and support
      for Workflow and Chatflow creation, DSL import/export, settings, environment
      variables, publishing, and version restoration. Draft hashes protect concurrent
      edits. (#42487, #42608, #43067)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: '**Enable KnowledgeFS deliberately.** Default Compose installations keep
      it off; local Community Edition development requires the explicit Community
      development opt-in. Configure its separate database and migrations, Capability
      v2 public verifier, Dify signing keys, model profile (embedding, reasoning,
      and rerank), and Workspace cutover gates before enabling traffic. The optional
      service must pass `/ready`, not only `/health`. Standard Dify API images do
      not contain the separate KnowledgeFS engine used by the optional engine-worker
      profile; the published default KnowledgeFS API image is currently amd64 only.
      Follow the [KnowledgeFS deployment and recovery guide](https://github.com/langgenius/dify/blob/laipz8200/release-1.18.0/docker/README.md#knowledgefs-integration-service).'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: 'Workflow and Chatflow packages include inline Agents, their Skills, and
      files from each node’s bound configuration snapshot. Imports recreate those
      Agents in the destination workspace and remap their resources. App icons, Site
      settings, and node plugin dependencies are included in the export flow. Missing
      resources are reported during import. (#42579, #42626, #42816, #42863, #42913)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: '**Build and Manage Apps with OpenAPI and difyctl**'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: '**Password hashing and plugin permissions:** optional `PASSWORD_PEPPER`
      adds a server-side secret to account password hashes. Plugin installation defaults
      to workspace owners and administrators when no explicit policy is stored; existing
      saved policies remain in effect. **Setting, changing, or removing the pepper
      invalidates existing password hashes.** See the upgrade guidance. ([ed772cfcf7](https://github.com/langgenius/dify/commit/ed772cfcf7))'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: '**Error and plugin handling:** API and webhook failures return fixed public
      messages instead of internal exception text, and plugin daemon requests use
      pinned package identifiers. (#43049, #44395, #44396)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: '**APIs, MCP, and SDKs**'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: 'MCP discovery follows all tool pages with bounded requests, mixed-type
      parameters preserve list values, failed SSE connections close before HTTP fallback,
      and unsupported methods return protocol errors. MCP protocol support includes
      `2025-11-25`. (#43842, #44182, #42761, #44197, #44066)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: 'The Node.js SDK handles workflow text chunks and message replacement,
      propagates streamed API errors, preserves SSE whitespace, and replaces headers
      case-insensitively. Write requests avoid automatic replay, and reused upload
      forms retain the explicitly supplied user. (#44177, #44199, #44083, #44090,
      #43079, #44120)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: '| Cloud network policies | `NETWORK_ACCESS_API_URL`, `NETWORK_ACCESS_TRUSTED_PROXY_CIDRS`,
      `WEBAPP_ACCESS_PREFLIGHT_URL`, and `WEBAPP_ACCESS_PREFLIGHT_PROXY_SECRET`; require
      the corresponding trusted ingress and Cloud Gateway integration. The preflight
      secret is server-only. |'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: 'The older KnowledgeFS implementation removed in #44163 is superseded by
      #44165. Do not reuse its `KNOWLEDGE_FS_JWT_SECRET` or SSE timeout configuration;
      the new integration uses Capability v2 signing and public verification material.
      `KNOWLEDGE_FS_ENABLED`, `KNOWLEDGE_FS_BASE_URL`, and `KNOWLEDGE_FS_TIMEOUT_SECONDS`
      remain supported by the new configuration.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: The Console feedback export endpoint, `GET /console/api/apps/{app_id}/feedbacks/export`,
      is removed. Update integrations that called it directly. (#43751)
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: '`UV_CACHE_DIR` no longer has a baked-in shared default. Keep any deliberate
      plugin-daemon cache override explicit. (#42481)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 14-apps-and-integrations-changes-in-1-18-0
  source_release: dify-2026-10-23-1-18-0-github-421489030-879b0613
  source_type: github_releases
  theme: apps-integrations
  title: 14 Apps and Integrations changes in 1.18.0
  type: change
related_changes:
- '[[Changes/Devin/2026-10-23-sensitivity-label-policy-unlabeled-files-and-files-mcp|Sensitivity-label
  Policy: Unlabeled Files and Files MCP]]'
- '[[Changes/Devin/2026-10-23-sharepoint-support-in-the-microsoft-365-files-mcp|SharePoint
  Support in the Microsoft 365 Files MCP]]'
- '[[Changes/Devin/2026-10-23-scan-complete-summaries-by-slack-dm-or-email|Scan-complete
  Summaries by Slack DM or Email]]'
source_release: '[[Releases/Dify/dify-2026-10-23-1-18-0-github-421489030-879b0613|dify-2026-10-23-1-18-0-github-421489030-879b0613]]'
source_type: github_releases
theme: apps-integrations
title: 14 Apps and Integrations changes in 1.18.0
type: change
---

<!-- chronolog:begin region="header" -->
# 14 Apps and Integrations changes in 1.18.0

**Dify** · 2026-10-23 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.18.0) · from [[Releases/Dify/dify-2026-10-23-1-18-0-github-421489030-879b0613|v1.18.0 — Smarter Agent Routing, Portable Apps, Deeper Workflow Visibility]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Create a knowledge space for your agents, add files or connect sources, and inspect document processing, metadata, retrieval traces, and quality evaluations in one place. The new Knowledge Retrieval node and Agent integrations share access-controlled KnowledgeFS spaces. Classic Knowledge remains available. This is an opt-in integration with a separate service and database; see the deployment requirements below. (#44165)

> **Build and manage apps with OpenAPI and difyctl.** The CLI discovers commands from the server's operation catalog, with searchable help and support for Workflow and Chatflow creation, DSL import/export, settings, environment variables, publishing, and version restoration. Draft hashes protect concurrent edits. (#42487, #42608, #43067)

> **Enable KnowledgeFS deliberately.** Default Compose installations keep it off; local Community Edition development requires the explicit Community development opt-in. Configure its separate database and migrations, Capability v2 public verifier, Dify signing keys, model profile (embedding, reasoning, and rerank), and Workspace cutover gates before enabling traffic. The optional service must pass `/ready`, not only `/health`. Standard Dify API images do not contain the separate KnowledgeFS engine used by the optional engine-worker profile; the published default KnowledgeFS API image is currently amd64 only. Follow the [KnowledgeFS deployment and recovery guide](https://github.com/langgenius/dify/blob/laipz8200/release-1.18.0/docker/README.md#knowledgefs-integration-service).

> Workflow and Chatflow packages include inline Agents, their Skills, and files from each node’s bound configuration snapshot. Imports recreate those Agents in the destination workspace and remap their resources. App icons, Site settings, and node plugin dependencies are included in the export flow. Missing resources are reported during import. (#42579, #42626, #42816, #42863, #42913)

> **Build and Manage Apps with OpenAPI and difyctl**

> **Password hashing and plugin permissions:** optional `PASSWORD_PEPPER` adds a server-side secret to account password hashes. Plugin installation defaults to workspace owners and administrators when no explicit policy is stored; existing saved policies remain in effect. **Setting, changing, or removing the pepper invalidates existing password hashes.** See the upgrade guidance. ([ed772cfcf7](https://github.com/langgenius/dify/commit/ed772cfcf7))

> **Error and plugin handling:** API and webhook failures return fixed public messages instead of internal exception text, and plugin daemon requests use pinned package identifiers. (#43049, #44395, #44396)

> **APIs, MCP, and SDKs**

> MCP discovery follows all tool pages with bounded requests, mixed-type parameters preserve list values, failed SSE connections close before HTTP fallback, and unsupported methods return protocol errors. MCP protocol support includes `2025-11-25`. (#43842, #44182, #42761, #44197, #44066)

> The Node.js SDK handles workflow text chunks and message replacement, propagates streamed API errors, preserves SSE whitespace, and replaces headers case-insensitively. Write requests avoid automatic replay, and reused upload forms retain the explicitly supplied user. (#44177, #44199, #44083, #44090, #43079, #44120)

> | Cloud network policies | `NETWORK_ACCESS_API_URL`, `NETWORK_ACCESS_TRUSTED_PROXY_CIDRS`, `WEBAPP_ACCESS_PREFLIGHT_URL`, and `WEBAPP_ACCESS_PREFLIGHT_PROXY_SECRET`; require the corresponding trusted ingress and Cloud Gateway integration. The preflight secret is server-only. |

> The older KnowledgeFS implementation removed in #44163 is superseded by #44165. Do not reuse its `KNOWLEDGE_FS_JWT_SECRET` or SSE timeout configuration; the new integration uses Capability v2 signing and public verification material. `KNOWLEDGE_FS_ENABLED`, `KNOWLEDGE_FS_BASE_URL`, and `KNOWLEDGE_FS_TIMEOUT_SECONDS` remain supported by the new configuration.

> The Console feedback export endpoint, `GET /console/api/apps/{app_id}/feedbacks/export`, is removed. Update integrations that called it directly. (#43751)

> `UV_CACHE_DIR` no longer has a baked-in shared default. Keep any deliberate plugin-daemon cache override explicit. (#42481)

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
- [[Changes/Dify/2026-10-23-32-agent-mode-changes-in-1-18-0|32 Agent Mode changes in 1.18.0]] · Agent Mode
- [[Changes/Dify/2026-10-23-11-safety-and-privacy-changes-in-1-18-0|11 Safety and Privacy changes in 1.18.0]] · Safety and Privacy
- [[Changes/Dify/2026-10-23-6-account-and-access-changes-in-1-18-0|6 Account and Access changes in 1.18.0]] · Account and Access
- [[Changes/Dify/2026-10-23-2-reliability-and-performance-changes-in-1-18-0|2 Reliability and Performance changes in 1.18.0]] · Reliability and Performance
- [[Changes/Dify/2026-10-23-5-collaboration-changes-in-1-18-0|5 Collaboration changes in 1.18.0]] · Collaboration
- [[Changes/Dify/2026-10-23-8-files-and-data-changes-in-1-18-0|8 Files and Data changes in 1.18.0]] · Files and Data
- [[Changes/Dify/2026-10-23-2-automation-and-scheduling-changes-in-1-18-0|2 Automation and Scheduling changes in 1.18.0]] · Automation and Scheduling
- [[Changes/Dify/2026-10-23-81-other-changes-in-1-18-0|81 other changes in 1.18.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-10-23 · Devin · [[Changes/Devin/2026-10-23-scan-complete-summaries-by-slack-dm-or-email|Scan-complete Summaries by Slack DM or Email]]
- Later: 2026-10-23 · OpenHands · [[Changes/OpenHands/2026-10-23-2-apps-and-integrations-changes-in-v1-32-0|2 Apps and Integrations changes in v1.32.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-10-23-d53418&body=Card%3A%20Changes%2FDify%2F2026-10-23-14-apps-and-integrations-changes-in-1-18-0.md%0ACard%20ID%3A%20dify-2026-10-23-d53418%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.18.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->