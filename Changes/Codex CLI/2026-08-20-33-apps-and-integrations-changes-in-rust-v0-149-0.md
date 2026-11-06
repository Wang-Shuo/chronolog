---
card_id: codex-cli-2026-08-20-b0b4dd
date: '2026-08-20'
description: 'Codex CLI · 2026-08-20 · Apps and Integrations: 33 changes in 0.149.0
  — SDK users can now pass exact CLI config overrides and select `max` or `ultra`
  reasoning…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1246
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: dfe9801d6a598f5f2c878b40924f02f5f49b6a6f587a8b55eb2a906e1aa9c22b
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-08-20-b0b4dd
  comparison: ''
  date: '2026-08-20'
  description: 'Codex CLI — 0.149.0: 33 Apps and Integrations changes'
  evidence:
  - quote: 'SDK users can now pass exact CLI config overrides and select `max` or
      `ultra` reasoning effort. (#38817, #39662)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#38817 Add raw config overrides to the TypeScript SDK @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#38840 Identify Mac mini hosts in remote control handshakes @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#38994 Remove the workspace settings gate for apps and plugins @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39017 Move MCP policy types into `codex-protocol` @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39023 Reduce retained MCP result data in TUI history @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39046 Restrict MCP HTTP redirects to the configured origin @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39047 Skip plugin hook loading when hooks are disabled @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39051 Use installed callable apps for TUI mentions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39058 Tag Codex Apps protocol discovery metrics @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39079 Apply user MCP policy to selected executor plugins @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39131 Validate identifiers in plugin creator workflows @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39143 Hydrate recommended plugin metadata on selection @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39155 Prepare Python SDK 0.147.0 stable release @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39187 Scope MCP app resource reads to their originating call @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39192 Preserve MCP resource origins across compaction @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39240 Deduplicate remote plugin bundle syncs with shared semaphores @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39244 Scope MCP resource reads by connector @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39296 Enable MCP tool hooks in Codex sessions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39309 Attribute executor skill invocations to plugins @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39314 Run hooks with the captured session environment @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39331 Route hook MCP calls through current connections @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39335 Enforce environment MCP policies @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39474 Consolidate Guardian extensions into `codex-guardian-v2` @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39520 Isolate automatic plugin Git operations @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39585 Test plugin sync isolation from repository Git config @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39590 Harden plugin manifest handling during installation @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39594 Raise the MCP tool name limit to 128 bytes @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39609 Limit Bazel integration test threads on macOS @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39655 Make core integration test permissions explicit @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39657 Warn when launching the deprecated MCP server @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39663 Restrict plugin migration to home scope @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39665 Add macOS Seatbelt filesystem integration tests @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 33-apps-and-integrations-changes-in-rust-v0-149-0
  source_release: codex-cli-2026-08-20-rust-v0-149-0-github-374028976-829da944
  source_type: github_releases
  theme: apps-integrations
  title: 33 Apps and Integrations changes in rust-v0.149.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-08-19-sigterm-in-print-sdk-mode-no-longer-records-an-interrupted-turn-or-synthetic-too|SIGTERM
  in print/SDK mode no longer records an interrupted turn or synthetic tool…]]'
- '[[Changes/ChatGPT/2026-08-20-use-apple-messages-from-codex-and-chatgpt-work-on-apple-silicon-macs-the-apple-m|Use
  Apple Messages from Codex and ChatGPT Work]]'
- '[[Changes/Claude Code/2026-08-20-6-apps-and-integrations-changes-in-v2-1-238|6
  Apps and Integrations changes in v2.1.238]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-08-20-rust-v0-149-0-github-374028976-829da944|codex-cli-2026-08-20-rust-v0-149-0-github-374028976-829da944]]'
source_type: github_releases
theme: apps-integrations
title: 33 Apps and Integrations changes in rust-v0.149.0
type: change
---

<!-- chronolog:begin region="header" -->
# 33 Apps and Integrations changes in rust-v0.149.0

**Codex CLI** · 2026-08-20 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.149.0) · from [[Releases/Codex CLI/codex-cli-2026-08-20-rust-v0-149-0-github-374028976-829da944|0.149.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> SDK users can now pass exact CLI config overrides and select `max` or `ultra` reasoning effort. (#38817, #39662)

> #38817 Add raw config overrides to the TypeScript SDK @copyberry

> #38840 Identify Mac mini hosts in remote control handshakes @copyberry

> #38994 Remove the workspace settings gate for apps and plugins @copyberry

> #39017 Move MCP policy types into `codex-protocol` @copyberry

> #39023 Reduce retained MCP result data in TUI history @copyberry

> #39046 Restrict MCP HTTP redirects to the configured origin @copyberry

> #39047 Skip plugin hook loading when hooks are disabled @copyberry

> #39051 Use installed callable apps for TUI mentions @copyberry

> #39058 Tag Codex Apps protocol discovery metrics @copyberry

> #39079 Apply user MCP policy to selected executor plugins @copyberry

> #39131 Validate identifiers in plugin creator workflows @copyberry

> #39143 Hydrate recommended plugin metadata on selection @copyberry

> #39155 Prepare Python SDK 0.147.0 stable release @copyberry

> #39187 Scope MCP app resource reads to their originating call @copyberry

> #39192 Preserve MCP resource origins across compaction @copyberry

> #39240 Deduplicate remote plugin bundle syncs with shared semaphores @copyberry

> #39244 Scope MCP resource reads by connector @copyberry

> #39296 Enable MCP tool hooks in Codex sessions @copyberry

> #39309 Attribute executor skill invocations to plugins @copyberry

> #39314 Run hooks with the captured session environment @copyberry

> #39331 Route hook MCP calls through current connections @copyberry

> #39335 Enforce environment MCP policies @copyberry

> #39474 Consolidate Guardian extensions into `codex-guardian-v2` @copyberry

> #39520 Isolate automatic plugin Git operations @copyberry

> #39585 Test plugin sync isolation from repository Git config @copyberry

> #39590 Harden plugin manifest handling during installation @copyberry

> #39594 Raise the MCP tool name limit to 128 bytes @copyberry

> #39609 Limit Bazel integration test threads on macOS @copyberry

> #39655 Make core integration test permissions explicit @copyberry

> #39657 Warn when launching the deprecated MCP server @copyberry

> #39663 Restrict plugin migration to home scope @copyberry

> #39665 Add macOS Seatbelt filesystem integration tests @copyberry

Source: https://github.com/openai/codex/releases/tag/rust-v0.149.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-08-20-2-reliability-and-performance-changes-in-rust-v0-149-0|2 Reliability and Performance changes in rust-v0.149.0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-08-20-6-model-support-changes-in-rust-v0-149-0|6 Model Support changes in rust-v0.149.0]] · Model Support
- [[Changes/Codex CLI/2026-08-20-18-developer-workflow-changes-in-rust-v0-149-0|18 Developer Workflow changes in rust-v0.149.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-08-20-2-memory-and-personalization-changes-in-rust-v0-149-0|2 Memory and Personalization changes in rust-v0.149.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-08-20-39045-add-managed-gates-for-in-app-chat-and-dictation-copyberry|♯39045 Add managed gates for in-app chat and dictation @copyberry]] · Voice and Audio
- [[Changes/Codex CLI/2026-08-20-18-safety-and-privacy-changes-in-rust-v0-149-0|18 Safety and Privacy changes in rust-v0.149.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-08-20-9-context-window-changes-in-rust-v0-149-0|9 Context Window changes in rust-v0.149.0]] · Context Window
- [[Changes/Codex CLI/2026-08-20-2-collaboration-changes-in-rust-v0-149-0|2 Collaboration changes in rust-v0.149.0]] · Collaboration
- [[Changes/Codex CLI/2026-08-20-5-editor-experience-changes-in-rust-v0-149-0|5 Editor Experience changes in rust-v0.149.0]] · Editor Experience
- [[Changes/Codex CLI/2026-08-20-7-mobile-and-desktop-changes-in-rust-v0-149-0|7 Mobile and Desktop changes in rust-v0.149.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-08-20-3-interface-experience-changes-in-rust-v0-149-0|3 Interface Experience changes in rust-v0.149.0]] · Interface Experience
- [[Changes/Codex CLI/2026-08-20-8-account-and-access-changes-in-rust-v0-149-0|8 Account and Access changes in rust-v0.149.0]] · Account and Access
- [[Changes/Codex CLI/2026-08-20-39072-persist-generated-images-through-turn-executors-copyberry|♯39072 Persist generated images through turn executors @copyberry]] · Image Generation
- [[Changes/Codex CLI/2026-08-20-12-agent-mode-changes-in-rust-v0-149-0|12 Agent Mode changes in rust-v0.149.0]] · Agent Mode
- [[Changes/Codex CLI/2026-08-20-39283-document-secure-devcontainer-dns-exfiltration-risk-copyberry|♯39283 Document secure devcontainer DNS exfiltration risk @copyberry]] · Files and Data
- [[Changes/Codex CLI/2026-08-20-39006-emit-api-key-turn-cost-telemetry-from-app-server-copyberry|♯39006 Emit API-key turn cost telemetry from app-server @copyberry]] · Pricing Model
- [[Changes/Codex CLI/2026-08-20-125-other-changes-in-rust-v0-149-0|125 other changes in rust-v0.149.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-08-20 · Claude Code · [[Changes/Claude Code/2026-08-20-6-apps-and-integrations-changes-in-v2-1-238|6 Apps and Integrations changes in v2.1.238]]
- Later: 2026-08-21 · ChatGPT · [[Changes/ChatGPT/2026-08-21-updated-plugin-recommendations-make-it-easier-to-find-tools-people-continue-to-u|Updated plugin recommendations make it easier to find tools people continue to use]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-08-20-b0b4dd&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-08-20-33-apps-and-integrations-changes-in-rust-v0-149-0.md%0ACard%20ID%3A%20codex-cli-2026-08-20-b0b4dd%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.149.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->