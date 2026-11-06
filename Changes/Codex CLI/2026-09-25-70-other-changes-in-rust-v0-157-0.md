---
card_id: codex-cli-2026-09-25-d11072
date: '2026-09-25'
description: 'Codex CLI · 2026-09-25 · Other changes: 70 changes in 0.157.0 — Enabled
  automatic background-server startup for eligible interactive sessions, with recovery…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 0e8c61612560021e0dbf24cacb94523361322c5b01ab483fe9d9d6dbcc49d436
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-09-25-d11072
  comparison: ''
  date: '2026-09-25'
  description: 'Codex CLI — 0.157.0: 70 other changes'
  evidence:
  - quote: 'Enabled automatic background-server startup for eligible interactive sessions,
      with recovery choices when server settings are incompatible. (#47179, #47318)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: Added an `f` shortcut to fork conversations open in another app, preserving
      drafts and queued prompts. (#47185)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: Made `/import` available in remote sessions and local background-server
      sessions. (#47317)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: 'Recovered unsent question answers into the composer when turns end, without
      disrupting active history searches. (#47422, #47423)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: 'Enforced network restrictions across redirects and ongoing HTTP and WebSocket
      traffic, including cancellation when policy changes revoke access. (#47389,
      #47407)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47064 Stop redundant message-board reads when limits reach one @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47065 Deduplicate deprecation notices in the TUI transcript @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47068 Highlight selected newlines in the transcript view @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47074 Refresh host-supplied cloud skills at turn startup @TAFOYA-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47077 Serialize environment updates and cancel removed pending attachments
      @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47079 Mask daemon socket paths exposed through ancestor bind mounts @nicksteele-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47083 Extract per-thread enrichment into a dedicated async helper @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47084 Avoid building a host SQLite driver for SQLx macros @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47088 Disable unused default dependency features @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47089 Centralize JSON-RPC response serialization through payloads @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47095 Remove the `rust-release-prepare` workflow @andrewgu-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47096 Keep TUI hints immediately above the composer @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47100 Preserve assistant answers in bounded TUI task responses @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47101 Honor configured proxies for realtime WebSocket connections @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47106 Preserve originating turn metadata for yielded skill calls @eddie-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47108 Preserve required Windows runtime variables for filesystem helpers
      @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47112 Lowercase the retry hint for conversations open in another app
      @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47113 Persist thread creator identity in rollouts and SQLite @nornagon-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47114 Preserve and expose thread item lifecycle timestamps @chiam-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47121 Pass thread IDs to attachment uploads @kchainani-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47122 Increase OpenAI file blob upload timeout from 60 seconds to 5 minutes
      @wilkes-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47125 Add extra policy configuration for Guardian reviews @won-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47129 Preserve foreign working directories in extension tool environments
      @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47132 Support caller-provided MITM CAs in the network proxy @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47143 Extract exec-server CLI startup into a dedicated module @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47149 Update code mode catalog snapshot hashes @andrewgu-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47155 Ignore stale thread-close notifications after resuming a thread
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47162 Apply workspace routing to Guardian v2 classifier requests @acrognale-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47174 Preserve empty cell metadata under pending tool-call pressure @ningyi-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47179 Enable automatic daemon startup by default @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47185 Allow forking conversations locked by another app in the TUI @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47191 Render aligned equations and optimization notation in TUI math
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47199 Separate thread preparation from execution persistence @dermanyang-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47257 Preserve explicit message-board unsubscribes when posting @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47258 Test spawn settings reporting after child removal @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47259 Subscribe authors to message-board channels created by posting
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47271 Implement `AgentControl` for `LocalAgentControl` @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47281 Add regression coverage for message board unsubscribe persistence
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47287 Update the Guardian extra-policy snapshot for retained instructions
      @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47302 Use compact display metadata for Guardian review threads @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47303 Clean up legacy Guardian thread metadata in SQLite @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47317 Enable `/import` in remote and local daemon sessions @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47318 Offer explicit recovery for incompatible background servers @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47321 Honor the system clock preference across more TUI timestamps @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47322 Render TUI Markdown lists with Unicode bullets and checkboxes @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47325 Keep report reason tags within Sentry limits @ningyi-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47330 Identify failed SQLite databases in `codex doctor` output @dkovalenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47331 Avoid redundant spacing above the transcript composer @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47340 Add conditional turn interruption that preserves pending input
      @pmccrary-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47342 Skip stored title lookups for ephemeral forks @keyz'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47350 Reuse cloud skill catalogs across turns until invalidated @hlevy-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47353 Preserve `invalid_prompt` as a distinct error classification @rennie-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47355 Reserve spacing after recaps at the transcript tail @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47358 Color paths and URLs in `codex doctor` by check status @dkovalenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47362 Bound inbound exec-server requests across client transports @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47389 Enforce network policy throughout HTTP and WebSocket requests @acrognale-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47393 Retry transient OpenAI file blob upload failures @mtsui-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47407 Enforce application network policy across app-server requests @acrognale-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47408 Enforce application network policy for AWS auth and telemetry @acrognale-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47414 Support Shift-click to extend transcript selections @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47422 Recover unsent question drafts when TUI turns end @imac-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47423 Preserve history search during background draft recovery @imac-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47424 Clear pending async question notifications when turns end @imac-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47428 Apply inherited environment settings at turn boundaries @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47437 Stabilize retry timing and WebSocket tests @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 70-other-changes-in-rust-v0-157-0
  source_release: codex-cli-2026-09-25-rust-v0-157-0-github-396234532-e8248ab3
  source_type: github_releases
  theme: uncategorized
  title: 70 other changes in rust-v0.157.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-09-25-rust-v0-157-0-github-396234532-e8248ab3|codex-cli-2026-09-25-rust-v0-157-0-github-396234532-e8248ab3]]'
source_type: github_releases
theme: uncategorized
title: 70 other changes in rust-v0.157.0
type: change
---

<!-- chronolog:begin region="header" -->
# 70 other changes in rust-v0.157.0

**Codex CLI** · 2026-09-25 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.157.0) · from [[Releases/Codex CLI/codex-cli-2026-09-25-rust-v0-157-0-github-396234532-e8248ab3|0.157.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Enabled automatic background-server startup for eligible interactive sessions, with recovery choices when server settings are incompatible. (#47179, #47318)

> Added an `f` shortcut to fork conversations open in another app, preserving drafts and queued prompts. (#47185)

> Made `/import` available in remote sessions and local background-server sessions. (#47317)

> Recovered unsent question answers into the composer when turns end, without disrupting active history searches. (#47422, #47423)

> Enforced network restrictions across redirects and ongoing HTTP and WebSocket traffic, including cancellation when policy changes revoke access. (#47389, #47407)

> #47064 Stop redundant message-board reads when limits reach one @jif-oai

> #47065 Deduplicate deprecation notices in the TUI transcript @etraut-openai

> #47068 Highlight selected newlines in the transcript view @etraut-openai

> #47074 Refresh host-supplied cloud skills at turn startup @TAFOYA-OAI

> #47077 Serialize environment updates and cancel removed pending attachments @sayan-oai

> #47079 Mask daemon socket paths exposed through ancestor bind mounts @nicksteele-oai

> #47083 Extract per-thread enrichment into a dedicated async helper @aibrahim-oai

> #47084 Avoid building a host SQLite driver for SQLx macros @aibrahim-oai

> #47088 Disable unused default dependency features @aibrahim-oai

> #47089 Centralize JSON-RPC response serialization through payloads @aibrahim-oai

> #47095 Remove the `rust-release-prepare` workflow @andrewgu-oai

> #47096 Keep TUI hints immediately above the composer @fcoury-oai

> #47100 Preserve assistant answers in bounded TUI task responses @etraut-openai

> #47101 Honor configured proxies for realtime WebSocket connections @celia-oai

> #47106 Preserve originating turn metadata for yielded skill calls @eddie-openai

> #47108 Preserve required Windows runtime variables for filesystem helpers @iceweasel-oai

> #47112 Lowercase the retry hint for conversations open in another app @fcoury-oai

> #47113 Persist thread creator identity in rollouts and SQLite @nornagon-openai

> #47114 Preserve and expose thread item lifecycle timestamps @chiam-oai

> #47121 Pass thread IDs to attachment uploads @kchainani-oai

> #47122 Increase OpenAI file blob upload timeout from 60 seconds to 5 minutes @wilkes-oai

> #47125 Add extra policy configuration for Guardian reviews @won-openai

> #47129 Preserve foreign working directories in extension tool environments @anp-oai

> #47132 Support caller-provided MITM CAs in the network proxy @viyatb-oai

> #47143 Extract exec-server CLI startup into a dedicated module @anp-oai

> #47149 Update code mode catalog snapshot hashes @andrewgu-oai

> #47155 Ignore stale thread-close notifications after resuming a thread @etraut-openai

> #47162 Apply workspace routing to Guardian v2 classifier requests @acrognale-oai

> #47174 Preserve empty cell metadata under pending tool-call pressure @ningyi-oai

> #47179 Enable automatic daemon startup by default @etraut-openai

> #47185 Allow forking conversations locked by another app in the TUI @fcoury-oai

> #47191 Render aligned equations and optimization notation in TUI math @etraut-openai

> #47199 Separate thread preparation from execution persistence @dermanyang-oai

> #47257 Preserve explicit message-board unsubscribes when posting @jif-oai

> #47258 Test spawn settings reporting after child removal @jif-oai

> #47259 Subscribe authors to message-board channels created by posting @jif-oai

> #47271 Implement `AgentControl` for `LocalAgentControl` @jif-oai

> #47281 Add regression coverage for message board unsubscribe persistence @jif-oai

> #47287 Update the Guardian extra-policy snapshot for retained instructions @felixxia-oai

> #47302 Use compact display metadata for Guardian review threads @charliemarsh-oai

> #47303 Clean up legacy Guardian thread metadata in SQLite @charliemarsh-oai

> #47317 Enable `/import` in remote and local daemon sessions @etraut-openai

> #47318 Offer explicit recovery for incompatible background servers @etraut-openai

> #47321 Honor the system clock preference across more TUI timestamps @etraut-openai

> #47322 Render TUI Markdown lists with Unicode bullets and checkboxes @etraut-openai

> #47325 Keep report reason tags within Sentry limits @ningyi-oai

> #47330 Identify failed SQLite databases in `codex doctor` output @dkovalenko-oai

> #47331 Avoid redundant spacing above the transcript composer @fcoury-oai

> #47340 Add conditional turn interruption that preserves pending input @pmccrary-oai

> #47342 Skip stored title lookups for ephemeral forks @keyz

> #47350 Reuse cloud skill catalogs across turns until invalidated @hlevy-openai

> #47353 Preserve `invalid_prompt` as a distinct error classification @rennie-openai

> #47355 Reserve spacing after recaps at the transcript tail @fcoury-oai

> #47358 Color paths and URLs in `codex doctor` by check status @dkovalenko-oai

> #47362 Bound inbound exec-server requests across client transports @viyatb-oai

> #47389 Enforce network policy throughout HTTP and WebSocket requests @acrognale-oai

> #47393 Retry transient OpenAI file blob upload failures @mtsui-oai

> #47407 Enforce application network policy across app-server requests @acrognale-oai

> #47408 Enforce application network policy for AWS auth and telemetry @acrognale-oai

> #47414 Support Shift-click to extend transcript selections @etraut-openai

> #47422 Recover unsent question drafts when TUI turns end @imac-oai

> #47423 Preserve history search during background draft recovery @imac-oai

> #47424 Clear pending async question notifications when turns end @imac-oai

> #47428 Apply inherited environment settings at turn boundaries @sayan-oai

> #47437 Stabilize retry timing and WebSocket tests @anp-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.157.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-09-25-9-apps-and-integrations-changes-in-rust-v0-157-0|9 Apps and Integrations changes in rust-v0.157.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-09-25-47411-apply-shared-network-policy-throughout-embedded-codex-startup-acrognale-oa|♯47411 Apply shared network policy throughout embedded Codex startup @acrognale-oai]] · Collaboration
- [[Changes/Codex CLI/2026-09-25-6-context-window-changes-in-rust-v0-157-0|6 Context Window changes in rust-v0.157.0]] · Context Window
- [[Changes/Codex CLI/2026-09-25-47086-format-analytics-credit-usage-with-consistent-decimal-precision-fcoury-oai|♯47086 Format analytics credit usage with consistent decimal precision @fcoury-oai]] · Pricing Model
- [[Changes/Codex CLI/2026-09-25-2-safety-and-privacy-changes-in-rust-v0-157-0|2 Safety and Privacy changes in rust-v0.157.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-09-25-8-model-support-changes-in-rust-v0-157-0|8 Model Support changes in rust-v0.157.0]] · Model Support
- [[Changes/Codex CLI/2026-09-25-9-interface-experience-changes-in-rust-v0-157-0|9 Interface Experience changes in rust-v0.157.0]] · Interface Experience
- [[Changes/Codex CLI/2026-09-25-added-retries-for-transient-file-upload-failures-and-increased-the-upload-timeou|Added retries for transient file-upload failures and increased the upload timeout…]] · Files and Data
- [[Changes/Codex CLI/2026-09-25-47327-preserve-image-generation-request-ids-on-failure-chrisdong-oai|♯47327 Preserve image generation request IDs on failure @chrisdong-oai]] · Image Generation
- [[Changes/Codex CLI/2026-09-25-5-voice-and-audio-changes-in-rust-v0-157-0|5 Voice and Audio changes in rust-v0.157.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-09-25-4-developer-workflow-changes-in-rust-v0-157-0|4 Developer Workflow changes in rust-v0.157.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-09-25-2-search-and-browsing-changes-in-rust-v0-157-0|2 Search and Browsing changes in rust-v0.157.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-09-25-13-agent-mode-changes-in-rust-v0-157-0|13 Agent Mode changes in rust-v0.157.0]] · Agent Mode
- [[Changes/Codex CLI/2026-09-25-5-account-and-access-changes-in-rust-v0-157-0|5 Account and Access changes in rust-v0.157.0]] · Account and Access
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-09-25-d11072&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-09-25-70-other-changes-in-rust-v0-157-0.md%0ACard%20ID%3A%20codex-cli-2026-09-25-d11072%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.157.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->