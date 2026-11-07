---
card_id: open-webui-2026-04-21-8016f1
date: '2026-04-21'
description: "Open WebUI · 2026-04-21 · Developer Workflow: 46 changes in v0.9.0 —
  \U0001F514 **Calendar reminders and alerts.** Calendar events now support reminder
  options from no…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1130
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: e2aec035f3318331e0b034788530b69c76ee6704214cb857e74437224ebe2e7a
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-04-21-8016f1
  comparison: ''
  date: '2026-04-21'
  description: 'Open WebUI — v0.9.0: 46 Developer Workflow changes'
  evidence:
  - quote: "\U0001F514 **Calendar reminders and alerts.** Calendar events now support
      reminder options from no alert up to one hour before start time, with upcoming
      alerts delivered through in-app toasts, browser notifications, and optional
      webhooks while avoiding duplicate sends. [Commit](https://github.com/open-webui/open-webui/commit/e5b5a174265d6710e986f6534ee7e3b2923233be)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F50E **Responses citation visibility.** Responses API flows now
      emit citation sources more consistently, making linked references easier to
      preserve and display in chat output. [Commit](https://github.com/open-webui/open-webui/commit/e695d854f2d11fada84d5fbec8d3edea4e468e19),
      [#23774](https://github.com/open-webui/open-webui/issues/23774)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F50C **WebSocket reconnect status feedback.** Open WebUI now warns
      when the real-time connection drops and confirms when it reconnects, while avoiding
      a reconnect message on the initial page load. [Commit](https://github.com/open-webui/open-webui/commit/1824e69a70e756cfcf543a9fbe4b0780d9b57292)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F3A8 **Theme updates.** Other windows can now update the app theme
      directly, keeping the interface in sync when theme changes are triggered externally.
      [Commit](https://github.com/open-webui/open-webui/commit/9f1b279e88bd22dfff4d2531209536dea6a2f65e)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F9F5 **Non-blocking file storage operations.** Uploading, reading,
      transcribing, and deleting files now offloads storage I/O to background threads,
      keeping the application responsive during file-heavy workflows. [Commit](https://github.com/open-webui/open-webui/commit/4866bec0f238198a721c952fe18dd04ba643be33)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F9F0 **AIOHTTP pool controls.** Administrators can now tune shared
      outbound HTTP connection behavior with \"AIOHTTP_POOL_CONNECTIONS\", \"AIOHTTP_POOL_CONNECTIONS_PER_HOST\",
      and \"AIOHTTP_POOL_DNS_TTL\" for better control under high concurrency. [Commit](https://github.com/open-webui/open-webui/commit/c47dd7b7717c4186e0f0549ca3c8cb4d9bb38135)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F5C4️ **Configurable storage local cache.** Administrators can now
      disable persistent local caching for cloud-backed uploads with the \"STORAGE_LOCAL_CACHE\"
      setting, reducing local disk usage by cleaning temporary upload copies after
      processing. [Commit](https://github.com/open-webui/open-webui/commit/8172c7e3d56918d1372be06b9369b58a3a88f6b1)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F5BC️ **Image MIME fallback option.** Administrators can now enable
      \"ENABLE_IMAGE_CONTENT_TYPE_EXTENSION_FALLBACK\" so image-to-base64 conversion
      can still detect common image types by file extension when MIME metadata is
      missing, improving compatibility on minimal container images and older file
      records. [Commit](https://github.com/open-webui/open-webui/commit/5127354b3eb4eaa71bc4ad68da69729e2196e7a4)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F6E1️ **Public sharing permissions.** Public channels, models, notes,
      prompts, and tools now respect allowed access grants more consistently, helping
      administrators control who can share content more safely. [Commit](https://github.com/open-webui/open-webui/commit/9d3e0637c86292b8b92e7607097a83f1075d7cd8)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F194 **Skill lookup by ID.** Skill instructions now include each
      skill’s ID, and the skill viewer now finds skills by ID in a case-insensitive
      way so attached skills are identified more reliably in chats. [Commit](https://github.com/open-webui/open-webui/commit/65ee771fd0d62d785ecbcf189e3f5b63858c11e6)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F4DD **Optional GET audit logging.** Administrators can now enable
      auditing for GET requests with the \"ENABLE_AUDIT_GET_REQUESTS\" setting when
      they need fuller request visibility. [Commit](https://github.com/open-webui/open-webui/commit/5ee791d5d28f236755243cb7d16d8737bb69ce36)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F4AC **Queued message handling.** Queued chat messages now send
      more reliably without advancing the queue too early, keeping follow-up prompts
      in the intended order. [Commit](https://github.com/open-webui/open-webui/commit/730e52a431d157dc62d72260668087437f1d52f4)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F39B️ **Reranking batch size control.** Administrators can now set
      \"RAG_RERANKING_BATCH_SIZE\" in Documents settings to control reranking workload
      size, helping balance retrieval speed and resource usage for their deployment.
      [Commit](https://github.com/open-webui/open-webui/commit/4d2f18981051205016bd24d39521e25a33581225)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F5E3️ **Pipeline error detail visibility.** Pipeline inlet and outlet
      failures now preserve and surface provider error details more reliably in chat
      error messages, making troubleshooting failed requests much clearer. [Commit](https://github.com/open-webui/open-webui/commit/d5e69f182cd7a6371ab25248f6432b277f83ef23)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F4E8 **Shared chat event routing.** Message update and send events
      now target the chat owner’s event channel, so shared chats receive the correct
      real-time updates instead of routing events to the acting user. [Commit](https://github.com/open-webui/open-webui/commit/47329b5032ba29716a7e7e973b07c6d9894968e0)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F510 **Knowledge file deletion ownership checks.** Collaborators
      with knowledge base write access can no longer permanently delete files they
      do not own, preventing unintended file removal across other linked chats and
      knowledge bases. [Commit](https://github.com/open-webui/open-webui/commit/914ccf07ef158afe5588b97ed42778c93c439938),
      [#23636](https://github.com/open-webui/open-webui/pull/23636#issuecomment-4232439454)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F5D1️ **Knowledge deletion reliability.** Deleting a knowledge base
      by ID now completes reliably without unexpected failures. [Commit](https://github.com/open-webui/open-webui/commit/7e453de4f7794ff386e285aa5951b94e926ec273),
      [#23776](https://github.com/open-webui/open-webui/issues/23776), [#23814](https://github.com/open-webui/open-webui/pull/23814)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F511 **SSO password option visibility.** Account settings now hide
      password change controls when password-change access is disabled, avoiding misleading
      password options for SSO-focused setups. [#15292](https://github.com/open-webui/open-webui/issues/15292),
      [Commit](https://github.com/open-webui/open-webui/commit/cced77b584d6ea46c58fecddb2b3dd5e955c8417)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F9EF **Provider error freeze recovery.** Task-based chat requests
      now surface provider HTTP errors through normal failure handling, so content-filter
      and other upstream 4xx responses no longer leave chats stuck in a perpetual
      loading state. [#23663](https://github.com/open-webui/open-webui/issues/23663),
      [Commit](https://github.com/open-webui/open-webui/commit/96265cf042c8ab97dbec5d0efcce8010d0cd76e5)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F5D2️ **Notes chat llama.cpp compatibility.** Notes AI chat no longer
      sends empty assistant prefill messages that can conflict with reasoning-enabled
      llama.cpp responses, preventing immediate 400 errors in Notes conversations.
      [Commit](https://github.com/open-webui/open-webui/commit/fd93bd3414a1725219e14561bc5640b62f9fd4a1),
      [#23703](https://github.com/open-webui/open-webui/issues/23703#issuecomment-4243907629)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: ⏳ **Interrupted response recovery.** Assistant placeholder messages now
      start as incomplete and recover more safely after interrupted generations, preventing
      silent empty replies after refreshes or dropped requests. [#23176](https://github.com/open-webui/open-webui/issues/23176),
      [Commit](https://github.com/open-webui/open-webui/commit/c8ef7b028931263e8773cb60a7111d80d9572d26),
      [Commit](https://github.com/open-webui/open-webui/commit/cf4218e688def6f11d195aeda6665ae5b5376b67)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F3A4 **STT SSL setting consistency.** Speech and related outbound
      media requests now consistently use shared async HTTP sessions and honor the
      configured SSL verification setting, improving compatibility with self-signed
      deployments. [#23672](https://github.com/open-webui/open-webui/issues/23672),
      [Commit](https://github.com/open-webui/open-webui/commit/2ddcb30b9a519885422ba1f36cc3485a7d897bf8)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F50E **FireCrawl timeout reliability.** FireCrawl web loading now
      uses direct scrape requests and improved timeout handling for single-URL fetches,
      reducing empty results and premature timeout failures with local FireCrawl setups.
      [#23411](https://github.com/open-webui/open-webui/issues/23411), [Commit](https://github.com/open-webui/open-webui/commit/9c64d84ad90804bf7d891e4a5097c03c4d7044c3)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F464 **Partial user profile updates.** User update API requests
      can now modify only the fields you provide, so administrators no longer need
      to resubmit unchanged name, email, and profile image values when changing a
      single setting like role. [#23424](https://github.com/open-webui/open-webui/issues/23424),
      [Commit](https://github.com/open-webui/open-webui/commit/3c2c611ba91d794a1e73134ec41b0de2b3927677)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F9F5 **Queued prompt race prevention.** Chat request queues now
      prevent overlapping processing for the same chat, avoiding duplicate queue handling
      when multiple queue-processing triggers fire close together. [#23181](https://github.com/open-webui/open-webui/issues/23181),
      [Commit](https://github.com/open-webui/open-webui/commit/e10a00132eed54a0108fb6ac120e8229deef3656)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F6D1 **Cancellation event delivery reliability.** Cancelled chat
      processing now safely emits task-cancel and error events only when an event
      emitter is available, while provider HTTP errors now also route through task-cancel
      handling so chats recover from blocked-loading states more reliably. [#23663](https://github.com/open-webui/open-webui/issues/23663),
      [Commit](https://github.com/open-webui/open-webui/commit/51765b619c8584b042af68c3a5c87525a105ccd8),
      [Commit](https://github.com/open-webui/open-webui/commit/96265cf042c8ab97dbec5d0efcce8010d0cd76e5)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F3F7️ **Prompt tag query accuracy.** Prompt tag filtering now uses
      JSON-element-aware queries so tag-based lookups return the correct prompts.
      [Commit](https://github.com/open-webui/open-webui/commit/e7e752f8e74e7b01fe2e6cb56f06e99312e1afe7),
      [#23386](https://github.com/open-webui/open-webui/pull/23386)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F5C3️ **SQLite async pool compatibility.** SQLite async database
      setup no longer forces an explicit queue pool class, avoiding pool configuration
      conflicts in SQLite deployments. [Commit](https://github.com/open-webui/open-webui/commit/26b8ca5b5eeb144fae3fe6eaeae826150d8af826)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F9E0 **Knowledge embedding deadlock prevention.** Knowledge file
      processing now runs blocking vector-save work in a worker thread while keeping
      async status updates reliable, preventing file processing from stalling during
      long embedding operations. [Commit](https://github.com/open-webui/open-webui/commit/d4b90f93bda2413ec8f040e61959acdb7b242061),
      [Commit](https://github.com/open-webui/open-webui/commit/22cfb3c673cbfa4a6bce26fde8e2e2754ce4963b)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F50E **Notes search matching.** Notes search now handles multi-word
      and hyphenated queries more reliably, so relevant notes and snippets are easier
      to find from partial phrase searches. [Commit](https://github.com/open-webui/open-webui/commit/a35926261646f8897ba71da1572ed5dff802e3be)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F9F1 **Redis cache key isolation.** Tool server and terminal server
      cache entries now include the Redis key prefix, preventing multiple Open WebUI
      instances that share one Redis database from overwriting each other’s cached
      connection data. [#23649](https://github.com/open-webui/open-webui/pull/23649)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F9E9 **Tool enum value handling.** Tool schema generation now safely
      handles enum values as strings, preventing failures when OpenAPI parameters
      include non-string enum entries. [#23597](https://github.com/open-webui/open-webui/issues/23597),
      [Commit](https://github.com/open-webui/open-webui/commit/4498e6faf2b1bdd1caa0e2c1c15d90a2790cd721)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F6E1️ **Collection process endpoint permissions.** Collection processing
      endpoints now enforce collection ownership checks for web and text processing
      requests. [Commit](https://github.com/open-webui/open-webui/commit/ba83613ff297bc82db660b5273f04672d744902f),
      [#23634](https://github.com/open-webui/open-webui/pull/23634)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F4DA **Knowledge query access enforcement.** Knowledge-base collection
      queries now block unauthorized enumeration and require read access before returning
      results. [Commit](https://github.com/open-webui/open-webui/commit/860b90fd17d14ba00674621edd294dee150491d2),
      [#23635](https://github.com/open-webui/open-webui/pull/23635), [#23452](https://github.com/open-webui/open-webui/pull/23452)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F50D **RAG collection query permissions.** Vector search collection
      queries now enforce access checks before retrieval results are returned. [Commit](https://github.com/open-webui/open-webui/commit/f44b7a01f5b854f47c1594a1ab5f72096f736262),
      [#23627](https://github.com/open-webui/open-webui/pull/23627)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F512 **Safer file access checks.** HTML file previews now treat
      missing or non-admin owners as inaccessible, preventing accidental access to
      files that should not be shown. [Commit](https://github.com/open-webui/open-webui/commit/6acaaea59a50ec26da03e6144017a2fd86241ce9)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F4E3 **Channel message lookups.** Channel message details and pinning
      now work more reliably when the sender account is missing, avoiding failures
      in those views. [Commit](https://github.com/open-webui/open-webui/commit/6acaaea59a50ec26da03e6144017a2fd86241ce9)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F4DE **Call overlay visibility.** Incoming call events now open
      the call overlay and controls reliably, preventing cases where the call interface
      briefly appeared and then disappeared. [Commit](https://github.com/open-webui/open-webui/commit/ee9db91df02120e1e3651e8881734966b710ad52)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F4AC **Prompt submission handling.** Chat messages now preserve
      attached files more reliably when prompts are sent, including queued messages
      and shared prompt actions. [Commit](https://github.com/open-webui/open-webui/commit/6d6dfbf02c893d72d85d4490cb41f1665b1f9f95)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F9FE **Code block line break reliability.** Blank lines in submitted
      code blocks are now preserved more reliably instead of being collapsed. [Commit](https://github.com/open-webui/open-webui/commit/1be9627dd27ffe75957729a4a0d1682a98684f01),
      [#20302](https://github.com/open-webui/open-webui/issues/20302), [#23451](https://github.com/open-webui/open-webui/pull/23451)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F5BC️ **Open Terminal file response handling.** Open Terminal tool
      responses now preserve binary content types in user-side connections, so image
      and non-text file reads work consistently instead of being forced into plain
      text. [#23125](https://github.com/open-webui/open-webui/issues/23125)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F5A5️ **Terminal label casing.** Terminal names in the chat input
      now display exactly as stored instead of being automatically capitalized, so
      domain-style server names appear correctly. [#23518](https://github.com/open-webui/open-webui/pull/23518)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F53D **Task list toggle icons.** The task list collapse button now
      shows the correct arrow direction, making task sections easier to expand and
      collapse at a glance. [Commit](https://github.com/open-webui/open-webui/commit/f66b67c8b86b6f9d896a23c7bb53907c2e6b15d3),
      [#23354](https://github.com/open-webui/open-webui/issues/23354)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F9F9 **Per-chat draft clearing.** Sent message drafts are now cleared
      using the active chat key, so sent text no longer reappears in the input after
      a refresh. [Commit](https://github.com/open-webui/open-webui/commit/124b7e9154d7f3ca8a16f2b90621209ac8d6b8c1),
      [#23296](https://github.com/open-webui/open-webui/issues/23296)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F9EA **Temp chat outlet filtering.** Outlet filters now process
      temporary chats more reliably, preserving assistant output and usage data so
      local chat responses stay consistent when filter pipelines are enabled. [Commit](https://github.com/open-webui/open-webui/commit/70a6a24f143b221c787bc50b72582ee1e0c2dac0)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F5C4️ **SQLite WAL default enabled.** SQLite deployments now default
      to enabling write-ahead logging, improving concurrent read and write behavior
      without requiring manual configuration. [Commit](https://github.com/open-webui/open-webui/commit/2f9e326dba3b1087932cb6b8075ed1881bd1c6d6)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 46-developer-workflow-changes-in-v0-9-0
  source_release: open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a
  source_type: github_releases
  theme: developer-workflow
  title: 46 Developer Workflow changes in v0.9.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-04-20-6-developer-workflow-changes-in-rust-v0-122-0|6
  Developer Workflow changes in rust-v0.122.0]]'
- '[[Changes/GitHub Copilot CLI/2026-04-20-2-developer-workflow-changes-in-v1-0-33|2
  Developer Workflow changes in v1.0.33]]'
- '[[Changes/OpenCode/2026-04-20-desktop-added-a-separate-terminal-font-setting-and-bundled-jetbrainsmono-nerd-fo|Desktop
  Added a separate terminal font setting and bundled JetBrainsMono Nerd Font Mono]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a|open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a]]'
source_type: github_releases
theme: developer-workflow
title: 46 Developer Workflow changes in v0.9.0
type: change
---

<!-- chronolog:begin region="header" -->
# 46 Developer Workflow changes in v0.9.0

**Open WebUI** · 2026-04-21 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.0) · from [[Releases/Open WebUI/open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a|v0.9.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔔 **Calendar reminders and alerts.** Calendar events now support reminder options from no alert up to one hour before start time, with upcoming alerts delivered through in-app toasts, browser notifications, and optional webhooks while avoiding duplicate sends. [Commit](https://github.com/open-webui/open-webui/commit/e5b5a174265d6710e986f6534ee7e3b2923233be)

> 🔎 **Responses citation visibility.** Responses API flows now emit citation sources more consistently, making linked references easier to preserve and display in chat output. [Commit](https://github.com/open-webui/open-webui/commit/e695d854f2d11fada84d5fbec8d3edea4e468e19), [#23774](https://github.com/open-webui/open-webui/issues/23774)

> 🔌 **WebSocket reconnect status feedback.** Open WebUI now warns when the real-time connection drops and confirms when it reconnects, while avoiding a reconnect message on the initial page load. [Commit](https://github.com/open-webui/open-webui/commit/1824e69a70e756cfcf543a9fbe4b0780d9b57292)

> 🎨 **Theme updates.** Other windows can now update the app theme directly, keeping the interface in sync when theme changes are triggered externally. [Commit](https://github.com/open-webui/open-webui/commit/9f1b279e88bd22dfff4d2531209536dea6a2f65e)

> 🧵 **Non-blocking file storage operations.** Uploading, reading, transcribing, and deleting files now offloads storage I/O to background threads, keeping the application responsive during file-heavy workflows. [Commit](https://github.com/open-webui/open-webui/commit/4866bec0f238198a721c952fe18dd04ba643be33)

> 🧰 **AIOHTTP pool controls.** Administrators can now tune shared outbound HTTP connection behavior with "AIOHTTP_POOL_CONNECTIONS", "AIOHTTP_POOL_CONNECTIONS_PER_HOST", and "AIOHTTP_POOL_DNS_TTL" for better control under high concurrency. [Commit](https://github.com/open-webui/open-webui/commit/c47dd7b7717c4186e0f0549ca3c8cb4d9bb38135)

> 🗄️ **Configurable storage local cache.** Administrators can now disable persistent local caching for cloud-backed uploads with the "STORAGE_LOCAL_CACHE" setting, reducing local disk usage by cleaning temporary upload copies after processing. [Commit](https://github.com/open-webui/open-webui/commit/8172c7e3d56918d1372be06b9369b58a3a88f6b1)

> 🖼️ **Image MIME fallback option.** Administrators can now enable "ENABLE_IMAGE_CONTENT_TYPE_EXTENSION_FALLBACK" so image-to-base64 conversion can still detect common image types by file extension when MIME metadata is missing, improving compatibility on minimal container images and older file records. [Commit](https://github.com/open-webui/open-webui/commit/5127354b3eb4eaa71bc4ad68da69729e2196e7a4)

> 🛡️ **Public sharing permissions.** Public channels, models, notes, prompts, and tools now respect allowed access grants more consistently, helping administrators control who can share content more safely. [Commit](https://github.com/open-webui/open-webui/commit/9d3e0637c86292b8b92e7607097a83f1075d7cd8)

> 🆔 **Skill lookup by ID.** Skill instructions now include each skill’s ID, and the skill viewer now finds skills by ID in a case-insensitive way so attached skills are identified more reliably in chats. [Commit](https://github.com/open-webui/open-webui/commit/65ee771fd0d62d785ecbcf189e3f5b63858c11e6)

> 📝 **Optional GET audit logging.** Administrators can now enable auditing for GET requests with the "ENABLE_AUDIT_GET_REQUESTS" setting when they need fuller request visibility. [Commit](https://github.com/open-webui/open-webui/commit/5ee791d5d28f236755243cb7d16d8737bb69ce36)

> 💬 **Queued message handling.** Queued chat messages now send more reliably without advancing the queue too early, keeping follow-up prompts in the intended order. [Commit](https://github.com/open-webui/open-webui/commit/730e52a431d157dc62d72260668087437f1d52f4)

> 🎛️ **Reranking batch size control.** Administrators can now set "RAG_RERANKING_BATCH_SIZE" in Documents settings to control reranking workload size, helping balance retrieval speed and resource usage for their deployment. [Commit](https://github.com/open-webui/open-webui/commit/4d2f18981051205016bd24d39521e25a33581225)

> 🗣️ **Pipeline error detail visibility.** Pipeline inlet and outlet failures now preserve and surface provider error details more reliably in chat error messages, making troubleshooting failed requests much clearer. [Commit](https://github.com/open-webui/open-webui/commit/d5e69f182cd7a6371ab25248f6432b277f83ef23)

> 📨 **Shared chat event routing.** Message update and send events now target the chat owner’s event channel, so shared chats receive the correct real-time updates instead of routing events to the acting user. [Commit](https://github.com/open-webui/open-webui/commit/47329b5032ba29716a7e7e973b07c6d9894968e0)

> 🔐 **Knowledge file deletion ownership checks.** Collaborators with knowledge base write access can no longer permanently delete files they do not own, preventing unintended file removal across other linked chats and knowledge bases. [Commit](https://github.com/open-webui/open-webui/commit/914ccf07ef158afe5588b97ed42778c93c439938), [#23636](https://github.com/open-webui/open-webui/pull/23636#issuecomment-4232439454)

> 🗑️ **Knowledge deletion reliability.** Deleting a knowledge base by ID now completes reliably without unexpected failures. [Commit](https://github.com/open-webui/open-webui/commit/7e453de4f7794ff386e285aa5951b94e926ec273), [#23776](https://github.com/open-webui/open-webui/issues/23776), [#23814](https://github.com/open-webui/open-webui/pull/23814)

> 🔑 **SSO password option visibility.** Account settings now hide password change controls when password-change access is disabled, avoiding misleading password options for SSO-focused setups. [#15292](https://github.com/open-webui/open-webui/issues/15292), [Commit](https://github.com/open-webui/open-webui/commit/cced77b584d6ea46c58fecddb2b3dd5e955c8417)

> 🧯 **Provider error freeze recovery.** Task-based chat requests now surface provider HTTP errors through normal failure handling, so content-filter and other upstream 4xx responses no longer leave chats stuck in a perpetual loading state. [#23663](https://github.com/open-webui/open-webui/issues/23663), [Commit](https://github.com/open-webui/open-webui/commit/96265cf042c8ab97dbec5d0efcce8010d0cd76e5)

> 🗒️ **Notes chat llama.cpp compatibility.** Notes AI chat no longer sends empty assistant prefill messages that can conflict with reasoning-enabled llama.cpp responses, preventing immediate 400 errors in Notes conversations. [Commit](https://github.com/open-webui/open-webui/commit/fd93bd3414a1725219e14561bc5640b62f9fd4a1), [#23703](https://github.com/open-webui/open-webui/issues/23703#issuecomment-4243907629)

> ⏳ **Interrupted response recovery.** Assistant placeholder messages now start as incomplete and recover more safely after interrupted generations, preventing silent empty replies after refreshes or dropped requests. [#23176](https://github.com/open-webui/open-webui/issues/23176), [Commit](https://github.com/open-webui/open-webui/commit/c8ef7b028931263e8773cb60a7111d80d9572d26), [Commit](https://github.com/open-webui/open-webui/commit/cf4218e688def6f11d195aeda6665ae5b5376b67)

> 🎤 **STT SSL setting consistency.** Speech and related outbound media requests now consistently use shared async HTTP sessions and honor the configured SSL verification setting, improving compatibility with self-signed deployments. [#23672](https://github.com/open-webui/open-webui/issues/23672), [Commit](https://github.com/open-webui/open-webui/commit/2ddcb30b9a519885422ba1f36cc3485a7d897bf8)

> 🔎 **FireCrawl timeout reliability.** FireCrawl web loading now uses direct scrape requests and improved timeout handling for single-URL fetches, reducing empty results and premature timeout failures with local FireCrawl setups. [#23411](https://github.com/open-webui/open-webui/issues/23411), [Commit](https://github.com/open-webui/open-webui/commit/9c64d84ad90804bf7d891e4a5097c03c4d7044c3)

> 👤 **Partial user profile updates.** User update API requests can now modify only the fields you provide, so administrators no longer need to resubmit unchanged name, email, and profile image values when changing a single setting like role. [#23424](https://github.com/open-webui/open-webui/issues/23424), [Commit](https://github.com/open-webui/open-webui/commit/3c2c611ba91d794a1e73134ec41b0de2b3927677)

> 🧵 **Queued prompt race prevention.** Chat request queues now prevent overlapping processing for the same chat, avoiding duplicate queue handling when multiple queue-processing triggers fire close together. [#23181](https://github.com/open-webui/open-webui/issues/23181), [Commit](https://github.com/open-webui/open-webui/commit/e10a00132eed54a0108fb6ac120e8229deef3656)

> 🛑 **Cancellation event delivery reliability.** Cancelled chat processing now safely emits task-cancel and error events only when an event emitter is available, while provider HTTP errors now also route through task-cancel handling so chats recover from blocked-loading states more reliably. [#23663](https://github.com/open-webui/open-webui/issues/23663), [Commit](https://github.com/open-webui/open-webui/commit/51765b619c8584b042af68c3a5c87525a105ccd8), [Commit](https://github.com/open-webui/open-webui/commit/96265cf042c8ab97dbec5d0efcce8010d0cd76e5)

> 🏷️ **Prompt tag query accuracy.** Prompt tag filtering now uses JSON-element-aware queries so tag-based lookups return the correct prompts. [Commit](https://github.com/open-webui/open-webui/commit/e7e752f8e74e7b01fe2e6cb56f06e99312e1afe7), [#23386](https://github.com/open-webui/open-webui/pull/23386)

> 🗃️ **SQLite async pool compatibility.** SQLite async database setup no longer forces an explicit queue pool class, avoiding pool configuration conflicts in SQLite deployments. [Commit](https://github.com/open-webui/open-webui/commit/26b8ca5b5eeb144fae3fe6eaeae826150d8af826)

> 🧠 **Knowledge embedding deadlock prevention.** Knowledge file processing now runs blocking vector-save work in a worker thread while keeping async status updates reliable, preventing file processing from stalling during long embedding operations. [Commit](https://github.com/open-webui/open-webui/commit/d4b90f93bda2413ec8f040e61959acdb7b242061), [Commit](https://github.com/open-webui/open-webui/commit/22cfb3c673cbfa4a6bce26fde8e2e2754ce4963b)

> 🔎 **Notes search matching.** Notes search now handles multi-word and hyphenated queries more reliably, so relevant notes and snippets are easier to find from partial phrase searches. [Commit](https://github.com/open-webui/open-webui/commit/a35926261646f8897ba71da1572ed5dff802e3be)

> 🧱 **Redis cache key isolation.** Tool server and terminal server cache entries now include the Redis key prefix, preventing multiple Open WebUI instances that share one Redis database from overwriting each other’s cached connection data. [#23649](https://github.com/open-webui/open-webui/pull/23649)

> 🧩 **Tool enum value handling.** Tool schema generation now safely handles enum values as strings, preventing failures when OpenAPI parameters include non-string enum entries. [#23597](https://github.com/open-webui/open-webui/issues/23597), [Commit](https://github.com/open-webui/open-webui/commit/4498e6faf2b1bdd1caa0e2c1c15d90a2790cd721)

> 🛡️ **Collection process endpoint permissions.** Collection processing endpoints now enforce collection ownership checks for web and text processing requests. [Commit](https://github.com/open-webui/open-webui/commit/ba83613ff297bc82db660b5273f04672d744902f), [#23634](https://github.com/open-webui/open-webui/pull/23634)

> 📚 **Knowledge query access enforcement.** Knowledge-base collection queries now block unauthorized enumeration and require read access before returning results. [Commit](https://github.com/open-webui/open-webui/commit/860b90fd17d14ba00674621edd294dee150491d2), [#23635](https://github.com/open-webui/open-webui/pull/23635), [#23452](https://github.com/open-webui/open-webui/pull/23452)

> 🔍 **RAG collection query permissions.** Vector search collection queries now enforce access checks before retrieval results are returned. [Commit](https://github.com/open-webui/open-webui/commit/f44b7a01f5b854f47c1594a1ab5f72096f736262), [#23627](https://github.com/open-webui/open-webui/pull/23627)

> 🔒 **Safer file access checks.** HTML file previews now treat missing or non-admin owners as inaccessible, preventing accidental access to files that should not be shown. [Commit](https://github.com/open-webui/open-webui/commit/6acaaea59a50ec26da03e6144017a2fd86241ce9)

> 📣 **Channel message lookups.** Channel message details and pinning now work more reliably when the sender account is missing, avoiding failures in those views. [Commit](https://github.com/open-webui/open-webui/commit/6acaaea59a50ec26da03e6144017a2fd86241ce9)

> 📞 **Call overlay visibility.** Incoming call events now open the call overlay and controls reliably, preventing cases where the call interface briefly appeared and then disappeared. [Commit](https://github.com/open-webui/open-webui/commit/ee9db91df02120e1e3651e8881734966b710ad52)

> 💬 **Prompt submission handling.** Chat messages now preserve attached files more reliably when prompts are sent, including queued messages and shared prompt actions. [Commit](https://github.com/open-webui/open-webui/commit/6d6dfbf02c893d72d85d4490cb41f1665b1f9f95)

> 🧾 **Code block line break reliability.** Blank lines in submitted code blocks are now preserved more reliably instead of being collapsed. [Commit](https://github.com/open-webui/open-webui/commit/1be9627dd27ffe75957729a4a0d1682a98684f01), [#20302](https://github.com/open-webui/open-webui/issues/20302), [#23451](https://github.com/open-webui/open-webui/pull/23451)

> 🖼️ **Open Terminal file response handling.** Open Terminal tool responses now preserve binary content types in user-side connections, so image and non-text file reads work consistently instead of being forced into plain text. [#23125](https://github.com/open-webui/open-webui/issues/23125)

> 🖥️ **Terminal label casing.** Terminal names in the chat input now display exactly as stored instead of being automatically capitalized, so domain-style server names appear correctly. [#23518](https://github.com/open-webui/open-webui/pull/23518)

> 🔽 **Task list toggle icons.** The task list collapse button now shows the correct arrow direction, making task sections easier to expand and collapse at a glance. [Commit](https://github.com/open-webui/open-webui/commit/f66b67c8b86b6f9d896a23c7bb53907c2e6b15d3), [#23354](https://github.com/open-webui/open-webui/issues/23354)

> 🧹 **Per-chat draft clearing.** Sent message drafts are now cleared using the active chat key, so sent text no longer reappears in the input after a refresh. [Commit](https://github.com/open-webui/open-webui/commit/124b7e9154d7f3ca8a16f2b90621209ac8d6b8c1), [#23296](https://github.com/open-webui/open-webui/issues/23296)

> 🧪 **Temp chat outlet filtering.** Outlet filters now process temporary chats more reliably, preserving assistant output and usage data so local chat responses stay consistent when filter pipelines are enabled. [Commit](https://github.com/open-webui/open-webui/commit/70a6a24f143b221c787bc50b72582ee1e0c2dac0)

> 🗄️ **SQLite WAL default enabled.** SQLite deployments now default to enabling write-ahead logging, improving concurrent read and write behavior without requiring manual configuration. [Commit](https://github.com/open-webui/open-webui/commit/2f9e326dba3b1087932cb6b8075ed1881bd1c6d6)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-04-21-3-files-and-data-changes-in-v0-9-0|3 Files and Data changes in v0.9.0]] · Files and Data
- [[Changes/Open WebUI/2026-04-21-4-image-generation-changes-in-v0-9-0|4 Image Generation changes in v0.9.0]] · Image Generation
- [[Changes/Open WebUI/2026-04-21-28-model-support-changes-in-v0-9-0|28 Model Support changes in v0.9.0]] · Model Support
- [[Changes/Open WebUI/2026-04-21-5-editor-experience-changes-in-v0-9-0|5 Editor Experience changes in v0.9.0]] · Editor Experience
- [[Changes/Open WebUI/2026-04-21-persistent-chat-payload-efficiency-persisted-chats-now-use-server-side-history-l|🚀 Persistent chat payload efficiency. Persisted chats now use server-side…]] · Multimodal Input
- [[Changes/Open WebUI/2026-04-21-8-context-window-changes-in-v0-9-0|8 Context Window changes in v0.9.0]] · Context Window
- [[Changes/Open WebUI/2026-04-21-24-reliability-and-performance-changes-in-v0-9-0|24 Reliability and Performance changes in v0.9.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-04-21-4-apps-and-integrations-changes-in-v0-9-0|4 Apps and Integrations changes in v0.9.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-04-21-8-automation-and-scheduling-changes-in-v0-9-0|8 Automation and Scheduling changes in v0.9.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-04-21-7-memory-and-personalization-changes-in-v0-9-0|7 Memory and Personalization changes in v0.9.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-04-21-2-mobile-and-desktop-changes-in-v0-9-0|2 Mobile and Desktop changes in v0.9.0]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-04-21-17-interface-experience-changes-in-v0-9-0|17 Interface Experience changes in v0.9.0]] · Interface Experience
- [[Changes/Open WebUI/2026-04-21-11-safety-and-privacy-changes-in-v0-9-0|11 Safety and Privacy changes in v0.9.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-04-21-4-search-and-browsing-changes-in-v0-9-0|4 Search and Browsing changes in v0.9.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-04-21-shared-chat-access-controls-you-can-now-control-who-has-access-to-a-shared-chat|🔗 Shared chat access controls. You can now control who has access to a shared…]] · Collaboration
- [[Changes/Open WebUI/2026-04-21-4-voice-and-audio-changes-in-v0-9-0|4 Voice and Audio changes in v0.9.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-04-21-17-account-and-access-changes-in-v0-9-0|17 Account and Access changes in v0.9.0]] · Account and Access
- [[Changes/Open WebUI/2026-04-21-21-other-changes-in-v0-9-0|21 other changes in v0.9.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-04-20 · OpenCode · [[Changes/OpenCode/2026-04-20-desktop-added-a-separate-terminal-font-setting-and-bundled-jetbrainsmono-nerd-fo|Desktop Added a separate terminal font setting and bundled JetBrainsMono Nerd Font Mono]]
- Later: 2026-04-22 · Claude Code · [[Changes/Claude Code/2026-04-22-2-developer-workflow-changes-in-v2-1-117|2 Developer Workflow changes in v2.1.117]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-04-21-8016f1&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-04-21-46-developer-workflow-changes-in-v0-9-0.md%0ACard%20ID%3A%20open-webui-2026-04-21-8016f1%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->