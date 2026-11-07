---
card_id: openclaw-2026-07-13-6e3705
date: '2026-07-13'
description: 'OpenClaw · 2026-07-13 · Model Support: 130 changes in v2026.7.1 — OpenClaw
  v2026.7.1 brings major Control UI and onboarding overhauls, major updates to the…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1281
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 39a5f4dceca8e981506c2f66a9baeb1c660d281088d305b28758e8af364b7697
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-07-13-6e3705
  comparison: ''
  date: '2026-07-13'
  description: 'OpenClaw — v2026.7.1: 130 Model Support changes'
  evidence:
  - quote: OpenClaw v2026.7.1 brings major Control UI and onboarding overhauls, major
      updates to the official iOS, Android, and macOS apps, expanded model and provider
      support including GPT-5.6 compatibility, Tencent Hy3, and Meta Muse Spark 1.1,
      and stronger Codex and connected coding-agent workflows. Telegram, Slack, Discord,
      and Apple Messages each receive substantial updates, while Gateway crash loops,
      scheduled work, remote browser control, workspace terminals, sessions, and goals
      also improve. There are also many general fixes and refinements throughout OpenClaw.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'WebChat now shows long provider and model names together with the selected
      reasoning level in the composer, while narrow screens retain a sensible overflow
      limit. #96990 Thanks @maweibin, @xiayingren123.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The Control UI composer now shows reasoning level clearly, keeps Talk
      and its settings together, and preserves usable model controls on phone and
      landscape layouts. #100445'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Control UI Talk now starts from a simpler composer while administrators
      can set durable provider, transport, timing, and reasoning defaults in Settings.
      #100453'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Onboarding now offers clearer paths to a usable first chat. Fresh CLI installs
      enter guided setup, configured installs open the TUI, and conversational Crestodian
      setup remains optional. Android and macOS guide users through pairing , permissions,
      local or remote setup, and recovery; macOS can also test detected Claude Code,
      Codex, Gemini CLI, API-key, and supported provider-catalog choices before saving
      them. Interrupted authentication or channel setup retains earlier choices, while
      users without a working model are guided through credential and model selection
      instead of being sent into an unusable chat. Owners and administrators can also
      renew an expired Codex or OpenAI login through private Telegram, Web UI, Discord,
      or Slack commands without SSH access.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'openclaw doctor --fix now preserves aliases, parameters, streaming choices,
      runtime settings, and other model tuning when several retired model names merge
      into one current model, and reports any merge conflicts accurately. #96544 Thanks
      @vincentkoc, @yetval.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Crestodian setup now guides users who lack a usable model provider through
      masked credential entry and model selection, while deterministic setup and repair
      commands remain available until inference is configured. #101887 Thanks @fuller-stack-dev.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Organizations with GPT-5.6 preview access can select Sol, Terra, or Luna
      through supported OpenAI and Codex routes with the expected context metadata,
      text and image input, reasoning levels, and cache-write accounting when OpenAI
      supplies it. Fresh OpenAI API-key and ChatGPT/Codex setups choose their intended
      GPT-5.6 defaults without replacing an explicit model choice. Supported Ultra
      choices remain aligned across OpenClaw and native Codex, and Codex supervision
      records native Codex child agents as tasks and returns their results to the
      parent.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Claude Sonnet 5 is selectable through direct Anthropic, Claude CLI, supported
      Vertex regions, Bedrock inference profiles, and Bedrock Mantle with its documented
      context, output, image, thinking, and pricing behavior. Users with Claude Mythos
      5 access can select it through supported Anthropic-family routes with its required
      context, output, adaptive-thinking, caching, and replay behavior.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Copilot sessions can explicitly use supported custom OpenAI, Azure OpenAI,
      Ollama-compatible, or Anthropic providers and start a compatible session when
      connection or credential settings change. Paired computers can run short tasks
      on eligible local Ollama models, while ClawRouter can expose the models granted
      to one managed key and report their usage and budget. Users can also claim active
      promotional models without replacing existing defaults, install LongCat-2.0
      through its official provider, and continue Gemini latest tool-calling conversations
      across both supported Google transports.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Copilot sessions can now use explicitly selected custom OpenAI, Azure
      OpenAI, Ollama-compatible, or Anthropic providers and restart cleanly when model,
      endpoint, credentials, headers, or token limits change. #96345 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'GPT-5.6 users can now select supported Ultra modes consistently, keep
      model and thinking choices aligned across OpenClaw surfaces, and receive native
      Codex child-agent results as tracked tasks. #98021 Thanks @anyech.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Claude Sonnet 5 is now selectable across Anthropic, Claude CLI, supported
      Vertex regions, Bedrock inference profiles, and Bedrock Mantle with its documented
      context, output, image, thinking, and pricing behavior. #98254 Thanks @vortexopenclaw.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Organizations with GPT-5.6 preview access can select Sol, Terra, or Luna
      across supported OpenAI and Codex paths with correct reasoning controls, context
      metadata, and cache-write accounting. #98333 Related #98296 . Thanks @steipete-oai.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Users can discover active promotional models and claim them with openclaw
      promos claim &lt;slug&gt; without rerunning onboarding or unexpectedly replacing
      existing defaults and credentials. #100236 Thanks @fuller-stack-dev.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Gemini latest aliases now continue tool-calling conversations across both
      supported Google transports instead of stopping with a missing-thought-signature
      HTTP 400. #100605 Thanks @chenxiaoyu209, @guarismo.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Legacy-state upgrades no longer stall repeatedly, while fresh OpenAI and
      ChatGPT/Codex setups select the intended GPT-5.6 defaults and use supported
      temperature and tool-call behavior. #104656 Thanks @bdjben, @obviyus, @sallyom.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Telegram received broad work across live progress, media, documents, topics,
      commands, retries, account routing, setup, and delivery. Albums reach the model
      with every available image, long replies remain easier to follow while they
      run, and temporary conflicts or network failures are less likely to block later
      messages or create duplicates.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Telegram photo albums now give the model every successfully downloaded
      image in order instead of only one photo and unusable file references, while
      failed items are omitted. #97045 Thanks @nianjiuzst, @obviyus.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Discord now shows enabled Anthropic reasoning, notes, and tool activity
      in the right order with accurate counters and nonblank summaries. #96106 Thanks
      @marvinthebored, @obviyus, @peetiegonzalez.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Signal users now receive clean assistant replies without internal tool
      status, reasoning tags, or tool-call markup. #97360 Thanks @masatohoshino.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Matrix replies now deliver the intended answer without leaking internal
      tool diagnostics, reasoning tags, or assistant-only scaffolding. #97372 Thanks
      @masatohoshino.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Punctuation around a model''s NO_REPLY token no longer turns it into a
      visible chat message, while legitimate messages containing the token still arrive.
      #98224 Thanks @sunnyshu0925.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Telegram replies retain literal wording such as &lt;think&gt; when it
      is part of the answer, while genuinely marked reasoning remains hidden. #97286
      Thanks @drickon, @obviyus.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Text commands such as /model fable now reliably display their confirmation
      even in flows that suppress ordinary source replies. #100151'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Telegram users with /reasoning on now receive the model''s saved reasoning
      messages alongside the final answer. #97875 Thanks @fuller-stack-dev, @marvinthebored.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The bare /think command now shows available thinking levels promptly in
      Telegram, Slack, and Discord without waiting on slow model discovery. #101926
      Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Across Anthropic and Claude, Gemini, OpenAI and Codex, local models, and
      other supported routes, providers now handle credentials, catalogs, limits,
      fallbacks, streaming, and tool calls more consistently. Readers should see fewer
      requests fail because the selected route used the wrong model metadata, replayed
      incompatible reasoning, lost authentication state, or interpreted a provider
      response incorrectly.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: The model catalog also reports availability and capability more accurately,
      while Codex supervision keeps connected model choices and session behavior aligned
      with the backend that was actually selected.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'OpenCode Zen users can browse and run its supported Claude, GPT, Gemini,
      GLM, DeepSeek, MiniMax, Qwen, and other models without manually defining each
      route. #92495 Thanks @mushuiyu886, @sallyom.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Amazon Bedrock adaptive-thinking Claude and Fable runs now honor configured
      high output-token limits for longer answers, reasoning, and tool calls. #97343
      Thanks @lilan0125, @prasithg.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Claude CLI users can combine multiple --mcp-config files without losing
      servers or corrupting the prompt, and concurrent Gemini CLI runs are less likely
      to interfere with shared credential files. #98983 Related #98944 , #98945 .
      Thanks @obviyus.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Anthropic Opus 4.8 can now run with tools.profile=coding without every
      turn failing with an HTTP 400 schema error before the assistant replies. #100492
      Thanks @lin-hongkuan, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Gemini streaming can retry with another configured API key after a retryable
      quota or rate-limit response instead of failing on the first key. #97328 Thanks
      @monkeyleet.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Gemini memory-embedding batch uploads, creation, and status checks now
      fail safely when a compatible endpoint returns an oversized control response.
      #97535 Thanks @hugenshen.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Google Gemini CLI sign-in now rejects oversized OAuth, profile, project,
      and onboarding responses with labeled errors instead of risking excessive memory
      use. #97587 Thanks @hugenshen.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Google Gemini CLI OAuth failures now keep oversized or malformed provider
      responses bounded while preserving useful error details. #99605 Thanks @mushuiyu886.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'openclaw models list now reports configured local Ollama models as available
      when they are running and usable. #97491 Thanks @lingfeizi, @qingminglong.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Rerunning provider onboarding or refreshing models now preserves operator-owned
      timeouts, transport settings, MiniMax models, and SecretRef credentials instead
      of silently erasing them. #100107 Thanks @frank-beans.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Ollama requests whose native response stream ends early can now continue
      to a configured fallback model instead of stopping with LLM request failed .
      #100482 Thanks @turbotheturtle.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'OpenAI-compatible Chat Completions now use OpenClaw''s guarded network
      path, adding the same response safety controls used by other protected model
      calls. #97228 Thanks @vincentkoc, @wangmiao0668000666.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'GPT-5.5 and other models can send valid streaming events larger than 64
      KiB through ChatGPT Responses without failing the request, while malformed unbounded
      streams remain limited. #98198 Thanks @marvinthebored, @obviyus, @peetiegonzalez.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Custom Xiaomi MiMo and other OpenAI-compatible models without a known output
      limit can now complete chats instead of failing with an invented oversized cap.
      00a8dae Thanks @peole, @sanjays2402.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: The managed Codex harness now surfaces supported GPT-5.6 Sol, Terra, and
      Luna models returned by the account catalog and gives self-managed users current
      version guidance. f80ce21 Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Bundled provider aliases now accept supported overlay settings such as
      request timeouts without demanding custom-provider fields like baseUrl and models
      . #88400 Thanks @pluviobyte.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Switching from thinking-off mode to a reasoning-required model now selects
      its lowest supported effort rather than silently choosing the most expensive
      level. #93335 Thanks @obuchowski.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'MiniMax M3 replies, including those routed through Fireworks, no longer
      expose hidden mm: reasoning in visible chat or progress output. #93767 Thanks
      @drhack1, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Hidden MiniMax reasoning no longer appears as a new iMessage or feeds
      back into the conversation as an echo-triggering inbound message. #93820 Thanks
      @alix-007.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Embedded-agent runs can now try the next configured fallback model after
      a temporary upstream LLM request failed error. #95542 Thanks @altaywtf, @mikasa0818.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'LM Studio model discovery and startup now stop pathological server responses
      at a fixed size and report a clear error instead of buffering them indefinitely.
      #96042 Thanks @alix-007.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Model aliases and partial names such as opus now resolve to the newest
      matching version even when catalogs reach double-digit versions, preventing
      silent routing to an older model. #96609 Thanks @yetval, @zw-xysk.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Paginated provider catalogs now expose models beyond the first page, while
      malformed, endless, or redirected catalogs fail safely instead of caching an
      incomplete list or forwarding sensitive headers across origins. #97012 Thanks
      @zhangguiping-xydt.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Long opencode-go model runs are less likely to be falsely stopped as stalled
      while valid provider events are still arriving. #97128 Thanks @liuwqgit, @vincentkoc,
      @yetval.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'OpenRouter''s DeepSeek V4 Flash and Pro models can answer with thinking
      enabled without failing with an HTTP 400. #97208 Related #97196 . Thanks @nianjiuzst,
      @patelmm79.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Proxy-backed model streams now fail with bounded, clearer errors when
      responses are oversized, malformed, incomplete, or idle instead of hanging or
      consuming unbounded data. #97235 Thanks @vincentkoc, @zhangguiping-xydt.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Configured fallback chains now try an alternate model when the primary
      provider reports model_not_found , reducing failures after model availability
      changes. #97571 Thanks @liuhao1024.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'When a configured runtime model is no longer available, chat now explains
      that a new session will not help and directs operators to choose an available
      model. #97611 Thanks @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Automatically configured video understanding now uses provider defaults
      such as Moonshot''s intended video model unless the user selected a model explicitly.
      #99791 Thanks @vincentkoc, @zhangguiping-xydt.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Direct mistral-medium-3-5 requests now send the user-selected adjustable
      reasoning level to Mistral as reasoningEffort . #100688 Thanks @aniruddhaadak80,
      @wm0018.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Featherless AI now has an official provider install and onboarding path,
      including FEATHERLESS_API_KEY , a curated featherless/Qwen/Qwen3-32B default,
      and support for exact Featherless model IDs. #101092 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Meta Model API is now exposed through the public meta provider, with meta/muse-spark-1.1
      , canonical provider docs, and standalone npm or ClawHub installation paths.
      #103070 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Trusted official external providers can now show model-specific thinking
      choices before full runtime activation, including off, low, high, and max for
      Z.AI GLM 5.2. b4fce16 Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Eligible direct API-key requests to Claude Fable 5 now return an Opus
      4.8 answer when Anthropic''s safety classifier declines Fable, with diagnostics
      and Opus billing made clear. #99906'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Anthropic-compatible model requests now consistently use OpenClaw''s guarded
      transport, response normalization, and managed stream cleanup rather than bypassing
      them through the SDK. #101357 Thanks @wangmiao0668000666.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Gemini CLI media analysis now returns its description even when the valid
      response also contains nested usage or other metadata. #96432 Thanks @lin-hongkuan.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Status summaries now respect provider-local model aliases, showing the
      selected alias without a false pinned-model mismatch warning. 1d4e789
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Legacy openai-codex references now direct operators to openclaw doctor
      --fix and openclaw models status instead of suggesting configuration that fails
      validation. #100120 Thanks @jason-vaughan, @sunnyshu0925, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Continued conversations with strict custom OpenAI Responses-compatible
      endpoints no longer fail on an unsupported input[n].status field and needlessly
      switch to a fallback model. #100831 Thanks @chenxiaoyu209.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Codex sessions using gpt-5.5-pro or gpt-5.4-pro now clamp unsupported
      reasoning levels before the first turn, avoiding an immediate request rejection
      when live metadata is unavailable. #101484 Thanks @zhangguiping-xydt.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'When an OpenAI or OpenAI-compatible chat-completions model refuses a request,
      users now see the provider''s explanation instead of a blank assistant reply.
      #102344 Thanks @wuqxuan, @yetval.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Model-call traces now include prompt-size and per-call token usage details,
      helping operators investigate cost and prompt growth without capturing raw content.
      #95770 Thanks @amknight.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: '/model default now actually returns an active session to its configured
      model after steering, fallback, or a previous manual selection. #96318 Thanks
      @marsman-lab, @sunnyshu0925.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Media-generation catalogs now keep the correct default model marker even
      when provider metadata includes harmless surrounding whitespace. #96430 Thanks
      @lin-hongkuan.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Reference-image edits through Fal-hosted Grok Imagine and Nano Banana
      2 Lite now reach the correct service, while mixed-model fallbacks honor each
      candidate''s supported resolution and reference limits. #98688 Thanks @davenicoll,
      @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Switching a live Control UI or TUI session through a provider-qualified
      model alias now saves the canonical provider and model, preventing the next
      request from being rejected. #100209 Thanks @sahilsatralkar.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'openclaw status and session_status now identify when a session is using
      a fallback model and show the configured primary model beside it. #101337 Thanks
      @lzy3538.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'OAuth-backed models now become available in Gateway model browsing after
      credentials are renewed from another CLI process, without requiring a Gateway
      restart. #104732 Thanks @fuller-stack-dev.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: The diagnostics timeline now shows when provider model calls ran, how long
      they took, and whether they succeeded without recording prompt or response content.
      7253552 Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Inferred follow-up commitments now return to the queue after temporary
      model or network extraction failures, reducing missed reminders without duplicate
      processing. #89817 Thanks @masatohoshino.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Long-running gateways can clear stale one-shot model-check sessions before
      they crowd out real conversation history, with dedicated CLI reporting for review.
      #91057 Thanks @jalehman, @wangwllu.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Messages mixing inline and offloaded images now preserve every attachment
      position so model instructions that depend on sequence remain accurate. #99902
      Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Local-model conversations now retain reusable prompt work when switching
      between interactive chats and background jobs, avoiding repeated multi-minute
      warm-up delays. #98267 Related #98261 . Thanks @headbouyjb.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Gateway startup now skips unnecessary provider thinking-policy work when
      an explicit setting or model catalog already determines the banner result. b18af41
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Model-provider keys stored with SecretRefs now receive additional protection
      against accidental exposure in logs, errors, proxy captures, SDK setup, and
      runtime inspection, with a compatibility switch for secret sentinels. #102009'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Failed OpenAI or Codex credential refreshes now report that reauthentication
      is required and privately identify the affected profile instead of appearing
      healthy until model turns fail. #99134 Related #99120 . Thanks @100yenadmin,
      @fuller-stack-dev.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Swift native clients now support device-scoped skill approvals, with the
      reviewer-device field encoded in their generated Gateway models. 1403c64
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Anthropic and Gemini PDF analysis now blocks unsafe private-network redirects
      and oversized responses by default while still supporting configured local endpoints.
      #97872 Thanks @eleqtrizit.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android hides thinking controls for models that do not support configurable
      reasoning, prevents unsupported settings from breaking live or queued sends,
      and restores the user''s preference on compatible models. #101002'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android model organization, default-model, and pinning controls now use
      the selected language. Sources: 41bea62 , bdc98f4 .'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android users can switch the current chat''s model from the composer,
      pin favorites, revisit recent choices, and return to the default without leaving
      the conversation; older pairings may need to be renewed. #100798'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Typing indicators now remain active during long Codex model, tool, command,
      recovery, and queued follow-up work instead of making the reply appear idle.
      #95844 Thanks @jalehman.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'iOS chat now shows and switches the active model, while iOS and macOS
      model pickers support pinned favorites and the five most recent choices. #100774'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'iOS and macOS hide the thinking-level control for models that cannot use
      it, avoid sending stale unsupported settings, and restore the previous level
      when a reasoning-capable model is selected again. #100875'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Custom usage footers now render alias and map fallbacks correctly even
      when model or mode names collide with properties such as toString or constructor
      . #98503 Related #98466 . Thanks @chenyangjun-xy, @zhanglei99586.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'openclaw tui --local now explains when a known slash command requires
      the Gateway instead of sending that command to the model as an unwanted prompt.
      #100188 Thanks @goslingmanagment.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The opt-in Logbook lets users review a model-organized workday timeline,
      generate standups, and ask questions about captured activity, with owner-only
      local storage and configurable retention. #99930'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Non-interactive openclaw models list and openclaw models status now exit
      normally after printing their results, allowing scripts and SSH diagnostics
      to finish without an external timeout. #77904 Thanks @dorukardahan, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Removing a visible built-in model alias now explains that the alias is
      automatic and shows how to shadow it, while genuinely absent aliases still report
      as not found. #81641 Thanks @scientificprogrammer, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Session logs and cached cost views now preserve provider-reconciled zero-dollar
      totals while recalculating genuinely missing costs from stored provider and
      model details. c45124a
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'A focused tool-result-cap Doctor lint check now identifies settings below
      model-aware defaults or above the runtime ceiling with actionable paths. #97500
      Thanks @giodl73-repo.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Crestodian on Claude Code or Gemini CLI can now hold multi-turn setup
      conversations, inspect state, request exact approval for changes, and verify
      writes instead of falling back immediately to a single-turn planner. #100029'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Crestodian now distinguishes ordinary questions from operational requests,
      accepts natural approval phrases, clears stale proposals, and keeps sensitive
      configuration out of the conversation model. #100656'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Langfuse, OpenTelemetry, and Prometheus can now capture usage, cost, model,
      provider, timing, and session data for runs started through /v1/responses and
      /v1/chat/completions . #96152 Thanks @rocke2020, @xialonglee.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Windows users can launch globally installed Gemini CLI and Claude Code
      backends through their npm command shims without immediate spawn failures or
      mangled prompt arguments. #101378 Thanks @wendy-chsy.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The agent configuration guide now identifies the current models selected
      by the built-in opus and gpt aliases. #96375 Thanks @niks999.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'A scheduled cloud-model job that opens a response but sends no content
      can now move to a healthy fallback model before the entire run times out. #96096
      Thanks @849261680, @velvet-shark.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'openclaw infer image describe now tries configured fallback image models
      after an explicitly selected model fails and reports which model ultimately
      succeeded. #98347 Thanks @momothemage.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Failed code-mode tool attempts now show the error type, message, and location,
      giving the model and operator enough detail to diagnose or correct the problem.
      #95906 Thanks @vincentkoc, @zengwen-dt.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Link understanding now keeps page fetching available for the slowest configured
      fallback and applies tools.links.timeoutSeconds consistently regardless of model
      order. #100731 Thanks @aniruddhaadak80, @cxbasdev.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Multi-attachment prompts now keep real captions while removing duplicate
      transport markers and placeholder-only text that could confuse the model. #96431
      Thanks @lin-hongkuan.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Strengthened coverage for binding Codex conversations without an explicit
      model, protecting the default workflow from regressions. #89535 Thanks @kesslerio.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Clarified internal fallback behavior so future maintenance is less likely
      to mishandle provider errors or older model responses. #89558'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Strengthened coverage so GitHub Copilot reasoning choices stay aligned
      with each account''s supported models. #91728 Thanks @saju01.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Reduced live-test disk usage by avoiding unnecessary copies of large Gemini
      browser data while preserving required credentials. #91907 Thanks @bryantegomoh,
      @pikaqqqqqq.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Prepared session status and model selection for future storage changes
      while preserving current behavior. #96460 Thanks @jalehman.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Prepared Feishu previews and Mattermost model summaries for future session-storage
      changes without changing behavior. #96507 Thanks @jalehman.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Prepared bundled channel session handling for future storage changes without
      altering routing, model choices, or user workflows. #96527 Thanks @jalehman.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Gave Claude CLI QA runs the appropriate longer time limits for Sonnet
      and Opus models. #96567 Thanks @clawsean.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Simplified maintenance of the paired BytePlus and Volcengine model catalogs
      without changing provider behavior. #99777 Thanks @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Reduced unnecessary setup work for models that cannot use tools while
      preserving existing tool-enabled workflows. #100536 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Added release coverage for corrected model labels and durable inbound-image
      previews in the Control UI. #100740 Thanks @hyspacex, @sweetcornna.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Strengthened regression coverage for setting up Hugging Face local apps
      with compatible local model servers. #100887 Thanks @osolmaz.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Removed an obsolete Android cache-cleanup path, leaving one clearer ownership
      model. #101470 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Added consistent OpenClaw identification to requests sent through the
      official Google Gemini API. #101834 Thanks @vishal-dharm.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Updated Meta provider validation and guidance for the deployed Muse Spark
      1.1 model. #103163'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Aligned plugin prerelease validation with the current GPT-5.6 model defaults.
      #104722'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Updated live-provider validation to use the intended July GPT-5.6 model
      by default. #104750'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Reduced false GPT-5.6 release-validation failures by retrying a small
      set of incorrect validation responses. #104939'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Made Telegram release validation work reliably with model selections from
      older compatible candidates. #105401'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Improved Codex model-switch validation so conversation compaction no longer
      causes a false failure. #105493'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 130-model-support-changes-in-v2026-7-1
  source_release: openclaw-2026-07-13-v2026-7-1-c2063718
  source_type: openclaw_changelog
  theme: model-support
  title: 130 Model Support changes in v2026.7.1
  type: change
related_changes:
- '[[Changes/Claude Code/2026-07-11-changed-bedrock-vertex-and-claude-platform-on-aws-to-default-to-claude-opus-4-8|Changed
  Bedrock, Vertex, and Claude Platform on AWS to default to Claude Opus 4.8]]'
- '[[Changes/Cline/2026-07-11-add-more-models-to-the-gcp-vertex-provider-plus-a-free-form-entry-option-in-the|Add
  more models to the GCP Vertex provider, plus a free-form entry option…]]'
- '[[Changes/Kimi Code/2026-07-12-3-model-support-changes-in-kimi-code-0-23-6|3 Model
  Support changes in Kimi Code 0.23.6]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-07-13-v2026-7-1-c2063718|openclaw-2026-07-13-v2026-7-1-c2063718]]'
source_type: openclaw_changelog
theme: model-support
title: 130 Model Support changes in v2026.7.1
type: change
---

<!-- chronolog:begin region="header" -->
# 130 Model Support changes in v2026.7.1

**OpenClaw** · 2026-07-13 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.7.1) · from [[Releases/OpenClaw/openclaw-2026-07-13-v2026-7-1-c2063718|v2026.7.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> OpenClaw v2026.7.1 brings major Control UI and onboarding overhauls, major updates to the official iOS, Android, and macOS apps, expanded model and provider support including GPT-5.6 compatibility, Tencent Hy3, and Meta Muse Spark 1.1, and stronger Codex and connected coding-agent workflows. Telegram, Slack, Discord, and Apple Messages each receive substantial updates, while Gateway crash loops, scheduled work, remote browser control, workspace terminals, sessions, and goals also improve. There are also many general fixes and refinements throughout OpenClaw.

> WebChat now shows long provider and model names together with the selected reasoning level in the composer, while narrow screens retain a sensible overflow limit. #96990 Thanks @maweibin, @xiayingren123.

> The Control UI composer now shows reasoning level clearly, keeps Talk and its settings together, and preserves usable model controls on phone and landscape layouts. #100445

> Control UI Talk now starts from a simpler composer while administrators can set durable provider, transport, timing, and reasoning defaults in Settings. #100453

> Onboarding now offers clearer paths to a usable first chat. Fresh CLI installs enter guided setup, configured installs open the TUI, and conversational Crestodian setup remains optional. Android and macOS guide users through pairing , permissions, local or remote setup, and recovery; macOS can also test detected Claude Code, Codex, Gemini CLI, API-key, and supported provider-catalog choices before saving them. Interrupted authentication or channel setup retains earlier choices, while users without a working model are guided through credential and model selection instead of being sent into an unusable chat. Owners and administrators can also renew an expired Codex or OpenAI login through private Telegram, Web UI, Discord, or Slack commands without SSH access.

> openclaw doctor --fix now preserves aliases, parameters, streaming choices, runtime settings, and other model tuning when several retired model names merge into one current model, and reports any merge conflicts accurately. #96544 Thanks @vincentkoc, @yetval.

> Crestodian setup now guides users who lack a usable model provider through masked credential entry and model selection, while deterministic setup and repair commands remain available until inference is configured. #101887 Thanks @fuller-stack-dev.

> Organizations with GPT-5.6 preview access can select Sol, Terra, or Luna through supported OpenAI and Codex routes with the expected context metadata, text and image input, reasoning levels, and cache-write accounting when OpenAI supplies it. Fresh OpenAI API-key and ChatGPT/Codex setups choose their intended GPT-5.6 defaults without replacing an explicit model choice. Supported Ultra choices remain aligned across OpenClaw and native Codex, and Codex supervision records native Codex child agents as tasks and returns their results to the parent.

> Claude Sonnet 5 is selectable through direct Anthropic, Claude CLI, supported Vertex regions, Bedrock inference profiles, and Bedrock Mantle with its documented context, output, image, thinking, and pricing behavior. Users with Claude Mythos 5 access can select it through supported Anthropic-family routes with its required context, output, adaptive-thinking, caching, and replay behavior.

> Copilot sessions can explicitly use supported custom OpenAI, Azure OpenAI, Ollama-compatible, or Anthropic providers and start a compatible session when connection or credential settings change. Paired computers can run short tasks on eligible local Ollama models, while ClawRouter can expose the models granted to one managed key and report their usage and budget. Users can also claim active promotional models without replacing existing defaults, install LongCat-2.0 through its official provider, and continue Gemini latest tool-calling conversations across both supported Google transports.

> Copilot sessions can now use explicitly selected custom OpenAI, Azure OpenAI, Ollama-compatible, or Anthropic providers and restart cleanly when model, endpoint, credentials, headers, or token limits change. #96345 Thanks @vincentkoc.

> GPT-5.6 users can now select supported Ultra modes consistently, keep model and thinking choices aligned across OpenClaw surfaces, and receive native Codex child-agent results as tracked tasks. #98021 Thanks @anyech.

> Claude Sonnet 5 is now selectable across Anthropic, Claude CLI, supported Vertex regions, Bedrock inference profiles, and Bedrock Mantle with its documented context, output, image, thinking, and pricing behavior. #98254 Thanks @vortexopenclaw.

> Organizations with GPT-5.6 preview access can select Sol, Terra, or Luna across supported OpenAI and Codex paths with correct reasoning controls, context metadata, and cache-write accounting. #98333 Related #98296 . Thanks @steipete-oai.

> Users can discover active promotional models and claim them with openclaw promos claim &lt;slug&gt; without rerunning onboarding or unexpectedly replacing existing defaults and credentials. #100236 Thanks @fuller-stack-dev.

> Gemini latest aliases now continue tool-calling conversations across both supported Google transports instead of stopping with a missing-thought-signature HTTP 400. #100605 Thanks @chenxiaoyu209, @guarismo.

> Legacy-state upgrades no longer stall repeatedly, while fresh OpenAI and ChatGPT/Codex setups select the intended GPT-5.6 defaults and use supported temperature and tool-call behavior. #104656 Thanks @bdjben, @obviyus, @sallyom.

> Telegram received broad work across live progress, media, documents, topics, commands, retries, account routing, setup, and delivery. Albums reach the model with every available image, long replies remain easier to follow while they run, and temporary conflicts or network failures are less likely to block later messages or create duplicates.

> Telegram photo albums now give the model every successfully downloaded image in order instead of only one photo and unusable file references, while failed items are omitted. #97045 Thanks @nianjiuzst, @obviyus.

> Discord now shows enabled Anthropic reasoning, notes, and tool activity in the right order with accurate counters and nonblank summaries. #96106 Thanks @marvinthebored, @obviyus, @peetiegonzalez.

> Signal users now receive clean assistant replies without internal tool status, reasoning tags, or tool-call markup. #97360 Thanks @masatohoshino.

> Matrix replies now deliver the intended answer without leaking internal tool diagnostics, reasoning tags, or assistant-only scaffolding. #97372 Thanks @masatohoshino.

> Punctuation around a model's NO_REPLY token no longer turns it into a visible chat message, while legitimate messages containing the token still arrive. #98224 Thanks @sunnyshu0925.

> Telegram replies retain literal wording such as &lt;think&gt; when it is part of the answer, while genuinely marked reasoning remains hidden. #97286 Thanks @drickon, @obviyus.

> Text commands such as /model fable now reliably display their confirmation even in flows that suppress ordinary source replies. #100151

> Telegram users with /reasoning on now receive the model's saved reasoning messages alongside the final answer. #97875 Thanks @fuller-stack-dev, @marvinthebored.

> The bare /think command now shows available thinking levels promptly in Telegram, Slack, and Discord without waiting on slow model discovery. #101926 Thanks @vincentkoc.

> Across Anthropic and Claude, Gemini, OpenAI and Codex, local models, and other supported routes, providers now handle credentials, catalogs, limits, fallbacks, streaming, and tool calls more consistently. Readers should see fewer requests fail because the selected route used the wrong model metadata, replayed incompatible reasoning, lost authentication state, or interpreted a provider response incorrectly.

> The model catalog also reports availability and capability more accurately, while Codex supervision keeps connected model choices and session behavior aligned with the backend that was actually selected.

> OpenCode Zen users can browse and run its supported Claude, GPT, Gemini, GLM, DeepSeek, MiniMax, Qwen, and other models without manually defining each route. #92495 Thanks @mushuiyu886, @sallyom.

> Amazon Bedrock adaptive-thinking Claude and Fable runs now honor configured high output-token limits for longer answers, reasoning, and tool calls. #97343 Thanks @lilan0125, @prasithg.

> Claude CLI users can combine multiple --mcp-config files without losing servers or corrupting the prompt, and concurrent Gemini CLI runs are less likely to interfere with shared credential files. #98983 Related #98944 , #98945 . Thanks @obviyus.

> Anthropic Opus 4.8 can now run with tools.profile=coding without every turn failing with an HTTP 400 schema error before the assistant replies. #100492 Thanks @lin-hongkuan, @vincentkoc.

> Gemini streaming can retry with another configured API key after a retryable quota or rate-limit response instead of failing on the first key. #97328 Thanks @monkeyleet.

> Gemini memory-embedding batch uploads, creation, and status checks now fail safely when a compatible endpoint returns an oversized control response. #97535 Thanks @hugenshen.

> Google Gemini CLI sign-in now rejects oversized OAuth, profile, project, and onboarding responses with labeled errors instead of risking excessive memory use. #97587 Thanks @hugenshen.

> Google Gemini CLI OAuth failures now keep oversized or malformed provider responses bounded while preserving useful error details. #99605 Thanks @mushuiyu886.

> openclaw models list now reports configured local Ollama models as available when they are running and usable. #97491 Thanks @lingfeizi, @qingminglong.

> Rerunning provider onboarding or refreshing models now preserves operator-owned timeouts, transport settings, MiniMax models, and SecretRef credentials instead of silently erasing them. #100107 Thanks @frank-beans.

> Ollama requests whose native response stream ends early can now continue to a configured fallback model instead of stopping with LLM request failed . #100482 Thanks @turbotheturtle.

> OpenAI-compatible Chat Completions now use OpenClaw's guarded network path, adding the same response safety controls used by other protected model calls. #97228 Thanks @vincentkoc, @wangmiao0668000666.

> GPT-5.5 and other models can send valid streaming events larger than 64 KiB through ChatGPT Responses without failing the request, while malformed unbounded streams remain limited. #98198 Thanks @marvinthebored, @obviyus, @peetiegonzalez.

> Custom Xiaomi MiMo and other OpenAI-compatible models without a known output limit can now complete chats instead of failing with an invented oversized cap. 00a8dae Thanks @peole, @sanjays2402.

> The managed Codex harness now surfaces supported GPT-5.6 Sol, Terra, and Luna models returned by the account catalog and gives self-managed users current version guidance. f80ce21 Thanks @vincentkoc.

> Bundled provider aliases now accept supported overlay settings such as request timeouts without demanding custom-provider fields like baseUrl and models . #88400 Thanks @pluviobyte.

> Switching from thinking-off mode to a reasoning-required model now selects its lowest supported effort rather than silently choosing the most expensive level. #93335 Thanks @obuchowski.

> MiniMax M3 replies, including those routed through Fireworks, no longer expose hidden mm: reasoning in visible chat or progress output. #93767 Thanks @drhack1, @vincentkoc.

> Hidden MiniMax reasoning no longer appears as a new iMessage or feeds back into the conversation as an echo-triggering inbound message. #93820 Thanks @alix-007.

> Embedded-agent runs can now try the next configured fallback model after a temporary upstream LLM request failed error. #95542 Thanks @altaywtf, @mikasa0818.

> LM Studio model discovery and startup now stop pathological server responses at a fixed size and report a clear error instead of buffering them indefinitely. #96042 Thanks @alix-007.

> Model aliases and partial names such as opus now resolve to the newest matching version even when catalogs reach double-digit versions, preventing silent routing to an older model. #96609 Thanks @yetval, @zw-xysk.

> Paginated provider catalogs now expose models beyond the first page, while malformed, endless, or redirected catalogs fail safely instead of caching an incomplete list or forwarding sensitive headers across origins. #97012 Thanks @zhangguiping-xydt.

> Long opencode-go model runs are less likely to be falsely stopped as stalled while valid provider events are still arriving. #97128 Thanks @liuwqgit, @vincentkoc, @yetval.

> OpenRouter's DeepSeek V4 Flash and Pro models can answer with thinking enabled without failing with an HTTP 400. #97208 Related #97196 . Thanks @nianjiuzst, @patelmm79.

> Proxy-backed model streams now fail with bounded, clearer errors when responses are oversized, malformed, incomplete, or idle instead of hanging or consuming unbounded data. #97235 Thanks @vincentkoc, @zhangguiping-xydt.

> Configured fallback chains now try an alternate model when the primary provider reports model_not_found , reducing failures after model availability changes. #97571 Thanks @liuhao1024.

> When a configured runtime model is no longer available, chat now explains that a new session will not help and directs operators to choose an available model. #97611 Thanks @romneyda.

> Automatically configured video understanding now uses provider defaults such as Moonshot's intended video model unless the user selected a model explicitly. #99791 Thanks @vincentkoc, @zhangguiping-xydt.

> Direct mistral-medium-3-5 requests now send the user-selected adjustable reasoning level to Mistral as reasoningEffort . #100688 Thanks @aniruddhaadak80, @wm0018.

> Featherless AI now has an official provider install and onboarding path, including FEATHERLESS_API_KEY , a curated featherless/Qwen/Qwen3-32B default, and support for exact Featherless model IDs. #101092 Thanks @vincentkoc.

> Meta Model API is now exposed through the public meta provider, with meta/muse-spark-1.1 , canonical provider docs, and standalone npm or ClawHub installation paths. #103070 Thanks @vincentkoc.

> Trusted official external providers can now show model-specific thinking choices before full runtime activation, including off, low, high, and max for Z.AI GLM 5.2. b4fce16 Thanks @vincentkoc.

> Eligible direct API-key requests to Claude Fable 5 now return an Opus 4.8 answer when Anthropic's safety classifier declines Fable, with diagnostics and Opus billing made clear. #99906

> Anthropic-compatible model requests now consistently use OpenClaw's guarded transport, response normalization, and managed stream cleanup rather than bypassing them through the SDK. #101357 Thanks @wangmiao0668000666.

> Gemini CLI media analysis now returns its description even when the valid response also contains nested usage or other metadata. #96432 Thanks @lin-hongkuan.

> Status summaries now respect provider-local model aliases, showing the selected alias without a false pinned-model mismatch warning. 1d4e789

> Legacy openai-codex references now direct operators to openclaw doctor --fix and openclaw models status instead of suggesting configuration that fails validation. #100120 Thanks @jason-vaughan, @sunnyshu0925, @vincentkoc.

> Continued conversations with strict custom OpenAI Responses-compatible endpoints no longer fail on an unsupported input[n].status field and needlessly switch to a fallback model. #100831 Thanks @chenxiaoyu209.

> Codex sessions using gpt-5.5-pro or gpt-5.4-pro now clamp unsupported reasoning levels before the first turn, avoiding an immediate request rejection when live metadata is unavailable. #101484 Thanks @zhangguiping-xydt.

> When an OpenAI or OpenAI-compatible chat-completions model refuses a request, users now see the provider's explanation instead of a blank assistant reply. #102344 Thanks @wuqxuan, @yetval.

> Model-call traces now include prompt-size and per-call token usage details, helping operators investigate cost and prompt growth without capturing raw content. #95770 Thanks @amknight.

> /model default now actually returns an active session to its configured model after steering, fallback, or a previous manual selection. #96318 Thanks @marsman-lab, @sunnyshu0925.

> Media-generation catalogs now keep the correct default model marker even when provider metadata includes harmless surrounding whitespace. #96430 Thanks @lin-hongkuan.

> Reference-image edits through Fal-hosted Grok Imagine and Nano Banana 2 Lite now reach the correct service, while mixed-model fallbacks honor each candidate's supported resolution and reference limits. #98688 Thanks @davenicoll, @vincentkoc.

> Switching a live Control UI or TUI session through a provider-qualified model alias now saves the canonical provider and model, preventing the next request from being rejected. #100209 Thanks @sahilsatralkar.

> openclaw status and session_status now identify when a session is using a fallback model and show the configured primary model beside it. #101337 Thanks @lzy3538.

> OAuth-backed models now become available in Gateway model browsing after credentials are renewed from another CLI process, without requiring a Gateway restart. #104732 Thanks @fuller-stack-dev.

> The diagnostics timeline now shows when provider model calls ran, how long they took, and whether they succeeded without recording prompt or response content. 7253552 Thanks @vincentkoc.

> Inferred follow-up commitments now return to the queue after temporary model or network extraction failures, reducing missed reminders without duplicate processing. #89817 Thanks @masatohoshino.

> Long-running gateways can clear stale one-shot model-check sessions before they crowd out real conversation history, with dedicated CLI reporting for review. #91057 Thanks @jalehman, @wangwllu.

> Messages mixing inline and offloaded images now preserve every attachment position so model instructions that depend on sequence remain accurate. #99902 Thanks @vincentkoc.

> Local-model conversations now retain reusable prompt work when switching between interactive chats and background jobs, avoiding repeated multi-minute warm-up delays. #98267 Related #98261 . Thanks @headbouyjb.

> Gateway startup now skips unnecessary provider thinking-policy work when an explicit setting or model catalog already determines the banner result. b18af41

> Model-provider keys stored with SecretRefs now receive additional protection against accidental exposure in logs, errors, proxy captures, SDK setup, and runtime inspection, with a compatibility switch for secret sentinels. #102009

> Failed OpenAI or Codex credential refreshes now report that reauthentication is required and privately identify the affected profile instead of appearing healthy until model turns fail. #99134 Related #99120 . Thanks @100yenadmin, @fuller-stack-dev.

> Swift native clients now support device-scoped skill approvals, with the reviewer-device field encoded in their generated Gateway models. 1403c64

> Anthropic and Gemini PDF analysis now blocks unsafe private-network redirects and oversized responses by default while still supporting configured local endpoints. #97872 Thanks @eleqtrizit.

> Android hides thinking controls for models that do not support configurable reasoning, prevents unsupported settings from breaking live or queued sends, and restores the user's preference on compatible models. #101002

> Android model organization, default-model, and pinning controls now use the selected language. Sources: 41bea62 , bdc98f4 .

> Android users can switch the current chat's model from the composer, pin favorites, revisit recent choices, and return to the default without leaving the conversation; older pairings may need to be renewed. #100798

> Typing indicators now remain active during long Codex model, tool, command, recovery, and queued follow-up work instead of making the reply appear idle. #95844 Thanks @jalehman.

> iOS chat now shows and switches the active model, while iOS and macOS model pickers support pinned favorites and the five most recent choices. #100774

> iOS and macOS hide the thinking-level control for models that cannot use it, avoid sending stale unsupported settings, and restore the previous level when a reasoning-capable model is selected again. #100875

> Custom usage footers now render alias and map fallbacks correctly even when model or mode names collide with properties such as toString or constructor . #98503 Related #98466 . Thanks @chenyangjun-xy, @zhanglei99586.

> openclaw tui --local now explains when a known slash command requires the Gateway instead of sending that command to the model as an unwanted prompt. #100188 Thanks @goslingmanagment.

> The opt-in Logbook lets users review a model-organized workday timeline, generate standups, and ask questions about captured activity, with owner-only local storage and configurable retention. #99930

> Non-interactive openclaw models list and openclaw models status now exit normally after printing their results, allowing scripts and SSH diagnostics to finish without an external timeout. #77904 Thanks @dorukardahan, @vincentkoc.

> Removing a visible built-in model alias now explains that the alias is automatic and shows how to shadow it, while genuinely absent aliases still report as not found. #81641 Thanks @scientificprogrammer, @vincentkoc.

> Session logs and cached cost views now preserve provider-reconciled zero-dollar totals while recalculating genuinely missing costs from stored provider and model details. c45124a

> A focused tool-result-cap Doctor lint check now identifies settings below model-aware defaults or above the runtime ceiling with actionable paths. #97500 Thanks @giodl73-repo.

> Crestodian on Claude Code or Gemini CLI can now hold multi-turn setup conversations, inspect state, request exact approval for changes, and verify writes instead of falling back immediately to a single-turn planner. #100029

> Crestodian now distinguishes ordinary questions from operational requests, accepts natural approval phrases, clears stale proposals, and keeps sensitive configuration out of the conversation model. #100656

> Langfuse, OpenTelemetry, and Prometheus can now capture usage, cost, model, provider, timing, and session data for runs started through /v1/responses and /v1/chat/completions . #96152 Thanks @rocke2020, @xialonglee.

> Windows users can launch globally installed Gemini CLI and Claude Code backends through their npm command shims without immediate spawn failures or mangled prompt arguments. #101378 Thanks @wendy-chsy.

> The agent configuration guide now identifies the current models selected by the built-in opus and gpt aliases. #96375 Thanks @niks999.

> A scheduled cloud-model job that opens a response but sends no content can now move to a healthy fallback model before the entire run times out. #96096 Thanks @849261680, @velvet-shark.

> openclaw infer image describe now tries configured fallback image models after an explicitly selected model fails and reports which model ultimately succeeded. #98347 Thanks @momothemage.

> Failed code-mode tool attempts now show the error type, message, and location, giving the model and operator enough detail to diagnose or correct the problem. #95906 Thanks @vincentkoc, @zengwen-dt.

> Link understanding now keeps page fetching available for the slowest configured fallback and applies tools.links.timeoutSeconds consistently regardless of model order. #100731 Thanks @aniruddhaadak80, @cxbasdev.

> Multi-attachment prompts now keep real captions while removing duplicate transport markers and placeholder-only text that could confuse the model. #96431 Thanks @lin-hongkuan.

> Strengthened coverage for binding Codex conversations without an explicit model, protecting the default workflow from regressions. #89535 Thanks @kesslerio.

> Clarified internal fallback behavior so future maintenance is less likely to mishandle provider errors or older model responses. #89558

> Strengthened coverage so GitHub Copilot reasoning choices stay aligned with each account's supported models. #91728 Thanks @saju01.

> Reduced live-test disk usage by avoiding unnecessary copies of large Gemini browser data while preserving required credentials. #91907 Thanks @bryantegomoh, @pikaqqqqqq.

> Prepared session status and model selection for future storage changes while preserving current behavior. #96460 Thanks @jalehman.

> Prepared Feishu previews and Mattermost model summaries for future session-storage changes without changing behavior. #96507 Thanks @jalehman.

> Prepared bundled channel session handling for future storage changes without altering routing, model choices, or user workflows. #96527 Thanks @jalehman.

> Gave Claude CLI QA runs the appropriate longer time limits for Sonnet and Opus models. #96567 Thanks @clawsean.

> Simplified maintenance of the paired BytePlus and Volcengine model catalogs without changing provider behavior. #99777 Thanks @romneyda.

> Reduced unnecessary setup work for models that cannot use tools while preserving existing tool-enabled workflows. #100536 Thanks @vincentkoc.

> Added release coverage for corrected model labels and durable inbound-image previews in the Control UI. #100740 Thanks @hyspacex, @sweetcornna.

> Strengthened regression coverage for setting up Hugging Face local apps with compatible local model servers. #100887 Thanks @osolmaz.

> Removed an obsolete Android cache-cleanup path, leaving one clearer ownership model. #101470 Thanks @vincentkoc.

> Added consistent OpenClaw identification to requests sent through the official Google Gemini API. #101834 Thanks @vishal-dharm.

> Updated Meta provider validation and guidance for the deployed Muse Spark 1.1 model. #103163

> Aligned plugin prerelease validation with the current GPT-5.6 model defaults. #104722

> Updated live-provider validation to use the intended July GPT-5.6 model by default. #104750

> Reduced false GPT-5.6 release-validation failures by retrying a small set of incorrect validation responses. #104939

> Made Telegram release validation work reliably with model selections from older compatible candidates. #105401

> Improved Codex model-switch validation so conversation compaction no longer causes a false failure. #105493

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
## Nearby in Model Support

- Earlier: 2026-07-12 · Kimi Code · [[Changes/Kimi Code/2026-07-12-3-model-support-changes-in-kimi-code-0-23-6|3 Model Support changes in Kimi Code 0.23.6]]
- Later: 2026-07-13 · OpenCode · [[Changes/OpenCode/2026-07-13-4-model-support-changes-in-v1-17-20-1|4 Model Support changes in v1.17.20 + 1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-07-13-6e3705&body=Card%3A%20Changes%2FOpenClaw%2F2026-07-13-130-model-support-changes-in-v2026-7-1.md%0ACard%20ID%3A%20openclaw-2026-07-13-6e3705%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.7.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->