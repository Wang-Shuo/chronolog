---
card_id: elevenlabs-2025-03-03-d93a13
date: '2025-03-03'
description: 'ElevenLabs · 2025-03-03 · Files and Data: Added `prompt_injectable`
  property to knowledge base…'
diffusion:
  first_in_tracked: '[[Changes/Dify/2023-05-25-2-files-and-data-changes-in-0-2-2|2
    Files and Data changes in 0.2.2]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 648
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: file-data
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: e8ffc6812baf895a86c44f87c27ad681762ae00a82f84b5cb9c6ba14600e66fa
product: elevenlabs
product_name: ElevenLabs
record:
  card_id: elevenlabs-2025-03-03-d93a13
  comparison: ''
  date: '2025-03-03'
  description: 'ElevenLabs — ElevenLabs updates — 2025-03-03: Added `prompt_injectable`
    property to knowledge base [endpoints](https://elevenlabs.io/docs/api-reference/knowledge-base/get-document#response.body.prompt_injectable)'
  evidence:
  - quote: Added `prompt_injectable` property to knowledge base [endpoints](https://elevenlabs.io/docs/api-reference/knowledge-base/get-document#response.body.prompt_injectable)
    source_release: https://elevenlabs.io/docs/changelog/2025/3/3
  - quote: 'Added `name` property to Knowledge Base document [creation](https://elevenlabs.io/docs/api-reference/knowledge-base/create-from-url#request.body.name)
      and [retrieval](https://elevenlabs.io/docs/api-reference/knowledge-base/get-document#response.body.name)
      endpoints:'
    source_release: https://elevenlabs.io/docs/changelog/2025/3/3
  - quote: Added `speed` property to [agent creation](https://elevenlabs.io/docs/api-reference/agents/create#request.body.conversation_config.tts.speed)
    source_release: https://elevenlabs.io/docs/changelog/2025/3/3
  - quote: Removed `secrets` property from agent endpoints (now handled by dedicated
      secrets endpoints)
    source_release: https://elevenlabs.io/docs/changelog/2025/3/3
  - quote: Added [secret deletion endpoint](https://elevenlabs.io/docs/api-reference/workspace/secrets/delete)
      for removing secrets
    source_release: https://elevenlabs.io/docs/changelog/2025/3/3
  - quote: Removed `secrets` property from settings [endpoints](https://elevenlabs.io/docs/api-reference/workspace/get)
    source_release: https://elevenlabs.io/docs/changelog/2025/3/3
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: elevenlabs
  product_name: ElevenLabs
  slug: updated-endpoints
  source_release: elevenlabs-2025-03-03-2025-03-03-b2b19356
  source_type: elevenlabs_changelog
  theme: file-data
  theme_matches: []
  theme_resolution: manual-semantic-rule-v1
  title: Updated Endpoints
  type: change
related_changes:
- "[[Changes/Open WebUI/2025-02-13-jupyter-notebook-support-in-code-interpreter-now-you-can-configure-code-interpre|\U0001F40D
  Jupyter Notebook Support in Code Interpreter]]"
- '[[Changes/Ollama/2025-02-27-granite-3-2-vision-https-ollama-com-library-granite3-2-vision-a-compact-and-effi|Granite-3.2-Vision((source
  link) A compact…]]'
- "[[Changes/Open WebUI/2025-02-27-deduplication-for-retrieved-documents-documents-retrieved-during-searches-are-no|\U0001F5C2️
  Deduplication for Retrieved Documents]]"
source_release: '[[Releases/ElevenLabs/elevenlabs-2025-03-03-2025-03-03-b2b19356|elevenlabs-2025-03-03-2025-03-03-b2b19356]]'
source_type: elevenlabs_changelog
theme: file-data
title: Updated Endpoints
type: change
---

<!-- chronolog:begin region="header" -->
# Updated Endpoints

**ElevenLabs** · 2025-03-03 · [[Themes/file-data|Files and Data]] · [Official source](https://elevenlabs.io/docs/changelog/2025/3/3) · from [[Releases/ElevenLabs/elevenlabs-2025-03-03-2025-03-03-b2b19356|ElevenLabs updates — 2025-03-03]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `prompt_injectable` property to knowledge base [endpoints](https://elevenlabs.io/docs/api-reference/knowledge-base/get-document#response.body.prompt_injectable)
>
> Added `name` property to Knowledge Base document [creation](https://elevenlabs.io/docs/api-reference/knowledge-base/create-from-url#request.body.name) and [retrieval](https://elevenlabs.io/docs/api-reference/knowledge-base/get-document#response.body.name) endpoints:
>
> Added `speed` property to [agent creation](https://elevenlabs.io/docs/api-reference/agents/create#request.body.conversation_config.tts.speed)
>
> Removed `secrets` property from agent endpoints (now handled by dedicated secrets endpoints)
>
> Added [secret deletion endpoint](https://elevenlabs.io/docs/api-reference/workspace/secrets/delete) for removing secrets
>
> Removed `secrets` property from settings [endpoints](https://elevenlabs.io/docs/api-reference/workspace/get)
>
> Source: https://elevenlabs.io/docs/changelog/2025/3/3
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2025-03-03-speech-to-text|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2025-03-03-agents-platform|Agents Platform]] · Agent Mode
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Files and Data

- Earlier: 2025-02-27 · Open WebUI · [[Changes/Open WebUI/2025-02-27-deduplication-for-retrieved-documents-documents-retrieved-during-searches-are-no|🗂️ Deduplication for Retrieved Documents]]
- Later: 2025-03-18 · Dify · [[Changes/Dify/2025-03-18-2-files-and-data-changes-in-1-1-0|2 Files and Data changes in 1.1.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-25 · Dify · [[Changes/Dify/2023-05-25-2-files-and-data-changes-in-0-2-2|2 Files and Data changes in 0.2.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2025-03-03-d93a13&body=Card%3A%20Changes%2FElevenLabs%2F2025-03-03-updated-endpoints.md%0ACard%20ID%3A%20elevenlabs-2025-03-03-d93a13%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2025%2F3%2F3%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->