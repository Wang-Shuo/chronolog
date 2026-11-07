---
card_id: lm-studio-2024-10-22-1272f5
date: '2024-10-22'
description: 'LM Studio · 2024-10-22 · Other changes: 22 changes in LM Studio 0.3.5
  — New installer'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 09204fbb9f0795b551ac7595cee594affe2034f02436080bad16b9dda354aaf4
product: lm-studio
product_name: LM Studio
record:
  card_id: lm-studio-2024-10-22-1272f5
  comparison: ''
  date: '2024-10-22'
  description: 'LM Studio — LM Studio 0.3.5: 22 other changes'
  evidence:
  - quote: New installer
    source_release: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.3.5
  - quote: OpenAI-like tool calls now supports streaming! (!)
    source_release: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.3.5
  - quote: Improved tool call reliability through sampling configuration for both
      streaming and non-streaming tool use
    source_release: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.3.5
  - quote: 'Bump mlx-engine versions: mlx==0.21.0, mlx_lm==0.20.1, mlx_vlm==0.1.1'
    source_release: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.3.5
  - quote: 'Tool use docs are now up on: https://lmstudio.ai/docs/advanced/tool-use'
    source_release: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.3.5
  - quote: Improved error reporting in the server API
    source_release: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.3.5
  - quote: Passing an empty or null tools array in the API request is treated as no
      tools provided
    source_release: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.3.5
  - quote: New in-app "Quick Docs" with code snippets and tool use examples (top right
      corner)
    source_release: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.3.5
  - quote: Opens in a new window for side-by-side usage in LM Studio
    source_release: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.3.5
  - quote: New role tool in ChatHistoryData that represents the result of a tool call
    source_release: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.3.5
  - quote: Run LM Studio as a service (headless)
    source_release: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.3.5
  - quote: '`lms load`, `lms server start` no longer requires launching the GUI'
    source_release: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.3.5
  - quote: ability to run on machine startup
    source_release: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.3.5
  - quote: Server start / stop button will remember last setting
    source_release: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.3.5
  - quote: This is useful when LM Studio is running as a service
    source_release: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.3.5
  - quote: Hugging Face search now happens automatically without Cmd / Ctrl + Enter
    source_release: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.3.5
  - quote: Update llama.cpp-based JSON response generation; now supports more complex
      JSON schemas
    source_release: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.3.5
  - quote: '[Mac][MLX Engine] Updated Transformers to `4.45.0`'
    source_release: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.3.5
  - quote: '[UI] Move Chat Appearance control to top bar'
    source_release: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.3.5
  - quote: '[UI] Tweaks to size of per-message action buttons'
    source_release: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.3.5
  - quote: Improved German translation thanks to [Goekdeniz-Guelmez](https://github.com/Goekdeniz-Guelmez)
    source_release: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.3.5
  - quote: Indonesian translation thanks to [dwirx](https://github.com/dwirx)
    source_release: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.3.5
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: lm-studio
  product_name: LM Studio
  slug: 22-other-changes-in-lm-studio-0-3-5
  source_release: lm-studio-2024-10-22-0-3-5-cd2c3784
  source_type: lmstudio_changelog
  theme: uncategorized
  title: 22 other changes in LM Studio 0.3.5
  type: change
source_release: '[[Releases/LM Studio/lm-studio-2024-10-22-0-3-5-cd2c3784|lm-studio-2024-10-22-0-3-5-cd2c3784]]'
source_type: lmstudio_changelog
theme: uncategorized
title: 22 other changes in LM Studio 0.3.5
type: change
---

<!-- chronolog:begin region="header" -->
# 22 other changes in LM Studio 0.3.5

**LM Studio** · 2024-10-22 · Other changes · Digest · [Official source](https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.3.5) · from [[Releases/LM Studio/lm-studio-2024-10-22-0-3-5-cd2c3784|LM Studio 0.3.5]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> New installer

> OpenAI-like tool calls now supports streaming! (!)

> Improved tool call reliability through sampling configuration for both streaming and non-streaming tool use

> Bump mlx-engine versions: mlx==0.21.0, mlx_lm==0.20.1, mlx_vlm==0.1.1

> Tool use docs are now up on: https://lmstudio.ai/docs/advanced/tool-use

> Improved error reporting in the server API

> Passing an empty or null tools array in the API request is treated as no tools provided

> New in-app "Quick Docs" with code snippets and tool use examples (top right corner)

> Opens in a new window for side-by-side usage in LM Studio

> New role tool in ChatHistoryData that represents the result of a tool call

> Run LM Studio as a service (headless)

> `lms load`, `lms server start` no longer requires launching the GUI

> ability to run on machine startup

> Server start / stop button will remember last setting

> This is useful when LM Studio is running as a service

> Hugging Face search now happens automatically without Cmd / Ctrl + Enter

> Update llama.cpp-based JSON response generation; now supports more complex JSON schemas

> [Mac][MLX Engine] Updated Transformers to `4.45.0`

> [UI] Move Chat Appearance control to top bar

> [UI] Tweaks to size of per-message action buttons

> Improved German translation thanks to [Goekdeniz-Guelmez](https://github.com/Goekdeniz-Guelmez)

> Indonesian translation thanks to [dwirx](https://github.com/dwirx)

Source: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.3.5
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/LM Studio/2024-10-22-8-model-support-changes-in-lm-studio-0-3-5|8 Model Support changes in LM Studio 0.3.5]] · Model Support
- [[Changes/LM Studio/2024-10-22-2-reliability-and-performance-changes-in-lm-studio-0-3-5|2 Reliability and Performance changes in LM Studio 0.3.5]] · Reliability and Performance
- [[Changes/LM Studio/2024-10-22-2-developer-workflow-changes-in-lm-studio-0-3-5|2 Developer Workflow changes in LM Studio 0.3.5]] · Developer Workflow
- [[Changes/LM Studio/2024-10-22-improved-performance-for-long-context-generation|Improved performance for long context generation]] · Context Window
- [[Changes/LM Studio/2024-10-22-3-interface-experience-changes-in-lm-studio-0-3-5|3 Interface Experience changes in LM Studio 0.3.5]] · Interface Experience
- [[Changes/LM Studio/2024-10-22-mac-mlx-vision-bump-mlx-vlm-version-to-0-0-15-support-qwen2vl|MacMLX Vision Bump mlx-vlm version to 0.0.15, support Qwen2VL]] · Multimodal Input
- [[Changes/LM Studio/2024-10-22-2-accessibility-and-localization-changes-in-lm-studio-0-3-5|2 Accessibility and Localization changes in LM Studio 0.3.5]] · Accessibility and Localization
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20lm-studio-2024-10-22-1272f5&body=Card%3A%20Changes%2FLM%20Studio%2F2024-10-22-22-other-changes-in-lm-studio-0-3-5.md%0ACard%20ID%3A%20lm-studio-2024-10-22-1272f5%0ASource%3A%20https%3A%2F%2Flmstudio.ai%2Fchangelog%2Flmstudio%2Flmstudio-v0.3.5%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->