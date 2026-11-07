---
card_id: open-webui-2026-04-21-6f9b2e
date: '2026-04-21'
description: "Open WebUI · 2026-04-21 · Reliability and Performance: 24 changes in
  v0.9.0 — \U0001F3A7 **STT preprocessing bypass option.** Administrators can now
  enable…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-11-19-opening-projects-is-now-much-faster|Opening
    Projects is now much faster]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2710
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: c3a655c87d56743d9a1d9e5b1a6eb6d33d54abb68158da46c355dd0357e42524
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-04-21-6f9b2e
  comparison: ''
  date: '2026-04-21'
  description: 'Open WebUI — v0.9.0: 24 Reliability and Performance changes'
  evidence:
  - quote: "\U0001F3A7 **STT preprocessing bypass option.** Administrators can now
      enable \"AUDIO_STT_SKIP_PREPROCESSING\" to send audio files directly to the
      speech-to-text backend, reducing memory and CPU consumption during large uploads
      for better transcription performance and stability on constrained deployments.
      [#23661](https://github.com/open-webui/open-webui/pull/23661)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F39A️ **Active filter valve shortcut.** Active filter badges now
      expose valve configuration directly in the chat input area, so filter tuning
      is faster during conversations. [Commit](https://github.com/open-webui/open-webui/commit/3c22afc5a67404047797921185aca984b10b45cd),
      [#23811](https://github.com/open-webui/open-webui/issues/23811), [#23813](https://github.com/open-webui/open-webui/pull/23813)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F680 **Async performance and responsiveness improvements.** The
      core backend database and request paths now run asynchronously across the application,
      massively improving responsiveness and performance under concurrent load and
      reducing request blocking during heavy activity. [Commit](https://github.com/open-webui/open-webui/commit/27169124f220e5cea21c88601c731c3749496ab0),
      [Commit](https://github.com/open-webui/open-webui/commit/8936721414a17832852a90f3ee592af5a8b7232d)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F680 **Chat history memory culling.** Long conversations now stay
      responsive no matter how many messages they contain. Off-screen messages are
      unloaded automatically and reloaded as you scroll, keeping memory usage low
      and the UI smooth on both desktop and mobile. [#23067](https://github.com/open-webui/open-webui/issues/23067),
      [Commit](https://github.com/open-webui/open-webui/commit/026903399be73ac4b6c226647110e5662d043a50),
      [Commit](https://github.com/open-webui/open-webui/commit/9dccd29c94875e6f0ac373c5802cb183296e47ff)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F9F5 **Async file and knowledge processing performance.** File processing,
      knowledge reindexing, and channel message helper paths now consistently await
      async operations, preventing skipped processing steps and improving reliability
      and performance of indexing and tool responses. [Commit](https://github.com/open-webui/open-webui/commit/de27a121511a31606f250ba4033490797216a0eb)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F3CE️ **Streaming response performance.** Streaming responses now
      process each output line in a single step instead of two separate yields, reducing
      async overhead and improving responsiveness during long-running generations.
      [#23266](https://github.com/open-webui/open-webui/pull/23266)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F50E **Faster mention parsing.** Chat text with HTML-like content,
      file paths, or tool output now parses mentions more efficiently, which helps
      keep typing and rendering responsive in messages that contain many '<' characters.
      [#23551](https://github.com/open-webui/open-webui/pull/23551)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F9EA **Code block rendering performance.** Code blocks now reuse
      a shared HTML unescape helper, reducing extra browser work when displaying encoded
      output in chat. [#23553](https://github.com/open-webui/open-webui/pull/23553)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F39E️ **Streaming text token animation performance.** Streaming
      text tokens now use a lightweight CSS intro animation, making output feel smoother
      while reducing transition overhead and preventing tokens from fading out when
      generation completes. [#23257](https://github.com/open-webui/open-webui/pull/23257)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F52C **Chinese text processing guard performance.** Streaming responses
      without Chinese characters now skip unnecessary Chinese-format processing checks,
      reducing per-update overhead and keeping output smoother during rapid generation.
      [#23162](https://github.com/open-webui/open-webui/pull/23162)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F3F7️ **Chat title update performance.** Chat title updates now
      run in a single database operation instead of multiple round trips, improving
      responsiveness and reducing overhead when titles are generated or renamed. [#23214](https://github.com/open-webui/open-webui/pull/23214)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F4C2 **Faster chat list queries performance.** Chat and folder lists
      now load more efficiently by fetching only the fields needed for sidebar views,
      improving responsiveness when browsing large conversation histories. [Commit](https://github.com/open-webui/open-webui/commit/0e5696de74cc0ba55b24cfc3d02efa83f08d7d3f)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F4E1 **Optimized user activity tracking performance.** User activity
      updates now use a single database query instead of multiple operations, improving
      response times across all authenticated requests. [#23215](https://github.com/open-webui/open-webui/pull/23215)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F465 **Faster channel thread author loading.** Channel thread responses
      now load author details in a single batch query, reducing database overhead
      and improving responsiveness in threads with many participants. [#23795](https://github.com/open-webui/open-webui/pull/23795)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F5C3️ **Faster chat tag loading.** Chat tag lookups now load only
      the metadata needed instead of full chat payloads, improving responsiveness
      for chats with large histories. [#23798](https://github.com/open-webui/open-webui/pull/23798)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F4CE **Faster chat file deduplication.** Attaching files to chat
      messages now checks duplicates more efficiently, reducing overhead when handling
      larger file lists. [#23800](https://github.com/open-webui/open-webui/pull/23800)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F4C8 **Faster message diff checks.** Chat message and status updates
      now compare content more efficiently during streaming, making active conversations
      feel smoother and more responsive. [#23370](https://github.com/open-webui/open-webui/pull/23370)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: ⚖️ **Faster deep equality checks.** Chat message updates, model selection,
      note editing, code block refreshes, and rich text state comparisons now use
      deep equality checks that reduce unnecessary UI work and improve responsiveness
      in active sessions. [#23845](https://github.com/open-webui/open-webui/pull/23845)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F9F9 **Mermaid render cleanup performance.** Mermaid diagrams now
      always clean up temporary render elements after failures, reducing DOM buildup
      and keeping repeated rendering more stable over time. [#23727](https://github.com/open-webui/open-webui/pull/23727)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F6A6 **Faster startup performance.** Open WebUI now checks for Torch
      MPS support only on macOS, avoiding unnecessary startup work on other platforms.
      [#23438](https://github.com/open-webui/open-webui/pull/23438)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F6E1️ **Redis timeout consistency.** Redis connections now honor
      the \"REDIS_SOCKET_CONNECT_TIMEOUT\" setting across standard and cluster setups,
      helping workers fail faster when Redis is unreachable. [#23572](https://github.com/open-webui/open-webui/pull/23572)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F504 **General improvements.** Various improvements were implemented
      across the application to enhance performance, stability, and security."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F4CB **Clipboard copy scroll stability.** Copying content with the
      fallback clipboard method no longer triggers unwanted page scrolling during
      focus, keeping your current reading position stable. [Commit](https://github.com/open-webui/open-webui/commit/fc98000aa8d439bbff21a70370f5e962bf23f4bc)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F9E0 **Client session leak prevention.** Outbound provider requests
      now use a shared session pool with safer response cleanup and shutdown handling,
      preventing aiohttp session buildup and reducing memory growth during heavy concurrent
      API traffic. [#23540](https://github.com/open-webui/open-webui/issues/23540),
      [Commit](https://github.com/open-webui/open-webui/commit/c47dd7b7717c4186e0f0549ca3c8cb4d9bb38135)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 24-reliability-and-performance-changes-in-v0-9-0
  source_release: open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a
  source_type: github_releases
  theme: reliability-performance
  title: 24 Reliability and Performance changes in v0.9.0
  type: change
related_changes:
- '[[Changes/Windsurf/2026-04-17-various-bug-fixes-and-performance-improvements|Various
  bug fixes and performance improvements]]'
- '[[Changes/Claude Code/2026-04-20-resume-on-large-sessions-is-significantly-faster-up-to-67-on-40mb-sessions-and-h|/resume
  on large sessions is significantly faster (up to 67% on 40MB+ sessions)…]]'
- '[[Changes/Granola/2026-04-21-granola-chat-is-rebuilt-to-be-agentic-faster-across-your-notes-team-space-and-wh|Granola
  Chat just got smarter]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a|open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a]]'
source_type: github_releases
theme: reliability-performance
title: 24 Reliability and Performance changes in v0.9.0
type: change
---

<!-- chronolog:begin region="header" -->
# 24 Reliability and Performance changes in v0.9.0

**Open WebUI** · 2026-04-21 · [[Themes/reliability-performance|Reliability and Performance]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.0) · from [[Releases/Open WebUI/open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a|v0.9.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🎧 **STT preprocessing bypass option.** Administrators can now enable "AUDIO_STT_SKIP_PREPROCESSING" to send audio files directly to the speech-to-text backend, reducing memory and CPU consumption during large uploads for better transcription performance and stability on constrained deployments. [#23661](https://github.com/open-webui/open-webui/pull/23661)

> 🎚️ **Active filter valve shortcut.** Active filter badges now expose valve configuration directly in the chat input area, so filter tuning is faster during conversations. [Commit](https://github.com/open-webui/open-webui/commit/3c22afc5a67404047797921185aca984b10b45cd), [#23811](https://github.com/open-webui/open-webui/issues/23811), [#23813](https://github.com/open-webui/open-webui/pull/23813)

> 🚀 **Async performance and responsiveness improvements.** The core backend database and request paths now run asynchronously across the application, massively improving responsiveness and performance under concurrent load and reducing request blocking during heavy activity. [Commit](https://github.com/open-webui/open-webui/commit/27169124f220e5cea21c88601c731c3749496ab0), [Commit](https://github.com/open-webui/open-webui/commit/8936721414a17832852a90f3ee592af5a8b7232d)

> 🚀 **Chat history memory culling.** Long conversations now stay responsive no matter how many messages they contain. Off-screen messages are unloaded automatically and reloaded as you scroll, keeping memory usage low and the UI smooth on both desktop and mobile. [#23067](https://github.com/open-webui/open-webui/issues/23067), [Commit](https://github.com/open-webui/open-webui/commit/026903399be73ac4b6c226647110e5662d043a50), [Commit](https://github.com/open-webui/open-webui/commit/9dccd29c94875e6f0ac373c5802cb183296e47ff)

> 🧵 **Async file and knowledge processing performance.** File processing, knowledge reindexing, and channel message helper paths now consistently await async operations, preventing skipped processing steps and improving reliability and performance of indexing and tool responses. [Commit](https://github.com/open-webui/open-webui/commit/de27a121511a31606f250ba4033490797216a0eb)

> 🏎️ **Streaming response performance.** Streaming responses now process each output line in a single step instead of two separate yields, reducing async overhead and improving responsiveness during long-running generations. [#23266](https://github.com/open-webui/open-webui/pull/23266)

> 🔎 **Faster mention parsing.** Chat text with HTML-like content, file paths, or tool output now parses mentions more efficiently, which helps keep typing and rendering responsive in messages that contain many '<' characters. [#23551](https://github.com/open-webui/open-webui/pull/23551)

> 🧪 **Code block rendering performance.** Code blocks now reuse a shared HTML unescape helper, reducing extra browser work when displaying encoded output in chat. [#23553](https://github.com/open-webui/open-webui/pull/23553)

> 🎞️ **Streaming text token animation performance.** Streaming text tokens now use a lightweight CSS intro animation, making output feel smoother while reducing transition overhead and preventing tokens from fading out when generation completes. [#23257](https://github.com/open-webui/open-webui/pull/23257)

> 🔬 **Chinese text processing guard performance.** Streaming responses without Chinese characters now skip unnecessary Chinese-format processing checks, reducing per-update overhead and keeping output smoother during rapid generation. [#23162](https://github.com/open-webui/open-webui/pull/23162)

> 🏷️ **Chat title update performance.** Chat title updates now run in a single database operation instead of multiple round trips, improving responsiveness and reducing overhead when titles are generated or renamed. [#23214](https://github.com/open-webui/open-webui/pull/23214)

> 📂 **Faster chat list queries performance.** Chat and folder lists now load more efficiently by fetching only the fields needed for sidebar views, improving responsiveness when browsing large conversation histories. [Commit](https://github.com/open-webui/open-webui/commit/0e5696de74cc0ba55b24cfc3d02efa83f08d7d3f)

> 📡 **Optimized user activity tracking performance.** User activity updates now use a single database query instead of multiple operations, improving response times across all authenticated requests. [#23215](https://github.com/open-webui/open-webui/pull/23215)

> 👥 **Faster channel thread author loading.** Channel thread responses now load author details in a single batch query, reducing database overhead and improving responsiveness in threads with many participants. [#23795](https://github.com/open-webui/open-webui/pull/23795)

> 🗃️ **Faster chat tag loading.** Chat tag lookups now load only the metadata needed instead of full chat payloads, improving responsiveness for chats with large histories. [#23798](https://github.com/open-webui/open-webui/pull/23798)

> 📎 **Faster chat file deduplication.** Attaching files to chat messages now checks duplicates more efficiently, reducing overhead when handling larger file lists. [#23800](https://github.com/open-webui/open-webui/pull/23800)

> 📈 **Faster message diff checks.** Chat message and status updates now compare content more efficiently during streaming, making active conversations feel smoother and more responsive. [#23370](https://github.com/open-webui/open-webui/pull/23370)

> ⚖️ **Faster deep equality checks.** Chat message updates, model selection, note editing, code block refreshes, and rich text state comparisons now use deep equality checks that reduce unnecessary UI work and improve responsiveness in active sessions. [#23845](https://github.com/open-webui/open-webui/pull/23845)

> 🧹 **Mermaid render cleanup performance.** Mermaid diagrams now always clean up temporary render elements after failures, reducing DOM buildup and keeping repeated rendering more stable over time. [#23727](https://github.com/open-webui/open-webui/pull/23727)

> 🚦 **Faster startup performance.** Open WebUI now checks for Torch MPS support only on macOS, avoiding unnecessary startup work on other platforms. [#23438](https://github.com/open-webui/open-webui/pull/23438)

> 🛡️ **Redis timeout consistency.** Redis connections now honor the "REDIS_SOCKET_CONNECT_TIMEOUT" setting across standard and cluster setups, helping workers fail faster when Redis is unreachable. [#23572](https://github.com/open-webui/open-webui/pull/23572)

> 🔄 **General improvements.** Various improvements were implemented across the application to enhance performance, stability, and security.

> 📋 **Clipboard copy scroll stability.** Copying content with the fallback clipboard method no longer triggers unwanted page scrolling during focus, keeping your current reading position stable. [Commit](https://github.com/open-webui/open-webui/commit/fc98000aa8d439bbff21a70370f5e962bf23f4bc)

> 🧠 **Client session leak prevention.** Outbound provider requests now use a shared session pool with safer response cleanup and shutdown handling, preventing aiohttp session buildup and reducing memory growth during heavy concurrent API traffic. [#23540](https://github.com/open-webui/open-webui/issues/23540), [Commit](https://github.com/open-webui/open-webui/commit/c47dd7b7717c4186e0f0549ca3c8cb4d9bb38135)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-04-21-3-files-and-data-changes-in-v0-9-0|3 Files and Data changes in v0.9.0]] · Files and Data
- [[Changes/Open WebUI/2026-04-21-4-image-generation-changes-in-v0-9-0|4 Image Generation changes in v0.9.0]] · Image Generation
- [[Changes/Open WebUI/2026-04-21-28-model-support-changes-in-v0-9-0|28 Model Support changes in v0.9.0]] · Model Support
- [[Changes/Open WebUI/2026-04-21-5-editor-experience-changes-in-v0-9-0|5 Editor Experience changes in v0.9.0]] · Editor Experience
- [[Changes/Open WebUI/2026-04-21-persistent-chat-payload-efficiency-persisted-chats-now-use-server-side-history-l|🚀 Persistent chat payload efficiency. Persisted chats now use server-side…]] · Multimodal Input
- [[Changes/Open WebUI/2026-04-21-8-context-window-changes-in-v0-9-0|8 Context Window changes in v0.9.0]] · Context Window
- [[Changes/Open WebUI/2026-04-21-4-apps-and-integrations-changes-in-v0-9-0|4 Apps and Integrations changes in v0.9.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-04-21-46-developer-workflow-changes-in-v0-9-0|46 Developer Workflow changes in v0.9.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-04-21-8-automation-and-scheduling-changes-in-v0-9-0|8 Automation and Scheduling changes in v0.9.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-04-21-7-memory-and-personalization-changes-in-v0-9-0|7 Memory and Personalization changes in v0.9.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-04-21-2-mobile-and-desktop-changes-in-v0-9-0|2 Mobile and Desktop changes in v0.9.0]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-04-21-17-interface-experience-changes-in-v0-9-0|17 Interface Experience changes in v0.9.0]] · Interface Experience
- [[Changes/Open WebUI/2026-04-21-11-safety-and-privacy-changes-in-v0-9-0|11 Safety and Privacy changes in v0.9.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-04-21-4-search-and-browsing-changes-in-v0-9-0|4 Search and Browsing changes in v0.9.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-04-21-shared-chat-access-controls-you-can-now-control-who-has-access-to-a-shared-chat|🔗 Shared chat access controls. You can now control who has access to a shared…]] · Collaboration
- [[Changes/Open WebUI/2026-04-21-4-voice-and-audio-changes-in-v0-9-0|4 Voice and Audio changes in v0.9.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-04-21-17-account-and-access-changes-in-v0-9-0|17 Account and Access changes in v0.9.0]] · Account and Access
- [[Changes/Open WebUI/2026-04-21-21-other-changes-in-v0-9-0|21 other changes in v0.9.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2026-04-21 · Granola · [[Changes/Granola/2026-04-21-granola-chat-is-rebuilt-to-be-agentic-faster-across-your-notes-team-space-and-wh|Granola Chat just got smarter]]
- Later: 2026-04-22 · Claude Code · [[Changes/Claude Code/2026-04-22-2-reliability-and-performance-changes-in-v2-1-117|2 Reliability and Performance changes in v2.1.117]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-11-19 · Descript · [[Changes/Descript/2018-11-19-opening-projects-is-now-much-faster|Opening Projects is now much faster]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-04-21-6f9b2e&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-04-21-24-reliability-and-performance-changes-in-v0-9-0.md%0ACard%20ID%3A%20open-webui-2026-04-21-6f9b2e%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->