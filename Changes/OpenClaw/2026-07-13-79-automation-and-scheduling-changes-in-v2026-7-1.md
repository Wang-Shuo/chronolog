---
card_id: openclaw-2026-07-13-5fba08
date: '2026-07-13'
description: 'OpenClaw · 2026-07-13 · Automation and Scheduling: 79 changes in v2026.7.1
  — Control UI Quick Create now lets users choose a model for an agent-turn cron job…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-change-gain-with-volume-automation|Change
    gain, with volume automation]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2490
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: automation-scheduling
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b6d1f66e60b153bbb90c6e283037614d3f29168af84f4f16afd8745b73c106d7
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-07-13-5fba08
  comparison: ''
  date: '2026-07-13'
  description: 'OpenClaw — v2026.7.1: 79 Automation and Scheduling changes'
  evidence:
  - quote: 'Control UI Quick Create now lets users choose a model for an agent-turn
      cron job and shows whether existing jobs use that model or the default. #95341
      Thanks @ly85206559.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Mounted deep links, Set Default, authenticated avatars, cron alerts, and
      Workboard scrolling now behave correctly again across the Control UI. #100106'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The Control UI Cron Jobs page now uses compact summaries, clear status
      cues, expandable details, and an overflow menu so large job lists are faster
      to review. #100646'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Non-English Control UI users now see translated cron overflow-menu and
      "run if due" labels, including the assistive label for more actions. 2585d6b
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Clicking a cron job''s History button now gives immediate feedback and
      scrolls directly to that job''s updated run history. #96281 Thanks @wyf027,
      @yzhong52.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Autonomous session history now keeps an earlier failed cron or scheduled
      turn marked as an error even after a later turn succeeds or the page reloads.
      #100514 Thanks @qingminglong.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Discord replies, cron reports, and other outbound messages are less likely
      to disappear during a brief Gateway reconnect, without replaying chunks or media
      Discord already accepted. #100896 Thanks @tiffanychum.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: A repeatedly crashing supervised Gateway now leaves a stable control process
      available for inspection and repair instead of trapping operators in a restart
      loop. a18708c Thanks @obviyus.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'A cron job can now watch a build, deploy, script, or other command and
      resume the originating workflow with its exit code and recent output when it
      finishes. #92037 Thanks @anagnorisis2peripeteia.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Cron declarations can now be safely reapplied without duplicate jobs or
      lost history, while ownership, next run, latest result, delivery, and failure
      notifications are easier to inspect. #100480'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Cron jobs can now watch an outside condition and run their real payload
      only when that state changes, avoiding full agent wakeups on unchanged polls.
      #101195'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Adding a named Discord account no longer knocks a SecretRef-backed default
      account offline or into a restart loop. #96401 Thanks @849261680.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Cron summaries, Teams and Slack replies, and other embedded assistant
      responses no longer expose provider reasoning markers such as &lt;/mm:think&gt;
      . #101036 Thanks @velanir-ai-manager.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Cron and outbound channel sends no longer report success without a usable
      platform receipt, making missing notifications show as not delivered or suppressed
      instead of falsely delivered. #79811 Thanks @indulgeback.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Telegram automations can now tell from platform metadata whether a sender
      is a bot, making routing and classification less dependent on usernames or naming
      conventions. #96810 Thanks @lin-hongkuan, @ohyeah521.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Zalo operators can send proactive CLI or scripted messages to valid nonnumeric
      chat_id values without an Unknown target rejection. #101548 Thanks @goutamadwant.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Replay-safe model timeouts can now advance to the next configured provider,
      letting agent, chat, and cron runs recover without repeating work that may have
      side effects. #96142 Thanks @brokemac79, @riazrahaman.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Isolated cron jobs can now use models supplied by enabled bundled plugins
      without failing as unknown or silently resolving to the wrong provider. #96070
      Thanks @sallyom, @sunnyshu0925.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Dreaming now keeps deleted or reset transcript archives and cron-created
      child conversations out of its learned session set, reducing duplicate history
      and automation noise without removing retained archives from historical search.
      #96517 Thanks @adam-researchh, @jalehman, @xialonglee.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'openclaw sessions cleanup --fix-missing now preserves fresh cron sessions
      with valid transcripts and clearly reports repaired entries. #97495 Thanks @qingminglong.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Recurring provider-CLI cron jobs and local openclaw agent runs now keep
      their existing provider conversation across the daily reset boundary instead
      of silently losing context. #98356 Thanks @yetval.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Small-context local models can now begin and continue conversations without
      immediately entering an overflow-compaction loop before useful prompt space
      is available. #100621 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Long agent prompt data containing emoji or other paired Unicode characters
      now stays well-formed when capped, avoiding broken text in agent and automation
      context. #101303 Thanks @alix-007.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Archived memories around user messages that begin with [cron:] remain
      searchable after a session reset or deletion, while genuine cron-generated archives
      stay hidden. #101322 Thanks @ly-wang19.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Timed-out cron jobs, expired agent requests, and disconnected HTTP clients
      now stop promptly instead of spending more time and provider calls on model
      fallback. #62682 Thanks @altaywtf, @cinapbot, @simonusa.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Isolated cron jobs can announce a cross-session result without feeding
      the recipient''s reply back into the cron run and creating duplicate message
      loops. #92283 Related #92257 . Thanks @harjothkhara, @nailujac, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Heartbeat and cron work on macOS and Linux is less likely to fail with
      Unknown system error -11 when reconnects overlap session or workspace updates.
      #100389 Thanks @ogarciarevett.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Agents using OpenClaw''s cron tools are now limited to their own scheduled
      jobs and session targets, while operator-managed cron remains unchanged and
      mixed-version setups fail closed with an openclaw gateway restart instruction.
      #96883 Thanks @joshavant.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Cron wake actions started by an agent now remain within that agent''s
      own session lanes, reducing the chance of waking another agent''s conversation.
      #97949 Thanks @eleqtrizit.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Failed cron webhooks no longer forward raw command summaries or diagnostics
      that may contain setup prompts, codes, or secret-like output. 1d17263 Thanks
      @joshavant.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Non-owner Gateway chat users are no longer offered the protected cron
      , gateway , or nodes control tools, even when those tools are otherwise allowlisted.
      #102030 Thanks @pgondhi987.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Browser automation now keeps Chrome control traffic tied to the configured
      or explicitly allowed CDP host, reducing the risk that a discovered debugger
      address redirects credentials or control elsewhere. #101171'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android notification automations now queue accepted events during Gateway
      connection or reconnection and deliver them in order once the link is ready.
      #92602 Related #79552 . Thanks @ashishpatel26, @hectorrp13.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Supported non-English Android builds now translate more cron inspection,
      delivery error, copy feedback, default-state, and agent request details. d83ee4c
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Google Meet join, creation, talk-back, transcription, and related automation
      now work across browser and account languages by using English in OpenClaw-controlled
      Meet tabs. #89671 Thanks @unayung.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'openclaw update on Windows now prevents the managed Gateway Scheduled
      Task from relaunching during package replacement, avoiding partially updated
      or mixed-version processes. #100757 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Windows Gateway setup now detects when Task Scheduler exits without starting
      a listener and can use the existing fallback launch without creating a duplicate
      if startup is merely late. #76245'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'A timeout while one isolated cron job is setting up no longer restarts
      the Gateway or interrupts unrelated agent and scheduled work. #96396 Thanks
      @849261680, @brycemurray, @velvet-shark.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Operators can run openclaw doctor --lint --all to include every opt-in
      diagnostic check without changing the behavior of existing doctor --lint automation.
      #96471 Thanks @giodl73-repo.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Default cron failure alerts enabled with openclaw cron edit &lt;job&gt;
      --failure-alert now survive Gateway restarts instead of silently disappearing
      after reload. #96615 Thanks @liuhao1024.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'openclaw doctor now warns when cron jobs target channels whose plugins
      are inactive, letting operators correct delivery before the next scheduled run
      fails. #98184 Thanks @masatohoshino, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Docker and bind-mount installations can finish legacy cron migration across
      filesystem boundaries, with actionable warnings and duplicate-safe retries when
      cleanup cannot complete. #98217 Thanks @masatohoshino.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'openclaw doctor now explains cron jobs that still look in flight after
      an interrupted Gateway run and how those leftover markers are cleared on the
      next start. #98620 Thanks @masatohoshino.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Doctor now warns when enabled cron jobs are stuck in repeated failures
      without configured alerts, while healthy and below-threshold jobs stay quiet.
      #99606 Thanks @masatohoshino.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'openclaw tasks maintenance --apply now preserves active cron session history
      even when job IDs contain spaces, capitals, punctuation, or explicit session
      keys. #96352 Thanks @ly-wang19, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'openclaw cron add now rejects invalid --no-output-timeout-seconds and
      --output-max-bytes values immediately instead of silently creating a command
      job without the requested limits. #96516 Thanks @zhangguiping-xydt.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'openclaw config unset now explains when a visible value is an inherited
      runtime default that is not stored in the user''s config, avoiding an unproductive
      loop between config get and config unset while leaving failed attempts unchanged.
      #96557 Thanks @moeghashim.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Human-readable cron list and cron show output now reveals repeated failure
      streaks such as error (12x) while leaving JSON status values unchanged. #99602
      Thanks @masatohoshino.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Operators can opt into core/doctor/legacy-cron-store to find legacy cron
      data that needs attention without the lint check changing any stored state.
      #99211 Thanks @giodl73-repo.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Matrix documentation now explains progress streaming, room-specific mention
      matching, per-room enablement, and bot-loop safeguards that operators can configure.
      #98318 Thanks @vincentkoc, @wm0018.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Official OpenClaw docs now help operators and plugin authors handle credentials
      safely, preflight cron jobs that use local-provider fallbacks, apply Talk timing
      defaults, configure MiniMax providers and models, and copy a complete minimal
      plugin package with the required dependency metadata. #100182'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Scheduled automation retains intended models, timing, state, and delivery
      across more restarts and edits. Tool calls and results also recover more cleanly
      from timeouts, malformed content, oversized output, and interrupted work instead
      of leaving a task looking complete when its usable result was lost.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Browser automation can now act on tabs by suggested ID, tab ID, label,
      or unique prefix without false target-mismatch failures. #96178 Thanks @zengwen-dt.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Cron jobs with a valid future run exactly on a second boundary now keep
      that scheduled time instead of being incorrectly treated as stale and rebased.
      #81731 Thanks @vincentkoc, @yashkot007.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Isolated agentTurn cron jobs can recover from temporarily mismatched runtime
      artifacts instead of failing at startup with a sourceReplyDeliveryMode error.
      #85249 Thanks @jerry-xin.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'openclaw tasks maintenance --apply can now repair false lost-task records
      when durable cron history proves the run completed successfully. #86088 Thanks
      @altaywtf, @liaoandi.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Scheduled agent jobs now warn when ANNOUNCE_SKIP suppresses a cron completion,
      making missing reports and partial output easier to diagnose. #90566 Related
      #68561 . Thanks @mibslee, @sahibzada-allahyar.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Catch-up cron jobs deferred briefly after startup are no longer skipped
      merely because an operator checks cron status before they fire. #94022 Related
      #93935 . Thanks @richchen01, @vincentkoc, @yetval.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Timed-out or cancelled isolated cron runs now retain their provider, model,
      and session details in cron_run_logs , making failed jobs easier to trace. #95943
      Related #95873 . Thanks @luke-renjoy, @zengwen-dt.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Editing a recurring cron job no longer skips a run that is already due
      or shifts an unchanged interval schedule to the edit time. #96159 Thanks @yetval.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Clearing a saved Model or Thinking/Effort override in the Cron Control
      UI now truly restores inherited defaults, with --clear-thinking available from
      the CLI. #96293 Related #96287 . Thanks @takamasa-aiso, @zengwen-dt.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'CLI-backed workers from isolated cron jobs now exit after completion instead
      of accumulating and slowing the host and Gateway. #97227 Thanks @vianne-droid,
      @xialonglee, @yusukeit0.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Long cron failure alerts now preserve emoji and other supplementary Unicode
      characters instead of ending with a broken replacement symbol. #97298 Thanks
      @zenglingbiao.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Scheduled jobs can deliver to a live chat without blocking replies or
      mixing background work into its transcript, and operators can clear stale childless
      cron tasks without cancelling active session-backed runs. #98755 Related #98121
      . Thanks @ethansk, @obviyus.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Recurring cron jobs created for current or session:&lt;id&gt; once again
      carry their selected conversation history into later runs, while isolated jobs
      still start clean. #98947 Thanks @ethansk, @obviyus.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Failed cron add , cron update , and cron remove commands now leave the
      running scheduler unchanged, so live jobs match the saved configuration and
      reported result. #99960 Thanks @masatohoshino, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Browser automation attached to an existing Chrome session now stops with
      a bounded error when Chrome crashes or a request is cancelled, and later requests
      can reconnect cleanly. #101454 Thanks @aniruddhaadak80.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Cron job updates can now remove a job-specific fallback model setting
      so scheduled runs inherit the global defaults again without recreating the job.
      #100801 Thanks @sunnyshu0925.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'openclaw cron edit now finds jobs more reliably and with less delay on
      Gateways that contain many scheduled jobs, including --exact and timeout-only
      edits. #100836 Thanks @machine3at, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Editing a cron payload with --no-best-effort-deliver no longer silently
      changes the job''s delivery mode to announcements. #100846 Thanks @machine3at.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Using openclaw cron edit &lt;id&gt; --no-best-effort-deliver on an older
      detached job no longer accidentally suppresses its completion announcement.
      #101027'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Agent and MCP cron requests using mixed-case command labels now fail closed
      instead of slipping past the restriction on shell-backed agent cron jobs. #101350
      Thanks @pgondhi987.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Replies now correctly confirm reminders scheduled through commands such
      as openclaw cron add instead of also claiming that no reminder was created.
      #101807 Thanks @bryantegomoh, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Standardized text-pattern escaping across maintainer automation to reduce
      duplication and future inconsistencies. #99778 Thanks @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Reduced unnecessary waiting in Docker scheduler coverage without changing
      runtime scheduling behavior. #99988'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Aligned documentation for environment protection, scheduled-task fallback
      checks, and Talk silence defaults without changing behavior. #100186'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Stabilized Windows startup fallback coverage and ensured scheduler changes
      reach the appropriate validation. #101223'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Reduced unnecessary internal script interfaces to make repository automation
      easier to understand and maintain. #101892 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Reduced unused internal types in repository automation, improving maintainability
      without changing commands. #101917 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 79-automation-and-scheduling-changes-in-v2026-7-1
  source_release: openclaw-2026-07-13-v2026-7-1-c2063718
  source_type: openclaw_changelog
  theme: automation-scheduling
  title: 79 Automation and Scheduling changes in v2026.7.1
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-07-09-work-can-also-keep-projects-moving-through-scheduled-tasks-that-run-once-repeat-2d6910|Work
  can also keep projects moving through Scheduled Tasks that run once, repeat…]]'
- '[[Changes/Superwhisper/2026-07-10-added-new-deep-links-to-start-and-stop-recording-making-it-easier-to-control-sup|Added
  new deep links to start and stop recording, making it easier to control…]]'
- '[[Changes/Kimi Code/2026-07-12-keep-kimi-p-runs-alive-after-a-turn-ends-while-a-goal-is-still-active-or-a-cron|Keep
  kimi -p runs alive after a turn ends while a goal is still active or a cron…]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-07-13-v2026-7-1-c2063718|openclaw-2026-07-13-v2026-7-1-c2063718]]'
source_type: openclaw_changelog
theme: automation-scheduling
title: 79 Automation and Scheduling changes in v2026.7.1
type: change
---

<!-- chronolog:begin region="header" -->
# 79 Automation and Scheduling changes in v2026.7.1

**OpenClaw** · 2026-07-13 · [[Themes/automation-scheduling|Automation and Scheduling]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.7.1) · from [[Releases/OpenClaw/openclaw-2026-07-13-v2026-7-1-c2063718|v2026.7.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Control UI Quick Create now lets users choose a model for an agent-turn cron job and shows whether existing jobs use that model or the default. #95341 Thanks @ly85206559.

> Mounted deep links, Set Default, authenticated avatars, cron alerts, and Workboard scrolling now behave correctly again across the Control UI. #100106

> The Control UI Cron Jobs page now uses compact summaries, clear status cues, expandable details, and an overflow menu so large job lists are faster to review. #100646

> Non-English Control UI users now see translated cron overflow-menu and "run if due" labels, including the assistive label for more actions. 2585d6b

> Clicking a cron job's History button now gives immediate feedback and scrolls directly to that job's updated run history. #96281 Thanks @wyf027, @yzhong52.

> Autonomous session history now keeps an earlier failed cron or scheduled turn marked as an error even after a later turn succeeds or the page reloads. #100514 Thanks @qingminglong.

> Discord replies, cron reports, and other outbound messages are less likely to disappear during a brief Gateway reconnect, without replaying chunks or media Discord already accepted. #100896 Thanks @tiffanychum.

> A repeatedly crashing supervised Gateway now leaves a stable control process available for inspection and repair instead of trapping operators in a restart loop. a18708c Thanks @obviyus.

> A cron job can now watch a build, deploy, script, or other command and resume the originating workflow with its exit code and recent output when it finishes. #92037 Thanks @anagnorisis2peripeteia.

> Cron declarations can now be safely reapplied without duplicate jobs or lost history, while ownership, next run, latest result, delivery, and failure notifications are easier to inspect. #100480

> Cron jobs can now watch an outside condition and run their real payload only when that state changes, avoiding full agent wakeups on unchanged polls. #101195

> Adding a named Discord account no longer knocks a SecretRef-backed default account offline or into a restart loop. #96401 Thanks @849261680.

> Cron summaries, Teams and Slack replies, and other embedded assistant responses no longer expose provider reasoning markers such as &lt;/mm:think&gt; . #101036 Thanks @velanir-ai-manager.

> Cron and outbound channel sends no longer report success without a usable platform receipt, making missing notifications show as not delivered or suppressed instead of falsely delivered. #79811 Thanks @indulgeback.

> Telegram automations can now tell from platform metadata whether a sender is a bot, making routing and classification less dependent on usernames or naming conventions. #96810 Thanks @lin-hongkuan, @ohyeah521.

> Zalo operators can send proactive CLI or scripted messages to valid nonnumeric chat_id values without an Unknown target rejection. #101548 Thanks @goutamadwant.

> Replay-safe model timeouts can now advance to the next configured provider, letting agent, chat, and cron runs recover without repeating work that may have side effects. #96142 Thanks @brokemac79, @riazrahaman.

> Isolated cron jobs can now use models supplied by enabled bundled plugins without failing as unknown or silently resolving to the wrong provider. #96070 Thanks @sallyom, @sunnyshu0925.

> Dreaming now keeps deleted or reset transcript archives and cron-created child conversations out of its learned session set, reducing duplicate history and automation noise without removing retained archives from historical search. #96517 Thanks @adam-researchh, @jalehman, @xialonglee.

> openclaw sessions cleanup --fix-missing now preserves fresh cron sessions with valid transcripts and clearly reports repaired entries. #97495 Thanks @qingminglong.

> Recurring provider-CLI cron jobs and local openclaw agent runs now keep their existing provider conversation across the daily reset boundary instead of silently losing context. #98356 Thanks @yetval.

> Small-context local models can now begin and continue conversations without immediately entering an overflow-compaction loop before useful prompt space is available. #100621 Thanks @vincentkoc.

> Long agent prompt data containing emoji or other paired Unicode characters now stays well-formed when capped, avoiding broken text in agent and automation context. #101303 Thanks @alix-007.

> Archived memories around user messages that begin with [cron:] remain searchable after a session reset or deletion, while genuine cron-generated archives stay hidden. #101322 Thanks @ly-wang19.

> Timed-out cron jobs, expired agent requests, and disconnected HTTP clients now stop promptly instead of spending more time and provider calls on model fallback. #62682 Thanks @altaywtf, @cinapbot, @simonusa.

> Isolated cron jobs can announce a cross-session result without feeding the recipient's reply back into the cron run and creating duplicate message loops. #92283 Related #92257 . Thanks @harjothkhara, @nailujac, @vincentkoc.

> Heartbeat and cron work on macOS and Linux is less likely to fail with Unknown system error -11 when reconnects overlap session or workspace updates. #100389 Thanks @ogarciarevett.

> Agents using OpenClaw's cron tools are now limited to their own scheduled jobs and session targets, while operator-managed cron remains unchanged and mixed-version setups fail closed with an openclaw gateway restart instruction. #96883 Thanks @joshavant.

> Cron wake actions started by an agent now remain within that agent's own session lanes, reducing the chance of waking another agent's conversation. #97949 Thanks @eleqtrizit.

> Failed cron webhooks no longer forward raw command summaries or diagnostics that may contain setup prompts, codes, or secret-like output. 1d17263 Thanks @joshavant.

> Non-owner Gateway chat users are no longer offered the protected cron , gateway , or nodes control tools, even when those tools are otherwise allowlisted. #102030 Thanks @pgondhi987.

> Browser automation now keeps Chrome control traffic tied to the configured or explicitly allowed CDP host, reducing the risk that a discovered debugger address redirects credentials or control elsewhere. #101171

> Android notification automations now queue accepted events during Gateway connection or reconnection and deliver them in order once the link is ready. #92602 Related #79552 . Thanks @ashishpatel26, @hectorrp13.

> Supported non-English Android builds now translate more cron inspection, delivery error, copy feedback, default-state, and agent request details. d83ee4c

> Google Meet join, creation, talk-back, transcription, and related automation now work across browser and account languages by using English in OpenClaw-controlled Meet tabs. #89671 Thanks @unayung.

> openclaw update on Windows now prevents the managed Gateway Scheduled Task from relaunching during package replacement, avoiding partially updated or mixed-version processes. #100757 Thanks @vincentkoc.

> Windows Gateway setup now detects when Task Scheduler exits without starting a listener and can use the existing fallback launch without creating a duplicate if startup is merely late. #76245

> A timeout while one isolated cron job is setting up no longer restarts the Gateway or interrupts unrelated agent and scheduled work. #96396 Thanks @849261680, @brycemurray, @velvet-shark.

> Operators can run openclaw doctor --lint --all to include every opt-in diagnostic check without changing the behavior of existing doctor --lint automation. #96471 Thanks @giodl73-repo.

> Default cron failure alerts enabled with openclaw cron edit &lt;job&gt; --failure-alert now survive Gateway restarts instead of silently disappearing after reload. #96615 Thanks @liuhao1024.

> openclaw doctor now warns when cron jobs target channels whose plugins are inactive, letting operators correct delivery before the next scheduled run fails. #98184 Thanks @masatohoshino, @vincentkoc.

> Docker and bind-mount installations can finish legacy cron migration across filesystem boundaries, with actionable warnings and duplicate-safe retries when cleanup cannot complete. #98217 Thanks @masatohoshino.

> openclaw doctor now explains cron jobs that still look in flight after an interrupted Gateway run and how those leftover markers are cleared on the next start. #98620 Thanks @masatohoshino.

> Doctor now warns when enabled cron jobs are stuck in repeated failures without configured alerts, while healthy and below-threshold jobs stay quiet. #99606 Thanks @masatohoshino.

> openclaw tasks maintenance --apply now preserves active cron session history even when job IDs contain spaces, capitals, punctuation, or explicit session keys. #96352 Thanks @ly-wang19, @vincentkoc.

> openclaw cron add now rejects invalid --no-output-timeout-seconds and --output-max-bytes values immediately instead of silently creating a command job without the requested limits. #96516 Thanks @zhangguiping-xydt.

> openclaw config unset now explains when a visible value is an inherited runtime default that is not stored in the user's config, avoiding an unproductive loop between config get and config unset while leaving failed attempts unchanged. #96557 Thanks @moeghashim.

> Human-readable cron list and cron show output now reveals repeated failure streaks such as error (12x) while leaving JSON status values unchanged. #99602 Thanks @masatohoshino.

> Operators can opt into core/doctor/legacy-cron-store to find legacy cron data that needs attention without the lint check changing any stored state. #99211 Thanks @giodl73-repo.

> Matrix documentation now explains progress streaming, room-specific mention matching, per-room enablement, and bot-loop safeguards that operators can configure. #98318 Thanks @vincentkoc, @wm0018.

> Official OpenClaw docs now help operators and plugin authors handle credentials safely, preflight cron jobs that use local-provider fallbacks, apply Talk timing defaults, configure MiniMax providers and models, and copy a complete minimal plugin package with the required dependency metadata. #100182

> Scheduled automation retains intended models, timing, state, and delivery across more restarts and edits. Tool calls and results also recover more cleanly from timeouts, malformed content, oversized output, and interrupted work instead of leaving a task looking complete when its usable result was lost.

> Browser automation can now act on tabs by suggested ID, tab ID, label, or unique prefix without false target-mismatch failures. #96178 Thanks @zengwen-dt.

> Cron jobs with a valid future run exactly on a second boundary now keep that scheduled time instead of being incorrectly treated as stale and rebased. #81731 Thanks @vincentkoc, @yashkot007.

> Isolated agentTurn cron jobs can recover from temporarily mismatched runtime artifacts instead of failing at startup with a sourceReplyDeliveryMode error. #85249 Thanks @jerry-xin.

> openclaw tasks maintenance --apply can now repair false lost-task records when durable cron history proves the run completed successfully. #86088 Thanks @altaywtf, @liaoandi.

> Scheduled agent jobs now warn when ANNOUNCE_SKIP suppresses a cron completion, making missing reports and partial output easier to diagnose. #90566 Related #68561 . Thanks @mibslee, @sahibzada-allahyar.

> Catch-up cron jobs deferred briefly after startup are no longer skipped merely because an operator checks cron status before they fire. #94022 Related #93935 . Thanks @richchen01, @vincentkoc, @yetval.

> Timed-out or cancelled isolated cron runs now retain their provider, model, and session details in cron_run_logs , making failed jobs easier to trace. #95943 Related #95873 . Thanks @luke-renjoy, @zengwen-dt.

> Editing a recurring cron job no longer skips a run that is already due or shifts an unchanged interval schedule to the edit time. #96159 Thanks @yetval.

> Clearing a saved Model or Thinking/Effort override in the Cron Control UI now truly restores inherited defaults, with --clear-thinking available from the CLI. #96293 Related #96287 . Thanks @takamasa-aiso, @zengwen-dt.

> CLI-backed workers from isolated cron jobs now exit after completion instead of accumulating and slowing the host and Gateway. #97227 Thanks @vianne-droid, @xialonglee, @yusukeit0.

> Long cron failure alerts now preserve emoji and other supplementary Unicode characters instead of ending with a broken replacement symbol. #97298 Thanks @zenglingbiao.

> Scheduled jobs can deliver to a live chat without blocking replies or mixing background work into its transcript, and operators can clear stale childless cron tasks without cancelling active session-backed runs. #98755 Related #98121 . Thanks @ethansk, @obviyus.

> Recurring cron jobs created for current or session:&lt;id&gt; once again carry their selected conversation history into later runs, while isolated jobs still start clean. #98947 Thanks @ethansk, @obviyus.

> Failed cron add , cron update , and cron remove commands now leave the running scheduler unchanged, so live jobs match the saved configuration and reported result. #99960 Thanks @masatohoshino, @vincentkoc.

> Browser automation attached to an existing Chrome session now stops with a bounded error when Chrome crashes or a request is cancelled, and later requests can reconnect cleanly. #101454 Thanks @aniruddhaadak80.

> Cron job updates can now remove a job-specific fallback model setting so scheduled runs inherit the global defaults again without recreating the job. #100801 Thanks @sunnyshu0925.

> openclaw cron edit now finds jobs more reliably and with less delay on Gateways that contain many scheduled jobs, including --exact and timeout-only edits. #100836 Thanks @machine3at, @vincentkoc.

> Editing a cron payload with --no-best-effort-deliver no longer silently changes the job's delivery mode to announcements. #100846 Thanks @machine3at.

> Using openclaw cron edit &lt;id&gt; --no-best-effort-deliver on an older detached job no longer accidentally suppresses its completion announcement. #101027

> Agent and MCP cron requests using mixed-case command labels now fail closed instead of slipping past the restriction on shell-backed agent cron jobs. #101350 Thanks @pgondhi987.

> Replies now correctly confirm reminders scheduled through commands such as openclaw cron add instead of also claiming that no reminder was created. #101807 Thanks @bryantegomoh, @vincentkoc.

> Standardized text-pattern escaping across maintainer automation to reduce duplication and future inconsistencies. #99778 Thanks @romneyda.

> Reduced unnecessary waiting in Docker scheduler coverage without changing runtime scheduling behavior. #99988

> Aligned documentation for environment protection, scheduled-task fallback checks, and Talk silence defaults without changing behavior. #100186

> Stabilized Windows startup fallback coverage and ensured scheduler changes reach the appropriate validation. #101223

> Reduced unnecessary internal script interfaces to make repository automation easier to understand and maintain. #101892 Thanks @vincentkoc.

> Reduced unused internal types in repository automation, improving maintainability without changing commands. #101917 Thanks @vincentkoc.

Source: https://docs.openclaw.ai/releases/2026.7.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-07-13-5-projects-and-workspaces-changes-in-v2026-7-1|5 Projects and Workspaces changes in v2026.7.1]] · Projects and Workspaces
- [[Changes/OpenClaw/2026-07-13-99-developer-workflow-changes-in-v2026-7-1|99 Developer Workflow changes in v2026.7.1]] · Developer Workflow
- [[Changes/OpenClaw/2026-07-13-69-context-window-changes-in-v2026-7-1|69 Context Window changes in v2026.7.1]] · Context Window
- [[Changes/OpenClaw/2026-07-13-10-accessibility-and-localization-changes-in-v2026-7-1|10 Accessibility and Localization changes in v2026.7.1]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-07-13-64-interface-experience-changes-in-v2026-7-1|64 Interface Experience changes in v2026.7.1]] · Interface Experience
- [[Changes/OpenClaw/2026-07-13-whatsapp-and-telegram-default-account-routing-warnings-are-now-available-through|WhatsApp and Telegram default-account routing warnings are now available through…]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-07-13-132-agent-mode-changes-in-v2026-7-1|132 Agent Mode changes in v2026.7.1]] · Agent Mode
- [[Changes/OpenClaw/2026-07-13-after-one-generated-video-clip-is-ready-a-different-next-clip-can-start-immediat|After one generated video clip is ready, a different next clip can start immediately…]] · Video Generation
- [[Changes/OpenClaw/2026-07-13-130-model-support-changes-in-v2026-7-1|130 Model Support changes in v2026.7.1]] · Model Support
- [[Changes/OpenClaw/2026-07-13-69-account-and-access-changes-in-v2026-7-1|69 Account and Access changes in v2026.7.1]] · Account and Access
- [[Changes/OpenClaw/2026-07-13-59-safety-and-privacy-changes-in-v2026-7-1|59 Safety and Privacy changes in v2026.7.1]] · Safety and Privacy
- [[Changes/OpenClaw/2026-07-13-224-mobile-and-desktop-changes-in-v2026-7-1|224 Mobile and Desktop changes in v2026.7.1]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-07-13-83-voice-and-audio-changes-in-v2026-7-1|83 Voice and Audio changes in v2026.7.1]] · Voice and Audio
- [[Changes/OpenClaw/2026-07-13-18-pricing-model-changes-in-v2026-7-1|18 Pricing Model changes in v2026.7.1]] · Pricing Model
- [[Changes/OpenClaw/2026-07-13-21-editor-experience-changes-in-v2026-7-1|21 Editor Experience changes in v2026.7.1]] · Editor Experience
- [[Changes/OpenClaw/2026-07-13-7-image-generation-changes-in-v2026-7-1|7 Image Generation changes in v2026.7.1]] · Image Generation
- [[Changes/OpenClaw/2026-07-13-channel-setup-warnings-are-now-available-as-structured-doctor-lint-findings-with|Channel setup warnings are now available as structured Doctor lint findings…]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-07-13-4-enterprise-and-administration-changes-in-v2026-7-1|4 Enterprise and Administration changes in v2026.7.1]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-07-13-2-presentation-creation-changes-in-v2026-7-1|2 Presentation Creation changes in v2026.7.1]] · Presentation Creation
- [[Changes/OpenClaw/2026-07-13-136-memory-and-personalization-changes-in-v2026-7-1|136 Memory and Personalization changes in v2026.7.1]] · Memory and Personalization
- [[Changes/OpenClaw/2026-07-13-213-apps-and-integrations-changes-in-v2026-7-1|213 Apps and Integrations changes in v2026.7.1]] · Apps and Integrations
- [[Changes/OpenClaw/2026-07-13-8-search-and-browsing-changes-in-v2026-7-1|8 Search and Browsing changes in v2026.7.1]] · Search and Browsing
- [[Changes/OpenClaw/2026-07-13-20-collaboration-changes-in-v2026-7-1|20 Collaboration changes in v2026.7.1]] · Collaboration
- [[Changes/OpenClaw/2026-07-13-13-files-and-data-changes-in-v2026-7-1|13 Files and Data changes in v2026.7.1]] · Files and Data
- [[Changes/OpenClaw/2026-07-13-19-multimodal-input-changes-in-v2026-7-1|19 Multimodal Input changes in v2026.7.1]] · Multimodal Input
- [[Changes/OpenClaw/2026-07-13-38-reliability-and-performance-changes-in-v2026-7-1|38 Reliability and Performance changes in v2026.7.1]] · Reliability and Performance
- [[Changes/OpenClaw/2026-07-13-686-other-changes-in-v2026-7-1|686 other changes in v2026.7.1]] · Other changes
- [[Changes/OpenClaw/2026-07-13-official-openclaw-container-images-are-now-available-from-docker-hub-as-well-as|Official OpenClaw container images are now available from Docker Hub as well…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Automation and Scheduling

- Earlier: 2026-07-12 · Kimi Code · [[Changes/Kimi Code/2026-07-12-keep-kimi-p-runs-alive-after-a-turn-ends-while-a-goal-is-still-active-or-a-cron|Keep kimi -p runs alive after a turn ends while a goal is still active or a cron…]]
- Later: 2026-07-16 · Notion · [[Changes/Notion/2026-07-16-what-s-on-my-schedule-today|What’s on my schedule today?]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-change-gain-with-volume-automation|Change gain, with volume automation]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-07-13-5fba08&body=Card%3A%20Changes%2FOpenClaw%2F2026-07-13-79-automation-and-scheduling-changes-in-v2026-7-1.md%0ACard%20ID%3A%20openclaw-2026-07-13-5fba08%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.7.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->