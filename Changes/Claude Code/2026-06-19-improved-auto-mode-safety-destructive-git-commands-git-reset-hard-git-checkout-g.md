---
card_id: claude-code-2026-06-19-dbf355
date: '2026-06-19'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|cursor-2023-07-06-d7057e]]'
  lag_days: 1079
  role: follower
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-06-15-nested-claude-directories-the-agent-workflow-and-output-style-closest-to-the-wor|claude-code-2026-06-15-f824ca]]'
extractor_version: fallback-v2
impact: paradigm-shift
machine_hash: ca6b7b353601e9cd84ca802c75bc3f3f516be88262c6263ddf6dea47b3c82714
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-06-15-nested-claude-directories-the-agent-workflow-and-output-style-closest-to-the-wor|claude-code-2026-06-15-f824ca]]'
- '[[Changes/Cursor/2026-06-17-cloud-subagents-with-in-cloud|cursor-2026-06-17-4c6d0e]]'
- '[[Changes/Cursor/2026-06-17-cloud-environment-setup|cursor-2026-06-17-4e4899]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-19-v2-1-183-github-341696059-98586912|claude-code-2026-06-19-v2-1-183-github-341696059-98586912]]'
theme: agent-mode
type: change
---

# Improved auto mode safety: destructive git commands (`git reset --hard`, `git ch

<!-- chronolog:begin region="description" -->
Improved auto mode safety: destructive git commands (`git reset --hard`, `git checkout -- .`, `git clean -fd`, `git stash drop`) are now blocked when you didn't ask to discard local work, `git commit --amend` is blocked when the commit wasn't made by the agent this session, and `terraform destroy`/`pulumi destroy`/`cdk destroy` are blocked unless you asked for the specific stack
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Improved auto mode safety: destructive git commands (`git reset --hard`, `git checkout -- .`, `git clean -fd`, `git stash drop`) are now blocked when you didn't ask to discard local work, `git commit --amend` is blocked when the commit wasn't made by the agent this session, and `terraform destroy`/`pulumi destroy`/`cdk destroy` are blocked unless you asked for the specific stack
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.183
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-06-15-nested-claude-directories-the-agent-workflow-and-output-style-closest-to-the-wor|claude-code-2026-06-15-f824ca]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: agent-mode
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|cursor-2023-07-06-d7057e]]
- Lag Days: 1079
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes