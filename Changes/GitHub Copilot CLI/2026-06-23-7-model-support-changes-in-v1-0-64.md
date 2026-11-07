---
card_id: github-copilot-cli-2026-06-23-a42f12
date: '2026-06-23'
description: 'GitHub Copilot CLI · 2026-06-23 · Model Support: 7 changes in 1.0.64
  — Changing the model now waits until the new model is applied'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1261
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b0964a2f92581e7846f752f09716baf88955b9b0d9058ca0179032495b639563
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-06-23-a42f12
  comparison: ''
  date: '2026-06-23'
  description: 'GitHub Copilot CLI — 1.0.64: 7 Model Support changes'
  evidence:
  - quote: Changing the model now waits until the new model is applied
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: OpenTelemetry GenAI chat spans emit `gen_ai.request.reasoning.level` for
      the configured reasoning effort
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Add model family aliases like opus, sonnet, haiku, gpt, and gemini in the
      model setting
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: 'Experimental: in the compact timeline, click a tool-call or reasoning
      row to expand or collapse just that entry (like ctrl+o / ctrl+t for one row),
      with a subtle highlight on the row under the mouse'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Keep /model working on resumed sessions after signing in
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Forward typed rejection feedback from preToolUse prompts to the model
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Images returned by tools stay visible to the model across later turns and
      after resuming a session
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 7-model-support-changes-in-v1-0-64
  source_release: github-copilot-cli-2026-06-23-v1-0-64-github-343650012-6d4aa4bd
  source_type: github_releases
  theme: model-support
  title: 7 Model Support changes in v1.0.64
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-06-22-music|Music]]'
- '[[Changes/ElevenLabs/2026-06-22-dubbing|Dubbing]]'
- '[[Changes/Kimi Code/2026-06-22-detect-the-real-image-format-from-file-contents-when-reading-media-so-a-mismatch|Detect
  the real image format from file contents when reading media, so a mismatched…]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-23-v1-0-64-github-343650012-6d4aa4bd|github-copilot-cli-2026-06-23-v1-0-64-github-343650012-6d4aa4bd]]'
source_type: github_releases
theme: model-support
title: 7 Model Support changes in v1.0.64
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Model Support changes in v1.0.64

**GitHub Copilot CLI** · 2026-06-23 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.64) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-23-v1-0-64-github-343650012-6d4aa4bd|1.0.64]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Changing the model now waits until the new model is applied

> OpenTelemetry GenAI chat spans emit `gen_ai.request.reasoning.level` for the configured reasoning effort

> Add model family aliases like opus, sonnet, haiku, gpt, and gemini in the model setting

> Experimental: in the compact timeline, click a tool-call or reasoning row to expand or collapse just that entry (like ctrl+o / ctrl+t for one row), with a subtle highlight on the row under the mouse

> Keep /model working on resumed sessions after signing in

> Forward typed rejection feedback from preToolUse prompts to the model

> Images returned by tools stay visible to the model across later turns and after resuming a session

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.64
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-06-23-clear-queued-tool-images-when-vision-is-disabled|Clear queued tool images when vision is disabled]] · Multimodal Input
- [[Changes/GitHub Copilot CLI/2026-06-23-9-editor-experience-changes-in-v1-0-64|9 Editor Experience changes in v1.0.64]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-06-23-2-account-and-access-changes-in-v1-0-64|2 Account and Access changes in v1.0.64]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-06-23-preserve-open-canvas-instances-across-reconnects-and-restarts|Preserve open canvas instances across reconnects and restarts]] · Files and Data
- [[Changes/GitHub Copilot CLI/2026-06-23-6-safety-and-privacy-changes-in-v1-0-64|6 Safety and Privacy changes in v1.0.64]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-06-23-preserve-markdown-blockquotes-in-share-exports|Preserve Markdown blockquotes in /share exports]] · Collaboration
- [[Changes/GitHub Copilot CLI/2026-06-23-show-per-model-token-totals-in-usage-and-speed-up-large-history-scans|Show per-model token totals in /usage and speed up large history scans]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-06-23-add-loop-alias-for-the-every-command|Add /loop alias for the /every command]] · Automation and Scheduling
- [[Changes/GitHub Copilot CLI/2026-06-23-add-mcp-registry-installation-for-browsing-and-installing-mcp-servers|Add /mcp registry installation for browsing and installing MCP servers]] · Search and Browsing
- [[Changes/GitHub Copilot CLI/2026-06-23-8-apps-and-integrations-changes-in-v1-0-64|8 Apps and Integrations changes in v1.0.64]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-06-23-6-agent-mode-changes-in-v1-0-64|6 Agent Mode changes in v1.0.64]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-06-23-11-interface-experience-changes-in-v1-0-64|11 Interface Experience changes in v1.0.64]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-06-23-15-developer-workflow-changes-in-v1-0-64|15 Developer Workflow changes in v1.0.64]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-06-23-4-projects-and-workspaces-changes-in-v1-0-64|4 Projects and Workspaces changes in v1.0.64]] · Projects and Workspaces
- [[Changes/GitHub Copilot CLI/2026-06-23-display-cache-write-pricing-for-models-that-omit-it|Display cache-write pricing for models that omit it]] · Pricing Model
- [[Changes/GitHub Copilot CLI/2026-06-23-3-context-window-changes-in-v1-0-64|3 Context Window changes in v1.0.64]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-06-23-42-other-changes-in-v1-0-64|42 other changes in v1.0.64]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-06-22 · Kimi Code · [[Changes/Kimi Code/2026-06-22-detect-the-real-image-format-from-file-contents-when-reading-media-so-a-mismatch|Detect the real image format from file contents when reading media, so a mismatched…]]
- Later: 2026-06-24 · ChatGPT · [[Changes/ChatGPT/2026-06-24-we-re-updating-gpt-5-5-instant-our-most-used-model-in-chatgpt-to-improve-convers|GPT-5.5 Instant Update]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-06-23-a42f12&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-06-23-7-model-support-changes-in-v1-0-64.md%0ACard%20ID%3A%20github-copilot-cli-2026-06-23-a42f12%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.64%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->