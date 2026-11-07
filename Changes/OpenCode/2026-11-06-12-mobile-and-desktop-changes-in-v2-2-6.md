---
card_id: opencode-2026-11-06-9b2b14
date: '2026-11-06'
description: 'OpenCode · 2026-11-06 · Mobile and Desktop: 12 changes in v2.2.6 — Core
  Added support for Microsoft Store installations of PowerShell 7 on Windows.'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-11-11-command-r-to-insert-a-speaker-label-ctrl-r-on-windows|command
    + R to insert a speaker label (ctrl + R on Windows)]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2917
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: mobile-desktop
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: e51a4042c9af2fdac5257c6513ee7f16ef84de1094bf256169d14ac6158519c7
product: opencode
product_name: OpenCode
record:
  card_id: opencode-2026-11-06-9b2b14
  comparison: ''
  date: '2026-11-06'
  description: 'OpenCode — v2.2.6: 12 Mobile and Desktop changes'
  evidence:
  - quote: Core Added support for Microsoft Store installations of PowerShell 7 on
      Windows.
    source_release: https://opencode.ai/changelog/v2.2.6
  - quote: Desktop Added close-other-tabs and close-tabs-after actions to the tab
      menu.
    source_release: https://opencode.ai/changelog/v2.2.6
  - quote: Desktop Added unread-session grouping in Inbox and failed-run indicators
      on tabs.
    source_release: https://opencode.ai/changelog/v2.2.6
  - quote: Desktop Markdown file previews now display frontmatter as a properties
      list.
    source_release: https://opencode.ai/changelog/v2.2.6
  - quote: Desktop The command palette shows a date instead of "Xd ago" for sessions
      7 or more days old. Hover the time to see the full date and time.
    source_release: https://opencode.ai/changelog/v2.2.6
  - quote: Desktop Prompt history now keeps up to 200 prompts. Past the newest 100,
      only prompts without attachments are kept.
    source_release: https://opencode.ai/changelog/v2.2.6
  - quote: Desktop Improved prompt submission and timeline behavior during loading,
      reconnects, retries, scrolling, compaction, and optimistic delivery.
    source_release: https://opencode.ai/changelog/v2.2.6
  - quote: Desktop Surface loading and offline failures in review previews, file search,
      details, Word pages, and review diffs instead of showing empty or clean results.
    source_release: https://opencode.ai/changelog/v2.2.6
  - quote: Desktop Corrected V2 file labels and mention syntax. Thanks @velmet and
      @cheapredwine.
    source_release: https://opencode.ai/changelog/v2.2.6
  - quote: Desktop Attach only the @mentions in a line comment that match an existing
      file or folder, so a comment such as Check @here no longer fails the send. Render
      partial diffs in the review pane when it shows all lines, instead of a blank
      pane. Thanks @Tarquinen.
    source_release: https://opencode.ai/changelog/v2.2.6
  - quote: Desktop Keep pasted images sendable after the clipboard tool deletes its
      temporary file. Thanks @lfscqk67.
    source_release: https://opencode.ai/changelog/v2.2.6
  - quote: Desktop While an input method is composing text, Escape, Enter, and Tab
      go to the input method instead of stopping the agent or picking a suggestion.
    source_release: https://opencode.ai/changelog/v2.2.6
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: opencode
  product_name: OpenCode
  slug: 12-mobile-and-desktop-changes-in-v2-2-6
  source_release: opencode-2026-11-06-v2-2-6-b1ac172e
  source_type: opencode_changelog
  theme: mobile-desktop
  title: 12 Mobile and Desktop changes in v2.2.6
  type: change
related_changes:
- '[[Changes/Descript/2026-11-06-3-mobile-and-desktop-changes-in-release-roundup-november-6-2026|3
  Mobile and Desktop changes in Release roundup—November 6, 2026]]'
- '[[Changes/GitHub Copilot CLI/2026-11-06-8-mobile-and-desktop-changes-in-v1-0-106|8
  Mobile and Desktop changes in v1.0.106]]'
- '[[Changes/OpenCode/2026-11-06-mobile-composer-dock|Mobile Composer Dock]]'
source_release: '[[Releases/OpenCode/opencode-2026-11-06-v2-2-6-b1ac172e|opencode-2026-11-06-v2-2-6-b1ac172e]]'
source_type: opencode_changelog
theme: mobile-desktop
title: 12 Mobile and Desktop changes in v2.2.6
type: change
---

<!-- chronolog:begin region="header" -->
# 12 Mobile and Desktop changes in v2.2.6

**OpenCode** · 2026-11-06 · [[Themes/mobile-desktop|Mobile and Desktop]] · Digest · [Official source](https://opencode.ai/changelog/v2.2.6) · from [[Releases/OpenCode/opencode-2026-11-06-v2-2-6-b1ac172e|v2.2.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Core Added support for Microsoft Store installations of PowerShell 7 on Windows.

> Desktop Added close-other-tabs and close-tabs-after actions to the tab menu.

> Desktop Added unread-session grouping in Inbox and failed-run indicators on tabs.

> Desktop Markdown file previews now display frontmatter as a properties list.

> Desktop The command palette shows a date instead of "Xd ago" for sessions 7 or more days old. Hover the time to see the full date and time.

> Desktop Prompt history now keeps up to 200 prompts. Past the newest 100, only prompts without attachments are kept.

> Desktop Improved prompt submission and timeline behavior during loading, reconnects, retries, scrolling, compaction, and optimistic delivery.

> Desktop Surface loading and offline failures in review previews, file search, details, Word pages, and review diffs instead of showing empty or clean results.

> Desktop Corrected V2 file labels and mention syntax. Thanks @velmet and @cheapredwine.

> Desktop Attach only the @mentions in a line comment that match an existing file or folder, so a comment such as Check @here no longer fails the send. Render partial diffs in the review pane when it shows all lines, instead of a blank pane. Thanks @Tarquinen.

> Desktop Keep pasted images sendable after the clipboard tool deletes its temporary file. Thanks @lfscqk67.

> Desktop While an input method is composing text, Escape, Enter, and Tab go to the input method instead of stopping the agent or picking a suggestion.

Source: https://opencode.ai/changelog/v2.2.6
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenCode/2026-11-06-scripted-runs-in-worktrees|Scripted Runs in Worktrees]] · Developer Workflow
- [[Changes/OpenCode/2026-11-06-shared-mcp-connections|Shared MCP Connections]] · Apps and Integrations
- [[Changes/OpenCode/2026-11-06-mobile-composer-dock|Mobile Composer Dock]] · Mobile and Desktop
- [[Changes/OpenCode/2026-11-06-gui-plugin-themes-and-new-slots|GUI Plugin Themes and New Slots]] · Apps and Integrations
- [[Changes/OpenCode/2026-11-06-12-developer-workflow-changes-in-v2-2-6|12 Developer Workflow changes in v2.2.6]] · Developer Workflow
- [[Changes/OpenCode/2026-11-06-desktop-mcp-sign-in-now-accepts-a-pasted-redirect-url-when-automatic-redirection|Desktop MCP sign-in now accepts a pasted redirect URL when automatic redirection…]] · Account and Access
- [[Changes/OpenCode/2026-11-06-3-safety-and-privacy-changes-in-v2-2-6|3 Safety and Privacy changes in v2.2.6]] · Safety and Privacy
- [[Changes/OpenCode/2026-11-06-core-added-azure-messages-support-for-foundry-claude-models|Core Added Azure Messages support for Foundry Claude models]] · Model Support
- [[Changes/OpenCode/2026-11-06-7-apps-and-integrations-changes-in-v2-2-6|7 Apps and Integrations changes in v2.2.6]] · Apps and Integrations
- [[Changes/OpenCode/2026-11-06-2-agent-mode-changes-in-v2-2-6|2 Agent Mode changes in v2.2.6]] · Agent Mode
- [[Changes/OpenCode/2026-11-06-core-keep-legacy-custom-providers-whose-models-set-only-part-of-limit-such-as-on|Core Keep legacy custom providers whose models set only part of limit , such as only…]] · Context Window
- [[Changes/OpenCode/2026-11-06-8-other-changes-in-v2-2-6|8 other changes in v2.2.6]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Mobile and Desktop

- Earlier: 2026-11-06 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-11-06-8-mobile-and-desktop-changes-in-v1-0-106|8 Mobile and Desktop changes in v1.0.106]]
- Later: 2026-11-06 · Qoder · [[Changes/Qoder/2026-11-06-remote-control-syncs-task-wide-pin-and-unpin-actions-in-both-directions-between|Remote Control: Syncs task-wide pin and unpin actions in both directions between…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-11-11 · Descript · [[Changes/Descript/2018-11-11-command-r-to-insert-a-speaker-label-ctrl-r-on-windows|command + R to insert a speaker label (ctrl + R on Windows)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20opencode-2026-11-06-9b2b14&body=Card%3A%20Changes%2FOpenCode%2F2026-11-06-12-mobile-and-desktop-changes-in-v2-2-6.md%0ACard%20ID%3A%20opencode-2026-11-06-9b2b14%0ASource%3A%20https%3A%2F%2Fopencode.ai%2Fchangelog%2Fv2.2.6%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->