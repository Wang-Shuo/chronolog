---
card_id: claude-code-2026-05-19-03fc6e
date: '2026-05-19'
description: 'Claude Code · 2026-05-19 · Editor Experience: Fewer spurious tool errors
  during search: `head`/`tail` file views now satisfy the read-before-edit check,
  and a…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3
    Editor Experience changes in 0.0.37]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1162
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: editor-experience
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: 31a426c4eb90a06495df030731f42d9c0aa9852727acb92c0eb10f4b702adc25
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-05-19-03fc6e
  comparison: ''
  date: '2026-05-19'
  description: 'Claude Code — v2.1.144: Fewer spurious tool errors during search:
    `head`/`tail` file views now satisfy the read-before-edit check, and a "no matches"
    result (exit code 1) from `egrep`, `fgrep`, `git grep`, or `git diff` is no longer
    reported as a command failure'
  evidence:
  - quote: 'Fewer spurious tool errors during search: `head`/`tail` file views now
      satisfy the read-before-edit check, and a "no matches" result (exit code 1)
      from `egrep`, `fgrep`, `git grep`, or `git diff` is no longer reported as a
      command failure'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.144
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: claude-code
  product_name: Claude Code
  slug: fewer-spurious-tool-errors-during-search-head-tail-file-views-now-satisfy-the-re
  source_release: claude-code-2026-05-19-v2-1-144-github-324524751-1469637a
  source_type: github_releases
  theme: editor-experience
  theme_matches: []
  theme_resolution: manual-semantic-rule-v1
  title: Fewer spurious tool errors during search
  type: change
related_changes:
- '[[Changes/v0/2026-05-15-reloading-the-preview-iframe-in-safari-shows-the-open-preview-in-new-tab-message|Reloading
  the preview iframe in Safari shows the "Open preview in new tab" message…]]'
- '[[Changes/Codex CLI/2026-05-18-21954-fix-goal-update-and-add-goal-edit-command-in-tui-etraut-openai|♯21954
  Fix goal update and add /goal edit command in TUI @etraut-openai]]'
- '[[Changes/Lovable/2026-05-18-seo-and-ai-search|SEO and AI search]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-19-v2-1-144-github-324524751-1469637a|claude-code-2026-05-19-v2-1-144-github-324524751-1469637a]]'
source_type: github_releases
theme: editor-experience
title: Fewer spurious tool errors during search
type: change
---

<!-- chronolog:begin region="header" -->
# Fewer spurious tool errors during search

**Claude Code** · 2026-05-19 · [[Themes/editor-experience|Editor Experience]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.144) · from [[Releases/Claude Code/claude-code-2026-05-19-v2-1-144-github-324524751-1469637a|v2.1.144]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Fewer spurious tool errors during search: `head`/`tail` file views now satisfy the read-before-edit check, and a "no matches" result (exit code 1) from `egrep`, `fgrep`, `git grep`, or `git diff` is no longer reported as a command failure
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.144
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-05-19-the-plugin-browse-and-discover-panes-now-show-when-a-plugin-was-last-updated|The /plugin browse and discover panes now show when a plugin was last updated]] · Search and Browsing
- [[Changes/Claude Code/2026-05-19-resumed-sessions-now-keep-the-model-they-were-using-instead-of-picking-up-anothe|Resumed sessions now keep the model they were using instead of picking up another…]] · Model Support
- [[Changes/Claude Code/2026-05-19-added-resume-support-for-background-sessions-sessions-started-via-claude-bg-or-a|Added /resume support for background sessions]] · Agent Mode
- [[Changes/Claude Code/2026-05-19-renamed-extra-usage-to-usage-credits-across-cli-copy-extra-usage-is-now-usage-cr|Renamed "extra usage" to "usage credits" across CLI copy]] · Pricing Model
- [[Changes/Claude Code/2026-05-19-fixed-skill-tool-failing-with-permission-error-in-headless-mode-regression-in-v2|Fixed Skill tool failing with permission error in headless mode (regression in v2.1.141)]] · Safety and Privacy
- [[Changes/Claude Code/2026-05-19-3-agent-mode-changes-in-v2-1-144|3 Agent Mode changes in v2.1.144]] · Agent Mode
- [[Changes/Claude Code/2026-05-19-3-developer-workflow-changes-in-v2-1-144|3 Developer Workflow changes in v2.1.144]] · Developer Workflow
- [[Changes/Claude Code/2026-05-19-3-apps-and-integrations-changes-in-v2-1-144|3 Apps and Integrations changes in v2.1.144]] · Apps and Integrations
- [[Changes/Claude Code/2026-05-19-model-now-changes-the-model-for-the-current-session-only-press-d-in-the-model-pi|/model now changes the model for the current session only]] · Interface Experience
- [[Changes/Claude Code/2026-05-19-the-post-survey-follow-up-hint-now-appears-after-every-non-dismiss-survey-respon|The post-survey follow-up hint now appears after every non-dismiss survey response…]] · Context Window
- [[Changes/Claude Code/2026-05-19-4-other-changes-in-v2-1-144|4 other changes in v2.1.144]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Editor Experience

- Earlier: 2026-05-18 · Lovable · [[Changes/Lovable/2026-05-18-seo-and-ai-search|SEO and AI search]]
- Later: 2026-05-19 · Dify · [[Changes/Dify/2026-05-19-feat-messagelogmodal-refactor-modal-structure-and-improve-tab-handling-by-coding|feat(MessageLogModal): refactor modal structure and improve tab handling]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-14 · Cursor · [[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3 Editor Experience changes in 0.0.37]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-05-19-03fc6e&body=Card%3A%20Changes%2FClaude%20Code%2F2026-05-19-fewer-spurious-tool-errors-during-search-head-tail-file-views-now-satisfy-the-re.md%0ACard%20ID%3A%20claude-code-2026-05-19-03fc6e%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.144%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->