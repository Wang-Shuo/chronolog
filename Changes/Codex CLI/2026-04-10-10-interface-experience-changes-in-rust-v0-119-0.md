---
card_id: codex-cli-2026-04-10-c3563d
date: '2026-04-10'
description: 'Codex CLI · 2026-04-10 · Interface Experience: 10 changes in 0.119.0
  — Resume flows are more stable: the picker no longer flashes false empty states,
  uses…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-04-14-descript-s-sidebar-now-has-an-economical-collapsed-state|Collapsed
    Sidebar]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2553
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ebc89ba6f9401445d3c0f5a6594edd9a6ac4fedfb687b28335e5df85b42d775c
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-04-10-c3563d
  comparison: ''
  date: '2026-04-10'
  description: 'Codex CLI — 0.119.0: 10 Interface Experience changes'
  evidence:
  - quote: 'Resume flows are more stable: the picker no longer flashes false empty
      states, uses fresher thread names, stabilizes timestamp labels, preserves resume
      hints on zero-token exits, and avoids crashing when resuming the current thread
      (#16591, #16601, #16822, #16987, #17086).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: 'Composer and chat behavior are smoother, including fixed paste teardown,
      CJK word navigation, stale `/copy` output, percent-decoded local file links,
      and clearer truncated exec-output hints (#16202, #16829, #16648, #16810, #17076).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16591 Fix resume picker initial loading state @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16601 Fix resume picker stale thread names @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16578 fix(tui): handle zellij redraw and composer rendering @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16829 Fix CJK word navigation in the TUI composer @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16822 Fix resume picker timestamp labels and stability @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16698 Remove expired April 2nd tooltip copy @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17138 fix(debug-config, guardian): fix /debug-config rendering and guardian…
      @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16966 feat(tui): Ctrl+O copy hotkey and harden copy-as-markdown behavior
      @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 10-interface-experience-changes-in-rust-v0-119-0
  source_release: codex-cli-2026-04-10-rust-v0-119-0-github-307754801-19f169d1
  source_type: github_releases
  theme: interface-experience
  title: 10 Interface Experience changes in rust-v0.119.0
  type: change
related_changes:
- '[[Changes/OpenCode/2026-04-08-terminal-added-a-keybinding-option-for-switch-model-variant|Terminal
  Added a keybinding option for "Switch model variant"]]'
- '[[Changes/GitHub Copilot CLI/2026-04-09-slash-command-picker-appears-above-the-text-input-for-a-more-stable-layout|Slash
  command picker appears above the text input for a more stable layout]]'
- '[[Changes/Claude Code/2026-04-10-improved-focus-mode-claude-now-writes-more-self-contained-summaries-since-it-kno|Improved
  focus mode]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-04-10-rust-v0-119-0-github-307754801-19f169d1|codex-cli-2026-04-10-rust-v0-119-0-github-307754801-19f169d1]]'
source_type: github_releases
theme: interface-experience
title: 10 Interface Experience changes in rust-v0.119.0
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Interface Experience changes in rust-v0.119.0

**Codex CLI** · 2026-04-10 · [[Themes/interface-experience|Interface Experience]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.119.0) · from [[Releases/Codex CLI/codex-cli-2026-04-10-rust-v0-119-0-github-307754801-19f169d1|0.119.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Resume flows are more stable: the picker no longer flashes false empty states, uses fresher thread names, stabilizes timestamp labels, preserves resume hints on zero-token exits, and avoids crashing when resuming the current thread (#16591, #16601, #16822, #16987, #17086).

> Composer and chat behavior are smoother, including fixed paste teardown, CJK word navigation, stale `/copy` output, percent-decoded local file links, and clearer truncated exec-output hints (#16202, #16829, #16648, #16810, #17076).

> #16591 Fix resume picker initial loading state @etraut-openai

> #16601 Fix resume picker stale thread names @etraut-openai

> #16578 fix(tui): handle zellij redraw and composer rendering @fcoury-oai

> #16829 Fix CJK word navigation in the TUI composer @etraut-openai

> #16822 Fix resume picker timestamp labels and stability @etraut-openai

> #16698 Remove expired April 2nd tooltip copy @etraut-openai

> #17138 fix(debug-config, guardian): fix /debug-config rendering and guardian… @owenlin0

> #16966 feat(tui): Ctrl+O copy hotkey and harden copy-as-markdown behavior @fcoury-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.119.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-04-10-4-context-window-changes-in-rust-v0-119-0|4 Context Window changes in rust-v0.119.0]] · Context Window
- [[Changes/Codex CLI/2026-04-10-8-safety-and-privacy-changes-in-rust-v0-119-0|8 Safety and Privacy changes in rust-v0.119.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-04-10-28-developer-workflow-changes-in-rust-v0-119-0|28 Developer Workflow changes in rust-v0.119.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-04-10-13-agent-mode-changes-in-rust-v0-119-0|13 Agent Mode changes in rust-v0.119.0]] · Agent Mode
- [[Changes/Codex CLI/2026-04-10-2-memory-and-personalization-changes-in-rust-v0-119-0|2 Memory and Personalization changes in rust-v0.119.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-04-10-the-readme-now-uses-the-current-chatgpt-business-plan-name-16348|The README now uses the current ChatGPT Business plan name (♯16348)]] · Enterprise and Administration
- [[Changes/Codex CLI/2026-04-10-3-voice-and-audio-changes-in-rust-v0-119-0|3 Voice and Audio changes in rust-v0.119.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-04-10-19-apps-and-integrations-changes-in-rust-v0-119-0|19 Apps and Integrations changes in rust-v0.119.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-04-10-2-account-and-access-changes-in-rust-v0-119-0|2 Account and Access changes in rust-v0.119.0]] · Account and Access
- [[Changes/Codex CLI/2026-04-10-17256-app-server-use-shared-receivers-for-app-server-message-processors-euroeles|♯17256 app-server: Use shared receivers for app-server message processors @euroelessar]] · Collaboration
- [[Changes/Codex CLI/2026-04-10-16202-fix-paste-driven-bottom-pane-completion-teardown-etraut-openai|♯16202 Fix paste-driven bottom pane completion teardown @etraut-openai]] · Editor Experience
- [[Changes/Codex CLI/2026-04-10-2-reliability-and-performance-changes-in-rust-v0-119-0|2 Reliability and Performance changes in rust-v0.119.0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-04-10-5-model-support-changes-in-rust-v0-119-0|5 Model Support changes in rust-v0.119.0]] · Model Support
- [[Changes/Codex CLI/2026-04-10-6-mobile-and-desktop-changes-in-rust-v0-119-0|6 Mobile and Desktop changes in rust-v0.119.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-04-10-187-other-changes-in-rust-v0-119-0|187 other changes in rust-v0.119.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Interface Experience

- Earlier: 2026-04-10 · Claude Code · [[Changes/Claude Code/2026-04-10-improved-focus-mode-claude-now-writes-more-self-contained-summaries-since-it-kno|Improved focus mode]]
- Later: 2026-04-10 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-04-10-slash-command-picker-shows-full-skill-descriptions-and-a-refined-scrollbar|Slash command picker shows full skill descriptions and a refined scrollbar]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-04-14 · Descript · [[Changes/Descript/2019-04-14-descript-s-sidebar-now-has-an-economical-collapsed-state|Collapsed Sidebar]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-04-10-c3563d&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-04-10-10-interface-experience-changes-in-rust-v0-119-0.md%0ACard%20ID%3A%20codex-cli-2026-04-10-c3563d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.119.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->