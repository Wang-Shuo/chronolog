---
card_id: anythingllm-2026-05-26-ebc1a7
date: '2026-05-26'
description: 'AnythingLLM · 2026-05-26 · Memory and Personalization: 10 changes in
  AnythingLLM v1.13.0 - A Hybrid AI Experience — AnythingLLM now supports automatic
  memory…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1041
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: e448d0e19c57d1470dd9767cacccaf48437e8f6a2525634d5c11c0e79e6eb274
product: anythingllm
product_name: AnythingLLM
record:
  card_id: anythingllm-2026-05-26-ebc1a7
  comparison: ''
  date: '2026-05-26'
  description: 'AnythingLLM — AnythingLLM v1.13.0 - A Hybrid AI Experience: 10 Memory
    and Personalization changes'
  evidence:
  - quote: AnythingLLM now supports automatic memory extraction and personalization
      so your AI assistant can remember what you've talked about and use that knowledge
      to personalize its responses.
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.13.0
  - quote: AnythingLLM runs a background job to extract memories from your chats and
      store them in a memory bank. This memory bank is then used to personalize the
      responses of your AI assistant - you have full control over what is remembered
      and how it is used
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.13.0
  - quote: you can even add memories manually to the memory bank if you dont want
      to have the model spend cycles reviewing chat history.
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.13.0
  - quote: 'There are two types of memories:'
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.13.0
  - quote: 'Workspace memories: These are memories that are specific to the current
      workspace (like what you are working on, projects-specific information, etc.)'
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.13.0
  - quote: 'Global memories: These are memories that are specific to the entire AnythingLLM
      instance (like your name, preferences, etc.)'
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.13.0
  - quote: Memories are injected into the system prompt of your AI assistant so it
      can use them to personalize its responses and are a welcome addition to your
      AI assistant's knowledge base.
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.13.0
  - quote: '[Learn how to enable and manage memories →](https://docs.anythingllm.com/features/memories)'
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.13.0
  - quote: <img width="1814" height="886" alt="memories-sidebar" src="https://github.com/user-attachments/assets/293dd888-8816-4359-8819-cb02bff4189f"
      />
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.13.0
  - quote: 'feat: Memories/Personalization by @shatfield4 in https://github.com/Mintplex-Labs/anything-llm/pull/5269'
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.13.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: anythingllm
  product_name: AnythingLLM
  slug: 10-memory-and-personalization-changes-in-v1-13-0
  source_release: anythingllm-2026-05-26-v1-13-0-github-328428142-e51170a3
  source_type: github_releases
  theme: memory
  title: 10 Memory and Personalization changes in v1.13.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-05-20-2-memory-and-personalization-changes-in-rust-v0-132-0|2
  Memory and Personalization changes in rust-v0.132.0]]'
- '[[Changes/GitHub Copilot CLI/2026-05-20-memory-show-displays-documentation-links-for-learning-about-and-managing-copilot|/memory
  show displays documentation links for learning about and managing Copilot Memory]]'
- '[[Changes/Gemini CLI/2026-05-22-2-memory-and-personalization-changes-in-v0-43-0|2
  Memory and Personalization changes in v0.43.0]]'
source_release: '[[Releases/AnythingLLM/anythingllm-2026-05-26-v1-13-0-github-328428142-e51170a3|anythingllm-2026-05-26-v1-13-0-github-328428142-e51170a3]]'
source_type: github_releases
theme: memory
title: 10 Memory and Personalization changes in v1.13.0
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Memory and Personalization changes in v1.13.0

**AnythingLLM** · 2026-05-26 · [[Themes/memory|Memory and Personalization]] · Digest · [Official source](https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.13.0) · from [[Releases/AnythingLLM/anythingllm-2026-05-26-v1-13-0-github-328428142-e51170a3|AnythingLLM v1.13.0 - A Hybrid AI Experience]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> AnythingLLM now supports automatic memory extraction and personalization so your AI assistant can remember what you've talked about and use that knowledge to personalize its responses.

> AnythingLLM runs a background job to extract memories from your chats and store them in a memory bank. This memory bank is then used to personalize the responses of your AI assistant - you have full control over what is remembered and how it is used

> you can even add memories manually to the memory bank if you dont want to have the model spend cycles reviewing chat history.

> There are two types of memories:

> Workspace memories: These are memories that are specific to the current workspace (like what you are working on, projects-specific information, etc.)

> Global memories: These are memories that are specific to the entire AnythingLLM instance (like your name, preferences, etc.)

> Memories are injected into the system prompt of your AI assistant so it can use them to personalize its responses and are a welcome addition to your AI assistant's knowledge base.

> [Learn how to enable and manage memories →](https://docs.anythingllm.com/features/memories)

> \<img width="1814" height="886" alt="memories-sidebar" src="https://github.com/user-attachments/assets/293dd888-8816-4359-8819-cb02bff4189f" />

> feat: Memories/Personalization by @shatfield4 in https://github.com/Mintplex-Labs/anything-llm/pull/5269

Source: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.13.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/AnythingLLM/2026-05-26-support-pulling-generated-documents-from-api-calls-by-timothycarambat-in-https-g|Support pulling generated documents from API calls]] · Files and Data
- [[Changes/AnythingLLM/2026-05-26-this-is-we-believe-a-fundamental-shift-in-how-ai-assistants-work-for-the-first-t|This is, we believe, a fundamental shift in how AI assistants work]] · Safety and Privacy
- [[Changes/AnythingLLM/2026-05-26-3-automation-and-scheduling-changes-in-v1-13-0|3 Automation and Scheduling changes in v1.13.0]] · Automation and Scheduling
- [[Changes/AnythingLLM/2026-05-26-feat-add-native-baidu-search-provider-for-agent-web-browsing-by-jimmyzhuu-in-htt|FEAT Add native Baidu Search provider for Agent web browsing]] · Search and Browsing
- [[Changes/AnythingLLM/2026-05-26-11-model-support-changes-in-v1-13-0|11 Model Support changes in v1.13.0]] · Model Support
- [[Changes/AnythingLLM/2026-05-26-10-agent-mode-changes-in-v1-13-0|10 Agent Mode changes in v1.13.0]] · Agent Mode
- [[Changes/AnythingLLM/2026-05-26-2-apps-and-integrations-changes-in-v1-13-0|2 Apps and Integrations changes in v1.13.0]] · Apps and Integrations
- [[Changes/AnythingLLM/2026-05-26-18-other-changes-in-v1-13-0|18 other changes in v1.13.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Memory and Personalization

- Earlier: 2026-05-22 · Gemini CLI · [[Changes/Gemini CLI/2026-05-22-2-memory-and-personalization-changes-in-v0-43-0|2 Memory and Personalization changes in v0.43.0]]
- Later: 2026-05-26 · Codex CLI · [[Changes/Codex CLI/2026-05-26-22915-3-of-4-tui-route-feature-and-memory-toggles-through-app-server-etraut-open|♯22915 3 of 4 tui: route feature and memory toggles through app server @etraut-openai]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20anythingllm-2026-05-26-ebc1a7&body=Card%3A%20Changes%2FAnythingLLM%2F2026-05-26-10-memory-and-personalization-changes-in-v1-13-0.md%0ACard%20ID%3A%20anythingllm-2026-05-26-ebc1a7%0ASource%3A%20https%3A%2F%2Fgithub.com%2FMintplex-Labs%2Fanything-llm%2Freleases%2Ftag%2Fv1.13.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->