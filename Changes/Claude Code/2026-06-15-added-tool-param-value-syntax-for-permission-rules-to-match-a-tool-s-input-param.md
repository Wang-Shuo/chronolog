---
card_id: claude-code-2026-06-15-47194d
date: '2026-06-15'
description: 'Claude Code · 2026-06-15 · Safety and Privacy: Added `Tool(param:value)`
  syntax for permission rules to match a tool''s input parameters (with `*` wildcard)…'
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
extractor_version: fallback-v4
impact: paradigm-shift
machine_hash: 452682eb0a3f8bc8613d5fe3bf40aeeb6704906c21870d449094b7b569edcbec
product: claude-code
product_name: Claude Code
record:
  ai_generated: true
  card_id: claude-code-2026-06-15-47194d
  comparison: ''
  confidence: low
  date: '2026-06-15'
  description: 'Claude Code — v2.1.178: Added `Tool(param:value)` syntax for permission
    rules to match a tool''s input parameters (with `*` wildcard), e.g. `Agent(model:opus)`
    to block Opus subagents'
  evidence:
  - quote: Added `Tool(param:value)` syntax for permission rules to match a tool's
      input parameters (with `*` wildcard), e.g. `Agent(model:opus)` to block Opus
      subagents
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.178
  extractor_version: fallback-v4
  impact: paradigm-shift
  product: claude-code
  product_name: Claude Code
  slug: added-tool-param-value-syntax-for-permission-rules-to-match-a-tool-s-input-param
  source_release: claude-code-2026-06-15-v2-1-178-github-339741361-902bc427
  source_type: github_releases
  theme: safety-privacy
  theme_matches:
  - matched_terms:
    - agent
    - subagents
    score: 100
    theme: agent-mode
  - matched_terms:
    - model
    - opus
    score: 100
    theme: model-support
  theme_resolution: manual-semantic-rule-v2
  title: Added `Tool(param:value)` syntax for permission rules to match a tool's input…
  type: change
related_changes:
- '[[Changes/Claude Code/2026-06-08-fixed-stale-permission-and-dialog-prompts-reappearing-every-time-you-reattached|Fixed
  stale permission and dialog prompts reappearing every time you reattached…]]'
- '[[Changes/Claude Code/2026-06-10-fixed-webfetch-domain-example-com-wildcard-domain-rules-never-matching-subdomain|Fixed
  WebFetch(domain:.example.com) wildcard domain rules never matching…]]'
- '[[Changes/Cursor/2026-06-10-you-can-now-run-bugbot-and-security-review-with-review-before-pushing-code-revie|Run
  Bugbot and Security Review with /review before pushing code]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-15-v2-1-178-github-339741361-902bc427|claude-code-2026-06-15-v2-1-178-github-339741361-902bc427]]'
source_type: github_releases
theme: safety-privacy
title: Added Tool(param:value) syntax for permission rules to match a tool's input…
type: change
---

<!-- chronolog:begin region="header" -->
# Added `Tool(param:value)` syntax for permission rules to match a tool's input…

**Claude Code** · 2026-06-15 · [[Themes/safety-privacy|Safety and Privacy]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.178) · from [[Releases/Claude Code/claude-code-2026-06-15-v2-1-178-github-339741361-902bc427|v2.1.178]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `Tool(param:value)` syntax for permission rules to match a tool's input parameters (with `*` wildcard), e.g. `Agent(model:opus)` to block Opus subagents
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.178
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-06-15-skills-in-nested-claude-skills-directories-now-load-when-working-on-files-there|Skills in nested .claude/skills directories now load when working on files there]] · Apps and Integrations
- [[Changes/Claude Code/2026-06-15-improved-auto-mode-subagent-spawns-are-now-evaluated-by-the-classifier-before-la|Improved auto mode]] · Agent Mode
- [[Changes/Claude Code/2026-06-15-improved-doctor-with-consistent-flat-tree-layout-across-all-sections-clearer-sec|Improved /doctor with consistent flat tree layout across all sections, clearer…]] · Developer Workflow
- [[Changes/Claude Code/2026-06-15-nested-claude-directories-the-agent-workflow-and-output-style-closest-to-the-wor|Nested .claude/ directories]] · Agent Mode
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-06-10 · Cursor · [[Changes/Cursor/2026-06-10-you-can-now-run-bugbot-and-security-review-with-review-before-pushing-code-revie|Run Bugbot and Security Review with /review before pushing code]]
- Later: 2026-06-17 · Claude Code · [[Changes/Claude Code/2026-06-17-added-sandbox-allowappleevents-opt-in-setting-that-lets-sandboxed-commands-send|Added sandbox.allowAppleEvents opt-in setting that lets sandboxed commands send…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-06-15-47194d&body=Card%3A%20Changes%2FClaude%20Code%2F2026-06-15-added-tool-param-value-syntax-for-permission-rules-to-match-a-tool-s-input-param.md%0ACard%20ID%3A%20claude-code-2026-06-15-47194d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.178%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->