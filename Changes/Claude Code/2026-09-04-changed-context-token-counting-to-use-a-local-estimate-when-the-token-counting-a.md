---
card_id: claude-code-2026-09-04-a43ccb
date: '2026-09-04'
description: 'Claude Code · 2026-09-04 · Context Window: Changed `/context` token
  counting to use a local estimate when the token-counting API is unavailable, instead
  of…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2
    Context Window changes in 0.2.9]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1219
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: change
machine_hash: 2ce536d9e5828e2230f69c52cdbf6010850fb51b35895088b70456a87bfbb1c4
product: claude-code
product_name: Claude Code
record:
  ai_generated: true
  card_id: claude-code-2026-09-04-a43ccb
  comparison: ''
  confidence: low
  date: '2026-09-04'
  description: 'Claude Code — v2.1.261: Changed `/context` token counting to use a
    local estimate when the token-counting API is unavailable, instead of extra small-model
    requests'
  evidence:
  - quote: Changed `/context` token counting to use a local estimate when the token-counting
      API is unavailable, instead of extra small-model requests
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.261
  extractor_version: fallback-v5
  impact: significant
  kind: change
  product: claude-code
  product_name: Claude Code
  slug: changed-context-token-counting-to-use-a-local-estimate-when-the-token-counting-a
  source_release: claude-code-2026-09-04-v2-1-261-github-382913543-2cb10519
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
  title: Changed `/context` token counting to use a local estimate when the token-counting…
  type: change
related_changes:
- '[[Changes/Claude Code/2026-08-28-improved-retry-when-the-model-s-tool-call-is-malformed-the-broken-output-is-now|Improved
  retry when the model''s tool call is malformed]]'
- '[[Changes/ChatGPT/2026-08-31-bring-your-browser-into-work-and-codex-mention-open-tabs-to-use-them-as-context-af2c3a|Bring
  your browser into Work and Codex]]'
- '[[Changes/Claude Code/2026-09-03-3-context-window-changes-in-v2-1-260|3 Context
  Window changes in v2.1.260]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-04-v2-1-261-github-382913543-2cb10519|claude-code-2026-09-04-v2-1-261-github-382913543-2cb10519]]'
source_type: github_releases
theme: context-window
title: Changed /context token counting to use a local estimate when the token-counting…
type: change
---

<!-- chronolog:begin region="header" -->
# Changed `/context` token counting to use a local estimate when the token-counting…

**Claude Code** · 2026-09-04 · [[Themes/context-window|Context Window]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.261) · from [[Releases/Claude Code/claude-code-2026-09-04-v2-1-261-github-382913543-2cb10519|v2.1.261]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Changed `/context` token counting to use a local estimate when the token-counting API is unavailable, instead of extra small-model requests
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.261
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-04-improved-streaming-performance-already-rendered-blocks-are-no-longer-re-checked|Improved streaming performance]] · Reliability and Performance
- [[Changes/Claude Code/2026-09-04-3-interface-experience-changes-in-v2-1-261|3 Interface Experience changes in v2.1.261]] · Interface Experience
- [[Changes/Claude Code/2026-09-04-3-developer-workflow-changes-in-v2-1-261|3 Developer Workflow changes in v2.1.261]] · Developer Workflow
- [[Changes/Claude Code/2026-09-04-2-agent-mode-changes-in-v2-1-261|2 Agent Mode changes in v2.1.261]] · Agent Mode
- [[Changes/Claude Code/2026-09-04-vscode-added-an-add-server-form-and-a-remove-action-to-the-mcp-servers-dialog-so|VSCode Added an Add server form and a Remove action to the MCP servers dialog…]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-04-2-account-and-access-changes-in-v2-1-261|2 Account and Access changes in v2.1.261]] · Account and Access
- [[Changes/Claude Code/2026-09-04-added-skill-doctor-to-show-which-loaded-skills-go-unused-and-what-they-cost-in-c|Added /skill-doctor to show which loaded skills go unused and what they cost…]] · Context Window
- [[Changes/Claude Code/2026-09-04-4-safety-and-privacy-changes-in-v2-1-261|4 Safety and Privacy changes in v2.1.261]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-04-improved-the-model-picker-and-the-vs-code-model-pill-to-show-a-model-s-name-inst|Improved the /model picker and the VS Code model pill to show a model's name…]] · Model Support
- [[Changes/Claude Code/2026-09-04-3-other-changes-in-v2-1-261|3 other changes in v2.1.261]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-09-03 · Claude Code · [[Changes/Claude Code/2026-09-03-3-context-window-changes-in-v2-1-260|3 Context Window changes in v2.1.260]]
- Later: 2026-09-09 · Claude Code · [[Changes/Claude Code/2026-09-09-improved-prompt-cache-stability-subagents-and-sessions-started-with-system-promp|Improved prompt-cache stability]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-04 · Cursor · [[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2 Context Window changes in 0.2.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-04-a43ccb&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-04-changed-context-token-counting-to-use-a-local-estimate-when-the-token-counting-a.md%0ACard%20ID%3A%20claude-code-2026-09-04-a43ccb%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.261%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->