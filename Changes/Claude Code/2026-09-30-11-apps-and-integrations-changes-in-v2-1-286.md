---
card_id: claude-code-2026-09-30-67fd04
date: '2026-09-30'
description: 'Claude Code · 2026-09-30 · Apps and Integrations: 11 changes in v2.1.286
  — Improved slash command suggestion responsiveness while typing when many skills
  or…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1287
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 681a2f5a2c35ba0245d2b3f7cdb36e2c8d40a5f7c4895a0c7c06167154f83d64
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-30-67fd04
  comparison: ''
  date: '2026-09-30'
  description: 'Claude Code — v2.1.286: 11 Apps and Integrations changes'
  evidence:
  - quote: Improved slash command suggestion responsiveness while typing when many
      skills or plugin commands are installed; command descriptions now match by word
      prefix
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.286
  - quote: 'Improved `/hooks`: the closing line of a hook''s detail screen now says
      "this hook" instead of "it"'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.286
  - quote: Improved responsiveness of SDK and `-p` sessions when a host re-sends an
      MCP server enable for a server that is already connected
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.286
  - quote: 'Improved the protocol page a Claude apps gateway serves at `/protocol`:
      it now says not to reject unknown input and matches what Claude Code sends today'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.286
  - quote: Changed `--bare` to connect only the MCP servers named on the command line,
      send the model no system reminders, and start no background tasks; under `--bare`,
      a shell command that reaches its timeout now stops instead of moving to the
      background
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.286
  - quote: Changed plugin installs to refuse npm sources that are git repositories
      or folders, and to install plugin dependencies only from registry packages
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.286
  - quote: Changed list screens (`/artifacts`, `/mcp`, `/skills`, `/hooks` and others)
      to always line up each row's details in one column after the names
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.286
  - quote: Changed `/hooks` to open on one list of your configured hooks grouped by
      event, so viewing a hook takes one Enter instead of three
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.286
  - quote: '[VSCode] Improved the Manage plugins dialog: it says when a turned-off
      plugin is still on because of other settings, and explains a plugin folder clash'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.286
  - quote: '[Claude Tag] Added an Add channel button to Claude Tag''s spend limits
      page in admin settings, so a limit can be set on any channel, including a private
      one, from its channel ID or Slack link'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.286
  - quote: '[Claude Tag] Improved the titles of sessions started from Slack as shown
      on claude.ai: they now read as the words you typed, without Slack user IDs or
      escape codes'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.286
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 11-apps-and-integrations-changes-in-v2-1-286
  source_release: claude-code-2026-09-30-v2-1-286-github-400266224-9fb31eb7
  source_type: github_releases
  theme: apps-integrations
  title: 11 Apps and Integrations changes in v2.1.286
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-09-29-we-re-making-it-easier-to-bring-meeting-context-into-chatgpt-so-you-can-act-on-n|We’re
  making it easier to bring meeting context into ChatGPT so you can act on next…]]'
- '[[Changes/ChatGPT/2026-09-29-supported-plugins-can-use-mcp-events-to-start-an-automation-when-something-chang-d9add6|Start
  automations from connected-app events]]'
- '[[Changes/Claude Code/2026-09-29-14-apps-and-integrations-changes-in-v2-1-285|14
  Apps and Integrations changes in v2.1.285]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-30-v2-1-286-github-400266224-9fb31eb7|claude-code-2026-09-30-v2-1-286-github-400266224-9fb31eb7]]'
source_type: github_releases
theme: apps-integrations
title: 11 Apps and Integrations changes in v2.1.286
type: change
---

<!-- chronolog:begin region="header" -->
# 11 Apps and Integrations changes in v2.1.286

**Claude Code** · 2026-09-30 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.286) · from [[Releases/Claude Code/claude-code-2026-09-30-v2-1-286-github-400266224-9fb31eb7|v2.1.286]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Improved slash command suggestion responsiveness while typing when many skills or plugin commands are installed; command descriptions now match by word prefix

> Improved `/hooks`: the closing line of a hook's detail screen now says "this hook" instead of "it"

> Improved responsiveness of SDK and `-p` sessions when a host re-sends an MCP server enable for a server that is already connected

> Improved the protocol page a Claude apps gateway serves at `/protocol`: it now says not to reject unknown input and matches what Claude Code sends today

> Changed `--bare` to connect only the MCP servers named on the command line, send the model no system reminders, and start no background tasks; under `--bare`, a shell command that reaches its timeout now stops instead of moving to the background

> Changed plugin installs to refuse npm sources that are git repositories or folders, and to install plugin dependencies only from registry packages

> Changed list screens (`/artifacts`, `/mcp`, `/skills`, `/hooks` and others) to always line up each row's details in one column after the names

> Changed `/hooks` to open on one list of your configured hooks grouped by event, so viewing a hook takes one Enter instead of three

> [VSCode] Improved the Manage plugins dialog: it says when a turned-off plugin is still on because of other settings, and explains a plugin folder clash

> [Claude Tag] Added an Add channel button to Claude Tag's spend limits page in admin settings, so a limit can be set on any channel, including a private one, from its channel ID or Slack link

> [Claude Tag] Improved the titles of sessions started from Slack as shown on claude.ai: they now read as the words you typed, without Slack user IDs or escape codes

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.286
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-30-6-agent-mode-changes-in-v2-1-286|6 Agent Mode changes in v2.1.286]] · Agent Mode
- [[Changes/Claude Code/2026-09-30-changed-how-failed-api-requests-are-retried-one-limit-now-covers-a-whole-model-c|Changed how failed API requests are retried]] · Model Support
- [[Changes/Claude Code/2026-09-30-4-interface-experience-changes-in-v2-1-286|4 Interface Experience changes in v2.1.286]] · Interface Experience
- [[Changes/Claude Code/2026-09-30-3-developer-workflow-changes-in-v2-1-286|3 Developer Workflow changes in v2.1.286]] · Developer Workflow
- [[Changes/Claude Code/2026-09-30-improved-the-external-editor-ctrl-g-editors-that-take-a-line-number-now-open-on|Improved the external editor (Ctrl+G)]] · Editor Experience
- [[Changes/Claude Code/2026-09-30-improved-the-model-fallback-notice-and-the-autocompact-thrashing-error-to-say-wh|Improved the model fallback notice and the autocompact-thrashing error to say…]] · Context Window
- [[Changes/Claude Code/2026-09-30-4-safety-and-privacy-changes-in-v2-1-286|4 Safety and Privacy changes in v2.1.286]] · Safety and Privacy
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-09-29 · Claude Code · [[Changes/Claude Code/2026-09-29-14-apps-and-integrations-changes-in-v2-1-285|14 Apps and Integrations changes in v2.1.285]]
- Later: 2026-10-01 · Claude Code · [[Changes/Claude Code/2026-10-01-11-apps-and-integrations-changes-in-v2-1-287|11 Apps and Integrations changes in v2.1.287]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-30-67fd04&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-30-11-apps-and-integrations-changes-in-v2-1-286.md%0ACard%20ID%3A%20claude-code-2026-09-30-67fd04%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.286%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->