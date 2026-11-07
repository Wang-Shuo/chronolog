---
card_id: krea-2026-10-24-5d6031
date: '2026-10-24'
description: 'Krea · 2026-10-24 · Image Generation: **OpenAI shut down `gpt-image-1`
  on October 23, so ChatGPT Image is no longer available.** Use ChatGPT Image 2 instead.'
diffusion:
  first_in_tracked: '[[Changes/Descript/2023-06-26-text-to-image-generation|Text-to-image
    generation]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1216
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: image-generation
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: policy
machine_hash: ca4e8942b685a66f9086171dae487f01e857aa44dbe917263678d92215975cde
product: krea
product_name: Krea
record:
  card_id: krea-2026-10-24-5d6031
  comparison: ''
  date: '2026-10-24'
  description: 'Krea — Audio tool and voice cloning for everyone, Nodes Apps management,
    workspace usage by member, model retirements including ChatGPT Image, bounding
    boxes and regional edits with Krea 3 Ultra and Zero Data Retention, and video
    fixes: **OpenAI shut down `gpt-image-1` on October 23, so ChatGPT Image is no
    longer available.** Use ChatGPT Image 2 instead.'
  evidence:
  - quote: '**OpenAI shut down `gpt-image-1` on October 23, so ChatGPT Image is no
      longer available.** Use ChatGPT Image 2 instead.'
    source_release: https://www.krea.ai/docs/changelog
  - quote: In the API, `image/openai/gpt-image` now returns `410 Gone`.
    source_release: https://www.krea.ai/docs/changelog
  - quote: Switch your request path to `image/openai/gpt-image-2`. `prompt`, `quality`,
      and `imageUrls` carry over. `presetStyles` is not supported.
    source_release: https://www.krea.ai/docs/changelog
  extractor_version: fallback-v5
  impact: incremental
  kind: policy
  product: krea
  product_name: Krea
  slug: chatgpt-image-retired
  source_release: krea-2026-10-24-2026-10-24-audio-tool-and-voice-cloning-for-everyone-nodes-apps-ec55257e
  source_type: krea_changelog
  theme: image-generation
  title: ChatGPT Image retired
  type: change
related_changes:
- '[[Changes/Krea/2026-10-15-krea-3-api-in-early-access|Krea 3 API in early access]]'
- "[[Changes/Open WebUI/2026-10-16-clear-input-selections-shortcut-clearing-the-model-override-selected-tools-and-f|\U0001F9F9
  Clear Input Selections shortcut. Clearing the model override, selected tools…]]"
- '[[Changes/Codex CLI/2026-10-23-2-image-generation-changes-in-rust-v0-164-0|2 Image
  Generation changes in rust-v0.164.0]]'
source_release: '[[Releases/Krea/krea-2026-10-24-2026-10-24-audio-tool-and-voice-cloning-for-everyone-nodes-apps-ec55257e|krea-2026-10-24-2026-10-24-audio-tool-and-voice-cloning-for-everyone-nodes-apps-ec55257e]]'
source_type: krea_changelog
theme: image-generation
title: ChatGPT Image retired
type: change
---

<!-- chronolog:begin region="header" -->
# ChatGPT Image retired

**Krea** · 2026-10-24 · [[Themes/image-generation|Image Generation]] · Policy · [Official source](https://www.krea.ai/docs/changelog) · from [[Releases/Krea/krea-2026-10-24-2026-10-24-audio-tool-and-voice-cloning-for-everyone-nodes-apps-ec55257e|Audio tool and voice cloning for everyone, Nodes Apps management, workspace usage by member, model retirements including ChatGPT Image, bounding boxes and regional edits with Krea 3 Ultra and Zero Data Retention, and video fixes]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **OpenAI shut down `gpt-image-1` on October 23, so ChatGPT Image is no longer available.** Use ChatGPT Image 2 instead.
>
> In the API, `image/openai/gpt-image` now returns `410 Gone`.
>
> Switch your request path to `image/openai/gpt-image-2`. `prompt`, `quality`, and `imageUrls` carry over. `presetStyles` is not supported.
>
> Source: https://www.krea.ai/docs/changelog
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Krea/2026-10-24-workspace-usage-by-member|Workspace usage by member]] · Pricing Model
- [[Changes/Krea/2026-10-24-video-upscale-picks-up-where-you-left-off|Video upscale picks up where you left off]] · Multimodal Input
- [[Changes/Krea/2026-10-24-reuse-parameters-on-the-video-tool-no-longer-crashes|Reuse parameters on the Video tool no longer crashes]] · Multimodal Input
- [[Changes/Krea/2026-10-24-audio-tool-and-voice-cloning-for-everyone|Audio tool and voice cloning for everyone]] · Voice and Audio
- [[Changes/Krea/2026-10-24-bounding-boxes-and-regional-edits-work-with-krea-3-ultra|Bounding boxes and regional edits work with Krea 3 Ultra]] · Editor Experience
- [[Changes/Krea/2026-10-24-more-agent-nodes-and-plugin-polish|More Agent, Nodes, and plugin polish]] · Apps and Integrations
- [[Changes/Krea/2026-10-24-sort-filter-and-delete-nodes-apps|Sort, filter, and delete Nodes Apps]] · Apps and Integrations
- [[Changes/Krea/2026-10-24-nodes-projects-with-old-veo-3-nodes-open-correctly|Nodes projects with old Veo 3 nodes open correctly]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Image Generation

- Earlier: 2026-10-23 · Codex CLI · [[Changes/Codex CLI/2026-10-23-2-image-generation-changes-in-rust-v0-164-0|2 Image Generation changes in rust-v0.164.0]]
- Later: 2026-10-25 · Open WebUI · [[Changes/Open WebUI/2026-10-25-images-settings-save-admins-can-now-save-images-settings-while-image-generation|🖌️ Images settings save. Admins can now save Images settings while Image…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-06-26 · Descript · [[Changes/Descript/2023-06-26-text-to-image-generation|Text-to-image generation]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20krea-2026-10-24-5d6031&body=Card%3A%20Changes%2FKrea%2F2026-10-24-chatgpt-image-retired.md%0ACard%20ID%3A%20krea-2026-10-24-5d6031%0ASource%3A%20https%3A%2F%2Fwww.krea.ai%2Fdocs%2Fchangelog%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->