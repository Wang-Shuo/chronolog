---
card_id: claude-code-2026-09-11-4d50a7
date: '2026-09-11'
description: 'Claude Code · 2026-09-11 · Apps and Integrations: 5 changes in v2.1.269
  — Added `claude plugin eval`: run a plugin''s eval suite against Claude Code and
  get…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1268
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b8724a57e7824ff6d04400184ebf5a224874c5b7f7f72898e8f3f3e56c6fb9b9
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-11-4d50a7
  comparison: ''
  date: '2026-09-11'
  description: 'Claude Code — v2.1.269: 5 Apps and Integrations changes'
  evidence:
  - quote: 'Added `claude plugin eval`: run a plugin''s eval suite against Claude
      Code and get scored, reproducible results (JSON + HTML report); see `claude
      plugin eval --help`'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.269
  - quote: Improved the Skill tool's "Unknown skill" error to name the plugin skill's
      full name when a bare name matches exactly one plugin skill
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.269
  - quote: 'Improved first-party sessions with telemetry disabled: an `alwaysLoad`
      MCP server that finishes connecting mid-conversation is usable on the next turn
      without a tool-search round trip'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.269
  - quote: '[VSCode] Added a Hooks dialog to the command menu for viewing hooks and
      adding, editing, or removing them in user, project, and local settings; managed,
      plugin, and session hooks stay read-only'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.269
  - quote: '[Claude Tag] Improved scheduled routines in Slack channels: a routine
      run can now reply in an existing thread instead of always posting a new top-level
      channel message'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.269
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 5-apps-and-integrations-changes-in-v2-1-269
  source_release: claude-code-2026-09-11-v2-1-269-github-387243742-288e9189
  source_type: github_releases
  theme: apps-integrations
  title: 5 Apps and Integrations changes in v2.1.269
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-09-10-the-data-plugin-helps-you-analyze-connected-business-data-in-chatgpt-work-and-co|Data
  plugin in ChatGPT Work and Codex]]'
- '[[Changes/Claude Code/2026-09-10-7-apps-and-integrations-changes-in-v2-1-268|7
  Apps and Integrations changes in v2.1.268]]'
- '[[Changes/ChatGPT/2026-09-11-we-re-planning-to-retire-custom-gpts-across-chatgpt-plans-and-provide-a-migratio|Planned
  custom GPT retirement and migration to plugins]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-11-v2-1-269-github-387243742-288e9189|claude-code-2026-09-11-v2-1-269-github-387243742-288e9189]]'
source_type: github_releases
theme: apps-integrations
title: 5 Apps and Integrations changes in v2.1.269
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Apps and Integrations changes in v2.1.269

**Claude Code** · 2026-09-11 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.269) · from [[Releases/Claude Code/claude-code-2026-09-11-v2-1-269-github-387243742-288e9189|v2.1.269]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `claude plugin eval`: run a plugin's eval suite against Claude Code and get scored, reproducible results (JSON + HTML report); see `claude plugin eval --help`

> Improved the Skill tool's "Unknown skill" error to name the plugin skill's full name when a bare name matches exactly one plugin skill

> Improved first-party sessions with telemetry disabled: an `alwaysLoad` MCP server that finishes connecting mid-conversation is usable on the next turn without a tool-search round trip

> [VSCode] Added a Hooks dialog to the command menu for viewing hooks and adding, editing, or removing them in user, project, and local settings; managed, plugin, and session hooks stay read-only

> [Claude Tag] Improved scheduled routines in Slack channels: a routine run can now reply in an existing thread instead of always posting a new top-level channel message

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.269
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-11-vscode-improved-documents-and-messages-written-for-someone-other-than-the-user-c|VSCode Improved documents and messages written for someone other than the user]] · Files and Data
- [[Changes/Claude Code/2026-09-11-added-output-style-name-to-list-and-switch-output-styles-including-over-remote-c|Added /output-style name to list and switch output styles, including over Remote…]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-11-changed-skills-synced-from-claude-ai-in-cloud-sessions-to-be-named-anthropic-ski|Changed skills synced from claude.ai in cloud sessions to be named…]] · Mobile and Desktop
- [[Changes/Claude Code/2026-09-11-added-otel-metrics-include-repository-to-tag-opentelemetry-metrics-and-events-wi|Added OTEL_METRICS_INCLUDE_REPOSITORY to tag OpenTelemetry metrics and events…]] · Developer Workflow
- [[Changes/Claude Code/2026-09-11-3-interface-experience-changes-in-v2-1-269|3 Interface Experience changes in v2.1.269]] · Interface Experience
- [[Changes/Claude Code/2026-09-11-improved-responsiveness-in-long-sessions-transcript-updates-no-longer-re-process|Improved responsiveness in long sessions]] · Reliability and Performance
- [[Changes/Claude Code/2026-09-11-3-editor-experience-changes-in-v2-1-269|3 Editor Experience changes in v2.1.269]] · Editor Experience
- [[Changes/Claude Code/2026-09-11-added-claude-code-gateway-model-discovery-timeout-ms-to-extend-the-llm-gateway-v|Added CLAUDE_CODE_GATEWAY_MODEL_DISCOVERY_TIMEOUT_MS to extend the LLM gateway…]] · Model Support
- [[Changes/Claude Code/2026-09-11-2-agent-mode-changes-in-v2-1-269|2 Agent Mode changes in v2.1.269]] · Agent Mode
- [[Changes/Claude Code/2026-09-11-5-safety-and-privacy-changes-in-v2-1-269|5 Safety and Privacy changes in v2.1.269]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-11-11-other-changes-in-v2-1-269|11 other changes in v2.1.269]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-09-11 · ChatGPT · [[Changes/ChatGPT/2026-09-11-we-re-planning-to-retire-custom-gpts-across-chatgpt-plans-and-provide-a-migratio|Planned custom GPT retirement and migration to plugins]]
- Later: 2026-09-14 · ChatGPT · [[Changes/ChatGPT/2026-09-14-for-new-health-plugin-connections-chatgpt-will-now-default-to-each-user-s-global|For new Health plugin connections, ChatGPT will now default to each user’s global…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-11-4d50a7&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-11-5-apps-and-integrations-changes-in-v2-1-269.md%0ACard%20ID%3A%20claude-code-2026-09-11-4d50a7%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.269%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->