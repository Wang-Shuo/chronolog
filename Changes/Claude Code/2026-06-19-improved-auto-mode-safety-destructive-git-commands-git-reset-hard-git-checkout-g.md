---
card_id: claude-code-2026-06-19-dbf355
date: '2026-06-19'
description: 'Claude Code · 2026-06-19 · Agent Mode: Improved auto mode safety: destructive
  git commands (`git reset --hard`, `git checkout -- .`, `git clean -fd`, `git…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Welcome
    to the first nightly release!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1079
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v4
impact: paradigm-shift
machine_hash: 113dc57dbb5bdcf728ca8f08d6f33489ba2db7ed3c33fd85b62c3de925ae4360
product: claude-code
product_name: Claude Code
record:
  ai_generated: true
  card_id: claude-code-2026-06-19-dbf355
  comparison: ''
  confidence: low
  date: '2026-06-19'
  description: 'Claude Code — v2.1.183: Improved auto mode safety: destructive git
    commands (`git reset --hard`, `git checkout -- .`, `git clean -fd`, `git stash
    drop`) are now blocked when you didn''t ask to discard local work, `git commit
    --amend` is blocked when the commit wasn''t made by the agent this session, and
    `terraform destroy`/`pulumi destroy`/`cdk destroy` are blocked unless you asked
    for the specific stack'
  evidence:
  - quote: 'Improved auto mode safety: destructive git commands (`git reset --hard`,
      `git checkout -- .`, `git clean -fd`, `git stash drop`) are now blocked when
      you didn''t ask to discard local work, `git commit --amend` is blocked when
      the commit wasn''t made by the agent this session, and `terraform destroy`/`pulumi
      destroy`/`cdk destroy` are blocked unless you asked for the specific stack'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.183
  extractor_version: fallback-v4
  impact: paradigm-shift
  product: claude-code
  product_name: Claude Code
  slug: improved-auto-mode-safety-destructive-git-commands-git-reset-hard-git-checkout-g
  source_release: claude-code-2026-06-19-v2-1-183-github-341696059-98586912
  source_type: github_releases
  theme: agent-mode
  theme_matches:
  - matched_terms:
    - agent
    - auto mode
    score: 110
    theme: agent-mode
  - matched_terms:
    - safety
    score: 50
    theme: safety-privacy
  title: Improved auto mode safety
  type: change
related_changes:
- '[[Changes/Claude Code/2026-06-15-improved-auto-mode-subagent-spawns-are-now-evaluated-by-the-classifier-before-la|Improved
  auto mode]]'
- '[[Changes/Claude Code/2026-06-15-nested-claude-directories-the-agent-workflow-and-output-style-closest-to-the-wor|Nested
  .claude/ directories]]'
- '[[Changes/Cursor/2026-06-17-use-in-cloud-to-spin-up-a-cloud-subagent-in-its-own-vm-to-work-on-the-next-task|Use
  /in-cloud to spin up a cloud subagent in its own VM to work on the next task you…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-19-v2-1-183-github-341696059-98586912|claude-code-2026-06-19-v2-1-183-github-341696059-98586912]]'
source_type: github_releases
theme: agent-mode
title: Improved auto mode safety
type: change
---

<!-- chronolog:begin region="header" -->
# Improved auto mode safety

**Claude Code** · 2026-06-19 · [[Themes/agent-mode|Agent Mode]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.183) · from [[Releases/Claude Code/claude-code-2026-06-19-v2-1-183-github-341696059-98586912|v2.1.183]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Improved auto mode safety: destructive git commands (`git reset --hard`, `git checkout -- .`, `git clean -fd`, `git stash drop`) are now blocked when you didn't ask to discard local work, `git commit --amend` is blocked when the commit wasn't made by the agent this session, and `terraform destroy`/`pulumi destroy`/`cdk destroy` are blocked unless you asked for the specific stack
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.183
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-06-19-added-config-help-to-list-all-available-shorthand-keys-for-config-key-value|Added /config --help to list all available shorthand keys for /config key=value]] · Interface Experience
- [[Changes/Claude Code/2026-06-19-added-a-warning-when-the-requested-model-is-deprecated-or-automatically-updated|Added a warning when the requested model is deprecated or automatically updated…]] · Model Support
- [[Changes/Claude Code/2026-06-19-added-attribution-sessionurl-setting-to-omit-the-claude-ai-session-link-from-com|Added attribution.sessionUrl setting to omit the claude.ai session link…]] · Apps and Integrations
- [[Changes/Claude Code/2026-06-19-changed-config-toggle-behavior-enter-and-space-both-change-the-selected-setting|Changed /config toggle behavior]] · Interface Experience
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-06-17 · Cursor · [[Changes/Cursor/2026-06-17-use-in-cloud-to-spin-up-a-cloud-subagent-in-its-own-vm-to-work-on-the-next-task|Use /in-cloud to spin up a cloud subagent in its own VM to work on the next task you…]]
- Later: 2026-06-22 · Claude Code · [[Changes/Claude Code/2026-06-22-added-teammatemode-iterm2-setting-with-a-warning-when-auto-mode-cannot-find-the|Added teammateMode: "iterm2" setting with a warning when auto mode cannot find…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Welcome to the first nightly release!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-06-19-dbf355&body=Card%3A%20Changes%2FClaude%20Code%2F2026-06-19-improved-auto-mode-safety-destructive-git-commands-git-reset-hard-git-checkout-g.md%0ACard%20ID%3A%20claude-code-2026-06-19-dbf355%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.183%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->