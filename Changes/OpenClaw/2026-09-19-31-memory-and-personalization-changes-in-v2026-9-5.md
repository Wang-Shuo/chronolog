---
card_id: openclaw-2026-09-19-859365
date: '2026-09-19'
description: 'OpenClaw · 2026-09-19 · Memory and Personalization: 31 changes in v2026.9.5
  — Once you agree on your new agent''s name and personality, setup can offer four…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1157
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: dacbc2621644e3eced4ef7e838dbaeba35aadbcd58680dd9973c2fcda5c927ba
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-19-859365
  comparison: ''
  date: '2026-09-19'
  description: 'OpenClaw — v2026.9.5: 31 Memory and Personalization changes'
  evidence:
  - quote: Once you agree on your new agent's name and personality, setup can offer
      four matching portraits and save the one you choose. You'll need an available
      image provider. You can skip this step and keep the emoji, which also lets setup
      continue if generation or saving fails. Existing avatars and completed workspaces
      stay unchanged.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Tool failures appear as a muted count beside collapsed activity, with full
      errors available when you expand it. Named operations keep their commands together,
      and plugin icons follow the current theme color. Background tasks use a compact,
      full-width feed with expandable commands, while the assistant’s reply keeps
      growing as one message. Saving conversation memory… now explains when that work
      is happening before a reply.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Minimize System busyness to keep CPU, diagnostics-request time, and process-memory
      graphs in a small widget while you work. Readings and history continue while
      minimized and return to the panel when you expand it. Closing stops the readings,
      and a lost connection shows Unavailable .
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: The widget’s ping measures the existing system.info request, separately
      from Settings’ connection ping. Neither measures model response time. The memory
      graph shows memory held by the Gateway process, known as resident memory or
      RSS.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Large conversation stores avoid repeated full scans when OpenClaw checks
      access to a session or reopens its database. The first check still reads the
      store, and the change adds some startup, memory, and write overhead.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Plugin cleanup failures now name the affected plugin and make stop or restart
      unsuccessful. A failed in-process restart exits with code 1 and starts no successor.
      Shared cleanup still finishes, and memory-only cleanup warnings remain nonfatal.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Large agent fleets avoid preparing chat metadata and Codex session locations
      for every agent before they are needed. Model preparation and multi-agent status
      scans give other Gateway requests more opportunities to run, while shared background
      workers reduce per-agent worker accumulation. These changes address specific
      sources of delay and memory growth; resource use still depends on the fleet.
      Parallel database checks can increase peak memory and disk activity, and keeping
      more authentication readers ready uses more open files.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Damage introduced after a file was checked may be detected by normal database
      access, the daily verifier, or explicit maintenance instead of the next reopen.
      Full integrity checkers use a larger temporary cache, with about 64 MiB more
      peak memory per active checker in the recorded measurement.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Profiles cover the main JavaScript runtime rather than all process memory
      or threads. Capture adds overhead and can take longer than requested if the
      Gateway stalls. Avoid competing profilers and review retained code symbols before
      sharing a profile. The results help investigate a problem; they do not repair
      it.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Interrupted memory rebuilds can reuse completed work, and large searches
      cause fewer pauses for other work in OpenClaw.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: With embedding caching enabled, a memory rebuild can reuse completed work
      after a retry or restart. The existing search index stays intact until its replacement
      succeeds. OpenClaw also repairs partially missing keyword indexes during normal
      initialization.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Forget removes a session's influence on memory ranking while keeping its
      source transcript. Forgetting a nonempty selection also clears that agent's
      entire embedding cache, so later indexing may make new provider requests. Unrelated
      published memories remain searchable.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Consolidated memories now keep the source links needed for Forget when
      a file replacement reports an error after writing, or its outcome is uncertain.
      Uncertain writes report an error without automatically appending another copy.
      This protects future Forget operations in that failure case; it does not recover
      source links lost before the fix.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: In affected multi-agent setups, memory_get now reads from the same agent
      workspace used by memory_search . If you intentionally want that agent to read
      the parent workspace, set an explicit workspace pin.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Memory search now has 30 seconds to run, up from 15, and that clock can
      pause while OpenClaw prepares the search. If it times out and the agent gives
      no final answer, a fallback reply explains what happened and counts any available
      keyword matches from memory files. These results remain incomplete and exclude
      conversation transcript matches that still need access checks.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Large memory searches and note preparation cause fewer pauses for other
      work in OpenClaw by running in the background. Control requests can also continue
      while large memory indexes are installed, though other database writes may still
      wait and indexing itself can take longer. Semantic search avoids a repeated-scan
      problem that could leave affected searches with only partial keyword results,
      without requiring a reindex.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Independent conversations can recall Active Memory at the same time when
      helper capacity is available. The existing subagent concurrency setting controls
      this separate shared limit, and busy periods can still cause timeouts. On the
      Codex path, recall follows the current request through prompt rebuilds instead
      of being triggered by an old memory question in the conversation history.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Memory Wiki reuses pages it has already parsed when searching, reading,
      and compiling your vault. OpenClaw can also find the Obsidian command when a
      folder with the same name appears earlier in the search path.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Embedding plugin authors can use the public SDK types for asynchronous
      text batches instead of importing internal memory types. Batches remain per-file
      by default; combining a whole source requires explicit opt-in through sourceWideBatchEmbed
      .
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Dreaming and manual promotion now check that the updated MEMORY.md fits
      the startup file limits of agents sharing the workspace. They use the smallest
      configured limit, up to the existing 10,000-character ceiling. Only memories
      actually saved are marked promoted or included in dream narratives. To make
      room, OpenClaw removes only recognized generated sections within the configured
      prior-entry loss allowance , 25% by default. User-written and ambiguous text
      is preserved.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: A full or oversized file can pause new promotions until consolidation,
      freed space, or changed limits let them fit. Candidates still follow normal
      eligibility and expiry rules, so retrying alone may not help. Existing oversized
      user-written text is not automatically trimmed. Dreaming reports also explain
      why candidates that reached promotion were not saved to long-term memory.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: The optional Omarchy 4 bar panel puts agents, sessions and quick prompts
      on your desktop, using the Linux app's Primary Gateway when available. Install
      it separately with a compatible app or CLI. Drafts stay in memory and are lost
      when the shell restarts, and uncertain sends are not retried automatically.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: During long ordinary-text replies through Completions, OpenClaw keeps less
      accumulated text in memory as the answer arrives. Completions and Responses
      also avoid repeated waits when a scheduled pause runs longer than expected.
      The reply text and cancellation checks stay intact. Processing time varies,
      and short replies can take longer.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Finishing cloud work can avoid repeatedly reading unchanged files, while
      changed files still receive the checks needed before their results are accepted.
      Large workspace scans also reuse temporary memory for file checks.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Large transfers and result checks now run expensive file calculations in
      the background so other requests can stay responsive. This can use more CPU
      and memory and does not necessarily shorten the transfer.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Repeated reloads also release more retired plugin state and reuse unchanged
      bundled setup code. Memory growth from native ESM modules remains unresolved,
      so long-running installations can still accumulate memory across reloads.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Passing large datasets to managed plugin tools uses less temporary memory
      and preparation work before execution. Existing object identities, shared references
      and cycles remain supported. The improvement concerns input preparation rather
      than total application memory.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Codex listings follow native activity recency and preserve conversations
      sharing the same timestamp. Browsing and search reuse already loaded session
      details, and valid saved listings can reopen while refreshing after a restart.
      Renames and successful archives update the catalog without another full scan;
      external changes may wait for background refresh. Older conversations remain
      accessible through native paging and search, which can take longer and return
      partial pages to continue. Very large native responses can still cause memory
      bursts.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: The tradeoff is more memory use and potentially longer waits for history.
      The warm background worker added about 270 MiB in the reported four-CPU Linux
      test. First reads can be slower, including after the worker shuts down while
      idle, and separate requests can use more CPU. Even small history pages can occasionally
      take longer to load.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Opening the branch list in a large saved conversation also uses a separate
      background worker, leaving the Gateway available for other requests. Incognito
      branch lists stay local. In a separate synthetic test, this worker added about
      105 MiB of process memory and took about 0.42 seconds for its first request.
      On Node, cold conversation-list scans also move off the Gateway thread, with
      possible extra startup time and memory use.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Plugin authors using worker pools should handle overload errors from the
      new queue limits. Rejected work is not retried automatically; check that the
      original request is still authorized and within its deadline before retrying.
      These limits cover queued work and reported input sizes, not total process memory.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 31-memory-and-personalization-changes-in-v2026-9-5
  source_release: openclaw-2026-09-19-v2026-9-5-506f537c
  source_type: openclaw_changelog
  theme: memory
  title: 31 Memory and Personalization changes in v2026.9.5
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-17-vscode-added-viewing-editing-and-deleting-a-saved-memory-inside-the-memory-dialo|VSCode
  Added viewing, editing and deleting a saved memory inside the Memory dialog]]'
- '[[Changes/Claude Code/2026-09-17-vscode-added-memory-and-instructions-entries-to-the-customize-menu-memory-shows|VSCode
  Added Memory and Instructions entries to the Customize menu]]'
- '[[Changes/Codex CLI/2026-09-17-7-memory-and-personalization-changes-in-rust-v0-155-0|7
  Memory and Personalization changes in rust-v0.155.0]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-19-v2026-9-5-506f537c|openclaw-2026-09-19-v2026-9-5-506f537c]]'
source_type: openclaw_changelog
theme: memory
title: 31 Memory and Personalization changes in v2026.9.5
type: change
---

<!-- chronolog:begin region="header" -->
# 31 Memory and Personalization changes in v2026.9.5

**OpenClaw** · 2026-09-19 · [[Themes/memory|Memory and Personalization]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.5) · from [[Releases/OpenClaw/openclaw-2026-09-19-v2026-9-5-506f537c|v2026.9.5]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Once you agree on your new agent's name and personality, setup can offer four matching portraits and save the one you choose. You'll need an available image provider. You can skip this step and keep the emoji, which also lets setup continue if generation or saving fails. Existing avatars and completed workspaces stay unchanged.

> Tool failures appear as a muted count beside collapsed activity, with full errors available when you expand it. Named operations keep their commands together, and plugin icons follow the current theme color. Background tasks use a compact, full-width feed with expandable commands, while the assistant’s reply keeps growing as one message. Saving conversation memory… now explains when that work is happening before a reply.

> Minimize System busyness to keep CPU, diagnostics-request time, and process-memory graphs in a small widget while you work. Readings and history continue while minimized and return to the panel when you expand it. Closing stops the readings, and a lost connection shows Unavailable .

> The widget’s ping measures the existing system.info request, separately from Settings’ connection ping. Neither measures model response time. The memory graph shows memory held by the Gateway process, known as resident memory or RSS.

> Large conversation stores avoid repeated full scans when OpenClaw checks access to a session or reopens its database. The first check still reads the store, and the change adds some startup, memory, and write overhead.

> Plugin cleanup failures now name the affected plugin and make stop or restart unsuccessful. A failed in-process restart exits with code 1 and starts no successor. Shared cleanup still finishes, and memory-only cleanup warnings remain nonfatal.

> Large agent fleets avoid preparing chat metadata and Codex session locations for every agent before they are needed. Model preparation and multi-agent status scans give other Gateway requests more opportunities to run, while shared background workers reduce per-agent worker accumulation. These changes address specific sources of delay and memory growth; resource use still depends on the fleet. Parallel database checks can increase peak memory and disk activity, and keeping more authentication readers ready uses more open files.

> Damage introduced after a file was checked may be detected by normal database access, the daily verifier, or explicit maintenance instead of the next reopen. Full integrity checkers use a larger temporary cache, with about 64 MiB more peak memory per active checker in the recorded measurement.

> Profiles cover the main JavaScript runtime rather than all process memory or threads. Capture adds overhead and can take longer than requested if the Gateway stalls. Avoid competing profilers and review retained code symbols before sharing a profile. The results help investigate a problem; they do not repair it.

> Interrupted memory rebuilds can reuse completed work, and large searches cause fewer pauses for other work in OpenClaw.

> With embedding caching enabled, a memory rebuild can reuse completed work after a retry or restart. The existing search index stays intact until its replacement succeeds. OpenClaw also repairs partially missing keyword indexes during normal initialization.

> Forget removes a session's influence on memory ranking while keeping its source transcript. Forgetting a nonempty selection also clears that agent's entire embedding cache, so later indexing may make new provider requests. Unrelated published memories remain searchable.

> Consolidated memories now keep the source links needed for Forget when a file replacement reports an error after writing, or its outcome is uncertain. Uncertain writes report an error without automatically appending another copy. This protects future Forget operations in that failure case; it does not recover source links lost before the fix.

> In affected multi-agent setups, memory_get now reads from the same agent workspace used by memory_search . If you intentionally want that agent to read the parent workspace, set an explicit workspace pin.

> Memory search now has 30 seconds to run, up from 15, and that clock can pause while OpenClaw prepares the search. If it times out and the agent gives no final answer, a fallback reply explains what happened and counts any available keyword matches from memory files. These results remain incomplete and exclude conversation transcript matches that still need access checks.

> Large memory searches and note preparation cause fewer pauses for other work in OpenClaw by running in the background. Control requests can also continue while large memory indexes are installed, though other database writes may still wait and indexing itself can take longer. Semantic search avoids a repeated-scan problem that could leave affected searches with only partial keyword results, without requiring a reindex.

> Independent conversations can recall Active Memory at the same time when helper capacity is available. The existing subagent concurrency setting controls this separate shared limit, and busy periods can still cause timeouts. On the Codex path, recall follows the current request through prompt rebuilds instead of being triggered by an old memory question in the conversation history.

> Memory Wiki reuses pages it has already parsed when searching, reading, and compiling your vault. OpenClaw can also find the Obsidian command when a folder with the same name appears earlier in the search path.

> Embedding plugin authors can use the public SDK types for asynchronous text batches instead of importing internal memory types. Batches remain per-file by default; combining a whole source requires explicit opt-in through sourceWideBatchEmbed .

> Dreaming and manual promotion now check that the updated MEMORY.md fits the startup file limits of agents sharing the workspace. They use the smallest configured limit, up to the existing 10,000-character ceiling. Only memories actually saved are marked promoted or included in dream narratives. To make room, OpenClaw removes only recognized generated sections within the configured prior-entry loss allowance , 25% by default. User-written and ambiguous text is preserved.

> A full or oversized file can pause new promotions until consolidation, freed space, or changed limits let them fit. Candidates still follow normal eligibility and expiry rules, so retrying alone may not help. Existing oversized user-written text is not automatically trimmed. Dreaming reports also explain why candidates that reached promotion were not saved to long-term memory.

> The optional Omarchy 4 bar panel puts agents, sessions and quick prompts on your desktop, using the Linux app's Primary Gateway when available. Install it separately with a compatible app or CLI. Drafts stay in memory and are lost when the shell restarts, and uncertain sends are not retried automatically.

> During long ordinary-text replies through Completions, OpenClaw keeps less accumulated text in memory as the answer arrives. Completions and Responses also avoid repeated waits when a scheduled pause runs longer than expected. The reply text and cancellation checks stay intact. Processing time varies, and short replies can take longer.

> Finishing cloud work can avoid repeatedly reading unchanged files, while changed files still receive the checks needed before their results are accepted. Large workspace scans also reuse temporary memory for file checks.

> Large transfers and result checks now run expensive file calculations in the background so other requests can stay responsive. This can use more CPU and memory and does not necessarily shorten the transfer.

> Repeated reloads also release more retired plugin state and reuse unchanged bundled setup code. Memory growth from native ESM modules remains unresolved, so long-running installations can still accumulate memory across reloads.

> Passing large datasets to managed plugin tools uses less temporary memory and preparation work before execution. Existing object identities, shared references and cycles remain supported. The improvement concerns input preparation rather than total application memory.

> Codex listings follow native activity recency and preserve conversations sharing the same timestamp. Browsing and search reuse already loaded session details, and valid saved listings can reopen while refreshing after a restart. Renames and successful archives update the catalog without another full scan; external changes may wait for background refresh. Older conversations remain accessible through native paging and search, which can take longer and return partial pages to continue. Very large native responses can still cause memory bursts.

> The tradeoff is more memory use and potentially longer waits for history. The warm background worker added about 270 MiB in the reported four-CPU Linux test. First reads can be slower, including after the worker shuts down while idle, and separate requests can use more CPU. Even small history pages can occasionally take longer to load.

> Opening the branch list in a large saved conversation also uses a separate background worker, leaving the Gateway available for other requests. Incognito branch lists stay local. In a separate synthetic test, this worker added about 105 MiB of process memory and took about 0.42 seconds for its first request. On Node, cold conversation-list scans also move off the Gateway thread, with possible extra startup time and memory use.

> Plugin authors using worker pools should handle overload errors from the new queue limits. Rejected work is not retried automatically; check that the original request is still authorized and within its deadline before retrying. These limits cover queued work and reported input sizes, not total process memory.

Source: https://docs.openclaw.ai/releases/2026.9.5
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-19-20-context-window-changes-in-v2026-9-5|20 Context Window changes in v2026.9.5]] · Context Window
- [[Changes/OpenClaw/2026-09-19-14-collaboration-changes-in-v2026-9-5|14 Collaboration changes in v2026.9.5]] · Collaboration
- [[Changes/OpenClaw/2026-09-19-the-browser-sidebar-gains-a-download-file-button-for-the-image-video-or-document|The Browser sidebar gains a Download file button for the image, video, or document…]] · Multimodal Input
- [[Changes/OpenClaw/2026-09-19-29-developer-workflow-changes-in-v2026-9-5|29 Developer Workflow changes in v2026.9.5]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-19-5-reliability-and-performance-changes-in-v2026-9-5|5 Reliability and Performance changes in v2026.9.5]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-19-retained-conversation-history-continues-to-follow-current-sharing-permissions-af|Retained conversation history continues to follow current sharing permissions after…]] · Projects and Workspaces
- [[Changes/OpenClaw/2026-09-19-2-enterprise-and-administration-changes-in-v2026-9-5|2 Enterprise and Administration changes in v2026.9.5]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-19-72-agent-mode-changes-in-v2026-9-5|72 Agent Mode changes in v2026.9.5]] · Agent Mode
- [[Changes/OpenClaw/2026-09-19-21-editor-experience-changes-in-v2026-9-5|21 Editor Experience changes in v2026.9.5]] · Editor Experience
- [[Changes/OpenClaw/2026-09-19-28-model-support-changes-in-v2026-9-5|28 Model Support changes in v2026.9.5]] · Model Support
- [[Changes/OpenClaw/2026-09-19-39-safety-and-privacy-changes-in-v2026-9-5|39 Safety and Privacy changes in v2026.9.5]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-19-14-automation-and-scheduling-changes-in-v2026-9-5|14 Automation and Scheduling changes in v2026.9.5]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-19-32-interface-experience-changes-in-v2026-9-5|32 Interface Experience changes in v2026.9.5]] · Interface Experience
- [[Changes/OpenClaw/2026-09-19-you-can-now-set-the-approval-reviewer-s-reasoning-and-optional-fast-mode-indepen|Set the approval reviewer's reasoning and optional Fast mode independently…]] · Agent Mode
- [[Changes/OpenClaw/2026-09-19-you-can-now-install-the-cli-on-freebsd-with-install-cli-sh-using-system-node-and|Install the CLI on FreeBSD with install-cli.sh using system Node and npm]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-19-6-pricing-model-changes-in-v2026-9-5|6 Pricing Model changes in v2026.9.5]] · Pricing Model
- [[Changes/OpenClaw/2026-09-19-28-account-and-access-changes-in-v2026-9-5|28 Account and Access changes in v2026.9.5]] · Account and Access
- [[Changes/OpenClaw/2026-09-19-you-can-now-ask-btw-side-questions-about-photos-attached-to-the-current-message|Ask /btw side questions about photos attached to the current message when using…]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-19-52-apps-and-integrations-changes-in-v2026-9-5|52 Apps and Integrations changes in v2026.9.5]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-19-23-mobile-and-desktop-changes-in-v2026-9-5|23 Mobile and Desktop changes in v2026.9.5]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-19-6-search-and-browsing-changes-in-v2026-9-5|6 Search and Browsing changes in v2026.9.5]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-19-video-generation-preserves-repeated-reference-positions-so-the-same-image-can-se|Video generation preserves repeated reference positions, so the same image can serve…]] · Music Generation
- [[Changes/OpenClaw/2026-09-19-browser-pages-appear-directly-in-the-chat-panel-header-leaving-more-room-for-the|Browser pages appear directly in the Chat panel header, leaving more room for the page]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-09-19-7-files-and-data-changes-in-v2026-9-5|7 Files and Data changes in v2026.9.5]] · Files and Data
- [[Changes/OpenClaw/2026-09-19-15-voice-and-audio-changes-in-v2026-9-5|15 Voice and Audio changes in v2026.9.5]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-19-shared-helpers-consolidate-repeated-implementation-including-preparation-and-res|Shared helpers consolidate repeated implementation, including preparation…]] · Video Generation
- [[Changes/OpenClaw/2026-09-19-171-other-changes-in-v2026-9-5|171 other changes in v2026.9.5]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Memory and Personalization

- Earlier: 2026-09-17 · Codex CLI · [[Changes/Codex CLI/2026-09-17-7-memory-and-personalization-changes-in-rust-v0-155-0|7 Memory and Personalization changes in rust-v0.155.0]]
- Later: 2026-09-21 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-09-21-tear-down-the-processes-an-internal-git-command-started-when-it-times-out-so-a-s|Tear down the processes an internal git command started when it times out, so a slow…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-19-859365&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-19-31-memory-and-personalization-changes-in-v2026-9-5.md%0ACard%20ID%3A%20openclaw-2026-09-19-859365%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.5%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->