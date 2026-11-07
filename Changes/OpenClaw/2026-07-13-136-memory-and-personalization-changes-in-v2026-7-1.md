---
card_id: openclaw-2026-07-13-d7525c
date: '2026-07-13'
description: 'OpenClaw · 2026-07-13 · Memory and Personalization: 136 changes in v2026.7.1
  — Control UI Settings now shows a remote Gateway''s host identity, address…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1089
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 4e9a4beea14160de5eecaecb52efb185d3b05e1adbc555cd8e48b16216f6cbf7
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-07-13-d7525c
  comparison: ''
  date: '2026-07-13'
  description: 'OpenClaw — v2026.7.1: 136 Memory and Personalization changes'
  evidence:
  - quote: 'Control UI Settings now shows a remote Gateway''s host identity, address,
      operating system, runtime, uptime, CPU load, memory, and free disk space without
      requiring SSH. #100478'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: The surrounding session workflow is more durable too. Important conversations
      can be pinned, renamed, archived, restored, and monitored as ongoing work, while
      active goals remain part of working memory across later turns, compaction, queues,
      and interruptions.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Discord REST calls now fail with a clear error when a response is oversized
      or stalls instead of risking unbounded memory use and process instability. #95412
      Thanks @alix-007.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Discord message, thread-history, and attachment requests now reject oversized
      successful responses before they can drive excessive Gateway memory growth.
      #97693 Thanks @alix-007.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Discord Gateway connections now cap incoming frames at 16 MiB, preserving
      tested large member events while rejecting extreme traffic before it pressures
      memory. #99998 Thanks @sunlit-deng.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Long-running Discord and Nextcloud Talk integrations now bound their channel
      metadata caches instead of letting each newly encountered room increase memory
      use forever. #101650 Thanks @alix-007, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Signal plugin setup now handles slow, malformed, or oversized GitHub release
      metadata without risking process memory exhaustion. #97536 Thanks @hugenshen.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Nextcloud Talk sends and reactions now bound server response sizes, protecting
      OpenClaw from hangs or runaway memory use while preserving normal delivery.
      #96031 Thanks @alix-007.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Google Chat sends and request verification now bound oversized API, certificate,
      and error responses, allowing normal traffic through while broken or hostile
      bodies fail or truncate without exhausting memory. #96772 Thanks @vincentkoc,
      @wangmiao0668000666.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Tlon and Urbit channel failures now bound oversized or malformed error
      responses before they can cause memory spikes, while retaining useful short
      messages. #98496 Thanks @pandah97.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Mattermost channel monitoring now rejects inbound events above 16 MiB
      and reconnects, limiting memory exposure while continuing to accept normal large
      messages. #99366 Thanks @sunlit-deng.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Tlon now stops oversized or stalled external image downloads before they
      consume unbounded memory and can continue the message with the original URL.
      #100374 Thanks @hugenshen.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Microsoft Teams attachment recovery now declines oversized Graph metadata
      with diagnostics instead of buffering it into Gateway memory, while normal hosted
      media still downloads within configured limits. #101082 Thanks @cxbasdev.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Telegram bot probes, webhook checks, membership audits, and polling now
      reject oversized Bot API success bodies before they can exhaust Gateway memory.
      #97271 Thanks @hugenshen.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Telegram chat-ID lookup now fails safely on oversized getChat responses
      instead of risking excessive Gateway memory use during onboarding or routing.
      #97274 Thanks @hugenshen.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Long-running Slack integrations now keep conversation metadata caching
      within a fixed limit, preventing memory use from growing indefinitely as more
      channels and workspaces are encountered. #101562 Thanks @vincentkoc, @zhangguiping-xydt.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Mattermost API calls now stop oversized or endless successful responses
      before they can consume unbounded memory, while normal requests and uploads
      continue unchanged. #96033 Thanks @alix-007.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Tlon media uploads now stop safely when Memex returns an oversized or
      malformed response instead of allowing the upload attempt to consume excessive
      memory. #101115 Thanks @cxbasdev.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Claude CLI agent runs now fail over instead of presenting provider errors
      or raw stream data as answers, preserve multilingual and emoji output, and stop
      runaway one-shot output before it exhausts Gateway memory. #98942 Related #98896
      . Thanks @obviyus.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Bedrock Mantle model discovery now times out and caps oversized catalog
      responses instead of hanging or consuming excessive memory, while cached models
      remain available. #99961 Thanks @zhangguiping-xydt.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Anthropic-compatible requests now fail promptly with a bounded transport
      error when an upstream stream sends an oversized partial event instead of hanging
      and consuming memory. #100686 Thanks @zhangguiping-xydt.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Provider setup now stops reading runaway model-discovery responses before
      they can stall or exhaust memory, while normal self-hosted server responses
      continue to work. #95244 Thanks @alix-007, @sallyom.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Ollama model discovery now stops oversized or never-ending endpoint responses
      before they can exhaust memory or leave setup hanging. #96027 Thanks @alix-007.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'OpenAI ChatGPT Responses streaming now cancels oversized or endless provider
      bodies with a clear error before they can consume excessive process memory,
      while normal responses keep using the existing parser. #96762 Thanks @vincentkoc,
      @wangmiao0668000666.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Azure OpenAI Responses now bound oversized streaming and error bodies,
      protecting memory while preserving normal errors and cancellation. #97349 Thanks
      @wangmiao0668000666.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'OpenAI embedding batch polling and Realtime setup now cancel oversized
      successful responses early and return a bounded error instead of growing memory
      without limit. #97533 Thanks @hugenshen.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'OpenAI-compatible embedding batch downloads now process valid large outputs
      while stopping oversized files or JSONL records before they can exhaust memory.
      #98554 Thanks @sunlit-deng, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'MiniMax OAuth device setup now limits authorization response size so a
      faulty proxied or self-hosted endpoint cannot exhaust Gateway memory. #96322
      Thanks @lsr911.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Azure Speech, Microsoft Speech, ElevenLabs, MiniMax TTS, OpenRouter transcription,
      and xAI transcription now stop oversized or endless responses before they can
      stall speech work or strain Gateway memory, while ordinary responses remain
      unchanged. #96496 Thanks @hugenshen.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'GitHub Copilot model discovery and memory search now reject oversized
      or malformed responses instead of buffering them without limit, while valid
      catalog and embedding results continue normally. #96499 Thanks @hugenshen, @sallyom.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Moonshot video understanding now returns a predictable error for oversized
      or malformed responses instead of hanging or consuming memory indefinitely,
      including with custom base URLs. #96502 Thanks @hugenshen.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'OpenRouter video model discovery now stops oversized or runaway catalog
      responses promptly instead of letting them consume memory without limit, while
      normal discovery behavior is preserved. #96505 Thanks @mushuiyu886.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Voyage embedding batch jobs now stop oversized status, failure, and error-file
      responses before they can hang or exhaust worker memory, while oversized diagnostics
      degrade safely and ordinary responses remain unchanged. #96608 Thanks @alix-007.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Chutes onboarding now fails clearly when token-exchange or user-info responses
      are oversized, preventing abnormal authentication traffic from causing unbounded
      memory growth. #96779 Thanks @wangmiao0668000666.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Vydra image, video, and speech generation now fails with a bounded error
      on oversized or endless control responses instead of hanging or exhausting memory,
      while valid responses continue normally. #96875 Thanks @alix-007.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Google audio and video understanding now stops oversized provider responses
      at the shared 16 MiB limit with a clear error instead of allowing them to consume
      excessive memory. #96920 Thanks @mushuiyu886, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'ClickClack now stops oversized REST success responses at the provider
      limit, giving users and operators a predictable failure instead of continued
      streaming and memory growth. #96970 Thanks @mushuiyu886, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Z.AI endpoint and model detection now fails gracefully on oversized or
      endless error responses instead of exhausting host memory. #97540 Thanks @alix-007.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'GitHub Copilot sign-in and token refresh now reject oversized service
      responses with a clear error before they can exhaust OpenClaw''s memory. #97579
      Thanks @hugenshen.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Abnormally large Google Meet, Calendar, or OAuth responses now stop with
      an error before they can consume uncontrolled Gateway memory. #98850 Thanks
      @pandah97.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'MiniMax image understanding now stops oversized or malformed successful
      responses at a bounded limit, protecting memory while returning a useful diagnostic.
      #100694 Thanks @zhangguiping-xydt.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Hugging Face model discovery now falls back to the bundled catalog when
      a provider response is malformed or oversized instead of risking excessive memory
      use. #101079 Thanks @cxbasdev.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Memory indexing, recall, wiki synchronization, and search recover from
      more malformed pages, stale status, large indexes, transient reads, and provider
      mismatches without hiding useful stored context or overwriting user notes. When
      a result is incomplete or a configured memory provider is unavailable, the failure
      is clearer instead of looking like a complete answer.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Memory-wiki pages titled Index now remain stored, searchable, and retrievable
      instead of being hidden or overwritten by generated directory pages. #94326
      Thanks @vincentkoc, @yetval.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Active Memory now warns when recalled operational details may be outdated
      and clearly marks clipped summaries, so old or incomplete status is less likely
      to look current. #95888 Thanks @spencer2211.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Memory-wiki pages in subfolders now appear in search, lookup, compiled
      indexes, digests, and vault counts just like pages at the top level. #96022
      Thanks @machine3at, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Large memory indexes can now return filtered matches beyond sqlite-vec''s
      first 4,096 candidates without failing or silently missing valid results. #96157
      Thanks @itsuzef, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Repeated QMD-backed memory_search and openclaw memory search requests
      can return faster after the first lookup, while diagnostics separate setup time
      from search time and missing collections still trigger repair. #96655 Thanks
      @bek91.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Memory search now works with installed generic embedding plugins such
      as local llama.cpp, including their default model and connection details. #97095
      Thanks @849261680.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'One memory-wiki page with broken YAML no longer blocks healthy pages from
      being searched, compiled, linted, counted, or updated. #97177 Related #96125
      . Thanks @cow11023, @sunnyshu0925.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Memory-core light dreaming no longer repeats an unchanged work-summary
      block in DREAMS.md , while genuine daily-note updates can still appear later.
      #97446 Thanks @aaajiao, @qingminglong.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Memory Wiki now marks claims with malformed explicit freshness timestamps
      as unknown instead of masking the bad metadata with the page date. #97465 Thanks
      @ly-wang19.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Detailed /status plugins now warns when a configured memory embedding
      provider is unavailable and semantic recall has fallen back to keyword search.
      #97968 Thanks @masatohoshino.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Memory Wiki lint now ignores link-looking text inside inline and fenced
      code while continuing to report genuine broken links in prose. #98095 Thanks
      @durambar, @vincentkoc, @zhangqueping.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Memory-wiki source updates now preserve hand-written Notes when a temporary
      read failure prevents OpenClaw from safely loading the existing page. #98360
      Related #98345 . Thanks @qingminglong, @vincentkoc, @yetval.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'QMD memory recall now turns malformed or warning-filled mcporter output
      into a clear, filtered error instead of exposing raw subprocess text. #98381
      Thanks @miorbnli.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Memory-wiki source sync can now recover when a page is missing or collides
      with a non-file, while preserving existing content when a retry remains unsafe.
      #99276 Thanks @obviyus.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'memory_get with corpus=all can now return an available wiki supplement
      when the requested memory file is missing instead of stopping with an empty
      result. #100904 Thanks @mushuiyu886, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Memory Wiki imports now continue when a source page collides with a protected
      vault entry instead of stopping the whole import. 76db9a3 Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'With memorySearch.provider: none , OpenClaw now starts FTS-only memory
      without an unnecessary plugin capability scan. fbf574a'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'After /new or /reset , the previous conversation remains available for
      daily memory summaries and full-history searches through the session-logs skill.
      #71537 Thanks @injinj.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'With memory flush enabled, important conversation context now gets a chance
      to reach durable memory before automatic compaction, reducing silent gaps in
      saved notes. #84792 Thanks @turbotheturtle.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Interactive QMD memory searches with no matches now return an empty result
      promptly instead of appearing stuck during unnecessary index maintenance. #90030
      Related #90023 . Thanks @ruben2000de, @sahibzada-allahyar.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Shared group and channel transcripts now retain the sender ID, display
      name, and username for each durable user turn, making later history and memory
      processing correctly attribute participants. #90552 Thanks @pick-cat.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Session-memory files created around /new and /reset now keep one copy
      of each assistant reply instead of duplicating reasoning-model responses. #94401
      Thanks @sallyom, @sunnyshu0925.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Newly promoted long-term memories now omit raw transcript, summary, session-header,
      flush-prompt, and scoring clutter so useful notes are easier to find. #94636
      Thanks @josephur, @pinghe-learn, @tayoun.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'openclaw doctor --fix can now carry legacy Memory Core indexes from 2026.6.9
      upgrades into the current store without forcing a full re-embed. #95631 Thanks
      @mushuiyu886, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Memory Wiki import summaries now shorten ChatGPT text containing emoji
      without leaving corrupted replacement characters. #97362 Thanks @mushuiyu886.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'openclaw memory status now warns when session transcripts still need indexing
      instead of incorrectly reporting memory as current. #97857 Related #97814 .
      Thanks @che10x, @zw-xysk.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Rerunning memory-wiki synthesis or ChatGPT imports no longer risks erasing
      handwritten notes, frontmatter, or import state when an existing page cannot
      be read briefly. #98787 Thanks @vincentkoc, @yetval.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Temporary memory-maintenance failures no longer replace the agent reply,
      and persistently oversized sessions can recover in a fresh session while preserving
      the previous transcript. #100618 Thanks @jerry-xin, @rhclaw.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Memory Core now preserves short standalone concepts such as kv and s3
      in tags, improving recall without matching them inside unrelated words. #96304
      Thanks @ly-wang19.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Memory dreaming now records structured success or failure outcomes for
      light, REM, and deep phases so dashboards and health checks can monitor them
      reliably. #97723 Thanks @lg320531124, @momothemage.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'openclaw wiki lint now ignores wikilink-like patterns inside code examples
      so real broken Memory Wiki links are easier to spot. #97954 Thanks @durambar,
      @liuhao1024, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Memory-wiki bridge status now returns a usable warning instead of crashing
      on malformed plugin artifacts, and readMemoryArtifacts: false now reliably prevents
      those reads. #100900 Thanks @huveewomg.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Wiki search and retrieval now explain when an older or partial memory
      plugin lacks shared-search support and offer a practical workaround instead
      of exposing a raw TypeError. #100902 Thanks @huveewomg, @vincentkoc, @xuanmingguo.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Memories containing emoji or supplementary CJK characters can now be indexed
      without malformed text stalling the operation. #101574 Thanks @jensenwang560-blip.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'When both a primary memory read and its wiki supplement fail, memory_get
      corpus=all now returns the original structured read error instead of crashing
      the tool call. #101902 Thanks @aniruddhaadak80, @vincentkoc, @zw-xysk.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Memory-index debug logs now show whether an embedding batch completed
      or failed, making indexing problems easier to trace. #94732 Thanks @doubleji817-lang,
      @xydt-tanshanshan.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'openclaw memory status --fix now repairs session-corpus state without
      mistaking healthy daily-memory records for stale data. #93389 Thanks @alix-007,
      @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'openclaw memory status no longer shows impossible session indexing totals
      where the indexed file count exceeds the total file count. #95452 Thanks @buyitsydney,
      @liuhao1024.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Preparing a reset for a long-running session now avoids scanning the entire
      transcript, reducing startup file activity and memory use as history grows.
      #99335 Thanks @gmschasiepen, @momothemage.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'openclaw sessions tail now rejects oversized trajectory snapshots and
      updates with a clear limit error before they can exhaust memory. #101450 Thanks
      @cxbasdev, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Session-memory diagnostics now show the correct workspace and memory-file
      paths for sibling directories whose names merely resemble the user''s home path.
      #101577 Thanks @cxbasdev.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Emoji and other supplementary characters now remain intact when long agent
      progress or active-memory recall text is shortened. #100244 Thanks @vincentkoc,
      @xialonglee, @zengwen-dt.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Fresh Claude CLI workspaces now run a pending BOOTSTRAP.md on the first
      reply so required identity, memory, and setup steps are completed before normal
      conversation. #100560 Thanks @bill-starfoundry, @kruegerb, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Long-running agents are less likely to lose workspace instructions such
      as AGENTS.md , SOUL.md , or MEMORY.md for a turn during a temporary filesystem
      error. #100910 Thanks @masatohoshino.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'APNs relay pushes now reject oversized response bodies as RelayResponseTooLarge
      instead of exhausting Gateway memory or reporting false delivery. #97550 Thanks
      @alix-007.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'A runaway tool_search_code subprocess can no longer grow Gateway memory
      without limit through stderr, while failure reports retain the latest useful
      diagnostic detail. #101007 Thanks @hugenshen, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Malformed MCP OAuth failures now return a bounded HTTP-status diagnostic
      instead of allowing an unbounded error response to exhaust agent memory. #98143
      Thanks @pick-cat.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Oversized or malformed Microsoft Teams personal-chat attachment metadata
      now fails safely with a warning instead of consuming unbounded Gateway memory.
      #99125 Thanks @ly85206559.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Oversized or never-ending responses from supported external providers now
      stop at a fixed limit with a labeled error instead of consuming memory until
      the full body arrives. 0a14444 Thanks @joshavant.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Web fetch and provider integrations now enforce response-size caps without
      allocating an entire nonstandard response in memory. #99884 Thanks @zenglingbiao.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Browser-control requests now reject oversized successful JSON responses
      with a BrowserServiceError before they can consume excessive memory, while supported
      large browser results still work. #100889 Thanks @mushuiyu886.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Gateway sign-in tracking now keeps bounded memory use during floods of
      failed attempts from many addresses while preserving existing lockouts. #96224
      Thanks @eleqtrizit.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Gateway-wide Active Memory can now be changed only by owners or administrators,
      while other authorized users retain session-level controls. #97841 Thanks @pgondhi987.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Only owners and administrative Gateway clients can now turn Memory Core
      dreaming on or off through /dreaming , while status and help remain available
      to others. #97869 Thanks @eleqtrizit.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Signal local-file attachments that are oversized or use suspicious paths
      now fail quickly with a clear error before consuming excessive Gateway memory.
      #101391 Thanks @cxbasdev.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Expanded Android link previews now keep thumbnail memory within a byte
      budget, reducing excessive memory retention during long chats. #101560'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'openclaw/memory-lancedb can now install and update under normal npm dependency
      resolution, keeping LanceDB-backed memory active without version pinning or
      bypass flags. #99118 Related #90295 . Thanks @allenhurff, @joshavant.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'openclaw docs now rejects oversized search responses with a clear error
      before they can destabilize the CLI or exhaust memory. #98188 Thanks @cxbasdev.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'OpenClaw update checks now limit malformed or unexpectedly large npm registry
      responses before they can consume excessive memory. #98508 Thanks @lzyyzznl.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'A focused memory-search Doctor lint check now reports provider, credential,
      backend, and QMD setup problems with structured paths and fixes. #97137 Thanks
      @giodl73-repo.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Default doctor --lint results now focus on actionable configuration and
      runtime problems, with optional backup and memory advice available only when
      requested. #99249 Thanks @giodl73-repo.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'openclaw plugins list now uses substantially less peak memory on fresh
      and already-migrated packaged installs while preserving required migration behavior.
      #103132'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Oversized browser-control error responses can no longer consume excessive
      Gateway memory, while ordinary failures still provide useful diagnostics. #98455
      Thanks @wings1029.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Reliability fixes now reject unsafe cron and plugin inputs, preserve skill
      formatting, surface Gateway and memory failures, fail LSP startup sooner, and
      prevent stale Android camera results after cancellation. #100399 Thanks @849261680,
      @anyech, @cxbasdev, @lin-hongkuan, @masatohoshino, @nankingjing, @qingminglong,
      @simon-xydt, @snotty, @xialonglee.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Oversized local socket replies now fail promptly without consuming memory
      until timeout, while large macOS commands still return completion status and
      bounded recent output. #98130 Thanks @pick-cat.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'QMD command pipe failures now report a clean memory-operation error instead
      of taking down the memory host. #101402 Thanks @wings1029.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Oversized ClawHub packages, skills, ClawPacks, resolver archives, and
      GitHub-source downloads now stop with a clear size-limit error before they can
      exhaust Gateway memory. #101176'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Added regression coverage ensuring memory search can recover after a separate
      reindex without restarting the gateway. #96094 Related #91167 . Thanks @849261680,
      @kiagentkronos-cell.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Reduced unnecessary processing for local memory installations configured
      to use shorter embedding vectors. #96952 Thanks @ly-wang19, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Reduced CPU and temporary memory use when branching or restoring sessions
      with many saved checkpoints. #96964 Thanks @ly-wang19.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Protected OpenClaw from excessive memory use when an agent proxy returns
      an unusually large error response. #97351 Thanks @zhangguiping-xydt.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Protected Matrix QA runs from excessive memory use when a homeserver returns
      an unusually large response. #97547 Thanks @alix-007.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Protected Discord smoke checks from excessive memory use when the service
      returns an unusually large response. #97548 Thanks @alix-007, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Protected QA Lab Telegram checks from excessive memory use when the Telegram
      API returns an unexpectedly large response. #99151 Thanks @hugenshen.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Protected QA Channel workflows from excessive memory use when a QA service
      returns oversized data. #99169 Thanks @hugenshen.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Restored reliable lint validation for the Memory Wiki extension without
      changing its behavior. #99307 Thanks @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Made true-or-false setting interpretation consistent across plugins, messaging,
      media, scheduling, and memory configuration. #99750 Thanks @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Improved artifact-build reliability by preventing memory-related validation
      failures. #99820'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Made QA report command validation substantially faster and less memory-intensive
      without changing its results. #99909'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Made plugin development surface validation faster and less memory-intensive
      without changing what it verifies. #99940'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Made lightweight realtime validation tools start faster and use less memory
      while preserving live smoke behavior. #100002'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Reduced memory use and kept isolated tests within their performance budget
      for faster, more dependable contributor feedback. #100019'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Added changelog coverage for a broad set of previously shipped provider,
      channel, memory, browser, and configuration fixes. #101128'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Hardened QA credential administration against oversized service responses,
      failing clearly without excessive memory use. #101131 Thanks @cxbasdev.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Reduced unsupported memory SDK surface so developers are less likely to
      depend on private internals. #101362 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Narrowed the private memory SDK surface and improved the accuracy of maintenance
      reports. #101508 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Simplified the private memory SDK surface by removing one-use layers and
      unused interfaces. #101568 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Reduced unused internal memory interfaces, making that code easier to
      maintain without changing user behavior. #101583 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Simplified internal Windows process-launching code for memory features
      without changing how they work. #101594 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Trimmed unused internal memory interfaces to reduce maintenance overhead
      while preserving existing behavior. #101604 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Reduced unused internal Memory Wiki interfaces to make future maintenance
      and dead-code checks clearer. #101931 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Tightened memory-core boundaries to reduce maintenance risk without changing
      storage or search behavior. #101969 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Kept offline memory-isolation QA fully local, preventing accidental calls
      to the live embeddings service. #105488'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 136-memory-and-personalization-changes-in-v2026-7-1
  source_release: openclaw-2026-07-13-v2026-7-1-c2063718
  source_type: openclaw_changelog
  theme: memory
  title: 136 Memory and Personalization changes in v2026.7.1
  type: change
related_changes:
- '[[Changes/Kimi Code/2026-07-08-progressive-tool-disclosure-select-tools-experimental-compaction-now-discards-th|Progressive
  tool disclosure (select_tools, experimental)]]'
- '[[Changes/Claude/2026-07-09-a-new-way-to-reflect-with-claude|A new way to reflect
  with Claude]]'
- '[[Changes/Claude/2026-07-10-updated-memory-for-claude|Updated memory for Claude]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-07-13-v2026-7-1-c2063718|openclaw-2026-07-13-v2026-7-1-c2063718]]'
source_type: openclaw_changelog
theme: memory
title: 136 Memory and Personalization changes in v2026.7.1
type: change
---

<!-- chronolog:begin region="header" -->
# 136 Memory and Personalization changes in v2026.7.1

**OpenClaw** · 2026-07-13 · [[Themes/memory|Memory and Personalization]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.7.1) · from [[Releases/OpenClaw/openclaw-2026-07-13-v2026-7-1-c2063718|v2026.7.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Control UI Settings now shows a remote Gateway's host identity, address, operating system, runtime, uptime, CPU load, memory, and free disk space without requiring SSH. #100478

> The surrounding session workflow is more durable too. Important conversations can be pinned, renamed, archived, restored, and monitored as ongoing work, while active goals remain part of working memory across later turns, compaction, queues, and interruptions.

> Discord REST calls now fail with a clear error when a response is oversized or stalls instead of risking unbounded memory use and process instability. #95412 Thanks @alix-007.

> Discord message, thread-history, and attachment requests now reject oversized successful responses before they can drive excessive Gateway memory growth. #97693 Thanks @alix-007.

> Discord Gateway connections now cap incoming frames at 16 MiB, preserving tested large member events while rejecting extreme traffic before it pressures memory. #99998 Thanks @sunlit-deng.

> Long-running Discord and Nextcloud Talk integrations now bound their channel metadata caches instead of letting each newly encountered room increase memory use forever. #101650 Thanks @alix-007, @vincentkoc.

> Signal plugin setup now handles slow, malformed, or oversized GitHub release metadata without risking process memory exhaustion. #97536 Thanks @hugenshen.

> Nextcloud Talk sends and reactions now bound server response sizes, protecting OpenClaw from hangs or runaway memory use while preserving normal delivery. #96031 Thanks @alix-007.

> Google Chat sends and request verification now bound oversized API, certificate, and error responses, allowing normal traffic through while broken or hostile bodies fail or truncate without exhausting memory. #96772 Thanks @vincentkoc, @wangmiao0668000666.

> Tlon and Urbit channel failures now bound oversized or malformed error responses before they can cause memory spikes, while retaining useful short messages. #98496 Thanks @pandah97.

> Mattermost channel monitoring now rejects inbound events above 16 MiB and reconnects, limiting memory exposure while continuing to accept normal large messages. #99366 Thanks @sunlit-deng.

> Tlon now stops oversized or stalled external image downloads before they consume unbounded memory and can continue the message with the original URL. #100374 Thanks @hugenshen.

> Microsoft Teams attachment recovery now declines oversized Graph metadata with diagnostics instead of buffering it into Gateway memory, while normal hosted media still downloads within configured limits. #101082 Thanks @cxbasdev.

> Telegram bot probes, webhook checks, membership audits, and polling now reject oversized Bot API success bodies before they can exhaust Gateway memory. #97271 Thanks @hugenshen.

> Telegram chat-ID lookup now fails safely on oversized getChat responses instead of risking excessive Gateway memory use during onboarding or routing. #97274 Thanks @hugenshen.

> Long-running Slack integrations now keep conversation metadata caching within a fixed limit, preventing memory use from growing indefinitely as more channels and workspaces are encountered. #101562 Thanks @vincentkoc, @zhangguiping-xydt.

> Mattermost API calls now stop oversized or endless successful responses before they can consume unbounded memory, while normal requests and uploads continue unchanged. #96033 Thanks @alix-007.

> Tlon media uploads now stop safely when Memex returns an oversized or malformed response instead of allowing the upload attempt to consume excessive memory. #101115 Thanks @cxbasdev.

> Claude CLI agent runs now fail over instead of presenting provider errors or raw stream data as answers, preserve multilingual and emoji output, and stop runaway one-shot output before it exhausts Gateway memory. #98942 Related #98896 . Thanks @obviyus.

> Bedrock Mantle model discovery now times out and caps oversized catalog responses instead of hanging or consuming excessive memory, while cached models remain available. #99961 Thanks @zhangguiping-xydt.

> Anthropic-compatible requests now fail promptly with a bounded transport error when an upstream stream sends an oversized partial event instead of hanging and consuming memory. #100686 Thanks @zhangguiping-xydt.

> Provider setup now stops reading runaway model-discovery responses before they can stall or exhaust memory, while normal self-hosted server responses continue to work. #95244 Thanks @alix-007, @sallyom.

> Ollama model discovery now stops oversized or never-ending endpoint responses before they can exhaust memory or leave setup hanging. #96027 Thanks @alix-007.

> OpenAI ChatGPT Responses streaming now cancels oversized or endless provider bodies with a clear error before they can consume excessive process memory, while normal responses keep using the existing parser. #96762 Thanks @vincentkoc, @wangmiao0668000666.

> Azure OpenAI Responses now bound oversized streaming and error bodies, protecting memory while preserving normal errors and cancellation. #97349 Thanks @wangmiao0668000666.

> OpenAI embedding batch polling and Realtime setup now cancel oversized successful responses early and return a bounded error instead of growing memory without limit. #97533 Thanks @hugenshen.

> OpenAI-compatible embedding batch downloads now process valid large outputs while stopping oversized files or JSONL records before they can exhaust memory. #98554 Thanks @sunlit-deng, @vincentkoc.

> MiniMax OAuth device setup now limits authorization response size so a faulty proxied or self-hosted endpoint cannot exhaust Gateway memory. #96322 Thanks @lsr911.

> Azure Speech, Microsoft Speech, ElevenLabs, MiniMax TTS, OpenRouter transcription, and xAI transcription now stop oversized or endless responses before they can stall speech work or strain Gateway memory, while ordinary responses remain unchanged. #96496 Thanks @hugenshen.

> GitHub Copilot model discovery and memory search now reject oversized or malformed responses instead of buffering them without limit, while valid catalog and embedding results continue normally. #96499 Thanks @hugenshen, @sallyom.

> Moonshot video understanding now returns a predictable error for oversized or malformed responses instead of hanging or consuming memory indefinitely, including with custom base URLs. #96502 Thanks @hugenshen.

> OpenRouter video model discovery now stops oversized or runaway catalog responses promptly instead of letting them consume memory without limit, while normal discovery behavior is preserved. #96505 Thanks @mushuiyu886.

> Voyage embedding batch jobs now stop oversized status, failure, and error-file responses before they can hang or exhaust worker memory, while oversized diagnostics degrade safely and ordinary responses remain unchanged. #96608 Thanks @alix-007.

> Chutes onboarding now fails clearly when token-exchange or user-info responses are oversized, preventing abnormal authentication traffic from causing unbounded memory growth. #96779 Thanks @wangmiao0668000666.

> Vydra image, video, and speech generation now fails with a bounded error on oversized or endless control responses instead of hanging or exhausting memory, while valid responses continue normally. #96875 Thanks @alix-007.

> Google audio and video understanding now stops oversized provider responses at the shared 16 MiB limit with a clear error instead of allowing them to consume excessive memory. #96920 Thanks @mushuiyu886, @vincentkoc.

> ClickClack now stops oversized REST success responses at the provider limit, giving users and operators a predictable failure instead of continued streaming and memory growth. #96970 Thanks @mushuiyu886, @vincentkoc.

> Z.AI endpoint and model detection now fails gracefully on oversized or endless error responses instead of exhausting host memory. #97540 Thanks @alix-007.

> GitHub Copilot sign-in and token refresh now reject oversized service responses with a clear error before they can exhaust OpenClaw's memory. #97579 Thanks @hugenshen.

> Abnormally large Google Meet, Calendar, or OAuth responses now stop with an error before they can consume uncontrolled Gateway memory. #98850 Thanks @pandah97.

> MiniMax image understanding now stops oversized or malformed successful responses at a bounded limit, protecting memory while returning a useful diagnostic. #100694 Thanks @zhangguiping-xydt.

> Hugging Face model discovery now falls back to the bundled catalog when a provider response is malformed or oversized instead of risking excessive memory use. #101079 Thanks @cxbasdev.

> Memory indexing, recall, wiki synchronization, and search recover from more malformed pages, stale status, large indexes, transient reads, and provider mismatches without hiding useful stored context or overwriting user notes. When a result is incomplete or a configured memory provider is unavailable, the failure is clearer instead of looking like a complete answer.

> Memory-wiki pages titled Index now remain stored, searchable, and retrievable instead of being hidden or overwritten by generated directory pages. #94326 Thanks @vincentkoc, @yetval.

> Active Memory now warns when recalled operational details may be outdated and clearly marks clipped summaries, so old or incomplete status is less likely to look current. #95888 Thanks @spencer2211.

> Memory-wiki pages in subfolders now appear in search, lookup, compiled indexes, digests, and vault counts just like pages at the top level. #96022 Thanks @machine3at, @vincentkoc.

> Large memory indexes can now return filtered matches beyond sqlite-vec's first 4,096 candidates without failing or silently missing valid results. #96157 Thanks @itsuzef, @vincentkoc.

> Repeated QMD-backed memory_search and openclaw memory search requests can return faster after the first lookup, while diagnostics separate setup time from search time and missing collections still trigger repair. #96655 Thanks @bek91.

> Memory search now works with installed generic embedding plugins such as local llama.cpp, including their default model and connection details. #97095 Thanks @849261680.

> One memory-wiki page with broken YAML no longer blocks healthy pages from being searched, compiled, linted, counted, or updated. #97177 Related #96125 . Thanks @cow11023, @sunnyshu0925.

> Memory-core light dreaming no longer repeats an unchanged work-summary block in DREAMS.md , while genuine daily-note updates can still appear later. #97446 Thanks @aaajiao, @qingminglong.

> Memory Wiki now marks claims with malformed explicit freshness timestamps as unknown instead of masking the bad metadata with the page date. #97465 Thanks @ly-wang19.

> Detailed /status plugins now warns when a configured memory embedding provider is unavailable and semantic recall has fallen back to keyword search. #97968 Thanks @masatohoshino.

> Memory Wiki lint now ignores link-looking text inside inline and fenced code while continuing to report genuine broken links in prose. #98095 Thanks @durambar, @vincentkoc, @zhangqueping.

> Memory-wiki source updates now preserve hand-written Notes when a temporary read failure prevents OpenClaw from safely loading the existing page. #98360 Related #98345 . Thanks @qingminglong, @vincentkoc, @yetval.

> QMD memory recall now turns malformed or warning-filled mcporter output into a clear, filtered error instead of exposing raw subprocess text. #98381 Thanks @miorbnli.

> Memory-wiki source sync can now recover when a page is missing or collides with a non-file, while preserving existing content when a retry remains unsafe. #99276 Thanks @obviyus.

> memory_get with corpus=all can now return an available wiki supplement when the requested memory file is missing instead of stopping with an empty result. #100904 Thanks @mushuiyu886, @vincentkoc.

> Memory Wiki imports now continue when a source page collides with a protected vault entry instead of stopping the whole import. 76db9a3 Thanks @vincentkoc.

> With memorySearch.provider: none , OpenClaw now starts FTS-only memory without an unnecessary plugin capability scan. fbf574a

> After /new or /reset , the previous conversation remains available for daily memory summaries and full-history searches through the session-logs skill. #71537 Thanks @injinj.

> With memory flush enabled, important conversation context now gets a chance to reach durable memory before automatic compaction, reducing silent gaps in saved notes. #84792 Thanks @turbotheturtle.

> Interactive QMD memory searches with no matches now return an empty result promptly instead of appearing stuck during unnecessary index maintenance. #90030 Related #90023 . Thanks @ruben2000de, @sahibzada-allahyar.

> Shared group and channel transcripts now retain the sender ID, display name, and username for each durable user turn, making later history and memory processing correctly attribute participants. #90552 Thanks @pick-cat.

> Session-memory files created around /new and /reset now keep one copy of each assistant reply instead of duplicating reasoning-model responses. #94401 Thanks @sallyom, @sunnyshu0925.

> Newly promoted long-term memories now omit raw transcript, summary, session-header, flush-prompt, and scoring clutter so useful notes are easier to find. #94636 Thanks @josephur, @pinghe-learn, @tayoun.

> openclaw doctor --fix can now carry legacy Memory Core indexes from 2026.6.9 upgrades into the current store without forcing a full re-embed. #95631 Thanks @mushuiyu886, @vincentkoc.

> Memory Wiki import summaries now shorten ChatGPT text containing emoji without leaving corrupted replacement characters. #97362 Thanks @mushuiyu886.

> openclaw memory status now warns when session transcripts still need indexing instead of incorrectly reporting memory as current. #97857 Related #97814 . Thanks @che10x, @zw-xysk.

> Rerunning memory-wiki synthesis or ChatGPT imports no longer risks erasing handwritten notes, frontmatter, or import state when an existing page cannot be read briefly. #98787 Thanks @vincentkoc, @yetval.

> Temporary memory-maintenance failures no longer replace the agent reply, and persistently oversized sessions can recover in a fresh session while preserving the previous transcript. #100618 Thanks @jerry-xin, @rhclaw.

> Memory Core now preserves short standalone concepts such as kv and s3 in tags, improving recall without matching them inside unrelated words. #96304 Thanks @ly-wang19.

> Memory dreaming now records structured success or failure outcomes for light, REM, and deep phases so dashboards and health checks can monitor them reliably. #97723 Thanks @lg320531124, @momothemage.

> openclaw wiki lint now ignores wikilink-like patterns inside code examples so real broken Memory Wiki links are easier to spot. #97954 Thanks @durambar, @liuhao1024, @vincentkoc.

> Memory-wiki bridge status now returns a usable warning instead of crashing on malformed plugin artifacts, and readMemoryArtifacts: false now reliably prevents those reads. #100900 Thanks @huveewomg.

> Wiki search and retrieval now explain when an older or partial memory plugin lacks shared-search support and offer a practical workaround instead of exposing a raw TypeError. #100902 Thanks @huveewomg, @vincentkoc, @xuanmingguo.

> Memories containing emoji or supplementary CJK characters can now be indexed without malformed text stalling the operation. #101574 Thanks @jensenwang560-blip.

> When both a primary memory read and its wiki supplement fail, memory_get corpus=all now returns the original structured read error instead of crashing the tool call. #101902 Thanks @aniruddhaadak80, @vincentkoc, @zw-xysk.

> Memory-index debug logs now show whether an embedding batch completed or failed, making indexing problems easier to trace. #94732 Thanks @doubleji817-lang, @xydt-tanshanshan.

> openclaw memory status --fix now repairs session-corpus state without mistaking healthy daily-memory records for stale data. #93389 Thanks @alix-007, @vincentkoc.

> openclaw memory status no longer shows impossible session indexing totals where the indexed file count exceeds the total file count. #95452 Thanks @buyitsydney, @liuhao1024.

> Preparing a reset for a long-running session now avoids scanning the entire transcript, reducing startup file activity and memory use as history grows. #99335 Thanks @gmschasiepen, @momothemage.

> openclaw sessions tail now rejects oversized trajectory snapshots and updates with a clear limit error before they can exhaust memory. #101450 Thanks @cxbasdev, @vincentkoc.

> Session-memory diagnostics now show the correct workspace and memory-file paths for sibling directories whose names merely resemble the user's home path. #101577 Thanks @cxbasdev.

> Emoji and other supplementary characters now remain intact when long agent progress or active-memory recall text is shortened. #100244 Thanks @vincentkoc, @xialonglee, @zengwen-dt.

> Fresh Claude CLI workspaces now run a pending BOOTSTRAP.md on the first reply so required identity, memory, and setup steps are completed before normal conversation. #100560 Thanks @bill-starfoundry, @kruegerb, @vincentkoc.

> Long-running agents are less likely to lose workspace instructions such as AGENTS.md , SOUL.md , or MEMORY.md for a turn during a temporary filesystem error. #100910 Thanks @masatohoshino.

> APNs relay pushes now reject oversized response bodies as RelayResponseTooLarge instead of exhausting Gateway memory or reporting false delivery. #97550 Thanks @alix-007.

> A runaway tool_search_code subprocess can no longer grow Gateway memory without limit through stderr, while failure reports retain the latest useful diagnostic detail. #101007 Thanks @hugenshen, @vincentkoc.

> Malformed MCP OAuth failures now return a bounded HTTP-status diagnostic instead of allowing an unbounded error response to exhaust agent memory. #98143 Thanks @pick-cat.

> Oversized or malformed Microsoft Teams personal-chat attachment metadata now fails safely with a warning instead of consuming unbounded Gateway memory. #99125 Thanks @ly85206559.

> Oversized or never-ending responses from supported external providers now stop at a fixed limit with a labeled error instead of consuming memory until the full body arrives. 0a14444 Thanks @joshavant.

> Web fetch and provider integrations now enforce response-size caps without allocating an entire nonstandard response in memory. #99884 Thanks @zenglingbiao.

> Browser-control requests now reject oversized successful JSON responses with a BrowserServiceError before they can consume excessive memory, while supported large browser results still work. #100889 Thanks @mushuiyu886.

> Gateway sign-in tracking now keeps bounded memory use during floods of failed attempts from many addresses while preserving existing lockouts. #96224 Thanks @eleqtrizit.

> Gateway-wide Active Memory can now be changed only by owners or administrators, while other authorized users retain session-level controls. #97841 Thanks @pgondhi987.

> Only owners and administrative Gateway clients can now turn Memory Core dreaming on or off through /dreaming , while status and help remain available to others. #97869 Thanks @eleqtrizit.

> Signal local-file attachments that are oversized or use suspicious paths now fail quickly with a clear error before consuming excessive Gateway memory. #101391 Thanks @cxbasdev.

> Expanded Android link previews now keep thumbnail memory within a byte budget, reducing excessive memory retention during long chats. #101560

> openclaw/memory-lancedb can now install and update under normal npm dependency resolution, keeping LanceDB-backed memory active without version pinning or bypass flags. #99118 Related #90295 . Thanks @allenhurff, @joshavant.

> openclaw docs now rejects oversized search responses with a clear error before they can destabilize the CLI or exhaust memory. #98188 Thanks @cxbasdev.

> OpenClaw update checks now limit malformed or unexpectedly large npm registry responses before they can consume excessive memory. #98508 Thanks @lzyyzznl.

> A focused memory-search Doctor lint check now reports provider, credential, backend, and QMD setup problems with structured paths and fixes. #97137 Thanks @giodl73-repo.

> Default doctor --lint results now focus on actionable configuration and runtime problems, with optional backup and memory advice available only when requested. #99249 Thanks @giodl73-repo.

> openclaw plugins list now uses substantially less peak memory on fresh and already-migrated packaged installs while preserving required migration behavior. #103132

> Oversized browser-control error responses can no longer consume excessive Gateway memory, while ordinary failures still provide useful diagnostics. #98455 Thanks @wings1029.

> Reliability fixes now reject unsafe cron and plugin inputs, preserve skill formatting, surface Gateway and memory failures, fail LSP startup sooner, and prevent stale Android camera results after cancellation. #100399 Thanks @849261680, @anyech, @cxbasdev, @lin-hongkuan, @masatohoshino, @nankingjing, @qingminglong, @simon-xydt, @snotty, @xialonglee.

> Oversized local socket replies now fail promptly without consuming memory until timeout, while large macOS commands still return completion status and bounded recent output. #98130 Thanks @pick-cat.

> QMD command pipe failures now report a clean memory-operation error instead of taking down the memory host. #101402 Thanks @wings1029.

> Oversized ClawHub packages, skills, ClawPacks, resolver archives, and GitHub-source downloads now stop with a clear size-limit error before they can exhaust Gateway memory. #101176

> Added regression coverage ensuring memory search can recover after a separate reindex without restarting the gateway. #96094 Related #91167 . Thanks @849261680, @kiagentkronos-cell.

> Reduced unnecessary processing for local memory installations configured to use shorter embedding vectors. #96952 Thanks @ly-wang19, @vincentkoc.

> Reduced CPU and temporary memory use when branching or restoring sessions with many saved checkpoints. #96964 Thanks @ly-wang19.

> Protected OpenClaw from excessive memory use when an agent proxy returns an unusually large error response. #97351 Thanks @zhangguiping-xydt.

> Protected Matrix QA runs from excessive memory use when a homeserver returns an unusually large response. #97547 Thanks @alix-007.

> Protected Discord smoke checks from excessive memory use when the service returns an unusually large response. #97548 Thanks @alix-007, @vincentkoc.

> Protected QA Lab Telegram checks from excessive memory use when the Telegram API returns an unexpectedly large response. #99151 Thanks @hugenshen.

> Protected QA Channel workflows from excessive memory use when a QA service returns oversized data. #99169 Thanks @hugenshen.

> Restored reliable lint validation for the Memory Wiki extension without changing its behavior. #99307 Thanks @romneyda.

> Made true-or-false setting interpretation consistent across plugins, messaging, media, scheduling, and memory configuration. #99750 Thanks @romneyda.

> Improved artifact-build reliability by preventing memory-related validation failures. #99820

> Made QA report command validation substantially faster and less memory-intensive without changing its results. #99909

> Made plugin development surface validation faster and less memory-intensive without changing what it verifies. #99940

> Made lightweight realtime validation tools start faster and use less memory while preserving live smoke behavior. #100002

> Reduced memory use and kept isolated tests within their performance budget for faster, more dependable contributor feedback. #100019

> Added changelog coverage for a broad set of previously shipped provider, channel, memory, browser, and configuration fixes. #101128

> Hardened QA credential administration against oversized service responses, failing clearly without excessive memory use. #101131 Thanks @cxbasdev.

> Reduced unsupported memory SDK surface so developers are less likely to depend on private internals. #101362 Thanks @vincentkoc.

> Narrowed the private memory SDK surface and improved the accuracy of maintenance reports. #101508 Thanks @vincentkoc.

> Simplified the private memory SDK surface by removing one-use layers and unused interfaces. #101568 Thanks @vincentkoc.

> Reduced unused internal memory interfaces, making that code easier to maintain without changing user behavior. #101583 Thanks @vincentkoc.

> Simplified internal Windows process-launching code for memory features without changing how they work. #101594 Thanks @vincentkoc.

> Trimmed unused internal memory interfaces to reduce maintenance overhead while preserving existing behavior. #101604 Thanks @vincentkoc.

> Reduced unused internal Memory Wiki interfaces to make future maintenance and dead-code checks clearer. #101931 Thanks @vincentkoc.

> Tightened memory-core boundaries to reduce maintenance risk without changing storage or search behavior. #101969 Thanks @vincentkoc.

> Kept offline memory-isolation QA fully local, preventing accidental calls to the live embeddings service. #105488

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
## Nearby in Memory and Personalization

- Earlier: 2026-07-10 · Claude · [[Changes/Claude/2026-07-10-updated-memory-for-claude|Updated memory for Claude]]
- Later: 2026-07-14 · Claude Code · [[Changes/Claude Code/2026-07-14-memory-writes-that-leave-a-memory-md-index-over-its-read-limit-now-produce-an-ex|Memory writes that leave a MEMORY.md index over its read limit now produce…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-07-13-d7525c&body=Card%3A%20Changes%2FOpenClaw%2F2026-07-13-136-memory-and-personalization-changes-in-v2026-7-1.md%0ACard%20ID%3A%20openclaw-2026-07-13-d7525c%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.7.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->