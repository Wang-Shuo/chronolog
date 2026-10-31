---
card_id: claude-code-2026-10-14-23bbb3
date: '2026-10-14'
description: 'Claude Code · 2026-10-14 · Apps and Integrations: 19 changes in v2.1.299
  — Added `--shutdown-drain-sec` to `claude self-hosted-runner orchestrator`: on SIGTERM…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1301
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 6d18eaccfb62dce6db1ed0a6098b37df896c8d883e6ce0fa56d5acdf24a7bbc5
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-14-23bbb3
  comparison: ''
  date: '2026-10-14'
  description: 'Claude Code — v2.1.299: 19 Apps and Integrations changes'
  evidence:
  - quote: 'Added `--shutdown-drain-sec` to `claude self-hosted-runner orchestrator`:
      on SIGTERM it stops polling and gives the poll in flight and running spawn hooks
      up to that many seconds to finish'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.299
  - quote: Added the skill's frontmatter, source, plugin name and file path to what
      a mod's `skill.prompt` hook receives
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.299
  - quote: Added `--disallow-tools` and a `disallowed_tools` case field to `claude
      plugin eval` to keep specific built-in tools, such as Agent, out of eval runs
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.299
  - quote: Added a field to the attribution block in Claude Code sessions behind a
      Claude apps gateway; remove the block with `CLAUDE_CODE_ATTRIBUTION_HEADER=0`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.299
  - quote: Added a note in `/plugin` and `claude plugin validate` naming a mod's hooks
      that are skipped where an organization manages Claude Code
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.299
  - quote: 'Improved the plugin-authoring skill''s steps for sharing a mod: Claude
      asks public or private and checks the files before creating a GitHub repository'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.299
  - quote: Changed plugin hooks and workflow scripts to refuse values they hand back
      that nest deeper than 28,000 levels, with an error naming the limit (workflow
      scripts allowed 100,000)
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.299
  - quote: Changed actions a plugin hook can block to be refused, not let through,
      when the hook cannot be handed them or cannot hand back its answer; a tool that
      already ran has its result withheld
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.299
  - quote: Changed requests to claude.ai's connector proxy and to Anthropic-hosted
      MCP servers to no longer follow HTTP redirects; redirects by a connector's own
      server are unaffected
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.299
  - quote: Changed MCP requests in cloud and self-hosted runner sessions to no longer
      follow HTTP redirects from the session's MCP proxy
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.299
  - quote: 'Changed `ui.render` trees in `claude plugin test`: each mod''s Box or
      Text root now carries `part: { plugin }` naming the mod, so exact-tree assertions
      must include it'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.299
  - quote: Changed `claude plugin test` to fail a call to a mod's served `$` method
      that has not answered within ten seconds, as a session does
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.299
  - quote: 'Changed MCP allow rules to reach only the server they name: `mcp__a` no
      longer allows a server named `a__b` or `a_`; write `mcp__<server>__*` with the
      server''s whole normalized name'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.299
  - quote: Changed agent `tools:` lists to take only the named MCP server's tools;
      list a server whose name contains `__` as `mcp__<whole name>__*`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.299
  - quote: Changed cloud session and Remote Control MCP connectors to negotiate MCP
      protocol version 2026-07-28 by default on installs that fetch no flags; `MCP_PROTOCOL_NEGOTIATION=legacy`
      opts out
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.299
  - quote: Changed MCP tool descriptions and server instructions from Anthropic's
      first-party MCP servers at `api.anthropic.com` to reach Claude in full instead
      of being cut at 4,096 characters
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.299
  - quote: Changed `UserPromptSubmit` hooks to run before a skill or custom slash
      command expands, so a hook that blocks the prompt now also stops its embedded
      shell commands
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.299
  - quote: '[Claude Tag] Changed how Claude in Slack corrects a message it got wrong:
      it edits the message in place and adds a short "Edited" note instead of striking
      through the old text'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.299
  - quote: '[Claude Tag] Changed Claude in Slack to join channels with more than 100
      members quietly, with no intro message'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.299
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 19-apps-and-integrations-changes-in-v2-1-299
  source_release: claude-code-2026-10-14-v2-1-299-github-412217284-623d9162
  source_type: github_releases
  theme: apps-integrations
  title: 19 Apps and Integrations changes in v2.1.299
  type: change
related_changes:
- '[[Changes/Cursor/2026-10-13-2-apps-and-integrations-changes-in-origin-app-marketplace|2
  Apps and Integrations changes in Origin App Marketplace]]'
- '[[Changes/Cursor/2026-10-13-apps-for-your-stack|Apps for your stack]]'
- '[[Changes/Claude Code/2026-10-14-7-apps-and-integrations-changes-in-v2-1-300|7
  Apps and Integrations changes in v2.1.300]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-14-v2-1-299-github-412217284-623d9162|claude-code-2026-10-14-v2-1-299-github-412217284-623d9162]]'
source_type: github_releases
theme: apps-integrations
title: 19 Apps and Integrations changes in v2.1.299
type: change
---

<!-- chronolog:begin region="header" -->
# 19 Apps and Integrations changes in v2.1.299

**Claude Code** · 2026-10-14 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.299) · from [[Releases/Claude Code/claude-code-2026-10-14-v2-1-299-github-412217284-623d9162|v2.1.299]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `--shutdown-drain-sec` to `claude self-hosted-runner orchestrator`: on SIGTERM it stops polling and gives the poll in flight and running spawn hooks up to that many seconds to finish

> Added the skill's frontmatter, source, plugin name and file path to what a mod's `skill.prompt` hook receives

> Added `--disallow-tools` and a `disallowed_tools` case field to `claude plugin eval` to keep specific built-in tools, such as Agent, out of eval runs

> Added a field to the attribution block in Claude Code sessions behind a Claude apps gateway; remove the block with `CLAUDE_CODE_ATTRIBUTION_HEADER=0`

> Added a note in `/plugin` and `claude plugin validate` naming a mod's hooks that are skipped where an organization manages Claude Code

> Improved the plugin-authoring skill's steps for sharing a mod: Claude asks public or private and checks the files before creating a GitHub repository

> Changed plugin hooks and workflow scripts to refuse values they hand back that nest deeper than 28,000 levels, with an error naming the limit (workflow scripts allowed 100,000)

> Changed actions a plugin hook can block to be refused, not let through, when the hook cannot be handed them or cannot hand back its answer; a tool that already ran has its result withheld

> Changed requests to claude.ai's connector proxy and to Anthropic-hosted MCP servers to no longer follow HTTP redirects; redirects by a connector's own server are unaffected

> Changed MCP requests in cloud and self-hosted runner sessions to no longer follow HTTP redirects from the session's MCP proxy

> Changed `ui.render` trees in `claude plugin test`: each mod's Box or Text root now carries `part: { plugin }` naming the mod, so exact-tree assertions must include it

> Changed `claude plugin test` to fail a call to a mod's served `$` method that has not answered within ten seconds, as a session does

> Changed MCP allow rules to reach only the server they name: `mcp__a` no longer allows a server named `a__b` or `a_`; write `mcp__<server>__*` with the server's whole normalized name

> Changed agent `tools:` lists to take only the named MCP server's tools; list a server whose name contains `__` as `mcp__<whole name>__*`

> Changed cloud session and Remote Control MCP connectors to negotiate MCP protocol version 2026-07-28 by default on installs that fetch no flags; `MCP_PROTOCOL_NEGOTIATION=legacy` opts out

> Changed MCP tool descriptions and server instructions from Anthropic's first-party MCP servers at `api.anthropic.com` to reach Claude in full instead of being cut at 4,096 characters

> Changed `UserPromptSubmit` hooks to run before a skill or custom slash command expands, so a hook that blocks the prompt now also stops its embedded shell commands

> [Claude Tag] Changed how Claude in Slack corrects a message it got wrong: it edits the message in place and adds a short "Edited" note instead of striking through the old text

> [Claude Tag] Changed Claude in Slack to join channels with more than 100 members quietly, with no intro message

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.299
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-14-2-context-window-changes-in-v2-1-299|2 Context Window changes in v2.1.299]] · Context Window
- [[Changes/Claude Code/2026-10-14-10-developer-workflow-changes-in-v2-1-299|10 Developer Workflow changes in v2.1.299]] · Developer Workflow
- [[Changes/Claude Code/2026-10-14-2-model-support-changes-in-v2-1-299|2 Model Support changes in v2.1.299]] · Model Support
- [[Changes/Claude Code/2026-10-14-2-files-and-data-changes-in-v2-1-299|2 Files and Data changes in v2.1.299]] · Files and Data
- [[Changes/Claude Code/2026-10-14-2-editor-experience-changes-in-v2-1-299|2 Editor Experience changes in v2.1.299]] · Editor Experience
- [[Changes/Claude Code/2026-10-14-5-agent-mode-changes-in-v2-1-299|5 Agent Mode changes in v2.1.299]] · Agent Mode
- [[Changes/Claude Code/2026-10-14-added-effort-and-fast-in-agent-view-to-set-what-new-sessions-start-with-a-bare-m|Added /effort and /fast in agent view to set what new sessions start with]] · Interface Experience
- [[Changes/Claude Code/2026-10-14-improved-memory-and-disk-use-when-pdfs-are-mentioned-their-bytes-are-no-longer-k|Improved memory and disk use when PDFs are @-mentioned]] · Reliability and Performance
- [[Changes/Claude Code/2026-10-14-added-usage-warnings-for-max-effort-workflows-always-on-context-and-large-tool-r|Added /usage warnings for max effort, workflows, always-on context and large tool…]] · Context Window
- [[Changes/Claude Code/2026-10-14-improved-the-error-shown-when-a-cloud-session-is-refused-because-your-claude-ai|Improved the error shown when a cloud session is refused because your claude.ai…]] · Account and Access
- [[Changes/Claude Code/2026-10-14-vscode-improved-startup-the-model-picker-and-slash-command-menu-now-fill-in-righ|VSCode Improved startup]] · Interface Experience
- [[Changes/Claude Code/2026-10-14-6-safety-and-privacy-changes-in-v2-1-299|6 Safety and Privacy changes in v2.1.299]] · Safety and Privacy
- [[Changes/Claude Code/2026-10-14-11-other-changes-in-v2-1-299|11 other changes in v2.1.299]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-10-14 · Claude Code · [[Changes/Claude Code/2026-10-14-7-apps-and-integrations-changes-in-v2-1-300|7 Apps and Integrations changes in v2.1.300]]
- Later: 2026-10-16 · ChatGPT · [[Changes/ChatGPT/2026-10-16-improved-use-of-plugins-and-tools-to-carry-out-tasks|Improved use of plugins and tools to carry out tasks]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-14-23bbb3&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-14-19-apps-and-integrations-changes-in-v2-1-299.md%0ACard%20ID%3A%20claude-code-2026-10-14-23bbb3%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.299%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->