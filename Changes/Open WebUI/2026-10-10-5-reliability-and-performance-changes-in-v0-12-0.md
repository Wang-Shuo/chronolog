---
card_id: open-webui-2026-10-10-1bcb15
date: '2026-10-10'
description: 'Open WebUI · 2026-10-10 · Reliability and Performance: 5 changes in
  v0.12.0 — ▪️ **Livelier typing cursor while a reply streams.** The cursor shown
  at the end…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General
    performance: Among other improvements, users will notice that ChatGPT is now…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1395
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 558a895496357ed9bc9ca966233df9b30933d778ced06ed5175bd9782c1c5489
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-10-10-1bcb15
  comparison: ''
  date: '2026-10-10'
  description: 'Open WebUI — v0.12.0: 5 Reliability and Performance changes'
  evidence:
  - quote: ▪️ **Livelier typing cursor while a reply streams.** The cursor shown at
      the end of a streaming reply now pulses faster and fades further, so an ongoing
      reply is easier to spot. [Commit](https://github.com/open-webui/open-webui/commit/382295d94153d617cbc0701e812471e3c9e8ed99)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F680 **Faster JSON handling across the app.** JSON is now read and
      written with orjson by default, speeding up request and response bodies, streamed
      provider responses and live socket updates, which now encode about 17 times
      and decode about 3 times faster. [#31616](https://github.com/open-webui/open-webui/pull/31616)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4C7 **Faster knowledge pages on PostgreSQL.** Opening a knowledge
      base on PostgreSQL no longer scans the whole file table to find files still
      being processed, which with many large files could take seconds per page load
      and slow the database for everyone; a new index covers that lookup and is created
      by a migration. [Commit](https://github.com/open-webui/open-webui/commit/e1bbc859f19aa5c88e9ed857a32303b101d2119b),
      [#30003](https://github.com/open-webui/open-webui/issues/30003)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F504 **General improvements.** Various improvements were implemented
      across the application to enhance performance, stability, and security."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: ⏩ **Speech Playback Speed for Read Aloud.** Read Aloud and response auto-playback
      now play at the chosen Speech Playback Speed for every sentence, where the speed
      fell back to normal at each new sentence. [#31881](https://github.com/open-webui/open-webui/pull/31881),
      [#31870](https://github.com/open-webui/open-webui/issues/31870)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 5-reliability-and-performance-changes-in-v0-12-0
  source_release: open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b
  source_type: github_releases
  theme: reliability-performance
  title: 5 Reliability and Performance changes in v0.12.0
  type: change
related_changes:
- '[[Changes/Midjourney/2026-10-08-we-re-trying-to-both-improve-performance-and-just-generally-investigate-this-dir|We''re
  trying to both improve performance and just generally investigate…]]'
- '[[Changes/Ollama/2026-10-08-models-downloaded-with-earlier-versions-of-ollama-are-upgraded-in-the-background|Models
  downloaded with earlier versions of Ollama are upgraded in the background…]]'
- '[[Changes/Claude Code/2026-10-09-improved-transcript-toggle-ctrl-o-responsiveness-in-code-heavy-conversations-by|Improved
  transcript toggle (ctrl+o) responsiveness in code-heavy conversations…]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b|open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b]]'
source_type: github_releases
theme: reliability-performance
title: 5 Reliability and Performance changes in v0.12.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Reliability and Performance changes in v0.12.0

**Open WebUI** · 2026-10-10 · [[Themes/reliability-performance|Reliability and Performance]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.0) · from [[Releases/Open WebUI/open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b|v0.12.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> ▪️ **Livelier typing cursor while a reply streams.** The cursor shown at the end of a streaming reply now pulses faster and fades further, so an ongoing reply is easier to spot. [Commit](https://github.com/open-webui/open-webui/commit/382295d94153d617cbc0701e812471e3c9e8ed99)

> 🚀 **Faster JSON handling across the app.** JSON is now read and written with orjson by default, speeding up request and response bodies, streamed provider responses and live socket updates, which now encode about 17 times and decode about 3 times faster. [#31616](https://github.com/open-webui/open-webui/pull/31616)

> 📇 **Faster knowledge pages on PostgreSQL.** Opening a knowledge base on PostgreSQL no longer scans the whole file table to find files still being processed, which with many large files could take seconds per page load and slow the database for everyone; a new index covers that lookup and is created by a migration. [Commit](https://github.com/open-webui/open-webui/commit/e1bbc859f19aa5c88e9ed857a32303b101d2119b), [#30003](https://github.com/open-webui/open-webui/issues/30003)

> 🔄 **General improvements.** Various improvements were implemented across the application to enhance performance, stability, and security.

> ⏩ **Speech Playback Speed for Read Aloud.** Read Aloud and response auto-playback now play at the chosen Speech Playback Speed for every sentence, where the speed fell back to normal at each new sentence. [#31881](https://github.com/open-webui/open-webui/pull/31881), [#31870](https://github.com/open-webui/open-webui/issues/31870)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-10-10-5-enterprise-and-administration-changes-in-v0-12-0|5 Enterprise and Administration changes in v0.12.0]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-10-10-7-apps-and-integrations-changes-in-v0-12-0|7 Apps and Integrations changes in v0.12.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-10-10-12-voice-and-audio-changes-in-v0-12-0|12 Voice and Audio changes in v0.12.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-10-10-27-developer-workflow-changes-in-v0-12-0|27 Developer Workflow changes in v0.12.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-10-10-5-image-generation-changes-in-v0-12-0|5 Image Generation changes in v0.12.0]] · Image Generation
- [[Changes/Open WebUI/2026-10-10-49-model-support-changes-in-v0-12-0|49 Model Support changes in v0.12.0]] · Model Support
- [[Changes/Open WebUI/2026-10-10-19-account-and-access-changes-in-v0-12-0|19 Account and Access changes in v0.12.0]] · Account and Access
- [[Changes/Open WebUI/2026-10-10-10-automation-and-scheduling-changes-in-v0-12-0|10 Automation and Scheduling changes in v0.12.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-10-10-3-mobile-and-desktop-changes-in-v0-12-0|3 Mobile and Desktop changes in v0.12.0]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-10-10-6-files-and-data-changes-in-v0-12-0|6 Files and Data changes in v0.12.0]] · Files and Data
- [[Changes/Open WebUI/2026-10-10-13-collaboration-changes-in-v0-12-0|13 Collaboration changes in v0.12.0]] · Collaboration
- [[Changes/Open WebUI/2026-10-10-2-memory-and-personalization-changes-in-v0-12-0|2 Memory and Personalization changes in v0.12.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-10-10-5-context-window-changes-in-v0-12-0|5 Context Window changes in v0.12.0]] · Context Window
- [[Changes/Open WebUI/2026-10-10-18-interface-experience-changes-in-v0-12-0|18 Interface Experience changes in v0.12.0]] · Interface Experience
- [[Changes/Open WebUI/2026-10-10-7-agent-mode-changes-in-v0-12-0|7 Agent Mode changes in v0.12.0]] · Agent Mode
- [[Changes/Open WebUI/2026-10-10-6-safety-and-privacy-changes-in-v0-12-0|6 Safety and Privacy changes in v0.12.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-10-10-21-editor-experience-changes-in-v0-12-0|21 Editor Experience changes in v0.12.0]] · Editor Experience
- [[Changes/Open WebUI/2026-10-10-4-search-and-browsing-changes-in-v0-12-0|4 Search and Browsing changes in v0.12.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-10-10-68-other-changes-in-v0-12-0|68 other changes in v0.12.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2026-10-09 · Claude Code · [[Changes/Claude Code/2026-10-09-improved-transcript-toggle-ctrl-o-responsiveness-in-code-heavy-conversations-by|Improved transcript toggle (ctrl+o) responsiveness in code-heavy conversations…]]
- Later: 2026-10-10 · OpenClaw · [[Changes/OpenClaw/2026-10-10-2-reliability-and-performance-changes-in-v2026-10-1|2 Reliability and Performance changes in v2026.10.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General performance: Among other improvements, users will notice that ChatGPT is now…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-10-1bcb15&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-10-5-reliability-and-performance-changes-in-v0-12-0.md%0ACard%20ID%3A%20open-webui-2026-10-10-1bcb15%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->