---
card_id: kimi-code-2026-07-10-807c6b
date: '2026-07-10'
description: 'Kimi Code · 2026-07-10 · Model Support: Keep image-heavy sessions within
  provider request-size limits: oversized images (model-read and pasted, including
  WebP)…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1278
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: change
machine_hash: f6bab4df8eedf885b3a6c80f497a0ffcbb853fe16931966e0e8f555b9f45840d
product: kimi-code
product_name: Kimi Code
record:
  ai_generated: true
  card_id: kimi-code-2026-07-10-807c6b
  comparison: ''
  confidence: low
  date: '2026-07-10'
  description: 'Kimi Code — Kimi Code 0.23.4 (2026-07-10): Keep image-heavy sessions
    within provider request-size limits: oversized images (model-read and pasted,
    including WebP) are downscaled and compressed, HEIC/HEIF reads are refused with
    a platform-matched conversion command instead of poisoning the session, and an
    HTTP 413 request-too-large now recovers automatically — the request and `/compact`
    retry with older media replaced by text markers. The limits are configurable via
    `[image]` in `config.toml` (or `KIMI_IMAGE_*` env vars), and each core keeps its
    own settings so reloading one client''s config no longer changes another client''s
    compression.'
  evidence:
  - quote: 'Keep image-heavy sessions within provider request-size limits: oversized
      images (model-read and pasted, including WebP) are downscaled and compressed,
      HEIC/HEIF reads are refused with a platform-matched conversion command instead
      of poisoning the session, and an HTTP 413 request-too-large now recovers automatically
      — the request and `/compact` retry with older media replaced by text markers.
      The limits are configurable via `[image]` in `config.toml` (or `KIMI_IMAGE_*`
      env vars), and each core keeps its own settings so reloading one client''s config
      no longer changes another client''s compression.'
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  extractor_version: fallback-v5
  impact: significant
  kind: change
  product: kimi-code
  product_name: Kimi Code
  slug: keep-image-heavy-sessions-within-provider-request-size-limits-oversized-images-m
  source_release: kimi-code-2026-07-10-0-23-4-eaffeeb0
  source_type: kimi_code_changelog
  theme: model-support
  title: Keep image-heavy sessions within provider request-size limits
  type: change
related_changes:
- '[[Changes/OpenCode/2026-07-09-2-model-support-changes-in-v1-17-16|2 Model Support
  changes in v1.17.16]]'
- '[[Changes/Claude Code/2026-07-10-improved-code-review-findings-quality-on-claude-opus-4-8-across-all-effort-level|Improved
  /code-review findings quality on claude-opus-4-8 across all effort levels]]'
- '[[Changes/GitHub Copilot CLI/2026-07-10-4-model-support-changes-in-v1-0-70|4 Model
  Support changes in v1.0.70]]'
source_release: '[[Releases/Kimi Code/kimi-code-2026-07-10-0-23-4-eaffeeb0|kimi-code-2026-07-10-0-23-4-eaffeeb0]]'
source_type: kimi_code_changelog
theme: model-support
title: Keep image-heavy sessions within provider request-size limits
type: change
---

<!-- chronolog:begin region="header" -->
# Keep image-heavy sessions within provider request-size limits

**Kimi Code** · 2026-07-10 · [[Themes/model-support|Model Support]] · [Official source](https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md) · from [[Releases/Kimi Code/kimi-code-2026-07-10-0-23-4-eaffeeb0|Kimi Code 0.23.4 (2026-07-10)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Keep image-heavy sessions within provider request-size limits: oversized images (model-read and pasted, including WebP) are downscaled and compressed, HEIC/HEIF reads are refused with a platform-matched conversion command instead of poisoning the session, and an HTTP 413 request-too-large now recovers automatically — the request and `/compact` retry with older media replaced by text markers. The limits are configurable via `[image]` in `config.toml` (or `KIMI_IMAGE_*` env vars), and each core keeps its own settings so reloading one client's config no longer changes another client's compression.
>
> Source: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Kimi Code/2026-07-10-2-interface-experience-changes-in-kimi-code-0-23-4|2 Interface Experience changes in Kimi Code 0.23.4]] · Interface Experience
- [[Changes/Kimi Code/2026-07-10-3-other-changes-in-kimi-code-0-23-4|3 other changes in Kimi Code 0.23.4]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-07-10 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-07-10-4-model-support-changes-in-v1-0-70|4 Model Support changes in v1.0.70]]
- Later: 2026-07-11 · Claude Code · [[Changes/Claude Code/2026-07-11-changed-bedrock-vertex-and-claude-platform-on-aws-to-default-to-claude-opus-4-8|Changed Bedrock, Vertex, and Claude Platform on AWS to default to Claude Opus 4.8]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20kimi-code-2026-07-10-807c6b&body=Card%3A%20Changes%2FKimi%20Code%2F2026-07-10-keep-image-heavy-sessions-within-provider-request-size-limits-oversized-images-m.md%0ACard%20ID%3A%20kimi-code-2026-07-10-807c6b%0ASource%3A%20https%3A%2F%2Fgithub.com%2FMoonshotAI%2Fkimi-code%2Fblob%2Fmain%2Fdocs%2Fen%2Frelease-notes%2Fchangelog.md%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->