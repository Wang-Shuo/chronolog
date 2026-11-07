---
card_id: open-webui-2025-09-09-1ea068
date: '2025-09-09'
description: "Open WebUI · 2025-09-09 · Account and Access: 6 changes in v0.6.27 —
  \U0001F512 Comprehensive server-side OAuth token management was implemented, securely
  storing…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 894
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: fb2f0332410ddd1217454c01e5cc9b43588d00954026f360986d485c929a0d1d
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-09-09-1ea068
  comparison: ''
  date: '2025-09-09'
  description: 'Open WebUI — v0.6.27: 6 Account and Access changes'
  evidence:
  - quote: "\U0001F512 Comprehensive server-side OAuth token management was implemented,
      securely storing encrypted tokens in a new database table and introducing an
      automatic refresh mechanism, enabling seamless and secure forwarding of valid
      user-specific OAuth tokens to downstream services, including OpenAI-compatible
      endpoints and external tool servers via the new \"system_oauth\" authentication
      type, resolving long-standing issues such as large token size limitations, stale/expired
      tokens, and reliable token propagation, and enhancing overall security by minimizing
      client-side token exposure, configurable via \"ENABLE_OAUTH_ID_TOKEN_COOKIE\"
      and \"OAUTH_SESSION_TOKEN_ENCRYPTION_KEY\" environment variables. [Docs:#683](https://github.com/open-webui/docs/pull/683),
      [#17210](https://github.com/open-webui/open-webui/pull/17210), [#8957](https://github.com/open-webui/open-webui/discussions/8957),
      [#11029](https://github.com/open-webui/open-webui/discussions/11029), [#17178](https://github.com/open-webui/open-webui/issues/17178),
      [#17183](https://github.com/open-webui/open-webui/issues/17183), [Commit](https://github.com/open-webui/open-webui/commit/217f4daef09b36d3d4cc4681e11d3ebd9984a1a5),
      [Commit](https://github.com/open-webui/open-webui/commit/fc11e4384fe98fac659e10596f67c23483578867),
      [Commit](https://github.com/open-webui/open-webui/commit/f11bdc6ab5dd5682bb3e27166e77581f5b8af3e0),
      [Commit](https://github.com/open-webui/open-webui/commit/f71834720e623761d972d4d740e9bbd90a3a86c6),
      [Commit](https://github.com/open-webui/open-webui/commit/b5bb6ae177dcdc4e8274d7e5ffa50bc8099fd466),
      [Commit](https://github.com/open-webui/open-webui/commit/b786d1e3f3308ef4f0f95d7130ddbcaaca4fc927),
      [Commit](https://github.com/open-webui/open-webui/commit/8a9f8627017bd0a74cbd647891552b26e56aabb7),
      [Commit](https://github.com/open-webui/open-webui/commit/30d1dc2c60e303756120fe1c5538968c4e6139f4),
      [Commit](https://github.com/open-webui/open-webui/commit/2b2d123531eb3f42c0e940593832a64e2806240d),
      [Commit](https://github.com/open-webui/open-webui/commit/6f6412dd16c63c2bb4df79a96b814bf69cb3f880)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.27
  - quote: "\U0001F465 Regex pattern support is added for OAuth blocked groups, allowing
      more flexible group filtering rules. [Commit](https://github.com/open-webui/open-webui/pull/17070/commits/df66e21472646648d008ebb22b0e8d5424d491df)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.27
  - quote: "\U0001F4F1 Mobile app config API authentication now supports Authorization
      header token verification with cookie fallback for iOS and Android requests.
      [#17175](https://github.com/open-webui/open-webui/pull/17175)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.27
  - quote: "\U0001F510 The SSO login button visibility is restored for OIDC PKCE authentication
      without a client secret. [#17012](https://github.com/open-webui/open-webui/pull/17012)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.27
  - quote: "\U0001F510 OAuth redirect reliability is improved by robustly preserving
      the intended redirect path using session storage. [#17235](https://github.com/open-webui/open-webui/issues/17235),
      [Commit](https://github.com/open-webui/open-webui/pull/17070/commits/4f2b821088367da18374027919594365c7a3f459),
      [#15575](https://github.com/open-webui/open-webui/pull/15575), [Commit](https://github.com/open-webui/open-webui/pull/17070/commits/d9f97c832c556fae4b116759da0177bf4fe619de)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.27
  - quote: "\U0001F512 Static asset authentication is improved by adding crossorigin=\"use-credentials\"
      attributes to all link elements, enabling proper cookie forwarding for proxy
      environments and authenticated requests to favicon, manifest, and stylesheet
      resources. [#17280](https://github.com/open-webui/open-webui/pull/17280), [Commit](https://github.com/open-webui/open-webui/commit/f17d8b5d19e1a05df7d63f53e939c99772a59c1e)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.27
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 6-account-and-access-changes-in-v0-6-27
  source_release: open-webui-2025-09-09-v0-6-27-github-245869039-35ab9819
  source_type: github_releases
  theme: account-access
  title: 6 Account and Access changes in v0.6.27
  type: change
related_changes:
- '[[Changes/Codex CLI/2025-09-05-3-account-and-access-changes-in-rust-v0-30-0|3 Account
  and Access changes in rust-v0.30.0]]'
- '[[Changes/Codex CLI/2025-09-08-3217-added-logic-to-cancel-pending-oauth-login-to-free-up-localhost-port|♯3217
  Added logic to cancel pending oauth login to free up localhost port]]'
- '[[Changes/Gemini CLI/2025-09-09-feat-oauth-create-hybrid-storage-class-by-shishu314-in-https-github-com-google-g|feat(oauth)
  - Create hybrid storage class]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-09-09-v0-6-27-github-245869039-35ab9819|open-webui-2025-09-09-v0-6-27-github-245869039-35ab9819]]'
source_type: github_releases
theme: account-access
title: 6 Account and Access changes in v0.6.27
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Account and Access changes in v0.6.27

**Open WebUI** · 2025-09-09 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.27) · from [[Releases/Open WebUI/open-webui-2025-09-09-v0-6-27-github-245869039-35ab9819|v0.6.27]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔒 Comprehensive server-side OAuth token management was implemented, securely storing encrypted tokens in a new database table and introducing an automatic refresh mechanism, enabling seamless and secure forwarding of valid user-specific OAuth tokens to downstream services, including OpenAI-compatible endpoints and external tool servers via the new "system_oauth" authentication type, resolving long-standing issues such as large token size limitations, stale/expired tokens, and reliable token propagation, and enhancing overall security by minimizing client-side token exposure, configurable via "ENABLE_OAUTH_ID_TOKEN_COOKIE" and "OAUTH_SESSION_TOKEN_ENCRYPTION_KEY" environment variables. [Docs:#683](https://github.com/open-webui/docs/pull/683), [#17210](https://github.com/open-webui/open-webui/pull/17210), [#8957](https://github.com/open-webui/open-webui/discussions/8957), [#11029](https://github.com/open-webui/open-webui/discussions/11029), [#17178](https://github.com/open-webui/open-webui/issues/17178), [#17183](https://github.com/open-webui/open-webui/issues/17183), [Commit](https://github.com/open-webui/open-webui/commit/217f4daef09b36d3d4cc4681e11d3ebd9984a1a5), [Commit](https://github.com/open-webui/open-webui/commit/fc11e4384fe98fac659e10596f67c23483578867), [Commit](https://github.com/open-webui/open-webui/commit/f11bdc6ab5dd5682bb3e27166e77581f5b8af3e0), [Commit](https://github.com/open-webui/open-webui/commit/f71834720e623761d972d4d740e9bbd90a3a86c6), [Commit](https://github.com/open-webui/open-webui/commit/b5bb6ae177dcdc4e8274d7e5ffa50bc8099fd466), [Commit](https://github.com/open-webui/open-webui/commit/b786d1e3f3308ef4f0f95d7130ddbcaaca4fc927), [Commit](https://github.com/open-webui/open-webui/commit/8a9f8627017bd0a74cbd647891552b26e56aabb7), [Commit](https://github.com/open-webui/open-webui/commit/30d1dc2c60e303756120fe1c5538968c4e6139f4), [Commit](https://github.com/open-webui/open-webui/commit/2b2d123531eb3f42c0e940593832a64e2806240d), [Commit](https://github.com/open-webui/open-webui/commit/6f6412dd16c63c2bb4df79a96b814bf69cb3f880)

> 👥 Regex pattern support is added for OAuth blocked groups, allowing more flexible group filtering rules. [Commit](https://github.com/open-webui/open-webui/pull/17070/commits/df66e21472646648d008ebb22b0e8d5424d491df)

> 📱 Mobile app config API authentication now supports Authorization header token verification with cookie fallback for iOS and Android requests. [#17175](https://github.com/open-webui/open-webui/pull/17175)

> 🔐 The SSO login button visibility is restored for OIDC PKCE authentication without a client secret. [#17012](https://github.com/open-webui/open-webui/pull/17012)

> 🔐 OAuth redirect reliability is improved by robustly preserving the intended redirect path using session storage. [#17235](https://github.com/open-webui/open-webui/issues/17235), [Commit](https://github.com/open-webui/open-webui/pull/17070/commits/4f2b821088367da18374027919594365c7a3f459), [#15575](https://github.com/open-webui/open-webui/pull/15575), [Commit](https://github.com/open-webui/open-webui/pull/17070/commits/d9f97c832c556fae4b116759da0177bf4fe619de)

> 🔒 Static asset authentication is improved by adding crossorigin="use-credentials" attributes to all link elements, enabling proper cookie forwarding for proxy environments and authenticated requests to favicon, manifest, and stylesheet resources. [#17280](https://github.com/open-webui/open-webui/pull/17280), [Commit](https://github.com/open-webui/open-webui/commit/f17d8b5d19e1a05df7d63f53e939c99772a59c1e)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.27
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-09-09-web-search-result-display-was-enhanced-to-include-titles-and-favicons-providing|💬 Web search result display was enhanced to include titles and favicons, providing…]] · Search and Browsing
- [[Changes/Open WebUI/2025-09-09-unicode-filename-support-is-improved-for-external-document-loaders-by-properly-u|📁 Unicode filename support is improved for external document loaders by properly…]] · Files and Data
- [[Changes/Open WebUI/2025-09-09-rag-loop-error-with-gemma-3-1-2b-instruct-is-fixed-by-correctly-unwrapping-unexp|🧠 RAG Loop/Error with Gemma 3.1 2B Instruct is fixed by correctly unwrapping…]] · Model Support
- [[Changes/Open WebUI/2025-09-09-4-safety-and-privacy-changes-in-v0-6-27|4 Safety and Privacy changes in v0.6.27]] · Safety and Privacy
- [[Changes/Open WebUI/2025-09-09-14-developer-workflow-changes-in-v0-6-27|14 Developer Workflow changes in v0.6.27]] · Developer Workflow
- [[Changes/Open WebUI/2025-09-09-a-provider-toggle-in-connection-settings-now-allows-users-to-manually-specify-az|☁️ A provider toggle in connection settings now allows users to manually specify…]] · Apps and Integrations
- [[Changes/Open WebUI/2025-09-09-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-09-09-follow-up-tooltip-duplication-is-removed-streamlining-the-user-interface-and-pre|💬 Follow-up tooltip duplication is removed, streamlining the user interface…]] · Interface Experience
- [[Changes/Open WebUI/2025-09-09-5-reliability-and-performance-changes-in-v0-6-27|5 Reliability and Performance changes in v0.6.27]] · Reliability and Performance
- [[Changes/Open WebUI/2025-09-09-azure-openai-image-generation-is-now-supported-with-configurations-for-images-op|🎨 Azure OpenAI image generation is now supported, with configurations…]] · Image Generation
- [[Changes/Open WebUI/2025-09-09-17-other-changes-in-v0-6-27|17 other changes in v0.6.27]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2025-09-09 · Gemini CLI · [[Changes/Gemini CLI/2025-09-09-feat-oauth-create-hybrid-storage-class-by-shishu314-in-https-github-com-google-g|feat(oauth) - Create hybrid storage class]]
- Later: 2025-09-15 · Codex CLI · [[Changes/Codex CLI/2025-09-15-6-account-and-access-changes-in-rust-v0-36-0|6 Account and Access changes in rust-v0.36.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-09-09-1ea068&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-09-09-6-account-and-access-changes-in-v0-6-27.md%0ACard%20ID%3A%20open-webui-2025-09-09-1ea068%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.27%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->