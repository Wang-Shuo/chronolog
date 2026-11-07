---
card_id: claude-code-2026-06-15-4c3fca
date: '2026-06-15'
description: 'Claude Code · 2026-06-15 · Agent Mode: 2 changes in v2.1.178 — Nested
  `.claude/` directories: the agent, workflow, and output-style closest to the working…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1075
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: abfd319c55a662077f35b421481c4953f949f815d41affc0ef6e193e79cccb94
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-06-15-4c3fca
  comparison: ''
  date: '2026-06-15'
  description: 'Claude Code — v2.1.178: 2 Agent Mode changes'
  evidence:
  - quote: 'Nested `.claude/` directories: the agent, workflow, and output-style closest
      to the working directory now wins when names collide; project-scope workflow
      saves now target the closest existing `.claude/workflows/`'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.178
  - quote: 'Improved auto mode: subagent spawns are now evaluated by the classifier
      before launch, closing a gap where a subagent could request a blocked action
      without review'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.178
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-agent-mode-changes-in-v2-1-178
  source_release: claude-code-2026-06-15-v2-1-178-github-339741361-902bc427
  source_type: github_releases
  theme: agent-mode
  title: 2 Agent Mode changes in v2.1.178
  type: change
related_changes:
- '[[Changes/Replit/2026-06-12-customize-agent-with-workspace-instructions-and-skills|Customize
  Agent with workspace instructions and skills]]'
- '[[Changes/Replit/2026-06-12-agent|Agent]]'
- '[[Changes/GitHub Copilot CLI/2026-06-13-4-agent-mode-changes-in-v1-0-62|4 Agent
  Mode changes in v1.0.62]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-15-v2-1-178-github-339741361-902bc427|claude-code-2026-06-15-v2-1-178-github-339741361-902bc427]]'
source_type: github_releases
theme: agent-mode
title: 2 Agent Mode changes in v2.1.178
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Agent Mode changes in v2.1.178

**Claude Code** · 2026-06-15 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.178) · from [[Releases/Claude Code/claude-code-2026-06-15-v2-1-178-github-339741361-902bc427|v2.1.178]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Nested `.claude/` directories: the agent, workflow, and output-style closest to the working directory now wins when names collide; project-scope workflow saves now target the closest existing `.claude/workflows/`

> Improved auto mode: subagent spawns are now evaluated by the classifier before launch, closing a gap where a subagent could request a blocked action without review

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.178
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-06-15-bug-now-requires-a-description-before-submitting-and-no-longer-uses-model-refusa|/bug now requires a description before submitting, and no longer uses…]] · Model Support
- [[Changes/Claude Code/2026-06-15-2-safety-and-privacy-changes-in-v2-1-178|2 Safety and Privacy changes in v2.1.178]] · Safety and Privacy
- [[Changes/Claude Code/2026-06-15-improved-doctor-with-consistent-flat-tree-layout-across-all-sections-clearer-sec|Improved /doctor with consistent flat tree layout across all sections, clearer…]] · Developer Workflow
- [[Changes/Claude Code/2026-06-15-2-apps-and-integrations-changes-in-v2-1-178|2 Apps and Integrations changes in v2.1.178]] · Apps and Integrations
- [[Changes/Claude Code/2026-06-15-2-other-changes-in-v2-1-178|2 other changes in v2.1.178]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-06-13 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-06-13-4-agent-mode-changes-in-v1-0-62|4 Agent Mode changes in v1.0.62]]
- Later: 2026-06-15 · Codex CLI · [[Changes/Codex CLI/2026-06-15-11-agent-mode-changes-in-rust-v0-140-0|11 Agent Mode changes in rust-v0.140.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-06-15-4c3fca&body=Card%3A%20Changes%2FClaude%20Code%2F2026-06-15-2-agent-mode-changes-in-v2-1-178.md%0ACard%20ID%3A%20claude-code-2026-06-15-4c3fca%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.178%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->