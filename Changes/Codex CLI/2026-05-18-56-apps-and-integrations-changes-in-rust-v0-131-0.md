---
card_id: codex-cli-2026-05-18-7794df
date: '2026-05-18'
description: 'Codex CLI · 2026-05-18 · Apps and Integrations: 56 changes in 0.131.0
  — `@` mentions now search files, directories, plugins, and skills in one picker,
  backed…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2712
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 05f5f7086c0b9bde27abf0ea9c5765ea876fee77f8d8ac957f08eb67236d12ab
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-05-18-7794df
  comparison: ''
  date: '2026-05-18'
  description: 'Codex CLI — 0.131.0: 56 Apps and Integrations changes'
  evidence:
  - quote: '`@` mentions now search files, directories, plugins, and skills in one
      picker, backed by app-server plugin metadata. (#19068, #22375)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: 'Plugin workflows gained marketplace CLI commands, version-aware sharing,
      share checkout, clearer shared-workspace buckets, and default-enabled plugin
      hooks. (#21396, #22397, #22425, #22435, #22549)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: 'Remote workflows now support daemon-managed `codex remote-control`, runtime
      enable/disable APIs, status reads, and registry-backed/configured remote environments.
      (#20718, #22218, #22562, #22578, #22877, #20667, #21323)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: 'The Python SDK moved to `openai-codex` / `openai_codex`, with pinned runtime-generated
      types, concurrent turn routing, approval modes, and integration coverage. (#21778,
      #21891, #21893, #21896, #21905, #21910, #22014)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: 'Reduced remote and Windows cleanup friction with longer exec-server transport
      timeouts, quieter `taskkill` cleanup, and non-queued plugin reads. (#21825,
      #21759, #22058, #22703)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: Updated plugin-creator guidance for the simplified local plugin handoff
      links. (#22240)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: 'Removed obsolete tool paths, feature flags, config gates, and legacy hooks
      as defaults stabilized. (#21651, #21805, #22173, #22246, #22565, #22711, #22717,
      #22724, #22730)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21805 [codex] Remove legacy after tool use hooks @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21497 Using cached connector directory for discoverable tools list @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21867 feat: Add role-aware plugin share context APIs @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21778 Route Python SDK turn notifications by ID @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21755 Improve hooks trust flow in TUI @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21759 fix(tui): suppress taskkill output for MCP teardown on Windows
      @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#20825 Read cached metadata for installed Git plugins @xli-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22163 feat: move extensions tool @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21061 feat(connectors): support managed app tool approval requirements
      @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21891 [1/8] Pin Python SDK runtime dependency @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21893 [2/8] Generate Python SDK types from pinned runtime @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21895 [3/8] Run Python SDK tests in CI @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21896 [4/8] Define Python SDK public API surface @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21905 [5/8] Rename Python SDK package to openai-codex @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21910 [6/8] Add high-level Python SDK approval mode @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22014 [7/8] Add Python SDK app-server integration harness @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22021 [8/8] Add Python SDK Ruff formatting @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22218 Update codex remote-control to start the daemon @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21595 Simplify MCP tool handler plumbing @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22221 feat(skills): default plugin creator to personal share flow @efrazer-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22265 feat: Normalize remote plugin summary identities. @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22240 docs(skills): simplify plugin creator deeplink shape @efrazer-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22397 feat: Expose plugin versions and gate plugin sharing @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#20319 Add allow_managed_hooks_only hook requirement @eternal-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22425 feat: Split shared workspace plugins by discoverability @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22439 Remove unavailable MCP placeholder tool backfill @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21969 Use root repo hooks in linked worktrees @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22435 feat: Add plugin share checkout @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22437 [codex] isolate plugin/list from config serialization queue @xli-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22476 feat: add thread lifecycle contributor hooks @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22505 fix: prevent fmt from updating Python SDK lockfile @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22326 [rollout-trace] Add a trace ID to MCP calls. @cassirer-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22527 [codex] Reuse Apps MCP path override for plugin-service rollout
      @adaley-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22549 Enable plugin hooks by default @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22375 Use plugin/list to get list of plugins for mentions @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22564 [codex] Canonicalize shared workspace plugin IDs @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22555 Remove connector_openai prefix filtering @ericning-o'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22562 Improve remote-control daemon UX @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22578 enable/disable remote control at runtime, not via features @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22594 Relax remote plugin sync gate @xli-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21396 [codex] add plugin marketplace CLI commands @caseychow-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22666 [codex] fix plugin CLI active user layer compile @caseychow-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22703 Unqueue plugin list and read requests @xli-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21624 Fix /review mode MCP startup render issue @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22237 Add `user_input_requested_during_turn` to MCP turn metadata @mchen-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22828 Run compact hooks for remote compaction v2 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22843 Ignore configured hooks in git helpers @bookholt-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22872 Forward apps MCP product SKU from Codex config @kumquatexpress'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22877 feat(app-server): update remote control APIs for better UX @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 56-apps-and-integrations-changes-in-rust-v0-131-0
  source_release: codex-cli-2026-05-18-rust-v0-131-0-github-324452638-5f16ff1d
  source_type: github_releases
  theme: apps-integrations
  title: 56 Apps and Integrations changes in rust-v0.131.0
  type: change
related_changes:
- '[[Changes/Replit/2026-05-15-nine-new-connectors-ready-to-use-out-of-the-box|Nine
  new connectors ready to use out of the box]]'
- '[[Changes/Replit/2026-05-15-four-new-mcp-servers-in-the-directory|Four new MCP
  servers in the directory]]'
- '[[Changes/v0/2026-05-15-the-built-with-v0-badge-respects-branding-settings-on-deployed-apps-and-the-prev|The
  "built with v0" badge respects branding settings on deployed apps…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-05-18-rust-v0-131-0-github-324452638-5f16ff1d|codex-cli-2026-05-18-rust-v0-131-0-github-324452638-5f16ff1d]]'
source_type: github_releases
theme: apps-integrations
title: 56 Apps and Integrations changes in rust-v0.131.0
type: change
---

<!-- chronolog:begin region="header" -->
# 56 Apps and Integrations changes in rust-v0.131.0

**Codex CLI** · 2026-05-18 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.131.0) · from [[Releases/Codex CLI/codex-cli-2026-05-18-rust-v0-131-0-github-324452638-5f16ff1d|0.131.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> `@` mentions now search files, directories, plugins, and skills in one picker, backed by app-server plugin metadata. (#19068, #22375)

> Plugin workflows gained marketplace CLI commands, version-aware sharing, share checkout, clearer shared-workspace buckets, and default-enabled plugin hooks. (#21396, #22397, #22425, #22435, #22549)

> Remote workflows now support daemon-managed `codex remote-control`, runtime enable/disable APIs, status reads, and registry-backed/configured remote environments. (#20718, #22218, #22562, #22578, #22877, #20667, #21323)

> The Python SDK moved to `openai-codex` / `openai_codex`, with pinned runtime-generated types, concurrent turn routing, approval modes, and integration coverage. (#21778, #21891, #21893, #21896, #21905, #21910, #22014)

> Reduced remote and Windows cleanup friction with longer exec-server transport timeouts, quieter `taskkill` cleanup, and non-queued plugin reads. (#21825, #21759, #22058, #22703)

> Updated plugin-creator guidance for the simplified local plugin handoff links. (#22240)

> Removed obsolete tool paths, feature flags, config gates, and legacy hooks as defaults stabilized. (#21651, #21805, #22173, #22246, #22565, #22711, #22717, #22724, #22730)

> #21805 [codex] Remove legacy after tool use hooks @pakrym-oai

> #21497 Using cached connector directory for discoverable tools list @mzeng-openai

> #21867 feat: Add role-aware plugin share context APIs @xl-openai

> #21778 Route Python SDK turn notifications by ID @aibrahim-oai

> #21755 Improve hooks trust flow in TUI @abhinav-oai

> #21759 fix(tui): suppress taskkill output for MCP teardown on Windows @fcoury-oai

> #20825 Read cached metadata for installed Git plugins @xli-oai

> #22163 feat: move extensions tool @jif-oai

> #21061 feat(connectors): support managed app tool approval requirements @viyatb-oai

> #21891 [1/8] Pin Python SDK runtime dependency @aibrahim-oai

> #21893 [2/8] Generate Python SDK types from pinned runtime @aibrahim-oai

> #21895 [3/8] Run Python SDK tests in CI @aibrahim-oai

> #21896 [4/8] Define Python SDK public API surface @aibrahim-oai

> #21905 [5/8] Rename Python SDK package to openai-codex @aibrahim-oai

> #21910 [6/8] Add high-level Python SDK approval mode @aibrahim-oai

> #22014 [7/8] Add Python SDK app-server integration harness @aibrahim-oai

> #22021 [8/8] Add Python SDK Ruff formatting @aibrahim-oai

> #22218 Update codex remote-control to start the daemon @owenlin0

> #21595 Simplify MCP tool handler plumbing @pakrym-oai

> #22221 feat(skills): default plugin creator to personal share flow @efrazer-oai

> #22265 feat: Normalize remote plugin summary identities. @xl-openai

> #22240 docs(skills): simplify plugin creator deeplink shape @efrazer-oai

> #22397 feat: Expose plugin versions and gate plugin sharing @xl-openai

> #20319 Add allow_managed_hooks_only hook requirement @eternal-openai

> #22425 feat: Split shared workspace plugins by discoverability @xl-openai

> #22439 Remove unavailable MCP placeholder tool backfill @sayan-oai

> #21969 Use root repo hooks in linked worktrees @abhinav-oai

> #22435 feat: Add plugin share checkout @xl-openai

> #22437 [codex] isolate plugin/list from config serialization queue @xli-oai

> #22476 feat: add thread lifecycle contributor hooks @jif-oai

> #22505 fix: prevent fmt from updating Python SDK lockfile @jif-oai

> #22326 [rollout-trace] Add a trace ID to MCP calls. @cassirer-openai

> #22527 [codex] Reuse Apps MCP path override for plugin-service rollout @adaley-openai

> #22549 Enable plugin hooks by default @abhinav-oai

> #22375 Use plugin/list to get list of plugins for mentions @canvrno-oai

> #22564 [codex] Canonicalize shared workspace plugin IDs @xl-openai

> #22555 Remove connector_openai prefix filtering @ericning-o

> #22562 Improve remote-control daemon UX @owenlin0

> #22578 enable/disable remote control at runtime, not via features @owenlin0

> #22594 Relax remote plugin sync gate @xli-oai

> #21396 [codex] add plugin marketplace CLI commands @caseychow-oai

> #22666 [codex] fix plugin CLI active user layer compile @caseychow-oai

> #22703 Unqueue plugin list and read requests @xli-oai

> #21624 Fix /review mode MCP startup render issue @canvrno-oai

> #22237 Add `user_input_requested_during_turn` to MCP turn metadata @mchen-oai

> #22828 Run compact hooks for remote compaction v2 @jif-oai

> #22843 Ignore configured hooks in git helpers @bookholt-oai

> #22872 Forward apps MCP product SKU from Codex config @kumquatexpress

> #22877 feat(app-server): update remote control APIs for better UX @owenlin0

Source: https://github.com/openai/codex/releases/tag/rust-v0.131.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-05-18-5-account-and-access-changes-in-rust-v0-131-0|5 Account and Access changes in rust-v0.131.0]] · Account and Access
- [[Changes/Codex CLI/2026-05-18-17-safety-and-privacy-changes-in-rust-v0-131-0|17 Safety and Privacy changes in rust-v0.131.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-05-18-9-agent-mode-changes-in-rust-v0-131-0|9 Agent Mode changes in rust-v0.131.0]] · Agent Mode
- [[Changes/Codex CLI/2026-05-18-4-memory-and-personalization-changes-in-rust-v0-131-0|4 Memory and Personalization changes in rust-v0.131.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-05-18-5-interface-experience-changes-in-rust-v0-131-0|5 Interface Experience changes in rust-v0.131.0]] · Interface Experience
- [[Changes/Codex CLI/2026-05-18-12-developer-workflow-changes-in-rust-v0-131-0|12 Developer Workflow changes in rust-v0.131.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-05-18-21954-fix-goal-update-and-add-goal-edit-command-in-tui-etraut-openai|♯21954 Fix goal update and add /goal edit command in TUI @etraut-openai]] · Editor Experience
- [[Changes/Codex CLI/2026-05-18-10-mobile-and-desktop-changes-in-rust-v0-131-0|10 Mobile and Desktop changes in rust-v0.131.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-05-18-7-context-window-changes-in-rust-v0-131-0|7 Context Window changes in rust-v0.131.0]] · Context Window
- [[Changes/Codex CLI/2026-05-18-3-collaboration-changes-in-rust-v0-131-0|3 Collaboration changes in rust-v0.131.0]] · Collaboration
- [[Changes/Codex CLI/2026-05-18-4-model-support-changes-in-rust-v0-131-0|4 Model Support changes in rust-v0.131.0]] · Model Support
- [[Changes/Codex CLI/2026-05-18-155-other-changes-in-rust-v0-131-0|155 other changes in rust-v0.131.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-05-15 · v0 · [[Changes/v0/2026-05-15-the-built-with-v0-badge-respects-branding-settings-on-deployed-apps-and-the-prev|The "built with v0" badge respects branding settings on deployed apps…]]
- Later: 2026-05-18 · ElevenLabs · [[Changes/ElevenLabs/2026-05-18-sdk-releases|SDK Releases]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-05-18-7794df&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-05-18-56-apps-and-integrations-changes-in-rust-v0-131-0.md%0ACard%20ID%3A%20codex-cli-2026-05-18-7794df%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.131.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->