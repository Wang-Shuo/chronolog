---
card_id: openclaw-2026-09-23-b49b94
date: '2026-09-23'
description: 'OpenClaw · 2026-09-23 · Memory and Personalization: 23 changes in v2026.9.6
  — New-session placement makes the cloud profile, operating system, machine size
  and…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1161
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 268229483f00cb4349e7fe036d75ae9fff5b989f023f66301a397bb0f77f7c46
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-23-b49b94
  comparison: ''
  date: '2026-09-23'
  description: 'OpenClaw — v2026.9.6: 23 Memory and Personalization changes'
  evidence:
  - quote: New-session placement makes the cloud profile, operating system, machine
      size and starting branch easier to confirm, and submits the choices shown in
      the picker. Your prompt and attachments remain visible beside startup progress
      while the first message waits for the destination to become active. Open session
      returns to a created conversation without sending the prompt again. Configured
      size defaults still apply and existing instances are not resized. Administrators
      can also register an existing repository using an accessible absolute path with
      a valid Git HEAD. Interrupted Incognito prompts remain only in the current tab's
      memory.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Incognito links now retain the exact conversation, provided you have administrator
      access and its memory-only session still exists. Reopen it from the sidebar
      to replace an older broken short link.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: If Pause, Resume, Clear or editing a Goal returns an uncertain result,
      Check outcome lets you check the original action without repeating completed
      work, even after reconnecting or reloading a normal chat. Recovery is explicit
      and requires browser tab storage for normal chats, while Incognito recovery
      remains in memory. Saved requests expire after 24 hours, after which Review
      current goal refreshes the current state before your next decision. The Goal
      controls guide explains the recovery flow.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Systems offers a compact machine list with sorting and online or offline
      filters, plus recent load, memory and volume free-space graphs for the selected
      machine. History accumulates while Systems is open and resets after reconnects
      or gaps, so it is a recent view rather than a stored monitoring history. Connected
      nodes report their home volume, and load should not be read as CPU utilization.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Saved agent history now uses selective lossless compression, and memory
      vectors keep their full precision in a more compact binary form. Search maintenance
      can find the rows belonging to a conversation without scanning unrelated history.
      Existing database files may not immediately shrink, and reading or appending
      full conversation bodies can take more CPU. Valid vector conversion happens
      locally without an embedding-provider call.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Eligible same-version clean restarts reuse completed database verification,
      and startup loads fewer unused dependencies. Memory, document and Codex workers
      also start with less overhead, while concurrent Windows UI preparation can reuse
      fully verified assets. Upgrades, unclean shutdowns, replaced files and migrations
      still require full checks; damage within the same file may be found after readiness,
      so a quick restart is not a fresh integrity certificate.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Memory search and maintenance can recover from more interruptions, helping
      saved information stay useful as conversations continue.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: When an embedding failure interrupts a compatible index upgrade, you can
      still find previously indexed memories by keyword. This fallback searches the
      old index, so it may miss later edits and leaves meaning-based search and the
      rebuild unavailable until the embedding problem is resolved. Changes to the
      indexed sources or incompatible index history can still prevent fallback. Repeated
      empty searches also avoid rebuilding an unchanged empty index, and memory status
      shows the configured local embedding model before loading it.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Memory settings no longer flag a loaded plugin as unhealthy just because
      it provides memory through another integration instead of host search. Actual
      loading and search failures remain visible, and this status does not certify
      the plugin's own service. Built-in searches also do less database work on the
      thread handling replies, although the searches themselves may take longer.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: History and search indexes can catch up while a conversation continues
      receiving messages, within a bounded amount of new history. Resets, branches,
      and larger backlogs still need a fresh rebuild. Completed memory saves keep
      their successful result if cleanup later fails, and the next sync can recover
      a lock left by completed local work instead of timing out. Recovery checks the
      original lock and database so it leaves active work and replacement locks alone.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Memory rebuilds also avoid a false “owner changed” failure when database
      commands wait in a queue. Genuine revocation or replacement still stops the
      affected work.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Generated reflections stay searchable but no longer compete with ordinary
      memories in promotion rankings for long-term memory, while existing long-term
      memories remain unchanged.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Memory Forget keeps track of memories already selected for deletion and
      picks up new links to the selected sessions while preparing the operation, preserving
      unrelated content. A preview remains a view of the current state, so pause or
      coordinate direct agent edits and external writers during a sensitive purge.
      This repair covers changing session links without extending deletion to every
      possible copy of the information.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Workspace adapters can now provide access to Memory files on a remote host
      for searching, reading, and maintenance, while the computer running OpenClaw
      keeps the index and original session data. This optional workspace capability
      requires a separately configured memoryFiles adapter and does not move existing
      storage automatically.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: After changing which source files the adapter uses, run openclaw memory
      index --force --agent <id> before searching. Keep the workspace binding unchanged
      during maintenance. Revoking access does not retract results already read or
      retained, and embedding requests or multi-step diary updates may continue after
      their original access checks.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Task tracking, maintenance, and flow reports do less repeated storage work
      while preserving newer progress, deletions, delivery details, and late results.
      Maintenance can continue around unsettled tasks, and restored or retried workflows
      show their committed status even when a background worker’s reply is delayed.
      Large task flows can also enter a waiting state without redundant result copies
      exhausting the worker’s memory. Individual requests can still wait for storage,
      and queued events become durable only when saved.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: The GitHub reader keeps source discussions beside your chat, remote workspaces
      connect that conversation to files, Memory, and Skills on another computer,
      and live meeting notes let you follow a capture before it ends.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: You can send uploaded files to the computer where an agent’s workspace
      lives and receive its finished files back in chat, with Memory files and supported
      workspace Skills available on that same computer. This requires an explicitly
      configured host integration, current file and command grants, and matching OpenClaw
      versions on the Gateway and paired node. Workspace Skills can be discovered,
      read, watched, and have their dependencies installed there; remote Skill source
      installation, updates, removal, and ClawHub management remain unsupported.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Transfers default to 50 MiB per file, and uploads hold the admitted file
      in memory. If an enabled upload fails, the turn does not start without its file;
      missing or denied output files fail explicitly instead of returning stale local
      copies. Remove saved file.create grants before downgrading to an older version.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: OpenClaw avoids some repeated local cleanup and rendering while receiving
      long replies containing comparison text or final-answer tags. The benefit depends
      on the reply, and the final-answer path can use more peak memory while reducing
      repeated processing.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Repeated conversation and state reads reuse eligible database connections
      and workers instead of repeatedly opening them. Healthy reusable resources can
      stay available for 30 idle minutes, reducing setup during intermittent activity
      while reads continue to see current data. Larger active installations can consequently
      retain more memory and open file handles during that window.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Bursts of conversation writes leave more opportunities for other work to
      proceed, and saving large replies or tool results shortens the time other writers
      can be held up. Small requests arriving during startup or reconnect can wait
      up to 10 seconds for capacity instead of failing immediately, while memory and
      oversized-request limits still apply. Lookups through large task and conversation
      histories also inspect fewer unrelated records.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Memory file watching is separated from indexing, and diagnostics and search-result
      preparation reuse existing information. This is maintenance of the current Memory
      implementation.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 23-memory-and-personalization-changes-in-v2026-9-6
  source_release: openclaw-2026-09-23-v2026-9-6-3f12c824
  source_type: openclaw_changelog
  theme: memory
  title: 23 Memory and Personalization changes in v2026.9.6
  type: change
related_changes:
- '[[Changes/Open WebUI/2026-09-21-6-memory-and-personalization-changes-in-v0-11-4|6
  Memory and Personalization changes in v0.11.4]]'
- '[[Changes/Codex CLI/2026-09-22-6-memory-and-personalization-changes-in-rust-v0-156-0|6
  Memory and Personalization changes in rust-v0.156.0]]'
- '[[Changes/GitHub Copilot CLI/2026-09-22-resuming-large-local-sessions-keeps-transcript-memory-bounded-for-smoother-cli-p|Resuming
  large local sessions keeps transcript memory bounded for smoother CLI performance]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-23-v2026-9-6-3f12c824|openclaw-2026-09-23-v2026-9-6-3f12c824]]'
source_type: openclaw_changelog
theme: memory
title: 23 Memory and Personalization changes in v2026.9.6
type: change
---

<!-- chronolog:begin region="header" -->
# 23 Memory and Personalization changes in v2026.9.6

**OpenClaw** · 2026-09-23 · [[Themes/memory|Memory and Personalization]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.6) · from [[Releases/OpenClaw/openclaw-2026-09-23-v2026-9-6-3f12c824|v2026.9.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> New-session placement makes the cloud profile, operating system, machine size and starting branch easier to confirm, and submits the choices shown in the picker. Your prompt and attachments remain visible beside startup progress while the first message waits for the destination to become active. Open session returns to a created conversation without sending the prompt again. Configured size defaults still apply and existing instances are not resized. Administrators can also register an existing repository using an accessible absolute path with a valid Git HEAD. Interrupted Incognito prompts remain only in the current tab's memory.

> Incognito links now retain the exact conversation, provided you have administrator access and its memory-only session still exists. Reopen it from the sidebar to replace an older broken short link.

> If Pause, Resume, Clear or editing a Goal returns an uncertain result, Check outcome lets you check the original action without repeating completed work, even after reconnecting or reloading a normal chat. Recovery is explicit and requires browser tab storage for normal chats, while Incognito recovery remains in memory. Saved requests expire after 24 hours, after which Review current goal refreshes the current state before your next decision. The Goal controls guide explains the recovery flow.

> Systems offers a compact machine list with sorting and online or offline filters, plus recent load, memory and volume free-space graphs for the selected machine. History accumulates while Systems is open and resets after reconnects or gaps, so it is a recent view rather than a stored monitoring history. Connected nodes report their home volume, and load should not be read as CPU utilization.

> Saved agent history now uses selective lossless compression, and memory vectors keep their full precision in a more compact binary form. Search maintenance can find the rows belonging to a conversation without scanning unrelated history. Existing database files may not immediately shrink, and reading or appending full conversation bodies can take more CPU. Valid vector conversion happens locally without an embedding-provider call.

> Eligible same-version clean restarts reuse completed database verification, and startup loads fewer unused dependencies. Memory, document and Codex workers also start with less overhead, while concurrent Windows UI preparation can reuse fully verified assets. Upgrades, unclean shutdowns, replaced files and migrations still require full checks; damage within the same file may be found after readiness, so a quick restart is not a fresh integrity certificate.

> Memory search and maintenance can recover from more interruptions, helping saved information stay useful as conversations continue.

> When an embedding failure interrupts a compatible index upgrade, you can still find previously indexed memories by keyword. This fallback searches the old index, so it may miss later edits and leaves meaning-based search and the rebuild unavailable until the embedding problem is resolved. Changes to the indexed sources or incompatible index history can still prevent fallback. Repeated empty searches also avoid rebuilding an unchanged empty index, and memory status shows the configured local embedding model before loading it.

> Memory settings no longer flag a loaded plugin as unhealthy just because it provides memory through another integration instead of host search. Actual loading and search failures remain visible, and this status does not certify the plugin's own service. Built-in searches also do less database work on the thread handling replies, although the searches themselves may take longer.

> History and search indexes can catch up while a conversation continues receiving messages, within a bounded amount of new history. Resets, branches, and larger backlogs still need a fresh rebuild. Completed memory saves keep their successful result if cleanup later fails, and the next sync can recover a lock left by completed local work instead of timing out. Recovery checks the original lock and database so it leaves active work and replacement locks alone.

> Memory rebuilds also avoid a false “owner changed” failure when database commands wait in a queue. Genuine revocation or replacement still stops the affected work.

> Generated reflections stay searchable but no longer compete with ordinary memories in promotion rankings for long-term memory, while existing long-term memories remain unchanged.

> Memory Forget keeps track of memories already selected for deletion and picks up new links to the selected sessions while preparing the operation, preserving unrelated content. A preview remains a view of the current state, so pause or coordinate direct agent edits and external writers during a sensitive purge. This repair covers changing session links without extending deletion to every possible copy of the information.

> Workspace adapters can now provide access to Memory files on a remote host for searching, reading, and maintenance, while the computer running OpenClaw keeps the index and original session data. This optional workspace capability requires a separately configured memoryFiles adapter and does not move existing storage automatically.

> After changing which source files the adapter uses, run openclaw memory index --force --agent \<id> before searching. Keep the workspace binding unchanged during maintenance. Revoking access does not retract results already read or retained, and embedding requests or multi-step diary updates may continue after their original access checks.

> Task tracking, maintenance, and flow reports do less repeated storage work while preserving newer progress, deletions, delivery details, and late results. Maintenance can continue around unsettled tasks, and restored or retried workflows show their committed status even when a background worker’s reply is delayed. Large task flows can also enter a waiting state without redundant result copies exhausting the worker’s memory. Individual requests can still wait for storage, and queued events become durable only when saved.

> The GitHub reader keeps source discussions beside your chat, remote workspaces connect that conversation to files, Memory, and Skills on another computer, and live meeting notes let you follow a capture before it ends.

> You can send uploaded files to the computer where an agent’s workspace lives and receive its finished files back in chat, with Memory files and supported workspace Skills available on that same computer. This requires an explicitly configured host integration, current file and command grants, and matching OpenClaw versions on the Gateway and paired node. Workspace Skills can be discovered, read, watched, and have their dependencies installed there; remote Skill source installation, updates, removal, and ClawHub management remain unsupported.

> Transfers default to 50 MiB per file, and uploads hold the admitted file in memory. If an enabled upload fails, the turn does not start without its file; missing or denied output files fail explicitly instead of returning stale local copies. Remove saved file.create grants before downgrading to an older version.

> OpenClaw avoids some repeated local cleanup and rendering while receiving long replies containing comparison text or final-answer tags. The benefit depends on the reply, and the final-answer path can use more peak memory while reducing repeated processing.

> Repeated conversation and state reads reuse eligible database connections and workers instead of repeatedly opening them. Healthy reusable resources can stay available for 30 idle minutes, reducing setup during intermittent activity while reads continue to see current data. Larger active installations can consequently retain more memory and open file handles during that window.

> Bursts of conversation writes leave more opportunities for other work to proceed, and saving large replies or tool results shortens the time other writers can be held up. Small requests arriving during startup or reconnect can wait up to 10 seconds for capacity instead of failing immediately, while memory and oversized-request limits still apply. Lookups through large task and conversation histories also inspect fewer unrelated records.

> Memory file watching is separated from indexing, and diagnostics and search-result preparation reuse existing information. This is maintenance of the current Memory implementation.

Source: https://docs.openclaw.ai/releases/2026.9.6
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-23-50-safety-and-privacy-changes-in-v2026-9-6|50 Safety and Privacy changes in v2026.9.6]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-23-localization-maintenance-removes-entries-whose-interface-text-has-already-been-r|Localization maintenance removes entries whose interface text has already been…]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-09-23-5-reliability-and-performance-changes-in-v2026-9-6|5 Reliability and Performance changes in v2026.9.6]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-23-2-image-generation-changes-in-v2026-9-6|2 Image Generation changes in v2026.9.6]] · Image Generation
- [[Changes/OpenClaw/2026-09-23-18-voice-and-audio-changes-in-v2026-9-6|18 Voice and Audio changes in v2026.9.6]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-23-25-context-window-changes-in-v2026-9-6|25 Context Window changes in v2026.9.6]] · Context Window
- [[Changes/OpenClaw/2026-09-23-16-mobile-and-desktop-changes-in-v2026-9-6|16 Mobile and Desktop changes in v2026.9.6]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-23-41-agent-mode-changes-in-v2026-9-6|41 Agent Mode changes in v2026.9.6]] · Agent Mode
- [[Changes/OpenClaw/2026-09-23-16-collaboration-changes-in-v2026-9-6|16 Collaboration changes in v2026.9.6]] · Collaboration
- [[Changes/OpenClaw/2026-09-23-15-editor-experience-changes-in-v2026-9-6|15 Editor Experience changes in v2026.9.6]] · Editor Experience
- [[Changes/OpenClaw/2026-09-23-2-enterprise-and-administration-changes-in-v2026-9-6|2 Enterprise and Administration changes in v2026.9.6]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-23-31-developer-workflow-changes-in-v2026-9-6|31 Developer Workflow changes in v2026.9.6]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-23-8-pricing-model-changes-in-v2026-9-6|8 Pricing Model changes in v2026.9.6]] · Pricing Model
- [[Changes/OpenClaw/2026-09-23-plugin-requested-answer-revisions-wait-for-session-history-to-become-available-a|Plugin-requested answer revisions wait for session history to become available…]] · Projects and Workspaces
- [[Changes/OpenClaw/2026-09-23-6-files-and-data-changes-in-v2026-9-6|6 Files and Data changes in v2026.9.6]] · Files and Data
- [[Changes/OpenClaw/2026-09-23-58-apps-and-integrations-changes-in-v2026-9-6|58 Apps and Integrations changes in v2026.9.6]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-23-17-account-and-access-changes-in-v2026-9-6|17 Account and Access changes in v2026.9.6]] · Account and Access
- [[Changes/OpenClaw/2026-09-23-background-image-video-and-music-generation-can-complete-independently-of-the-re|Background image, video, and music generation can complete independently…]] · Music Generation
- [[Changes/OpenClaw/2026-09-23-3-search-and-browsing-changes-in-v2026-9-6|3 Search and Browsing changes in v2026.9.6]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-23-19-interface-experience-changes-in-v2026-9-6|19 Interface Experience changes in v2026.9.6]] · Interface Experience
- [[Changes/OpenClaw/2026-09-23-9-automation-and-scheduling-changes-in-v2026-9-6|9 Automation and Scheduling changes in v2026.9.6]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-23-22-model-support-changes-in-v2026-9-6|22 Model Support changes in v2026.9.6]] · Model Support
- [[Changes/OpenClaw/2026-09-23-119-other-changes-in-v2026-9-6|119 other changes in v2026.9.6]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Memory and Personalization

- Earlier: 2026-09-22 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-09-22-resuming-large-local-sessions-keeps-transcript-memory-bounded-for-smoother-cli-p|Resuming large local sessions keeps transcript memory bounded for smoother CLI performance]]
- Later: 2026-09-25 · Claude Code · [[Changes/Claude Code/2026-09-25-improved-lists-in-help-hooks-copy-chrome-memory-ide-release-notes-rewind-diff-re|Improved lists in /help, /hooks, /copy, /chrome, /memory, /ide…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-23-b49b94&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-23-23-memory-and-personalization-changes-in-v2026-9-6.md%0ACard%20ID%3A%20openclaw-2026-09-23-b49b94%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.6%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->