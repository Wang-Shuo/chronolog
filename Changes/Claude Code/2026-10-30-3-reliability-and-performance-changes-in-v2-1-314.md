---
card_id: claude-code-2026-10-30-55bd53
date: '2026-10-30'
description: 'Claude Code · 2026-10-30 · Reliability and Performance: 3 changes in
  v2.1.314 — Improved memory use in long headless and SDK turns that run many subagents:
  the…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-11-19-opening-projects-is-now-much-faster|Opening
    Projects is now much faster]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2902
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 168f00256a949d926df57e9bde2131dd727b3d8f39cf36c4a110a459fce31e83
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-30-55bd53
  comparison: ''
  date: '2026-10-30'
  description: 'Claude Code — v2.1.314: 3 Reliability and Performance changes'
  evidence:
  - quote: 'Improved memory use in long headless and SDK turns that run many subagents:
      the parent session no longer keeps each subagent''s tool results until the turn
      ends'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.314
  - quote: Improved `--resume` speed and memory use on damaged transcripts
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.314
  - quote: 'macOS: Changed `git grep` in most commands that Claude runs to use the
      C locale, to avoid a reported memory leak in macOS''s regex library on files
      that aren''t valid UTF-8'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.314
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-reliability-and-performance-changes-in-v2-1-314
  source_release: claude-code-2026-10-30-v2-1-314-github-428518421-b7ac83d7
  source_type: github_releases
  theme: reliability-performance
  title: 3 Reliability and Performance changes in v2.1.314
  type: change
related_changes:
- '[[Changes/Open WebUI/2026-10-29-2-reliability-and-performance-changes-in-v0-12-5|2
  Reliability and Performance changes in v0.12.5]]'
- '[[Changes/OpenCode/2026-10-29-core-improve-snapshot-performance-by-coalescing-captures-and-avoiding-repeated-i|Core
  Improve snapshot performance by coalescing captures and avoiding repeated…]]'
- '[[Changes/Windsurf/2026-10-29-reduced-memory-usage-for-large-devin-local-sessions|Reduced
  memory usage for large Devin Local sessions]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-30-v2-1-314-github-428518421-b7ac83d7|claude-code-2026-10-30-v2-1-314-github-428518421-b7ac83d7]]'
source_type: github_releases
theme: reliability-performance
title: 3 Reliability and Performance changes in v2.1.314
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Reliability and Performance changes in v2.1.314

**Claude Code** · 2026-10-30 · [[Themes/reliability-performance|Reliability and Performance]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.314) · from [[Releases/Claude Code/claude-code-2026-10-30-v2-1-314-github-428518421-b7ac83d7|v2.1.314]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Improved memory use in long headless and SDK turns that run many subagents: the parent session no longer keeps each subagent's tool results until the turn ends

> Improved `--resume` speed and memory use on damaged transcripts

> macOS: Changed `git grep` in most commands that Claude runs to use the C locale, to avoid a reported memory leak in macOS's regex library on files that aren't valid UTF-8

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.314
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-30-3-agent-mode-changes-in-v2-1-314|3 Agent Mode changes in v2.1.314]] · Agent Mode
- [[Changes/Claude Code/2026-10-30-3-enterprise-and-administration-changes-in-v2-1-314|3 Enterprise and Administration changes in v2.1.314]] · Enterprise and Administration
- [[Changes/Claude Code/2026-10-30-4-developer-workflow-changes-in-v2-1-314|4 Developer Workflow changes in v2.1.314]] · Developer Workflow
- [[Changes/Claude Code/2026-10-30-2-model-support-changes-in-v2-1-314|2 Model Support changes in v2.1.314]] · Model Support
- [[Changes/Claude Code/2026-10-30-improved-the-cloud-session-error-shown-while-a-request-refused-for-your-claude-a|Improved the cloud session error shown while a request refused for your claude.ai…]] · Account and Access
- [[Changes/Claude Code/2026-10-30-3-apps-and-integrations-changes-in-v2-1-314|3 Apps and Integrations changes in v2.1.314]] · Apps and Integrations
- [[Changes/Claude Code/2026-10-30-10-safety-and-privacy-changes-in-v2-1-314|10 Safety and Privacy changes in v2.1.314]] · Safety and Privacy
- [[Changes/Claude Code/2026-10-30-2-mobile-and-desktop-changes-in-v2-1-314|2 Mobile and Desktop changes in v2.1.314]] · Mobile and Desktop
- [[Changes/Claude Code/2026-10-30-2-editor-experience-changes-in-v2-1-314|2 Editor Experience changes in v2.1.314]] · Editor Experience
- [[Changes/Claude Code/2026-10-30-10-other-changes-in-v2-1-314|10 other changes in v2.1.314]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2026-10-29 · Windsurf · [[Changes/Windsurf/2026-10-29-reduced-memory-usage-for-large-devin-local-sessions|Reduced memory usage for large Devin Local sessions]]
- Later: 2026-10-30 · OpenCode · [[Changes/OpenCode/2026-10-30-desktop-stability-fixes|Desktop Stability Fixes]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-11-19 · Descript · [[Changes/Descript/2018-11-19-opening-projects-is-now-much-faster|Opening Projects is now much faster]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-30-55bd53&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-30-3-reliability-and-performance-changes-in-v2-1-314.md%0ACard%20ID%3A%20claude-code-2026-10-30-55bd53%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.314%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->