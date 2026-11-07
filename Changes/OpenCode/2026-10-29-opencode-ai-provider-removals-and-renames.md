---
card_id: opencode-2026-10-29-ec9cce
date: '2026-10-29'
description: 'OpenCode · 2026-10-29 · Mobile and Desktop: These changes affect code
  that imports @opencode/ai directly. They don''t change the CLI, Desktop, or the
  HTTP API.'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-11-11-command-r-to-insert-a-speaker-label-ctrl-r-on-windows|command
    + R to insert a speaker label (ctrl + R on Windows)]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2909
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: mobile-desktop
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: launch
machine_hash: d00f21a220c5f97806a9f3f27d21e2a9eadcc2374c7e0ac2ac885ec9426aea8d
product: opencode
product_name: OpenCode
record:
  card_id: opencode-2026-10-29-ec9cce
  comparison: ''
  date: '2026-10-29'
  description: 'OpenCode — v2.2.1: These changes affect code that imports @opencode/ai
    directly. They don''t change the CLI, Desktop, or the HTTP API.'
  evidence:
  - quote: These changes affect code that imports @opencode/ai directly. They don't
      change the CLI, Desktop, or the HTTP API.
    source_release: https://opencode.ai/changelog/v2.2.1
  - quote: The fal, Black Forest Labs, Replicate, and Stability providers are removed,
      along with their ./providers/fal , ./providers/black-forest-labs , ./providers/replicate
      , and ./providers/stability entry points.
    source_release: https://opencode.ai/changelog/v2.2.1
  - quote: 'Five legacy entry points are removed. Import the nested paths instead,
      which 2.2.0 already exports: ./providers/amazon-bedrock-mantle → ./providers/amazon-bedrock/mantle
      , and ./providers/google-vertex-chat , -interactions , -mistral , and -responses
      → ./providers/google-vertex/chat , /interactions , /mistral , and /responses
      .'
    source_release: https://opencode.ai/changelog/v2.2.1
  - quote: Each provider's configure() input type is now named Config , for example
      Groq.LanguageModelOptions → Groq.Config , and model() settings are optional
      when every setting is optional.
    source_release: https://opencode.ai/changelog/v2.2.1
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: opencode
  product_name: OpenCode
  slug: opencode-ai-provider-removals-and-renames
  source_release: opencode-2026-10-29-v2-2-1-8378da57
  source_type: opencode_changelog
  theme: mobile-desktop
  title: opencode/ai provider removals and renames
  type: change
related_changes:
- '[[Changes/OpenCode/2026-10-29-10-mobile-and-desktop-changes-in-v2-2-2|10 Mobile
  and Desktop changes in v2.2.2]]'
- '[[Changes/OpenCode/2026-10-29-9-mobile-and-desktop-changes-in-v2-2-1|9 Mobile and
  Desktop changes in v2.2.1]]'
- '[[Changes/OpenCode/2026-10-29-keep-working-toward-a-goal|Keep Working Toward a
  Goal]]'
source_release: '[[Releases/OpenCode/opencode-2026-10-29-v2-2-1-8378da57|opencode-2026-10-29-v2-2-1-8378da57]]'
source_type: opencode_changelog
theme: mobile-desktop
title: opencode/ai provider removals and renames
type: change
---

<!-- chronolog:begin region="header" -->
# opencode/ai provider removals and renames

**OpenCode** · 2026-10-29 · [[Themes/mobile-desktop|Mobile and Desktop]] · Launch · [Official source](https://opencode.ai/changelog/v2.2.1) · from [[Releases/OpenCode/opencode-2026-10-29-v2-2-1-8378da57|v2.2.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> These changes affect code that imports @opencode/ai directly. They don't change the CLI, Desktop, or the HTTP API.
>
> The fal, Black Forest Labs, Replicate, and Stability providers are removed, along with their ./providers/fal , ./providers/black-forest-labs , ./providers/replicate , and ./providers/stability entry points.
>
> Five legacy entry points are removed. Import the nested paths instead, which 2.2.0 already exports: ./providers/amazon-bedrock-mantle → ./providers/amazon-bedrock/mantle , and ./providers/google-vertex-chat , -interactions , -mistral , and -responses → ./providers/google-vertex/chat , /interactions , /mistral , and /responses .
>
> Each provider's configure() input type is now named Config , for example Groq.LanguageModelOptions → Groq.Config , and model() settings are optional when every setting is optional.
>
> Source: https://opencode.ai/changelog/v2.2.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenCode/2026-10-29-terminal-keep-the-activity-spinner-visible-while-a-continued-subagent-runs|Terminal Keep the activity spinner visible while a continued subagent runs]] · Interface Experience
- [[Changes/OpenCode/2026-10-29-generate-images|Generate Images]] · Image Generation
- [[Changes/OpenCode/2026-10-29-sdk-add-client-experimental-schedule-create-list-get-pause-resume-delete-for-man|SDK Add…]] · Automation and Scheduling
- [[Changes/OpenCode/2026-10-29-core-send-image-edit-references-and-image-sizes-in-the-formats-expected-by-openr|Core Send image-edit references and image sizes in the formats expected…]] · Editor Experience
- [[Changes/OpenCode/2026-10-29-new-default-model-picker|New Default Model Picker]] · Model Support
- [[Changes/OpenCode/2026-10-29-2-context-window-changes-in-v2-2-1|2 Context Window changes in v2.2.1]] · Context Window
- [[Changes/OpenCode/2026-10-29-core-add-opt-in-scheduled-prompts-through-schedule-agent-tools-and-experimental|Core Add opt-in scheduled prompts through /schedule , agent tools…]] · Agent Mode
- [[Changes/OpenCode/2026-10-29-9-mobile-and-desktop-changes-in-v2-2-1|9 Mobile and Desktop changes in v2.2.1]] · Mobile and Desktop
- [[Changes/OpenCode/2026-10-29-2-search-and-browsing-changes-in-v2-2-1|2 Search and Browsing changes in v2.2.1]] · Search and Browsing
- [[Changes/OpenCode/2026-10-29-2-model-support-changes-in-v2-2-1|2 Model Support changes in v2.2.1]] · Model Support
- [[Changes/OpenCode/2026-10-29-5-developer-workflow-changes-in-v2-2-1|5 Developer Workflow changes in v2.2.1]] · Developer Workflow
- [[Changes/OpenCode/2026-10-29-core-improve-snapshot-performance-by-coalescing-captures-and-avoiding-repeated-i|Core Improve snapshot performance by coalescing captures and avoiding repeated…]] · Reliability and Performance
- [[Changes/OpenCode/2026-10-29-inspect-background-shells|Inspect Background Shells]] · Interface Experience
- [[Changes/OpenCode/2026-10-29-5-apps-and-integrations-changes-in-v2-2-1|5 Apps and Integrations changes in v2.2.1]] · Apps and Integrations
- [[Changes/OpenCode/2026-10-29-keep-working-toward-a-goal|Keep Working Toward a Goal]] · Mobile and Desktop
- [[Changes/OpenCode/2026-10-29-core-offer-gpt-image-2-after-codex-sign-in-and-add-minimax-and-meta-muse-image-g|Core Offer GPT Image 2 after Codex sign-in and add MiniMax and Meta Muse image…]] · Image Generation
- [[Changes/OpenCode/2026-10-29-core-add-responses-api-support-for-openrouter-digitalocean-and-venice-including|Core Add Responses API support for OpenRouter, DigitalOcean, and Venice, including…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Mobile and Desktop

- Earlier: 2026-10-29 · OpenCode · [[Changes/OpenCode/2026-10-29-10-mobile-and-desktop-changes-in-v2-2-2|10 Mobile and Desktop changes in v2.2.2]]
- Later: 2026-10-29 · Superwhisper · [[Changes/Superwhisper/2026-10-29-s1-mini-tone-slider-updated-to-match-macos|S1-mini tone slider updated to match macOS]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-11-11 · Descript · [[Changes/Descript/2018-11-11-command-r-to-insert-a-speaker-label-ctrl-r-on-windows|command + R to insert a speaker label (ctrl + R on Windows)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20opencode-2026-10-29-ec9cce&body=Card%3A%20Changes%2FOpenCode%2F2026-10-29-opencode-ai-provider-removals-and-renames.md%0ACard%20ID%3A%20opencode-2026-10-29-ec9cce%0ASource%3A%20https%3A%2F%2Fopencode.ai%2Fchangelog%2Fv2.2.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->