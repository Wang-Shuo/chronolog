---
card_id: codex-cli-2025-09-05-510f16
date: '2025-09-05'
description: 'Codex CLI · 2025-09-05 · Account and Access: 3 changes in 0.30.0 — **Security/behavior**:
  Never store requests; free port by canceling pending OAuth login.'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 890
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 58e218e9d85e0fea6b78a18fb8c7964327dd9ddf55b2aa52f9054ed3dde7da56
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2025-09-05-510f16
  comparison: ''
  date: '2025-09-05'
  description: 'Codex CLI — 0.30.0: 3 Account and Access changes'
  evidence:
  - quote: '**Security/behavior**: Never store requests; free port by canceling pending
      OAuth login.'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.30.0
  - quote: '[#3217] Added logic to cancel pending oauth login to free up localhost
      port'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.30.0
  - quote: '[#3117] Include originator in authentication URL parameters'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.30.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 3-account-and-access-changes-in-rust-v0-30-0
  source_release: codex-cli-2025-09-05-rust-v0-30-0-github-245199079-dedb4e90
  source_type: github_releases
  theme: account-access
  title: 3 Account and Access changes in rust-v0.30.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2025-08-29-2737-changed-oauth-success-screen-to-use-the-string-codex-rather-than-codex-cli|♯2737
  Changed OAuth success screen to use the string "Codex" rather than "Codex CLI"]]'
- '[[Changes/Dify/2025-09-03-2-account-and-access-changes-in-1-8-1|2 Account and Access
  changes in 1.8.1]]'
- '[[Changes/Gemini CLI/2025-09-04-feat-mcp-add-odic-fallback-to-oauth-metadata-look-up-by-xiaoheh-in-https-github|feat(mcp):
  Add ODIC fallback to OAuth metadata look up]]'
source_release: '[[Releases/Codex CLI/codex-cli-2025-09-05-rust-v0-30-0-github-245199079-dedb4e90|codex-cli-2025-09-05-rust-v0-30-0-github-245199079-dedb4e90]]'
source_type: github_releases
theme: account-access
title: 3 Account and Access changes in rust-v0.30.0
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Account and Access changes in rust-v0.30.0

**Codex CLI** · 2025-09-05 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.30.0) · from [[Releases/Codex CLI/codex-cli-2025-09-05-rust-v0-30-0-github-245199079-dedb4e90|0.30.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **Security/behavior**: Never store requests; free port by canceling pending OAuth login.

> [#3217] Added logic to cancel pending oauth login to free up localhost port

> [#3117] Include originator in authentication URL parameters

Source: https://github.com/openai/codex/releases/tag/rust-v0.30.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2025-09-05-2-model-support-changes-in-rust-v0-30-0|2 Model Support changes in rust-v0.30.0]] · Model Support
- [[Changes/Codex CLI/2025-09-05-3-developer-workflow-changes-in-rust-v0-30-0|3 Developer Workflow changes in rust-v0.30.0]] · Developer Workflow
- [[Changes/Codex CLI/2025-09-05-3135-tui-add-session-resume-picker-resume-and-quick-resume-continue|♯3135 TUI: Add session resume picker (--resume) and quick resume (--continue)]] · Interface Experience
- [[Changes/Codex CLI/2025-09-05-2-context-window-changes-in-rust-v0-30-0|2 Context Window changes in rust-v0.30.0]] · Context Window
- [[Changes/Codex CLI/2025-09-05-3128-mcp-sandbox-call|♯3128 MCP sandbox call]] · Safety and Privacy
- [[Changes/Codex CLI/2025-09-05-3118-codex-document-use-experimental-reasoning-summary-toml-key-config|♯3118 codex document use_experimental_reasoning_summary toml key config]] · Files and Data
- [[Changes/Codex CLI/2025-09-05-3-agent-mode-changes-in-rust-v0-30-0|3 Agent Mode changes in rust-v0.30.0]] · Agent Mode
- [[Changes/Codex CLI/2025-09-05-4-apps-and-integrations-changes-in-rust-v0-30-0|4 Apps and Integrations changes in rust-v0.30.0]] · Apps and Integrations
- [[Changes/Codex CLI/2025-09-05-24-other-changes-in-rust-v0-30-0|24 other changes in rust-v0.30.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2025-09-04 · Gemini CLI · [[Changes/Gemini CLI/2025-09-04-feat-mcp-add-odic-fallback-to-oauth-metadata-look-up-by-xiaoheh-in-https-github|feat(mcp): Add ODIC fallback to OAuth metadata look up]]
- Later: 2025-09-08 · Codex CLI · [[Changes/Codex CLI/2025-09-08-3217-added-logic-to-cancel-pending-oauth-login-to-free-up-localhost-port|♯3217 Added logic to cancel pending oauth login to free up localhost port]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2025-09-05-510f16&body=Card%3A%20Changes%2FCodex%20CLI%2F2025-09-05-3-account-and-access-changes-in-rust-v0-30-0.md%0ACard%20ID%3A%20codex-cli-2025-09-05-510f16%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.30.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->