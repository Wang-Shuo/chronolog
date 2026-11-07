---
card_id: openclaw-2026-09-23-ef18bb
date: '2026-09-23'
description: 'OpenClaw · 2026-09-23 · Model Support: 22 changes in v2026.9.6 — Activity
  recaps and people lists avoid preparing information they do not need, reducing…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1353
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 3ab259943befcd58260681eaab2981fb7a2632db284b418a7376c8863f0395f0
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-23-ef18bb
  comparison: ''
  date: '2026-09-23'
  description: 'OpenClaw — v2026.9.6: 22 Model Support changes'
  evidence:
  - quote: Activity recaps and people lists avoid preparing information they do not
      need, reducing repeated work during refreshes. Session assessments and recaps
      also recover when an implicit model choice selects unavailable Codex, while
      an explicitly chosen unavailable Codex route still reports failure. These utility
      requests remain tool-free.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Twenty existing interface languages receive updated wording for setup,
      chat status, recovery, themes, usage, models and desktop guidance. These updates
      bring more current controls and explanations into those languages without introducing
      new language choices or changing the behavior of the features they describe.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Repeated --media flags in the message CLI now preserve every attachment
      in command-line order, using each channel's existing sending behavior. Animated
      WebP files keep their animation within the existing size and model limits, with
      oversized animations rejected instead of flattened. Attachments also survive
      when a caption is stripped, without bringing the removed text back into chat.
      Older tool calls without a recorded publication no longer reconstruct a reply
      bubble, but their expanded diagnostics remain available.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: TypeSafe Jev and local Decision Models give supporting plugins a way to
      make structured choices separately from chat. Claude Opus 5.5, GPT-6 Sol and
      Luna, and Grok 4.7 add new conversation choices, with their own account requirements,
      settings, and costs.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Claude Opus 5.5 is now selectable in the Anthropic API and Claude CLI catalogs
      as anthropic/claude-opus-5-5 , with explicit opus-5.5 and opus-5-5 aliases.
      Existing selections stay unchanged, and the bare opus alias still chooses Opus
      5. Thinking is always enabled, defaults to medium, and offers low through max;
      saved off or minimal settings use low instead. API use carries Opus 5.5-specific
      charges, and availability still depends on the selected account and route.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Direct Anthropic OAuth requests now advertise a maintained Claude client
      version to address newer models rejecting an outdated client identity. OpenClaw
      uses at least version 2.1.278 or a newer installed stable Claude CLI, with the
      result cached until restart. This updates request compatibility while leaving
      account entitlement, billing policy, and local model restrictions unchanged.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Xiaomi MiMo V2.6 adds Pro, Flash, and Pro UltraSpeed for pay-as-you-go
      accounts, with Pro and Flash presets for regional Token Plans. New setups default
      to Pro when no primary model is selected, while existing selections remain.
      The new models support text and images, thinking controls, and retained reasoning
      history; Pro and Flash also prefer automatic Code Mode unless explicitly overridden.
      Token Plan zero-dollar catalog prices represent quota accounting, not free service.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Evaluations can allow up to thirty seconds, with shorter deadlines still
      respected. Large cold models may need preloading or a smaller model. Invalid
      replacement preparation leaves an already-loaded model available, though failure
      while creating the replacement's native session can still evict it.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Default merge-mode catalogs now show eligible newly discovered models alongside
      older saved provider rows. To restrict the available choices, use an explicit
      modelPolicy.allow policy or models.mode=replace ; a saved provider array alone
      no longer limits discovery.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: OpenClaw avoids more repeated storage reads, process starts, filesystem
      checks, and copying while preparing model credentials, allowing other Gateway
      work to progress during asynchronous reads. Reuse is invalidated when relevant
      credentials or ownership change. Credentials changed by another process can
      take up to 100 milliseconds to become visible through the cached path, while
      changes made within the running process invalidate it immediately.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Retiring catalog workers now wait for already-started OAuth refreshes to
      save replacement credentials, while failed Gemini credential replacement removes
      its staged file and retains the previous credentials for retry. Already-stranded
      logins may still need a fresh sign-in.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Conversations and scheduled work can reach configured alternatives sooner
      when a provider asks for a rate-limit wait longer than the saved retry cap .
      This requires a configured model fallback, a positive cap, and a request that
      can be replayed safely; zero disables the cap. Switching accounts or models
      sooner can change costs and answers. Long tasks also regain their transient-outage
      recovery window after a completed successful model response, while overall retry
      and run limits remain in force. Conversation compaction now keeps the current
      healthy account, including a selected fallback, in both explicitly ordered and
      implicit account pools; actual failures and preferred-account recovery can still
      change it.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Opt-in diagnostic timelines show model activity and explain existing recovery
      decisions. OpenAI misalignment errors are also identified as provider refusals
      instead of malformed requests; the separate findings-review flow below governs
      whether a supported conversation can continue.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Gemini tool requests no longer include the internal optional-field metadata
      that could cause rejection. Plugin authors also get deeper finite-schema support
      in the Gemini normalizer and unsupported-keyword cleaner, avoiding recursive
      stack overflow in those two paths while still rejecting circular objects.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Claude Code, Codex CLI, and Gemini CLI now honor explicit search-provider
      and disabled-search settings. Eligible native OpenAI search also keeps its selected
      route through Tool Search and Code Mode. Choosing a managed provider suppresses
      native fallback even when that provider's connection fails, so a failed connection
      does not silently change your search choice.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Managed local model servers retain shutdown ownership and wait for child
      output and termination to settle before a replacement starts. Incomplete shutdown
      remains visible as an error that later requests can recheck, and Windows cleanup
      avoids signaling a different process that has reused the old process ID. Existing
      stop budgets and platform limits still apply.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Long available Codex tool responses now remain saved after a reload, with
      Show full output , Copy, and Download providing inspection and export of the
      original captured text. Recognized native Code Mode results also get readable
      command and text displays with expandable source and Raw details, while unknown
      or incomplete results keep their original representation and failed exit statuses
      stay visible. The output guide explains the distinction between execution output
      and provider responses. Older discarded text cannot be recovered, and redaction,
      provider truncation, and transport limits still apply, including a requested
      maximum of two million characters per text field. Neither view proves exactly
      what Codex later sends to its model.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: When an A2A task switches models, its completed result now contains the
      fallback model’s actual answer. The task no longer finishes early with only
      the notice that a different model will be used.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Code Mode now activates automatically for catalog-preferred models when
      the global setting is absent, including after an upgrade. Explicit false , an
      empty global object, or a global object containing only options stays off unless
      an agent or model override enables it. Haiku 4.5 remains available through explicit
      activation but is excluded from automatic selection, and native Codex Code Mode
      is unchanged.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Secrets audits now reject symlinked generated models.json files and keep
      malformed file contents out of error messages. These checks are read-only and
      limited to 5 MiB per generated model file; ordinary hardlinks and parent-directory
      aliases remain supported.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: The default gateway-only managed proxy mode now keeps localhost and literal
      loopback connections direct, fixing WebChat and Codex failures when their local
      model relay was sent through an external proxy. External destinations and non-loopback
      private, LAN, and tailnet traffic still use the proxy, while explicit proxy
      and block modes and application network-access checks retain their restrictions.
      Doctor now explains failed local connectivity; restrictive configurations may
      need gateway-only restored and a Gateway restart.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: The temporary extension of tool and model duration histograms was reverted,
      leaving the existing finite buckets ending at ten seconds. Anyone who deployed
      the brief main-branch extension should compare common bucket boundaries or keep
      observations separate across the rollback. The source list also retains credit
      for a codec-import repair whose merge added no further changes.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 22-model-support-changes-in-v2026-9-6
  source_release: openclaw-2026-09-23-v2026-9-6-3f12c824
  source_type: openclaw_changelog
  theme: model-support
  title: 22 Model Support changes in v2026.9.6
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-09-23-image-video|Image & Video]]'
- '[[Changes/Lovable/2026-09-23-claude-models-for-your-app-s-ai-features|Claude models
  for your app''s AI features]]'
- '[[Changes/Lovable/2026-09-23-enable-extended-retention-models-in-your-enterprise-workspace|Enable
  extended-retention models in your Enterprise workspace]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-23-v2026-9-6-3f12c824|openclaw-2026-09-23-v2026-9-6-3f12c824]]'
source_type: openclaw_changelog
theme: model-support
title: 22 Model Support changes in v2026.9.6
type: change
---

<!-- chronolog:begin region="header" -->
# 22 Model Support changes in v2026.9.6

**OpenClaw** · 2026-09-23 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.6) · from [[Releases/OpenClaw/openclaw-2026-09-23-v2026-9-6-3f12c824|v2026.9.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Activity recaps and people lists avoid preparing information they do not need, reducing repeated work during refreshes. Session assessments and recaps also recover when an implicit model choice selects unavailable Codex, while an explicitly chosen unavailable Codex route still reports failure. These utility requests remain tool-free.

> Twenty existing interface languages receive updated wording for setup, chat status, recovery, themes, usage, models and desktop guidance. These updates bring more current controls and explanations into those languages without introducing new language choices or changing the behavior of the features they describe.

> Repeated --media flags in the message CLI now preserve every attachment in command-line order, using each channel's existing sending behavior. Animated WebP files keep their animation within the existing size and model limits, with oversized animations rejected instead of flattened. Attachments also survive when a caption is stripped, without bringing the removed text back into chat. Older tool calls without a recorded publication no longer reconstruct a reply bubble, but their expanded diagnostics remain available.

> TypeSafe Jev and local Decision Models give supporting plugins a way to make structured choices separately from chat. Claude Opus 5.5, GPT-6 Sol and Luna, and Grok 4.7 add new conversation choices, with their own account requirements, settings, and costs.

> Claude Opus 5.5 is now selectable in the Anthropic API and Claude CLI catalogs as anthropic/claude-opus-5-5 , with explicit opus-5.5 and opus-5-5 aliases. Existing selections stay unchanged, and the bare opus alias still chooses Opus 5. Thinking is always enabled, defaults to medium, and offers low through max; saved off or minimal settings use low instead. API use carries Opus 5.5-specific charges, and availability still depends on the selected account and route.

> Direct Anthropic OAuth requests now advertise a maintained Claude client version to address newer models rejecting an outdated client identity. OpenClaw uses at least version 2.1.278 or a newer installed stable Claude CLI, with the result cached until restart. This updates request compatibility while leaving account entitlement, billing policy, and local model restrictions unchanged.

> Xiaomi MiMo V2.6 adds Pro, Flash, and Pro UltraSpeed for pay-as-you-go accounts, with Pro and Flash presets for regional Token Plans. New setups default to Pro when no primary model is selected, while existing selections remain. The new models support text and images, thinking controls, and retained reasoning history; Pro and Flash also prefer automatic Code Mode unless explicitly overridden. Token Plan zero-dollar catalog prices represent quota accounting, not free service.

> Evaluations can allow up to thirty seconds, with shorter deadlines still respected. Large cold models may need preloading or a smaller model. Invalid replacement preparation leaves an already-loaded model available, though failure while creating the replacement's native session can still evict it.

> Default merge-mode catalogs now show eligible newly discovered models alongside older saved provider rows. To restrict the available choices, use an explicit modelPolicy.allow policy or models.mode=replace ; a saved provider array alone no longer limits discovery.

> OpenClaw avoids more repeated storage reads, process starts, filesystem checks, and copying while preparing model credentials, allowing other Gateway work to progress during asynchronous reads. Reuse is invalidated when relevant credentials or ownership change. Credentials changed by another process can take up to 100 milliseconds to become visible through the cached path, while changes made within the running process invalidate it immediately.

> Retiring catalog workers now wait for already-started OAuth refreshes to save replacement credentials, while failed Gemini credential replacement removes its staged file and retains the previous credentials for retry. Already-stranded logins may still need a fresh sign-in.

> Conversations and scheduled work can reach configured alternatives sooner when a provider asks for a rate-limit wait longer than the saved retry cap . This requires a configured model fallback, a positive cap, and a request that can be replayed safely; zero disables the cap. Switching accounts or models sooner can change costs and answers. Long tasks also regain their transient-outage recovery window after a completed successful model response, while overall retry and run limits remain in force. Conversation compaction now keeps the current healthy account, including a selected fallback, in both explicitly ordered and implicit account pools; actual failures and preferred-account recovery can still change it.

> Opt-in diagnostic timelines show model activity and explain existing recovery decisions. OpenAI misalignment errors are also identified as provider refusals instead of malformed requests; the separate findings-review flow below governs whether a supported conversation can continue.

> Gemini tool requests no longer include the internal optional-field metadata that could cause rejection. Plugin authors also get deeper finite-schema support in the Gemini normalizer and unsupported-keyword cleaner, avoiding recursive stack overflow in those two paths while still rejecting circular objects.

> Claude Code, Codex CLI, and Gemini CLI now honor explicit search-provider and disabled-search settings. Eligible native OpenAI search also keeps its selected route through Tool Search and Code Mode. Choosing a managed provider suppresses native fallback even when that provider's connection fails, so a failed connection does not silently change your search choice.

> Managed local model servers retain shutdown ownership and wait for child output and termination to settle before a replacement starts. Incomplete shutdown remains visible as an error that later requests can recheck, and Windows cleanup avoids signaling a different process that has reused the old process ID. Existing stop budgets and platform limits still apply.

> Long available Codex tool responses now remain saved after a reload, with Show full output , Copy, and Download providing inspection and export of the original captured text. Recognized native Code Mode results also get readable command and text displays with expandable source and Raw details, while unknown or incomplete results keep their original representation and failed exit statuses stay visible. The output guide explains the distinction between execution output and provider responses. Older discarded text cannot be recovered, and redaction, provider truncation, and transport limits still apply, including a requested maximum of two million characters per text field. Neither view proves exactly what Codex later sends to its model.

> When an A2A task switches models, its completed result now contains the fallback model’s actual answer. The task no longer finishes early with only the notice that a different model will be used.

> Code Mode now activates automatically for catalog-preferred models when the global setting is absent, including after an upgrade. Explicit false , an empty global object, or a global object containing only options stays off unless an agent or model override enables it. Haiku 4.5 remains available through explicit activation but is excluded from automatic selection, and native Codex Code Mode is unchanged.

> Secrets audits now reject symlinked generated models.json files and keep malformed file contents out of error messages. These checks are read-only and limited to 5 MiB per generated model file; ordinary hardlinks and parent-directory aliases remain supported.

> The default gateway-only managed proxy mode now keeps localhost and literal loopback connections direct, fixing WebChat and Codex failures when their local model relay was sent through an external proxy. External destinations and non-loopback private, LAN, and tailnet traffic still use the proxy, while explicit proxy and block modes and application network-access checks retain their restrictions. Doctor now explains failed local connectivity; restrictive configurations may need gateway-only restored and a Gateway restart.

> The temporary extension of tool and model duration histograms was reverted, leaving the existing finite buckets ending at ten seconds. Anyone who deployed the brief main-branch extension should compare common bucket boundaries or keep observations separate across the rollback. The source list also retains credit for a codec-import repair whose merge added no further changes.

Source: https://docs.openclaw.ai/releases/2026.9.6
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-23-50-safety-and-privacy-changes-in-v2026-9-6|50 Safety and Privacy changes in v2026.9.6]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-23-localization-maintenance-removes-entries-whose-interface-text-has-already-been-r|Localization maintenance removes entries whose interface text has already been…]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-09-23-5-reliability-and-performance-changes-in-v2026-9-6|5 Reliability and Performance changes in v2026.9.6]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-23-2-image-generation-changes-in-v2026-9-6|2 Image Generation changes in v2026.9.6]] · Image Generation
- [[Changes/OpenClaw/2026-09-23-18-voice-and-audio-changes-in-v2026-9-6|18 Voice and Audio changes in v2026.9.6]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-23-25-context-window-changes-in-v2026-9-6|25 Context Window changes in v2026.9.6]] · Context Window
- [[Changes/OpenClaw/2026-09-23-16-mobile-and-desktop-changes-in-v2026-9-6|16 Mobile and Desktop changes in v2026.9.6]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-23-41-agent-mode-changes-in-v2026-9-6|41 Agent Mode changes in v2026.9.6]] · Agent Mode
- [[Changes/OpenClaw/2026-09-23-16-collaboration-changes-in-v2026-9-6|16 Collaboration changes in v2026.9.6]] · Collaboration
- [[Changes/OpenClaw/2026-09-23-15-editor-experience-changes-in-v2026-9-6|15 Editor Experience changes in v2026.9.6]] · Editor Experience
- [[Changes/OpenClaw/2026-09-23-2-enterprise-and-administration-changes-in-v2026-9-6|2 Enterprise and Administration changes in v2026.9.6]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-23-31-developer-workflow-changes-in-v2026-9-6|31 Developer Workflow changes in v2026.9.6]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-23-8-pricing-model-changes-in-v2026-9-6|8 Pricing Model changes in v2026.9.6]] · Pricing Model
- [[Changes/OpenClaw/2026-09-23-plugin-requested-answer-revisions-wait-for-session-history-to-become-available-a|Plugin-requested answer revisions wait for session history to become available…]] · Projects and Workspaces
- [[Changes/OpenClaw/2026-09-23-6-files-and-data-changes-in-v2026-9-6|6 Files and Data changes in v2026.9.6]] · Files and Data
- [[Changes/OpenClaw/2026-09-23-58-apps-and-integrations-changes-in-v2026-9-6|58 Apps and Integrations changes in v2026.9.6]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-23-17-account-and-access-changes-in-v2026-9-6|17 Account and Access changes in v2026.9.6]] · Account and Access
- [[Changes/OpenClaw/2026-09-23-background-image-video-and-music-generation-can-complete-independently-of-the-re|Background image, video, and music generation can complete independently…]] · Music Generation
- [[Changes/OpenClaw/2026-09-23-23-memory-and-personalization-changes-in-v2026-9-6|23 Memory and Personalization changes in v2026.9.6]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-23-3-search-and-browsing-changes-in-v2026-9-6|3 Search and Browsing changes in v2026.9.6]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-23-19-interface-experience-changes-in-v2026-9-6|19 Interface Experience changes in v2026.9.6]] · Interface Experience
- [[Changes/OpenClaw/2026-09-23-9-automation-and-scheduling-changes-in-v2026-9-6|9 Automation and Scheduling changes in v2026.9.6]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-23-119-other-changes-in-v2026-9-6|119 other changes in v2026.9.6]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-09-23 · Lovable · [[Changes/Lovable/2026-09-23-enable-extended-retention-models-in-your-enterprise-workspace|Enable extended-retention models in your Enterprise workspace]]
- Later: 2026-09-24 · Claude Code · [[Changes/Claude Code/2026-09-24-2-model-support-changes-in-v2-1-282|2 Model Support changes in v2.1.282]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-23-ef18bb&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-23-22-model-support-changes-in-v2026-9-6.md%0ACard%20ID%3A%20openclaw-2026-09-23-ef18bb%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.6%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->