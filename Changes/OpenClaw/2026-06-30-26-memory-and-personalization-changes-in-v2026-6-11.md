---
card_id: openclaw-2026-06-30-54da95
date: '2026-06-30'
description: 'OpenClaw · 2026-06-30 · Memory and Personalization: 26 changes in v2026.6.11
  — Matrix E2EE gateways can stay online during long-running use instead of…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1076
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 877a9c5f3e625ef9ce7e82dbe643bc4fcfdcf3af1264289882fc8241bf179524
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-06-30-54da95
  comparison: ''
  date: '2026-06-30'
  description: 'OpenClaw — v2026.6.11: 26 Memory and Personalization changes'
  evidence:
  - quote: 'Matrix E2EE gateways can stay online during long-running use instead of
      gradually consuming memory until a crash takes channels and in-flight work down.
      #94942 Related #90455 . Thanks @xzh-icenter, @yar-sh.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Matrix users and operators now get a clear failure when a homeserver sends
      an oversized or stalled response, instead of OpenClaw continuing to buffer it
      and risking unbounded memory use. #95240 Thanks @alix-007.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'OpenClaw now rejects oversized provider catalog or JSON responses with
      a clear error before buffering the entire response in memory. #95218 Thanks
      @alix-007.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Google-backed embedded-agent runs now stop reading oversized or never-ending
      prompt-cache responses before they can exhaust memory or leave the run stalled.
      #95417 Thanks @alix-007.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'OpenRouter model scans fail safely on oversized or malformed catalogs
      instead of risking excessive memory use that can destabilize OpenClaw. #95418
      Thanks @alix-007.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'OpenRouter setups now reject oversized model catalogs before they can
      exhaust OpenClaw''s memory, without caching or immediately refetching the failed
      response. #95420 Thanks @alix-007, @sallyom.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Oversized or stalled provider catalogs now fail quickly with a clear error
      instead of hanging OpenClaw or consuming unbounded memory, while normal catalogs
      continue to load. #95827 Thanks @alix-007.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: OpenRouter model scans now accept the same larger valid catalogs as runtime
      discovery while still rejecting oversized responses before they can consume
      unbounded memory. ad3b2f4 Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: Sessions , compaction , memory , and QMD-backed memory preserve the intended
      conversation and useful context more consistently through long-running work,
      reconnects, upgrades, and transcript repair. Tool search also behaves more reliably
      when agents need to recover the right context or capability.
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'openclaw memory status now shows an active light or REM dreaming phase
      instead of incorrectly reporting Dreaming: off , so operators can see that valid
      memory configurations are enabled. #93113 Related #67868 . Thanks @agentarclab,
      @mrossit.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Timed-out QMD memory searches now stop their background work when the
      agent moves on, preventing abandoned processes from continuing to consume CPU
      and memory. #93394 Thanks @alix-007.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Memory Wiki''s Stale Pages report now leaves durable concept and synthesis
      pages out of freshness warnings, keeping attention on source and entity pages
      that may actually need review. #94369 Thanks @sunnyshu0925, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Ollama memory search now respects a configured smaller embedding dimension
      and keeps indexes for different dimensions separate, avoiding incompatible vectors
      being mixed together. #94811 Thanks @mushuiyu886.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Memory searches and targeted refreshes now stay connected to the correct
      OpenClaw session even when transcript filenames change or QMD exports use a
      different name. #95087 Thanks @jalehman.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Windows users can now run QMD-backed memory indexing and search through
      configured absolute memory.qmd.command paths, including drive-letter and UNC
      locations, without OpenClaw stripping the path separators before launch. #95274
      Related #92302 . Thanks @ardooken, @ly85206559.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Saved session-memory summaries now leave out raw model tokens, tool-call
      blocks, media placeholders, role tags, and stale NO_REPLY markers so future
      conversations keep useful context. #95791 Thanks @sweetsophia, @vincentkoc,
      @yb0y.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'When memory_search is unavailable because the Node runtime lacks node:sqlite
      , OpenClaw now points users to a compatible runtime instead of sending them
      through unrelated embedding-provider troubleshooting. #95916 Thanks @rrrrrredy,
      @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: Windows memory-backed session syncing now keeps using the intended transcript
      file even when path formatting differs. b3b5b08 Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'When a model guesses the wrong tool name, Tool Search and Code Mode now
      show how to find and retry the correct tool, reducing the risk that long-running
      sessions get stuck or lose durable memory during compaction. #93374 Related
      #92273 . Thanks @mushuiyu886, @poison, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'OpenClaw memory features now keep active, reset, and deleted transcript
      coverage aligned with configured session stores and agent ownership, making
      dreaming, QMD exports, indexing, and sync less likely to miss or misattribute
      conversation history. #96162 Thanks @jalehman.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Memory-wiki status cards and bridge-backed source sync are less likely
      to fail during simultaneous page rewrites because OpenClaw now retries the transient
      path mismatch while still stopping unsafe or persistent filesystem writes. #94443
      Related #92134 . Thanks @cknzraposo, @zengwen-dt.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Memory Wiki now keeps user-written notes intact when an existing source
      page is re-ingested or synced, while still refreshing its generated content.
      #95614 Thanks @yetval.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'For operators using Active Memory with memory-core dreaming, nightly dreaming
      jobs no longer start unnecessary recall work and hit 45-second timeouts, while
      regular web chats continue to receive memory recall. #95721 Related #78500 .
      Thanks @vincentkoc, @vishutdhar, @xialonglee.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: Windows qmd-backed memory work now stops all related processes after availability
      probes and command timeouts, preventing qmd children from continuing to run
      in the background. 830691b
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'ClawHub skill discovery and install checks are less likely to stall or
      crash OpenClaw because oversized or stalled marketplace responses are now stopped
      before they can exhaust memory. #95226 Thanks @alix-007.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Long responses, busy tool streams, image-heavy requests, and memory recall
      now incur less CPU and filesystem overhead without requiring settings or workflow
      changes. #95697 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 26-memory-and-personalization-changes-in-v2026-6-11
  source_release: openclaw-2026-06-30-v2026-6-11-23cb95a9
  source_type: openclaw_changelog
  theme: memory
  title: 26 Memory and Personalization changes in v2026.6.11
  type: change
related_changes:
- '[[Changes/Claude Code/2026-06-22-improved-memory-the-agent-is-now-reminded-to-compact-its-memory-md-index-when-ne|Improved
  memory: the agent is now reminded to compact its MEMORY.md index…]]'
- '[[Changes/Kimi Code/2026-06-24-read-large-text-files-in-bounded-memory-and-read-tail-lines-without-scanning-who|Read
  large text files in bounded memory and read tail lines without scanning whole files]]'
- '[[Changes/Open WebUI/2026-06-29-5-memory-and-personalization-changes-in-v0-10-0|5
  Memory and Personalization changes in v0.10.0]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-06-30-v2026-6-11-23cb95a9|openclaw-2026-06-30-v2026-6-11-23cb95a9]]'
source_type: openclaw_changelog
theme: memory
title: 26 Memory and Personalization changes in v2026.6.11
type: change
---

<!-- chronolog:begin region="header" -->
# 26 Memory and Personalization changes in v2026.6.11

**OpenClaw** · 2026-06-30 · [[Themes/memory|Memory and Personalization]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.6.11) · from [[Releases/OpenClaw/openclaw-2026-06-30-v2026-6-11-23cb95a9|v2026.6.11]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Matrix E2EE gateways can stay online during long-running use instead of gradually consuming memory until a crash takes channels and in-flight work down. #94942 Related #90455 . Thanks @xzh-icenter, @yar-sh.

> Matrix users and operators now get a clear failure when a homeserver sends an oversized or stalled response, instead of OpenClaw continuing to buffer it and risking unbounded memory use. #95240 Thanks @alix-007.

> OpenClaw now rejects oversized provider catalog or JSON responses with a clear error before buffering the entire response in memory. #95218 Thanks @alix-007.

> Google-backed embedded-agent runs now stop reading oversized or never-ending prompt-cache responses before they can exhaust memory or leave the run stalled. #95417 Thanks @alix-007.

> OpenRouter model scans fail safely on oversized or malformed catalogs instead of risking excessive memory use that can destabilize OpenClaw. #95418 Thanks @alix-007.

> OpenRouter setups now reject oversized model catalogs before they can exhaust OpenClaw's memory, without caching or immediately refetching the failed response. #95420 Thanks @alix-007, @sallyom.

> Oversized or stalled provider catalogs now fail quickly with a clear error instead of hanging OpenClaw or consuming unbounded memory, while normal catalogs continue to load. #95827 Thanks @alix-007.

> OpenRouter model scans now accept the same larger valid catalogs as runtime discovery while still rejecting oversized responses before they can consume unbounded memory. ad3b2f4 Thanks @vincentkoc.

> Sessions , compaction , memory , and QMD-backed memory preserve the intended conversation and useful context more consistently through long-running work, reconnects, upgrades, and transcript repair. Tool search also behaves more reliably when agents need to recover the right context or capability.

> openclaw memory status now shows an active light or REM dreaming phase instead of incorrectly reporting Dreaming: off , so operators can see that valid memory configurations are enabled. #93113 Related #67868 . Thanks @agentarclab, @mrossit.

> Timed-out QMD memory searches now stop their background work when the agent moves on, preventing abandoned processes from continuing to consume CPU and memory. #93394 Thanks @alix-007.

> Memory Wiki's Stale Pages report now leaves durable concept and synthesis pages out of freshness warnings, keeping attention on source and entity pages that may actually need review. #94369 Thanks @sunnyshu0925, @vincentkoc.

> Ollama memory search now respects a configured smaller embedding dimension and keeps indexes for different dimensions separate, avoiding incompatible vectors being mixed together. #94811 Thanks @mushuiyu886.

> Memory searches and targeted refreshes now stay connected to the correct OpenClaw session even when transcript filenames change or QMD exports use a different name. #95087 Thanks @jalehman.

> Windows users can now run QMD-backed memory indexing and search through configured absolute memory.qmd.command paths, including drive-letter and UNC locations, without OpenClaw stripping the path separators before launch. #95274 Related #92302 . Thanks @ardooken, @ly85206559.

> Saved session-memory summaries now leave out raw model tokens, tool-call blocks, media placeholders, role tags, and stale NO_REPLY markers so future conversations keep useful context. #95791 Thanks @sweetsophia, @vincentkoc, @yb0y.

> When memory_search is unavailable because the Node runtime lacks node:sqlite , OpenClaw now points users to a compatible runtime instead of sending them through unrelated embedding-provider troubleshooting. #95916 Thanks @rrrrrredy, @vincentkoc.

> Windows memory-backed session syncing now keeps using the intended transcript file even when path formatting differs. b3b5b08 Thanks @vincentkoc.

> When a model guesses the wrong tool name, Tool Search and Code Mode now show how to find and retry the correct tool, reducing the risk that long-running sessions get stuck or lose durable memory during compaction. #93374 Related #92273 . Thanks @mushuiyu886, @poison, @vincentkoc.

> OpenClaw memory features now keep active, reset, and deleted transcript coverage aligned with configured session stores and agent ownership, making dreaming, QMD exports, indexing, and sync less likely to miss or misattribute conversation history. #96162 Thanks @jalehman.

> Memory-wiki status cards and bridge-backed source sync are less likely to fail during simultaneous page rewrites because OpenClaw now retries the transient path mismatch while still stopping unsafe or persistent filesystem writes. #94443 Related #92134 . Thanks @cknzraposo, @zengwen-dt.

> Memory Wiki now keeps user-written notes intact when an existing source page is re-ingested or synced, while still refreshing its generated content. #95614 Thanks @yetval.

> For operators using Active Memory with memory-core dreaming, nightly dreaming jobs no longer start unnecessary recall work and hit 45-second timeouts, while regular web chats continue to receive memory recall. #95721 Related #78500 . Thanks @vincentkoc, @vishutdhar, @xialonglee.

> Windows qmd-backed memory work now stops all related processes after availability probes and command timeouts, preventing qmd children from continuing to run in the background. 830691b

> ClawHub skill discovery and install checks are less likely to stall or crash OpenClaw because oversized or stalled marketplace responses are now stopped before they can exhaust memory. #95226 Thanks @alix-007.

> Long responses, busy tool streams, image-heavy requests, and memory recall now incur less CPU and filesystem overhead without requiring settings or workflow changes. #95697 Thanks @vincentkoc.

Source: https://docs.openclaw.ai/releases/2026.6.11
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-06-30-7-editor-experience-changes-in-v2026-6-11|7 Editor Experience changes in v2026.6.11]] · Editor Experience
- [[Changes/OpenClaw/2026-06-30-canvas-a2ui-now-serves-only-the-current-app-assets-after-each-build-so-outdated|Canvas A2UI now serves only the current app assets after each build, so outdated…]] · Files and Data
- [[Changes/OpenClaw/2026-06-30-word-powerpoint-and-excel-document-reads-and-writes-now-use-the-intended-docx-pp|Word, PowerPoint, and Excel document reads and writes now use the intended .docx…]] · Presentation Creation
- [[Changes/OpenClaw/2026-06-30-20-context-window-changes-in-v2026-6-11|20 Context Window changes in v2026.6.11]] · Context Window
- [[Changes/OpenClaw/2026-06-30-32-agent-mode-changes-in-v2026-6-11|32 Agent Mode changes in v2026.6.11]] · Agent Mode
- [[Changes/OpenClaw/2026-06-30-15-mobile-and-desktop-changes-in-v2026-6-11|15 Mobile and Desktop changes in v2026.6.11]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-06-30-5-collaboration-changes-in-v2026-6-11|5 Collaboration changes in v2026.6.11]] · Collaboration
- [[Changes/OpenClaw/2026-06-30-34-apps-and-integrations-changes-in-v2026-6-11|34 Apps and Integrations changes in v2026.6.11]] · Apps and Integrations
- [[Changes/OpenClaw/2026-06-30-6-voice-and-audio-changes-in-v2026-6-11|6 Voice and Audio changes in v2026.6.11]] · Voice and Audio
- [[Changes/OpenClaw/2026-06-30-32-model-support-changes-in-v2026-6-11|32 Model Support changes in v2026.6.11]] · Model Support
- [[Changes/OpenClaw/2026-06-30-qqbot-group-admins-can-choose-how-broadly-slash-commands-are-available-and-priva|QQBot group admins can choose how broadly slash commands are available…]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-06-30-4-reliability-and-performance-changes-in-v2026-6-11|4 Reliability and Performance changes in v2026.6.11]] · Reliability and Performance
- [[Changes/OpenClaw/2026-06-30-3-interface-experience-changes-in-v2026-6-11|3 Interface Experience changes in v2026.6.11]] · Interface Experience
- [[Changes/OpenClaw/2026-06-30-15-automation-and-scheduling-changes-in-v2026-6-11|15 Automation and Scheduling changes in v2026.6.11]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-06-30-when-a-codex-subscription-reaches-its-usage-limit-openclaw-now-moves-to-configur|When a Codex subscription reaches its usage limit, OpenClaw now moves to configured…]] · Pricing Model
- [[Changes/OpenClaw/2026-06-30-9-developer-workflow-changes-in-v2026-6-11|9 Developer Workflow changes in v2026.6.11]] · Developer Workflow
- [[Changes/OpenClaw/2026-06-30-6-safety-and-privacy-changes-in-v2026-6-11|6 Safety and Privacy changes in v2026.6.11]] · Safety and Privacy
- [[Changes/OpenClaw/2026-06-30-more-official-channel-provider-and-web-search-plugins-can-now-be-installed-or-re|More official channel, provider, and web-search plugins can now be installed…]] · Search and Browsing
- [[Changes/OpenClaw/2026-06-30-generated-images-from-a-remote-codex-app-server-now-arrive-as-attachments-instea|Generated images from a remote Codex app-server now arrive as attachments instead…]] · Image Generation
- [[Changes/OpenClaw/2026-06-30-background-image-video-and-music-results-now-return-to-the-chat-that-requested-t|Background image, video, and music results now return to the chat that requested…]] · Music Generation
- [[Changes/OpenClaw/2026-06-30-2-account-and-access-changes-in-v2026-6-11|2 Account and Access changes in v2026.6.11]] · Account and Access
- [[Changes/OpenClaw/2026-06-30-96-other-changes-in-v2026-6-11|96 other changes in v2026.6.11]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Memory and Personalization

- Earlier: 2026-06-29 · Open WebUI · [[Changes/Open WebUI/2026-06-29-5-memory-and-personalization-changes-in-v0-10-0|5 Memory and Personalization changes in v0.10.0]]
- Later: 2026-07-01 · Open WebUI · [[Changes/Open WebUI/2026-07-01-2-memory-and-personalization-changes-in-v0-10-2|2 Memory and Personalization changes in v0.10.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-06-30-54da95&body=Card%3A%20Changes%2FOpenClaw%2F2026-06-30-26-memory-and-personalization-changes-in-v2026-6-11.md%0ACard%20ID%3A%20openclaw-2026-06-30-54da95%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.6.11%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->