---
card_id: open-webui-2026-06-01-2a27f4
date: '2026-06-01'
description: "Open WebUI · 2026-06-01 · Developer Workflow: 27 changes in v0.9.6 —
  \U0001F4C2 **Smart directory sync for knowledge bases.** Local directories can now
  be synced into a…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2820
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: cf655ee7ef5ed597b396cd6a6475e20b7a82d2c64b63a51a363d3788d771365b
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-06-01-2a27f4
  comparison: ''
  date: '2026-06-01'
  description: 'Open WebUI — v0.9.6: 27 Developer Workflow changes'
  evidence:
  - quote: "\U0001F4C2 **Smart directory sync for knowledge bases.** Local directories
      can now be synced into a knowledge base in one action: file checksums are compared
      against what's already stored, and only added or modified files are uploaded
      while removed files and orphaned subdirectories are cleaned up, with the directory
      structure mirrored automatically and per-file progress shown throughout. [#19190](https://github.com/open-webui/open-webui/issues/19190),
      [#19394](https://github.com/open-webui/open-webui/issues/19394), [Commit](https://github.com/open-webui/open-webui/commit/60c9db1cb81d021589cb49bee8744a799b51211f),
      [Commit](https://github.com/open-webui/open-webui/commit/73bdf86766d3f44467cdec436786fe089481baf3),
      [Commit](https://github.com/open-webui/open-webui/commit/9835b3f1dd7aa9c92ff08a634a0f97cc2a046e42),
      [Commit](https://github.com/open-webui/open-webui/commit/97252fa609440573251d8e75090f347ed1e51e1d),
      [Commit](https://github.com/open-webui/open-webui/commit/8f2d346e10c47b57bf6b5a6aa02d453488a88b89),
      [Commit](https://github.com/open-webui/open-webui/commit/1527eb6e01d441225c979d12d78b7625edf1086f)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: ✏️ **File renaming in knowledge bases.** Files inside a knowledge base
      can now be renamed directly from the workspace, with the new name reflected
      wherever the file is referenced. [Commit](https://github.com/open-webui/open-webui/commit/3127f1b46255626ea92eb0b598e45078287303f1)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F4C4 **Configurable knowledge base file page size.** Administrators
      can now request a larger page size when listing a knowledge base's files through
      the API, reducing the number of requests needed to retrieve large collections
      instead of paging through fixed increments of 30. [#25148](https://github.com/open-webui/open-webui/issues/25148),
      [Commit](https://github.com/open-webui/open-webui/commit/a4d1b3e9378a61a11dd9822a8dbb525f39753081)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F503 **Persistent processing indicator for knowledge files.** Files
      still being processed in a knowledge base now keep showing a processing indicator
      across page reloads, so you can tell what's still ingesting after navigating
      away and back. [#25031](https://github.com/open-webui/open-webui/issues/25031),
      [Commit](https://github.com/open-webui/open-webui/commit/ad9f2eeb15a448147d5e47e6a391cabb9aefd0ea)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F40E **Lighter Ollama backend connections.** Requests to Ollama
      backends now reuse a shared connection pool instead of opening a fresh session
      each time, reducing TCP and TLS handshake overhead for installs that poll Ollama
      frequently or have multiple backends configured. [Commit](https://github.com/open-webui/open-webui/commit/5d9a09a88a9094ebfcd249340be3aaee544b34d0)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001FAAA **More user placeholders in custom headers.** Custom-header
      templates for direct connections and tool servers now support \"{{USER_EMAIL}}\"
      and \"{{USER_ROLE}}\" alongside the existing user and session placeholders.
      [Commit](https://github.com/open-webui/open-webui/commit/ed73ef3d8df988b0e9646b82df5b1a453202ef8d)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F4CA **Paginated feedback history.** The feedback and evaluation
      history list is now paginated, keeping it responsive for instances that have
      accumulated large numbers of feedback entries. [Commit](https://github.com/open-webui/open-webui/commit/160a6694e4bd66fc42e6361947516e8e15414ef3)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F9CA **Valkey vector database support.** Valkey can now be used
      as the vector database backend, configurable through new \"VALKEY_URL\" and
      related settings including index type, distance metric, and HNSW tuning. [#24769](https://github.com/open-webui/open-webui/pull/24769),
      [Commit](https://github.com/open-webui/open-webui/commit/c0f1aa291938bbef62db8d4013dbc498b0abea15)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F6AA **Terminal proxy path traversal.** The terminal proxy now fully
      decodes request paths before validating them, blocking multi-encoded payloads
      that could otherwise escape the intended path. [#25157](https://github.com/open-webui/open-webui/pull/25157)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F9E9 **Chat recovery from corrupted history.** Chats whose internal
      message graph was left in a malformed state by a failed regeneration now open
      and load correctly, with missing roles, parent references, and current-message
      pointers reconstructed automatically instead of breaking the chat. [#24424](https://github.com/open-webui/open-webui/issues/24424),
      [#24157](https://github.com/open-webui/open-webui/issues/24157), [#20474](https://github.com/open-webui/open-webui/issues/20474),
      [#24799](https://github.com/open-webui/open-webui/pull/24799), [Commit](https://github.com/open-webui/open-webui/commit/d310a0777c4c48ec772bdc9a510005d5e91b09c7)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F4E8 **Imported chats with folders appear correctly.** Importing
      grouped chats no longer leaves them invisible when a referenced folder is missing;
      such chats now appear in the chat list instead of being silently orphaned. [#24910](https://github.com/open-webui/open-webui/issues/24910),
      [Commit](https://github.com/open-webui/open-webui/commit/7f7cd210186cb6a67e028c17974eb210fc7ba9fd)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F522 **Bracketed numbers in code blocks.** Numbers in square brackets
      such as \"[0]\" inside code blocks are no longer stripped out as if they were
      source citations, so code displays and copies correctly. [#24948](https://github.com/open-webui/open-webui/issues/24948),
      [Commit](https://github.com/open-webui/open-webui/commit/e90a618f4555cea2c024bb60c1332ca04eed96da)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F50C **API chat completions reliability.** Direct calls to the chat
      completions API no longer fail with an internal error when no chat session identifier
      is supplied. [#24553](https://github.com/open-webui/open-webui/issues/24553),
      [#25235](https://github.com/open-webui/open-webui/issues/25235), [Commit](https://github.com/open-webui/open-webui/commit/bc244fdc90504824b76654880898bf3f6649c299),
      [Commit](https://github.com/open-webui/open-webui/commit/f16b5c446027eae1bd767617bac2fdf54b24d6fc)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F3F7️ **Skill mentions in messages.** Mentioning a skill in a message
      now keeps the skill's name as readable text instead of removing it, and selecting
      a skill without typing anything no longer causes an error on providers that
      reject empty messages. [#24929](https://github.com/open-webui/open-webui/issues/24929),
      [Commit](https://github.com/open-webui/open-webui/commit/01810e32ad51305ca3247e8f83da95f6e6260f0c)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F5D1️ **Background tasks stop when a chat is removed.** Deleting
      or archiving a chat now cancels any in-flight generation or title and tag tasks
      for it, instead of leaving orphaned background work running. [#25050](https://github.com/open-webui/open-webui/pull/25050),
      [Commit](https://github.com/open-webui/open-webui/commit/778dba1d6b8dc3962163fa7bf9d802d9a07fba26)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F524 **Non-UTF-8 text and CSV uploads.** Text and CSV files saved
      in legacy encodings, including Latin-1, Windows-1252, and Chinese encodings
      such as GB18030, are now detected and loaded correctly instead of being rejected
      as binary or failing with an empty-content error. [#25172](https://github.com/open-webui/open-webui/issues/25172),
      [#24973](https://github.com/open-webui/open-webui/issues/24973), [Commit](https://github.com/open-webui/open-webui/commit/6f0277db52d005420480abb0702d421525d6ea8b),
      [Commit](https://github.com/open-webui/open-webui/commit/1bbb2b933d4cee70a5102eca4109e77b8625f8fc)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F9FD **Null bytes in nested data no longer break saves.** Data containing
      null bytes nested inside structured fields is now sanitized correctly before
      being written, preventing database errors that the previous check failed to
      catch. [#25018](https://github.com/open-webui/open-webui/pull/25018), [Commit](https://github.com/open-webui/open-webui/commit/e3ab4bd212e44c39f439ec4ff5df7c3dbd046895)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: ⏳ **Terminal session stability.** The terminal proxy no longer hangs when
      one direction of the connection closes before the other, so terminal sessions
      shut down cleanly instead of stalling. [#25464](https://github.com/open-webui/open-webui/issues/25464),
      [#25479](https://github.com/open-webui/open-webui/pull/25479)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F9F7 **Tool call continuity with strict providers.** Chats that
      contain incomplete tool calls or orphaned tool results no longer fail to continue
      when sent to providers that strictly validate tool pairings, such as Anthropic
      and AWS Bedrock Converse. [#24758](https://github.com/open-webui/open-webui/issues/24758),
      [#24940](https://github.com/open-webui/open-webui/issues/24940), [#24798](https://github.com/open-webui/open-webui/pull/24798),
      [Commit](https://github.com/open-webui/open-webui/commit/cfa6908d579e1f7f202a321289029996130b8411)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001FA9D **Reliable knowledge base file linking.** Files uploaded to
      a knowledge collection are now linked on the server as part of the upload itself,
      so they remain attached to the collection even if you navigate away or close
      the page before processing finishes. [#24807](https://github.com/open-webui/open-webui/issues/24807),
      [Commit](https://github.com/open-webui/open-webui/commit/d0b17f056911ec73df2b686a0d92bb789391db27)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: ☁️ **Azure connections on custom hostnames.** Connections marked as the
      Azure provider now use the Azure code path even when the endpoint does not contain
      "azure" in its hostname, fixing custom Azure deployments served from non-standard
      domains. [#24882](https://github.com/open-webui/open-webui/pull/24882), [Commit](https://github.com/open-webui/open-webui/commit/c8f851bd2de3d127f1e818fc116c27174f96d3f1)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F5D3️ **Clearing calendar event fields.** Removing the description
      or location from a calendar event now saves correctly instead of silently keeping
      the previous value. [#25026](https://github.com/open-webui/open-webui/issues/25026),
      [Commit](https://github.com/open-webui/open-webui/commit/91810f1c4e93d4f559bdf61cd085cadc288a732d),
      [Commit](https://github.com/open-webui/open-webui/commit/78b1637a035d71099262412e5dee3e4d65c7fb2f)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001FA7A **Database health check recovery.** After a transient database
      connection error, the health check endpoint now recovers automatically instead
      of staying permanently broken on the affected worker. [Commit](https://github.com/open-webui/open-webui/commit/0b81520e072bb4ed15532b8e153b43dd3243feaf)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001FAB5 **JSON exception logging.** With JSON log formatting enabled,
      exceptions are now recorded correctly with a structured type, message, and stacktrace
      instead of being dropped, and a logging failure can no longer crash the application.
      [#25135](https://github.com/open-webui/open-webui/issues/25135), [Commit](https://github.com/open-webui/open-webui/commit/79bf3d28d88e78b0136ef3c3c9f8e7bb85d3cea9)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F501 **Resilient database migrations.** Database migrations now
      skip tables, indexes, and columns that already exist and add missing primary
      keys to legacy tables, so upgrades succeed even when parts of the schema were
      manually or partially created beforehand. [Commit](https://github.com/open-webui/open-webui/commit/81f611fb73c726cfcfc20ee57a926a543f07e95f),
      [Commit](https://github.com/open-webui/open-webui/commit/f0e88dadc8502ea05b1a00f3155bee7d1cf32249),
      [Commit](https://github.com/open-webui/open-webui/commit/bd9f82d5a681ee94bde44325033447500a0c76bf),
      [Commit](https://github.com/open-webui/open-webui/commit/459b1c3fda2ec3579fbd2ab408d0fdeb07c96b99),
      [Commit](https://github.com/open-webui/open-webui/commit/6df09a4039d181f4e2d41324e93cd36c6fb27dfd),
      [Commit](https://github.com/open-webui/open-webui/commit/95840e307a66429168775de389b329487a4311c4),
      [Commit](https://github.com/open-webui/open-webui/commit/6b1df94bf933af92f5c7d093a2d92e2e50d6fdd0),
      [Commit](https://github.com/open-webui/open-webui/commit/98d3b2308564e2112290773ea240b90419ebb48d),
      [Commit](https://github.com/open-webui/open-webui/commit/1b9d22e324181b96511a15cbacc40fdbb439ad79),
      [Commit](https://github.com/open-webui/open-webui/commit/dc0f8ae6f2372b6e5dd42f3520813b09c54146c0),
      [Commit](https://github.com/open-webui/open-webui/commit/ee3b14233a642ff1bc38aef03a2418afcf5d6c1d),
      [Commit](https://github.com/open-webui/open-webui/commit/1004dad2749bcc369d511315a808d4bb5277854c),
      [Commit](https://github.com/open-webui/open-webui/commit/db2b3d7fd86cc7d76424671ead3c62a3f6302fe7),
      [Commit](https://github.com/open-webui/open-webui/commit/2e1b671e8db49f47d69fd59ece2b58e109ec8b84),
      [Commit](https://github.com/open-webui/open-webui/commit/9a8969ca93f8c9109d956518a085be3e2afacc07),
      [Commit](https://github.com/open-webui/open-webui/commit/9717ada92fdb3761a217d309f322ee9fbe418d0d),
      [Commit](https://github.com/open-webui/open-webui/commit/d7cfc1e46a8f3e5c8f6758c12ef641f41fb51a39),
      [Commit](https://github.com/open-webui/open-webui/commit/9263b7568eaa83f43e4a118c98490c4f7aaba570),
      [Commit](https://github.com/open-webui/open-webui/commit/73d2065227e651cf90a2cfade721516815743ab4),
      [#24722](https://github.com/open-webui/open-webui/pull/24722)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: ⚙️ **Tool-call iteration cap renamed and raised.** The environment variable
      that limits how many tool calls a single chat response may make is now "CHAT_RESPONSE_MAX_TOOL_CALL_ITERATIONS",
      with its default raised from 30 to 256 and a new "-1" value for unlimited; the
      previous "CHAT_RESPONSE_MAX_TOOL_CALL_RETRIES" name continues to work as a fallback,
      and chats that hit the cap now show a clear error in-chat instead of stopping
      silently. [#24918](https://github.com/open-webui/open-webui/pull/24918), [Commit](https://github.com/open-webui/open-webui/commit/2b99945d2726bdf5aed7b1712f9e3b7b622671df)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F510 **Reduced public \"/api/config\" exposure.** The \"/api/config\"
      response no longer includes several feature flags (\"enable_api_keys\", \"enable_password_change_form\",
      \"enable_version_update_check\", \"enable_public_active_users_count\", \"enable_easter_eggs\")
      for unauthenticated callers, reducing information disclosure to anonymous visitors.
      [Commit](https://github.com/open-webui/open-webui/commit/245e0ee029e9e10617f62953a9e6f67dd00ecf81),
      [Commit](https://github.com/open-webui/open-webui/commit/ae06e199d5d3f65296a978cc35079bdacba596d2)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 27-developer-workflow-changes-in-v0-9-6
  source_release: open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e
  source_type: github_releases
  theme: developer-workflow
  title: 27 Developer Workflow changes in v0.9.6
  type: change
related_changes:
- '[[Changes/OpenCode/2026-05-30-terminal-wrapped-inline-tool-rows-now-stay-aligned-and-failed-inline-tools-can-e|Terminal
  Wrapped inline tool rows now stay aligned, and failed inline tools can…]]'
- '[[Changes/Codex CLI/2026-06-01-11-developer-workflow-changes-in-rust-v0-136-0|11
  Developer Workflow changes in rust-v0.136.0]]'
- '[[Changes/GitHub Copilot CLI/2026-06-01-lsp-show-lsp-test-and-lsp-reload-correctly-discover-project-lsp-config-when-the|/lsp
  show, /lsp test, and /lsp reload correctly discover project LSP config…]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e|open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e]]'
source_type: github_releases
theme: developer-workflow
title: 27 Developer Workflow changes in v0.9.6
type: change
---

<!-- chronolog:begin region="header" -->
# 27 Developer Workflow changes in v0.9.6

**Open WebUI** · 2026-06-01 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.6) · from [[Releases/Open WebUI/open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e|v0.9.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📂 **Smart directory sync for knowledge bases.** Local directories can now be synced into a knowledge base in one action: file checksums are compared against what's already stored, and only added or modified files are uploaded while removed files and orphaned subdirectories are cleaned up, with the directory structure mirrored automatically and per-file progress shown throughout. [#19190](https://github.com/open-webui/open-webui/issues/19190), [#19394](https://github.com/open-webui/open-webui/issues/19394), [Commit](https://github.com/open-webui/open-webui/commit/60c9db1cb81d021589cb49bee8744a799b51211f), [Commit](https://github.com/open-webui/open-webui/commit/73bdf86766d3f44467cdec436786fe089481baf3), [Commit](https://github.com/open-webui/open-webui/commit/9835b3f1dd7aa9c92ff08a634a0f97cc2a046e42), [Commit](https://github.com/open-webui/open-webui/commit/97252fa609440573251d8e75090f347ed1e51e1d), [Commit](https://github.com/open-webui/open-webui/commit/8f2d346e10c47b57bf6b5a6aa02d453488a88b89), [Commit](https://github.com/open-webui/open-webui/commit/1527eb6e01d441225c979d12d78b7625edf1086f)

> ✏️ **File renaming in knowledge bases.** Files inside a knowledge base can now be renamed directly from the workspace, with the new name reflected wherever the file is referenced. [Commit](https://github.com/open-webui/open-webui/commit/3127f1b46255626ea92eb0b598e45078287303f1)

> 📄 **Configurable knowledge base file page size.** Administrators can now request a larger page size when listing a knowledge base's files through the API, reducing the number of requests needed to retrieve large collections instead of paging through fixed increments of 30. [#25148](https://github.com/open-webui/open-webui/issues/25148), [Commit](https://github.com/open-webui/open-webui/commit/a4d1b3e9378a61a11dd9822a8dbb525f39753081)

> 🔃 **Persistent processing indicator for knowledge files.** Files still being processed in a knowledge base now keep showing a processing indicator across page reloads, so you can tell what's still ingesting after navigating away and back. [#25031](https://github.com/open-webui/open-webui/issues/25031), [Commit](https://github.com/open-webui/open-webui/commit/ad9f2eeb15a448147d5e47e6a391cabb9aefd0ea)

> 🐎 **Lighter Ollama backend connections.** Requests to Ollama backends now reuse a shared connection pool instead of opening a fresh session each time, reducing TCP and TLS handshake overhead for installs that poll Ollama frequently or have multiple backends configured. [Commit](https://github.com/open-webui/open-webui/commit/5d9a09a88a9094ebfcd249340be3aaee544b34d0)

> 🪪 **More user placeholders in custom headers.** Custom-header templates for direct connections and tool servers now support "{{USER_EMAIL}}" and "{{USER_ROLE}}" alongside the existing user and session placeholders. [Commit](https://github.com/open-webui/open-webui/commit/ed73ef3d8df988b0e9646b82df5b1a453202ef8d)

> 📊 **Paginated feedback history.** The feedback and evaluation history list is now paginated, keeping it responsive for instances that have accumulated large numbers of feedback entries. [Commit](https://github.com/open-webui/open-webui/commit/160a6694e4bd66fc42e6361947516e8e15414ef3)

> 🧊 **Valkey vector database support.** Valkey can now be used as the vector database backend, configurable through new "VALKEY_URL" and related settings including index type, distance metric, and HNSW tuning. [#24769](https://github.com/open-webui/open-webui/pull/24769), [Commit](https://github.com/open-webui/open-webui/commit/c0f1aa291938bbef62db8d4013dbc498b0abea15)

> 🚪 **Terminal proxy path traversal.** The terminal proxy now fully decodes request paths before validating them, blocking multi-encoded payloads that could otherwise escape the intended path. [#25157](https://github.com/open-webui/open-webui/pull/25157)

> 🧩 **Chat recovery from corrupted history.** Chats whose internal message graph was left in a malformed state by a failed regeneration now open and load correctly, with missing roles, parent references, and current-message pointers reconstructed automatically instead of breaking the chat. [#24424](https://github.com/open-webui/open-webui/issues/24424), [#24157](https://github.com/open-webui/open-webui/issues/24157), [#20474](https://github.com/open-webui/open-webui/issues/20474), [#24799](https://github.com/open-webui/open-webui/pull/24799), [Commit](https://github.com/open-webui/open-webui/commit/d310a0777c4c48ec772bdc9a510005d5e91b09c7)

> 📨 **Imported chats with folders appear correctly.** Importing grouped chats no longer leaves them invisible when a referenced folder is missing; such chats now appear in the chat list instead of being silently orphaned. [#24910](https://github.com/open-webui/open-webui/issues/24910), [Commit](https://github.com/open-webui/open-webui/commit/7f7cd210186cb6a67e028c17974eb210fc7ba9fd)

> 🔢 **Bracketed numbers in code blocks.** Numbers in square brackets such as "[0]" inside code blocks are no longer stripped out as if they were source citations, so code displays and copies correctly. [#24948](https://github.com/open-webui/open-webui/issues/24948), [Commit](https://github.com/open-webui/open-webui/commit/e90a618f4555cea2c024bb60c1332ca04eed96da)

> 🔌 **API chat completions reliability.** Direct calls to the chat completions API no longer fail with an internal error when no chat session identifier is supplied. [#24553](https://github.com/open-webui/open-webui/issues/24553), [#25235](https://github.com/open-webui/open-webui/issues/25235), [Commit](https://github.com/open-webui/open-webui/commit/bc244fdc90504824b76654880898bf3f6649c299), [Commit](https://github.com/open-webui/open-webui/commit/f16b5c446027eae1bd767617bac2fdf54b24d6fc)

> 🏷️ **Skill mentions in messages.** Mentioning a skill in a message now keeps the skill's name as readable text instead of removing it, and selecting a skill without typing anything no longer causes an error on providers that reject empty messages. [#24929](https://github.com/open-webui/open-webui/issues/24929), [Commit](https://github.com/open-webui/open-webui/commit/01810e32ad51305ca3247e8f83da95f6e6260f0c)

> 🗑️ **Background tasks stop when a chat is removed.** Deleting or archiving a chat now cancels any in-flight generation or title and tag tasks for it, instead of leaving orphaned background work running. [#25050](https://github.com/open-webui/open-webui/pull/25050), [Commit](https://github.com/open-webui/open-webui/commit/778dba1d6b8dc3962163fa7bf9d802d9a07fba26)

> 🔤 **Non-UTF-8 text and CSV uploads.** Text and CSV files saved in legacy encodings, including Latin-1, Windows-1252, and Chinese encodings such as GB18030, are now detected and loaded correctly instead of being rejected as binary or failing with an empty-content error. [#25172](https://github.com/open-webui/open-webui/issues/25172), [#24973](https://github.com/open-webui/open-webui/issues/24973), [Commit](https://github.com/open-webui/open-webui/commit/6f0277db52d005420480abb0702d421525d6ea8b), [Commit](https://github.com/open-webui/open-webui/commit/1bbb2b933d4cee70a5102eca4109e77b8625f8fc)

> 🧽 **Null bytes in nested data no longer break saves.** Data containing null bytes nested inside structured fields is now sanitized correctly before being written, preventing database errors that the previous check failed to catch. [#25018](https://github.com/open-webui/open-webui/pull/25018), [Commit](https://github.com/open-webui/open-webui/commit/e3ab4bd212e44c39f439ec4ff5df7c3dbd046895)

> ⏳ **Terminal session stability.** The terminal proxy no longer hangs when one direction of the connection closes before the other, so terminal sessions shut down cleanly instead of stalling. [#25464](https://github.com/open-webui/open-webui/issues/25464), [#25479](https://github.com/open-webui/open-webui/pull/25479)

> 🧷 **Tool call continuity with strict providers.** Chats that contain incomplete tool calls or orphaned tool results no longer fail to continue when sent to providers that strictly validate tool pairings, such as Anthropic and AWS Bedrock Converse. [#24758](https://github.com/open-webui/open-webui/issues/24758), [#24940](https://github.com/open-webui/open-webui/issues/24940), [#24798](https://github.com/open-webui/open-webui/pull/24798), [Commit](https://github.com/open-webui/open-webui/commit/cfa6908d579e1f7f202a321289029996130b8411)

> 🪝 **Reliable knowledge base file linking.** Files uploaded to a knowledge collection are now linked on the server as part of the upload itself, so they remain attached to the collection even if you navigate away or close the page before processing finishes. [#24807](https://github.com/open-webui/open-webui/issues/24807), [Commit](https://github.com/open-webui/open-webui/commit/d0b17f056911ec73df2b686a0d92bb789391db27)

> ☁️ **Azure connections on custom hostnames.** Connections marked as the Azure provider now use the Azure code path even when the endpoint does not contain "azure" in its hostname, fixing custom Azure deployments served from non-standard domains. [#24882](https://github.com/open-webui/open-webui/pull/24882), [Commit](https://github.com/open-webui/open-webui/commit/c8f851bd2de3d127f1e818fc116c27174f96d3f1)

> 🗓️ **Clearing calendar event fields.** Removing the description or location from a calendar event now saves correctly instead of silently keeping the previous value. [#25026](https://github.com/open-webui/open-webui/issues/25026), [Commit](https://github.com/open-webui/open-webui/commit/91810f1c4e93d4f559bdf61cd085cadc288a732d), [Commit](https://github.com/open-webui/open-webui/commit/78b1637a035d71099262412e5dee3e4d65c7fb2f)

> 🩺 **Database health check recovery.** After a transient database connection error, the health check endpoint now recovers automatically instead of staying permanently broken on the affected worker. [Commit](https://github.com/open-webui/open-webui/commit/0b81520e072bb4ed15532b8e153b43dd3243feaf)

> 🪵 **JSON exception logging.** With JSON log formatting enabled, exceptions are now recorded correctly with a structured type, message, and stacktrace instead of being dropped, and a logging failure can no longer crash the application. [#25135](https://github.com/open-webui/open-webui/issues/25135), [Commit](https://github.com/open-webui/open-webui/commit/79bf3d28d88e78b0136ef3c3c9f8e7bb85d3cea9)

> 🔁 **Resilient database migrations.** Database migrations now skip tables, indexes, and columns that already exist and add missing primary keys to legacy tables, so upgrades succeed even when parts of the schema were manually or partially created beforehand. [Commit](https://github.com/open-webui/open-webui/commit/81f611fb73c726cfcfc20ee57a926a543f07e95f), [Commit](https://github.com/open-webui/open-webui/commit/f0e88dadc8502ea05b1a00f3155bee7d1cf32249), [Commit](https://github.com/open-webui/open-webui/commit/bd9f82d5a681ee94bde44325033447500a0c76bf), [Commit](https://github.com/open-webui/open-webui/commit/459b1c3fda2ec3579fbd2ab408d0fdeb07c96b99), [Commit](https://github.com/open-webui/open-webui/commit/6df09a4039d181f4e2d41324e93cd36c6fb27dfd), [Commit](https://github.com/open-webui/open-webui/commit/95840e307a66429168775de389b329487a4311c4), [Commit](https://github.com/open-webui/open-webui/commit/6b1df94bf933af92f5c7d093a2d92e2e50d6fdd0), [Commit](https://github.com/open-webui/open-webui/commit/98d3b2308564e2112290773ea240b90419ebb48d), [Commit](https://github.com/open-webui/open-webui/commit/1b9d22e324181b96511a15cbacc40fdbb439ad79), [Commit](https://github.com/open-webui/open-webui/commit/dc0f8ae6f2372b6e5dd42f3520813b09c54146c0), [Commit](https://github.com/open-webui/open-webui/commit/ee3b14233a642ff1bc38aef03a2418afcf5d6c1d), [Commit](https://github.com/open-webui/open-webui/commit/1004dad2749bcc369d511315a808d4bb5277854c), [Commit](https://github.com/open-webui/open-webui/commit/db2b3d7fd86cc7d76424671ead3c62a3f6302fe7), [Commit](https://github.com/open-webui/open-webui/commit/2e1b671e8db49f47d69fd59ece2b58e109ec8b84), [Commit](https://github.com/open-webui/open-webui/commit/9a8969ca93f8c9109d956518a085be3e2afacc07), [Commit](https://github.com/open-webui/open-webui/commit/9717ada92fdb3761a217d309f322ee9fbe418d0d), [Commit](https://github.com/open-webui/open-webui/commit/d7cfc1e46a8f3e5c8f6758c12ef641f41fb51a39), [Commit](https://github.com/open-webui/open-webui/commit/9263b7568eaa83f43e4a118c98490c4f7aaba570), [Commit](https://github.com/open-webui/open-webui/commit/73d2065227e651cf90a2cfade721516815743ab4), [#24722](https://github.com/open-webui/open-webui/pull/24722)

> ⚙️ **Tool-call iteration cap renamed and raised.** The environment variable that limits how many tool calls a single chat response may make is now "CHAT_RESPONSE_MAX_TOOL_CALL_ITERATIONS", with its default raised from 30 to 256 and a new "-1" value for unlimited; the previous "CHAT_RESPONSE_MAX_TOOL_CALL_RETRIES" name continues to work as a fallback, and chats that hit the cap now show a clear error in-chat instead of stopping silently. [#24918](https://github.com/open-webui/open-webui/pull/24918), [Commit](https://github.com/open-webui/open-webui/commit/2b99945d2726bdf5aed7b1712f9e3b7b622671df)

> 🔐 **Reduced public "/api/config" exposure.** The "/api/config" response no longer includes several feature flags ("enable_api_keys", "enable_password_change_form", "enable_version_update_check", "enable_public_active_users_count", "enable_easter_eggs") for unauthenticated callers, reducing information disclosure to anonymous visitors. [Commit](https://github.com/open-webui/open-webui/commit/245e0ee029e9e10617f62953a9e6f67dd00ecf81), [Commit](https://github.com/open-webui/open-webui/commit/ae06e199d5d3f65296a978cc35079bdacba596d2)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-06-01-bulk-enable-or-disable-automations-automations-can-now-be-enabled-or-disabled-in|🔘 Bulk enable or disable automations. Automations can now be enabled or disabled…]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-06-01-4-context-window-changes-in-v0-9-6|4 Context Window changes in v0.9.6]] · Context Window
- [[Changes/Open WebUI/2026-06-01-2-memory-and-personalization-changes-in-v0-9-6|2 Memory and Personalization changes in v0.9.6]] · Memory and Personalization
- [[Changes/Open WebUI/2026-06-01-keyboard-and-screen-reader-access-to-menus-the-integrations-more-options-and-use|♿ Keyboard and screen reader access to menus. The integrations, more-options…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-06-01-4-interface-experience-changes-in-v0-9-6|4 Interface Experience changes in v0.9.6]] · Interface Experience
- [[Changes/Open WebUI/2026-06-01-4-editor-experience-changes-in-v0-9-6|4 Editor Experience changes in v0.9.6]] · Editor Experience
- [[Changes/Open WebUI/2026-06-01-5-files-and-data-changes-in-v0-9-6|5 Files and Data changes in v0.9.6]] · Files and Data
- [[Changes/Open WebUI/2026-06-01-7-safety-and-privacy-changes-in-v0-9-6|7 Safety and Privacy changes in v0.9.6]] · Safety and Privacy
- [[Changes/Open WebUI/2026-06-01-startup-on-non-unicode-consoles-open-webui-no-longer-crashes-at-startup-when-the|🥾 Startup on non-Unicode consoles. Open WebUI no longer crashes at startup…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-06-01-youtube-short-link-transcripts-pasting-a-youtu-be-short-link-into-a-chat-now-loa|📺 YouTube short link transcripts. Pasting a "youtu.be" short link into a chat…]] · Multimodal Input
- [[Changes/Open WebUI/2026-06-01-9-search-and-browsing-changes-in-v0-9-6|9 Search and Browsing changes in v0.9.6]] · Search and Browsing
- [[Changes/Open WebUI/2026-06-01-shared-chat-file-write-protection-access-to-a-file-through-a-shared-chat-now-onl|🔐 Shared-chat file write protection. Access to a file through a shared chat now…]] · Collaboration
- [[Changes/Open WebUI/2026-06-01-2-enterprise-and-administration-changes-in-v0-9-6|2 Enterprise and Administration changes in v0.9.6]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-06-01-image-generation-with-non-standard-response-headers-image-generation-now-works-w|🖌️ Image generation with non-standard response headers. Image generation now…]] · Image Generation
- [[Changes/Open WebUI/2026-06-01-6-account-and-access-changes-in-v0-9-6|6 Account and Access changes in v0.9.6]] · Account and Access
- [[Changes/Open WebUI/2026-06-01-12-model-support-changes-in-v0-9-6|12 Model Support changes in v0.9.6]] · Model Support
- [[Changes/Open WebUI/2026-06-01-4-apps-and-integrations-changes-in-v0-9-6|4 Apps and Integrations changes in v0.9.6]] · Apps and Integrations
- [[Changes/Open WebUI/2026-06-01-5-reliability-and-performance-changes-in-v0-9-6|5 Reliability and Performance changes in v0.9.6]] · Reliability and Performance
- [[Changes/Open WebUI/2026-06-01-4-voice-and-audio-changes-in-v0-9-6|4 Voice and Audio changes in v0.9.6]] · Voice and Audio
- [[Changes/Open WebUI/2026-06-01-20-other-changes-in-v0-9-6|20 other changes in v0.9.6]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-06-01 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-06-01-lsp-show-lsp-test-and-lsp-reload-correctly-discover-project-lsp-config-when-the|/lsp show, /lsp test, and /lsp reload correctly discover project LSP config…]]
- Later: 2026-06-02 · Claude Code · [[Changes/Claude Code/2026-06-02-2-developer-workflow-changes-in-v2-1-160|2 Developer Workflow changes in v2.1.160]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-06-01-2a27f4&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-06-01-27-developer-workflow-changes-in-v0-9-6.md%0ACard%20ID%3A%20open-webui-2026-06-01-2a27f4%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.6%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->