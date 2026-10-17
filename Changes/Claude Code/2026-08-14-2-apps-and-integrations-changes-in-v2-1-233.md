---
card_id: claude-code-2026-08-14-e97c7a
date: '2026-08-14'
description: 'Claude Code · 2026-08-14 · Apps and Integrations: 2 changes in v2.1.233
  — Added an opt-in `forward_user_identity` apps gateway setting on Anthropic upstreams…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1240
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: e7995b2ffbbf60744661f8d8f5b190935892fd9e68f7ecf7c7aa7565ad9f0a75
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-08-14-e97c7a
  comparison: ''
  date: '2026-08-14'
  description: 'Claude Code — v2.1.233: 2 Apps and Integrations changes'
  evidence:
  - quote: Added an opt-in `forward_user_identity` apps gateway setting on Anthropic
      upstreams that sends the signed-in user's identity as headers, so a proxy behind
      the gateway can attribute spend per user
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.233
  - quote: Improved `claude plugin validate` to check a bare `.claude/skills` directory,
      reporting SKILL.md files whose frontmatter fails to parse
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.233
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-apps-and-integrations-changes-in-v2-1-233
  source_release: claude-code-2026-08-14-v2-1-233-github-370762090-de6823a9
  source_type: github_releases
  theme: apps-integrations
  title: 2 Apps and Integrations changes in v2.1.233
  type: change
related_changes:
- '[[Changes/Claude Code/2026-08-11-2-apps-and-integrations-changes-in-v2-1-228|2
  Apps and Integrations changes in v2.1.228]]'
- '[[Changes/Claude Code/2026-08-12-3-apps-and-integrations-changes-in-v2-1-229|3
  Apps and Integrations changes in v2.1.229]]'
- '[[Changes/Claude Code/2026-08-13-4-apps-and-integrations-changes-in-v2-1-232|4
  Apps and Integrations changes in v2.1.232]]'
source_release: '[[Releases/Claude Code/claude-code-2026-08-14-v2-1-233-github-370762090-de6823a9|claude-code-2026-08-14-v2-1-233-github-370762090-de6823a9]]'
source_type: github_releases
theme: apps-integrations
title: 2 Apps and Integrations changes in v2.1.233
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Apps and Integrations changes in v2.1.233

**Claude Code** · 2026-08-14 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.233) · from [[Releases/Claude Code/claude-code-2026-08-14-v2-1-233-github-370762090-de6823a9|v2.1.233]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added an opt-in `forward_user_identity` apps gateway setting on Anthropic upstreams that sends the signed-in user's identity as headers, so a proxy behind the gateway can attribute spend per user

> Improved `claude plugin validate` to check a bare `.claude/skills` directory, reporting SKILL.md files whose frontmatter fails to parse

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.233
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-08-14-3-safety-and-privacy-changes-in-v2-1-233|3 Safety and Privacy changes in v2.1.233]] · Safety and Privacy
- [[Changes/Claude Code/2026-08-14-improved-screen-reader-mode-the-effort-selector-renders-as-a-numbered-list-with|Improved screen reader mode]] · Accessibility and Localization
- [[Changes/Claude Code/2026-08-14-changed-the-github-app-setup-tip-to-no-longer-appear-in-repositories-whose-origi|Changed the GitHub app setup tip to no longer appear in repositories whose origin…]] · Enterprise and Administration
- [[Changes/Claude Code/2026-08-14-improved-apps-gateway-error-forwarding-400-413-errors-from-vertex-foundry-and-cl|Improved apps gateway error forwarding]] · Context Window
- [[Changes/Claude Code/2026-08-14-improved-claude-self-hosted-runner-session-start-time-the-session-branch-is-now|Improved claude self-hosted-runner session start time]] · Agent Mode
- [[Changes/Claude Code/2026-08-14-2-model-support-changes-in-v2-1-233|2 Model Support changes in v2.1.233]] · Model Support
- [[Changes/Claude Code/2026-08-14-added-opt-in-memory-cgroup-support-for-bash-tool-commands-on-linux-claude-code-t|Added opt-in memory cgroup support for Bash tool commands on Linux…]] · Memory and Personalization
- [[Changes/Claude Code/2026-08-14-added-gitlab-merge-request-url-support-to-the-worktree-flag-and-the-claude-agent|Added GitLab merge request URL support to the --worktree flag…]] · Developer Workflow
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-08-13 · Claude Code · [[Changes/Claude Code/2026-08-13-4-apps-and-integrations-changes-in-v2-1-232|4 Apps and Integrations changes in v2.1.232]]
- Later: 2026-08-17 · Claude Code · [[Changes/Claude Code/2026-08-17-2-apps-and-integrations-changes-in-v2-1-234|2 Apps and Integrations changes in v2.1.234]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-08-14-e97c7a&body=Card%3A%20Changes%2FClaude%20Code%2F2026-08-14-2-apps-and-integrations-changes-in-v2-1-233.md%0ACard%20ID%3A%20claude-code-2026-08-14-e97c7a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.233%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->