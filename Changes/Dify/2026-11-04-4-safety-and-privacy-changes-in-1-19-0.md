---
card_id: dify-2026-11-04-c11b38
date: '2026-11-04'
description: 'Dify · 2026-11-04 · Safety and Privacy: 4 changes in v1.19.0 - Trace
  Your Workflows, Layer by Layer — **Upgrade the components together.** Use matching…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2290
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: cc7824652bf3e668fb5313cfac9b55c3ffb5c0bea7f332fb89ebaf91999d59bb
product: dify
product_name: Dify
record:
  card_id: dify-2026-11-04-c11b38
  comparison: ''
  date: '2026-11-04'
  description: 'Dify — v1.19.0 - Trace Your Workflows, Layer by Layer: 4 Safety and
    Privacy changes'
  evidence:
  - quote: '**Upgrade the components together.** Use matching `1.19.0` API, worker,
      web, Agent Backend, and Local sandbox images, with plugin daemon `0.6.14-local`.
      Keep the existing Local sandbox authentication token and any configured `PASSWORD_PEPPER`
      unchanged. If upgrading from before 1.18.0, also follow the [1.18.0 upgrade
      guide](https://github.com/langgenius/dify/releases/tag/1.18.0).'
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  - quote: Package the workflows behind called Workflow Tools, including transitive
      dependencies, with a default maximum of **20** bundled tool workflows. Missing
      destination tools are recreated and published; existing tools are reused. Creating
      missing tools requires tool-management permission and sufficient app quota.
      Packages needing DSL-version confirmation are rejected in this flow, and apps
      created before an import failure are cleaned up. (#44592)
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  - quote: <summary><strong>Security enhancements</strong></summary>
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  - quote: '| `OPS_TRACE_QUEUE` | New; defaults to `ops_trace_v2`. Shared by trace
      delivery/retries, Agent trace work, payload cleanup, and sandbox metering. API,
      workers, and Beat must agree. |'
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 4-safety-and-privacy-changes-in-1-19-0
  source_release: dify-2026-11-04-1-19-0-github-433629888-738006ec
  source_type: github_releases
  theme: safety-privacy
  title: 4 Safety and Privacy changes in 1.19.0
  type: change
related_changes:
- '[[Changes/Lovable/2026-11-03-protect-a-project-from-abandonment-cleanup|Protect
  a project from abandonment cleanup]]'
- '[[Changes/Open WebUI/2026-11-03-2-safety-and-privacy-changes-in-v0-13-0|2 Safety
  and Privacy changes in v0.13.0]]'
- '[[Changes/OpenClaw/2026-11-03-7-safety-and-privacy-changes-in-v2026-10-10|7 Safety
  and Privacy changes in v2026.10.10]]'
source_release: '[[Releases/Dify/dify-2026-11-04-1-19-0-github-433629888-738006ec|dify-2026-11-04-1-19-0-github-433629888-738006ec]]'
source_type: github_releases
theme: safety-privacy
title: 4 Safety and Privacy changes in 1.19.0
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Safety and Privacy changes in 1.19.0

**Dify** · 2026-11-04 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.19.0) · from [[Releases/Dify/dify-2026-11-04-1-19-0-github-433629888-738006ec|v1.19.0 - Trace Your Workflows, Layer by Layer]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **Upgrade the components together.** Use matching `1.19.0` API, worker, web, Agent Backend, and Local sandbox images, with plugin daemon `0.6.14-local`. Keep the existing Local sandbox authentication token and any configured `PASSWORD_PEPPER` unchanged. If upgrading from before 1.18.0, also follow the [1.18.0 upgrade guide](https://github.com/langgenius/dify/releases/tag/1.18.0).

> Package the workflows behind called Workflow Tools, including transitive dependencies, with a default maximum of **20** bundled tool workflows. Missing destination tools are recreated and published; existing tools are reused. Creating missing tools requires tool-management permission and sufficient app quota. Packages needing DSL-version confirmation are rejected in this flow, and apps created before an import failure are cleaned up. (#44592)

> \<summary>\<strong>Security enhancements\</strong>\</summary>

> | `OPS_TRACE_QUEUE` | New; defaults to `ops_trace_v2`. Shared by trace delivery/retries, Agent trace work, payload cleanup, and sandbox metering. API, workers, and Beat must agree. |

Source: https://github.com/langgenius/dify/releases/tag/1.19.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-11-04-4-model-support-changes-in-1-19-0|4 Model Support changes in 1.19.0]] · Model Support
- [[Changes/Dify/2026-11-04-stop-serializing-the-entire-prompt-history-into-every-agent-llm-gateway-response|Stop serializing the entire prompt history into every Agent LLM gateway response chunk]] · Multimodal Input
- [[Changes/Dify/2026-11-04-4-collaboration-changes-in-1-19-0|4 Collaboration changes in 1.19.0]] · Collaboration
- [[Changes/Dify/2026-11-04-15-apps-and-integrations-changes-in-1-19-0|15 Apps and Integrations changes in 1.19.0]] · Apps and Integrations
- [[Changes/Dify/2026-11-04-3-automation-and-scheduling-changes-in-1-19-0|3 Automation and Scheduling changes in 1.19.0]] · Automation and Scheduling
- [[Changes/Dify/2026-11-04-2-developer-workflow-changes-in-1-19-0|2 Developer Workflow changes in 1.19.0]] · Developer Workflow
- [[Changes/Dify/2026-11-04-6-files-and-data-changes-in-1-19-0|6 Files and Data changes in 1.19.0]] · Files and Data
- [[Changes/Dify/2026-11-04-3-pricing-model-changes-in-1-19-0|3 Pricing Model changes in 1.19.0]] · Pricing Model
- [[Changes/Dify/2026-11-04-3-editor-experience-changes-in-1-19-0|3 Editor Experience changes in 1.19.0]] · Editor Experience
- [[Changes/Dify/2026-11-04-2-voice-and-audio-changes-in-1-19-0|2 Voice and Audio changes in 1.19.0]] · Voice and Audio
- [[Changes/Dify/2026-11-04-workspace-controls-enabling-or-disabling-provider-models-requires-an-owner-or-ad|Workspace controls: enabling or disabling provider models requires an owner…]] · Enterprise and Administration
- [[Changes/Dify/2026-11-04-summary-strong-improvements-editing-accessibility-performance-and-operations-str|summarystrongImprovements · editing, accessibility, performance…]] · Accessibility and Localization
- [[Changes/Dify/2026-11-04-2-interface-experience-changes-in-1-19-0|2 Interface Experience changes in 1.19.0]] · Interface Experience
- [[Changes/Dify/2026-11-04-6-context-window-changes-in-1-19-0|6 Context Window changes in 1.19.0]] · Context Window
- [[Changes/Dify/2026-11-04-14-agent-mode-changes-in-1-19-0|14 Agent Mode changes in 1.19.0]] · Agent Mode
- [[Changes/Dify/2026-11-04-2-account-and-access-changes-in-1-19-0|2 Account and Access changes in 1.19.0]] · Account and Access
- [[Changes/Dify/2026-11-04-66-other-changes-in-1-19-0|66 other changes in 1.19.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-11-03 · OpenClaw · [[Changes/OpenClaw/2026-11-03-7-safety-and-privacy-changes-in-v2026-10-10|7 Safety and Privacy changes in v2026.10.10]]
- Later: 2026-11-04 · Gemini CLI · [[Changes/Gemini CLI/2026-11-04-fix-acp-include-mcp-server-and-tool-metadata-in-permission-requests-by-duvanka-p|fix(acp): include MCP server and tool metadata in permission requests]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-11-04-c11b38&body=Card%3A%20Changes%2FDify%2F2026-11-04-4-safety-and-privacy-changes-in-1-19-0.md%0ACard%20ID%3A%20dify-2026-11-04-c11b38%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.19.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->