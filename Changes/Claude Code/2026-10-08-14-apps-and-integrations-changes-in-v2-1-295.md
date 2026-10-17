---
card_id: claude-code-2026-10-08-70f161
date: '2026-10-08'
description: 'Claude Code · 2026-10-08 · Apps and Integrations: 14 changes in v2.1.295
  — Added `onFailure: "block"` for command and HTTP hooks: a hook that can''t start…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1295
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b371ded510fa4045d10fa89125e575a58dfda7a2ff30e84e5676cff33fd84058
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-08-70f161
  comparison: ''
  date: '2026-10-08'
  description: 'Claude Code — v2.1.295: 14 Apps and Integrations changes'
  evidence:
  - quote: 'Added `onFailure: "block"` for command and HTTP hooks: a hook that can''t
      start, times out, or exits with an unexpected code blocks the action instead
      of letting it through'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.295
  - quote: Added a warning to `claude plugin install`, `enable`, `disable` and `marketplace
      add` when the settings file they write to does not load
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.295
  - quote: 'Added support for `timeouts.upstream_ttfb_ms` on the Claude apps gateway''s
      Bedrock, Vertex, Foundry and other cloud upstreams: a value you set now limits
      how long a stream may take to start there, after which it fails over or gets
      a 502'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.295
  - quote: 'Added advice to `claude plugin validate` when a plugin''s README has no
      install line: it prints the line to paste and never changes the exit code, even
      with `--strict`'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.295
  - quote: 'Added `upstream_request_id` to the Claude apps gateway''s `inference`
      audit event: the request ID from Amazon Bedrock, the Anthropic API or another
      upstream, for support cases'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.295
  - quote: Added a `request-id` header to the Claude apps gateway's successful inference
      responses, so `request_id` in Claude Code telemetry matches the gateway's audit
      log
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.295
  - quote: Improved the Claude apps gateway to log a warning every 30 seconds while
      its PostgreSQL database is read-only, saying what fails and how to recover
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.295
  - quote: 'Improved the built-in `plugin-authoring` skill: it no longer tells a session
      with no terminal to run terminal commands, and explains sharing a mod only when
      asked'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.295
  - quote: 'Improved `claude plugin validate` and plugin loading: when a hooks module
      is refused over a rebound top-level `var`, the error now names the line that
      rebinds it, the cause, and a fix'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.295
  - quote: Changed MCP tool descriptions the model loads through tool search to be
      cut at 16,384 characters instead of 2,048
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.295
  - quote: Changed claude.ai connectors to negotiate MCP protocol version 2026-07-28
      by default on installs that fetch no flags; `MCP_PROTOCOL_NEGOTIATION=legacy`
      opts out
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.295
  - quote: 'Changed what Claude and you read when a mod denies a tool call after the
      tool ran: it now says the tool ran and a plugin withheld its result'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.295
  - quote: 'Changed WebSocket (`ws`) MCP servers: a message over 16 MiB is no longer
      parsed and closes the connection, the limit the other transports already have'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.295
  - quote: '[Claude Tag] Changed the settings confirmation cards Claude posts in a
      Slack channel to stay open for 30 minutes instead of 10'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.295
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 14-apps-and-integrations-changes-in-v2-1-295
  source_release: claude-code-2026-10-08-v2-1-295-github-407134589-d5c87510
  source_type: github_releases
  theme: apps-integrations
  title: 14 Apps and Integrations changes in v2.1.295
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-06-9-apps-and-integrations-changes-in-v2-1-292|9
  Apps and Integrations changes in v2.1.292]]'
- '[[Changes/Claude Code/2026-10-07-3-apps-and-integrations-changes-in-v2-1-293|3
  Apps and Integrations changes in v2.1.293]]'
- '[[Changes/Claude Code/2026-10-08-improved-how-prompt-hooks-on-stop-and-subagentstop-written-as-instructions-such|Improved
  how prompt hooks on Stop and SubagentStop written as instructions…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-08-v2-1-295-github-407134589-d5c87510|claude-code-2026-10-08-v2-1-295-github-407134589-d5c87510]]'
source_type: github_releases
theme: apps-integrations
title: 14 Apps and Integrations changes in v2.1.295
type: change
---

<!-- chronolog:begin region="header" -->
# 14 Apps and Integrations changes in v2.1.295

**Claude Code** · 2026-10-08 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.295) · from [[Releases/Claude Code/claude-code-2026-10-08-v2-1-295-github-407134589-d5c87510|v2.1.295]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `onFailure: "block"` for command and HTTP hooks: a hook that can't start, times out, or exits with an unexpected code blocks the action instead of letting it through

> Added a warning to `claude plugin install`, `enable`, `disable` and `marketplace add` when the settings file they write to does not load

> Added support for `timeouts.upstream_ttfb_ms` on the Claude apps gateway's Bedrock, Vertex, Foundry and other cloud upstreams: a value you set now limits how long a stream may take to start there, after which it fails over or gets a 502

> Added advice to `claude plugin validate` when a plugin's README has no install line: it prints the line to paste and never changes the exit code, even with `--strict`

> Added `upstream_request_id` to the Claude apps gateway's `inference` audit event: the request ID from Amazon Bedrock, the Anthropic API or another upstream, for support cases

> Added a `request-id` header to the Claude apps gateway's successful inference responses, so `request_id` in Claude Code telemetry matches the gateway's audit log

> Improved the Claude apps gateway to log a warning every 30 seconds while its PostgreSQL database is read-only, saying what fails and how to recover

> Improved the built-in `plugin-authoring` skill: it no longer tells a session with no terminal to run terminal commands, and explains sharing a mod only when asked

> Improved `claude plugin validate` and plugin loading: when a hooks module is refused over a rebound top-level `var`, the error now names the line that rebinds it, the cause, and a fix

> Changed MCP tool descriptions the model loads through tool search to be cut at 16,384 characters instead of 2,048

> Changed claude.ai connectors to negotiate MCP protocol version 2026-07-28 by default on installs that fetch no flags; `MCP_PROTOCOL_NEGOTIATION=legacy` opts out

> Changed what Claude and you read when a mod denies a tool call after the tool ran: it now says the tool ran and a plugin withheld its result

> Changed WebSocket (`ws`) MCP servers: a message over 16 MiB is no longer parsed and closes the connection, the limit the other transports already have

> [Claude Tag] Changed the settings confirmation cards Claude posts in a Slack channel to stay open for 30 minutes instead of 10

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.295
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-08-3-agent-mode-changes-in-v2-1-295|3 Agent Mode changes in v2.1.295]] · Agent Mode
- [[Changes/Claude Code/2026-10-08-added-a-line-on-stderr-when-it-is-a-terminal-that-says-what-a-claude-p-run-is-wa|Added a line on stderr, when it is a terminal, that says what a claude -p run…]] · Developer Workflow
- [[Changes/Claude Code/2026-10-08-improved-token-counts-behind-a-claude-apps-gateway-on-amazon-bedrock-which-conte|Improved token counts behind a Claude apps gateway on Amazon Bedrock…]] · Context Window
- [[Changes/Claude Code/2026-10-08-changed-ctrl-c-at-the-idle-prompt-of-an-attached-background-session-to-leave-a-p|Changed Ctrl+C at the idle prompt of an attached background session to leave…]] · Automation and Scheduling
- [[Changes/Claude Code/2026-10-08-added-support-for-forceloginmethod-gateway-and-forcelogingatewayurl-in-your-own|Added support for forceLoginMethod: "gateway" and forceLoginGatewayUrl…]] · Account and Access
- [[Changes/Claude Code/2026-10-08-changed-tab-stops-to-count-from-where-a-text-starts-instead-of-from-the-screen-s|Changed tab stops to count from where a text starts instead of from the screen's left edge]] · Editor Experience
- [[Changes/Claude Code/2026-10-08-2-model-support-changes-in-v2-1-295|2 Model Support changes in v2.1.295]] · Model Support
- [[Changes/Claude Code/2026-10-08-2-interface-experience-changes-in-v2-1-295|2 Interface Experience changes in v2.1.295]] · Interface Experience
- [[Changes/Claude Code/2026-10-08-2-mobile-and-desktop-changes-in-v2-1-295|2 Mobile and Desktop changes in v2.1.295]] · Mobile and Desktop
- [[Changes/Claude Code/2026-10-08-5-safety-and-privacy-changes-in-v2-1-295|5 Safety and Privacy changes in v2.1.295]] · Safety and Privacy
- [[Changes/Claude Code/2026-10-08-claude-tag-changed-claude-s-notice-that-a-channel-shared-across-enterprise-grid|Claude Tag Changed Claude's notice that a channel shared across Enterprise Grid…]] · Enterprise and Administration
- [[Changes/Claude Code/2026-10-08-15-other-changes-in-v2-1-295|15 other changes in v2.1.295]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-10-08 · Claude Code · [[Changes/Claude Code/2026-10-08-improved-how-prompt-hooks-on-stop-and-subagentstop-written-as-instructions-such|Improved how prompt hooks on Stop and SubagentStop written as instructions…]]
- Later: 2026-10-09 · Claude Code · [[Changes/Claude Code/2026-10-09-3-apps-and-integrations-changes-in-v2-1-296|3 Apps and Integrations changes in v2.1.296]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-08-70f161&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-08-14-apps-and-integrations-changes-in-v2-1-295.md%0ACard%20ID%3A%20claude-code-2026-10-08-70f161%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.295%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->