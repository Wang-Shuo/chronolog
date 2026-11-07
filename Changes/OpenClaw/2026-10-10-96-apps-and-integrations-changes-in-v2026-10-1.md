---
card_id: openclaw-2026-10-10-0b2260
date: '2026-10-10'
description: 'OpenClaw · 2026-10-10 · Apps and Integrations: 96 changes in v2026.10.1
  — OpenClaw v2026.10.1 helps your agent find a relevant installed skill when a task…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2857
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 971cd037ea261caf81c524c38ffdf5b5685d20a62cc91bd5d6b24728f5f58268
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-10-10-0b2260
  comparison: ''
  date: '2026-10-10'
  description: 'OpenClaw — v2026.10.1: 96 Apps and Integrations changes'
  evidence:
  - quote: OpenClaw v2026.10.1 helps your agent find a relevant installed skill when
      a task needs it, without putting the whole skill library in the prompt. You
      can then work with compatible, opt-in MCP Apps beside chat, using supported
      forms and workspace files. To keep your setup recoverable, full backups can
      now live on external storage or Cloudflare R2 and restore into a fresh staging
      directory.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: With MCP Apps enabled and a compatible server configured, you can work
      in an app beside chat and attach selected content to your next message. Supported
      apps can also view or edit workspace files and offer richer forms with previews
      and resource choices.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Open apps directly, use their settings, attach removable content, and
      view or edit advertised workspace-file formats. #161747 . Thanks @steipete .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'MCP session controls follow current metadata, withdrawn previews disappear,
      and access revoked during preparation returns an authorization error. #163548
      . Thanks @steipete .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Transparent, theme-aware MCP Apps blend with the dashboard in light and
      dark modes; apps with their own opaque background retain it. #161494 . Thanks
      @steipete .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Dashboard, widget and MCP App reads follow previously accepted board writes,
      avoiding older widget revisions. A changed destination rejects the read instead
      of serving from its former location. #164448 . Thanks @steipete .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: MCP Apps fill their dashboard panel again in fullscreen, resized and split
      layouts instead of shrinking above a blank gap. 11515ce . Thanks @steipete .
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: The optional Workboard plugin lets you organize conversations on Sessions
      boards using run status, rules and persistent pins. Personal filters focus on
      conversations involving you or a chosen person without changing anyone else's
      view. Nested sidebar links make boards easier to reach, and the Board agent
      can help reshape a board when asked.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Bun now reports useful Codex startup errors and lets valid messages follow
      a malformed one. Native dependency repair keeps existing packages and warns
      when it cannot repair them. Large computer-control screenshots and piped MCP
      responses avoid the affected output failures, and affected macOS builds leave
      intended background processes running after command output ends.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Supported Discord and Slack browser plugins add a header link back to the
      conversation where a session began. Slack and GovSlack open the channel or DM.
      Older sessions gain the link after a later inbound event, and it appears only
      when a valid source link and supporting plugin are available.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Move and verify callbacks before removing old listener settings, retaining
      the marker in the configuration migration guide . Old Teams and Nextcloud listeners
      can remain accessible on all network interfaces until migrated. Upgrade core
      to at least 2026.9.9 before manually replacing these standalone plugins. If
      Nextcloud Talk still uses the retired private-network setting, follow the guide's
      2026.9.5 intermediate upgrade first.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Scheduled Workshop skill reviews can use compatible Codex runtimes to read
      and edit within the assigned Workshop directory. They run through restricted
      host tools, without shell access, external MCP tools or delegation, and refuse
      to start if those restrictions cannot be verified.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: New-format sessions keep their remote ID when credentials change, although
      hosted access still requires the creating key. Older authFingerprint bindings,
      including those from 9.7, can no longer continue, reset or delete, and have
      no automatic migration. Model, environment or effective HTTP MCP changes still
      require reset. Check previous tool results before repeating an interrupted operation.
      See the Agents API access guide .
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Whole-conversation forks of compatible Claude CLI sessions can preserve
      the model's context in an independent child. Per-message forks, missing checkpoints
      and changed accounts or environments start fresh native sessions. You can also
      find and read existing sdk-ts transcripts through the Gateway, although the
      native Mac node reader does not gain that support.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Ordinary local Claude CLI chats using bundled Gateway MCP can return control
      while long shell work continues under configured permissions and deadlines.
      Background answers retain parent context, permitted tools remain available for
      verified local child results, and Gateway tools work on later CLI turns. Conversations
      blocked by a completed consult or handoff can resume without resetting; recovered
      runs preserve their provider connection, and cancelled remote turns avoid new
      approval prompts. See CLI backends and child tool policy .
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Temporary context stops consuming model input on your next message but
      remains in the saved transcript. Failed, rolled-back plugin registrations also
      stop blocking otherwise healthy agent turns. See Anthropic retained context
      and the context guide .
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Default scheduled agent jobs can use their owning conversation's current
      tools, including eligible older jobs held back by outdated tool lists. These
      jobs now follow the conversation's current permissions, losing restrictions
      tied only to the original sender or its plugin hooks. Explicit tool limits,
      scripts, condition-trigger jobs and app- or runtime-bound jobs keep their restrictions,
      and saved execution hosts stay pinned.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Scheduled conditions and scripts can check explicitly allowed MCP services
      and skip the payload and model call when nothing changed. Enable tools by name
      or a server-specific pattern; a bare wildcard enables none. Conditions keep
      their time and tool-call limits, and requester-scoped services remain unavailable.
      See condition watchers and payloads .
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: With the optional Lobster plugin, you can answer workflow questions in
      chat, correct rejected answers and continue from saved progress, or cancel the
      remaining steps. Keep resume tokens secret. Anyone holding one can resume the
      workflow; tokens are not tied to your OpenClaw user or session. See Lobster
      structured input .
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Self-hosted users can submit input files when their registered workspace
      provider prepares them for the executor. Native image input and automatic output-file
      transfer remain unavailable. Agents API also has its own plugin selections that
      can change without restarting the Gateway; copy supported selections from Codex
      explicitly, since this alone does not enable native apps or connectors.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Fresh Agents API sessions discover and call configured Streamable HTTP
      MCP tools with resolved credential headers. #160931 . Thanks @sjf-oa , @sjf
      .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Agents API gains an independent plugin-selection configuration block that
      needs no Gateway restart; it does not activate native apps or connectors. #161048
      . Thanks @sjf-oa , @sjf .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'The dedicated plugin guide brings Agents API setup and capabilities together,
      replacing the older runtime-fragment bookmarks. #162255 . Thanks @sjf-oa .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Loaded local, linked and community plugins can save their own managed state
      and incoming-message queues , with storage limits and trust requirements for
      privileged operations retained. Normal stops and restarts preserve plugin session
      state. Disabling or removing a plugin still deletes that state, and earlier
      losses cannot be recovered.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Plugins can adopt a reader for the end of a conversation, including after
      a reset, without accidentally reading its replacement. External plugins must
      opt into conversation access and read within the handler's lifetime. Tracked
      start and end work can also finish after the request closes.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Ordinary stop/restart preserves plugin session state and reports settled
      callback errors as named warnings. #164975 . Thanks @steipete .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Every loaded plugin can save its own managed state and process durable
      incoming-message queues without the former storage trust refusal. #165063 .
      Thanks @steipete .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Adopting session-end plugins can read an authorized bounded tail of the
      ended conversation during the handler lifetime; external plugins must opt into
      conversation access. #161451 . Thanks @ekinnee , @jalehman , @PaulClawitzki
      , @xydigitLybnnnn , @azuretek .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Plugin authors can wait for conversation history, session changes and provider
      replay metadata to be saved before using the results, with similar methods for
      workspace results, publication and Mention Inbox. Follow the persistence migration
      guide , especially for transcript rewrites that require awaiting both preparation
      and its returned commit. The documented synchronous adapters remain during the
      compatibility window.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Mention Inbox uses background storage and settles accepted records and
      dismissals on orderly shutdown; plugin authors gain awaited methods while synchronous
      methods remain with deprecation warnings. Publication callbacks must send their
      response synchronously and await dependent mutations afterward. #164291 . Thanks
      @steipete .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Plugin authors can retain a draft throttle deadline during reset and defer
      stale-message retirement through optional lifecycle arguments. #162219 . Thanks
      @steipete .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: ChannelThreadBindingsSchema exposes existing validation through the channel-config-schema
      facade for reuse by plugin authors. 1a158881cd01 . Thanks @steipete .
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Client developers can show available README text, release notes and trust
      information for a selected ClawHub plugin or skill release before a user decides
      to install it. Missing information stays explicit, including incomplete capability
      summaries and unknown download availability; inspecting a listing does not authorize
      installation.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Client developers can retrieve selected ClawHub plugin and skill release
      details before installation, with missing metadata and incomplete remote capability
      summaries explicit. #163460 . Thanks @jacobtomlinson .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Agents API users can allow, disable or restrict network access for an OpenAI-hosted
      session. Restricted access matches exact hostnames, so include needed subdomains
      and redirect destinations. Reset the session whenever you add, change or remove
      a policy. Hosted stdio MCP requires enabled networking; service-origin remote
      MCP connections use a separate path. See hosted network controls .
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Agents API hosted VMs can use enabled, disabled or restricted networking
      with 1–100 exact hosts. Subdomains and redirects need their own entries, and
      adding, changing or removing the policy requires a session reset. Hosted stdio
      MCP requires enabled networking. See hosted network controls . #161004 . Thanks
      @sjf-oa , @sjf .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Prometheus and OpenTelemetry now identify registered plugin and auxiliary
      traffic by method name. Update dashboard queries for registered traffic moving
      from other to named methods and generic traffic moving from unknown to other
      . Prometheus can still drop new series when its shared sample cap fills, with
      omissions recorded by the dropped-series counter.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Preference edits: Preference-only edits avoid an unnecessary restart when
      plugin defaults arrive between loading and saving.'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Stopping the Gateway waits for accepted database maintenance and worker
      cleanup. A plugin cleanup timeout no longer turns a successful message command
      into a failure, though cleanup can remain pending. A final native-worker cleanup
      failure leaves that source unavailable until the process restarts. Restarts
      continue after duplicate configuration notifications, and crash-loop pauses
      keep interrupted-turn retries for replay after a full stable window. Running
      or queued work survives an access-policy change only while its original access
      remains valid. See restart recovery and message commands .
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Background-command and restart replies return to the eligible web conversation
      they belong to. Affected channels keep answering after wake-from-sleep maintenance,
      and a channel with unchanged settings can finish a prepared reply after an unrelated
      plugin reload. Successful background media requests no longer show a false missing-reply
      notice while waiting for the result.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Slack fallback progress cards show quieter narration by default; the existing
      option still enables detailed tool activity. Slack and Matrix previews wait
      before displaying fragments that might be a silent-reply instruction. Matrix
      preserves unrelated contacts by stopping contact-map writes when account reads
      fail; retry the repair after reads recover.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Long conversations can finish a summary that needs several stages when
      a plugin delegates to built-in compaction. Each request remains bounded; plugin
      authors must pass the original host cancellation signal for this fix to apply.
      Automatic summaries use your reasoning setting and current conversation size,
      keep requested AGENTS.md excerpts separate from unrelated material, and distinguish
      completed checks from work still needed. See the context-engine guide , compaction
      settings , compaction policy and overview .
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Skill instructions give clearer routes for finding integrations: general
      requests use existing ClawHub plugins, while explicit skill requests use skills;
      installing either still needs separate authorization. Feishu Wiki instructions
      use supported browsing or a known wiki token. Callers must adopt the corrected
      tmux completion-marker example to distinguish fresh output from echoed commands
      and older results.'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: A solo Codex conversation can delegate even when native admission hooks
      are unavailable; another signed-in person's message is queued as a follow-up.
      Conversations affected by the earlier source-main regression need a new conversation
      to recover. A stale readiness check gets one refresh before a child follow-up
      is refused.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: OpenClaw keeps handling events while task edits, results and scratch notes
      wait to save, preserving newer changes, recorded recipients and cancellation
      checks. Scheduled-session cleanup does less work in large stores, and background
      runs can reuse matching prepared plugins without changing their workspace or
      file-access boundaries. Removing a running job requests cancellation; the acknowledgment
      does not mean work has stopped or undo completed effects.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Plugin upgrades. Keep affected plugins working by updating them before
      the OpenClaw host; the SDK migration guide explains retired imports and replacements.
      Legacy extension-only installs need an explicit supported installation or 2026.9.7
      Doctor repair before upgrading. Updated Zoom, Teams, ClickClack, Google Chat,
      IRC, Slack, SMS and Zalo packages using the refactored helpers require host
      2026.9.8 or newer. Historical conversation bindings without recognized plugin
      ownership can refuse reassignment, with recovery still unresolved.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Loading and reloads. You can read model lists, sign-in status and session
      metadata while a plugin reload waits for work to finish. If that wait fails,
      retry openclaw plugins reload <id> --wait or revert pending settings; a model
      call blocking its own reload fails promptly and can be retried afterward. Loading
      avoids repeated native-plugin scans and supports managed npm layouts across
      filesystems and symlinks. After editing bundled TypeScript, restart OpenClaw;
      compiled installations also need a rebuild first.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Tool discovery and input. Tool Search finds tools with trusted arguments
      nested in combined schemas. Repeated tool or skill searches reuse unchanged
      indexes. Inputs keep referenced types and defaults and accept custom strings
      alongside presets; overly nested MCP results explain the need for flatter output.
      Meeting captions and Logbook skip completed history, though their first index
      build can take time and temporary disk space.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: External plugins avoid unnecessary reloads during model-catalog adoption.
      Installed-plugin startup repeats fewer file reads, Windows uses a bounded copy
      path for eligible small files, and valid plugins can load through ancestor directory
      junctions. Changed or incomplete captures remain rejected.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Whole-store and transcript-file SDK bridges are removed; affected plugins
      must adopt the supported focused APIs before the host update. #162220 . Thanks
      @steipete .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'The command-auth , discord and telegram-account SDK facades are retired;
      use the supported channel contracts and injected runtime. #163366 . Thanks @steipete
      .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Provider plugins replace eight retired stream/replay constants with the
      existing family constructors; the compatibility guide lists replacements and
      retained aliases. #163591 . Thanks @steipete .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'The refactored Zoom and Teams plugin packages require host 2026.9.8 or
      newer. #161628 . Thanks @steipete .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Updated ClickClack, Google Chat, IRC, Slack, SMS and Zalo packages using
      the shared secret helper require host 2026.9.8 or newer. #162827 . Thanks @steipete
      .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Bundled source plugins share loaded host code, so source edits take effect
      after restarting the Gateway. #163639 . Thanks @steipete .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Supported older Codex harness plugins retain sourceVisibleReplies ; visibleReplies
      is the canonical field and explicit message configuration takes precedence.
      #163497 , #163786 . Thanks @steipete .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Typed approval hooks must omit the retired requireApproval.timeoutBehavior
      field; timeoutMs and timeoutReason remain supported. #163333 . Thanks @steipete
      .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Installed QA runner plugins using legacy-only registration must move their
      runner registration to qa-runner-api.ts or .js . #164058 . Thanks @steipete
      .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'A plugin model call that would prevent its own reload fails promptly with
      instructions to retry afterward. #162484 . Thanks @jalehman .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Ongoing sessions can use current tool-policy handlers after old plugin
      generations retire. #164451 . Thanks @RomneyDa .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Managed npm plugins with native dependencies load across filesystem boundaries
      and supported symlink layouts. For a wrong-host installation, run doctor --fix
      on the intended host, then reload. #163876 . Thanks @steipete , @wlassalle724
      , @EmisvaldoSilva .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Bun plugins resolve valid wildcard package-import aliases with filename
      suffixes. #163232 . Thanks @steipete .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Deferred Bun SDK imports retain the source or built host selected by their
      plugin generation. #163360 . Thanks @steipete .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Bun retains its intended plugin loader when it exposes Node-compatible
      module hooks. #163539 . Thanks @steipete .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Shared plugin caches follow the selected state location, and failed setup
      preserves its diagnostic error while attempting cleanup. #161351 . Thanks @steipete
      .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Plugins forwarding provider streams through multiple layers avoid inspecting
      the same event repeatedly. #161696 . Thanks @steipete .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Stream and result handoff removes repeated boundary wrapping; plugin authors
      retain responsibility for leaving delivered payloads unchanged. #163818 . Thanks
      @steipete .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Native hooks retry brief database locks within the existing deadline before
      declaring their authenticated bridge unavailable. #161822 . Thanks @steipete
      .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Remote-exec bootstrap includes required published .setup runtime chunks
      for affected external plugins such as Codex. #165669 . Thanks @LiuwqGit , @JakeBotFleet
      .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: CLI help and command discovery release executable-owned plugin metadata
      resources and retain reported cleanup failures. bfdb432570ac . Thanks @steipete
      , @vincentkoc .
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Saved Control UI plugin descriptors remain readable after retirement without
      invoking the retired plugin. dc8393473d09 . Thanks @steipete .
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Catalog-created resource controls keep their factory's plugin context,
      including the repaired speech-stream release callback. a388b8f1a736 . Thanks
      @steipete .
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Installed-plugin ownership and conflict checks reuse resolved paths within
      each check. 6fc676c5b563 . Thanks @RomneyDa .
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Claw cleanup and MCP setup-status saving run in the background; cleanup
      waits until its ownership record is saved. #163112 . Thanks @steipete .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Custom legacy PCM Talk integrations avoid starting an obsolete reply when
      cancellation arrives after its replacement. #163732 . Thanks @steipete .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Global MCP cleanup continues reporting an earlier unconfirmed disposal
      instead of losing that uncertainty on a later empty cleanup. a6089edc5cd9 .
      Thanks @steipete .
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Affected plugin and MCP tool schemas accept valid custom strings alongside
      named presets. #159755 . Thanks @Shenrui-Ma .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Overly nested MCP results fail with flatter-output guidance, including
      consistent Code Mode output errors. #160825 . Thanks @wangmiao0668000666 , @hpyhandsome
      .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Encoded plugin schema references retain separators and defaults; use ~1
      for a literal slash in a key and ~0 for a tilde. #161954 . Thanks @boeingchoco
      , @obviyus .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Native plugin preparation reuses successful checks on unchanged captured
      files in affected hardlink installations. #162254 . Thanks @steipete , @WG-Mojo
      , @eddiekk , @NickM83 .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Bun-backed npm plugin operations use bundled npm 12.1.0 while preserving
      explicit Git and remote-tarball source restrictions. #162581 . Thanks @vincentkoc
      .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Running Bun plugins retain selected dependency contents reached through
      supported package aliases after source edits. #164223 . Thanks @steipete .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'The Lobster plugin''s runtime 2026.9.14 update corrects structured LLM
      task request/result translation. #162558 . Thanks @vincentkoc .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Doctor repairs old MCP type aliases, and an explicit canonical transport
      wins over a conflicting legacy type. #162256 . Thanks @steipete .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: MCP listings preserve opaque pagination tokens, and supported models sent
      directly to ollama.com receive maximum thinking without changing local-relay
      compatibility. db0c17463643 .
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Malformed Claude Workshop replies reject the waiting MCP request promptly
      instead of leaving it until the SDK timeout. #158916 . Thanks @steipete , @VACInc
      .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Adopting a downloaded model catalog reuses unchanged external plugins
      instead of reloading them and making the Gateway unresponsive shortly after
      startup. Initial plugin loading and explicit reloads still do their own work.
      #167544 . Thanks @cmrstudio56 , @obviyus .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Installed-plugin startup repeats fewer ordinary-file reads. On Windows,
      eligible small ordinary plugin files also use the existing bounded copy path;
      large and native files retain their guarded path. Changed or incomplete plugin
      captures remain rejected. #168017 , #168256 . Thanks @gollymashed , @krumch
      , @RomneyDa , @RuiCatalao7 , @steipete , @utesara .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Windows can load valid installed plugins when an ancestor Node directory
      redirects through a junction. Entries outside the verified package root remain
      rejected. 052baa8c . Thanks @steipete .
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Doctor uses an updated plugin's own repair callbacks and settings rules.
      Preparing large plugins can use fewer disk writes on supported filesystems while
      later edits stay independent. Reload verifies copied content and asks you to
      retry if files change during preparation. 7039983b , dd51d9cc . Thanks @jjjhenriksen
      , @RomneyDa .
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Plugin state operations continue through harmless concurrent conversation
      edits, while still refusing work after the active session writer changes. 01c06759
      . Thanks @RomneyDa .
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Valid Gateway startup avoids unnecessary diagnostic-module loading for
      affected external plugins. Invalid configuration and explicit Doctor still receive
      the plugin's repair checks. See running the Gateway . a84bd1a5 . Thanks @RomneyDa
      .
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Work on a node respects current workspace and patch-tool restrictions .
      Eligible native apps on the same machine avoid repeated initial approvals under
      existing local policy, and reused writable SSH sandboxes receive new uploads.
      Strict filesystem mode can refuse recursive cleanup on Windows or Linux without
      openat2 , leaving directories behind; use a platform supporting the required
      protection. Migrate old filesystem mode variable names to their native-mode
      equivalents.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Tool-heavy conversations retain fewer duplicate results and discarded strings;
      reusable readers release completed requests. Plugin and SDK callers must treat
      transcript payloads as immutable as soon as they submit them, even while an
      asynchronous save is pending. Create new values for later updates. Hooks receive
      saved rewritten activity and omit suppressed entries. See the SDK runtime guide
      .
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Network updates fix compressed responses and redirects while preserving
      Slack proxy compatibility. Replaced skill folders can be watched again, with
      polling fallback available. Doctor retains loaded native plugin files after
      cleanup.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Finished chats, old display rows, disconnected tool subscriptions and short
      previews release unneeded data without interrupting accepted work. Non-Windows
      Bash and Zsh caches retain recent shell snapshots. Abandoned HTTP responses
      can release buffers when garbage collection runs; SDK callers should still finish
      or cancel response bodies for prompt cleanup.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 96-apps-and-integrations-changes-in-v2026-10-1
  source_release: openclaw-2026-10-10-v2026-10-1-d64e4e93
  source_type: openclaw_changelog
  theme: apps-integrations
  title: 96 Apps and Integrations changes in v2026.10.1
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-10-09-managed-plugin-setup-retries-hourly-or-after-policy-changes-instead-of-on-every|Managed
  plugin setup retries hourly or after policy changes instead of on every…]]'
- '[[Changes/Lovable/2026-10-09-generate-a-secret-that-another-app-also-needs|Generate
  a secret that another app also needs]]'
- '[[Changes/Open WebUI/2026-10-10-7-apps-and-integrations-changes-in-v0-12-0|7 Apps
  and Integrations changes in v0.12.0]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-10-10-v2026-10-1-d64e4e93|openclaw-2026-10-10-v2026-10-1-d64e4e93]]'
source_type: openclaw_changelog
theme: apps-integrations
title: 96 Apps and Integrations changes in v2026.10.1
type: change
---

<!-- chronolog:begin region="header" -->
# 96 Apps and Integrations changes in v2026.10.1

**OpenClaw** · 2026-10-10 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.10.1) · from [[Releases/OpenClaw/openclaw-2026-10-10-v2026-10-1-d64e4e93|v2026.10.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> OpenClaw v2026.10.1 helps your agent find a relevant installed skill when a task needs it, without putting the whole skill library in the prompt. You can then work with compatible, opt-in MCP Apps beside chat, using supported forms and workspace files. To keep your setup recoverable, full backups can now live on external storage or Cloudflare R2 and restore into a fresh staging directory.

> With MCP Apps enabled and a compatible server configured, you can work in an app beside chat and attach selected content to your next message. Supported apps can also view or edit workspace files and offer richer forms with previews and resource choices.

> Open apps directly, use their settings, attach removable content, and view or edit advertised workspace-file formats. #161747 . Thanks @steipete .

> MCP session controls follow current metadata, withdrawn previews disappear, and access revoked during preparation returns an authorization error. #163548 . Thanks @steipete .

> Transparent, theme-aware MCP Apps blend with the dashboard in light and dark modes; apps with their own opaque background retain it. #161494 . Thanks @steipete .

> Dashboard, widget and MCP App reads follow previously accepted board writes, avoiding older widget revisions. A changed destination rejects the read instead of serving from its former location. #164448 . Thanks @steipete .

> MCP Apps fill their dashboard panel again in fullscreen, resized and split layouts instead of shrinking above a blank gap. 11515ce . Thanks @steipete .

> The optional Workboard plugin lets you organize conversations on Sessions boards using run status, rules and persistent pins. Personal filters focus on conversations involving you or a chosen person without changing anyone else's view. Nested sidebar links make boards easier to reach, and the Board agent can help reshape a board when asked.

> Bun now reports useful Codex startup errors and lets valid messages follow a malformed one. Native dependency repair keeps existing packages and warns when it cannot repair them. Large computer-control screenshots and piped MCP responses avoid the affected output failures, and affected macOS builds leave intended background processes running after command output ends.

> Supported Discord and Slack browser plugins add a header link back to the conversation where a session began. Slack and GovSlack open the channel or DM. Older sessions gain the link after a later inbound event, and it appears only when a valid source link and supporting plugin are available.

> Move and verify callbacks before removing old listener settings, retaining the marker in the configuration migration guide . Old Teams and Nextcloud listeners can remain accessible on all network interfaces until migrated. Upgrade core to at least 2026.9.9 before manually replacing these standalone plugins. If Nextcloud Talk still uses the retired private-network setting, follow the guide's 2026.9.5 intermediate upgrade first.

> Scheduled Workshop skill reviews can use compatible Codex runtimes to read and edit within the assigned Workshop directory. They run through restricted host tools, without shell access, external MCP tools or delegation, and refuse to start if those restrictions cannot be verified.

> New-format sessions keep their remote ID when credentials change, although hosted access still requires the creating key. Older authFingerprint bindings, including those from 9.7, can no longer continue, reset or delete, and have no automatic migration. Model, environment or effective HTTP MCP changes still require reset. Check previous tool results before repeating an interrupted operation. See the Agents API access guide .

> Whole-conversation forks of compatible Claude CLI sessions can preserve the model's context in an independent child. Per-message forks, missing checkpoints and changed accounts or environments start fresh native sessions. You can also find and read existing sdk-ts transcripts through the Gateway, although the native Mac node reader does not gain that support.

> Ordinary local Claude CLI chats using bundled Gateway MCP can return control while long shell work continues under configured permissions and deadlines. Background answers retain parent context, permitted tools remain available for verified local child results, and Gateway tools work on later CLI turns. Conversations blocked by a completed consult or handoff can resume without resetting; recovered runs preserve their provider connection, and cancelled remote turns avoid new approval prompts. See CLI backends and child tool policy .

> Temporary context stops consuming model input on your next message but remains in the saved transcript. Failed, rolled-back plugin registrations also stop blocking otherwise healthy agent turns. See Anthropic retained context and the context guide .

> Default scheduled agent jobs can use their owning conversation's current tools, including eligible older jobs held back by outdated tool lists. These jobs now follow the conversation's current permissions, losing restrictions tied only to the original sender or its plugin hooks. Explicit tool limits, scripts, condition-trigger jobs and app- or runtime-bound jobs keep their restrictions, and saved execution hosts stay pinned.

> Scheduled conditions and scripts can check explicitly allowed MCP services and skip the payload and model call when nothing changed. Enable tools by name or a server-specific pattern; a bare wildcard enables none. Conditions keep their time and tool-call limits, and requester-scoped services remain unavailable. See condition watchers and payloads .

> With the optional Lobster plugin, you can answer workflow questions in chat, correct rejected answers and continue from saved progress, or cancel the remaining steps. Keep resume tokens secret. Anyone holding one can resume the workflow; tokens are not tied to your OpenClaw user or session. See Lobster structured input .

> Self-hosted users can submit input files when their registered workspace provider prepares them for the executor. Native image input and automatic output-file transfer remain unavailable. Agents API also has its own plugin selections that can change without restarting the Gateway; copy supported selections from Codex explicitly, since this alone does not enable native apps or connectors.

> Fresh Agents API sessions discover and call configured Streamable HTTP MCP tools with resolved credential headers. #160931 . Thanks @sjf-oa , @sjf .

> Agents API gains an independent plugin-selection configuration block that needs no Gateway restart; it does not activate native apps or connectors. #161048 . Thanks @sjf-oa , @sjf .

> The dedicated plugin guide brings Agents API setup and capabilities together, replacing the older runtime-fragment bookmarks. #162255 . Thanks @sjf-oa .

> Loaded local, linked and community plugins can save their own managed state and incoming-message queues , with storage limits and trust requirements for privileged operations retained. Normal stops and restarts preserve plugin session state. Disabling or removing a plugin still deletes that state, and earlier losses cannot be recovered.

> Plugins can adopt a reader for the end of a conversation, including after a reset, without accidentally reading its replacement. External plugins must opt into conversation access and read within the handler's lifetime. Tracked start and end work can also finish after the request closes.

> Ordinary stop/restart preserves plugin session state and reports settled callback errors as named warnings. #164975 . Thanks @steipete .

> Every loaded plugin can save its own managed state and process durable incoming-message queues without the former storage trust refusal. #165063 . Thanks @steipete .

> Adopting session-end plugins can read an authorized bounded tail of the ended conversation during the handler lifetime; external plugins must opt into conversation access. #161451 . Thanks @ekinnee , @jalehman , @PaulClawitzki , @xydigitLybnnnn , @azuretek .

> Plugin authors can wait for conversation history, session changes and provider replay metadata to be saved before using the results, with similar methods for workspace results, publication and Mention Inbox. Follow the persistence migration guide , especially for transcript rewrites that require awaiting both preparation and its returned commit. The documented synchronous adapters remain during the compatibility window.

> Mention Inbox uses background storage and settles accepted records and dismissals on orderly shutdown; plugin authors gain awaited methods while synchronous methods remain with deprecation warnings. Publication callbacks must send their response synchronously and await dependent mutations afterward. #164291 . Thanks @steipete .

> Plugin authors can retain a draft throttle deadline during reset and defer stale-message retirement through optional lifecycle arguments. #162219 . Thanks @steipete .

> ChannelThreadBindingsSchema exposes existing validation through the channel-config-schema facade for reuse by plugin authors. 1a158881cd01 . Thanks @steipete .

> Client developers can show available README text, release notes and trust information for a selected ClawHub plugin or skill release before a user decides to install it. Missing information stays explicit, including incomplete capability summaries and unknown download availability; inspecting a listing does not authorize installation.

> Client developers can retrieve selected ClawHub plugin and skill release details before installation, with missing metadata and incomplete remote capability summaries explicit. #163460 . Thanks @jacobtomlinson .

> Agents API users can allow, disable or restrict network access for an OpenAI-hosted session. Restricted access matches exact hostnames, so include needed subdomains and redirect destinations. Reset the session whenever you add, change or remove a policy. Hosted stdio MCP requires enabled networking; service-origin remote MCP connections use a separate path. See hosted network controls .

> Agents API hosted VMs can use enabled, disabled or restricted networking with 1–100 exact hosts. Subdomains and redirects need their own entries, and adding, changing or removing the policy requires a session reset. Hosted stdio MCP requires enabled networking. See hosted network controls . #161004 . Thanks @sjf-oa , @sjf .

> Prometheus and OpenTelemetry now identify registered plugin and auxiliary traffic by method name. Update dashboard queries for registered traffic moving from other to named methods and generic traffic moving from unknown to other . Prometheus can still drop new series when its shared sample cap fills, with omissions recorded by the dropped-series counter.

> Preference edits: Preference-only edits avoid an unnecessary restart when plugin defaults arrive between loading and saving.

> Stopping the Gateway waits for accepted database maintenance and worker cleanup. A plugin cleanup timeout no longer turns a successful message command into a failure, though cleanup can remain pending. A final native-worker cleanup failure leaves that source unavailable until the process restarts. Restarts continue after duplicate configuration notifications, and crash-loop pauses keep interrupted-turn retries for replay after a full stable window. Running or queued work survives an access-policy change only while its original access remains valid. See restart recovery and message commands .

> Background-command and restart replies return to the eligible web conversation they belong to. Affected channels keep answering after wake-from-sleep maintenance, and a channel with unchanged settings can finish a prepared reply after an unrelated plugin reload. Successful background media requests no longer show a false missing-reply notice while waiting for the result.

> Slack fallback progress cards show quieter narration by default; the existing option still enables detailed tool activity. Slack and Matrix previews wait before displaying fragments that might be a silent-reply instruction. Matrix preserves unrelated contacts by stopping contact-map writes when account reads fail; retry the repair after reads recover.

> Long conversations can finish a summary that needs several stages when a plugin delegates to built-in compaction. Each request remains bounded; plugin authors must pass the original host cancellation signal for this fix to apply. Automatic summaries use your reasoning setting and current conversation size, keep requested AGENTS.md excerpts separate from unrelated material, and distinguish completed checks from work still needed. See the context-engine guide , compaction settings , compaction policy and overview .

> Skill instructions give clearer routes for finding integrations: general requests use existing ClawHub plugins, while explicit skill requests use skills; installing either still needs separate authorization. Feishu Wiki instructions use supported browsing or a known wiki token. Callers must adopt the corrected tmux completion-marker example to distinguish fresh output from echoed commands and older results.

> A solo Codex conversation can delegate even when native admission hooks are unavailable; another signed-in person's message is queued as a follow-up. Conversations affected by the earlier source-main regression need a new conversation to recover. A stale readiness check gets one refresh before a child follow-up is refused.

> OpenClaw keeps handling events while task edits, results and scratch notes wait to save, preserving newer changes, recorded recipients and cancellation checks. Scheduled-session cleanup does less work in large stores, and background runs can reuse matching prepared plugins without changing their workspace or file-access boundaries. Removing a running job requests cancellation; the acknowledgment does not mean work has stopped or undo completed effects.

> Plugin upgrades. Keep affected plugins working by updating them before the OpenClaw host; the SDK migration guide explains retired imports and replacements. Legacy extension-only installs need an explicit supported installation or 2026.9.7 Doctor repair before upgrading. Updated Zoom, Teams, ClickClack, Google Chat, IRC, Slack, SMS and Zalo packages using the refactored helpers require host 2026.9.8 or newer. Historical conversation bindings without recognized plugin ownership can refuse reassignment, with recovery still unresolved.

> Loading and reloads. You can read model lists, sign-in status and session metadata while a plugin reload waits for work to finish. If that wait fails, retry openclaw plugins reload \<id> --wait or revert pending settings; a model call blocking its own reload fails promptly and can be retried afterward. Loading avoids repeated native-plugin scans and supports managed npm layouts across filesystems and symlinks. After editing bundled TypeScript, restart OpenClaw; compiled installations also need a rebuild first.

> Tool discovery and input. Tool Search finds tools with trusted arguments nested in combined schemas. Repeated tool or skill searches reuse unchanged indexes. Inputs keep referenced types and defaults and accept custom strings alongside presets; overly nested MCP results explain the need for flatter output. Meeting captions and Logbook skip completed history, though their first index build can take time and temporary disk space.

> External plugins avoid unnecessary reloads during model-catalog adoption. Installed-plugin startup repeats fewer file reads, Windows uses a bounded copy path for eligible small files, and valid plugins can load through ancestor directory junctions. Changed or incomplete captures remain rejected.

> Whole-store and transcript-file SDK bridges are removed; affected plugins must adopt the supported focused APIs before the host update. #162220 . Thanks @steipete .

> The command-auth , discord and telegram-account SDK facades are retired; use the supported channel contracts and injected runtime. #163366 . Thanks @steipete .

> Provider plugins replace eight retired stream/replay constants with the existing family constructors; the compatibility guide lists replacements and retained aliases. #163591 . Thanks @steipete .

> The refactored Zoom and Teams plugin packages require host 2026.9.8 or newer. #161628 . Thanks @steipete .

> Updated ClickClack, Google Chat, IRC, Slack, SMS and Zalo packages using the shared secret helper require host 2026.9.8 or newer. #162827 . Thanks @steipete .

> Bundled source plugins share loaded host code, so source edits take effect after restarting the Gateway. #163639 . Thanks @steipete .

> Supported older Codex harness plugins retain sourceVisibleReplies ; visibleReplies is the canonical field and explicit message configuration takes precedence. #163497 , #163786 . Thanks @steipete .

> Typed approval hooks must omit the retired requireApproval.timeoutBehavior field; timeoutMs and timeoutReason remain supported. #163333 . Thanks @steipete .

> Installed QA runner plugins using legacy-only registration must move their runner registration to qa-runner-api.ts or .js . #164058 . Thanks @steipete .

> A plugin model call that would prevent its own reload fails promptly with instructions to retry afterward. #162484 . Thanks @jalehman .

> Ongoing sessions can use current tool-policy handlers after old plugin generations retire. #164451 . Thanks @RomneyDa .

> Managed npm plugins with native dependencies load across filesystem boundaries and supported symlink layouts. For a wrong-host installation, run doctor --fix on the intended host, then reload. #163876 . Thanks @steipete , @wlassalle724 , @EmisvaldoSilva .

> Bun plugins resolve valid wildcard package-import aliases with filename suffixes. #163232 . Thanks @steipete .

> Deferred Bun SDK imports retain the source or built host selected by their plugin generation. #163360 . Thanks @steipete .

> Bun retains its intended plugin loader when it exposes Node-compatible module hooks. #163539 . Thanks @steipete .

> Shared plugin caches follow the selected state location, and failed setup preserves its diagnostic error while attempting cleanup. #161351 . Thanks @steipete .

> Plugins forwarding provider streams through multiple layers avoid inspecting the same event repeatedly. #161696 . Thanks @steipete .

> Stream and result handoff removes repeated boundary wrapping; plugin authors retain responsibility for leaving delivered payloads unchanged. #163818 . Thanks @steipete .

> Native hooks retry brief database locks within the existing deadline before declaring their authenticated bridge unavailable. #161822 . Thanks @steipete .

> Remote-exec bootstrap includes required published .setup runtime chunks for affected external plugins such as Codex. #165669 . Thanks @LiuwqGit , @JakeBotFleet .

> CLI help and command discovery release executable-owned plugin metadata resources and retain reported cleanup failures. bfdb432570ac . Thanks @steipete , @vincentkoc .

> Saved Control UI plugin descriptors remain readable after retirement without invoking the retired plugin. dc8393473d09 . Thanks @steipete .

> Catalog-created resource controls keep their factory's plugin context, including the repaired speech-stream release callback. a388b8f1a736 . Thanks @steipete .

> Installed-plugin ownership and conflict checks reuse resolved paths within each check. 6fc676c5b563 . Thanks @RomneyDa .

> Claw cleanup and MCP setup-status saving run in the background; cleanup waits until its ownership record is saved. #163112 . Thanks @steipete .

> Custom legacy PCM Talk integrations avoid starting an obsolete reply when cancellation arrives after its replacement. #163732 . Thanks @steipete .

> Global MCP cleanup continues reporting an earlier unconfirmed disposal instead of losing that uncertainty on a later empty cleanup. a6089edc5cd9 . Thanks @steipete .

> Affected plugin and MCP tool schemas accept valid custom strings alongside named presets. #159755 . Thanks @Shenrui-Ma .

> Overly nested MCP results fail with flatter-output guidance, including consistent Code Mode output errors. #160825 . Thanks @wangmiao0668000666 , @hpyhandsome .

> Encoded plugin schema references retain separators and defaults; use ~1 for a literal slash in a key and ~0 for a tilde. #161954 . Thanks @boeingchoco , @obviyus .

> Native plugin preparation reuses successful checks on unchanged captured files in affected hardlink installations. #162254 . Thanks @steipete , @WG-Mojo , @eddiekk , @NickM83 .

> Bun-backed npm plugin operations use bundled npm 12.1.0 while preserving explicit Git and remote-tarball source restrictions. #162581 . Thanks @vincentkoc .

> Running Bun plugins retain selected dependency contents reached through supported package aliases after source edits. #164223 . Thanks @steipete .

> The Lobster plugin's runtime 2026.9.14 update corrects structured LLM task request/result translation. #162558 . Thanks @vincentkoc .

> Doctor repairs old MCP type aliases, and an explicit canonical transport wins over a conflicting legacy type. #162256 . Thanks @steipete .

> MCP listings preserve opaque pagination tokens, and supported models sent directly to ollama.com receive maximum thinking without changing local-relay compatibility. db0c17463643 .

> Malformed Claude Workshop replies reject the waiting MCP request promptly instead of leaving it until the SDK timeout. #158916 . Thanks @steipete , @VACInc .

> Adopting a downloaded model catalog reuses unchanged external plugins instead of reloading them and making the Gateway unresponsive shortly after startup. Initial plugin loading and explicit reloads still do their own work. #167544 . Thanks @cmrstudio56 , @obviyus .

> Installed-plugin startup repeats fewer ordinary-file reads. On Windows, eligible small ordinary plugin files also use the existing bounded copy path; large and native files retain their guarded path. Changed or incomplete plugin captures remain rejected. #168017 , #168256 . Thanks @gollymashed , @krumch , @RomneyDa , @RuiCatalao7 , @steipete , @utesara .

> Windows can load valid installed plugins when an ancestor Node directory redirects through a junction. Entries outside the verified package root remain rejected. 052baa8c . Thanks @steipete .

> Doctor uses an updated plugin's own repair callbacks and settings rules. Preparing large plugins can use fewer disk writes on supported filesystems while later edits stay independent. Reload verifies copied content and asks you to retry if files change during preparation. 7039983b , dd51d9cc . Thanks @jjjhenriksen , @RomneyDa .

> Plugin state operations continue through harmless concurrent conversation edits, while still refusing work after the active session writer changes. 01c06759 . Thanks @RomneyDa .

> Valid Gateway startup avoids unnecessary diagnostic-module loading for affected external plugins. Invalid configuration and explicit Doctor still receive the plugin's repair checks. See running the Gateway . a84bd1a5 . Thanks @RomneyDa .

> Work on a node respects current workspace and patch-tool restrictions . Eligible native apps on the same machine avoid repeated initial approvals under existing local policy, and reused writable SSH sandboxes receive new uploads. Strict filesystem mode can refuse recursive cleanup on Windows or Linux without openat2 , leaving directories behind; use a platform supporting the required protection. Migrate old filesystem mode variable names to their native-mode equivalents.

> Tool-heavy conversations retain fewer duplicate results and discarded strings; reusable readers release completed requests. Plugin and SDK callers must treat transcript payloads as immutable as soon as they submit them, even while an asynchronous save is pending. Create new values for later updates. Hooks receive saved rewritten activity and omit suppressed entries. See the SDK runtime guide .

> Network updates fix compressed responses and redirects while preserving Slack proxy compatibility. Replaced skill folders can be watched again, with polling fallback available. Doctor retains loaded native plugin files after cleanup.

> Finished chats, old display rows, disconnected tool subscriptions and short previews release unneeded data without interrupting accepted work. Non-Windows Bash and Zsh caches retain recent shell snapshots. Abandoned HTTP responses can release buffers when garbage collection runs; SDK callers should still finish or cancel response bodies for prompt cleanup.

Source: https://docs.openclaw.ai/releases/2026.10.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-10-10-2-reliability-and-performance-changes-in-v2026-10-1|2 Reliability and Performance changes in v2026.10.1]] · Reliability and Performance
- [[Changes/OpenClaw/2026-10-10-13-memory-and-personalization-changes-in-v2026-10-1|13 Memory and Personalization changes in v2026.10.1]] · Memory and Personalization
- [[Changes/OpenClaw/2026-10-10-15-mobile-and-desktop-changes-in-v2026-10-1|15 Mobile and Desktop changes in v2026.10.1]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-10-10-12-context-window-changes-in-v2026-10-1|12 Context Window changes in v2026.10.1]] · Context Window
- [[Changes/OpenClaw/2026-10-10-4-pricing-model-changes-in-v2026-10-1|4 Pricing Model changes in v2026.10.1]] · Pricing Model
- [[Changes/OpenClaw/2026-10-10-18-account-and-access-changes-in-v2026-10-1|18 Account and Access changes in v2026.10.1]] · Account and Access
- [[Changes/OpenClaw/2026-10-10-18-model-support-changes-in-v2026-10-1|18 Model Support changes in v2026.10.1]] · Model Support
- [[Changes/OpenClaw/2026-10-10-20-safety-and-privacy-changes-in-v2026-10-1|20 Safety and Privacy changes in v2026.10.1]] · Safety and Privacy
- [[Changes/OpenClaw/2026-10-10-3-search-and-browsing-changes-in-v2026-10-1|3 Search and Browsing changes in v2026.10.1]] · Search and Browsing
- [[Changes/OpenClaw/2026-10-10-plugin-authors-can-await-session-history-extension-changes-and-replay-metadata-t|Plugin authors can await session history, extension changes and replay metadata]] · Projects and Workspaces
- [[Changes/OpenClaw/2026-10-10-2-accessibility-and-localization-changes-in-v2026-10-1|2 Accessibility and Localization changes in v2026.10.1]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-10-10-image-generation-with-oauth-can-retry-using-a-supported-openai-chat-model-in-age|Image generation with OAuth can retry using a supported OpenAI chat model…]] · Image Generation
- [[Changes/OpenClaw/2026-10-10-10-editor-experience-changes-in-v2026-10-1|10 Editor Experience changes in v2026.10.1]] · Editor Experience
- [[Changes/OpenClaw/2026-10-10-2-files-and-data-changes-in-v2026-10-1|2 Files and Data changes in v2026.10.1]] · Files and Data
- [[Changes/OpenClaw/2026-10-10-8-voice-and-audio-changes-in-v2026-10-1|8 Voice and Audio changes in v2026.10.1]] · Voice and Audio
- [[Changes/OpenClaw/2026-10-10-27-agent-mode-changes-in-v2026-10-1|27 Agent Mode changes in v2026.10.1]] · Agent Mode
- [[Changes/OpenClaw/2026-10-10-12-collaboration-changes-in-v2026-10-1|12 Collaboration changes in v2026.10.1]] · Collaboration
- [[Changes/OpenClaw/2026-10-10-video-previews-new-video-previews-can-download-media-before-play|Video previews: New video previews can download media before Play]] · Multimodal Input
- [[Changes/OpenClaw/2026-10-10-11-developer-workflow-changes-in-v2026-10-1|11 Developer Workflow changes in v2026.10.1]] · Developer Workflow
- [[Changes/OpenClaw/2026-10-10-5-enterprise-and-administration-changes-in-v2026-10-1|5 Enterprise and Administration changes in v2026.10.1]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-10-10-20-interface-experience-changes-in-v2026-10-1|20 Interface Experience changes in v2026.10.1]] · Interface Experience
- [[Changes/OpenClaw/2026-10-10-10-automation-and-scheduling-changes-in-v2026-10-1|10 Automation and Scheduling changes in v2026.10.1]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-10-10-112-other-changes-in-v2026-10-1|112 other changes in v2026.10.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-10-10 · Open WebUI · [[Changes/Open WebUI/2026-10-10-7-apps-and-integrations-changes-in-v0-12-0|7 Apps and Integrations changes in v0.12.0]]
- Later: 2026-10-11 · Ollama · [[Changes/Ollama/2026-10-11-ollama-launch-claude-no-longer-shows-a-warning-about-claude-connectors-by-hoyyev|ollama launch claude no longer shows a warning about Claude connectors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-10-10-0b2260&body=Card%3A%20Changes%2FOpenClaw%2F2026-10-10-96-apps-and-integrations-changes-in-v2026-10-1.md%0ACard%20ID%3A%20openclaw-2026-10-10-0b2260%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.10.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->