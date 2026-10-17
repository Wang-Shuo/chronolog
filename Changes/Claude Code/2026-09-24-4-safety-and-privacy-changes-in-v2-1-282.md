---
card_id: claude-code-2026-09-24-baf1e4
date: '2026-09-24'
description: 'Claude Code · 2026-09-24 · Safety and Privacy: 4 changes in v2.1.282
  — Fixed Bash permission rules with a mid-pattern `:*` being skipped in settings
  files…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1257
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 79ab02042b049f4ca9cb533debbf3cef78737e795b44010f94aed667bc1a4244
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-24-baf1e4
  comparison: ''
  date: '2026-09-24'
  description: 'Claude Code — v2.1.282: 4 Safety and Privacy changes'
  evidence:
  - quote: Fixed Bash permission rules with a mid-pattern `:*` being skipped in settings
      files while `--allowedTools` honored them; they now work from every source,
      with a startup warning on how they match
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.282
  - quote: Fixed a command approved on a restored permission prompt running twice
      when a remote session's worker restarted
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.282
  - quote: Improved rendering of unusual Unicode in permission prompts
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.282
  - quote: 'Changed `sandbox.excludedCommands` to ignore project and local settings
      entries when managed settings or `--settings` set `allowUnsandboxedCommands:
      false`, or managed `allowManagedDomainsOnly: true`'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.282
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 4-safety-and-privacy-changes-in-v2-1-282
  source_release: claude-code-2026-09-24-v2-1-282-github-395840120-957e42c4
  source_type: github_releases
  theme: safety-privacy
  title: 4 Safety and Privacy changes in v2.1.282
  type: change
related_changes:
- '[[Changes/Cursor/2026-09-23-today-we-re-launching-two-cursor-bots-for-the-last-mile-of-shipping-code-rollout-af394f|Cursor
  launches two Cursor bots for the last mile of shipping code]]'
- '[[Changes/Cursor/2026-09-23-security-review|Security Review]]'
- '[[Changes/Cursor/2026-09-23-findings|Findings]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-24-v2-1-282-github-395840120-957e42c4|claude-code-2026-09-24-v2-1-282-github-395840120-957e42c4]]'
source_type: github_releases
theme: safety-privacy
title: 4 Safety and Privacy changes in v2.1.282
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Safety and Privacy changes in v2.1.282

**Claude Code** · 2026-09-24 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.282) · from [[Releases/Claude Code/claude-code-2026-09-24-v2-1-282-github-395840120-957e42c4|v2.1.282]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Fixed Bash permission rules with a mid-pattern `:*` being skipped in settings files while `--allowedTools` honored them; they now work from every source, with a startup warning on how they match

> Fixed a command approved on a restored permission prompt running twice when a remote session's worker restarted

> Improved rendering of unusual Unicode in permission prompts

> Changed `sandbox.excludedCommands` to ignore project and local settings entries when managed settings or `--settings` set `allowUnsandboxedCommands: false`, or managed `allowManagedDomainsOnly: true`

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.282
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-24-claude-tag-changed-newly-connected-slack-workspaces-to-follow-the-current-defaul|Claude Tag Changed newly connected Slack workspaces to follow the current default…]] · Model Support
- [[Changes/Claude Code/2026-09-24-2-mobile-and-desktop-changes-in-v2-1-282|2 Mobile and Desktop changes in v2.1.282]] · Mobile and Desktop
- [[Changes/Claude Code/2026-09-24-4-interface-experience-changes-in-v2-1-282|4 Interface Experience changes in v2.1.282]] · Interface Experience
- [[Changes/Claude Code/2026-09-24-updated-the-claude-api-skill-pre-output-refusal-billing-now-links-to-the-how-ref|Updated the claude-api skill]] · Pricing Model
- [[Changes/Claude Code/2026-09-24-changed-windows-wsl-managed-settings-so-an-admin-policy-that-is-present-but-inva|Changed Windows/WSL managed settings so an admin policy that is present but invalid…]] · Developer Workflow
- [[Changes/Claude Code/2026-09-24-2-agent-mode-changes-in-v2-1-282|2 Agent Mode changes in v2.1.282]] · Agent Mode
- [[Changes/Claude Code/2026-09-24-8-apps-and-integrations-changes-in-v2-1-282|8 Apps and Integrations changes in v2.1.282]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-09-23 · Cursor · [[Changes/Cursor/2026-09-23-findings|Findings]]
- Later: 2026-09-25 · ChatGPT · [[Changes/ChatGPT/2026-09-25-we-re-introducing-security-history-a-new-way-to-review-recent-security-activity-6f32cc|Security history in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-24-baf1e4&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-24-4-safety-and-privacy-changes-in-v2-1-282.md%0ACard%20ID%3A%20claude-code-2026-09-24-baf1e4%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.282%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->