---
card_id: claude-code-2026-02-24-30f423
date: '2026-02-24'
description: 'Claude Code · 2026-02-24 · Developer Workflow: BashTool now skips login
  shell (`-l` flag) by default when a shell snapshot is available, improving command…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1074
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: c558625798467e70cf5a68205562de1586a368b131ba8feb1e1d8b1c4aa8d8ec
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-02-24-30f423
  comparison: ''
  date: '2026-02-24'
  description: 'Claude Code — v2.1.51: BashTool now skips login shell (`-l` flag)
    by default when a shell snapshot is available, improving command execution performance.
    Previously this required setting `CLAUDE_BASH_NO_LOGIN=true`.'
  evidence:
  - quote: BashTool now skips login shell (`-l` flag) by default when a shell snapshot
      is available, improving command execution performance. Previously this required
      setting `CLAUDE_BASH_NO_LOGIN=true`.
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.51
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: claude-code
  product_name: Claude Code
  slug: bashtool-now-skips-login-shell-l-flag-by-default-when-a-shell-snapshot-is-availa
  source_release: claude-code-2026-02-24-v2-1-51-github-289665343-b4bbdd9c
  source_type: github_releases
  theme: developer-workflow
  theme_matches:
  - matched_terms:
    - login
    score: 50
    theme: account-access
  - matched_terms:
    - performance
    score: 50
    theme: reliability-performance
  theme_resolution: manual-backfill-review-v1
  title: BashTool now skips login shell (`-l` flag) by default when a shell snapshot…
  type: change
related_changes:
- '[[Changes/Cursor/2026-02-18-3-developer-workflow-changes-in-cli-improvements-and-mermaid-ascii|3
  Developer Workflow changes in CLI Improvements and Mermaid ASCII…]]'
- '[[Changes/ChatGPT/2026-02-19-review-code-in-split-screen-views|Review code in split-screen
  views]]'
- '[[Changes/Claude Code/2026-02-20-3-developer-workflow-changes-in-v2-1-50|3 Developer
  Workflow changes in v2.1.50]]'
source_release: '[[Releases/Claude Code/claude-code-2026-02-24-v2-1-51-github-289665343-b4bbdd9c|claude-code-2026-02-24-v2-1-51-github-289665343-b4bbdd9c]]'
source_type: github_releases
theme: developer-workflow
title: BashTool now skips login shell (-l flag) by default when a shell snapshot…
type: change
---

<!-- chronolog:begin region="header" -->
# BashTool now skips login shell (`-l` flag) by default when a shell snapshot…

**Claude Code** · 2026-02-24 · [[Themes/developer-workflow|Developer Workflow]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.51) · from [[Releases/Claude Code/claude-code-2026-02-24-v2-1-51-github-289665343-b4bbdd9c|v2.1.51]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> BashTool now skips login shell (`-l` flag) by default when a shell snapshot is available, improving command execution performance. Previously this required setting `CLAUDE_BASH_NO_LOGIN=true`.
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.51
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-02-24-3-safety-and-privacy-changes-in-v2-1-51|3 Safety and Privacy changes in v2.1.51]] · Safety and Privacy
- [[Changes/Claude Code/2026-02-24-4-apps-and-integrations-changes-in-v2-1-51|4 Apps and Integrations changes in v2.1.51]] · Apps and Integrations
- [[Changes/Claude Code/2026-02-24-tool-results-larger-than-50k-characters-are-now-persisted-to-disk-previously-100|Tool results larger than 50K characters are now persisted to disk (previously 100K)]] · Context Window
- [[Changes/Claude Code/2026-02-24-the-model-picker-now-shows-human-readable-labels-e-g-sonnet-4-5-instead-of-raw-m|The /model picker now shows human-readable labels (e.g., "Sonnet 4.5") instead…]] · Model Support
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-02-20 · Claude Code · [[Changes/Claude Code/2026-02-20-3-developer-workflow-changes-in-v2-1-50|3 Developer Workflow changes in v2.1.50]]
- Later: 2026-02-26 · Claude Code · [[Changes/Claude Code/2026-02-26-improved-always-allow-prefix-suggestions-for-compound-bash-commands-e-g-cd-tmp-g|Improved "always allow" prefix suggestions for compound bash commands…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-02-24-30f423&body=Card%3A%20Changes%2FClaude%20Code%2F2026-02-24-bashtool-now-skips-login-shell-l-flag-by-default-when-a-shell-snapshot-is-availa.md%0ACard%20ID%3A%20claude-code-2026-02-24-30f423%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.51%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->