---
card_id: claude-code-2026-09-14-9c4f61
date: '2026-09-14'
description: 'Claude Code · 2026-09-14 · Safety and Privacy: 7 changes in v2.1.271
  — Fixed Bash permission checks missing the file that `fmt`, `column` and similar
  commands…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1247
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 586103f55026c3d70ecd8ef6750d1a88a0a0667fdd11dc58bb1d9e1fac7a7708
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-14-9c4f61
  comparison: ''
  date: '2026-09-14'
  description: 'Claude Code — v2.1.271: 7 Safety and Privacy changes'
  evidence:
  - quote: Fixed Bash permission checks missing the file that `fmt`, `column` and
      similar commands read when it follows an option the checker doesn't recognize
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.271
  - quote: Fixed Bash permission checks skipping files a wildcard expands to when
      the wildcard sits in a command's pattern or option value (for example `grep
      -v dir/* file`)
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.271
  - quote: Fixed Bash permission checks so that shell variable declaration flags cannot
      misrepresent the command being run
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.271
  - quote: 'Fixed MCP OAuth mishandling client registrations: denying consent forced
      a new one, one for another redirect URI was reused, and a concurrent write could
      delete a valid one or keep a mismatched one'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.271
  - quote: 'Fixed cross-session messages held by the receiving session''s permission-mode
      policy leaving no trace: headless senders now get a delivery notice, and `SendMessage`
      results no longer imply it was read'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.271
  - quote: Changed auto mode so that a skill's or slash command's inline `!` shell
      commands follow default-mode permission rules instead of the classifier; a command
      no rule decides runs as a reviewed tool call
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.271
  - quote: '[VSCode] Fixed the Hooks and Permission rules dialogs reporting a save
      that landed as failed, and the Hooks dialog going blank under a plugin-only
      policy lock or showing color codes in save errors'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.271
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 7-safety-and-privacy-changes-in-v2-1-271
  source_release: claude-code-2026-09-14-v2-1-271-github-388664071-570fd44f
  source_type: github_releases
  theme: safety-privacy
  title: 7 Safety and Privacy changes in v2.1.271
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-11-5-safety-and-privacy-changes-in-v2-1-269|5 Safety
  and Privacy changes in v2.1.269]]'
- '[[Changes/Claude Code/2026-09-12-fixed-read-only-git-commands-in-bash-unexpectedly-asking-for-permission-after-a|Fixed
  read-only git commands in Bash unexpectedly asking for permission after…]]'
- '[[Changes/ChatGPT/2026-09-14-if-you-make-no-changes-to-your-plugins-settings-the-default-permission-setting-i|If
  you make no changes to your Plugins settings, the default permission setting…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-14-v2-1-271-github-388664071-570fd44f|claude-code-2026-09-14-v2-1-271-github-388664071-570fd44f]]'
source_type: github_releases
theme: safety-privacy
title: 7 Safety and Privacy changes in v2.1.271
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Safety and Privacy changes in v2.1.271

**Claude Code** · 2026-09-14 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.271) · from [[Releases/Claude Code/claude-code-2026-09-14-v2-1-271-github-388664071-570fd44f|v2.1.271]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Fixed Bash permission checks missing the file that `fmt`, `column` and similar commands read when it follows an option the checker doesn't recognize

> Fixed Bash permission checks skipping files a wildcard expands to when the wildcard sits in a command's pattern or option value (for example `grep -v dir/* file`)

> Fixed Bash permission checks so that shell variable declaration flags cannot misrepresent the command being run

> Fixed MCP OAuth mishandling client registrations: denying consent forced a new one, one for another redirect URI was reused, and a concurrent write could delete a valid one or keep a mismatched one

> Fixed cross-session messages held by the receiving session's permission-mode policy leaving no trace: headless senders now get a delivery notice, and `SendMessage` results no longer imply it was read

> Changed auto mode so that a skill's or slash command's inline `!` shell commands follow default-mode permission rules instead of the classifier; a command no rule decides runs as a reviewed tool call

> [VSCode] Fixed the Hooks and Permission rules dialogs reporting a save that landed as failed, and the Hooks dialog going blank under a plugin-only policy lock or showing color codes in save errors

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.271
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-14-changed-claude-apps-gateway-bedrock-vertex-ai-and-foundry-sessions-so-that-they|Changed Claude apps gateway, Bedrock, Vertex AI, and Foundry sessions so that they…]] · Account and Access
- [[Changes/Claude Code/2026-09-14-added-support-for-a-multiplier-above-1-up-to-10-in-the-modelpricing-managed-sett|Added support for a multiplier above 1, up to 10, in the modelPricing managed…]] · Pricing Model
- [[Changes/Claude Code/2026-09-14-2-files-and-data-changes-in-v2-1-271|2 Files and Data changes in v2.1.271]] · Files and Data
- [[Changes/Claude Code/2026-09-14-5-apps-and-integrations-changes-in-v2-1-271|5 Apps and Integrations changes in v2.1.271]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-14-3-editor-experience-changes-in-v2-1-271|3 Editor Experience changes in v2.1.271]] · Editor Experience
- [[Changes/Claude Code/2026-09-14-improved-the-spinner-status-during-long-thinking-it-now-reads-deep-in-thought-af|Improved the spinner status during long thinking]] · Context Window
- [[Changes/Claude Code/2026-09-14-7-agent-mode-changes-in-v2-1-271|7 Agent Mode changes in v2.1.271]] · Agent Mode
- [[Changes/Claude Code/2026-09-14-improved-terminal-rendering-performance-large-diffs-and-long-transcripts-render|Improved terminal rendering performance]] · Reliability and Performance
- [[Changes/Claude Code/2026-09-14-2-mobile-and-desktop-changes-in-v2-1-271|2 Mobile and Desktop changes in v2.1.271]] · Mobile and Desktop
- [[Changes/Claude Code/2026-09-14-3-interface-experience-changes-in-v2-1-271|3 Interface Experience changes in v2.1.271]] · Interface Experience
- [[Changes/Claude Code/2026-09-14-improved-startup-time-slightly-by-skipping-a-redundant-validation-of-built-in-mo|Improved startup time slightly by skipping a redundant validation of built-in model…]] · Model Support
- [[Changes/Claude Code/2026-09-14-9-other-changes-in-v2-1-271|9 other changes in v2.1.271]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-09-14 · ChatGPT · [[Changes/ChatGPT/2026-09-14-if-you-make-no-changes-to-your-plugins-settings-the-default-permission-setting-i|If you make no changes to your Plugins settings, the default permission setting…]]
- Later: 2026-09-15 · Claude Code · [[Changes/Claude Code/2026-09-15-5-safety-and-privacy-changes-in-v2-1-273|5 Safety and Privacy changes in v2.1.273]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-14-9c4f61&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-14-7-safety-and-privacy-changes-in-v2-1-271.md%0ACard%20ID%3A%20claude-code-2026-09-14-9c4f61%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.271%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->