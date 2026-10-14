---
card_id: claude-code-2026-06-19-dbf355
date: '2026-06-19'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|cursor-2023-07-06-d7057e]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1079
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v3
impact: paradigm-shift
machine_hash: ab21de41ff2a45b46dacd24f63445f3fd4cd1812f0e95fa5bfbedb19eb7e5581
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
  extractor_version: fallback-v3
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
  title: 'Improved auto mode safety: destructive git commands (`git reset --hard`,
    `git ch'
  type: change
related_changes:
- '[[Changes/Claude Code/2026-06-15-improved-auto-mode-subagent-spawns-are-now-evaluated-by-the-classifier-before-la|claude-code-2026-06-15-1d14c3]]'
- '[[Changes/Claude Code/2026-06-15-nested-claude-directories-the-agent-workflow-and-output-style-closest-to-the-wor|claude-code-2026-06-15-f824ca]]'
- '[[Changes/Cursor/2026-06-17-use-in-cloud-to-spin-up-a-cloud-subagent-in-its-own-vm-to-work-on-the-next-task|cursor-2026-06-17-cd2290]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-19-v2-1-183-github-341696059-98586912|claude-code-2026-06-19-v2-1-183-github-341696059-98586912]]'
source_type: github_releases
theme: agent-mode
title: 'Improved auto mode safety: destructive git commands (git reset --hard, git
  ch'
type: change
---

# Improved auto mode safety: destructive git commands (`git reset --hard`, `git ch

<!-- chronolog:begin region="description" -->
Claude Code — v2.1.183: Improved auto mode safety: destructive git commands (`git reset --hard`, `git checkout -- .`, `git clean -fd`, `git stash drop`) are now blocked when you didn't ask to discard local work, `git commit --amend` is blocked when the commit wasn't made by the agent this session, and `terraform destroy`/`pulumi destroy`/`cdk destroy` are blocked unless you asked for the specific stack
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Improved auto mode safety: destructive git commands (`git reset --hard`, `git checkout -- .`, `git clean -fd`, `git stash drop`) are now blocked when you didn't ask to discard local work, `git commit --amend` is blocked when the commit wasn't made by the agent this session, and `terraform destroy`/`pulumi destroy`/`cdk destroy` are blocked unless you asked for the specific stack
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.183
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
No evidence-backed evolution relationship assigned.
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: agent-mode
- Relation: same-theme-chronology
- Inference: No adoption, equivalence, or causation claim.
- Scope: tracked-products-only
- Role: later-observed
- First In Tracked: [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|cursor-2023-07-06-d7057e]]
- Lag Days: 1079
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes