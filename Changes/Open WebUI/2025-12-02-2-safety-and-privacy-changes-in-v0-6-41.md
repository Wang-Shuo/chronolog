---
card_id: open-webui-2025-12-02-5f380d
date: '2025-12-02'
description: "Open WebUI · 2025-12-02 · Safety and Privacy: 2 changes in v0.6.41 —
  \U0001F39B️ Channel feature access can now be controlled through both the…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 961
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 17b4abc0dc4b5fba11b84b2bc79dd85ec2f68eb36fcb3e06bb43822fda67e710
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-12-02-5f380d
  comparison: ''
  date: '2025-12-02'
  description: 'Open WebUI — v0.6.41: 2 Safety and Privacy changes'
  evidence:
  - quote: "\U0001F39B️ Channel feature access can now be controlled through both
      the \"USER_PERMISSIONS_FEATURES_CHANNELS\" environment variable and group permission
      toggles in the admin panel, allowing administrators to restrict channel functionality
      for specific users or groups while defaulting to enabled for all users. [Commit](https://github.com/open-webui/open-webui/commit/f589b7c1895a6a77166c047891acfa21bc0936c4)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: "\U0001F510 Knowledge base file access inconsistencies were resolved where
      authorized non-admin users received \"Not found\" or permission errors for certain
      files due to race conditions during upload causing mismatched collection_name
      values, with file access validation now properly checking against knowledge
      base file associations. [#18689](https://github.com/open-webui/open-webui/issues/18689),
      [#19523](https://github.com/open-webui/open-webui/pull/19523), [Commit](https://github.com/open-webui/open-webui/commit/e301d1962e45900ababd3eabb7e9a2ad275a5761)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 2-safety-and-privacy-changes-in-v0-6-41
  source_release: open-webui-2025-12-02-v0-6-41-github-266904152-3dfc9f25
  source_type: github_releases
  theme: safety-privacy
  title: 2 Safety and Privacy changes in v0.6.41
  type: change
related_changes:
- '[[Changes/Cline/2025-11-27-maint-npm-audit-fix-for-glob-package-vulnerability-by-canvrno-in-https-github-co|maint:
  npm audit fix for glob package vulnerability]]'
- '[[Changes/Codex CLI/2025-12-02-9-safety-and-privacy-changes-in-rust-v0-64-0|9 Safety
  and Privacy changes in rust-v0.64.0]]'
- '[[Changes/Gemini CLI/2025-12-02-improve-code-coverage-for-cli-src-ui-privacy-package-by-megha1188-in-https-githu|Improve
  code coverage for cli/src/ui/privacy package]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-12-02-v0-6-41-github-266904152-3dfc9f25|open-webui-2025-12-02-v0-6-41-github-266904152-3dfc9f25]]'
source_type: github_releases
theme: safety-privacy
title: 2 Safety and Privacy changes in v0.6.41
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Safety and Privacy changes in v0.6.41

**Open WebUI** · 2025-12-02 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.41) · from [[Releases/Open WebUI/open-webui-2025-12-02-v0-6-41-github-266904152-3dfc9f25|v0.6.41]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🎛️ Channel feature access can now be controlled through both the "USER_PERMISSIONS_FEATURES_CHANNELS" environment variable and group permission toggles in the admin panel, allowing administrators to restrict channel functionality for specific users or groups while defaulting to enabled for all users. [Commit](https://github.com/open-webui/open-webui/commit/f589b7c1895a6a77166c047891acfa21bc0936c4)

> 🔐 Knowledge base file access inconsistencies were resolved where authorized non-admin users received "Not found" or permission errors for certain files due to race conditions during upload causing mismatched collection_name values, with file access validation now properly checking against knowledge base file associations. [#18689](https://github.com/open-webui/open-webui/issues/18689), [#19523](https://github.com/open-webui/open-webui/pull/19523), [Commit](https://github.com/open-webui/open-webui/commit/e301d1962e45900ababd3eabb7e9a2ad275a5761)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-12-02-group-channels-were-introduced-as-a-new-channel-type-enabling-membership-based-c|👥 Group channels were introduced as a new channel type enabling membership-based…]] · Collaboration
- [[Changes/Open WebUI/2025-12-02-web-search-domain-filtering-was-corrected-to-properly-block-results-when-any-res|🛡️ Web search domain filtering was corrected to properly block results when any…]] · Search and Browsing
- [[Changes/Open WebUI/2025-12-02-tool-call-response-token-duplication-was-fixed-by-removing-redundant-message-his|🔄 Tool call response token duplication was fixed by removing redundant message…]] · Context Window
- [[Changes/Open WebUI/2025-12-02-7-account-and-access-changes-in-v0-6-41|7 Account and Access changes in v0.6.41]] · Account and Access
- [[Changes/Open WebUI/2025-12-02-13-developer-workflow-changes-in-v0-6-41|13 Developer Workflow changes in v0.6.41]] · Developer Workflow
- [[Changes/Open WebUI/2025-12-02-4-reliability-and-performance-changes-in-v0-6-41|4 Reliability and Performance changes in v0.6.41]] · Reliability and Performance
- [[Changes/Open WebUI/2025-12-02-the-model-editor-interface-was-refined-with-access-control-settings-moved-to-a-d|🎨 The model editor interface was refined with access control settings moved…]] · Editor Experience
- [[Changes/Open WebUI/2025-12-02-9-model-support-changes-in-v0-6-41|9 Model Support changes in v0.6.41]] · Model Support
- [[Changes/Open WebUI/2025-12-02-image-generation-in-temporary-chats-was-fixed-by-correctly-handling-local-chat-s|🎨 Image generation in temporary chats was fixed by correctly handling local chat…]] · Image Generation
- [[Changes/Open WebUI/2025-12-02-2-enterprise-and-administration-changes-in-v0-6-41|2 Enterprise and Administration changes in v0.6.41]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-12-02-sentencetransformers-embedding-initialization-was-fixed-by-updating-the-transfor|🐍 SentenceTransformers embedding initialization was fixed by updating…]] · Files and Data
- [[Changes/Open WebUI/2025-12-02-11-interface-experience-changes-in-v0-6-41|11 Interface Experience changes in v0.6.41]] · Interface Experience
- [[Changes/Open WebUI/2025-12-02-2-apps-and-integrations-changes-in-v0-6-41|2 Apps and Integrations changes in v0.6.41]] · Apps and Integrations
- [[Changes/Open WebUI/2025-12-02-13-other-changes-in-v0-6-41|13 other changes in v0.6.41]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2025-12-02 · Gemini CLI · [[Changes/Gemini CLI/2025-12-02-improve-code-coverage-for-cli-src-ui-privacy-package-by-megha1188-in-https-githu|Improve code coverage for cli/src/ui/privacy package]]
- Later: 2025-12-08 · Google Antigravity · [[Changes/Google Antigravity/2025-12-08-various-security-fixes|Various security fixes]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-12-02-5f380d&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-12-02-2-safety-and-privacy-changes-in-v0-6-41.md%0ACard%20ID%3A%20open-webui-2025-12-02-5f380d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.41%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->