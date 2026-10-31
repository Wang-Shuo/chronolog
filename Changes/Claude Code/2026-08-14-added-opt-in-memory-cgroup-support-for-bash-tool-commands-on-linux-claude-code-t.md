---
card_id: claude-code-2026-08-14-c22adb
date: '2026-08-14'
description: 'Claude Code · 2026-08-14 · Reliability and Performance: Added opt-in
  memory cgroup support for Bash tool commands on Linux (`CLAUDE_CODE_TOOL_MEMORY_LIMIT`)
  so…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General
    performance: Among other improvements, users will notice that ChatGPT is now…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1338
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: change
machine_hash: 4fa75a5f0169ea030ba7bcdbc3cff4a32e702565af0c6ff7839f476d60d0ad8f
product: claude-code
product_name: Claude Code
record:
  ai_generated: true
  card_id: claude-code-2026-08-14-c22adb
  comparison: ''
  confidence: low
  date: '2026-08-14'
  description: 'Claude Code — v2.1.233: Added opt-in memory cgroup support for Bash
    tool commands on Linux (`CLAUDE_CODE_TOOL_MEMORY_LIMIT`) so a runaway build can''t
    stall the session'
  evidence:
  - quote: Added opt-in memory cgroup support for Bash tool commands on Linux (`CLAUDE_CODE_TOOL_MEMORY_LIMIT`)
      so a runaway build can't stall the session
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.233
  extractor_version: fallback-v5
  impact: significant
  kind: change
  product: claude-code
  product_name: Claude Code
  slug: added-opt-in-memory-cgroup-support-for-bash-tool-commands-on-linux-claude-code-t
  source_release: claude-code-2026-08-14-v2-1-233-github-370762090-de6823a9
  source_type: github_releases
  theme: reliability-performance
  theme_matches: []
  theme_resolution: manual-semantic-rule-v2
  title: Added opt-in memory cgroup support for Bash tool commands on Linux…
  type: change
related_changes:
- '[[Changes/Claude Code/2026-07-21-added-warnings-when-transcript-writes-are-failing-e-g-disk-full-or-when-session|Added
  warnings when transcript writes are failing (e.g. disk full) or when session…]]'
- '[[Changes/Claude Code/2026-08-10-improved-performance-fewer-event-loop-stalls-on-file-not-found-suggestions-and-a|Improved
  performance: fewer event-loop stalls on file-not-found suggestions…]]'
- '[[Changes/Cursor/2026-08-13-faster-starts|Faster starts]]'
source_release: '[[Releases/Claude Code/claude-code-2026-08-14-v2-1-233-github-370762090-de6823a9|claude-code-2026-08-14-v2-1-233-github-370762090-de6823a9]]'
source_type: github_releases
theme: reliability-performance
title: Added opt-in memory cgroup support for Bash tool commands on Linux…
type: change
---

<!-- chronolog:begin region="header" -->
# Added opt-in memory cgroup support for Bash tool commands on Linux…

**Claude Code** · 2026-08-14 · [[Themes/reliability-performance|Reliability and Performance]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.233) · from [[Releases/Claude Code/claude-code-2026-08-14-v2-1-233-github-370762090-de6823a9|v2.1.233]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added opt-in memory cgroup support for Bash tool commands on Linux (`CLAUDE_CODE_TOOL_MEMORY_LIMIT`) so a runaway build can't stall the session
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.233
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-08-14-3-safety-and-privacy-changes-in-v2-1-233|3 Safety and Privacy changes in v2.1.233]] · Safety and Privacy
- [[Changes/Claude Code/2026-08-14-improved-screen-reader-mode-the-effort-selector-renders-as-a-numbered-list-with|Improved screen reader mode]] · Accessibility and Localization
- [[Changes/Claude Code/2026-08-14-changed-the-github-app-setup-tip-to-no-longer-appear-in-repositories-whose-origi|Changed the GitHub app setup tip to no longer appear in repositories whose origin…]] · Enterprise and Administration
- [[Changes/Claude Code/2026-08-14-improved-apps-gateway-error-forwarding-400-413-errors-from-vertex-foundry-and-cl|Improved apps gateway error forwarding]] · Context Window
- [[Changes/Claude Code/2026-08-14-improved-claude-self-hosted-runner-session-start-time-the-session-branch-is-now|Improved claude self-hosted-runner session start time]] · Agent Mode
- [[Changes/Claude Code/2026-08-14-2-model-support-changes-in-v2-1-233|2 Model Support changes in v2.1.233]] · Model Support
- [[Changes/Claude Code/2026-08-14-added-gitlab-merge-request-url-support-to-the-worktree-flag-and-the-claude-agent|Added GitLab merge request URL support to the --worktree flag…]] · Developer Workflow
- [[Changes/Claude Code/2026-08-14-2-apps-and-integrations-changes-in-v2-1-233|2 Apps and Integrations changes in v2.1.233]] · Apps and Integrations
- [[Changes/Claude Code/2026-08-14-added-claude-code-webfetch-cache-ttl-ms-environment-variable-to-configure-the-we|Added CLAUDE_CODE_WEBFETCH_CACHE_TTL_MS environment variable to configure…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2026-08-13 · Cursor · [[Changes/Cursor/2026-08-13-faster-starts|Faster starts]]
- Later: 2026-08-18 · Claude Code · [[Changes/Claude Code/2026-08-18-2-reliability-and-performance-changes-in-v2-1-235|2 Reliability and Performance changes in v2.1.235]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General performance: Among other improvements, users will notice that ChatGPT is now…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-08-14-c22adb&body=Card%3A%20Changes%2FClaude%20Code%2F2026-08-14-added-opt-in-memory-cgroup-support-for-bash-tool-commands-on-linux-claude-code-t.md%0ACard%20ID%3A%20claude-code-2026-08-14-c22adb%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.233%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->