---
card_id: claude-code-2026-10-06-2a26ab
date: '2026-10-06'
description: 'Claude Code · 2026-10-06 · Apps and Integrations: 9 changes in v2.1.292
  — Added `--marketplace <source>` to `claude plugin install`: adds the marketplace
  if…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1293
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b0e2141fe5bf51d5e78128ba914954197093f9ea211c4c122049a5c836d0ca69
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-06-2a26ab
  comparison: ''
  date: '2026-10-06'
  description: 'Claude Code — v2.1.292: 9 Apps and Integrations changes'
  evidence:
  - quote: 'Added `--marketplace <source>` to `claude plugin install`: adds the marketplace
      if needed, under the same policy checks as `claude plugin marketplace add`,
      then installs the plugin from it'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.292
  - quote: 'Improved startup of `claude -p` and SDK sessions: the first turn no longer
      waits for HTTP and SSE MCP servers to answer `resources/list`'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.292
  - quote: 'Improved startup with local (stdio) MCP servers that ignore the newer
      protocol check: after one slow connect they are remembered for 7 days and connected
      the older way without the wait'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.292
  - quote: Changed local (stdio) MCP server connections to negotiate protocol version
      2026-07-28 by default on every install, including Bedrock, Vertex and Foundry;
      `MCP_PROTOCOL_NEGOTIATION=legacy` opts out
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.292
  - quote: 'Changed `claude plugin test`: a failed `expect` inside a hook the test
      registered, or a stub answer the engine refuses, now fails the test instead
      of passing silently'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.292
  - quote: Changed usage limit messages to write claude.ai settings links with https://
      so terminals and apps can make them clickable
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.292
  - quote: Changed scheduled and Run now routine runs to publish a new artifact only
      you can see without asking for approval; artifacts that request connectors or
      other access still ask
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.292
  - quote: 'Changed agent names to allow at most 256 characters: a longer one is rejected,
      and a skill''s or a plugin file''s `name` longer than that is ignored'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.292
  - quote: '[Claude Tag] Changed the first message of a Slack thread continued with
      `!fork` to a card showing where it came from, the request, and who asked, with
      a link to the original thread'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.292
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 9-apps-and-integrations-changes-in-v2-1-292
  source_release: claude-code-2026-10-06-v2-1-292-github-404958910-b2fd21ab
  source_type: github_releases
  theme: apps-integrations
  title: 9 Apps and Integrations changes in v2.1.292
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-02-5-apps-and-integrations-changes-in-v2-1-288|5
  Apps and Integrations changes in v2.1.288]]'
- '[[Changes/Claude Code/2026-10-03-2-apps-and-integrations-changes-in-v2-1-289|2
  Apps and Integrations changes in v2.1.289]]'
- '[[Changes/Claude Code/2026-10-05-14-apps-and-integrations-changes-in-v2-1-290|14
  Apps and Integrations changes in v2.1.290]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-06-v2-1-292-github-404958910-b2fd21ab|claude-code-2026-10-06-v2-1-292-github-404958910-b2fd21ab]]'
source_type: github_releases
theme: apps-integrations
title: 9 Apps and Integrations changes in v2.1.292
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Apps and Integrations changes in v2.1.292

**Claude Code** · 2026-10-06 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.292) · from [[Releases/Claude Code/claude-code-2026-10-06-v2-1-292-github-404958910-b2fd21ab|v2.1.292]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `--marketplace <source>` to `claude plugin install`: adds the marketplace if needed, under the same policy checks as `claude plugin marketplace add`, then installs the plugin from it

> Improved startup of `claude -p` and SDK sessions: the first turn no longer waits for HTTP and SSE MCP servers to answer `resources/list`

> Improved startup with local (stdio) MCP servers that ignore the newer protocol check: after one slow connect they are remembered for 7 days and connected the older way without the wait

> Changed local (stdio) MCP server connections to negotiate protocol version 2026-07-28 by default on every install, including Bedrock, Vertex and Foundry; `MCP_PROTOCOL_NEGOTIATION=legacy` opts out

> Changed `claude plugin test`: a failed `expect` inside a hook the test registered, or a stub answer the engine refuses, now fails the test instead of passing silently

> Changed usage limit messages to write claude.ai settings links with https:// so terminals and apps can make them clickable

> Changed scheduled and Run now routine runs to publish a new artifact only you can see without asking for approval; artifacts that request connectors or other access still ask

> Changed agent names to allow at most 256 characters: a longer one is rejected, and a skill's or a plugin file's `name` longer than that is ignored

> [Claude Tag] Changed the first message of a Slack thread continued with `!fork` to a card showing where it came from, the request, and who asked, with a link to the original thread

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.292
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-06-6-safety-and-privacy-changes-in-v2-1-292|6 Safety and Privacy changes in v2.1.292]] · Safety and Privacy
- [[Changes/Claude Code/2026-10-06-improved-rendering-speed-of-long-bulleted-or-numbered-replies-they-stream-resize|Improved rendering speed of long bulleted or numbered replies]] · Reliability and Performance
- [[Changes/Claude Code/2026-10-06-added-prompt-autocomplete-an-event-a-mod-hooks-to-add-its-own-rows-to-the-prompt|Added prompt.autocomplete, an event a mod hooks to add its own rows to the prompt…]] · Editor Experience
- [[Changes/Claude Code/2026-10-06-2-developer-workflow-changes-in-v2-1-292|2 Developer Workflow changes in v2.1.292]] · Developer Workflow
- [[Changes/Claude Code/2026-10-06-claude-tag-added-an-edit-button-to-the-allowed-domains-card-on-a-channel-s-confi|Claude Tag Added an Edit button to the Allowed domains card on a channel's…]] · Enterprise and Administration
- [[Changes/Claude Code/2026-10-06-improved-the-focus-tip-it-now-invites-you-to-try-focus-view-mid-turn-and-shows-h|Improved the /focus tip]] · Interface Experience
- [[Changes/Claude Code/2026-10-06-added-prompt-caching-to-model-complete-for-mods-prompt-and-system-take-blocks-of|Added prompt caching to $.model.complete for mods]] · Model Support
- [[Changes/Claude Code/2026-10-06-3-agent-mode-changes-in-v2-1-292|3 Agent Mode changes in v2.1.292]] · Agent Mode
- [[Changes/Claude Code/2026-10-06-8-other-changes-in-v2-1-292|8 other changes in v2.1.292]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-10-05 · Claude Code · [[Changes/Claude Code/2026-10-05-14-apps-and-integrations-changes-in-v2-1-290|14 Apps and Integrations changes in v2.1.290]]
- Later: 2026-10-07 · Claude Code · [[Changes/Claude Code/2026-10-07-3-apps-and-integrations-changes-in-v2-1-293|3 Apps and Integrations changes in v2.1.293]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-06-2a26ab&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-06-9-apps-and-integrations-changes-in-v2-1-292.md%0ACard%20ID%3A%20claude-code-2026-10-06-2a26ab%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.292%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->