---
card_id: open-webui-2025-09-09-8243b9
date: '2025-09-09'
description: "Open WebUI · 2025-09-09 · Safety and Privacy: 4 changes in v0.6.27 —
  \U0001F512 Conditional Permission Hardening for OpenShift Deployments: Added a build
  argument to…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1869
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ad4c6947e795d957e38430cff04797cab619182eb56e31a8b427a34398c32cd7
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-09-09-8243b9
  comparison: ''
  date: '2025-09-09'
  description: 'Open WebUI — v0.6.27: 4 Safety and Privacy changes'
  evidence:
  - quote: "\U0001F512 Conditional Permission Hardening for OpenShift Deployments:
      Added a build argument to enable optional permission hardening for OpenShift
      and container environments. [Commit](https://github.com/open-webui/open-webui/pull/17070/commits/0ebe4f8f8490451ac8e85a4846f010854d9b54e5)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.27
  - quote: "\U0001F510 Resolved a security issue where a global web search setting
      overrode model-specific restrictions, ensuring model-level settings are now
      correctly prioritized. [#17151](https://github.com/open-webui/open-webui/issues/17151),
      [Commit](https://github.com/open-webui/open-webui/commit/9368d0ac751ec3072d5a96712b80a9b20a642ce6)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.27
  - quote: "\U0001F510 Fixed a security vulnerability where knowledge base access
      within chat folders persisted after permissions were revoked. [#17182](https://github.com/open-webui/open-webui/issues/17182),
      [Commit](https://github.com/open-webui/open-webui/commit/40e40d1dddf9ca937e99af41c8ca038dbc93a7e6)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.27
  - quote: "\U0001F6E1️ Default permission validation for message regeneration and
      deletion actions is enhanced to provide more restrictive access controls, improving
      chat security and user data protection. [#17285](https://github.com/open-webui/open-webui/pull/17285)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.27
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 4-safety-and-privacy-changes-in-v0-6-27
  source_release: open-webui-2025-09-09-v0-6-27-github-245869039-35ab9819
  source_type: github_releases
  theme: safety-privacy
  title: 4 Safety and Privacy changes in v0.6.27
  type: change
related_changes:
- '[[Changes/Gemini CLI/2025-09-04-2-safety-and-privacy-changes-in-v0-3-0|2 Safety
  and Privacy changes in v0.3.0]]'
- '[[Changes/Codex CLI/2025-09-05-3128-mcp-sandbox-call|♯3128 MCP sandbox call]]'
- '[[Changes/Gemini CLI/2025-09-09-2-safety-and-privacy-changes-in-v0-4-0|2 Safety
  and Privacy changes in v0.4.0]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-09-09-v0-6-27-github-245869039-35ab9819|open-webui-2025-09-09-v0-6-27-github-245869039-35ab9819]]'
source_type: github_releases
theme: safety-privacy
title: 4 Safety and Privacy changes in v0.6.27
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Safety and Privacy changes in v0.6.27

**Open WebUI** · 2025-09-09 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.27) · from [[Releases/Open WebUI/open-webui-2025-09-09-v0-6-27-github-245869039-35ab9819|v0.6.27]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔒 Conditional Permission Hardening for OpenShift Deployments: Added a build argument to enable optional permission hardening for OpenShift and container environments. [Commit](https://github.com/open-webui/open-webui/pull/17070/commits/0ebe4f8f8490451ac8e85a4846f010854d9b54e5)

> 🔐 Resolved a security issue where a global web search setting overrode model-specific restrictions, ensuring model-level settings are now correctly prioritized. [#17151](https://github.com/open-webui/open-webui/issues/17151), [Commit](https://github.com/open-webui/open-webui/commit/9368d0ac751ec3072d5a96712b80a9b20a642ce6)

> 🔐 Fixed a security vulnerability where knowledge base access within chat folders persisted after permissions were revoked. [#17182](https://github.com/open-webui/open-webui/issues/17182), [Commit](https://github.com/open-webui/open-webui/commit/40e40d1dddf9ca937e99af41c8ca038dbc93a7e6)

> 🛡️ Default permission validation for message regeneration and deletion actions is enhanced to provide more restrictive access controls, improving chat security and user data protection. [#17285](https://github.com/open-webui/open-webui/pull/17285)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.27
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-09-09-web-search-result-display-was-enhanced-to-include-titles-and-favicons-providing|💬 Web search result display was enhanced to include titles and favicons, providing…]] · Search and Browsing
- [[Changes/Open WebUI/2025-09-09-6-account-and-access-changes-in-v0-6-27|6 Account and Access changes in v0.6.27]] · Account and Access
- [[Changes/Open WebUI/2025-09-09-unicode-filename-support-is-improved-for-external-document-loaders-by-properly-u|📁 Unicode filename support is improved for external document loaders by properly…]] · Files and Data
- [[Changes/Open WebUI/2025-09-09-rag-loop-error-with-gemma-3-1-2b-instruct-is-fixed-by-correctly-unwrapping-unexp|🧠 RAG Loop/Error with Gemma 3.1 2B Instruct is fixed by correctly unwrapping…]] · Model Support
- [[Changes/Open WebUI/2025-09-09-14-developer-workflow-changes-in-v0-6-27|14 Developer Workflow changes in v0.6.27]] · Developer Workflow
- [[Changes/Open WebUI/2025-09-09-a-provider-toggle-in-connection-settings-now-allows-users-to-manually-specify-az|☁️ A provider toggle in connection settings now allows users to manually specify…]] · Apps and Integrations
- [[Changes/Open WebUI/2025-09-09-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-09-09-follow-up-tooltip-duplication-is-removed-streamlining-the-user-interface-and-pre|💬 Follow-up tooltip duplication is removed, streamlining the user interface…]] · Interface Experience
- [[Changes/Open WebUI/2025-09-09-5-reliability-and-performance-changes-in-v0-6-27|5 Reliability and Performance changes in v0.6.27]] · Reliability and Performance
- [[Changes/Open WebUI/2025-09-09-azure-openai-image-generation-is-now-supported-with-configurations-for-images-op|🎨 Azure OpenAI image generation is now supported, with configurations…]] · Image Generation
- [[Changes/Open WebUI/2025-09-09-17-other-changes-in-v0-6-27|17 other changes in v0.6.27]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2025-09-09 · Gemini CLI · [[Changes/Gemini CLI/2025-09-09-2-safety-and-privacy-changes-in-v0-4-0|2 Safety and Privacy changes in v0.4.0]]
- Later: 2025-09-10 · Codex CLI · [[Changes/Codex CLI/2025-09-10-ci-build-faster-tests-with-nextest-add-shear-minor-macos-permission-adjustment|CI/Build: faster tests with nextest, add shear; minor macOS permission adjustment]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-09-09-8243b9&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-09-09-4-safety-and-privacy-changes-in-v0-6-27.md%0ACard%20ID%3A%20open-webui-2025-09-09-8243b9%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.27%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->