---
card_id: claude-code-2026-10-31-01fa85
date: '2026-10-31'
description: 'Claude Code · 2026-10-31 · Apps and Integrations: 7 changes in v2.1.316
  — Added pooled group budgets to the Claude apps gateway: one monthly budget that
  a…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1318
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 613b1cd837caeeb20d8613c0e473795afb355f2a90be5ef911dd4252f20790d5
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-31-01fa85
  comparison: ''
  date: '2026-10-31'
  description: 'Claude Code — v2.1.316: 7 Apps and Integrations changes'
  evidence:
  - quote: 'Added pooled group budgets to the Claude apps gateway: one monthly budget
      that a group''s members share, on top of each member''s own limit, set with
      `pooled_budget` on the spend limits admin API'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.316
  - quote: 'Added `managed.policy_mode: layered` to the Claude apps gateway: every
      policy that matches a developer applies, each merged over the ones listed below
      it, not only the first'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.316
  - quote: Added `guardrail.input_tagging` on Claude apps gateway Bedrock upstreams,
      which wraps prompts in the input tags that an Amazon Bedrock guardrail's prompt
      attacks filter needs; `all_messages_and_system` also tags the system prompt
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.316
  - quote: 'Improved `/code-review` started from the Code tab in Claude Desktop or
      on the web: cloud and `claude remote-control` sessions now show the findings
      card, not a plain-text list'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.316
  - quote: '[Cloud sessions] Added a form card to cloud sessions, so you can fill
      in or decline a form an MCP server asks for instead of the request being canceled
      without you seeing it'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.316
  - quote: '[Cloud sessions] Added a "Catching up…" line that shows while a cloud
      or Remote Control session you switch back to is still bringing its messages
      up to date'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.316
  - quote: '[Claude Tag] Changed a Slack channel''s Respond automatically switch to
      a "How Claude participates" choice on the channel''s Configure page and in Claude
      Tag admin settings'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.316
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 7-apps-and-integrations-changes-in-v2-1-316
  source_release: claude-code-2026-10-31-v2-1-316-github-429617179-a30f32c9
  source_type: github_releases
  theme: apps-integrations
  title: 7 Apps and Integrations changes in v2.1.316
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-26-3-apps-and-integrations-changes-in-v2-1-311|3
  Apps and Integrations changes in v2.1.311]]'
- '[[Changes/Claude Code/2026-10-27-2-apps-and-integrations-changes-in-v2-1-312|2
  Apps and Integrations changes in v2.1.312]]'
- '[[Changes/Claude Code/2026-10-30-3-apps-and-integrations-changes-in-v2-1-314|3
  Apps and Integrations changes in v2.1.314]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-31-v2-1-316-github-429617179-a30f32c9|claude-code-2026-10-31-v2-1-316-github-429617179-a30f32c9]]'
source_type: github_releases
theme: apps-integrations
title: 7 Apps and Integrations changes in v2.1.316
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Apps and Integrations changes in v2.1.316

**Claude Code** · 2026-10-31 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.316) · from [[Releases/Claude Code/claude-code-2026-10-31-v2-1-316-github-429617179-a30f32c9|v2.1.316]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added pooled group budgets to the Claude apps gateway: one monthly budget that a group's members share, on top of each member's own limit, set with `pooled_budget` on the spend limits admin API

> Added `managed.policy_mode: layered` to the Claude apps gateway: every policy that matches a developer applies, each merged over the ones listed below it, not only the first

> Added `guardrail.input_tagging` on Claude apps gateway Bedrock upstreams, which wraps prompts in the input tags that an Amazon Bedrock guardrail's prompt attacks filter needs; `all_messages_and_system` also tags the system prompt

> Improved `/code-review` started from the Code tab in Claude Desktop or on the web: cloud and `claude remote-control` sessions now show the findings card, not a plain-text list

> [Cloud sessions] Added a form card to cloud sessions, so you can fill in or decline a form an MCP server asks for instead of the request being canceled without you seeing it

> [Cloud sessions] Added a "Catching up…" line that shows while a cloud or Remote Control session you switch back to is still bringing its messages up to date

> [Claude Tag] Changed a Slack channel's Respond automatically switch to a "How Claude participates" choice on the channel's Configure page and in Claude Tag admin settings

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.316
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-31-2-developer-workflow-changes-in-v2-1-316|2 Developer Workflow changes in v2.1.316]] · Developer Workflow
- [[Changes/Claude Code/2026-10-31-2-automation-and-scheduling-changes-in-v2-1-316|2 Automation and Scheduling changes in v2.1.316]] · Automation and Scheduling
- [[Changes/Claude Code/2026-10-31-vscode-added-sign-in-to-a-claude-apps-gateway-from-the-chat-panel-with-no-termin|VSCode Added sign-in to a Claude apps gateway from the chat panel, with no…]] · Account and Access
- [[Changes/Claude Code/2026-10-31-deprecated-fast-mode-for-opus-4-8-as-of-october-30-2026-it-will-be-removed-on-no|Deprecated fast mode for Opus 4.8 as of October 30, 2026]] · Model Support
- [[Changes/Claude Code/2026-10-31-2-agent-mode-changes-in-v2-1-316|2 Agent Mode changes in v2.1.316]] · Agent Mode
- [[Changes/Claude Code/2026-10-31-2-editor-experience-changes-in-v2-1-316|2 Editor Experience changes in v2.1.316]] · Editor Experience
- [[Changes/Claude Code/2026-10-31-2-enterprise-and-administration-changes-in-v2-1-316|2 Enterprise and Administration changes in v2.1.316]] · Enterprise and Administration
- [[Changes/Claude Code/2026-10-31-2-other-changes-in-v2-1-316|2 other changes in v2.1.316]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-10-30 · Claude Code · [[Changes/Claude Code/2026-10-30-3-apps-and-integrations-changes-in-v2-1-314|3 Apps and Integrations changes in v2.1.314]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-31-01fa85&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-31-7-apps-and-integrations-changes-in-v2-1-316.md%0ACard%20ID%3A%20claude-code-2026-10-31-01fa85%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.316%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->