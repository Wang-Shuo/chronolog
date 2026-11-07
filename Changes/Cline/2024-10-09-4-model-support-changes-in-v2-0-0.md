---
card_id: cline-2024-10-09-686ddf
date: '2024-10-09'
description: 'Cline · 2024-10-09 · Model Support: 4 changes in v2.0.0 — **New name:**
  Meet Cline, an AI assistant that can use your **CLI** a**N**d **E**ditor. While
  “Claude…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 639
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 94e637ee3f018cb61bb681c45c2f5dd110b75de233928c8a772e6fc3ed75ce96
product: cline
product_name: Cline
record:
  card_id: cline-2024-10-09-686ddf
  comparison: ''
  date: '2024-10-09'
  description: 'Cline — v2.0.0: 4 Model Support changes'
  evidence:
  - quote: '**New name:** Meet Cline, an AI assistant that can use your **CLI** a**N**d
      **E**ditor. While “Claude Dev” was a tribute to Claude 3.5 Sonnet, v2.0 brings
      updates that significantly improve performance across other models making it
      a good opportunity to give the extension its own identity.'
    source_release: https://github.com/cline/cline/releases/tag/v2.0.0
  - quote: '**40% fewer requests to accomplish tasks + better performance with other
      models:** This update **r**eplaces the rigid tool use API with a customized
      XML tags approach, allowing for more flexible tool interactions and significantly
      improving results for non-Claude models. Behind the scenes, older versions of
      the extension used an API feature called “Tool Use” (AKA “Function Calling”)
      where tools like `read_file` and `execute_command` were defined in a strict
      JSON schema sent with each request, requiring models to respond with a structured
      output that had to fit into this schema. While some models like Claude 3.5 Sonnet
      are heavily fine-tuned to be good at this, other models like Llama and DeepSeek
      are not as adept, often leading to inability to complete even the most basic
      tasks. This not only limited the extension’s accessibility with other models,
      but also diminished Claude 3.5 Sonnet’s potential as forcing any model to respond
      in structured output has been proven to have negative qualitative effects. To
      eliminate these bottlenecks while still giving models the ability to invoke
      tools, I took inspiration from [this study](https://arxiv.org/html/2407.04997v1)
      showing how prompt-engineering can enable stable tool-calling capabilities +
      [Anthropic’s prompt to achieve their Artifacts feature](https://gist.github.com/dedlim/6bf6d81f77c19e20cd40594aa09e3ecd)
      (uses tags like `<antArtifact>`) to create a completely re-imagined system prompt
      where models are effectively fine-tuned on the spot how to best interact with
      Cline’s toolset. Instead of having to respond in a rigid JSON format, models
      can now invoke tools in unstructured text with XML tags like `<read_file>` and
      `<execute_command>`. Since we define the tool use guidelines ourselves we can
      even tailor it with context like “these tools are executed upon the user''s
      approval” instead of relying on the generalized internal prompts that Anthropic
      uses to achieve tool calling for their API. To quantify the improvement these
      changes made, I ran a simple benchmark: I gave the following task in a Next.js
      app “Implement a dark mode toggle feature, and save the user’s preference to
      persist across sessions” and measured the # of requests until the task was successfully
      completed. This was a practical scenario that tested models’ abilities to use
      the appropriate tools to explore an existing project’s source code, apply edits,
      and debug issues that came up along the way.'
    source_release: https://github.com/cline/cline/releases/tag/v2.0.0
  - quote: 'Claude 3.5 Sonnet saw a ~40% reduction in # of requests required to accomplish
      the task, while other models like Llama and DeepSeek are now not only able to
      tool call more reliably but seem to have a greater capacity to reason about
      executing tasks successfully.'
    source_release: https://github.com/cline/cline/releases/tag/v2.0.0
  - quote: '**Search and use any OpenRouter model:** the extension automatically fetches
      the latest model list + pricing details, giving you access to the newest models
      as soon as they’re available. Try searching “free” to find no-cost options.'
    source_release: https://github.com/cline/cline/releases/tag/v2.0.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: cline
  product_name: Cline
  slug: 4-model-support-changes-in-v2-0-0
  source_release: cline-2024-10-09-v2-0-0-github-179063623-cccde13e
  source_type: github_releases
  theme: model-support
  title: 4 Model Support changes in v2.0.0
  type: change
related_changes:
- '[[Changes/Aider/2024-10-04-sanity-checks-the-editor-model-on-launch-now-same-as-main-and-weak-models|Sanity
  checks the --editor-model on launch now, same as main and weak models]]'
- '[[Changes/Open WebUI/2024-10-07-3-model-support-changes-in-v0-3-31|3 Model Support
  changes in v0.3.31]]'
- "[[Changes/Open WebUI/2024-10-07-workspace-enhancements-added-a-display-count-for-models-prompts-tools-and-functi|\U0001F522
  Workspace Enhancements]]"
source_release: '[[Releases/Cline/cline-2024-10-09-v2-0-0-github-179063623-cccde13e|cline-2024-10-09-v2-0-0-github-179063623-cccde13e]]'
source_type: github_releases
theme: model-support
title: 4 Model Support changes in v2.0.0
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Model Support changes in v2.0.0

**Cline** · 2024-10-09 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/cline/cline/releases/tag/v2.0.0) · from [[Releases/Cline/cline-2024-10-09-v2-0-0-github-179063623-cccde13e|v2.0.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **New name:** Meet Cline, an AI assistant that can use your **CLI** a**N**d **E**ditor. While “Claude Dev” was a tribute to Claude 3.5 Sonnet, v2.0 brings updates that significantly improve performance across other models making it a good opportunity to give the extension its own identity.

> **40% fewer requests to accomplish tasks + better performance with other models:** This update **r**eplaces the rigid tool use API with a customized XML tags approach, allowing for more flexible tool interactions and significantly improving results for non-Claude models. Behind the scenes, older versions of the extension used an API feature called “Tool Use” (AKA “Function Calling”) where tools like `read_file` and `execute_command` were defined in a strict JSON schema sent with each request, requiring models to respond with a structured output that had to fit into this schema. While some models like Claude 3.5 Sonnet are heavily fine-tuned to be good at this, other models like Llama and DeepSeek are not as adept, often leading to inability to complete even the most basic tasks. This not only limited the extension’s accessibility with other models, but also diminished Claude 3.5 Sonnet’s potential as forcing any model to respond in structured output has been proven to have negative qualitative effects. To eliminate these bottlenecks while still giving models the ability to invoke tools, I took inspiration from [this study](https://arxiv.org/html/2407.04997v1) showing how prompt-engineering can enable stable tool-calling capabilities + [Anthropic’s prompt to achieve their Artifacts feature](https://gist.github.com/dedlim/6bf6d81f77c19e20cd40594aa09e3ecd) (uses tags like `<antArtifact>`) to create a completely re-imagined system prompt where models are effectively fine-tuned on the spot how to best interact with Cline’s toolset. Instead of having to respond in a rigid JSON format, models can now invoke tools in unstructured text with XML tags like `<read_file>` and `<execute_command>`. Since we define the tool use guidelines ourselves we can even tailor it with context like “these tools are executed upon the user's approval” instead of relying on the generalized internal prompts that Anthropic uses to achieve tool calling for their API. To quantify the improvement these changes made, I ran a simple benchmark: I gave the following task in a Next.js app “Implement a dark mode toggle feature, and save the user’s preference to persist across sessions” and measured the # of requests until the task was successfully completed. This was a practical scenario that tested models’ abilities to use the appropriate tools to explore an existing project’s source code, apply edits, and debug issues that came up along the way.

> Claude 3.5 Sonnet saw a ~40% reduction in # of requests required to accomplish the task, while other models like Llama and DeepSeek are now not only able to tool call more reliably but seem to have a greater capacity to reason about executing tasks successfully.

> **Search and use any OpenRouter model:** the extension automatically fetches the latest model list + pricing details, giving you access to the newest models as soon as they’re available. Try searching “free” to find no-cost options.

Source: https://github.com/cline/cline/releases/tag/v2.0.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Cline/2024-10-09-new-readme-and-got-a-cool-domain-for-the-project-https-cline-bot-wip-on-a-final|New README and got a cool domain for the project (source link) (wip)]] · Collaboration
- [[Changes/Cline/2024-10-09-2-reliability-and-performance-changes-in-v2-0-0|2 Reliability and Performance changes in v2.0.0]] · Reliability and Performance
- [[Changes/Cline/2024-10-09-no-more-staring-at-loading-spinners-responses-are-now-streamed-into-the-editor-a|No more staring at loading spinners: Responses are now streamed into the editor…]] · Editor Experience
- [[Changes/Cline/2024-10-09-3-other-changes-in-v2-0-0|3 other changes in v2.0.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2024-10-07 · Open WebUI · [[Changes/Open WebUI/2024-10-07-workspace-enhancements-added-a-display-count-for-models-prompts-tools-and-functi|🔢 Workspace Enhancements]]
- Later: 2024-10-09 · Gemini · [[Changes/Gemini/2024-10-09-introducing-imagen-3|Introducing Imagen 3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20cline-2024-10-09-686ddf&body=Card%3A%20Changes%2FCline%2F2024-10-09-4-model-support-changes-in-v2-0-0.md%0ACard%20ID%3A%20cline-2024-10-09-686ddf%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fcline%2Fcline%2Freleases%2Ftag%2Fv2.0.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->