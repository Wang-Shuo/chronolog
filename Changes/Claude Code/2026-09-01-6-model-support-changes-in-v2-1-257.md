---
card_id: claude-code-2026-09-01-f40169
date: '2026-09-01'
description: 'Claude Code · 2026-09-01 · Model Support: 6 changes in v2.1.257 — Added
  Claude Fable 5.1 (`claude-fable-5-1`), now the default Fable model — 1M context…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1331
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b70eb184422dce622944900bd8749552eaf69714ce91b04d936711e1ccc78de5
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-01-f40169
  comparison: ''
  date: '2026-09-01'
  description: 'Claude Code — v2.1.257: 6 Model Support changes'
  evidence:
  - quote: Added Claude Fable 5.1 (`claude-fable-5-1`), now the default Fable model
      — 1M context, $10/$50 per Mtok with $0.25/Mtok cache reads
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.257
  - quote: Added `s` in `/effort` to change effort for the current session only, matching
      `/model`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.257
  - quote: Changed `--effort` to lift a new model's default-effort hold for that session
      only rather than permanently; an effort picked on claude.ai for a Remote Control
      session now applies during the hold
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.257
  - quote: Changed gateway model discovery (`CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1`)
      to run even when `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` is set, since it
      only queries your gateway
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.257
  - quote: Changed `fable` and `best` in Claude apps gateway sessions to keep resolving
      to Fable 5 for now, since gateways not yet configured for Fable 5.1 reject it;
      pick Fable 5.1 in `/model` to use it
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.257
  - quote: '[VSCode] Added a model pill to the input footer that shows the current
      model and opens the model picker, with an Effort row and a "More models" page'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.257
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 6-model-support-changes-in-v2-1-257
  source_release: claude-code-2026-09-01-v2-1-257-github-380686035-b86855a6
  source_type: github_releases
  theme: model-support
  title: 6 Model Support changes in v2.1.257
  type: change
related_changes:
- '[[Changes/Claude Code/2026-08-26-added-claude-api-cost-optimize-to-profile-an-existing-project-s-claude-api-spend|Added
  /claude-api cost-optimize to profile an existing project''s Claude API spend…]]'
- '[[Changes/Claude Code/2026-08-28-5-model-support-changes-in-v2-1-251|5 Model Support
  changes in v2.1.251]]'
- '[[Changes/ChatGPT/2026-08-31-site-tools-use-webmcp-and-require-a-supported-account-model-and-webpage-they-are|Site
  tools use WebMCP and require a supported account, model, and webpage]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-01-v2-1-257-github-380686035-b86855a6|claude-code-2026-09-01-v2-1-257-github-380686035-b86855a6]]'
source_type: github_releases
theme: model-support
title: 6 Model Support changes in v2.1.257
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Model Support changes in v2.1.257

**Claude Code** · 2026-09-01 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.257) · from [[Releases/Claude Code/claude-code-2026-09-01-v2-1-257-github-380686035-b86855a6|v2.1.257]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added Claude Fable 5.1 (`claude-fable-5-1`), now the default Fable model — 1M context, $10/$50 per Mtok with $0.25/Mtok cache reads

> Added `s` in `/effort` to change effort for the current session only, matching `/model`

> Changed `--effort` to lift a new model's default-effort hold for that session only rather than permanently; an effort picked on claude.ai for a Remote Control session now applies during the hold

> Changed gateway model discovery (`CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1`) to run even when `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` is set, since it only queries your gateway

> Changed `fable` and `best` in Claude apps gateway sessions to keep resolving to Fable 5 for now, since gateways not yet configured for Fable 5.1 reject it; pick Fable 5.1 in `/model` to use it

> [VSCode] Added a model pill to the input footer that shows the current model and opens the model picker, with an Effort row and a "More models" page

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.257
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-01-2-editor-experience-changes-in-v2-1-257|2 Editor Experience changes in v2.1.257]] · Editor Experience
- [[Changes/Claude Code/2026-09-01-3-developer-workflow-changes-in-v2-1-257|3 Developer Workflow changes in v2.1.257]] · Developer Workflow
- [[Changes/Claude Code/2026-09-01-improved-prompt-input-responsiveness-by-reducing-per-keystroke-rendering-work|Improved prompt input responsiveness by reducing per-keystroke rendering work]] · Reliability and Performance
- [[Changes/Claude Code/2026-09-01-5-agent-mode-changes-in-v2-1-257|5 Agent Mode changes in v2.1.257]] · Agent Mode
- [[Changes/Claude Code/2026-09-01-changed-btw-history-browsing-from-to-shift-shift-or-stepping-through-your-recent|Changed /btw history browsing from ←/→ to Shift+←/Shift+→ (or /)…]] · Search and Browsing
- [[Changes/Claude Code/2026-09-01-10-safety-and-privacy-changes-in-v2-1-257|10 Safety and Privacy changes in v2.1.257]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-01-changed-add-dir-add-dir-and-additionaldirectories-to-refuse-network-paths-unc-sh|Changed --add-dir, /add-dir, and additionalDirectories to refuse network paths…]] · Mobile and Desktop
- [[Changes/Claude Code/2026-09-01-2-apps-and-integrations-changes-in-v2-1-257|2 Apps and Integrations changes in v2.1.257]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-01-2-account-and-access-changes-in-v2-1-257|2 Account and Access changes in v2.1.257]] · Account and Access
- [[Changes/Claude Code/2026-09-01-2-interface-experience-changes-in-v2-1-257|2 Interface Experience changes in v2.1.257]] · Interface Experience
- [[Changes/Claude Code/2026-09-01-7-other-changes-in-v2-1-257|7 other changes in v2.1.257]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-08-31 · ChatGPT · [[Changes/ChatGPT/2026-08-31-site-tools-use-webmcp-and-require-a-supported-account-model-and-webpage-they-are|Site tools use WebMCP and require a supported account, model, and webpage]]
- Later: 2026-09-03 · ChatGPT · [[Changes/ChatGPT/2026-09-03-today-we-re-introducing-gpt-6-astra-with-improvements-in-coding-research-compute-069f67|Introducing GPT-6 Astra]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-01-f40169&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-01-6-model-support-changes-in-v2-1-257.md%0ACard%20ID%3A%20claude-code-2026-09-01-f40169%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.257%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->