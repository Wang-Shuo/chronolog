---
card_id: codex-cli-2026-04-10-187a75
date: '2026-04-10'
description: 'Codex CLI · 2026-04-10 · Safety and Privacy: 8 changes in 0.119.0 —
  Remote/app-server workflows now support egress websocket transport, remote `--cd`…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2082
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: c75e848dacbd5cf128c3d8eb1e2fcd6039aa5994352ee6d4460b2106212c9476
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-04-10-187a75
  comparison: ''
  date: '2026-04-10'
  description: 'Codex CLI — 0.119.0: 8 Safety and Privacy changes'
  evidence:
  - quote: 'Remote/app-server workflows now support egress websocket transport, remote
      `--cd` forwarding, runtime remote-control enablement, sandbox-aware filesystem
      APIs, and an experimental `codex exec-server` subcommand (#15951, #16700, #16973,
      #16751, #17059, #17142, #17162).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: 'Sandbox, network, and platform edge cases were tightened, including clearer
      read-only `apply_patch` errors, refreshed network proxy policy after sandbox
      changes, suppressed irrelevant bubblewrap warnings, a macOS HTTP-client sandbox
      panic fix, and Windows firewall address handling (#16885, #17040, #16667, #16670,
      #17053).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16422 fix(core) rm execute_exec_request sandbox_policy @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16284 Fix TUI app-server permission profile conversions @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16670 Fix macOS sandbox panic in Codex HTTP client @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17040 fix: refresh network proxy settings when sandbox mode changes @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16751 Add sandbox support to filesystem APIs @starr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17168 refactor(proxy): clarify sandbox block messages @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 8-safety-and-privacy-changes-in-rust-v0-119-0
  source_release: codex-cli-2026-04-10-rust-v0-119-0-github-307754801-19f169d1
  source_type: github_releases
  theme: safety-privacy
  title: 8 Safety and Privacy changes in rust-v0.119.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-04-09-permission-checks-and-other-hooks-now-work-correctly-when-using-anthropic-models|Permission
  checks and other hooks now work correctly when using Anthropic models…]]'
- '[[Changes/OpenCode/2026-04-09-core-add-permission-prompts-for-gitlab-duo-workflow-tool-calls-instead-of-auto-r|Core
  Add permission prompts for GitLab Duo Workflow tool calls instead…]]'
- '[[Changes/Claude Code/2026-04-10-fixed-a-command-injection-vulnerability-in-the-posix-which-fallback-used-by-lsp|Fixed
  a command injection vulnerability in the POSIX which fallback used by LSP…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-04-10-rust-v0-119-0-github-307754801-19f169d1|codex-cli-2026-04-10-rust-v0-119-0-github-307754801-19f169d1]]'
source_type: github_releases
theme: safety-privacy
title: 8 Safety and Privacy changes in rust-v0.119.0
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Safety and Privacy changes in rust-v0.119.0

**Codex CLI** · 2026-04-10 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.119.0) · from [[Releases/Codex CLI/codex-cli-2026-04-10-rust-v0-119-0-github-307754801-19f169d1|0.119.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Remote/app-server workflows now support egress websocket transport, remote `--cd` forwarding, runtime remote-control enablement, sandbox-aware filesystem APIs, and an experimental `codex exec-server` subcommand (#15951, #16700, #16973, #16751, #17059, #17142, #17162).

> Sandbox, network, and platform edge cases were tightened, including clearer read-only `apply_patch` errors, refreshed network proxy policy after sandbox changes, suppressed irrelevant bubblewrap warnings, a macOS HTTP-client sandbox panic fix, and Windows firewall address handling (#16885, #17040, #16667, #16670, #17053).

> #16422 fix(core) rm execute_exec_request sandbox_policy @dylan-hurd-oai

> #16284 Fix TUI app-server permission profile conversions @etraut-openai

> #16670 Fix macOS sandbox panic in Codex HTTP client @etraut-openai

> #17040 fix: refresh network proxy settings when sandbox mode changes @viyatb-oai

> #16751 Add sandbox support to filesystem APIs @starr-openai

> #17168 refactor(proxy): clarify sandbox block messages @viyatb-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.119.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-04-10-4-context-window-changes-in-rust-v0-119-0|4 Context Window changes in rust-v0.119.0]] · Context Window
- [[Changes/Codex CLI/2026-04-10-28-developer-workflow-changes-in-rust-v0-119-0|28 Developer Workflow changes in rust-v0.119.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-04-10-13-agent-mode-changes-in-rust-v0-119-0|13 Agent Mode changes in rust-v0.119.0]] · Agent Mode
- [[Changes/Codex CLI/2026-04-10-2-memory-and-personalization-changes-in-rust-v0-119-0|2 Memory and Personalization changes in rust-v0.119.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-04-10-the-readme-now-uses-the-current-chatgpt-business-plan-name-16348|The README now uses the current ChatGPT Business plan name (♯16348)]] · Enterprise and Administration
- [[Changes/Codex CLI/2026-04-10-3-voice-and-audio-changes-in-rust-v0-119-0|3 Voice and Audio changes in rust-v0.119.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-04-10-19-apps-and-integrations-changes-in-rust-v0-119-0|19 Apps and Integrations changes in rust-v0.119.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-04-10-2-account-and-access-changes-in-rust-v0-119-0|2 Account and Access changes in rust-v0.119.0]] · Account and Access
- [[Changes/Codex CLI/2026-04-10-17256-app-server-use-shared-receivers-for-app-server-message-processors-euroeles|♯17256 app-server: Use shared receivers for app-server message processors @euroelessar]] · Collaboration
- [[Changes/Codex CLI/2026-04-10-10-interface-experience-changes-in-rust-v0-119-0|10 Interface Experience changes in rust-v0.119.0]] · Interface Experience
- [[Changes/Codex CLI/2026-04-10-16202-fix-paste-driven-bottom-pane-completion-teardown-etraut-openai|♯16202 Fix paste-driven bottom pane completion teardown @etraut-openai]] · Editor Experience
- [[Changes/Codex CLI/2026-04-10-2-reliability-and-performance-changes-in-rust-v0-119-0|2 Reliability and Performance changes in rust-v0.119.0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-04-10-5-model-support-changes-in-rust-v0-119-0|5 Model Support changes in rust-v0.119.0]] · Model Support
- [[Changes/Codex CLI/2026-04-10-6-mobile-and-desktop-changes-in-rust-v0-119-0|6 Mobile and Desktop changes in rust-v0.119.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-04-10-187-other-changes-in-rust-v0-119-0|187 other changes in rust-v0.119.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-04-10 · Claude Code · [[Changes/Claude Code/2026-04-10-fixed-a-command-injection-vulnerability-in-the-posix-which-fallback-used-by-lsp|Fixed a command injection vulnerability in the POSIX which fallback used by LSP…]]
- Later: 2026-04-11 · Codex CLI · [[Changes/Codex CLI/2026-04-11-4-safety-and-privacy-changes-in-rust-v0-120-0|4 Safety and Privacy changes in rust-v0.120.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-04-10-187a75&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-04-10-8-safety-and-privacy-changes-in-rust-v0-119-0.md%0ACard%20ID%3A%20codex-cli-2026-04-10-187a75%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.119.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->