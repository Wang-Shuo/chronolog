---
card_id: github-copilot-cli-2026-09-21-7336e8
date: '2026-09-21'
description: 'GitHub Copilot CLI · 2026-09-21 · Developer Workflow: 5 changes in 1.0.87
  — A `worktreePathTemplate` setting decides where `/worktree`, `/move`, `/new` and…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2932
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 5d3ae00b4c9c0a3431eaf33ecaddf4f1c3e4ab86b6ef55ef1fb5633517570e76
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-09-21-7336e8
  comparison: ''
  date: '2026-09-21'
  description: 'GitHub Copilot CLI — 1.0.87: 5 Developer Workflow changes'
  evidence:
  - quote: A `worktreePathTemplate` setting decides where `/worktree`, `/move`, `/new`
      and `--worktree` create worktrees. Set for example `~/src/worktrees/{repo}/{branch}`;
      `{repoPath}`, `{repo}`, `{branch}` and `{branchSlug}` are supported. Unset keeps
      the current layout, `<repo>.worktrees/` with slashes in the branch name flattened
      to dashes.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.87
  - quote: '`/keep-alive` (and `/caffeinate`) no longer reports that sleep is prevented
      when the sleep inhibitor exits immediately on startup instead of acquiring the
      lock (e.g. no session bus on WSL/containers/headless); it now reports the failure.'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.87
  - quote: Pull request badge and GitHub status tabs remain available after auth or
      branch refreshes
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.87
  - quote: Secrets exported in the launching shell are no longer written to debug
      logs when a session is created or resumed
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.87
  - quote: Reduce allocation overhead when repainting blank terminal areas.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.87
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 5-developer-workflow-changes-in-v1-0-87
  source_release: github-copilot-cli-2026-09-21-v1-0-87-github-393077593-9fe949ec
  source_type: github_releases
  theme: developer-workflow
  title: 5 Developer Workflow changes in v1.0.87
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-09-19-29-developer-workflow-changes-in-v2026-9-5|29 Developer
  Workflow changes in v2026.9.5]]'
- '[[Changes/Devin/2026-09-21-devin-review-for-bitbucket-data-center|Devin Review
  for Bitbucket Data Center]]'
- '[[Changes/Devin/2026-09-21-azure-devops-improvements|Azure DevOps Improvements]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-09-21-v1-0-87-github-393077593-9fe949ec|github-copilot-cli-2026-09-21-v1-0-87-github-393077593-9fe949ec]]'
source_type: github_releases
theme: developer-workflow
title: 5 Developer Workflow changes in v1.0.87
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Developer Workflow changes in v1.0.87

**GitHub Copilot CLI** · 2026-09-21 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.87) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-09-21-v1-0-87-github-393077593-9fe949ec|1.0.87]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> A `worktreePathTemplate` setting decides where `/worktree`, `/move`, `/new` and `--worktree` create worktrees. Set for example `~/src/worktrees/{repo}/{branch}`; `{repoPath}`, `{repo}`, `{branch}` and `{branchSlug}` are supported. Unset keeps the current layout, `<repo>.worktrees/` with slashes in the branch name flattened to dashes.

> `/keep-alive` (and `/caffeinate`) no longer reports that sleep is prevented when the sleep inhibitor exits immediately on startup instead of acquiring the lock (e.g. no session bus on WSL/containers/headless); it now reports the failure.

> Pull request badge and GitHub status tabs remain available after auth or branch refreshes

> Secrets exported in the launching shell are no longer written to debug logs when a session is created or resumed

> Reduce allocation overhead when repainting blank terminal areas.

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.87
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-09-21-tear-down-the-processes-an-internal-git-command-started-when-it-times-out-so-a-s|Tear down the processes an internal git command started when it times out, so a slow…]] · Memory and Personalization
- [[Changes/GitHub Copilot CLI/2026-09-21-consecutive-steering-prompts-in-the-same-mode-combine-into-one-pending-message-p|Consecutive steering prompts in the same mode combine into one pending message]] · Search and Browsing
- [[Changes/GitHub Copilot CLI/2026-09-21-show-live-elapsed-time-for-execution-subagents-in-timeline-entries|Show live elapsed time for execution subagents in timeline entries]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-09-21-8-apps-and-integrations-changes-in-v1-0-87|8 Apps and Integrations changes in v1.0.87]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-09-21-managed-plugin-commands-load-organization-marketplace-policy-with-environment-gi|Managed plugin commands load organization marketplace policy with environment…]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-09-21-enable-the-rubber-duck-agent-for-every-model-family-and-for-low-cost-tier-sessio|Enable the rubber-duck agent for every model family and for low-cost-tier session models]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-09-21-2-safety-and-privacy-changes-in-v1-0-87|2 Safety and Privacy changes in v1.0.87]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-09-21-number-key-selection-in-the-question-dialog-works-for-choices-10-and-beyond|Number-key selection in the question dialog works for choices 10 and beyond]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-09-21-4-other-changes-in-v1-0-87|4 other changes in v1.0.87]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-09-21 · Devin · [[Changes/Devin/2026-09-21-azure-devops-improvements|Azure DevOps Improvements]]
- Later: 2026-09-21 · Open WebUI · [[Changes/Open WebUI/2026-09-21-39-developer-workflow-changes-in-v0-11-4|39 Developer Workflow changes in v0.11.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-09-21-7336e8&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-09-21-5-developer-workflow-changes-in-v1-0-87.md%0ACard%20ID%3A%20github-copilot-cli-2026-09-21-7336e8%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.87%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->