---
card_id: github-copilot-cli-2026-06-13-f2853a
date: '2026-06-13'
description: 'GitHub Copilot CLI · 2026-06-13 · Model Support: 3 changes in 1.0.62
  — Keep blank lines between reasoning summary sections'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1251
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 975452bfc87125bff16845c1a9fa80aa413ab6e8eb49196c8494d87a22559b8c
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-06-13-f2853a
  comparison: ''
  date: '2026-06-13'
  description: 'GitHub Copilot CLI — 1.0.62: 3 Model Support changes'
  evidence:
  - quote: Keep blank lines between reasoning summary sections
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.62
  - quote: An image attachment rejected because vision is disabled by policy or unsupported
      by the current model no longer poisons the rest of the session. The image is
      stripped from conversation history after the 400 so subsequent prompts succeed.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.62
  - quote: Keep custom agents on their configured model when using BYOK providers
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.62
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 3-model-support-changes-in-v1-0-62
  source_release: github-copilot-cli-2026-06-13-v1-0-62-github-339039020-f6ff7e5e
  source_type: github_releases
  theme: model-support
  title: 3 Model Support changes in v1.0.62
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-06-12-as-of-june-12-2026-gpt-5-2-models-are-no-longer-available-in-chatgpt-this-applie|Retiring
  GPT-5.2 models]]'
- '[[Changes/Claude Code/2026-06-12-added-enforceavailablemodels-managed-setting-when-enabled-the-availablemodels-al|Added
  enforceAvailableModels managed setting]]'
- '[[Changes/Ollama/2026-06-12-improved-recurrent-model-support-with-per-boundary-states-from-the-gated-delta-k|Improved
  recurrent model support with per-boundary states from the gated-delta kernels]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-13-v1-0-62-github-339039020-f6ff7e5e|github-copilot-cli-2026-06-13-v1-0-62-github-339039020-f6ff7e5e]]'
source_type: github_releases
theme: model-support
title: 3 Model Support changes in v1.0.62
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Model Support changes in v1.0.62

**GitHub Copilot CLI** · 2026-06-13 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.62) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-13-v1-0-62-github-339039020-f6ff7e5e|1.0.62]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Keep blank lines between reasoning summary sections

> An image attachment rejected because vision is disabled by policy or unsupported by the current model no longer poisons the rest of the session. The image is stripped from conversation history after the 400 so subsequent prompts succeed.

> Keep custom agents on their configured model when using BYOK providers

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.62
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-06-13-8-apps-and-integrations-changes-in-v1-0-62|8 Apps and Integrations changes in v1.0.62]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-06-13-speed-up-branch-and-head-detection-in-warm-sessions|Speed up branch and HEAD detection in warm sessions]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-06-13-4-agent-mode-changes-in-v1-0-62|4 Agent Mode changes in v1.0.62]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-06-13-every-and-after-can-now-schedule-slash-commands-e-g-every-1d-chronicle-standup|/every and /after can now schedule slash commands (e.g. /every 1d /chronicle standup)]] · Automation and Scheduling
- [[Changes/GitHub Copilot CLI/2026-06-13-voice-runtime-download-dialog-no-longer-reopens-in-a-loop-after-an-install-failu|Voice runtime download dialog no longer reopens in a loop after an install failure]] · Voice and Audio
- [[Changes/GitHub Copilot CLI/2026-06-13-2-safety-and-privacy-changes-in-v1-0-62|2 Safety and Privacy changes in v1.0.62]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-06-13-2-editor-experience-changes-in-v1-0-62|2 Editor Experience changes in v1.0.62]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-06-13-honor-max-output-tokens-for-byok-responses-providers|Honor max_output_tokens for BYOK Responses providers]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-06-13-remote-mcp-oauth-servers-start-only-once-per-matching-config-instead-of-restarti|Remote MCP OAuth servers start only once per matching config instead of restarting…]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-06-13-git-commands-no-longer-flash-a-console-window-on-windows|Git commands no longer flash a console window on Windows]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-06-13-allow-sdk-clients-to-configure-session-memory-through-session-create-and-session|Allow SDK clients to configure session memory through session.create and session.resume]] · Memory and Personalization
- [[Changes/GitHub Copilot CLI/2026-06-13-3-interface-experience-changes-in-v1-0-62|3 Interface Experience changes in v1.0.62]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-06-13-improve-color-contrast-in-github-themes-to-meet-wcag-aa-accessibility-standards|Improve color contrast in GitHub themes to meet WCAG AA accessibility standards]] · Accessibility and Localization
- [[Changes/GitHub Copilot CLI/2026-06-13-6-developer-workflow-changes-in-v1-0-62|6 Developer Workflow changes in v1.0.62]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-06-13-14-other-changes-in-v1-0-62|14 other changes in v1.0.62]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-06-12 · Ollama · [[Changes/Ollama/2026-06-12-improved-recurrent-model-support-with-per-boundary-states-from-the-gated-delta-k|Improved recurrent model support with per-boundary states from the gated-delta kernels]]
- Later: 2026-06-15 · Claude Code · [[Changes/Claude Code/2026-06-15-bug-now-requires-a-description-before-submitting-and-no-longer-uses-model-refusa|/bug now requires a description before submitting, and no longer uses…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-06-13-f2853a&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-06-13-3-model-support-changes-in-v1-0-62.md%0ACard%20ID%3A%20github-copilot-cli-2026-06-13-f2853a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.62%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->