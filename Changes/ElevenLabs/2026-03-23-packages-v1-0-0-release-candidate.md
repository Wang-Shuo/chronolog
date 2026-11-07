---
card_id: elevenlabs-2026-03-23-88c652
date: '2026-03-23'
description: 'ElevenLabs · 2026-03-23 · Reliability and Performance: The first release
  candidate for v1.0.0 of the ElevenAgents client SDKs is now available. This is a
  major…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-11-19-opening-projects-is-now-much-faster|Opening
    Projects is now much faster]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2681
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: 9405d13b4ba52b16e40aa70af015b2641f1287f3339c6f7b6910aa023d8c5a59
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-03-23-88c652
  comparison: ''
  confidence: low
  date: '2026-03-23'
  description: 'ElevenLabs — ElevenLabs updates — 2026-03-23: The first release candidate
    for v1.0.0 of the ElevenAgents client SDKs is now available. This is a major release
    with breaking changes that improve the API surface, add granular React hooks for
    better render performance, and unify the React Native SDK with the React SDK.'
  evidence:
  - quote: The first release candidate for v1.0.0 of the ElevenAgents client SDKs
      is now available. This is a major release with breaking changes that improve
      the API surface, add granular React hooks for better render performance, and
      unify the React Native SDK with the React SDK.
    source_release: https://elevenlabs.io/docs/changelog/2026/3/23
  - quote: 'To try out the release candidate:'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/23
  - quote: An [`elevenlabs:sdk-migration`](https://github.com/elevenlabs/packages/blob/main/.agents/skills/elevenlabs%3Asdk-migration/SKILL.md)
      skill is available to help AI coding assistants automatically migrate your codebase
      to the new APIs. Add it to your Claude Code, Cursor, or Windsurf project to
      get guided migration support.
    source_release: https://elevenlabs.io/docs/changelog/2026/3/23
  - quote: 'Key changes in v1.0.0:'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/23
  - quote: '**`@elevenlabs/client`**: `Conversation` is now a namespace object and
      type alias for `TextConversation | VoiceConversation` instead of a class. The
      `Input` and `Output` classes are replaced by `InputController` and `OutputController`
      interfaces, with new convenience methods on the conversation instance (`setMicMuted()`,
      `setVolume()`, `getInputByteFrequencyData()`, `getOutputByteFrequencyData()`).
      `changeInputDevice()` and `changeOutputDevice()` now return `void`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/23
  - quote: '**`@elevenlabs/react`**: `useConversation` now requires a `ConversationProvider`
      ancestor. New granular hooks for fine-grained re-rendering: `useConversationControls()`,
      `useConversationStatus()`, `useConversationInput()`, `useConversationMode()`,
      `useConversationFeedback()`. New `useConversationClientTool()` hook for dynamically
      registering client tools from React components with full type safety.'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/23
  - quote: '**`@elevenlabs/react-native`**: Complete API rewrite replacing `ElevenLabsProvider`
      and `useConversation` with `ConversationProvider` and the same granular hooks
      from `@elevenlabs/react`. WebRTC polyfills and native AudioSession configuration
      are applied automatically on import.'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/23
  - quote: '[@elevenlabs/client@1.0.0-rc.1](https://github.com/elevenlabs/packages/releases/tag/@elevenlabs/client@1.0.0-rc.1)'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/23
  - quote: '[@elevenlabs/react@1.0.0-rc.1](https://github.com/elevenlabs/packages/releases/tag/@elevenlabs/react@1.0.0-rc.1)'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/23
  - quote: '[@elevenlabs/react-native@1.0.0-rc.1](https://github.com/elevenlabs/packages/releases/tag/@elevenlabs/react-native@1.0.0-rc.1)'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/23
  - quote: '[@elevenlabs/types@0.7.0-rc.0](https://github.com/elevenlabs/packages/releases/tag/@elevenlabs/types@0.7.0-rc.0)'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/23
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: packages-v1-0-0-release-candidate
  source_release: elevenlabs-2026-03-23-2026-03-23-c7dac693
  source_type: elevenlabs_changelog
  theme: reliability-performance
  title: Packages v1.0.0 Release Candidate
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-03-20-reduced-memory-usage-when-viewing-large-files-in-their-entirety|Reduced
  memory usage when viewing large files in their entirety]]'
- '[[Changes/Midjourney/2026-03-21-two-versions-of-sref-moodboards-now-available|Two
  Versions of SREF / Moodboards now available]]'
- '[[Changes/OpenCode/2026-03-22-providers-models-xai-responses-api-improved-xai-reasoning-models-performance-in|Providers
  & Models xAI Responses API]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-03-23-2026-03-23-c7dac693|elevenlabs-2026-03-23-2026-03-23-c7dac693]]'
source_type: elevenlabs_changelog
theme: reliability-performance
title: Packages v1.0.0 Release Candidate
type: change
---

<!-- chronolog:begin region="header" -->
# Packages v1.0.0 Release Candidate

**ElevenLabs** · 2026-03-23 · [[Themes/reliability-performance|Reliability and Performance]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/3/23) · from [[Releases/ElevenLabs/elevenlabs-2026-03-23-2026-03-23-c7dac693|ElevenLabs updates — 2026-03-23]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> The first release candidate for v1.0.0 of the ElevenAgents client SDKs is now available. This is a major release with breaking changes that improve the API surface, add granular React hooks for better render performance, and unify the React Native SDK with the React SDK.
>
> To try out the release candidate:
>
> An [`elevenlabs:sdk-migration`](https://github.com/elevenlabs/packages/blob/main/.agents/skills/elevenlabs%3Asdk-migration/SKILL.md) skill is available to help AI coding assistants automatically migrate your codebase to the new APIs. Add it to your Claude Code, Cursor, or Windsurf project to get guided migration support.
>
> Key changes in v1.0.0:
>
> **`@elevenlabs/client`**: `Conversation` is now a namespace object and type alias for `TextConversation | VoiceConversation` instead of a class. The `Input` and `Output` classes are replaced by `InputController` and `OutputController` interfaces, with new convenience methods on the conversation instance (`setMicMuted()`, `setVolume()`, `getInputByteFrequencyData()`, `getOutputByteFrequencyData()`). `changeInputDevice()` and `changeOutputDevice()` now return `void`.
>
> **`@elevenlabs/react`**: `useConversation` now requires a `ConversationProvider` ancestor. New granular hooks for fine-grained re-rendering: `useConversationControls()`, `useConversationStatus()`, `useConversationInput()`, `useConversationMode()`, `useConversationFeedback()`. New `useConversationClientTool()` hook for dynamically registering client tools from React components with full type safety.
>
> **`@elevenlabs/react-native`**: Complete API rewrite replacing `ElevenLabsProvider` and `useConversation` with `ConversationProvider` and the same granular hooks from `@elevenlabs/react`. WebRTC polyfills and native AudioSession configuration are applied automatically on import.
>
> [@elevenlabs/client@1.0.0-rc.1](https://github.com/elevenlabs/packages/releases/tag/@elevenlabs/client@1.0.0-rc.1)
>
> [@elevenlabs/react@1.0.0-rc.1](https://github.com/elevenlabs/packages/releases/tag/@elevenlabs/react@1.0.0-rc.1)
>
> [@elevenlabs/react-native@1.0.0-rc.1](https://github.com/elevenlabs/packages/releases/tag/@elevenlabs/react-native@1.0.0-rc.1)
>
> [@elevenlabs/types@0.7.0-rc.0](https://github.com/elevenlabs/packages/releases/tag/@elevenlabs/types@0.7.0-rc.0)
>
> Source: https://elevenlabs.io/docs/changelog/2026/3/23
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-03-23-speech-to-text|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-03-23-packages|Packages]] · Multimodal Input
- [[Changes/ElevenLabs/2026-03-23-ios-sdk|iOS SDK]] · Mobile and Desktop
- [[Changes/ElevenLabs/2026-03-23-workspaces|Workspaces]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-03-23-new-schemas|New Schemas]] · Model Support
- [[Changes/ElevenLabs/2026-03-23-elevenagents|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-03-23-sdk-releases|SDK Releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-03-23-javascript-sdk|JavaScript SDK]] · Multimodal Input
- [[Changes/ElevenLabs/2026-03-23-python-sdk|Python SDK]] · Agent Mode
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2026-03-22 · OpenCode · [[Changes/OpenCode/2026-03-22-providers-models-xai-responses-api-improved-xai-reasoning-models-performance-in|Providers & Models xAI Responses API]]
- Later: 2026-03-24 · Devin · [[Changes/Devin/2026-03-24-various-bug-fixes-and-performance-improvements-across-the-platform|Various bug fixes and performance improvements across the platform]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-11-19 · Descript · [[Changes/Descript/2018-11-19-opening-projects-is-now-much-faster|Opening Projects is now much faster]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-03-23-88c652&body=Card%3A%20Changes%2FElevenLabs%2F2026-03-23-packages-v1-0-0-release-candidate.md%0ACard%20ID%3A%20elevenlabs-2026-03-23-88c652%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F3%2F23%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->