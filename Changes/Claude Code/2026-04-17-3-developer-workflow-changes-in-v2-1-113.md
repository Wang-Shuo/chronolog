---
card_id: claude-code-2026-04-17-273ed9
date: '2026-04-17'
description: 'Claude Code · 2026-04-17 · Developer Workflow: 3 changes in v2.1.113
  — Changed the CLI to spawn a native Claude Code binary (via a per-platform optional…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2775
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 3e676cbb0d96fbf9e92e7795366cb3c08c2f31f9ddb79d90e0f7d7ce06e1e631
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-04-17-273ed9
  comparison: ''
  date: '2026-04-17'
  description: 'Claude Code — v2.1.113: 3 Developer Workflow changes'
  evidence:
  - quote: Changed the CLI to spawn a native Claude Code binary (via a per-platform
      optional dependency) instead of bundled JavaScript
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.113
  - quote: Long URLs in responses and bash output stay clickable when they wrap across
      lines (in terminals with OSC 8 hyperlinks)
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.113
  - quote: 'Bash tool: multi-line commands whose first line is a comment now show
      the full command in the transcript, closing a UI-spoofing vector'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.113
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-developer-workflow-changes-in-v2-1-113
  source_release: claude-code-2026-04-17-v2-1-113-github-310525785-1b5293ba
  source_type: github_releases
  theme: developer-workflow
  title: 3 Developer Workflow changes in v2.1.113
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-04-16-support-copilot-disable-terminal-title-environment-variable-to-opt-out-of-termin|Support
  COPILOT_DISABLE_TERMINAL_TITLE environment variable to opt out of terminal…]]'
- '[[Changes/GitHub Copilot CLI/2026-04-16-undo-shows-an-explanatory-message-when-rewind-is-unavailable-e-g-not-in-a-git-re|/undo
  shows an explanatory message when rewind is unavailable…]]'
- '[[Changes/OpenCode/2026-04-16-3-developer-workflow-changes-in-v1-4-7|3 Developer
  Workflow changes in v1.4.7]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-17-v2-1-113-github-310525785-1b5293ba|claude-code-2026-04-17-v2-1-113-github-310525785-1b5293ba]]'
source_type: github_releases
theme: developer-workflow
title: 3 Developer Workflow changes in v2.1.113
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Developer Workflow changes in v2.1.113

**Claude Code** · 2026-04-17 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.113) · from [[Releases/Claude Code/claude-code-2026-04-17-v2-1-113-github-310525785-1b5293ba|v2.1.113]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Changed the CLI to spawn a native Claude Code binary (via a per-platform optional dependency) instead of bundled JavaScript

> Long URLs in responses and bash output stay clickable when they wrap across lines (in terminals with OSC 8 hyperlinks)

> Bash tool: multi-line commands whose first line is a comment now show the full command in the transcript, closing a UI-spoofing vector

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.113
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-04-17-remote-control-clients-can-now-query-file-autocomplete-suggestions|Remote Control clients can now query @-file autocomplete suggestions]] · Editor Experience
- [[Changes/Claude Code/2026-04-17-improved-loop-pressing-esc-now-cancels-pending-wakeups-and-wakeups-display-as-cl|Improved /loop: pressing Esc now cancels pending wakeups, and wakeups display…]] · Automation and Scheduling
- [[Changes/Claude Code/2026-04-17-3-interface-experience-changes-in-v2-1-113|3 Interface Experience changes in v2.1.113]] · Interface Experience
- [[Changes/Claude Code/2026-04-17-extra-usage-now-works-from-remote-control-mobile-web-clients|/extra-usage now works from Remote Control (mobile/web) clients]] · Mobile and Desktop
- [[Changes/Claude Code/2026-04-17-improved-ultrareview-faster-launch-with-parallelized-checks-diffstat-in-the-laun|Improved /ultrareview: faster launch with parallelized checks, diffstat…]] · Reliability and Performance
- [[Changes/Claude Code/2026-04-17-subagents-that-stall-mid-stream-now-fail-with-a-clear-error-after-10-minutes-ins|Subagents that stall mid-stream now fail with a clear error after 10 minutes instead…]] · Agent Mode
- [[Changes/Claude Code/2026-04-17-6-safety-and-privacy-changes-in-v2-1-113|6 Safety and Privacy changes in v2.1.113]] · Safety and Privacy
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-04-16 · OpenCode · [[Changes/OpenCode/2026-04-16-3-developer-workflow-changes-in-v1-4-7|3 Developer Workflow changes in v1.4.7]]
- Later: 2026-04-17 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-04-17-3-developer-workflow-changes-in-v1-0-32|3 Developer Workflow changes in v1.0.32]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-04-17-273ed9&body=Card%3A%20Changes%2FClaude%20Code%2F2026-04-17-3-developer-workflow-changes-in-v2-1-113.md%0ACard%20ID%3A%20claude-code-2026-04-17-273ed9%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.113%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->