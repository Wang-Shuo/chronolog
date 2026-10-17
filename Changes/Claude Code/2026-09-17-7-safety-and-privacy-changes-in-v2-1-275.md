---
card_id: claude-code-2026-09-17-964d22
date: '2026-09-17'
description: 'Claude Code · 2026-09-17 · Safety and Privacy: 7 changes in v2.1.275
  — Fixed `/update-config` writing `Write(path)` permission rules, which file permission…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1250
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 172f83b1cf58b8d9b95c989781d0362c0f2a1c9436c0ada1e63c2c04f35ddac3
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-17-964d22
  comparison: ''
  date: '2026-09-17'
  description: 'Claude Code — v2.1.275: 7 Safety and Privacy changes'
  evidence:
  - quote: Fixed `/update-config` writing `Write(path)` permission rules, which file
      permission checks don't match, instead of `Edit(path)` rules
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.275
  - quote: 'Improved pasted and attached images: they are now saved where Claude can
      open them as files without a permission prompt, including in Desktop and VS
      Code'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.275
  - quote: Changed hosted sessions to keep an unanswered permission prompt up after
      a container restart, instead of asking again
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.275
  - quote: Changed Claude in Chrome in auto mode to skip the extension's per-site
      check for classifier-approved calls, as bypass mode does, fixing `browser_batch`
      "Permission denied" after a redirect
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.275
  - quote: '[VSCode] Fixed the transcript creeping toward the bottom in small steps
      while a permission card waits and content keeps arriving'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.275
  - quote: '[VSCode] Fixed rewound and forked conversations not keeping the permission
      mode you had picked for the original conversation'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.275
  - quote: '[VSCode] Fixed unreadable code in the plan preview and the Hooks and Permission
      rules dialogs with the High Contrast Light theme'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.275
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 7-safety-and-privacy-changes-in-v2-1-275
  source_release: claude-code-2026-09-17-v2-1-275-github-391032307-12ccfafd
  source_type: github_releases
  theme: safety-privacy
  title: 7 Safety and Privacy changes in v2.1.275
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-09-14-if-you-make-no-changes-to-your-plugins-settings-the-default-permission-setting-i|If
  you make no changes to your Plugins settings, the default permission setting…]]'
- '[[Changes/Claude Code/2026-09-14-7-safety-and-privacy-changes-in-v2-1-271|7 Safety
  and Privacy changes in v2.1.271]]'
- '[[Changes/Claude Code/2026-09-15-5-safety-and-privacy-changes-in-v2-1-273|5 Safety
  and Privacy changes in v2.1.273]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-17-v2-1-275-github-391032307-12ccfafd|claude-code-2026-09-17-v2-1-275-github-391032307-12ccfafd]]'
source_type: github_releases
theme: safety-privacy
title: 7 Safety and Privacy changes in v2.1.275
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Safety and Privacy changes in v2.1.275

**Claude Code** · 2026-09-17 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.275) · from [[Releases/Claude Code/claude-code-2026-09-17-v2-1-275-github-391032307-12ccfafd|v2.1.275]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Fixed `/update-config` writing `Write(path)` permission rules, which file permission checks don't match, instead of `Edit(path)` rules

> Improved pasted and attached images: they are now saved where Claude can open them as files without a permission prompt, including in Desktop and VS Code

> Changed hosted sessions to keep an unanswered permission prompt up after a container restart, instead of asking again

> Changed Claude in Chrome in auto mode to skip the extension's per-site check for classifier-approved calls, as bypass mode does, fixing `browser_batch` "Permission denied" after a redirect

> [VSCode] Fixed the transcript creeping toward the bottom in small steps while a permission card waits and content keeps arriving

> [VSCode] Fixed rewound and forked conversations not keeping the permission mode you had picked for the original conversation

> [VSCode] Fixed unreadable code in the plan preview and the Hooks and Permission rules dialogs with the High Contrast Light theme

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.275
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-17-vscode-improved-the-agent-map-the-pill-counts-running-agents-and-turns-red-after|VSCode Improved the agent map]] · Agent Mode
- [[Changes/Claude Code/2026-09-17-6-apps-and-integrations-changes-in-v2-1-275|6 Apps and Integrations changes in v2.1.275]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-17-10-editor-experience-changes-in-v2-1-275|10 Editor Experience changes in v2.1.275]] · Editor Experience
- [[Changes/Claude Code/2026-09-17-vscode-added-viewing-editing-and-deleting-a-saved-memory-inside-the-memory-dialo|VSCode Added viewing, editing and deleting a saved memory inside the Memory dialog]] · Memory and Personalization
- [[Changes/Claude Code/2026-09-17-claude-tag-improved-claude-s-notices-in-enterprise-grid-channels-shared-across-w|Claude Tag Improved Claude's notices in Enterprise Grid channels shared across…]] · Enterprise and Administration
- [[Changes/Claude Code/2026-09-17-added-a-send-now-key-ctrl-enter-or-ctrl-x-ctrl-s-that-interrupts-the-current-tur|Added a send-now key (ctrl+enter, or ctrl+x ctrl+s) that interrupts the current turn…]] · Model Support
- [[Changes/Claude Code/2026-09-17-2-developer-workflow-changes-in-v2-1-275|2 Developer Workflow changes in v2.1.275]] · Developer Workflow
- [[Changes/Claude Code/2026-09-17-added-the-signed-in-account-to-claude-apps-gateway-sign-in-when-the-gateway-name|Added the signed-in account to Claude apps gateway sign-in]] · Account and Access
- [[Changes/Claude Code/2026-09-17-improved-the-desktop-error-when-claude-desktop-does-not-open-it-now-says-why-and|Improved the /desktop error when Claude Desktop does not open]] · Mobile and Desktop
- [[Changes/Claude Code/2026-09-17-improved-the-artifact-tool-s-publish-and-read-results-they-now-say-who-can-open|Improved the Artifact tool's publish and read results]] · Interface Experience
- [[Changes/Claude Code/2026-09-17-added-plugin-install-plugin-marketplace-source-which-offers-to-add-the-marketpla|Added /plugin install plugin --marketplace source, which offers to add…]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-17-6-other-changes-in-v2-1-275|6 other changes in v2.1.275]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-09-15 · Claude Code · [[Changes/Claude Code/2026-09-15-5-safety-and-privacy-changes-in-v2-1-273|5 Safety and Privacy changes in v2.1.273]]
- Later: 2026-09-17 · Claude Code · [[Changes/Claude Code/2026-09-17-3-safety-and-privacy-changes-in-v2-1-274|3 Safety and Privacy changes in v2.1.274]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-17-964d22&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-17-7-safety-and-privacy-changes-in-v2-1-275.md%0ACard%20ID%3A%20claude-code-2026-09-17-964d22%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.275%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->