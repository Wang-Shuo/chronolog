---
card_id: dify-2026-11-04-f86d91
date: '2026-11-04'
description: 'Dify · 2026-11-04 · Agent Mode: 14 changes in v1.19.0 - Trace Your Workflows,
  Layer by Layer — <summary><strong>See Agent file uploads and…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1217
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: e775b18ff410388cb874573a57614f56845a76fb6d8e3353589c309e87f8ccf1
product: dify
product_name: Dify
record:
  card_id: dify-2026-11-04-f86d91
  comparison: ''
  date: '2026-11-04'
  description: 'Dify — v1.19.0 - Trace Your Workflows, Layer by Layer: 14 Agent Mode
    changes'
  evidence:
  - quote: <summary><strong>See Agent file uploads and previews</strong></summary>
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  - quote: '![Inline PDF preview in Agent files, with the research brief and file
      list](https://github.com/user-attachments/assets/22bafc75-c8f5-46fd-b7ba-c5097f9cffb6)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  - quote: '*Read a PDF directly in the Agent file preview and switch between project
      files.*'
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  - quote: '![Agent batch upload dialog with a PDF, Python source file, and Markdown
      guidelines selected](https://github.com/user-attachments/assets/5eafd0c1-f46d-4966-bbc0-e6cd5eacff02)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  - quote: '![Syntax-highlighted Python source in the Agent file preview](https://github.com/user-attachments/assets/1435fd23-7489-450a-a200-dbd81c1b588d)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  - quote: '**Back up first.** Retain the database, vector-store data, uploaded files,
      Agent snapshot/workspace storage, deployment secrets, and environment files.
      Use a maintenance window for a single-stack upgrade.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  - quote: '**Tracing history is not rebuilt.** Existing Agent trace-ledger data remains
      readable, but previously exported traces do not acquire the new nested spans.
      (#44673)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  - quote: Always emit format v2 for App packages, including nested packages and packages
      without Workflow Tools. This does not change the separate roster-Agent package
      format. (#45353)
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  - quote: '**Batch Agent file management:** multi-select and multi-file drop, parallel
      uploads, one atomic binding request, retry using cached upload IDs, and protection
      against stale Composer saves overwriting newly bound files. Existing single-file
      endpoints remain compatible. (#44947)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  - quote: '**More usable previews:** highlighted text, on-demand PDF rendering, stable
      open previews, and explicit truncated-text notices across Agent files, Skills,
      and working directories. (#45032, #45045)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  - quote: '**Dependency hardening:** update Authlib to 1.9.1, require LiteLLM 1.100.4
      or later within its supported major version, move Agent Pydantic AI to 2.53.0
      and Pillow to 13.0.0, update pypdf to 6.21.4, and refresh Werkzeug, GitPython,
      and other dependency fixes. The standalone Agent pins filelock 4.2.1; Docker
      build tooling updates uv to 0.13.4. These source updates do not claim to resolve
      every finding in external or Enterprise base images. (#44606, #44793, #44868,
      #44871, #44886, #45041, #45104, #45215, #45259, #45214, #45260)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  - quote: <summary><strong>Bug fixes · workflows, Agents, knowledge, APIs, and the
      web app</strong></summary>
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  - quote: 'Preserve caller identity for scheduled Agent file access, use the UTC
      clock for the Start node''s `sys.timestamp`, and order weekly schedule previews
      by date. Webhook query/form numbers retain integer precision and reject non-finite
      values. (#44796, #44847, #44718, #44706)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  - quote: '**Agents, tools, and Skills**'
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 14-agent-mode-changes-in-1-19-0
  source_release: dify-2026-11-04-1-19-0-github-433629888-738006ec
  source_type: github_releases
  theme: agent-mode
  title: 14 Agent Mode changes in 1.19.0
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-11-03-9-agent-mode-changes-in-v2026-10-10|9 Agent Mode
  changes in v2026.10.10]]'
- '[[Changes/OpenClaw/2026-11-03-you-can-now-work-directly-in-a-folder-on-another-computer-connected-to-openclaw|Work
  directly in a folder on another computer connected to OpenClaw]]'
- '[[Changes/OpenHands/2026-11-03-3-agent-mode-changes-in-v1-35-0|3 Agent Mode changes
  in v1.35.0]]'
source_release: '[[Releases/Dify/dify-2026-11-04-1-19-0-github-433629888-738006ec|dify-2026-11-04-1-19-0-github-433629888-738006ec]]'
source_type: github_releases
theme: agent-mode
title: 14 Agent Mode changes in 1.19.0
type: change
---

<!-- chronolog:begin region="header" -->
# 14 Agent Mode changes in 1.19.0

**Dify** · 2026-11-04 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.19.0) · from [[Releases/Dify/dify-2026-11-04-1-19-0-github-433629888-738006ec|v1.19.0 - Trace Your Workflows, Layer by Layer]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> \<summary>\<strong>See Agent file uploads and previews\</strong>\</summary>

> ![Inline PDF preview in Agent files, with the research brief and file list](https://github.com/user-attachments/assets/22bafc75-c8f5-46fd-b7ba-c5097f9cffb6)

> *Read a PDF directly in the Agent file preview and switch between project files.*

> ![Agent batch upload dialog with a PDF, Python source file, and Markdown guidelines selected](https://github.com/user-attachments/assets/5eafd0c1-f46d-4966-bbc0-e6cd5eacff02)

> ![Syntax-highlighted Python source in the Agent file preview](https://github.com/user-attachments/assets/1435fd23-7489-450a-a200-dbd81c1b588d)

> **Back up first.** Retain the database, vector-store data, uploaded files, Agent snapshot/workspace storage, deployment secrets, and environment files. Use a maintenance window for a single-stack upgrade.

> **Tracing history is not rebuilt.** Existing Agent trace-ledger data remains readable, but previously exported traces do not acquire the new nested spans. (#44673)

> Always emit format v2 for App packages, including nested packages and packages without Workflow Tools. This does not change the separate roster-Agent package format. (#45353)

> **Batch Agent file management:** multi-select and multi-file drop, parallel uploads, one atomic binding request, retry using cached upload IDs, and protection against stale Composer saves overwriting newly bound files. Existing single-file endpoints remain compatible. (#44947)

> **More usable previews:** highlighted text, on-demand PDF rendering, stable open previews, and explicit truncated-text notices across Agent files, Skills, and working directories. (#45032, #45045)

> **Dependency hardening:** update Authlib to 1.9.1, require LiteLLM 1.100.4 or later within its supported major version, move Agent Pydantic AI to 2.53.0 and Pillow to 13.0.0, update pypdf to 6.21.4, and refresh Werkzeug, GitPython, and other dependency fixes. The standalone Agent pins filelock 4.2.1; Docker build tooling updates uv to 0.13.4. These source updates do not claim to resolve every finding in external or Enterprise base images. (#44606, #44793, #44868, #44871, #44886, #45041, #45104, #45215, #45259, #45214, #45260)

> \<summary>\<strong>Bug fixes · workflows, Agents, knowledge, APIs, and the web app\</strong>\</summary>

> Preserve caller identity for scheduled Agent file access, use the UTC clock for the Start node's `sys.timestamp`, and order weekly schedule previews by date. Webhook query/form numbers retain integer precision and reject non-finite values. (#44796, #44847, #44718, #44706)

> **Agents, tools, and Skills**

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
- [[Changes/Dify/2026-11-04-4-safety-and-privacy-changes-in-1-19-0|4 Safety and Privacy changes in 1.19.0]] · Safety and Privacy
- [[Changes/Dify/2026-11-04-workspace-controls-enabling-or-disabling-provider-models-requires-an-owner-or-ad|Workspace controls: enabling or disabling provider models requires an owner…]] · Enterprise and Administration
- [[Changes/Dify/2026-11-04-summary-strong-improvements-editing-accessibility-performance-and-operations-str|summarystrongImprovements · editing, accessibility, performance…]] · Accessibility and Localization
- [[Changes/Dify/2026-11-04-2-interface-experience-changes-in-1-19-0|2 Interface Experience changes in 1.19.0]] · Interface Experience
- [[Changes/Dify/2026-11-04-6-context-window-changes-in-1-19-0|6 Context Window changes in 1.19.0]] · Context Window
- [[Changes/Dify/2026-11-04-2-account-and-access-changes-in-1-19-0|2 Account and Access changes in 1.19.0]] · Account and Access
- [[Changes/Dify/2026-11-04-66-other-changes-in-1-19-0|66 other changes in 1.19.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-11-03 · OpenHands · [[Changes/OpenHands/2026-11-03-3-agent-mode-changes-in-v1-35-0|3 Agent Mode changes in v1.35.0]]
- Later: 2026-11-04 · Kimi Code · [[Changes/Kimi Code/2026-11-04-3-agent-mode-changes-in-kimi-code-2-5-0|3 Agent Mode changes in Kimi Code 2.5.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-11-04-f86d91&body=Card%3A%20Changes%2FDify%2F2026-11-04-14-agent-mode-changes-in-1-19-0.md%0ACard%20ID%3A%20dify-2026-11-04-f86d91%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.19.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->