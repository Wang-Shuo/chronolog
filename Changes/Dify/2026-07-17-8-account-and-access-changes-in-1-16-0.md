---
card_id: dify-2026-07-17-4f5a9f
date: '2026-07-17'
description: 'Dify · 2026-07-17 · Account and Access: 8 changes in v1.16.0 — The workflow-as-MCP
  server now supports MCP protocol 2025-06-18 with version negotiation and…'
diffusion:
  first_in_tracked: "[[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign
    into Notion with your Apple ID \U0001F5DD️ The perfect combination of speedy and
    secure]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2180
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9422daf6ec7f469cc92b074091764602bcdec79929bc7865a93a626791b2524c
product: dify
product_name: Dify
record:
  card_id: dify-2026-07-17-4f5a9f
  comparison: ''
  date: '2026-07-17'
  description: 'Dify — v1.16.0: 8 Account and Access changes'
  evidence:
  - quote: The workflow-as-MCP server now supports MCP protocol 2025-06-18 with version
      negotiation and structured tool output, while remaining backward compatible
      with older clients. MCPClient connections can now inject dynamic HTTP request
      headers at runtime using placeholders (e.g. `{{request.headers.X-Custom-Auth}}`),
      enabling per-request authentication passthrough.
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: Workflow run archives can now be exported, and active runs are properly
      aborted during Celery warm shutdown to prevent orphaned tasks. Redis connections
      are more resilient with TCP keepalive support and expanded retry coverage. Model
      providers now receive `app_id` for provider-side cost attribution (e.g. Bedrock
      requestMetadata, OpenAI metadata, Vertex AI labels). OAuth and SSO login flows
      now preserve redirect URLs more reliably, with a dedicated error view for failed
      SSO completions.
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: '**Authentication & Access Control**'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: '**Open redirects**: Prevented open redirects in post-login and auth redirect
      flows'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'test: use sqlite3 session in test_oauth_device_flow by @asukaminato0721
      in https://github.com/langgenius/dify/pull/38782'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'feat(oauth): preserve redirect_url through OAuth state for post-login…
      by @linw1995 in https://github.com/langgenius/dify/pull/38900'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'test: remove unit-only authentication integration cases by @asukaminato0721
      in https://github.com/langgenius/dify/pull/38948'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'test: move API key authentication coverage to unit tests by @asukaminato0721
      in https://github.com/langgenius/dify/pull/38919'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 8-account-and-access-changes-in-1-16-0
  source_release: dify-2026-07-17-1-16-0-github-355594285-636849e9
  source_type: github_releases
  theme: account-access
  title: 8 Account and Access changes in 1.16.0
  type: change
related_changes:
- '[[Changes/Ollama/2026-07-16-agent-web-search-and-fetch-now-tell-users-to-run-ollama-signin-when-authenticati|Agent
  web search and fetch now tell users to run ollama signin when authentication…]]'
- '[[Changes/Claude Code/2026-07-17-updated-the-auth-status-panel-title-from-cloud-authentication-to-authentication|Updated
  the auth status panel title from "Cloud authentication" to "Authentication"]]'
- '[[Changes/Devin/2026-07-17-this-release-also-includes-improved-bulk-secret-import-with-name-validation-expa|This
  release also includes improved bulk secret import with name validation…]]'
source_release: '[[Releases/Dify/dify-2026-07-17-1-16-0-github-355594285-636849e9|dify-2026-07-17-1-16-0-github-355594285-636849e9]]'
source_type: github_releases
theme: account-access
title: 8 Account and Access changes in 1.16.0
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Account and Access changes in 1.16.0

**Dify** · 2026-07-17 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.16.0) · from [[Releases/Dify/dify-2026-07-17-1-16-0-github-355594285-636849e9|v1.16.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> The workflow-as-MCP server now supports MCP protocol 2025-06-18 with version negotiation and structured tool output, while remaining backward compatible with older clients. MCPClient connections can now inject dynamic HTTP request headers at runtime using placeholders (e.g. `{{request.headers.X-Custom-Auth}}`), enabling per-request authentication passthrough.

> Workflow run archives can now be exported, and active runs are properly aborted during Celery warm shutdown to prevent orphaned tasks. Redis connections are more resilient with TCP keepalive support and expanded retry coverage. Model providers now receive `app_id` for provider-side cost attribution (e.g. Bedrock requestMetadata, OpenAI metadata, Vertex AI labels). OAuth and SSO login flows now preserve redirect URLs more reliably, with a dedicated error view for failed SSO completions.

> **Authentication & Access Control**

> **Open redirects**: Prevented open redirects in post-login and auth redirect flows

> test: use sqlite3 session in test_oauth_device_flow by @asukaminato0721 in https://github.com/langgenius/dify/pull/38782

> feat(oauth): preserve redirect_url through OAuth state for post-login… by @linw1995 in https://github.com/langgenius/dify/pull/38900

> test: remove unit-only authentication integration cases by @asukaminato0721 in https://github.com/langgenius/dify/pull/38948

> test: move API key authentication coverage to unit tests by @asukaminato0721 in https://github.com/langgenius/dify/pull/38919

Source: https://github.com/langgenius/dify/releases/tag/1.16.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-07-17-20-safety-and-privacy-changes-in-1-16-0|20 Safety and Privacy changes in 1.16.0]] · Safety and Privacy
- [[Changes/Dify/2026-07-17-agent-app-enters-open-beta-and-is-now-enabled-by-default-for-all-users-it-introd|Agent App enters open beta and is now enabled by default for all users]] · Safety and Privacy
- [[Changes/Dify/2026-07-17-16-context-window-changes-in-1-16-0|16 Context Window changes in 1.16.0]] · Context Window
- [[Changes/Dify/2026-07-17-perf-memory-batch-load-message-files-in-tokenbuffermemory-to-remove-n-1-queries|perf(memory): batch-load message files in TokenBufferMemory to remove N+1 queries]] · Memory and Personalization
- [[Changes/Dify/2026-07-17-4-editor-experience-changes-in-1-16-0|4 Editor Experience changes in 1.16.0]] · Editor Experience
- [[Changes/Dify/2026-07-17-3-voice-and-audio-changes-in-1-16-0|3 Voice and Audio changes in 1.16.0]] · Voice and Audio
- [[Changes/Dify/2026-07-17-4-collaboration-changes-in-1-16-0|4 Collaboration changes in 1.16.0]] · Collaboration
- [[Changes/Dify/2026-07-17-3-developer-workflow-changes-in-1-16-0|3 Developer Workflow changes in 1.16.0]] · Developer Workflow
- [[Changes/Dify/2026-07-17-24-apps-and-integrations-changes-in-1-16-0|24 Apps and Integrations changes in 1.16.0]] · Apps and Integrations
- [[Changes/Dify/2026-07-17-2-automation-and-scheduling-changes-in-1-16-0|2 Automation and Scheduling changes in 1.16.0]] · Automation and Scheduling
- [[Changes/Dify/2026-07-17-2-interface-experience-changes-in-1-16-0|2 Interface Experience changes in 1.16.0]] · Interface Experience
- [[Changes/Dify/2026-07-17-2-files-and-data-changes-in-1-16-0|2 Files and Data changes in 1.16.0]] · Files and Data
- [[Changes/Dify/2026-07-17-12-model-support-changes-in-1-16-0|12 Model Support changes in 1.16.0]] · Model Support
- [[Changes/Dify/2026-07-17-chore-improve-workflow-generator-accessibility-and-api-contracts-by-crazywoola-i|chore: Improve workflow generator accessibility and API contracts]] · Accessibility and Localization
- [[Changes/Dify/2026-07-17-2-enterprise-and-administration-changes-in-1-16-0|2 Enterprise and Administration changes in 1.16.0]] · Enterprise and Administration
- [[Changes/Dify/2026-07-17-3-reliability-and-performance-changes-in-1-16-0|3 Reliability and Performance changes in 1.16.0]] · Reliability and Performance
- [[Changes/Dify/2026-07-17-64-agent-mode-changes-in-1-16-0|64 Agent Mode changes in 1.16.0]] · Agent Mode
- [[Changes/Dify/2026-07-17-5-pricing-model-changes-in-1-16-0|5 Pricing Model changes in 1.16.0]] · Pricing Model
- [[Changes/Dify/2026-07-17-237-other-changes-in-1-16-0|237 other changes in 1.16.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-07-17 · Devin · [[Changes/Devin/2026-07-17-this-release-also-includes-improved-bulk-secret-import-with-name-validation-expa|This release also includes improved bulk secret import with name validation…]]
- Later: 2026-07-17 · Kimi Code · [[Changes/Kimi Code/2026-07-17-oauth-connection-errors-now-include-the-underlying-network-cause-dns-refused-con|OAuth connection errors now include the underlying network cause…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Notion · [[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign into Notion with your Apple ID 🗝️ The perfect combination of speedy and secure]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-07-17-4f5a9f&body=Card%3A%20Changes%2FDify%2F2026-07-17-8-account-and-access-changes-in-1-16-0.md%0ACard%20ID%3A%20dify-2026-07-17-4f5a9f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.16.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->