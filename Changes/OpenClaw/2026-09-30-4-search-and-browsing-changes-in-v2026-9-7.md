---
card_id: openclaw-2026-09-30-ca1b58
date: '2026-09-30'
description: 'OpenClaw · 2026-09-30 · Search and Browsing: 4 changes in v2026.9.7
  — This release fixes how agents pick up edited skills and how you browse and revisit
  skill…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-05-28-added-ability-to-batch-delete-ignore-search-results|Added
    ability to batch delete/ignore search results]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2316
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: search-browsing
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 101bbef8aca8d925db944d4209d79b8655a340aeb2442a306c1b0e200ae35462
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-30-ca1b58
  comparison: ''
  date: '2026-09-30'
  description: 'OpenClaw — v2026.9.7: 4 Search and Browsing changes'
  evidence:
  - quote: This release fixes how agents pick up edited skills and how you browse
      and revisit skill suggestions.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: The optional Agents API runtime runs chats in a persistent hosted Linux
      workspace, with web search, OpenClaw tools, and file transfers on supported
      Linux storage. It requires an OpenAI API key with access to the chosen model.
      Self-hosted execution needs your own controller and matching workspace path,
      and does not support file transfers.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: You can browse OpenCode v2 sessions , read their transcripts, and track
      activity again, with v1 still supported. Activity tracking also works for initially
      empty sessions. If listing takes too long, OpenClaw reports an error instead
      of showing a misleading empty list.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Opening conversation history and refreshing session lists require fewer
      repeated checks and reads. Lists also avoid unpacking large saved snapshots
      they do not need, and browsing a parent’s child conversations skips unrelated
      sessions. Large session-group changes do less background work, though the effect
      on loading time depends on your setup.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 4-search-and-browsing-changes-in-v2026-9-7
  source_release: openclaw-2026-09-30-v2026-9-7-3d25d2bd
  source_type: openclaw_changelog
  theme: search-browsing
  title: 4 Search and Browsing changes in v2026.9.7
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-09-25-2-search-and-browsing-changes-in-rust-v0-157-0|2
  Search and Browsing changes in rust-v0.157.0]]'
- '[[Changes/Ollama/2026-09-29-models-using-web-search-can-now-perform-up-to-ten-searches-per-response-up-from|Models
  using web search can now perform up to ten searches per response, up from three]]'
- '[[Changes/Devin/2026-09-30-ask-devin-recognizes-commented-out-code|Ask Devin Recognizes
  Commented-Out Code]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-30-v2026-9-7-3d25d2bd|openclaw-2026-09-30-v2026-9-7-3d25d2bd]]'
source_type: openclaw_changelog
theme: search-browsing
title: 4 Search and Browsing changes in v2026.9.7
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Search and Browsing changes in v2026.9.7

**OpenClaw** · 2026-09-30 · [[Themes/search-browsing|Search and Browsing]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.7) · from [[Releases/OpenClaw/openclaw-2026-09-30-v2026-9-7-3d25d2bd|v2026.9.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> This release fixes how agents pick up edited skills and how you browse and revisit skill suggestions.

> The optional Agents API runtime runs chats in a persistent hosted Linux workspace, with web search, OpenClaw tools, and file transfers on supported Linux storage. It requires an OpenAI API key with access to the chosen model. Self-hosted execution needs your own controller and matching workspace path, and does not support file transfers.

> You can browse OpenCode v2 sessions , read their transcripts, and track activity again, with v1 still supported. Activity tracking also works for initially empty sessions. If listing takes too long, OpenClaw reports an error instead of showing a misleading empty list.

> Opening conversation history and refreshing session lists require fewer repeated checks and reads. Lists also avoid unpacking large saved snapshots they do not need, and browsing a parent’s child conversations skips unrelated sessions. Large session-group changes do less background work, though the effect on loading time depends on your setup.

Source: https://docs.openclaw.ai/releases/2026.9.7
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-30-4-context-window-changes-in-v2026-9-7|4 Context Window changes in v2026.9.7]] · Context Window
- [[Changes/OpenClaw/2026-09-30-13-developer-workflow-changes-in-v2026-9-7|13 Developer Workflow changes in v2026.9.7]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-30-3-files-and-data-changes-in-v2026-9-7|3 Files and Data changes in v2026.9.7]] · Files and Data
- [[Changes/OpenClaw/2026-09-30-13-account-and-access-changes-in-v2026-9-7|13 Account and Access changes in v2026.9.7]] · Account and Access
- [[Changes/OpenClaw/2026-09-30-2-enterprise-and-administration-changes-in-v2026-9-7|2 Enterprise and Administration changes in v2026.9.7]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-30-15-memory-and-personalization-changes-in-v2026-9-7|15 Memory and Personalization changes in v2026.9.7]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-30-33-agent-mode-changes-in-v2026-9-7|33 Agent Mode changes in v2026.9.7]] · Agent Mode
- [[Changes/OpenClaw/2026-09-30-17-interface-experience-changes-in-v2026-9-7|17 Interface Experience changes in v2026.9.7]] · Interface Experience
- [[Changes/OpenClaw/2026-09-30-36-apps-and-integrations-changes-in-v2026-9-7|36 Apps and Integrations changes in v2026.9.7]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-30-2-video-generation-changes-in-v2026-9-7|2 Video Generation changes in v2026.9.7]] · Video Generation
- [[Changes/OpenClaw/2026-09-30-12-voice-and-audio-changes-in-v2026-9-7|12 Voice and Audio changes in v2026.9.7]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-30-21-safety-and-privacy-changes-in-v2026-9-7|21 Safety and Privacy changes in v2026.9.7]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-30-administrators-can-opt-into-heap-snapshots-to-investigate-memory-growth-a-snapsh|Administrators can opt into heap snapshots to investigate memory growth]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-30-14-mobile-and-desktop-changes-in-v2026-9-7|14 Mobile and Desktop changes in v2026.9.7]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-30-9-editor-experience-changes-in-v2026-9-7|9 Editor Experience changes in v2026.9.7]] · Editor Experience
- [[Changes/OpenClaw/2026-09-30-22-model-support-changes-in-v2026-9-7|22 Model Support changes in v2026.9.7]] · Model Support
- [[Changes/OpenClaw/2026-09-30-11-automation-and-scheduling-changes-in-v2026-9-7|11 Automation and Scheduling changes in v2026.9.7]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-30-3-pricing-model-changes-in-v2026-9-7|3 Pricing Model changes in v2026.9.7]] · Pricing Model
- [[Changes/OpenClaw/2026-09-30-10-collaboration-changes-in-v2026-9-7|10 Collaboration changes in v2026.9.7]] · Collaboration
- [[Changes/OpenClaw/2026-09-30-4-multimodal-input-changes-in-v2026-9-7|4 Multimodal Input changes in v2026.9.7]] · Multimodal Input
- [[Changes/OpenClaw/2026-09-30-72-other-changes-in-v2026-9-7|72 other changes in v2026.9.7]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Search and Browsing

- Earlier: 2026-09-30 · Devin · [[Changes/Devin/2026-09-30-ask-devin-recognizes-commented-out-code|Ask Devin Recognizes Commented-Out Code]]
- Later: 2026-10-01 · AnythingLLM · [[Changes/AnythingLLM/2026-10-01-feat-add-firecrawl-agent-web-search-provider-by-juampihernandez-in-https-github|feat: add Firecrawl agent web-search provider]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-05-28 · Descript · [[Changes/Descript/2020-05-28-added-ability-to-batch-delete-ignore-search-results|Added ability to batch delete/ignore search results]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-30-ca1b58&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-30-4-search-and-browsing-changes-in-v2026-9-7.md%0ACard%20ID%3A%20openclaw-2026-09-30-ca1b58%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.7%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->