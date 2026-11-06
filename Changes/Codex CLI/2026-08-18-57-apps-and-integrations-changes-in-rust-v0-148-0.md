---
card_id: codex-cli-2026-08-18-029114
date: '2026-08-18'
description: 'Codex CLI · 2026-08-18 · Apps and Integrations: 57 changes in 0.148.0
  — Hooks can now run commands asynchronously and invoke MCP tools. (#37533, #38705)'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1244
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 6fe01a96000a3de34660dcd4cb94bf399771028ca4f54916a80d61c4570209c5
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-08-18-029114
  comparison: ''
  date: '2026-08-18'
  description: 'Codex CLI — 0.148.0: 57 Apps and Integrations changes'
  evidence:
  - quote: 'Hooks can now run commands asynchronously and invoke MCP tools. (#37533,
      #38705)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37210 Fetch remote installed plugins across all scopes @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37248 Cover remote MCP discovery timeout cleanup @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37261 Start cached MCP servers lazily for subagents @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37267 Support plugin roots in the host skill loader @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37273 Reuse MCP handlers across sampling steps @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37338 Honor the configured ChatGPT origin in connector install URLs @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37344 Fix subagent MCP startup status settling @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37363 Recognize MCP tool hook configurations @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37366 Harden local MCP server process tree cleanup @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37440 Load plugin skill roots through the host skills service @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37444 Unify plugin skill loading with the host skill service @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37447 Respect plugin skill availability in tool suggestions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37452 Unify plugin skill loading through the shared loader @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37477 Include call IDs in MCP requests and clarify metadata config @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37494 Add MCP event discovery and subscriptions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37533 Support asynchronous command hooks @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37645 Improve plugin install failure analytics @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37773 Forward install attempt IDs for remote plugins @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37806 Initialize the install attempt ID in the plugin analytics test
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37832 Remove obsolete plugin skill discovery helpers @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37836 Run plugin and skill tests on Windows @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37850 Expose plugin ownership in MCP server status @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37864 Support MCP form input in full-access user threads @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37896 Add hermetic Windows SDK and MSVC runtime repositories @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37970 Cache tool catalogs for streamable HTTP MCP servers @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38035 Propagate MCP elicitation event delivery failures @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38040 Propagate custom CA settings to local MCP servers @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38057 Track artifact operations from trusted plugin markers @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38081 Use `ReviewDecision` for MCP tool approvals @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38103 Avoid cloning MCP invocations in TUI history @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38108 Route MCP tool calls through shared approval handling @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38184 Run search tool integration tests on Windows @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38189 Run plugin app-server tests in automatic environments @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38217 Start required cached MCP servers lazily for subagents @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38238 Add manifest-defined metrics for trusted plugin scripts @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38239 Add bounded plugin measurement analytics @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38245 Add dynamic HTTP header helpers for MCP servers @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38252 Collect metrics from plugin shell commands @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38253 Collect plugin metrics from unified exec commands @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38276 Track plugin metrics for background unified exec commands @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38278 Add app-server coverage for plugin measurement analytics @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38283 Collect plugin metrics from remote executors @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38394 Reject sessions with unloadable required managed hooks @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38403 Expose conversation history to tool lifecycle extensions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38436 Add rustls fallback for local MCP HTTP requests @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38484 Search selected plugin apps before falling back @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38492 Enforce strict auto-review for MCP tool calls @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38493 Reuse pending MCP startups during reconciliation @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38568 Run tool start callbacks after pre-tool hooks @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38592 Let extensions resolve approval reviews before Guardian @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38602 Isolate Guardian reviewer sessions from parent extensions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38623 Preserve MCP namespace descriptions in the tool catalog cache @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38634 Add MCP protocol discovery metrics @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38703 Refresh hook runtimes after plugin changes @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38705 Add MCP tool handler support to the hooks engine @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38743 Scope TUI app directory state to the active context @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 57-apps-and-integrations-changes-in-rust-v0-148-0
  source_release: codex-cli-2026-08-18-rust-v0-148-0-github-372686337-4265c0ae
  source_type: github_releases
  theme: apps-integrations
  title: 57 Apps and Integrations changes in rust-v0.148.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-08-17-remote-control-signing-this-computer-in-to-a-different-claude-ai-account-or-orga|Remote
  Control: signing this computer in to a different claude.ai account…]]'
- '[[Changes/Cursor/2026-08-17-app-extensions-for-cursor-repos|App extensions for
  Cursor repos]]'
- '[[Changes/Cursor/2026-08-17-settings|Settings]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-08-18-rust-v0-148-0-github-372686337-4265c0ae|codex-cli-2026-08-18-rust-v0-148-0-github-372686337-4265c0ae]]'
source_type: github_releases
theme: apps-integrations
title: 57 Apps and Integrations changes in rust-v0.148.0
type: change
---

<!-- chronolog:begin region="header" -->
# 57 Apps and Integrations changes in rust-v0.148.0

**Codex CLI** · 2026-08-18 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.148.0) · from [[Releases/Codex CLI/codex-cli-2026-08-18-rust-v0-148-0-github-372686337-4265c0ae|0.148.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Hooks can now run commands asynchronously and invoke MCP tools. (#37533, #38705)

> #37210 Fetch remote installed plugins across all scopes @copyberry

> #37248 Cover remote MCP discovery timeout cleanup @copyberry

> #37261 Start cached MCP servers lazily for subagents @copyberry

> #37267 Support plugin roots in the host skill loader @copyberry

> #37273 Reuse MCP handlers across sampling steps @copyberry

> #37338 Honor the configured ChatGPT origin in connector install URLs @copyberry

> #37344 Fix subagent MCP startup status settling @copyberry

> #37363 Recognize MCP tool hook configurations @copyberry

> #37366 Harden local MCP server process tree cleanup @copyberry

> #37440 Load plugin skill roots through the host skills service @copyberry

> #37444 Unify plugin skill loading with the host skill service @copyberry

> #37447 Respect plugin skill availability in tool suggestions @copyberry

> #37452 Unify plugin skill loading through the shared loader @copyberry

> #37477 Include call IDs in MCP requests and clarify metadata config @copyberry

> #37494 Add MCP event discovery and subscriptions @copyberry

> #37533 Support asynchronous command hooks @copyberry

> #37645 Improve plugin install failure analytics @copyberry

> #37773 Forward install attempt IDs for remote plugins @copyberry

> #37806 Initialize the install attempt ID in the plugin analytics test @copyberry

> #37832 Remove obsolete plugin skill discovery helpers @copyberry

> #37836 Run plugin and skill tests on Windows @copyberry

> #37850 Expose plugin ownership in MCP server status @copyberry

> #37864 Support MCP form input in full-access user threads @copyberry

> #37896 Add hermetic Windows SDK and MSVC runtime repositories @copyberry

> #37970 Cache tool catalogs for streamable HTTP MCP servers @copyberry

> #38035 Propagate MCP elicitation event delivery failures @copyberry

> #38040 Propagate custom CA settings to local MCP servers @copyberry

> #38057 Track artifact operations from trusted plugin markers @copyberry

> #38081 Use `ReviewDecision` for MCP tool approvals @copyberry

> #38103 Avoid cloning MCP invocations in TUI history @copyberry

> #38108 Route MCP tool calls through shared approval handling @copyberry

> #38184 Run search tool integration tests on Windows @copyberry

> #38189 Run plugin app-server tests in automatic environments @copyberry

> #38217 Start required cached MCP servers lazily for subagents @copyberry

> #38238 Add manifest-defined metrics for trusted plugin scripts @copyberry

> #38239 Add bounded plugin measurement analytics @copyberry

> #38245 Add dynamic HTTP header helpers for MCP servers @copyberry

> #38252 Collect metrics from plugin shell commands @copyberry

> #38253 Collect plugin metrics from unified exec commands @copyberry

> #38276 Track plugin metrics for background unified exec commands @copyberry

> #38278 Add app-server coverage for plugin measurement analytics @copyberry

> #38283 Collect plugin metrics from remote executors @copyberry

> #38394 Reject sessions with unloadable required managed hooks @copyberry

> #38403 Expose conversation history to tool lifecycle extensions @copyberry

> #38436 Add rustls fallback for local MCP HTTP requests @copyberry

> #38484 Search selected plugin apps before falling back @copyberry

> #38492 Enforce strict auto-review for MCP tool calls @copyberry

> #38493 Reuse pending MCP startups during reconciliation @copyberry

> #38568 Run tool start callbacks after pre-tool hooks @copyberry

> #38592 Let extensions resolve approval reviews before Guardian @copyberry

> #38602 Isolate Guardian reviewer sessions from parent extensions @copyberry

> #38623 Preserve MCP namespace descriptions in the tool catalog cache @copyberry

> #38634 Add MCP protocol discovery metrics @copyberry

> #38703 Refresh hook runtimes after plugin changes @copyberry

> #38705 Add MCP tool handler support to the hooks engine @copyberry

> #38743 Scope TUI app directory state to the active context @copyberry

Source: https://github.com/openai/codex/releases/tag/rust-v0.148.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-08-18-13-interface-experience-changes-in-rust-v0-148-0|13 Interface Experience changes in rust-v0.148.0]] · Interface Experience
- [[Changes/Codex CLI/2026-08-18-18-model-support-changes-in-rust-v0-148-0|18 Model Support changes in rust-v0.148.0]] · Model Support
- [[Changes/Codex CLI/2026-08-18-3-mobile-and-desktop-changes-in-rust-v0-148-0|3 Mobile and Desktop changes in rust-v0.148.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-08-18-5-developer-workflow-changes-in-rust-v0-148-0|5 Developer Workflow changes in rust-v0.148.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-08-18-38650-canonicalize-default-namespaces-in-grpc-subscription-filters-copyberry|♯38650 Canonicalize default namespaces in gRPC subscription filters @copyberry]] · Pricing Model
- [[Changes/Codex CLI/2026-08-18-37828-track-running-unified-exec-processes-at-turn-completion-copyberry|♯37828 Track running unified exec processes at turn completion @copyberry]] · Editor Experience
- [[Changes/Codex CLI/2026-08-18-17-safety-and-privacy-changes-in-rust-v0-148-0|17 Safety and Privacy changes in rust-v0.148.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-08-18-16-account-and-access-changes-in-rust-v0-148-0|16 Account and Access changes in rust-v0.148.0]] · Account and Access
- [[Changes/Codex CLI/2026-08-18-13-context-window-changes-in-rust-v0-148-0|13 Context Window changes in rust-v0.148.0]] · Context Window
- [[Changes/Codex CLI/2026-08-18-12-agent-mode-changes-in-rust-v0-148-0|12 Agent Mode changes in rust-v0.148.0]] · Agent Mode
- [[Changes/Codex CLI/2026-08-18-38024-expose-image-generation-usage-limit-failures-copyberry|♯38024 Expose image generation usage-limit failures @copyberry]] · Image Generation
- [[Changes/Codex CLI/2026-08-18-5-collaboration-changes-in-rust-v0-148-0|5 Collaboration changes in rust-v0.148.0]] · Collaboration
- [[Changes/Codex CLI/2026-08-18-231-other-changes-in-rust-v0-148-0|231 other changes in rust-v0.148.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-08-17 · Cursor · [[Changes/Cursor/2026-08-17-settings|Settings]]
- Later: 2026-08-19 · Claude Code · [[Changes/Claude Code/2026-08-19-sigterm-in-print-sdk-mode-no-longer-records-an-interrupted-turn-or-synthetic-too|SIGTERM in print/SDK mode no longer records an interrupted turn or synthetic tool…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-08-18-029114&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-08-18-57-apps-and-integrations-changes-in-rust-v0-148-0.md%0ACard%20ID%3A%20codex-cli-2026-08-18-029114%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.148.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->