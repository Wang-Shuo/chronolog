---
card_id: github-copilot-cli-2026-09-04-a4323a
date: '2026-09-04'
description: 'GitHub Copilot CLI · 2026-09-04 · Model Support: 3 changes in 1.0.83
  — Custom agents can list several models in `model`, tried in order until one is
  available…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1334
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d94ddf8d3fb832bbc98b3aa1e8c87fd20df2df13e596adc45da34f5875af0fdc
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-09-04-a4323a
  comparison: ''
  date: '2026-09-04'
  description: 'GitHub Copilot CLI — 1.0.83: 3 Model Support changes'
  evidence:
  - quote: 'Custom agents can list several models in `model`, tried in order until
      one is available to you, and `model-policy: required` keeps model changes on
      that list'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.83
  - quote: Add automatic HTTPS proxy mTLS client certificate support for model and
      web requests
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.83
  - quote: Remove retired Claude and Gemini models from /model picker results
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.83
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 3-model-support-changes-in-v1-0-83
  source_release: github-copilot-cli-2026-09-04-v1-0-83-github-382838246-6f996d9c
  source_type: github_releases
  theme: model-support
  title: 3 Model Support changes in v1.0.83
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-09-03-12-model-support-changes-in-v2026-9-1|12 Model Support
  changes in v2026.9.1]]'
- '[[Changes/Claude Code/2026-09-04-improved-the-model-picker-and-the-vs-code-model-pill-to-show-a-model-s-name-inst|Improved
  the /model picker and the VS Code model pill to show a model''s name…]]'
- '[[Changes/Codex CLI/2026-09-04-3-model-support-changes-in-rust-v0-153-3|3 Model
  Support changes in rust-v0.153.3]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-09-04-v1-0-83-github-382838246-6f996d9c|github-copilot-cli-2026-09-04-v1-0-83-github-382838246-6f996d9c]]'
source_type: github_releases
theme: model-support
title: 3 Model Support changes in v1.0.83
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Model Support changes in v1.0.83

**GitHub Copilot CLI** · 2026-09-04 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.83) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-09-04-v1-0-83-github-382838246-6f996d9c|1.0.83]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Custom agents can list several models in `model`, tried in order until one is available to you, and `model-policy: required` keeps model changes on that list

> Add automatic HTTPS proxy mTLS client certificate support for model and web requests

> Remove retired Claude and Gemini models from /model picker results

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.83
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-09-04-long-running-sessions-on-linux-return-freed-memory-to-the-system-instead-of-hold|Long-running sessions on Linux return freed memory to the system instead of holding…]] · Memory and Personalization
- [[Changes/GitHub Copilot CLI/2026-09-04-7-apps-and-integrations-changes-in-v1-0-83|7 Apps and Integrations changes in v1.0.83]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-09-04-enterprise-admins-can-pin-sign-in-to-approved-github-organizations-with-the-forc|Enterprise admins can pin sign-in to approved GitHub organizations…]] · Enterprise and Administration
- [[Changes/GitHub Copilot CLI/2026-09-04-2-editor-experience-changes-in-v1-0-83|2 Editor Experience changes in v1.0.83]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-09-04-detect-the-herdr-terminal-multiplexer-instead-of-mistaking-it-for-tmux-so-the-ki|Detect the herdr terminal multiplexer instead of mistaking it for tmux, so the Kitty…]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-09-04-exporting-a-resumed-session-with-share-or-share-gist-writes-the-whole-transcript|Exporting a resumed session with --share or --share-gist writes the whole transcript…]] · Collaboration
- [[Changes/GitHub Copilot CLI/2026-09-04-5-safety-and-privacy-changes-in-v1-0-83|5 Safety and Privacy changes in v1.0.83]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-09-04-stopping-a-timed-out-shell-command-now-lets-queued-messages-run-and-sessions-ret|Stopping a timed-out shell command now lets queued messages run and sessions return…]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-09-04-add-recent-created-name-and-classic-none-sorting-to-the-split-sessions-sidebar-w|Add Recent, Created, Name, and classic None sorting to the split Sessions sidebar…]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-09-04-3-account-and-access-changes-in-v1-0-83|3 Account and Access changes in v1.0.83]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-09-04-11-other-changes-in-v1-0-83|11 other changes in v1.0.83]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-09-04 · Codex CLI · [[Changes/Codex CLI/2026-09-04-3-model-support-changes-in-rust-v0-153-3|3 Model Support changes in rust-v0.153.3]]
- Later: 2026-09-04 · OpenCode · [[Changes/OpenCode/2026-09-04-core-fixes-issue-of-gpt-6-astra-not-showing-up-for-openai-subscription-users|Core Fixes issue of gpt-6-astra not showing up for openai subscription users]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-09-04-a4323a&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-09-04-3-model-support-changes-in-v1-0-83.md%0ACard%20ID%3A%20github-copilot-cli-2026-09-04-a4323a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.83%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->