---
card_id: codex-cli-2025-09-05-8e0123
date: '2025-09-05'
description: 'Codex CLI · 2025-09-05 · Other changes: 24 changes in 0.30.0 — **Breaking**:
  Stop loading project `.env` files automatically.'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: fda6163dddf348aea3f0d53bed7155820f95465ce364c2cc0910e3ce768ff5ca
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2025-09-05-8e0123
  comparison: ''
  date: '2025-09-05'
  description: 'Codex CLI — 0.30.0: 24 other changes'
  evidence:
  - quote: '**Breaking**: Stop loading project `.env` files automatically.'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.30.0
  - quote: '**Deps**: Bump `uuid` and `wiremock`.'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.30.0
  - quote: '**Windows**: no more asking for approvals on Full Access mode'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.30.0
  - quote: '[#3218] hide resume until it''s complete'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.30.0
  - quote: '[#3212] Never store requests'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.30.0
  - quote: '[#3193] chore: improve serialization of ServerNotification'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.30.0
  - quote: '[#3191] refactor: remove AttachImage tui event'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.30.0
  - quote: '[#3187] ZSH on UNIX system and better detection'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.30.0
  - quote: '[#3184] [BREAKING] Stop loading project .env files'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.30.0
  - quote: '[#3167] tui: pager pins scroll to bottom'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.30.0
  - quote: '[#3143] Use ⌥⇧⌃ glyphs for key hints on mac'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.30.0
  - quote: '[#3133] tui: avoid panic when active exec cell area is zero height'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.30.0
  - quote: '[#3131] Pause status timer while modals are open'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.30.0
  - quote: '[#3127] Dividing UserMsgs into categories to send it back to the tui'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.30.0
  - quote: '[#3123] Replay EventMsgs from Response Items when resuming a session with
      history.'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.30.0
  - quote: '[#3121] remove bold the keyword from prompt'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.30.0
  - quote: '[#3116] Introduce Rollout Policy'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.30.0
  - quote: '[#3112] Update guidance on API key permissions'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.30.0
  - quote: '[#3110] Add a common way to create HTTP client'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.30.0
  - quote: '[#3056] chore: Clean up verbosity config'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.30.0
  - quote: '[#2988] Auto-approve DangerFullAccess patches on non-sandboxed platforms'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.30.0
  - quote: '[#2981] Improve @ file search: include specific hidden dirs such as .github,
      .gitlab'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.30.0
  - quote: '[#2666] chore(deps): bump wiremock from 0.6.4 to 0.6.5 in /codex-rs'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.30.0
  - quote: '[#2493] chore(deps): bump uuid from 1.17.0 to 1.18.0 in /codex-rs'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.30.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 24-other-changes-in-rust-v0-30-0
  source_release: codex-cli-2025-09-05-rust-v0-30-0-github-245199079-dedb4e90
  source_type: github_releases
  theme: uncategorized
  title: 24 other changes in rust-v0.30.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2025-09-05-rust-v0-30-0-github-245199079-dedb4e90|codex-cli-2025-09-05-rust-v0-30-0-github-245199079-dedb4e90]]'
source_type: github_releases
theme: uncategorized
title: 24 other changes in rust-v0.30.0
type: change
---

<!-- chronolog:begin region="header" -->
# 24 other changes in rust-v0.30.0

**Codex CLI** · 2025-09-05 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.30.0) · from [[Releases/Codex CLI/codex-cli-2025-09-05-rust-v0-30-0-github-245199079-dedb4e90|0.30.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **Breaking**: Stop loading project `.env` files automatically.

> **Deps**: Bump `uuid` and `wiremock`.

> **Windows**: no more asking for approvals on Full Access mode

> [#3218] hide resume until it's complete

> [#3212] Never store requests

> [#3193] chore: improve serialization of ServerNotification

> [#3191] refactor: remove AttachImage tui event

> [#3187] ZSH on UNIX system and better detection

> [#3184] [BREAKING] Stop loading project .env files

> [#3167] tui: pager pins scroll to bottom

> [#3143] Use ⌥⇧⌃ glyphs for key hints on mac

> [#3133] tui: avoid panic when active exec cell area is zero height

> [#3131] Pause status timer while modals are open

> [#3127] Dividing UserMsgs into categories to send it back to the tui

> [#3123] Replay EventMsgs from Response Items when resuming a session with history.

> [#3121] remove bold the keyword from prompt

> [#3116] Introduce Rollout Policy

> [#3112] Update guidance on API key permissions

> [#3110] Add a common way to create HTTP client

> [#3056] chore: Clean up verbosity config

> [#2988] Auto-approve DangerFullAccess patches on non-sandboxed platforms

> [#2981] Improve @ file search: include specific hidden dirs such as .github, .gitlab

> [#2666] chore(deps): bump wiremock from 0.6.4 to 0.6.5 in /codex-rs

> [#2493] chore(deps): bump uuid from 1.17.0 to 1.18.0 in /codex-rs

Source: https://github.com/openai/codex/releases/tag/rust-v0.30.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2025-09-05-2-model-support-changes-in-rust-v0-30-0|2 Model Support changes in rust-v0.30.0]] · Model Support
- [[Changes/Codex CLI/2025-09-05-3-developer-workflow-changes-in-rust-v0-30-0|3 Developer Workflow changes in rust-v0.30.0]] · Developer Workflow
- [[Changes/Codex CLI/2025-09-05-3135-tui-add-session-resume-picker-resume-and-quick-resume-continue|♯3135 TUI: Add session resume picker (--resume) and quick resume (--continue)]] · Interface Experience
- [[Changes/Codex CLI/2025-09-05-2-context-window-changes-in-rust-v0-30-0|2 Context Window changes in rust-v0.30.0]] · Context Window
- [[Changes/Codex CLI/2025-09-05-3-account-and-access-changes-in-rust-v0-30-0|3 Account and Access changes in rust-v0.30.0]] · Account and Access
- [[Changes/Codex CLI/2025-09-05-3128-mcp-sandbox-call|♯3128 MCP sandbox call]] · Safety and Privacy
- [[Changes/Codex CLI/2025-09-05-3118-codex-document-use-experimental-reasoning-summary-toml-key-config|♯3118 codex document use_experimental_reasoning_summary toml key config]] · Files and Data
- [[Changes/Codex CLI/2025-09-05-3-agent-mode-changes-in-rust-v0-30-0|3 Agent Mode changes in rust-v0.30.0]] · Agent Mode
- [[Changes/Codex CLI/2025-09-05-4-apps-and-integrations-changes-in-rust-v0-30-0|4 Apps and Integrations changes in rust-v0.30.0]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2025-09-05-8e0123&body=Card%3A%20Changes%2FCodex%20CLI%2F2025-09-05-24-other-changes-in-rust-v0-30-0.md%0ACard%20ID%3A%20codex-cli-2025-09-05-8e0123%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.30.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->