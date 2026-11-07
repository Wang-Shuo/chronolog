---
card_id: gemini-cli-2026-03-17-df0c81
date: '2026-03-17'
description: 'Gemini CLI · 2026-03-17 · Model Support: 5 changes in Release v0.34.0
  — feat(loop-reduction): implement iterative loop detection and model feedback by…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1163
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 0e61d4e12b1e9b725f014eca8d4331a3bb8528c237993e8377ea1705b5434705
product: gemini-cli
product_name: Gemini CLI
record:
  card_id: gemini-cli-2026-03-17-df0c81
  comparison: ''
  date: '2026-03-17'
  description: 'Gemini CLI — Release v0.34.0: 5 Model Support changes'
  evidence:
  - quote: 'feat(loop-reduction): implement iterative loop detection and model feedback
      by @aishaneeshah in https://github.com/google-gemini/gemini-cli/pull/20763'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.34.0
  - quote: 'feat(core): fallback to 2.5 models with no access for toolcalls by @sehoon38
      in https://github.com/google-gemini/gemini-cli/pull/21283'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.34.0
  - quote: Make test suite pass when the GEMINI_SYSTEM_MD env variable or GEMINI_WRITE_SYSTEM_MD
      variable happens to be set locally/ by @jacob314 in https://github.com/google-gemini/gemini-cli/pull/21480
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.34.0
  - quote: 'feat(core): add per-model token usage to stream-json output by @yongruilin
      in https://github.com/google-gemini/gemini-cli/pull/21839'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.34.0
  - quote: 'docs(cli): mention per-model token usage in stream-json result event by
      @yongruilin in https://github.com/google-gemini/gemini-cli/pull/21908'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.34.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: gemini-cli
  product_name: Gemini CLI
  slug: 5-model-support-changes-in-v0-34-0
  source_release: gemini-cli-2026-03-17-v0-34-0-github-298158994-68230a41
  source_type: github_releases
  theme: model-support
  title: 5 Model Support changes in v0.34.0
  type: change
related_changes:
- '[[Changes/Descript/2026-03-17-heads-up-for-existing-projects|Heads up for existing
  projects]]'
- '[[Changes/Descript/2026-03-17-updated-the-underlying-model-powering-regenerate-to-improve-how-natural-the-outp|Updated
  the underlying model powering Regenerate to improve how natural the output sounds]]'
- '[[Changes/Dify/2026-03-17-18-model-support-changes-in-1-13-1|18 Model Support changes
  in 1.13.1]]'
source_release: '[[Releases/Gemini CLI/gemini-cli-2026-03-17-v0-34-0-github-298158994-68230a41|gemini-cli-2026-03-17-v0-34-0-github-298158994-68230a41]]'
source_type: github_releases
theme: model-support
title: 5 Model Support changes in v0.34.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Model Support changes in v0.34.0

**Gemini CLI** · 2026-03-17 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/google-gemini/gemini-cli/releases/tag/v0.34.0) · from [[Releases/Gemini CLI/gemini-cli-2026-03-17-v0-34-0-github-298158994-68230a41|Release v0.34.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> feat(loop-reduction): implement iterative loop detection and model feedback by @aishaneeshah in https://github.com/google-gemini/gemini-cli/pull/20763

> feat(core): fallback to 2.5 models with no access for toolcalls by @sehoon38 in https://github.com/google-gemini/gemini-cli/pull/21283

> Make test suite pass when the GEMINI_SYSTEM_MD env variable or GEMINI_WRITE_SYSTEM_MD variable happens to be set locally/ by @jacob314 in https://github.com/google-gemini/gemini-cli/pull/21480

> feat(core): add per-model token usage to stream-json output by @yongruilin in https://github.com/google-gemini/gemini-cli/pull/21839

> docs(cli): mention per-model token usage in stream-json result event by @yongruilin in https://github.com/google-gemini/gemini-cli/pull/21908

Source: https://github.com/google-gemini/gemini-cli/releases/tag/v0.34.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Gemini CLI/2026-03-17-feat-voice-implement-speech-friendly-response-formatter-by-ayush31010-in-https-g|feat(voice): implement speech-friendly response formatter]] · Voice and Audio
- [[Changes/Gemini CLI/2026-03-17-refactor-core-extract-shared-oauth-flow-primitives-from-mcpoauthprovider-by-sand|refactor(core): extract shared OAuth flow primitives from MCPOAuthProvider]] · Account and Access
- [[Changes/Gemini CLI/2026-03-17-2-pricing-model-changes-in-v0-34-0|2 Pricing Model changes in v0.34.0]] · Pricing Model
- [[Changes/Gemini CLI/2026-03-17-3-safety-and-privacy-changes-in-v0-34-0|3 Safety and Privacy changes in v0.34.0]] · Safety and Privacy
- [[Changes/Gemini CLI/2026-03-17-9-developer-workflow-changes-in-v0-34-0|9 Developer Workflow changes in v0.34.0]] · Developer Workflow
- [[Changes/Gemini CLI/2026-03-17-3-interface-experience-changes-in-v0-34-0|3 Interface Experience changes in v0.34.0]] · Interface Experience
- [[Changes/Gemini CLI/2026-03-17-4-apps-and-integrations-changes-in-v0-34-0|4 Apps and Integrations changes in v0.34.0]] · Apps and Integrations
- [[Changes/Gemini CLI/2026-03-17-docs-add-documentation-for-notifications-experimental-macos-by-jkcinouye-in-http|Docs: Add documentation for notifications (experimental)(macOS)]] · Mobile and Desktop
- [[Changes/Gemini CLI/2026-03-17-docs-document-tool-exclusion-from-memory-via-deny-policy-by-abhijit-2592-in-http|docs: document tool exclusion from memory via deny policy]] · Memory and Personalization
- [[Changes/Gemini CLI/2026-03-17-docs-document-planning-workflows-with-conductor-example-by-jerop-in-https-github|docs: document planning workflows with Conductor example]] · Files and Data
- [[Changes/Gemini CLI/2026-03-17-7-agent-mode-changes-in-v0-34-0|7 Agent Mode changes in v0.34.0]] · Agent Mode
- [[Changes/Gemini CLI/2026-03-17-feat-core-improve-file-autocomplete-to-prioritize-filenames-by-sehoon38-in-https|feat(core): improve @file autocomplete to prioritize filenames]] · Editor Experience
- [[Changes/Gemini CLI/2026-03-17-2-automation-and-scheduling-changes-in-v0-34-0|2 Automation and Scheduling changes in v0.34.0]] · Automation and Scheduling
- [[Changes/Gemini CLI/2026-03-17-78-other-changes-in-v0-34-0|78 other changes in v0.34.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-03-17 · Dify · [[Changes/Dify/2026-03-17-18-model-support-changes-in-1-13-1|18 Model Support changes in 1.13.1]]
- Later: 2026-03-17 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-03-17-2-model-support-changes-in-v1-0-7|2 Model Support changes in v1.0.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20gemini-cli-2026-03-17-df0c81&body=Card%3A%20Changes%2FGemini%20CLI%2F2026-03-17-5-model-support-changes-in-v0-34-0.md%0ACard%20ID%3A%20gemini-cli-2026-03-17-df0c81%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgoogle-gemini%2Fgemini-cli%2Freleases%2Ftag%2Fv0.34.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->