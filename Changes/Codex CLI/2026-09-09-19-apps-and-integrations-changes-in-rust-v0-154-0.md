---
card_id: codex-cli-2026-09-09-2c7ca8
date: '2026-09-09'
description: 'Codex CLI · 2026-09-09 · Apps and Integrations: 19 changes in 0.154.0
  — Copying responses preserves formatting in rich-text apps, and `/copy` can copy
  status…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2826
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 3b0317593320610c341c3cac1d1960901823b9745fbb7808477dea63822e3fa1
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-09-09-2c7ca8
  comparison: ''
  date: '2026-09-09'
  description: 'Codex CLI — 0.154.0: 19 Apps and Integrations changes'
  evidence:
  - quote: 'Copying responses preserves formatting in rich-text apps, and `/copy`
      can copy status output or individual session fields. (#42847, #43055)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: 'Existing sessions pick up newly installed plugin tools and refresh skills
      and hooks after external plugin upgrades or rollbacks. (#42284, #42593, #42990)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: The deprecated `codex mcp-server` entry point is no longer available. (#42993)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42192 Use native spawning for bare macOS MCP commands @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42284 Refresh plugin skills after out-of-process version changes @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42370 Improve MCP server startup error logging @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42406 Honor explicit plugin mentions during MCP startup @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42445 Include originator in plugin measurement analytics @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42593 Reload user config after local plugin installation @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42598 Report MCP tool discovery errors in server status @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42668 Cancel remote control enrollment on stdio shutdown @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42990 Refresh session hooks after external plugin updates @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42993 Remove the deprecated `codex mcp-server` command @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43031 Keep refreshed MCP tool catalogs with their clients @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43074 Show a retryable error when the apps popup fails to load @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43289 Add capability-gated MCP user-verification handling @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43352 Add opt-in MCP user-verification transport @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43428 Notify opted-in stdio MCP servers of auth changes @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43447 Route MCP elicitations through the shared approval decision path
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 19-apps-and-integrations-changes-in-rust-v0-154-0
  source_release: codex-cli-2026-09-09-rust-v0-154-0-github-385887902-ee241ff1
  source_type: github_releases
  theme: apps-integrations
  title: 19 Apps and Integrations changes in rust-v0.154.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-08-4-apps-and-integrations-changes-in-v2-1-265|4
  Apps and Integrations changes in v2.1.265]]'
- '[[Changes/OpenClaw/2026-09-08-23-apps-and-integrations-changes-in-v2026-9-3|23
  Apps and Integrations changes in v2026.9.3]]'
- '[[Changes/Claude Code/2026-09-09-claude-tag-added-a-use-a-custom-connector-link-to-the-preset-connection-forms-in|Claude
  Tag Added a "Use a custom connector" link to the preset connection forms…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-09-09-rust-v0-154-0-github-385887902-ee241ff1|codex-cli-2026-09-09-rust-v0-154-0-github-385887902-ee241ff1]]'
source_type: github_releases
theme: apps-integrations
title: 19 Apps and Integrations changes in rust-v0.154.0
type: change
---

<!-- chronolog:begin region="header" -->
# 19 Apps and Integrations changes in rust-v0.154.0

**Codex CLI** · 2026-09-09 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.154.0) · from [[Releases/Codex CLI/codex-cli-2026-09-09-rust-v0-154-0-github-385887902-ee241ff1|0.154.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Copying responses preserves formatting in rich-text apps, and `/copy` can copy status output or individual session fields. (#42847, #43055)

> Existing sessions pick up newly installed plugin tools and refresh skills and hooks after external plugin upgrades or rollbacks. (#42284, #42593, #42990)

> The deprecated `codex mcp-server` entry point is no longer available. (#42993)

> #42192 Use native spawning for bare macOS MCP commands @copyberry

> #42284 Refresh plugin skills after out-of-process version changes @copyberry

> #42370 Improve MCP server startup error logging @copyberry

> #42406 Honor explicit plugin mentions during MCP startup @copyberry

> #42445 Include originator in plugin measurement analytics @copyberry

> #42593 Reload user config after local plugin installation @copyberry

> #42598 Report MCP tool discovery errors in server status @copyberry

> #42668 Cancel remote control enrollment on stdio shutdown @copyberry

> #42990 Refresh session hooks after external plugin updates @copyberry

> #42993 Remove the deprecated `codex mcp-server` command @copyberry

> #43031 Keep refreshed MCP tool catalogs with their clients @copyberry

> #43074 Show a retryable error when the apps popup fails to load @copyberry

> #43289 Add capability-gated MCP user-verification handling @copyberry

> #43352 Add opt-in MCP user-verification transport @copyberry

> #43428 Notify opted-in stdio MCP servers of auth changes @copyberry

> #43447 Route MCP elicitations through the shared approval decision path @copyberry

Source: https://github.com/openai/codex/releases/tag/rust-v0.154.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-09-09-21-model-support-changes-in-rust-v0-154-0|21 Model Support changes in rust-v0.154.0]] · Model Support
- [[Changes/Codex CLI/2026-09-09-5-account-and-access-changes-in-rust-v0-154-0|5 Account and Access changes in rust-v0.154.0]] · Account and Access
- [[Changes/Codex CLI/2026-09-09-4-interface-experience-changes-in-rust-v0-154-0|4 Interface Experience changes in rust-v0.154.0]] · Interface Experience
- [[Changes/Codex CLI/2026-09-09-17-context-window-changes-in-rust-v0-154-0|17 Context Window changes in rust-v0.154.0]] · Context Window
- [[Changes/Codex CLI/2026-09-09-6-mobile-and-desktop-changes-in-rust-v0-154-0|6 Mobile and Desktop changes in rust-v0.154.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-09-09-25-safety-and-privacy-changes-in-rust-v0-154-0|25 Safety and Privacy changes in rust-v0.154.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-09-09-gpt-6-astra-is-now-available-in-the-model-picker-and-amazon-bedrock-catalogs-428|GPT-6-Astra is now available in the model picker and Amazon Bedrock catalogs]] · Model Support
- [[Changes/Codex CLI/2026-09-09-20-voice-and-audio-changes-in-rust-v0-154-0|20 Voice and Audio changes in rust-v0.154.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-09-09-2-memory-and-personalization-changes-in-rust-v0-154-0|2 Memory and Personalization changes in rust-v0.154.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-09-09-experimental-worktree-support-lets-you-create-isolated-checkouts-for-new-or-fork|Experimental worktree support lets you create isolated checkouts for new or forked…]] · Search and Browsing
- [[Changes/Codex CLI/2026-09-09-42746-handle-pending-network-reviews-after-process-completion-copyberry|♯42746 Handle pending network reviews after process completion @copyberry]] · Editor Experience
- [[Changes/Codex CLI/2026-09-09-6-agent-mode-changes-in-rust-v0-154-0|6 Agent Mode changes in rust-v0.154.0]] · Agent Mode
- [[Changes/Codex CLI/2026-09-09-42306-stabilize-the-detached-exec-server-session-resume-test-copyberry|♯42306 Stabilize the detached exec-server session resume test @copyberry]] · Projects and Workspaces
- [[Changes/Codex CLI/2026-09-09-6-collaboration-changes-in-rust-v0-154-0|6 Collaboration changes in rust-v0.154.0]] · Collaboration
- [[Changes/Codex CLI/2026-09-09-7-developer-workflow-changes-in-rust-v0-154-0|7 Developer Workflow changes in rust-v0.154.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-09-09-119-other-changes-in-rust-v0-154-0|119 other changes in rust-v0.154.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-09-09 · Claude Code · [[Changes/Claude Code/2026-09-09-claude-tag-added-a-use-a-custom-connector-link-to-the-preset-connection-forms-in|Claude Tag Added a "Use a custom connector" link to the preset connection forms…]]
- Later: 2026-09-09 · Kimi Code · [[Changes/Kimi Code/2026-09-09-remote-control-is-now-always-on-the-experimental-kimi-code-experimental-remote-c|Remote Control is now always on]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-09-09-2c7ca8&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-09-09-19-apps-and-integrations-changes-in-rust-v0-154-0.md%0ACard%20ID%3A%20codex-cli-2026-09-09-2c7ca8%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.154.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->