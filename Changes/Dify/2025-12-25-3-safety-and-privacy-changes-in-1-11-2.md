---
card_id: dify-2025-12-25-fdd520
date: '2025-12-25'
description: 'Dify · 2025-12-25 · Safety and Privacy: 3 changes in v1.11.2 — **Security
  Enhancements**: We''ve patched an XSS vulnerability with the Mermaid Graph and tackled…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1976
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 4fd6b116f80ebff42dd6c90dcf9dd27544334fce4f8a8b0cacf0fabd1076bf4d
product: dify
product_name: Dify
record:
  card_id: dify-2025-12-25-fdd520
  comparison: ''
  date: '2025-12-25'
  description: 'Dify — v1.11.2: 3 Safety and Privacy changes'
  evidence:
  - quote: '**Security Enhancements**: We''ve patched an XSS vulnerability with the
      Mermaid Graph and tackled SSRF and CSV injection issues. Kudos to @zyssyz123
      and @laipz8200. (#29811, #29462)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.11.2
  - quote: 'revert: "security/fix-swagger-info-leak-m02" by @crazywoola in https://github.com/langgenius/dify/pull/29721'
    source_release: https://github.com/langgenius/dify/releases/tag/1.11.2
  - quote: 'feat: sandbox retention basic settings by @hj24 in https://github.com/langgenius/dify/pull/29842'
    source_release: https://github.com/langgenius/dify/releases/tag/1.11.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 3-safety-and-privacy-changes-in-1-11-2
  source_release: dify-2025-12-25-1-11-2-github-272776889-1d40e2fa
  source_type: github_releases
  theme: safety-privacy
  title: 3 Safety and Privacy changes in 1.11.2
  type: change
related_changes:
- '[[Changes/Open WebUI/2025-12-21-6-safety-and-privacy-changes-in-v0-6-42|6 Safety
  and Privacy changes in v0.6.42]]'
- '[[Changes/Cursor/2025-12-22-improved-stability-around-how-the-agent-respects-auto-run-preferences-to-prevent|Improved
  stability around how the agent respects auto-run preferences to prevent…]]'
- '[[Changes/Lovable/2025-12-23-public-preview-link-controls|Public preview link controls]]'
source_release: '[[Releases/Dify/dify-2025-12-25-1-11-2-github-272776889-1d40e2fa|dify-2025-12-25-1-11-2-github-272776889-1d40e2fa]]'
source_type: github_releases
theme: safety-privacy
title: 3 Safety and Privacy changes in 1.11.2
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Safety and Privacy changes in 1.11.2

**Dify** · 2025-12-25 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.11.2) · from [[Releases/Dify/dify-2025-12-25-1-11-2-github-272776889-1d40e2fa|v1.11.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **Security Enhancements**: We've patched an XSS vulnerability with the Mermaid Graph and tackled SSRF and CSV injection issues. Kudos to @zyssyz123 and @laipz8200. (#29811, #29462)

> revert: "security/fix-swagger-info-leak-m02" by @crazywoola in https://github.com/langgenius/dify/pull/29721

> feat: sandbox retention basic settings by @hj24 in https://github.com/langgenius/dify/pull/29842

Source: https://github.com/langgenius/dify/releases/tag/1.11.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2025-12-25-feat-show-generate-speed-in-chatbot-by-leslie2046-in-https-github-com-langgenius|feat: show generate speed in chatbot]] · Reliability and Performance
- [[Changes/Dify/2025-12-25-test-add-unit-tests-for-datasetconfig-component-with-comprehensive-coverage-of-r|test: add unit tests for DatasetConfig component with comprehensive coverage…]] · Context Window
- [[Changes/Dify/2025-12-25-2-agent-mode-changes-in-1-11-2|2 Agent Mode changes in 1.11.2]] · Agent Mode
- [[Changes/Dify/2025-12-25-chore-add-apptypeselector-tests-and-improve-clear-button-accessibility-by-lyzno1|chore: add AppTypeSelector tests and improve clear button accessibility]] · Accessibility and Localization
- [[Changes/Dify/2025-12-25-12-apps-and-integrations-changes-in-1-11-2|12 Apps and Integrations changes in 1.11.2]] · Apps and Integrations
- [[Changes/Dify/2025-12-25-3-pricing-model-changes-in-1-11-2|3 Pricing Model changes in 1.11.2]] · Pricing Model
- [[Changes/Dify/2025-12-25-refactor-create-shared-react-i18next-mock-to-reduce-duplication-by-lyzno1-in-htt|refactor: create shared react-i18next mock to reduce duplication]] · Collaboration
- [[Changes/Dify/2025-12-25-2-developer-workflow-changes-in-1-11-2|2 Developer Workflow changes in 1.11.2]] · Developer Workflow
- [[Changes/Dify/2025-12-25-refactor-split-changes-for-api-controllers-web-audio-py-by-asukaminato0721-in-ht|refactor: split changes for api/controllers/web/audio.py]] · Voice and Audio
- [[Changes/Dify/2025-12-25-2-editor-experience-changes-in-1-11-2|2 Editor Experience changes in 1.11.2]] · Editor Experience
- [[Changes/Dify/2025-12-25-add-file-upload-enabled-check-and-new-i18n-message-by-halogen22-in-https-github|Add file upload enabled check and new i18n message]] · Files and Data
- [[Changes/Dify/2025-12-25-feat-add-type-field-to-pipelinerecommendedplugin-model-add-query-param-type-to-r|feat: Add "type" field to PipelineRecommendedPlugin model]] · Model Support
- [[Changes/Dify/2025-12-25-chore-remove-unused-login-call-from-activation-flow-by-hjlarry-in-https-github-c|chore: remove unused login call from activation flow]] · Account and Access
- [[Changes/Dify/2025-12-25-137-other-changes-in-1-11-2|137 other changes in 1.11.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2025-12-23 · Lovable · [[Changes/Lovable/2025-12-23-public-preview-link-controls|Public preview link controls]]
- Later: 2025-12-26 · Replit · [[Changes/Replit/2025-12-26-security-center-for-enterprise|Security Center for Enterprise]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2025-12-25-fdd520&body=Card%3A%20Changes%2FDify%2F2025-12-25-3-safety-and-privacy-changes-in-1-11-2.md%0ACard%20ID%3A%20dify-2025-12-25-fdd520%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.11.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->