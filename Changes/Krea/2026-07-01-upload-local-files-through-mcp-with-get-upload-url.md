---
card_id: krea-2026-07-01-2e11c0
date: '2026-07-01'
description: 'Krea · 2026-07-01 · Apps and Integrations: **The MCP upload flow now
  uses presigned URLs.** The new `get_upload_url` tool returns a short-lived URL that
  your…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2756
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: launch
machine_hash: 549f8be9f245f4925c2c1caea7e900bea8d9544d9e725c8506e72aaa6291a429
product: krea
product_name: Krea
record:
  ai_generated: true
  card_id: krea-2026-07-01-2e11c0
  comparison: ''
  confidence: low
  date: '2026-07-01'
  description: 'Krea — Workspace picker and presigned uploads for MCP: **The MCP upload
    flow now uses presigned URLs.** The new `get_upload_url` tool returns a short-lived
    URL that your client `POST`s the file to as `multipart/form-data`, and the response
    contains an asset URL you can pass straight into a `generate` call.'
  evidence:
  - quote: '**The MCP upload flow now uses presigned URLs.** The new `get_upload_url`
      tool returns a short-lived URL that your client `POST`s the file to as `multipart/form-data`,
      and the response contains an asset URL you can pass straight into a `generate`
      call.'
    source_release: https://www.krea.ai/docs/changelog
  - quote: Presigned URLs are valid for **three hours** — plenty of time for a client
      to stream the file up before generating.
    source_release: https://www.krea.ai/docs/changelog
  - quote: If your file is already reachable at a public URL, or you can encode it
      as a base64 data URI, skip the upload and pass that value directly instead.
    source_release: https://www.krea.ai/docs/changelog
  extractor_version: fallback-v5
  impact: significant
  kind: launch
  product: krea
  product_name: Krea
  slug: upload-local-files-through-mcp-with-get-upload-url
  source_release: krea-2026-07-01-2026-07-01-workspace-picker-and-presigned-uploads-for-mcp-8107866e
  source_type: krea_changelog
  theme: apps-integrations
  title: Upload local files through MCP with `get_upload_url`
  type: change
related_changes:
- '[[Changes/Devin/2026-07-01-unarchive-on-mention|Unarchive on Mention]]'
- '[[Changes/GitHub Copilot CLI/2026-07-01-2-apps-and-integrations-changes-in-v1-0-68|2
  Apps and Integrations changes in v1.0.68]]'
- '[[Changes/Kimi Code/2026-07-01-plugins-can-now-provide-slash-commands-via-a-commands-field-in-their-manifest-re|Plugins
  can now provide slash commands via a commands field in their manifest…]]'
source_release: '[[Releases/Krea/krea-2026-07-01-2026-07-01-workspace-picker-and-presigned-uploads-for-mcp-8107866e|krea-2026-07-01-2026-07-01-workspace-picker-and-presigned-uploads-for-mcp-8107866e]]'
source_type: krea_changelog
theme: apps-integrations
title: Upload local files through MCP with get_upload_url
type: change
---

<!-- chronolog:begin region="header" -->
# Upload local files through MCP with `get_upload_url`

**Krea** · 2026-07-01 · [[Themes/apps-integrations|Apps and Integrations]] · Launch · [Official source](https://www.krea.ai/docs/changelog) · from [[Releases/Krea/krea-2026-07-01-2026-07-01-workspace-picker-and-presigned-uploads-for-mcp-8107866e|Workspace picker and presigned uploads for MCP]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **The MCP upload flow now uses presigned URLs.** The new `get_upload_url` tool returns a short-lived URL that your client `POST`s the file to as `multipart/form-data`, and the response contains an asset URL you can pass straight into a `generate` call.
>
> Presigned URLs are valid for **three hours** — plenty of time for a client to stream the file up before generating.
>
> If your file is already reachable at a public URL, or you can encode it as a base64 data URI, skip the upload and pass that value directly instead.
>
> Source: https://www.krea.ai/docs/changelog
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Krea/2026-07-01-media-url-inputs-are-consistent-across-the-api|Media URL inputs are consistent across the API]] · Apps and Integrations
- [[Changes/Krea/2026-07-01-choose-a-workspace-when-connecting-to-mcp|Choose a workspace when connecting to MCP]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-07-01 · Kimi Code · [[Changes/Kimi Code/2026-07-01-plugins-can-now-provide-slash-commands-via-a-commands-field-in-their-manifest-re|Plugins can now provide slash commands via a commands field in their manifest…]]
- Later: 2026-07-01 · Notion · [[Changes/Notion/2026-07-01-five-new-mcp-connections-for-custom-agents|Five new MCP connections for Custom Agents]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20krea-2026-07-01-2e11c0&body=Card%3A%20Changes%2FKrea%2F2026-07-01-upload-local-files-through-mcp-with-get-upload-url.md%0ACard%20ID%3A%20krea-2026-07-01-2e11c0%0ASource%3A%20https%3A%2F%2Fwww.krea.ai%2Fdocs%2Fchangelog%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->