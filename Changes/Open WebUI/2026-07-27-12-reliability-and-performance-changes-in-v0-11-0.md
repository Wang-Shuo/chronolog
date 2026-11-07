---
card_id: open-webui-2026-07-27-d3e580
date: '2026-07-27'
description: "Open WebUI · 2026-07-27 · Reliability and Performance: 12 changes in
  v0.11.0 — \U0001F527 **Faster tool and knowledge base listings.** Listing tools
  no longer loads…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-11-19-opening-projects-is-now-much-faster|Opening
    Projects is now much faster]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2807
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 021da1914192c438b13cec4741c35c5bf4ae02be12f27d33075680f30dc6047f
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-07-27-d3e580
  comparison: ''
  date: '2026-07-27'
  description: 'Open WebUI — v0.11.0: 12 Reliability and Performance changes'
  evidence:
  - quote: "\U0001F527 **Faster tool and knowledge base listings.** Listing tools
      no longer loads each one's full source, and working out which tools and knowledge
      bases you can see takes a single check rather than one per item. [#27387](https://github.com/open-webui/open-webui/pull/27387)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F4D7 **Faster knowledge base file lists.** Opening a knowledge base
      now loads just the file names and details instead of the entire extracted text
      of every document, so large collections appear almost instantly. [#27386](https://github.com/open-webui/open-webui/pull/27386),
      [#26144](https://github.com/open-webui/open-webui/issues/26144)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F5DD️ **Faster file access checks.** Working out whether you can
      open a file no longer scales with how many workspace models and knowledge bases
      exist, so opening files and listing folder contents stays quick on large instances.
      [#27383](https://github.com/open-webui/open-webui/pull/27383)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F4C1 **Faster folder loading.** Your folder list no longer runs
      a separate lookup for every folder to check where it sits, so it loads in a
      single pass. [Commit](https://github.com/open-webui/open-webui/commit/9a49b271aaf5d6eeaec24ab974be38a8c68ddd76)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: ✍️ **Faster saves across the app.** Saving a chat, note, prompt, tool or
      user setting no longer re-reads the record it just wrote, so writes finish sooner,
      most noticeably on long conversations. [#27381](https://github.com/open-webui/open-webui/pull/27381),
      [#27379](https://github.com/open-webui/open-webui/pull/27379), [Commit](https://github.com/open-webui/open-webui/commit/c182a95ffdb87bae3d47d93387ec1a26c97740a2),
      [Commit](https://github.com/open-webui/open-webui/commit/977c7930623b860949410a73922579daf81705a7)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F680 **Lower per-request overhead.** Requests no longer each perform
      a settings lookup before they are handled, trimming a little latency from everything
      the app does. [Commit](https://github.com/open-webui/open-webui/commit/4493b56e424db29fa9e72310b1ca6b025c3e5f8b),
      [#27395](https://github.com/open-webui/open-webui/pull/27395), [Commit](https://github.com/open-webui/open-webui/commit/6ff1df326c76824f0706671b0974df4035cb453f),
      [Commit](https://github.com/open-webui/open-webui/commit/85664f650cc111a6b170b97ed0c391d962717bec),
      [#27227](https://github.com/open-webui/open-webui/pull/27227)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F4E6 **Faster JSON handling as an option.** Administrators can now
      switch the whole application to a faster encoder through a new \"ENABLE_ORJSON\"
      setting, covering request bodies, responses, upstream provider payloads and
      live updates, where the encoding of live updates was the largest single cost
      on the workers handling them in clustered deployments; it stays off by default
      because the faster encoder is stricter about what it accepts. [#27583](https://github.com/open-webui/open-webui/pull/27583)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: ⚙️ **Faster Redis handling.** The compiled "hiredis" parser now ships as
      a dependency and is used automatically, so deployments backed by Redis spend
      noticeably less processor time reading responses. [#27282](https://github.com/open-webui/open-webui/pull/27282)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F3CE️ **Faster chat search on PostgreSQL.** Searching chats on PostgreSQL
      now reads from the message table instead of unpacking each conversation's stored
      data row by row, so results stay quick as your history grows. [Commit](https://github.com/open-webui/open-webui/commit/cc9a44569ef08b64ff44d15607c43966f362ce75),
      [#27221](https://github.com/open-webui/open-webui/issues/27221)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F236 **Faster uploads of non-English text files.** Working out the
      encoding of an uploaded text file now samples the part that needs it rather
      than scanning the whole file, taking a four megabyte Japanese or Chinese document
      from several seconds down to well under one. [#27445](https://github.com/open-webui/open-webui/pull/27445)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F504 **General improvements.** Various improvements were implemented
      across the application to enhance performance, stability, and security."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: ⏳ **Faster licensed startup.** Instances with a license key no longer wait
      on the license server during startup, so the app becomes ready to serve traffic
      without that delay. [Commit](https://github.com/open-webui/open-webui/commit/8f7753331752e72b17ef8f055318ab548a73f4b8),
      [Commit](https://github.com/open-webui/open-webui/commit/0c7ddbdb4f7dbd46f1dadc3242dbb13b81b47758)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 12-reliability-and-performance-changes-in-v0-11-0
  source_release: open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f
  source_type: github_releases
  theme: reliability-performance
  title: 12 Reliability and Performance changes in v0.11.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-07-21-3-reliability-and-performance-changes-in-rust-v0-145-0|3
  Reliability and Performance changes in rust-v0.145.0]]'
- '[[Changes/Kimi Code/2026-07-22-improve-tui-performance-and-resume-speed-for-long-running-sessions|Improve
  TUI performance and resume speed for long-running sessions]]'
- '[[Changes/Ollama/2026-07-23-expanded-gpu-support-with-cuda-on-windows-arm64-b200-support-through-cuda-12-and|Expanded
  GPU support with CUDA on Windows ARM64, B200 support through CUDA 12…]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f|open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f]]'
source_type: github_releases
theme: reliability-performance
title: 12 Reliability and Performance changes in v0.11.0
type: change
---

<!-- chronolog:begin region="header" -->
# 12 Reliability and Performance changes in v0.11.0

**Open WebUI** · 2026-07-27 · [[Themes/reliability-performance|Reliability and Performance]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.0) · from [[Releases/Open WebUI/open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f|v0.11.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔧 **Faster tool and knowledge base listings.** Listing tools no longer loads each one's full source, and working out which tools and knowledge bases you can see takes a single check rather than one per item. [#27387](https://github.com/open-webui/open-webui/pull/27387)

> 📗 **Faster knowledge base file lists.** Opening a knowledge base now loads just the file names and details instead of the entire extracted text of every document, so large collections appear almost instantly. [#27386](https://github.com/open-webui/open-webui/pull/27386), [#26144](https://github.com/open-webui/open-webui/issues/26144)

> 🗝️ **Faster file access checks.** Working out whether you can open a file no longer scales with how many workspace models and knowledge bases exist, so opening files and listing folder contents stays quick on large instances. [#27383](https://github.com/open-webui/open-webui/pull/27383)

> 📁 **Faster folder loading.** Your folder list no longer runs a separate lookup for every folder to check where it sits, so it loads in a single pass. [Commit](https://github.com/open-webui/open-webui/commit/9a49b271aaf5d6eeaec24ab974be38a8c68ddd76)

> ✍️ **Faster saves across the app.** Saving a chat, note, prompt, tool or user setting no longer re-reads the record it just wrote, so writes finish sooner, most noticeably on long conversations. [#27381](https://github.com/open-webui/open-webui/pull/27381), [#27379](https://github.com/open-webui/open-webui/pull/27379), [Commit](https://github.com/open-webui/open-webui/commit/c182a95ffdb87bae3d47d93387ec1a26c97740a2), [Commit](https://github.com/open-webui/open-webui/commit/977c7930623b860949410a73922579daf81705a7)

> 🚀 **Lower per-request overhead.** Requests no longer each perform a settings lookup before they are handled, trimming a little latency from everything the app does. [Commit](https://github.com/open-webui/open-webui/commit/4493b56e424db29fa9e72310b1ca6b025c3e5f8b), [#27395](https://github.com/open-webui/open-webui/pull/27395), [Commit](https://github.com/open-webui/open-webui/commit/6ff1df326c76824f0706671b0974df4035cb453f), [Commit](https://github.com/open-webui/open-webui/commit/85664f650cc111a6b170b97ed0c391d962717bec), [#27227](https://github.com/open-webui/open-webui/pull/27227)

> 📦 **Faster JSON handling as an option.** Administrators can now switch the whole application to a faster encoder through a new "ENABLE_ORJSON" setting, covering request bodies, responses, upstream provider payloads and live updates, where the encoding of live updates was the largest single cost on the workers handling them in clustered deployments; it stays off by default because the faster encoder is stricter about what it accepts. [#27583](https://github.com/open-webui/open-webui/pull/27583)

> ⚙️ **Faster Redis handling.** The compiled "hiredis" parser now ships as a dependency and is used automatically, so deployments backed by Redis spend noticeably less processor time reading responses. [#27282](https://github.com/open-webui/open-webui/pull/27282)

> 🏎️ **Faster chat search on PostgreSQL.** Searching chats on PostgreSQL now reads from the message table instead of unpacking each conversation's stored data row by row, so results stay quick as your history grows. [Commit](https://github.com/open-webui/open-webui/commit/cc9a44569ef08b64ff44d15607c43966f362ce75), [#27221](https://github.com/open-webui/open-webui/issues/27221)

> 🈶 **Faster uploads of non-English text files.** Working out the encoding of an uploaded text file now samples the part that needs it rather than scanning the whole file, taking a four megabyte Japanese or Chinese document from several seconds down to well under one. [#27445](https://github.com/open-webui/open-webui/pull/27445)

> 🔄 **General improvements.** Various improvements were implemented across the application to enhance performance, stability, and security.

> ⏳ **Faster licensed startup.** Instances with a license key no longer wait on the license server during startup, so the app becomes ready to serve traffic without that delay. [Commit](https://github.com/open-webui/open-webui/commit/8f7753331752e72b17ef8f055318ab548a73f4b8), [Commit](https://github.com/open-webui/open-webui/commit/0c7ddbdb4f7dbd46f1dadc3242dbb13b81b47758)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-07-27-9-automation-and-scheduling-changes-in-v0-11-0|9 Automation and Scheduling changes in v0.11.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-07-27-13-safety-and-privacy-changes-in-v0-11-0|13 Safety and Privacy changes in v0.11.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-07-27-4-voice-and-audio-changes-in-v0-11-0|4 Voice and Audio changes in v0.11.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-07-27-62-developer-workflow-changes-in-v0-11-0|62 Developer Workflow changes in v0.11.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-07-27-19-interface-experience-changes-in-v0-11-0|19 Interface Experience changes in v0.11.0]] · Interface Experience
- [[Changes/Open WebUI/2026-07-27-7-memory-and-personalization-changes-in-v0-11-0|7 Memory and Personalization changes in v0.11.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-07-27-sub-agents-administrators-can-now-enable-sub-agents-which-let-a-model-hand-parts|🤖 Sub-agents. Administrators can now enable sub-agents, which let a model hand…]] · Agent Mode
- [[Changes/Open WebUI/2026-07-27-media-types-an-extraction-engine-may-handle-administrators-can-now-list-which-im|🖼️ Media types an extraction engine may handle. Administrators can now list…]] · Multimodal Input
- [[Changes/Open WebUI/2026-07-27-15-account-and-access-changes-in-v0-11-0|15 Account and Access changes in v0.11.0]] · Account and Access
- [[Changes/Open WebUI/2026-07-27-shared-image-checkpoint-changes-only-administrators-can-now-change-the-instance|🖌️ Shared image checkpoint changes. Only administrators can now change…]] · Image Generation
- [[Changes/Open WebUI/2026-07-27-7-search-and-browsing-changes-in-v0-11-0|7 Search and Browsing changes in v0.11.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-07-27-2-collaboration-changes-in-v0-11-0|2 Collaboration changes in v0.11.0]] · Collaboration
- [[Changes/Open WebUI/2026-07-27-6-apps-and-integrations-changes-in-v0-11-0|6 Apps and Integrations changes in v0.11.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-07-27-3-enterprise-and-administration-changes-in-v0-11-0|3 Enterprise and Administration changes in v0.11.0]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-07-27-9-context-window-changes-in-v0-11-0|9 Context Window changes in v0.11.0]] · Context Window
- [[Changes/Open WebUI/2026-07-27-2-pricing-model-changes-in-v0-11-0|2 Pricing Model changes in v0.11.0]] · Pricing Model
- [[Changes/Open WebUI/2026-07-27-9-files-and-data-changes-in-v0-11-0|9 Files and Data changes in v0.11.0]] · Files and Data
- [[Changes/Open WebUI/2026-07-27-39-model-support-changes-in-v0-11-0|39 Model Support changes in v0.11.0]] · Model Support
- [[Changes/Open WebUI/2026-07-27-7-editor-experience-changes-in-v0-11-0|7 Editor Experience changes in v0.11.0]] · Editor Experience
- [[Changes/Open WebUI/2026-07-27-2-mobile-and-desktop-changes-in-v0-11-0|2 Mobile and Desktop changes in v0.11.0]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-07-27-42-other-changes-in-v0-11-0|42 other changes in v0.11.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2026-07-23 · Ollama · [[Changes/Ollama/2026-07-23-expanded-gpu-support-with-cuda-on-windows-arm64-b200-support-through-cuda-12-and|Expanded GPU support with CUDA on Windows ARM64, B200 support through CUDA 12…]]
- Later: 2026-07-28 · Dify · [[Changes/Dify/2026-07-28-lightweight-recent-apps-endpoint-new-get-console-api-apps-recent-endpoint-reduce|Lightweight recent apps endpoint]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-11-19 · Descript · [[Changes/Descript/2018-11-19-opening-projects-is-now-much-faster|Opening Projects is now much faster]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-07-27-d3e580&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-07-27-12-reliability-and-performance-changes-in-v0-11-0.md%0ACard%20ID%3A%20open-webui-2026-07-27-d3e580%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->