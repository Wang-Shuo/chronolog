---
card_id: github-copilot-cli-2026-09-16-744300
date: '2026-09-16'
description: 'GitHub Copilot CLI · 2026-09-16 · Model Support: 13 changes in 1.0.85
  — Add support for GPT-6 Astra'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1346
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 10716b03ccd7012e341283d0f8fa46a77652f93065c7db23c8c3898aaebaea96
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-09-16-744300
  comparison: ''
  date: '2026-09-16'
  description: 'GitHub Copilot CLI — 1.0.85: 13 Model Support changes'
  evidence:
  - quote: Add support for GPT-6 Astra
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: Streamer mode masks internal model names in /model, the footer, and startup
      diagnostics without restarting model initialization on toggles
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: Authenticated model lists refresh after startup auth hydration
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: Resumed sessions show completed reasoning as Thought instead of Thinking…
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: Model lists refresh after signing in, switching accounts, or signing out
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: Changing reasoning effort now takes effect before the next logical request
      in an active turn, while retries keep their original effort
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: Interactive mode submits startup prompts even when model discovery is still
      loading.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: MCP tools with boolean property or array-item schemas work with Gemini
      instead of causing a 400 error
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: Viewing or attaching an image in a format the model cannot read, such as
      BMP or TIFF, no longer leaves the session unable to send any further message;
      the image is now reported as an unsupported format that you can convert to PNG,
      JPEG, WebP or GIF
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: /compact no longer reports an empty model response when a valid summary
      was returned
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: Retry responses keep the correct streamed message and reasoning after mid-stream
      model failures
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: When image-heavy requests exceed model limits, user-provided images are
      prioritized over tool-generated images, newer messages are kept first, and the
      CLI reports any removals.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: The `/rubber-duck` command is hidden after a model refresh removes its
      compatible critic
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 13-model-support-changes-in-v1-0-85
  source_release: github-copilot-cli-2026-09-16-v1-0-85-github-389603482-889a46d9
  source_type: github_releases
  theme: model-support
  title: 13 Model Support changes in v1.0.85
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-09-14-we-re-retiring-automatic-switching-from-instant-to-thinking-reasoning-for-chatgp|Changes
  to automatic switching to thinking in ChatGPT (Plus and Pro)]]'
- '[[Changes/Claude Code/2026-09-14-2-model-support-changes-in-v2-1-271|2 Model Support
  changes in v2.1.271]]'
- '[[Changes/Claude Code/2026-09-15-changed-bug-and-feedback-reports-to-include-only-model-behavior-params-model-sys|Changed
  /bug and /feedback reports to include only model-behavior params…]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-09-16-v1-0-85-github-389603482-889a46d9|github-copilot-cli-2026-09-16-v1-0-85-github-389603482-889a46d9]]'
source_type: github_releases
theme: model-support
title: 13 Model Support changes in v1.0.85
type: change
---

<!-- chronolog:begin region="header" -->
# 13 Model Support changes in v1.0.85

**GitHub Copilot CLI** · 2026-09-16 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.85) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-09-16-v1-0-85-github-389603482-889a46d9|1.0.85]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Add support for GPT-6 Astra

> Streamer mode masks internal model names in /model, the footer, and startup diagnostics without restarting model initialization on toggles

> Authenticated model lists refresh after startup auth hydration

> Resumed sessions show completed reasoning as Thought instead of Thinking…

> Model lists refresh after signing in, switching accounts, or signing out

> Changing reasoning effort now takes effect before the next logical request in an active turn, while retries keep their original effort

> Interactive mode submits startup prompts even when model discovery is still loading.

> MCP tools with boolean property or array-item schemas work with Gemini instead of causing a 400 error

> Viewing or attaching an image in a format the model cannot read, such as BMP or TIFF, no longer leaves the session unable to send any further message; the image is now reported as an unsupported format that you can convert to PNG, JPEG, WebP or GIF

> /compact no longer reports an empty model response when a valid summary was returned

> Retry responses keep the correct streamed message and reasoning after mid-stream model failures

> When image-heavy requests exceed model limits, user-provided images are prioritized over tool-generated images, newer messages are kept first, and the CLI reports any removals.

> The `/rubber-duck` command is hidden after a model refresh removes its compatible critic

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.85
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-09-16-4-account-and-access-changes-in-v1-0-85|4 Account and Access changes in v1.0.85]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-09-16-6-developer-workflow-changes-in-v1-0-85|6 Developer Workflow changes in v1.0.85]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-09-16-9-editor-experience-changes-in-v1-0-85|9 Editor Experience changes in v1.0.85]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-09-16-speed-up-startup-when-resuming-an-existing-local-session-by-its-exact-uuid-with|Speed up startup when resuming an existing local session by its exact UUID with --resume]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-09-16-17-safety-and-privacy-changes-in-v1-0-85|17 Safety and Privacy changes in v1.0.85]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-09-16-usage-shows-per-model-ai-credit-consumption-in-usage-breakdowns|/usage shows per-model AI Credit consumption in usage breakdowns]] · Pricing Model
- [[Changes/GitHub Copilot CLI/2026-09-16-3-memory-and-personalization-changes-in-v1-0-85|3 Memory and Personalization changes in v1.0.85]] · Memory and Personalization
- [[Changes/GitHub Copilot CLI/2026-09-16-4-mobile-and-desktop-changes-in-v1-0-85|4 Mobile and Desktop changes in v1.0.85]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-09-16-add-json-to-copilot-plugin-list-copilot-plugin-marketplace-list-and-copilot-plug|Add --json to copilot plugin list, copilot plugin marketplace list…]] · Search and Browsing
- [[Changes/GitHub Copilot CLI/2026-09-16-3-context-window-changes-in-v1-0-85|3 Context Window changes in v1.0.85]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-09-16-2-agent-mode-changes-in-v1-0-85|2 Agent Mode changes in v1.0.85]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-09-16-20-apps-and-integrations-changes-in-v1-0-85|20 Apps and Integrations changes in v1.0.85]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-09-16-share-notes-md-now-writes-the-exported-session-to-your-home-directory-instead-of|--share=~/notes.md now writes the exported session to your home directory instead…]] · Collaboration
- [[Changes/GitHub Copilot CLI/2026-09-16-when-session-history-is-truncated-or-compacted-just-as-a-turn-finishes-the-worki|When session history is truncated or compacted just as a turn finishes…]] · Projects and Workspaces
- [[Changes/GitHub Copilot CLI/2026-09-16-3-interface-experience-changes-in-v1-0-85|3 Interface Experience changes in v1.0.85]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-09-16-19-other-changes-in-v1-0-85|19 other changes in v1.0.85]] · Other changes
- [[Changes/GitHub Copilot CLI/2026-09-16-vim-mode-is-now-available-to-everyone-turn-it-on-with-vim-or-by-setting-editormo|Vim mode is now available to everyone]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-09-15 · Claude Code · [[Changes/Claude Code/2026-09-15-changed-bug-and-feedback-reports-to-include-only-model-behavior-params-model-sys|Changed /bug and /feedback reports to include only model-behavior params…]]
- Later: 2026-09-16 · OpenHands · [[Changes/OpenHands/2026-09-16-feat-add-gpt-6-astra-model-support-by-neubig-in-https-github-com-openhands-openh|feat: add GPT-6 Astra model support]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-09-16-744300&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-09-16-13-model-support-changes-in-v1-0-85.md%0ACard%20ID%3A%20github-copilot-cli-2026-09-16-744300%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.85%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->