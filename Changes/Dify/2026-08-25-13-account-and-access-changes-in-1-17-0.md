---
card_id: dify-2026-08-25-a1329e
date: '2026-08-25'
description: 'Dify · 2026-08-25 · Account and Access: 13 changes in v1.17.0 — Optional
  Turnstile challenge on sign-in and email-code login to protect authentication…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1244
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 4994e63a8cd88e88c65b64f5d07c5b994f333d105ac20fd0220e26a2b65918f5
product: dify
product_name: Dify
record:
  card_id: dify-2026-08-25-a1329e
  comparison: ''
  date: '2026-08-25'
  description: 'Dify — v1.17.0: 13 Account and Access changes'
  evidence:
  - quote: Optional Turnstile challenge on sign-in and email-code login to protect
      authentication endpoints from abuse, with configurable site/secret keys and
      allowed hostnames (#40494).
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: '**Authentication hardening**: Turnstile challenge on login/email-code
      flows, hardened email-code verification with attempt limits and token expiry
      (`EMAIL_CODE_LOGIN_MAX_ATTEMPTS`, `EMAIL_CODE_LOGIN_TOKEN_EXPIRY_MINUTES`),
      suspended-email-domain handling, and short-lived agent authorization tokens
      (#40494, #40960, #41004, #40884).'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: '**Access-control / ownership scoping**: dataset, document, RAG, conversation,
      workspace-credential, and OAuth-client resources are now consistently bound
      to their owners and app scope, closing several unauthorized-access paths (#40989,
      #40888, #40790, #40745, #40893, #40786, and related).'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'Numerous webapp/UI fixes: restore email-code and password form submissions,
      mobile sign-in overflow, toast stacking, model selector spacing (#40227, #40222,
      #40921, #40970, #8d612895).'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: '`EMAIL_CODE_LOGIN_MAX_ATTEMPTS`, `EMAIL_CODE_LOGIN_TOKEN_EXPIRY_MINUTES`'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: '`add_oauth_provider_app_auto_authorize` — silent OAuth authorization flag'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: move OAuth server service coverage to unit tests by @asukaminato0721
      in https://github.com/langgenius/dify/pull/38931'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: use sqlite3 session in test_web_login by @asukaminato0721 in https://github.com/langgenius/dify/pull/38725'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'chore: dep inject for model in oauth server by @likalikali in https://github.com/langgenius/dify/pull/40147'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'feat(oauth): drive silent authorization from oauth_provider_apps.auto_authorize
      by @lin-snow in https://github.com/langgenius/dify/pull/40783'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'feat(plugin-auth): visibility picker for OAuth credentials by @ForeignKeyCN
      in https://github.com/langgenius/dify/pull/39840'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'refactor(controllers/web): dep-inject login and forgot-password payloads
      (#36659) by @weike-zhang in https://github.com/langgenius/dify/pull/40856'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'refactor(api): move account access behind application services by @41tair
      in https://github.com/langgenius/dify/pull/40437'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 13-account-and-access-changes-in-1-17-0
  source_release: dify-2026-08-25-1-17-0-github-376348099-66c16161
  source_type: github_releases
  theme: account-access
  title: 13 Account and Access changes in 1.17.0
  type: change
related_changes:
- '[[Changes/OpenCode/2026-08-24-core-fixed-opencode-device-login-links-when-servers-return-relative-verification|Core
  Fixed OpenCode device login links when servers return relative verification…]]'
- '[[Changes/ChatGPT/2026-08-25-chatgpt-work-s-browser-on-web-and-mobile-can-also-help-you-get-tasks-done-on-som-99be54|ChatGPT
  Work can now complete tasks on signed-in websites]]'
- '[[Changes/Claude Code/2026-08-25-improved-attribution-of-usage-telemetry-to-your-organization-for-workload-identi|Improved
  attribution of usage telemetry to your organization for workload identity…]]'
source_release: '[[Releases/Dify/dify-2026-08-25-1-17-0-github-376348099-66c16161|dify-2026-08-25-1-17-0-github-376348099-66c16161]]'
source_type: github_releases
theme: account-access
title: 13 Account and Access changes in 1.17.0
type: change
---

<!-- chronolog:begin region="header" -->
# 13 Account and Access changes in 1.17.0

**Dify** · 2026-08-25 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.17.0) · from [[Releases/Dify/dify-2026-08-25-1-17-0-github-376348099-66c16161|v1.17.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Optional Turnstile challenge on sign-in and email-code login to protect authentication endpoints from abuse, with configurable site/secret keys and allowed hostnames (#40494).

> **Authentication hardening**: Turnstile challenge on login/email-code flows, hardened email-code verification with attempt limits and token expiry (`EMAIL_CODE_LOGIN_MAX_ATTEMPTS`, `EMAIL_CODE_LOGIN_TOKEN_EXPIRY_MINUTES`), suspended-email-domain handling, and short-lived agent authorization tokens (#40494, #40960, #41004, #40884).

> **Access-control / ownership scoping**: dataset, document, RAG, conversation, workspace-credential, and OAuth-client resources are now consistently bound to their owners and app scope, closing several unauthorized-access paths (#40989, #40888, #40790, #40745, #40893, #40786, and related).

> Numerous webapp/UI fixes: restore email-code and password form submissions, mobile sign-in overflow, toast stacking, model selector spacing (#40227, #40222, #40921, #40970, #8d612895).

> `EMAIL_CODE_LOGIN_MAX_ATTEMPTS`, `EMAIL_CODE_LOGIN_TOKEN_EXPIRY_MINUTES`

> `add_oauth_provider_app_auto_authorize` — silent OAuth authorization flag

> test: move OAuth server service coverage to unit tests by @asukaminato0721 in https://github.com/langgenius/dify/pull/38931

> test: use sqlite3 session in test_web_login by @asukaminato0721 in https://github.com/langgenius/dify/pull/38725

> chore: dep inject for model in oauth server by @likalikali in https://github.com/langgenius/dify/pull/40147

> feat(oauth): drive silent authorization from oauth_provider_apps.auto_authorize by @lin-snow in https://github.com/langgenius/dify/pull/40783

> feat(plugin-auth): visibility picker for OAuth credentials by @ForeignKeyCN in https://github.com/langgenius/dify/pull/39840

> refactor(controllers/web): dep-inject login and forgot-password payloads (#36659) by @weike-zhang in https://github.com/langgenius/dify/pull/40856

> refactor(api): move account access behind application services by @41tair in https://github.com/langgenius/dify/pull/40437

Source: https://github.com/langgenius/dify/releases/tag/1.17.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-08-25-2-enterprise-and-administration-changes-in-1-17-0|2 Enterprise and Administration changes in 1.17.0]] · Enterprise and Administration
- [[Changes/Dify/2026-08-25-audio-asr-now-accepts-audio-x-m4a-and-audio-mime-types-are-validated-more-accura|Audio ASR now accepts audio/x-m4a, and audio MIME types are validated more…]] · Voice and Audio
- [[Changes/Dify/2026-08-25-5-collaboration-changes-in-1-17-0|5 Collaboration changes in 1.17.0]] · Collaboration
- [[Changes/Dify/2026-08-25-16-safety-and-privacy-changes-in-1-17-0|16 Safety and Privacy changes in 1.17.0]] · Safety and Privacy
- [[Changes/Dify/2026-08-25-feat-workflow-support-human-input-in-loop-and-iteration-by-laipz8200-in-https-gi|feat(workflow): support human input in loop and iteration]] · Automation and Scheduling
- [[Changes/Dify/2026-08-25-4-editor-experience-changes-in-1-17-0|4 Editor Experience changes in 1.17.0]] · Editor Experience
- [[Changes/Dify/2026-08-25-3-multimodal-input-changes-in-1-17-0|3 Multimodal Input changes in 1.17.0]] · Multimodal Input
- [[Changes/Dify/2026-08-25-53-agent-mode-changes-in-1-17-0|53 Agent Mode changes in 1.17.0]] · Agent Mode
- [[Changes/Dify/2026-08-25-4-developer-workflow-changes-in-1-17-0|4 Developer Workflow changes in 1.17.0]] · Developer Workflow
- [[Changes/Dify/2026-08-25-93-model-support-changes-in-1-17-0|93 Model Support changes in 1.17.0]] · Model Support
- [[Changes/Dify/2026-08-25-28-apps-and-integrations-changes-in-1-17-0|28 Apps and Integrations changes in 1.17.0]] · Apps and Integrations
- [[Changes/Dify/2026-08-25-7-pricing-model-changes-in-1-17-0|7 Pricing Model changes in 1.17.0]] · Pricing Model
- [[Changes/Dify/2026-08-25-5-files-and-data-changes-in-1-17-0|5 Files and Data changes in 1.17.0]] · Files and Data
- [[Changes/Dify/2026-08-25-workflow-runtime-stability|Workflow & Runtime Stability]] · Reliability and Performance
- [[Changes/Dify/2026-08-25-8-context-window-changes-in-1-17-0|8 Context Window changes in 1.17.0]] · Context Window
- [[Changes/Dify/2026-08-25-9-interface-experience-changes-in-1-17-0|9 Interface Experience changes in 1.17.0]] · Interface Experience
- [[Changes/Dify/2026-08-25-3-accessibility-and-localization-changes-in-1-17-0|3 Accessibility and Localization changes in 1.17.0]] · Accessibility and Localization
- [[Changes/Dify/2026-08-25-351-other-changes-in-1-17-0|351 other changes in 1.17.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-08-25 · Claude Code · [[Changes/Claude Code/2026-08-25-improved-attribution-of-usage-telemetry-to-your-organization-for-workload-identi|Improved attribution of usage telemetry to your organization for workload identity…]]
- Later: 2026-08-25 · Open WebUI · [[Changes/Open WebUI/2026-08-25-13-account-and-access-changes-in-v0-11-1|13 Account and Access changes in v0.11.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-08-25-a1329e&body=Card%3A%20Changes%2FDify%2F2026-08-25-13-account-and-access-changes-in-1-17-0.md%0ACard%20ID%3A%20dify-2026-08-25-a1329e%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.17.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->