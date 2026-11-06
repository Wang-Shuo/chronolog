---
card_id: codex-cli-2026-03-26-02066c
date: '2026-03-26'
description: 'Codex CLI · 2026-03-26 · Developer Workflow: 19 changes in 0.117.0 —
  App-server clients can now send `!` shell commands, watch filesystem changes, and
  connect…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1104
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 225d61585ce894d26cacc1373e9d0179c0616789fe610e7682eb1acadceef721
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-03-26-02066c
  comparison: ''
  date: '2026-03-26'
  description: 'Codex CLI — 0.117.0: 19 Developer Workflow changes'
  evidence:
  - quote: 'App-server clients can now send `!` shell commands, watch filesystem changes,
      and connect to remote websocket servers with bearer-token auth. (#14988, #14533,
      #14847, #14853)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: 'Early exits now restore terminal state reliably, avoiding broken shell
      state after quitting; tmux users also get a working queued-message edit shortcut
      on `Shift+Left`. (#15671, #15480)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#12334 feat(tui): add /title terminal title configuration @yvolovich-cyber'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15216 Move terminal module to terminal-detection crate @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15036 fix(core) disable command_might_be_dangerous when unsandboxed @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15658 try to fix git glitch @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15657 try to fix git glitch @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15656 try to fix git glitch @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15655 try to fix git glitch @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15654 try to fix git glitch @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15653 try to fix git glitch @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15652 try to fix git glitch @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15651 try to fix git glitch @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15650 try to fix git glitch @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15547 app-server: Add back pressure and batching to `command/exec` @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15564 Move git utilities into a dedicated crate @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15671 tui: always restore the terminal on early exit @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15796 [codex] Block unsafe git global options from safe allowlist @adrian-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15860 feat(tui): add terminal title support to tui app server @fcoury'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 19-developer-workflow-changes-in-rust-v0-117-0
  source_release: codex-cli-2026-03-26-rust-v0-117-0-github-302123790-7cb322b6
  source_type: github_releases
  theme: developer-workflow
  title: 19 Developer Workflow changes in rust-v0.117.0
  type: change
related_changes:
- '[[Changes/Gemini CLI/2026-03-24-feat-skills-improve-async-pr-review-workflow-and-logging-by-mattkorwel-in-https|feat(skills):
  improve async-pr-review workflow and logging]]'
- '[[Changes/Claude Code/2026-03-26-5-developer-workflow-changes-in-v2-1-84|5 Developer
  Workflow changes in v2.1.84]]'
- '[[Changes/Claude Code/2026-03-26-improved-powershell-dangerous-command-detection|Improved
  PowerShell dangerous command detection]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-03-26-rust-v0-117-0-github-302123790-7cb322b6|codex-cli-2026-03-26-rust-v0-117-0-github-302123790-7cb322b6]]'
source_type: github_releases
theme: developer-workflow
title: 19 Developer Workflow changes in rust-v0.117.0
type: change
---

<!-- chronolog:begin region="header" -->
# 19 Developer Workflow changes in rust-v0.117.0

**Codex CLI** · 2026-03-26 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.117.0) · from [[Releases/Codex CLI/codex-cli-2026-03-26-rust-v0-117-0-github-302123790-7cb322b6|0.117.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> App-server clients can now send `!` shell commands, watch filesystem changes, and connect to remote websocket servers with bearer-token auth. (#14988, #14533, #14847, #14853)

> Early exits now restore terminal state reliably, avoiding broken shell state after quitting; tmux users also get a working queued-message edit shortcut on `Shift+Left`. (#15671, #15480)

> #12334 feat(tui): add /title terminal title configuration @yvolovich-cyber

> #15216 Move terminal module to terminal-detection crate @aibrahim-oai

> #15036 fix(core) disable command_might_be_dangerous when unsandboxed @dylan-hurd-oai

> #15658 try to fix git glitch @jif-oai

> #15657 try to fix git glitch @jif-oai

> #15656 try to fix git glitch @jif-oai

> #15655 try to fix git glitch @jif-oai

> #15654 try to fix git glitch @jif-oai

> #15653 try to fix git glitch @jif-oai

> #15652 try to fix git glitch @jif-oai

> #15651 try to fix git glitch @jif-oai

> #15650 try to fix git glitch @jif-oai

> #15547 app-server: Add back pressure and batching to `command/exec` @euroelessar

> #15564 Move git utilities into a dedicated crate @aibrahim-oai

> #15671 tui: always restore the terminal on early exit @etraut-openai

> #15796 [codex] Block unsafe git global options from safe allowlist @adrian-openai

> #15860 feat(tui): add terminal title support to tui app server @fcoury

Source: https://github.com/openai/codex/releases/tag/rust-v0.117.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

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
- [[Changes/Codex CLI/2026-03-26-57-apps-and-integrations-changes-in-rust-v0-117-0|57 Apps and Integrations changes in rust-v0.117.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-03-26-3-mobile-and-desktop-changes-in-rust-v0-117-0|3 Mobile and Desktop changes in rust-v0.117.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-03-26-5-safety-and-privacy-changes-in-rust-v0-117-0|5 Safety and Privacy changes in rust-v0.117.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-03-26-3-model-support-changes-in-rust-v0-117-0|3 Model Support changes in rust-v0.117.0]] · Model Support
- [[Changes/Codex CLI/2026-03-26-15175-chore-morpheus-does-not-generate-memories-jif-oai|♯15175 chore: morpheus does not generate memories @jif-oai]] · Memory and Personalization
- [[Changes/Codex CLI/2026-03-26-117-other-changes-in-rust-v0-117-0|117 other changes in rust-v0.117.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-03-26 · Claude Code · [[Changes/Claude Code/2026-03-26-improved-powershell-dangerous-command-detection|Improved PowerShell dangerous command detection]]
- Later: 2026-03-26 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-03-26-2-developer-workflow-changes-in-v1-0-12|2 Developer Workflow changes in v1.0.12]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-03-26-02066c&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-03-26-19-developer-workflow-changes-in-rust-v0-117-0.md%0ACard%20ID%3A%20codex-cli-2026-03-26-02066c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.117.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->