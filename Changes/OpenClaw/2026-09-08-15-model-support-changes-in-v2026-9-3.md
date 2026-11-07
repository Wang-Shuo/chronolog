---
card_id: openclaw-2026-09-08-736eac
date: '2026-09-08'
description: 'OpenClaw · 2026-09-08 · Model Support: 15 changes in v2026.9.3 — On
  a Mac with an independently managed local Gateway, setup can continue into model…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1338
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: fb3a08a75e62bbd9cafad10297e6f8fa874e3aef9983aaf4975f96ccbb868c4d
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-08-736eac
  comparison: ''
  date: '2026-09-08'
  description: 'OpenClaw — v2026.9.3: 15 Model Support changes'
  evidence:
  - quote: On a Mac with an independently managed local Gateway, setup can continue
      into model configuration without waiting for a CLI installation that was deliberately
      skipped. Finishing model setup still requires a verified response, and failed
      verification now retains the useful underlying error instead of treating failed
      or timed-out output as success.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Supported provider setup leaves generated model lists to discovery while
      preserving existing saved models and explicit replacement modes. Channel choices
      also follow the selected agent's workspace, while newly installed runtimes become
      available to the first dashboard conversation.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Session creators and Gateway admins can publish a revocable link to a conversation's
      existing and future text. Anyone with that public link can read it until access
      is revoked, so review the conversation before enabling sharing. Revoking access
      cannot recall copies people have already saved. The read-only page leaves out
      tools, reasoning, files, images and executable widgets.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Verified imported conversations hide generated trust wrappers only in their
      human-facing presentation; stored history and model-facing protections remain
      intact. On narrow screens, chat text and working output align with the composer,
      while avatars avoid overlapping the conversation.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Keyword indexing can continue when optional embedding credentials or providers
      are unavailable, so a missing optional model does not make all of your notes
      disappear from search. When SQLite extensions cannot load, a batched fallback
      scan can still return vector-backed results, although that degraded path can
      be costly on larger collections.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: When the keyboard leaves little height, chat extras move into Details so
      your draft and Send controls remain accessible. Larger text can wrap in more
      settings and quick actions, and approval details gain clearer contrast. Chat
      and attachment menus, plus Model and Permissions sheets, also stay within usable
      fold-safe regions.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Models settings adds controls for individual connected accounts, while
      model selection, temporary failure recovery and prompt caching receive changes
      that keep ongoing work attached to the choices you made.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Agents settings now offers searchable model choices for building a fallback
      chain. Selected models appear as removable chips in priority order, and you
      can still add a custom model reference when it is not in the catalog. Session
      diagnostics can also show which fallback completed the answer while keeping
      your selected primary model distinct.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Provider-specific fixes preserve Gemini’s final instructions and stable
      caches, keep Anthropic tool checkpoints independent of system edits, and place
      Bedrock checkpoints against retained conversation history. Native OpenAI cache
      settings reach supported transports, while supported Anthropic-compatible routes
      receive their cache markers. These changes follow each route’s retention settings
      and capabilities.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Supported Amazon Nova models on Bedrock also gain opt-in prompt caching
      with a five-minute lifetime.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Local model setup preserves other agents’ capabilities and defaults to
      compact tool discovery. Run openclaw doctor --fix if an upgrade reports retired
      local-model setup markers.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Failed discovery now stays visible while compatible previously discovered
      models remain available across more providers, including DeepInfra, NVIDIA,
      Bedrock, Google, Copilot, Ollama, external llama-server and LM Studio. A successful
      empty response is still empty, and changing credentials or endpoints can invalidate
      earlier inventory.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Browsing models can initialize a cold catalog on demand, and source installations
      can load provider plugins that depend on import-only modules. Downloaded hosted
      catalog changes activate after a full Gateway restart. Finding a model remains
      separate from having credentials that can actually run it.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: The ChatGPT model retirements handled here leave Platform API routes unaffected.
      A model merely missing from a catalog is not treated as retired.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: ACP history limits now count UTF-8 bytes consistently, which can make previously
      undercounted Unicode history eligible for earlier eviction on a later write.
      Transcript fallback cannot reconstruct every tool or system event, and unsupported
      saved model overrides may still require resetting the session.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 15-model-support-changes-in-v2026-9-3
  source_release: openclaw-2026-09-08-v2026-9-3-dfcfef48
  source_type: openclaw_changelog
  theme: model-support
  title: 15 Model Support changes in v2026.9.3
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-09-05-17-model-support-changes-in-v2026-9-2|17 Model Support
  changes in v2026.9.2]]'
- '[[Changes/Qoder/2026-09-05-custom-byok-endpoints-personal-plan-byok-now-supports-custom-base-urls-for-any-o|Custom
  BYOK endpoints]]'
- '[[Changes/Lovable/2026-09-08-gpt-6-astra-gemini-3-8-flash-and-gemini-3-5-transcribe-for-your-app-s-ai-feature|GPT-6
  Astra, Gemini 3.8 Flash, and Gemini 3.5 Transcribe for your app''s AI features]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-08-v2026-9-3-dfcfef48|openclaw-2026-09-08-v2026-9-3-dfcfef48]]'
source_type: openclaw_changelog
theme: model-support
title: 15 Model Support changes in v2026.9.3
type: change
---

<!-- chronolog:begin region="header" -->
# 15 Model Support changes in v2026.9.3

**OpenClaw** · 2026-09-08 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.3) · from [[Releases/OpenClaw/openclaw-2026-09-08-v2026-9-3-dfcfef48|v2026.9.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> On a Mac with an independently managed local Gateway, setup can continue into model configuration without waiting for a CLI installation that was deliberately skipped. Finishing model setup still requires a verified response, and failed verification now retains the useful underlying error instead of treating failed or timed-out output as success.

> Supported provider setup leaves generated model lists to discovery while preserving existing saved models and explicit replacement modes. Channel choices also follow the selected agent's workspace, while newly installed runtimes become available to the first dashboard conversation.

> Session creators and Gateway admins can publish a revocable link to a conversation's existing and future text. Anyone with that public link can read it until access is revoked, so review the conversation before enabling sharing. Revoking access cannot recall copies people have already saved. The read-only page leaves out tools, reasoning, files, images and executable widgets.

> Verified imported conversations hide generated trust wrappers only in their human-facing presentation; stored history and model-facing protections remain intact. On narrow screens, chat text and working output align with the composer, while avatars avoid overlapping the conversation.

> Keyword indexing can continue when optional embedding credentials or providers are unavailable, so a missing optional model does not make all of your notes disappear from search. When SQLite extensions cannot load, a batched fallback scan can still return vector-backed results, although that degraded path can be costly on larger collections.

> When the keyboard leaves little height, chat extras move into Details so your draft and Send controls remain accessible. Larger text can wrap in more settings and quick actions, and approval details gain clearer contrast. Chat and attachment menus, plus Model and Permissions sheets, also stay within usable fold-safe regions.

> Models settings adds controls for individual connected accounts, while model selection, temporary failure recovery and prompt caching receive changes that keep ongoing work attached to the choices you made.

> Agents settings now offers searchable model choices for building a fallback chain. Selected models appear as removable chips in priority order, and you can still add a custom model reference when it is not in the catalog. Session diagnostics can also show which fallback completed the answer while keeping your selected primary model distinct.

> Provider-specific fixes preserve Gemini’s final instructions and stable caches, keep Anthropic tool checkpoints independent of system edits, and place Bedrock checkpoints against retained conversation history. Native OpenAI cache settings reach supported transports, while supported Anthropic-compatible routes receive their cache markers. These changes follow each route’s retention settings and capabilities.

> Supported Amazon Nova models on Bedrock also gain opt-in prompt caching with a five-minute lifetime.

> Local model setup preserves other agents’ capabilities and defaults to compact tool discovery. Run openclaw doctor --fix if an upgrade reports retired local-model setup markers.

> Failed discovery now stays visible while compatible previously discovered models remain available across more providers, including DeepInfra, NVIDIA, Bedrock, Google, Copilot, Ollama, external llama-server and LM Studio. A successful empty response is still empty, and changing credentials or endpoints can invalidate earlier inventory.

> Browsing models can initialize a cold catalog on demand, and source installations can load provider plugins that depend on import-only modules. Downloaded hosted catalog changes activate after a full Gateway restart. Finding a model remains separate from having credentials that can actually run it.

> The ChatGPT model retirements handled here leave Platform API routes unaffected. A model merely missing from a catalog is not treated as retired.

> ACP history limits now count UTF-8 bytes consistently, which can make previously undercounted Unicode history eligible for earlier eviction on a later write. Transcript fallback cannot reconstruct every tool or system event, and unsupported saved model overrides may still require resetting the session.

Source: https://docs.openclaw.ai/releases/2026.9.3
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-08-7-automation-and-scheduling-changes-in-v2026-9-3|7 Automation and Scheduling changes in v2026.9.3]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-08-10-memory-and-personalization-changes-in-v2026-9-3|10 Memory and Personalization changes in v2026.9.3]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-08-2-files-and-data-changes-in-v2026-9-3|2 Files and Data changes in v2026.9.3]] · Files and Data
- [[Changes/OpenClaw/2026-09-08-12-context-window-changes-in-v2026-9-3|12 Context Window changes in v2026.9.3]] · Context Window
- [[Changes/OpenClaw/2026-09-08-23-apps-and-integrations-changes-in-v2026-9-3|23 Apps and Integrations changes in v2026.9.3]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-08-ordinary-model-changes-now-apply-to-the-current-chat-by-default-including-admini|Ordinary model changes now apply to the current chat by default, including…]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-08-10-mobile-and-desktop-changes-in-v2026-9-3|10 Mobile and Desktop changes in v2026.9.3]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-08-4-reliability-and-performance-changes-in-v2026-9-3|4 Reliability and Performance changes in v2026.9.3]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-08-provider-adapters-preserve-initial-anthropic-text-and-thinking-keep-images-with|Provider adapters preserve initial Anthropic text and thinking, keep images…]] · Multimodal Input
- [[Changes/OpenClaw/2026-09-08-8-editor-experience-changes-in-v2026-9-3|8 Editor Experience changes in v2026.9.3]] · Editor Experience
- [[Changes/OpenClaw/2026-09-08-8-voice-and-audio-changes-in-v2026-9-3|8 Voice and Audio changes in v2026.9.3]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-08-3-search-and-browsing-changes-in-v2026-9-3|3 Search and Browsing changes in v2026.9.3]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-08-16-agent-mode-changes-in-v2026-9-3|16 Agent Mode changes in v2026.9.3]] · Agent Mode
- [[Changes/OpenClaw/2026-09-08-11-interface-experience-changes-in-v2026-9-3|11 Interface Experience changes in v2026.9.3]] · Interface Experience
- [[Changes/OpenClaw/2026-09-08-slack-delivers-valid-structured-sections-intact-even-when-their-accessibility-te|Slack delivers valid structured sections intact even when their accessibility text…]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-09-08-4-collaboration-changes-in-v2026-9-3|4 Collaboration changes in v2026.9.3]] · Collaboration
- [[Changes/OpenClaw/2026-09-08-14-safety-and-privacy-changes-in-v2026-9-3|14 Safety and Privacy changes in v2026.9.3]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-08-4-pricing-model-changes-in-v2026-9-3|4 Pricing Model changes in v2026.9.3]] · Pricing Model
- [[Changes/OpenClaw/2026-09-08-8-account-and-access-changes-in-v2026-9-3|8 Account and Access changes in v2026.9.3]] · Account and Access
- [[Changes/OpenClaw/2026-09-08-22-developer-workflow-changes-in-v2026-9-3|22 Developer Workflow changes in v2026.9.3]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-08-77-other-changes-in-v2026-9-3|77 other changes in v2026.9.3]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-09-08 · Lovable · [[Changes/Lovable/2026-09-08-gpt-6-astra-gemini-3-8-flash-and-gemini-3-5-transcribe-for-your-app-s-ai-feature|GPT-6 Astra, Gemini 3.8 Flash, and Gemini 3.5 Transcribe for your app's AI features]]
- Later: 2026-09-09 · ChatGPT · [[Changes/ChatGPT/2026-09-09-chatgpt-voice-can-now-use-gpt-5-6-or-gpt-6-astra-when-it-needs-to-search-or-reas-848954|ChatGPT Voice can now use GPT-5.6 or GPT-6 Astra when it needs to search or reason…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-08-736eac&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-08-15-model-support-changes-in-v2026-9-3.md%0ACard%20ID%3A%20openclaw-2026-09-08-736eac%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.3%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->