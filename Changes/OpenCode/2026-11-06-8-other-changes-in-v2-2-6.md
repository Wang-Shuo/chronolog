---
card_id: opencode-2026-11-06-64d423
date: '2026-11-06'
description: 'OpenCode · 2026-11-06 · Other changes: 8 changes in v2.2.6 — Core Added
  the websearch.use policy action and switches for enabling all feature flags with…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 6c48361613457b2ff21791533508874f674a8c2248947a428bce6c371daca60f
product: opencode
product_name: OpenCode
record:
  card_id: opencode-2026-11-06-64d423
  comparison: ''
  date: '2026-11-06'
  description: 'OpenCode — v2.2.6: 8 other changes'
  evidence:
  - quote: Core Added the websearch.use policy action and switches for enabling all
      feature flags with OPENCODE_FLAGS=all or experimental.all_flags .
    source_release: https://opencode.ai/changelog/v2.2.6
  - quote: 'Core Added an experimental bytecode VM for Code Mode. It is off by default;
      turn it on with experimental.codemode_vm: true or OPENCODE_FLAGS=codemode_vm
      .'
    source_release: https://opencode.ai/changelog/v2.2.6
  - quote: Core Reworked noninteractive opencode run execution so arguments, cancellation,
      compiled WebSocket upgrades, and service shutdown complete reliably. SIGTERM
      now cancels the session and its background jobs and exits with code 143.
    source_release: https://opencode.ai/changelog/v2.2.6
  - quote: Core Serve file reads and media from the server API as sandboxed downloads,
      and refuse cross-site browser navigations and requests from disallowed origins
      to /api/* , so a file in your project cannot run scripts on the server's origin.
    source_release: https://opencode.ai/changelog/v2.2.6
  - quote: Core Time out OpenCode Console config requests after 5 seconds, so startup
      no longer hangs when the Console accepts the connection but never answers.
    source_release: https://opencode.ai/changelog/v2.2.6
  - quote: Core Retry provider requests while their host is unreachable and recover
      prematurely ended Cohere streams.
    source_release: https://opencode.ai/changelog/v2.2.6
  - quote: Core opencode acp now removes a session that a client creates with session/new
      and closes without prompting, so IDE integrations no longer leave empty sessions
      behind.
    source_release: https://opencode.ai/changelog/v2.2.6
  - quote: Core Allow npm upgrade install scripts again. Thanks @renatomoselli.
    source_release: https://opencode.ai/changelog/v2.2.6
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: opencode
  product_name: OpenCode
  slug: 8-other-changes-in-v2-2-6
  source_release: opencode-2026-11-06-v2-2-6-b1ac172e
  source_type: opencode_changelog
  theme: uncategorized
  title: 8 other changes in v2.2.6
  type: change
source_release: '[[Releases/OpenCode/opencode-2026-11-06-v2-2-6-b1ac172e|opencode-2026-11-06-v2-2-6-b1ac172e]]'
source_type: opencode_changelog
theme: uncategorized
title: 8 other changes in v2.2.6
type: change
---

<!-- chronolog:begin region="header" -->
# 8 other changes in v2.2.6

**OpenCode** · 2026-11-06 · Other changes · Digest · [Official source](https://opencode.ai/changelog/v2.2.6) · from [[Releases/OpenCode/opencode-2026-11-06-v2-2-6-b1ac172e|v2.2.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Core Added the websearch.use policy action and switches for enabling all feature flags with OPENCODE_FLAGS=all or experimental.all_flags .

> Core Added an experimental bytecode VM for Code Mode. It is off by default; turn it on with experimental.codemode_vm: true or OPENCODE_FLAGS=codemode_vm .

> Core Reworked noninteractive opencode run execution so arguments, cancellation, compiled WebSocket upgrades, and service shutdown complete reliably. SIGTERM now cancels the session and its background jobs and exits with code 143.

> Core Serve file reads and media from the server API as sandboxed downloads, and refuse cross-site browser navigations and requests from disallowed origins to /api/* , so a file in your project cannot run scripts on the server's origin.

> Core Time out OpenCode Console config requests after 5 seconds, so startup no longer hangs when the Console accepts the connection but never answers.

> Core Retry provider requests while their host is unreachable and recover prematurely ended Cohere streams.

> Core opencode acp now removes a session that a client creates with session/new and closes without prompting, so IDE integrations no longer leave empty sessions behind.

> Core Allow npm upgrade install scripts again. Thanks @renatomoselli.

Source: https://opencode.ai/changelog/v2.2.6
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenCode/2026-11-06-scripted-runs-in-worktrees|Scripted Runs in Worktrees]] · Developer Workflow
- [[Changes/OpenCode/2026-11-06-shared-mcp-connections|Shared MCP Connections]] · Apps and Integrations
- [[Changes/OpenCode/2026-11-06-mobile-composer-dock|Mobile Composer Dock]] · Mobile and Desktop
- [[Changes/OpenCode/2026-11-06-gui-plugin-themes-and-new-slots|GUI Plugin Themes and New Slots]] · Apps and Integrations
- [[Changes/OpenCode/2026-11-06-12-developer-workflow-changes-in-v2-2-6|12 Developer Workflow changes in v2.2.6]] · Developer Workflow
- [[Changes/OpenCode/2026-11-06-desktop-mcp-sign-in-now-accepts-a-pasted-redirect-url-when-automatic-redirection|Desktop MCP sign-in now accepts a pasted redirect URL when automatic redirection…]] · Account and Access
- [[Changes/OpenCode/2026-11-06-3-safety-and-privacy-changes-in-v2-2-6|3 Safety and Privacy changes in v2.2.6]] · Safety and Privacy
- [[Changes/OpenCode/2026-11-06-12-mobile-and-desktop-changes-in-v2-2-6|12 Mobile and Desktop changes in v2.2.6]] · Mobile and Desktop
- [[Changes/OpenCode/2026-11-06-core-added-azure-messages-support-for-foundry-claude-models|Core Added Azure Messages support for Foundry Claude models]] · Model Support
- [[Changes/OpenCode/2026-11-06-7-apps-and-integrations-changes-in-v2-2-6|7 Apps and Integrations changes in v2.2.6]] · Apps and Integrations
- [[Changes/OpenCode/2026-11-06-2-agent-mode-changes-in-v2-2-6|2 Agent Mode changes in v2.2.6]] · Agent Mode
- [[Changes/OpenCode/2026-11-06-core-keep-legacy-custom-providers-whose-models-set-only-part-of-limit-such-as-on|Core Keep legacy custom providers whose models set only part of limit , such as only…]] · Context Window
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20opencode-2026-11-06-64d423&body=Card%3A%20Changes%2FOpenCode%2F2026-11-06-8-other-changes-in-v2-2-6.md%0ACard%20ID%3A%20opencode-2026-11-06-64d423%0ASource%3A%20https%3A%2F%2Fopencode.ai%2Fchangelog%2Fv2.2.6%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->