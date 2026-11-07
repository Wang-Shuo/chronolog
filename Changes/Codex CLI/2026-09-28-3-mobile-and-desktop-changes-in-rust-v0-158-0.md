---
card_id: codex-cli-2026-09-28-357f56
date: '2026-09-28'
description: 'Codex CLI · 2026-09-28 · Mobile and Desktop: 3 changes in 0.158.0 —
  macOS patch operations now recognize system path aliases covered by existing permissions…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-11-11-command-r-to-insert-a-speaker-label-ctrl-r-on-windows|command
    + R to insert a speaker label (ctrl + R on Windows)]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2878
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: mobile-desktop
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: fb73055c15e0b77457d1a1db6ea64c25c281cb8dd751850aa9bb48eb5869a30d
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-09-28-357f56
  comparison: ''
  date: '2026-09-28'
  description: 'Codex CLI — 0.158.0: 3 Mobile and Desktop changes'
  evidence:
  - quote: macOS patch operations now recognize system path aliases covered by existing
      permissions, avoiding unnecessary approval prompts. (#47879)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47672 Fix no-reparse directory opens on Windows 10 @zm-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47951 Use prebuilt V8 archives for Bazel on macOS and GNU Linux @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 3-mobile-and-desktop-changes-in-rust-v0-158-0
  source_release: codex-cli-2026-09-28-rust-v0-158-0-github-397962047-f52f49e7
  source_type: github_releases
  theme: mobile-desktop
  title: 3 Mobile and Desktop changes in rust-v0.158.0
  type: change
related_changes:
- '[[Changes/OpenHands/2026-09-23-feat-desktop-universal-macos-dmg-with-per-arch-bundled-runtimes-by-harsh-batheja|feat(desktop):
  universal macOS DMG with per-arch bundled runtimes]]'
- '[[Changes/Claude Code/2026-09-24-improved-the-error-shown-on-windows-when-a-session-can-t-be-resumed-because-its|Improved
  the error shown on Windows when a session can''t be resumed because…]]'
- '[[Changes/Windsurf/2026-09-24-devin-desktop|Devin Desktop]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-09-28-rust-v0-158-0-github-397962047-f52f49e7|codex-cli-2026-09-28-rust-v0-158-0-github-397962047-f52f49e7]]'
source_type: github_releases
theme: mobile-desktop
title: 3 Mobile and Desktop changes in rust-v0.158.0
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Mobile and Desktop changes in rust-v0.158.0

**Codex CLI** · 2026-09-28 · [[Themes/mobile-desktop|Mobile and Desktop]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.158.0) · from [[Releases/Codex CLI/codex-cli-2026-09-28-rust-v0-158-0-github-397962047-f52f49e7|0.158.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> macOS patch operations now recognize system path aliases covered by existing permissions, avoiding unnecessary approval prompts. (#47879)

> #47672 Fix no-reparse directory opens on Windows 10 @zm-oai

> #47951 Use prebuilt V8 archives for Bazel on macOS and GNU Linux @aibrahim-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.158.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-09-28-9-safety-and-privacy-changes-in-rust-v0-158-0|9 Safety and Privacy changes in rust-v0.158.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-09-28-47975-prevent-stale-voice-answers-from-reappearing-during-speech-recovery-etraut|♯47975 Prevent stale voice answers from reappearing during speech recovery @etraut-openai]] · Voice and Audio
- [[Changes/Codex CLI/2026-09-28-13-apps-and-integrations-changes-in-rust-v0-158-0|13 Apps and Integrations changes in rust-v0.158.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-09-28-8-account-and-access-changes-in-rust-v0-158-0|8 Account and Access changes in rust-v0.158.0]] · Account and Access
- [[Changes/Codex CLI/2026-09-28-3-memory-and-personalization-changes-in-rust-v0-158-0|3 Memory and Personalization changes in rust-v0.158.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-09-28-2-collaboration-changes-in-rust-v0-158-0|2 Collaboration changes in rust-v0.158.0]] · Collaboration
- [[Changes/Codex CLI/2026-09-28-7-model-support-changes-in-rust-v0-158-0|7 Model Support changes in rust-v0.158.0]] · Model Support
- [[Changes/Codex CLI/2026-09-28-3-image-generation-changes-in-rust-v0-158-0|3 Image Generation changes in rust-v0.158.0]] · Image Generation
- [[Changes/Codex CLI/2026-09-28-4-editor-experience-changes-in-rust-v0-158-0|4 Editor Experience changes in rust-v0.158.0]] · Editor Experience
- [[Changes/Codex CLI/2026-09-28-6-interface-experience-changes-in-rust-v0-158-0|6 Interface Experience changes in rust-v0.158.0]] · Interface Experience
- [[Changes/Codex CLI/2026-09-28-47984-add-multi-agent-spawn-latency-and-failure-metrics-owenlin0|♯47984 Add multi-agent spawn latency and failure metrics @owenlin0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-09-28-14-developer-workflow-changes-in-rust-v0-158-0|14 Developer Workflow changes in rust-v0.158.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-09-28-11-agent-mode-changes-in-rust-v0-158-0|11 Agent Mode changes in rust-v0.158.0]] · Agent Mode
- [[Changes/Codex CLI/2026-09-28-17-context-window-changes-in-rust-v0-158-0|17 Context Window changes in rust-v0.158.0]] · Context Window
- [[Changes/Codex CLI/2026-09-28-96-other-changes-in-rust-v0-158-0|96 other changes in rust-v0.158.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Mobile and Desktop

- Earlier: 2026-09-24 · Windsurf · [[Changes/Windsurf/2026-09-24-devin-desktop|Devin Desktop]]
- Later: 2026-09-28 · Google Antigravity · [[Changes/Google Antigravity/2026-09-28-press-option-command-p-on-macos-or-alt-shift-p-on-windows-and-linux-to-pin-or-un|Press Option+Command+P on macOS or Alt+Shift+P on Windows and Linux to pin or unpin…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-11-11 · Descript · [[Changes/Descript/2018-11-11-command-r-to-insert-a-speaker-label-ctrl-r-on-windows|command + R to insert a speaker label (ctrl + R on Windows)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-09-28-357f56&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-09-28-3-mobile-and-desktop-changes-in-rust-v0-158-0.md%0ACard%20ID%3A%20codex-cli-2026-09-28-357f56%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.158.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->