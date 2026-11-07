---
card_id: open-webui-2026-03-01-2cb1a4
date: '2026-03-01'
description: "Open WebUI · 2026-03-01 · Reliability and Performance: 21 changes in
  v0.8.6 — \U0001F4A8 **Streaming performance.** Chat responses now render more efficiently
  during…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General
    performance: Among other improvements, users will notice that ChatGPT is now…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1172
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 7ad37f0e6a87407bc3b5d4da52fcbf1aa30cf5da8d2a23e55c2cc46ff7d20ef8
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-03-01-2cb1a4
  comparison: ''
  date: '2026-03-01'
  description: 'Open WebUI — v0.8.6: 21 Reliability and Performance changes'
  evidence:
  - quote: "\U0001F4A8 **Streaming performance.** Chat responses now render more efficiently
      during streaming, reducing CPU usage and improving responsiveness. [Commit](https://github.com/open-webui/open-webui/commit/484ba91b0777042eb848134f206ef3921f968dea)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  - quote: "\U0001F9EE **Streaming message comparison.** Chat message updates during
      streaming are now faster thanks to an optimization that skips expensive comparisons
      when content changes. [#21884](https://github.com/open-webui/open-webui/pull/21884)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  - quote: "\U0001F680 **Streaming scroll optimization.** Chat auto-scroll during
      streaming is now more efficient by batching scroll operations via requestAnimationFrame,
      reducing unnecessary layout reflows when tokens arrive faster than the browser
      can paint. [#21946](https://github.com/open-webui/open-webui/pull/21946)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  - quote: "\U0001F4CB **Message cloning performance.** Chat message cloning during
      streaming is now more efficient thanks to the use of structuredClone() instead
      of JSON.parse(JSON.stringify(...)). [#21948](https://github.com/open-webui/open-webui/pull/21948)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  - quote: "\U0001F3AF **Faster code block rendering.** Chat message updates during
      streaming are now faster. [#22101](https://github.com/open-webui/open-webui/pull/22101)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  - quote: "\U0001F4CA **Faster status history display.** Chat message updates during
      streaming are now faster. [#22103](https://github.com/open-webui/open-webui/pull/22103)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  - quote: "\U0001F6E0️ **Faster tool result handling.** Tool execution results are
      now handled more efficiently, improving streaming performance. [#22104](https://github.com/open-webui/open-webui/pull/22104)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  - quote: "\U0001F527 **Faster tool loading.** Tool access control now skips an unnecessary
      database query when no tools are attached to the request, slightly improving
      performance. [#21873](https://github.com/open-webui/open-webui/pull/21873)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  - quote: ➗ **Faster math rendering.** Mathematical notation now renders more efficiently,
      improving responsiveness when displaying equations in chat. [#21880](https://github.com/open-webui/open-webui/pull/21880)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  - quote: "\U0001F3CE️ **Faster message list updates.** The chat message list now
      rebuilds at most once per animation frame during streaming, reducing CPU overhead.
      [#21885](https://github.com/open-webui/open-webui/pull/21885)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  - quote: "\U0001F4CB **Faster message rendering.** Chat message rendering is now
      more efficient during streaming. [#22086](https://github.com/open-webui/open-webui/pull/22086)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  - quote: "\U0001F5C4️ **Faster real-time chat updates.** Chat responses now process
      faster with improved handling for concurrent users. [#22087](https://github.com/open-webui/open-webui/pull/22087)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  - quote: "\U0001F4DD **Faster status persistence.** Only final status updates are
      now saved to the database during streaming, reducing unnecessary writes. [#22085](https://github.com/open-webui/open-webui/pull/22085)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  - quote: "\U0001F504 **Faster event matching.** Event handling in the socket handler
      is now more efficient. [Commit](https://github.com/open-webui/open-webui/commit/ff86283be0479ccb86b639926b2b67ccbbe78746)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  - quote: "\U0001F500 **General improvements.** Various improvements were implemented
      across the application to enhance performance, stability, and security."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  - quote: "\U0001F9F9 **Tooltip memory leak.** Tooltip instances are now properly
      destroyed when elements change, fixing a memory leak that could cause performance
      issues over time. [#21969](https://github.com/open-webui/open-webui/pull/21969)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  - quote: ⌨️ **MessageInput memory leak.** Event listeners in the message input component
      are now properly cleaned up, preventing a memory leak that could cause page
      crashes during extended use. [#21968](https://github.com/open-webui/open-webui/pull/21968)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  - quote: "\U0001F4DD **Notes memory leak.** Event listeners in the Notes component
      are now properly cleaned up, fixing a memory leak that could cause page crashes
      during extended use. [#21963](https://github.com/open-webui/open-webui/pull/21963)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  - quote: "\U0001F3D7️ **Model create memory leak.** Event listeners in the model
      creation page are now properly cleaned up, fixing a memory leak that could cause
      page crashes during extended use. [#21966](https://github.com/open-webui/open-webui/pull/21966)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  - quote: "\U0001F4AC **MentionList memory leak.** Event listeners in the MentionList
      component are now properly cleaned up, fixing a memory leak that could cause
      page crashes during extended use. [#21965](https://github.com/open-webui/open-webui/pull/21965)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  - quote: "\U0001F4D0 **Sidebar memory leak.** Event listeners in the Sidebar component
      are now properly cleaned up, fixing a memory leak that could cause page crashes
      during extended use. [#22082](https://github.com/open-webui/open-webui/pull/22082)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 21-reliability-and-performance-changes-in-v0-8-6
  source_release: open-webui-2026-03-01-v0-8-6-github-291846033-263bca05
  source_type: github_releases
  theme: reliability-performance
  title: 21 Reliability and Performance changes in v0.8.6
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-02-27-faster-sharing-sharing-chats-is-now-easier-and-faster-with-a-quicker-loading-sha|Faster
  sharing. Sharing chats is now easier and faster, with a quicker-loading share menu]]'
- '[[Changes/Replit/2026-02-27-agent-performance-improvements|Agent performance improvements]]'
- '[[Changes/Claude Code/2026-02-28-improved-memory-usage-in-long-sessions-with-subagents-by-stripping-heavy-progres|Improved
  memory usage in long sessions with subagents by stripping heavy progress…]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-03-01-v0-8-6-github-291846033-263bca05|open-webui-2026-03-01-v0-8-6-github-291846033-263bca05]]'
source_type: github_releases
theme: reliability-performance
title: 21 Reliability and Performance changes in v0.8.6
type: change
---

<!-- chronolog:begin region="header" -->
# 21 Reliability and Performance changes in v0.8.6

**Open WebUI** · 2026-03-01 · [[Themes/reliability-performance|Reliability and Performance]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.6) · from [[Releases/Open WebUI/open-webui-2026-03-01-v0-8-6-github-291846033-263bca05|v0.8.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 💨 **Streaming performance.** Chat responses now render more efficiently during streaming, reducing CPU usage and improving responsiveness. [Commit](https://github.com/open-webui/open-webui/commit/484ba91b0777042eb848134f206ef3921f968dea)

> 🧮 **Streaming message comparison.** Chat message updates during streaming are now faster thanks to an optimization that skips expensive comparisons when content changes. [#21884](https://github.com/open-webui/open-webui/pull/21884)

> 🚀 **Streaming scroll optimization.** Chat auto-scroll during streaming is now more efficient by batching scroll operations via requestAnimationFrame, reducing unnecessary layout reflows when tokens arrive faster than the browser can paint. [#21946](https://github.com/open-webui/open-webui/pull/21946)

> 📋 **Message cloning performance.** Chat message cloning during streaming is now more efficient thanks to the use of structuredClone() instead of JSON.parse(JSON.stringify(...)). [#21948](https://github.com/open-webui/open-webui/pull/21948)

> 🎯 **Faster code block rendering.** Chat message updates during streaming are now faster. [#22101](https://github.com/open-webui/open-webui/pull/22101)

> 📊 **Faster status history display.** Chat message updates during streaming are now faster. [#22103](https://github.com/open-webui/open-webui/pull/22103)

> 🛠️ **Faster tool result handling.** Tool execution results are now handled more efficiently, improving streaming performance. [#22104](https://github.com/open-webui/open-webui/pull/22104)

> 🔧 **Faster tool loading.** Tool access control now skips an unnecessary database query when no tools are attached to the request, slightly improving performance. [#21873](https://github.com/open-webui/open-webui/pull/21873)

> ➗ **Faster math rendering.** Mathematical notation now renders more efficiently, improving responsiveness when displaying equations in chat. [#21880](https://github.com/open-webui/open-webui/pull/21880)

> 🏎️ **Faster message list updates.** The chat message list now rebuilds at most once per animation frame during streaming, reducing CPU overhead. [#21885](https://github.com/open-webui/open-webui/pull/21885)

> 📋 **Faster message rendering.** Chat message rendering is now more efficient during streaming. [#22086](https://github.com/open-webui/open-webui/pull/22086)

> 🗄️ **Faster real-time chat updates.** Chat responses now process faster with improved handling for concurrent users. [#22087](https://github.com/open-webui/open-webui/pull/22087)

> 📝 **Faster status persistence.** Only final status updates are now saved to the database during streaming, reducing unnecessary writes. [#22085](https://github.com/open-webui/open-webui/pull/22085)

> 🔄 **Faster event matching.** Event handling in the socket handler is now more efficient. [Commit](https://github.com/open-webui/open-webui/commit/ff86283be0479ccb86b639926b2b67ccbbe78746)

> 🔀 **General improvements.** Various improvements were implemented across the application to enhance performance, stability, and security.

> 🧹 **Tooltip memory leak.** Tooltip instances are now properly destroyed when elements change, fixing a memory leak that could cause performance issues over time. [#21969](https://github.com/open-webui/open-webui/pull/21969)

> ⌨️ **MessageInput memory leak.** Event listeners in the message input component are now properly cleaned up, preventing a memory leak that could cause page crashes during extended use. [#21968](https://github.com/open-webui/open-webui/pull/21968)

> 📝 **Notes memory leak.** Event listeners in the Notes component are now properly cleaned up, fixing a memory leak that could cause page crashes during extended use. [#21963](https://github.com/open-webui/open-webui/pull/21963)

> 🏗️ **Model create memory leak.** Event listeners in the model creation page are now properly cleaned up, fixing a memory leak that could cause page crashes during extended use. [#21966](https://github.com/open-webui/open-webui/pull/21966)

> 💬 **MentionList memory leak.** Event listeners in the MentionList component are now properly cleaned up, fixing a memory leak that could cause page crashes during extended use. [#21965](https://github.com/open-webui/open-webui/pull/21965)

> 📐 **Sidebar memory leak.** Event listeners in the Sidebar component are now properly cleaned up, fixing a memory leak that could cause page crashes during extended use. [#22082](https://github.com/open-webui/open-webui/pull/22082)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-03-01-2-search-and-browsing-changes-in-v0-8-6|2 Search and Browsing changes in v0.8.6]] · Search and Browsing
- [[Changes/Open WebUI/2026-03-01-oauth-session-token-decryption-oauth-sessions-are-now-properly-detached-from-the|🔓 OAuth session token decryption. OAuth sessions are now properly detached…]] · Context Window
- [[Changes/Open WebUI/2026-03-01-individual-user-sharing-control-administrators-can-now-disable-individual-user-s|🔐 Individual user sharing control. Administrators can now disable individual…]] · Collaboration
- [[Changes/Open WebUI/2026-03-01-4-interface-experience-changes-in-v0-8-6|4 Interface Experience changes in v0.8.6]] · Interface Experience
- [[Changes/Open WebUI/2026-03-01-3-account-and-access-changes-in-v0-8-6|3 Account and Access changes in v0.8.6]] · Account and Access
- [[Changes/Open WebUI/2026-03-01-4-safety-and-privacy-changes-in-v0-8-6|4 Safety and Privacy changes in v0.8.6]] · Safety and Privacy
- [[Changes/Open WebUI/2026-03-01-8-model-support-changes-in-v0-8-6|8 Model Support changes in v0.8.6]] · Model Support
- [[Changes/Open WebUI/2026-03-01-9-developer-workflow-changes-in-v0-8-6|9 Developer Workflow changes in v0.8.6]] · Developer Workflow
- [[Changes/Open WebUI/2026-03-01-6-other-changes-in-v0-8-6|6 other changes in v0.8.6]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2026-02-28 · Claude Code · [[Changes/Claude Code/2026-02-28-improved-memory-usage-in-long-sessions-with-subagents-by-stripping-heavy-progres|Improved memory usage in long sessions with subagents by stripping heavy progress…]]
- Later: 2026-03-02 · Ollama · [[Changes/Ollama/2026-03-02-ollama-run-verbose-will-now-show-peak-memory-usage-when-using-ollama-s-mlx-engin|ollama run --verbose will now show peak memory usage when using Ollama's MLX engine]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General performance: Among other improvements, users will notice that ChatGPT is now…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-03-01-2cb1a4&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-03-01-21-reliability-and-performance-changes-in-v0-8-6.md%0ACard%20ID%3A%20open-webui-2026-03-01-2cb1a4%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.6%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->