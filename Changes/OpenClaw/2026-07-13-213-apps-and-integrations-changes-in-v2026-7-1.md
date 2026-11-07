---
card_id: openclaw-2026-07-13-d95cc3
date: '2026-07-13'
description: 'OpenClaw · 2026-07-13 · Apps and Integrations: 213 changes in v2026.7.1
  — Existing installations receive safeguards before their working state is changed…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2768
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a8051f8a1917c66bf0e1fd4d0e73386d7877d5a6e731391a62a8425dd6d03efc
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-07-13-d95cc3
  comparison: ''
  date: '2026-07-13'
  description: 'OpenClaw — v2026.7.1: 213 Apps and Integrations changes'
  evidence:
  - quote: Existing installations receive safeguards before their working state is
      changed. Doctor and updates refuse to replace an unreadable configuration, Doctor
      preserves model tuning while merging retired entries, and extended-stable updates
      retain the selected release channel. Container upgrades complete migrations
      and plugin repairs before reporting readiness, and unsafe runtimes are stopped
      before they can open OpenClaw state databases.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'openclaw doctor and updates now refuse to replace an unreadable openclaw.json
      , preserving existing Gateway, agent, channel, and plugin settings instead of
      breaking the installation. #96469 Thanks @obviyus, @yetval.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Container upgrades now finish required migrations and plugin repairs before
      reporting the Gateway ready, and failed repairs stop with actionable guidance
      instead of leaving a false-green service. #101881 Thanks @sallyom.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Hosted LongCat-2.0 can now be installed through the official LongCat plugin,
      configured with LONGCAT_API_KEY during onboarding, and selected as longcat/LongCat-2.0
      for multi-turn tool use. #100501 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'When Slack accepts a reply but the confirmation is lost, OpenClaw can
      verify the existing post and avoid sending a duplicate. #97480 Thanks @joeyfrasier.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Discord, Slack, WhatsApp, Apple Messages, and other supported channels
      also receive clearer command, thread, attachment, proxy, and recovery behavior.
      The Apple Messages setup and delivery paths in this group preserve the chat
      context readers expect rather than exposing the routing work underneath.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Slack operators running multiple Gateways through one Socket Mode app
      now receive a startup warning explaining why events may reach another connection
      and how to choose a safer deployment setup. #79938 Thanks @jeffvsutherland.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Slack operators can now choose off , first , all , or batched reply threading
      per channel, with automatic replies and message tools following the same effective
      choice. #82253'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Slack button and select interactions now remain in the correct assistant
      thread and show a working status there until the follow-up turn finishes. #82895
      Thanks @wukongai-cmu.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Longer Slack assistant-thread replies now show changing progress notes
      so users can tell OpenClaw is still working. #85507 Thanks @emergentash.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Slack rich-text block actions can now include emoji near the preview limit
      without producing malformed interaction text or downstream encoding failures.
      #96577 Thanks @llagy007, @weeli-009.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The first Slack reply after a daily or idle reset can reuse recent thread
      history, so the conversation does not suddenly start from scratch. #97100 Thanks
      @bek91.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Slack replies no longer expose internal tool-failure banners, reasoning
      scaffolding, or tool-call markup to users. #97367 Thanks @masatohoshino.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Slack replies now retry after a temporary session-start conflict instead
      of stopping before the expected message is delivered. #99647 Thanks @steipete-oai.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Slack buttons and menus now preserve time labels such as 9:00 and return
      the intended action value when selected. #99877 Thanks @qingminglong, @rodja.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Slack message reactions now accept common emoji or shortcode names, can
      target the current message without repeating its ID, and provide clearer member-lookup
      guidance. #100375 Thanks @gorkem2020.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Slack now uses one static acknowledgement reaction alongside its native
      assistant loading status by default, avoiding two competing progress displays
      for the same reply. #100462 Thanks @steipete-oai.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Ordinary Slack thread replies no longer download and process the opening
      message attachments again, while new or reset sessions still receive those files
      once. #100516'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Messages that fail before reaching Discord, Slack, Matrix, or another
      channel can now be replayed after connectivity returns, while uncertain post-send
      outcomes still avoid blind duplicates. #101024 Thanks @sunnyshu0925.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Channel previews, thread names, snippets, and shortened errors across browser
      and messaging integrations now preserve whole emoji and other Unicode characters.
      c16bb87 Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Signal reaction shortcuts now apply only to the intended structured exec
      or plugin approval, including forwarded monitor and chunked prompts, while ordinary
      messages that merely quote approval commands no longer gain controls; older
      delivered prompts may still require /approve once after upgrade. #96880 Thanks
      @joshavant.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Long unbroken messages now keep emoji intact when split into delivery-sized
      chunks, preventing garbled replacement characters for users and channel plugins.
      #96951 Thanks @bartok9, @ly-wang19.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Always-on group agents can now receive and answer valid unmentioned messages
      after a plugin fallback instead of silently dropping them. #99506 Related #99457
      . Thanks @lzy3538, @zqchris.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Telegram stickers and other plugin message actions now stay in the active
      forum topic or thread when sent to the matching conversation, including through
      Gateway dispatch. #80293 Thanks @artdaal.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Telegram and Discord plugin commands that send their own response can
      return { suppressReply: true } , preventing a second misleading empty-response
      warning or failure. #80928 Related #80756 . Thanks @alexuser, @unclouded77.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'With messages.ackReactionScope: "all" , ambient room messages now receive
      the configured acknowledgement reaction across Discord, Slack, and Telegram.
      #87433 Thanks @paul-phan, @scoootscooob.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Telegram inline buttons supplied by plugins now run their intended actions
      and cleanup instead of posting raw callback data into chat. #97174 Thanks @goldmar.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Slack read actions can again access intentionally allowlisted channel
      names when Slack supplies an ID and dangerouslyAllowNameMatching is enabled.
      #95313 Thanks @jontsai.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Slack message and attachment text is no longer copied into verbose or
      debug logs during inbound processing. #96312 Thanks @steipete-oai.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Slack messages and Block Kit labels now truncate without splitting emoji
      into broken replacement characters or invalid payload text. #96382 Thanks @ly-wang19.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Long Slack command and plugin approval previews now keep emoji intact
      at the length boundary, avoiding malformed approval text or payloads. #96576
      Thanks @llagy007, @weeli-009.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'OpenClaw can use a trusted override for a compatible Slack API endpoint,
      while normal workspaces continue using Slack''s public API and untrusted project
      .env files cannot redirect bearer-token requests. #97154 Thanks @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Slack slash-command choice menus now shorten long labels without splitting
      emoji at the 75-character limit. #97923 Thanks @lexes7.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Slack Socket Mode relay diagnostics now distinguish malformed WebSocket
      frames from transport failures, making channel problems easier to identify.
      #98587 Thanks @lsr911, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Slack Codex conversations now retain one final assistant reply in history
      instead of duplicating it through both the app-server transcript and delivery
      fallback. #100160 Thanks @steipete-oai.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Mattermost installations repaired after an upgrade now load and reconnect
      on Gateway restart without requiring a manual plugin-enable setting, including
      restrictive allowlist setups. #98608 Related #98564 . Thanks @jacobtomlinson,
      @shakkernerd.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Channel plugins can resume automatic recovery after a long healthy run,
      so an occasional later disconnect is not blocked by an old restart budget while
      true rapid crash loops remain capped. #101413 Thanks @clintoncodewell.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Library and integration developers can now install a version-matched package,
      create independent AI runtimes, and reuse OpenClaw''s supported model transports
      without embedding the full application. #99059'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The bundled Codex plugin can complete backend requests again after updating
      its managed app-server runtime, with no model-picker or configuration migration
      required. #106098'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Generic provider configurations for official DashScope/Qwen, Moonshot,
      Z.AI, DeepSeek, Groq, Cerebras, and Chutes endpoints now retain the compatibility
      behavior those services require even without optional plugins. #100125'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'MCP tools that expect arrays or objects can now accept those values when
      Xiaomi MiMo, Ollama, or another affected provider returns them as JSON strings,
      avoiding a pre-execution validation failure. #96922 Thanks @liuhao1024.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Context-engine plugins can now identify the exact session that continues
      after compaction while older integrations using sessionFile remain compatible.
      #101182 Thanks @jalehman.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Slack and similar channel turns with context-injecting plugins now send
      each inbound system label to the model once instead of duplicating it. #95349
      Thanks @gorkem2020, @openperf, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Local Ollama-backed CLI agent turns can now continue when the context
      engine reports an already-compacted transcript, allowing the assistant or MCP
      tool result to reach the user. #99136 Thanks @mushuiyu886, @peterskwang, @pkoserowski,
      @psedd.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'MCP stdio sessions now report stderr pipe failures as transport errors
      without taking down OpenClaw or losing available diagnostics. #99803 Thanks
      @cxbasdev, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'ACPX MCP proxies now turn closed input or output pipes into a clear proxy
      failure instead of an uncaught Node stream crash. #99852 Thanks @sunlit-deng,
      @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Sub-agents and other HTTP loopback MCP clients can again receive browser
      screenshots and valid image or embedded-resource results without schema failures.
      #100336 Thanks @tzy-17.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Lean local-model agents can now choose the familiar exec tool directly
      when policy permits it, while existing allowlists, sandboxing, approvals, and
      hooks still govern command execution. #101607 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Shortened text across CLI output, diagnostics, plugin messages, previews,
      errors, task summaries, and Zalo sends now preserves complete emoji and other
      supplementary characters. #101654 Thanks @lsr911, @maweibin, @wm0018.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Legacy Codex bindings with large tool or MCP configurations can now migrate
      without overflowing plugin-state records or copying raw configuration secrets.
      23228b6 Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Codex sessions created in beta 5 can keep their existing conversation after
      upgrade when the user MCP configuration is unchanged, without retaining its
      authorization token. 272750d Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Agent requests with several MCP servers now initialize those servers concurrently,
      shortening the wait before the model begins while isolating slow or failed servers.
      #94230 Thanks @mmyzwl, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'New Codex-backed threads now preserve configured plugin apps, can activate
      remote curated plugins, and run Guardian on the first eligible native OpenAI
      turn. #98042 Thanks @kevinslin.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Discord now presents commentary, reasoning, and tool activity in a clearer
      sequence across queued turns, while loopback MCP clients can attach to one Gateway
      session with an expiring, revocable token. 35af831 Thanks @dwc1997, @lsr911,
      @ooiuuii, @romneyda, @solodmd, @vincentkoc, @wendy-chsy, @yeager, @zenglingbiao.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Embedded terminals can now open, resize, stream output, and close consistently
      across the Gateway, Control UI, and native apps. 6601576
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Gateway startup channel warnings now use the same plugin manifests as the
      running startup process, reducing inconsistent warnings and repeated discovery.
      10ca94e Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: An agent no longer stays silent after compaction when a plugin's final-answer
      hook hangs; OpenClaw times out the hook and still delivers the response. b2baf79
      Thanks @dserious, @obviyus, @villa-feng.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Gateway MCP logs are now quieter and identify the responsible tool when
      schema problems occur, while distinct conflicts remain visible. #98821 Thanks
      @alvelda, @harjothkhara.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Malformed Gateway MCP tools/call arguments now return a clear invalid-parameters
      response before any hook or tool can process them. #99180 Thanks @vectorpeak.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'MCP attach requests without a valid session key now return the intended
      validation error instead of crashing the Gateway with a TypeError. #99488 Thanks
      @zhanglei99586.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Discord Code Mode progress no longer fills with repetitive Wait rows from
      background polling, while ordinary custom and plugin tools remain visible. #100164'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'ClawHub now checks community plugin and skill releases before download,
      blocking prohibited releases and requiring explicit acknowledgement for suspicious
      ones while leaving existing installs in place when an update is skipped. #81364
      Thanks @jesse-merhi.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Authorized non-owner chat participants can no longer inspect or change
      owner-controlled MCP server configuration through /mcp . ad5a26c Thanks @joshavant.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Codex session bindings now keep large MCP configurations and rotated Authorization
      credentials in bounded fingerprints without persisting readable bearer values.
      491e42e Thanks @100yenadmin.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Hooks and skills no longer activate from unsafe inherited configuration
      values, while ordinary configured paths and explicit defaults continue to work.
      #59694 Thanks @yonganzhang.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Codex plugin users can allow read-only app actions while requiring a fresh
      approval for every write or destructive action. #97123 Thanks @kevinslin.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Codex plugin apps now avoid approval prompts for read-only actions, preserve
      per-app write policies across recovery, and refresh their app inventory after
      upgrades. #97327 Thanks @kevinslin.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The Codex plugin now names per-action destructive approval mode ask ,
      making it clear that each write or destructive action remains available but
      requires confirmation. #98501 Related #98499 . Thanks @kevinslin.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Authenticated owners can use their already-granted shell, file, process,
      Skill Workshop, and plugin tools in WebChat without extending those permissions
      to guests or external senders. #101271 Thanks @fuller-stack-dev.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'MCP include and exclude filters with many wildcard segments now reject
      nonmatches quickly instead of stalling tool discovery for minutes. #100330 Thanks
      @lsr911.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Codex /btw side conversations now preserve an ask-mode plugin app''s requirement
      to obtain approval before destructive actions. #98812'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Installing or updating ClawHub skills, plugins, and packages on Linux
      no longer risks changing shared /tmp permissions and disrupting unrelated services.
      #101246 Thanks @ch3ch2cho2021, @yangxiansheng.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Plugin approval titles and descriptions now remain readable when emoji
      or supplementary CJK characters fall at the Gateway''s text limit. #101580 Thanks
      @wm0018.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'TUI /new now performs a real session transition with the expected lifecycle
      hooks and prevents a new session from racing an active turn. #100241 Thanks
      @caopulan.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Supported non-English native apps now translate newer app information,
      support links, and message retry, delete, and waiting-to-send states. 82f5ac1
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: The Mac About screen now links directly to the OpenClaw website, documentation,
      GitHub project, and Discord community, matching the other native apps. 6e7ef63
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Skills can be drafted from a conversation or source, reviewed, pinned,
      archived, restored, and kept out of future context when stale. Plugin management
      is clearer about discovery, installation, updates, marketplace snapshots, connected
      Codex apps, approvals, and runtime failures, while Codex supervision can give
      each new thread an explicit bounded app allowlist.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Official packages are easier to obtain through the supported Docker and
      Android paths, and plugin-backed workflows such as Google Meet and Apple Messages
      recover from more setup and migration problems. Doctor also handles damaged
      migration caches and older plugin or skill layouts without turning a recoverable
      upgrade into a dead end.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Operators can run openclaw plugins marketplace refresh to verify and save
      a hosted feed, enforce a SHA-256 match, and see whether live, saved, or bundled
      data was used. #96155 Thanks @giodl73-repo.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Updated integration runtimes keep Codex, ACP, Copilot, Telegram, and diff
      rendering aligned with compatible upstream behavior, while reconnect recovery
      no longer floods operator logs with duplicate messages. #100027'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Declared plugin tools now remain callable in subagent sessions after plugin
      registry changes, avoiding repeated plugin tool runtime missing failures and
      Gateway restarts. #82562 Thanks @luoyanglang, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Plugin metadata cache hits no longer flood diagnostics with repeated full-scan
      entries, leaving smaller timelines where real scans are easier to identify.
      #86796 Thanks @galiniliev, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Plugin loading no longer evaluates OpenClaw''s own package code twice,
      reducing startup work and avoiding duplicate module, class, singleton, or registry
      identities in one process. #88384 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'openclaw plugins inspect now shows the bundled document-extract plugin''s
      PDF extractor as an available capability instead of reporting none. #91597 Thanks
      @xydt-tanshanshan.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'openclaw plugins init can now scaffold a model-provider plugin with authentication,
      model setup, tests, packaging, validation, and ClawHub publishing structure.
      #94352 Thanks @patrick-erichsen.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Existing plugin discovery keeps the same bundled official catalog while
      gaining a versioned, fail-closed fallback format for the hosted marketplace
      work. #95846 Thanks @giodl73-repo.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'ClawHub marketplace reads now fail back to OpenClaw''s bundled plugin
      catalog when hosted data is unsafe or unusable, providing a guarded base for
      the new marketplace workflow. #95868 Thanks @giodl73-repo.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Plugin update failures now report the real npm metadata or registry problem
      instead of disguising it as an unsupported package specification. #96143 Thanks
      @brokemac79, @romneyda, @slideshow-dingo.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The new openclaw plugins marketplace entries command lists available hosted
      plugins, versions, and install choices while showing whether results came from
      live, saved, or bundled data. #96158 Thanks @giodl73-repo.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Gateway startup now reports configured channels that failed to load, so
      operators can fix plugin trust, enablement, or installation before messages
      go missing. #96397 Thanks @849261680.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Operators can install a pinned older ClawHub plugin when that version
      is compatible with their OpenClaw deployment, without the latest release''s
      requirements incorrectly blocking it; incompatible or unverifiable versions
      remain blocked. #96506 Thanks @isaiahstapleton.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Plugin-heavy startup and configuration checks, especially on Windows,
      now repeat fewer package-path lookups while rebuilding installed-plugin fingerprints,
      making those paths more responsive. #96710 Thanks @211-lee, @sheyanmin, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'macOS users can run Codex Computer Use desktop controls through managed
      installation without a manual appServer.command , and an outdated Codex Desktop
      app-server no longer blocks a supported plugin-local binary. #96730 Thanks @bdjben.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Official Weixin installs and core-upgrade reconciliation now target plugin
      version 2.4.6 with its correct compatibility requirement instead of unexpectedly
      returning users to 2.4.3. #96801 Thanks @lin-hongkuan.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'openclaw plugins update --all now realigns trusted official plugins with
      the current stable or beta catalog after a core upgrade, without manual force
      installs or overwriting intentional targeted pins. #96831 Thanks @ooiuuii, @velvet-shark.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Configured and accessible native Codex plugin apps now remain available
      when a new OpenClaw thread starts during an app-inventory and activation-state
      transition instead of disappearing silently. #96872 Thanks @kevinslin.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Changes made by plugin hooks now reach agent and child-run context, including
      replacements or removals made by agent:bootstrap . #97281 Thanks @outdog-hwh.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'openclaw plugins update &lt;id&gt; --dry-run now tells operators when
      a newer default release exists even if the installed plugin is pinned exactly.
      #97282 Thanks @yungchentang.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: '/status plugins now labels a plugin as loaded only when it is actually
      running, while still showing healthy installed inventory. #97479 Thanks @masatohoshino.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Windows plugin updates no longer create managed paths so long that official
      Codex-backed agents fail before they can start and reply. #97488 Thanks @ooiuuii.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Raising a running Gateway''s log level to debug now immediately enables
      Mattermost, Matrix, Microsoft Teams, IRC, Nextcloud Talk, and other plugin diagnostics
      without a restart. #97617 Thanks @amknight, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Plugins can now react when a new DM pairing request is created, enabling
      owner alerts, audit records, tickets, and approval integrations without polling.
      #97733 Thanks @clawsean, @omarshahine, @trupe-rs.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Detailed /status plugins now flags a plugin that was configured to run
      but did not load, separating runtime drift from ordinary inactive inventory.
      #97878 Thanks @masatohoshino.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'openclaw update now accepts valid bundle-format marketplace and ClawHub
      plugins without package.json , preventing plugin sync from aborting and leaving
      the Gateway stopped. #98010 Related #97985 . Thanks @herove, @lilan0125.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'OpenClaw npm packages are now about 3.18 MB smaller unpacked and 371 KB
      smaller compressed, with plugin SDK entrypoints and runtime behavior unchanged.
      #98758 Related #98757 . Thanks @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Installing a managed npm plugin no longer makes workspace plugins from
      plugins.load.paths disappear after startup or restart. #99196 Thanks @leonidaslux.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Git-backed plugin installs and updates now work when ~/.openclaw and the
      system temp directory are on different filesystems, without a TMPDIR workaround.
      #99896 Thanks @bartok9, @carelvanheerden, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Plugin loading now honors operator-configured Jiti native-module exceptions
      while retaining protection against duplicate OpenClaw package evaluation. #100344'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Extended-stable users can install, repair, and update eligible official
      plugins at the exact OpenClaw core version instead of drifting onto the regular
      stable line. #100448 Thanks @kevinslin.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Bundled channel setup plugins now load correctly through current-release
      symlinks and mixed source/dist layouts without false outside-package warnings.
      #100758'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Source checkouts with a partial bundled plugin tree now retain complete
      built-in metadata for plugin health checks and provider endpoint discovery.
      26c0285 Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: openclaw update no longer retries a plugin after successfully moving it
      to ClawHub, preventing a redundant transient failure from disabling the migrated
      plugin. 3ce26d6 Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The GitHub Copilot plugin no longer breaks openclaw plugins list or openclaw
      status during metadata-only loading before full runtime state is available.
      #95229 Related #94516 . Thanks @cuihaijun, @sunlit-deng.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'When a Telegram plugin approval cannot be routed, operators now receive
      practical Web UI, terminal UI, and configuration guidance instead of a generic
      failure or timeout. #95973 Related #95800 . Thanks @chrisbot2026, @monkeyleet.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Provider plugins that mask text now restore intended values inside tool-call
      inputs before messages, file operations, and other external actions run. #97769
      Related #97761 . Thanks @get-viti, @zoowh.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Plugin install and update failures now show whether npm exited, was killed,
      or timed out instead of presenting a blank error that makes valid packages look
      invalid. 4dcd95d Thanks @sanjays2402, @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Plugin and media workflows now handle malformed or truncated ffprobe output
      without crashing while continuing to read valid video dimensions normally. #98613
      Thanks @pick-cat.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: '/status plugins now groups disabled plugins by reason, including allowlist,
      denylist, default, and override decisions, without changing activation behavior.
      #99598 Thanks @masatohoshino.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Plugin authors can now import shared textResult and jsonResult helpers
      from openclaw/plugin-sdk/tool-results instead of recreating common response
      shapes. #99740 Thanks @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Plugin authors now have a shared formatByteSize helper for consistent
      byte labels, while existing labels across OpenClaw remain unchanged. #99768
      Thanks @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Failed plugin installations now show the useful plugin error without adding
      a false Also not a valid hook pack diagnosis, while genuine hook-pack failures
      remain visible. #100554 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Bundled channel runtime and setup plugins now load from valid source-only
      registry roots in mixed source/dist checkouts instead of silently disappearing.
      #100737'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Duplicate plugin-request scopes now normalize consistently, and genuine
      plugin scan access failures are surfaced. #99932'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The bounded openclaw hooks commands now return control promptly after
      printing their output, so terminals, scripts, and CI jobs no longer remain stuck.
      #76922 Thanks @dorukardahan.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Built-in openclaw nodes status , openclaw nodes list , and related node
      commands now start quickly without unnecessary plugin initialization, while
      plugin-provided node commands still load when requested. #96702 Thanks @erhhung,
      @qijian-zhang, @zengwen-dt.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Shell-completion repair during openclaw doctor and updates now skips expensive
      plugin-command loading, avoiding unnecessary delays while full user-requested
      generation still includes plugin commands. #76235'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'An opt-in Doctor lint check now explains which configured plugin installation
      is broken and previews the repair before operators run the existing fix workflow.
      #96171 Thanks @giodl73-repo.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The workspace-status Doctor lint check now reports plugin drift, compatibility,
      loading diagnostics, and recoverable TaskFlow state in machine-readable form.
      #97358 Thanks @giodl73-repo.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Operators can request a structured Doctor lint check for configured channels
      whose backing plugins are blocked, including the unmet requirement and suggested
      fix. #97496 Thanks @giodl73-repo.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Structured Doctor lint can now report stale global plugin-runtime symlinks,
      including the obsolete link, its target, and the openclaw doctor --fix cleanup
      command. #98729 Thanks @giodl73-repo.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Configuration and plugin-schema validation hints now show clear allowed
      values instead of the misleading literal label undefined . #99045 Thanks @lzyyzznl.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Compact /status no longer shows the ambiguous Plugins: OK row, while warnings
      and detailed plugin diagnostics remain available. #100143'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Failed OpenClaw and plugin-harness traces now include useful redacted
      error details in OpenTelemetry instead of only a generic failure label. #101244
      Thanks @amknight.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Restarting, updating, reinstalling, or repairing a macOS Gateway now preserves
      active SecretRef-backed channel credentials instead of leaving Telegram and
      other integrations unable to authenticate. #99124 Thanks @mushuiyu886.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'openclaw agents list now shows configured external channels even when
      their plugin is missing and provides the appropriate install or openclaw doctor
      --fix guidance. #95363 Thanks @hugenshen.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Optional Doctor lint can now identify stale or missing plugin registry
      data, shadowed bundled plugins, stale install records, and broken OpenClaw peer
      links. #96169 Thanks @giodl73-repo.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Plugin operators can run doctor --lint --only core/doctor/legacy-plugin-manifests
      or --all to identify legacy manifest keys and see the affected plugin, path,
      and repair command. #98695 Thanks @giodl73-repo.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Operators can use openclaw doctor --lint --only core/doctor/legacy-plugin-dependencies
      or --all to find stale plugin dependency state and receive a path plus safe
      repair guidance without changing the installation. #98725 Thanks @giodl73-repo.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Plugin and channel-status documentation now clarifies that a MessageReceipt
      or durable sent result proves platform acceptance, not display or read confirmation
      on a recipient''s device. #90063 Thanks @pdurlej.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Plugin developers now receive clearer SDK deprecations and migration guidance
      for session-store and transcript-file helpers ahead of the planned SQLite transition.
      #97494 Thanks @jalehman.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The public onboarding docs now cover eleven existing non-interactive flags
      for token auth, Cloudflare AI Gateway, daemon, UI, hooks, and token output.
      #97753 Thanks @vincentkoc, @wm0018.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Plugin authors now get clearer packaging guidance for runtime dependencies,
      built artifacts, npm-pack: validation, and trusted official-plugin checks before
      publication. #99962 Thanks @hxy91819.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Official plugin package examples now agree on the required typebox runtime
      and openclaw peer dependencies, reducing copy-and-paste setup failures. #99973'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: The Codex and WhatsApp plugin references now identify their tools contract,
      making supported plugin capabilities easier to match with OpenClaw workflows.
      46ad3f9 Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'openclaw mcp serve and bare openclaw acp now begin with clean machine-protocol
      output, preventing startup warnings from corrupting JSON-RPC for MCP and ACP
      clients. #89997 Thanks @kenners22, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Screenshot-style images returned by plugin tools over MCP now reach clients
      as usable results instead of causing the tool call to fail. #90902 Thanks @k-schmidt,
      @mushuiyu886.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'When a bundled MCP server stops mid-session, users now get a prompt server-specific
      disconnect message and can clear the dead session by refreshing the catalog.
      #98738 Thanks @masatohoshino, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Malformed draft-2020-12 tool schemas from an MCP server now produce an
      actionable setup error that identifies the external schema and retains the underlying
      failure. #89619 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'MCP tools now receive optional null values correctly instead of having
      them changed into empty strings that can break valid calls. #97212 Thanks @vincentkoc,
      @zw-xysk.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Markdown frontmatter now preserves null-valued fields named toString ,
      constructor , valueOf , or hasOwnProperty instead of silently dropping metadata
      from skills, hooks, or commands. #99129 Thanks @vincentkoc, @zenglingbiao.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Invalid plugin approval requests now show the actual validation problem
      instead of misleading users with a Gateway-unavailable error. #100337 Thanks
      @tzy-17.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Automatic session rotation is less likely to strand the next conversation
      when a context-engine plugin immediately reads or checkpoints its transcript.
      #101192'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Restored reliable changed-code validation for plugin discovery work without
      altering plugin behavior. #87695 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Added repeatable Slack QA coverage for Codex command and file-change approvals.
      #91519 Thanks @kevinslin.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Enabled repeatable WhatsApp integration testing against a controlled local
      service without requiring live credentials. #95920 Thanks @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Reduced repeated work when plugins resolve cached tool calls without changing
      tool selection. #96948 Thanks @ly-wang19.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Reduced bookkeeping during updates that encounter many missing plugin
      files while preserving repair decisions and warnings. #96950 Thanks @ly-wang19.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Refreshed plugin SDK validation limits to match the current public surface
      while preserving future growth checks. #97604 Thanks @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Improved QA traceability for gateway connection, protocol negotiation,
      and startup retry behavior used by MCP channel bridges. #97609 Thanks @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Restored reliable plugin SDK build validation by removing a conflicting
      test-only definition. #97661 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Added structured QA coverage for ClawHub marketplace listings and packaged
      plugin installation checks. #97712 Thanks @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Enabled Slack QA flows to run against a local test provider, reducing
      reliance on live Slack credentials. #97891 Thanks @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Improved official plugin publishing reliability by adopting corrected
      ClawHub package-family detection. #97907 Thanks @patrick-erichsen.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Updated official plugin publishing to use corrected ClawHub tooling for
      package-family handling. #98233 Thanks @patrick-erichsen.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Allowed four legacy official plugins to be republished without ClawHub
      rejecting their established package family. #98249 Thanks @patrick-erichsen.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Prevented message-tool tests from timing out while preserving the plugin
      behavior they verify. #98701'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Unified repeated loading patterns across Discord, Slack, and Telegram
      while preserving existing channel behavior. #99298 Thanks @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Restored CI checks for Telegram context handling and supported plugin
      SDK boundaries. #99355 Thanks @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Consolidated repeated data-shape checks across bundled plugins to reduce
      maintenance drift. #99361 Thanks @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Unified internal work ordering across account, session, file, message,
      and plugin paths while preserving existing behavior. #99691 Thanks @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Strengthened release validation for important chat, search, compatibility,
      and plugin workflows. #99705 Thanks @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Made web and WebSocket address validation more consistent across configuration,
      proxy, media, webhook, and plugin workflows. #99719 Thanks @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Consolidated common waiting and timeout behavior across core workflows,
      plugins, tools, and tests without changing intended timing. #99721 Thanks @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Strengthened release coverage for real Gateway and MCP startup, connections,
      discovery, negotiation, and tool calls. #99735 Thanks @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Consolidated shared channel state and plugin migration maintenance across
      Slack, Mattermost, Teams, and Matrix without changing workflows. #99850'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Prevented Codex plugin releases from publishing with an outdated embedded
      runtime, reducing false-green updates. #100015 Thanks @100yenadmin, @fuller-stack-dev.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Removed redundant internal type names so maintainers and plugin developers
      can follow affected code more directly. #100061 Thanks @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Restored complete package artifacts for more reliable source, Docker,
      and plugin development builds. #100249 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Recorded three shipped plugin and configuration fixes so their release
      coverage remained complete. #100609 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Made plugin registry expectations clearer and easier to validate without
      changing runtime behavior. #100990 Thanks @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Consolidated Slack and Matrix thread and direct-message coverage for clearer
      cross-channel validation. #101112 Thanks @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Clarified the Copilot plugin''s internal boundaries without changing its
      runtime behavior. #101379 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Kept private plugin details internal, improving dead-code reports and
      future cleanup. #101406 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Clarified supported boundaries for the Brave, Firecrawl, and DeepInfra
      provider plugins. #101425 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Kept OpenCode Go streaming and catalog internals private so extension
      developers see clearer integration boundaries. #101440 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Cleaned up private OpenRouter and SMS plugin definitions to improve internal
      API accuracy. #101452 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Contributed to the fix that keeps plugin approval text readable when emoji
      appear near length limits. #101579 Thanks @wm0018.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Clarified internal boundaries across reply handling and bundled plugins
      without changing runtime behavior. #101666 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Reduced accidental internal interfaces across core, plugins, and the Control
      UI to simplify ongoing maintenance. #101701 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Strengthened compatibility checks for the bundled Codex integration to
      catch request mismatches before release. #101726 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Kept private implementation details from appearing as supported integration
      points, improving codebase maintainability. #101731 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Expanded release preflight coverage so official plugin packages can be
      built and inspected before an extended-stable npm release. #101757 Thanks @kevinslin.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Reduced unused internal declarations across core, plugins, and the Control
      UI without changing product behavior. #101758 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Reduced accidental internal interfaces in bundled extensions without changing
      plugin behavior. #101860 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Made plugin tests more portable across common developer and hosted environments.
      #101896'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Clarified the browser plugin''s supported surface by keeping implementation
      details private. #101898 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Clarified Microsoft Teams plugin boundaries by keeping private implementation
      details internal. #101903 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Clarified internal boundaries in the ClickClack and Logbook plugins without
      changing their behavior. #101922 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Clarified the iMessage plugin''s internal boundaries without changing
      its capabilities or behavior. #101936 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Clarified which Feishu integration details are private, making the code
      easier to maintain. #101949 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Narrowed Matrix integration internals without changing user behavior or
      documented configuration. #101954 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Clarified the WhatsApp integration''s supported type surface while preserving
      messaging behavior. #101959 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Clarified internal boundaries in the Diffs and File Transfer plugins without
      changing their behavior. #102021 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Kept Google Chat implementation details private while preserving all existing
      integration behavior. #102029 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Narrowed LINE integration internals without changing messages, webhooks,
      or configuration. #102037 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Clarified Mattermost integration boundaries by keeping implementation-only
      details private. #102040 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Reduced accidental internal interfaces in the Signal plugin without changing
      how Signal works. #102042 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Narrowed Slack plugin internals while preserving messaging and delivery
      behavior. #102044 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Clarified QQBot''s supported integration surface without changing runtime
      behavior. #102048 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Narrowed Zalo integration internals without changing messaging, webhooks,
      media, or configuration. #102065 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Restored reliable Codex plugin release validation after its connection
      records moved to a new storage system. #103467 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Restored Chinese documentation validation for Meta provider and plugin
      reference pages. #103923'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Backported fixes for startup recovery, Discord reconnection, readable
      refusal messages, and lighter plugin listing. #104794 Thanks @wuqxuan.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 213-apps-and-integrations-changes-in-v2026-7-1
  source_release: openclaw-2026-07-13-v2026-7-1-c2063718
  source_type: openclaw_changelog
  theme: apps-integrations
  title: 213 Apps and Integrations changes in v2026.7.1
  type: change
related_changes:
- '[[Changes/Lovable/2026-07-13-connect-klipy-in-one-click-no-api-key|Connect KLIPY
  in one click, no API key]]'
- '[[Changes/Lovable/2026-07-13-mapbox-connector|Mapbox connector]]'
- '[[Changes/Lovable/2026-07-13-let-your-app-s-users-connect-their-own-accounts|Let
  your app''s users connect their own accounts]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-07-13-v2026-7-1-c2063718|openclaw-2026-07-13-v2026-7-1-c2063718]]'
source_type: openclaw_changelog
theme: apps-integrations
title: 213 Apps and Integrations changes in v2026.7.1
type: change
---

<!-- chronolog:begin region="header" -->
# 213 Apps and Integrations changes in v2026.7.1

**OpenClaw** · 2026-07-13 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.7.1) · from [[Releases/OpenClaw/openclaw-2026-07-13-v2026-7-1-c2063718|v2026.7.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Existing installations receive safeguards before their working state is changed. Doctor and updates refuse to replace an unreadable configuration, Doctor preserves model tuning while merging retired entries, and extended-stable updates retain the selected release channel. Container upgrades complete migrations and plugin repairs before reporting readiness, and unsafe runtimes are stopped before they can open OpenClaw state databases.

> openclaw doctor and updates now refuse to replace an unreadable openclaw.json , preserving existing Gateway, agent, channel, and plugin settings instead of breaking the installation. #96469 Thanks @obviyus, @yetval.

> Container upgrades now finish required migrations and plugin repairs before reporting the Gateway ready, and failed repairs stop with actionable guidance instead of leaving a false-green service. #101881 Thanks @sallyom.

> Hosted LongCat-2.0 can now be installed through the official LongCat plugin, configured with LONGCAT_API_KEY during onboarding, and selected as longcat/LongCat-2.0 for multi-turn tool use. #100501 Thanks @vincentkoc.

> When Slack accepts a reply but the confirmation is lost, OpenClaw can verify the existing post and avoid sending a duplicate. #97480 Thanks @joeyfrasier.

> Discord, Slack, WhatsApp, Apple Messages, and other supported channels also receive clearer command, thread, attachment, proxy, and recovery behavior. The Apple Messages setup and delivery paths in this group preserve the chat context readers expect rather than exposing the routing work underneath.

> Slack operators running multiple Gateways through one Socket Mode app now receive a startup warning explaining why events may reach another connection and how to choose a safer deployment setup. #79938 Thanks @jeffvsutherland.

> Slack operators can now choose off , first , all , or batched reply threading per channel, with automatic replies and message tools following the same effective choice. #82253

> Slack button and select interactions now remain in the correct assistant thread and show a working status there until the follow-up turn finishes. #82895 Thanks @wukongai-cmu.

> Longer Slack assistant-thread replies now show changing progress notes so users can tell OpenClaw is still working. #85507 Thanks @emergentash.

> Slack rich-text block actions can now include emoji near the preview limit without producing malformed interaction text or downstream encoding failures. #96577 Thanks @llagy007, @weeli-009.

> The first Slack reply after a daily or idle reset can reuse recent thread history, so the conversation does not suddenly start from scratch. #97100 Thanks @bek91.

> Slack replies no longer expose internal tool-failure banners, reasoning scaffolding, or tool-call markup to users. #97367 Thanks @masatohoshino.

> Slack replies now retry after a temporary session-start conflict instead of stopping before the expected message is delivered. #99647 Thanks @steipete-oai.

> Slack buttons and menus now preserve time labels such as 9:00 and return the intended action value when selected. #99877 Thanks @qingminglong, @rodja.

> Slack message reactions now accept common emoji or shortcode names, can target the current message without repeating its ID, and provide clearer member-lookup guidance. #100375 Thanks @gorkem2020.

> Slack now uses one static acknowledgement reaction alongside its native assistant loading status by default, avoiding two competing progress displays for the same reply. #100462 Thanks @steipete-oai.

> Ordinary Slack thread replies no longer download and process the opening message attachments again, while new or reset sessions still receive those files once. #100516

> Messages that fail before reaching Discord, Slack, Matrix, or another channel can now be replayed after connectivity returns, while uncertain post-send outcomes still avoid blind duplicates. #101024 Thanks @sunnyshu0925.

> Channel previews, thread names, snippets, and shortened errors across browser and messaging integrations now preserve whole emoji and other Unicode characters. c16bb87 Thanks @vincentkoc.

> Signal reaction shortcuts now apply only to the intended structured exec or plugin approval, including forwarded monitor and chunked prompts, while ordinary messages that merely quote approval commands no longer gain controls; older delivered prompts may still require /approve once after upgrade. #96880 Thanks @joshavant.

> Long unbroken messages now keep emoji intact when split into delivery-sized chunks, preventing garbled replacement characters for users and channel plugins. #96951 Thanks @bartok9, @ly-wang19.

> Always-on group agents can now receive and answer valid unmentioned messages after a plugin fallback instead of silently dropping them. #99506 Related #99457 . Thanks @lzy3538, @zqchris.

> Telegram stickers and other plugin message actions now stay in the active forum topic or thread when sent to the matching conversation, including through Gateway dispatch. #80293 Thanks @artdaal.

> Telegram and Discord plugin commands that send their own response can return { suppressReply: true } , preventing a second misleading empty-response warning or failure. #80928 Related #80756 . Thanks @alexuser, @unclouded77.

> With messages.ackReactionScope: "all" , ambient room messages now receive the configured acknowledgement reaction across Discord, Slack, and Telegram. #87433 Thanks @paul-phan, @scoootscooob.

> Telegram inline buttons supplied by plugins now run their intended actions and cleanup instead of posting raw callback data into chat. #97174 Thanks @goldmar.

> Slack read actions can again access intentionally allowlisted channel names when Slack supplies an ID and dangerouslyAllowNameMatching is enabled. #95313 Thanks @jontsai.

> Slack message and attachment text is no longer copied into verbose or debug logs during inbound processing. #96312 Thanks @steipete-oai.

> Slack messages and Block Kit labels now truncate without splitting emoji into broken replacement characters or invalid payload text. #96382 Thanks @ly-wang19.

> Long Slack command and plugin approval previews now keep emoji intact at the length boundary, avoiding malformed approval text or payloads. #96576 Thanks @llagy007, @weeli-009.

> OpenClaw can use a trusted override for a compatible Slack API endpoint, while normal workspaces continue using Slack's public API and untrusted project .env files cannot redirect bearer-token requests. #97154 Thanks @romneyda.

> Slack slash-command choice menus now shorten long labels without splitting emoji at the 75-character limit. #97923 Thanks @lexes7.

> Slack Socket Mode relay diagnostics now distinguish malformed WebSocket frames from transport failures, making channel problems easier to identify. #98587 Thanks @lsr911, @vincentkoc.

> Slack Codex conversations now retain one final assistant reply in history instead of duplicating it through both the app-server transcript and delivery fallback. #100160 Thanks @steipete-oai.

> Mattermost installations repaired after an upgrade now load and reconnect on Gateway restart without requiring a manual plugin-enable setting, including restrictive allowlist setups. #98608 Related #98564 . Thanks @jacobtomlinson, @shakkernerd.

> Channel plugins can resume automatic recovery after a long healthy run, so an occasional later disconnect is not blocked by an old restart budget while true rapid crash loops remain capped. #101413 Thanks @clintoncodewell.

> Library and integration developers can now install a version-matched package, create independent AI runtimes, and reuse OpenClaw's supported model transports without embedding the full application. #99059

> The bundled Codex plugin can complete backend requests again after updating its managed app-server runtime, with no model-picker or configuration migration required. #106098

> Generic provider configurations for official DashScope/Qwen, Moonshot, Z.AI, DeepSeek, Groq, Cerebras, and Chutes endpoints now retain the compatibility behavior those services require even without optional plugins. #100125

> MCP tools that expect arrays or objects can now accept those values when Xiaomi MiMo, Ollama, or another affected provider returns them as JSON strings, avoiding a pre-execution validation failure. #96922 Thanks @liuhao1024.

> Context-engine plugins can now identify the exact session that continues after compaction while older integrations using sessionFile remain compatible. #101182 Thanks @jalehman.

> Slack and similar channel turns with context-injecting plugins now send each inbound system label to the model once instead of duplicating it. #95349 Thanks @gorkem2020, @openperf, @vincentkoc.

> Local Ollama-backed CLI agent turns can now continue when the context engine reports an already-compacted transcript, allowing the assistant or MCP tool result to reach the user. #99136 Thanks @mushuiyu886, @peterskwang, @pkoserowski, @psedd.

> MCP stdio sessions now report stderr pipe failures as transport errors without taking down OpenClaw or losing available diagnostics. #99803 Thanks @cxbasdev, @vincentkoc.

> ACPX MCP proxies now turn closed input or output pipes into a clear proxy failure instead of an uncaught Node stream crash. #99852 Thanks @sunlit-deng, @vincentkoc.

> Sub-agents and other HTTP loopback MCP clients can again receive browser screenshots and valid image or embedded-resource results without schema failures. #100336 Thanks @tzy-17.

> Lean local-model agents can now choose the familiar exec tool directly when policy permits it, while existing allowlists, sandboxing, approvals, and hooks still govern command execution. #101607 Thanks @vincentkoc.

> Shortened text across CLI output, diagnostics, plugin messages, previews, errors, task summaries, and Zalo sends now preserves complete emoji and other supplementary characters. #101654 Thanks @lsr911, @maweibin, @wm0018.

> Legacy Codex bindings with large tool or MCP configurations can now migrate without overflowing plugin-state records or copying raw configuration secrets. 23228b6 Thanks @vincentkoc.

> Codex sessions created in beta 5 can keep their existing conversation after upgrade when the user MCP configuration is unchanged, without retaining its authorization token. 272750d Thanks @vincentkoc.

> Agent requests with several MCP servers now initialize those servers concurrently, shortening the wait before the model begins while isolating slow or failed servers. #94230 Thanks @mmyzwl, @vincentkoc.

> New Codex-backed threads now preserve configured plugin apps, can activate remote curated plugins, and run Guardian on the first eligible native OpenAI turn. #98042 Thanks @kevinslin.

> Discord now presents commentary, reasoning, and tool activity in a clearer sequence across queued turns, while loopback MCP clients can attach to one Gateway session with an expiring, revocable token. 35af831 Thanks @dwc1997, @lsr911, @ooiuuii, @romneyda, @solodmd, @vincentkoc, @wendy-chsy, @yeager, @zenglingbiao.

> Embedded terminals can now open, resize, stream output, and close consistently across the Gateway, Control UI, and native apps. 6601576

> Gateway startup channel warnings now use the same plugin manifests as the running startup process, reducing inconsistent warnings and repeated discovery. 10ca94e Thanks @vincentkoc.

> An agent no longer stays silent after compaction when a plugin's final-answer hook hangs; OpenClaw times out the hook and still delivers the response. b2baf79 Thanks @dserious, @obviyus, @villa-feng.

> Gateway MCP logs are now quieter and identify the responsible tool when schema problems occur, while distinct conflicts remain visible. #98821 Thanks @alvelda, @harjothkhara.

> Malformed Gateway MCP tools/call arguments now return a clear invalid-parameters response before any hook or tool can process them. #99180 Thanks @vectorpeak.

> MCP attach requests without a valid session key now return the intended validation error instead of crashing the Gateway with a TypeError. #99488 Thanks @zhanglei99586.

> Discord Code Mode progress no longer fills with repetitive Wait rows from background polling, while ordinary custom and plugin tools remain visible. #100164

> ClawHub now checks community plugin and skill releases before download, blocking prohibited releases and requiring explicit acknowledgement for suspicious ones while leaving existing installs in place when an update is skipped. #81364 Thanks @jesse-merhi.

> Authorized non-owner chat participants can no longer inspect or change owner-controlled MCP server configuration through /mcp . ad5a26c Thanks @joshavant.

> Codex session bindings now keep large MCP configurations and rotated Authorization credentials in bounded fingerprints without persisting readable bearer values. 491e42e Thanks @100yenadmin.

> Hooks and skills no longer activate from unsafe inherited configuration values, while ordinary configured paths and explicit defaults continue to work. #59694 Thanks @yonganzhang.

> Codex plugin users can allow read-only app actions while requiring a fresh approval for every write or destructive action. #97123 Thanks @kevinslin.

> Codex plugin apps now avoid approval prompts for read-only actions, preserve per-app write policies across recovery, and refresh their app inventory after upgrades. #97327 Thanks @kevinslin.

> The Codex plugin now names per-action destructive approval mode ask , making it clear that each write or destructive action remains available but requires confirmation. #98501 Related #98499 . Thanks @kevinslin.

> Authenticated owners can use their already-granted shell, file, process, Skill Workshop, and plugin tools in WebChat without extending those permissions to guests or external senders. #101271 Thanks @fuller-stack-dev.

> MCP include and exclude filters with many wildcard segments now reject nonmatches quickly instead of stalling tool discovery for minutes. #100330 Thanks @lsr911.

> Codex /btw side conversations now preserve an ask-mode plugin app's requirement to obtain approval before destructive actions. #98812

> Installing or updating ClawHub skills, plugins, and packages on Linux no longer risks changing shared /tmp permissions and disrupting unrelated services. #101246 Thanks @ch3ch2cho2021, @yangxiansheng.

> Plugin approval titles and descriptions now remain readable when emoji or supplementary CJK characters fall at the Gateway's text limit. #101580 Thanks @wm0018.

> TUI /new now performs a real session transition with the expected lifecycle hooks and prevents a new session from racing an active turn. #100241 Thanks @caopulan.

> Supported non-English native apps now translate newer app information, support links, and message retry, delete, and waiting-to-send states. 82f5ac1

> The Mac About screen now links directly to the OpenClaw website, documentation, GitHub project, and Discord community, matching the other native apps. 6e7ef63

> Skills can be drafted from a conversation or source, reviewed, pinned, archived, restored, and kept out of future context when stale. Plugin management is clearer about discovery, installation, updates, marketplace snapshots, connected Codex apps, approvals, and runtime failures, while Codex supervision can give each new thread an explicit bounded app allowlist.

> Official packages are easier to obtain through the supported Docker and Android paths, and plugin-backed workflows such as Google Meet and Apple Messages recover from more setup and migration problems. Doctor also handles damaged migration caches and older plugin or skill layouts without turning a recoverable upgrade into a dead end.

> Operators can run openclaw plugins marketplace refresh to verify and save a hosted feed, enforce a SHA-256 match, and see whether live, saved, or bundled data was used. #96155 Thanks @giodl73-repo.

> Updated integration runtimes keep Codex, ACP, Copilot, Telegram, and diff rendering aligned with compatible upstream behavior, while reconnect recovery no longer floods operator logs with duplicate messages. #100027

> Declared plugin tools now remain callable in subagent sessions after plugin registry changes, avoiding repeated plugin tool runtime missing failures and Gateway restarts. #82562 Thanks @luoyanglang, @vincentkoc.

> Plugin metadata cache hits no longer flood diagnostics with repeated full-scan entries, leaving smaller timelines where real scans are easier to identify. #86796 Thanks @galiniliev, @vincentkoc.

> Plugin loading no longer evaluates OpenClaw's own package code twice, reducing startup work and avoiding duplicate module, class, singleton, or registry identities in one process. #88384 Thanks @vincentkoc.

> openclaw plugins inspect now shows the bundled document-extract plugin's PDF extractor as an available capability instead of reporting none. #91597 Thanks @xydt-tanshanshan.

> openclaw plugins init can now scaffold a model-provider plugin with authentication, model setup, tests, packaging, validation, and ClawHub publishing structure. #94352 Thanks @patrick-erichsen.

> Existing plugin discovery keeps the same bundled official catalog while gaining a versioned, fail-closed fallback format for the hosted marketplace work. #95846 Thanks @giodl73-repo.

> ClawHub marketplace reads now fail back to OpenClaw's bundled plugin catalog when hosted data is unsafe or unusable, providing a guarded base for the new marketplace workflow. #95868 Thanks @giodl73-repo.

> Plugin update failures now report the real npm metadata or registry problem instead of disguising it as an unsupported package specification. #96143 Thanks @brokemac79, @romneyda, @slideshow-dingo.

> The new openclaw plugins marketplace entries command lists available hosted plugins, versions, and install choices while showing whether results came from live, saved, or bundled data. #96158 Thanks @giodl73-repo.

> Gateway startup now reports configured channels that failed to load, so operators can fix plugin trust, enablement, or installation before messages go missing. #96397 Thanks @849261680.

> Operators can install a pinned older ClawHub plugin when that version is compatible with their OpenClaw deployment, without the latest release's requirements incorrectly blocking it; incompatible or unverifiable versions remain blocked. #96506 Thanks @isaiahstapleton.

> Plugin-heavy startup and configuration checks, especially on Windows, now repeat fewer package-path lookups while rebuilding installed-plugin fingerprints, making those paths more responsive. #96710 Thanks @211-lee, @sheyanmin, @vincentkoc.

> macOS users can run Codex Computer Use desktop controls through managed installation without a manual appServer.command , and an outdated Codex Desktop app-server no longer blocks a supported plugin-local binary. #96730 Thanks @bdjben.

> Official Weixin installs and core-upgrade reconciliation now target plugin version 2.4.6 with its correct compatibility requirement instead of unexpectedly returning users to 2.4.3. #96801 Thanks @lin-hongkuan.

> openclaw plugins update --all now realigns trusted official plugins with the current stable or beta catalog after a core upgrade, without manual force installs or overwriting intentional targeted pins. #96831 Thanks @ooiuuii, @velvet-shark.

> Configured and accessible native Codex plugin apps now remain available when a new OpenClaw thread starts during an app-inventory and activation-state transition instead of disappearing silently. #96872 Thanks @kevinslin.

> Changes made by plugin hooks now reach agent and child-run context, including replacements or removals made by agent:bootstrap . #97281 Thanks @outdog-hwh.

> openclaw plugins update &lt;id&gt; --dry-run now tells operators when a newer default release exists even if the installed plugin is pinned exactly. #97282 Thanks @yungchentang.

> /status plugins now labels a plugin as loaded only when it is actually running, while still showing healthy installed inventory. #97479 Thanks @masatohoshino.

> Windows plugin updates no longer create managed paths so long that official Codex-backed agents fail before they can start and reply. #97488 Thanks @ooiuuii.

> Raising a running Gateway's log level to debug now immediately enables Mattermost, Matrix, Microsoft Teams, IRC, Nextcloud Talk, and other plugin diagnostics without a restart. #97617 Thanks @amknight, @vincentkoc.

> Plugins can now react when a new DM pairing request is created, enabling owner alerts, audit records, tickets, and approval integrations without polling. #97733 Thanks @clawsean, @omarshahine, @trupe-rs.

> Detailed /status plugins now flags a plugin that was configured to run but did not load, separating runtime drift from ordinary inactive inventory. #97878 Thanks @masatohoshino.

> openclaw update now accepts valid bundle-format marketplace and ClawHub plugins without package.json , preventing plugin sync from aborting and leaving the Gateway stopped. #98010 Related #97985 . Thanks @herove, @lilan0125.

> OpenClaw npm packages are now about 3.18 MB smaller unpacked and 371 KB smaller compressed, with plugin SDK entrypoints and runtime behavior unchanged. #98758 Related #98757 . Thanks @romneyda.

> Installing a managed npm plugin no longer makes workspace plugins from plugins.load.paths disappear after startup or restart. #99196 Thanks @leonidaslux.

> Git-backed plugin installs and updates now work when ~/.openclaw and the system temp directory are on different filesystems, without a TMPDIR workaround. #99896 Thanks @bartok9, @carelvanheerden, @vincentkoc.

> Plugin loading now honors operator-configured Jiti native-module exceptions while retaining protection against duplicate OpenClaw package evaluation. #100344

> Extended-stable users can install, repair, and update eligible official plugins at the exact OpenClaw core version instead of drifting onto the regular stable line. #100448 Thanks @kevinslin.

> Bundled channel setup plugins now load correctly through current-release symlinks and mixed source/dist layouts without false outside-package warnings. #100758

> Source checkouts with a partial bundled plugin tree now retain complete built-in metadata for plugin health checks and provider endpoint discovery. 26c0285 Thanks @vincentkoc.

> openclaw update no longer retries a plugin after successfully moving it to ClawHub, preventing a redundant transient failure from disabling the migrated plugin. 3ce26d6 Thanks @vincentkoc.

> The GitHub Copilot plugin no longer breaks openclaw plugins list or openclaw status during metadata-only loading before full runtime state is available. #95229 Related #94516 . Thanks @cuihaijun, @sunlit-deng.

> When a Telegram plugin approval cannot be routed, operators now receive practical Web UI, terminal UI, and configuration guidance instead of a generic failure or timeout. #95973 Related #95800 . Thanks @chrisbot2026, @monkeyleet.

> Provider plugins that mask text now restore intended values inside tool-call inputs before messages, file operations, and other external actions run. #97769 Related #97761 . Thanks @get-viti, @zoowh.

> Plugin install and update failures now show whether npm exited, was killed, or timed out instead of presenting a blank error that makes valid packages look invalid. 4dcd95d Thanks @sanjays2402, @vincentkoc.

> Plugin and media workflows now handle malformed or truncated ffprobe output without crashing while continuing to read valid video dimensions normally. #98613 Thanks @pick-cat.

> /status plugins now groups disabled plugins by reason, including allowlist, denylist, default, and override decisions, without changing activation behavior. #99598 Thanks @masatohoshino.

> Plugin authors can now import shared textResult and jsonResult helpers from openclaw/plugin-sdk/tool-results instead of recreating common response shapes. #99740 Thanks @romneyda.

> Plugin authors now have a shared formatByteSize helper for consistent byte labels, while existing labels across OpenClaw remain unchanged. #99768 Thanks @romneyda.

> Failed plugin installations now show the useful plugin error without adding a false Also not a valid hook pack diagnosis, while genuine hook-pack failures remain visible. #100554 Thanks @vincentkoc.

> Bundled channel runtime and setup plugins now load from valid source-only registry roots in mixed source/dist checkouts instead of silently disappearing. #100737

> Duplicate plugin-request scopes now normalize consistently, and genuine plugin scan access failures are surfaced. #99932

> The bounded openclaw hooks commands now return control promptly after printing their output, so terminals, scripts, and CI jobs no longer remain stuck. #76922 Thanks @dorukardahan.

> Built-in openclaw nodes status , openclaw nodes list , and related node commands now start quickly without unnecessary plugin initialization, while plugin-provided node commands still load when requested. #96702 Thanks @erhhung, @qijian-zhang, @zengwen-dt.

> Shell-completion repair during openclaw doctor and updates now skips expensive plugin-command loading, avoiding unnecessary delays while full user-requested generation still includes plugin commands. #76235

> An opt-in Doctor lint check now explains which configured plugin installation is broken and previews the repair before operators run the existing fix workflow. #96171 Thanks @giodl73-repo.

> The workspace-status Doctor lint check now reports plugin drift, compatibility, loading diagnostics, and recoverable TaskFlow state in machine-readable form. #97358 Thanks @giodl73-repo.

> Operators can request a structured Doctor lint check for configured channels whose backing plugins are blocked, including the unmet requirement and suggested fix. #97496 Thanks @giodl73-repo.

> Structured Doctor lint can now report stale global plugin-runtime symlinks, including the obsolete link, its target, and the openclaw doctor --fix cleanup command. #98729 Thanks @giodl73-repo.

> Configuration and plugin-schema validation hints now show clear allowed values instead of the misleading literal label undefined . #99045 Thanks @lzyyzznl.

> Compact /status no longer shows the ambiguous Plugins: OK row, while warnings and detailed plugin diagnostics remain available. #100143

> Failed OpenClaw and plugin-harness traces now include useful redacted error details in OpenTelemetry instead of only a generic failure label. #101244 Thanks @amknight.

> Restarting, updating, reinstalling, or repairing a macOS Gateway now preserves active SecretRef-backed channel credentials instead of leaving Telegram and other integrations unable to authenticate. #99124 Thanks @mushuiyu886.

> openclaw agents list now shows configured external channels even when their plugin is missing and provides the appropriate install or openclaw doctor --fix guidance. #95363 Thanks @hugenshen.

> Optional Doctor lint can now identify stale or missing plugin registry data, shadowed bundled plugins, stale install records, and broken OpenClaw peer links. #96169 Thanks @giodl73-repo.

> Plugin operators can run doctor --lint --only core/doctor/legacy-plugin-manifests or --all to identify legacy manifest keys and see the affected plugin, path, and repair command. #98695 Thanks @giodl73-repo.

> Operators can use openclaw doctor --lint --only core/doctor/legacy-plugin-dependencies or --all to find stale plugin dependency state and receive a path plus safe repair guidance without changing the installation. #98725 Thanks @giodl73-repo.

> Plugin and channel-status documentation now clarifies that a MessageReceipt or durable sent result proves platform acceptance, not display or read confirmation on a recipient's device. #90063 Thanks @pdurlej.

> Plugin developers now receive clearer SDK deprecations and migration guidance for session-store and transcript-file helpers ahead of the planned SQLite transition. #97494 Thanks @jalehman.

> The public onboarding docs now cover eleven existing non-interactive flags for token auth, Cloudflare AI Gateway, daemon, UI, hooks, and token output. #97753 Thanks @vincentkoc, @wm0018.

> Plugin authors now get clearer packaging guidance for runtime dependencies, built artifacts, npm-pack: validation, and trusted official-plugin checks before publication. #99962 Thanks @hxy91819.

> Official plugin package examples now agree on the required typebox runtime and openclaw peer dependencies, reducing copy-and-paste setup failures. #99973

> The Codex and WhatsApp plugin references now identify their tools contract, making supported plugin capabilities easier to match with OpenClaw workflows. 46ad3f9 Thanks @vincentkoc.

> openclaw mcp serve and bare openclaw acp now begin with clean machine-protocol output, preventing startup warnings from corrupting JSON-RPC for MCP and ACP clients. #89997 Thanks @kenners22, @vincentkoc.

> Screenshot-style images returned by plugin tools over MCP now reach clients as usable results instead of causing the tool call to fail. #90902 Thanks @k-schmidt, @mushuiyu886.

> When a bundled MCP server stops mid-session, users now get a prompt server-specific disconnect message and can clear the dead session by refreshing the catalog. #98738 Thanks @masatohoshino, @vincentkoc.

> Malformed draft-2020-12 tool schemas from an MCP server now produce an actionable setup error that identifies the external schema and retains the underlying failure. #89619 Thanks @vincentkoc.

> MCP tools now receive optional null values correctly instead of having them changed into empty strings that can break valid calls. #97212 Thanks @vincentkoc, @zw-xysk.

> Markdown frontmatter now preserves null-valued fields named toString , constructor , valueOf , or hasOwnProperty instead of silently dropping metadata from skills, hooks, or commands. #99129 Thanks @vincentkoc, @zenglingbiao.

> Invalid plugin approval requests now show the actual validation problem instead of misleading users with a Gateway-unavailable error. #100337 Thanks @tzy-17.

> Automatic session rotation is less likely to strand the next conversation when a context-engine plugin immediately reads or checkpoints its transcript. #101192

> Restored reliable changed-code validation for plugin discovery work without altering plugin behavior. #87695 Thanks @vincentkoc.

> Added repeatable Slack QA coverage for Codex command and file-change approvals. #91519 Thanks @kevinslin.

> Enabled repeatable WhatsApp integration testing against a controlled local service without requiring live credentials. #95920 Thanks @romneyda.

> Reduced repeated work when plugins resolve cached tool calls without changing tool selection. #96948 Thanks @ly-wang19.

> Reduced bookkeeping during updates that encounter many missing plugin files while preserving repair decisions and warnings. #96950 Thanks @ly-wang19.

> Refreshed plugin SDK validation limits to match the current public surface while preserving future growth checks. #97604 Thanks @romneyda.

> Improved QA traceability for gateway connection, protocol negotiation, and startup retry behavior used by MCP channel bridges. #97609 Thanks @romneyda.

> Restored reliable plugin SDK build validation by removing a conflicting test-only definition. #97661 Thanks @vincentkoc.

> Added structured QA coverage for ClawHub marketplace listings and packaged plugin installation checks. #97712 Thanks @romneyda.

> Enabled Slack QA flows to run against a local test provider, reducing reliance on live Slack credentials. #97891 Thanks @romneyda.

> Improved official plugin publishing reliability by adopting corrected ClawHub package-family detection. #97907 Thanks @patrick-erichsen.

> Updated official plugin publishing to use corrected ClawHub tooling for package-family handling. #98233 Thanks @patrick-erichsen.

> Allowed four legacy official plugins to be republished without ClawHub rejecting their established package family. #98249 Thanks @patrick-erichsen.

> Prevented message-tool tests from timing out while preserving the plugin behavior they verify. #98701

> Unified repeated loading patterns across Discord, Slack, and Telegram while preserving existing channel behavior. #99298 Thanks @romneyda.

> Restored CI checks for Telegram context handling and supported plugin SDK boundaries. #99355 Thanks @romneyda.

> Consolidated repeated data-shape checks across bundled plugins to reduce maintenance drift. #99361 Thanks @romneyda.

> Unified internal work ordering across account, session, file, message, and plugin paths while preserving existing behavior. #99691 Thanks @romneyda.

> Strengthened release validation for important chat, search, compatibility, and plugin workflows. #99705 Thanks @romneyda.

> Made web and WebSocket address validation more consistent across configuration, proxy, media, webhook, and plugin workflows. #99719 Thanks @romneyda.

> Consolidated common waiting and timeout behavior across core workflows, plugins, tools, and tests without changing intended timing. #99721 Thanks @romneyda.

> Strengthened release coverage for real Gateway and MCP startup, connections, discovery, negotiation, and tool calls. #99735 Thanks @romneyda.

> Consolidated shared channel state and plugin migration maintenance across Slack, Mattermost, Teams, and Matrix without changing workflows. #99850

> Prevented Codex plugin releases from publishing with an outdated embedded runtime, reducing false-green updates. #100015 Thanks @100yenadmin, @fuller-stack-dev.

> Removed redundant internal type names so maintainers and plugin developers can follow affected code more directly. #100061 Thanks @romneyda.

> Restored complete package artifacts for more reliable source, Docker, and plugin development builds. #100249 Thanks @vincentkoc.

> Recorded three shipped plugin and configuration fixes so their release coverage remained complete. #100609 Thanks @vincentkoc.

> Made plugin registry expectations clearer and easier to validate without changing runtime behavior. #100990 Thanks @romneyda.

> Consolidated Slack and Matrix thread and direct-message coverage for clearer cross-channel validation. #101112 Thanks @romneyda.

> Clarified the Copilot plugin's internal boundaries without changing its runtime behavior. #101379 Thanks @vincentkoc.

> Kept private plugin details internal, improving dead-code reports and future cleanup. #101406 Thanks @vincentkoc.

> Clarified supported boundaries for the Brave, Firecrawl, and DeepInfra provider plugins. #101425 Thanks @vincentkoc.

> Kept OpenCode Go streaming and catalog internals private so extension developers see clearer integration boundaries. #101440 Thanks @vincentkoc.

> Cleaned up private OpenRouter and SMS plugin definitions to improve internal API accuracy. #101452 Thanks @vincentkoc.

> Contributed to the fix that keeps plugin approval text readable when emoji appear near length limits. #101579 Thanks @wm0018.

> Clarified internal boundaries across reply handling and bundled plugins without changing runtime behavior. #101666 Thanks @vincentkoc.

> Reduced accidental internal interfaces across core, plugins, and the Control UI to simplify ongoing maintenance. #101701 Thanks @vincentkoc.

> Strengthened compatibility checks for the bundled Codex integration to catch request mismatches before release. #101726 Thanks @vincentkoc.

> Kept private implementation details from appearing as supported integration points, improving codebase maintainability. #101731 Thanks @vincentkoc.

> Expanded release preflight coverage so official plugin packages can be built and inspected before an extended-stable npm release. #101757 Thanks @kevinslin.

> Reduced unused internal declarations across core, plugins, and the Control UI without changing product behavior. #101758 Thanks @vincentkoc.

> Reduced accidental internal interfaces in bundled extensions without changing plugin behavior. #101860 Thanks @vincentkoc.

> Made plugin tests more portable across common developer and hosted environments. #101896

> Clarified the browser plugin's supported surface by keeping implementation details private. #101898 Thanks @vincentkoc.

> Clarified Microsoft Teams plugin boundaries by keeping private implementation details internal. #101903 Thanks @vincentkoc.

> Clarified internal boundaries in the ClickClack and Logbook plugins without changing their behavior. #101922 Thanks @vincentkoc.

> Clarified the iMessage plugin's internal boundaries without changing its capabilities or behavior. #101936 Thanks @vincentkoc.

> Clarified which Feishu integration details are private, making the code easier to maintain. #101949 Thanks @vincentkoc.

> Narrowed Matrix integration internals without changing user behavior or documented configuration. #101954 Thanks @vincentkoc.

> Clarified the WhatsApp integration's supported type surface while preserving messaging behavior. #101959 Thanks @vincentkoc.

> Clarified internal boundaries in the Diffs and File Transfer plugins without changing their behavior. #102021 Thanks @vincentkoc.

> Kept Google Chat implementation details private while preserving all existing integration behavior. #102029 Thanks @vincentkoc.

> Narrowed LINE integration internals without changing messages, webhooks, or configuration. #102037 Thanks @vincentkoc.

> Clarified Mattermost integration boundaries by keeping implementation-only details private. #102040 Thanks @vincentkoc.

> Reduced accidental internal interfaces in the Signal plugin without changing how Signal works. #102042 Thanks @vincentkoc.

> Narrowed Slack plugin internals while preserving messaging and delivery behavior. #102044 Thanks @vincentkoc.

> Clarified QQBot's supported integration surface without changing runtime behavior. #102048 Thanks @vincentkoc.

> Narrowed Zalo integration internals without changing messaging, webhooks, media, or configuration. #102065 Thanks @vincentkoc.

> Restored reliable Codex plugin release validation after its connection records moved to a new storage system. #103467 Thanks @vincentkoc.

> Restored Chinese documentation validation for Meta provider and plugin reference pages. #103923

> Backported fixes for startup recovery, Discord reconnection, readable refusal messages, and lighter plugin listing. #104794 Thanks @wuqxuan.

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
- [[Changes/OpenClaw/2026-07-13-8-search-and-browsing-changes-in-v2026-7-1|8 Search and Browsing changes in v2026.7.1]] · Search and Browsing
- [[Changes/OpenClaw/2026-07-13-20-collaboration-changes-in-v2026-7-1|20 Collaboration changes in v2026.7.1]] · Collaboration
- [[Changes/OpenClaw/2026-07-13-13-files-and-data-changes-in-v2026-7-1|13 Files and Data changes in v2026.7.1]] · Files and Data
- [[Changes/OpenClaw/2026-07-13-19-multimodal-input-changes-in-v2026-7-1|19 Multimodal Input changes in v2026.7.1]] · Multimodal Input
- [[Changes/OpenClaw/2026-07-13-38-reliability-and-performance-changes-in-v2026-7-1|38 Reliability and Performance changes in v2026.7.1]] · Reliability and Performance
- [[Changes/OpenClaw/2026-07-13-686-other-changes-in-v2026-7-1|686 other changes in v2026.7.1]] · Other changes
- [[Changes/OpenClaw/2026-07-13-official-openclaw-container-images-are-now-available-from-docker-hub-as-well-as|Official OpenClaw container images are now available from Docker Hub as well…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-07-13 · Lovable · [[Changes/Lovable/2026-07-13-let-your-app-s-users-connect-their-own-accounts|Let your app's users connect their own accounts]]
- Later: 2026-07-14 · Claude Code · [[Changes/Claude Code/2026-07-14-3-apps-and-integrations-changes-in-v2-1-208|3 Apps and Integrations changes in v2.1.208]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-07-13-d95cc3&body=Card%3A%20Changes%2FOpenClaw%2F2026-07-13-213-apps-and-integrations-changes-in-v2026-7-1.md%0ACard%20ID%3A%20openclaw-2026-07-13-d95cc3%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.7.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->