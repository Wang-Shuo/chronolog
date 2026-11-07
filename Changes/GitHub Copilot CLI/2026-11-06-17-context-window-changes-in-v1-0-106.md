---
card_id: github-copilot-cli-2026-11-06-7c7848
date: '2026-11-06'
description: 'GitHub Copilot CLI · 2026-11-06 · Context Window: 17 changes in 1.0.106
  — Model picker shows context window size for flat, unpriced, and single-tier models'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click
    to select a range]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2606
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 7e28493eb8c04262380630581d4bf6de478914cb38939b6652b84afee8f0f182
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-11-06-7c7848
  comparison: ''
  date: '2026-11-06'
  description: 'GitHub Copilot CLI — 1.0.106: 17 Context Window changes'
  evidence:
  - quote: Model picker shows context window size for flat, unpriced, and single-tier
      models
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: The model picker keeps its Context and Reasoning column labels when a search
      or scroll hides the first model group.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Sessions without required recovery tools continue automatic compaction
      instead of failing rollover.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Warn when older messages are dropped for context limits and include compaction/truncation
      events in JSON output.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: /context shows updated usage details after switching models in an active
      session
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: '`copilot workflow run` and `copilot -p` text output now redact `--secret-env-vars`
      values and recognized tokens in lines a workflow or extension logs, as the JSON
      output and the final result already did.'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Resumed handoff and compaction timeline text is sanitized to prevent style
      injection and extra label rows.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: /context correctly separates custom instructions from the system prompt
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Cancelling /compact with Esc Esc shows "Compaction Cancelled" instead of
      a failure message
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Sessions authenticated through GitHub CLI recover from expired access tokens
      without restarting or changing the selected account
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Changing reasoning effort or context tier on the same model no longer cancels
      running sidekick tasks.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Resuming a session with `copilot -p` now compacts its history before the
      new prompt when it is over the compaction threshold, so repeated prompt-mode
      runs keep the session compacted
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Assisted mode now reviews individual human messages up to 32,000 characters
      and fails closed before dispatch when the complete judge request exceeds model
      context
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Prompts submitted during local /compact stay queued and send after compaction
      completes or is cancelled.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Improve Claude token estimation so context budgeting and trimming decisions
      are more accurate.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Cloud startup now shows repository-cloning progress before initial workspace
      context persistence finishes.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Offer a long-context switch option when changing to models with lower default
      token limits.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 17-context-window-changes-in-v1-0-106
  source_release: github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4
  source_type: github_releases
  theme: context-window
  title: 17 Context Window changes in v1.0.106
  type: change
related_changes:
- '[[Changes/Raycast/2026-11-04-today-we-re-introducing-dictate-to-ai-a-new-command-that-combines-what-you-say-w-9ef173|Raycast
  introduces Dictate to AI, a new command that combines what you say…]]'
- '[[Changes/OpenClaw/2026-11-05-3-context-window-changes-in-v2026-11-1|3 Context
  Window changes in v2026.11.1]]'
- '[[Changes/Codex CLI/2026-11-06-8-context-window-changes-in-rust-v0-167-0|8 Context
  Window changes in rust-v0.167.0]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4|github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4]]'
source_type: github_releases
theme: context-window
title: 17 Context Window changes in v1.0.106
type: change
---

<!-- chronolog:begin region="header" -->
# 17 Context Window changes in v1.0.106

**GitHub Copilot CLI** · 2026-11-06 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.106) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4|1.0.106]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Model picker shows context window size for flat, unpriced, and single-tier models

> The model picker keeps its Context and Reasoning column labels when a search or scroll hides the first model group.

> Sessions without required recovery tools continue automatic compaction instead of failing rollover.

> Warn when older messages are dropped for context limits and include compaction/truncation events in JSON output.

> /context shows updated usage details after switching models in an active session

> `copilot workflow run` and `copilot -p` text output now redact `--secret-env-vars` values and recognized tokens in lines a workflow or extension logs, as the JSON output and the final result already did.

> Resumed handoff and compaction timeline text is sanitized to prevent style injection and extra label rows.

> /context correctly separates custom instructions from the system prompt

> Cancelling /compact with Esc Esc shows "Compaction Cancelled" instead of a failure message

> Sessions authenticated through GitHub CLI recover from expired access tokens without restarting or changing the selected account

> Changing reasoning effort or context tier on the same model no longer cancels running sidekick tasks.

> Resuming a session with `copilot -p` now compacts its history before the new prompt when it is over the compaction threshold, so repeated prompt-mode runs keep the session compacted

> Assisted mode now reviews individual human messages up to 32,000 characters and fails closed before dispatch when the complete judge request exceeds model context

> Prompts submitted during local /compact stay queued and send after compaction completes or is cancelled.

> Improve Claude token estimation so context budgeting and trimming decisions are more accurate.

> Cloud startup now shows repository-cloning progress before initial workspace context persistence finishes.

> Offer a long-context switch option when changing to models with lower default token limits.

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.106
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-11-06-4-voice-and-audio-changes-in-v1-0-106|4 Voice and Audio changes in v1.0.106]] · Voice and Audio
- [[Changes/GitHub Copilot CLI/2026-11-06-2-files-and-data-changes-in-v1-0-106|2 Files and Data changes in v1.0.106]] · Files and Data
- [[Changes/GitHub Copilot CLI/2026-11-06-3-reliability-and-performance-changes-in-v1-0-106|3 Reliability and Performance changes in v1.0.106]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-11-06-34-agent-mode-changes-in-v1-0-106|34 Agent Mode changes in v1.0.106]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-11-06-10-memory-and-personalization-changes-in-v1-0-106|10 Memory and Personalization changes in v1.0.106]] · Memory and Personalization
- [[Changes/GitHub Copilot CLI/2026-11-06-64-developer-workflow-changes-in-v1-0-106|64 Developer Workflow changes in v1.0.106]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-11-06-34-safety-and-privacy-changes-in-v1-0-106|34 Safety and Privacy changes in v1.0.106]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-11-06-9-collaboration-changes-in-v1-0-106|9 Collaboration changes in v1.0.106]] · Collaboration
- [[Changes/GitHub Copilot CLI/2026-11-06-8-mobile-and-desktop-changes-in-v1-0-106|8 Mobile and Desktop changes in v1.0.106]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-11-06-4-projects-and-workspaces-changes-in-v1-0-106|4 Projects and Workspaces changes in v1.0.106]] · Projects and Workspaces
- [[Changes/GitHub Copilot CLI/2026-11-06-8-accessibility-and-localization-changes-in-v1-0-106|8 Accessibility and Localization changes in v1.0.106]] · Accessibility and Localization
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
## Nearby in Context Window

- Earlier: 2026-11-06 · Codex CLI · [[Changes/Codex CLI/2026-11-06-8-context-window-changes-in-rust-v0-167-0|8 Context Window changes in rust-v0.167.0]]
- Later: 2026-11-06 · OpenCode · [[Changes/OpenCode/2026-11-06-core-keep-legacy-custom-providers-whose-models-set-only-part-of-limit-such-as-on|Core Keep legacy custom providers whose models set only part of limit , such as only…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click to select a range]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-11-06-7c7848&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-11-06-17-context-window-changes-in-v1-0-106.md%0ACard%20ID%3A%20github-copilot-cli-2026-11-06-7c7848%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.106%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->