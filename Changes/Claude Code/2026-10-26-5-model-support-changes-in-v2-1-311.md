---
card_id: claude-code-2026-10-26-765e67
date: '2026-10-26'
description: 'Claude Code · 2026-10-26 · Model Support: 5 changes in v2.1.311 — Improved
  compaction: when the model''s reply has no summary in it, Claude Code now usually…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1386
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 25df82ab9f5c112ceb6d6d85b05adedd361b1d350ecac49bef829dc5f6607979
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-26-765e67
  comparison: ''
  date: '2026-10-26'
  description: 'Claude Code — v2.1.311: 5 Model Support changes'
  evidence:
  - quote: 'Improved compaction: when the model''s reply has no summary in it, Claude
      Code now usually asks for the summary once more before it replaces the conversation'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.311
  - quote: Improved startup time for launches whose only arguments are options and
      their values, such as `claude --model opus`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.311
  - quote: Changed `ultrathink` in the interactive terminal to run its turn at xhigh
      effort on Opus 5.5, Sonnet 5.5, Haiku 5.5 and Fable 5.1 through Anthropic's
      API; typed while Claude is working, it raises the rest of that turn
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.311
  - quote: Changed model names and IDs to drop the `[1m]` suffix and its label on
      models where the suffix has no effect; the suffix is still accepted
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.311
  - quote: Changed Claude Code on Bedrock, Mantle, Vertex, and Foundry to load model
      settings from a signed file on downloads.claude.ai; set CLAUDE_CODE_MODEL_CATALOG=off
      to turn this off
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.311
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 5-model-support-changes-in-v2-1-311
  source_release: claude-code-2026-10-26-v2-1-311-github-424682562-151da26b
  source_type: github_releases
  theme: model-support
  title: 5 Model Support changes in v2.1.311
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-16-improved-the-message-when-a-background-session-reopened-from-another-folder-has|Improved
  the message when a background session reopened from another folder has no…]]'
- '[[Changes/Claude Code/2026-10-19-2-model-support-changes-in-v2-1-304|2 Model Support
  changes in v2.1.304]]'
- '[[Changes/ChatGPT/2026-10-26-gpt-6-1-terra-is-rolling-out-in-chatgpt-work-and-codex-it-supports-a-range-of-ta|GPT-6.1
  Terra]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-26-v2-1-311-github-424682562-151da26b|claude-code-2026-10-26-v2-1-311-github-424682562-151da26b]]'
source_type: github_releases
theme: model-support
title: 5 Model Support changes in v2.1.311
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Model Support changes in v2.1.311

**Claude Code** · 2026-10-26 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.311) · from [[Releases/Claude Code/claude-code-2026-10-26-v2-1-311-github-424682562-151da26b|v2.1.311]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Improved compaction: when the model's reply has no summary in it, Claude Code now usually asks for the summary once more before it replaces the conversation

> Improved startup time for launches whose only arguments are options and their values, such as `claude --model opus`

> Changed `ultrathink` in the interactive terminal to run its turn at xhigh effort on Opus 5.5, Sonnet 5.5, Haiku 5.5 and Fable 5.1 through Anthropic's API; typed while Claude is working, it raises the rest of that turn

> Changed model names and IDs to drop the `[1m]` suffix and its label on models where the suffix has no effect; the suffix is still accepted

> Changed Claude Code on Bedrock, Mantle, Vertex, and Foundry to load model settings from a signed file on downloads.claude.ai; set CLAUDE_CODE_MODEL_CATALOG=off to turn this off

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.311
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-26-3-apps-and-integrations-changes-in-v2-1-311|3 Apps and Integrations changes in v2.1.311]] · Apps and Integrations
- [[Changes/Claude Code/2026-10-26-changed-startup-warnings-about-permission-rules-in-settings-files-to-show-once-p|Changed startup warnings about permission rules in settings files to show once per…]] · Safety and Privacy
- [[Changes/Claude Code/2026-10-26-changed-clicks-on-scrollbar-arrows-and-bars-in-fullscreen-lists-to-act-when-the|Changed clicks on scrollbar arrows and bars in fullscreen lists to act…]] · Interface Experience
- [[Changes/Claude Code/2026-10-26-2-agent-mode-changes-in-v2-1-311|2 Agent Mode changes in v2.1.311]] · Agent Mode
- [[Changes/Claude Code/2026-10-26-vscode-changed-the-session-list-side-bar-to-load-web-sessions-when-the-web-tab-i|VSCode Changed the session list side bar to load Web sessions when the Web tab…]] · Editor Experience
- [[Changes/Claude Code/2026-10-26-3-accessibility-and-localization-changes-in-v2-1-311|3 Accessibility and Localization changes in v2.1.311]] · Accessibility and Localization
- [[Changes/Claude Code/2026-10-26-improved-the-artifact-tool-s-choice-between-a-page-and-a-document-explainers-and|Improved the Artifact tool's choice between a page and a document]] · Files and Data
- [[Changes/Claude Code/2026-10-26-2-context-window-changes-in-v2-1-311|2 Context Window changes in v2.1.311]] · Context Window
- [[Changes/Claude Code/2026-10-26-4-developer-workflow-changes-in-v2-1-311|4 Developer Workflow changes in v2.1.311]] · Developer Workflow
- [[Changes/Claude Code/2026-10-26-improved-the-message-shown-when-a-pasted-sign-in-code-is-refused-it-now-says-the|Improved the message shown when a pasted sign-in code is refused]] · Account and Access
- [[Changes/Claude Code/2026-10-26-12-other-changes-in-v2-1-311|12 other changes in v2.1.311]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-10-26 · ChatGPT · [[Changes/ChatGPT/2026-10-26-gpt-6-1-terra-is-rolling-out-in-chatgpt-work-and-codex-it-supports-a-range-of-ta|GPT-6.1 Terra]]
- Later: 2026-10-27 · Claude Code · [[Changes/Claude Code/2026-10-27-3-model-support-changes-in-v2-1-312|3 Model Support changes in v2.1.312]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-26-765e67&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-26-5-model-support-changes-in-v2-1-311.md%0ACard%20ID%3A%20claude-code-2026-10-26-765e67%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.311%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->