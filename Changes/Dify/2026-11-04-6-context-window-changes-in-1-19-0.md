---
card_id: dify-2026-11-04-f06464
date: '2026-11-04'
description: 'Dify · 2026-11-04 · Context Window: 6 changes in v1.19.0 - Trace Your
  Workflows, Layer by Layer — **Dify 1.19.0 brings nested workflow tracing to your…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2
    Context Window changes in 0.2.9]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1280
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 627e4ab2a6e5cfd92928213267b89351000e0c92ca561cacad82bfbecdcf379a
product: dify
product_name: Dify
record:
  card_id: dify-2026-11-04-f06464
  comparison: ''
  date: '2026-11-04'
  description: 'Dify — v1.19.0 - Trace Your Workflows, Layer by Layer: 6 Context Window
    changes'
  evidence:
  - quote: '**Dify 1.19.0 brings nested workflow tracing to your observability tools.**
      Follow a workflow into the Workflow Tools it calls, inspect the steps inside
      each invocation, and keep the LLM context alongside the execution tree.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  - quote: '**Keep the LLM context.** Inspect formatted prompts and responses, token
      usage, and project, trace, and observation links.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  - quote: '**Dataset token scope:** resource access tokens can list only their explicitly
      bound active datasets; `include_all=true` cannot widen that scope. Legacy workspace
      Dataset API keys retain tenant-wide behavior without inheriting an injected
      owner''s personal visibility filters. (#44840)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  - quote: 'Admit streaming Workflow and Chatflow requests only once against app concurrency
      limits, so a limit of one accepts the single active request. Terminal Chatflow
      events now stop the execution watchdog and release its retained context. (#45038,
      #45029)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  - quote: 'Reuse extracted PDF image assets for repeated previews of the same source
      upload. Restore Service API file-document creation/update when tenant context
      is missing or the original dataset creator has left. (#44684, #44972)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  - quote: The old `OPS_TRACE_UNIFIED_ENABLED`, `OPS_TRACE_RETRYABLE_DISPATCH_MAX_RETRIES`,
      `OPS_TRACE_RETRYABLE_DISPATCH_DELAY_SECONDS`, and `OPS_TRACE_PARENT_CONTEXT_TTL_SECONDS`
      settings are removed. Existing Agent application-tracing opt-in settings remain
      supported. (#44673)
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 6-context-window-changes-in-1-19-0
  source_release: dify-2026-11-04-1-19-0-github-433629888-738006ec
  source_type: github_releases
  theme: context-window
  title: 6 Context Window changes in 1.19.0
  type: change
related_changes:
- '[[Changes/Ollama/2026-11-03-qwen3-and-qwen3-5-models-using-long-context-yarn-scaling|Qwen3
  and Qwen3.5 models using long-context (YaRN) scaling]]'
- "[[Changes/Open WebUI/2026-11-03-live-context-usage-estimates-the-context-indicator-now-accounts-for-output-arriv|\U0001F4CF
  Live context usage estimates. The context indicator now accounts for output…]]"
- '[[Changes/OpenClaw/2026-11-03-5-context-window-changes-in-v2026-10-10|5 Context
  Window changes in v2026.10.10]]'
source_release: '[[Releases/Dify/dify-2026-11-04-1-19-0-github-433629888-738006ec|dify-2026-11-04-1-19-0-github-433629888-738006ec]]'
source_type: github_releases
theme: context-window
title: 6 Context Window changes in 1.19.0
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Context Window changes in 1.19.0

**Dify** · 2026-11-04 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.19.0) · from [[Releases/Dify/dify-2026-11-04-1-19-0-github-433629888-738006ec|v1.19.0 - Trace Your Workflows, Layer by Layer]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **Dify 1.19.0 brings nested workflow tracing to your observability tools.** Follow a workflow into the Workflow Tools it calls, inspect the steps inside each invocation, and keep the LLM context alongside the execution tree.

> **Keep the LLM context.** Inspect formatted prompts and responses, token usage, and project, trace, and observation links.

> **Dataset token scope:** resource access tokens can list only their explicitly bound active datasets; `include_all=true` cannot widen that scope. Legacy workspace Dataset API keys retain tenant-wide behavior without inheriting an injected owner's personal visibility filters. (#44840)

> Admit streaming Workflow and Chatflow requests only once against app concurrency limits, so a limit of one accepts the single active request. Terminal Chatflow events now stop the execution watchdog and release its retained context. (#45038, #45029)

> Reuse extracted PDF image assets for repeated previews of the same source upload. Restore Service API file-document creation/update when tenant context is missing or the original dataset creator has left. (#44684, #44972)

> The old `OPS_TRACE_UNIFIED_ENABLED`, `OPS_TRACE_RETRYABLE_DISPATCH_MAX_RETRIES`, `OPS_TRACE_RETRYABLE_DISPATCH_DELAY_SECONDS`, and `OPS_TRACE_PARENT_CONTEXT_TTL_SECONDS` settings are removed. Existing Agent application-tracing opt-in settings remain supported. (#44673)

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
- [[Changes/Dify/2026-11-04-14-agent-mode-changes-in-1-19-0|14 Agent Mode changes in 1.19.0]] · Agent Mode
- [[Changes/Dify/2026-11-04-2-account-and-access-changes-in-1-19-0|2 Account and Access changes in 1.19.0]] · Account and Access
- [[Changes/Dify/2026-11-04-66-other-changes-in-1-19-0|66 other changes in 1.19.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-11-03 · OpenClaw · [[Changes/OpenClaw/2026-11-03-5-context-window-changes-in-v2026-10-10|5 Context Window changes in v2026.10.10]]
- Later: 2026-11-05 · OpenClaw · [[Changes/OpenClaw/2026-11-05-3-context-window-changes-in-v2026-11-1|3 Context Window changes in v2026.11.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-04 · Cursor · [[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2 Context Window changes in 0.2.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-11-04-f06464&body=Card%3A%20Changes%2FDify%2F2026-11-04-6-context-window-changes-in-1-19-0.md%0ACard%20ID%3A%20dify-2026-11-04-f06464%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.19.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->