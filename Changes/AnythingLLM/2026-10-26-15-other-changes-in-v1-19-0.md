---
card_id: anythingllm-2026-10-26-402dfa
date: '2026-10-26'
description: 'AnythingLLM · 2026-10-26 · Other changes: 15 changes in AnythingLLM
  v1.19.0 — Pass your GPU into the container and the engine is accelerated on whatever…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: fc4ab0fed311fcba7f77851a226320ad19fa98e62955c052f93223a58cdc0793
product: anythingllm
product_name: AnythingLLM
record:
  card_id: anythingllm-2026-10-26-402dfa
  comparison: ''
  date: '2026-10-26'
  description: 'AnythingLLM — AnythingLLM v1.19.0: 15 other changes'
  evidence:
  - quote: 'Pass your GPU into the container and the engine is accelerated on whatever
      hardware you have. It picks the fastest backend automatically: CUDA for NVIDIA
      GPUs, Vulkan for AMD and Intel GPUs, or the CPU. It runs on both `amd64` and
      `arm64` hosts.'
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.19.0
  - quote: Color palettes are straightforward thematic tinting you can apply to the
      entire UI. We plan to expand this functionality more so you can more heavily
      customize the UI and even layout. [Learn more](https://docs.anythingllm.com/features/branding)
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.19.0
  - quote: <td><img width="100%" alt="Ocean color palette" src="https://github.com/user-attachments/assets/08c2baa2-9a9b-4ecd-ae95-88e88175ffe5"
      /></td>
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.19.0
  - quote: <td><img width="100%" alt="Forest color palette" src="https://github.com/user-attachments/assets/4274998a-dba8-490e-ab5d-9faecf9248c4"
      /></td>
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.19.0
  - quote: <td><img width="100%" alt="Plum color palette" src="https://github.com/user-attachments/assets/214c3571-7d72-4111-bf08-ce3d60ff1b99"
      /></td>
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.19.0
  - quote: <td><img width="100%" alt="Ember color palette" src="https://github.com/user-attachments/assets/88449231-139c-40a3-bb49-135bd0f1e9fa"
      /></td>
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.19.0
  - quote: Remove open-computer (moved to its own repo) by @timothycarambat in https://github.com/Mintplex-Labs/anything-llm/pull/6727
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.19.0
  - quote: Cap request body size to prevent unauthenticated embed DoS by @timothycarambat
      in https://github.com/Mintplex-Labs/anything-llm/pull/6729
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.19.0
  - quote: Hold clarifying-question timeout once the user starts answering by @timothycarambat
      in https://github.com/Mintplex-Labs/anything-llm/pull/6730
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.19.0
  - quote: Move Weaviate to weaviate-client v3 by @shatfield4 in https://github.com/Mintplex-Labs/anything-llm/pull/6675
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.19.0
  - quote: Stop system prompt variable values from expanding other placeholders by
      @shatfield4 in https://github.com/Mintplex-Labs/anything-llm/pull/6731
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.19.0
  - quote: 'docs: remove references to removed sqlite:migrate script by @jrlprost
      in https://github.com/Mintplex-Labs/anything-llm/pull/6759'
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.19.0
  - quote: Add Hungarian (hu) translation by @Proxy5 in https://github.com/Mintplex-Labs/anything-llm/pull/6757
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.19.0
  - quote: 'feat: instance color palettes and tabbed branding settings by @timothycarambat
      in https://github.com/Mintplex-Labs/anything-llm/pull/6796'
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.19.0
  - quote: 'chore: bump version to 1.19.0 by @timothycarambat in https://github.com/Mintplex-Labs/anything-llm/pull/6822'
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.19.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: anythingllm
  product_name: AnythingLLM
  slug: 15-other-changes-in-v1-19-0
  source_release: anythingllm-2026-10-26-v1-19-0-github-422387962-7ad9a2a3
  source_type: github_releases
  theme: uncategorized
  title: 15 other changes in v1.19.0
  type: change
source_release: '[[Releases/AnythingLLM/anythingllm-2026-10-26-v1-19-0-github-422387962-7ad9a2a3|anythingllm-2026-10-26-v1-19-0-github-422387962-7ad9a2a3]]'
source_type: github_releases
theme: uncategorized
title: 15 other changes in v1.19.0
type: change
---

<!-- chronolog:begin region="header" -->
# 15 other changes in v1.19.0

**AnythingLLM** · 2026-10-26 · Other changes · Digest · [Official source](https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.19.0) · from [[Releases/AnythingLLM/anythingllm-2026-10-26-v1-19-0-github-422387962-7ad9a2a3|AnythingLLM v1.19.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Pass your GPU into the container and the engine is accelerated on whatever hardware you have. It picks the fastest backend automatically: CUDA for NVIDIA GPUs, Vulkan for AMD and Intel GPUs, or the CPU. It runs on both `amd64` and `arm64` hosts.

> Color palettes are straightforward thematic tinting you can apply to the entire UI. We plan to expand this functionality more so you can more heavily customize the UI and even layout. [Learn more](https://docs.anythingllm.com/features/branding)

> \<td>\<img width="100%" alt="Ocean color palette" src="https://github.com/user-attachments/assets/08c2baa2-9a9b-4ecd-ae95-88e88175ffe5" />\</td>

> \<td>\<img width="100%" alt="Forest color palette" src="https://github.com/user-attachments/assets/4274998a-dba8-490e-ab5d-9faecf9248c4" />\</td>

> \<td>\<img width="100%" alt="Plum color palette" src="https://github.com/user-attachments/assets/214c3571-7d72-4111-bf08-ce3d60ff1b99" />\</td>

> \<td>\<img width="100%" alt="Ember color palette" src="https://github.com/user-attachments/assets/88449231-139c-40a3-bb49-135bd0f1e9fa" />\</td>

> Remove open-computer (moved to its own repo) by @timothycarambat in https://github.com/Mintplex-Labs/anything-llm/pull/6727

> Cap request body size to prevent unauthenticated embed DoS by @timothycarambat in https://github.com/Mintplex-Labs/anything-llm/pull/6729

> Hold clarifying-question timeout once the user starts answering by @timothycarambat in https://github.com/Mintplex-Labs/anything-llm/pull/6730

> Move Weaviate to weaviate-client v3 by @shatfield4 in https://github.com/Mintplex-Labs/anything-llm/pull/6675

> Stop system prompt variable values from expanding other placeholders by @shatfield4 in https://github.com/Mintplex-Labs/anything-llm/pull/6731

> docs: remove references to removed sqlite:migrate script by @jrlprost in https://github.com/Mintplex-Labs/anything-llm/pull/6759

> Add Hungarian (hu) translation by @Proxy5 in https://github.com/Mintplex-Labs/anything-llm/pull/6757

> feat: instance color palettes and tabbed branding settings by @timothycarambat in https://github.com/Mintplex-Labs/anything-llm/pull/6796

> chore: bump version to 1.19.0 by @timothycarambat in https://github.com/Mintplex-Labs/anything-llm/pull/6822

Source: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.19.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/AnythingLLM/2026-10-26-2-context-window-changes-in-v1-19-0|2 Context Window changes in v1.19.0]] · Context Window
- [[Changes/AnythingLLM/2026-10-26-6-model-support-changes-in-v1-19-0|6 Model Support changes in v1.19.0]] · Model Support
- [[Changes/AnythingLLM/2026-10-26-chore-drop-api-key-fragments-from-web-search-error-messages-by-u00dxk2-in-https|chore: drop API key fragments from web search error messages]] · Search and Browsing
- [[Changes/AnythingLLM/2026-10-26-apply-workspace-model-changes-to-agent-sessions-mid-thread-by-shatfield4-in-http|Apply workspace model changes to agent sessions mid-thread]] · Agent Mode
- [[Changes/AnythingLLM/2026-10-26-support-mov-files-for-transcription-by-shatfield4-in-https-github-com-mintplex-l|Support .mov files for transcription]] · Voice and Audio
- [[Changes/AnythingLLM/2026-10-26-2-files-and-data-changes-in-v1-19-0|2 Files and Data changes in v1.19.0]] · Files and Data
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20anythingllm-2026-10-26-402dfa&body=Card%3A%20Changes%2FAnythingLLM%2F2026-10-26-15-other-changes-in-v1-19-0.md%0ACard%20ID%3A%20anythingllm-2026-10-26-402dfa%0ASource%3A%20https%3A%2F%2Fgithub.com%2FMintplex-Labs%2Fanything-llm%2Freleases%2Ftag%2Fv1.19.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->