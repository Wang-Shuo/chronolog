---
card_id: codex-cli-2026-10-08-56613a
date: '2026-10-08'
description: 'Codex CLI · 2026-10-08 · Safety and Privacy: 13 changes in 0.162.0 —
  Restore ordinary drive-letter file access on Windows 10 and match Windows sandbox
  temp…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2263
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 1987e96da30aae6ba9e49855b71cf15d5f500bb64a5432f41ed0aa69afcab98f
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-10-08-56613a
  comparison: ''
  date: '2026-10-08'
  description: 'Codex CLI — 0.162.0: 13 Safety and Privacy changes'
  evidence:
  - quote: 'Restore ordinary drive-letter file access on Windows 10 and match Windows
      sandbox temp permissions to the child process environment. (#51511, #51512)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50059 Fix Linux sandbox startup with multiple denied files @yuzhu-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50140 Use the server permission catalog for TUI permission shortcuts
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50339 Add end-to-end coverage for MCP sandbox state enforcement @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50437 Add a CLI command to uninstall the legacy Windows sandbox @chess-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50480 Skip managed config loading for registered Windows sandbox refreshes
      @zm-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50507 Record Windows sandbox service stop diagnostics @zm-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51211 Reject sandbox-writable bubblewrap executables from PATH @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51256 Start the Windows sandbox service during registered Core setup
      @zm-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51407 Protect ripgrep lookup during Linux sandbox construction @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51459 Preserve wrapped help links in Windows sandbox prompts @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51512 Align Windows sandbox temp permissions with the child environment
      @zm-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51527 Ignore ripgrep configuration when expanding sandbox deny globs
      @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 13-safety-and-privacy-changes-in-rust-v0-162-0
  source_release: codex-cli-2026-10-08-rust-v0-162-0-github-407151970-b80d60db
  source_type: github_releases
  theme: safety-privacy
  title: 13 Safety and Privacy changes in rust-v0.162.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-10-07-2-safety-and-privacy-changes-in-v1-0-93|2
  Safety and Privacy changes in v1.0.93]]'
- '[[Changes/Google Antigravity/2026-10-07-on-macos-if-privacy-settings-block-antigravity-from-reading-a-file-or-folder-you|On
  macOS, if privacy settings block Antigravity from reading a file or folder you…]]'
- '[[Changes/Claude Code/2026-10-08-5-safety-and-privacy-changes-in-v2-1-295|5 Safety
  and Privacy changes in v2.1.295]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-10-08-rust-v0-162-0-github-407151970-b80d60db|codex-cli-2026-10-08-rust-v0-162-0-github-407151970-b80d60db]]'
source_type: github_releases
theme: safety-privacy
title: 13 Safety and Privacy changes in rust-v0.162.0
type: change
---

<!-- chronolog:begin region="header" -->
# 13 Safety and Privacy changes in rust-v0.162.0

**Codex CLI** · 2026-10-08 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.162.0) · from [[Releases/Codex CLI/codex-cli-2026-10-08-rust-v0-162-0-github-407151970-b80d60db|0.162.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Restore ordinary drive-letter file access on Windows 10 and match Windows sandbox temp permissions to the child process environment. (#51511, #51512)

> #50059 Fix Linux sandbox startup with multiple denied files @yuzhu-oai

> #50140 Use the server permission catalog for TUI permission shortcuts @etraut-openai

> #50339 Add end-to-end coverage for MCP sandbox state enforcement @bolinfest

> #50437 Add a CLI command to uninstall the legacy Windows sandbox @chess-oai

> #50480 Skip managed config loading for registered Windows sandbox refreshes @zm-oai

> #50507 Record Windows sandbox service stop diagnostics @zm-oai

> #51211 Reject sandbox-writable bubblewrap executables from PATH @viyatb-oai

> #51256 Start the Windows sandbox service during registered Core setup @zm-oai

> #51407 Protect ripgrep lookup during Linux sandbox construction @viyatb-oai

> #51459 Preserve wrapped help links in Windows sandbox prompts @charliemarsh-oai

> #51512 Align Windows sandbox temp permissions with the child environment @zm-oai

> #51527 Ignore ripgrep configuration when expanding sandbox deny globs @viyatb-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.162.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-10-08-51223-remove-legacy-personality-template-metadata-rhan-oai|♯51223 Remove legacy personality template metadata @rhan-oai]] · Memory and Personalization
- [[Changes/Codex CLI/2026-10-08-3-reliability-and-performance-changes-in-rust-v0-162-0|3 Reliability and Performance changes in rust-v0.162.0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-10-08-2-voice-and-audio-changes-in-rust-v0-162-0|2 Voice and Audio changes in rust-v0.162.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-10-08-10-context-window-changes-in-rust-v0-162-0|10 Context Window changes in rust-v0.162.0]] · Context Window
- [[Changes/Codex CLI/2026-10-08-50216-use-the-shared-text-editor-for-command-center-task-renaming-bc-openai|♯50216 Use the shared text editor for command-center task renaming @bc-openai]] · Editor Experience
- [[Changes/Codex CLI/2026-10-08-20-apps-and-integrations-changes-in-rust-v0-162-0|20 Apps and Integrations changes in rust-v0.162.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-10-08-50384-allow-opting-into-16-kib-arm64-code-pages-for-macos-signing-chess-oai|♯50384 Allow opting into 16 KiB ARM64 code pages for macOS signing @chess-oai]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-10-08-8-interface-experience-changes-in-rust-v0-162-0|8 Interface Experience changes in rust-v0.162.0]] · Interface Experience
- [[Changes/Codex CLI/2026-10-08-12-developer-workflow-changes-in-rust-v0-162-0|12 Developer Workflow changes in rust-v0.162.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-10-08-14-agent-mode-changes-in-rust-v0-162-0|14 Agent Mode changes in rust-v0.162.0]] · Agent Mode
- [[Changes/Codex CLI/2026-10-08-11-model-support-changes-in-rust-v0-162-0|11 Model Support changes in rust-v0.162.0]] · Model Support
- [[Changes/Codex CLI/2026-10-08-2-account-and-access-changes-in-rust-v0-162-0|2 Account and Access changes in rust-v0.162.0]] · Account and Access
- [[Changes/Codex CLI/2026-10-08-2-collaboration-changes-in-rust-v0-162-0|2 Collaboration changes in rust-v0.162.0]] · Collaboration
- [[Changes/Codex CLI/2026-10-08-137-other-changes-in-rust-v0-162-0|137 other changes in rust-v0.162.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-10-08 · Claude Code · [[Changes/Claude Code/2026-10-08-5-safety-and-privacy-changes-in-v2-1-295|5 Safety and Privacy changes in v2.1.295]]
- Later: 2026-10-08 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-10-08-2-safety-and-privacy-changes-in-v1-0-94|2 Safety and Privacy changes in v1.0.94]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-10-08-56613a&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-10-08-13-safety-and-privacy-changes-in-rust-v0-162-0.md%0ACard%20ID%3A%20codex-cli-2026-10-08-56613a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.162.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->