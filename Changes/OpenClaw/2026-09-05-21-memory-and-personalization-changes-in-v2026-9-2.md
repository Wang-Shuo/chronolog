---
card_id: openclaw-2026-09-05-6b7c4d
date: '2026-09-05'
description: 'OpenClaw · 2026-09-05 · Memory and Personalization: 21 changes in v2026.9.2
  — The managed llama.cpp setup now recommends a model using the available memory…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1143
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: cbcb20510765a02ada3a12f81bd156d2d6a7d4e61fc7067f86e9ac951d5c611a
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-05-6b7c4d
  comparison: ''
  date: '2026-09-05'
  description: 'OpenClaw — v2026.9.2: 21 Memory and Personalization changes'
  evidence:
  - quote: The managed llama.cpp setup now recommends a model using the available
      memory, supported graphics hardware, and disk space on the computer running
      OpenClaw. It shows you that computer's name, the model, and the download size
      before asking to proceed, which matters when you are opening setup in a browser
      connected to a different machine. Before changing your default, it checks both
      a response and a real file-read tool result; a failed or cancelled activation
      leaves the previous model selected.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: The local-model recommendations begin with an 8 GiB memory floor for the
      smallest recipe, with larger choices needing more memory and, in some cases,
      graphics acceleration. Actual fit and speed still depend on available resources
      and the workload. CPU-only replies can still take several minutes, and setup
      now distinguishes a response-check timeout from a tool-use-check timeout with
      the failed check named in the error.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Large Codex histories use bounded pages and shortened tool-output previews,
      with full output retained in Codex. Very large individual records and some legacy
      histories can still exceed the transport limits. On the computer running OpenClaw,
      cold runtime history checks let unrelated activity continue, and browsing retained
      archives leaves less message content in memory between requests, at the cost
      of reading those pages from disk again.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Interrupted personal-account setup can resume with its original session
      and worktree, while failed cloud starts retain their error and elapsed time
      when you return. Covered app-triggered reloads protect unsaved starts while
      the page is responsive and offer an explicit discard action when needed. Incognito
      starts remain memory-only, and closing the page or choosing to discard unsaved
      input can still lose them.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: The Review panel keeps unchanged files out of a session's changes and reports
      full addition counts for large new text files even when their previews must
      stay bounded. GitHub publication controls also retain a retry and its original
      account across chat navigation and same-chat split panes. That state is held
      in page memory and clears on reload or relevant connection and access changes.
      A rejected first account choice can be refreshed before an explicit new Publish,
      while an uncertain outcome keeps checking the original request.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Large conversation stores also do less maintenance work on the thread serving
      interactive Gateway requests. Eligible transcript reclamation and physical disk
      accounting run in workers, excluded sessions avoid unnecessary metadata reads,
      and large archive backlogs can progress without overflowing SQLite's parameter
      limit. Scan scheduling and old-history inspection use less temporary memory
      in their affected paths, keeping the same retention decisions and disk totals.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Memory needs to stay useful as conversations grow, daily notes become longer-term
      knowledge, and you change the way your Claw stores and searches them. This release
      repairs several places where that continuity could break, from daily memories
      missing later evidence to recalled context disappearing when a session rotated,
      while reducing repeated search and indexing work and giving you a clearer view
      of what is taking up disk space.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Memories first recorded by the daily Dreaming pass can now collect evidence
      from later recalls and grounded observations, so they can qualify for long-term
      storage under the existing promotion rules. The original source stays attached,
      and reinforcement from combined memory and Wiki searches now counts only the
      memory results actually shown to the model. During consolidation, the model
      chooses what to add, merge, or supersede, while OpenClaw builds the saved entries
      from their source evidence and preserves unrelated memories.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Active Memory also keeps eligible recalled context and unavailable-memory
      warnings through session rotation. A completed, grounded recall can still reach
      the reply when its cleanup crosses the deadline, without turning on transcript
      exports; failed recalls, failed cleanup, and unavailable results remain excluded
      from that recovery. Dreaming and Skill Workshop now share visible background
      capacity in System busyness, with foreground work keeping its own capacity.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Memory searches that return only notes, or no results at all, now skip
      processing unrelated conversation history. First searches also avoid decoding
      unrelated saved prompts and reopening an already verified agent database, while
      indexing large memory files prepares their source text once instead of repeating
      the same work for each piece. These changes address specific sources of delay
      as your saved history grows, with the selected search corpus, annotations, and
      transcript access checks preserved.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Preparing memory tools no longer starts the embedding provider before a
      search is requested, and changing settings after a failed search lets the tool
      retry with the new configuration immediately. Targeted refreshes read fewer
      unrelated session records, while an exact lookup for a missing message in an
      imported CLI conversation now returns empty history instead of substituting
      recent messages that do not answer the request.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Affected plugins that keep their memory managers immutable can now report
      status, search, read, and finish cleanup normally, so the Memory page can show
      the actual provider instead of a misleading attention warning. Dreaming schedules
      also follow frequency changes, disabling, and re-enabling after a plugin reload,
      without requiring a full restart.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Once your Memory Wiki vault is active, opening an existing visible page
      by its exact Markdown path reads that page without scanning unrelated pages,
      so a broken file elsewhere no longer has to block the page you asked for. Local
      source sync can also reuse an existing compiled Wiki after startup. Fresh CLI
      processes still validate the saved snapshot, and lookups by a short name, page
      ID, or missing path can still need a vault scan.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Forgetting a session also protects unrelated saved memory when a staged
      file rewrite fails, allowing you to fix the storage problem and retry. Doctor
      imports large legacy memory logs in batches and recognizes configured secret-store
      credentials without telling you to replace working keys, while file-watcher
      warnings now point to supported recovery steps for the affected agent.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: The Devices page can show memory readings from connected iPhones and iPads,
      plus memory and available storage from Android phones, when the Gateway supports
      device resource reporting. The apps send a reading on connection and refresh
      it while connected, giving you a way to check phone resources from the same
      place as your other devices.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Ending a Gateway-controlled OpenAI Realtime call now reports a failed provider
      hangup and retains it for bounded automatic cleanup retries. If those attempts
      are exhausted, cleanup remains incomplete and the call still reserves capacity;
      pressing End again is not the retry mechanism. The OpenAI cleanup guidance explains
      recovery, including that a restart can lose the in-memory cleanup obligation
      and does not prove the provider call ended.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: There are important boundaries to those choices. Under tree or all , requester-owned
      native subagent and ACP child sessions remain reachable even when agent-to-agent
      access is disabled. tree also lets the canonical main session reach all same-agent
      conversations, while self stays limited to its current conversation. Sandboxing
      restricts what the sandboxed caller can reach; it does not hide its transcripts
      from another permitted caller. Incognito sessions remain hidden from these tools,
      and memory_search remains agent-scoped while sessions_search searches transcripts
      within the permitted scope.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Preparing a long saved conversation now happens in background workers so
      that reading its history does not hold up unrelated Gateway activity. Context
      loading also batches message reads, startup can check for existing messages
      without decoding their full contents, and resuming an older view of a conversation
      uses fewer database statements when saving the next message. These changes reduce
      interference and unnecessary work while preserving the selected conversation
      branch; the amount of history still matters, and the work does not have a fixed
      memory cost.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Branching keeps your current conversation in place until the new branch
      has saved, preserves current session details, and prevents an older run from
      writing after another run takes over. Shared databases also retain the correct
      agent ownership in session views and save the activity records needed to inspect
      non-default agents. Incognito history follows the active branch again while
      remaining in memory, and stopped history workers release their database leases
      when cleanup succeeds. A cleanup failure stays visible with restart guidance
      before deletion.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Folder browsing now preserves the exact path returned in a listing, including
      a trailing space, so selecting Project with a trailing space opens that folder
      instead of a sibling named Project without one. The Files pane also accepts
      contained names such as ..notes , and matching configured memory sources can
      discover and read those files without mistaking the name for a parent-directory
      traversal. This fixes directory browsing; New Session submission and saved-preference
      handling are separate paths.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Agents can read from the beginning of a blank line without receiving a
      false end-of-line error, including when an ordinary Markdown or memory file
      starts that way. Operators can also delete an agent with file cleanup, recreate
      the same ID, and create new sessions without restarting the Gateway.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 21-memory-and-personalization-changes-in-v2026-9-2
  source_release: openclaw-2026-09-05-v2026-9-2-377f6d77
  source_type: openclaw_changelog
  theme: memory
  title: 21 Memory and Personalization changes in v2026.9.2
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-09-01-4-memory-and-personalization-changes-in-v2026-8-2|4
  Memory and Personalization changes in v2026.8.2]]'
- '[[Changes/OpenClaw/2026-09-03-19-memory-and-personalization-changes-in-v2026-9-1|19
  Memory and Personalization changes in v2026.9.1]]'
- '[[Changes/GitHub Copilot CLI/2026-09-04-long-running-sessions-on-linux-return-freed-memory-to-the-system-instead-of-hold|Long-running
  sessions on Linux return freed memory to the system instead of holding…]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-05-v2026-9-2-377f6d77|openclaw-2026-09-05-v2026-9-2-377f6d77]]'
source_type: openclaw_changelog
theme: memory
title: 21 Memory and Personalization changes in v2026.9.2
type: change
---

<!-- chronolog:begin region="header" -->
# 21 Memory and Personalization changes in v2026.9.2

**OpenClaw** · 2026-09-05 · [[Themes/memory|Memory and Personalization]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.2) · from [[Releases/OpenClaw/openclaw-2026-09-05-v2026-9-2-377f6d77|v2026.9.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> The managed llama.cpp setup now recommends a model using the available memory, supported graphics hardware, and disk space on the computer running OpenClaw. It shows you that computer's name, the model, and the download size before asking to proceed, which matters when you are opening setup in a browser connected to a different machine. Before changing your default, it checks both a response and a real file-read tool result; a failed or cancelled activation leaves the previous model selected.

> The local-model recommendations begin with an 8 GiB memory floor for the smallest recipe, with larger choices needing more memory and, in some cases, graphics acceleration. Actual fit and speed still depend on available resources and the workload. CPU-only replies can still take several minutes, and setup now distinguishes a response-check timeout from a tool-use-check timeout with the failed check named in the error.

> Large Codex histories use bounded pages and shortened tool-output previews, with full output retained in Codex. Very large individual records and some legacy histories can still exceed the transport limits. On the computer running OpenClaw, cold runtime history checks let unrelated activity continue, and browsing retained archives leaves less message content in memory between requests, at the cost of reading those pages from disk again.

> Interrupted personal-account setup can resume with its original session and worktree, while failed cloud starts retain their error and elapsed time when you return. Covered app-triggered reloads protect unsaved starts while the page is responsive and offer an explicit discard action when needed. Incognito starts remain memory-only, and closing the page or choosing to discard unsaved input can still lose them.

> The Review panel keeps unchanged files out of a session's changes and reports full addition counts for large new text files even when their previews must stay bounded. GitHub publication controls also retain a retry and its original account across chat navigation and same-chat split panes. That state is held in page memory and clears on reload or relevant connection and access changes. A rejected first account choice can be refreshed before an explicit new Publish, while an uncertain outcome keeps checking the original request.

> Large conversation stores also do less maintenance work on the thread serving interactive Gateway requests. Eligible transcript reclamation and physical disk accounting run in workers, excluded sessions avoid unnecessary metadata reads, and large archive backlogs can progress without overflowing SQLite's parameter limit. Scan scheduling and old-history inspection use less temporary memory in their affected paths, keeping the same retention decisions and disk totals.

> Memory needs to stay useful as conversations grow, daily notes become longer-term knowledge, and you change the way your Claw stores and searches them. This release repairs several places where that continuity could break, from daily memories missing later evidence to recalled context disappearing when a session rotated, while reducing repeated search and indexing work and giving you a clearer view of what is taking up disk space.

> Memories first recorded by the daily Dreaming pass can now collect evidence from later recalls and grounded observations, so they can qualify for long-term storage under the existing promotion rules. The original source stays attached, and reinforcement from combined memory and Wiki searches now counts only the memory results actually shown to the model. During consolidation, the model chooses what to add, merge, or supersede, while OpenClaw builds the saved entries from their source evidence and preserves unrelated memories.

> Active Memory also keeps eligible recalled context and unavailable-memory warnings through session rotation. A completed, grounded recall can still reach the reply when its cleanup crosses the deadline, without turning on transcript exports; failed recalls, failed cleanup, and unavailable results remain excluded from that recovery. Dreaming and Skill Workshop now share visible background capacity in System busyness, with foreground work keeping its own capacity.

> Memory searches that return only notes, or no results at all, now skip processing unrelated conversation history. First searches also avoid decoding unrelated saved prompts and reopening an already verified agent database, while indexing large memory files prepares their source text once instead of repeating the same work for each piece. These changes address specific sources of delay as your saved history grows, with the selected search corpus, annotations, and transcript access checks preserved.

> Preparing memory tools no longer starts the embedding provider before a search is requested, and changing settings after a failed search lets the tool retry with the new configuration immediately. Targeted refreshes read fewer unrelated session records, while an exact lookup for a missing message in an imported CLI conversation now returns empty history instead of substituting recent messages that do not answer the request.

> Affected plugins that keep their memory managers immutable can now report status, search, read, and finish cleanup normally, so the Memory page can show the actual provider instead of a misleading attention warning. Dreaming schedules also follow frequency changes, disabling, and re-enabling after a plugin reload, without requiring a full restart.

> Once your Memory Wiki vault is active, opening an existing visible page by its exact Markdown path reads that page without scanning unrelated pages, so a broken file elsewhere no longer has to block the page you asked for. Local source sync can also reuse an existing compiled Wiki after startup. Fresh CLI processes still validate the saved snapshot, and lookups by a short name, page ID, or missing path can still need a vault scan.

> Forgetting a session also protects unrelated saved memory when a staged file rewrite fails, allowing you to fix the storage problem and retry. Doctor imports large legacy memory logs in batches and recognizes configured secret-store credentials without telling you to replace working keys, while file-watcher warnings now point to supported recovery steps for the affected agent.

> The Devices page can show memory readings from connected iPhones and iPads, plus memory and available storage from Android phones, when the Gateway supports device resource reporting. The apps send a reading on connection and refresh it while connected, giving you a way to check phone resources from the same place as your other devices.

> Ending a Gateway-controlled OpenAI Realtime call now reports a failed provider hangup and retains it for bounded automatic cleanup retries. If those attempts are exhausted, cleanup remains incomplete and the call still reserves capacity; pressing End again is not the retry mechanism. The OpenAI cleanup guidance explains recovery, including that a restart can lose the in-memory cleanup obligation and does not prove the provider call ended.

> There are important boundaries to those choices. Under tree or all , requester-owned native subagent and ACP child sessions remain reachable even when agent-to-agent access is disabled. tree also lets the canonical main session reach all same-agent conversations, while self stays limited to its current conversation. Sandboxing restricts what the sandboxed caller can reach; it does not hide its transcripts from another permitted caller. Incognito sessions remain hidden from these tools, and memory_search remains agent-scoped while sessions_search searches transcripts within the permitted scope.

> Preparing a long saved conversation now happens in background workers so that reading its history does not hold up unrelated Gateway activity. Context loading also batches message reads, startup can check for existing messages without decoding their full contents, and resuming an older view of a conversation uses fewer database statements when saving the next message. These changes reduce interference and unnecessary work while preserving the selected conversation branch; the amount of history still matters, and the work does not have a fixed memory cost.

> Branching keeps your current conversation in place until the new branch has saved, preserves current session details, and prevents an older run from writing after another run takes over. Shared databases also retain the correct agent ownership in session views and save the activity records needed to inspect non-default agents. Incognito history follows the active branch again while remaining in memory, and stopped history workers release their database leases when cleanup succeeds. A cleanup failure stays visible with restart guidance before deletion.

> Folder browsing now preserves the exact path returned in a listing, including a trailing space, so selecting Project with a trailing space opens that folder instead of a sibling named Project without one. The Files pane also accepts contained names such as ..notes , and matching configured memory sources can discover and read those files without mistaking the name for a parent-directory traversal. This fixes directory browsing; New Session submission and saved-preference handling are separate paths.

> Agents can read from the beginning of a blank line without receiving a false end-of-line error, including when an ordinary Markdown or memory file starts that way. Operators can also delete an agent with file cleanup, recreate the same ID, and create new sessions without restarting the Gateway.

Source: https://docs.openclaw.ai/releases/2026.9.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-05-24-safety-and-privacy-changes-in-v2026-9-2|24 Safety and Privacy changes in v2026.9.2]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-05-3-pricing-model-changes-in-v2026-9-2|3 Pricing Model changes in v2026.9.2]] · Pricing Model
- [[Changes/OpenClaw/2026-09-05-8-editor-experience-changes-in-v2026-9-2|8 Editor Experience changes in v2026.9.2]] · Editor Experience
- [[Changes/OpenClaw/2026-09-05-progress-mode-can-stay-quiet-about-routine-tool-calls-while-keeping-the-updates|Progress mode can stay quiet about routine tool calls while keeping the updates…]] · Presentation Creation
- [[Changes/OpenClaw/2026-09-05-swarm-is-now-available-to-eligible-agents-without-a-separate-enablement-step-so|Swarm is now available to eligible agents without a separate enablement step…]] · Agent Mode
- [[Changes/OpenClaw/2026-09-05-a-rejected-send-can-keep-its-original-attachments-and-retry-action-when-you-leav|A rejected send can keep its original attachments and Retry action when you leave…]] · Files and Data
- [[Changes/OpenClaw/2026-09-05-20-account-and-access-changes-in-v2026-9-2|20 Account and Access changes in v2026.9.2]] · Account and Access
- [[Changes/OpenClaw/2026-09-05-17-model-support-changes-in-v2026-9-2|17 Model Support changes in v2026.9.2]] · Model Support
- [[Changes/OpenClaw/2026-09-05-16-developer-workflow-changes-in-v2026-9-2|16 Developer Workflow changes in v2026.9.2]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-05-4-enterprise-and-administration-changes-in-v2026-9-2|4 Enterprise and Administration changes in v2026.9.2]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-05-if-background-image-video-or-music-generation-finishes-but-final-delivery-fails|If background image, video or music generation finishes but final delivery fails…]] · Music Generation
- [[Changes/OpenClaw/2026-09-05-34-agent-mode-changes-in-v2026-9-2|34 Agent Mode changes in v2026.9.2]] · Agent Mode
- [[Changes/OpenClaw/2026-09-05-35-apps-and-integrations-changes-in-v2026-9-2|35 Apps and Integrations changes in v2026.9.2]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-05-8-automation-and-scheduling-changes-in-v2026-9-2|8 Automation and Scheduling changes in v2026.9.2]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-05-9-collaboration-changes-in-v2026-9-2|9 Collaboration changes in v2026.9.2]] · Collaboration
- [[Changes/OpenClaw/2026-09-05-10-mobile-and-desktop-changes-in-v2026-9-2|10 Mobile and Desktop changes in v2026.9.2]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-05-15-context-window-changes-in-v2026-9-2|15 Context Window changes in v2026.9.2]] · Context Window
- [[Changes/OpenClaw/2026-09-05-4-search-and-browsing-changes-in-v2026-9-2|4 Search and Browsing changes in v2026.9.2]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-05-17-voice-and-audio-changes-in-v2026-9-2|17 Voice and Audio changes in v2026.9.2]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-05-21-interface-experience-changes-in-v2026-9-2|21 Interface Experience changes in v2026.9.2]] · Interface Experience
- [[Changes/OpenClaw/2026-09-05-3-reliability-and-performance-changes-in-v2026-9-2|3 Reliability and Performance changes in v2026.9.2]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-05-you-can-now-put-the-part-of-a-task-you-are-working-on-in-the-main-view-and-keep|Put the part of a task you are working on in the main view and keep the conversation…]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-05-72-other-changes-in-v2026-9-2|72 other changes in v2026.9.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Memory and Personalization

- Earlier: 2026-09-04 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-09-04-long-running-sessions-on-linux-return-freed-memory-to-the-system-instead-of-hold|Long-running sessions on Linux return freed memory to the system instead of holding…]]
- Later: 2026-09-08 · OpenClaw · [[Changes/OpenClaw/2026-09-08-10-memory-and-personalization-changes-in-v2026-9-3|10 Memory and Personalization changes in v2026.9.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-05-6b7c4d&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-05-21-memory-and-personalization-changes-in-v2026-9-2.md%0ACard%20ID%3A%20openclaw-2026-09-05-6b7c4d%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->