---
card_id: codex-cli-2026-04-15-f42c11
date: '2026-04-15'
description: 'Codex CLI · 2026-04-15 · Safety and Privacy: 10 changes in 0.121.0 —
  Expanded MCP/plugin support with MCP Apps tool calls, namespaced MCP registration…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2087
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 560cb8380df63726794f1dd86630af59f8e0ca9e45deda10297ad19bc9752138
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-04-15-f42c11
  comparison: ''
  date: '2026-04-15'
  description: 'Codex CLI — 0.121.0: 10 Safety and Privacy changes'
  evidence:
  - quote: 'Expanded MCP/plugin support with MCP Apps tool calls, namespaced MCP registration,
      parallel-call opt-in, and sandbox-state metadata for MCP servers (#17364, #17404,
      #17667, #17763).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: 'Added a secure devcontainer profile with bubblewrap support, plus macOS
      sandbox allowlists for Unix sockets (#10431, #17547, #17654).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17370 fix: unblock private DNS in macOS sandbox @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17294 Run exec-server fs operations through sandbox helper @starr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17365 Include legacy deny paths in elevated Windows sandbox setup @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17859 sandbox: remove dead seatbelt helper and update tests @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17763 Send sandbox state through MCP tool metadata @aaronl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17654 Support Unix socket allowlists in macOS sandbox @aaronl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17883 Remove exec-server fs sandbox request preflight @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17957 mcp: remove codex/sandbox-state custom request support @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 10-safety-and-privacy-changes-in-rust-v0-121-0
  source_release: codex-cli-2026-04-15-rust-v0-121-0-github-309557036-bb698f03
  source_type: github_releases
  theme: safety-privacy
  title: 10 Safety and Privacy changes in rust-v0.121.0
  type: change
related_changes:
- '[[Changes/Gemini CLI/2026-04-14-3-safety-and-privacy-changes-in-v0-38-0|3 Safety
  and Privacy changes in v0.38.0]]'
- '[[Changes/GitHub Copilot CLI/2026-04-14-permission-prompt-notification-hook-only-fires-when-a-prompt-is-actually-shown-t|Permission
  prompt notification hook only fires when a prompt is actually shown to the user]]'
- '[[Changes/Notion/2026-04-14-new-database-permission-can-create-pages|New database
  permission: “Can create pages”]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-04-15-rust-v0-121-0-github-309557036-bb698f03|codex-cli-2026-04-15-rust-v0-121-0-github-309557036-bb698f03]]'
source_type: github_releases
theme: safety-privacy
title: 10 Safety and Privacy changes in rust-v0.121.0
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Safety and Privacy changes in rust-v0.121.0

**Codex CLI** · 2026-04-15 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.121.0) · from [[Releases/Codex CLI/codex-cli-2026-04-15-rust-v0-121-0-github-309557036-bb698f03|0.121.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Expanded MCP/plugin support with MCP Apps tool calls, namespaced MCP registration, parallel-call opt-in, and sandbox-state metadata for MCP servers (#17364, #17404, #17667, #17763).

> Added a secure devcontainer profile with bubblewrap support, plus macOS sandbox allowlists for Unix sockets (#10431, #17547, #17654).

> #17370 fix: unblock private DNS in macOS sandbox @viyatb-oai

> #17294 Run exec-server fs operations through sandbox helper @starr-openai

> #17365 Include legacy deny paths in elevated Windows sandbox setup @iceweasel-oai

> #17859 sandbox: remove dead seatbelt helper and update tests @bolinfest

> #17763 Send sandbox state through MCP tool metadata @aaronl-openai

> #17654 Support Unix socket allowlists in macOS sandbox @aaronl-openai

> #17883 Remove exec-server fs sandbox request preflight @pakrym-oai

> #17957 mcp: remove codex/sandbox-state custom request support @bolinfest

Source: https://github.com/openai/codex/releases/tag/rust-v0.121.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-04-15-3-model-support-changes-in-rust-v0-121-0|3 Model Support changes in rust-v0.121.0]] · Model Support
- [[Changes/Codex CLI/2026-04-15-17684-adjust-default-tool-search-result-caps-malone-oai|♯17684 Adjust default tool search result caps @malone-oai]] · Search and Browsing
- [[Changes/Codex CLI/2026-04-15-9-memory-and-personalization-changes-in-rust-v0-121-0|9 Memory and Personalization changes in rust-v0.121.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-04-15-9-apps-and-integrations-changes-in-rust-v0-121-0|9 Apps and Integrations changes in rust-v0.121.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-04-15-4-context-window-changes-in-rust-v0-121-0|4 Context Window changes in rust-v0.121.0]] · Context Window
- [[Changes/Codex CLI/2026-04-15-7-agent-mode-changes-in-rust-v0-121-0|7 Agent Mode changes in rust-v0.121.0]] · Agent Mode
- [[Changes/Codex CLI/2026-04-15-4-developer-workflow-changes-in-rust-v0-121-0|4 Developer Workflow changes in rust-v0.121.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-04-15-17640-fix-stability-exec-server-jif-oai|♯17640 fix: stability exec server @jif-oai]] · Reliability and Performance
- [[Changes/Codex CLI/2026-04-15-added-realtime-and-app-server-apis-for-output-modality-transcript-completion-eve|Added realtime and app-server APIs for output modality, transcript completion…]] · Editor Experience
- [[Changes/Codex CLI/2026-04-15-17414-fix-thread-list-cwd-filtering-for-windows-verbatim-paths-etraut-openai|♯17414 Fix thread/list cwd filtering for Windows verbatim paths @etraut-openai]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-04-15-17717-codex-refactor-marketplace-add-into-shared-core-flow-xli-oai|♯17717 codex Refactor marketplace add into shared core flow @xli-oai]] · Collaboration
- [[Changes/Codex CLI/2026-04-15-99-other-changes-in-rust-v0-121-0|99 other changes in rust-v0.121.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-04-14 · Notion · [[Changes/Notion/2026-04-14-new-database-permission-can-create-pages|New database permission: “Can create pages”]]
- Later: 2026-04-16 · Claude Code · [[Changes/Claude Code/2026-04-16-added-less-permission-prompts-skill-scans-transcripts-for-common-read-only-bash|Added /less-permission-prompts skill]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-04-15-f42c11&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-04-15-10-safety-and-privacy-changes-in-rust-v0-121-0.md%0ACard%20ID%3A%20codex-cli-2026-04-15-f42c11%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.121.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->