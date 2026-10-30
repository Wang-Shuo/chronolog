---
card_id: claude-code-2026-10-23-5faf4b
date: '2026-10-23'
description: 'Claude Code · 2026-10-23 · Safety and Privacy: 4 changes in v2.1.310
  — Fixed file read permission prompts not showing where a symbolic link leads'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1286
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: af0b6aa0dc0e38870fda1634133a826382bb0c27f0742f01c26d2332e83695be
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-23-5faf4b
  comparison: ''
  date: '2026-10-23'
  description: 'Claude Code — v2.1.310: 4 Safety and Privacy changes'
  evidence:
  - quote: Fixed file read permission prompts not showing where a symbolic link leads
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.310
  - quote: 'Improved auto mode''s prompt before the first read outside the working
      directories: it now says when blocking those reads makes shell commands ask
      for permission'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.310
  - quote: 'Linux: Improved `/sandbox` and the sandbox startup warning to name Ubuntu''s
      AppArmor restriction on user namespaces, and how to lift it, when it keeps bubblewrap
      from starting the sandbox'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.310
  - quote: '[Cloud sessions] Changed turning on Cloud sessions or Remote Control in
      admin settings to ask for confirmation and list the custom roles that have that
      permission'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.310
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 4-safety-and-privacy-changes-in-v2-1-310
  source_release: claude-code-2026-10-23-v2-1-310-github-422315867-36b541d2
  source_type: github_releases
  theme: safety-privacy
  title: 4 Safety and Privacy changes in v2.1.310
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-20-3-safety-and-privacy-changes-in-v2-1-305|3 Safety
  and Privacy changes in v2.1.305]]'
- '[[Changes/Claude Code/2026-10-21-added-the-claude-code-safety-event-opentelemetry-event-for-each-tool-call-a-perm|Added
  the claude_code.safety_event OpenTelemetry event for each tool call…]]'
- '[[Changes/Claude Code/2026-10-22-8-safety-and-privacy-changes-in-v2-1-309|8 Safety
  and Privacy changes in v2.1.309]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-23-v2-1-310-github-422315867-36b541d2|claude-code-2026-10-23-v2-1-310-github-422315867-36b541d2]]'
source_type: github_releases
theme: safety-privacy
title: 4 Safety and Privacy changes in v2.1.310
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Safety and Privacy changes in v2.1.310

**Claude Code** · 2026-10-23 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.310) · from [[Releases/Claude Code/claude-code-2026-10-23-v2-1-310-github-422315867-36b541d2|v2.1.310]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Fixed file read permission prompts not showing where a symbolic link leads

> Improved auto mode's prompt before the first read outside the working directories: it now says when blocking those reads makes shell commands ask for permission

> Linux: Improved `/sandbox` and the sandbox startup warning to name Ubuntu's AppArmor restriction on user namespaces, and how to lift it, when it keeps bubblewrap from starting the sandbox

> [Cloud sessions] Changed turning on Cloud sessions or Remote Control in admin settings to ask for confirmation and list the custom roles that have that permission

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.310
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-23-2-agent-mode-changes-in-v2-1-310|2 Agent Mode changes in v2.1.310]] · Agent Mode
- [[Changes/Claude Code/2026-10-23-cloud-sessions-changed-the-cloud-environment-dialog-to-open-network-access-setup|Cloud sessions Changed the cloud environment dialog to open network access, setup…]] · Editor Experience
- [[Changes/Claude Code/2026-10-23-improved-memory-use-of-non-interactive-sessions-p-agent-sdk-during-compaction-wh|Improved memory use of non-interactive sessions (-p, Agent SDK) during compaction…]] · Memory and Personalization
- [[Changes/Claude Code/2026-10-23-cloud-sessions-added-claude-code-cloud-sessions-and-remote-control-permissions-t|Cloud sessions Added Claude Code cloud sessions and Remote Control permissions…]] · Enterprise and Administration
- [[Changes/Claude Code/2026-10-23-code-review-improved-the-code-review-admin-section-to-retry-the-first-load-and-s|Code Review Improved the Code Review admin section to retry the first load…]] · Developer Workflow
- [[Changes/Claude Code/2026-10-23-improved-a-mod-s-image-to-draw-inside-tmux-with-allow-passthrough-and-focus-even|Improved a mod's Image to draw inside tmux with allow-passthrough…]] · Interface Experience
- [[Changes/Claude Code/2026-10-23-2-apps-and-integrations-changes-in-v2-1-310|2 Apps and Integrations changes in v2.1.310]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-10-22 · Claude Code · [[Changes/Claude Code/2026-10-22-8-safety-and-privacy-changes-in-v2-1-309|8 Safety and Privacy changes in v2.1.309]]
- Later: 2026-10-26 · Claude Code · [[Changes/Claude Code/2026-10-26-changed-startup-warnings-about-permission-rules-in-settings-files-to-show-once-p|Changed startup warnings about permission rules in settings files to show once per…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-23-5faf4b&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-23-4-safety-and-privacy-changes-in-v2-1-310.md%0ACard%20ID%3A%20claude-code-2026-10-23-5faf4b%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.310%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->