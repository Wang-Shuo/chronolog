---
card_id: openclaw-2026-09-23-3e2e1b
date: '2026-09-23'
description: 'OpenClaw · 2026-09-23 · Agent Mode: 41 changes in v2026.9.6 — Setup
  has clearer recovery paths when an installation cannot continue, and new custom
  agents keep…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1175
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 7d655375aaa9b5a88321c613eca9346622233b953f5c219a02e037b4e385ce6e
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-23-3e2e1b
  comparison: ''
  date: '2026-09-23'
  description: 'OpenClaw — v2026.9.6: 41 Agent Mode changes'
  evidence:
  - quote: Setup has clearer recovery paths when an installation cannot continue,
      and new custom agents keep the job you approved for them.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: A new custom agent created through the Control UI now keeps its approved
      purpose as saved instructions for later conversations. This applies when creating
      a custom agent in a local workspace. Existing instructions stay intact, and
      conflicting instructions prompt you to choose another workspace. Changing the
      proposed purpose requires fresh approval.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Reopening New agent brings back the creation choices without discarding
      your Ask OpenClaw conversation, once pending questions, setup steps and approvals
      are finished. New agents also retain the display name you requested separately
      from their identifier, including when you choose a bundled role.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: A failed project lookup now keeps your saved choice and blocks starting
      until discovery recovers or you deliberately change the destination. New Session
      also remembers a supported Fast mode choice, including off, for the same agent
      and Gateway.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Returning to a chat restores your saved reading position once, then leaves
      scrolling under your control. Delayed history refreshes also preserve newer
      live replies and keep saved transcripts with the selected agent.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Agent Files also waits for file contents to load before allowing edits
      or saves, while retaining loaded files and unsaved drafts during refresh.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Open a background task or inline subagent activity to inspect its status
      and transcript inside Tasks , then use Back to tasks to return to the list.
      Review keeps its diff and Files keeps its selection, while reload can restore
      the selected task or show that it is unavailable. Compact activity summaries
      retain expandable details, and completed or canceled tasks update their labels
      correctly. Operation counts include repeated attempts and do not mean distinct
      files or successful results.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Running, queued and waiting subagents keep a stable order in live chat
      activity. Finished, failed, canceled and timed-out runs leave that list when
      their final state arrives, making all five slots available for ongoing work.
      Their results, delivery details and final edit statistics remain in Tasks history
      and details, where expanded results remain readable and accessible. Completed
      native subagents also publish their final Tasks status without requiring a page
      reload.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: New visible child conversations can inherit the human owner when the verified
      requester matches the parent's human owner. Other cases retain the agent fallback,
      and existing conversations are not reassigned.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Operator-created scheduled agent jobs can request an ordinary Gateway update
      without inventing a chat owner identity. Jobs originating from external requesters
      do not gain that exception, and notification destinations do not become the
      authorizing user. Existing update restrictions still apply. If scheduled authority
      ends while update preparation is underway, inspect the update status; that late
      revocation may not stop the prepared update from proceeding. See updating .
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: In larger installations, prepared agents can take requests while the rest
      of the fleet finishes starting, with pending agents shown as still preparing.
      Startup and session-source reads also avoid repeated checks and unnecessary
      loading of saved prompts. A ready Gateway can therefore have optional agents
      that are not yet available; readiness does not mean the whole fleet has finished,
      but the required default and system agents must have usable databases.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Use the supported update or Doctor migration path with all writers stopped,
      a verified backup that includes pending database journal data, and space for
      temporary tables, journals and backups. The final formats are agent schema 23
      and shared-state schema 18 ; older builds refuse converted stores, so downgrading
      requires the matching older build and pre-upgrade backup in a separate state
      directory, not changing version markers. Direct database readers need supported
      accessors or exports, and compressed rows require a compatible decoder. See
      database versioning .
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Successful imports can continue past archive-only or scratch-cleanup warnings,
      while changed originals, incomplete captured data and storage or ownership failures
      still need attention. Ambiguous task identifiers remain unchanged rather than
      risking a result reaching the wrong task; title repair also retains a limitation
      when several agents share one physical store.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Intentionally retained stores from deleted agents no longer block unrelated
      active-agent repairs, and valid ACP ownership repairs can finish while retired
      workers settle. Deleted agents stay deleted, with unverified or changed history
      still protected.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: With the Gateway stopped, Doctor can settle verified leftover imported
      transcripts, append an eligible missing suffix and archive the original bytes.
      Conflicting or malformed files remain protected, and recovery through a fixed
      custom store for a nondefault agent still has a path-selection limitation. New
      reports distinguish current findings from historical errors; a retained archive
      warning alone needs no repair when the expected conversations are present.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Managed restarts verify the serving Gateway and give admitted agent, subagent
      and scheduled work time to finish before storage and helpers close. Unknown
      activity no longer counts as idle. Forced restarts close new admissions immediately
      and normally allow up to five minutes for admitted work, capped by the service's
      remaining shutdown allowance; work still running at the deadline is canceled.
      An explicit forced wait of zero is immediate, while ordinary --wait 0 remains
      unbounded except for native service limits. These Unix recovery changes require
      the updated launcher. Recognized stale Linux shutdown policy can now be repaired
      during eligible updates or Doctor maintenance; custom definitions may still
      need same-profile openclaw gateway install --force to pick up KillMode=mixed
      . See restart recovery .
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Already-pending authorized answers and approvals can complete during graceful
      draining, and eligible replacement subagents can save their results. New work
      stays blocked, and exhausted budgets are not renewed. Older forced callers that
      supply no budget retain at most 45 seconds of draining within their 60-second
      replacement window.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: You can return to unfinished conversations after a restart with their saved
      history, progress and tool results, plus a restart notice. The agent leading
      the conversation decides how to continue interrupted subagents instead of automatically
      relaunching them, checking that earlier work stopped and whether an action already
      took effect before repeating or replacing it. Stopped conversations stay stopped,
      and continuation still depends on current permissions and recovery checks. See
      what survives a restart .
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Supported container image upgrades now run Doctor's retained-state migrations
      automatically before serving traffic, including on qualifying FUSE volumes.
      A refused default or system agent prevents a healthy readiness response, while
      an optional refused agent can remain isolated. Use /readyz when incoming traffic
      needs usable agents, and retain verified matching backups for rollback.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Accepted group and channel requests now require an answer by default, including
      unmentioned messages in groups configured to accept them. If tools finish and
      the agent ends silently, reply recovery can produce the missing answer without
      repeating completed actions. Confirmed or still-pending delivery prevents another
      recovery reply, and pending tool or delegated work stays pending while restart
      recovery waits for capacity.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Always-on groups may receive more replies after updating. To keep optional
      replies for unaddressed requests, set agents.defaults.silentReply.group to "allow"
      or use the corresponding surface override described under silent replies . Mention
      and access rules still decide which requests reach the agent, while ambient
      events, heartbeats, and internal helper turns remain optional. Internal child-result
      and coordination notifications can now finish silently without triggering a
      repeated answer. Messages canceled by Stop while still queued also remain silent,
      while new user requests retain normal reply recovery.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: With Discord streaming.mode set to progress , an accepted handoff to child
      agents keeps the existing progress checklist visible while their work continues.
      The final answer arrives separately, so the checklist remains a useful record
      of the work in progress. Declined handoffs and media or control-message paths
      keep their ordinary delivery behavior.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: If a conversation's assignment is changed, removed, or superseded before
      dispatch, OpenClaw asks you to retry instead of continuing through the old session.
      Custom session-store updates and newly recorded delayed replies also keep the
      selected agent, while /session idle and /session max-age wait for their settings
      to be saved before confirming success.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: If a Feishu meeting invitation fails before the agent durably accepts it,
      a later delivery of that invitation from Feishu can be processed again instead
      of being discarded as a duplicate. vcAutoJoin remains an explicit opt-in, and
      this change neither schedules retries nor guarantees a meeting join. Already
      accepted invitations and older duplicate-message records keep their existing
      behavior.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Requesting a specific Matrix message through the message CLI or agent tool
      now returns that event or an error, instead of substituting unrelated recent
      room history. Existing permissions and encrypted-message limits still apply,
      while ordinary history reads keep their current behavior. Configured contact,
      room, and approver checks avoid unnecessary credential reads, and expired secret-storage
      requests fail promptly while transient network errors can still retry.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: With inbound batching configured, rapid WhatsApp messages from the same
      sender can reach the agent together instead of waiting through separate batching
      delays. Group conversations keep each participant's identity and message order,
      including when another person's quoted or buffered message interrupts a batch.
      This restores the existing setting's behavior without introducing a new default.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Skills now refresh around actual content changes, while Workshop keeps
      a clearer record of the skills available to an agent and the reviews that shape
      them.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Supported remote workspace connections let agent tasks use Skills and supporting
      files on the machine where the workspace lives. Adapters that also supply the
      required host information and management operations can show that machine's
      installed skills, choose matching dependencies, and run approved dependency
      or source and ClawHub management operations there. Missing capabilities return
      an error without installing on the Gateway computer. The workspace adapter documentation
      describes the requirements; a document bridge alone does not enable this management,
      and the paired-node adapter does not support remote source or ClawHub installation,
      updates or removal.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: The Tauri desktop app puts your latest exchange above a separate bottom
      composer, letting you prepare the next message while a reply streams. Collapsing
      the reply preserves the draft, live text, and widget interactions; sending and
      switching agents wait until the current turn finishes. Cmd/Ctrl+Shift+O now
      reaches the foreground app for New Session instead of summoning a background
      dashboard. The separate configurable Quick Chat shortcut remains available,
      as described in the desktop app guide .
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: The precaution concerns the agent's interpretation of the task and does
      not establish that the user violated a policy. It does not undo completed actions
      or bypass a refusal automatically. Model failover guidance covers the limits,
      including that downgrading to code from before this feature removes pause and
      held-message enforcement.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Resumed Codex sessions retain their captured inherited AGENTS.md instructions
      even if the source file changes or disappears; start a new session to load edited
      instructions. Eligible /btw side questions regain inherited shell tools, and
      cancellation settles the side question's native background terminals or reports
      when stopping cannot be confirmed. Main-conversation terminals and OpenClaw
      background jobs keep their existing lifetimes.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Accepted manual runs can start after the calling tool or native agent reply
      finishes, without keeping that reply open for the whole job, and acknowledgement
      now follows a saved run receipt. Cancellation, cleared queues, and withdrawn
      permissions still prevent activation. If OpenClaw crashes before dispatch, the
      interrupted receipt remains for diagnosis without automatically replaying the
      run.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Overdue heartbeat checks no longer hold up scheduler startup or reload,
      and their results can wait for busy storage without blocking unrelated work.
      A successful or skipped agent no longer hides another agent’s failure in a combined
      heartbeat result. Background command results can also reach their idle originating
      conversation while unrelated sessions are busy, when automatic wake is enabled.
      Activity in the destination conversation or pending recovery can still defer
      delivery, and subagent sessions remain excluded from automatic wake.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Routine heartbeat checks with no queued events or tasks now skip a busy
      agent if preparation has not started, avoiding a false timeout and error backoff.
      Their next opportunity is the normal scheduled tick. Manual wakes, queued work,
      and checks already started keep their retry behavior, and real execution timeouts
      remain errors.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Managed ACP agents now default to at most eight Tokio workers per child,
      or fewer when fewer CPUs are available, while preserving an inherited worker
      setting. This is a worker-pool default, not a total thread or CPU limit. ACPX
      0.19.1 adds startup, logging, launch-admission, and cleanup fixes; let active
      turns finish and restart embedding hosts to load the updated runtime. Windows
      queue cleanup requires every participating acpx client to be updated.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Embedded and Copilot agents now use Tool Search when its setting is omitted
      and higher-precedence Code Mode is inactive, discovering relevant tools as needed
      instead of receiving every eligible tool’s full description upfront. You can
      turn it off in Labs or set tools.toolSearch to false ; restoring direct tool
      descriptions also requires Code Mode to be inactive. Extra discovery turns can
      cost more, particularly with a small tool catalog.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Supported host integrations can point the existing agent document editor
      and instruction readers at the workspace on a paired node, without maintaining
      a local copy. This requires an explicit workspace mapping, a compatible connected
      node, and separate file grants, with a 16 MiB document limit. If that workspace
      becomes unavailable, reads fail instead of using stale local files. Owner writes
      remain limited to the root AGENTS , SOUL , IDENTITY , and USER documents, and
      an already-dispatched write cannot be undone by disconnecting.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Configuration help now explains that skipBootstrap controls creating workspace
      files, while existing files can still enter the prompt. The workspace settings
      reference clarifies the existing contextInjection choices for the embedded runtime,
      including never . Those choices do not control ordinary CLI-backed prompt preparation
      or prevent an agent from reading files with tools.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: 'Creating an eligible session now queues a notice for its agent''s Home
      conversation , including the session key and available title, creator, and creation
      source without copying messages. This is enabled by default, and you can opt
      out with session.notifyOnCreate: false in session settings . Home receives the
      notice on its next turn or scheduled heartbeat, without an immediate wake-up
      or ongoing monitoring of that conversation.'
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: The terminal interface restores your remembered conversation even when
      newer conversations have similar names, and can show its model details without
      relying on a short search-results list. After reconnecting, old connection responses
      can no longer replace the current details. Existing agent scope and hidden-conversation
      rules still apply. Opening or attaching to a conversation now uses the agent
      identified by the Gateway, including when an older link names a different agent.
      Replies and side-question results from other agents are rejected, with existing
      attachment permissions unchanged.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Agent execution, sessions and scheduled work share more of their existing
      preparation and cleanup code. These changes remove repeated lookups, temporary
      copies and unused imports while retaining current routing and recovery rules.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 41-agent-mode-changes-in-v2026-9-6
  source_release: openclaw-2026-09-23-v2026-9-6-3f12c824
  source_type: openclaw_changelog
  theme: agent-mode
  title: 41 Agent Mode changes in v2026.9.6
  type: change
related_changes:
- '[[Changes/Cursor/2026-09-23-when-rollouts-detects-a-regression-it-names-the-change-it-suspects-and-notifies|When
  Rollouts detects a regression, it names the change it suspects and notifies…]]'
- '[[Changes/Microsoft 365 Copilot/2026-09-23-planner-agent-chat-windows-web-microsoft-365-copilot|Planner
  Agent chat Windows, Web (Microsoft 365 Copilot)]]'
- '[[Changes/Microsoft 365 Copilot/2026-09-23-integrated-extensibility-experience-capability-for-declarative-agents-for-micros|Integrated
  extensibility experience capability for declarative agents for Microsoft…]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-23-v2026-9-6-3f12c824|openclaw-2026-09-23-v2026-9-6-3f12c824]]'
source_type: openclaw_changelog
theme: agent-mode
title: 41 Agent Mode changes in v2026.9.6
type: change
---

<!-- chronolog:begin region="header" -->
# 41 Agent Mode changes in v2026.9.6

**OpenClaw** · 2026-09-23 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.6) · from [[Releases/OpenClaw/openclaw-2026-09-23-v2026-9-6-3f12c824|v2026.9.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Setup has clearer recovery paths when an installation cannot continue, and new custom agents keep the job you approved for them.

> A new custom agent created through the Control UI now keeps its approved purpose as saved instructions for later conversations. This applies when creating a custom agent in a local workspace. Existing instructions stay intact, and conflicting instructions prompt you to choose another workspace. Changing the proposed purpose requires fresh approval.

> Reopening New agent brings back the creation choices without discarding your Ask OpenClaw conversation, once pending questions, setup steps and approvals are finished. New agents also retain the display name you requested separately from their identifier, including when you choose a bundled role.

> A failed project lookup now keeps your saved choice and blocks starting until discovery recovers or you deliberately change the destination. New Session also remembers a supported Fast mode choice, including off, for the same agent and Gateway.

> Returning to a chat restores your saved reading position once, then leaves scrolling under your control. Delayed history refreshes also preserve newer live replies and keep saved transcripts with the selected agent.

> Agent Files also waits for file contents to load before allowing edits or saves, while retaining loaded files and unsaved drafts during refresh.

> Open a background task or inline subagent activity to inspect its status and transcript inside Tasks , then use Back to tasks to return to the list. Review keeps its diff and Files keeps its selection, while reload can restore the selected task or show that it is unavailable. Compact activity summaries retain expandable details, and completed or canceled tasks update their labels correctly. Operation counts include repeated attempts and do not mean distinct files or successful results.

> Running, queued and waiting subagents keep a stable order in live chat activity. Finished, failed, canceled and timed-out runs leave that list when their final state arrives, making all five slots available for ongoing work. Their results, delivery details and final edit statistics remain in Tasks history and details, where expanded results remain readable and accessible. Completed native subagents also publish their final Tasks status without requiring a page reload.

> New visible child conversations can inherit the human owner when the verified requester matches the parent's human owner. Other cases retain the agent fallback, and existing conversations are not reassigned.

> Operator-created scheduled agent jobs can request an ordinary Gateway update without inventing a chat owner identity. Jobs originating from external requesters do not gain that exception, and notification destinations do not become the authorizing user. Existing update restrictions still apply. If scheduled authority ends while update preparation is underway, inspect the update status; that late revocation may not stop the prepared update from proceeding. See updating .

> In larger installations, prepared agents can take requests while the rest of the fleet finishes starting, with pending agents shown as still preparing. Startup and session-source reads also avoid repeated checks and unnecessary loading of saved prompts. A ready Gateway can therefore have optional agents that are not yet available; readiness does not mean the whole fleet has finished, but the required default and system agents must have usable databases.

> Use the supported update or Doctor migration path with all writers stopped, a verified backup that includes pending database journal data, and space for temporary tables, journals and backups. The final formats are agent schema 23 and shared-state schema 18 ; older builds refuse converted stores, so downgrading requires the matching older build and pre-upgrade backup in a separate state directory, not changing version markers. Direct database readers need supported accessors or exports, and compressed rows require a compatible decoder. See database versioning .

> Successful imports can continue past archive-only or scratch-cleanup warnings, while changed originals, incomplete captured data and storage or ownership failures still need attention. Ambiguous task identifiers remain unchanged rather than risking a result reaching the wrong task; title repair also retains a limitation when several agents share one physical store.

> Intentionally retained stores from deleted agents no longer block unrelated active-agent repairs, and valid ACP ownership repairs can finish while retired workers settle. Deleted agents stay deleted, with unverified or changed history still protected.

> With the Gateway stopped, Doctor can settle verified leftover imported transcripts, append an eligible missing suffix and archive the original bytes. Conflicting or malformed files remain protected, and recovery through a fixed custom store for a nondefault agent still has a path-selection limitation. New reports distinguish current findings from historical errors; a retained archive warning alone needs no repair when the expected conversations are present.

> Managed restarts verify the serving Gateway and give admitted agent, subagent and scheduled work time to finish before storage and helpers close. Unknown activity no longer counts as idle. Forced restarts close new admissions immediately and normally allow up to five minutes for admitted work, capped by the service's remaining shutdown allowance; work still running at the deadline is canceled. An explicit forced wait of zero is immediate, while ordinary --wait 0 remains unbounded except for native service limits. These Unix recovery changes require the updated launcher. Recognized stale Linux shutdown policy can now be repaired during eligible updates or Doctor maintenance; custom definitions may still need same-profile openclaw gateway install --force to pick up KillMode=mixed . See restart recovery .

> Already-pending authorized answers and approvals can complete during graceful draining, and eligible replacement subagents can save their results. New work stays blocked, and exhausted budgets are not renewed. Older forced callers that supply no budget retain at most 45 seconds of draining within their 60-second replacement window.

> You can return to unfinished conversations after a restart with their saved history, progress and tool results, plus a restart notice. The agent leading the conversation decides how to continue interrupted subagents instead of automatically relaunching them, checking that earlier work stopped and whether an action already took effect before repeating or replacing it. Stopped conversations stay stopped, and continuation still depends on current permissions and recovery checks. See what survives a restart .

> Supported container image upgrades now run Doctor's retained-state migrations automatically before serving traffic, including on qualifying FUSE volumes. A refused default or system agent prevents a healthy readiness response, while an optional refused agent can remain isolated. Use /readyz when incoming traffic needs usable agents, and retain verified matching backups for rollback.

> Accepted group and channel requests now require an answer by default, including unmentioned messages in groups configured to accept them. If tools finish and the agent ends silently, reply recovery can produce the missing answer without repeating completed actions. Confirmed or still-pending delivery prevents another recovery reply, and pending tool or delegated work stays pending while restart recovery waits for capacity.

> Always-on groups may receive more replies after updating. To keep optional replies for unaddressed requests, set agents.defaults.silentReply.group to "allow" or use the corresponding surface override described under silent replies . Mention and access rules still decide which requests reach the agent, while ambient events, heartbeats, and internal helper turns remain optional. Internal child-result and coordination notifications can now finish silently without triggering a repeated answer. Messages canceled by Stop while still queued also remain silent, while new user requests retain normal reply recovery.

> With Discord streaming.mode set to progress , an accepted handoff to child agents keeps the existing progress checklist visible while their work continues. The final answer arrives separately, so the checklist remains a useful record of the work in progress. Declined handoffs and media or control-message paths keep their ordinary delivery behavior.

> If a conversation's assignment is changed, removed, or superseded before dispatch, OpenClaw asks you to retry instead of continuing through the old session. Custom session-store updates and newly recorded delayed replies also keep the selected agent, while /session idle and /session max-age wait for their settings to be saved before confirming success.

> If a Feishu meeting invitation fails before the agent durably accepts it, a later delivery of that invitation from Feishu can be processed again instead of being discarded as a duplicate. vcAutoJoin remains an explicit opt-in, and this change neither schedules retries nor guarantees a meeting join. Already accepted invitations and older duplicate-message records keep their existing behavior.

> Requesting a specific Matrix message through the message CLI or agent tool now returns that event or an error, instead of substituting unrelated recent room history. Existing permissions and encrypted-message limits still apply, while ordinary history reads keep their current behavior. Configured contact, room, and approver checks avoid unnecessary credential reads, and expired secret-storage requests fail promptly while transient network errors can still retry.

> With inbound batching configured, rapid WhatsApp messages from the same sender can reach the agent together instead of waiting through separate batching delays. Group conversations keep each participant's identity and message order, including when another person's quoted or buffered message interrupts a batch. This restores the existing setting's behavior without introducing a new default.

> Skills now refresh around actual content changes, while Workshop keeps a clearer record of the skills available to an agent and the reviews that shape them.

> Supported remote workspace connections let agent tasks use Skills and supporting files on the machine where the workspace lives. Adapters that also supply the required host information and management operations can show that machine's installed skills, choose matching dependencies, and run approved dependency or source and ClawHub management operations there. Missing capabilities return an error without installing on the Gateway computer. The workspace adapter documentation describes the requirements; a document bridge alone does not enable this management, and the paired-node adapter does not support remote source or ClawHub installation, updates or removal.

> The Tauri desktop app puts your latest exchange above a separate bottom composer, letting you prepare the next message while a reply streams. Collapsing the reply preserves the draft, live text, and widget interactions; sending and switching agents wait until the current turn finishes. Cmd/Ctrl+Shift+O now reaches the foreground app for New Session instead of summoning a background dashboard. The separate configurable Quick Chat shortcut remains available, as described in the desktop app guide .

> The precaution concerns the agent's interpretation of the task and does not establish that the user violated a policy. It does not undo completed actions or bypass a refusal automatically. Model failover guidance covers the limits, including that downgrading to code from before this feature removes pause and held-message enforcement.

> Resumed Codex sessions retain their captured inherited AGENTS.md instructions even if the source file changes or disappears; start a new session to load edited instructions. Eligible /btw side questions regain inherited shell tools, and cancellation settles the side question's native background terminals or reports when stopping cannot be confirmed. Main-conversation terminals and OpenClaw background jobs keep their existing lifetimes.

> Accepted manual runs can start after the calling tool or native agent reply finishes, without keeping that reply open for the whole job, and acknowledgement now follows a saved run receipt. Cancellation, cleared queues, and withdrawn permissions still prevent activation. If OpenClaw crashes before dispatch, the interrupted receipt remains for diagnosis without automatically replaying the run.

> Overdue heartbeat checks no longer hold up scheduler startup or reload, and their results can wait for busy storage without blocking unrelated work. A successful or skipped agent no longer hides another agent’s failure in a combined heartbeat result. Background command results can also reach their idle originating conversation while unrelated sessions are busy, when automatic wake is enabled. Activity in the destination conversation or pending recovery can still defer delivery, and subagent sessions remain excluded from automatic wake.

> Routine heartbeat checks with no queued events or tasks now skip a busy agent if preparation has not started, avoiding a false timeout and error backoff. Their next opportunity is the normal scheduled tick. Manual wakes, queued work, and checks already started keep their retry behavior, and real execution timeouts remain errors.

> Managed ACP agents now default to at most eight Tokio workers per child, or fewer when fewer CPUs are available, while preserving an inherited worker setting. This is a worker-pool default, not a total thread or CPU limit. ACPX 0.19.1 adds startup, logging, launch-admission, and cleanup fixes; let active turns finish and restart embedding hosts to load the updated runtime. Windows queue cleanup requires every participating acpx client to be updated.

> Embedded and Copilot agents now use Tool Search when its setting is omitted and higher-precedence Code Mode is inactive, discovering relevant tools as needed instead of receiving every eligible tool’s full description upfront. You can turn it off in Labs or set tools.toolSearch to false ; restoring direct tool descriptions also requires Code Mode to be inactive. Extra discovery turns can cost more, particularly with a small tool catalog.

> Supported host integrations can point the existing agent document editor and instruction readers at the workspace on a paired node, without maintaining a local copy. This requires an explicit workspace mapping, a compatible connected node, and separate file grants, with a 16 MiB document limit. If that workspace becomes unavailable, reads fail instead of using stale local files. Owner writes remain limited to the root AGENTS , SOUL , IDENTITY , and USER documents, and an already-dispatched write cannot be undone by disconnecting.

> Configuration help now explains that skipBootstrap controls creating workspace files, while existing files can still enter the prompt. The workspace settings reference clarifies the existing contextInjection choices for the embedded runtime, including never . Those choices do not control ordinary CLI-backed prompt preparation or prevent an agent from reading files with tools.

> Creating an eligible session now queues a notice for its agent's Home conversation , including the session key and available title, creator, and creation source without copying messages. This is enabled by default, and you can opt out with session.notifyOnCreate: false in session settings . Home receives the notice on its next turn or scheduled heartbeat, without an immediate wake-up or ongoing monitoring of that conversation.

> The terminal interface restores your remembered conversation even when newer conversations have similar names, and can show its model details without relying on a short search-results list. After reconnecting, old connection responses can no longer replace the current details. Existing agent scope and hidden-conversation rules still apply. Opening or attaching to a conversation now uses the agent identified by the Gateway, including when an older link names a different agent. Replies and side-question results from other agents are rejected, with existing attachment permissions unchanged.

> Agent execution, sessions and scheduled work share more of their existing preparation and cleanup code. These changes remove repeated lookups, temporary copies and unused imports while retaining current routing and recovery rules.

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
- [[Changes/OpenClaw/2026-09-23-23-memory-and-personalization-changes-in-v2026-9-6|23 Memory and Personalization changes in v2026.9.6]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-23-3-search-and-browsing-changes-in-v2026-9-6|3 Search and Browsing changes in v2026.9.6]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-23-19-interface-experience-changes-in-v2026-9-6|19 Interface Experience changes in v2026.9.6]] · Interface Experience
- [[Changes/OpenClaw/2026-09-23-9-automation-and-scheduling-changes-in-v2026-9-6|9 Automation and Scheduling changes in v2026.9.6]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-23-22-model-support-changes-in-v2026-9-6|22 Model Support changes in v2026.9.6]] · Model Support
- [[Changes/OpenClaw/2026-09-23-119-other-changes-in-v2026-9-6|119 other changes in v2026.9.6]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-09-23 · Microsoft 365 Copilot · [[Changes/Microsoft 365 Copilot/2026-09-23-integrated-extensibility-experience-capability-for-declarative-agents-for-micros|Integrated extensibility experience capability for declarative agents for Microsoft…]]
- Later: 2026-09-23 · Qoder · [[Changes/Qoder/2026-09-23-2-agent-mode-changes-in-qoder-0-4-1|2 Agent Mode changes in Qoder 0.4.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-23-3e2e1b&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-23-41-agent-mode-changes-in-v2026-9-6.md%0ACard%20ID%3A%20openclaw-2026-09-23-3e2e1b%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.6%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->