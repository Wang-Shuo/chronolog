---
card_id: codex-cli-2026-04-30-91eb52
date: '2026-04-30'
description: 'Codex CLI · 2026-04-30 · Apps and Integrations: 37 changes in 0.128.0
  — Improved plugin workflows with marketplace installation, remote bundle caching,
  remote…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2694
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 79ab3d4a640957ca3a21140e7dfc1457105def016c065acf3024a49fd66a7de4
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-04-30-91eb52
  comparison: ''
  date: '2026-04-30'
  description: 'Codex CLI — 0.128.0: 37 Apps and Integrations changes'
  evidence:
  - quote: 'Improved plugin workflows with marketplace installation, remote bundle
      caching, remote uninstall, plugin-bundled hooks, hook enablement state, and
      external-agent config import. (#18704, #19914, #19456, #19705, #19840, #19949)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: Added Codex-pinned versioning for the Python app-server SDK package. (#18996)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19380 chore: drop MCP Plugins and App from Morpheus @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#18907 respect workspace option for disabling plugins @zamoshchin-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#18584 [4/4] Honor Streamable HTTP MCP placement @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19207 [codex] Forward Codex Apps tool call IDs to backend metadata @rreichel3-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19524 [codex] Prune unused codex-mcp API and duplicate helpers @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19526 [codex] Order codex-mcp items by visibility @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19593 test: isolate remote thread store regression from plugin warmups
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19683 test: harden app-server integration tests @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19725 Split MCP connection modules @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19490 Streamline plugin, apps, and skills handlers @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19862 [codex] Shard exec Bazel integration test @starr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#18996 Publish Python SDK with Codex-pinned versioning @sdcoffey'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19884 Add MCP app feature flag @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19452 Stabilize plugin MCP fixture tests @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19914 feat: Cache remote plugin bundles on install @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19456 Add remote plugin uninstall API @xli-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19753 Terminate stdio MCP servers on shutdown to avoid process leaks
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19875 Strip connector provenance metadata from custom MCP tools @colby-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19509 Record MCP result telemetry on mcp.tools.call spans @mchen-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20047 app-server: allow remote_control runtime feature override @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20068 app-server: disable remote control without sqlite @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19705 Discover hooks bundled with plugins @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#18704 /plugins: add marketplace install flow @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20088 Fix flaky plugin hook env test @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19919 app-server: notify clients of remote-control status changes @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20100 Increase plugin hook env test timeout @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19949 Support detect and import MCP, Subagents, hooks, commands from
      external @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20086 Fix plugin list workspace settings test isolation @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20096 feat: Use remote installed plugin cache for skills and MCP @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19966 Require remote plugin detail before uninstall @xli-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20231 [apps] Add apps MCP path override @adaley-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19537 [mcp] Fix plugin MCP approval policy. @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19778 Add hooks/list app-server RPC @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20250 update codex_plugins_beta_setting (from workspace settings) @zamoshchin-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20304 [plugins] Allow MSFT curated plugins in tool_suggest @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 37-apps-and-integrations-changes-in-rust-v0-128-0
  source_release: codex-cli-2026-04-30-rust-v0-128-0-github-315916672-1708ab89
  source_type: github_releases
  theme: apps-integrations
  title: 37 Apps and Integrations changes in rust-v0.128.0
  type: change
related_changes:
- '[[Changes/Devin/2026-04-29-slack-trigger-message-in-sessions-list|Slack Trigger
  Message in Sessions List]]'
- '[[Changes/Dify/2026-04-29-48-apps-and-integrations-changes-in-1-14-0|48 Apps and
  Integrations changes in 1.14.0]]'
- '[[Changes/Superwhisper/2026-04-29-activation-apps-ui-and-indexing-overhaul|Activation
  Apps UI and indexing overhaul]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-04-30-rust-v0-128-0-github-315916672-1708ab89|codex-cli-2026-04-30-rust-v0-128-0-github-315916672-1708ab89]]'
source_type: github_releases
theme: apps-integrations
title: 37 Apps and Integrations changes in rust-v0.128.0
type: change
---

<!-- chronolog:begin region="header" -->
# 37 Apps and Integrations changes in rust-v0.128.0

**Codex CLI** · 2026-04-30 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.128.0) · from [[Releases/Codex CLI/codex-cli-2026-04-30-rust-v0-128-0-github-315916672-1708ab89|0.128.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Improved plugin workflows with marketplace installation, remote bundle caching, remote uninstall, plugin-bundled hooks, hook enablement state, and external-agent config import. (#18704, #19914, #19456, #19705, #19840, #19949)

> Added Codex-pinned versioning for the Python app-server SDK package. (#18996)

> #19380 chore: drop MCP Plugins and App from Morpheus @jif-oai

> #18907 respect workspace option for disabling plugins @zamoshchin-openai

> #18584 [4/4] Honor Streamable HTTP MCP placement @aibrahim-oai

> #19207 [codex] Forward Codex Apps tool call IDs to backend metadata @rreichel3-oai

> #19524 [codex] Prune unused codex-mcp API and duplicate helpers @aibrahim-oai

> #19526 [codex] Order codex-mcp items by visibility @aibrahim-oai

> #19593 test: isolate remote thread store regression from plugin warmups @bolinfest

> #19683 test: harden app-server integration tests @bolinfest

> #19725 Split MCP connection modules @aibrahim-oai

> #19490 Streamline plugin, apps, and skills handlers @pakrym-oai

> #19862 [codex] Shard exec Bazel integration test @starr-openai

> #18996 Publish Python SDK with Codex-pinned versioning @sdcoffey

> #19884 Add MCP app feature flag @mzeng-openai

> #19452 Stabilize plugin MCP fixture tests @dylan-hurd-oai

> #19914 feat: Cache remote plugin bundles on install @xl-openai

> #19456 Add remote plugin uninstall API @xli-oai

> #19753 Terminate stdio MCP servers on shutdown to avoid process leaks @etraut-openai

> #19875 Strip connector provenance metadata from custom MCP tools @colby-oai

> #19509 Record MCP result telemetry on mcp.tools.call spans @mchen-oai

> #20047 app-server: allow remote_control runtime feature override @euroelessar

> #20068 app-server: disable remote control without sqlite @euroelessar

> #19705 Discover hooks bundled with plugins @abhinav-oai

> #18704 /plugins: add marketplace install flow @canvrno-oai

> #20088 Fix flaky plugin hook env test @abhinav-oai

> #19919 app-server: notify clients of remote-control status changes @euroelessar

> #20100 Increase plugin hook env test timeout @abhinav-oai

> #19949 Support detect and import MCP, Subagents, hooks, commands from external @alexsong-oai

> #20086 Fix plugin list workspace settings test isolation @canvrno-oai

> #20096 feat: Use remote installed plugin cache for skills and MCP @xl-openai

> #19966 Require remote plugin detail before uninstall @xli-oai

> #20231 [apps] Add apps MCP path override @adaley-openai

> #19537 [mcp] Fix plugin MCP approval policy. @mzeng-openai

> #19778 Add hooks/list app-server RPC @abhinav-oai

> #20250 update codex_plugins_beta_setting (from workspace settings) @zamoshchin-openai

> #20304 [plugins] Allow MSFT curated plugins in tool_suggest @mzeng-openai

Source: https://github.com/openai/codex/releases/tag/rust-v0.128.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-04-30-2-interface-experience-changes-in-rust-v0-128-0|2 Interface Experience changes in rust-v0.128.0]] · Interface Experience
- [[Changes/Codex CLI/2026-04-30-19805-add-multiagentv2-root-and-subagent-context-hints-jif-oai|♯19805 Add MultiAgentV2 root and subagent context hints @jif-oai]] · Context Window
- [[Changes/Codex CLI/2026-04-30-3-mobile-and-desktop-changes-in-rust-v0-128-0|3 Mobile and Desktop changes in rust-v0.128.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-04-30-12-memory-and-personalization-changes-in-rust-v0-128-0|12 Memory and Personalization changes in rust-v0.128.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-04-30-19-agent-mode-changes-in-rust-v0-128-0|19 Agent Mode changes in rust-v0.128.0]] · Agent Mode
- [[Changes/Codex CLI/2026-04-30-20149-reduce-the-surface-of-collaboration-modes-pakrym-oai|♯20149 Reduce the surface of collaboration modes @pakrym-oai]] · Collaboration
- [[Changes/Codex CLI/2026-04-30-14-developer-workflow-changes-in-rust-v0-128-0|14 Developer Workflow changes in rust-v0.128.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-04-30-19443-add-gpt-image-2-to-bundled-openai-docs-skill-kkahadze-oai|♯19443 Add gpt-image-2 to bundled OpenAI Docs skill @kkahadze-oai]] · Image Generation
- [[Changes/Codex CLI/2026-04-30-3-account-and-access-changes-in-rust-v0-128-0|3 Account and Access changes in rust-v0.128.0]] · Account and Access
- [[Changes/Codex CLI/2026-04-30-20045-fix-plan-mode-nudge-test-after-task-completion-signature-change-canvrno-oa|♯20045 Fix plan mode nudge test after task completion signature change @canvrno-oai]] · Editor Experience
- [[Changes/Codex CLI/2026-04-30-21-safety-and-privacy-changes-in-rust-v0-128-0|21 Safety and Privacy changes in rust-v0.128.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-04-30-10-model-support-changes-in-rust-v0-128-0|10 Model Support changes in rust-v0.128.0]] · Model Support
- [[Changes/Codex CLI/2026-04-30-145-other-changes-in-rust-v0-128-0|145 other changes in rust-v0.128.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-04-29 · Superwhisper · [[Changes/Superwhisper/2026-04-29-activation-apps-ui-and-indexing-overhaul|Activation Apps UI and indexing overhaul]]
- Later: 2026-05-01 · Devin · [[Changes/Devin/2026-05-01-session-origin-in-api|Session Origin in API]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-04-30-91eb52&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-04-30-37-apps-and-integrations-changes-in-rust-v0-128-0.md%0ACard%20ID%3A%20codex-cli-2026-04-30-91eb52%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.128.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->