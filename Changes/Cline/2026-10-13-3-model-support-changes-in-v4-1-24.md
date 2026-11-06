---
card_id: cline-2026-10-13-b7300d
date: '2026-10-13'
description: 'Cline · 2026-10-13 · Model Support: 3 changes in v4.1.24 — With no model
  chosen, the Cline and OpenRouter providers now use Claude Sonnet 5.5. For Cline…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1373
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d7717cf27bccb43adf16a16566e33ea3f5b42d187d4461221552743134b8e535
product: cline
product_name: Cline
record:
  card_id: cline-2026-10-13-b7300d
  comparison: ''
  date: '2026-10-13'
  description: 'Cline — v4.1.24: 3 Model Support changes'
  evidence:
  - quote: With no model chosen, the Cline and OpenRouter providers now use Claude
      Sonnet 5.5. For Cline, that's the first model in Cline's recommended list.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.24
  - quote: Refreshed the model catalog. Adds Claude Haiku 5.5 and the AI/ML API, LowRouter,
      and Prime Inference providers. The Cline free list adds Step 5 Preview. The
      v0 provider now offers only its default model, `v0-1.5-md`, and OpenCode Go
      uses its new `https://opencode.ai/inference/go/v1` endpoint. Default models
      change for 302.AI, Cortecs, CrossModel, DevPass, DigitalOcean, Eden AI, GitHub
      Copilot, Google Vertex AI, LLM Gateway, Meta, Moark, NanoGPT, NEAR AI Cloud,
      Neuralwatt, Novita AI, Ofox, OpenCode Go, Requesty, Vivgrid, and a few others
      (most now Claude Haiku 5.5 or Muse Wonder 1.0). If you use one of those providers
      without pinning a model, expect a different default.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.24
  - quote: Turning reasoning off no longer fails with a 400 error on GPT-6 Astra,
      GPT-6.1 Sol, Claude Fable 5 or Claude Opus 5.5, and now works on every provider.
      Level-only Gemini models no longer reject the request with a thinking-budget
      error.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.24
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: cline
  product_name: Cline
  slug: 3-model-support-changes-in-v4-1-24
  source_release: cline-2026-10-13-v4-1-24-github-411804449-05899922
  source_type: github_releases
  theme: model-support
  title: 3 Model Support changes in v4.1.24
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-09-claude-tag-changed-claude-in-slack-to-show-the-footer-with-the-session-link-mode|Claude
  Tag Changed Claude in Slack to show the footer with the session link, model…]]'
- '[[Changes/GitHub Copilot CLI/2026-10-12-2-model-support-changes-in-v1-0-96|2 Model
  Support changes in v1.0.96]]'
- '[[Changes/OpenHands/2026-10-12-3-model-support-changes-in-v1-27-0|3 Model Support
  changes in v1.27.0]]'
source_release: '[[Releases/Cline/cline-2026-10-13-v4-1-24-github-411804449-05899922|cline-2026-10-13-v4-1-24-github-411804449-05899922]]'
source_type: github_releases
theme: model-support
title: 3 Model Support changes in v4.1.24
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Model Support changes in v4.1.24

**Cline** · 2026-10-13 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/cline/cline/releases/tag/v4.1.24) · from [[Releases/Cline/cline-2026-10-13-v4-1-24-github-411804449-05899922|v4.1.24]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> With no model chosen, the Cline and OpenRouter providers now use Claude Sonnet 5.5. For Cline, that's the first model in Cline's recommended list.

> Refreshed the model catalog. Adds Claude Haiku 5.5 and the AI/ML API, LowRouter, and Prime Inference providers. The Cline free list adds Step 5 Preview. The v0 provider now offers only its default model, `v0-1.5-md`, and OpenCode Go uses its new `https://opencode.ai/inference/go/v1` endpoint. Default models change for 302.AI, Cortecs, CrossModel, DevPass, DigitalOcean, Eden AI, GitHub Copilot, Google Vertex AI, LLM Gateway, Meta, Moark, NanoGPT, NEAR AI Cloud, Neuralwatt, Novita AI, Ofox, OpenCode Go, Requesty, Vivgrid, and a few others (most now Claude Haiku 5.5 or Muse Wonder 1.0). If you use one of those providers without pinning a model, expect a different default.

> Turning reasoning off no longer fails with a 400 error on GPT-6 Astra, GPT-6.1 Sol, Claude Fable 5 or Claude Opus 5.5, and now works on every provider. Level-only Gemini models no longer reject the request with a thinking-budget error.

Source: https://github.com/cline/cline/releases/tag/v4.1.24
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Cline/2026-10-13-2-context-window-changes-in-v4-1-24|2 Context Window changes in v4.1.24]] · Context Window
- [[Changes/Cline/2026-10-13-2-account-and-access-changes-in-v4-1-24|2 Account and Access changes in v4.1.24]] · Account and Access
- [[Changes/Cline/2026-10-13-the-editor-tool-no-longer-receives-null-in-place-of-the-text-to-replace-from-som|The editor tool no longer receives null in place of the text to replace from some models]] · Editor Experience
- [[Changes/Cline/2026-10-13-deleting-a-slash-command-from-the-input-keeps-the-spacing-of-the-text-around-it|Deleting a slash command from the input keeps the spacing of the text around it]] · Developer Workflow
- [[Changes/Cline/2026-10-13-an-mcp-server-or-hook-that-exits-before-reading-all-of-its-input-no-longer-crash|An MCP server or hook that exits before reading all of its input no longer crashes…]] · Apps and Integrations
- [[Changes/Cline/2026-10-13-rule-files-that-are-symlinks-now-load-and-skills-in-claude-skills-are-now-discov|Rule files that are symlinks now load, and skills in .claude/skills are now discovered]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-10-12 · OpenHands · [[Changes/OpenHands/2026-10-12-3-model-support-changes-in-v1-27-0|3 Model Support changes in v1.27.0]]
- Later: 2026-10-14 · Claude Code · [[Changes/Claude Code/2026-10-14-2-model-support-changes-in-v2-1-299|2 Model Support changes in v2.1.299]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20cline-2026-10-13-b7300d&body=Card%3A%20Changes%2FCline%2F2026-10-13-3-model-support-changes-in-v4-1-24.md%0ACard%20ID%3A%20cline-2026-10-13-b7300d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fcline%2Fcline%2Freleases%2Ftag%2Fv4.1.24%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->