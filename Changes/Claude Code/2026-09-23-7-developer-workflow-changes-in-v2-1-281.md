---
card_id: claude-code-2026-09-23-485af9
date: '2026-09-23'
description: 'Claude Code · 2026-09-23 · Developer Workflow: 7 changes in v2.1.281
  — Added `"attribution": false` in `settings.json` to hide all commit and PR attribution…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1285
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 369a0de9f9a25cc454f35450c9e757d7d37fee3cbadb725b7a66dd07db7fbbe3
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-23-485af9
  comparison: ''
  date: '2026-09-23'
  description: 'Claude Code — v2.1.281: 7 Developer Workflow changes'
  evidence:
  - quote: 'Added `"attribution": false` in `settings.json` to hide all commit and
      PR attribution; older CLI versions skip a settings file that holds it, so keep
      the object form in files shared across versions'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
  - quote: Improved the dangerous-rm check to also flag a removal at a shell variable
      followed by a top-level directory name, at a variable derived from the working
      directory, or at a backslash-only target
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
  - quote: Improved debug logs to name settings `env` variables ignored because the
      session's launch environment already sets them
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
  - quote: 'Improved the Remote Control confirmation: its options are briefly inactive
      again after the terminal window regains focus, so a key pressed while switching
      back cannot answer it'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
  - quote: Changed self-hosted runners to pass system prompts to Claude Code as private
      files instead of command-line text, so large prompts no longer fail the launch;
      a wrapper or `command` hook that appends `--system-prompt` or `--append-system-prompt`
      must switch to `--system-prompt-file` or `--append-system-prompt-file`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
  - quote: 'Changed /workflows: each run''s row leads with its status icon and elapsed
      time, and a narrow terminal keeps the run''s name and time, dropping the agent
      and token counts first'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
  - quote: Removed the leftover "(removed)" `/agents` entry from the command menu
      and `/help`; typing `/agents` still explains where the wizard went
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 7-developer-workflow-changes-in-v2-1-281
  source_release: claude-code-2026-09-23-v2-1-281-github-394877414-9173ae95
  source_type: github_releases
  theme: developer-workflow
  title: 7 Developer Workflow changes in v2.1.281
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-17-2-developer-workflow-changes-in-v2-1-275|2 Developer
  Workflow changes in v2.1.275]]'
- '[[Changes/Claude Code/2026-09-18-improved-ultrareview-when-there-s-nothing-to-review-messages-say-which-case-you|Improved
  /ultrareview when there''s nothing to review]]'
- '[[Changes/Claude Code/2026-09-22-3-developer-workflow-changes-in-v2-1-280|3 Developer
  Workflow changes in v2.1.280]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-23-v2-1-281-github-394877414-9173ae95|claude-code-2026-09-23-v2-1-281-github-394877414-9173ae95]]'
source_type: github_releases
theme: developer-workflow
title: 7 Developer Workflow changes in v2.1.281
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Developer Workflow changes in v2.1.281

**Claude Code** · 2026-09-23 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.281) · from [[Releases/Claude Code/claude-code-2026-09-23-v2-1-281-github-394877414-9173ae95|v2.1.281]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `"attribution": false` in `settings.json` to hide all commit and PR attribution; older CLI versions skip a settings file that holds it, so keep the object form in files shared across versions

> Improved the dangerous-rm check to also flag a removal at a shell variable followed by a top-level directory name, at a variable derived from the working directory, or at a backslash-only target

> Improved debug logs to name settings `env` variables ignored because the session's launch environment already sets them

> Improved the Remote Control confirmation: its options are briefly inactive again after the terminal window regains focus, so a key pressed while switching back cannot answer it

> Changed self-hosted runners to pass system prompts to Claude Code as private files instead of command-line text, so large prompts no longer fail the launch; a wrapper or `command` hook that appends `--system-prompt` or `--append-system-prompt` must switch to `--system-prompt-file` or `--append-system-prompt-file`

> Changed /workflows: each run's row leads with its status icon and elapsed time, and a narrow terminal keeps the run's name and time, dropping the agent and token counts first

> Removed the leftover "(removed)" `/agents` entry from the command menu and `/help`; typing `/agents` still explains where the wizard went

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-23-10-agent-mode-changes-in-v2-1-281|10 Agent Mode changes in v2.1.281]] · Agent Mode
- [[Changes/Claude Code/2026-09-23-improved-interactive-startup-time-git-reads-startup-telemetry-and-the-bedrock-ve|Improved interactive startup time]] · Model Support
- [[Changes/Claude Code/2026-09-23-2-account-and-access-changes-in-v2-1-281|2 Account and Access changes in v2.1.281]] · Account and Access
- [[Changes/Claude Code/2026-09-23-claude-tag-changed-the-routine-list-claude-gives-when-asked-in-a-slack-thread-to|Claude Tag Changed the routine list Claude gives when asked in a Slack thread…]] · Automation and Scheduling
- [[Changes/Claude Code/2026-09-23-2-mobile-and-desktop-changes-in-v2-1-281|2 Mobile and Desktop changes in v2.1.281]] · Mobile and Desktop
- [[Changes/Claude Code/2026-09-23-4-interface-experience-changes-in-v2-1-281|4 Interface Experience changes in v2.1.281]] · Interface Experience
- [[Changes/Claude Code/2026-09-23-17-apps-and-integrations-changes-in-v2-1-281|17 Apps and Integrations changes in v2.1.281]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-23-improved-deep-research-reliability-on-long-research-briefs-by-removing-unused-re|Improved /deep-research reliability on long research briefs by removing unused…]] · Search and Browsing
- [[Changes/Claude Code/2026-09-23-12-safety-and-privacy-changes-in-v2-1-281|12 Safety and Privacy changes in v2.1.281]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-23-improved-screen-reader-output-in-mcp-a-disabled-server-is-read-as-off-instead-of|Improved screen-reader output in /mcp]] · Accessibility and Localization
- [[Changes/Claude Code/2026-09-23-13-other-changes-in-v2-1-281|13 other changes in v2.1.281]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-09-22 · Claude Code · [[Changes/Claude Code/2026-09-22-3-developer-workflow-changes-in-v2-1-280|3 Developer Workflow changes in v2.1.280]]
- Later: 2026-09-23 · Cursor · [[Changes/Cursor/2026-09-23-rollouts|Rollouts]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-23-485af9&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-23-7-developer-workflow-changes-in-v2-1-281.md%0ACard%20ID%3A%20claude-code-2026-09-23-485af9%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.281%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->