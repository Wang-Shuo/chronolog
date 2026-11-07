---
card_id: openclaw-2026-09-01-b6fd44
date: '2026-09-01'
description: 'OpenClaw · 2026-09-01 · Memory and Personalization: 4 changes in v2026.8.2
  — Busy Gateways now spend less time repeating work while sessions are renamed…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1139
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 63e3fa6053a49a9266ac293158ee8a766740d8abae19bdbbeb254409459e2f2a
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-01-b6fd44
  comparison: ''
  date: '2026-09-01'
  description: 'OpenClaw — v2026.8.2: 4 Memory and Personalization changes'
  evidence:
  - quote: Busy Gateways now spend less time repeating work while sessions are renamed,
      histories are opened, task pages are listed, scheduled work is checked, or several
      agent turns are running at once. Large session listings retain less memory,
      unusually branched histories no longer repeat the same ancestry work, and bounded
      operator requests get a fairer chance to start before returning a retryable
      overload result.
    source_release: https://docs.openclaw.ai/releases/2026.8.2
  - quote: Memory and large retained histories now avoid more unnecessary work without
      changing the information available to the paths that need it. Memory Wiki rejects
      invalid operations before changing a page, local scans stop importing generated
      copies of their own vault content, and several long-session paths hold less
      transient data while they prepare context or inspect history.
    source_release: https://docs.openclaw.ai/releases/2026.8.2
  - quote: Memory Wiki now rejects unknown operations before changing or synchronizing
      a page, and local scans stop importing generated copies of its own vault pages
      again. Canceled Memory requests return the original cancellation error, while
      the optional database-backed memory plugin starts with less memory and keeps
      the same three tools.
    source_release: https://docs.openclaw.ai/releases/2026.8.2
  - quote: Optional image decoding now uses patched Sharp 0.35.4 and libheif 1.23.2
      components without making Sharp mandatory. A standalone @openclaw/memory-lancedb
      installation can still resolve an older Sharp through its optional Transformers
      path, so the dependency repair should not be read as universal coverage. Bun
      1.4 Gateway connections also use the installed npm WebSocket receiver.
    source_release: https://docs.openclaw.ai/releases/2026.8.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 4-memory-and-personalization-changes-in-v2026-8-2
  source_release: openclaw-2026-09-01-v2026-8-2-cca64187
  source_type: openclaw_changelog
  theme: memory
  title: 4 Memory and Personalization changes in v2026.8.2
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-08-27-ship-mcp-2026-07-28-support-to-cli-sdk-ide-and-in-memory-clients|Ship
  MCP 2026-07-28 support to CLI, SDK, IDE, and in-memory clients]]'
- '[[Changes/Midjourney/2026-08-27-using-personalization-moodboards-and-srefs-moodboards-srefs-may-work-best-with-s|Using
  personalization, moodboards and srefs…]]'
- '[[Changes/OpenClaw/2026-08-31-memory-an-eligible-personal-claw-can-recall-relevant-context-from-that-agent-s-o|Memory
  - An eligible personal Claw can recall relevant context from that agent''s…]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-01-v2026-8-2-cca64187|openclaw-2026-09-01-v2026-8-2-cca64187]]'
source_type: openclaw_changelog
theme: memory
title: 4 Memory and Personalization changes in v2026.8.2
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Memory and Personalization changes in v2026.8.2

**OpenClaw** · 2026-09-01 · [[Themes/memory|Memory and Personalization]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.8.2) · from [[Releases/OpenClaw/openclaw-2026-09-01-v2026-8-2-cca64187|v2026.8.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Busy Gateways now spend less time repeating work while sessions are renamed, histories are opened, task pages are listed, scheduled work is checked, or several agent turns are running at once. Large session listings retain less memory, unusually branched histories no longer repeat the same ancestry work, and bounded operator requests get a fairer chance to start before returning a retryable overload result.

> Memory and large retained histories now avoid more unnecessary work without changing the information available to the paths that need it. Memory Wiki rejects invalid operations before changing a page, local scans stop importing generated copies of their own vault content, and several long-session paths hold less transient data while they prepare context or inspect history.

> Memory Wiki now rejects unknown operations before changing or synchronizing a page, and local scans stop importing generated copies of its own vault pages again. Canceled Memory requests return the original cancellation error, while the optional database-backed memory plugin starts with less memory and keeps the same three tools.

> Optional image decoding now uses patched Sharp 0.35.4 and libheif 1.23.2 components without making Sharp mandatory. A standalone @openclaw/memory-lancedb installation can still resolve an older Sharp through its optional Transformers path, so the dependency repair should not be read as universal coverage. Bun 1.4 Gateway connections also use the installed npm WebSocket receiver.

Source: https://docs.openclaw.ai/releases/2026.8.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-01-4-model-support-changes-in-v2026-8-2|4 Model Support changes in v2026.8.2]] · Model Support
- [[Changes/OpenClaw/2026-09-01-11-agent-mode-changes-in-v2026-8-2|11 Agent Mode changes in v2026.8.2]] · Agent Mode
- [[Changes/OpenClaw/2026-09-01-9-voice-and-audio-changes-in-v2026-8-2|9 Voice and Audio changes in v2026.8.2]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-01-3-context-window-changes-in-v2026-8-2|3 Context Window changes in v2026.8.2]] · Context Window
- [[Changes/OpenClaw/2026-09-01-4-collaboration-changes-in-v2026-8-2|4 Collaboration changes in v2026.8.2]] · Collaboration
- [[Changes/OpenClaw/2026-09-01-5-editor-experience-changes-in-v2026-8-2|5 Editor Experience changes in v2026.8.2]] · Editor Experience
- [[Changes/OpenClaw/2026-09-01-7-safety-and-privacy-changes-in-v2026-8-2|7 Safety and Privacy changes in v2026.8.2]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-01-3-mobile-and-desktop-changes-in-v2026-8-2|3 Mobile and Desktop changes in v2026.8.2]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-01-another-382-changes-in-v2026-8-2-primarily-affect-the-people-who-build-test-docu|Another 382 changes in v2026.8.2 primarily affect the people who build, test…]] · Files and Data
- [[Changes/OpenClaw/2026-09-01-usage-and-status-views-now-carry-cumulative-output-token-totals-through-tool-cal|Usage and status views now carry cumulative output-token totals through tool calls…]] · Pricing Model
- [[Changes/OpenClaw/2026-09-01-2-automation-and-scheduling-changes-in-v2026-8-2|2 Automation and Scheduling changes in v2026.8.2]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-01-9-apps-and-integrations-changes-in-v2026-8-2|9 Apps and Integrations changes in v2026.8.2]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-01-3-interface-experience-changes-in-v2026-8-2|3 Interface Experience changes in v2026.8.2]] · Interface Experience
- [[Changes/OpenClaw/2026-09-01-2-account-and-access-changes-in-v2026-8-2|2 Account and Access changes in v2026.8.2]] · Account and Access
- [[Changes/OpenClaw/2026-09-01-importing-or-returning-to-a-large-retained-history-also-requires-less-local-work|Importing or returning to a large retained history also requires less local work…]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-01-20-other-changes-in-v2026-8-2|20 other changes in v2026.8.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Memory and Personalization

- Earlier: 2026-08-31 · OpenClaw · [[Changes/OpenClaw/2026-08-31-memory-an-eligible-personal-claw-can-recall-relevant-context-from-that-agent-s-o|Memory - An eligible personal Claw can recall relevant context from that agent's…]]
- Later: 2026-09-03 · OpenClaw · [[Changes/OpenClaw/2026-09-03-19-memory-and-personalization-changes-in-v2026-9-1|19 Memory and Personalization changes in v2026.9.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-01-b6fd44&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-01-4-memory-and-personalization-changes-in-v2026-8-2.md%0ACard%20ID%3A%20openclaw-2026-09-01-b6fd44%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.8.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->