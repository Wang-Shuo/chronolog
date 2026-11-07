---
card_id: opencode-2026-03-22-d1baec
date: '2026-03-22'
description: 'OpenCode · 2026-03-22 · Editor Experience: 3 changes in v1.3.0 — Terminal
  & Editor Terminal Error Recovery : Fixed an issue where terminals would become…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-11-11-tab-to-play-pause|TAB to play/pause]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2688
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: editor-experience
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 20179b518bfd1598be1cfdae95efa908d14f45b0a44a3606d6120251d53f8f0b
product: opencode
product_name: OpenCode
record:
  card_id: opencode-2026-03-22-d1baec
  comparison: ''
  date: '2026-03-22'
  description: 'OpenCode — v1.3.0: 3 Editor Experience changes'
  evidence:
  - quote: 'Terminal & Editor Terminal Error Recovery : Fixed an issue where terminals
      would become unresponsive when the server returned a "not found" error for terminal
      sessions. Terminals now properly reinitialize and remain interactive.'
    source_release: https://opencode.ai/changelog/v1.3.0
  - quote: 'Terminal & Editor Paste Operations : Paste operations now preserve raw
      byte data, enabling proper handling of binary content and special characters
      when pasting into the terminal.'
    source_release: https://opencode.ai/changelog/v1.3.0
  - quote: 'Terminal & Editor Prevent Duplicate Submits : Fixed issue where rapidly
      pressing Enter could submit prompts multiple times. Now ignores repeated Enter
      submits.'
    source_release: https://opencode.ai/changelog/v1.3.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: opencode
  product_name: OpenCode
  slug: 3-editor-experience-changes-in-v1-3-0
  source_release: opencode-2026-03-22-v1-3-0-00955596
  source_type: opencode_changelog
  theme: editor-experience
  title: 3 Editor Experience changes in v1.3.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-03-18-mouse-scroll-works-correctly-in-tmux-after-returning-from-an-external-editor|Mouse
  scroll works correctly in tmux after returning from an external editor]]'
- '[[Changes/Claude Code/2026-03-19-improved-permissions-tab-and-arrow-keys-now-switch-tabs-from-within-a-list|Improved
  /permissions — Tab and arrow keys now switch tabs from within a list]]'
- '[[Changes/GitHub Copilot CLI/2026-03-20-elicitation-form-shows-shift-tab-hint-for-navigating-between-fields-in-reverse|Elicitation
  form shows Shift+Tab hint for navigating between fields in reverse]]'
source_release: '[[Releases/OpenCode/opencode-2026-03-22-v1-3-0-00955596|opencode-2026-03-22-v1-3-0-00955596]]'
source_type: opencode_changelog
theme: editor-experience
title: 3 Editor Experience changes in v1.3.0
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Editor Experience changes in v1.3.0

**OpenCode** · 2026-03-22 · [[Themes/editor-experience|Editor Experience]] · Digest · [Official source](https://opencode.ai/changelog/v1.3.0) · from [[Releases/OpenCode/opencode-2026-03-22-v1-3-0-00955596|v1.3.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Terminal & Editor Terminal Error Recovery : Fixed an issue where terminals would become unresponsive when the server returned a "not found" error for terminal sessions. Terminals now properly reinitialize and remain interactive.

> Terminal & Editor Paste Operations : Paste operations now preserve raw byte data, enabling proper handling of binary content and special characters when pasting into the terminal.

> Terminal & Editor Prevent Duplicate Submits : Fixed issue where rapidly pressing Enter could submit prompts multiple times. Now ignores repeated Enter submits.

Source: https://opencode.ai/changelog/v1.3.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenCode/2026-03-22-2-collaboration-changes-in-v1-3-0|2 Collaboration changes in v1.3.0]] · Collaboration
- [[Changes/OpenCode/2026-03-22-2-developer-workflow-changes-in-v1-3-0|2 Developer Workflow changes in v1.3.0]] · Developer Workflow
- [[Changes/OpenCode/2026-03-22-3-model-support-changes-in-v1-3-0|3 Model Support changes in v1.3.0]] · Model Support
- [[Changes/OpenCode/2026-03-22-5-mobile-and-desktop-changes-in-v1-3-0|5 Mobile and Desktop changes in v1.3.0]] · Mobile and Desktop
- [[Changes/OpenCode/2026-03-22-4-account-and-access-changes-in-v1-3-0|4 Account and Access changes in v1.3.0]] · Account and Access
- [[Changes/OpenCode/2026-03-22-ui-ux-improvements-agent-skill-ordering-more-consistent-ai-responses-with-improv|UI/UX Improvements Agent & Skill Ordering]] · Agent Mode
- [[Changes/OpenCode/2026-03-22-3-interface-experience-changes-in-v1-3-0|3 Interface Experience changes in v1.3.0]] · Interface Experience
- [[Changes/OpenCode/2026-03-22-removed-anthropic-oauth-plugin-see|Removed anthropic oauth plugin, see]] · Account and Access
- [[Changes/OpenCode/2026-03-22-providers-models-xai-responses-api-improved-xai-reasoning-models-performance-in|Providers & Models xAI Responses API]] · Reliability and Performance
- [[Changes/OpenCode/2026-03-22-2-context-window-changes-in-v1-3-0|2 Context Window changes in v1.3.0]] · Context Window
- [[Changes/OpenCode/2026-03-22-8-other-changes-in-v1-3-0|8 other changes in v1.3.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Editor Experience

- Earlier: 2026-03-20 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-03-20-elicitation-form-shows-shift-tab-hint-for-navigating-between-fields-in-reverse|Elicitation form shows Shift+Tab hint for navigating between fields in reverse]]
- Later: 2026-03-24 · OpenCode · [[Changes/OpenCode/2026-03-24-changed-command-palette-shortcut-to-cmd-k-with-cmd-p-still-working-as-fallback|Changed command palette shortcut to Cmd+K (with Cmd+P still working as fallback)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-11-11 · Descript · [[Changes/Descript/2018-11-11-tab-to-play-pause|TAB to play/pause]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20opencode-2026-03-22-d1baec&body=Card%3A%20Changes%2FOpenCode%2F2026-03-22-3-editor-experience-changes-in-v1-3-0.md%0ACard%20ID%3A%20opencode-2026-03-22-d1baec%0ASource%3A%20https%3A%2F%2Fopencode.ai%2Fchangelog%2Fv1.3.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->