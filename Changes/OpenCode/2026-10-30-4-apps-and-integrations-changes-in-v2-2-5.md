---
card_id: opencode-2026-10-30-085ca1
date: '2026-10-30'
description: 'OpenCode · 2026-10-30 · Apps and Integrations: 4 changes in v2.2.5 —
  Core Calls to a tool named bash now run as shell instead of failing, with the same…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1317
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9ae1b2fe9578656586b88e7fc1e1dc355efdff3bc381214176f00d2f2d7c94a0
product: opencode
product_name: OpenCode
record:
  card_id: opencode-2026-10-30-085ca1
  comparison: ''
  date: '2026-10-30'
  description: 'OpenCode — v2.2.5: 4 Apps and Integrations changes'
  evidence:
  - quote: Core Calls to a tool named bash now run as shell instead of failing, with
      the same permissions. A plugin tool actually named bash still takes precedence.
    source_release: https://opencode.ai/changelog/v2.2.5
  - quote: Core MCP servers that send stdio messages larger than 10 MiB no longer
      get disconnected, and large messages are read much faster.
    source_release: https://opencode.ai/changelog/v2.2.5
  - quote: Core Idle locations no longer restart their MCP servers right after shutting
      down.
    source_release: https://opencode.ai/changelog/v2.2.5
  - quote: Terminal, Desktop The connect menu no longer lists MCP servers, which are
      managed in their own place.
    source_release: https://opencode.ai/changelog/v2.2.5
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: opencode
  product_name: OpenCode
  slug: 4-apps-and-integrations-changes-in-v2-2-5
  source_release: opencode-2026-10-30-v2-2-5-7ac090eb
  source_type: opencode_changelog
  theme: apps-integrations
  title: 4 Apps and Integrations changes in v2.2.5
  type: change
related_changes:
- '[[Changes/OpenCode/2026-10-29-3-apps-and-integrations-changes-in-v2-2-2|3 Apps
  and Integrations changes in v2.2.2]]'
- '[[Changes/OpenCode/2026-10-29-5-apps-and-integrations-changes-in-v2-2-1|5 Apps
  and Integrations changes in v2.2.1]]'
- '[[Changes/Claude Code/2026-10-30-3-apps-and-integrations-changes-in-v2-1-314|3
  Apps and Integrations changes in v2.1.314]]'
source_release: '[[Releases/OpenCode/opencode-2026-10-30-v2-2-5-7ac090eb|opencode-2026-10-30-v2-2-5-7ac090eb]]'
source_type: opencode_changelog
theme: apps-integrations
title: 4 Apps and Integrations changes in v2.2.5
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Apps and Integrations changes in v2.2.5

**OpenCode** · 2026-10-30 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://opencode.ai/changelog/v2.2.5) · from [[Releases/OpenCode/opencode-2026-10-30-v2-2-5-7ac090eb|v2.2.5]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Core Calls to a tool named bash now run as shell instead of failing, with the same permissions. A plugin tool actually named bash still takes precedence.

> Core MCP servers that send stdio messages larger than 10 MiB no longer get disconnected, and large messages are read much faster.

> Core Idle locations no longer restart their MCP servers right after shutting down.

> Terminal, Desktop The connect menu no longer lists MCP servers, which are managed in their own place.

Source: https://opencode.ai/changelog/v2.2.5
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenCode/2026-10-30-worktree-and-shell-mode-shortcuts|Worktree and Shell Mode Shortcuts]] · Developer Workflow
- [[Changes/OpenCode/2026-10-30-desktop-added-flat-input-surfaces-and-a-compact-input-size|Desktop Added flat input surfaces and a compact input size]] · Mobile and Desktop
- [[Changes/OpenCode/2026-10-30-desktop-added-the-missing-top-inset-to-the-search-field-in-the-recently-closed-m|Desktop Added the missing top inset to the search field in the recently closed menu]] · Interface Experience
- [[Changes/OpenCode/2026-10-30-2-context-window-changes-in-v2-2-5|2 Context Window changes in v2.2.5]] · Context Window
- [[Changes/OpenCode/2026-10-30-core-when-edit-can-t-find-oldstring-the-error-shows-the-file-s-closest-lines-or|Core When edit can't find oldString , the error shows the file's closest lines…]] · Editor Experience
- [[Changes/OpenCode/2026-10-30-percentage-compaction-buffer|Percentage Compaction Buffer]] · Context Window
- [[Changes/OpenCode/2026-10-30-core-reasoning-is-no-longer-turned-into-plain-text-when-you-switch-models-or-res|Core Reasoning is no longer turned into plain text when you switch models or resume…]] · Model Support
- [[Changes/OpenCode/2026-10-30-core-when-read-misses-because-a-folder-is-missing-the-error-names-that-folder-an|Core When read misses because a folder is missing, the error names that folder…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-10-30 · Claude Code · [[Changes/Claude Code/2026-10-30-3-apps-and-integrations-changes-in-v2-1-314|3 Apps and Integrations changes in v2.1.314]]
- Later: 2026-10-30 · OpenCode · [[Changes/OpenCode/2026-10-30-sdk-extended-client-experimental-persistentpty-update-to-rename-terminals-or-cle|SDK Extended client.experimental.persistentPty.update to rename terminals or clear…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20opencode-2026-10-30-085ca1&body=Card%3A%20Changes%2FOpenCode%2F2026-10-30-4-apps-and-integrations-changes-in-v2-2-5.md%0ACard%20ID%3A%20opencode-2026-10-30-085ca1%0ASource%3A%20https%3A%2F%2Fopencode.ai%2Fchangelog%2Fv2.2.5%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->