---
card_id: claude-code-2026-09-22-271f3e
date: '2026-09-22'
description: 'Claude Code · 2026-09-22 · Apps and Integrations: 8 changes in v2.1.280
  — Added mouse support to more lists in fullscreen mode: the wheel scrolls the `/skills`…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2839
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b93a069463c2cf4343e6d10faf0d09ff299a5003643857c6db5e00470370dd59
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-22-271f3e
  comparison: ''
  date: '2026-09-22'
  description: 'Claude Code — v2.1.280: 8 Apps and Integrations changes'
  evidence:
  - quote: 'Added mouse support to more lists in fullscreen mode: the wheel scrolls
      the `/skills` list, and a skill''s state options in `/plugin` can be clicked'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.280
  - quote: Added `CLAUDE_CODE_MAX_MCP_DESCRIPTION_LENGTH` to change the 2,048-character
      cap on MCP tool descriptions and server instructions for every MCP server in
      the session
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.280
  - quote: 'Improved `/install-github-app`: the GitHub CLI check and repository selection
      steps now show "Esc to cancel"'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.280
  - quote: 'Improved `/plugin`''s Add Marketplace form in fullscreen: it no longer
      draws a box inside the pane, and its text and key hints line up with the rest
      of `/plugin`'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.280
  - quote: 'Self-hosted runner: Changed git in lifecycle hooks to ignore hook folders
      and programs named in the runner''s shared git files; local-path and `git://`
      remotes there now need `GIT_ALLOW_PROTOCOL`'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.280
  - quote: Changed plugin marketplaces whose name imitates a reserved marketplace
      name to be refused when added, and to stop loading if one was already added
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.280
  - quote: '[Claude Tag] Added Slack''s native Working indicator, Stop button and
      thread title to Claude''s threads in channels; the indicator stays up until
      Claude finishes, and Stop interrupts the task'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.280
  - quote: '[Claude Tag] Added a short notice in the Slack channel when a guest joining,
      or the last guest leaving, changes how Claude responds there under a Restrict
      or Channel only guest setting'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.280
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 8-apps-and-integrations-changes-in-v2-1-280
  source_release: claude-code-2026-09-22-v2-1-280-github-393879189-1cf5db2b
  source_type: github_releases
  theme: apps-integrations
  title: 8 Apps and Integrations changes in v2.1.280
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-09-21-sdk-releases|SDK releases]]'
- '[[Changes/GitHub Copilot CLI/2026-09-21-8-apps-and-integrations-changes-in-v1-0-87|8
  Apps and Integrations changes in v1.0.87]]'
- '[[Changes/Open WebUI/2026-09-21-3-apps-and-integrations-changes-in-v0-11-4|3 Apps
  and Integrations changes in v0.11.4]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-22-v2-1-280-github-393879189-1cf5db2b|claude-code-2026-09-22-v2-1-280-github-393879189-1cf5db2b]]'
source_type: github_releases
theme: apps-integrations
title: 8 Apps and Integrations changes in v2.1.280
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Apps and Integrations changes in v2.1.280

**Claude Code** · 2026-09-22 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.280) · from [[Releases/Claude Code/claude-code-2026-09-22-v2-1-280-github-393879189-1cf5db2b|v2.1.280]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added mouse support to more lists in fullscreen mode: the wheel scrolls the `/skills` list, and a skill's state options in `/plugin` can be clicked

> Added `CLAUDE_CODE_MAX_MCP_DESCRIPTION_LENGTH` to change the 2,048-character cap on MCP tool descriptions and server instructions for every MCP server in the session

> Improved `/install-github-app`: the GitHub CLI check and repository selection steps now show "Esc to cancel"

> Improved `/plugin`'s Add Marketplace form in fullscreen: it no longer draws a box inside the pane, and its text and key hints line up with the rest of `/plugin`

> Self-hosted runner: Changed git in lifecycle hooks to ignore hook folders and programs named in the runner's shared git files; local-path and `git://` remotes there now need `GIT_ALLOW_PROTOCOL`

> Changed plugin marketplaces whose name imitates a reserved marketplace name to be refused when added, and to stop loading if one was already added

> [Claude Tag] Added Slack's native Working indicator, Stop button and thread title to Claude's threads in channels; the indicator stays up until Claude finishes, and Stop interrupts the task

> [Claude Tag] Added a short notice in the Slack channel when a guest joining, or the last guest leaving, changes how Claude responds there under a Restrict or Channel only guest setting

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.280
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-22-improved-cost-cache-miss-causes-to-name-thinking-mode-and-thinking-display-chang|Improved /cost cache-miss causes to name thinking mode and thinking display changes]] · Pricing Model
- [[Changes/Claude Code/2026-09-22-2-agent-mode-changes-in-v2-1-280|2 Agent Mode changes in v2.1.280]] · Agent Mode
- [[Changes/Claude Code/2026-09-22-5-model-support-changes-in-v2-1-280|5 Model Support changes in v2.1.280]] · Model Support
- [[Changes/Claude Code/2026-09-22-2-safety-and-privacy-changes-in-v2-1-280|2 Safety and Privacy changes in v2.1.280]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-22-5-interface-experience-changes-in-v2-1-280|5 Interface Experience changes in v2.1.280]] · Interface Experience
- [[Changes/Claude Code/2026-09-22-claude-tag-improved-the-github-banner-in-claude-tag-admin-settings-to-say-why-gi|Claude Tag Improved the GitHub banner in Claude Tag admin settings to say why…]] · Account and Access
- [[Changes/Claude Code/2026-09-22-vscode-changed-open-in-new-tab-to-open-claude-beside-the-editor-group-you-are-wo|VSCode Changed "Open in New Tab" to open Claude beside the editor group you…]] · Editor Experience
- [[Changes/Claude Code/2026-09-22-3-developer-workflow-changes-in-v2-1-280|3 Developer Workflow changes in v2.1.280]] · Developer Workflow
- [[Changes/Claude Code/2026-09-22-17-other-changes-in-v2-1-280|17 other changes in v2.1.280]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-09-21 · Open WebUI · [[Changes/Open WebUI/2026-09-21-3-apps-and-integrations-changes-in-v0-11-4|3 Apps and Integrations changes in v0.11.4]]
- Later: 2026-09-22 · Codex CLI · [[Changes/Codex CLI/2026-09-22-42-apps-and-integrations-changes-in-rust-v0-156-0|42 Apps and Integrations changes in rust-v0.156.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-22-271f3e&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-22-8-apps-and-integrations-changes-in-v2-1-280.md%0ACard%20ID%3A%20claude-code-2026-09-22-271f3e%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.280%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->