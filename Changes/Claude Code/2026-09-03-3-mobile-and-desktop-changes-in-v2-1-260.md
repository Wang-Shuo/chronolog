---
card_id: claude-code-2026-09-03-9ed8ec
date: '2026-09-03'
description: 'Claude Code · 2026-09-03 · Mobile and Desktop: 3 changes in v2.1.260
  — Added Claude apps gateway support for newer Claude Desktop keys in `desktop` policy…'
diffusion:
  first_in_tracked: "[[Changes/Cursor/2023-03-14-windows-and-linux-support|Windows
    and Linux support \U0001F973]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1269
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: mobile-desktop
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 6b3b99b78e22a859b1593796a4a11fde6670833b5487d2ebdf714dd6b1638d23
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-03-9ed8ec
  comparison: ''
  date: '2026-09-03'
  description: 'Claude Code — v2.1.260: 3 Mobile and Desktop changes'
  evidence:
  - quote: Added Claude apps gateway support for newer Claude Desktop keys in `desktop`
      policy blocks, including `userPluginMarketplacesEnabled` and `userPluginUploadsEnabled`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.260
  - quote: Changed Claude apps gateway to send `orgPluginSettings` in the list form
      read by Claude Desktop 1.15200.0 and later; older desktops ignore it
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.260
  - quote: Changed Claude apps gateway to also refuse to start, naming the field,
      when a `desktop` policy misspells a field in a nested object of a `managedMcpServers`
      or `orgPluginSettings` entry
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.260
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-mobile-and-desktop-changes-in-v2-1-260
  source_release: claude-code-2026-09-03-v2-1-260-github-382367470-ac2ba1fc
  source_type: github_releases
  theme: mobile-desktop
  title: 3 Mobile and Desktop changes in v2.1.260
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-08-31-share-your-stickers-in-messaging-apps-download-your-pack-or-add-it-to-imessage-o|Share
  your stickers in messaging apps]]'
- '[[Changes/ChatGPT/2026-08-31-chatgpt-work-and-codex-can-now-use-tools-that-supported-websites-provide-directl|ChatGPT
  Work and Codex can now use tools that supported websites provide directly…]]'
- '[[Changes/Claude Code/2026-09-01-changed-add-dir-add-dir-and-additionaldirectories-to-refuse-network-paths-unc-sh|Changed
  --add-dir, /add-dir, and additionalDirectories to refuse network paths…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-03-v2-1-260-github-382367470-ac2ba1fc|claude-code-2026-09-03-v2-1-260-github-382367470-ac2ba1fc]]'
source_type: github_releases
theme: mobile-desktop
title: 3 Mobile and Desktop changes in v2.1.260
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Mobile and Desktop changes in v2.1.260

**Claude Code** · 2026-09-03 · [[Themes/mobile-desktop|Mobile and Desktop]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.260) · from [[Releases/Claude Code/claude-code-2026-09-03-v2-1-260-github-382367470-ac2ba1fc|v2.1.260]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added Claude apps gateway support for newer Claude Desktop keys in `desktop` policy blocks, including `userPluginMarketplacesEnabled` and `userPluginUploadsEnabled`

> Changed Claude apps gateway to send `orgPluginSettings` in the list form read by Claude Desktop 1.15200.0 and later; older desktops ignore it

> Changed Claude apps gateway to also refuse to start, naming the field, when a `desktop` policy misspells a field in a nested object of a `managedMcpServers` or `orgPluginSettings` entry

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.260
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-03-2-model-support-changes-in-v2-1-260|2 Model Support changes in v2.1.260]] · Model Support
- [[Changes/Claude Code/2026-09-03-improved-the-settings-error-for-rules-such-as-edit-c-dir-name-where-is-read-as-a|Improved the settings error for rules such as Edit(C:\dir\(name)\), where…]] · Editor Experience
- [[Changes/Claude Code/2026-09-03-improved-deleting-a-background-session-whose-worktree-has-unpushed-commits-the-m|Improved deleting a background session whose worktree has unpushed commits]] · Developer Workflow
- [[Changes/Claude Code/2026-09-03-4-interface-experience-changes-in-v2-1-260|4 Interface Experience changes in v2.1.260]] · Interface Experience
- [[Changes/Claude Code/2026-09-03-2-agent-mode-changes-in-v2-1-260|2 Agent Mode changes in v2.1.260]] · Agent Mode
- [[Changes/Claude Code/2026-09-03-3-context-window-changes-in-v2-1-260|3 Context Window changes in v2.1.260]] · Context Window
- [[Changes/Claude Code/2026-09-03-4-apps-and-integrations-changes-in-v2-1-260|4 Apps and Integrations changes in v2.1.260]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-03-7-safety-and-privacy-changes-in-v2-1-260|7 Safety and Privacy changes in v2.1.260]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-03-added-reload-plugins-to-headless-sessions-so-it-appears-in-the-claude-code-deskt|Added /reload-plugins to headless sessions, so it appears in the Claude Code…]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-03-3-other-changes-in-v2-1-260|3 other changes in v2.1.260]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Mobile and Desktop

- Earlier: 2026-09-01 · Claude Code · [[Changes/Claude Code/2026-09-01-changed-add-dir-add-dir-and-additionaldirectories-to-refuse-network-paths-unc-sh|Changed --add-dir, /add-dir, and additionalDirectories to refuse network paths…]]
- Later: 2026-09-08 · ChatGPT · [[Changes/ChatGPT/2026-09-08-turn-a-sketch-into-an-image-on-mobile-type-in-the-message-box-and-select-sketch|Turn a sketch into an image]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-14 · Cursor · [[Changes/Cursor/2023-03-14-windows-and-linux-support|Windows and Linux support 🥳]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-03-9ed8ec&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-03-3-mobile-and-desktop-changes-in-v2-1-260.md%0ACard%20ID%3A%20claude-code-2026-09-03-9ed8ec%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.260%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->