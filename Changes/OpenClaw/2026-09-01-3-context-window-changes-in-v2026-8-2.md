---
card_id: openclaw-2026-09-01-1f36a1
date: '2026-09-01'
description: 'OpenClaw · 2026-09-01 · Context Window: 3 changes in v2026.8.2 — Long
  native Codex conversations and detached Skill Workshop reviews also prepare the
  context…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click
    to select a range]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2540
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 10279223464c460bca99eb86bb68c60d8e4d5639b7904db4d6dfd1621c89a97f
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-01-1f36a1
  comparison: ''
  date: '2026-09-01'
  description: 'OpenClaw — v2026.8.2: 3 Context Window changes'
  evidence:
  - quote: Long native Codex conversations and detached Skill Workshop reviews also
      prepare the context they need without loading as much history that the model
      will never see. Resuming, listing, cleaning up, and checking large session stores
      does less unnecessary work while keeping the full history available to the paths
      that need it.
    source_release: https://docs.openclaw.ai/releases/2026.8.2
  - quote: Known local Codex sessions in a large home can now be continued, opened
      in a terminal, viewed, or archived without scanning unrelated rollout history
      first, and compatible conversations can return to the same thread after the
      app server restarts. A fresh Codex thread also carries forward facts preserved
      only in a saved compaction or branch summary, while token counts and the effective
      context window recover after /new instead of looking like a fresh zero.
    source_release: https://docs.openclaw.ai/releases/2026.8.2
  - quote: When an agent edits or searches a workspace, more of what was actually
      on disk now survives the trip. Patches preserve untouched content and line endings,
      formatting-only edits are no longer silently discarded, search results keep
      readable context from files that previously looked garbled and from unusual
      filenames, and local names beginning with @ stay literal when that file or directory
      exists.
    source_release: https://docs.openclaw.ai/releases/2026.8.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 3-context-window-changes-in-v2026-8-2
  source_release: openclaw-2026-09-01-v2026-8-2-cca64187
  source_type: openclaw_changelog
  theme: context-window
  title: 3 Context Window changes in v2026.8.2
  type: change
related_changes:
- '[[Changes/Claude Code/2026-08-28-improved-retry-when-the-model-s-tool-call-is-malformed-the-broken-output-is-now|Improved
  retry when the model''s tool call is malformed]]'
- '[[Changes/ChatGPT/2026-08-31-bring-your-browser-into-work-and-codex-mention-open-tabs-to-use-them-as-context-af2c3a|Bring
  your browser into Work and Codex]]'
- '[[Changes/Codex CLI/2026-09-01-9-context-window-changes-in-rust-v0-152-0|9 Context
  Window changes in rust-v0.152.0]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-01-v2026-8-2-cca64187|openclaw-2026-09-01-v2026-8-2-cca64187]]'
source_type: openclaw_changelog
theme: context-window
title: 3 Context Window changes in v2026.8.2
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Context Window changes in v2026.8.2

**OpenClaw** · 2026-09-01 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.8.2) · from [[Releases/OpenClaw/openclaw-2026-09-01-v2026-8-2-cca64187|v2026.8.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Long native Codex conversations and detached Skill Workshop reviews also prepare the context they need without loading as much history that the model will never see. Resuming, listing, cleaning up, and checking large session stores does less unnecessary work while keeping the full history available to the paths that need it.

> Known local Codex sessions in a large home can now be continued, opened in a terminal, viewed, or archived without scanning unrelated rollout history first, and compatible conversations can return to the same thread after the app server restarts. A fresh Codex thread also carries forward facts preserved only in a saved compaction or branch summary, while token counts and the effective context window recover after /new instead of looking like a fresh zero.

> When an agent edits or searches a workspace, more of what was actually on disk now survives the trip. Patches preserve untouched content and line endings, formatting-only edits are no longer silently discarded, search results keep readable context from files that previously looked garbled and from unusual filenames, and local names beginning with @ stay literal when that file or directory exists.

Source: https://docs.openclaw.ai/releases/2026.8.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-01-4-model-support-changes-in-v2026-8-2|4 Model Support changes in v2026.8.2]] · Model Support
- [[Changes/OpenClaw/2026-09-01-11-agent-mode-changes-in-v2026-8-2|11 Agent Mode changes in v2026.8.2]] · Agent Mode
- [[Changes/OpenClaw/2026-09-01-9-voice-and-audio-changes-in-v2026-8-2|9 Voice and Audio changes in v2026.8.2]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-01-4-collaboration-changes-in-v2026-8-2|4 Collaboration changes in v2026.8.2]] · Collaboration
- [[Changes/OpenClaw/2026-09-01-5-editor-experience-changes-in-v2026-8-2|5 Editor Experience changes in v2026.8.2]] · Editor Experience
- [[Changes/OpenClaw/2026-09-01-7-safety-and-privacy-changes-in-v2026-8-2|7 Safety and Privacy changes in v2026.8.2]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-01-3-mobile-and-desktop-changes-in-v2026-8-2|3 Mobile and Desktop changes in v2026.8.2]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-01-another-382-changes-in-v2026-8-2-primarily-affect-the-people-who-build-test-docu|Another 382 changes in v2026.8.2 primarily affect the people who build, test…]] · Files and Data
- [[Changes/OpenClaw/2026-09-01-usage-and-status-views-now-carry-cumulative-output-token-totals-through-tool-cal|Usage and status views now carry cumulative output-token totals through tool calls…]] · Pricing Model
- [[Changes/OpenClaw/2026-09-01-2-automation-and-scheduling-changes-in-v2026-8-2|2 Automation and Scheduling changes in v2026.8.2]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-01-9-apps-and-integrations-changes-in-v2026-8-2|9 Apps and Integrations changes in v2026.8.2]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-01-4-memory-and-personalization-changes-in-v2026-8-2|4 Memory and Personalization changes in v2026.8.2]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-01-3-interface-experience-changes-in-v2026-8-2|3 Interface Experience changes in v2026.8.2]] · Interface Experience
- [[Changes/OpenClaw/2026-09-01-2-account-and-access-changes-in-v2026-8-2|2 Account and Access changes in v2026.8.2]] · Account and Access
- [[Changes/OpenClaw/2026-09-01-importing-or-returning-to-a-large-retained-history-also-requires-less-local-work|Importing or returning to a large retained history also requires less local work…]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-01-20-other-changes-in-v2026-8-2|20 other changes in v2026.8.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-09-01 · Codex CLI · [[Changes/Codex CLI/2026-09-01-9-context-window-changes-in-rust-v0-152-0|9 Context Window changes in rust-v0.152.0]]
- Later: 2026-09-02 · Google Antigravity · [[Changes/Google Antigravity/2026-09-02-you-can-now-highlight-portions-of-antigravity-responses-to-quote-as-context-for|Highlight portions of Antigravity responses to quote as context for follow-up prompts]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click to select a range]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-01-1f36a1&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-01-3-context-window-changes-in-v2026-8-2.md%0ACard%20ID%3A%20openclaw-2026-09-01-1f36a1%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.8.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->