---
card_id: dify-2026-11-04-9a8559
date: '2026-11-04'
description: 'Dify · 2026-11-04 · Apps and Integrations: 15 changes in v1.19.0 - Trace
  Your Workflows, Layer by Layer — All Dify app exports now use **package format v2**…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1322
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 1652195e17d18bb60ec7cdaaccec96b5ebf6ea3d26cfc7e3ef3aa6ec2c2c99e2
product: dify
product_name: Dify
record:
  card_id: dify-2026-11-04-9a8559
  comparison: ''
  date: '2026-11-04'
  description: 'Dify — v1.19.0 - Trace Your Workflows, Layer by Layer: 15 Apps and
    Integrations changes'
  evidence:
  - quote: All Dify app exports now use **package format v2**, including apps without
      Workflow Tools. Existing v1 imports and explicit YAML export remain supported.
      See the [upgrade guide](#user-content-upgrade-guide) before importing new packages
      into older installations. (#45353)
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  - quote: '> **Read the upgrade guide before deploying.** Docker Compose now requires
      **v2.35.0 or later**. Preserve existing environment files, upgrade the Dify
      components together, and use the new tracing queue during rolling deployments.
      New App packages use format v2 and require a compatible destination importer.
      The bundled plugin daemon moves to **0.6.14-local**.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  - quote: Configure shared plugin credentials, `PLUGIN_DAEMON_KEY` and `PLUGIN_DIFY_INNER_API_KEY`,
      in root `docker/.env` so the daemon and its clients receive matching values.
      Ports, volume paths, profiles, and health-check scheduling also remain root
      configuration inputs. See the [Docker configuration guide](https://github.com/langgenius/dify/blob/laipz8200/release-1.19.0/docker/README.md#configure-dify).
      (#45359)
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  - quote: '**Tracing and provider integrations**'
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  - quote: Workflow and API tool IDs no longer become spurious `langgenius/<uuid>`
      plugin dependencies during export. (#44592)
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  - quote: '**Safer editing dialogs:** deletion, rename, metadata, annotation, member-role,
      and plugin-setting dialogs preserve their sessions and drafts, keep pending
      actions open, and restore focus after completion. Repeated deletion submissions
      are blocked while a request is pending. (#44618, #44623, #44643, #44646, #44698,
      #44736, #44743, #44810, #44825, #44788, #44715, #44652, #44838, #44830)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  - quote: 'Honor configured file and file-list defaults across Studio, published
      apps, and API execution. Explicit clearing stays distinct from omission, reset
      conversations restore defaults, and saving file defaults no longer sends browser
      Blob objects that cause `415` errors. (#44780, #45042)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  - quote: 'Reject late non-terminal events after an Agent stream has completed or
      been cancelled. Deduplicate plugin JSON output by content rather than formatting,
      and retain trailing partial action/thought prefixes in ReAct output. (#45080,
      #45297, #43353)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  - quote: 'Restore creator-based Agent edit permissions. Skill and snippet searches
      treat wildcard characters literally, and imported integration bundles retain
      their plugin icons. (#45040, #44922, #44708, #45112)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  - quote: 'Let MCP Chatflow generation commit its conversation session without a
      closed-transaction error. API-tool imports ignore non-method Swagger path keys.
      Suggested-question parsing retains brackets inside quoted questions, and missing
      citation resources return an empty list. (#44636, #44992, #44916, #43036)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  - quote: 'The Node.js SDK accepts long knowledge-document text, handles CR/LF/CRLF
      SSE framing and a leading BOM, and accepts an empty pagination cursor as the
      first page. (#44679, #44263, #44265)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  - quote: 'Use navigable links in document menus, open publisher destinations in
      new tabs, and advance integration-tour steps without reloading the page. (#44694,
      #44808, #44934, #44944)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  - quote: 'Respect Marketplace availability across template and plugin entry points
      and render emoji-ID icons in recommended cards. (#45009, #45027, #45066)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  - quote: <summary><strong>Environment variables and integration changes</strong></summary>
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  - quote: Custom clients of **`GET /console/api/apps/{app_id}/trace-config`** must
      consume `configured_secrets` instead of expecting saved secret values. (#44673)
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 15-apps-and-integrations-changes-in-1-19-0
  source_release: dify-2026-11-04-1-19-0-github-433629888-738006ec
  source_type: github_releases
  theme: apps-integrations
  title: 15 Apps and Integrations changes in 1.19.0
  type: change
related_changes:
- '[[Changes/Lovable/2026-11-02-connect-your-app-to-bamboohr|Connect your app to BambooHR]]'
- "[[Changes/Open WebUI/2026-11-03-mcp-apps-in-chat-tools-from-mcp-servers-that-come-with-an-interactive-app-now-sh|\U0001F9E9
  MCP Apps in chat. Tools from MCP servers that come with an interactive app now…]]"
- '[[Changes/OpenHands/2026-11-03-3-apps-and-integrations-changes-in-v1-35-0|3 Apps
  and Integrations changes in v1.35.0]]'
source_release: '[[Releases/Dify/dify-2026-11-04-1-19-0-github-433629888-738006ec|dify-2026-11-04-1-19-0-github-433629888-738006ec]]'
source_type: github_releases
theme: apps-integrations
title: 15 Apps and Integrations changes in 1.19.0
type: change
---

<!-- chronolog:begin region="header" -->
# 15 Apps and Integrations changes in 1.19.0

**Dify** · 2026-11-04 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.19.0) · from [[Releases/Dify/dify-2026-11-04-1-19-0-github-433629888-738006ec|v1.19.0 - Trace Your Workflows, Layer by Layer]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> All Dify app exports now use **package format v2**, including apps without Workflow Tools. Existing v1 imports and explicit YAML export remain supported. See the [upgrade guide](#user-content-upgrade-guide) before importing new packages into older installations. (#45353)

> > **Read the upgrade guide before deploying.** Docker Compose now requires **v2.35.0 or later**. Preserve existing environment files, upgrade the Dify components together, and use the new tracing queue during rolling deployments. New App packages use format v2 and require a compatible destination importer. The bundled plugin daemon moves to **0.6.14-local**.

> Configure shared plugin credentials, `PLUGIN_DAEMON_KEY` and `PLUGIN_DIFY_INNER_API_KEY`, in root `docker/.env` so the daemon and its clients receive matching values. Ports, volume paths, profiles, and health-check scheduling also remain root configuration inputs. See the [Docker configuration guide](https://github.com/langgenius/dify/blob/laipz8200/release-1.19.0/docker/README.md#configure-dify). (#45359)

> **Tracing and provider integrations**

> Workflow and API tool IDs no longer become spurious `langgenius/<uuid>` plugin dependencies during export. (#44592)

> **Safer editing dialogs:** deletion, rename, metadata, annotation, member-role, and plugin-setting dialogs preserve their sessions and drafts, keep pending actions open, and restore focus after completion. Repeated deletion submissions are blocked while a request is pending. (#44618, #44623, #44643, #44646, #44698, #44736, #44743, #44810, #44825, #44788, #44715, #44652, #44838, #44830)

> Honor configured file and file-list defaults across Studio, published apps, and API execution. Explicit clearing stays distinct from omission, reset conversations restore defaults, and saving file defaults no longer sends browser Blob objects that cause `415` errors. (#44780, #45042)

> Reject late non-terminal events after an Agent stream has completed or been cancelled. Deduplicate plugin JSON output by content rather than formatting, and retain trailing partial action/thought prefixes in ReAct output. (#45080, #45297, #43353)

> Restore creator-based Agent edit permissions. Skill and snippet searches treat wildcard characters literally, and imported integration bundles retain their plugin icons. (#45040, #44922, #44708, #45112)

> Let MCP Chatflow generation commit its conversation session without a closed-transaction error. API-tool imports ignore non-method Swagger path keys. Suggested-question parsing retains brackets inside quoted questions, and missing citation resources return an empty list. (#44636, #44992, #44916, #43036)

> The Node.js SDK accepts long knowledge-document text, handles CR/LF/CRLF SSE framing and a leading BOM, and accepts an empty pagination cursor as the first page. (#44679, #44263, #44265)

> Use navigable links in document menus, open publisher destinations in new tabs, and advance integration-tour steps without reloading the page. (#44694, #44808, #44934, #44944)

> Respect Marketplace availability across template and plugin entry points and render emoji-ID icons in recommended cards. (#45009, #45027, #45066)

> \<summary>\<strong>Environment variables and integration changes\</strong>\</summary>

> Custom clients of **`GET /console/api/apps/{app_id}/trace-config`** must consume `configured_secrets` instead of expecting saved secret values. (#44673)

Source: https://github.com/langgenius/dify/releases/tag/1.19.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-11-04-4-model-support-changes-in-1-19-0|4 Model Support changes in 1.19.0]] · Model Support
- [[Changes/Dify/2026-11-04-stop-serializing-the-entire-prompt-history-into-every-agent-llm-gateway-response|Stop serializing the entire prompt history into every Agent LLM gateway response chunk]] · Multimodal Input
- [[Changes/Dify/2026-11-04-4-collaboration-changes-in-1-19-0|4 Collaboration changes in 1.19.0]] · Collaboration
- [[Changes/Dify/2026-11-04-3-automation-and-scheduling-changes-in-1-19-0|3 Automation and Scheduling changes in 1.19.0]] · Automation and Scheduling
- [[Changes/Dify/2026-11-04-2-developer-workflow-changes-in-1-19-0|2 Developer Workflow changes in 1.19.0]] · Developer Workflow
- [[Changes/Dify/2026-11-04-6-files-and-data-changes-in-1-19-0|6 Files and Data changes in 1.19.0]] · Files and Data
- [[Changes/Dify/2026-11-04-3-pricing-model-changes-in-1-19-0|3 Pricing Model changes in 1.19.0]] · Pricing Model
- [[Changes/Dify/2026-11-04-3-editor-experience-changes-in-1-19-0|3 Editor Experience changes in 1.19.0]] · Editor Experience
- [[Changes/Dify/2026-11-04-2-voice-and-audio-changes-in-1-19-0|2 Voice and Audio changes in 1.19.0]] · Voice and Audio
- [[Changes/Dify/2026-11-04-4-safety-and-privacy-changes-in-1-19-0|4 Safety and Privacy changes in 1.19.0]] · Safety and Privacy
- [[Changes/Dify/2026-11-04-workspace-controls-enabling-or-disabling-provider-models-requires-an-owner-or-ad|Workspace controls: enabling or disabling provider models requires an owner…]] · Enterprise and Administration
- [[Changes/Dify/2026-11-04-summary-strong-improvements-editing-accessibility-performance-and-operations-str|summarystrongImprovements · editing, accessibility, performance…]] · Accessibility and Localization
- [[Changes/Dify/2026-11-04-2-interface-experience-changes-in-1-19-0|2 Interface Experience changes in 1.19.0]] · Interface Experience
- [[Changes/Dify/2026-11-04-6-context-window-changes-in-1-19-0|6 Context Window changes in 1.19.0]] · Context Window
- [[Changes/Dify/2026-11-04-14-agent-mode-changes-in-1-19-0|14 Agent Mode changes in 1.19.0]] · Agent Mode
- [[Changes/Dify/2026-11-04-2-account-and-access-changes-in-1-19-0|2 Account and Access changes in 1.19.0]] · Account and Access
- [[Changes/Dify/2026-11-04-66-other-changes-in-1-19-0|66 other changes in 1.19.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-11-03 · OpenHands · [[Changes/OpenHands/2026-11-03-3-apps-and-integrations-changes-in-v1-35-0|3 Apps and Integrations changes in v1.35.0]]
- Later: 2026-11-05 · OpenHands · [[Changes/OpenHands/2026-11-05-3-apps-and-integrations-changes-in-v1-36-0|3 Apps and Integrations changes in v1.36.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-11-04-9a8559&body=Card%3A%20Changes%2FDify%2F2026-11-04-15-apps-and-integrations-changes-in-1-19-0.md%0ACard%20ID%3A%20dify-2026-11-04-9a8559%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.19.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->