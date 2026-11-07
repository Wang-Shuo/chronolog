---
card_id: open-webui-2026-03-25-e9e881
date: '2026-03-25'
description: "Open WebUI · 2026-03-25 · Developer Workflow: 34 changes in v0.8.11
  — \U0001F500 **Responses API stateful sessions.** Administrators can now enable
  experimental…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2752
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: bfd1a2233c1b895b65a488a3151356dde7b773f3f172769a64953918d7f9decd
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-03-25-e9e881
  comparison: ''
  date: '2026-03-25'
  description: 'Open WebUI — v0.8.11: 34 Developer Workflow changes'
  evidence:
  - quote: "\U0001F500 **Responses API stateful sessions.** Administrators can now
      enable experimental stateful session support via the ENABLE_RESPONSES_API_STATEFUL
      environment variable, allowing compatible backends to store responses server-side
      with previous_response_id anchoring for improved multi-turn conversations. [Commit](https://github.com/open-webui/open-webui/commit/dfc2dc2c0bd298cb4bfcf212ef11223586aa54f1)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F9E9 **Model and filter lookup optimization.** Model and filter
      membership lookups are now faster thanks to optimized data structure operations
      during model list loading. [Commit](https://github.com/open-webui/open-webui/commit/7eae377c01f8d2de94a694b72279f769c82658cd)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F9EA **Terminal connection verification.** Users can now verify
      their terminal server connection is working before saving the configuration,
      making setup more reliable. [#22567](https://github.com/open-webui/open-webui/pull/22567)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F529 **Tool server timeout configuration.** Administrators can now
      configure a separate HTTP timeout for tool server requests via the AIOHTTP_CLIENT_TIMEOUT_TOOL_SERVER
      environment variable, enabling fine-tuned control over how long tool calls are
      allowed to take. [Commit](https://github.com/open-webui/open-webui/commit/a3238aa79f344765f5b62cb64eba71ffd001abaf)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F3AF **Knowledge tool hybrid search support.** The built-in query_knowledge_files
      tool now respects hybrid search and reranking settings, matching the behavior
      of the middleware RAG pipeline. [Commit](https://github.com/open-webui/open-webui/commit/9a2c60d5954ecbc172d09e9955d52a07d135dcbc)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F5E3️ **Temporary chat folder support.** Temporary chats can now
      use folder-level system prompts and knowledge files, making them more powerful
      for quick explorations. [Commit](https://github.com/open-webui/open-webui/commit/adcc50d3370301afd5561e0f58ff6f3ab3750818)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F5D1️ **Delete connection confirmations.** Users are now prompted
      with a confirmation dialog before deleting connections, preventing accidental
      deletions. [Commit](https://github.com/open-webui/open-webui/commit/157ff57c40bc40c53bc608828dac3779e95c2ffa)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F4E6 **SBOM generation script.** A new script for generating CycloneDX
      Software Bill of Materials is now available in the scripts directory. [Commit](https://github.com/open-webui/open-webui/commit/39100eca4915e4fe86a6912aa97dde86ed72e015)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: ⚙️ **Ruff linter and formatter.** Added Ruff as the Python linter and formatter,
      replacing the black-based workflow for better code quality with near-instant
      execution. [#22576](https://github.com/open-webui/open-webui/pull/22576), [#22462](https://github.com/open-webui/open-webui/discussions/22462)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F5A5️ **Offline code formatting support.** The black formatter for
      Python code editing is now bundled locally in the Docker image, enabling code
      formatting to work in air-gapped deployments where client browsers cannot reach
      PyPI. Formatting failures no longer block saves, allowing code to be preserved
      even when offline. [#22509](https://github.com/open-webui/open-webui/issues/22509),
      [Commit](https://github.com/open-webui/open-webui/commit/8507e5eb0d18896f1bbf990a00a4361aec171a30)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F587 **Web fetch content length config.** Administrators can now
      configure the maximum characters to return from fetched URLs via WEB_FETCH_MAX_CONTENT_LENGTH
      environment variable or the admin settings page, instead of the previous hardcoded
      50K limit. [Commit](https://github.com/open-webui/open-webui/commit/b171b0216b916745420c7caf513093a315ed9560),
      [#22774](https://github.com/open-webui/open-webui/issues/22774)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: ⌨️ **Terminal system prompts.** Terminal servers can now provide custom
      system prompts that are automatically included when their tools are used. [Commit](https://github.com/open-webui/open-webui/commit/6a9d67b5bb4c93fd343b334bee3e37703dff59f6)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F4BE **Terminal state persistence.** The selected terminal server
      and its enabled state now persist across page loads, making terminal usage more
      seamless. [Commit](https://github.com/open-webui/open-webui/commit/d577ff1e4af750dda09e558dac7edb8dd2470850)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F4BE **Terminal folder downloads.** Users can now download folders
      as ZIP archives and bulk-download multiple selected files as a single ZIP directly
      from the File Navigator toolbar, making file exports faster and more convenient.
      [Commit](https://github.com/open-webui/open-webui/commit/3841e85abb3ea3e8d8b364dff0102f0124844d22),
      [Commit](https://github.com/open-webui/open-webui/commit/cf60b1882f1929200649b59f867289dea54e4210)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F3AA **Collapsible tool and thinking groups.** Consecutive tool
      calls and reasoning blocks are now grouped into a single collapsible summary
      (e.g., \"Explored tool1, tool2\"), keeping chat responses clean and readable
      while preserving full detail on expand. [#21604](https://github.com/open-webui/open-webui/issues/21604),
      [Commit](https://github.com/open-webui/open-webui/commit/261aec8c864646eb7215be0d5c14a79cad3cb93f)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F6E1️ **Tool configuration access control.** Tool configuration
      endpoints now properly verify user permissions, preventing unauthorized access
      to tool settings. [Commit](https://github.com/open-webui/open-webui/commit/bc5b3ec6b8ec0fef894eb8046c636ee33688b8c4)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F5DD️ **Tool valves access control.** The tool user valves endpoints
      now properly verify ownership and access grants before returning or updating
      configuration, with appropriate 404 responses for missing tools and 401 for
      unauthorized access. [Commit](https://github.com/open-webui/open-webui/commit/f949d17db1e62e0b79aecbbcbcabe3d57d8d4af6)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F510 **Forwarded allow IPs configuration.** The FORWARDED_ALLOW_IPS
      environment variable is now properly respected by the startup scripts instead
      of being hardcoded to '\\*', allowing administrators to restrict which proxies
      are trusted for request forwarding. [#22539](https://github.com/open-webui/open-webui/issues/22539),
      [Commit](https://github.com/open-webui/open-webui/commit/0aebdd5f83cd1d811009edcbb2bec432a34e7c81)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F504 **Paginated list duplicates.** Fixed duplicate items appearing
      in paginated lists when loading more items in chats, knowledge, notes, and search
      across the UI. [Commit](https://github.com/open-webui/open-webui/commit/58e78e8946fb3644107489fe8e01b17709302b2f)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F529 **Tool server index bounds checking.** Tool servers with invalid
      indices no longer crash the application with IndexError after upgrades, preventing
      tool server configuration loss. [#22490](https://github.com/open-webui/open-webui/issues/22490),
      [Commit](https://github.com/open-webui/open-webui/commit/8da29566a1f81c38e80009bdea3ce4d9be860605)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F50C **Tool server frontend timeout.** Fetch requests to external
      tool servers now time out after 10 seconds, preventing the UI from hanging indefinitely
      when a configured tool server is unreachable. [#22543](https://github.com/open-webui/open-webui/issues/22543),
      [Commit](https://github.com/open-webui/open-webui/commit/adf7af34ff934319a35470c572237d2d08f1de0b)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: ⏱️ **Chat action button timing.** Action buttons under assistant messages
      no longer appear prematurely when switching chats while a response is still
      streaming. [Commit](https://github.com/open-webui/open-webui/commit/ecba37070d6eb3cb033195a070b6c4ab5f396415),
      [#22891](https://github.com/open-webui/open-webui/issues/22891)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F9EE **Logit bias parameter handling.** Using logit_bias parameters
      no longer causes errors when the input is already in dictionary format. [#22597](https://github.com/open-webui/open-webui/issues/22597),
      [Commit](https://github.com/open-webui/open-webui/commit/e34ed72e1e958505e940b74bf1c6a4808640bd17)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001FA9B **Temp chat tool calling.** Temporary chats now properly preserve
      tool call information, fixing native tool calling with JSON schema that was
      previously broken. [#22475](https://github.com/open-webui/open-webui/pull/22475),
      [Commit](https://github.com/open-webui/open-webui/commit/bcd313c363ca50d71aa80bcb2f29c81fad3dff37)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F4DC **Public note access.** Opening public notes via direct share
      link no longer returns a 500 error caused by a missing function import. [#22680](https://github.com/open-webui/open-webui/issues/22680),
      [Commit](https://github.com/open-webui/open-webui/commit/566e25569e5e7d9c1e42db840ba4ba578887d208)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F464 **Terminal access user visibility.** The terminal connection
      access dialog now shows the currently logged-in user when searching for users
      to grant access, fixing an issue where users with identical display names were
      filtered incorrectly. [#22491](https://github.com/open-webui/open-webui/issues/22491),
      [Commit](https://github.com/open-webui/open-webui/commit/4a8f995c3fd4602ec2aaccc07efc4e8504dda84d)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F5C4️ **Oracle 23AI hybrid search.** Fixed an UnboundLocalError
      that occurred when using hybrid search with Oracle 23AI as the vector store,
      preventing knowledge base queries from failing. [Commit](https://github.com/open-webui/open-webui/commit/fcf720835285a4cea10fc1ebed0b454971463b20),
      [#22616](https://github.com/open-webui/open-webui/issues/22616)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F310 **Dynamic HTML language attribute.** The HTML lang attribute
      now dynamically updates when users change their interface language, preventing
      browsers from triggering unwanted translation popups. [Commit](https://github.com/open-webui/open-webui/commit/de5e0fbc00e7abcd84e1272c301b0707f8ea5ac6)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F5C2️ **Reasoning block copy cleanup.** Copied chat responses no
      longer include reasoning block content or excess whitespace, ensuring only the
      intended message text is captured. [#22786](https://github.com/open-webui/open-webui/issues/22786),
      [Commit](https://github.com/open-webui/open-webui/commit/4f0e57420154800946394bc986b2c691462b2782)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F47B **Response message skeleton display.** Fixed an issue where
      the skeleton loader would incorrectly show or hide based on complex status history
      conditions, by extracting the visibility logic into a cleaner reactive variable.
      [Commit](https://github.com/open-webui/open-webui/commit/5df4277216fbb9de603fdf4289f8366292568234)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F3A7 **Read Aloud in chat preview.** The Read Aloud button in the
      Search Chats modal preview no longer causes crashes, and TTS functionality is
      now properly hidden in read-only chat contexts. [Commit](https://github.com/open-webui/open-webui/commit/d8fa0f426a88f5c27b3216b7db35e1db47bbba28)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F5DD️ **Message upsert API reliability.** The message upsert API
      endpoint no longer crashes when called, fixing an error where a database session
      was incorrectly passed to a function that doesn't accept it. [#22959](https://github.com/open-webui/open-webui/issues/22959),
      [Commit](https://github.com/open-webui/open-webui/commit/70285fb6cad26b50d783583b68be5227ace16055)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F503 **Tool call streaming display.** Sequential tool calls are
      now properly accumulated during streaming, fixing an issue where completed tool
      calls could disappear from the display before the next tool call finished streaming.
      [Commit](https://github.com/open-webui/open-webui/commit/a9c5c787b9f6b10491924d38645042064b3c941e)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001FA9D **User webhooks disabled by default.** User webhook notifications
      are now disabled by default and properly gated by the ENABLE_USER_WEBHOOKS configuration,
      ensuring webhooks only fire when explicitly enabled. [Commit](https://github.com/open-webui/open-webui/commit/c24a4da17dbaddf47e2e0f865c1d602d0ff36ee6)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 34-developer-workflow-changes-in-v0-8-11
  source_release: open-webui-2026-03-25-v0-8-11-github-301478856-55ceba69
  source_type: github_releases
  theme: developer-workflow
  title: 34 Developer Workflow changes in v0.8.11
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-03-23-2-developer-workflow-changes-in-v1-0-11|2
  Developer Workflow changes in v1.0.11]]'
- '[[Changes/Devin/2026-03-24-streaming-shell-output-in-worklog|Streaming Shell Output
  in Worklog]]'
- '[[Changes/Gemini CLI/2026-03-24-feat-skills-improve-async-pr-review-workflow-and-logging-by-mattkorwel-in-https|feat(skills):
  improve async-pr-review workflow and logging]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-03-25-v0-8-11-github-301478856-55ceba69|open-webui-2026-03-25-v0-8-11-github-301478856-55ceba69]]'
source_type: github_releases
theme: developer-workflow
title: 34 Developer Workflow changes in v0.8.11
type: change
---

<!-- chronolog:begin region="header" -->
# 34 Developer Workflow changes in v0.8.11

**Open WebUI** · 2026-03-25 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.11) · from [[Releases/Open WebUI/open-webui-2026-03-25-v0-8-11-github-301478856-55ceba69|v0.8.11]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔀 **Responses API stateful sessions.** Administrators can now enable experimental stateful session support via the ENABLE_RESPONSES_API_STATEFUL environment variable, allowing compatible backends to store responses server-side with previous_response_id anchoring for improved multi-turn conversations. [Commit](https://github.com/open-webui/open-webui/commit/dfc2dc2c0bd298cb4bfcf212ef11223586aa54f1)

> 🧩 **Model and filter lookup optimization.** Model and filter membership lookups are now faster thanks to optimized data structure operations during model list loading. [Commit](https://github.com/open-webui/open-webui/commit/7eae377c01f8d2de94a694b72279f769c82658cd)

> 🧪 **Terminal connection verification.** Users can now verify their terminal server connection is working before saving the configuration, making setup more reliable. [#22567](https://github.com/open-webui/open-webui/pull/22567)

> 🔩 **Tool server timeout configuration.** Administrators can now configure a separate HTTP timeout for tool server requests via the AIOHTTP_CLIENT_TIMEOUT_TOOL_SERVER environment variable, enabling fine-tuned control over how long tool calls are allowed to take. [Commit](https://github.com/open-webui/open-webui/commit/a3238aa79f344765f5b62cb64eba71ffd001abaf)

> 🎯 **Knowledge tool hybrid search support.** The built-in query_knowledge_files tool now respects hybrid search and reranking settings, matching the behavior of the middleware RAG pipeline. [Commit](https://github.com/open-webui/open-webui/commit/9a2c60d5954ecbc172d09e9955d52a07d135dcbc)

> 🗣️ **Temporary chat folder support.** Temporary chats can now use folder-level system prompts and knowledge files, making them more powerful for quick explorations. [Commit](https://github.com/open-webui/open-webui/commit/adcc50d3370301afd5561e0f58ff6f3ab3750818)

> 🗑️ **Delete connection confirmations.** Users are now prompted with a confirmation dialog before deleting connections, preventing accidental deletions. [Commit](https://github.com/open-webui/open-webui/commit/157ff57c40bc40c53bc608828dac3779e95c2ffa)

> 📦 **SBOM generation script.** A new script for generating CycloneDX Software Bill of Materials is now available in the scripts directory. [Commit](https://github.com/open-webui/open-webui/commit/39100eca4915e4fe86a6912aa97dde86ed72e015)

> ⚙️ **Ruff linter and formatter.** Added Ruff as the Python linter and formatter, replacing the black-based workflow for better code quality with near-instant execution. [#22576](https://github.com/open-webui/open-webui/pull/22576), [#22462](https://github.com/open-webui/open-webui/discussions/22462)

> 🖥️ **Offline code formatting support.** The black formatter for Python code editing is now bundled locally in the Docker image, enabling code formatting to work in air-gapped deployments where client browsers cannot reach PyPI. Formatting failures no longer block saves, allowing code to be preserved even when offline. [#22509](https://github.com/open-webui/open-webui/issues/22509), [Commit](https://github.com/open-webui/open-webui/commit/8507e5eb0d18896f1bbf990a00a4361aec171a30)

> 🖇 **Web fetch content length config.** Administrators can now configure the maximum characters to return from fetched URLs via WEB_FETCH_MAX_CONTENT_LENGTH environment variable or the admin settings page, instead of the previous hardcoded 50K limit. [Commit](https://github.com/open-webui/open-webui/commit/b171b0216b916745420c7caf513093a315ed9560), [#22774](https://github.com/open-webui/open-webui/issues/22774)

> ⌨️ **Terminal system prompts.** Terminal servers can now provide custom system prompts that are automatically included when their tools are used. [Commit](https://github.com/open-webui/open-webui/commit/6a9d67b5bb4c93fd343b334bee3e37703dff59f6)

> 💾 **Terminal state persistence.** The selected terminal server and its enabled state now persist across page loads, making terminal usage more seamless. [Commit](https://github.com/open-webui/open-webui/commit/d577ff1e4af750dda09e558dac7edb8dd2470850)

> 💾 **Terminal folder downloads.** Users can now download folders as ZIP archives and bulk-download multiple selected files as a single ZIP directly from the File Navigator toolbar, making file exports faster and more convenient. [Commit](https://github.com/open-webui/open-webui/commit/3841e85abb3ea3e8d8b364dff0102f0124844d22), [Commit](https://github.com/open-webui/open-webui/commit/cf60b1882f1929200649b59f867289dea54e4210)

> 🎪 **Collapsible tool and thinking groups.** Consecutive tool calls and reasoning blocks are now grouped into a single collapsible summary (e.g., "Explored tool1, tool2"), keeping chat responses clean and readable while preserving full detail on expand. [#21604](https://github.com/open-webui/open-webui/issues/21604), [Commit](https://github.com/open-webui/open-webui/commit/261aec8c864646eb7215be0d5c14a79cad3cb93f)

> 🛡️ **Tool configuration access control.** Tool configuration endpoints now properly verify user permissions, preventing unauthorized access to tool settings. [Commit](https://github.com/open-webui/open-webui/commit/bc5b3ec6b8ec0fef894eb8046c636ee33688b8c4)

> 🗝️ **Tool valves access control.** The tool user valves endpoints now properly verify ownership and access grants before returning or updating configuration, with appropriate 404 responses for missing tools and 401 for unauthorized access. [Commit](https://github.com/open-webui/open-webui/commit/f949d17db1e62e0b79aecbbcbcabe3d57d8d4af6)

> 🔐 **Forwarded allow IPs configuration.** The FORWARDED_ALLOW_IPS environment variable is now properly respected by the startup scripts instead of being hardcoded to '\*', allowing administrators to restrict which proxies are trusted for request forwarding. [#22539](https://github.com/open-webui/open-webui/issues/22539), [Commit](https://github.com/open-webui/open-webui/commit/0aebdd5f83cd1d811009edcbb2bec432a34e7c81)

> 🔄 **Paginated list duplicates.** Fixed duplicate items appearing in paginated lists when loading more items in chats, knowledge, notes, and search across the UI. [Commit](https://github.com/open-webui/open-webui/commit/58e78e8946fb3644107489fe8e01b17709302b2f)

> 🔩 **Tool server index bounds checking.** Tool servers with invalid indices no longer crash the application with IndexError after upgrades, preventing tool server configuration loss. [#22490](https://github.com/open-webui/open-webui/issues/22490), [Commit](https://github.com/open-webui/open-webui/commit/8da29566a1f81c38e80009bdea3ce4d9be860605)

> 🔌 **Tool server frontend timeout.** Fetch requests to external tool servers now time out after 10 seconds, preventing the UI from hanging indefinitely when a configured tool server is unreachable. [#22543](https://github.com/open-webui/open-webui/issues/22543), [Commit](https://github.com/open-webui/open-webui/commit/adf7af34ff934319a35470c572237d2d08f1de0b)

> ⏱️ **Chat action button timing.** Action buttons under assistant messages no longer appear prematurely when switching chats while a response is still streaming. [Commit](https://github.com/open-webui/open-webui/commit/ecba37070d6eb3cb033195a070b6c4ab5f396415), [#22891](https://github.com/open-webui/open-webui/issues/22891)

> 🧮 **Logit bias parameter handling.** Using logit_bias parameters no longer causes errors when the input is already in dictionary format. [#22597](https://github.com/open-webui/open-webui/issues/22597), [Commit](https://github.com/open-webui/open-webui/commit/e34ed72e1e958505e940b74bf1c6a4808640bd17)

> 🪛 **Temp chat tool calling.** Temporary chats now properly preserve tool call information, fixing native tool calling with JSON schema that was previously broken. [#22475](https://github.com/open-webui/open-webui/pull/22475), [Commit](https://github.com/open-webui/open-webui/commit/bcd313c363ca50d71aa80bcb2f29c81fad3dff37)

> 📜 **Public note access.** Opening public notes via direct share link no longer returns a 500 error caused by a missing function import. [#22680](https://github.com/open-webui/open-webui/issues/22680), [Commit](https://github.com/open-webui/open-webui/commit/566e25569e5e7d9c1e42db840ba4ba578887d208)

> 👤 **Terminal access user visibility.** The terminal connection access dialog now shows the currently logged-in user when searching for users to grant access, fixing an issue where users with identical display names were filtered incorrectly. [#22491](https://github.com/open-webui/open-webui/issues/22491), [Commit](https://github.com/open-webui/open-webui/commit/4a8f995c3fd4602ec2aaccc07efc4e8504dda84d)

> 🗄️ **Oracle 23AI hybrid search.** Fixed an UnboundLocalError that occurred when using hybrid search with Oracle 23AI as the vector store, preventing knowledge base queries from failing. [Commit](https://github.com/open-webui/open-webui/commit/fcf720835285a4cea10fc1ebed0b454971463b20), [#22616](https://github.com/open-webui/open-webui/issues/22616)

> 🌐 **Dynamic HTML language attribute.** The HTML lang attribute now dynamically updates when users change their interface language, preventing browsers from triggering unwanted translation popups. [Commit](https://github.com/open-webui/open-webui/commit/de5e0fbc00e7abcd84e1272c301b0707f8ea5ac6)

> 🗂️ **Reasoning block copy cleanup.** Copied chat responses no longer include reasoning block content or excess whitespace, ensuring only the intended message text is captured. [#22786](https://github.com/open-webui/open-webui/issues/22786), [Commit](https://github.com/open-webui/open-webui/commit/4f0e57420154800946394bc986b2c691462b2782)

> 👻 **Response message skeleton display.** Fixed an issue where the skeleton loader would incorrectly show or hide based on complex status history conditions, by extracting the visibility logic into a cleaner reactive variable. [Commit](https://github.com/open-webui/open-webui/commit/5df4277216fbb9de603fdf4289f8366292568234)

> 🎧 **Read Aloud in chat preview.** The Read Aloud button in the Search Chats modal preview no longer causes crashes, and TTS functionality is now properly hidden in read-only chat contexts. [Commit](https://github.com/open-webui/open-webui/commit/d8fa0f426a88f5c27b3216b7db35e1db47bbba28)

> 🗝️ **Message upsert API reliability.** The message upsert API endpoint no longer crashes when called, fixing an error where a database session was incorrectly passed to a function that doesn't accept it. [#22959](https://github.com/open-webui/open-webui/issues/22959), [Commit](https://github.com/open-webui/open-webui/commit/70285fb6cad26b50d783583b68be5227ace16055)

> 🔃 **Tool call streaming display.** Sequential tool calls are now properly accumulated during streaming, fixing an issue where completed tool calls could disappear from the display before the next tool call finished streaming. [Commit](https://github.com/open-webui/open-webui/commit/a9c5c787b9f6b10491924d38645042064b3c941e)

> 🪝 **User webhooks disabled by default.** User webhook notifications are now disabled by default and properly gated by the ENABLE_USER_WEBHOOKS configuration, ensuring webhooks only fire when explicitly enabled. [Commit](https://github.com/open-webui/open-webui/commit/c24a4da17dbaddf47e2e0f865c1d602d0ff36ee6)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-03-25-4-editor-experience-changes-in-v0-8-11|4 Editor Experience changes in v0.8.11]] · Editor Experience
- [[Changes/Open WebUI/2026-03-25-rag-query-generation-robustness-the-rag-query-generation-web-search-and-image-ge|🔍 RAG query generation robustness. The RAG query generation, web search…]] · Image Generation
- [[Changes/Open WebUI/2026-03-25-shared-chat-viewing-crash-shared-chats-can-now-be-viewed-by-unauthenticated-user|🐛 Shared chat viewing crash. Shared chats can now be viewed by unauthenticated…]] · Collaboration
- [[Changes/Open WebUI/2026-03-25-11-account-and-access-changes-in-v0-8-11|11 Account and Access changes in v0.8.11]] · Account and Access
- [[Changes/Open WebUI/2026-03-25-3-context-window-changes-in-v0-8-11|3 Context Window changes in v0.8.11]] · Context Window
- [[Changes/Open WebUI/2026-03-25-2-search-and-browsing-changes-in-v0-8-11|2 Search and Browsing changes in v0.8.11]] · Search and Browsing
- [[Changes/Open WebUI/2026-03-25-2-files-and-data-changes-in-v0-8-11|2 Files and Data changes in v0.8.11]] · Files and Data
- [[Changes/Open WebUI/2026-03-25-4-memory-and-personalization-changes-in-v0-8-11|4 Memory and Personalization changes in v0.8.11]] · Memory and Personalization
- [[Changes/Open WebUI/2026-03-25-3-apps-and-integrations-changes-in-v0-8-11|3 Apps and Integrations changes in v0.8.11]] · Apps and Integrations
- [[Changes/Open WebUI/2026-03-25-17-interface-experience-changes-in-v0-8-11|17 Interface Experience changes in v0.8.11]] · Interface Experience
- [[Changes/Open WebUI/2026-03-25-5-reliability-and-performance-changes-in-v0-8-11|5 Reliability and Performance changes in v0.8.11]] · Reliability and Performance
- [[Changes/Open WebUI/2026-03-25-tool-binary-response-handling-tool-servers-can-now-return-binary-data-such-as-im|🏮 Tool binary response handling. Tool servers can now return binary data such…]] · Multimodal Input
- [[Changes/Open WebUI/2026-03-25-23-model-support-changes-in-v0-8-11|23 Model Support changes in v0.8.11]] · Model Support
- [[Changes/Open WebUI/2026-03-25-4-safety-and-privacy-changes-in-v0-8-11|4 Safety and Privacy changes in v0.8.11]] · Safety and Privacy
- [[Changes/Open WebUI/2026-03-25-metrics-export-interval-configuration-administrators-can-now-control-opentelemet|📊 Metrics export interval configuration. Administrators can now control…]] · Pricing Model
- [[Changes/Open WebUI/2026-03-25-19-other-changes-in-v0-8-11|19 other changes in v0.8.11]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-03-24 · Gemini CLI · [[Changes/Gemini CLI/2026-03-24-feat-skills-improve-async-pr-review-workflow-and-logging-by-mattkorwel-in-https|feat(skills): improve async-pr-review workflow and logging]]
- Later: 2026-03-26 · Claude Code · [[Changes/Claude Code/2026-03-26-5-developer-workflow-changes-in-v2-1-84|5 Developer Workflow changes in v2.1.84]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-03-25-e9e881&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-03-25-34-developer-workflow-changes-in-v0-8-11.md%0ACard%20ID%3A%20open-webui-2026-03-25-e9e881%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.11%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->