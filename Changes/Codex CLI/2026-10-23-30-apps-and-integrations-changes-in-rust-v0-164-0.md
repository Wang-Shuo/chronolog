---
card_id: codex-cli-2026-10-23-b57220
date: '2026-10-23'
description: 'Codex CLI · 2026-10-23 · Apps and Integrations: 30 changes in 0.164.0
  — #53747 Prefer remote Visualize installs over the bundled plugin @philipp-oai'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1310
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 906d0aa18f5581cb5c68cfdc3f6b4aee2c4edff47d5771792b14f32efa5a5683
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-10-23-b57220
  comparison: ''
  date: '2026-10-23'
  description: 'Codex CLI — 0.164.0: 30 Apps and Integrations changes'
  evidence:
  - quote: '#53747 Prefer remote Visualize installs over the bundled plugin @philipp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#53763 Enrich V2 capability discovery with resolved plugin and skill metadata
      @TAFOYA-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#53795 Use the bundled model catalog in the MCP startup invalidation test
      @OLI-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#53990 Keep host MCP and plugin configuration local with remote environments
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54069 Fix Windows environment handling for remote MCP servers @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54094 Preserve specific MCP failure codes in metrics and spans @TAFOYA-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54096 Add Bazel targets for on-demand schemas and Python SDK generation
      @dkovalenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54424 Add remote plugin metadata to plugin configuration @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54619 Bind plugin hook approval to plugin contents @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54647 Make remote-control conflict retry tests deterministic @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54656 Honor MCP tool-list changes within a turn @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54679 Distinguish MCP approval cancellation reasons @vkg-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54686 Preserve MCP tool-list metadata in server status @victor-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54761 Upgrade `zip` to 9.0.0 and update plugin archive extraction @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55263 Start dormant MCP servers for hook calls @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55287 Track MCP enterprise auth cancellation across config reloads @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55301 Reconcile V2 executor plugins with cloud catalogs @TAFOYA-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55334 Enable enterprise-managed authorization for MCP connections @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55394 Use thread connections for enterprise MCP status listings @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55463 Add optional MCP disablement for prediction forks and samples @liame-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55691 Refine enterprise MCP auth errors and request authority checks
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55696 Preserve enterprise MCP authorization across runtime refreshes
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55710 Resolve MCP backend identity from runtime events in rollout traces
      @cassirer-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55724 Share prepared MCP tool definitions across sessions @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55859 Fix enterprise MCP credential selection and reauthentication @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55883 Expand enterprise MCP authorization lifecycle test coverage @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55946 Bound remote installed-plugin inventory pagination @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55957 Refresh cloud plugin and skill catalogs after mid-turn auth changes
      @TAFOYA-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55968 Back off failed cloud skill and plugin catalog refreshes @TAFOYA-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#56044 Enable executor cleanup hooks with V2 capability discovery @TAFOYA-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 30-apps-and-integrations-changes-in-rust-v0-164-0
  source_release: codex-cli-2026-10-23-rust-v0-164-0-github-421457270-d867151d
  source_type: github_releases
  theme: apps-integrations
  title: 30 Apps and Integrations changes in rust-v0.164.0
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-10-22-10-apps-and-integrations-changes-in-v2026-10-6|10
  Apps and Integrations changes in v2026.10.6]]'
- '[[Changes/OpenHands/2026-10-22-chore-bump-openhands-extensions-to-0-33-0-by-neubig-in-https-github-com-openhand|chore:
  bump @openhands/extensions to 0.33.0]]'
- '[[Changes/Claude Code/2026-10-23-2-apps-and-integrations-changes-in-v2-1-310|2
  Apps and Integrations changes in v2.1.310]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-10-23-rust-v0-164-0-github-421457270-d867151d|codex-cli-2026-10-23-rust-v0-164-0-github-421457270-d867151d]]'
source_type: github_releases
theme: apps-integrations
title: 30 Apps and Integrations changes in rust-v0.164.0
type: change
---

<!-- chronolog:begin region="header" -->
# 30 Apps and Integrations changes in rust-v0.164.0

**Codex CLI** · 2026-10-23 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.164.0) · from [[Releases/Codex CLI/codex-cli-2026-10-23-rust-v0-164-0-github-421457270-d867151d|0.164.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> #53747 Prefer remote Visualize installs over the bundled plugin @philipp-oai

> #53763 Enrich V2 capability discovery with resolved plugin and skill metadata @TAFOYA-OAI

> #53795 Use the bundled model catalog in the MCP startup invalidation test @OLI-OAI

> #53990 Keep host MCP and plugin configuration local with remote environments @jif-oai

> #54069 Fix Windows environment handling for remote MCP servers @iceweasel-oai

> #54094 Preserve specific MCP failure codes in metrics and spans @TAFOYA-OAI

> #54096 Add Bazel targets for on-demand schemas and Python SDK generation @dkovalenko-oai

> #54424 Add remote plugin metadata to plugin configuration @mzeng-openai

> #54619 Bind plugin hook approval to plugin contents @jif-oai

> #54647 Make remote-control conflict retry tests deterministic @jif-oai

> #54656 Honor MCP tool-list changes within a turn @jif-oai

> #54679 Distinguish MCP approval cancellation reasons @vkg-oai

> #54686 Preserve MCP tool-list metadata in server status @victor-openai

> #54761 Upgrade `zip` to 9.0.0 and update plugin archive extraction @anp-oai

> #55263 Start dormant MCP servers for hook calls @charliemarsh-oai

> #55287 Track MCP enterprise auth cancellation across config reloads @jif-oai

> #55301 Reconcile V2 executor plugins with cloud catalogs @TAFOYA-OAI

> #55334 Enable enterprise-managed authorization for MCP connections @jif-oai

> #55394 Use thread connections for enterprise MCP status listings @jif-oai

> #55463 Add optional MCP disablement for prediction forks and samples @liame-oai

> #55691 Refine enterprise MCP auth errors and request authority checks @jif-oai

> #55696 Preserve enterprise MCP authorization across runtime refreshes @jif-oai

> #55710 Resolve MCP backend identity from runtime events in rollout traces @cassirer-openai

> #55724 Share prepared MCP tool definitions across sessions @charliemarsh-oai

> #55859 Fix enterprise MCP credential selection and reauthentication @jif-oai

> #55883 Expand enterprise MCP authorization lifecycle test coverage @jif-oai

> #55946 Bound remote installed-plugin inventory pagination @mzeng-openai

> #55957 Refresh cloud plugin and skill catalogs after mid-turn auth changes @TAFOYA-OAI

> #55968 Back off failed cloud skill and plugin catalog refreshes @TAFOYA-OAI

> #56044 Enable executor cleanup hooks with V2 capability discovery @TAFOYA-OAI

Source: https://github.com/openai/codex/releases/tag/rust-v0.164.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-10-23-24-account-and-access-changes-in-rust-v0-164-0|24 Account and Access changes in rust-v0.164.0]] · Account and Access
- [[Changes/Codex CLI/2026-10-23-2-reliability-and-performance-changes-in-rust-v0-164-0|2 Reliability and Performance changes in rust-v0.164.0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-10-23-8-collaboration-changes-in-rust-v0-164-0|8 Collaboration changes in rust-v0.164.0]] · Collaboration
- [[Changes/Codex CLI/2026-10-23-4-memory-and-personalization-changes-in-rust-v0-164-0|4 Memory and Personalization changes in rust-v0.164.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-10-23-15-safety-and-privacy-changes-in-rust-v0-164-0|15 Safety and Privacy changes in rust-v0.164.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-10-23-13-agent-mode-changes-in-rust-v0-164-0|13 Agent Mode changes in rust-v0.164.0]] · Agent Mode
- [[Changes/Codex CLI/2026-10-23-2-image-generation-changes-in-rust-v0-164-0|2 Image Generation changes in rust-v0.164.0]] · Image Generation
- [[Changes/Codex CLI/2026-10-23-8-mobile-and-desktop-changes-in-rust-v0-164-0|8 Mobile and Desktop changes in rust-v0.164.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-10-23-18-context-window-changes-in-rust-v0-164-0|18 Context Window changes in rust-v0.164.0]] · Context Window
- [[Changes/Codex CLI/2026-10-23-the-amazon-bedrock-setup-wizard-is-now-enabled-by-default-with-api-key-entry-gro|The Amazon Bedrock setup wizard is now enabled by default, with API key entry…]] · Account and Access
- [[Changes/Codex CLI/2026-10-23-9-interface-experience-changes-in-rust-v0-164-0|9 Interface Experience changes in rust-v0.164.0]] · Interface Experience
- [[Changes/Codex CLI/2026-10-23-9-model-support-changes-in-rust-v0-164-0|9 Model Support changes in rust-v0.164.0]] · Model Support
- [[Changes/Codex CLI/2026-10-23-14-developer-workflow-changes-in-rust-v0-164-0|14 Developer Workflow changes in rust-v0.164.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-10-23-3-voice-and-audio-changes-in-rust-v0-164-0|3 Voice and Audio changes in rust-v0.164.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-10-23-183-other-changes-in-rust-v0-164-0|183 other changes in rust-v0.164.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-10-23 · Claude Code · [[Changes/Claude Code/2026-10-23-2-apps-and-integrations-changes-in-v2-1-310|2 Apps and Integrations changes in v2.1.310]]
- Later: 2026-10-23 · Dify · [[Changes/Dify/2026-10-23-14-apps-and-integrations-changes-in-1-18-0|14 Apps and Integrations changes in 1.18.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-10-23-b57220&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-10-23-30-apps-and-integrations-changes-in-rust-v0-164-0.md%0ACard%20ID%3A%20codex-cli-2026-10-23-b57220%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.164.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->