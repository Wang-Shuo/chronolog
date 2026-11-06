---
card_id: codex-cli-2026-10-29-a0b156
date: '2026-10-29'
description: 'Codex CLI · 2026-10-29 · Safety and Privacy: 10 changes in 0.166.0 —
  Added clearer safety-block explanations and selectable safer follow-up prompts in
  the TUI…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1292
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: e49901939b5d9c41f48476b4c615e87593586958611d58032abcebf3845fd6ce
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-10-29-a0b156
  comparison: ''
  date: '2026-10-29'
  description: 'Codex CLI — 0.166.0: 10 Safety and Privacy changes'
  evidence:
  - quote: 'Added clearer safety-block explanations and selectable safer follow-up
      prompts in the TUI. (#57363, #57365)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: Preserved acknowledged approval and permission settings when resuming or
      forking threads. (#57227)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#56468 Preserve `SystemRoot` for Windows filesystem sandbox helpers @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57203 Preserve command cwd in permission and post-tool hooks @eternal-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57255 Record reviewed exceptions for zstd security advisories @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57260 Centralize permission request preparation and approval actions
      @swastik-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57263 Support model-catalog wording for permission path warnings @goodman-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57270 Load cloud config for sandbox and remote exec-server commands @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57363 Explain safety policy blocks with turn-scoped recourse in the TUI
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57365 Offer safer rewrites after safety blocks in the TUI @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 10-safety-and-privacy-changes-in-rust-v0-166-0
  source_release: codex-cli-2026-10-29-rust-v0-166-0-github-428320524-44f8c24a
  source_type: github_releases
  theme: safety-privacy
  title: 10 Safety and Privacy changes in rust-v0.166.0
  type: change
related_changes:
- '[[Changes/Gemini CLI/2026-10-27-fix-ci-remove-unsupported-members-permission-in-unassign-inactive-assignees-work|fix(ci):
  remove unsupported members permission in unassign-inactive-assignees workflow]]'
- '[[Changes/OpenHands/2026-10-27-feat-sidebar-start-a-new-conversation-in-the-row-s-sandbox-ohe-3689-by-hieptl-in|feat(sidebar):
  start a new conversation in the row''s sandbox (OHE-3689)]]'
- '[[Changes/ChatGPT/2026-10-28-texting-your-dot-is-starting-to-roll-out-in-beta-to-pro-users-in-the-u-s|Texting
  your dot]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-10-29-rust-v0-166-0-github-428320524-44f8c24a|codex-cli-2026-10-29-rust-v0-166-0-github-428320524-44f8c24a]]'
source_type: github_releases
theme: safety-privacy
title: 10 Safety and Privacy changes in rust-v0.166.0
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Safety and Privacy changes in rust-v0.166.0

**Codex CLI** · 2026-10-29 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.166.0) · from [[Releases/Codex CLI/codex-cli-2026-10-29-rust-v0-166-0-github-428320524-44f8c24a|0.166.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added clearer safety-block explanations and selectable safer follow-up prompts in the TUI. (#57363, #57365)

> Preserved acknowledged approval and permission settings when resuming or forking threads. (#57227)

> #56468 Preserve `SystemRoot` for Windows filesystem sandbox helpers @jif-oai

> #57203 Preserve command cwd in permission and post-tool hooks @eternal-openai

> #57255 Record reviewed exceptions for zstd security advisories @charliemarsh-oai

> #57260 Centralize permission request preparation and approval actions @swastik-oai

> #57263 Support model-catalog wording for permission path warnings @goodman-oai

> #57270 Load cloud config for sandbox and remote exec-server commands @abhinav-oai

> #57363 Explain safety policy blocks with turn-scoped recourse in the TUI @etraut-openai

> #57365 Offer safer rewrites after safety blocks in the TUI @etraut-openai

Source: https://github.com/openai/codex/releases/tag/rust-v0.166.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-10-29-57503-fix-macos-standalone-release-pruning-etraut-openai|♯57503 Fix macOS standalone release pruning @etraut-openai]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-10-29-3-image-generation-changes-in-rust-v0-166-0|3 Image Generation changes in rust-v0.166.0]] · Image Generation
- [[Changes/Codex CLI/2026-10-29-10-developer-workflow-changes-in-rust-v0-166-0|10 Developer Workflow changes in rust-v0.166.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-10-29-22-apps-and-integrations-changes-in-rust-v0-166-0|22 Apps and Integrations changes in rust-v0.166.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-10-29-57342-separate-tui-session-resume-preparation-from-activation-bc-openai|♯57342 Separate TUI session resume preparation from activation @bc-openai]] · Projects and Workspaces
- [[Changes/Codex CLI/2026-10-29-12-interface-experience-changes-in-rust-v0-166-0|12 Interface Experience changes in rust-v0.166.0]] · Interface Experience
- [[Changes/Codex CLI/2026-10-29-3-editor-experience-changes-in-rust-v0-166-0|3 Editor Experience changes in rust-v0.166.0]] · Editor Experience
- [[Changes/Codex CLI/2026-10-29-10-model-support-changes-in-rust-v0-166-0|10 Model Support changes in rust-v0.166.0]] · Model Support
- [[Changes/Codex CLI/2026-10-29-57542-add-model-gated-literature-search-to-standalone-web-search-rhan-oai|♯57542 Add model-gated literature search to standalone web search @rhan-oai]] · Search and Browsing
- [[Changes/Codex CLI/2026-10-29-57226-allow-nfs-database-migration-with-shared-file-permissions-dkovalenko-oai|♯57226 Allow NFS database migration with shared file permissions @dkovalenko-oai]] · Collaboration
- [[Changes/Codex CLI/2026-10-29-8-account-and-access-changes-in-rust-v0-166-0|8 Account and Access changes in rust-v0.166.0]] · Account and Access
- [[Changes/Codex CLI/2026-10-29-2-memory-and-personalization-changes-in-rust-v0-166-0|2 Memory and Personalization changes in rust-v0.166.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-10-29-56495-add-paginated-channel-subscription-queries-to-the-local-message-board-feli|♯56495 Add paginated channel subscription queries to the local message board @felixxia-oai]] · Pricing Model
- [[Changes/Codex CLI/2026-10-29-7-agent-mode-changes-in-rust-v0-166-0|7 Agent Mode changes in rust-v0.166.0]] · Agent Mode
- [[Changes/Codex CLI/2026-10-29-13-context-window-changes-in-rust-v0-166-0|13 Context Window changes in rust-v0.166.0]] · Context Window
- [[Changes/Codex CLI/2026-10-29-173-other-changes-in-rust-v0-166-0|173 other changes in rust-v0.166.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-10-28 · ChatGPT · [[Changes/ChatGPT/2026-10-28-texting-your-dot-is-starting-to-roll-out-in-beta-to-pro-users-in-the-u-s|Texting your dot]]
- Later: 2026-10-30 · Claude Code · [[Changes/Claude Code/2026-10-30-10-safety-and-privacy-changes-in-v2-1-314|10 Safety and Privacy changes in v2.1.314]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-10-29-a0b156&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-10-29-10-safety-and-privacy-changes-in-rust-v0-166-0.md%0ACard%20ID%3A%20codex-cli-2026-10-29-a0b156%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.166.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->