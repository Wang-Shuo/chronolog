---
card_id: elevenlabs-2026-03-23-6eac98
date: '2026-03-23'
description: 'ElevenLabs · 2026-03-23 · Model Support: `ConvAIEnvironmentVariable`,
  `ConvAIEnvironmentVariableCreate`, `ConvAIEnvironmentVariableUpdate` - Environment…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1169
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: launch
machine_hash: e7d3e79b7e11596a1ed5315354e8f5db1dde4a97e73c329807ada4aebce41567
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-03-23-6eac98
  comparison: ''
  confidence: low
  date: '2026-03-23'
  description: 'ElevenLabs — ElevenLabs updates — 2026-03-23: `ConvAIEnvironmentVariable`,
    `ConvAIEnvironmentVariableCreate`, `ConvAIEnvironmentVariableUpdate` - Environment
    variable models supporting string, secret, and auth-connection types'
  evidence:
  - quote: '`ConvAIEnvironmentVariable`, `ConvAIEnvironmentVariableCreate`, `ConvAIEnvironmentVariableUpdate`
      - Environment variable models supporting string, secret, and auth-connection
      types'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/23
  - quote: '`ConvAIEnvVarLocator`, `EnvironmentAuthConnectionLocator` - Locators for
      referencing environment variables in tool and MCP server configs'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/23
  - quote: '`EndCallTriggerAction`, `RetryTriggerAction` - Guardrail trigger action
      schemas for end-call and retry-with-feedback behaviors'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/23
  - quote: '`ConditionalOperator` - New AST node for conditional expressions in agent
      workflows'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/23
  - quote: '`AuthConnectionCreateRequest`, `AuthConnectionResponse`, `AuthConnectionDependencies`
      - Workspace auth connection management schemas with support for OAuth2, JWT,
      basic, bearer, custom header, WhatsApp, and integration-managed auth methods'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/23
  - quote: '`SpeechToTextEvaluation*` - Suite of schemas for speech-to-text evaluation
      criteria, evaluations, human agents, and analytics'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/23
  extractor_version: fallback-v5
  impact: significant
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: new-schemas
  source_release: elevenlabs-2026-03-23-2026-03-23-c7dac693
  source_type: elevenlabs_changelog
  theme: model-support
  title: New Schemas
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-03-19-2-model-support-changes-in-rust-v0-116-0|2 Model
  Support changes in rust-v0.116.0]]'
- '[[Changes/GitHub Copilot CLI/2026-03-20-2-model-support-changes-in-v1-0-10|2 Model
  Support changes in v1.0.10]]'
- '[[Changes/OpenCode/2026-03-22-3-model-support-changes-in-v1-3-0|3 Model Support
  changes in v1.3.0]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-03-23-2026-03-23-c7dac693|elevenlabs-2026-03-23-2026-03-23-c7dac693]]'
source_type: elevenlabs_changelog
theme: model-support
title: New Schemas
type: change
---

<!-- chronolog:begin region="header" -->
# New Schemas

**ElevenLabs** · 2026-03-23 · [[Themes/model-support|Model Support]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/3/23) · from [[Releases/ElevenLabs/elevenlabs-2026-03-23-2026-03-23-c7dac693|ElevenLabs updates — 2026-03-23]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> `ConvAIEnvironmentVariable`, `ConvAIEnvironmentVariableCreate`, `ConvAIEnvironmentVariableUpdate` - Environment variable models supporting string, secret, and auth-connection types
>
> `ConvAIEnvVarLocator`, `EnvironmentAuthConnectionLocator` - Locators for referencing environment variables in tool and MCP server configs
>
> `EndCallTriggerAction`, `RetryTriggerAction` - Guardrail trigger action schemas for end-call and retry-with-feedback behaviors
>
> `ConditionalOperator` - New AST node for conditional expressions in agent workflows
>
> `AuthConnectionCreateRequest`, `AuthConnectionResponse`, `AuthConnectionDependencies` - Workspace auth connection management schemas with support for OAuth2, JWT, basic, bearer, custom header, WhatsApp, and integration-managed auth methods
>
> `SpeechToTextEvaluation*` - Suite of schemas for speech-to-text evaluation criteria, evaluations, human agents, and analytics
>
> Source: https://elevenlabs.io/docs/changelog/2026/3/23
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-03-23-speech-to-text|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-03-23-packages|Packages]] · Multimodal Input
- [[Changes/ElevenLabs/2026-03-23-ios-sdk|iOS SDK]] · Mobile and Desktop
- [[Changes/ElevenLabs/2026-03-23-workspaces|Workspaces]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-03-23-packages-v1-0-0-release-candidate|Packages v1.0.0 Release Candidate]] · Reliability and Performance
- [[Changes/ElevenLabs/2026-03-23-elevenagents|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-03-23-sdk-releases|SDK Releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-03-23-javascript-sdk|JavaScript SDK]] · Multimodal Input
- [[Changes/ElevenLabs/2026-03-23-python-sdk|Python SDK]] · Agent Mode
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-03-22 · OpenCode · [[Changes/OpenCode/2026-03-22-3-model-support-changes-in-v1-3-0|3 Model Support changes in v1.3.0]]
- Later: 2026-03-23 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-03-23-ensure-models-appear-in-picker-correctly-display-model-names-where-possible|Ensure models appear in picker correctly, display model names where possible]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-03-23-6eac98&body=Card%3A%20Changes%2FElevenLabs%2F2026-03-23-new-schemas.md%0ACard%20ID%3A%20elevenlabs-2026-03-23-6eac98%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F3%2F23%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->