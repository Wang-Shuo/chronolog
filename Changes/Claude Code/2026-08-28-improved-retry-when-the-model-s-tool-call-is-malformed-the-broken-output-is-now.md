---
card_id: claude-code-2026-08-28-bb3dfd
date: '2026-08-28'
description: 'Claude Code · 2026-08-28 · Context Window: Improved retry when the model''s
  tool call is malformed: the broken output is now dropped from the retry context…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2
    Context Window changes in 0.2.9]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1212
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: change
machine_hash: 2171db3181ab6a7aaf8b1d729031d9938b6a4a53658357bbc9012df20477af39
product: claude-code
product_name: Claude Code
record:
  ai_generated: true
  card_id: claude-code-2026-08-28-bb3dfd
  comparison: ''
  confidence: low
  date: '2026-08-28'
  description: 'Claude Code — v2.1.251: Improved retry when the model''s tool call
    is malformed: the broken output is now dropped from the retry context, including
    on Bedrock, Vertex, and Foundry'
  evidence:
  - quote: 'Improved retry when the model''s tool call is malformed: the broken output
      is now dropped from the retry context, including on Bedrock, Vertex, and Foundry'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.251
  extractor_version: fallback-v5
  impact: significant
  kind: change
  product: claude-code
  product_name: Claude Code
  slug: improved-retry-when-the-model-s-tool-call-is-malformed-the-broken-output-is-now
  source_release: claude-code-2026-08-28-v2-1-251-github-378586104-42ac2f96
  source_type: github_releases
  theme: context-window
  theme_matches:
  - matched_terms:
    - context
    score: 50
    theme: context-window
  - matched_terms:
    - model
    score: 50
    theme: model-support
  theme_resolution: manual-semantic-rule-v1
  title: Improved retry when the model's tool call is malformed
  type: change
related_changes:
- '[[Changes/Claude Code/2026-08-21-improved-the-reminder-shown-after-compaction-so-a-skill-s-original-arguments-are|Improved
  the reminder shown after compaction so a skill''s original arguments are not…]]'
- '[[Changes/Claude Code/2026-08-26-changed-sonnet-5-s-default-auto-compact-window-to-its-full-1m-context-so-session|Changed
  Sonnet 5''s default auto-compact window to its full 1M context, so sessions…]]'
- '[[Changes/Claude Code/2026-08-27-improved-the-workflow-tool-s-prompt-footprint-its-description-is-now-about-1k-to|Improved
  the Workflow tool''s prompt footprint]]'
source_release: '[[Releases/Claude Code/claude-code-2026-08-28-v2-1-251-github-378586104-42ac2f96|claude-code-2026-08-28-v2-1-251-github-378586104-42ac2f96]]'
source_type: github_releases
theme: context-window
title: Improved retry when the model's tool call is malformed
type: change
---

<!-- chronolog:begin region="header" -->
# Improved retry when the model's tool call is malformed

**Claude Code** · 2026-08-28 · [[Themes/context-window|Context Window]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.251) · from [[Releases/Claude Code/claude-code-2026-08-28-v2-1-251-github-378586104-42ac2f96|v2.1.251]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Improved retry when the model's tool call is malformed: the broken output is now dropped from the retry context, including on Bedrock, Vertex, and Foundry
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.251
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-08-28-changed-analytics-to-no-longer-turn-off-before-sign-in-solely-because-managed-se|Changed analytics to no longer turn off before sign-in solely because managed…]] · Account and Access
- [[Changes/Claude Code/2026-08-28-added-a-per-session-prompt-cache-line-to-cost-hit-ratio-misses-tokens-re-cached|Added a per-session prompt-cache line to /cost…]] · Pricing Model
- [[Changes/Claude Code/2026-08-28-4-apps-and-integrations-changes-in-v2-1-251|4 Apps and Integrations changes in v2.1.251]] · Apps and Integrations
- [[Changes/Claude Code/2026-08-28-3-developer-workflow-changes-in-v2-1-251|3 Developer Workflow changes in v2.1.251]] · Developer Workflow
- [[Changes/Claude Code/2026-08-28-4-agent-mode-changes-in-v2-1-251|4 Agent Mode changes in v2.1.251]] · Agent Mode
- [[Changes/Claude Code/2026-08-28-added-a-spend-limit-bar-to-usage-and-a-rate-limits-spend-limit-status-line-field|Added a Spend limit bar to /usage and a rate_limits.spend_limit status line…]] · Interface Experience
- [[Changes/Claude Code/2026-08-28-5-model-support-changes-in-v2-1-251|5 Model Support changes in v2.1.251]] · Model Support
- [[Changes/Claude Code/2026-08-28-6-safety-and-privacy-changes-in-v2-1-251|6 Safety and Privacy changes in v2.1.251]] · Safety and Privacy
- [[Changes/Claude Code/2026-08-28-7-other-changes-in-v2-1-251|7 other changes in v2.1.251]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-08-27 · Claude Code · [[Changes/Claude Code/2026-08-27-improved-the-workflow-tool-s-prompt-footprint-its-description-is-now-about-1k-to|Improved the Workflow tool's prompt footprint]]
- Later: 2026-08-31 · ChatGPT · [[Changes/ChatGPT/2026-08-31-bring-your-browser-into-work-and-codex-mention-open-tabs-to-use-them-as-context-af2c3a|Bring your browser into Work and Codex]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-04 · Cursor · [[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2 Context Window changes in 0.2.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-08-28-bb3dfd&body=Card%3A%20Changes%2FClaude%20Code%2F2026-08-28-improved-retry-when-the-model-s-tool-call-is-malformed-the-broken-output-is-now.md%0ACard%20ID%3A%20claude-code-2026-08-28-bb3dfd%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.251%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->