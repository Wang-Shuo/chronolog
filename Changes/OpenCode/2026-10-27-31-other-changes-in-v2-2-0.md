---
card_id: opencode-2026-10-27-c619d1
date: '2026-10-27'
description: 'OpenCode · 2026-10-27 · Other changes: 31 changes in v2.2.0 — Core Add
  an experimental API for session media and opt-in media URI support.'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 0c249a523f1e3bdb4f1686500f34604ea2e09fd417abb75a23abbd088184340c
product: opencode
product_name: OpenCode
record:
  card_id: opencode-2026-10-27-c619d1
  comparison: ''
  date: '2026-10-27'
  description: 'OpenCode — v2.2.0: 31 other changes'
  evidence:
  - quote: Core Add an experimental API for session media and opt-in media URI support.
    source_release: https://opencode.ai/changelog/v2.2.0
  - quote: Core Add the machine hostname to /api/info .
    source_release: https://opencode.ai/changelog/v2.2.0
  - quote: Core Add experimental content-addressed blob storage for session media
      behind experimental.media_blob .
    source_release: https://opencode.ai/changelog/v2.2.0
  - quote: Core Reduce work encoding durable event payloads that are not persisted.
    source_release: https://opencode.ai/changelog/v2.2.0
  - quote: Core Apply OpenCode Console workspace configuration as a configuration
      layer.
    source_release: https://opencode.ai/changelog/v2.2.0
  - quote: Core Show OpenCode Console budget limits and Go usage where they block
      you.
    source_release: https://opencode.ai/changelog/v2.2.0
  - quote: Core Record provider-reported session costs.
    source_release: https://opencode.ai/changelog/v2.2.0
  - quote: Core Return a server error with a reference ID when the server cannot encode
      a response.
    source_release: https://opencode.ai/changelog/v2.2.0
  - quote: Core Use the correct Vertex AI endpoints for the eu and us multi-regions.
    source_release: https://opencode.ai/changelog/v2.2.0
  - quote: Core Accept Databricks hosts that include http:// or https:// .
    source_release: https://opencode.ai/changelog/v2.2.0
  - quote: Core Close project locations concurrently during shutdown.
    source_release: https://opencode.ai/changelog/v2.2.0
  - quote: Core Treat equivalent directory paths, including trailing slashes, as one
      location.
    source_release: https://opencode.ai/changelog/v2.2.0
  - quote: Core Send valid tool schemas to Kimi for tuple, default, and keyword-like
      arguments.
    source_release: https://opencode.ai/changelog/v2.2.0
  - quote: Core Detect AVIF, HEIC/HEIF, QuickTime, and M4A attachments correctly.
    source_release: https://opencode.ai/changelog/v2.2.0
  - quote: Core Keep active locations alive when session events use an equivalent
      directory path.
    source_release: https://opencode.ai/changelog/v2.2.0
  - quote: Core Reload compatibility skills only when their own sources change.
    source_release: https://opencode.ai/changelog/v2.2.0
  - quote: Core Avoid publishing redundant catalog updates when configuration is unchanged.
    source_release: https://opencode.ai/changelog/v2.2.0
  - quote: Core Avoid booting idle or deleted project locations while polling session
      forms.
    source_release: https://opencode.ai/changelog/v2.2.0
  - quote: Core Manage sessions and instruction entries after their project directory
      is deleted.
    source_release: https://opencode.ai/changelog/v2.2.0
  - quote: Core Start fuzzy file search only on first use, reducing project startup
      work.
    source_release: https://opencode.ai/changelog/v2.2.0
  - quote: Core Exit after 10 seconds when shutdown hangs and report pending work.
    source_release: https://opencode.ai/changelog/v2.2.0
  - quote: Core Send xAI Responses top_k settings and stop sending unsupported penalties.
    source_release: https://opencode.ai/changelog/v2.2.0
  - quote: Core Classify AWS REST JSON errors consistently regardless of where the
      error type appears.
    source_release: https://opencode.ai/changelog/v2.2.0
  - quote: Core Validate large base64 attachments without slowdowns or hangs.
    source_release: https://opencode.ai/changelog/v2.2.0
  - quote: Core Match absolute instruction-file globs across directories.
    source_release: https://opencode.ai/changelog/v2.2.0
  - quote: Core Use configured provider regions in Bedrock endpoint URLs.
    source_release: https://opencode.ai/changelog/v2.2.0
  - quote: Core Handle unknown OpenAI Chat finish reasons without failing the response.
    source_release: https://opencode.ai/changelog/v2.2.0
  - quote: Core Prefer JPEG for opaque browser screenshots, reducing attachment size.
    source_release: https://opencode.ai/changelog/v2.2.0
  - quote: Core Detect generated image types from their bytes when compatible hosts
      omit the format.
    source_release: https://opencode.ai/changelog/v2.2.0
  - quote: Core Keep project services alive while sessions run long tools or wait
      for input, with a 24-hour inactivity cap.
    source_release: https://opencode.ai/changelog/v2.2.0
  - quote: Core Prevent unrelated configuration changes and compatibility-skill update
      bursts from repeatedly reloading skills.
    source_release: https://opencode.ai/changelog/v2.2.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: opencode
  product_name: OpenCode
  slug: 31-other-changes-in-v2-2-0
  source_release: opencode-2026-10-27-v2-2-0-f60b51f1
  source_type: opencode_changelog
  theme: uncategorized
  title: 31 other changes in v2.2.0
  type: change
source_release: '[[Releases/OpenCode/opencode-2026-10-27-v2-2-0-f60b51f1|opencode-2026-10-27-v2-2-0-f60b51f1]]'
source_type: opencode_changelog
theme: uncategorized
title: 31 other changes in v2.2.0
type: change
---

<!-- chronolog:begin region="header" -->
# 31 other changes in v2.2.0

**OpenCode** · 2026-10-27 · Other changes · Digest · [Official source](https://opencode.ai/changelog/v2.2.0) · from [[Releases/OpenCode/opencode-2026-10-27-v2-2-0-f60b51f1|v2.2.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Core Add an experimental API for session media and opt-in media URI support.

> Core Add the machine hostname to /api/info .

> Core Add experimental content-addressed blob storage for session media behind experimental.media_blob .

> Core Reduce work encoding durable event payloads that are not persisted.

> Core Apply OpenCode Console workspace configuration as a configuration layer.

> Core Show OpenCode Console budget limits and Go usage where they block you.

> Core Record provider-reported session costs.

> Core Return a server error with a reference ID when the server cannot encode a response.

> Core Use the correct Vertex AI endpoints for the eu and us multi-regions.

> Core Accept Databricks hosts that include http:// or https:// .

> Core Close project locations concurrently during shutdown.

> Core Treat equivalent directory paths, including trailing slashes, as one location.

> Core Send valid tool schemas to Kimi for tuple, default, and keyword-like arguments.

> Core Detect AVIF, HEIC/HEIF, QuickTime, and M4A attachments correctly.

> Core Keep active locations alive when session events use an equivalent directory path.

> Core Reload compatibility skills only when their own sources change.

> Core Avoid publishing redundant catalog updates when configuration is unchanged.

> Core Avoid booting idle or deleted project locations while polling session forms.

> Core Manage sessions and instruction entries after their project directory is deleted.

> Core Start fuzzy file search only on first use, reducing project startup work.

> Core Exit after 10 seconds when shutdown hangs and report pending work.

> Core Send xAI Responses top_k settings and stop sending unsupported penalties.

> Core Classify AWS REST JSON errors consistently regardless of where the error type appears.

> Core Validate large base64 attachments without slowdowns or hangs.

> Core Match absolute instruction-file globs across directories.

> Core Use configured provider regions in Bedrock endpoint URLs.

> Core Handle unknown OpenAI Chat finish reasons without failing the response.

> Core Prefer JPEG for opaque browser screenshots, reducing attachment size.

> Core Detect generated image types from their bytes when compatible hosts omit the format.

> Core Keep project services alive while sessions run long tools or wait for input, with a 24-hour inactivity cap.

> Core Prevent unrelated configuration changes and compatibility-skill update bursts from repeatedly reloading skills.

Source: https://opencode.ai/changelog/v2.2.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenCode/2026-10-27-73-mobile-and-desktop-changes-in-v2-2-0|73 Mobile and Desktop changes in v2.2.0]] · Mobile and Desktop
- [[Changes/OpenCode/2026-10-27-13-model-support-changes-in-v2-2-0|13 Model Support changes in v2.2.0]] · Model Support
- [[Changes/OpenCode/2026-10-27-core-preserve-literal-0-and-arguments-text-in-custom-command-input|Core Preserve literal $0 and $ARGUMENTS text in custom command input]] · Pricing Model
- [[Changes/OpenCode/2026-10-27-add-experimental-image-and-decision-generation-apis-to-plugins-and-sdk|Add experimental image and decision generation APIs to plugins and sdk]] · Apps and Integrations
- [[Changes/OpenCode/2026-10-27-2-search-and-browsing-changes-in-v2-2-0|2 Search and Browsing changes in v2.2.0]] · Search and Browsing
- [[Changes/OpenCode/2026-10-27-create-install-and-share-desktop-plugins-experimental|Create, install and share Desktop plugins (experimental)]] · Apps and Integrations
- [[Changes/OpenCode/2026-10-27-10-interface-experience-changes-in-v2-2-0|10 Interface Experience changes in v2.2.0]] · Interface Experience
- [[Changes/OpenCode/2026-10-27-3-context-window-changes-in-v2-2-0|3 Context Window changes in v2.2.0]] · Context Window
- [[Changes/OpenCode/2026-10-27-restored-the-todo-tool-in-desktop-via-opt-in|Restored the Todo tool in desktop via opt-in]] · Mobile and Desktop
- [[Changes/OpenCode/2026-10-27-tui-plugins-require-opentui-0-7|TUI plugins require OpenTUI 0.7]] · Apps and Integrations
- [[Changes/OpenCode/2026-10-27-8-memory-and-personalization-changes-in-v2-2-0|8 Memory and Personalization changes in v2.2.0]] · Memory and Personalization
- [[Changes/OpenCode/2026-10-27-14-apps-and-integrations-changes-in-v2-2-0|14 Apps and Integrations changes in v2.2.0]] · Apps and Integrations
- [[Changes/OpenCode/2026-10-27-core-honor-shared-parallel-tool-call-and-service-tier-settings-for-groq|Core Honor shared parallel tool-call and service-tier settings for Groq]] · Collaboration
- [[Changes/OpenCode/2026-10-27-2-voice-and-audio-changes-in-v2-2-0|2 Voice and Audio changes in v2.2.0]] · Voice and Audio
- [[Changes/OpenCode/2026-10-27-refreshed-the-desktop-app-experience|Refreshed the desktop app experience]] · Mobile and Desktop
- [[Changes/OpenCode/2026-10-27-2-safety-and-privacy-changes-in-v2-2-0|2 Safety and Privacy changes in v2.2.0]] · Safety and Privacy
- [[Changes/OpenCode/2026-10-27-core-coordinate-oauth-credential-refreshes-across-locations-and-processes|Core Coordinate OAuth credential refreshes across locations and processes]] · Account and Access
- [[Changes/OpenCode/2026-10-27-5-editor-experience-changes-in-v2-2-0|5 Editor Experience changes in v2.2.0]] · Editor Experience
- [[Changes/OpenCode/2026-10-27-plugins-can-now-attach-and-update-keyed-session-instructions-with-ctx-session-in|Plugins can now attach and update keyed session instructions…]] · Apps and Integrations
- [[Changes/OpenCode/2026-10-27-add-configurable-prompt-cache-ttls-per-provider-model|Add configurable prompt cache TTLs per provider/model]] · Model Support
- [[Changes/OpenCode/2026-10-27-2-agent-mode-changes-in-v2-2-0|2 Agent Mode changes in v2.2.0]] · Agent Mode
- [[Changes/OpenCode/2026-10-27-3-projects-and-workspaces-changes-in-v2-2-0|3 Projects and Workspaces changes in v2.2.0]] · Projects and Workspaces
- [[Changes/OpenCode/2026-10-27-opencode-ai-root-is-now-the-promise-api|opencode/ai root is now the Promise API]] · Apps and Integrations
- [[Changes/OpenCode/2026-10-27-13-developer-workflow-changes-in-v2-2-0|13 Developer Workflow changes in v2.2.0]] · Developer Workflow
- [[Changes/OpenCode/2026-10-27-6-reliability-and-performance-changes-in-v2-2-0|6 Reliability and Performance changes in v2.2.0]] · Reliability and Performance
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20opencode-2026-10-27-c619d1&body=Card%3A%20Changes%2FOpenCode%2F2026-10-27-31-other-changes-in-v2-2-0.md%0ACard%20ID%3A%20opencode-2026-10-27-c619d1%0ASource%3A%20https%3A%2F%2Fopencode.ai%2Fchangelog%2Fv2.2.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->