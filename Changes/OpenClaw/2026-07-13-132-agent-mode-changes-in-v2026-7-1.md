---
card_id: openclaw-2026-07-13-50a48c
date: '2026-07-13'
description: 'OpenClaw · 2026-07-13 · Agent Mode: 132 changes in v2026.7.1 — A default
  agent selected in the Control UI now remains selected after refresh without saving…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1103
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 1563347a578ded2ed95d05449f718a838eae25559917ead8bcb3da04975aca5d
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-07-13-50a48c
  comparison: ''
  date: '2026-07-13'
  description: 'OpenClaw — v2026.7.1: 132 Agent Mode changes'
  evidence:
  - quote: 'A default agent selected in the Control UI now remains selected after
      refresh without saving unrelated unfinished settings. #91457 Thanks @zengwen-dt.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Agents can use targetless message.send for progress or intermediate updates
      in the current WebChat without an explicit destination. #97167 Related #96840
      . Thanks @mantiscartography, @zhangguiping-xydt.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Control UI now shows channel-triggered agent runs as in progress, so users
      can tell that messages from channels such as Weixin are actively being handled.
      #98257 Thanks @scotthuang.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Control UI users can organize large session lists by custom group, channel,
      kind, agent, or date, with persistent assignments and drag-and-drop management.
      #100262'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The Control UI keeps Overview, Workboard, Agents, and More visible while
      allowing the session list to use available height and scroll independently.
      #100742'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'During device pairing, / pair qr now follows the same authorized pairing
      flow as /pair qr without starting an agent turn or disrupting the existing Control
      UI route. #98262 Thanks @brokemac79.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The Control UI Skills page now shows readable Agent and Search labels
      with aligned filters and correctly sized selection controls. #100526 Thanks
      @evan-ym.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Clearing a Control UI session model override now shows the selected agent''s
      own default model rather than the unrelated global default. #100719 Thanks @hyspacex.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Fresh installs can now complete conversational Crestodian setup, approve
      the proposed plan once, connect channels, and continue into the normal agent
      while classic and scripted onboarding remain available. #99935'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: OpenClaw now works more cleanly with coding agents that live outside the
      current chat. openclaw attach can open Claude Code against the main or a selected
      Gateway session with temporary, revocable access instead of process-wide credentials.
      Codex app-server sessions can resume, delegate to native subagents, and return
      their results as tracked work, while Copilot sessions can use explicitly selected
      custom providers and restart when their connection settings change.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Codex app-server agents can again list allowed agents, spawn OpenClaw
      or connected subagents, and yield during delegated work without resumed heartbeats
      hitting incompatible tool definitions. #99561 Related #99464 . Thanks @100yenadmin,
      @joshavant.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Slack threads retain their conversation history more consistently, interactive
      cards and progress stay in the right place, and accepted replies are less likely
      to be repeated after an uncertain confirmation. Long-running conversations also
      avoid more unnecessary waits before reaching the agent.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Scheduled jobs can react when an external command finishes or a watched
      condition changes, so the full agent runs only when there is something new to
      handle. Reapplying the same declaration updates the intended job in place, preserving
      identity and history instead of creating duplicate schedules.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Agents can now save a browser download to a chosen guarded path or wait
      for a delayed export, receiving the final URL, filename, and local path. #101369
      Thanks @grd-chang.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Authenticated admins can open an interactive terminal in an agent workspace
      from Gateway-backed controls, while fully sandboxed agents remain blocked and
      the feature can be disabled with gateway.terminal.enabled . f083f35
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Scheduled and heartbeat-driven Slack messages now use the configured agent
      name and icon, with graceful fallback to the app identity when Slack rejects
      customization. #84335 Thanks @rohang2005.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Slack replies in very long threads and on busy Gateways now avoid several
      unnecessary waits, reducing stalls before thread and direct-message events reach
      the agent. #101888 Thanks @obviyus.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Agents now answer iMessage polls, including polls with comments, with
      one native vote instead of an ordinary text answer, a repeated selection, or
      a separate reply to the comment. #98781 Thanks @omarshahine.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'ClickClack agent replies to top-level messages now stay in the active
      channel or direct message, while replies inside real threads remain threaded.
      #100582 Thanks @marvinthebored, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Long Matrix reply quotes sent to agents now truncate emoji and other multi-unit
      characters without leaving broken text. #97471 Thanks @ly-wang19.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Microsoft Teams Adaptive Card button clicks now deliver the submitted
      value to the agent instead of arriving as empty messages. #97546 Thanks @jimmypuckett.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Long Feishu comments containing emoji at the cutoff now reach the agent
      as valid text instead of being split into malformed characters. #97595 Thanks
      @llagy007, @weeli-009.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Completions from subagents, scheduled tasks, media jobs, and agent harnesses
      now return through the same configured account, destination, and thread that
      requested them. #98240 Thanks @yetval.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Ambient group chats now remain silent unless the agent deliberately sends
      a message, without stray status lines, tool summaries, compaction notices, delivery
      warnings, or overflow follow-ups. #99145 Thanks @obviyus.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Agents catching up in busy group chats now receive clearer sender-by-sender
      history, making multi-person conversations easier to follow without exposing
      local paths or URLs. #100366 Thanks @gorkem2020.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Telegram messages entering through isolated ingress now proceed to the
      agent reply instead of replaying the same message in a loop. #96847 Thanks @obviyus.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Telegram rich messages and text-bearing forwards without a normal caption
      now reach the agent as readable conversation content instead of an unsupported-message
      placeholder. #98735 Thanks @obviyus.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Telegram plugins can now turn a button tap into a normal user reply to
      the agent, while failed or skipped submissions leave the button available for
      another attempt. #98922 Thanks @goldmar.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'sessions_send now rejects Telegram topic child sessions before dispatch
      and directs callers to the parent group, reducing misrouted agent work. #99845
      Thanks @nianjiuzst, @qingminglong.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Telegram group agents now post visible replies when directly mentioned
      or replied to, while continuing to ignore unaddressed background chatter. #99866
      Related #99854 . Thanks @obviyus.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Slack agents can now read thread messages whose visible content exists
      only in attachments or blocks, including alerts with empty top-level text. #97727
      Thanks @chthtlo.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Slack agents can now identify admitted bot-authored messages through is_bot:
      true , making it easier to prevent unwanted bot-to-bot replies. #97822 Thanks
      @masatohoshino, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Discord agents now receive is_bot: true for admitted bot messages while
      human and PluralKit sender behavior stays unchanged. #97824 Thanks @masatohoshino,
      @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Slack replies now keep each agent''s custom name and avatar through streaming
      or fallback delivery instead of reverting to the app identity. #100084 Thanks
      @moerai.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Bursts of long iMessage messages can now be combined without cutting an
      emoji in half and sending broken text to the agent. #97598 Thanks @weeli-009.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Google Chat agents can now distinguish allowed bot messages through is_bot:
      true and handle automated senders differently from people. #97825 Thanks @masatohoshino,
      @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Microsoft Teams thread history now preserves literal entity text such
      as &lt;APIKEY&gt; instead of turning it into different markup before the agent
      sees it. #96342 Thanks @ly-wang19.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Feishu card headers now show a clean agent emoji and name instead of descriptive
      text from identity.emoji , while flags, skin-tone variants, family emoji, and
      other valid sequences remain intact. #96587 Thanks @harjothkhara, @leedongyu1128.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Repeated Nostr profile publishing now clears relay timeout timers after
      success, reducing stale resource buildup in long-running agents. #98720 Related
      #98463 . Thanks @wangmiao0668000666, @zhanglei99586.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Long emoji-containing agent labels now produce clean native channel thread
      names and introductions instead of broken characters. #101527 Thanks @lsr911.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Claude CLI-backed agents now show native reasoning in /reasoning stream
      or /reasoning on , while /reasoning off consistently suppresses it for queued
      follow-ups too. #99401 Thanks @marvinthebored.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'vLLM, Ollama proxies, and other OpenAI-compatible gateways can deliver
      streamed replies even when they incorrectly label an event stream as JSON, avoiding
      an early parsing failure that previously ended the agent run. #96503 Thanks
      @zengwen-dt.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'openclaw agent --local now reports a clear first-event timeout when a
      provider opens a stream but never sends usable output instead of appearing to
      hang indefinitely. #98525 Thanks @osolmaz.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'With models.mode set to replace , agent startup now uses only explicitly
      configured providers and skips the slow implicit provider scan. #82638 Related
      #66957 . Thanks @eldar702, @wangzhengshu.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Agent runs can move to the next configured model after a provider drops
      a stream, while genuine cancellations still stop promptly. #90908 Thanks @shengting.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'OpenRouter cost tracking now caps unexpectedly large metadata responses
      and keeps the original streamed estimate instead of disrupting the agent turn.
      #97490 Thanks @hugenshen.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'ClawRouter models selected in agent defaults now resolve at runtime when
      the credential is stored in an auth profile instead of the environment. #99759'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Anthropic agents routed through AWS Bedrock can keep Feishu Bitable write
      tools enabled without the tool definitions blocking every conversation. #94990
      Thanks @twinslee, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Agents created by copying credentials now preserve the source agent''s
      portable provider-profile priority instead of unexpectedly choosing a different
      credential. #100833 Thanks @machine3at.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Very long OpenRouter Fusion model IDs now remain valid Unicode in the
      agent prompt instead of showing a corrupted character when an emoji reaches
      the display limit. #104433 Thanks @zhangguiping-xydt.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Images shared from iOS or through node agent.request now remain attached
      to the correct conversation turn after history reload, so later messages can
      still use them. #86936 Thanks @peterdsp.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Compacted agent history now lists genuine tool failures instead of repeatedly
      mislabeling successful subagent launches, including when older transcript records
      contain the incorrect error flag. #96842 Thanks @nxmxbbd.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Resuming work from a project now opens only that project''s saved agent
      session, preventing unrelated transcripts from being mixed together. #97785
      Related #96542 . Thanks @qingminglong, @yetval.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Agents in long-running WebChat, Discord, and other direct sessions can
      keep reading fresh command, file, browser, and status output instead of seeing
      it disappear or turn into an image placeholder. #98955 Related #98874 . Thanks
      @lamkan0210, @momothemage.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Resetting a multi-agent room now restores message delivery promptly instead
      of blocking most agents'' acknowledgement and queued replies for several minutes.
      #99091 Thanks @gorkem2020, @zengwen-dt.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Embedded agents now receive well-formed summaries of long media or JSON
      values instead of broken characters at Unicode truncation boundaries. #101311
      Thanks @alix-007.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'A successfully completed main-agent conversation now continues in the
      same session on the next message instead of unexpectedly resetting and archiving
      its transcript. #99985 Thanks @sunnyshu0925.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: The Gateway now starts, connects, reloads, and reports health with clearer
      behavior across configuration, networking, task routing, and result delivery.
      Agents are less likely to lose their selected workspace or conversation, background
      work reaches the right destination more consistently, and tool failures can
      stay out of chat progress when a useful final reply is still available.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Legacy subagent sessions now follow their actual nesting level, so nested-agent
      limits and controls no longer fall back to top-level behavior. #54593 Thanks
      @ruanrrn.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Telling an agent to remember a preference no longer triggers the unrelated
      warning used for promises to schedule an automatic reminder. #93862 Thanks @arkyu2077.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Truncated agent logs and diagnostic previews now keep emoji and other
      extended Unicode characters intact at the cutoff. #96296 Thanks @ly-wang19.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Successful embedded-agent subagent launches now remain successful in transcripts
      and later compaction summaries instead of being recorded as tool failures, while
      real launch failures stay visible. #96851 Thanks @neomail2, @parveshsaini.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Codex-runtime transcripts and compaction summaries now keep successful
      subagent launches and goal operations out of failure records, while genuine
      failures remain visible and accepted-launch hooks can run. #96856 Thanks @nxmxbbd.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Long agent grep lines now truncate emoji and uncommon CJK characters cleanly
      instead of ending with corrupted replacement symbols. #97559 Thanks @zenglingbiao.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Agents can now read structured JSON and resource tool results during provider
      replay instead of receiving an empty result or generic media placeholder. #97742
      Thanks @obviyus.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Codex app-server agents can again list allowed agents, spawn OpenClaw
      or ACP subagents, and yield during delegated work without resumed heartbeats
      hitting incompatible tool definitions. #99561 Related #99464 . Thanks @100yenadmin,
      @joshavant.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Requester agents now receive a follow-up when an accepted sessions_send
      delivery later fails because the target session is locked, so they can retry
      or choose another route. #99907 Thanks @849261680, @alex-heyuqing.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Agent sessions are less likely to lose output, alter unrelated formatting,
      stall after temporary provider errors, reject BMP images, or drop longer ChatGPT
      connections. #99949'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Embedded agent jobs with an explicitly longer timeout now keep their lane
      until that requested deadline instead of being recovered at the default limit.
      1437512 Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Parent sessions waiting on a subagent now receive the subagent''s actual
      hard-timeout phase and timestamps instead of a generic timeout. #89367 Thanks
      @pick-cat.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Malformed cyclic attachments can no longer crash subagent delivery-evidence
      collection, so the reply handoff completes and still returns reachable media
      URLs. #97041 Thanks @pick-cat.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'A parent session waiting on several subagents now resumes and returns
      their combined results when the last outstanding work finishes, without requiring
      the user to send another message. #97090 Thanks @galiniliev.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Operators can inspect the effective tools for global sessions assigned
      to any configured agent, not only the default one. #97265 Thanks @pick-cat.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: '/subagents list now shortens long names and task descriptions containing
      emoji or uncommon CJK characters without displaying broken glyphs. #97557 Thanks
      @zenglingbiao.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Claude CLI agent runs now fail clearly when messaging tools are unavailable,
      recover when Claude exits without a result, retain more long-session continuity,
      and clean up prompt images and failed preparation files. #99159 Related #98946
      . Thanks @obviyus.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Built-in grep stream failures now become ordinary tool errors instead
      of crashing the agent runtime, hanging the search, or leaving incomplete results
      unexplained. #101014 Thanks @cxbasdev.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: After a Gateway restart, a redirected subagent now continues the user's
      newest instruction instead of returning to stale work. 7b5d86e Thanks @amittell.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: A wedged provider call now releases its embedded agent lane on a bounded
      watchdog instead of indefinitely blocking queued work when run timeouts are
      disabled. ec28935 Thanks @arismontclair, @obviyus, @patelmm79.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Agents running on macOS 26 now receive the macOS product version in their
      runtime prompt instead of the Darwin kernel version. #95225 Thanks @sunlit-deng.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Successful agent tools that return safe plain text now show that output
      instead of leaving users with an apparently empty result. #99526 Related #99523
      . Thanks @snowzlm.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Malformed surrogate HTML entities in provider output no longer corrupt
      agent tool arguments, transcripts, or URLs, while legitimate entities and emoji
      still decode normally. #99564 Thanks @mikasa0818.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Compact subagent lists now keep long labels and task text within their
      display budget without splitting emoji or breaking alignment. #100013 Thanks
      @qingminglong.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Very long agent conversations are less likely to loop through failed overflow
      recovery because compaction now reflects the prompt OpenClaw actually prepared.
      #101181 Thanks @jalehman.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Normally completed agent and subagent runs no longer appear as error-level
      log entries, reducing false alarms while genuine failures remain elevated. #101703
      Thanks @zengwen-dt.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Oversized agent tool results now preserve complete emoji and similar Unicode
      characters when shortened before being sent to the model. #102087 Thanks @chengzhichao-xydt.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Authorized operators now have a durable audit history for agent and tool
      activity, with filters, stable paging, bounded JSON export, configurable recording,
      and automatic retention limits. #98704'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Running a read-only local Gateway check no longer leaves stale pairing
      permissions that block a later agent, admin, write, or device-approval command.
      #96002 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Sandboxed agents with host browser control disabled can no longer reach
      a signed-in host browser through a paired browser node. #97958 Thanks @eleqtrizit.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Agent payload logs and cache traces now redact provider keys even when
      those credentials appear inside free-text diagnostic values. d8ee630 Thanks
      @joshavant.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'After an agent is removed, its leftover sessions can no longer start new
      model runs through the Gateway. #97260 Thanks @obviyus, @pick-cat.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Unsafe, malformed, or unexpectedly large fd and ripgrep helper archives
      now fail early and clean up after themselves instead of putting agent setup
      at risk. #98988 Thanks @leonidaslux, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'openclaw security audit now warns that per-agent skill allowlists do not
      prevent shell-capable agents from reaching globally configured MCP servers.
      #98352 Thanks @momothemage.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Skills created by agents now remain pending for Skill Workshop review
      and approval instead of becoming active immediately without the expected safeguards.
      #98346 Related #96054 . Thanks @momothemage, @xianshishan.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Multi-user bridges using openclaw agent --agent ... --channel ... --to
      ... now keep recipients in separate sessions when per-recipient isolation is
      configured. #101507 Thanks @pingfanfan, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Long exec auto-review explanations containing emoji or supplementary CJK
      characters now shorten cleanly instead of showing a broken replacement symbol.
      #101513 Thanks @wm0018.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: macOS improves first-run local-agent setup, native chat and session controls,
      remote-mode tunnels, app launching, background efficiency, and device identity
      across upgrades and reconnects.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android Chat now includes a New chat action and a / command browser that
      filters the current agent''s advertised commands without dropping command arguments.
      #98796 Thanks @iwhatsskill, @solvely-colin.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'TUI users can now submit prompts while an agent is working and receive
      the configured followup, collect, or interrupt behavior, with Esc and /stop
      canceling only the intended work. #100123 Thanks @kevinlp, @sebtardif.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The iOS chat experience now offers useful starting prompts, clearer pairing
      and setup actions, better agent placeholders, and steadier message ordering
      during refreshes. #99243 Thanks @jcooley8.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Finder-launched macOS sessions can now use SSH aliases backed by common
      user-installed ProxyCommand helpers without losing agent state or failing Gateway
      readiness checks. #100214'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Realtime Talk consult calls acknowledge as soon as the embedded agent
      run is accepted, rather than waiting for it to finish. #101091 Thanks @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Repeated submits while the TUI agent is busy now update one warning instead
      of flooding the conversation with duplicate notices. #99879 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Owner-operated native Codex agents can now use selected apps already connected
      to the operator''s Codex account, with a bounded per-thread allowlist and existing
      approval controls preserved. #100973 Thanks @pash-openai.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Owner-controlled agents can opt into appServer.homeScope: "user" to inspect
      and safely fork the same Codex threads available in Desktop and the CLI. #99821'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'openclaw sessions --json now includes available subagent lineage and runtime
      details such as parent linkage, workspace, depth, role, timestamps, and status.
      #87917 Related #80286 . Thanks @islandpreneur007, @zhangguiping-xydt.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Debug proxy capture now keeps oversized or endless response bodies from
      crashing the agent, while retaining useful status and header metadata. #97551
      Thanks @alix-007.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'openclaw doctor now evaluates the default agent''s actual per-agent bootstrap
      limits, producing accurate truncation warnings and remediation guidance. #84424
      Thanks @kasangyong, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'openclaw doctor no longer aborts when a configured agent workspace has
      not been created yet, while real file operations still enforce workspace boundaries.
      #89226 Thanks @sasan1200, @shifengwang333-ai.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Setup now checks the configured custom agent or auth directory for credentials
      instead of reporting the wrong bootstrap state from a default location. 0fd69dc
      Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The bundled imsg skill now guides agents toward the correct direct or
      group conversation, stable targets, least-privilege actions, and confirmation
      before visible or sensitive changes. #100105 Thanks @omarshahine.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: The onboarding reference now explains that bare openclaw starts onboarding
      for a missing config, opens Crestodian for an invalid config, and launches the
      agent TUI for a valid config. d9dbee7
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Browser downloads now tell the agent the saved filename and path, helping
      it use the completed download instead of retrying the action. #93307 Thanks
      @sunlit-deng.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Scheduled agent turns using claude-cli or another CLI backend now start
      normally, while explicitly unsupported tool restrictions still fail closed.
      #95615 Thanks @anagnorisis2peripeteia, @obviyus.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Failed shell-tool messages now separate the command the agent typed from
      framework labels and show the exit code, node, and working directory more clearly.
      #97511 Thanks @aditya-vithaldas.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Agent commands with an invalid explicit workdir , including a literal
      ~ , now stop clearly instead of running from an unintended fallback directory.
      #94441 Thanks @jesse-merhi, @renaudcerrato.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Agent workflows can now survive transient stdout or stderr read failures
      from helper processes instead of losing the whole OpenClaw process. #100522
      Thanks @cxbasdev, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Agent runs now stop cleanly when a write , edit , or apply_patch operation
      would make no change, preventing repeated false-progress retries while real
      mutations and valid sibling edits continue normally. #97044 Thanks @vincentkoc,
      @zw-xysk.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'When users say things like "next time" or "remember to," OpenClaw can
      now offer one reviewable Skill Workshop proposal without requiring autonomous
      capture or repeatedly prompting after dismissal. #100692'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'When an installed fd or rg binary is unusable, agent search can now install
      a working copy and recover instead of failing repeatedly. #96361 Thanks @miorbnli.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'A failed find search now returns one contained tool error and stops its
      fd process instead of risking an agent crash or orphaned search. #101158 Thanks
      @cxbasdev.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Broken child-process output, timeouts, and aborts during agent shell commands
      are now contained instead of causing rare Gateway crashes. #101370 Thanks @wings1029.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The agent find tool now reports an interrupted or failed directory search
      as an error instead of returning a partial match list as complete. #99446 Thanks
      @zhangguiping-xydt.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Repeated failed or cancelled agent directory listings now release their
      cancellation listeners, avoiding listener buildup over time. #101588 Thanks
      @lzw112.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Added Cursor''s command-line agent as an optional engine for repository
      code reviews. #97348 Thanks @hxy91819.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Added coverage for global and per-agent command-highlighting settings
      and their fallback behavior. #98087 Thanks @solodmd.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Made configured model references more consistent across the catalog, agent
      runtime, Gateway, and plugins without changing intended behavior. #99682 Related
      #99674 . Thanks @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Removed redundant list-cleanup layers across channels, agents, the CLI,
      and diagnostics to make maintenance clearer. #99702 Related #99697 . Thanks
      @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Unified cancellation handling so stops and timeouts remain consistent
      across agent, Gateway, reply, media, and process workflows. #99753 Thanks @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Consolidated repeated internal task handoffs across setup, approvals,
      agent turns, and plugins without changing behavior. #99755 Thanks @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Unified numeric limit handling across agent workflows while preserving
      their existing allowed ranges. #99786 Thanks @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Extended consistent provider and model reference handling across media,
      speech, agent policy, and diagnostic workflows. #99790 Thanks @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Tightened internal agent code boundaries so maintainers have fewer accidental
      interfaces to preserve. #100909 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 132-agent-mode-changes-in-v2026-7-1
  source_release: openclaw-2026-07-13-v2026-7-1-c2063718
  source_type: openclaw_changelog
  theme: agent-mode
  title: 132 Agent Mode changes in v2026.7.1
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-07-13-elevenagents|ElevenAgents]]'
- '[[Changes/ElevenLabs/2026-07-13-javascript-sdk|JavaScript SDK]]'
- '[[Changes/Google Antigravity/2026-07-13-2-agent-mode-changes-in-hub-v2-3-0-queued-messages-plain|2
  Agent Mode changes in HUB v2.3.0 — Queued messages, plain…]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-07-13-v2026-7-1-c2063718|openclaw-2026-07-13-v2026-7-1-c2063718]]'
source_type: openclaw_changelog
theme: agent-mode
title: 132 Agent Mode changes in v2026.7.1
type: change
---

<!-- chronolog:begin region="header" -->
# 132 Agent Mode changes in v2026.7.1

**OpenClaw** · 2026-07-13 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.7.1) · from [[Releases/OpenClaw/openclaw-2026-07-13-v2026-7-1-c2063718|v2026.7.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> A default agent selected in the Control UI now remains selected after refresh without saving unrelated unfinished settings. #91457 Thanks @zengwen-dt.

> Agents can use targetless message.send for progress or intermediate updates in the current WebChat without an explicit destination. #97167 Related #96840 . Thanks @mantiscartography, @zhangguiping-xydt.

> Control UI now shows channel-triggered agent runs as in progress, so users can tell that messages from channels such as Weixin are actively being handled. #98257 Thanks @scotthuang.

> Control UI users can organize large session lists by custom group, channel, kind, agent, or date, with persistent assignments and drag-and-drop management. #100262

> The Control UI keeps Overview, Workboard, Agents, and More visible while allowing the session list to use available height and scroll independently. #100742

> During device pairing, / pair qr now follows the same authorized pairing flow as /pair qr without starting an agent turn or disrupting the existing Control UI route. #98262 Thanks @brokemac79.

> The Control UI Skills page now shows readable Agent and Search labels with aligned filters and correctly sized selection controls. #100526 Thanks @evan-ym.

> Clearing a Control UI session model override now shows the selected agent's own default model rather than the unrelated global default. #100719 Thanks @hyspacex.

> Fresh installs can now complete conversational Crestodian setup, approve the proposed plan once, connect channels, and continue into the normal agent while classic and scripted onboarding remain available. #99935

> OpenClaw now works more cleanly with coding agents that live outside the current chat. openclaw attach can open Claude Code against the main or a selected Gateway session with temporary, revocable access instead of process-wide credentials. Codex app-server sessions can resume, delegate to native subagents, and return their results as tracked work, while Copilot sessions can use explicitly selected custom providers and restart when their connection settings change.

> Codex app-server agents can again list allowed agents, spawn OpenClaw or connected subagents, and yield during delegated work without resumed heartbeats hitting incompatible tool definitions. #99561 Related #99464 . Thanks @100yenadmin, @joshavant.

> Slack threads retain their conversation history more consistently, interactive cards and progress stay in the right place, and accepted replies are less likely to be repeated after an uncertain confirmation. Long-running conversations also avoid more unnecessary waits before reaching the agent.

> Scheduled jobs can react when an external command finishes or a watched condition changes, so the full agent runs only when there is something new to handle. Reapplying the same declaration updates the intended job in place, preserving identity and history instead of creating duplicate schedules.

> Agents can now save a browser download to a chosen guarded path or wait for a delayed export, receiving the final URL, filename, and local path. #101369 Thanks @grd-chang.

> Authenticated admins can open an interactive terminal in an agent workspace from Gateway-backed controls, while fully sandboxed agents remain blocked and the feature can be disabled with gateway.terminal.enabled . f083f35

> Scheduled and heartbeat-driven Slack messages now use the configured agent name and icon, with graceful fallback to the app identity when Slack rejects customization. #84335 Thanks @rohang2005.

> Slack replies in very long threads and on busy Gateways now avoid several unnecessary waits, reducing stalls before thread and direct-message events reach the agent. #101888 Thanks @obviyus.

> Agents now answer iMessage polls, including polls with comments, with one native vote instead of an ordinary text answer, a repeated selection, or a separate reply to the comment. #98781 Thanks @omarshahine.

> ClickClack agent replies to top-level messages now stay in the active channel or direct message, while replies inside real threads remain threaded. #100582 Thanks @marvinthebored, @vincentkoc.

> Long Matrix reply quotes sent to agents now truncate emoji and other multi-unit characters without leaving broken text. #97471 Thanks @ly-wang19.

> Microsoft Teams Adaptive Card button clicks now deliver the submitted value to the agent instead of arriving as empty messages. #97546 Thanks @jimmypuckett.

> Long Feishu comments containing emoji at the cutoff now reach the agent as valid text instead of being split into malformed characters. #97595 Thanks @llagy007, @weeli-009.

> Completions from subagents, scheduled tasks, media jobs, and agent harnesses now return through the same configured account, destination, and thread that requested them. #98240 Thanks @yetval.

> Ambient group chats now remain silent unless the agent deliberately sends a message, without stray status lines, tool summaries, compaction notices, delivery warnings, or overflow follow-ups. #99145 Thanks @obviyus.

> Agents catching up in busy group chats now receive clearer sender-by-sender history, making multi-person conversations easier to follow without exposing local paths or URLs. #100366 Thanks @gorkem2020.

> Telegram messages entering through isolated ingress now proceed to the agent reply instead of replaying the same message in a loop. #96847 Thanks @obviyus.

> Telegram rich messages and text-bearing forwards without a normal caption now reach the agent as readable conversation content instead of an unsupported-message placeholder. #98735 Thanks @obviyus.

> Telegram plugins can now turn a button tap into a normal user reply to the agent, while failed or skipped submissions leave the button available for another attempt. #98922 Thanks @goldmar.

> sessions_send now rejects Telegram topic child sessions before dispatch and directs callers to the parent group, reducing misrouted agent work. #99845 Thanks @nianjiuzst, @qingminglong.

> Telegram group agents now post visible replies when directly mentioned or replied to, while continuing to ignore unaddressed background chatter. #99866 Related #99854 . Thanks @obviyus.

> Slack agents can now read thread messages whose visible content exists only in attachments or blocks, including alerts with empty top-level text. #97727 Thanks @chthtlo.

> Slack agents can now identify admitted bot-authored messages through is_bot: true , making it easier to prevent unwanted bot-to-bot replies. #97822 Thanks @masatohoshino, @vincentkoc.

> Discord agents now receive is_bot: true for admitted bot messages while human and PluralKit sender behavior stays unchanged. #97824 Thanks @masatohoshino, @vincentkoc.

> Slack replies now keep each agent's custom name and avatar through streaming or fallback delivery instead of reverting to the app identity. #100084 Thanks @moerai.

> Bursts of long iMessage messages can now be combined without cutting an emoji in half and sending broken text to the agent. #97598 Thanks @weeli-009.

> Google Chat agents can now distinguish allowed bot messages through is_bot: true and handle automated senders differently from people. #97825 Thanks @masatohoshino, @vincentkoc.

> Microsoft Teams thread history now preserves literal entity text such as &lt;APIKEY&gt; instead of turning it into different markup before the agent sees it. #96342 Thanks @ly-wang19.

> Feishu card headers now show a clean agent emoji and name instead of descriptive text from identity.emoji , while flags, skin-tone variants, family emoji, and other valid sequences remain intact. #96587 Thanks @harjothkhara, @leedongyu1128.

> Repeated Nostr profile publishing now clears relay timeout timers after success, reducing stale resource buildup in long-running agents. #98720 Related #98463 . Thanks @wangmiao0668000666, @zhanglei99586.

> Long emoji-containing agent labels now produce clean native channel thread names and introductions instead of broken characters. #101527 Thanks @lsr911.

> Claude CLI-backed agents now show native reasoning in /reasoning stream or /reasoning on , while /reasoning off consistently suppresses it for queued follow-ups too. #99401 Thanks @marvinthebored.

> vLLM, Ollama proxies, and other OpenAI-compatible gateways can deliver streamed replies even when they incorrectly label an event stream as JSON, avoiding an early parsing failure that previously ended the agent run. #96503 Thanks @zengwen-dt.

> openclaw agent --local now reports a clear first-event timeout when a provider opens a stream but never sends usable output instead of appearing to hang indefinitely. #98525 Thanks @osolmaz.

> With models.mode set to replace , agent startup now uses only explicitly configured providers and skips the slow implicit provider scan. #82638 Related #66957 . Thanks @eldar702, @wangzhengshu.

> Agent runs can move to the next configured model after a provider drops a stream, while genuine cancellations still stop promptly. #90908 Thanks @shengting.

> OpenRouter cost tracking now caps unexpectedly large metadata responses and keeps the original streamed estimate instead of disrupting the agent turn. #97490 Thanks @hugenshen.

> ClawRouter models selected in agent defaults now resolve at runtime when the credential is stored in an auth profile instead of the environment. #99759

> Anthropic agents routed through AWS Bedrock can keep Feishu Bitable write tools enabled without the tool definitions blocking every conversation. #94990 Thanks @twinslee, @vincentkoc.

> Agents created by copying credentials now preserve the source agent's portable provider-profile priority instead of unexpectedly choosing a different credential. #100833 Thanks @machine3at.

> Very long OpenRouter Fusion model IDs now remain valid Unicode in the agent prompt instead of showing a corrupted character when an emoji reaches the display limit. #104433 Thanks @zhangguiping-xydt.

> Images shared from iOS or through node agent.request now remain attached to the correct conversation turn after history reload, so later messages can still use them. #86936 Thanks @peterdsp.

> Compacted agent history now lists genuine tool failures instead of repeatedly mislabeling successful subagent launches, including when older transcript records contain the incorrect error flag. #96842 Thanks @nxmxbbd.

> Resuming work from a project now opens only that project's saved agent session, preventing unrelated transcripts from being mixed together. #97785 Related #96542 . Thanks @qingminglong, @yetval.

> Agents in long-running WebChat, Discord, and other direct sessions can keep reading fresh command, file, browser, and status output instead of seeing it disappear or turn into an image placeholder. #98955 Related #98874 . Thanks @lamkan0210, @momothemage.

> Resetting a multi-agent room now restores message delivery promptly instead of blocking most agents' acknowledgement and queued replies for several minutes. #99091 Thanks @gorkem2020, @zengwen-dt.

> Embedded agents now receive well-formed summaries of long media or JSON values instead of broken characters at Unicode truncation boundaries. #101311 Thanks @alix-007.

> A successfully completed main-agent conversation now continues in the same session on the next message instead of unexpectedly resetting and archiving its transcript. #99985 Thanks @sunnyshu0925.

> The Gateway now starts, connects, reloads, and reports health with clearer behavior across configuration, networking, task routing, and result delivery. Agents are less likely to lose their selected workspace or conversation, background work reaches the right destination more consistently, and tool failures can stay out of chat progress when a useful final reply is still available.

> Legacy subagent sessions now follow their actual nesting level, so nested-agent limits and controls no longer fall back to top-level behavior. #54593 Thanks @ruanrrn.

> Telling an agent to remember a preference no longer triggers the unrelated warning used for promises to schedule an automatic reminder. #93862 Thanks @arkyu2077.

> Truncated agent logs and diagnostic previews now keep emoji and other extended Unicode characters intact at the cutoff. #96296 Thanks @ly-wang19.

> Successful embedded-agent subagent launches now remain successful in transcripts and later compaction summaries instead of being recorded as tool failures, while real launch failures stay visible. #96851 Thanks @neomail2, @parveshsaini.

> Codex-runtime transcripts and compaction summaries now keep successful subagent launches and goal operations out of failure records, while genuine failures remain visible and accepted-launch hooks can run. #96856 Thanks @nxmxbbd.

> Long agent grep lines now truncate emoji and uncommon CJK characters cleanly instead of ending with corrupted replacement symbols. #97559 Thanks @zenglingbiao.

> Agents can now read structured JSON and resource tool results during provider replay instead of receiving an empty result or generic media placeholder. #97742 Thanks @obviyus.

> Codex app-server agents can again list allowed agents, spawn OpenClaw or ACP subagents, and yield during delegated work without resumed heartbeats hitting incompatible tool definitions. #99561 Related #99464 . Thanks @100yenadmin, @joshavant.

> Requester agents now receive a follow-up when an accepted sessions_send delivery later fails because the target session is locked, so they can retry or choose another route. #99907 Thanks @849261680, @alex-heyuqing.

> Agent sessions are less likely to lose output, alter unrelated formatting, stall after temporary provider errors, reject BMP images, or drop longer ChatGPT connections. #99949

> Embedded agent jobs with an explicitly longer timeout now keep their lane until that requested deadline instead of being recovered at the default limit. 1437512 Thanks @vincentkoc.

> Parent sessions waiting on a subagent now receive the subagent's actual hard-timeout phase and timestamps instead of a generic timeout. #89367 Thanks @pick-cat.

> Malformed cyclic attachments can no longer crash subagent delivery-evidence collection, so the reply handoff completes and still returns reachable media URLs. #97041 Thanks @pick-cat.

> A parent session waiting on several subagents now resumes and returns their combined results when the last outstanding work finishes, without requiring the user to send another message. #97090 Thanks @galiniliev.

> Operators can inspect the effective tools for global sessions assigned to any configured agent, not only the default one. #97265 Thanks @pick-cat.

> /subagents list now shortens long names and task descriptions containing emoji or uncommon CJK characters without displaying broken glyphs. #97557 Thanks @zenglingbiao.

> Claude CLI agent runs now fail clearly when messaging tools are unavailable, recover when Claude exits without a result, retain more long-session continuity, and clean up prompt images and failed preparation files. #99159 Related #98946 . Thanks @obviyus.

> Built-in grep stream failures now become ordinary tool errors instead of crashing the agent runtime, hanging the search, or leaving incomplete results unexplained. #101014 Thanks @cxbasdev.

> After a Gateway restart, a redirected subagent now continues the user's newest instruction instead of returning to stale work. 7b5d86e Thanks @amittell.

> A wedged provider call now releases its embedded agent lane on a bounded watchdog instead of indefinitely blocking queued work when run timeouts are disabled. ec28935 Thanks @arismontclair, @obviyus, @patelmm79.

> Agents running on macOS 26 now receive the macOS product version in their runtime prompt instead of the Darwin kernel version. #95225 Thanks @sunlit-deng.

> Successful agent tools that return safe plain text now show that output instead of leaving users with an apparently empty result. #99526 Related #99523 . Thanks @snowzlm.

> Malformed surrogate HTML entities in provider output no longer corrupt agent tool arguments, transcripts, or URLs, while legitimate entities and emoji still decode normally. #99564 Thanks @mikasa0818.

> Compact subagent lists now keep long labels and task text within their display budget without splitting emoji or breaking alignment. #100013 Thanks @qingminglong.

> Very long agent conversations are less likely to loop through failed overflow recovery because compaction now reflects the prompt OpenClaw actually prepared. #101181 Thanks @jalehman.

> Normally completed agent and subagent runs no longer appear as error-level log entries, reducing false alarms while genuine failures remain elevated. #101703 Thanks @zengwen-dt.

> Oversized agent tool results now preserve complete emoji and similar Unicode characters when shortened before being sent to the model. #102087 Thanks @chengzhichao-xydt.

> Authorized operators now have a durable audit history for agent and tool activity, with filters, stable paging, bounded JSON export, configurable recording, and automatic retention limits. #98704

> Running a read-only local Gateway check no longer leaves stale pairing permissions that block a later agent, admin, write, or device-approval command. #96002 Thanks @vincentkoc.

> Sandboxed agents with host browser control disabled can no longer reach a signed-in host browser through a paired browser node. #97958 Thanks @eleqtrizit.

> Agent payload logs and cache traces now redact provider keys even when those credentials appear inside free-text diagnostic values. d8ee630 Thanks @joshavant.

> After an agent is removed, its leftover sessions can no longer start new model runs through the Gateway. #97260 Thanks @obviyus, @pick-cat.

> Unsafe, malformed, or unexpectedly large fd and ripgrep helper archives now fail early and clean up after themselves instead of putting agent setup at risk. #98988 Thanks @leonidaslux, @vincentkoc.

> openclaw security audit now warns that per-agent skill allowlists do not prevent shell-capable agents from reaching globally configured MCP servers. #98352 Thanks @momothemage.

> Skills created by agents now remain pending for Skill Workshop review and approval instead of becoming active immediately without the expected safeguards. #98346 Related #96054 . Thanks @momothemage, @xianshishan.

> Multi-user bridges using openclaw agent --agent ... --channel ... --to ... now keep recipients in separate sessions when per-recipient isolation is configured. #101507 Thanks @pingfanfan, @vincentkoc.

> Long exec auto-review explanations containing emoji or supplementary CJK characters now shorten cleanly instead of showing a broken replacement symbol. #101513 Thanks @wm0018.

> macOS improves first-run local-agent setup, native chat and session controls, remote-mode tunnels, app launching, background efficiency, and device identity across upgrades and reconnects.

> Android Chat now includes a New chat action and a / command browser that filters the current agent's advertised commands without dropping command arguments. #98796 Thanks @iwhatsskill, @solvely-colin.

> TUI users can now submit prompts while an agent is working and receive the configured followup, collect, or interrupt behavior, with Esc and /stop canceling only the intended work. #100123 Thanks @kevinlp, @sebtardif.

> The iOS chat experience now offers useful starting prompts, clearer pairing and setup actions, better agent placeholders, and steadier message ordering during refreshes. #99243 Thanks @jcooley8.

> Finder-launched macOS sessions can now use SSH aliases backed by common user-installed ProxyCommand helpers without losing agent state or failing Gateway readiness checks. #100214

> Realtime Talk consult calls acknowledge as soon as the embedded agent run is accepted, rather than waiting for it to finish. #101091 Thanks @romneyda.

> Repeated submits while the TUI agent is busy now update one warning instead of flooding the conversation with duplicate notices. #99879 Thanks @vincentkoc.

> Owner-operated native Codex agents can now use selected apps already connected to the operator's Codex account, with a bounded per-thread allowlist and existing approval controls preserved. #100973 Thanks @pash-openai.

> Owner-controlled agents can opt into appServer.homeScope: "user" to inspect and safely fork the same Codex threads available in Desktop and the CLI. #99821

> openclaw sessions --json now includes available subagent lineage and runtime details such as parent linkage, workspace, depth, role, timestamps, and status. #87917 Related #80286 . Thanks @islandpreneur007, @zhangguiping-xydt.

> Debug proxy capture now keeps oversized or endless response bodies from crashing the agent, while retaining useful status and header metadata. #97551 Thanks @alix-007.

> openclaw doctor now evaluates the default agent's actual per-agent bootstrap limits, producing accurate truncation warnings and remediation guidance. #84424 Thanks @kasangyong, @vincentkoc.

> openclaw doctor no longer aborts when a configured agent workspace has not been created yet, while real file operations still enforce workspace boundaries. #89226 Thanks @sasan1200, @shifengwang333-ai.

> Setup now checks the configured custom agent or auth directory for credentials instead of reporting the wrong bootstrap state from a default location. 0fd69dc Thanks @vincentkoc.

> The bundled imsg skill now guides agents toward the correct direct or group conversation, stable targets, least-privilege actions, and confirmation before visible or sensitive changes. #100105 Thanks @omarshahine.

> The onboarding reference now explains that bare openclaw starts onboarding for a missing config, opens Crestodian for an invalid config, and launches the agent TUI for a valid config. d9dbee7

> Browser downloads now tell the agent the saved filename and path, helping it use the completed download instead of retrying the action. #93307 Thanks @sunlit-deng.

> Scheduled agent turns using claude-cli or another CLI backend now start normally, while explicitly unsupported tool restrictions still fail closed. #95615 Thanks @anagnorisis2peripeteia, @obviyus.

> Failed shell-tool messages now separate the command the agent typed from framework labels and show the exit code, node, and working directory more clearly. #97511 Thanks @aditya-vithaldas.

> Agent commands with an invalid explicit workdir , including a literal ~ , now stop clearly instead of running from an unintended fallback directory. #94441 Thanks @jesse-merhi, @renaudcerrato.

> Agent workflows can now survive transient stdout or stderr read failures from helper processes instead of losing the whole OpenClaw process. #100522 Thanks @cxbasdev, @vincentkoc.

> Agent runs now stop cleanly when a write , edit , or apply_patch operation would make no change, preventing repeated false-progress retries while real mutations and valid sibling edits continue normally. #97044 Thanks @vincentkoc, @zw-xysk.

> When users say things like "next time" or "remember to," OpenClaw can now offer one reviewable Skill Workshop proposal without requiring autonomous capture or repeatedly prompting after dismissal. #100692

> When an installed fd or rg binary is unusable, agent search can now install a working copy and recover instead of failing repeatedly. #96361 Thanks @miorbnli.

> A failed find search now returns one contained tool error and stops its fd process instead of risking an agent crash or orphaned search. #101158 Thanks @cxbasdev.

> Broken child-process output, timeouts, and aborts during agent shell commands are now contained instead of causing rare Gateway crashes. #101370 Thanks @wings1029.

> The agent find tool now reports an interrupted or failed directory search as an error instead of returning a partial match list as complete. #99446 Thanks @zhangguiping-xydt.

> Repeated failed or cancelled agent directory listings now release their cancellation listeners, avoiding listener buildup over time. #101588 Thanks @lzw112.

> Added Cursor's command-line agent as an optional engine for repository code reviews. #97348 Thanks @hxy91819.

> Added coverage for global and per-agent command-highlighting settings and their fallback behavior. #98087 Thanks @solodmd.

> Made configured model references more consistent across the catalog, agent runtime, Gateway, and plugins without changing intended behavior. #99682 Related #99674 . Thanks @romneyda.

> Removed redundant list-cleanup layers across channels, agents, the CLI, and diagnostics to make maintenance clearer. #99702 Related #99697 . Thanks @romneyda.

> Unified cancellation handling so stops and timeouts remain consistent across agent, Gateway, reply, media, and process workflows. #99753 Thanks @romneyda.

> Consolidated repeated internal task handoffs across setup, approvals, agent turns, and plugins without changing behavior. #99755 Thanks @romneyda.

> Unified numeric limit handling across agent workflows while preserving their existing allowed ranges. #99786 Thanks @romneyda.

> Extended consistent provider and model reference handling across media, speech, agent policy, and diagnostic workflows. #99790 Thanks @romneyda.

> Tightened internal agent code boundaries so maintainers have fewer accidental interfaces to preserve. #100909 Thanks @vincentkoc.

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
## Nearby in Agent Mode

- Earlier: 2026-07-13 · Google Antigravity · [[Changes/Google Antigravity/2026-07-13-2-agent-mode-changes-in-hub-v2-3-0-queued-messages-plain|2 Agent Mode changes in HUB v2.3.0 — Queued messages, plain…]]
- Later: 2026-07-14 · Claude Code · [[Changes/Claude Code/2026-07-14-4-agent-mode-changes-in-v2-1-208|4 Agent Mode changes in v2.1.208]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-07-13-50a48c&body=Card%3A%20Changes%2FOpenClaw%2F2026-07-13-132-agent-mode-changes-in-v2026-7-1.md%0ACard%20ID%3A%20openclaw-2026-07-13-50a48c%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.7.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->