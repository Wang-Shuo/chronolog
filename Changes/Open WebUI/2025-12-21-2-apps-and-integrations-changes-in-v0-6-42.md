---
card_id: open-webui-2025-12-21-4d5fec
date: '2025-12-21'
description: 'Open WebUI · 2025-12-21 · Apps and Integrations: 2 changes in v0.6.42
  — > This release includes dependency version bumps; existing plugins may need to
  update…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1004
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 381610107f9264a9867aa6caab0590d24a9315c92bc5fbbe4da02380ce00a595
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-12-21-4d5fec
  comparison: ''
  date: '2025-12-21'
  description: 'Open WebUI — v0.6.42: 2 Apps and Integrations changes'
  evidence:
  - quote: '> This release includes dependency version bumps; existing plugins may
      need to update their imports to remain compatible, as outdated import paths
      or APIs may cause build or runtime errors.'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F50C Knowledge base file listing API was redesigned with paginated
      responses and new filtering parameters; the GET /knowledge/{id}/files endpoint
      now returns paginated results with user attribution instead of embedding all
      files in the knowledge object, which may require updates to custom integrations
      or scripts accessing knowledge base data programmatically. [Commit](https://github.com/open-webui/open-webui/commit/94a8439105f30203ea9d729787c9c5978f5c22a2)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 2-apps-and-integrations-changes-in-v0-6-42
  source_release: open-webui-2025-12-21-v0-6-42-github-272053915-b8e46ad9
  source_type: github_releases
  theme: apps-integrations
  title: 2 Apps and Integrations changes in v0.6.42
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2025-12-18-2-apps-and-integrations-changes-in-v0-0-370|2
  Apps and Integrations changes in v0.0.370]]'
- '[[Changes/Claude Code/2025-12-19-2-apps-and-integrations-changes-in-v2-0-73|2 Apps
  and Integrations changes in v2.0.73]]'
- '[[Changes/Replit/2025-12-19-custom-mcp-server-icons|Custom MCP Server Icons]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-12-21-v0-6-42-github-272053915-b8e46ad9|open-webui-2025-12-21-v0-6-42-github-272053915-b8e46ad9]]'
source_type: github_releases
theme: apps-integrations
title: 2 Apps and Integrations changes in v0.6.42
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Apps and Integrations changes in v0.6.42

**Open WebUI** · 2025-12-21 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.42) · from [[Releases/Open WebUI/open-webui-2025-12-21-v0-6-42-github-272053915-b8e46ad9|v0.6.42]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> > This release includes dependency version bumps; existing plugins may need to update their imports to remain compatible, as outdated import paths or APIs may cause build or runtime errors.

> 🔌 Knowledge base file listing API was redesigned with paginated responses and new filtering parameters; the GET /knowledge/{id}/files endpoint now returns paginated results with user attribution instead of embedding all files in the knowledge object, which may require updates to custom integrations or scripts accessing knowledge base data programmatically. [Commit](https://github.com/open-webui/open-webui/commit/94a8439105f30203ea9d729787c9c5978f5c22a2)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-12-21-user-uploaded-images-are-now-automatically-converted-from-base64-to-actual-file|🖼️ User-uploaded images are now automatically converted from base64 to actual file…]] · Collaboration
- [[Changes/Open WebUI/2025-12-21-3-editor-experience-changes-in-v0-6-42|3 Editor Experience changes in v0.6.42]] · Editor Experience
- [[Changes/Open WebUI/2025-12-21-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-12-21-6-files-and-data-changes-in-v0-6-42|6 Files and Data changes in v0.6.42]] · Files and Data
- [[Changes/Open WebUI/2025-12-21-7-reliability-and-performance-changes-in-v0-6-42|7 Reliability and Performance changes in v0.6.42]] · Reliability and Performance
- [[Changes/Open WebUI/2025-12-21-11-model-support-changes-in-v0-6-42|11 Model Support changes in v0.6.42]] · Model Support
- [[Changes/Open WebUI/2025-12-21-6-safety-and-privacy-changes-in-v0-6-42|6 Safety and Privacy changes in v0.6.42]] · Safety and Privacy
- [[Changes/Open WebUI/2025-12-21-8-interface-experience-changes-in-v0-6-42|8 Interface Experience changes in v0.6.42]] · Interface Experience
- [[Changes/Open WebUI/2025-12-21-4-account-and-access-changes-in-v0-6-42|4 Account and Access changes in v0.6.42]] · Account and Access
- [[Changes/Open WebUI/2025-12-21-external-reranker-operations-were-optimized-to-prevent-event-loop-blocking-by-of|⚡ External reranker operations were optimized to prevent event loop blocking…]] · Automation and Scheduling
- [[Changes/Open WebUI/2025-12-21-3-search-and-browsing-changes-in-v0-6-42|3 Search and Browsing changes in v0.6.42]] · Search and Browsing
- [[Changes/Open WebUI/2025-12-21-11-developer-workflow-changes-in-v0-6-42|11 Developer Workflow changes in v0.6.42]] · Developer Workflow
- [[Changes/Open WebUI/2025-12-21-2-multimodal-input-changes-in-v0-6-42|2 Multimodal Input changes in v0.6.42]] · Multimodal Input
- [[Changes/Open WebUI/2025-12-21-4-image-generation-changes-in-v0-6-42|4 Image Generation changes in v0.6.42]] · Image Generation
- [[Changes/Open WebUI/2025-12-21-2-voice-and-audio-changes-in-v0-6-42|2 Voice and Audio changes in v0.6.42]] · Voice and Audio
- [[Changes/Open WebUI/2025-12-21-channel-image-upload-handling-was-optimized-to-process-and-store-compressed-imag|🖼️ Channel image upload handling was optimized to process and store compressed…]] · Memory and Personalization
- [[Changes/Open WebUI/2025-12-21-28-other-changes-in-v0-6-42|28 other changes in v0.6.42]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2025-12-19 · Replit · [[Changes/Replit/2025-12-19-custom-mcp-server-icons|Custom MCP Server Icons]]
- Later: 2025-12-22 · Cursor · [[Changes/Cursor/2025-12-22-2-apps-and-integrations-changes-in-2-3|2 Apps and Integrations changes in 2.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-12-21-4d5fec&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-12-21-2-apps-and-integrations-changes-in-v0-6-42.md%0ACard%20ID%3A%20open-webui-2025-12-21-4d5fec%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.42%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->