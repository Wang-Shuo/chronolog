---
card_id: open-webui-2026-02-12-525053
date: '2026-02-12'
description: "Open WebUI · 2026-02-12 · Developer Workflow: 27 changes in v0.8.0 —
  \U0001F4E8 **Message queuing.** Messages can now be queued while a response is generating
  rather…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1062
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 53aa7588673f387735caf696a5ea56c8f310b257e55f36a12a314be160bf04b2
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-02-12-525053
  comparison: ''
  date: '2026-02-12'
  description: 'Open WebUI — v0.8.0: 27 Developer Workflow changes'
  evidence:
  - quote: "\U0001F4E8 **Message queuing.** Messages can now be queued while a response
      is generating rather than being blocked, allowing you to continue your train
      of thought; queued messages are automatically combined and sent when generation
      completes, and can be edited, deleted, or sent immediately from the input area.
      [Commit](https://github.com/open-webui/open-webui/commit/62750b8980ef0a3f2da7bc64b5416706a7495686),
      [Commit](https://github.com/open-webui/open-webui/commit/d3f2cf74748db42311ca04a56ccd1ea15399eca0)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F4DD **Prompt version control.** Prompts now include version control
      with full history tracking, allowing users to commit changes with messages,
      view past versions, compare differences between versions, and roll back to previous
      versions when needed. [#20945](https://github.com/open-webui/open-webui/pull/20945)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F91D **Shared chats management.** Users can now view and manage
      all their shared chats from Settings, with options to copy share links or unshare
      conversations they no longer want public. [Commit](https://github.com/open-webui/open-webui/commit/a10ac774ab5d47b505e840b029c0c0340002508b)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F512 **Password-masked valve fields.** Tool and function developers
      can now mark sensitive fields as passwords, which are automatically masked in
      the settings UI to prevent shoulder surfing and accidental exposure. [#20852](https://github.com/open-webui/open-webui/issues/20852),
      [Commit](https://github.com/open-webui/open-webui/commit/8c70453b2e3a6958437d951751e84acbbaafd9aa)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F4CB **Prompt quick copy.** Prompts in the workspace now include
      a quick copy button for easily copying prompt content to the clipboard. [Commit](https://github.com/open-webui/open-webui/commit/78f856e2049991441a3469230ae52799cb86954e)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F514 **Dismissible notification toasts.** Notification toasts for
      new messages and other events now include a close button that appears on hover,
      allowing users to dismiss them immediately instead of waiting for auto-dismissal.
      [#21056](https://github.com/open-webui/open-webui/issues/21056), [Commit](https://github.com/open-webui/open-webui/commit/73bb600034c8532e30726129743a5ffe9002c5fb)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F4E1 **Custom user info headers.** Administrators can now customize
      the header names used when forwarding user information to external services,
      enabling compatibility with services like AWS Bedrock AgentCore that require
      specific header prefixes. [Commit](https://github.com/open-webui/open-webui/commit/6c0f886cdf4b4249dca29e9340b3b998a7262d61)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F4A8 **Batched group member counts.** Group member counts are now
      fetched in a single batch query when loading group lists, eliminating redundant
      database lookups. [Commit](https://github.com/open-webui/open-webui/commit/96c07f44a8f5e6346b2ea6ac529ff4ec3c47e90a)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F381 **Easter eggs toggle.** Administrators can now control the
      visibility of easter egg features via the \"ENABLE_EASTER_EGGS\" environment
      variable. [Commit](https://github.com/open-webui/open-webui/commit/907dba4517903e5646e40223a0edca26a7107bc8)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F6E1️ **SSRF protection for image loading.** External image loading
      now validates URLs before fetching to prevent SSRF attacks against local and
      private network addresses. [Commit](https://github.com/open-webui/open-webui/commit/ce50d9bac4f30b054b09a2fbda52569b73ea591c)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F6E1️ **Malformed Authorization header fix.** Malformed Authorization
      headers no longer cause server crashes; requests are now handled gracefully
      instead of returning HTTP 500 errors. [#20938](https://github.com/open-webui/open-webui/issues/20938),
      [Commit](https://github.com/open-webui/open-webui/commit/7e79f8d1c6b5a02f1a46e792540c6bbf7bed8edc)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F4BB **ANSI code execution fix.** Code execution is now reliable
      when LLMs include ANSI terminal color codes in their output, preventing random
      failures that previously caused syntax errors. [#21091](https://github.com/open-webui/open-webui/issues/21091),
      [Commit](https://github.com/open-webui/open-webui/commit/b1737040a7d3bb5efcfe0f1432e89d7e82e51d2d)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F305 **Dark mode icon inversion fix.** Icons in chat and action
      menus are now displayed correctly in dark mode, fixing an issue where PNG icons
      with \"svg\" in their base64 encoding were randomly inverted. [#21272](https://github.com/open-webui/open-webui/pull/21272),
      [Commit](https://github.com/open-webui/open-webui/commit/0a44d80252afae73de4098ab1c3eb6cf54157fd6)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F6E0️ **Prompt access control save fix.** Prompt access control
      settings are now saved correctly when modifying resource permissions. [Commit](https://github.com/open-webui/open-webui/commit/30f72672fac2579c267a076e6ba89dfe1812137b)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F510 **Group resource sharing fix.** Sharing resources with groups
      now works correctly, fixing database errors and an issue where models shared
      with read-only access were not visible to group members. [#20666](https://github.com/open-webui/open-webui/issues/20666),
      [#21043](https://github.com/open-webui/open-webui/issues/21043), [Commit](https://github.com/open-webui/open-webui/commit/5a075a2c836e46b83f8710285f09aff1f6125072)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: ⚙️ **Persistent config with Redis fix.** Configuration values now respect
      the "ENABLE_PERSISTENT_CONFIG" setting when Redis is used, ensuring environment
      variables are reloaded on restart when persistent config is disabled. [#20830](https://github.com/open-webui/open-webui/issues/20830),
      [Commit](https://github.com/open-webui/open-webui/commit/5d48e48e15b003874cc821d896998a01e87580a0)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F527 **Engine.IO logging fix.** The \"WEBSOCKET_SERVER_ENGINEIO_LOGGING\"
      environment variable now works correctly, allowing administrators to configure
      Engine.IO logging independently from general websocket logging. [#20727](https://github.com/open-webui/open-webui/pull/20727),
      [Commit](https://github.com/open-webui/open-webui/commit/5cfb7a08cbde5d39aaf4097b849a80da87c30d66)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F310 **French language default fix.** Browsers requesting French
      language now default to French (France) instead of French (Canada), matching
      standard language preference expectations. [#20603](https://github.com/open-webui/open-webui/pull/20603),
      [Commit](https://github.com/open-webui/open-webui/commit/4d9a7cc6c0adea54b58046c576250a0c3ae7b512)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F518 **Firefox delete button fix.** Pressing Enter after clicking
      delete buttons no longer incorrectly retriggers confirmation modals in Firefox.
      [Commit](https://github.com/open-webui/open-webui/commit/57a2024c58b9c674f2ae08eeb552994ef1796888)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F4DD **Audit log browser session fix.** Audit logs now properly
      capture all user activity including browser-based sessions, not just API key
      requests. [#20651](https://github.com/open-webui/open-webui/issues/20651), [Commit](https://github.com/open-webui/open-webui/commit/86e6b2b68b85e958188881785495030de1a30402),
      [Commit](https://github.com/open-webui/open-webui/commit/ee5fd1246cb3f8f16ca5cbb24feeea43b7800dcb)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F465 **Admin user filter pagination fix.** Filtering users in the
      admin panel now automatically resets to page 1, preventing empty results when
      searching from pages beyond the first. [#20723](https://github.com/open-webui/open-webui/pull/20723),
      [Commit](https://github.com/open-webui/open-webui/commit/be75bc506adb048ef11b1612c0e3662511c920d0)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F5D1️ **File deletion orphaned embeddings fix.** Deleting files
      now properly removes associated knowledge base embeddings, preventing orphaned
      data from accumulating. [Commit](https://github.com/open-webui/open-webui/commit/93ed4ae2cda2f4311143e51f586aaa73b83a37a7)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F527 **OpenAPI tool import fix.** Importing OpenAPI tool specifications
      no longer crashes when parameters lack explicit name fields, fixing compatibility
      with complex request body definitions. [#21121](https://github.com/open-webui/open-webui/pull/21121),
      [Commit](https://github.com/open-webui/open-webui/commit/8e79b3d0bc4903f30e747b663ac818976618c83c)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F310 **Webpage attachment content fix.** Attaching webpages to chats
      now retrieves full content instead of only metadata, fixing an unawaited coroutine
      in SSL certificate verification. [#21166](https://github.com/open-webui/open-webui/issues/21166),
      [Commit](https://github.com/open-webui/open-webui/commit/a214ec40ea00eebcba49570647ca6ab8f61765d5)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F527 **Batch embeddings endpoint fix.** The '/api/embeddings' endpoint
      now correctly returns separate embeddings for each input string when processing
      batch requests to Ollama providers. [Commit](https://github.com/open-webui/open-webui/commit/8fd5c06e5bf7e0ccbda15d83338912ea17f66783),
      [#21279](https://github.com/open-webui/open-webui/issues/21279)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: ⛔ **OpenAI endpoint detection fix.** OpenAI API endpoint detection was
      corrected to use exact hostname matching instead of substring matching, preventing
      third-party providers with similar URL patterns from being incorrectly filtered.
      [Commit](https://github.com/open-webui/open-webui/commit/423d8b18170a0b92b582aba6ef7bb9ba173e876e)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F6E0️ **RedisCluster task stopping fix.** Task stopping now works
      correctly in RedisCluster deployments, fixing an issue where tasks would remain
      active after cancellation attempts. [#20803](https://github.com/open-webui/open-webui/pull/20803),
      [Commit](https://github.com/open-webui/open-webui/commit/0dcbd05e2436929ae9d2c559a204844ae0239b57)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 27-developer-workflow-changes-in-v0-8-0
  source_release: open-webui-2026-02-12-v0-8-0-github-285910626-490914ba
  source_type: github_releases
  theme: developer-workflow
  title: 27 Developer Workflow changes in v0.8.0
  type: change
related_changes:
- '[[Changes/Cline/2026-02-12-terminal-surface-command-exit-codes-in-results-and-improve-long-running-execute|Terminal:
  surface command exit codes in results and improve long-running…]]'
- '[[Changes/Codex CLI/2026-02-12-11412-tui-show-non-file-layer-content-in-debug-config-bolinfest|♯11412
  tui: show non-file layer content in /debug-config @bolinfest]]'
- '[[Changes/GitHub Copilot CLI/2026-02-12-change-run-command-shortcut-from-ctrl-p-to-ctrl-s|Change
  run command shortcut from ctrl+p to ctrl+s]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-02-12-v0-8-0-github-285910626-490914ba|open-webui-2026-02-12-v0-8-0-github-285910626-490914ba]]'
source_type: github_releases
theme: developer-workflow
title: 27 Developer Workflow changes in v0.8.0
type: change
---

<!-- chronolog:begin region="header" -->
# 27 Developer Workflow changes in v0.8.0

**Open WebUI** · 2026-02-12 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.0) · from [[Releases/Open WebUI/open-webui-2026-02-12-v0-8-0-github-285910626-490914ba|v0.8.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📨 **Message queuing.** Messages can now be queued while a response is generating rather than being blocked, allowing you to continue your train of thought; queued messages are automatically combined and sent when generation completes, and can be edited, deleted, or sent immediately from the input area. [Commit](https://github.com/open-webui/open-webui/commit/62750b8980ef0a3f2da7bc64b5416706a7495686), [Commit](https://github.com/open-webui/open-webui/commit/d3f2cf74748db42311ca04a56ccd1ea15399eca0)

> 📝 **Prompt version control.** Prompts now include version control with full history tracking, allowing users to commit changes with messages, view past versions, compare differences between versions, and roll back to previous versions when needed. [#20945](https://github.com/open-webui/open-webui/pull/20945)

> 🤝 **Shared chats management.** Users can now view and manage all their shared chats from Settings, with options to copy share links or unshare conversations they no longer want public. [Commit](https://github.com/open-webui/open-webui/commit/a10ac774ab5d47b505e840b029c0c0340002508b)

> 🔒 **Password-masked valve fields.** Tool and function developers can now mark sensitive fields as passwords, which are automatically masked in the settings UI to prevent shoulder surfing and accidental exposure. [#20852](https://github.com/open-webui/open-webui/issues/20852), [Commit](https://github.com/open-webui/open-webui/commit/8c70453b2e3a6958437d951751e84acbbaafd9aa)

> 📋 **Prompt quick copy.** Prompts in the workspace now include a quick copy button for easily copying prompt content to the clipboard. [Commit](https://github.com/open-webui/open-webui/commit/78f856e2049991441a3469230ae52799cb86954e)

> 🔔 **Dismissible notification toasts.** Notification toasts for new messages and other events now include a close button that appears on hover, allowing users to dismiss them immediately instead of waiting for auto-dismissal. [#21056](https://github.com/open-webui/open-webui/issues/21056), [Commit](https://github.com/open-webui/open-webui/commit/73bb600034c8532e30726129743a5ffe9002c5fb)

> 📡 **Custom user info headers.** Administrators can now customize the header names used when forwarding user information to external services, enabling compatibility with services like AWS Bedrock AgentCore that require specific header prefixes. [Commit](https://github.com/open-webui/open-webui/commit/6c0f886cdf4b4249dca29e9340b3b998a7262d61)

> 💨 **Batched group member counts.** Group member counts are now fetched in a single batch query when loading group lists, eliminating redundant database lookups. [Commit](https://github.com/open-webui/open-webui/commit/96c07f44a8f5e6346b2ea6ac529ff4ec3c47e90a)

> 🎁 **Easter eggs toggle.** Administrators can now control the visibility of easter egg features via the "ENABLE_EASTER_EGGS" environment variable. [Commit](https://github.com/open-webui/open-webui/commit/907dba4517903e5646e40223a0edca26a7107bc8)

> 🛡️ **SSRF protection for image loading.** External image loading now validates URLs before fetching to prevent SSRF attacks against local and private network addresses. [Commit](https://github.com/open-webui/open-webui/commit/ce50d9bac4f30b054b09a2fbda52569b73ea591c)

> 🛡️ **Malformed Authorization header fix.** Malformed Authorization headers no longer cause server crashes; requests are now handled gracefully instead of returning HTTP 500 errors. [#20938](https://github.com/open-webui/open-webui/issues/20938), [Commit](https://github.com/open-webui/open-webui/commit/7e79f8d1c6b5a02f1a46e792540c6bbf7bed8edc)

> 💻 **ANSI code execution fix.** Code execution is now reliable when LLMs include ANSI terminal color codes in their output, preventing random failures that previously caused syntax errors. [#21091](https://github.com/open-webui/open-webui/issues/21091), [Commit](https://github.com/open-webui/open-webui/commit/b1737040a7d3bb5efcfe0f1432e89d7e82e51d2d)

> 🌅 **Dark mode icon inversion fix.** Icons in chat and action menus are now displayed correctly in dark mode, fixing an issue where PNG icons with "svg" in their base64 encoding were randomly inverted. [#21272](https://github.com/open-webui/open-webui/pull/21272), [Commit](https://github.com/open-webui/open-webui/commit/0a44d80252afae73de4098ab1c3eb6cf54157fd6)

> 🛠️ **Prompt access control save fix.** Prompt access control settings are now saved correctly when modifying resource permissions. [Commit](https://github.com/open-webui/open-webui/commit/30f72672fac2579c267a076e6ba89dfe1812137b)

> 🔐 **Group resource sharing fix.** Sharing resources with groups now works correctly, fixing database errors and an issue where models shared with read-only access were not visible to group members. [#20666](https://github.com/open-webui/open-webui/issues/20666), [#21043](https://github.com/open-webui/open-webui/issues/21043), [Commit](https://github.com/open-webui/open-webui/commit/5a075a2c836e46b83f8710285f09aff1f6125072)

> ⚙️ **Persistent config with Redis fix.** Configuration values now respect the "ENABLE_PERSISTENT_CONFIG" setting when Redis is used, ensuring environment variables are reloaded on restart when persistent config is disabled. [#20830](https://github.com/open-webui/open-webui/issues/20830), [Commit](https://github.com/open-webui/open-webui/commit/5d48e48e15b003874cc821d896998a01e87580a0)

> 🔧 **Engine.IO logging fix.** The "WEBSOCKET_SERVER_ENGINEIO_LOGGING" environment variable now works correctly, allowing administrators to configure Engine.IO logging independently from general websocket logging. [#20727](https://github.com/open-webui/open-webui/pull/20727), [Commit](https://github.com/open-webui/open-webui/commit/5cfb7a08cbde5d39aaf4097b849a80da87c30d66)

> 🌐 **French language default fix.** Browsers requesting French language now default to French (France) instead of French (Canada), matching standard language preference expectations. [#20603](https://github.com/open-webui/open-webui/pull/20603), [Commit](https://github.com/open-webui/open-webui/commit/4d9a7cc6c0adea54b58046c576250a0c3ae7b512)

> 🔘 **Firefox delete button fix.** Pressing Enter after clicking delete buttons no longer incorrectly retriggers confirmation modals in Firefox. [Commit](https://github.com/open-webui/open-webui/commit/57a2024c58b9c674f2ae08eeb552994ef1796888)

> 📝 **Audit log browser session fix.** Audit logs now properly capture all user activity including browser-based sessions, not just API key requests. [#20651](https://github.com/open-webui/open-webui/issues/20651), [Commit](https://github.com/open-webui/open-webui/commit/86e6b2b68b85e958188881785495030de1a30402), [Commit](https://github.com/open-webui/open-webui/commit/ee5fd1246cb3f8f16ca5cbb24feeea43b7800dcb)

> 👥 **Admin user filter pagination fix.** Filtering users in the admin panel now automatically resets to page 1, preventing empty results when searching from pages beyond the first. [#20723](https://github.com/open-webui/open-webui/pull/20723), [Commit](https://github.com/open-webui/open-webui/commit/be75bc506adb048ef11b1612c0e3662511c920d0)

> 🗑️ **File deletion orphaned embeddings fix.** Deleting files now properly removes associated knowledge base embeddings, preventing orphaned data from accumulating. [Commit](https://github.com/open-webui/open-webui/commit/93ed4ae2cda2f4311143e51f586aaa73b83a37a7)

> 🔧 **OpenAPI tool import fix.** Importing OpenAPI tool specifications no longer crashes when parameters lack explicit name fields, fixing compatibility with complex request body definitions. [#21121](https://github.com/open-webui/open-webui/pull/21121), [Commit](https://github.com/open-webui/open-webui/commit/8e79b3d0bc4903f30e747b663ac818976618c83c)

> 🌐 **Webpage attachment content fix.** Attaching webpages to chats now retrieves full content instead of only metadata, fixing an unawaited coroutine in SSL certificate verification. [#21166](https://github.com/open-webui/open-webui/issues/21166), [Commit](https://github.com/open-webui/open-webui/commit/a214ec40ea00eebcba49570647ca6ab8f61765d5)

> 🔧 **Batch embeddings endpoint fix.** The '/api/embeddings' endpoint now correctly returns separate embeddings for each input string when processing batch requests to Ollama providers. [Commit](https://github.com/open-webui/open-webui/commit/8fd5c06e5bf7e0ccbda15d83338912ea17f66783), [#21279](https://github.com/open-webui/open-webui/issues/21279)

> ⛔ **OpenAI endpoint detection fix.** OpenAI API endpoint detection was corrected to use exact hostname matching instead of substring matching, preventing third-party providers with similar URL patterns from being incorrectly filtered. [Commit](https://github.com/open-webui/open-webui/commit/423d8b18170a0b92b582aba6ef7bb9ba173e876e)

> 🛠️ **RedisCluster task stopping fix.** Task stopping now works correctly in RedisCluster deployments, fixing an issue where tasks would remain active after cancellation attempts. [#20803](https://github.com/open-webui/open-webui/pull/20803), [Commit](https://github.com/open-webui/open-webui/commit/0dcbd05e2436929ae9d2c559a204844ae0239b57)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-02-12-16-reliability-and-performance-changes-in-v0-8-0|16 Reliability and Performance changes in v0.8.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-02-12-audio-service-timeout-handling-audio-transcription-and-text-to-speech-requests-n|🔌 Audio service timeout handling. Audio transcription and text-to-speech…]] · Voice and Audio
- [[Changes/Open WebUI/2026-02-12-2-editor-experience-changes-in-v0-8-0|2 Editor Experience changes in v0.8.0]] · Editor Experience
- [[Changes/Open WebUI/2026-02-12-5-safety-and-privacy-changes-in-v0-8-0|5 Safety and Privacy changes in v0.8.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-02-12-19-model-support-changes-in-v0-8-0|19 Model Support changes in v0.8.0]] · Model Support
- [[Changes/Open WebUI/2026-02-12-5-context-window-changes-in-v0-8-0|5 Context Window changes in v0.8.0]] · Context Window
- [[Changes/Open WebUI/2026-02-12-2-image-generation-changes-in-v0-8-0|2 Image Generation changes in v0.8.0]] · Image Generation
- [[Changes/Open WebUI/2026-02-12-2-memory-and-personalization-changes-in-v0-8-0|2 Memory and Personalization changes in v0.8.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-02-12-gboard-multi-line-paste-fix-multi-line-text-pasted-from-gboard-on-android-now-in|📱 Gboard multi-line paste fix. Multi-line text pasted from Gboard on Android now…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-02-12-2-collaboration-changes-in-v0-8-0|2 Collaboration changes in v0.8.0]] · Collaboration
- [[Changes/Open WebUI/2026-02-12-6-account-and-access-changes-in-v0-8-0|6 Account and Access changes in v0.8.0]] · Account and Access
- [[Changes/Open WebUI/2026-02-12-async-pipeline-operations-pipeline-operations-now-run-asynchronously-instead-of|🔧 Async pipeline operations. Pipeline operations now run asynchronously instead…]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-02-12-5-search-and-browsing-changes-in-v0-8-0|5 Search and Browsing changes in v0.8.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-02-12-8-interface-experience-changes-in-v0-8-0|8 Interface Experience changes in v0.8.0]] · Interface Experience
- [[Changes/Open WebUI/2026-02-12-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-02-12-screen-reader-accessibility-screen-reader-users-now-hear-the-password-field-labe|♿ Screen reader accessibility. Screen reader users now hear the password field…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-02-12-10-files-and-data-changes-in-v0-8-0|10 Files and Data changes in v0.8.0]] · Files and Data
- [[Changes/Open WebUI/2026-02-12-6-apps-and-integrations-changes-in-v0-8-0|6 Apps and Integrations changes in v0.8.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-02-12-29-other-changes-in-v0-8-0|29 other changes in v0.8.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-02-12 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-02-12-change-run-command-shortcut-from-ctrl-p-to-ctrl-s|Change run command shortcut from ctrl+p to ctrl+s]]
- Later: 2026-02-12 · OpenCode · [[Changes/OpenCode/2026-02-12-2-developer-workflow-changes-in-v1-1-64-1|2 Developer Workflow changes in v1.1.64 + 1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-02-12-525053&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-02-12-27-developer-workflow-changes-in-v0-8-0.md%0ACard%20ID%3A%20open-webui-2026-02-12-525053%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->