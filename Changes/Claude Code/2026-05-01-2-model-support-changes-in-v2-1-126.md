---
card_id: claude-code-2026-05-01-1520ea
date: '2026-05-01'
description: 'Claude Code · 2026-05-01 · Model Support: 2 changes in v2.1.126 — The
  `/model` picker now lists models from your gateway''s `/v1/models` endpoint when…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1208
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2d997400675a5f4d0e52900ddc363f5bf7edbc96242b6c991b3acf550f997d82
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-05-01-1520ea
  comparison: ''
  date: '2026-05-01'
  description: 'Claude Code — v2.1.126: 2 Model Support changes'
  evidence:
  - quote: The `/model` picker now lists models from your gateway's `/v1/models` endpoint
      when `ANTHROPIC_BASE_URL` points at an Anthropic-compatible gateway
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.126
  - quote: 'Read tool: removed the per-file malware-assessment reminder that could
      cause spurious refusals and "this is not malware" commentary on legacy models'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.126
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-model-support-changes-in-v2-1-126
  source_release: claude-code-2026-05-01-v2-1-126-github-316244540-de18d9bb
  source_type: github_releases
  theme: model-support
  title: 2 Model Support changes in v2.1.126
  type: change
related_changes:
- '[[Changes/Claude Code/2026-04-22-2-model-support-changes-in-v2-1-117|2 Model Support
  changes in v2.1.117]]'
- '[[Changes/ChatGPT/2026-04-28-we-re-making-it-easier-to-choose-the-right-model-before-you-send-a-message-model|Easier
  model selection in ChatGPT]]'
- '[[Changes/Claude Code/2026-04-28-opentelemetry-added-stop-reason-gen-ai-response-finish-reasons-and-user-system-p|OpenTelemetry:
  added stop_reason, gen_ai.response.finish_reasons…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-01-v2-1-126-github-316244540-de18d9bb|claude-code-2026-05-01-v2-1-126-github-316244540-de18d9bb]]'
source_type: github_releases
theme: model-support
title: 2 Model Support changes in v2.1.126
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Model Support changes in v2.1.126

**Claude Code** · 2026-05-01 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.126) · from [[Releases/Claude Code/claude-code-2026-05-01-v2-1-126-github-316244540-de18d9bb|v2.1.126]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> The `/model` picker now lists models from your gateway's `/v1/models` endpoint when `ANTHROPIC_BASE_URL` points at an Anthropic-compatible gateway

> Read tool: removed the per-file malware-assessment reminder that could cause spurious refusals and "this is not malware" commentary on legacy models

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.126
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-05-01-claude-code-skill-activated-opentelemetry-event-now-fires-for-user-typed-slash-c|claude_code.skill_activated OpenTelemetry event now fires for user-typed slash…]] · Automation and Scheduling
- [[Changes/Claude Code/2026-05-01-3-developer-workflow-changes-in-v2-1-126|3 Developer Workflow changes in v2.1.126]] · Developer Workflow
- [[Changes/Claude Code/2026-05-01-3-safety-and-privacy-changes-in-v2-1-126|3 Safety and Privacy changes in v2.1.126]] · Safety and Privacy
- [[Changes/Claude Code/2026-05-01-added-claude-project-purge-path-to-delete-all-claude-code-state-for-a-project-tr|- Added claude project purge path to delete all Claude Code state for a project…]] · Projects and Workspaces
- [[Changes/Claude Code/2026-05-01-powershell-tool-bare-e-g-git-diff-file-is-no-longer-mis-flagged-as-the-stop-pars|PowerShell tool: bare -- (e.g. git diff -- file) is no longer mis-flagged…]] · Editor Experience
- [[Changes/Claude Code/2026-05-01-claude-auth-login-now-accepts-the-oauth-code-pasted-into-the-terminal-when-the-b|claude auth login now accepts the OAuth code pasted into the terminal…]] · Account and Access
- [[Changes/Claude Code/2026-05-01-2-other-changes-in-v2-1-126|2 other changes in v2.1.126]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-04-28 · Claude Code · [[Changes/Claude Code/2026-04-28-opentelemetry-added-stop-reason-gen-ai-response-finish-reasons-and-user-system-p|OpenTelemetry: added stop_reason, gen_ai.response.finish_reasons…]]
- Later: 2026-05-04 · Claude Code · [[Changes/Claude Code/2026-05-04-updated-model-picker-collapsed-duplicate-opus-4-7-entries-and-current-opus-now-s|Updated /model picker]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-05-01-1520ea&body=Card%3A%20Changes%2FClaude%20Code%2F2026-05-01-2-model-support-changes-in-v2-1-126.md%0ACard%20ID%3A%20claude-code-2026-05-01-1520ea%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.126%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->