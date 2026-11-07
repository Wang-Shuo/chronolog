---
card_id: dify-2026-04-29-5e78bf
date: '2026-04-29'
description: 'Dify · 2026-04-29 · Apps and Integrations: 48 changes in v1.14.0 — **MCP
  tool metadata** — refresh after updates so the UI stays in sync.'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2693
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8455746aead843a1c43549d5aa2fd1b05eab16c904ebee810d51e1de968b2adb
product: dify
product_name: Dify
record:
  card_id: dify-2026-04-29-5e78bf
  comparison: ''
  date: '2026-04-29'
  description: 'Dify — v1.14.0: 48 Apps and Integrations changes'
  evidence:
  - quote: '**MCP tool metadata** — refresh after updates so the UI stays in sync.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: '**MCP schema publishing** — map `checkbox` and `json_object` types correctly.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: '**Plugins** — auto-upgrade strategy persistence, local installer and file-input
      behavior, tenant scoping for inner API end-user lookup.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: '**Quota v3** integration in the product stack.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'test: migrate plugin parameter service tests to testcontainers by @YB0y
      in https://github.com/langgenius/dify/pull/34090'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'test: migrate plugin service tests to testcontainers by @YB0y in https://github.com/langgenius/dify/pull/34098'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'test: migrate auth integration tests to testcontainers by @YB0y in https://github.com/langgenius/dify/pull/34089'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'feat: return correct dify-plugin-daemon error message by @fatelei in https://github.com/langgenius/dify/pull/34171'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor: core/tools, agent, callback_handler, encrypter, llm_generator,
      plugin, inner_api by @RenzoMXD in https://github.com/langgenius/dify/pull/34205'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'chore(ci): split API unit and integration coverage reporting by @laipz8200
      in https://github.com/langgenius/dify/pull/34211'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'test: migrate mcp controller tests to testcontainers by @YB0y in https://github.com/langgenius/dify/pull/34297'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'test: add tests for api/services retention, enterprise, plugin by @cryptus-neoxys
      in https://github.com/langgenius/dify/pull/32648'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor(nodejs-sdk): replace axios with fetch transport by @lyzno1 in
      https://github.com/langgenius/dify/pull/34325'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor: use sessionmaker().begin() in web and mcp controllers by @Desel72
      in https://github.com/langgenius/dify/pull/34281'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'chore: update code-inspector-plugin to 1.5.1 by @hyoban in https://github.com/langgenius/dify/pull/34506'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor(api): type MCP tool schema and arguments with TypedDict by @YB0y
      in https://github.com/langgenius/dify/pull/34612'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor(api): type plugin migration results with TypedDict by @statxc
      in https://github.com/langgenius/dify/pull/34627'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor(api): type Tenant custom config with TypedDict and tighten MCP
      headers type by @YB0y in https://github.com/langgenius/dify/pull/34670'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor(api): use sessionmaker in plugin & trigger services by @carlos4s
      in https://github.com/langgenius/dify/pull/34764'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor: convert appmode plugin if/elif to match/case (#30001) by @dataCenter430
      in https://github.com/langgenius/dify/pull/34790'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor: migrate session.query to select API in plugin services by @aliworksx08
      in https://github.com/langgenius/dify/pull/34817'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor(mcp): remove unused AnyFunction alias, tighten callback type
      by @corevibe555 in https://github.com/langgenius/dify/pull/34890'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'test: update TestContainers integration tests and unit test fixtures to
      SQLAlchemy 2.0 select() API by @wdeveloper16 in https://github.com/langgenius/dify/pull/34969'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor(api): migrate tools, account, workflow and plugin services to
      SQLAlchemy 2.0 by @wdeveloper16 in https://github.com/langgenius/dify/pull/34966'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'test: migrate conftest and plugin lifecycle tests to SQLAlchemy 2.0 select()
      API by @dataCenter430 in https://github.com/langgenius/dify/pull/34979'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'test: migrate conversation rename/delete edge cases to Testcontainers
      integration tests by @wdeveloper16 in https://github.com/langgenius/dify/pull/34991'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'test: implement Account/Tenant model integration tests to replace db-mocked
      unit tests by @wdeveloper16 in https://github.com/langgenius/dify/pull/34994'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor: migrate mcp_server from marshal_with/api.model to Pydantic BaseModel
      by @ai-hpc in https://github.com/langgenius/dify/pull/34935'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'test: migrate AudioService TTS message-ID lookup tests to Testcontainers
      integration tests by @wdeveloper16 in https://github.com/langgenius/dify/pull/34992'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor: replace bare dict with dict[str, Any] in plugin endpoint_service
      by @wdeveloper16 in https://github.com/langgenius/dify/pull/35065'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor: replace bare dict with dict[str, Any] in provider entities and
      plugin client by @wdeveloper16 in https://github.com/langgenius/dify/pull/35077'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'test: migrate trigger integration tests to SQLAlchemy 2.0 select API by
      @bohdansolovie in https://github.com/langgenius/dify/pull/35081'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'test: migrate remove_app_and_related_data integration tests to SQLAlchemy
      2.0 APIs by @bohdansolovie in https://github.com/langgenius/dify/pull/35092'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'test: migrate mail and segment indexing integration tests to SQLAlchemy
      2.0 APIs by @bohdansolovie in https://github.com/langgenius/dify/pull/35091'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor: replace bare dict with typed annotations in core plugin module
      by @dataCenter430 in https://github.com/langgenius/dify/pull/35096'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'test: migrate clean_dataset integration tests to SQLAlchemy 2.0 APIs by
      @bohdansolovie in https://github.com/langgenius/dify/pull/35146'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'test: migrate task integration tests to SQLAlchemy 2.0 query APIs by @bohdansolovie
      in https://github.com/langgenius/dify/pull/35170'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'test: migrate clean_notion_document integration tests to SQLAlchemy 2…
      by @bohdansolovie in https://github.com/langgenius/dify/pull/35147'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'test: remove legacy python3 code executor integration test by @jamesrayammons
      in https://github.com/langgenius/dify/pull/35223'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'test: remove legacy code executor integration test by @jamesrayammons
      in https://github.com/langgenius/dify/pull/35224'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'test: remove legacy storage key loader integration test by @jamesrayammons
      in https://github.com/langgenius/dify/pull/35225'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'test: remove legacy jinja2 code executor integration test by @jamesrayammons
      in https://github.com/langgenius/dify/pull/35222'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'test: migrate duplicate and vector index task integration tests to SQLAlchemy
      2.0 APIs by @bohdansolovie in https://github.com/langgenius/dify/pull/35292'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor(api): migrate console mcp-server responses to BaseModel by @ai-hpc
      in https://github.com/langgenius/dify/pull/35219'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'feat: copy nodes cross apps by @hjlarry in https://github.com/langgenius/dify/pull/33273'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'chore: resolve oxlint warnings across web and SDK by @agenthaulk in https://github.com/langgenius/dify/pull/34540'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor: quota v3 integration by @hj24 in https://github.com/langgenius/dify/pull/35436'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor: improve scrollbar handling in plugin and model selector UI by
      @lyzno1 in https://github.com/langgenius/dify/pull/35630'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 48-apps-and-integrations-changes-in-1-14-0
  source_release: dify-2026-04-29-1-14-0-github-314986233-63073e86
  source_type: github_releases
  theme: apps-integrations
  title: 48 Apps and Integrations changes in 1.14.0
  type: change
related_changes:
- '[[Changes/OpenCode/2026-04-28-desktop-sync-state-loading-is-more-reliable-for-mcp-lsp-and-workspace-refreshes|Desktop
  Sync state loading is more reliable for MCP, LSP, and workspace refreshes]]'
- '[[Changes/Cursor/2026-04-29-we-re-introducing-the-cursor-sdk-so-you-can-build-agents-with-the-same-runtime-h|Cursor
  introduces the Cursor SDK so you can build agents with the same runtime…]]'
- '[[Changes/Cursor/2026-04-29-run-npm-install-cursor-sdk-to-get-started-you-can-also-use-cursor-s-native-sdk-s-76fb76|Run
  npm install @cursor/sdk to get started]]'
source_release: '[[Releases/Dify/dify-2026-04-29-1-14-0-github-314986233-63073e86|dify-2026-04-29-1-14-0-github-314986233-63073e86]]'
source_type: github_releases
theme: apps-integrations
title: 48 Apps and Integrations changes in 1.14.0
type: change
---

<!-- chronolog:begin region="header" -->
# 48 Apps and Integrations changes in 1.14.0

**Dify** · 2026-04-29 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.14.0) · from [[Releases/Dify/dify-2026-04-29-1-14-0-github-314986233-63073e86|v1.14.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **MCP tool metadata** — refresh after updates so the UI stays in sync.

> **MCP schema publishing** — map `checkbox` and `json_object` types correctly.

> **Plugins** — auto-upgrade strategy persistence, local installer and file-input behavior, tenant scoping for inner API end-user lookup.

> **Quota v3** integration in the product stack.

> test: migrate plugin parameter service tests to testcontainers by @YB0y in https://github.com/langgenius/dify/pull/34090

> test: migrate plugin service tests to testcontainers by @YB0y in https://github.com/langgenius/dify/pull/34098

> test: migrate auth integration tests to testcontainers by @YB0y in https://github.com/langgenius/dify/pull/34089

> feat: return correct dify-plugin-daemon error message by @fatelei in https://github.com/langgenius/dify/pull/34171

> refactor: core/tools, agent, callback_handler, encrypter, llm_generator, plugin, inner_api by @RenzoMXD in https://github.com/langgenius/dify/pull/34205

> chore(ci): split API unit and integration coverage reporting by @laipz8200 in https://github.com/langgenius/dify/pull/34211

> test: migrate mcp controller tests to testcontainers by @YB0y in https://github.com/langgenius/dify/pull/34297

> test: add tests for api/services retention, enterprise, plugin by @cryptus-neoxys in https://github.com/langgenius/dify/pull/32648

> refactor(nodejs-sdk): replace axios with fetch transport by @lyzno1 in https://github.com/langgenius/dify/pull/34325

> refactor: use sessionmaker().begin() in web and mcp controllers by @Desel72 in https://github.com/langgenius/dify/pull/34281

> chore: update code-inspector-plugin to 1.5.1 by @hyoban in https://github.com/langgenius/dify/pull/34506

> refactor(api): type MCP tool schema and arguments with TypedDict by @YB0y in https://github.com/langgenius/dify/pull/34612

> refactor(api): type plugin migration results with TypedDict by @statxc in https://github.com/langgenius/dify/pull/34627

> refactor(api): type Tenant custom config with TypedDict and tighten MCP headers type by @YB0y in https://github.com/langgenius/dify/pull/34670

> refactor(api): use sessionmaker in plugin & trigger services by @carlos4s in https://github.com/langgenius/dify/pull/34764

> refactor: convert appmode plugin if/elif to match/case (#30001) by @dataCenter430 in https://github.com/langgenius/dify/pull/34790

> refactor: migrate session.query to select API in plugin services by @aliworksx08 in https://github.com/langgenius/dify/pull/34817

> refactor(mcp): remove unused AnyFunction alias, tighten callback type by @corevibe555 in https://github.com/langgenius/dify/pull/34890

> test: update TestContainers integration tests and unit test fixtures to SQLAlchemy 2.0 select() API by @wdeveloper16 in https://github.com/langgenius/dify/pull/34969

> refactor(api): migrate tools, account, workflow and plugin services to SQLAlchemy 2.0 by @wdeveloper16 in https://github.com/langgenius/dify/pull/34966

> test: migrate conftest and plugin lifecycle tests to SQLAlchemy 2.0 select() API by @dataCenter430 in https://github.com/langgenius/dify/pull/34979

> test: migrate conversation rename/delete edge cases to Testcontainers integration tests by @wdeveloper16 in https://github.com/langgenius/dify/pull/34991

> test: implement Account/Tenant model integration tests to replace db-mocked unit tests by @wdeveloper16 in https://github.com/langgenius/dify/pull/34994

> refactor: migrate mcp_server from marshal_with/api.model to Pydantic BaseModel by @ai-hpc in https://github.com/langgenius/dify/pull/34935

> test: migrate AudioService TTS message-ID lookup tests to Testcontainers integration tests by @wdeveloper16 in https://github.com/langgenius/dify/pull/34992

> refactor: replace bare dict with dict[str, Any] in plugin endpoint_service by @wdeveloper16 in https://github.com/langgenius/dify/pull/35065

> refactor: replace bare dict with dict[str, Any] in provider entities and plugin client by @wdeveloper16 in https://github.com/langgenius/dify/pull/35077

> test: migrate trigger integration tests to SQLAlchemy 2.0 select API by @bohdansolovie in https://github.com/langgenius/dify/pull/35081

> test: migrate remove_app_and_related_data integration tests to SQLAlchemy 2.0 APIs by @bohdansolovie in https://github.com/langgenius/dify/pull/35092

> test: migrate mail and segment indexing integration tests to SQLAlchemy 2.0 APIs by @bohdansolovie in https://github.com/langgenius/dify/pull/35091

> refactor: replace bare dict with typed annotations in core plugin module by @dataCenter430 in https://github.com/langgenius/dify/pull/35096

> test: migrate clean_dataset integration tests to SQLAlchemy 2.0 APIs by @bohdansolovie in https://github.com/langgenius/dify/pull/35146

> test: migrate task integration tests to SQLAlchemy 2.0 query APIs by @bohdansolovie in https://github.com/langgenius/dify/pull/35170

> test: migrate clean_notion_document integration tests to SQLAlchemy 2… by @bohdansolovie in https://github.com/langgenius/dify/pull/35147

> test: remove legacy python3 code executor integration test by @jamesrayammons in https://github.com/langgenius/dify/pull/35223

> test: remove legacy code executor integration test by @jamesrayammons in https://github.com/langgenius/dify/pull/35224

> test: remove legacy storage key loader integration test by @jamesrayammons in https://github.com/langgenius/dify/pull/35225

> test: remove legacy jinja2 code executor integration test by @jamesrayammons in https://github.com/langgenius/dify/pull/35222

> test: migrate duplicate and vector index task integration tests to SQLAlchemy 2.0 APIs by @bohdansolovie in https://github.com/langgenius/dify/pull/35292

> refactor(api): migrate console mcp-server responses to BaseModel by @ai-hpc in https://github.com/langgenius/dify/pull/35219

> feat: copy nodes cross apps by @hjlarry in https://github.com/langgenius/dify/pull/33273

> chore: resolve oxlint warnings across web and SDK by @agenthaulk in https://github.com/langgenius/dify/pull/34540

> refactor: quota v3 integration by @hj24 in https://github.com/langgenius/dify/pull/35436

> refactor: improve scrollbar handling in plugin and model selector UI by @lyzno1 in https://github.com/langgenius/dify/pull/35630

Source: https://github.com/langgenius/dify/releases/tag/1.14.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-04-29-13-files-and-data-changes-in-1-14-0|13 Files and Data changes in 1.14.0]] · Files and Data
- [[Changes/Dify/2026-04-29-2-developer-workflow-changes-in-1-14-0|2 Developer Workflow changes in 1.14.0]] · Developer Workflow
- [[Changes/Dify/2026-04-29-10-interface-experience-changes-in-1-14-0|10 Interface Experience changes in 1.14.0]] · Interface Experience
- [[Changes/Dify/2026-04-29-27-model-support-changes-in-1-14-0|27 Model Support changes in 1.14.0]] · Model Support
- [[Changes/Dify/2026-04-29-2-accessibility-and-localization-changes-in-1-14-0|2 Accessibility and Localization changes in 1.14.0]] · Accessibility and Localization
- [[Changes/Dify/2026-04-29-6-editor-experience-changes-in-1-14-0|6 Editor Experience changes in 1.14.0]] · Editor Experience
- [[Changes/Dify/2026-04-29-7-pricing-model-changes-in-1-14-0|7 Pricing Model changes in 1.14.0]] · Pricing Model
- [[Changes/Dify/2026-04-29-13-collaboration-changes-in-1-14-0|13 Collaboration changes in 1.14.0]] · Collaboration
- [[Changes/Dify/2026-04-29-7-safety-and-privacy-changes-in-1-14-0|7 Safety and Privacy changes in 1.14.0]] · Safety and Privacy
- [[Changes/Dify/2026-04-29-8-account-and-access-changes-in-1-14-0|8 Account and Access changes in 1.14.0]] · Account and Access
- [[Changes/Dify/2026-04-29-2-agent-mode-changes-in-1-14-0|2 Agent Mode changes in 1.14.0]] · Agent Mode
- [[Changes/Dify/2026-04-29-3-automation-and-scheduling-changes-in-1-14-0|3 Automation and Scheduling changes in 1.14.0]] · Automation and Scheduling
- [[Changes/Dify/2026-04-29-2-enterprise-and-administration-changes-in-1-14-0|2 Enterprise and Administration changes in 1.14.0]] · Enterprise and Administration
- [[Changes/Dify/2026-04-29-3-context-window-changes-in-1-14-0|3 Context Window changes in 1.14.0]] · Context Window
- [[Changes/Dify/2026-04-29-3-reliability-and-performance-changes-in-1-14-0|3 Reliability and Performance changes in 1.14.0]] · Reliability and Performance
- [[Changes/Dify/2026-04-29-520-other-changes-in-1-14-0|520 other changes in 1.14.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-04-29 · Cursor · [[Changes/Cursor/2026-04-29-run-npm-install-cursor-sdk-to-get-started-you-can-also-use-cursor-s-native-sdk-s-76fb76|Run npm install @cursor/sdk to get started]]
- Later: 2026-04-30 · Codex CLI · [[Changes/Codex CLI/2026-04-30-37-apps-and-integrations-changes-in-rust-v0-128-0|37 Apps and Integrations changes in rust-v0.128.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-04-29-5e78bf&body=Card%3A%20Changes%2FDify%2F2026-04-29-48-apps-and-integrations-changes-in-1-14-0.md%0ACard%20ID%3A%20dify-2026-04-29-5e78bf%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.14.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->