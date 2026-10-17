---
card_id: claude-code-2026-05-19-555b83
date: '2026-05-19'
description: 'Claude Code · 2026-05-19 · Agent Mode: 3 changes in v2.1.144 — Added
  elapsed duration to background subagent completion notifications (e.g. "Agent completed…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1048
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 525b856851670586c58a1ba469094beaddd8ff152bc51f6c253549da71df63e8
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-05-19-555b83
  comparison: ''
  date: '2026-05-19'
  description: 'Claude Code — v2.1.144: 3 Agent Mode changes'
  evidence:
  - quote: Added elapsed duration to background subagent completion notifications
      (e.g. "Agent completed · 3h 2m 5s")
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.144
  - quote: '`claude agents` / `--bg` rejection messages now name the specific gate
      (non-TTY, env var, or setting) instead of a generic message'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.144
  - quote: '`claude agents`: renaming a background session with Ctrl+R now updates
      the attached session''s banner immediately'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.144
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-agent-mode-changes-in-v2-1-144
  source_release: claude-code-2026-05-19-v2-1-144-github-324524751-1469637a
  source_type: github_releases
  theme: agent-mode
  title: 3 Agent Mode changes in v2.1.144
  type: change
related_changes:
- '[[Changes/Claude Code/2026-05-15-2-agent-mode-changes-in-v2-1-143|2 Agent Mode
  changes in v2.1.143]]'
- '[[Changes/Cursor/2026-05-18-composer-2-5-is-now-available-in-cursor|Composer 2.5
  is now available in Cursor]]'
- '[[Changes/Claude Code/2026-05-19-added-resume-support-for-background-sessions-sessions-started-via-claude-bg-or-a|Added
  /resume support for background sessions]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-19-v2-1-144-github-324524751-1469637a|claude-code-2026-05-19-v2-1-144-github-324524751-1469637a]]'
source_type: github_releases
theme: agent-mode
title: 3 Agent Mode changes in v2.1.144
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Agent Mode changes in v2.1.144

**Claude Code** · 2026-05-19 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.144) · from [[Releases/Claude Code/claude-code-2026-05-19-v2-1-144-github-324524751-1469637a|v2.1.144]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added elapsed duration to background subagent completion notifications (e.g. "Agent completed · 3h 2m 5s")

> `claude agents` / `--bg` rejection messages now name the specific gate (non-TTY, env var, or setting) instead of a generic message

> `claude agents`: renaming a background session with Ctrl+R now updates the attached session's banner immediately

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.144
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-05-19-fewer-spurious-tool-errors-during-search-head-tail-file-views-now-satisfy-the-re|Fewer spurious tool errors during search]] · Editor Experience
- [[Changes/Claude Code/2026-05-19-the-plugin-browse-and-discover-panes-now-show-when-a-plugin-was-last-updated|The /plugin browse and discover panes now show when a plugin was last updated]] · Search and Browsing
- [[Changes/Claude Code/2026-05-19-resumed-sessions-now-keep-the-model-they-were-using-instead-of-picking-up-anothe|Resumed sessions now keep the model they were using instead of picking up another…]] · Model Support
- [[Changes/Claude Code/2026-05-19-added-resume-support-for-background-sessions-sessions-started-via-claude-bg-or-a|Added /resume support for background sessions]] · Agent Mode
- [[Changes/Claude Code/2026-05-19-renamed-extra-usage-to-usage-credits-across-cli-copy-extra-usage-is-now-usage-cr|Renamed "extra usage" to "usage credits" across CLI copy]] · Pricing Model
- [[Changes/Claude Code/2026-05-19-fixed-skill-tool-failing-with-permission-error-in-headless-mode-regression-in-v2|Fixed Skill tool failing with permission error in headless mode (regression in v2.1.141)]] · Safety and Privacy
- [[Changes/Claude Code/2026-05-19-3-developer-workflow-changes-in-v2-1-144|3 Developer Workflow changes in v2.1.144]] · Developer Workflow
- [[Changes/Claude Code/2026-05-19-3-apps-and-integrations-changes-in-v2-1-144|3 Apps and Integrations changes in v2.1.144]] · Apps and Integrations
- [[Changes/Claude Code/2026-05-19-model-now-changes-the-model-for-the-current-session-only-press-d-in-the-model-pi|/model now changes the model for the current session only]] · Interface Experience
- [[Changes/Claude Code/2026-05-19-the-post-survey-follow-up-hint-now-appears-after-every-non-dismiss-survey-respon|The post-survey follow-up hint now appears after every non-dismiss survey response…]] · Context Window
- [[Changes/Claude Code/2026-05-19-4-other-changes-in-v2-1-144|4 other changes in v2.1.144]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-05-18 · Cursor · [[Changes/Cursor/2026-05-18-composer-2-5-is-now-available-in-cursor|Composer 2.5 is now available in Cursor]]
- Later: 2026-05-19 · Claude Code · [[Changes/Claude Code/2026-05-19-3-agent-mode-changes-in-v2-1-145|3 Agent Mode changes in v2.1.145]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-05-19-555b83&body=Card%3A%20Changes%2FClaude%20Code%2F2026-05-19-3-agent-mode-changes-in-v2-1-144.md%0ACard%20ID%3A%20claude-code-2026-05-19-555b83%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.144%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->