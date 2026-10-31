---
card_id: claude-code-2026-10-30-bdebb6
date: '2026-10-30'
description: 'Claude Code · 2026-10-30 · Safety and Privacy: 10 changes in v2.1.314
  — Added `permissions.blockWritesOutsideWorkingDirectories`: Write, Edit and NotebookEdit…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1293
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: edd4618bac4fc5987b4570a63de510cd1360c47552c22945b03ffda56597ed1f
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-30-bdebb6
  comparison: ''
  date: '2026-10-30'
  description: 'Claude Code — v2.1.314: 10 Safety and Privacy changes'
  evidence:
  - quote: 'Added `permissions.blockWritesOutsideWorkingDirectories`: Write, Edit
      and NotebookEdit refuse paths outside the working directories in every permission
      mode'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.314
  - quote: Fixed `claude ultrareview` and `claude remote-control` asking the workspace
      trust question in a CI job that has a terminal; with `CI` set they now refuse
      an untrusted folder at once
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.314
  - quote: Fixed a settings file excluded with `--setting-sources` still supplying
      some settings, such as auto mode rules and saved permission consents
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.314
  - quote: Fixed the session name from /rename disappearing while Claude asks for
      permission or a plan decision, so side-by-side sessions stay identifiable
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.314
  - quote: 'Improved permission prompts: a long reason takes fewer rows, so it pushes
      the command being approved off the screen on fewer terminals'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.314
  - quote: 'Improved session auto-titles: a session that starts with a skill or a
      prompt-based command such as `/security-review` now gets a title from it instead
      of staying untitled'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.314
  - quote: Changed `/ultrareview` to check workspace trust before it runs git, as
      `claude ultrareview` does
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.314
  - quote: 'Changed auto mode in Cowork cloud sessions: a hook''s allow of an MCP
      tool call now counts as no answer, so the classifier or a permission prompt
      decides'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.314
  - quote: '[Cloud sessions] Fixed the permission mode picker staying on Auto after
      a running cloud or Remote Control session refused the switch; it now shows the
      mode in use and tells you'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.314
  - quote: '[Remote Control] Fixed the permission mode button in Remote Control sessions
      showing the wrong mode until you typed; while your computer is online it now
      shows the real mode on open'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.314
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 10-safety-and-privacy-changes-in-v2-1-314
  source_release: claude-code-2026-10-30-v2-1-314-github-428518421-b7ac83d7
  source_type: github_releases
  theme: safety-privacy
  title: 10 Safety and Privacy changes in v2.1.314
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-26-changed-startup-warnings-about-permission-rules-in-settings-files-to-show-once-p|Changed
  startup warnings about permission rules in settings files to show once per…]]'
- '[[Changes/Claude Code/2026-10-27-changed-claude-code-to-stop-sending-the-claude-code-safety-event-opentelemetry-e|Changed
  Claude Code to stop sending the claude_code.safety_event OpenTelemetry event]]'
- '[[Changes/ChatGPT/2026-10-28-texting-your-dot-is-starting-to-roll-out-in-beta-to-pro-users-in-the-u-s|Texting
  your dot]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-30-v2-1-314-github-428518421-b7ac83d7|claude-code-2026-10-30-v2-1-314-github-428518421-b7ac83d7]]'
source_type: github_releases
theme: safety-privacy
title: 10 Safety and Privacy changes in v2.1.314
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Safety and Privacy changes in v2.1.314

**Claude Code** · 2026-10-30 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.314) · from [[Releases/Claude Code/claude-code-2026-10-30-v2-1-314-github-428518421-b7ac83d7|v2.1.314]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `permissions.blockWritesOutsideWorkingDirectories`: Write, Edit and NotebookEdit refuse paths outside the working directories in every permission mode

> Fixed `claude ultrareview` and `claude remote-control` asking the workspace trust question in a CI job that has a terminal; with `CI` set they now refuse an untrusted folder at once

> Fixed a settings file excluded with `--setting-sources` still supplying some settings, such as auto mode rules and saved permission consents

> Fixed the session name from /rename disappearing while Claude asks for permission or a plan decision, so side-by-side sessions stay identifiable

> Improved permission prompts: a long reason takes fewer rows, so it pushes the command being approved off the screen on fewer terminals

> Improved session auto-titles: a session that starts with a skill or a prompt-based command such as `/security-review` now gets a title from it instead of staying untitled

> Changed `/ultrareview` to check workspace trust before it runs git, as `claude ultrareview` does

> Changed auto mode in Cowork cloud sessions: a hook's allow of an MCP tool call now counts as no answer, so the classifier or a permission prompt decides

> [Cloud sessions] Fixed the permission mode picker staying on Auto after a running cloud or Remote Control session refused the switch; it now shows the mode in use and tells you

> [Remote Control] Fixed the permission mode button in Remote Control sessions showing the wrong mode until you typed; while your computer is online it now shows the real mode on open

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.314
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-30-3-agent-mode-changes-in-v2-1-314|3 Agent Mode changes in v2.1.314]] · Agent Mode
- [[Changes/Claude Code/2026-10-30-3-reliability-and-performance-changes-in-v2-1-314|3 Reliability and Performance changes in v2.1.314]] · Reliability and Performance
- [[Changes/Claude Code/2026-10-30-3-enterprise-and-administration-changes-in-v2-1-314|3 Enterprise and Administration changes in v2.1.314]] · Enterprise and Administration
- [[Changes/Claude Code/2026-10-30-4-developer-workflow-changes-in-v2-1-314|4 Developer Workflow changes in v2.1.314]] · Developer Workflow
- [[Changes/Claude Code/2026-10-30-2-model-support-changes-in-v2-1-314|2 Model Support changes in v2.1.314]] · Model Support
- [[Changes/Claude Code/2026-10-30-improved-the-cloud-session-error-shown-while-a-request-refused-for-your-claude-a|Improved the cloud session error shown while a request refused for your claude.ai…]] · Account and Access
- [[Changes/Claude Code/2026-10-30-3-apps-and-integrations-changes-in-v2-1-314|3 Apps and Integrations changes in v2.1.314]] · Apps and Integrations
- [[Changes/Claude Code/2026-10-30-2-mobile-and-desktop-changes-in-v2-1-314|2 Mobile and Desktop changes in v2.1.314]] · Mobile and Desktop
- [[Changes/Claude Code/2026-10-30-2-editor-experience-changes-in-v2-1-314|2 Editor Experience changes in v2.1.314]] · Editor Experience
- [[Changes/Claude Code/2026-10-30-10-other-changes-in-v2-1-314|10 other changes in v2.1.314]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-10-28 · ChatGPT · [[Changes/ChatGPT/2026-10-28-texting-your-dot-is-starting-to-roll-out-in-beta-to-pro-users-in-the-u-s|Texting your dot]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-30-bdebb6&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-30-10-safety-and-privacy-changes-in-v2-1-314.md%0ACard%20ID%3A%20claude-code-2026-10-30-bdebb6%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.314%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->