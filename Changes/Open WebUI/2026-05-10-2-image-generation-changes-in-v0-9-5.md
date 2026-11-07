---
card_id: open-webui-2026-05-10-6ec4aa
date: '2026-05-10'
description: "Open WebUI · 2026-05-10 · Image Generation: 2 changes in v0.9.5 — \U0001F50C
  **Channel streaming and tool support.** Mentioning a model in a Channel now streams…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2023-06-26-text-to-image-generation|Text-to-image
    generation]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1049
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: image-generation
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 79ab7f1190bd28df520ded0caa22243dcc118f02242f9214d2be0c1c1d9d8155
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-05-10-6ec4aa
  comparison: ''
  date: '2026-05-10'
  description: 'Open WebUI — v0.9.5: 2 Image Generation changes'
  evidence:
  - quote: "\U0001F50C **Channel streaming and tool support.** Mentioning a model
      in a Channel now streams responses in real time and supports the full chat completion
      pipeline, including native and default function calling, built-in tools (web
      search, image generation), user tools, MCP tools, filters, and RAG knowledge
      injection — the same capabilities available in standard chats."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.5
  - quote: "\U0001F6E1️ **Image generation URL validation.** Generated image URLs
      are now validated through `validate_url()` before fetching, aligning the defense-in-depth
      posture with sibling image-loading paths. [#24518](https://github.com/open-webui/open-webui/pull/24518)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.5
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 2-image-generation-changes-in-v0-9-5
  source_release: open-webui-2026-05-10-v0-9-5-github-320167431-c515d0a2
  source_type: github_releases
  theme: image-generation
  title: 2 Image Generation changes in v0.9.5
  type: change
related_changes:
- '[[Changes/Open WebUI/2026-04-21-4-image-generation-changes-in-v0-9-0|4 Image Generation
  changes in v0.9.0]]'
- '[[Changes/Codex CLI/2026-04-30-19443-add-gpt-image-2-to-bundled-openai-docs-skill-kkahadze-oai|♯19443
  Add gpt-image-2 to bundled OpenAI Docs skill @kkahadze-oai]]'
- '[[Changes/Ollama/2026-05-07-cleaner-image-generation-layout-in-the-mlx-runner|Cleaner
  image generation layout in the MLX runner]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-05-10-v0-9-5-github-320167431-c515d0a2|open-webui-2026-05-10-v0-9-5-github-320167431-c515d0a2]]'
source_type: github_releases
theme: image-generation
title: 2 Image Generation changes in v0.9.5
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Image Generation changes in v0.9.5

**Open WebUI** · 2026-05-10 · [[Themes/image-generation|Image Generation]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.5) · from [[Releases/Open WebUI/open-webui-2026-05-10-v0-9-5-github-320167431-c515d0a2|v0.9.5]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔌 **Channel streaming and tool support.** Mentioning a model in a Channel now streams responses in real time and supports the full chat completion pipeline, including native and default function calling, built-in tools (web search, image generation), user tools, MCP tools, filters, and RAG knowledge injection — the same capabilities available in standard chats.

> 🛡️ **Image generation URL validation.** Generated image URLs are now validated through `validate_url()` before fetching, aligning the defense-in-depth posture with sibling image-loading paths. [#24518](https://github.com/open-webui/open-webui/pull/24518)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.5
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-05-10-url-parser-ssrf-bypass-url-validation-now-rejects-backslash-tab-cr-and-lf-charac|🛡️ URL parser SSRF bypass. URL validation now rejects backslash, tab, CR, and LF…]] · Editor Experience
- [[Changes/Open WebUI/2026-05-10-shared-chat-access-for-owners-and-admins-chat-owners-can-now-view-and-clone-thei|🔐 Shared chat access for owners and admins. Chat owners can now view and clone…]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-05-10-2-developer-workflow-changes-in-v0-9-5|2 Developer Workflow changes in v0.9.5]] · Developer Workflow
- [[Changes/Open WebUI/2026-05-10-6-safety-and-privacy-changes-in-v0-9-5|6 Safety and Privacy changes in v0.9.5]] · Safety and Privacy
- [[Changes/Open WebUI/2026-05-10-2-interface-experience-changes-in-v0-9-5|2 Interface Experience changes in v0.9.5]] · Interface Experience
- [[Changes/Open WebUI/2026-05-10-file-ownership-in-folder-and-knowledge-attachments-attaching-files-to-folders-or|🔐 File ownership in folder and knowledge attachments. Attaching files to folders…]] · Context Window
- [[Changes/Open WebUI/2026-05-10-3-model-support-changes-in-v0-9-5|3 Model Support changes in v0.9.5]] · Model Support
- [[Changes/Open WebUI/2026-05-10-redirect-based-ssrf-protection-all-outbound-http-requests-now-block-3xx-redirect|🛡️ Redirect-based SSRF protection. All outbound HTTP requests now block 3xx…]] · Account and Access
- [[Changes/Open WebUI/2026-05-10-6-other-changes-in-v0-9-5|6 other changes in v0.9.5]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Image Generation

- Earlier: 2026-05-07 · Ollama · [[Changes/Ollama/2026-05-07-cleaner-image-generation-layout-in-the-mlx-runner|Cleaner image generation layout in the MLX runner]]
- Later: 2026-05-14 · Descript · [[Changes/Descript/2026-05-14-gpt-image-2-in-image-generation|GPT Image 2 in image generation]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-06-26 · Descript · [[Changes/Descript/2023-06-26-text-to-image-generation|Text-to-image generation]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-05-10-6ec4aa&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-05-10-2-image-generation-changes-in-v0-9-5.md%0ACard%20ID%3A%20open-webui-2026-05-10-6ec4aa%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.5%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->