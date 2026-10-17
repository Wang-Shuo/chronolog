---
card_id: claude-code-2026-09-25-e69489
date: '2026-09-25'
description: 'Claude Code · 2026-09-25 · Model Support: 3 changes in v2.1.283 — Added
  `x-claude-code-prompt-id` to the gateway hint headers so LLM gateways can group
  the…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1355
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b39103eb36e4e193cddec3da3bb6442a8b80fd670ff9bc4a0624bd37267d41e8
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-25-e69489
  comparison: ''
  date: '2026-09-25'
  description: 'Claude Code — v2.1.283: 3 Model Support changes'
  evidence:
  - quote: Added `x-claude-code-prompt-id` to the gateway hint headers so LLM gateways
      can group the requests that serve one user prompt; opt in with `CLAUDE_CODE_GATEWAY_HINT_HEADERS=1`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.283
  - quote: 'Added `availableModelsMatch` managed setting: with `"exact"`, an `availableModels`
      entry allows only the model version it names, so new releases stay blocked until
      listed'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.283
  - quote: Added `deniedModels` managed setting to block specific models, even when
      `availableModels` allows them
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.283
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-model-support-changes-in-v2-1-283
  source_release: claude-code-2026-09-25-v2-1-283-github-396845205-9a5a07f8
  source_type: github_releases
  theme: model-support
  title: 3 Model Support changes in v2.1.283
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-22-5-model-support-changes-in-v2-1-280|5 Model Support
  changes in v2.1.280]]'
- '[[Changes/Claude Code/2026-09-23-improved-interactive-startup-time-git-reads-startup-telemetry-and-the-bedrock-ve|Improved
  interactive startup time]]'
- '[[Changes/Claude Code/2026-09-24-claude-tag-changed-newly-connected-slack-workspaces-to-follow-the-current-defaul|Claude
  Tag Changed newly connected Slack workspaces to follow the current default…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-25-v2-1-283-github-396845205-9a5a07f8|claude-code-2026-09-25-v2-1-283-github-396845205-9a5a07f8]]'
source_type: github_releases
theme: model-support
title: 3 Model Support changes in v2.1.283
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Model Support changes in v2.1.283

**Claude Code** · 2026-09-25 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.283) · from [[Releases/Claude Code/claude-code-2026-09-25-v2-1-283-github-396845205-9a5a07f8|v2.1.283]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `x-claude-code-prompt-id` to the gateway hint headers so LLM gateways can group the requests that serve one user prompt; opt in with `CLAUDE_CODE_GATEWAY_HINT_HEADERS=1`

> Added `availableModelsMatch` managed setting: with `"exact"`, an `availableModels` entry allows only the model version it names, so new releases stay blocked until listed

> Added `deniedModels` managed setting to block specific models, even when `availableModels` allows them

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.283
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-25-3-developer-workflow-changes-in-v2-1-283|3 Developer Workflow changes in v2.1.283]] · Developer Workflow
- [[Changes/Claude Code/2026-09-25-improved-startup-claude-p-and-claude-code-remote-no-longer-load-the-interactive|Improved startup: claude -p and Claude Code Remote no longer load the interactive…]] · Agent Mode
- [[Changes/Claude Code/2026-09-25-14-apps-and-integrations-changes-in-v2-1-283|14 Apps and Integrations changes in v2.1.283]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-25-3-safety-and-privacy-changes-in-v2-1-283|3 Safety and Privacy changes in v2.1.283]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-25-improved-prompt-audit-on-claude-code-configuration-stale-paths-stale-commands-an|Improved prompt-audit on Claude Code configuration]] · Files and Data
- [[Changes/Claude Code/2026-09-25-2-context-window-changes-in-v2-1-283|2 Context Window changes in v2.1.283]] · Context Window
- [[Changes/Claude Code/2026-09-25-2-reliability-and-performance-changes-in-v2-1-283|2 Reliability and Performance changes in v2.1.283]] · Reliability and Performance
- [[Changes/Claude Code/2026-09-25-improved-lists-in-help-hooks-copy-chrome-memory-ide-release-notes-rewind-diff-re|Improved lists in /help, /hooks, /copy, /chrome, /memory, /ide…]] · Memory and Personalization
- [[Changes/Claude Code/2026-09-25-2-interface-experience-changes-in-v2-1-283|2 Interface Experience changes in v2.1.283]] · Interface Experience
- [[Changes/Claude Code/2026-09-25-9-other-changes-in-v2-1-283|9 other changes in v2.1.283]] · Other changes
- [[Changes/Claude Code/2026-09-25-added-doctor-prompt-audit-also-checkup-prompt-audit-to-audit-your-claude-md-file|Added /doctor prompt-audit (also /checkup prompt-audit) to audit your CLAUDE.md…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-09-24 · Claude Code · [[Changes/Claude Code/2026-09-24-claude-tag-changed-newly-connected-slack-workspaces-to-follow-the-current-defaul|Claude Tag Changed newly connected Slack workspaces to follow the current default…]]
- Later: 2026-09-28 · Claude Code · [[Changes/Claude Code/2026-09-28-6-model-support-changes-in-v2-1-284|6 Model Support changes in v2.1.284]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-25-e69489&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-25-3-model-support-changes-in-v2-1-283.md%0ACard%20ID%3A%20claude-code-2026-09-25-e69489%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.283%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->