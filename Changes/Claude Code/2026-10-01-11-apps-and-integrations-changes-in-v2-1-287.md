---
card_id: claude-code-2026-10-01-62a9e3
date: '2026-10-01'
description: 'Claude Code · 2026-10-01 · Apps and Integrations: 11 changes in v2.1.287
  — Added Claude Mods: plugins may now modify deeper behavior'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1288
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 7b881558ad55550668f949b8b738c2d42b85c86c99089292bfba46ce776cb61e
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-01-62a9e3
  comparison: ''
  date: '2026-10-01'
  description: 'Claude Code — v2.1.287: 11 Apps and Integrations changes'
  evidence:
  - quote: 'Added Claude Mods: plugins may now modify deeper behavior'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.287
  - quote: Added You should know, a built-in mod where a side agent watches your back
      and flags things you or Claude might miss. Turn it on with `/plugin enable cc-plugin-you-should-know@builtin`
      (for first-party sessions with telemetry on)
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.287
  - quote: Improved plugin marketplace errors to say in plain words why a marketplace
      was ignored or refused, and what to do
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.287
  - quote: Improved plugin listings to note when a plugin's dependencies were not
      installed, and updating a plugin now retries an install that did not finish
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.287
  - quote: 'Improved delivery of files Claude sends from cloud sessions and Remote
      Control: an upload that fails on a timeout, a network error or a 502, 503 or
      504 is now retried once'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.287
  - quote: 'Improved MCP startup in headless mode: a remote server whose first connect
      fails transiently is now retried without waiting for the slowest server to finish
      connecting'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.287
  - quote: Improved the explanation Claude gives when the server refuses a file it
      sends from a Remote Control or cloud session, such as an oversized image
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.287
  - quote: Changed whole-tool `Bash` allow rules and allowing hooks to prompt for,
      not run, shell writes to files Claude Code's file tools refuse outright (the
      Anthropic profile store, the host credentials file)
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.287
  - quote: 'Changed MCP server `alwaysLoad: false` to defer all of that server''s
      tools behind tool search'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.287
  - quote: '[VSCode] Improved the Manage plugins dialog: a failed marketplace add,
      remove or refresh now says what went wrong'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.287
  - quote: '[Claude Tag] Improved Claude''s task list in long Slack threads: background
      work no longer reposts it as a new message on its own, so people following the
      thread aren''t notified'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.287
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 11-apps-and-integrations-changes-in-v2-1-287
  source_release: claude-code-2026-10-01-v2-1-287-github-401174143-9cfdbb87
  source_type: github_releases
  theme: apps-integrations
  title: 11 Apps and Integrations changes in v2.1.287
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-09-29-supported-plugins-can-use-mcp-events-to-start-an-automation-when-something-chang-d9add6|Start
  automations from connected-app events]]'
- '[[Changes/Claude Code/2026-09-29-14-apps-and-integrations-changes-in-v2-1-285|14
  Apps and Integrations changes in v2.1.285]]'
- '[[Changes/Claude Code/2026-09-30-11-apps-and-integrations-changes-in-v2-1-286|11
  Apps and Integrations changes in v2.1.286]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-01-v2-1-287-github-401174143-9cfdbb87|claude-code-2026-10-01-v2-1-287-github-401174143-9cfdbb87]]'
source_type: github_releases
theme: apps-integrations
title: 11 Apps and Integrations changes in v2.1.287
type: change
---

<!-- chronolog:begin region="header" -->
# 11 Apps and Integrations changes in v2.1.287

**Claude Code** · 2026-10-01 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.287) · from [[Releases/Claude Code/claude-code-2026-10-01-v2-1-287-github-401174143-9cfdbb87|v2.1.287]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added Claude Mods: plugins may now modify deeper behavior

> Added You should know, a built-in mod where a side agent watches your back and flags things you or Claude might miss. Turn it on with `/plugin enable cc-plugin-you-should-know@builtin` (for first-party sessions with telemetry on)

> Improved plugin marketplace errors to say in plain words why a marketplace was ignored or refused, and what to do

> Improved plugin listings to note when a plugin's dependencies were not installed, and updating a plugin now retries an install that did not finish

> Improved delivery of files Claude sends from cloud sessions and Remote Control: an upload that fails on a timeout, a network error or a 502, 503 or 504 is now retried once

> Improved MCP startup in headless mode: a remote server whose first connect fails transiently is now retried without waiting for the slowest server to finish connecting

> Improved the explanation Claude gives when the server refuses a file it sends from a Remote Control or cloud session, such as an oversized image

> Changed whole-tool `Bash` allow rules and allowing hooks to prompt for, not run, shell writes to files Claude Code's file tools refuse outright (the Anthropic profile store, the host credentials file)

> Changed MCP server `alwaysLoad: false` to defer all of that server's tools behind tool search

> [VSCode] Improved the Manage plugins dialog: a failed marketplace add, remove or refresh now says what went wrong

> [Claude Tag] Improved Claude's task list in long Slack threads: background work no longer reposts it as a new message on its own, so people following the thread aren't notified

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.287
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-01-4-model-support-changes-in-v2-1-287|4 Model Support changes in v2.1.287]] · Model Support
- [[Changes/Claude Code/2026-10-01-changed-opus-4-7-and-fable-to-use-a-1m-context-window-by-default-on-bedrock-vert|Changed Opus 4.7+ and Fable to use a 1M context window by default on Bedrock…]] · Context Window
- [[Changes/Claude Code/2026-10-01-2-mobile-and-desktop-changes-in-v2-1-287|2 Mobile and Desktop changes in v2.1.287]] · Mobile and Desktop
- [[Changes/Claude Code/2026-10-01-vscode-changed-the-claude-in-chrome-enabled-by-default-switch-to-also-connect-th|VSCode Changed the Claude in Chrome "Enabled by default" switch to also connect…]] · Editor Experience
- [[Changes/Claude Code/2026-10-01-6-safety-and-privacy-changes-in-v2-1-287|6 Safety and Privacy changes in v2.1.287]] · Safety and Privacy
- [[Changes/Claude Code/2026-10-01-3-developer-workflow-changes-in-v2-1-287|3 Developer Workflow changes in v2.1.287]] · Developer Workflow
- [[Changes/Claude Code/2026-10-01-2-reliability-and-performance-changes-in-v2-1-287|2 Reliability and Performance changes in v2.1.287]] · Reliability and Performance
- [[Changes/Claude Code/2026-10-01-changed-screen-reader-mode-to-write-new-or-changed-lines-without-first-pausing-w|Changed screen reader mode to write new or changed lines without first pausing…]] · Accessibility and Localization
- [[Changes/Claude Code/2026-10-01-4-agent-mode-changes-in-v2-1-287|4 Agent Mode changes in v2.1.287]] · Agent Mode
- [[Changes/Claude Code/2026-10-01-added-url-prompts-from-mcp-servers-on-the-2025-11-25-protocol-for-example-to-sig|Added URL prompts from MCP servers on the 2025-11-25 protocol, for example to sign in]] · Account and Access
- [[Changes/Claude Code/2026-10-01-improved-sdk-sessions-so-a-message-sent-with-priority-now-no-longer-cancels-a-ru|Improved SDK sessions so a message sent with priority "now" no longer cancels…]] · Search and Browsing
- [[Changes/Claude Code/2026-10-01-2-memory-and-personalization-changes-in-v2-1-287|2 Memory and Personalization changes in v2.1.287]] · Memory and Personalization
- [[Changes/Claude Code/2026-10-01-4-other-changes-in-v2-1-287|4 other changes in v2.1.287]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-09-30 · Claude Code · [[Changes/Claude Code/2026-09-30-11-apps-and-integrations-changes-in-v2-1-286|11 Apps and Integrations changes in v2.1.286]]
- Later: 2026-10-02 · Claude Code · [[Changes/Claude Code/2026-10-02-5-apps-and-integrations-changes-in-v2-1-288|5 Apps and Integrations changes in v2.1.288]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-01-62a9e3&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-01-11-apps-and-integrations-changes-in-v2-1-287.md%0ACard%20ID%3A%20claude-code-2026-10-01-62a9e3%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.287%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->