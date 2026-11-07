---
card_id: openclaw-2026-07-13-1da3e8
date: '2026-07-13'
description: 'OpenClaw · 2026-07-13 · Context Window: 69 changes in v2026.7.1 — Control
  UI now makes conversations easier to create, find, and switch from a populated…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2
    Context Window changes in 0.2.9]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1166
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ac4be5ba8ccd50135231e2b4c640b4f47f0129791899d26329413b307d5e5870
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-07-13-1da3e8
  comparison: ''
  date: '2026-07-13'
  description: 'OpenClaw — v2026.7.1: 69 Context Window changes'
  evidence:
  - quote: 'Control UI now makes conversations easier to create, find, and switch
      from a populated session sidebar, while keeping context pressure and provider
      quota information close at hand. #99289 Related #99288 .'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The Control UI context indicator now remains visible with an approximate
      cached total while a response is active, without using stale data for urgent
      warnings or the Compact action. #89772 Thanks @bladin.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Dashboard WebChat users can right-click a completed message and reply
      with visible quote context instead of manually copying and formatting it. #92654
      Thanks @programmingwtf, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'New Control UI chats now use the selected model''s current context window
      instead of inheriting an outdated, smaller limit from a parent session. #97332
      Thanks @galiniliev.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Session Workspace file paths can now be copied from Chat even when the
      Control UI runs over plain HTTP or another context without the standard Clipboard
      API. #98764 Related #98759 . Thanks @adinballew, @zengwen-dt.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Users can open the Control UI context ring to inspect exact context use,
      the latest input and output token counts, and the active model without leaving
      chat. #100264'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Control UI Settings now offers a persistent Simple/Advanced switch, cleaner
      Appearance controls, and a Pending label only when a Context Profile change
      is actually staged. #100147'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Users with Claude Mythos 5 access can select it through Anthropic, Anthropic
      Vertex, Amazon Bedrock, or Bedrock Mantle with its required context, output,
      thinking, caching, and replay behavior. #101238 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'An active /goal now keeps guiding later turns and survives compaction,
      queues, and interruptions until the goal is paused, completed, blocked, or limited.
      #100468'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Slack channels can keep ambient OpenClaw participation while the opt-in
      ignoreOtherMentions setting prevents replies to conversations aimed at another
      person or group and retains that conversation as context for a later bot mention.
      #53467 Thanks @hanamizuki.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Malformed successful Discord responses now fail with endpoint-specific
      context instead of surfacing a raw parser error or crashing OpenClaw. #97889
      Thanks @lsr911.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Long Slack context labels, Zalo messages and captions, and extension command
      output now truncate without breaking emoji or other non-BMP characters. 7e03242
      Thanks @hugenshen, @mushuiyu886, @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Microsoft Teams replies to long parent messages now keep emoji and similar
      characters intact in the agent''s parent-message context instead of inserting
      malformed text. #96569 Thanks @llagy007, @weeli-009.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Long Matrix thread starters keep emoji and other special characters intact
      when OpenClaw shortens them for agent context. #97121 Thanks @bartok9, @ly-wang19.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Telegram direct-message follow-ups now include one copy of the previous
      assistant reply in recent context instead of duplicating it and wasting tokens.
      #98769 Related #98767 . Thanks @rabsef-bicrym.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Telegram bots in ambient group mode now see recent room context before
      deciding whether to speak, reducing replies to isolated fragments that were
      not directed at the bot. #99143 Related #99142 . Thanks @obviyus.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Telegram group agents now receive one chronological copy of recent messages
      instead of duplicated history and repeated delivery details consuming context.
      #99256 Related #99218 . Thanks @obviyus.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Telegram ambient group conversations can now retain unmentioned room context
      across later turns, restarts, and compaction without repeatedly replaying the
      same window. #99306 Related #99257 . Thanks @obviyus.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Telegram ambient group sessions now restore the relevant older chat context
      after a reset instead of silently treating archived messages as already visible.
      #99385 Related #99373 . Thanks @obviyus.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Claude native-thinking sessions can now recover automatically after Anthropic
      rejects a replayed thinking block, without manual compaction or transcript loss.
      #98411 Related #98308 . Thanks @clearhorizoninvestments, @sunlit-deng.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Codex users can route both codex/* and openai/* models through the bundled
      runtime, and older conversations resume without unnecessary context reprojection.
      #105034'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Nemotron 3 Super now exposes its full 1,048,576-token context budget in
      OpenClaw''s bundled NVIDIA fallback catalog instead of compacting at the stale
      262,144-token limit. #98726 Thanks @eleqtrizit.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Claude Fable 5 now uses the expected Anthropic context1m stream setup
      when 1M context is enabled, without affecting similar model IDs. #100572 Thanks
      @zhangguiping-xydt.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Sessions , transcripts, compaction, goals, and routing also retain the
      intended conversation more consistently through restarts, resets, delayed follow-ups,
      tool-heavy runs, and client changes. The practical result is less missing history,
      fewer replies stored against the wrong session, and more dependable continuation
      of long-running work.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Long CJK-heavy sessions using a context engine such as lossless-claw no
      longer stop on a false prompt too large precheck after the engine has already
      managed the prompt. #95342 Thanks @jalehman, @mpz4life.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Large Chinese, Japanese, and Korean tool results are now estimated more
      accurately, reducing false context-overflow interruptions and premature compaction.
      #95447 Thanks @moguangyu5-design, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Prompts containing fullwidth East Asian characters now receive more accurate
      size estimates, allowing context management to start before an oversized request
      reaches the model. #96442 Thanks @lin-hongkuan.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Long conversations now recover compaction after transient provider disconnects
      instead of replacing useful history with a degraded placeholder summary. #97504
      Thanks @hugenshen.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Long conversations using historyLimit or dmHistoryLimit now retain their
      saved earlier summary after compaction, helping the assistant remember prior
      context. #97591 Thanks @liuhao1024, @yetval.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'CLI-backed agents in multi-person group chats now retain conversational
      context when participants alternate, without expanding non-owner tool permissions.
      #99640 Related #99633 . Thanks @obviyus.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Local-model sessions now retain auto-compaction bookkeeping, reducing
      repeated context refills and the unresponsive behavior they could cause. #99678
      Related #99677 . Thanks @headbouyjb, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'CLI-backed group agents now keep one warm conversation across mentioned
      and unmentioned follow-ups instead of resetting and losing context. #99722 Related
      #99696 . Thanks @obviyus.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Claude CLI model fallback now carries the prior tool-call trail alongside
      tool results, giving the replacement model enough context to continue coherently.
      #99851 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Long cached Anthropic tool sessions now compact near the configured context
      threshold instead of interrupting work early because cumulative cache tokens
      looked like live context. #99864 Thanks @jrex-jooni, @lzy3538, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Long-lived agents with large context windows now retain fresh tool output,
      compact under aggregate pressure, and warn users to run /compact or /new if
      pressure persists. #100077 Thanks @obviyus.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Long-running agents can now recover full command output and truncated
      web_fetch content after history cleanup, reducing repeated expensive work and
      lost page context. #100135 Thanks @obviyus.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Long sessions that compact in stages now preserve clearer older-to-newer
      ordering when summaries are combined, reducing the chance that stale context
      appears equally recent. #100684 Thanks @vincentkoc, @zw-xysk.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Embedded agents now retain configured compaction reserve limits when runtime
      safeguards save settings, reducing unexpected context-budget shrinkage during
      long work. #92237 Thanks @sercada.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Sessions with large command output or summaries now compact before exceeding
      the model context, avoiding failed provider requests and misleading token budgets.
      #97861 Thanks @yetval.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Long tool-heavy or compacted sessions now budget the real size of command
      output and summaries before sending a prompt, reducing context overflow failures.
      #97928 Related #97927 . Thanks @liuhao1024, @yetval.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Claude CLI conversations that exhaust their context now recover into a
      fresh reseeded session automatically, and timeout retries retain the temporary
      files they need to complete. #98934 Related #98897 . Thanks @obviyus.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Images attached to a CLI-backed prompt now survive embedded-model fallback,
      preserving the visual context needed to answer. #99891 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Long Claude CLI-backed runs now show honest Thinking... (~N tokens) activity
      for direct and queued work instead of appearing stalled when readable reasoning
      text is unavailable. #100148 Thanks @obviyus.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Existing Codex sessions can resume their bound threads more reliably after
      upgrades, resets, and compaction without depending on leftover transcript-side
      JSON files. #101210'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Bounded text in Parallel searches, compaction, telemetry, presence, Workboard,
      badges, and Control UI metadata now keeps or omits whole Unicode characters
      instead of leaving malformed fragments. #101711'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Embedded agent runs that omit a session key now retain the intended fallback
      session context more reliably. 31a65e0 Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Long agent runs can now resume from a valid conversation boundary after
      compaction recovery instead of wedging or incorrectly demoting the selected
      model. 486033b Thanks @mettlyz11, @neltomw, @obviyus.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'An empty non-image tool result no longer becomes (see attached image)
      in OpenAI-compatible agent context, avoiding misleading follow-up behavior.
      #97423 Thanks @scribe-dandelion-cult.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Telegram timeout logs now hide bot tokens embedded in Bot API paths, including
      custom and proxy roots, while retaining useful endpoint context. #99428 Related
      #96982 . Thanks @liuhaiyang14, @xialonglee.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Custom ACP error redactors now keep OpenClaw''s built-in secret cleanup,
      preventing known tokens, credentials, and private-key material from leaking
      into formatted errors. #100191 Thanks @lin-hongkuan.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'On macOS, an explicit OPENCLAW_STATE_DIR now stays isolated from the machine''s
      existing App Group pairing identity and device tokens. #101779'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Telegram bot tokens now remain masked even when they cross internal boundaries
      inside very large logs or tool-error messages. #103861 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'iOS and macOS chat now show a context-usage ring that changes warning
      color near the limit, helping users anticipate compaction or truncation in long
      conversations. #101183'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Long-running agents can automatically retire unused Skill Workshop skills
      from future context, pin important ones, restore archives, and surface possible
      overlaps without deleting the underlying skills. #101214'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Configured context-engine plugins such as lossless-claw now stay active
      after discovery instead of being silently replaced by the built-in legacy engine.
      #96357 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Embedded context-engine plugins now see the current turn in the transcript
      during afterTurn , preventing missing first messages and duplicate imports.
      #97342 Thanks @gorkem2020, @iwhatsskill, @sgh6688, @udjin79.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The first Gateway status check after a restart now reports the selected
      model''s actual context window instead of briefly showing a generic 200k limit.
      #97576 Thanks @turbotheturtle.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Browser extensions can reconnect with a newly rotated pairing token while
      Browser control remains running, and old tokens continue to be rejected. a703183
      Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Scheduled commitment follow-ups now stay focused on their original conversation
      instead of absorbing unrelated heartbeat instructions, queued context, or recovery
      work. #98169 Thanks @bdjben.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Natural-language corrections can now become the right pending Skill Workshop
      improvement after successful or failed turns without repeating old feedback,
      duplicating /learn , or replacing proposal context. #100576 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'OpenTelemetry latency dashboards now provide useful duration and context-size
      distributions for agent and harness work lasting well beyond 10 seconds, including
      multi-minute runs, without collector-side bucket customization. #96592 Thanks
      @hcnode, @vincentkoc, @zhiling-chen-20230331.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Successful Codex thread-goal reads now appear as successful in model context,
      transcripts, and diagnostics instead of being recorded as failed tool calls.
      #98659 Thanks @yetval.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Failed exact-match edits now show readable current-file context even when
      truncation falls beside an emoji or other non-BMP character. #99527 Thanks @mikasa0818.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Documented compaction retry timing behavior to make future maintenance
      safer without changing runtime behavior. #89585'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Prevented valid Codex long-context results from causing false QA failures
      while still checking that earlier evidence remains available. #96366 Thanks
      @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Aligned internal conversation audience labels with verified group context
      for future access-control work. #99816'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Corrected QA prompt handling so validation responds to the user''s actual
      instruction rather than hidden runtime context. #100272 Thanks @marvinthebored,
      @obviyus, @peetiegonzalez.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Prepared compaction, scheduled checks, and session forks for future storage
      changes without altering behavior. #101179 Thanks @jalehman.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Prepared session routing, goals, delivery, and compaction tracking for
      safer storage changes without altering workflows. #101180 Thanks @jalehman.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 69-context-window-changes-in-v2026-7-1
  source_release: openclaw-2026-07-13-v2026-7-1-c2063718
  source_type: openclaw_changelog
  theme: context-window
  title: 69 Context Window changes in v2026.7.1
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-07-09-3-context-window-changes-in-rust-v0-144-0|3 Context
  Window changes in rust-v0.144.0]]'
- '[[Changes/Cursor/2026-07-10-side-chats|Side chats]]'
- '[[Changes/GitHub Copilot CLI/2026-07-10-press-tab-to-switch-the-context-window-in-model|Press
  Tab to switch the context window in /model]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-07-13-v2026-7-1-c2063718|openclaw-2026-07-13-v2026-7-1-c2063718]]'
source_type: openclaw_changelog
theme: context-window
title: 69 Context Window changes in v2026.7.1
type: change
---

<!-- chronolog:begin region="header" -->
# 69 Context Window changes in v2026.7.1

**OpenClaw** · 2026-07-13 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.7.1) · from [[Releases/OpenClaw/openclaw-2026-07-13-v2026-7-1-c2063718|v2026.7.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Control UI now makes conversations easier to create, find, and switch from a populated session sidebar, while keeping context pressure and provider quota information close at hand. #99289 Related #99288 .

> The Control UI context indicator now remains visible with an approximate cached total while a response is active, without using stale data for urgent warnings or the Compact action. #89772 Thanks @bladin.

> Dashboard WebChat users can right-click a completed message and reply with visible quote context instead of manually copying and formatting it. #92654 Thanks @programmingwtf, @vincentkoc.

> New Control UI chats now use the selected model's current context window instead of inheriting an outdated, smaller limit from a parent session. #97332 Thanks @galiniliev.

> Session Workspace file paths can now be copied from Chat even when the Control UI runs over plain HTTP or another context without the standard Clipboard API. #98764 Related #98759 . Thanks @adinballew, @zengwen-dt.

> Users can open the Control UI context ring to inspect exact context use, the latest input and output token counts, and the active model without leaving chat. #100264

> Control UI Settings now offers a persistent Simple/Advanced switch, cleaner Appearance controls, and a Pending label only when a Context Profile change is actually staged. #100147

> Users with Claude Mythos 5 access can select it through Anthropic, Anthropic Vertex, Amazon Bedrock, or Bedrock Mantle with its required context, output, thinking, caching, and replay behavior. #101238 Thanks @vincentkoc.

> An active /goal now keeps guiding later turns and survives compaction, queues, and interruptions until the goal is paused, completed, blocked, or limited. #100468

> Slack channels can keep ambient OpenClaw participation while the opt-in ignoreOtherMentions setting prevents replies to conversations aimed at another person or group and retains that conversation as context for a later bot mention. #53467 Thanks @hanamizuki.

> Malformed successful Discord responses now fail with endpoint-specific context instead of surfacing a raw parser error or crashing OpenClaw. #97889 Thanks @lsr911.

> Long Slack context labels, Zalo messages and captions, and extension command output now truncate without breaking emoji or other non-BMP characters. 7e03242 Thanks @hugenshen, @mushuiyu886, @vincentkoc.

> Microsoft Teams replies to long parent messages now keep emoji and similar characters intact in the agent's parent-message context instead of inserting malformed text. #96569 Thanks @llagy007, @weeli-009.

> Long Matrix thread starters keep emoji and other special characters intact when OpenClaw shortens them for agent context. #97121 Thanks @bartok9, @ly-wang19.

> Telegram direct-message follow-ups now include one copy of the previous assistant reply in recent context instead of duplicating it and wasting tokens. #98769 Related #98767 . Thanks @rabsef-bicrym.

> Telegram bots in ambient group mode now see recent room context before deciding whether to speak, reducing replies to isolated fragments that were not directed at the bot. #99143 Related #99142 . Thanks @obviyus.

> Telegram group agents now receive one chronological copy of recent messages instead of duplicated history and repeated delivery details consuming context. #99256 Related #99218 . Thanks @obviyus.

> Telegram ambient group conversations can now retain unmentioned room context across later turns, restarts, and compaction without repeatedly replaying the same window. #99306 Related #99257 . Thanks @obviyus.

> Telegram ambient group sessions now restore the relevant older chat context after a reset instead of silently treating archived messages as already visible. #99385 Related #99373 . Thanks @obviyus.

> Claude native-thinking sessions can now recover automatically after Anthropic rejects a replayed thinking block, without manual compaction or transcript loss. #98411 Related #98308 . Thanks @clearhorizoninvestments, @sunlit-deng.

> Codex users can route both codex/* and openai/* models through the bundled runtime, and older conversations resume without unnecessary context reprojection. #105034

> Nemotron 3 Super now exposes its full 1,048,576-token context budget in OpenClaw's bundled NVIDIA fallback catalog instead of compacting at the stale 262,144-token limit. #98726 Thanks @eleqtrizit.

> Claude Fable 5 now uses the expected Anthropic context1m stream setup when 1M context is enabled, without affecting similar model IDs. #100572 Thanks @zhangguiping-xydt.

> Sessions , transcripts, compaction, goals, and routing also retain the intended conversation more consistently through restarts, resets, delayed follow-ups, tool-heavy runs, and client changes. The practical result is less missing history, fewer replies stored against the wrong session, and more dependable continuation of long-running work.

> Long CJK-heavy sessions using a context engine such as lossless-claw no longer stop on a false prompt too large precheck after the engine has already managed the prompt. #95342 Thanks @jalehman, @mpz4life.

> Large Chinese, Japanese, and Korean tool results are now estimated more accurately, reducing false context-overflow interruptions and premature compaction. #95447 Thanks @moguangyu5-design, @vincentkoc.

> Prompts containing fullwidth East Asian characters now receive more accurate size estimates, allowing context management to start before an oversized request reaches the model. #96442 Thanks @lin-hongkuan.

> Long conversations now recover compaction after transient provider disconnects instead of replacing useful history with a degraded placeholder summary. #97504 Thanks @hugenshen.

> Long conversations using historyLimit or dmHistoryLimit now retain their saved earlier summary after compaction, helping the assistant remember prior context. #97591 Thanks @liuhao1024, @yetval.

> CLI-backed agents in multi-person group chats now retain conversational context when participants alternate, without expanding non-owner tool permissions. #99640 Related #99633 . Thanks @obviyus.

> Local-model sessions now retain auto-compaction bookkeeping, reducing repeated context refills and the unresponsive behavior they could cause. #99678 Related #99677 . Thanks @headbouyjb, @vincentkoc.

> CLI-backed group agents now keep one warm conversation across mentioned and unmentioned follow-ups instead of resetting and losing context. #99722 Related #99696 . Thanks @obviyus.

> Claude CLI model fallback now carries the prior tool-call trail alongside tool results, giving the replacement model enough context to continue coherently. #99851 Thanks @vincentkoc.

> Long cached Anthropic tool sessions now compact near the configured context threshold instead of interrupting work early because cumulative cache tokens looked like live context. #99864 Thanks @jrex-jooni, @lzy3538, @vincentkoc.

> Long-lived agents with large context windows now retain fresh tool output, compact under aggregate pressure, and warn users to run /compact or /new if pressure persists. #100077 Thanks @obviyus.

> Long-running agents can now recover full command output and truncated web_fetch content after history cleanup, reducing repeated expensive work and lost page context. #100135 Thanks @obviyus.

> Long sessions that compact in stages now preserve clearer older-to-newer ordering when summaries are combined, reducing the chance that stale context appears equally recent. #100684 Thanks @vincentkoc, @zw-xysk.

> Embedded agents now retain configured compaction reserve limits when runtime safeguards save settings, reducing unexpected context-budget shrinkage during long work. #92237 Thanks @sercada.

> Sessions with large command output or summaries now compact before exceeding the model context, avoiding failed provider requests and misleading token budgets. #97861 Thanks @yetval.

> Long tool-heavy or compacted sessions now budget the real size of command output and summaries before sending a prompt, reducing context overflow failures. #97928 Related #97927 . Thanks @liuhao1024, @yetval.

> Claude CLI conversations that exhaust their context now recover into a fresh reseeded session automatically, and timeout retries retain the temporary files they need to complete. #98934 Related #98897 . Thanks @obviyus.

> Images attached to a CLI-backed prompt now survive embedded-model fallback, preserving the visual context needed to answer. #99891 Thanks @vincentkoc.

> Long Claude CLI-backed runs now show honest Thinking... (~N tokens) activity for direct and queued work instead of appearing stalled when readable reasoning text is unavailable. #100148 Thanks @obviyus.

> Existing Codex sessions can resume their bound threads more reliably after upgrades, resets, and compaction without depending on leftover transcript-side JSON files. #101210

> Bounded text in Parallel searches, compaction, telemetry, presence, Workboard, badges, and Control UI metadata now keeps or omits whole Unicode characters instead of leaving malformed fragments. #101711

> Embedded agent runs that omit a session key now retain the intended fallback session context more reliably. 31a65e0 Thanks @vincentkoc.

> Long agent runs can now resume from a valid conversation boundary after compaction recovery instead of wedging or incorrectly demoting the selected model. 486033b Thanks @mettlyz11, @neltomw, @obviyus.

> An empty non-image tool result no longer becomes (see attached image) in OpenAI-compatible agent context, avoiding misleading follow-up behavior. #97423 Thanks @scribe-dandelion-cult.

> Telegram timeout logs now hide bot tokens embedded in Bot API paths, including custom and proxy roots, while retaining useful endpoint context. #99428 Related #96982 . Thanks @liuhaiyang14, @xialonglee.

> Custom ACP error redactors now keep OpenClaw's built-in secret cleanup, preventing known tokens, credentials, and private-key material from leaking into formatted errors. #100191 Thanks @lin-hongkuan.

> On macOS, an explicit OPENCLAW_STATE_DIR now stays isolated from the machine's existing App Group pairing identity and device tokens. #101779

> Telegram bot tokens now remain masked even when they cross internal boundaries inside very large logs or tool-error messages. #103861 Thanks @vincentkoc.

> iOS and macOS chat now show a context-usage ring that changes warning color near the limit, helping users anticipate compaction or truncation in long conversations. #101183

> Long-running agents can automatically retire unused Skill Workshop skills from future context, pin important ones, restore archives, and surface possible overlaps without deleting the underlying skills. #101214

> Configured context-engine plugins such as lossless-claw now stay active after discovery instead of being silently replaced by the built-in legacy engine. #96357 Thanks @vincentkoc.

> Embedded context-engine plugins now see the current turn in the transcript during afterTurn , preventing missing first messages and duplicate imports. #97342 Thanks @gorkem2020, @iwhatsskill, @sgh6688, @udjin79.

> The first Gateway status check after a restart now reports the selected model's actual context window instead of briefly showing a generic 200k limit. #97576 Thanks @turbotheturtle.

> Browser extensions can reconnect with a newly rotated pairing token while Browser control remains running, and old tokens continue to be rejected. a703183 Thanks @vincentkoc.

> Scheduled commitment follow-ups now stay focused on their original conversation instead of absorbing unrelated heartbeat instructions, queued context, or recovery work. #98169 Thanks @bdjben.

> Natural-language corrections can now become the right pending Skill Workshop improvement after successful or failed turns without repeating old feedback, duplicating /learn , or replacing proposal context. #100576 Thanks @vincentkoc.

> OpenTelemetry latency dashboards now provide useful duration and context-size distributions for agent and harness work lasting well beyond 10 seconds, including multi-minute runs, without collector-side bucket customization. #96592 Thanks @hcnode, @vincentkoc, @zhiling-chen-20230331.

> Successful Codex thread-goal reads now appear as successful in model context, transcripts, and diagnostics instead of being recorded as failed tool calls. #98659 Thanks @yetval.

> Failed exact-match edits now show readable current-file context even when truncation falls beside an emoji or other non-BMP character. #99527 Thanks @mikasa0818.

> Documented compaction retry timing behavior to make future maintenance safer without changing runtime behavior. #89585

> Prevented valid Codex long-context results from causing false QA failures while still checking that earlier evidence remains available. #96366 Thanks @vincentkoc.

> Aligned internal conversation audience labels with verified group context for future access-control work. #99816

> Corrected QA prompt handling so validation responds to the user's actual instruction rather than hidden runtime context. #100272 Thanks @marvinthebored, @obviyus, @peetiegonzalez.

> Prepared compaction, scheduled checks, and session forks for future storage changes without altering behavior. #101179 Thanks @jalehman.

> Prepared session routing, goals, delivery, and compaction tracking for safer storage changes without altering workflows. #101180 Thanks @jalehman.

Source: https://docs.openclaw.ai/releases/2026.7.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-07-13-5-projects-and-workspaces-changes-in-v2026-7-1|5 Projects and Workspaces changes in v2026.7.1]] · Projects and Workspaces
- [[Changes/OpenClaw/2026-07-13-99-developer-workflow-changes-in-v2026-7-1|99 Developer Workflow changes in v2026.7.1]] · Developer Workflow
- [[Changes/OpenClaw/2026-07-13-10-accessibility-and-localization-changes-in-v2026-7-1|10 Accessibility and Localization changes in v2026.7.1]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-07-13-64-interface-experience-changes-in-v2026-7-1|64 Interface Experience changes in v2026.7.1]] · Interface Experience
- [[Changes/OpenClaw/2026-07-13-whatsapp-and-telegram-default-account-routing-warnings-are-now-available-through|WhatsApp and Telegram default-account routing warnings are now available through…]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-07-13-132-agent-mode-changes-in-v2026-7-1|132 Agent Mode changes in v2026.7.1]] · Agent Mode
- [[Changes/OpenClaw/2026-07-13-after-one-generated-video-clip-is-ready-a-different-next-clip-can-start-immediat|After one generated video clip is ready, a different next clip can start immediately…]] · Video Generation
- [[Changes/OpenClaw/2026-07-13-79-automation-and-scheduling-changes-in-v2026-7-1|79 Automation and Scheduling changes in v2026.7.1]] · Automation and Scheduling
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
## Nearby in Context Window

- Earlier: 2026-07-10 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-07-10-press-tab-to-switch-the-context-window-in-model|Press Tab to switch the context window in /model]]
- Later: 2026-07-13 · OpenCode · [[Changes/OpenCode/2026-07-13-desktop-aligned-context-token-counts-with-usage-totals|Desktop Aligned context token counts with usage totals]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-04 · Cursor · [[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2 Context Window changes in 0.2.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-07-13-1da3e8&body=Card%3A%20Changes%2FOpenClaw%2F2026-07-13-69-context-window-changes-in-v2026-7-1.md%0ACard%20ID%3A%20openclaw-2026-07-13-1da3e8%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.7.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->