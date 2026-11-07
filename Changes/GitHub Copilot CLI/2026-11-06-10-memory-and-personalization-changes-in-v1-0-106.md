---
card_id: github-copilot-cli-2026-11-06-48f426
date: '2026-11-06'
description: 'GitHub Copilot CLI · 2026-11-06 · Memory and Personalization: 10 changes
  in 1.0.106 — `copilot help permissions` now documents glob patterns in `write(path)`…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1205
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: acbf35da9d46993eaa3c956fd43f580caa58f2be530841986127c816f5c66f8a
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-11-06-48f426
  comparison: ''
  date: '2026-11-06'
  description: 'GitHub Copilot CLI — 1.0.106: 10 Memory and Personalization changes'
  evidence:
  - quote: '`copilot help permissions` now documents glob patterns in `write(path)`
      and `read(path)` rules, lists the `read` and `memory` kinds, and explains that
      an unscoped `write` rule approves shell output redirection but not the command
      itself; it no longer says wildcard matching is coming in the future.'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: /memory now reports when Memory is disabled for the session by an experiment
      and clarifies /memory on behavior.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Tool rows and the memory prompt no longer let escape sequences in text
      the model wrote hide words or add links. Search patterns and memory text show
      their control characters instead.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: A ~/ directory in skillDirectories, COPILOT_SKILLS_DIRS or COPILOT_CUSTOM_INSTRUCTIONS_DIRS
      now resolves to your home directory, so its skills and instructions load.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: '`copilot help config` now says `autoUpdate` defaults to off in CI environments
      and that non-interactive `-p` runs start with memory off unless `--enable-memory`
      is passed'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: copilot sessions import and copilot memories import with --output json
      now escape C1 control characters from the imported file instead of writing them
      to the terminal raw
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Sessions and memories import now accept quoted ~/ paths, including session
      --working-directory values.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: sessions import and memories import accept JSONL files with a UTF-8 BOM
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Collapsed memory timeline entries show multi-line facts as a single preview
      row.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: /memory show indicates when repository memory scope is unavailable
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 10-memory-and-personalization-changes-in-v1-0-106
  source_release: github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4
  source_type: github_releases
  theme: memory
  title: 10 Memory and Personalization changes in v1.0.106
  type: change
related_changes:
- '[[Changes/Lovable/2026-11-04-dreaming-lovable-keeps-its-memory-up-to-date|Dreaming:
  Lovable keeps its memory up to date]]'
- '[[Changes/OpenClaw/2026-11-05-5-memory-and-personalization-changes-in-v2026-11-1|5
  Memory and Personalization changes in v2026.11.1]]'
- '[[Changes/Codex CLI/2026-11-06-2-memory-and-personalization-changes-in-rust-v0-167-0|2
  Memory and Personalization changes in rust-v0.167.0]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4|github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4]]'
source_type: github_releases
theme: memory
title: 10 Memory and Personalization changes in v1.0.106
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Memory and Personalization changes in v1.0.106

**GitHub Copilot CLI** · 2026-11-06 · [[Themes/memory|Memory and Personalization]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.106) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4|1.0.106]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> `copilot help permissions` now documents glob patterns in `write(path)` and `read(path)` rules, lists the `read` and `memory` kinds, and explains that an unscoped `write` rule approves shell output redirection but not the command itself; it no longer says wildcard matching is coming in the future.

> /memory now reports when Memory is disabled for the session by an experiment and clarifies /memory on behavior.

> Tool rows and the memory prompt no longer let escape sequences in text the model wrote hide words or add links. Search patterns and memory text show their control characters instead.

> A ~/ directory in skillDirectories, COPILOT_SKILLS_DIRS or COPILOT_CUSTOM_INSTRUCTIONS_DIRS now resolves to your home directory, so its skills and instructions load.

> `copilot help config` now says `autoUpdate` defaults to off in CI environments and that non-interactive `-p` runs start with memory off unless `--enable-memory` is passed

> copilot sessions import and copilot memories import with --output json now escape C1 control characters from the imported file instead of writing them to the terminal raw

> Sessions and memories import now accept quoted ~/ paths, including session --working-directory values.

> sessions import and memories import accept JSONL files with a UTF-8 BOM

> Collapsed memory timeline entries show multi-line facts as a single preview row.

> /memory show indicates when repository memory scope is unavailable

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.106
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-11-06-4-voice-and-audio-changes-in-v1-0-106|4 Voice and Audio changes in v1.0.106]] · Voice and Audio
- [[Changes/GitHub Copilot CLI/2026-11-06-2-files-and-data-changes-in-v1-0-106|2 Files and Data changes in v1.0.106]] · Files and Data
- [[Changes/GitHub Copilot CLI/2026-11-06-3-reliability-and-performance-changes-in-v1-0-106|3 Reliability and Performance changes in v1.0.106]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-11-06-34-agent-mode-changes-in-v1-0-106|34 Agent Mode changes in v1.0.106]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-11-06-64-developer-workflow-changes-in-v1-0-106|64 Developer Workflow changes in v1.0.106]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-11-06-34-safety-and-privacy-changes-in-v1-0-106|34 Safety and Privacy changes in v1.0.106]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-11-06-9-collaboration-changes-in-v1-0-106|9 Collaboration changes in v1.0.106]] · Collaboration
- [[Changes/GitHub Copilot CLI/2026-11-06-8-mobile-and-desktop-changes-in-v1-0-106|8 Mobile and Desktop changes in v1.0.106]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-11-06-4-projects-and-workspaces-changes-in-v1-0-106|4 Projects and Workspaces changes in v1.0.106]] · Projects and Workspaces
- [[Changes/GitHub Copilot CLI/2026-11-06-8-accessibility-and-localization-changes-in-v1-0-106|8 Accessibility and Localization changes in v1.0.106]] · Accessibility and Localization
- [[Changes/GitHub Copilot CLI/2026-11-06-17-context-window-changes-in-v1-0-106|17 Context Window changes in v1.0.106]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-11-06-57-editor-experience-changes-in-v1-0-106|57 Editor Experience changes in v1.0.106]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-11-06-33-model-support-changes-in-v1-0-106|33 Model Support changes in v1.0.106]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-11-06-89-apps-and-integrations-changes-in-v1-0-106|89 Apps and Integrations changes in v1.0.106]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-11-06-2-image-generation-changes-in-v1-0-106|2 Image Generation changes in v1.0.106]] · Image Generation
- [[Changes/GitHub Copilot CLI/2026-11-06-42-interface-experience-changes-in-v1-0-106|42 Interface Experience changes in v1.0.106]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-11-06-5-pricing-model-changes-in-v1-0-106|5 Pricing Model changes in v1.0.106]] · Pricing Model
- [[Changes/GitHub Copilot CLI/2026-11-06-in-the-every-schedule-manager-x-now-removes-the-highlighted-schedule-even-after|In the /every schedule manager, x now removes the highlighted schedule even after…]] · Automation and Scheduling
- [[Changes/GitHub Copilot CLI/2026-11-06-23-account-and-access-changes-in-v1-0-106|23 Account and Access changes in v1.0.106]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-11-06-172-other-changes-in-v1-0-106|172 other changes in v1.0.106]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Memory and Personalization

- Earlier: 2026-11-06 · Codex CLI · [[Changes/Codex CLI/2026-11-06-2-memory-and-personalization-changes-in-rust-v0-167-0|2 Memory and Personalization changes in rust-v0.167.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-11-06-48f426&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-11-06-10-memory-and-personalization-changes-in-v1-0-106.md%0ACard%20ID%3A%20github-copilot-cli-2026-11-06-48f426%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.106%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->