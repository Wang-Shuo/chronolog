---
card_id: codex-cli-2026-06-04-548620
date: '2026-06-04'
description: 'Codex CLI · 2026-06-04 · Apps and Integrations: 19 changes in 0.137.0
  — Remote-control clients can start pairing and list or revoke controller grants
  through…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2729
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 0fde00db184f669a7231839ee7fd2e032e6fe27d44f1efaa8deb8f67813480b2
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-06-04-548620
  comparison: ''
  date: '2026-06-04'
  description: 'Codex CLI — 0.137.0: 19 Apps and Integrations changes'
  evidence:
  - quote: 'Remote-control clients can start pairing and list or revoke controller
      grants through app-server v2 RPCs (#25675, #25785).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: 'Plugin workflows gained machine-readable `codex plugin list --json` output
      and cached remote catalog suggestions (#25330, #25457).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: 'Plugin loading preserves app manifest order, deduplicates local/remote
      curated installs, and treats malformed `skills` fields as warnings (#25491,
      #25681, #25717, #25782).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: 'Python SDK releases now publish runtime wheels from the SDK workflow and
      pin to a glibc-compatible runtime package (#25906, #25907).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25491 Preserve plugin app manifest order @charlesgong-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25681 fix: Deduplicate installed local and remote curated plugins @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25705 Fix stale TestAppServer rename in plugin_list test @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25717 Handle invalid plugin skills manifest field @xli-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25675 feat(remote-control): add pairing start @apanasenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25330 [codex] Add plugin list JSON output @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25457 [codex] Cache remote plugin catalog for suggestions @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25783 [codex] Move plugin discoverable logic into core-plugins @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25782 [codex] Validate plugin skill base names @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25857 flake: Keep plugin test homes alive @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25167 [app-server][core] Add connector-level Guardian reviewer overrides
      @zamoshchin-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25907 [codex] Pin Python SDK to glibc-compatible runtime @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25867 Add remote request permissions integration coverage @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25906 [codex] Publish Python runtime wheels with Python SDK releases
      @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25785 feat(app-server): add remote control client management RPCs @apanasenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 19-apps-and-integrations-changes-in-rust-v0-137-0
  source_release: codex-cli-2026-06-04-rust-v0-137-0-github-334076532-fadfeece
  source_type: github_releases
  theme: apps-integrations
  title: 19 Apps and Integrations changes in rust-v0.137.0
  type: change
related_changes:
- '[[Changes/Lovable/2026-06-03-lovable-mcp-server-now-available-on-all-plans|Lovable
  MCP server now available on all plans]]'
- '[[Changes/Claude Code/2026-06-04-2-apps-and-integrations-changes-in-v2-1-163|2
  Apps and Integrations changes in v2.1.163]]'
- '[[Changes/Claude Code/2026-06-04-added-plugin-list-command-to-list-installed-plugins-with-enabled-disabled-filter|Added
  /plugin list command to list installed plugins…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-06-04-rust-v0-137-0-github-334076532-fadfeece|codex-cli-2026-06-04-rust-v0-137-0-github-334076532-fadfeece]]'
source_type: github_releases
theme: apps-integrations
title: 19 Apps and Integrations changes in rust-v0.137.0
type: change
---

<!-- chronolog:begin region="header" -->
# 19 Apps and Integrations changes in rust-v0.137.0

**Codex CLI** · 2026-06-04 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.137.0) · from [[Releases/Codex CLI/codex-cli-2026-06-04-rust-v0-137-0-github-334076532-fadfeece|0.137.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Remote-control clients can start pairing and list or revoke controller grants through app-server v2 RPCs (#25675, #25785).

> Plugin workflows gained machine-readable `codex plugin list --json` output and cached remote catalog suggestions (#25330, #25457).

> Plugin loading preserves app manifest order, deduplicates local/remote curated installs, and treats malformed `skills` fields as warnings (#25491, #25681, #25717, #25782).

> Python SDK releases now publish runtime wheels from the SDK workflow and pin to a glibc-compatible runtime package (#25906, #25907).

> #25491 Preserve plugin app manifest order @charlesgong-openai

> #25681 fix: Deduplicate installed local and remote curated plugins @xl-openai

> #25705 Fix stale TestAppServer rename in plugin_list test @bolinfest

> #25717 Handle invalid plugin skills manifest field @xli-oai

> #25675 feat(remote-control): add pairing start @apanasenko-oai

> #25330 [codex] Add plugin list JSON output @xl-openai

> #25457 [codex] Cache remote plugin catalog for suggestions @xl-openai

> #25783 [codex] Move plugin discoverable logic into core-plugins @xl-openai

> #25782 [codex] Validate plugin skill base names @xl-openai

> #25857 flake: Keep plugin test homes alive @jif-oai

> #25167 [app-server][core] Add connector-level Guardian reviewer overrides @zamoshchin-openai

> #25907 [codex] Pin Python SDK to glibc-compatible runtime @aibrahim-oai

> #25867 Add remote request permissions integration coverage @jif-oai

> #25906 [codex] Publish Python runtime wheels with Python SDK releases @aibrahim-oai

> #25785 feat(app-server): add remote control client management RPCs @apanasenko-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.137.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-06-04-6-developer-workflow-changes-in-rust-v0-137-0|6 Developer Workflow changes in rust-v0.137.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-06-04-25702-codex-enable-parallel-standalone-web-search-calls-sayan-oai|♯25702 codex enable parallel standalone web search calls @sayan-oai]] · Search and Browsing
- [[Changes/Codex CLI/2026-06-04-3-image-generation-changes-in-rust-v0-137-0|3 Image Generation changes in rust-v0.137.0]] · Image Generation
- [[Changes/Codex CLI/2026-06-04-2-interface-experience-changes-in-rust-v0-137-0|2 Interface Experience changes in rust-v0.137.0]] · Interface Experience
- [[Changes/Codex CLI/2026-06-04-2-enterprise-and-administration-changes-in-rust-v0-137-0|2 Enterprise and Administration changes in rust-v0.137.0]] · Enterprise and Administration
- [[Changes/Codex CLI/2026-06-04-local-session-history-is-safer-for-compressed-rollouts-renamed-titles-pathless-s|Local session history is safer for compressed rollouts, renamed titles, pathless…]] · Projects and Workspaces
- [[Changes/Codex CLI/2026-06-04-4-collaboration-changes-in-rust-v0-137-0|4 Collaboration changes in rust-v0.137.0]] · Collaboration
- [[Changes/Codex CLI/2026-06-04-3-context-window-changes-in-rust-v0-137-0|3 Context Window changes in rust-v0.137.0]] · Context Window
- [[Changes/Codex CLI/2026-06-04-2-mobile-and-desktop-changes-in-rust-v0-137-0|2 Mobile and Desktop changes in rust-v0.137.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-06-04-12-agent-mode-changes-in-rust-v0-137-0|12 Agent Mode changes in rust-v0.137.0]] · Agent Mode
- [[Changes/Codex CLI/2026-06-04-25682-codex-document-out-of-line-test-module-convention-anp-oai|♯25682 codex document out-of-line test module convention @anp-oai]] · Files and Data
- [[Changes/Codex CLI/2026-06-04-3-model-support-changes-in-rust-v0-137-0|3 Model Support changes in rust-v0.137.0]] · Model Support
- [[Changes/Codex CLI/2026-06-04-8-safety-and-privacy-changes-in-rust-v0-137-0|8 Safety and Privacy changes in rust-v0.137.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-06-04-69-other-changes-in-rust-v0-137-0|69 other changes in rust-v0.137.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-06-04 · Claude Code · [[Changes/Claude Code/2026-06-04-added-plugin-list-command-to-list-installed-plugins-with-enabled-disabled-filter|Added /plugin list command to list installed plugins…]]
- Later: 2026-06-04 · Cursor · [[Changes/Cursor/2026-06-04-we-ve-shipped-a-batch-of-new-functionality-across-the-typescript-and-python-sdks|We've shipped a batch of new functionality across the TypeScript and Python SDKs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-06-04-548620&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-06-04-19-apps-and-integrations-changes-in-rust-v0-137-0.md%0ACard%20ID%3A%20codex-cli-2026-06-04-548620%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.137.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->