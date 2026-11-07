---
card_id: gemini-cli-2025-07-25-210aea
date: '2025-07-25'
description: 'Gemini CLI · 2025-07-25 · Model Support: 11 changes in Release v0.1.14
  — Set port dynamically in VSCode extension and read from it in gemini-cli and send…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 928
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d33468787de63812ae66bcf4e3a5ad37c5d20dab7bc80c33d51b7a56e28dbc2c
product: gemini-cli
product_name: Gemini CLI
record:
  card_id: gemini-cli-2025-07-25-210aea
  comparison: ''
  date: '2025-07-25'
  description: 'Gemini CLI — Release v0.1.14: 11 Model Support changes'
  evidence:
  - quote: Set port dynamically in VSCode extension and read from it in gemini-cli
      and send initial notification by @chrstnb in https://github.com/google-gemini/gemini-cli/pull/4255
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.14
  - quote: Clarifies that Gemini Code Assist, when offered through the Google De…
      by @cdemeke in https://github.com/google-gemini/gemini-cli/pull/3086
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.14
  - quote: '[ide-mode] Add active file to user model request by @chrstnb in https://github.com/google-gemini/gemini-cli/pull/4312'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.14
  - quote: Implement loop check with LLM by @SandyTao520 in https://github.com/google-gemini/gemini-cli/pull/4337
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.14
  - quote: 'feat(cli): add warnings when gemini-cli is called in the root directory
      by @y-okt in https://github.com/google-gemini/gemini-cli/pull/4542'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.14
  - quote: 'feat(auth): support gemini api key and vertex auth in non-interactive
      mode by @jerop in https://github.com/google-gemini/gemini-cli/pull/4631'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.14
  - quote: 'feat(core): Resolve GEMINI_SYSTEM_MD case-insensitively by @olk in https://github.com/google-gemini/gemini-cli/pull/4538'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.14
  - quote: add notes on API keys and .gemini/.env to authentication.md by @slhck in
      https://github.com/google-gemini/gemini-cli/pull/2004
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.14
  - quote: Log when flash model decided to continue by @SandyTao520 in https://github.com/google-gemini/gemini-cli/pull/4698
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.14
  - quote: 'feat: add GEMINI_CLI environment variable to spawned shell commands by
      @taeold in https://github.com/google-gemini/gemini-cli/pull/4791'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.14
  - quote: 'Add "Gemini CLI: Run" command shortcut by @skeshive in https://github.com/google-gemini/gemini-cli/pull/4792'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.14
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: gemini-cli
  product_name: Gemini CLI
  slug: 11-model-support-changes-in-v0-1-14
  source_release: gemini-cli-2025-07-25-v0-1-14-github-235287807-631ef7fa
  source_type: github_releases
  theme: model-support
  title: 11 Model Support changes in v0.1.14
  type: change
related_changes:
- '[[Changes/Cline/2025-07-23-adding-support-for-new-models-qwen-3-models-on-qwen-provider-by-arafatkatze-in-h|Adding
  support for new models Qwen 3 models on Qwen provider]]'
- '[[Changes/Dify/2025-07-23-2-model-support-changes-in-1-7-0|2 Model Support changes
  in 1.7.0]]'
- '[[Changes/OpenHands/2025-07-24-2-model-support-changes-in-0-50-0|2 Model Support
  changes in 0.50.0]]'
source_release: '[[Releases/Gemini CLI/gemini-cli-2025-07-25-v0-1-14-github-235287807-631ef7fa|gemini-cli-2025-07-25-v0-1-14-github-235287807-631ef7fa]]'
source_type: github_releases
theme: model-support
title: 11 Model Support changes in v0.1.14
type: change
---

<!-- chronolog:begin region="header" -->
# 11 Model Support changes in v0.1.14

**Gemini CLI** · 2025-07-25 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.14) · from [[Releases/Gemini CLI/gemini-cli-2025-07-25-v0-1-14-github-235287807-631ef7fa|Release v0.1.14]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Set port dynamically in VSCode extension and read from it in gemini-cli and send initial notification by @chrstnb in https://github.com/google-gemini/gemini-cli/pull/4255

> Clarifies that Gemini Code Assist, when offered through the Google De… by @cdemeke in https://github.com/google-gemini/gemini-cli/pull/3086

> [ide-mode] Add active file to user model request by @chrstnb in https://github.com/google-gemini/gemini-cli/pull/4312

> Implement loop check with LLM by @SandyTao520 in https://github.com/google-gemini/gemini-cli/pull/4337

> feat(cli): add warnings when gemini-cli is called in the root directory by @y-okt in https://github.com/google-gemini/gemini-cli/pull/4542

> feat(auth): support gemini api key and vertex auth in non-interactive mode by @jerop in https://github.com/google-gemini/gemini-cli/pull/4631

> feat(core): Resolve GEMINI_SYSTEM_MD case-insensitively by @olk in https://github.com/google-gemini/gemini-cli/pull/4538

> add notes on API keys and .gemini/.env to authentication.md by @slhck in https://github.com/google-gemini/gemini-cli/pull/2004

> Log when flash model decided to continue by @SandyTao520 in https://github.com/google-gemini/gemini-cli/pull/4698

> feat: add GEMINI_CLI environment variable to spawned shell commands by @taeold in https://github.com/google-gemini/gemini-cli/pull/4791

> Add "Gemini CLI: Run" command shortcut by @skeshive in https://github.com/google-gemini/gemini-cli/pull/4792

Source: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.14
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Gemini CLI/2025-07-25-5-agent-mode-changes-in-v0-1-14|5 Agent Mode changes in v0.1.14]] · Agent Mode
- [[Changes/Gemini CLI/2025-07-25-run-model-availability-check-in-the-background-to-speed-up-startup-by-sandytao52|Run model availability check in the background to speed up startup]] · Reliability and Performance
- [[Changes/Gemini CLI/2025-07-25-2-context-window-changes-in-v0-1-14|2 Context Window changes in v0.1.14]] · Context Window
- [[Changes/Gemini CLI/2025-07-25-migrate-privacy-to-new-architecture-by-abhipatel12-in-https-github-com-google-ge|Migrate /privacy to new architecture]] · Safety and Privacy
- [[Changes/Gemini CLI/2025-07-25-4-account-and-access-changes-in-v0-1-14|4 Account and Access changes in v0.1.14]] · Account and Access
- [[Changes/Gemini CLI/2025-07-25-18-apps-and-integrations-changes-in-v0-1-14|18 Apps and Integrations changes in v0.1.14]] · Apps and Integrations
- [[Changes/Gemini CLI/2025-07-25-19-editor-experience-changes-in-v0-1-14|19 Editor Experience changes in v0.1.14]] · Editor Experience
- [[Changes/Gemini CLI/2025-07-25-2-mobile-and-desktop-changes-in-v0-1-14|2 Mobile and Desktop changes in v0.1.14]] · Mobile and Desktop
- [[Changes/Gemini CLI/2025-07-25-2-interface-experience-changes-in-v0-1-14|2 Interface Experience changes in v0.1.14]] · Interface Experience
- [[Changes/Gemini CLI/2025-07-25-16-developer-workflow-changes-in-v0-1-14|16 Developer Workflow changes in v0.1.14]] · Developer Workflow
- [[Changes/Gemini CLI/2025-07-25-4-automation-and-scheduling-changes-in-v0-1-14|4 Automation and Scheduling changes in v0.1.14]] · Automation and Scheduling
- [[Changes/Gemini CLI/2025-07-25-feat-memory-make-directory-search-limit-on-memory-discovery-configurable-with-se|feat(memory): make directory search limit on memory discovery configurable…]] · Memory and Personalization
- [[Changes/Gemini CLI/2025-07-25-57-other-changes-in-v0-1-14|57 other changes in v0.1.14]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2025-07-24 · OpenHands · [[Changes/OpenHands/2025-07-24-2-model-support-changes-in-0-50-0|2 Model Support changes in 0.50.0]]
- Later: 2025-07-28 · Dify · [[Changes/Dify/2025-07-28-2-model-support-changes-in-1-7-1|2 Model Support changes in 1.7.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20gemini-cli-2025-07-25-210aea&body=Card%3A%20Changes%2FGemini%20CLI%2F2025-07-25-11-model-support-changes-in-v0-1-14.md%0ACard%20ID%3A%20gemini-cli-2025-07-25-210aea%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgoogle-gemini%2Fgemini-cli%2Freleases%2Ftag%2Fv0.1.14%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->