---
card_id: gemini-cli-2025-08-14-e9ac27
date: '2025-08-14'
description: 'Gemini CLI · 2025-08-14 · Model Support: 28 changes in Release v0.1.21
  — Set port dynamically in VSCode extension and read from it in gemini-cli and send…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 948
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9f437003f39978526a589d9babeb5f1364f0a8bbf27eea9fe3c0670abc353ae4
product: gemini-cli
product_name: Gemini CLI
record:
  card_id: gemini-cli-2025-08-14-e9ac27
  comparison: ''
  date: '2025-08-14'
  description: 'Gemini CLI — Release v0.1.21: 28 Model Support changes'
  evidence:
  - quote: Set port dynamically in VSCode extension and read from it in gemini-cli
      and send initial notification by @chrstnb in https://github.com/google-gemini/gemini-cli/pull/4255
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.21
  - quote: Clarifies that Gemini Code Assist, when offered through the Google De…
      by @cdemeke in https://github.com/google-gemini/gemini-cli/pull/3086
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.21
  - quote: '[ide-mode] Add active file to user model request by @chrstnb in https://github.com/google-gemini/gemini-cli/pull/4312'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.21
  - quote: Implement loop check with LLM by @SandyTao520 in https://github.com/google-gemini/gemini-cli/pull/4337
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.21
  - quote: 'feat(cli): add warnings when gemini-cli is called in the root directory
      by @y-okt in https://github.com/google-gemini/gemini-cli/pull/4542'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.21
  - quote: 'feat(auth): support gemini api key and vertex auth in non-interactive
      mode by @jerop in https://github.com/google-gemini/gemini-cli/pull/4631'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.21
  - quote: 'feat(core): Resolve GEMINI_SYSTEM_MD case-insensitively by @olk in https://github.com/google-gemini/gemini-cli/pull/4538'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.21
  - quote: add notes on API keys and .gemini/.env to authentication.md by @slhck in
      https://github.com/google-gemini/gemini-cli/pull/2004
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.21
  - quote: Log when flash model decided to continue by @SandyTao520 in https://github.com/google-gemini/gemini-cli/pull/4698
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.21
  - quote: 'feat: add GEMINI_CLI environment variable to spawned shell commands by
      @taeold in https://github.com/google-gemini/gemini-cli/pull/4791'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.21
  - quote: 'Add "Gemini CLI: Run" command shortcut by @skeshive in https://github.com/google-gemini/gemini-cli/pull/4792'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.21
  - quote: (model) - Use Flash Lite For Next Speaker Checks by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/4991
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.21
  - quote: Refactors companion VS Code extension to import & use notification schema
      defined in gemini-cli by @skeshive in https://github.com/google-gemini/gemini-cli/pull/5059
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.21
  - quote: Adds docs outlining keyboard shortcuts for gemini-cli by @Dannyzen in https://github.com/google-gemini/gemini-cli/pull/4727
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.21
  - quote: Only enable IDE integration if gemini-cli is running in the same path as
      open workspace by @skeshive in https://github.com/google-gemini/gemini-cli/pull/5068
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.21
  - quote: 'feat(cli): introduce /init command for GEMINI.md creation by @shamso-goog
      in https://github.com/google-gemini/gemini-cli/pull/4852'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.21
  - quote: 'feat(docs): document GEMINI.md import syntax by @allenhutchison in https://github.com/google-gemini/gemini-cli/pull/5145'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.21
  - quote: do not mention GEMINI.md in system prompt as it is not fixed and can confuse
      model as it is not mentioned by memory tool and memory file paths are generally
      not exposed to model (yet) by @olcan in https://github.com/google-gemini/gemini-cli/pull/5202
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.21
  - quote: Update gemini-automated-issue-triage.yml by @raushanraj in https://github.com/google-gemini/gemini-cli/pull/5312
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.21
  - quote: Switch utility calls to use the gemini-2.5-flash-lite model by @mrcabbage972
      in https://github.com/google-gemini/gemini-cli/pull/5193
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.21
  - quote: 'refactor: use `google-github-actions/run-gemini-cli` action by @gsquared94
      in https://github.com/google-gemini/gemini-cli/pull/5643'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.21
  - quote: 'feat(mcp): add `gemini mcp` commands for `add`, `remove` and `list` by
      @jackwotherspoon in https://github.com/google-gemini/gemini-cli/pull/5481'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.21
  - quote: 'feat(cli): get the run-gemini-cli version from the GitHub API by @sethvargo
      in https://github.com/google-gemini/gemini-cli/pull/5708'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.21
  - quote: 'update: `google-github-actions/run-gemini-cli` version in workflows by
      @gsquared94 in https://github.com/google-gemini/gemini-cli/pull/5802'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.21
  - quote: 'chore(telemetry): Log `FIREBASE_STUDIO` when using Gemini CLI within Firebase
      Studio by @richieforeman in https://github.com/google-gemini/gemini-cli/pull/5790'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.21
  - quote: 'feat: add humorous tip for new line shortcut in Gemini CLI by @JayadityaGit
      in https://github.com/google-gemini/gemini-cli/pull/5666'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.21
  - quote: Bump version number of companion extension to match next Gemini CLI version
      number by @skeshive in https://github.com/google-gemini/gemini-cli/pull/6065
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.21
  - quote: 'chore(gemini.md): Make the checkExhaustive helper section more brief/direct
      by @richieforeman in https://github.com/google-gemini/gemini-cli/pull/6181'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.21
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: gemini-cli
  product_name: Gemini CLI
  slug: 28-model-support-changes-in-v0-1-21
  source_release: gemini-cli-2025-08-14-v0-1-21-github-239867721-f576cbaa
  source_type: github_releases
  theme: model-support
  title: 28 Model Support changes in v0.1.21
  type: change
related_changes:
- '[[Changes/Gemini CLI/2025-08-12-7-model-support-changes-in-v0-1-19|7 Model Support
  changes in v0.1.19]]'
- '[[Changes/Cline/2025-08-13-4-model-support-changes-in-v3-24-0|4 Model Support changes
  in v3.24.0]]'
- '[[Changes/OpenHands/2025-08-13-3-model-support-changes-in-0-52-0|3 Model Support
  changes in 0.52.0]]'
source_release: '[[Releases/Gemini CLI/gemini-cli-2025-08-14-v0-1-21-github-239867721-f576cbaa|gemini-cli-2025-08-14-v0-1-21-github-239867721-f576cbaa]]'
source_type: github_releases
theme: model-support
title: 28 Model Support changes in v0.1.21
type: change
---

<!-- chronolog:begin region="header" -->
# 28 Model Support changes in v0.1.21

**Gemini CLI** · 2025-08-14 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.21) · from [[Releases/Gemini CLI/gemini-cli-2025-08-14-v0-1-21-github-239867721-f576cbaa|Release v0.1.21]]
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

> (model) - Use Flash Lite For Next Speaker Checks by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/4991

> Refactors companion VS Code extension to import & use notification schema defined in gemini-cli by @skeshive in https://github.com/google-gemini/gemini-cli/pull/5059

> Adds docs outlining keyboard shortcuts for gemini-cli by @Dannyzen in https://github.com/google-gemini/gemini-cli/pull/4727

> Only enable IDE integration if gemini-cli is running in the same path as open workspace by @skeshive in https://github.com/google-gemini/gemini-cli/pull/5068

> feat(cli): introduce /init command for GEMINI.md creation by @shamso-goog in https://github.com/google-gemini/gemini-cli/pull/4852

> feat(docs): document GEMINI.md import syntax by @allenhutchison in https://github.com/google-gemini/gemini-cli/pull/5145

> do not mention GEMINI.md in system prompt as it is not fixed and can confuse model as it is not mentioned by memory tool and memory file paths are generally not exposed to model (yet) by @olcan in https://github.com/google-gemini/gemini-cli/pull/5202

> Update gemini-automated-issue-triage.yml by @raushanraj in https://github.com/google-gemini/gemini-cli/pull/5312

> Switch utility calls to use the gemini-2.5-flash-lite model by @mrcabbage972 in https://github.com/google-gemini/gemini-cli/pull/5193

> refactor: use `google-github-actions/run-gemini-cli` action by @gsquared94 in https://github.com/google-gemini/gemini-cli/pull/5643

> feat(mcp): add `gemini mcp` commands for `add`, `remove` and `list` by @jackwotherspoon in https://github.com/google-gemini/gemini-cli/pull/5481

> feat(cli): get the run-gemini-cli version from the GitHub API by @sethvargo in https://github.com/google-gemini/gemini-cli/pull/5708

> update: `google-github-actions/run-gemini-cli` version in workflows by @gsquared94 in https://github.com/google-gemini/gemini-cli/pull/5802

> chore(telemetry): Log `FIREBASE_STUDIO` when using Gemini CLI within Firebase Studio by @richieforeman in https://github.com/google-gemini/gemini-cli/pull/5790

> feat: add humorous tip for new line shortcut in Gemini CLI by @JayadityaGit in https://github.com/google-gemini/gemini-cli/pull/5666

> Bump version number of companion extension to match next Gemini CLI version number by @skeshive in https://github.com/google-gemini/gemini-cli/pull/6065

> chore(gemini.md): Make the checkExhaustive helper section more brief/direct by @richieforeman in https://github.com/google-gemini/gemini-cli/pull/6181

Source: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.21
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Gemini CLI/2025-08-14-39-developer-workflow-changes-in-v0-1-21|39 Developer Workflow changes in v0.1.21]] · Developer Workflow
- [[Changes/Gemini CLI/2025-08-14-7-agent-mode-changes-in-v0-1-21|7 Agent Mode changes in v0.1.21]] · Agent Mode
- [[Changes/Gemini CLI/2025-08-14-3-interface-experience-changes-in-v0-1-21|3 Interface Experience changes in v0.1.21]] · Interface Experience
- [[Changes/Gemini CLI/2025-08-14-6-reliability-and-performance-changes-in-v0-1-21|6 Reliability and Performance changes in v0.1.21]] · Reliability and Performance
- [[Changes/Gemini CLI/2025-08-14-feat-core-parse-multimodal-mcp-tool-responses-by-luccasparoni-in-https-github-co|feat(core): Parse Multimodal MCP Tool responses]] · Multimodal Input
- [[Changes/Gemini CLI/2025-08-14-6-context-window-changes-in-v0-1-21|6 Context Window changes in v0.1.21]] · Context Window
- [[Changes/Gemini CLI/2025-08-14-41-apps-and-integrations-changes-in-v0-1-21|41 Apps and Integrations changes in v0.1.21]] · Apps and Integrations
- [[Changes/Gemini CLI/2025-08-14-2-mobile-and-desktop-changes-in-v0-1-21|2 Mobile and Desktop changes in v0.1.21]] · Mobile and Desktop
- [[Changes/Gemini CLI/2025-08-14-3-memory-and-personalization-changes-in-v0-1-21|3 Memory and Personalization changes in v0.1.21]] · Memory and Personalization
- [[Changes/Gemini CLI/2025-08-14-8-automation-and-scheduling-changes-in-v0-1-21|8 Automation and Scheduling changes in v0.1.21]] · Automation and Scheduling
- [[Changes/Gemini CLI/2025-08-14-document-certificate-issue-workaround-by-scidomino-in-https-github-com-google-ge|Document certificate issue workaround]] · Files and Data
- [[Changes/Gemini CLI/2025-08-14-7-account-and-access-changes-in-v0-1-21|7 Account and Access changes in v0.1.21]] · Account and Access
- [[Changes/Gemini CLI/2025-08-14-7-safety-and-privacy-changes-in-v0-1-21|7 Safety and Privacy changes in v0.1.21]] · Safety and Privacy
- [[Changes/Gemini CLI/2025-08-14-35-editor-experience-changes-in-v0-1-21|35 Editor Experience changes in v0.1.21]] · Editor Experience
- [[Changes/Gemini CLI/2025-08-14-181-other-changes-in-v0-1-21|181 other changes in v0.1.21]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2025-08-13 · OpenHands · [[Changes/OpenHands/2025-08-13-3-model-support-changes-in-0-52-0|3 Model Support changes in 0.52.0]]
- Later: 2025-08-15 · ChatGPT · [[Changes/ChatGPT/2025-08-15-we-re-making-gpt-5-s-default-personality-warmer-and-more-familiar-this-is-in-res-19a03e|GPT-5 Updates]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20gemini-cli-2025-08-14-e9ac27&body=Card%3A%20Changes%2FGemini%20CLI%2F2025-08-14-28-model-support-changes-in-v0-1-21.md%0ACard%20ID%3A%20gemini-cli-2025-08-14-e9ac27%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgoogle-gemini%2Fgemini-cli%2Freleases%2Ftag%2Fv0.1.21%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->