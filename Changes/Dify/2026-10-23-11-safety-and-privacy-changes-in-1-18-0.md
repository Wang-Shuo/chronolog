---
card_id: dify-2026-10-23-a5a144
date: '2026-10-23'
description: 'Dify · 2026-10-23 · Safety and Privacy: 11 changes in v1.18.0 — Smarter
  Agent Routing, Portable Apps, Deeper Workflow Visibility — **Configure the Local…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2278
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ace68df5046a7c5fd758f2dd35e503f041484947c565868412ff01f692fc1134
product: dify
product_name: Dify
record:
  card_id: dify-2026-10-23-a5a144
  comparison: ''
  date: '2026-10-23'
  description: 'Dify — v1.18.0 — Smarter Agent Routing, Portable Apps, Deeper Workflow
    Visibility: 11 Safety and Privacy changes'
  evidence:
  - quote: '**Configure the Local sandbox token before restart.** Supply a high-entropy
      secret through the shared Compose interpolation source. The `1.17.1` runtime
      image does not support the new `--require-auth-token` flag; deploy the matching
      `1.18.0` Agent Backend and Local sandbox images. (#44152)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: '**Edit Agent Prompts from the Sandbox**'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: '**OpenShell Sandbox Backend and E2B Usage Collection**'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: Agent execution can use a self-hosted NVIDIA OpenShell gateway with `DIFY_AGENT_RUNTIME_BACKEND=openshell`.
      Each Binding has its own sandbox, with authenticated shell access, Home Snapshots
      on an operator-managed shared volume, and an optional egress allowlist. OpenShell
      gateway 0.0.106 or newer and a compatible runtime image are required. (#41076)
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: OpenShell lease release closes the connection but leaves the sandbox running.
      There is no automatic idle-stop or sandbox TTL; operators must manage those
      resources. Multi-tenant deployments require separate OpenShell workspaces and
      snapshot volumes per tenant. See the [OpenShell deployment guide](https://github.com/langgenius/dify/blob/laipz8200/release-1.18.0/dify-agent/docs/dify-agent/guide/openshell.md).
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: 'Reusable network access groups let supported Cloud deployments share IP
      rules across apps, with permission checks, effective-policy status, and trusted
      client-IP previews. Enforcement depends on the Cloud policy service and Gateway;
      this is not a standalone Community Edition firewall. (#41025, #44464)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: <summary><strong>Security enhancements</strong></summary>
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: '**Local sandbox authentication and isolation:** enabled Local runtimes
      reject blank authentication tokens. When path isolation is enabled, a Landlock
      setup failure aborts the job with exit code `125` before executing user code.
      (#44152)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: '**Dependency updates:** bundled Weaviate moves from `1.39.2` to `1.39.13`,
      alongside Next.js and other dependency security updates. The Weaviate change
      stays within the 1.39 series; the staged minor-version migration described for
      1.17.1 still matters when upgrading from older installations. (#44508, #44127,
      #44148, #44524)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: 'E2B sandbox acquisition checks that Home and Workspace resources exist,
      and confirmed-missing Enterprise Home Snapshots count as successful deletion.
      (#44014, #44085)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: '| `e7b2a9c4d601` | Add Agent sandbox usage events and execution accounting.
      |'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 11-safety-and-privacy-changes-in-1-18-0
  source_release: dify-2026-10-23-1-18-0-github-421489030-879b0613
  source_type: github_releases
  theme: safety-privacy
  title: 11 Safety and Privacy changes in 1.18.0
  type: change
related_changes:
- '[[Changes/Qoder/2026-10-22-dynamic-island-macos-view-task-progress-answer-questions-and-handle-permission-r|Dynamic
  Island (macOS)]]'
- '[[Changes/Claude Code/2026-10-23-4-safety-and-privacy-changes-in-v2-1-310|4 Safety
  and Privacy changes in v2.1.310]]'
- '[[Changes/Codex CLI/2026-10-23-15-safety-and-privacy-changes-in-rust-v0-164-0|15
  Safety and Privacy changes in rust-v0.164.0]]'
source_release: '[[Releases/Dify/dify-2026-10-23-1-18-0-github-421489030-879b0613|dify-2026-10-23-1-18-0-github-421489030-879b0613]]'
source_type: github_releases
theme: safety-privacy
title: 11 Safety and Privacy changes in 1.18.0
type: change
---

<!-- chronolog:begin region="header" -->
# 11 Safety and Privacy changes in 1.18.0

**Dify** · 2026-10-23 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.18.0) · from [[Releases/Dify/dify-2026-10-23-1-18-0-github-421489030-879b0613|v1.18.0 — Smarter Agent Routing, Portable Apps, Deeper Workflow Visibility]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **Configure the Local sandbox token before restart.** Supply a high-entropy secret through the shared Compose interpolation source. The `1.17.1` runtime image does not support the new `--require-auth-token` flag; deploy the matching `1.18.0` Agent Backend and Local sandbox images. (#44152)

> **Edit Agent Prompts from the Sandbox**

> **OpenShell Sandbox Backend and E2B Usage Collection**

> Agent execution can use a self-hosted NVIDIA OpenShell gateway with `DIFY_AGENT_RUNTIME_BACKEND=openshell`. Each Binding has its own sandbox, with authenticated shell access, Home Snapshots on an operator-managed shared volume, and an optional egress allowlist. OpenShell gateway 0.0.106 or newer and a compatible runtime image are required. (#41076)

> OpenShell lease release closes the connection but leaves the sandbox running. There is no automatic idle-stop or sandbox TTL; operators must manage those resources. Multi-tenant deployments require separate OpenShell workspaces and snapshot volumes per tenant. See the [OpenShell deployment guide](https://github.com/langgenius/dify/blob/laipz8200/release-1.18.0/dify-agent/docs/dify-agent/guide/openshell.md).

> Reusable network access groups let supported Cloud deployments share IP rules across apps, with permission checks, effective-policy status, and trusted client-IP previews. Enforcement depends on the Cloud policy service and Gateway; this is not a standalone Community Edition firewall. (#41025, #44464)

> \<summary>\<strong>Security enhancements\</strong>\</summary>

> **Local sandbox authentication and isolation:** enabled Local runtimes reject blank authentication tokens. When path isolation is enabled, a Landlock setup failure aborts the job with exit code `125` before executing user code. (#44152)

> **Dependency updates:** bundled Weaviate moves from `1.39.2` to `1.39.13`, alongside Next.js and other dependency security updates. The Weaviate change stays within the 1.39 series; the staged minor-version migration described for 1.17.1 still matters when upgrading from older installations. (#44508, #44127, #44148, #44524)

> E2B sandbox acquisition checks that Home and Workspace resources exist, and confirmed-missing Enterprise Home Snapshots count as successful deletion. (#44014, #44085)

> | `e7b2a9c4d601` | Add Agent sandbox usage events and execution accounting. |

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
- [[Changes/Dify/2026-10-23-14-apps-and-integrations-changes-in-1-18-0|14 Apps and Integrations changes in 1.18.0]] · Apps and Integrations
- [[Changes/Dify/2026-10-23-6-account-and-access-changes-in-1-18-0|6 Account and Access changes in 1.18.0]] · Account and Access
- [[Changes/Dify/2026-10-23-2-reliability-and-performance-changes-in-1-18-0|2 Reliability and Performance changes in 1.18.0]] · Reliability and Performance
- [[Changes/Dify/2026-10-23-5-collaboration-changes-in-1-18-0|5 Collaboration changes in 1.18.0]] · Collaboration
- [[Changes/Dify/2026-10-23-8-files-and-data-changes-in-1-18-0|8 Files and Data changes in 1.18.0]] · Files and Data
- [[Changes/Dify/2026-10-23-2-automation-and-scheduling-changes-in-1-18-0|2 Automation and Scheduling changes in 1.18.0]] · Automation and Scheduling
- [[Changes/Dify/2026-10-23-81-other-changes-in-1-18-0|81 other changes in 1.18.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-10-23 · Codex CLI · [[Changes/Codex CLI/2026-10-23-15-safety-and-privacy-changes-in-rust-v0-164-0|15 Safety and Privacy changes in rust-v0.164.0]]
- Later: 2026-10-23 · Kimi Code · [[Changes/Kimi Code/2026-10-23-fix-workspace-trust-failures-when-git-bash-is-unavailable-on-windows|Fix workspace trust failures when Git Bash is unavailable on Windows]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-10-23-a5a144&body=Card%3A%20Changes%2FDify%2F2026-10-23-11-safety-and-privacy-changes-in-1-18-0.md%0ACard%20ID%3A%20dify-2026-10-23-a5a144%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.18.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->