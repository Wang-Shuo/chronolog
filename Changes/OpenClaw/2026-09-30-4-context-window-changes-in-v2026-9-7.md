---
card_id: openclaw-2026-09-30-1fd6e5
date: '2026-09-30'
description: 'OpenClaw · 2026-09-30 · Context Window: 4 changes in v2026.9.7 — Context-engine
  plugins that store completed turns now give the current conversation priority…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click
    to select a range]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2569
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 55ad171725acde4e2c60b59f20edd6fcea4da6164d3101311f73cc47ae153348
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-30-1fd6e5
  comparison: ''
  date: '2026-09-30'
  description: 'OpenClaw — v2026.9.7: 4 Context Window changes'
  evidence:
  - quote: Context-engine plugins that store completed turns now give the current
      conversation priority over retries from other sessions, preventing stale work
      elsewhere from holding up new context.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: The managed Codex runtime moves to 0.158.0, fixing missing output from
      completed commands. Parent agents can continue when workers finish, and conversation
      forks and compaction retain their context more consistently. These fixes need
      the updated runtime and do not replay previously failed deliveries. Model discovery
      also waits longer for slow responses, unless you configured a shorter timeout.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: GitHub badges show when an item was merged or closed in your browser's
      local time, and closed draft pull requests are correctly marked Closed . Personal
      GitHub connections also skip unnecessary background checks while their tokens
      are fresh.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: If your settings or tokens contain environment-variable expressions, check
      the configuration guidance before updating. Some values now change meaning and
      can break access.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 4-context-window-changes-in-v2026-9-7
  source_release: openclaw-2026-09-30-v2026-9-7-3d25d2bd
  source_type: openclaw_changelog
  theme: context-window
  title: 4 Context Window changes in v2026.9.7
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-30-improved-the-model-fallback-notice-and-the-autocompact-thrashing-error-to-say-wh|Improved
  the model fallback notice and the autocompact-thrashing error to say…]]'
- '[[Changes/Cline/2026-09-30-reasoning-tokens-are-no-longer-counted-twice-in-token-usage-cost-is-unchanged|Reasoning
  tokens are no longer counted twice in token usage]]'
- '[[Changes/GitHub Copilot CLI/2026-09-30-compaction-now-returns-a-summary-even-when-instructions-ask-for-tool-use|Compaction
  now returns a summary even when instructions ask for tool use]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-30-v2026-9-7-3d25d2bd|openclaw-2026-09-30-v2026-9-7-3d25d2bd]]'
source_type: openclaw_changelog
theme: context-window
title: 4 Context Window changes in v2026.9.7
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Context Window changes in v2026.9.7

**OpenClaw** · 2026-09-30 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.7) · from [[Releases/OpenClaw/openclaw-2026-09-30-v2026-9-7-3d25d2bd|v2026.9.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Context-engine plugins that store completed turns now give the current conversation priority over retries from other sessions, preventing stale work elsewhere from holding up new context.

> The managed Codex runtime moves to 0.158.0, fixing missing output from completed commands. Parent agents can continue when workers finish, and conversation forks and compaction retain their context more consistently. These fixes need the updated runtime and do not replay previously failed deliveries. Model discovery also waits longer for slow responses, unless you configured a shorter timeout.

> GitHub badges show when an item was merged or closed in your browser's local time, and closed draft pull requests are correctly marked Closed . Personal GitHub connections also skip unnecessary background checks while their tokens are fresh.

> If your settings or tokens contain environment-variable expressions, check the configuration guidance before updating. Some values now change meaning and can break access.

Source: https://docs.openclaw.ai/releases/2026.9.7
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

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
- [[Changes/OpenClaw/2026-09-30-4-search-and-browsing-changes-in-v2026-9-7|4 Search and Browsing changes in v2026.9.7]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-30-3-pricing-model-changes-in-v2026-9-7|3 Pricing Model changes in v2026.9.7]] · Pricing Model
- [[Changes/OpenClaw/2026-09-30-10-collaboration-changes-in-v2026-9-7|10 Collaboration changes in v2026.9.7]] · Collaboration
- [[Changes/OpenClaw/2026-09-30-4-multimodal-input-changes-in-v2026-9-7|4 Multimodal Input changes in v2026.9.7]] · Multimodal Input
- [[Changes/OpenClaw/2026-09-30-72-other-changes-in-v2026-9-7|72 other changes in v2026.9.7]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-09-30 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-09-30-compaction-now-returns-a-summary-even-when-instructions-ask-for-tool-use|Compaction now returns a summary even when instructions ask for tool use]]
- Later: 2026-10-01 · Claude Code · [[Changes/Claude Code/2026-10-01-changed-opus-4-7-and-fable-to-use-a-1m-context-window-by-default-on-bedrock-vert|Changed Opus 4.7+ and Fable to use a 1M context window by default on Bedrock…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click to select a range]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-30-1fd6e5&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-30-4-context-window-changes-in-v2026-9-7.md%0ACard%20ID%3A%20openclaw-2026-09-30-1fd6e5%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.7%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->