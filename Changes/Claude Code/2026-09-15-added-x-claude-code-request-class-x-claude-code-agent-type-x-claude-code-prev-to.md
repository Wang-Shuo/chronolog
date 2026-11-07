---
card_id: claude-code-2026-09-15-d69af3
date: '2026-09-15'
description: 'Claude Code · 2026-09-15 · Context Window: Added `x-claude-code-request-class`,
  `x-claude-code-agent-type`, `x-claude-code-prev-tool-durations`…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click
    to select a range]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2554
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: change
machine_hash: 1f822b2ac83630fbf8addc431b6bc1e24921c5c2e17e97152d62c8a92caea2a9
product: claude-code
product_name: Claude Code
record:
  ai_generated: true
  card_id: claude-code-2026-09-15-d69af3
  comparison: ''
  confidence: low
  date: '2026-09-15'
  description: 'Claude Code — v2.1.273: Added `x-claude-code-request-class`, `x-claude-code-agent-type`,
    `x-claude-code-prev-tool-durations`, `x-claude-code-compaction` and `x-claude-code-context-compacted`
    request headers for LLM gateways; opt in with `CLAUDE_CODE_GATEWAY_HINT_HEADERS=1`'
  evidence:
  - quote: Added `x-claude-code-request-class`, `x-claude-code-agent-type`, `x-claude-code-prev-tool-durations`,
      `x-claude-code-compaction` and `x-claude-code-context-compacted` request headers
      for LLM gateways; opt in with `CLAUDE_CODE_GATEWAY_HINT_HEADERS=1`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.273
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: change
  product: claude-code
  product_name: Claude Code
  slug: added-x-claude-code-request-class-x-claude-code-agent-type-x-claude-code-prev-to
  source_release: claude-code-2026-09-15-v2-1-273-github-389362239-6ea37826
  source_type: github_releases
  theme: context-window
  theme_matches:
  - matched_terms:
    - agent
    score: 50
    theme: agent-mode
  - matched_terms:
    - context
    score: 50
    theme: context-window
  - matched_terms:
    - llm
    score: 50
    theme: model-support
  theme_resolution: manual-semantic-rule-v1
  title: Added `x-claude-code-request-class`, `x-claude-code-agent-type`…
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-09-11-2-context-window-changes-in-v2026-9-4|2 Context Window
  changes in v2026.9.4]]'
- '[[Changes/Claude Code/2026-09-14-improved-the-spinner-status-during-long-thinking-it-now-reads-deep-in-thought-af|Improved
  the spinner status during long thinking]]'
- '[[Changes/Ollama/2026-09-14-runaway-repeat-token-detection-now-requires-100-repeat-tokens-for-reduced-false|Runaway
  repeat token detection now requires 100 repeat tokens for reduced false…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-15-v2-1-273-github-389362239-6ea37826|claude-code-2026-09-15-v2-1-273-github-389362239-6ea37826]]'
source_type: github_releases
theme: context-window
title: Added x-claude-code-request-class, x-claude-code-agent-type…
type: change
---

<!-- chronolog:begin region="header" -->
# Added `x-claude-code-request-class`, `x-claude-code-agent-type`…

**Claude Code** · 2026-09-15 · [[Themes/context-window|Context Window]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.273) · from [[Releases/Claude Code/claude-code-2026-09-15-v2-1-273-github-389362239-6ea37826|v2.1.273]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `x-claude-code-request-class`, `x-claude-code-agent-type`, `x-claude-code-prev-tool-durations`, `x-claude-code-compaction` and `x-claude-code-context-compacted` request headers for LLM gateways; opt in with `CLAUDE_CODE_GATEWAY_HINT_HEADERS=1`
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.273
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-15-claude-code-on-the-web-improved-the-routine-detail-page-menu-and-rename-in-the-b|Claude Code on the web Improved the routine detail page]] · Interface Experience
- [[Changes/Claude Code/2026-09-15-improved-artifact-database-writes-an-update-can-now-remove-a-single-field-instea|Improved artifact database writes]] · Files and Data
- [[Changes/Claude Code/2026-09-15-5-safety-and-privacy-changes-in-v2-1-273|5 Safety and Privacy changes in v2.1.273]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-15-3-apps-and-integrations-changes-in-v2-1-273|3 Apps and Integrations changes in v2.1.273]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-15-changed-auto-mode-on-bedrock-vertex-and-foundry-to-use-the-local-classifier-by-d|Changed auto mode on Bedrock, Vertex and Foundry to use the local classifier…]] · Agent Mode
- [[Changes/Claude Code/2026-09-15-changed-bug-and-feedback-reports-to-include-only-model-behavior-params-model-sys|Changed /bug and /feedback reports to include only model-behavior params…]] · Model Support
- [[Changes/Claude Code/2026-09-15-claude-code-on-the-web-added-a-discard-unsaved-changes-confirmation-before-the-n|Claude Code on the web Added a "Discard unsaved changes?" confirmation before…]] · Editor Experience
- [[Changes/Claude Code/2026-09-15-4-account-and-access-changes-in-v2-1-273|4 Account and Access changes in v2.1.273]] · Account and Access
- [[Changes/Claude Code/2026-09-15-improved-responsiveness-in-long-sessions-hook-progress-and-sub-agent-activity-no|Improved responsiveness in long sessions]] · Reliability and Performance
- [[Changes/Claude Code/2026-09-15-claude-code-on-the-web-removed-the-full-page-desktop-app-download-screen-that-ne|Claude Code on the web Removed the full-page desktop-app download screen that new…]] · Mobile and Desktop
- [[Changes/Claude Code/2026-09-15-3-developer-workflow-changes-in-v2-1-273|3 Developer Workflow changes in v2.1.273]] · Developer Workflow
- [[Changes/Claude Code/2026-09-15-8-other-changes-in-v2-1-273|8 other changes in v2.1.273]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-09-14 · Ollama · [[Changes/Ollama/2026-09-14-runaway-repeat-token-detection-now-requires-100-repeat-tokens-for-reduced-false|Runaway repeat token detection now requires 100 repeat tokens for reduced false…]]
- Later: 2026-09-15 · Notion · [[Changes/Notion/2026-09-15-run-a-skill-the-moment-you-need-it|Run a skill the moment you need it]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click to select a range]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-15-d69af3&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-15-added-x-claude-code-request-class-x-claude-code-agent-type-x-claude-code-prev-to.md%0ACard%20ID%3A%20claude-code-2026-09-15-d69af3%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.273%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->