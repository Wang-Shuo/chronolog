---
card_id: elevenlabs-2026-02-16-601f5f
date: '2026-02-16'
description: 'ElevenLabs · 2026-02-16 · Model Support: `GetPronunciationDictionaryWithRulesResponseModel`
  - Response model with embedded rules array'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1134
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: launch
machine_hash: b69e6902a388501ed146c87c4be3eb9ab019b08cd9389fce9a84979f5eae03d1
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-02-16-601f5f
  comparison: ''
  confidence: low
  date: '2026-02-16'
  description: 'ElevenLabs — ElevenLabs updates — 2026-02-16: `GetPronunciationDictionaryWithRulesResponseModel`
    - Response model with embedded rules array'
  evidence:
  - quote: '`GetPronunciationDictionaryWithRulesResponseModel` - Response model with
      embedded rules array'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/16
  - quote: '`PronunciationDictionaryAliasRuleResponseModel` - Alias rule with `string_to_replace`
      and `alias`'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/16
  - quote: '`PronunciationDictionaryPhonemeRuleResponseModel` - Phoneme rule with
      `string_to_replace`, `phoneme`, and `alphabet`'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/16
  - quote: '`MultiSourceConfigJson` - Multi-source RAG configuration'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/16
  - quote: '`SourceConfigJson` - Individual source configuration for RAG'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/16
  - quote: '`SourceRetrievalConfig` - Retrieval configuration for RAG sources'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/16
  - quote: '`MergingStrategy` - Enum for RAG result merging strategies'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/16
  - quote: '`MCPToolConfig` - Configuration for MCP tools'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/16
  - quote: '`ContentGuardrail-Input`, `ContentGuardrail-Output` - Content moderation
      guardrail configuration'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/16
  - quote: '`ContentConfig` - Content category thresholds configuration'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/16
  - quote: '`TestType` - Enum with values `llm`, `tool`, `simulation`'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/16
  - quote: '`CreateAgentTestResponseModel` - Response for test creation'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/16
  - quote: '`LLMResponseTest*`, `ToolCallTest*`, `SimulationTest*` - Per-type test
      schemas replacing legacy `Create/Get/UpdateUnitTest*` models'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/16
  extractor_version: fallback-v5
  impact: significant
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: new-schemas
  source_release: elevenlabs-2026-02-16-2026-02-16-06b87f89
  source_type: elevenlabs_changelog
  theme: model-support
  title: New Schemas
  type: change
related_changes:
- '[[Changes/Replit/2026-02-13-claude-opus-4-5-support|Claude Opus 4.5 support]]'
- '[[Changes/Ollama/2026-02-14-2-model-support-changes-in-v0-16-2|2 Model Support
  changes in v0.16.2]]'
- '[[Changes/Open WebUI/2026-02-14-6-model-support-changes-in-v0-8-1|6 Model Support
  changes in v0.8.1]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-02-16-2026-02-16-06b87f89|elevenlabs-2026-02-16-2026-02-16-06b87f89]]'
source_type: elevenlabs_changelog
theme: model-support
title: New Schemas
type: change
---

<!-- chronolog:begin region="header" -->
# New Schemas

**ElevenLabs** · 2026-02-16 · [[Themes/model-support|Model Support]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/2/16) · from [[Releases/ElevenLabs/elevenlabs-2026-02-16-2026-02-16-06b87f89|ElevenLabs updates — 2026-02-16]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> `GetPronunciationDictionaryWithRulesResponseModel` - Response model with embedded rules array
>
> `PronunciationDictionaryAliasRuleResponseModel` - Alias rule with `string_to_replace` and `alias`
>
> `PronunciationDictionaryPhonemeRuleResponseModel` - Phoneme rule with `string_to_replace`, `phoneme`, and `alphabet`
>
> `MultiSourceConfigJson` - Multi-source RAG configuration
>
> `SourceConfigJson` - Individual source configuration for RAG
>
> `SourceRetrievalConfig` - Retrieval configuration for RAG sources
>
> `MergingStrategy` - Enum for RAG result merging strategies
>
> `MCPToolConfig` - Configuration for MCP tools
>
> `ContentGuardrail-Input`, `ContentGuardrail-Output` - Content moderation guardrail configuration
>
> `ContentConfig` - Content category thresholds configuration
>
> `TestType` - Enum with values `llm`, `tool`, `simulation`
>
> `CreateAgentTestResponseModel` - Response for test creation
>
> `LLMResponseTest*`, `ToolCallTest*`, `SimulationTest*` - Per-type test schemas replacing legacy `Create/Get/UpdateUnitTest*` models
>
> Source: https://elevenlabs.io/docs/changelog/2026/2/16
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-02-16-widget-packages|Widget Packages]] · Agent Mode
- [[Changes/ElevenLabs/2026-02-16-elevenagents|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-02-16-elevenagents-31304c|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-02-16-javascript-sdk|JavaScript SDK]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-02-16-knowledge-base|Knowledge Base]] · Files and Data
- [[Changes/ElevenLabs/2026-02-16-python-sdk|Python SDK]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-02-16-new-endpoints|New Endpoints]] · Agent Mode
- [[Changes/ElevenLabs/2026-02-16-knowledge-base-d4f24c|Knowledge Base]] · Files and Data
- [[Changes/ElevenLabs/2026-02-16-sdk-releases|SDK Releases]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-02-14 · Open WebUI · [[Changes/Open WebUI/2026-02-14-6-model-support-changes-in-v0-8-1|6 Model Support changes in v0.8.1]]
- Later: 2026-02-16 · Open WebUI · [[Changes/Open WebUI/2026-02-16-4-model-support-changes-in-v0-8-2|4 Model Support changes in v0.8.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-02-16-601f5f&body=Card%3A%20Changes%2FElevenLabs%2F2026-02-16-new-schemas.md%0ACard%20ID%3A%20elevenlabs-2026-02-16-601f5f%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F2%2F16%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->