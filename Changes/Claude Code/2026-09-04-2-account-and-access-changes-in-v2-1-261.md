---
card_id: claude-code-2026-09-04-881212
date: '2026-09-04'
description: 'Claude Code · 2026-09-04 · Account and Access: 2 changes in v2.1.261
  — Changed a Claude apps gateway 403 on the managed settings load (at startup or
  after…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1254
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: fd4232bb989502186b185efd10a086ab365eab0996acd6fa9c1e924cf0635b6f
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-04-881212
  comparison: ''
  date: '2026-09-04'
  description: 'Claude Code — v2.1.261: 2 Account and Access changes'
  evidence:
  - quote: Changed a Claude apps gateway 403 on the managed settings load (at startup
      or after `/login`) to say Claude Code may not be enabled for the organization,
      instead of advising a new sign-in
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.261
  - quote: 'Changed machines whose managed settings pin `forceLoginMethod: "gateway"`
      to ignore a leftover API key or claude.ai login and ask for `/login`; Bedrock,
      Vertex AI, and Foundry sessions are unaffected'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.261
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-account-and-access-changes-in-v2-1-261
  source_release: claude-code-2026-09-04-v2-1-261-github-382913543-2cb10519
  source_type: github_releases
  theme: account-access
  title: 2 Account and Access changes in v2.1.261
  type: change
related_changes:
- '[[Changes/Claude Code/2026-08-26-3-account-and-access-changes-in-v2-1-247|3 Account
  and Access changes in v2.1.247]]'
- '[[Changes/Claude Code/2026-08-28-changed-analytics-to-no-longer-turn-off-before-sign-in-solely-because-managed-se|Changed
  analytics to no longer turn off before sign-in solely because managed…]]'
- '[[Changes/Claude Code/2026-09-01-2-account-and-access-changes-in-v2-1-257|2 Account
  and Access changes in v2.1.257]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-04-v2-1-261-github-382913543-2cb10519|claude-code-2026-09-04-v2-1-261-github-382913543-2cb10519]]'
source_type: github_releases
theme: account-access
title: 2 Account and Access changes in v2.1.261
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Account and Access changes in v2.1.261

**Claude Code** · 2026-09-04 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.261) · from [[Releases/Claude Code/claude-code-2026-09-04-v2-1-261-github-382913543-2cb10519|v2.1.261]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Changed a Claude apps gateway 403 on the managed settings load (at startup or after `/login`) to say Claude Code may not be enabled for the organization, instead of advising a new sign-in

> Changed machines whose managed settings pin `forceLoginMethod: "gateway"` to ignore a leftover API key or claude.ai login and ask for `/login`; Bedrock, Vertex AI, and Foundry sessions are unaffected

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.261
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-04-improved-streaming-performance-already-rendered-blocks-are-no-longer-re-checked|Improved streaming performance]] · Reliability and Performance
- [[Changes/Claude Code/2026-09-04-3-interface-experience-changes-in-v2-1-261|3 Interface Experience changes in v2.1.261]] · Interface Experience
- [[Changes/Claude Code/2026-09-04-3-developer-workflow-changes-in-v2-1-261|3 Developer Workflow changes in v2.1.261]] · Developer Workflow
- [[Changes/Claude Code/2026-09-04-2-agent-mode-changes-in-v2-1-261|2 Agent Mode changes in v2.1.261]] · Agent Mode
- [[Changes/Claude Code/2026-09-04-vscode-added-an-add-server-form-and-a-remove-action-to-the-mcp-servers-dialog-so|VSCode Added an Add server form and a Remove action to the MCP servers dialog…]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-04-changed-context-token-counting-to-use-a-local-estimate-when-the-token-counting-a|Changed /context token counting to use a local estimate when the token-counting…]] · Context Window
- [[Changes/Claude Code/2026-09-04-added-skill-doctor-to-show-which-loaded-skills-go-unused-and-what-they-cost-in-c|Added /skill-doctor to show which loaded skills go unused and what they cost…]] · Context Window
- [[Changes/Claude Code/2026-09-04-4-safety-and-privacy-changes-in-v2-1-261|4 Safety and Privacy changes in v2.1.261]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-04-improved-the-model-picker-and-the-vs-code-model-pill-to-show-a-model-s-name-inst|Improved the /model picker and the VS Code model pill to show a model's name…]] · Model Support
- [[Changes/Claude Code/2026-09-04-3-other-changes-in-v2-1-261|3 other changes in v2.1.261]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-09-01 · Claude Code · [[Changes/Claude Code/2026-09-01-2-account-and-access-changes-in-v2-1-257|2 Account and Access changes in v2.1.257]]
- Later: 2026-09-08 · Claude Code · [[Changes/Claude Code/2026-09-08-2-account-and-access-changes-in-v2-1-265|2 Account and Access changes in v2.1.265]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-04-881212&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-04-2-account-and-access-changes-in-v2-1-261.md%0ACard%20ID%3A%20claude-code-2026-09-04-881212%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.261%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->