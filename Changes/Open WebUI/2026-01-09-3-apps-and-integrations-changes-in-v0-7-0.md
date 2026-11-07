---
card_id: open-webui-2026-01-09-4cd271
date: '2026-01-09'
description: "Open WebUI · 2026-01-09 · Apps and Integrations: 3 changes in v0.7.0
  — \U0001F512 Administrators can now disable SSL certificate verification for external
  tools using…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2583
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a3d7d25cd1aba80f5a8a346991284b4e4ff0339b937cf1371d56c54495ee52bb
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-01-09-4cd271
  comparison: ''
  date: '2026-01-09'
  description: 'Open WebUI — v0.7.0: 3 Apps and Integrations changes'
  evidence:
  - quote: "\U0001F512 Administrators can now disable SSL certificate verification
      for external tools using the \"REQUESTS_VERIFY\" environment variable, enabling
      integration with self-signed certificates for Tika, Ollama embeddings, and external
      rerankers. [#19968](https://github.com/open-webui/open-webui/issues/19968),
      [Commit](https://github.com/open-webui/open-webui/commit/dfc5dad63167eabb7fb027e63c324675b23f2e9d)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F510 Users with MCP integrations now experience reliable OAuth 2.1
      token refresh after access token expiration through proper Protected Resource
      discovery, preventing integration failures that caused sessions to be deleted.
      [#19794](https://github.com/open-webui/open-webui/issues/19794), [#20138](https://github.com/open-webui/open-webui/pull/20138),
      [#20291](https://github.com/open-webui/open-webui/issues/20291), [Commit](https://github.com/open-webui/open-webui/commit/bf2b2962399e341926bdbf9e0a82101f31a90b23),
      [Commit](https://github.com/open-webui/open-webui/commit/89565c58c6ae6b5b129559ef68b5a0c18c110765)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F50C Administrators no longer experience infinite loading screens
      when invalid or MCP-style configurations are used with OpenAPI connection types
      for external tools. [#20207](https://github.com/open-webui/open-webui/issues/20207),
      [#20257](https://github.com/open-webui/open-webui/pull/20257)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 3-apps-and-integrations-changes-in-v0-7-0
  source_release: open-webui-2026-01-09-v0-7-0-github-275585328-a4da522c
  source_type: github_releases
  theme: apps-integrations
  title: 3 Apps and Integrations changes in v0.7.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-01-09-2-apps-and-integrations-changes-in-v2-1-2|2 Apps
  and Integrations changes in v2.1.2]]'
- '[[Changes/Codex CLI/2026-01-09-2-apps-and-integrations-changes-in-rust-v0-80-0|2
  Apps and Integrations changes in rust-v0.80.0]]'
- '[[Changes/Devin/2026-01-09-native-linear-integration|Native Linear Integration]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-01-09-v0-7-0-github-275585328-a4da522c|open-webui-2026-01-09-v0-7-0-github-275585328-a4da522c]]'
source_type: github_releases
theme: apps-integrations
title: 3 Apps and Integrations changes in v0.7.0
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Apps and Integrations changes in v0.7.0

**Open WebUI** · 2026-01-09 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.7.0) · from [[Releases/Open WebUI/open-webui-2026-01-09-v0-7-0-github-275585328-a4da522c|v0.7.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔒 Administrators can now disable SSL certificate verification for external tools using the "REQUESTS_VERIFY" environment variable, enabling integration with self-signed certificates for Tika, Ollama embeddings, and external rerankers. [#19968](https://github.com/open-webui/open-webui/issues/19968), [Commit](https://github.com/open-webui/open-webui/commit/dfc5dad63167eabb7fb027e63c324675b23f2e9d)

> 🔐 Users with MCP integrations now experience reliable OAuth 2.1 token refresh after access token expiration through proper Protected Resource discovery, preventing integration failures that caused sessions to be deleted. [#19794](https://github.com/open-webui/open-webui/issues/19794), [#20138](https://github.com/open-webui/open-webui/pull/20138), [#20291](https://github.com/open-webui/open-webui/issues/20291), [Commit](https://github.com/open-webui/open-webui/commit/bf2b2962399e341926bdbf9e0a82101f31a90b23), [Commit](https://github.com/open-webui/open-webui/commit/89565c58c6ae6b5b129559ef68b5a0c18c110765)

> 🔌 Administrators no longer experience infinite loading screens when invalid or MCP-style configurations are used with OpenAPI connection types for external tools. [#20207](https://github.com/open-webui/open-webui/issues/20207), [#20257](https://github.com/open-webui/open-webui/pull/20257)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-01-09-3-editor-experience-changes-in-v0-7-0|3 Editor Experience changes in v0.7.0]] · Editor Experience
- [[Changes/Open WebUI/2026-01-09-users-on-windows-now-see-correctly-preserved-line-breaks-when-using-the-clipboar|📋 Users on Windows now see correctly preserved line breaks when using…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-01-09-2-memory-and-personalization-changes-in-v0-7-0|2 Memory and Personalization changes in v0.7.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-01-09-4-search-and-browsing-changes-in-v0-7-0|4 Search and Browsing changes in v0.7.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-01-09-5-files-and-data-changes-in-v0-7-0|5 Files and Data changes in v0.7.0]] · Files and Data
- [[Changes/Open WebUI/2026-01-09-3-context-window-changes-in-v0-7-0|3 Context Window changes in v0.7.0]] · Context Window
- [[Changes/Open WebUI/2026-01-09-9-reliability-and-performance-changes-in-v0-7-0|9 Reliability and Performance changes in v0.7.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-01-09-6-safety-and-privacy-changes-in-v0-7-0|6 Safety and Privacy changes in v0.7.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-01-09-3-account-and-access-changes-in-v0-7-0|3 Account and Access changes in v0.7.0]] · Account and Access
- [[Changes/Open WebUI/2026-01-09-4-image-generation-changes-in-v0-7-0|4 Image Generation changes in v0.7.0]] · Image Generation
- [[Changes/Open WebUI/2026-01-09-5-interface-experience-changes-in-v0-7-0|5 Interface Experience changes in v0.7.0]] · Interface Experience
- [[Changes/Open WebUI/2026-01-09-11-model-support-changes-in-v0-7-0|11 Model Support changes in v0.7.0]] · Model Support
- [[Changes/Open WebUI/2026-01-09-24-developer-workflow-changes-in-v0-7-0|24 Developer Workflow changes in v0.7.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-01-09-3-voice-and-audio-changes-in-v0-7-0|3 Voice and Audio changes in v0.7.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-01-09-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-01-09-26-other-changes-in-v0-7-0|26 other changes in v0.7.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-01-09 · Devin · [[Changes/Devin/2026-01-09-native-linear-integration|Native Linear Integration]]
- Later: 2026-01-09 · OpenCode · [[Changes/OpenCode/2026-01-09-2-apps-and-integrations-changes-in-v1-1-10|2 Apps and Integrations changes in v1.1.10]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-01-09-4cd271&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-01-09-3-apps-and-integrations-changes-in-v0-7-0.md%0ACard%20ID%3A%20open-webui-2026-01-09-4cd271%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.7.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->