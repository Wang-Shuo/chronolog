---
card_id: openclaw-2026-09-19-2f1bc6
date: '2026-09-19'
description: 'OpenClaw · 2026-09-19 · Agent Mode: 72 changes in v2026.9.5 — OpenClaw
  2026.9.5 brings Atomic Updates that check the next version before switching over…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1171
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: fee4c9cecd6403234a29eb00096e263decfd98cb1230a224fea44ed1b24d891b
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-19-2f1bc6
  comparison: ''
  date: '2026-09-19'
  description: 'OpenClaw — v2026.9.5: 72 Agent Mode changes'
  evidence:
  - quote: OpenClaw 2026.9.5 brings Atomic Updates that check the next version before
      switching over, plugins you can install without restarting your Gateway, conversations
      you can share, GPT Live in your meetings and phone calls, browser pages you
      can work on alongside your agent, conversation archives you can revisit later,
      guided setup for your own team of specialist agents, everyday reliability improvements,
      and more.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Start with a chief of staff, researcher, writer and reviewer, or choose
      a single specialist. Guided setup can create the four-agent team, and New agent
      in the web UI offers the same roles through a proposal you approve before anything
      is created. Setup remembers your chosen coordinator if you need to resume. Choosing
      Skip creates the team offline, with AI access still to configure.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: If creation stops partway through, check openclaw agents list and repair
      the incomplete team before retrying. If all four members already exist, finish
      with openclaw onboard --workspace <workspace> without --team .
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Migrated multi-agent setups now keep their saved default after a restart,
      so integrations can find the intended agent again. The web UI saves and displays
      that same choice. If your agent list has no valid default, choose one with Set
      Default in the web UI. Choosing a default does not move your older workspaces
      or conversation data.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: The web UI makes it easier to find an agent, follow its work, and keep
      a conversation going while the rest of the page catches up.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: The new Agents overview brings recent activity and conversation previews
      together, with a direct link to each agent’s main chat. Turn on Show all agents
      for an optional team sidebar that groups conversations by agent. That choice
      is remembered in this browser for each Gateway, and agent creation remains available
      in Settings.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Activity keeps delegated subagent work with its parent conversation, so
      it no longer crowds out your conversations or inflates people counts. Switching
      agents also cancels obsolete archive-deletion confirmations from the previous
      agent.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: To give a conversation its own artwork, paste a custom SVG in Icon & color
      → Custom icon… , or ask your agent to set it. Artwork keeps its own colors and
      must be self-contained and no larger than 16 KiB decoded. Scripts, embedded
      documents, and external references are rejected.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Web chat also shows accepted queued follow-ups from CLI, TUI, native apps,
      and RPC clients while the agent is working. Labels such as via CLI describe
      the submitting app; they do not establish a person’s identity or grant permissions.
      If an interruption leaves input queued outside the saved conversation, resend
      it explicitly after restart. That queue is not replayed automatically.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Active chats and split panes make fewer routine requests for model information.
      Choosing a model, account, or agent runtime still refreshes that information
      promptly, as do credential and availability changes. Ordinary account usage
      remains recorded without making every connected web UI reload its model information.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Ask your agent to add a hosted HTTPS website to a session dashboard , expand
      it across the task area, and return through a named, pinned session. The browser
      also remembers layouts, panel choices, and dashboard tabs for up to 500 sessions.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Established Labs controls now live with their related settings, including
      Swarm and loop detection under Agent Defaults → Tools . Settings forms put readable
      controls and individual hints first, without repeating their defaults in a block
      of raw JSON.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Agent Files keeps unsaved edits when you switch agents, including their
      save-conflict checks. Save before leaving the Agents settings page, reloading
      the browser, or changing Gateway connections; these drafts are temporary.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: The conversation you open now loads before automatic background session
      lists. Long histories and chats with many child sessions need less repeated
      database work, and large session lists let other requests proceed while they
      load. Chat startup also avoids compression delays on busy Gateways.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Large session lists also reuse unchanged titles as messages arrive, choose
      the correct title after a reset, and keep child-session links in a consistent
      order. Opening an exact session link and preparing list pages now require less
      repeated work, including when conversations have many subagents.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Generating recaps sends the previous recap and bounded transcript excerpts
      through the owning agent’s utility model . These separate model calls may incur
      usage charges. Disabling utility routing stops new recaps, and a failed call
      does not fall back to the primary model.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: When you ask an agent to change a page, pane, or panel through screen controls
      , the change now stays in the browser that requested it. Your other tabs and
      other people’s dashboards keep their views. Reply also returns focus to the
      composer when a streamed update has redrawn the conversation.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Conversation archiving compresses older, inactive history while keeping
      it available to reopen later. Settings shows how much storage each agent’s conversations
      use, with a Run now control for archiving. Cold storage is off by default. Turn
      it on to archive eligible inactive history after 30 days, or change that interval
      without restarting. Opening or resuming an archived conversation restores its
      history and makes it searchable again, even if you have since turned archiving
      off.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: This release upgrades agent databases to schema 21 , which older builds
      cannot open. Make and verify a pre-upgrade backup that includes committed data
      still in the database journal, or WAL. Going back requires restoring that backup
      with its matching older build and loses work saved after the backup. Reinstalling
      an older package alone is insufficient. Do not change schema markers or delete
      database tables to force a downgrade. Users updating from 2026.9.2 must follow
      the manual schema-upgrade instructions .
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Triage can hand repair work to installed Muse Code, Grok Build, Cursor,
      Kimi Code, and Qwen Code, alongside its existing choices. Select one with openclaw
      triage --agent ; Cursor requires cursor-agent on your PATH. These choices extend
      explicitly requested repair assistance, while unattended recovery keeps its
      existing routes.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: With openclaw backup git create --all , healthy agents receive fresh snapshots
      while an unavailable configured agent keeps its previous Git backup, if one
      exists. The result warns that coverage is degraded because the retained snapshot
      is older. Explicit agent selection and runs with no copyable databases still
      fail.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Healthy agents can remain available while another agent's database checks
      finish. The affected agent is shown as degraded until preparation succeeds;
      even the default agent can remain unavailable while healthy peers serve. A responding
      Gateway therefore does not mean every agent is ready. Shared-state failures
      and uncertain database ownership can still block work. Stop the Gateway before
      Doctor repair or verified-backup restoration, then restart and check the affected
      agent.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Doctor also continues independent repairs when older agent folders contain
      conflicting files, preserving current files and existing SDK conversations.
      Databases awaiting relocation stay at their original location with their companion
      files. Inspect retained quarantines before removing them.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Eligible full startup checks can now inspect agent databases directly without
      copying their entire contents, while retaining fresh integrity, ownership, and
      migration checks. Recovery-sensitive databases , empty files, and incomplete
      journal families still need snapshots. Independent agent checks can run two
      at a time, which can increase peak temporary-storage use and disk activity.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Doctor repairs now preserve supported nested model and agent settings without
      flattening included files. Removing an explicit included default model policy
      keeps an empty policy so later aliases do not unexpectedly restrict model access.
      A later update failure can leave the candidate package installed after those
      include changes, so retain the native backups and follow the repair guidance.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Git installations report the built version and flag when it needs rebuilding
      to catch up with the checkout. Doctor also gives rebuild and restart guidance
      when the recorded build and checkout commits differ. That warning is advisory
      and stays quiet during updates. If an agent fails because OpenClaw was replaced
      while still running, its error explains that a restart is needed.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Setup and repair conversations now use your configured agent timeout instead
      of stopping after two minutes. The embedded helper also skips skills it cannot
      use. Set an explicit shorter agents.defaults.timeoutSeconds value when you want
      to limit these runs; the documented default is 48 hours, and 0 disables the
      deadline. See the setup and repair guide .
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Experimental room teams let several agents take part in one conversation.
      Messaging also improves replies, interactive questions and recovery after interruptions
      across supported channels.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Experimental room teams let you bring several configured agents into one
      conversation, address a particular specialist, and let the agents discuss their
      answers for a limited number of rounds. Discord and Slack replies and attachments
      now stay with the participant who answered. Extra rounds use more agent runs,
      and the discussion's active budget does not survive a restart. See broadcast
      groups for setup and limits.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Agents with message-tool access can now send messages and perform permitted
      actions across configured chat services without a separate cross-provider opt-in.
      This also changes existing installations that leave tools.message.crossContext.allowAcrossProviders
      unset. Other tool, account, channel, and provider permissions still apply.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: To keep services isolated, set tools.message.crossContext.allowAcrossProviders
      to false . To confine guarded actions to the current bound conversation, also
      set tools.message.crossContext.allowWithinProvider to false . Per-agent settings
      override global settings. CLI calls without a bound source conversation are
      not confined to one conversation by these controls, and separate shell and filesystem
      restrictions still matter. See cross-provider messaging guidance .
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: When Discord starts, saved threads reconnect to their agent conversations
      without holding up other Gateway work on the database lookup. Failed or canceled
      startup cleans up the pending thread setup, and presence greetings recheck the
      current settings before they start. Stopping an account waits for accepted introductions
      to finish their delivery and recording work, so shutdown can take longer while
      that work settles.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: LINE can bring photos sent together into one turn so your agent can consider
      the set, and supported questions in direct chats offer answer buttons. You can
      also enable native quoted replies or receive completed portions of an answer
      as they finish.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Telegram conversation titles include known forum topic names, and earlier
      text reaches the agent before later long-message fragments. An authorized /stop
      clears your pending input in that chat or topic. Agents can also discover supported
      persistent subagent conversations again, keeping follow-ups with the same helper
      when binding is enabled.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Replies on affected channels keep working after live settings changes without
      a restart. Queued replies and attachment cleanup keep using their original storage,
      even if settings change while they wait. Delayed replies and discovered conversations
      respect changes to the agent handling them, and follow-up messages waiting behind
      long replies avoid unnecessary timeout retries.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Supported channel previews now show readable progress notes, so you can
      see what your agent is doing while you wait. Slack and Telegram also remove
      abandoned previews after tool work while retaining the final answer or useful
      failure notice. Slack keeps a preview when someone has replied to it, preserving
      that part of the conversation. Your existing preview settings still control
      what appears.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Discord server-wide reads require an allowed server and unrestricted or
      wildcard channel access. Delegated agents do not get the filtered channel-list
      exception available to direct operators. Other actions and unverified installations
      keep their restrictions, and revoking access cannot recall a request already
      sent.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: When optional conversation indexing is off, the agent is now guided to
      use available tools for reading the original conversation before suggesting
      a settings change. Indexing stays opt-in, and existing tool permissions still
      apply. When indexing is enabled, excerpts from before and after a conversation
      reset stay separate. Normal synchronization rebuilds existing indexes once for
      this fix and can reuse cached embeddings.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Explicitly selected manual personal skills now work with workspace-only
      file access. Agents can read the selected revision's instructions and supporting
      files without enabling automatic invocation or opening access to unrelated files.
      Directory listing and changes to those files remain restricted.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: When you apply or reject a suggestion in Skill Workshop , its row updates
      as soon as the result is confirmed and stays consistent through refreshes and
      agent switches. Temporary confirmations disappear on time. If a result is uncertain,
      refresh and check before trying again. A changed suggestion still needs your
      review and another explicit action.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: If an older Workshop backup was left behind after moving a workspace, run
      openclaw doctor --fix . Doctor can recover it when exactly one agent's skills
      match all the recorded contents, then a Gateway restart clears the retained
      warning. Incomplete, changed, or ambiguous matches stay preserved for manual
      recovery . Do not edit the saved manifest or change your workspace to force
      a match.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: The sag speech skill now stays available with supported alternate credentials,
      such as SAG_API_KEY or an explicitly supplied key file. If it was previously
      disabled, run openclaw config set skills.entries.sag.enabled true and refresh
      Skills before your next agent turn. Ready means the executable is available;
      it does not verify credentials or successful speech generation.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: When a skill installer cannot find Homebrew on FreeBSD, the error now explains
      how to recover. Install the required tools manually through pkg or Ports on
      the computer running OpenClaw, then run openclaw skills check . Add --agent
      <id> to check a specific agent.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: The Google Workspace skill now tells agents to try your existing sign-in
      before asking you to set it up again. Updated guidance explains how to complete
      sign-in from a trusted shell when OpenClaw runs on a remote computer. Keep callback
      URLs and secrets out of chat, and enter callback URLs yourself in that shell
      rather than passing them through an agent tool.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: The bundled visualize skill helps agents create interactive explanations
      as one-off visuals or saved dashboards, and update existing widgets. Widgets
      can now use chart libraries such as D3 and fonts from approved public hosts
      .
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Android adds the same interaction to default, agent-main and dashboard
      chats, with channel conversations keeping their full transcript. Active and
      steered work stays expanded, and unanswered failures remain accessible. Folding
      changes the view without deleting conversation content.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: You can speak while GPT Live replies in supported Meet, Teams and Zoom
      meetings , and let it consult your OpenClaw agent during meetings or phone calls
      . Select Live explicitly for these surfaces. In Talk , unpinned sessions now
      choose Live using your configured OpenAI access. Existing model pins stay in
      place.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: An agent can continue from a progress message to tools and a final answer
      when a Responses provider explicitly says the turn is unfinished. You no longer
      need to send another prompt in that case, and cancellation and stop controls
      still apply.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Revoking the initiating device's authorization stops later scheduling changes
      from its admitted agent turn, including after disconnect. An ordinary disconnect
      does not revoke that authority, and already accepted changes keep their recorded
      outcomes. Existing schedules are not canceled by revoking their creator's token.
      A queued run can still be stopped before execution by later revocation.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Scheduled agents can read supported channels without an incoming chat,
      using either their operator permissions or their saved creator account. Eligible
      Discord jobs can also edit, delete, pin and unpin messages. Operator-created
      jobs can edit channels and threads through supported adapters; account-owned
      jobs need authorization from the actual requester in the owning Discord conversation.
      Current requester and bot permissions, enabled actions, target restrictions
      and the job's allowed tools still apply. Delivery settings do not grant access,
      and changing the default account does not replace the saved creator account.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: 'A parent agent can now review a subagent''s result privately , ask for
      more work, or stay silent before anything is automatically announced to a channel.
      Opt in with completionTarget: "parent" when spawning the subagent. A busy parent
      handles the result in a separate private turn after its current work, and resetting
      or removing the parent keeps the result from reaching a replacement session.
      Fast child results wait for the parent turn to settle; after a normal parent
      response, a ready result can proceed while siblings continue. Private processing
      also retains accurate timeout outcomes and available final details.'
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: The task inspector now shows whether a subagent is working, waiting or
      finished, and whether its result has reached the parent. You can inspect its
      activity and child dependencies beside the parent conversation without losing
      your draft. When a runtime cannot report current activity, the inspector leaves
      it unknown.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Agents can wait for selected tasks to finish or need attention. OpenClaw
      reduces a source of delays in subagent waits, task lists and cancellation checks
      when many past tasks are retained. Explicit message modes let them supply future
      context, steer supported active work, or start a follow-up turn. Ending a wait
      or reaching its time limit leaves the tasks running and their results available
      for delivery. The notify mode queues context for a future turn without waking
      the target or confirming it has read the message. That queued context can be
      evicted or lost on restart.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Agents can find conversations by owner, creator, project or workspace,
      filter for activity, and continue through matching results instead of mistaking
      the first page for the whole inventory. Metadata-only requests do not read transcripts
      or start sessions. These filters preserve existing access permissions; filters
      relative to the current user need a trusted identity, and current activity requires
      a Gateway connection. Results are a live view, so agents need to account for
      conversations changing between pages.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Work resumed after a background command finishes uses the normal agent
      timeout instead of the shorter heartbeat budget. ACP turns and approved-command
      continuations can use their configured execution budgets, resumed native subagents
      retain their saved timeout, and late replies can still be observed after an
      initial wait expires. Explicit limits and cancellation still apply, and that
      late-reply observation does not survive a Gateway restart.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Background commands still do not automatically wake a subagent. Collect
      their terminal results with process poll before yielding without another completion
      source, including after a requested stop. Confirmed requested stops with successful
      cleanup avoid false failure notices, while real timeouts and cleanup failures
      remain errors. Completion entries now explain the existing tools.exec.notifyOnExit=false
      setting for stopping automatic completion turns while keeping background commands.
      Check per-agent overrides; changed settings apply only to newly started commands,
      whose results you can collect with process poll or process log .
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: You can share a page in a local managed browser with your agent and use
      computer controls on supported local or cloud desktops. Cloud sessions also
      gain more ways to reuse prepared work and recover after interruptions.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: 'On desktop-enabled Linux cloud workers , agents can launch a graphical
      app with exec and use it on the same desktop. Use background: true for apps
      that need to stay open.'
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Supported window actions return a fresh screenshot and element references
      for the agent's next step. If input or the refresh fails, get a fresh observation
      before deciding what to do next. Input is not automatically replayed.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Agent browser previews stay readable during refresh, with progress on the
      reload button. Browser message-dispatch failures now close the affected connection
      without stopping unrelated Gateway work. The failed browser operation is not
      automatically retried.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Existing agent files are not copied. Each new session starts with its own
      Git history and remotes, and Git remains an internal requirement. Normal managed
      snapshots and recovery still apply; this does not add disposable workspaces
      or general multi-repository support.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Connected coding agents can recover from a stalled /reset or /new after
      the existing 15-second cleanup deadline, letting a fresh conversation proceed
      without restarting the Gateway. Old cleanup may continue in the background.
      Canceling queued or initializing ACP work also prevents unwanted provider submission
      through the repaired setup paths.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Finished subagent tasks and their linked flows also avoid redundant updates
      during idle Gateway restarts. Genuine corrections still persist, and failed
      notifications can still retry.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Workboard filters now work together, so you can narrow cards by status,
      priority, attention needed and recent completion, including on mobile. Switch
      from the default board to a list with aligned task details and collapsible status
      groups when you want to scan more work at once. The list-view choice is not
      saved. Clearing filters keeps your selected agent context; use the agent picker
      to return to All agents.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: In installations with many agents, 1Password item listings can skip unrelated
      access grants and avoid failures caused by damage in those grants. This requires
      a storage adapter that supports reading only the requesting agent's relevant
      grants. Listings still return metadata, with existing secret-access and approval
      rules in place.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Shared agent instructions now explicitly allow user-authorized email CLI
      and API actions under existing tool permissions and approvals. Replies to connected
      chat channels still use OpenClaw routing. This clarifies existing permissions;
      the separately reported native Codex email refusal remains unresolved.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Files passed to native subagents now live in OpenClaw-owned storage, with
      Docker and Podman children receiving read-only access to their own attachments.
      Use the file paths supplied to the child. Attachment-bearing spawns are refused
      on shared-scope sandboxes and unsupported backends, including SSH; spawns without
      attachments continue as before. Pre-upgrade attachments in child workspaces
      remain for operator cleanup. The subagent guide explains the supported configurations
      and changed paths.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Secure credential reads on Windows x64 verify ownership and access permissions
      using the matching native helper. If that helper is disabled, missing, or outdated,
      the read is refused. Restore auto mode or reinstall the matching helper without
      resetting your credentials. Native Windows ARM64 has no matching helper for
      these reads. See secure file operations for recovery guidance.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: OpenClaw does less repeated work when preparing long conversations, showing
      progress, and running agents in parallel. It makes fewer temporary copies without
      changing the conversation content, and requests for recent history, usage, or
      selected agent results skip older details they do not need.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Installations using the default concurrency limit can run more independent
      conversations while others wait for model or tool responses. The default now
      allows four main agent runs per available CPU, with at least eight slots—32
      on an eight-CPU host and 192 on a 48-CPU host. Each conversation still runs
      one turn at a time, and subagent and scheduled-job limits remain separate.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: In OpenClaw's built-in agent runtime, the system expert can now answer
      even when only one ordinary agent is allowed to run at a time. Cancelling the
      parent task can still leave queued expert work able to start. If a subagent
      was already paused before upgrading, send it a follow-up to resume it. Abandoned
      tasks cleared by maintenance follow the existing retention rules. Downgrading
      does not restore their earlier status or records already removed by retention.
      To return to an older binary, restore a verified pre-update backup into fresh
      state.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: If you answer only part of an agent's multi-part question, the chat now
      explains what needs correcting and keeps the question open. Send a complete
      answer using the question numbers or IDs. Authorized plain-text answers can
      reach the waiting run, save its tool result, and let it continue without waiting
      for the asking turn to finish. Partial answers are not saved as accepted answers.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 72-agent-mode-changes-in-v2026-9-5
  source_release: openclaw-2026-09-19-v2026-9-5-506f537c
  source_type: openclaw_changelog
  theme: agent-mode
  title: 72 Agent Mode changes in v2026.9.5
  type: change
related_changes:
- '[[Changes/Replit/2026-09-18-connect-custom-apis-to-agent|Connect custom APIs to
  Agent]]'
- '[[Changes/Claude Code/2026-09-19-added-an-auto-mode-server-row-to-status-showing-whether-this-session-s-auto-mode|Added
  an Auto mode server row to /status showing whether this session''s auto…]]'
- '[[Changes/Kimi Code/2026-09-19-the-agent-no-longer-assumes-the-current-working-directory-is-the-project-root|The
  agent no longer assumes the current working directory is the project root]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-19-v2026-9-5-506f537c|openclaw-2026-09-19-v2026-9-5-506f537c]]'
source_type: openclaw_changelog
theme: agent-mode
title: 72 Agent Mode changes in v2026.9.5
type: change
---

<!-- chronolog:begin region="header" -->
# 72 Agent Mode changes in v2026.9.5

**OpenClaw** · 2026-09-19 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.5) · from [[Releases/OpenClaw/openclaw-2026-09-19-v2026-9-5-506f537c|v2026.9.5]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> OpenClaw 2026.9.5 brings Atomic Updates that check the next version before switching over, plugins you can install without restarting your Gateway, conversations you can share, GPT Live in your meetings and phone calls, browser pages you can work on alongside your agent, conversation archives you can revisit later, guided setup for your own team of specialist agents, everyday reliability improvements, and more.

> Start with a chief of staff, researcher, writer and reviewer, or choose a single specialist. Guided setup can create the four-agent team, and New agent in the web UI offers the same roles through a proposal you approve before anything is created. Setup remembers your chosen coordinator if you need to resume. Choosing Skip creates the team offline, with AI access still to configure.

> If creation stops partway through, check openclaw agents list and repair the incomplete team before retrying. If all four members already exist, finish with openclaw onboard --workspace \<workspace> without --team .

> Migrated multi-agent setups now keep their saved default after a restart, so integrations can find the intended agent again. The web UI saves and displays that same choice. If your agent list has no valid default, choose one with Set Default in the web UI. Choosing a default does not move your older workspaces or conversation data.

> The web UI makes it easier to find an agent, follow its work, and keep a conversation going while the rest of the page catches up.

> The new Agents overview brings recent activity and conversation previews together, with a direct link to each agent’s main chat. Turn on Show all agents for an optional team sidebar that groups conversations by agent. That choice is remembered in this browser for each Gateway, and agent creation remains available in Settings.

> Activity keeps delegated subagent work with its parent conversation, so it no longer crowds out your conversations or inflates people counts. Switching agents also cancels obsolete archive-deletion confirmations from the previous agent.

> To give a conversation its own artwork, paste a custom SVG in Icon & color → Custom icon… , or ask your agent to set it. Artwork keeps its own colors and must be self-contained and no larger than 16 KiB decoded. Scripts, embedded documents, and external references are rejected.

> Web chat also shows accepted queued follow-ups from CLI, TUI, native apps, and RPC clients while the agent is working. Labels such as via CLI describe the submitting app; they do not establish a person’s identity or grant permissions. If an interruption leaves input queued outside the saved conversation, resend it explicitly after restart. That queue is not replayed automatically.

> Active chats and split panes make fewer routine requests for model information. Choosing a model, account, or agent runtime still refreshes that information promptly, as do credential and availability changes. Ordinary account usage remains recorded without making every connected web UI reload its model information.

> Ask your agent to add a hosted HTTPS website to a session dashboard , expand it across the task area, and return through a named, pinned session. The browser also remembers layouts, panel choices, and dashboard tabs for up to 500 sessions.

> Established Labs controls now live with their related settings, including Swarm and loop detection under Agent Defaults → Tools . Settings forms put readable controls and individual hints first, without repeating their defaults in a block of raw JSON.

> Agent Files keeps unsaved edits when you switch agents, including their save-conflict checks. Save before leaving the Agents settings page, reloading the browser, or changing Gateway connections; these drafts are temporary.

> The conversation you open now loads before automatic background session lists. Long histories and chats with many child sessions need less repeated database work, and large session lists let other requests proceed while they load. Chat startup also avoids compression delays on busy Gateways.

> Large session lists also reuse unchanged titles as messages arrive, choose the correct title after a reset, and keep child-session links in a consistent order. Opening an exact session link and preparing list pages now require less repeated work, including when conversations have many subagents.

> Generating recaps sends the previous recap and bounded transcript excerpts through the owning agent’s utility model . These separate model calls may incur usage charges. Disabling utility routing stops new recaps, and a failed call does not fall back to the primary model.

> When you ask an agent to change a page, pane, or panel through screen controls , the change now stays in the browser that requested it. Your other tabs and other people’s dashboards keep their views. Reply also returns focus to the composer when a streamed update has redrawn the conversation.

> Conversation archiving compresses older, inactive history while keeping it available to reopen later. Settings shows how much storage each agent’s conversations use, with a Run now control for archiving. Cold storage is off by default. Turn it on to archive eligible inactive history after 30 days, or change that interval without restarting. Opening or resuming an archived conversation restores its history and makes it searchable again, even if you have since turned archiving off.

> This release upgrades agent databases to schema 21 , which older builds cannot open. Make and verify a pre-upgrade backup that includes committed data still in the database journal, or WAL. Going back requires restoring that backup with its matching older build and loses work saved after the backup. Reinstalling an older package alone is insufficient. Do not change schema markers or delete database tables to force a downgrade. Users updating from 2026.9.2 must follow the manual schema-upgrade instructions .

> Triage can hand repair work to installed Muse Code, Grok Build, Cursor, Kimi Code, and Qwen Code, alongside its existing choices. Select one with openclaw triage --agent ; Cursor requires cursor-agent on your PATH. These choices extend explicitly requested repair assistance, while unattended recovery keeps its existing routes.

> With openclaw backup git create --all , healthy agents receive fresh snapshots while an unavailable configured agent keeps its previous Git backup, if one exists. The result warns that coverage is degraded because the retained snapshot is older. Explicit agent selection and runs with no copyable databases still fail.

> Healthy agents can remain available while another agent's database checks finish. The affected agent is shown as degraded until preparation succeeds; even the default agent can remain unavailable while healthy peers serve. A responding Gateway therefore does not mean every agent is ready. Shared-state failures and uncertain database ownership can still block work. Stop the Gateway before Doctor repair or verified-backup restoration, then restart and check the affected agent.

> Doctor also continues independent repairs when older agent folders contain conflicting files, preserving current files and existing SDK conversations. Databases awaiting relocation stay at their original location with their companion files. Inspect retained quarantines before removing them.

> Eligible full startup checks can now inspect agent databases directly without copying their entire contents, while retaining fresh integrity, ownership, and migration checks. Recovery-sensitive databases , empty files, and incomplete journal families still need snapshots. Independent agent checks can run two at a time, which can increase peak temporary-storage use and disk activity.

> Doctor repairs now preserve supported nested model and agent settings without flattening included files. Removing an explicit included default model policy keeps an empty policy so later aliases do not unexpectedly restrict model access. A later update failure can leave the candidate package installed after those include changes, so retain the native backups and follow the repair guidance.

> Git installations report the built version and flag when it needs rebuilding to catch up with the checkout. Doctor also gives rebuild and restart guidance when the recorded build and checkout commits differ. That warning is advisory and stays quiet during updates. If an agent fails because OpenClaw was replaced while still running, its error explains that a restart is needed.

> Setup and repair conversations now use your configured agent timeout instead of stopping after two minutes. The embedded helper also skips skills it cannot use. Set an explicit shorter agents.defaults.timeoutSeconds value when you want to limit these runs; the documented default is 48 hours, and 0 disables the deadline. See the setup and repair guide .

> Experimental room teams let several agents take part in one conversation. Messaging also improves replies, interactive questions and recovery after interruptions across supported channels.

> Experimental room teams let you bring several configured agents into one conversation, address a particular specialist, and let the agents discuss their answers for a limited number of rounds. Discord and Slack replies and attachments now stay with the participant who answered. Extra rounds use more agent runs, and the discussion's active budget does not survive a restart. See broadcast groups for setup and limits.

> Agents with message-tool access can now send messages and perform permitted actions across configured chat services without a separate cross-provider opt-in. This also changes existing installations that leave tools.message.crossContext.allowAcrossProviders unset. Other tool, account, channel, and provider permissions still apply.

> To keep services isolated, set tools.message.crossContext.allowAcrossProviders to false . To confine guarded actions to the current bound conversation, also set tools.message.crossContext.allowWithinProvider to false . Per-agent settings override global settings. CLI calls without a bound source conversation are not confined to one conversation by these controls, and separate shell and filesystem restrictions still matter. See cross-provider messaging guidance .

> When Discord starts, saved threads reconnect to their agent conversations without holding up other Gateway work on the database lookup. Failed or canceled startup cleans up the pending thread setup, and presence greetings recheck the current settings before they start. Stopping an account waits for accepted introductions to finish their delivery and recording work, so shutdown can take longer while that work settles.

> LINE can bring photos sent together into one turn so your agent can consider the set, and supported questions in direct chats offer answer buttons. You can also enable native quoted replies or receive completed portions of an answer as they finish.

> Telegram conversation titles include known forum topic names, and earlier text reaches the agent before later long-message fragments. An authorized /stop clears your pending input in that chat or topic. Agents can also discover supported persistent subagent conversations again, keeping follow-ups with the same helper when binding is enabled.

> Replies on affected channels keep working after live settings changes without a restart. Queued replies and attachment cleanup keep using their original storage, even if settings change while they wait. Delayed replies and discovered conversations respect changes to the agent handling them, and follow-up messages waiting behind long replies avoid unnecessary timeout retries.

> Supported channel previews now show readable progress notes, so you can see what your agent is doing while you wait. Slack and Telegram also remove abandoned previews after tool work while retaining the final answer or useful failure notice. Slack keeps a preview when someone has replied to it, preserving that part of the conversation. Your existing preview settings still control what appears.

> Discord server-wide reads require an allowed server and unrestricted or wildcard channel access. Delegated agents do not get the filtered channel-list exception available to direct operators. Other actions and unverified installations keep their restrictions, and revoking access cannot recall a request already sent.

> When optional conversation indexing is off, the agent is now guided to use available tools for reading the original conversation before suggesting a settings change. Indexing stays opt-in, and existing tool permissions still apply. When indexing is enabled, excerpts from before and after a conversation reset stay separate. Normal synchronization rebuilds existing indexes once for this fix and can reuse cached embeddings.

> Explicitly selected manual personal skills now work with workspace-only file access. Agents can read the selected revision's instructions and supporting files without enabling automatic invocation or opening access to unrelated files. Directory listing and changes to those files remain restricted.

> When you apply or reject a suggestion in Skill Workshop , its row updates as soon as the result is confirmed and stays consistent through refreshes and agent switches. Temporary confirmations disappear on time. If a result is uncertain, refresh and check before trying again. A changed suggestion still needs your review and another explicit action.

> If an older Workshop backup was left behind after moving a workspace, run openclaw doctor --fix . Doctor can recover it when exactly one agent's skills match all the recorded contents, then a Gateway restart clears the retained warning. Incomplete, changed, or ambiguous matches stay preserved for manual recovery . Do not edit the saved manifest or change your workspace to force a match.

> The sag speech skill now stays available with supported alternate credentials, such as SAG_API_KEY or an explicitly supplied key file. If it was previously disabled, run openclaw config set skills.entries.sag.enabled true and refresh Skills before your next agent turn. Ready means the executable is available; it does not verify credentials or successful speech generation.

> When a skill installer cannot find Homebrew on FreeBSD, the error now explains how to recover. Install the required tools manually through pkg or Ports on the computer running OpenClaw, then run openclaw skills check . Add --agent \<id> to check a specific agent.

> The Google Workspace skill now tells agents to try your existing sign-in before asking you to set it up again. Updated guidance explains how to complete sign-in from a trusted shell when OpenClaw runs on a remote computer. Keep callback URLs and secrets out of chat, and enter callback URLs yourself in that shell rather than passing them through an agent tool.

> The bundled visualize skill helps agents create interactive explanations as one-off visuals or saved dashboards, and update existing widgets. Widgets can now use chart libraries such as D3 and fonts from approved public hosts .

> Android adds the same interaction to default, agent-main and dashboard chats, with channel conversations keeping their full transcript. Active and steered work stays expanded, and unanswered failures remain accessible. Folding changes the view without deleting conversation content.

> You can speak while GPT Live replies in supported Meet, Teams and Zoom meetings , and let it consult your OpenClaw agent during meetings or phone calls . Select Live explicitly for these surfaces. In Talk , unpinned sessions now choose Live using your configured OpenAI access. Existing model pins stay in place.

> An agent can continue from a progress message to tools and a final answer when a Responses provider explicitly says the turn is unfinished. You no longer need to send another prompt in that case, and cancellation and stop controls still apply.

> Revoking the initiating device's authorization stops later scheduling changes from its admitted agent turn, including after disconnect. An ordinary disconnect does not revoke that authority, and already accepted changes keep their recorded outcomes. Existing schedules are not canceled by revoking their creator's token. A queued run can still be stopped before execution by later revocation.

> Scheduled agents can read supported channels without an incoming chat, using either their operator permissions or their saved creator account. Eligible Discord jobs can also edit, delete, pin and unpin messages. Operator-created jobs can edit channels and threads through supported adapters; account-owned jobs need authorization from the actual requester in the owning Discord conversation. Current requester and bot permissions, enabled actions, target restrictions and the job's allowed tools still apply. Delivery settings do not grant access, and changing the default account does not replace the saved creator account.

> A parent agent can now review a subagent's result privately , ask for more work, or stay silent before anything is automatically announced to a channel. Opt in with completionTarget: "parent" when spawning the subagent. A busy parent handles the result in a separate private turn after its current work, and resetting or removing the parent keeps the result from reaching a replacement session. Fast child results wait for the parent turn to settle; after a normal parent response, a ready result can proceed while siblings continue. Private processing also retains accurate timeout outcomes and available final details.

> The task inspector now shows whether a subagent is working, waiting or finished, and whether its result has reached the parent. You can inspect its activity and child dependencies beside the parent conversation without losing your draft. When a runtime cannot report current activity, the inspector leaves it unknown.

> Agents can wait for selected tasks to finish or need attention. OpenClaw reduces a source of delays in subagent waits, task lists and cancellation checks when many past tasks are retained. Explicit message modes let them supply future context, steer supported active work, or start a follow-up turn. Ending a wait or reaching its time limit leaves the tasks running and their results available for delivery. The notify mode queues context for a future turn without waking the target or confirming it has read the message. That queued context can be evicted or lost on restart.

> Agents can find conversations by owner, creator, project or workspace, filter for activity, and continue through matching results instead of mistaking the first page for the whole inventory. Metadata-only requests do not read transcripts or start sessions. These filters preserve existing access permissions; filters relative to the current user need a trusted identity, and current activity requires a Gateway connection. Results are a live view, so agents need to account for conversations changing between pages.

> Work resumed after a background command finishes uses the normal agent timeout instead of the shorter heartbeat budget. ACP turns and approved-command continuations can use their configured execution budgets, resumed native subagents retain their saved timeout, and late replies can still be observed after an initial wait expires. Explicit limits and cancellation still apply, and that late-reply observation does not survive a Gateway restart.

> Background commands still do not automatically wake a subagent. Collect their terminal results with process poll before yielding without another completion source, including after a requested stop. Confirmed requested stops with successful cleanup avoid false failure notices, while real timeouts and cleanup failures remain errors. Completion entries now explain the existing tools.exec.notifyOnExit=false setting for stopping automatic completion turns while keeping background commands. Check per-agent overrides; changed settings apply only to newly started commands, whose results you can collect with process poll or process log .

> You can share a page in a local managed browser with your agent and use computer controls on supported local or cloud desktops. Cloud sessions also gain more ways to reuse prepared work and recover after interruptions.

> On desktop-enabled Linux cloud workers , agents can launch a graphical app with exec and use it on the same desktop. Use background: true for apps that need to stay open.

> Supported window actions return a fresh screenshot and element references for the agent's next step. If input or the refresh fails, get a fresh observation before deciding what to do next. Input is not automatically replayed.

> Agent browser previews stay readable during refresh, with progress on the reload button. Browser message-dispatch failures now close the affected connection without stopping unrelated Gateway work. The failed browser operation is not automatically retried.

> Existing agent files are not copied. Each new session starts with its own Git history and remotes, and Git remains an internal requirement. Normal managed snapshots and recovery still apply; this does not add disposable workspaces or general multi-repository support.

> Connected coding agents can recover from a stalled /reset or /new after the existing 15-second cleanup deadline, letting a fresh conversation proceed without restarting the Gateway. Old cleanup may continue in the background. Canceling queued or initializing ACP work also prevents unwanted provider submission through the repaired setup paths.

> Finished subagent tasks and their linked flows also avoid redundant updates during idle Gateway restarts. Genuine corrections still persist, and failed notifications can still retry.

> Workboard filters now work together, so you can narrow cards by status, priority, attention needed and recent completion, including on mobile. Switch from the default board to a list with aligned task details and collapsible status groups when you want to scan more work at once. The list-view choice is not saved. Clearing filters keeps your selected agent context; use the agent picker to return to All agents.

> In installations with many agents, 1Password item listings can skip unrelated access grants and avoid failures caused by damage in those grants. This requires a storage adapter that supports reading only the requesting agent's relevant grants. Listings still return metadata, with existing secret-access and approval rules in place.

> Shared agent instructions now explicitly allow user-authorized email CLI and API actions under existing tool permissions and approvals. Replies to connected chat channels still use OpenClaw routing. This clarifies existing permissions; the separately reported native Codex email refusal remains unresolved.

> Files passed to native subagents now live in OpenClaw-owned storage, with Docker and Podman children receiving read-only access to their own attachments. Use the file paths supplied to the child. Attachment-bearing spawns are refused on shared-scope sandboxes and unsupported backends, including SSH; spawns without attachments continue as before. Pre-upgrade attachments in child workspaces remain for operator cleanup. The subagent guide explains the supported configurations and changed paths.

> Secure credential reads on Windows x64 verify ownership and access permissions using the matching native helper. If that helper is disabled, missing, or outdated, the read is refused. Restore auto mode or reinstall the matching helper without resetting your credentials. Native Windows ARM64 has no matching helper for these reads. See secure file operations for recovery guidance.

> OpenClaw does less repeated work when preparing long conversations, showing progress, and running agents in parallel. It makes fewer temporary copies without changing the conversation content, and requests for recent history, usage, or selected agent results skip older details they do not need.

> Installations using the default concurrency limit can run more independent conversations while others wait for model or tool responses. The default now allows four main agent runs per available CPU, with at least eight slots—32 on an eight-CPU host and 192 on a 48-CPU host. Each conversation still runs one turn at a time, and subagent and scheduled-job limits remain separate.

> In OpenClaw's built-in agent runtime, the system expert can now answer even when only one ordinary agent is allowed to run at a time. Cancelling the parent task can still leave queued expert work able to start. If a subagent was already paused before upgrading, send it a follow-up to resume it. Abandoned tasks cleared by maintenance follow the existing retention rules. Downgrading does not restore their earlier status or records already removed by retention. To return to an older binary, restore a verified pre-update backup into fresh state.

> If you answer only part of an agent's multi-part question, the chat now explains what needs correcting and keeps the question open. Send a complete answer using the question numbers or IDs. Authorized plain-text answers can reach the waiting run, save its tool result, and let it continue without waiting for the asking turn to finish. Partial answers are not saved as accepted answers.

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
- [[Changes/OpenClaw/2026-09-19-21-editor-experience-changes-in-v2026-9-5|21 Editor Experience changes in v2026.9.5]] · Editor Experience
- [[Changes/OpenClaw/2026-09-19-28-model-support-changes-in-v2026-9-5|28 Model Support changes in v2026.9.5]] · Model Support
- [[Changes/OpenClaw/2026-09-19-39-safety-and-privacy-changes-in-v2026-9-5|39 Safety and Privacy changes in v2026.9.5]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-19-14-automation-and-scheduling-changes-in-v2026-9-5|14 Automation and Scheduling changes in v2026.9.5]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-19-32-interface-experience-changes-in-v2026-9-5|32 Interface Experience changes in v2026.9.5]] · Interface Experience
- [[Changes/OpenClaw/2026-09-19-you-can-now-set-the-approval-reviewer-s-reasoning-and-optional-fast-mode-indepen|Set the approval reviewer's reasoning and optional Fast mode independently…]] · Agent Mode
- [[Changes/OpenClaw/2026-09-19-you-can-now-install-the-cli-on-freebsd-with-install-cli-sh-using-system-node-and|Install the CLI on FreeBSD with install-cli.sh using system Node and npm]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-19-6-pricing-model-changes-in-v2026-9-5|6 Pricing Model changes in v2026.9.5]] · Pricing Model
- [[Changes/OpenClaw/2026-09-19-28-account-and-access-changes-in-v2026-9-5|28 Account and Access changes in v2026.9.5]] · Account and Access
- [[Changes/OpenClaw/2026-09-19-31-memory-and-personalization-changes-in-v2026-9-5|31 Memory and Personalization changes in v2026.9.5]] · Memory and Personalization
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
## Nearby in Agent Mode

- Earlier: 2026-09-19 · Kimi Code · [[Changes/Kimi Code/2026-09-19-the-agent-no-longer-assumes-the-current-working-directory-is-the-project-root|The agent no longer assumes the current working directory is the project root]]
- Later: 2026-09-21 · Devin · [[Changes/Devin/2026-09-21-swe-2-research-preview-in-the-agent-selector|SWE-2 Research Preview in the Agent Selector]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-19-2f1bc6&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-19-72-agent-mode-changes-in-v2026-9-5.md%0ACard%20ID%3A%20openclaw-2026-09-19-2f1bc6%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.5%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->