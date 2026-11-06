---
card_id: codex-cli-2026-03-26-93f043
date: '2026-03-26'
description: 'Codex CLI · 2026-03-26 · Interface Experience: 3 changes in 0.117.0
  — The `/title` terminal-title picker now works in both the classic TUI and the app-server…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop
    generating: Based on your feedback, we''ve added the ability to stop generating…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1172
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 34e46db036471f57469fb895ecbf964f649519a2abd62b11eb02d08ffd5c82a6
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-03-26-93f043
  comparison: ''
  date: '2026-03-26'
  description: 'Codex CLI — 0.117.0: 3 Interface Experience changes'
  evidence:
  - quote: 'The `/title` terminal-title picker now works in both the classic TUI and
      the app-server TUI, making parallel sessions easier to tell apart. (#12334,
      #15860)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15778 feat: rendering library v1 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15825 Fix quoted command rendering in tui_app_server @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 3-interface-experience-changes-in-rust-v0-117-0
  source_release: codex-cli-2026-03-26-rust-v0-117-0-github-302123790-7cb322b6
  source_type: github_releases
  theme: interface-experience
  title: 3 Interface Experience changes in rust-v0.117.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-03-25-2-interface-experience-changes-in-v2-1-83|2 Interface
  Experience changes in v2.1.83]]'
- '[[Changes/ChatGPT/2026-03-26-to-give-you-more-space-to-view-your-most-critical-chats-and-projects-the-sidebar|A
  simplified sidebar on mobile]]'
- '[[Changes/Claude Code/2026-03-26-improved-mention-file-autocomplete-performance-on-large-repositories|Improved
  @-mention file autocomplete performance on large repositories]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-03-26-rust-v0-117-0-github-302123790-7cb322b6|codex-cli-2026-03-26-rust-v0-117-0-github-302123790-7cb322b6]]'
source_type: github_releases
theme: interface-experience
title: 3 Interface Experience changes in rust-v0.117.0
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Interface Experience changes in rust-v0.117.0

**Codex CLI** · 2026-03-26 · [[Themes/interface-experience|Interface Experience]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.117.0) · from [[Releases/Codex CLI/codex-cli-2026-03-26-rust-v0-117-0-github-302123790-7cb322b6|0.117.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> The `/title` terminal-title picker now works in both the classic TUI and the app-server TUI, making parallel sessions easier to tell apart. (#12334, #15860)

> #15778 feat: rendering library v1 @jif-oai

> #15825 Fix quoted command rendering in tui_app_server @etraut-openai

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
## Nearby in Interface Experience

- Earlier: 2026-03-26 · Claude Code · [[Changes/Claude Code/2026-03-26-improved-mention-file-autocomplete-performance-on-large-repositories|Improved @-mention file autocomplete performance on large repositories]]
- Later: 2026-03-26 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-03-26-3-interface-experience-changes-in-v1-0-12|3 Interface Experience changes in v1.0.12]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop generating: Based on your feedback, we've added the ability to stop generating…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-03-26-93f043&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-03-26-3-interface-experience-changes-in-rust-v0-117-0.md%0ACard%20ID%3A%20codex-cli-2026-03-26-93f043%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.117.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->