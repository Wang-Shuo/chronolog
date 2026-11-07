---
card_id: codex-cli-2026-03-26-374b30
date: '2026-03-26'
description: 'Codex CLI · 2026-03-26 · Search and Browsing: Plugins are now a first-class
  workflow: Codex can sync product-scoped plugins at startup, browse them in…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-05-28-added-ability-to-batch-delete-ignore-search-results|Added
    ability to batch delete/ignore search results]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2128
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: search-browsing
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: 4615d66afdd5e8162c5494a5690c09e465c4c6c6e2064b0bea47bc8f6c576e39
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-03-26-374b30
  comparison: ''
  date: '2026-03-26'
  description: 'Codex CLI — 0.117.0: Plugins are now a first-class workflow: Codex
    can sync product-scoped plugins at startup, browse them in `/plugins`, and install
    or remove them with clearer auth/setup handling. (#15041, #15042, #15195, #15215,
    #15217, #15264, #15275, #15342, #15580, #15606, #15802)'
  evidence:
  - quote: 'Plugins are now a first-class workflow: Codex can sync product-scoped
      plugins at startup, browse them in `/plugins`, and install or remove them with
      clearer auth/setup handling. (#15041, #15042, #15195, #15215, #15217, #15264,
      #15275, #15342, #15580, #15606, #15802)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: codex-cli
  product_name: Codex CLI
  slug: plugins-are-now-a-first-class-workflow-codex-can-sync-product-scoped-plugins-at
  source_release: codex-cli-2026-03-26-rust-v0-117-0-github-302123790-7cb322b6
  source_type: github_releases
  theme: search-browsing
  theme_matches:
  - matched_terms:
    - plugins
    score: 50
    theme: apps-integrations
  - matched_terms:
    - browse
    score: 50
    theme: search-browsing
  theme_resolution: manual-semantic-rule-v1
  title: Plugins are now a first-class workflow
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-03-23-now-it-s-easier-to-find-reuse-and-build-on-your-files-over-time-when-you-upload|File
  Library in ChatGPT]]'
- '[[Changes/ChatGPT/2026-03-24-we-ve-improved-shopping-in-chatgpt-to-make-it-easier-to-discover-compare-and-dec|Shopping
  updates in ChatGPT]]'
- '[[Changes/Open WebUI/2026-03-25-2-search-and-browsing-changes-in-v0-8-11|2 Search
  and Browsing changes in v0.8.11]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-03-26-rust-v0-117-0-github-302123790-7cb322b6|codex-cli-2026-03-26-rust-v0-117-0-github-302123790-7cb322b6]]'
source_type: github_releases
theme: search-browsing
title: Plugins are now a first-class workflow
type: change
---

<!-- chronolog:begin region="header" -->
# Plugins are now a first-class workflow

**Codex CLI** · 2026-03-26 · [[Themes/search-browsing|Search and Browsing]] · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.117.0) · from [[Releases/Codex CLI/codex-cli-2026-03-26-rust-v0-117-0-github-302123790-7cb322b6|0.117.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Plugins are now a first-class workflow: Codex can sync product-scoped plugins at startup, browse them in `/plugins`, and install or remove them with clearer auth/setup handling. (#15041, #15042, #15195, #15215, #15217, #15264, #15275, #15342, #15580, #15606, #15802)
>
> Source: https://github.com/openai/codex/releases/tag/rust-v0.117.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-03-26-19-developer-workflow-changes-in-rust-v0-117-0|19 Developer Workflow changes in rust-v0.117.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-03-26-15789-treat-chatgpt-hc-plan-as-enterprise-arnavdugar-openai|♯15789 Treat ChatGPT hc plan as Enterprise @arnavdugar-openai]] · Enterprise and Administration
- [[Changes/Codex CLI/2026-03-26-the-app-server-backed-tui-is-now-enabled-by-default-and-the-plugin-app-rollout-f|The app-server-backed TUI is now enabled by default, and the plugin/app rollout…]] · Apps and Integrations
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
## Nearby in Search and Browsing

- Earlier: 2026-03-25 · Open WebUI · [[Changes/Open WebUI/2026-03-25-2-search-and-browsing-changes-in-v0-8-11|2 Search and Browsing changes in v0.8.11]]
- Later: 2026-03-27 · Notion · [[Changes/Notion/2026-03-27-archive-lets-you-mark-pages-as-outdated-to-keep-your-workspace-clean-and-improve|Archive lets you mark pages as outdated to keep your workspace clean and improve…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-05-28 · Descript · [[Changes/Descript/2020-05-28-added-ability-to-batch-delete-ignore-search-results|Added ability to batch delete/ignore search results]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-03-26-374b30&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-03-26-plugins-are-now-a-first-class-workflow-codex-can-sync-product-scoped-plugins-at.md%0ACard%20ID%3A%20codex-cli-2026-03-26-374b30%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.117.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->