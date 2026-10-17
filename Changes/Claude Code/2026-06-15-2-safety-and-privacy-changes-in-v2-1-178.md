---
card_id: claude-code-2026-06-15-497841
date: '2026-06-15'
description: 'Claude Code · 2026-06-15 · Safety and Privacy: 2 changes in v2.1.178
  — Added `Tool(param:value)` syntax for permission rules to match a tool''s input
  parameters…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1156
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 238ffc6dc9a16321b4e4dae69b953b815404e82552e82c1d6b37c2627af611b1
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-06-15-497841
  comparison: ''
  date: '2026-06-15'
  description: 'Claude Code — v2.1.178: 2 Safety and Privacy changes'
  evidence:
  - quote: Added `Tool(param:value)` syntax for permission rules to match a tool's
      input parameters (with `*` wildcard), e.g. `Agent(model:opus)` to block Opus
      subagents
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.178
  - quote: Fixed nested `.claude/skills` skills with directory-qualified names being
      blocked by permission prompts in non-interactive runs
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.178
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-safety-and-privacy-changes-in-v2-1-178
  source_release: claude-code-2026-06-15-v2-1-178-github-339741361-902bc427
  source_type: github_releases
  theme: safety-privacy
  title: 2 Safety and Privacy changes in v2.1.178
  type: change
related_changes:
- '[[Changes/Claude Code/2026-06-08-2-safety-and-privacy-changes-in-v2-1-169|2 Safety
  and Privacy changes in v2.1.169]]'
- '[[Changes/Claude Code/2026-06-10-2-safety-and-privacy-changes-in-v2-1-172|2 Safety
  and Privacy changes in v2.1.172]]'
- '[[Changes/Cursor/2026-06-10-run-bugbot-before-you-push-3e5964|Run Bugbot before
  you push]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-15-v2-1-178-github-339741361-902bc427|claude-code-2026-06-15-v2-1-178-github-339741361-902bc427]]'
source_type: github_releases
theme: safety-privacy
title: 2 Safety and Privacy changes in v2.1.178
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Safety and Privacy changes in v2.1.178

**Claude Code** · 2026-06-15 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.178) · from [[Releases/Claude Code/claude-code-2026-06-15-v2-1-178-github-339741361-902bc427|v2.1.178]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `Tool(param:value)` syntax for permission rules to match a tool's input parameters (with `*` wildcard), e.g. `Agent(model:opus)` to block Opus subagents

> Fixed nested `.claude/skills` skills with directory-qualified names being blocked by permission prompts in non-interactive runs

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.178
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-06-15-bug-now-requires-a-description-before-submitting-and-no-longer-uses-model-refusa|/bug now requires a description before submitting, and no longer uses…]] · Model Support
- [[Changes/Claude Code/2026-06-15-2-agent-mode-changes-in-v2-1-178|2 Agent Mode changes in v2.1.178]] · Agent Mode
- [[Changes/Claude Code/2026-06-15-improved-doctor-with-consistent-flat-tree-layout-across-all-sections-clearer-sec|Improved /doctor with consistent flat tree layout across all sections, clearer…]] · Developer Workflow
- [[Changes/Claude Code/2026-06-15-2-apps-and-integrations-changes-in-v2-1-178|2 Apps and Integrations changes in v2.1.178]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-06-10 · Cursor · [[Changes/Cursor/2026-06-10-run-bugbot-before-you-push-3e5964|Run Bugbot before you push]]
- Later: 2026-06-17 · Claude Code · [[Changes/Claude Code/2026-06-17-added-sandbox-allowappleevents-opt-in-setting-that-lets-sandboxed-commands-send|Added sandbox.allowAppleEvents opt-in setting that lets sandboxed commands send…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-06-15-497841&body=Card%3A%20Changes%2FClaude%20Code%2F2026-06-15-2-safety-and-privacy-changes-in-v2-1-178.md%0ACard%20ID%3A%20claude-code-2026-06-15-497841%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.178%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->