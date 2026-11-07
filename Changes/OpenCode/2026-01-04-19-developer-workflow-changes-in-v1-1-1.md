---
card_id: opencode-2026-01-04-3d88ad
date: '2026-01-04'
description: 'OpenCode · 2026-01-04 · Developer Workflow: 19 changes in v1.1.1 — Core
  Add development scripts for better debugging workflow in TUI'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2672
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 62fada5e2a996d2e29c581198e32dadbec5fd284d8c79fef65e7611c25c1922a
product: opencode
product_name: OpenCode
record:
  card_id: opencode-2026-01-04-3d88ad
  comparison: ''
  date: '2026-01-04'
  description: 'OpenCode — v1.1.1: 19 Developer Workflow changes'
  evidence:
  - quote: Core Add development scripts for better debugging workflow in TUI
    source_release: https://opencode.ai/changelog/v1.1.1
  - quote: Core Initialize config in worktree
    source_release: https://opencode.ai/changelog/v1.1.1
  - quote: Core Fixed dependency installation and git worktree branch creation
    source_release: https://opencode.ai/changelog/v1.1.1
  - quote: Core Improve root detection for Gradle multi-project builds in Kotlin language
      server
    source_release: https://opencode.ai/changelog/v1.1.1
  - quote: Core Add managed git worktrees
    source_release: https://opencode.ai/changelog/v1.1.1
  - quote: Core Ensure new permissions changes work for special case bash commands
      like rm, cd, etc
    source_release: https://opencode.ai/changelog/v1.1.1
  - quote: Terminal Add missing theme list keybind in TUI
    source_release: https://opencode.ai/changelog/v1.1.1
  - quote: Terminal Handle duplicate PR creation when agent creates PR
    source_release: https://opencode.ai/changelog/v1.1.1
  - quote: Terminal Fix system theme diff highlighting in TUI
    source_release: https://opencode.ai/changelog/v1.1.1
  - quote: Terminal Add --variant flag to run command
    source_release: https://opencode.ai/changelog/v1.1.1
  - quote: Terminal Remove OpenRouter provider from priority list
    source_release: https://opencode.ai/changelog/v1.1.1
  - quote: Terminal Make LSP status icon muted when no LSPs are active
    source_release: https://opencode.ai/changelog/v1.1.1
  - quote: Terminal Pass attach directory to SDK client in TUI
    source_release: https://opencode.ai/changelog/v1.1.1
  - quote: Terminal Handle actions/checkout v6 credential storage change
    source_release: https://opencode.ai/changelog/v1.1.1
  - quote: Terminal Use Bun.sleep instead of Promise with setTimeout
    source_release: https://opencode.ai/changelog/v1.1.1
  - quote: Terminal Add Osaka Jade theme
    source_release: https://opencode.ai/changelog/v1.1.1
  - quote: Terminal Fixed Windows fallback for "less" command in session list
    source_release: https://opencode.ai/changelog/v1.1.1
  - quote: Terminal Fix import command regex to properly handle file paths
    source_release: https://opencode.ai/changelog/v1.1.1
  - quote: Terminal Fix stats command day calculation and time filtering
    source_release: https://opencode.ai/changelog/v1.1.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: opencode
  product_name: OpenCode
  slug: 19-developer-workflow-changes-in-v1-1-1
  source_release: opencode-2026-01-04-v1-1-1-588acaae
  source_type: opencode_changelog
  theme: developer-workflow
  title: 19 Developer Workflow changes in v1.1.1
  type: change
related_changes:
- '[[Changes/OpenCode/2025-12-31-terminal-clarify-agent-name-placeholder-in-tips|Terminal
  Clarify agent-name placeholder in tips]]'
- '[[Changes/OpenCode/2025-12-31-terminal-adjust-keys-for-uniqueness-calculations-to-use-provider-model|Terminal
  Adjust keys for uniqueness calculations to use provider/model]]'
- '[[Changes/OpenCode/2025-12-31-core-add-support-for-lsp-workspace-didchangewatchedfiles-notifications|Core
  Add support for LSP workspace/didChangeWatchedFiles notifications]]'
source_release: '[[Releases/OpenCode/opencode-2026-01-04-v1-1-1-588acaae|opencode-2026-01-04-v1-1-1-588acaae]]'
source_type: opencode_changelog
theme: developer-workflow
title: 19 Developer Workflow changes in v1.1.1
type: change
---

<!-- chronolog:begin region="header" -->
# 19 Developer Workflow changes in v1.1.1

**OpenCode** · 2026-01-04 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://opencode.ai/changelog/v1.1.1) · from [[Releases/OpenCode/opencode-2026-01-04-v1-1-1-588acaae|v1.1.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Core Add development scripts for better debugging workflow in TUI

> Core Initialize config in worktree

> Core Fixed dependency installation and git worktree branch creation

> Core Improve root detection for Gradle multi-project builds in Kotlin language server

> Core Add managed git worktrees

> Core Ensure new permissions changes work for special case bash commands like rm, cd, etc

> Terminal Add missing theme list keybind in TUI

> Terminal Handle duplicate PR creation when agent creates PR

> Terminal Fix system theme diff highlighting in TUI

> Terminal Add --variant flag to run command

> Terminal Remove OpenRouter provider from priority list

> Terminal Make LSP status icon muted when no LSPs are active

> Terminal Pass attach directory to SDK client in TUI

> Terminal Handle actions/checkout v6 credential storage change

> Terminal Use Bun.sleep instead of Promise with setTimeout

> Terminal Add Osaka Jade theme

> Terminal Fixed Windows fallback for "less" command in session list

> Terminal Fix import command regex to properly handle file paths

> Terminal Fix stats command day calculation and time filtering

Source: https://opencode.ai/changelog/v1.1.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenCode/2026-01-04-13-safety-and-privacy-changes-in-v1-1-1|13 Safety and Privacy changes in v1.1.1]] · Safety and Privacy
- [[Changes/OpenCode/2026-01-04-3-model-support-changes-in-v1-1-1|3 Model Support changes in v1.1.1]] · Model Support
- [[Changes/OpenCode/2026-01-04-18-apps-and-integrations-changes-in-v1-1-1|18 Apps and Integrations changes in v1.1.1]] · Apps and Integrations
- [[Changes/OpenCode/2026-01-04-core-handle-notfounderror-for-non-shared-sessions-in-sync|Core Handle NotFoundError for non-shared sessions in sync]] · Collaboration
- [[Changes/OpenCode/2026-01-04-13-mobile-and-desktop-changes-in-v1-1-1|13 Mobile and Desktop changes in v1.1.1]] · Mobile and Desktop
- [[Changes/OpenCode/2026-01-04-core-add-tui-session-selection-api-endpoint-for-navigation|Core Add TUI session selection API endpoint for navigation]] · Interface Experience
- [[Changes/OpenCode/2026-01-04-4-agent-mode-changes-in-v1-1-1|4 Agent Mode changes in v1.1.1]] · Agent Mode
- [[Changes/OpenCode/2026-01-04-2-editor-experience-changes-in-v1-1-1|2 Editor Experience changes in v1.1.1]] · Editor Experience
- [[Changes/OpenCode/2026-01-04-2-context-window-changes-in-v1-1-1|2 Context Window changes in v1.1.1]] · Context Window
- [[Changes/OpenCode/2026-01-04-3-reliability-and-performance-changes-in-v1-1-1|3 Reliability and Performance changes in v1.1.1]] · Reliability and Performance
- [[Changes/OpenCode/2026-01-04-17-other-changes-in-v1-1-1|17 other changes in v1.1.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2025-12-31 · OpenCode · [[Changes/OpenCode/2025-12-31-core-add-support-for-lsp-workspace-didchangewatchedfiles-notifications|Core Add support for LSP workspace/didChangeWatchedFiles notifications]]
- Later: 2026-01-05 · OpenCode · [[Changes/OpenCode/2026-01-05-4-developer-workflow-changes-in-v1-1-2|4 Developer Workflow changes in v1.1.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20opencode-2026-01-04-3d88ad&body=Card%3A%20Changes%2FOpenCode%2F2026-01-04-19-developer-workflow-changes-in-v1-1-1.md%0ACard%20ID%3A%20opencode-2026-01-04-3d88ad%0ASource%3A%20https%3A%2F%2Fopencode.ai%2Fchangelog%2Fv1.1.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->