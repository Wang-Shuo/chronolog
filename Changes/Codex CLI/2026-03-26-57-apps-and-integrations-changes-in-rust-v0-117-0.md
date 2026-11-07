---
card_id: codex-cli-2026-03-26-be1ed6
date: '2026-03-26'
description: 'Codex CLI · 2026-03-26 · Apps and Integrations: 57 changes in 0.117.0
  — Plugin-backed mentions and product gating now behave more predictably, fixing
  cases…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2659
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 926ae782e50dfd367e89906be56c51b8afaa266b06e0e669f9501128fd45878c
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-03-26-be1ed6
  comparison: ''
  date: '2026-03-26'
  description: 'Codex CLI — 0.117.0: 57 Apps and Integrations changes'
  evidence:
  - quote: 'Plugin-backed mentions and product gating now behave more predictably,
      fixing cases where explicit mentions lost context or plugins were filtered incorrectly.
      (#15372, #15263, #15279)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15102 Revert "fix: harden plugin feature gating" @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15104 fix: harden plugin feature gating @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15042 Support featured plugins @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15088 Add Python SDK thread.run convenience methods @shaqayeq-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15011 Forward session and turn headers to MCP HTTP requests @nicholasclark-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15118 [hooks] turn_id extension for Stop & UserPromptSubmit @eternal-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15041 feat: support product-scoped plugins. @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15185 Revert "Forward session and turn headers to MCP HTTP requests"
      @nicholasclark-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#14867 [hooks] use a user message > developer message for prompt continuation
      @eternal-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15217 feat: expose needs_auth for plugin/read. @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15190 Plumb MCP turn metadata through _meta @nicholasclark-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15195 [plugins] Install MCPs when calling plugin/install @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15263 fix: Distinguish missing and empty plugin products @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15252 Disable hooks on windows for now @eternal-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15264 feat: Add One-Time Startup Remote Plugin Sync @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15275 feat: prefer git for curated plugin sync @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#14869 Add remote env CI matrix and integration test @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15244 Pin Python SDK app-server stdio to UTF-8 on Windows @shaqayeq-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15273 [apps] Use ARC for yolo mode. @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15348 Pass platform param to featured plugins @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15372 [plugins] Fix plugin explicit mention context management. @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15376 [apps] Improve app tools loading for TUI. @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15279 Label plugins as plugins, and hide skills/apps for given plugin
      @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15342 Plugins TUI install/uninstall @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15211 [hooks] add non-streaming (non-stdin style) shell-only PreToolUse
      support @eternal-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15554 Add plugin-creator as system skill @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15580 Remove filter from plugins/list result @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15598 Refresh mentions list after plugin install/uninstall @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15606 Pretty plugin labels, preserve plugin app provenance during MCP
      tool refresh @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15438 feat: include marketplace loading error in plugin/list @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15644 fix: keep zsh-fork release assets after removing shell-tool-mcp
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15669 Clean up TUI /plugins row allignment @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15676 Tweak /plugin menu wording @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15666 Suppress plugin-install MCP OAuth URL console spam @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15573 [plugins] Additional gating for tool suggest and apps. @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15674 Use delayed shimmer for plugin loading headers in tui and tui_app_server
      @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15700 Remove provenance filtering in $mentions for apps and skills from
      plugins @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15692 Add legal link to TUI /plugin details @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15708 TUI plugin menu cleanup - hide app ID @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15677 Fix stale quickstart integration assertion @shaqayeq-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15713 [plugins] Flip the flags. @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15719 [plugins] Flip on additional flags. @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15722 [plugins] Add a flag for tool search. @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15734 Update plugin creator skill. @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15519 fix(core): default approval behavior for mcp missing annotations
      @fouad-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15746 Extract codex-utils-plugins crate @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15747 Extract codex-plugin crate @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#14856 [apps][tool_suggest] Remove tool_suggest''s dependency on tool
      search. @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15659 Add MCP tool call spans @nicholasclark-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15802 TUI plugin menu polish @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15800 [mcp] Improve custom MCP elicitation @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15531 [hooks] add non-streaming (non-stdin style) shell-only PostToolUse
      support @eternal-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15820 [plugins] Flip flags on. @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15829 [plugins] Update the suggestable plugins list. @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15805 Add MCP connector metrics @nicholasclark-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15885 [mcp] Fix legacy_tools @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 57-apps-and-integrations-changes-in-rust-v0-117-0
  source_release: codex-cli-2026-03-26-rust-v0-117-0-github-302123790-7cb322b6
  source_type: github_releases
  theme: apps-integrations
  title: 57 Apps and Integrations changes in rust-v0.117.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-03-26-5-apps-and-integrations-changes-in-v2-1-84|5 Apps
  and Integrations changes in v2.1.84]]'
- '[[Changes/Claude Code/2026-03-26-4-apps-and-integrations-changes-in-v2-1-85|4 Apps
  and Integrations changes in v2.1.85]]'
- '[[Changes/Codex CLI/2026-03-26-the-app-server-backed-tui-is-now-enabled-by-default-and-the-plugin-app-rollout-f|The
  app-server-backed TUI is now enabled by default, and the plugin/app rollout…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-03-26-rust-v0-117-0-github-302123790-7cb322b6|codex-cli-2026-03-26-rust-v0-117-0-github-302123790-7cb322b6]]'
source_type: github_releases
theme: apps-integrations
title: 57 Apps and Integrations changes in rust-v0.117.0
type: change
---

<!-- chronolog:begin region="header" -->
# 57 Apps and Integrations changes in rust-v0.117.0

**Codex CLI** · 2026-03-26 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.117.0) · from [[Releases/Codex CLI/codex-cli-2026-03-26-rust-v0-117-0-github-302123790-7cb322b6|0.117.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Plugin-backed mentions and product gating now behave more predictably, fixing cases where explicit mentions lost context or plugins were filtered incorrectly. (#15372, #15263, #15279)

> #15102 Revert "fix: harden plugin feature gating" @xl-openai

> #15104 fix: harden plugin feature gating @xl-openai

> #15042 Support featured plugins @alexsong-oai

> #15088 Add Python SDK thread.run convenience methods @shaqayeq-oai

> #15011 Forward session and turn headers to MCP HTTP requests @nicholasclark-openai

> #15118 [hooks] turn_id extension for Stop & UserPromptSubmit @eternal-openai

> #15041 feat: support product-scoped plugins. @xl-openai

> #15185 Revert "Forward session and turn headers to MCP HTTP requests" @nicholasclark-openai

> #14867 [hooks] use a user message > developer message for prompt continuation @eternal-openai

> #15217 feat: expose needs_auth for plugin/read. @xl-openai

> #15190 Plumb MCP turn metadata through _meta @nicholasclark-openai

> #15195 [plugins] Install MCPs when calling plugin/install @mzeng-openai

> #15263 fix: Distinguish missing and empty plugin products @xl-openai

> #15252 Disable hooks on windows for now @eternal-openai

> #15264 feat: Add One-Time Startup Remote Plugin Sync @xl-openai

> #15275 feat: prefer git for curated plugin sync @xl-openai

> #14869 Add remote env CI matrix and integration test @pakrym-oai

> #15244 Pin Python SDK app-server stdio to UTF-8 on Windows @shaqayeq-oai

> #15273 [apps] Use ARC for yolo mode. @mzeng-openai

> #15348 Pass platform param to featured plugins @alexsong-oai

> #15372 [plugins] Fix plugin explicit mention context management. @mzeng-openai

> #15376 [apps] Improve app tools loading for TUI. @mzeng-openai

> #15279 Label plugins as plugins, and hide skills/apps for given plugin @canvrno-oai

> #15342 Plugins TUI install/uninstall @canvrno-oai

> #15211 [hooks] add non-streaming (non-stdin style) shell-only PreToolUse support @eternal-openai

> #15554 Add plugin-creator as system skill @alexsong-oai

> #15580 Remove filter from plugins/list result @canvrno-oai

> #15598 Refresh mentions list after plugin install/uninstall @canvrno-oai

> #15606 Pretty plugin labels, preserve plugin app provenance during MCP tool refresh @canvrno-oai

> #15438 feat: include marketplace loading error in plugin/list @xl-openai

> #15644 fix: keep zsh-fork release assets after removing shell-tool-mcp @bolinfest

> #15669 Clean up TUI /plugins row allignment @canvrno-oai

> #15676 Tweak /plugin menu wording @canvrno-oai

> #15666 Suppress plugin-install MCP OAuth URL console spam @canvrno-oai

> #15573 [plugins] Additional gating for tool suggest and apps. @mzeng-openai

> #15674 Use delayed shimmer for plugin loading headers in tui and tui_app_server @canvrno-oai

> #15700 Remove provenance filtering in $mentions for apps and skills from plugins @canvrno-oai

> #15692 Add legal link to TUI /plugin details @canvrno-oai

> #15708 TUI plugin menu cleanup - hide app ID @canvrno-oai

> #15677 Fix stale quickstart integration assertion @shaqayeq-oai

> #15713 [plugins] Flip the flags. @mzeng-openai

> #15719 [plugins] Flip on additional flags. @mzeng-openai

> #15722 [plugins] Add a flag for tool search. @mzeng-openai

> #15734 Update plugin creator skill. @xl-openai

> #15519 fix(core): default approval behavior for mcp missing annotations @fouad-openai

> #15746 Extract codex-utils-plugins crate @aibrahim-oai

> #15747 Extract codex-plugin crate @aibrahim-oai

> #14856 [apps][tool_suggest] Remove tool_suggest's dependency on tool search. @mzeng-openai

> #15659 Add MCP tool call spans @nicholasclark-openai

> #15802 TUI plugin menu polish @canvrno-oai

> #15800 [mcp] Improve custom MCP elicitation @mzeng-openai

> #15531 [hooks] add non-streaming (non-stdin style) shell-only PostToolUse support @eternal-openai

> #15820 [plugins] Flip flags on. @mzeng-openai

> #15829 [plugins] Update the suggestable plugins list. @mzeng-openai

> #15805 Add MCP connector metrics @nicholasclark-openai

> #15885 [mcp] Fix legacy_tools @mzeng-openai

Source: https://github.com/openai/codex/releases/tag/rust-v0.117.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-03-26-19-developer-workflow-changes-in-rust-v0-117-0|19 Developer Workflow changes in rust-v0.117.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-03-26-15789-treat-chatgpt-hc-plan-as-enterprise-arnavdugar-openai|♯15789 Treat ChatGPT hc plan as Enterprise @arnavdugar-openai]] · Enterprise and Administration
- [[Changes/Codex CLI/2026-03-26-the-app-server-backed-tui-is-now-enabled-by-default-and-the-plugin-app-rollout-f|The app-server-backed TUI is now enabled by default, and the plugin/app rollout…]] · Apps and Integrations
- [[Changes/Codex CLI/2026-03-26-plugins-are-now-a-first-class-workflow-codex-can-sync-product-scoped-plugins-at|Plugins are now a first-class workflow]] · Search and Browsing
- [[Changes/Codex CLI/2026-03-26-2-image-generation-changes-in-rust-v0-117-0|2 Image Generation changes in rust-v0.117.0]] · Image Generation
- [[Changes/Codex CLI/2026-03-26-15579-increase-voice-space-hold-timeout-to-1s-aibrahim-oai|♯15579 Increase voice space hold timeout to 1s @aibrahim-oai]] · Voice and Audio
- [[Changes/Codex CLI/2026-03-26-2-automation-and-scheduling-changes-in-rust-v0-117-0|2 Automation and Scheduling changes in rust-v0.117.0]] · Automation and Scheduling
- [[Changes/Codex CLI/2026-03-26-5-context-window-changes-in-rust-v0-117-0|5 Context Window changes in rust-v0.117.0]] · Context Window
- [[Changes/Codex CLI/2026-03-26-14945-feat-tui-restore-composer-history-in-app-server-tui-fcoury|♯14945 feat(tui): restore composer history in app-server tui @fcoury]] · Projects and Workspaces
- [[Changes/Codex CLI/2026-03-26-15480-use-shift-left-to-edit-queued-messages-in-tmux-charley-oai|♯15480 Use Shift+Left to edit queued messages in tmux @charley-oai]] · Editor Experience
- [[Changes/Codex CLI/2026-03-26-3-interface-experience-changes-in-rust-v0-117-0|3 Interface Experience changes in rust-v0.117.0]] · Interface Experience
- [[Changes/Codex CLI/2026-03-26-4-account-and-access-changes-in-rust-v0-117-0|4 Account and Access changes in rust-v0.117.0]] · Account and Access
- [[Changes/Codex CLI/2026-03-26-19-agent-mode-changes-in-rust-v0-117-0|19 Agent Mode changes in rust-v0.117.0]] · Agent Mode
- [[Changes/Codex CLI/2026-03-26-3-mobile-and-desktop-changes-in-rust-v0-117-0|3 Mobile and Desktop changes in rust-v0.117.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-03-26-5-safety-and-privacy-changes-in-rust-v0-117-0|5 Safety and Privacy changes in rust-v0.117.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-03-26-3-model-support-changes-in-rust-v0-117-0|3 Model Support changes in rust-v0.117.0]] · Model Support
- [[Changes/Codex CLI/2026-03-26-15175-chore-morpheus-does-not-generate-memories-jif-oai|♯15175 chore: morpheus does not generate memories @jif-oai]] · Memory and Personalization
- [[Changes/Codex CLI/2026-03-26-117-other-changes-in-rust-v0-117-0|117 other changes in rust-v0.117.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-03-26 · Claude Code · [[Changes/Claude Code/2026-03-26-4-apps-and-integrations-changes-in-v2-1-85|4 Apps and Integrations changes in v2.1.85]]
- Later: 2026-03-26 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-03-26-4-apps-and-integrations-changes-in-v1-0-12|4 Apps and Integrations changes in v1.0.12]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-03-26-be1ed6&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-03-26-57-apps-and-integrations-changes-in-rust-v0-117-0.md%0ACard%20ID%3A%20codex-cli-2026-03-26-be1ed6%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.117.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->